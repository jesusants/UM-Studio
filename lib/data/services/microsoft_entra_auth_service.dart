import 'dart:async';
import 'dart:convert';
import 'dart:math' as math;

import 'package:crypto/crypto.dart';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/entra_id_constants.dart';
import '../../services/oauth_platform/oauth_platform.dart';

/// Resultado del canje o renovación de tokens de Microsoft Entra ID.
class EntraTokenResult {
  const EntraTokenResult({
    required this.accessToken,
    required this.idToken,
    this.refreshToken,
    required this.expiresAt,
    required this.claims,
    this.photoBytes,
  });

  final String accessToken;
  final String idToken;
  final String? refreshToken;
  final DateTime expiresAt;
  final Map<String, dynamic> claims;
  final Uint8List? photoBytes;

  String? get oid => claims['oid']?.toString();
  String? get tid => claims['tid']?.toString();
  String? get name => (claims['name'] ?? claims['preferred_username'])?.toString();
  String? get email => (claims['preferred_username'] ?? claims['email'])?.toString();

  /// Identificador inmutable compuesto `${tid}_${oid}` (o fallback a `oid`).
  String get immutableKey {
    final t = tid;
    final o = oid;
    if (t != null && t.isNotEmpty && o != null && o.isNotEmpty) {
      return '${t}_$o';
    }
    return o ?? (email?.split('@').first ?? 'student');
  }

  bool get isExpired => DateTime.now().isAfter(expiresAt.subtract(const Duration(seconds: 45)));
}

/// Servicio oficial de autenticación OpenID Connect / OAuth 2.0 con PKCE
/// contra Microsoft Entra ID (Azure AD multiinquilino educativo) y Microsoft Graph API.
class MicrosoftEntraAuthService {
  MicrosoftEntraAuthService({
    http.Client? httpClient,
    OAuthPlatformDelegate? platformDelegate,
  })  : _http = httpClient ?? http.Client(),
        _platform = platformDelegate ?? createOAuthPlatform();

  final http.Client _http;
  final OAuthPlatformDelegate _platform;

  /// Detecta dinámicamente el redirect URI adecuado para el entorno actual.
  String get effectiveRedirectUri {
    if (kIsWeb) {
      final origin = Uri.base.origin;
      if (origin.contains('github.io')) {
        return EntraIdConstants.webProdRedirectUri;
      }
      // Entorno de desarrollo local (localhost:puerto)
      final path = Uri.base.path;
      final cleanPath = path.endsWith('/') ? path : '$path/';
      return '$origin$cleanPath';
    }
    return EntraIdConstants.mobileRedirectUri;
  }

  /// Genera un `code_verifier` de 64 caracteres seguros (RFC 7636).
  String generateCodeVerifier() {
    final random = math.Random.secure();
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~';
    return List.generate(64, (_) => chars[random.nextInt(chars.length)]).join();
  }

  /// Calcula el `code_challenge` S256 codificado en Base64Url sin relleno.
  String generateCodeChallenge(String verifier) {
    final bytes = ascii.encode(verifier);
    final digest = sha256.convert(bytes);
    return base64Url.encode(digest.bytes).replaceAll('=', '');
  }

  /// Genera un parámetro `state` criptográfico aleatorio para prevención CSRF.
  String generateState() {
    final random = math.Random.secure();
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    return List.generate(32, (_) => chars[random.nextInt(chars.length)]).join();
  }

  /// Construye la URL de inicio de sesión con Microsoft Entra ID.
  Uri buildAuthorizeUri({
    required String codeChallenge,
    required String state,
    required String redirectUri,
    String? prompt,
  }) {
    final query = <String, String>{
      'client_id': EntraIdConstants.clientId,
      'response_type': 'code',
      'redirect_uri': redirectUri,
      'response_mode': 'query',
      'scope': EntraIdConstants.scopes.join(' '),
      'state': state,
      'code_challenge': codeChallenge,
      'code_challenge_method': 'S256',
      if (prompt != null) 'prompt': prompt,
    };
    return Uri.parse(EntraIdConstants.authorizeEndpoint).replace(queryParameters: query);
  }

  /// Decodifica el payload de un `id_token` JWT normalizando el padding Base64Url.
  static Map<String, dynamic> decodeIdToken(String idToken) {
    try {
      final parts = idToken.split('.');
      if (parts.length < 2) return const {};
      var payload = parts[1].replaceAll('-', '+').replaceAll('_', '/');
      while (payload.length % 4 != 0) {
        payload += '=';
      }
      final decodedJson = utf8.decode(base64Decode(payload));
      return jsonDecode(decodedJson) as Map<String, dynamic>;
    } catch (_) {
      return const {};
    }
  }

  /// Ejecuta el flujo interactivo de autenticación mediante Popup / Redirect con PKCE.
  Future<({EntraTokenResult? result, String? error})> loginInteractive({
    String? prompt,
  }) async {
    try {
      final verifier = generateCodeVerifier();
      final challenge = generateCodeChallenge(verifier);
      final state = generateState();
      final redirectUri = effectiveRedirectUri;

      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(EntraIdConstants.prefsPkceVerifier, verifier);
      await prefs.setString(EntraIdConstants.prefsPkceState, state);

      final authUri = buildAuthorizeUri(
        codeChallenge: challenge,
        state: state,
        redirectUri: redirectUri,
        prompt: prompt,
      );

      // Disparar flujo según plataforma (Popup en Web, CustomTab en Móvil)
      final code = await _platform.authorize(
        authUrl: authUri.toString(),
        redirectUri: redirectUri,
        expectedState: state,
      );

      if (code == null || code.isEmpty) {
        // Web sin popup: la pestaña navega a Microsoft y al volver se canjea ?code=...
        if (kIsWeb) return (result: null, error: null);
        return (
          result: null,
          error: 'Completa el inicio de sesión en el navegador y vuelve a la app.',
        );
      }

      // Canje del código de autorización por tokens
      final tokens = await exchangeCodeForTokens(
        code: code,
        verifier: verifier,
        redirectUri: redirectUri,
      );

      if (tokens.error != null || tokens.result == null) {
        return (result: null, error: tokens.error ?? 'Error al canjear tokens con Microsoft.');
      }

      // Descargar foto de perfil desde Graph API
      final photo = await fetchProfilePhoto(tokens.result!.accessToken);
      final fullResult = EntraTokenResult(
        accessToken: tokens.result!.accessToken,
        idToken: tokens.result!.idToken,
        refreshToken: tokens.result!.refreshToken,
        expiresAt: tokens.result!.expiresAt,
        claims: tokens.result!.claims,
        photoBytes: photo,
      );

      await persistSession(fullResult);
      return (result: fullResult, error: null);
    } on OAuthFlowException catch (e) {
      return (result: null, error: e.message);
    } on TimeoutException {
      return (
        result: null,
        error: 'Microsoft no respondió a tiempo. Revisa tu conexión e inténtalo de nuevo.',
      );
    } catch (e) {
      return (result: null, error: 'No se pudo iniciar sesión con Microsoft: $e');
    }
  }

  /// Canjea el código de autorización por Access, ID y Refresh Token (RFC 7636).
  Future<({EntraTokenResult? result, String? error})> exchangeCodeForTokens({
    required String code,
    required String verifier,
    required String redirectUri,
  }) async {
    try {
      final res = await _http.post(
        Uri.parse(EntraIdConstants.tokenEndpoint),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json',
        },
        body: {
          'client_id': EntraIdConstants.clientId,
          'grant_type': 'authorization_code',
          'code': code,
          'redirect_uri': redirectUri,
          'code_verifier': verifier,
          'scope': EntraIdConstants.scopes.join(' '),
        },
      ).timeout(const Duration(seconds: 12));

      if (res.statusCode == 200) {
        final body = jsonDecode(res.body) as Map<String, dynamic>;
        final access = (body['access_token'] ?? '').toString();
        final idToken = (body['id_token'] ?? '').toString();
        final refresh = body['refresh_token']?.toString();
        final expiresIn = (body['expires_in'] is num) ? (body['expires_in'] as num).toInt() : 3600;
        final expiresAt = DateTime.now().add(Duration(seconds: expiresIn));
        final claims = decodeIdToken(idToken);

        return (
          result: EntraTokenResult(
            accessToken: access,
            idToken: idToken,
            refreshToken: refresh,
            expiresAt: expiresAt,
            claims: claims,
          ),
          error: null,
        );
      }

      final errorBody = res.body;
      String? oauthError;
      String? oauthDesc;
      try {
        final decoded = jsonDecode(errorBody);
        if (decoded is Map) {
          oauthError = decoded['error']?.toString();
          oauthDesc = decoded['error_description']?.toString();
        }
      } catch (_) {}
      return (
        result: null,
        error: oauthError != null
            ? OAuthFlowException.fromOAuthError(oauthError, oauthDesc).message
            : 'Microsoft respondió con un error (HTTP ${res.statusCode}). Inténtalo de nuevo.',
      );
    } on TimeoutException {
      return (
        result: null,
        error: 'Microsoft no respondió a tiempo. Revisa tu conexión e inténtalo de nuevo.',
      );
    } catch (e) {
      return (result: null, error: 'Error de conexión con Microsoft: $e');
    }
  }

  /// Renueva los tokens silenciosamente usando el `refresh_token` sin intervención del usuario.
  Future<EntraTokenResult?> refreshTokensSilently(String refreshToken) async {
    try {
      final res = await _http.post(
        Uri.parse(EntraIdConstants.tokenEndpoint),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json',
        },
        body: {
          'client_id': EntraIdConstants.clientId,
          'grant_type': 'refresh_token',
          'refresh_token': refreshToken,
          'scope': EntraIdConstants.scopes.join(' '),
        },
      ).timeout(const Duration(seconds: 10));

      if (res.statusCode == 200) {
        final body = jsonDecode(res.body) as Map<String, dynamic>;
        final access = (body['access_token'] ?? '').toString();
        final idToken = (body['id_token'] ?? '').toString();
        final newRefresh = body['refresh_token']?.toString() ?? refreshToken;
        final expiresIn = (body['expires_in'] is num) ? (body['expires_in'] as num).toInt() : 3600;
        final expiresAt = DateTime.now().add(Duration(seconds: expiresIn));
        final claims = decodeIdToken(idToken);

        final tokenResult = EntraTokenResult(
          accessToken: access,
          idToken: idToken,
          refreshToken: newRefresh,
          expiresAt: expiresAt,
          claims: claims,
        );
        await persistSession(tokenResult);
        return tokenResult;
      }
      return null;
    } catch (_) {
      return null;
    }
  }

  /// Obtiene los bytes de la foto de perfil desde Microsoft Graph API.
  Future<Uint8List?> fetchProfilePhoto(String accessToken) async {
    try {
      final res = await _http.get(
        Uri.parse(EntraIdConstants.graphPhotoEndpoint),
        headers: {
          'Authorization': 'Bearer $accessToken',
        },
      ).timeout(const Duration(seconds: 8));

      if (res.statusCode == 200 && res.bodyBytes.isNotEmpty) {
        return res.bodyBytes;
      }
      return null;
    } catch (_) {
      return null;
    }
  }

  /// Persiste la sesión y la foto en Base64 en `SharedPreferences` para arranque en 0 ms.
  Future<void> persistSession(EntraTokenResult result) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(EntraIdConstants.prefsAccessToken, result.accessToken);
    await prefs.setString(EntraIdConstants.prefsIdToken, result.idToken);
    if (result.refreshToken != null) {
      await prefs.setString(EntraIdConstants.prefsRefreshToken, result.refreshToken!);
    }
    await prefs.setInt(
      EntraIdConstants.prefsTokenExp,
      result.expiresAt.millisecondsSinceEpoch,
    );

    if (result.oid != null) {
      await prefs.setString(EntraIdConstants.prefsUserOid, result.oid!);
    }
    if (result.tid != null) {
      await prefs.setString(EntraIdConstants.prefsUserTid, result.tid!);
    }
    if (result.name != null) {
      await prefs.setString(EntraIdConstants.prefsUserName, result.name!);
    }
    if (result.email != null) {
      await prefs.setString(EntraIdConstants.prefsUserEmail, result.email!);
    }

    if (result.photoBytes != null && result.photoBytes!.isNotEmpty) {
      final b64 = base64Encode(result.photoBytes!);
      await prefs.setString(EntraIdConstants.prefsProfilePhotoB64, b64);
    }
  }

  /// Carga la sesión guardada desde `SharedPreferences` y la renueva en segundo plano si expiró.
  Future<EntraTokenResult?> restorePersistedSession() async {
    final prefs = await SharedPreferences.getInstance();
    final access = prefs.getString(EntraIdConstants.prefsAccessToken);
    final idToken = prefs.getString(EntraIdConstants.prefsIdToken);
    final refresh = prefs.getString(EntraIdConstants.prefsRefreshToken);
    final expMs = prefs.getInt(EntraIdConstants.prefsTokenExp);
    final photoB64 = prefs.getString(EntraIdConstants.prefsProfilePhotoB64);

    if (access == null || idToken == null || expMs == null) {
      return null;
    }

    final expiresAt = DateTime.fromMillisecondsSinceEpoch(expMs);
    final claims = decodeIdToken(idToken);
    Uint8List? photoBytes;
    if (photoB64 != null && photoB64.isNotEmpty) {
      try {
        photoBytes = base64Decode(photoB64);
      } catch (_) {}
    }

    final cached = EntraTokenResult(
      accessToken: access,
      idToken: idToken,
      refreshToken: refresh,
      expiresAt: expiresAt,
      claims: claims,
      photoBytes: photoBytes,
    );

    // Si aún está vigente, retornamos de inmediato
    if (!cached.isExpired) {
      return cached;
    }

    // Si expiró pero tenemos refresh token, renovamos
    if (refresh != null && refresh.isNotEmpty) {
      final renewed = await refreshTokensSilently(refresh);
      if (renewed != null) {
        return EntraTokenResult(
          accessToken: renewed.accessToken,
          idToken: renewed.idToken,
          refreshToken: renewed.refreshToken,
          expiresAt: renewed.expiresAt,
          claims: renewed.claims,
          photoBytes: photoBytes,
        );
      }
    }

    return cached;
  }

  /// Lee la foto de perfil en Base64 en 0 ms desde caché local.
  Future<Uint8List?> loadCachedPhoto() async {
    final prefs = await SharedPreferences.getInstance();
    final b64 = prefs.getString(EntraIdConstants.prefsProfilePhotoB64);
    if (b64 != null && b64.isNotEmpty) {
      try {
        return base64Decode(b64);
      } catch (_) {}
    }
    return null;
  }

  /// Cierra la sesión en Microsoft y elimina credenciales locales.
  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(EntraIdConstants.prefsAccessToken);
    await prefs.remove(EntraIdConstants.prefsIdToken);
    await prefs.remove(EntraIdConstants.prefsRefreshToken);
    await prefs.remove(EntraIdConstants.prefsTokenExp);
    await prefs.remove(EntraIdConstants.prefsUserOid);
    await prefs.remove(EntraIdConstants.prefsUserTid);
    await prefs.remove(EntraIdConstants.prefsUserName);
    await prefs.remove(EntraIdConstants.prefsUserEmail);
    await prefs.remove(EntraIdConstants.prefsProfilePhotoB64);
    await prefs.remove(EntraIdConstants.prefsPkceVerifier);
    await prefs.remove(EntraIdConstants.prefsPkceState);
  }

  /// Ejecuta la purga controlada de datos de login legacy conservando intactos
  /// todos los apuntes, notas locales, horarios y progreso de materias.
  Future<void> runMigrationIfNeeded() async {
    final prefs = await SharedPreferences.getInstance();
    final migrated = prefs.getBool(EntraIdConstants.prefsMigrationFlag) ?? false;
    if (!migrated) {
      // Purgamos PINs anteriores sin tocar 'um_studio_active_student_json_v2'
      await prefs.remove('um_studio_student_pin');
      await prefs.remove('um_studio_login_pin');
      await prefs.setBool(EntraIdConstants.prefsMigrationFlag, true);
    }
  }

  /// Limpia la barra de direcciones del navegador web tras canjear parámetros OAuth.
  void cleanWebUrl() {
    _platform.cleanUrl(kIsWeb ? '/UM-Studio/' : '/');
  }

  /// Revisa si el navegador cargó inicialmente con un código OAuth en la URL.
  String? checkInitialAuthCode() => _platform.getInitialAuthCode();
  String? checkInitialState() => _platform.getInitialState();

  /// Error OAuth (`?error=...`) devuelto por Microsoft al volver por redirección.
  String? checkInitialError() => _platform.getInitialError()?.message;
}
