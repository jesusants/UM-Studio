import 'dart:async';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/app_constants.dart';
import '../models/global_env_config.dart';
import 'github_sync_service.dart';

/// Servicio centralizado de variables de entorno y configuración global en tiempo real.
///
/// Gestiona la lectura desde GitHub (`db/global_config.json`) con contingencia offline
/// en `SharedPreferences` y la publicación exclusiva por el administrador `jsierra`.
class GlobalEnvironmentService extends ChangeNotifier {
  GlobalEnvironmentService._internal();

  static final GlobalEnvironmentService instance =
      GlobalEnvironmentService._internal();

  static const String _prefsKey = 'um_global_env_config';
  static const String _shaPrefsKey = 'um_global_env_sha';

  static const String _rawUrl =
      'https://raw.githubusercontent.com/${AppConstants.githubOwner}/${AppConstants.githubRepo}/${AppConstants.githubBranch}/db/global_config.json';
  static const String _apiContentsUrl =
      'https://api.github.com/repos/${AppConstants.githubOwner}/${AppConstants.githubRepo}/contents/db/global_config.json';

  GlobalEnvConfig _config = const GlobalEnvConfig();
  String? _knownSha;
  bool _isLoading = false;
  bool _isPublishing = false;
  String? _lastError;
  Timer? _pollingTimer;
  bool _initialized = false;

  GlobalEnvConfig get config => _config;
  bool get isLoading => _isLoading;
  bool get isPublishing => _isPublishing;
  String? get lastError => _lastError;
  bool get isInitialized => _initialized;

  /// Inicializa el servicio cargando caché local de inmediato (0ms)
  /// y realizando la sincronización con GitHub en segundo plano.
  Future<void> initialize() async {
    if (_initialized) return;
    _initialized = true;

    // 1. Cargar desde SharedPreferences (Offline-First instantáneo)
    try {
      final prefs = await SharedPreferences.getInstance();
      _knownSha = prefs.getString(_shaPrefsKey);
      final cachedJson = prefs.getString(_prefsKey);
      if (cachedJson != null && cachedJson.isNotEmpty) {
        final decoded = jsonDecode(cachedJson) as Map<String, dynamic>;
        _config = GlobalEnvConfig.fromJson(decoded);
        notifyListeners();
      } else {
        // Cargar desde asset empaquetado inicial
        try {
          final assetData =
              await rootBundle.loadString('assets/data/global_config.json');
          final decoded = jsonDecode(assetData) as Map<String, dynamic>;
          _config = GlobalEnvConfig.fromJson(decoded);
          notifyListeners();
        } catch (_) {}
      }
    } catch (_) {}

    // 2. Fetch fresco desde GitHub sin caché
    unawaited(fetchRemoteConfig());

    // 3. Polling periódico cada 5 minutos
    _pollingTimer?.cancel();
    _pollingTimer = Timer.periodic(const Duration(minutes: 5), (_) {
      fetchRemoteConfig();
    });
  }

  /// Consulta la versión más reciente en GitHub con cache-busting
  Future<bool> fetchRemoteConfig() async {
    _isLoading = true;
    _lastError = null;
    notifyListeners();

    try {
      final cacheBustUrl =
          '$_rawUrl?ts=${DateTime.now().millisecondsSinceEpoch}';
      final response = await http
          .get(Uri.parse(cacheBustUrl))
          .timeout(const Duration(seconds: 8));

      if (response.statusCode == 200) {
        final decoded = jsonDecode(utf8.decode(response.bodyBytes))
            as Map<String, dynamic>;
        _config = GlobalEnvConfig.fromJson(decoded);

        // Guardar en SharedPreferences
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString(_prefsKey, jsonEncode(decoded));
        _isLoading = false;
        notifyListeners();
        return true;
      }
    } catch (e) {
      _lastError = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
    return false;
  }

  /// Obtiene el SHA actual de `db/global_config.json` en GitHub Contents API
  Future<String?> _fetchCurrentSha(String token) async {
    try {
      final response = await http.get(
        Uri.parse(_apiContentsUrl),
        headers: {
          'Accept': 'application/vnd.github+json',
          'User-Agent': 'UM-Studio-Web-Admin',
          if (token.isNotEmpty) 'Authorization': 'Bearer $token',
        },
      ).timeout(const Duration(seconds: 8));

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body) as Map<String, dynamic>;
        return data['sha']?.toString();
      }
    } catch (_) {}
    return null;
  }

  /// Publica la nueva configuración en GitHub mediante PUT (`db/global_config.json`).
  /// Exclusivo para administradores.
  Future<({bool success, String? error})> publishGlobalConfig({
    required GlobalEnvConfig newConfig,
    required String adminUsername,
    required String adminPin,
    GitHubSyncService? syncService,
  }) async {
    _isPublishing = true;
    _lastError = null;
    notifyListeners();

    try {
      // 1. Determinar token efectivo con permisos de escritura
      final token = syncService?.effectiveToken ?? AppConstants.envGithubToken;
      if (token.isEmpty) {
        _isPublishing = false;
        notifyListeners();
        return (
          success: false,
          error:
              'No hay token de GitHub configurado para publicar cambios globales.',
        );
      }

      // 2. Obtener SHA actual del archivo remoto
      final remoteSha = await _fetchCurrentSha(token) ?? _knownSha;

      final updatedConfig = newConfig.copyWith(
        updatedAt: DateTime.now().toIso8601String(),
        updatedBy: adminUsername,
      );

      final prettyJson = const JsonEncoder.withIndent('  ').convert(
        updatedConfig.toJson(),
      );
      final contentB64 = base64Encode(utf8.encode(prettyJson));

      final payload = <String, dynamic>{
        'message':
            'chore(config): actualizar variables de entorno globales por @$adminUsername',
        'content': contentB64,
        'branch': AppConstants.githubBranch,
        if (remoteSha != null && remoteSha.isNotEmpty) 'sha': remoteSha,
      };

      final response = await http
          .put(
            Uri.parse(_apiContentsUrl),
            headers: {
              'Accept': 'application/vnd.github+json',
              'Authorization': 'Bearer $token',
              'Content-Type': 'application/json',
              'User-Agent': 'UM-Studio-Web-Admin',
            },
            body: jsonEncode(payload),
          )
          .timeout(const Duration(seconds: 12));

      if (response.statusCode == 200 || response.statusCode == 201) {
        final decoded = jsonDecode(response.body) as Map<String, dynamic>;
        final contentMap = decoded['content'];
        if (contentMap is Map && contentMap['sha'] != null) {
          _knownSha = contentMap['sha'].toString();
          final prefs = await SharedPreferences.getInstance();
          await prefs.setString(_shaPrefsKey, _knownSha!);
          await prefs.setString(_prefsKey, jsonEncode(updatedConfig.toJson()));
        }

        _config = updatedConfig;
        _isPublishing = false;
        notifyListeners();
        return (success: true, error: null);
      }

      final body = response.body;
      _isPublishing = false;
      notifyListeners();
      return (
        success: false,
        error: 'Error al sincronizar con GitHub (${response.statusCode}): $body',
      );
    } catch (e) {
      _isPublishing = false;
      _lastError = e.toString();
      notifyListeners();
      return (success: false, error: e.toString());
    }
  }

  /// Permite sobrescribir la configuración local temporalmente para pruebas
  void updateLocalDraft(GlobalEnvConfig draft) {
    _config = draft;
    notifyListeners();
  }

  @override
  void dispose() {
    _pollingTimer?.cancel();
    super.dispose();
  }
}
