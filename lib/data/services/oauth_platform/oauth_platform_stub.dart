import 'dart:async';
import 'package:url_launcher/url_launcher.dart';

import 'oauth_flow_exception.dart';

/// Fallback para plataformas no-web (móvil y tests VM).
class OAuthPlatformDelegate {
  Future<String?> authorize({
    required String authUrl,
    required String redirectUri,
    required String expectedState,
  }) async {
    final uri = Uri.parse(authUrl);
    if (!await canLaunchUrl(uri)) {
      throw const OAuthFlowException(
        'No se pudo abrir el navegador para iniciar sesión con Microsoft.',
        code: 'launch_failed',
      );
    }
    await launchUrl(uri, mode: LaunchMode.externalApplication);
    return null;
  }

  String? getInitialAuthCode() => null;

  String? getInitialState() => null;

  /// Error OAuth (`?error=...`) con el que cargó la página, si existe.
  OAuthFlowException? getInitialError() => null;

  void cleanUrl(String cleanPath) {}
}

OAuthPlatformDelegate getOAuthPlatformDelegate() => OAuthPlatformDelegate();
