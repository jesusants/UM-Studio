import 'dart:async';
import 'dart:convert';
import 'dart:math' as math;

import 'package:crypto/crypto.dart';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/entra_id_constants.dart';
import 'oauth_platform/oauth_platform.dart';

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
  String? get name =>
      (claims['name'] ?? claims['preferred_username'])?.toString();
  String? get email =>
      (claims['preferred_username'] ?? claims['email'] ?? claims['upn'])
          ?.toString();

  /// Identificador inmutable compuesto `${tid}_${oid}` (o fallback a `oid`).
  String get immutableKey {
    final t = tid;
    final o = oid;
    if (t != null && t.isNotEmpty && o != null && o.isNotEmpty) {
      return '${t}_$o';
    }
    return o ?? (email?.split('@').first ?? 'student');
  }

  bool get isExpired =>
      DateTime.now().isAfter(expiresAt.subtract(const Duration(seconds: 45)));
}

/// Servicio de autenticación OpenID Connect / OAuth 2.0 con PKCE
/// contra Microsoft Entra ID (modo multiinquilino educativo) y Microsoft Graph API.
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
    const chars =
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~';
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
    const chars =
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
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
    return Uri.parse(EntraIdConstants.authorizeEndpoint)
        .replace(queryParameters: query);
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

  /// Purga sesiones o tokens obsoletos antes de un nuevo handshake.
  Future<void> purgeStaleTokens() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(EntraIdConstants.prefsAccessToken);
    await prefs.remove(EntraIdConstants.prefsIdToken);
    await prefs.remove(EntraIdConstants.prefsRefreshToken);
    await prefs.remove(EntraIdConstants.prefsTokenExp);
    await prefs.remove(EntraIdConstants.prefsPkceVerifier);
    await prefs.remove(EntraIdConstants.prefsPkceState);
  }

  /// Ejecuta el flujo interactivo de autenticación mediante Popup / Redirect con PKCE.
  Future<({EntraTokenResult? result, String? error})> loginInteractive({
    String? prompt,
  }) async {
    try {
      // 1. Limpieza preventiva de tokens residuales antes del handshake
      await purgeStaleTokens();

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

      final authCode = await _platform.authorize(
        authUrl: authUri.toString(),
        redirectUri: redirectUri,
        expectedState: state,
      );

      // Si fue redirección en la misma ventana, el código vendrá al recargar
      if (authCode == null) {
        return (result: null, error: null);
      }

      return await exchangeCodeForTokens(
        code: authCode,
        verifier: verifier,
        redirectUri: redirectUri,
      );
    } on OAuthFlowException catch (e) {
      return (result: null, error: e.message);
    } catch (e) {
      return (
        result: null,
        error: 'Ocurrió un error inesperado al conectar con Microsoft: $e'
      );
    }
  }

  /// Canjea el `authorization_code` por tokens definitivos mediante PKCE.
  Future<({EntraTokenResult? result, String? error})> exchangeCodeForTokens({
    required String code,
    required String verifier,
    required String redirectUri,
  }) async {
    try {
      final response = await _http.post(
        Uri.parse(EntraIdConstants.tokenEndpoint),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        },
        body: {
          'client_id': EntraIdConstants.clientId,
          'grant_type': 'authorization_code',
          'code': code,
          'redirect_uri': redirectUri,
          'code_verifier': verifier,
          'scope': EntraIdConstants.scopes.join(' '),
        },
      );

      if (response.statusCode != 200) {
        try {
          final errJson = jsonDecode(response.body) as Map<String, dynamic>;
          final err = errJson['error']?.toString() ?? 'token_exchange_failed';
          final desc = errJson['error_description']?.toString();
          return (
            result: null,
            error: OAuthFlowException.fromOAuthError(err, desc).message
          );
        } catch (_) {
          return (
            result: null,
            error:
                'Error al canjear el código con Microsoft (HTTP ${response.statusCode}).'
          );
        }
      }

      final body = jsonDecode(response.body) as Map<String, dynamic>;
      final accessToken = body['access_token']?.toString() ?? '';
      final idToken = body['id_token']?.toString() ?? '';
      final refreshToken = body['refresh_token']?.toString();
      final expiresIn = body['expires_in'] is num
          ? (body['expires_in'] as num).toInt()
          : int.tryParse(body['expires_in']?.toString() ?? '') ?? 3600;

      final claims = decodeIdToken(idToken);
      final expiresAt = DateTime.now().add(Duration(seconds: expiresIn));

      // 2. Validación institucional: verificar claims organizacionales
      final userEmail =
          (claims['preferred_username'] ?? claims['email'] ?? claims['upn'])
              ?.toString();
      if (userEmail != null && userEmail.isNotEmpty) {
        final clean = userEmail.trim().toLowerCase();
        // Si tiene dominio de correo, validar que sea @unimagdalena.edu.co o tenga claim oid/tid
        if (clean.contains('@') &&
            !clean.endsWith('@unimagdalena.edu.co') &&
            claims['tid'] == null) {
          return (
            result: null,
            error:
                'Acceso restringido: Se requiere una cuenta institucional (@unimagdalena.edu.co).'
          );
        }
      }

      // 3. Obtener la foto de perfil desde Microsoft Graph API
      final photoBytes = await fetchProfilePhoto(accessToken);

      final tokenResult = EntraTokenResult(
        accessToken: accessToken,
        idToken: idToken,
        refreshToken: refreshToken,
        expiresAt: expiresAt,
        claims: claims,
        photoBytes: photoBytes,
      );

      // Guardar en persistencia segura
      await persistSession(tokenResult);

      return (result: tokenResult, error: null);
    } catch (e) {
      return (
        result: null,
        error: 'No se pudo completar el intercambio de credenciales: $e'
      );
    }
  }

  /// Obtiene la foto de perfil del usuario desde Microsoft Graph API.
  /// Maneja graciosamente el 404 cuando la cuenta no tiene foto.
  Future<Uint8List?> fetchProfilePhoto(String accessToken) async {
    try {
      final response = await _http.get(
        Uri.parse(EntraIdConstants.graphPhotoEndpoint),
        headers: {
          'Authorization': 'Bearer $accessToken',
        },
      );

      if (response.statusCode == 200 && response.bodyBytes.isNotEmpty) {
        return response.bodyBytes;
      }
      // 404: La cuenta no tiene foto en Microsoft Graph
      if (response.statusCode == 404) {
        return null;
      }
      return null;
    } catch (_) {
      return null;
    }
  }

  /// Renueva los tokens en segundo plano usando el `refresh_token`.
  Future<EntraTokenResult?> refreshTokensSilently(String refreshToken) async {
    try {
      final response = await _http.post(
        Uri.parse(EntraIdConstants.tokenEndpoint),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        },
        body: {
          'client_id': EntraIdConstants.clientId,
          'grant_type': 'refresh_token',
          'refresh_token': refreshToken,
          'scope': EntraIdConstants.scopes.join(' '),
        },
      );

      if (response.statusCode != 200) return null;

      final body = jsonDecode(response.body) as Map<String, dynamic>;
      final newAccess = body['access_token']?.toString() ?? '';
      final newIdToken = body['id_token']?.toString() ?? '';
      final newRefresh = body['refresh_token']?.toString() ?? refreshToken;
      final expiresIn = body['expires_in'] is num
          ? (body['expires_in'] as num).toInt()
          : 3600;

      final claims = decodeIdToken(newIdToken);
      final expiresAt = DateTime.now().add(Duration(seconds: expiresIn));
      final photoBytes = await fetchProfilePhoto(newAccess);

      final result = EntraTokenResult(
        accessToken: newAccess,
        idToken: newIdToken,
        refreshToken: newRefresh,
        expiresAt: expiresAt,
        claims: claims,
        photoBytes: photoBytes,
      );

      await persistSession(result);
      return result;
    } catch (_) {
      return null;
    }
  }

  /// Guarda los tokens y claims de Microsoft Entra ID en `SharedPreferences`.
  Future<void> persistSession(EntraTokenResult result) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(EntraIdConstants.prefsAccessToken, result.accessToken);
    await prefs.setString(EntraIdConstants.prefsIdToken, result.idToken);
    if (result.refreshToken != null) {
      await prefs.setString(
          EntraIdConstants.prefsRefreshToken, result.refreshToken!);
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

  /// Carga la sesión guardada desde `SharedPreferences` y la renueva si expiró.
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

    if (!cached.isExpired) {
      return cached;
    }

    if (refresh != null && refresh.isNotEmpty) {
      final renewed = await refreshTokensSilently(refresh);
      if (renewed != null) {
        return renewed;
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

  /// Ejecuta la migración/reasignación de datos locales al `oid` / `${tid}_${oid}`
  /// garantizando que no se pierdan apuntes, notas o progreso previos.
  Future<void> migrateLocalDataToOid({
    required String immutableKey,
    required String legacyUsername,
  }) async {
    if (immutableKey == legacyUsername) return;
    final prefs = await SharedPreferences.getInstance();
    // Reasignar claves de notas si existen bajo el nombre previo
    final allKeys = prefs.getKeys();
    for (final key in allKeys) {
      if (key.contains('_${legacyUsername}_')) {
        final newKey = key.replaceAll('_${legacyUsername}_', '_${immutableKey}_');
        final value = prefs.get(key);
        if (value is String) {
          await prefs.setString(newKey, value);
        }
      }
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
