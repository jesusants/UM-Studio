import 'dart:async';
import 'package:url_launcher/url_launcher.dart';

/// Fallback para plataformas no-web (móvil y tests VM).
class OAuthPlatformDelegate {
  Future<String?> authorize({
    required String authUrl,
    required String redirectUri,
    required String expectedState,
  }) async {
    final uri = Uri.parse(authUrl);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
    return null;
  }

  String? getInitialAuthCode() => null;

  String? getInitialState() => null;

  void cleanUrl(String cleanPath) {}
}

OAuthPlatformDelegate getOAuthPlatformDelegate() => OAuthPlatformDelegate();
