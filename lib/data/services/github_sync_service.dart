import 'dart:async';
import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/app_constants.dart';
import '../../core/utils/institutional_validator.dart';
import '../models/student_user_model.dart';

/// Estado de sincronización con `jesusants/UM-Studio`.
enum GitHubSyncStatus {
  idle,
  syncing,
  synced,
  localOnly,
  error,
}

/// Resultado de lectura de `db/users/{username}.json` en GitHub.
class RemoteUserFetchResult {
  const RemoteUserFetchResult({
    this.user,
    this.sha,
    required this.statusCode,
    this.errorMessage,
  });

  final StudentUserModel? user;
  final String? sha;
  final int statusCode;
  final String? errorMessage;

  bool get exists => statusCode == 200 && user != null;
  bool get notFound => statusCode == 404;
}

/// Servicio Serverless ultraligero conectado a `jesusants/UM-Studio`.
///
/// Gestiona autenticación simple por compañero en `db/users/{username}.json`,
/// persistencia inmediata (0 ms) en `SharedPreferences` y sincronización
/// silenciosa mediante `GET` / `PUT` contra la API Contents de GitHub.
class GitHubSyncService extends ChangeNotifier {
  GitHubSyncService({http.Client? httpClient})
      : _http = httpClient ?? http.Client();

  static const String _activeUserPrefsKey = 'um_studio_active_student_json_v2';
  static const String _activeShaPrefsKey = 'um_studio_active_student_sha_v2';
  static const String _pendingSyncPrefsKey = 'um_studio_pending_gh_sync_v2';
  static const String _localRegistryPrefsKey = 'um_studio_local_users_cache_v2';
  static const String _customTokenPrefsKey = 'um_studio_gh_token_override_v2';

  final http.Client _http;

  String _customToken = '';
  String? _knownSha;
  bool _pendingSync = false;
  bool _isPushing = false;
  StudentUserModel? _queuedPushUser;
  Timer? _debounceTimer;
  GitHubSyncStatus _status = GitHubSyncStatus.idle;
  String? _lastSyncMessage;

  GitHubSyncStatus get status => _status;
  String? get lastSyncMessage => _lastSyncMessage;
  bool get hasWriteToken => effectiveToken.isNotEmpty;

  String get effectiveToken {
    final override = _customToken.trim();
    if (override.isNotEmpty) return override;
    return AppConstants.envGithubToken.trim();
  }

  /// Carga configuración inicial y sesión recordada desde `SharedPreferences`.
  Future<StudentUserModel?> loadPersistedSession() async {
    final prefs = await SharedPreferences.getInstance();
    _customToken = prefs.getString(_customTokenPrefsKey) ?? '';
    _knownSha = prefs.getString(_activeShaPrefsKey);
    _pendingSync = prefs.getBool(_pendingSyncPrefsKey) ?? false;

    final rawJson = prefs.getString(_activeUserPrefsKey);
    if (rawJson == null || rawJson.isEmpty) {
      return null;
    }

    try {
      final map = jsonDecode(rawJson) as Map<String, dynamic>;
      final user = StudentUserModel.fromJson(map);
      _status = hasWriteToken
          ? (_pendingSync ? GitHubSyncStatus.syncing : GitHubSyncStatus.synced)
          : GitHubSyncStatus.localOnly;
      return user;
    } catch (_) {
      return null;
    }
  }

  /// Permite configurar o actualizar un Personal Access Token de GitHub en local.
  Future<void> setCustomGitHubToken(String token) async {
    _customToken = token.trim();
    final prefs = await SharedPreferences.getInstance();
    if (_customToken.isEmpty) {
      await prefs.remove(_customTokenPrefsKey);
    } else {
      await prefs.setString(_customTokenPrefsKey, _customToken);
    }
    _status =
        hasWriteToken ? GitHubSyncStatus.idle : GitHubSyncStatus.localOnly;
    notifyListeners();
  }

  Uri _userContentsUri(String username) => Uri.parse(
        '${AppConstants.githubApiBase}/db/users/$username.json?ref=${AppConstants.githubBranch}',
      );

  Uri _userPutUri(String username) => Uri.parse(
        '${AppConstants.githubApiBase}/db/users/$username.json',
      );

  Uri _userRawFallbackUri(String username) => Uri.parse(
        'https://raw.githubusercontent.com/${AppConstants.githubOwner}/${AppConstants.githubRepo}/${AppConstants.githubBranch}/db/users/$username.json',
      );

  Map<String, String> _buildHeaders({bool includeAuth = true}) {
    final headers = <String, String>{
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
    };
    final token = effectiveToken;
    if (includeAuth && token.isNotEmpty) {
      headers['Authorization'] = 'Bearer $token';
    }
    return headers;
  }

  /// Consulta `GET /repos/jesusants/UM-Studio/contents/db/users/{username}.json`.
  Future<RemoteUserFetchResult> fetchRemoteUser(String username) async {
    try {
      final res = await _http
          .get(_userContentsUri(username), headers: _buildHeaders())
          .timeout(const Duration(seconds: 8));

      if (res.statusCode == 200) {
        final body = jsonDecode(res.body) as Map<String, dynamic>;
        final sha = body['sha']?.toString();
        final rawB64 = (body['content'] ?? '').toString().replaceAll(
              RegExp(r'\s+'),
              '',
            );
        final decodedJson = utf8.decode(base64Decode(rawB64));
        final userMap = jsonDecode(decodedJson) as Map<String, dynamic>;
        return RemoteUserFetchResult(
          user: StudentUserModel.fromJson(userMap),
          sha: sha,
          statusCode: 200,
        );
      }

      if (res.statusCode == 404) {
        return const RemoteUserFetchResult(statusCode: 404);
      }

      // Si el API rate-limit sin token bloquea Contents API, intentamos raw público.
      if (res.statusCode == 403 || res.statusCode == 401) {
        final rawRes = await _http
            .get(_userRawFallbackUri(username))
            .timeout(const Duration(seconds: 6));
        if (rawRes.statusCode == 200) {
          final userMap = jsonDecode(rawRes.body) as Map<String, dynamic>;
          return RemoteUserFetchResult(
            user: StudentUserModel.fromJson(userMap),
            statusCode: 200,
          );
        } else if (rawRes.statusCode == 404) {
          return const RemoteUserFetchResult(statusCode: 404);
        }
      }

      return RemoteUserFetchResult(
        statusCode: res.statusCode,
        errorMessage: 'GitHub API respondió HTTP ${res.statusCode}.',
      );
    } catch (e) {
      return RemoteUserFetchResult(
        statusCode: 0,
        errorMessage: e.toString(),
      );
    }
  }

  /// Registra un nuevo estudiante de Ingeniería Energética creando
  /// `db/users/{username}.json` en GitHub (con respaldo local inmediato).
  Future<({StudentUserModel? user, String? error})> registerStudent({
    required String rawUserOrEmail,
    required String nombre,
    required String pin,
    int cuatrimestreActual = 2,
    List<String> starterSubjectCodes = const ['02021810', '03041819'],
  }) async {
    final parsed = InstitutionalValidator.parseInstitutionalUser(rawUserOrEmail);
    if (parsed.error != null || parsed.identity == null) {
      return (user: null, error: parsed.error);
    }
    final cleanName = nombre.trim();
    if (cleanName.length < 2) {
      return (user: null, error: 'Ingresa tu nombre completo.');
    }
    final cleanPin = pin.trim();
    if (cleanPin.length < 4) {
      return (
        user: null,
        error: 'Define un PIN o contraseña de al menos 4 caracteres.',
      );
    }

    final identity = parsed.identity!;
    final remote = await fetchRemoteUser(identity.username);

    if (remote.exists && remote.user != null) {
      // Si el usuario ya existía y colocó su mismo PIN, iniciamos sesión sin fricción.
      if (InstitutionalValidator.verifyPin(cleanPin, remote.user!.pinHash)) {
        _knownSha = remote.sha;
        await _persistLocalUser(remote.user!, sha: remote.sha, pending: false);
        _status = GitHubSyncStatus.synced;
        notifyListeners();
        return (user: remote.user, error: null);
      }
      return (
        user: null,
        error:
            'El usuario @${identity.username} ya existe. Inicia sesión con tu PIN.',
      );
    }

    // Revisar registro local offline para evitar sobrescribir otra cuenta local.
    final localExisting = await _loadFromLocalRegistry(identity.username);
    if (localExisting != null && remote.statusCode == 0) {
      if (InstitutionalValidator.verifyPin(cleanPin, localExisting.pinHash)) {
        await _persistLocalUser(localExisting, pending: true);
        return (user: localExisting, error: null);
      }
      return (
        user: null,
        error:
            'El usuario @${identity.username} ya está registrado en este dispositivo.',
      );
    }

    final newUser = StudentUserModel.createNew(
      username: identity.username,
      nombre: cleanName,
      email: identity.email,
      pinHash: InstitutionalValidator.hashPin(cleanPin),
      cuatrimestreActual: cuatrimestreActual,
      starterSubjectCodes: starterSubjectCodes,
    );

    // Guardado local instantáneo (0 ms) para sesión permanente.
    await _persistLocalUser(newUser, pending: true);

    if (hasWriteToken) {
      final pushed = await _putUserToGitHub(
        newUser,
        commitMessage:
            'feat(users): registrar estudiante ${newUser.username} (Ing. Energética)',
      );
      if (pushed) {
        _status = GitHubSyncStatus.synced;
      } else {
        _status = GitHubSyncStatus.localOnly;
      }
    } else {
      _status = GitHubSyncStatus.localOnly;
    }

    notifyListeners();
    return (user: newUser, error: null);
  }

  /// Inicia sesión descargando `db/users/{username}.json`, verificando el PIN
  /// y guardando toda la sesión en `SharedPreferences`.
  Future<({StudentUserModel? user, String? error})> loginStudent({
    required String rawUserOrEmail,
    required String pin,
  }) async {
    final parsed = InstitutionalValidator.parseInstitutionalUser(rawUserOrEmail);
    if (parsed.error != null || parsed.identity == null) {
      return (user: null, error: parsed.error);
    }
    final cleanPin = pin.trim();
    if (cleanPin.isEmpty) {
      return (user: null, error: 'Ingresa tu PIN o contraseña.');
    }

    final identity = parsed.identity!;
    final remote = await fetchRemoteUser(identity.username);

    if (remote.exists && remote.user != null) {
      if (!InstitutionalValidator.verifyPin(cleanPin, remote.user!.pinHash)) {
        return (user: null, error: 'PIN o contraseña incorrectos.');
      }
      _knownSha = remote.sha;
      await _persistLocalUser(remote.user!, sha: remote.sha, pending: false);
      _status =
          hasWriteToken ? GitHubSyncStatus.synced : GitHubSyncStatus.localOnly;
      notifyListeners();
      return (user: remote.user, error: null);
    }

    // Respaldo offline si el usuario ya había iniciado sesión en este dispositivo.
    final cachedLocal = await _loadFromLocalRegistry(identity.username);
    if (cachedLocal != null) {
      if (!InstitutionalValidator.verifyPin(cleanPin, cachedLocal.pinHash)) {
        return (user: null, error: 'PIN o contraseña incorrectos.');
      }
      await _persistLocalUser(cachedLocal, pending: _pendingSync);
      _status = GitHubSyncStatus.localOnly;
      notifyListeners();
      return (user: cachedLocal, error: null);
    }

    if (remote.notFound) {
      return (
        user: null,
        error:
            'No encontramos a @${identity.username}. Cambia a "Crear Cuenta" para registrarte en 1 paso.',
      );
    }

    return (
      user: null,
      error:
          'Sin conexión con GitHub (${remote.errorMessage ?? 'offline'}). Verifica tu red o regístrate.',
    );
  }

  /// Guardado Optimista (0 ms en `SharedPreferences`) + `PUT` silencioso
  /// en segundo plano hacia `db/users/{username}.json` en GitHub.
  Future<void> saveOptimisticAndSync(StudentUserModel updatedUser) async {
    await _persistLocalUser(updatedUser, sha: _knownSha, pending: true);

    if (!hasWriteToken) {
      _status = GitHubSyncStatus.localOnly;
      notifyListeners();
      return;
    }

    _status = GitHubSyncStatus.syncing;
    notifyListeners();

    _queuedPushUser = updatedUser;
    _debounceTimer?.cancel();
    _debounceTimer = Timer(AppConstants.githubSyncDebounce, _flushQueuedPush);
  }

  /// Fuerza la sincronización inmediata sin esperar el debounce.
  Future<bool> flushNow(StudentUserModel currentUser) async {
    _debounceTimer?.cancel();
    _queuedPushUser = currentUser;
    return _flushQueuedPush();
  }

  Future<bool> _flushQueuedPush() async {
    if (_isPushing) return false;
    final target = _queuedPushUser;
    if (target == null) return true;

    _isPushing = true;
    _queuedPushUser = null;
    try {
      final ok = await _putUserToGitHub(
        target,
        commitMessage: 'sync(users): actualizar estado de ${target.username}',
      );
      if (_queuedPushUser != null) {
        _isPushing = false;
        return await _flushQueuedPush();
      }
      _status = ok ? GitHubSyncStatus.synced : GitHubSyncStatus.error;
      notifyListeners();
      return ok;
    } finally {
      _isPushing = false;
    }
  }

  /// Sincroniza al abrir la app con conexión a internet:
  /// - Si había cambios locales pendientes (`_pendingSync`), los sube a GitHub.
  /// - Si no había pendientes, descarga la versión más reciente desde GitHub.
  Future<StudentUserModel?> syncOnStartup(StudentUserModel localUser) async {
    if (_pendingSync && hasWriteToken) {
      await _putUserToGitHub(
        localUser,
        commitMessage:
            'sync(users): sincronizar cambios offline de ${localUser.username}',
      );
      _status = GitHubSyncStatus.synced;
      notifyListeners();
      return localUser;
    }

    final remote = await fetchRemoteUser(localUser.username);
    if (remote.exists && remote.user != null) {
      _knownSha = remote.sha;
      await _persistLocalUser(remote.user!, sha: remote.sha, pending: false);
      _status =
          hasWriteToken ? GitHubSyncStatus.synced : GitHubSyncStatus.localOnly;
      notifyListeners();
      return remote.user;
    }
    return localUser;
  }

  Future<bool> _putUserToGitHub(
    StudentUserModel user, {
    required String commitMessage,
    bool isRetry = false,
  }) async {
    if (!hasWriteToken) return false;

    try {
      if (_knownSha == null) {
        final existing = await fetchRemoteUser(user.username);
        if (existing.exists) {
          _knownSha = existing.sha;
        }
      }

      final prettyJson = user.toPrettyJsonString();
      final contentB64 = base64Encode(utf8.encode(prettyJson));

      final payload = <String, dynamic>{
        'message': commitMessage,
        'content': contentB64,
        'branch': AppConstants.githubBranch,
        if (_knownSha != null && _knownSha!.isNotEmpty) 'sha': _knownSha,
      };

      final response = await _http
          .put(
            _userPutUri(user.username),
            headers: {
              ..._buildHeaders(),
              'Content-Type': 'application/json',
            },
            body: jsonEncode(payload),
          )
          .timeout(const Duration(seconds: 10));

      if (response.statusCode == 200 || response.statusCode == 201) {
        final decoded = jsonDecode(response.body) as Map<String, dynamic>;
        final contentMap = decoded['content'];
        if (contentMap is Map && contentMap['sha'] != null) {
          _knownSha = contentMap['sha'].toString();
        }
        await _persistLocalUser(user, sha: _knownSha, pending: false);
        _lastSyncMessage = 'Sincronizado con GitHub';
        return true;
      }

      // Conflicto de SHA (409 o 422): refrescar SHA actual y reintentar 1 vez.
      if (!isRetry &&
          (response.statusCode == 409 || response.statusCode == 422)) {
        final latest = await fetchRemoteUser(user.username);
        _knownSha = latest.sha;
        return await _putUserToGitHub(
          user,
          commitMessage: commitMessage,
          isRetry: true,
        );
      }

      _lastSyncMessage = 'HTTP ${response.statusCode} al sincronizar';
      return false;
    } catch (e) {
      _lastSyncMessage = 'Modo offline local';
      return false;
    }
  }

  Future<void> _persistLocalUser(
    StudentUserModel user, {
    String? sha,
    required bool pending,
  }) async {
    _pendingSync = pending;
    if (sha != null) _knownSha = sha;

    final prefs = await SharedPreferences.getInstance();
    final encoded = jsonEncode(user.toJson());
    await prefs.setString(_activeUserPrefsKey, encoded);
    await prefs.setBool(_pendingSyncPrefsKey, pending);
    if (_knownSha != null) {
      await prefs.setString(_activeShaPrefsKey, _knownSha!);
    }

    // Actualizar diccionario local multi-usuario para soporte offline.
    final rawReg = prefs.getString(_localRegistryPrefsKey);
    final registry = <String, dynamic>{};
    if (rawReg != null && rawReg.isNotEmpty) {
      try {
        registry.addAll(jsonDecode(rawReg) as Map<String, dynamic>);
      } catch (_) {}
    }
    registry[user.username] = user.toJson();
    await prefs.setString(_localRegistryPrefsKey, jsonEncode(registry));
  }

  Future<StudentUserModel?> _loadFromLocalRegistry(String username) async {
    final prefs = await SharedPreferences.getInstance();
    final rawReg = prefs.getString(_localRegistryPrefsKey);
    if (rawReg == null || rawReg.isEmpty) return null;
    try {
      final registry = jsonDecode(rawReg) as Map<String, dynamic>;
      final entry = registry[username];
      if (entry is Map) {
        return StudentUserModel.fromJson(
          entry.map((k, v) => MapEntry(k.toString(), v)),
        );
      }
    } catch (_) {}
    return null;
  }

  /// Cierra la sesión activa conservando los datos en GitHub y caché local.
  Future<void> clearActiveSession() async {
    _debounceTimer?.cancel();
    _knownSha = null;
    _pendingSync = false;
    _queuedPushUser = null;
    _status = GitHubSyncStatus.idle;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_activeUserPrefsKey);
    await prefs.remove(_activeShaPrefsKey);
    await prefs.remove(_pendingSyncPrefsKey);
    notifyListeners();
  }
}
