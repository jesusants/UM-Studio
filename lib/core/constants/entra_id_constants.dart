/// Constantes oficiales de Microsoft Entra ID para UM Studio.
abstract final class EntraIdConstants {
  /// Nombre oficial de la aplicación en Azure / Entra ID.
  static const String appName = 'UM Studio';

  /// Client ID (Id. de aplicación) registrado en Microsoft Entra ID.
  static const String clientId = 'bb954d45-ebcd-4a04-8ac0-af00cc9cece1';

  /// Directory (Tenant) ID institucional de la Universidad del Magdalena.
  static const String tenantId = 'b6b897f5-08ad-4ed7-8ed6-55207495fad0';

  /// Authority para cuentas educativas/institucionales (multiinquilino).
  static const String authority =
      'https://login.microsoftonline.com/organizations/oauth2/v2.0';

  /// Endpoint de autorización interactiva OAuth 2.0 PKCE.
  static const String authorizeEndpoint =
      '$authority/authorize';

  /// Endpoint de canje y renovación de tokens OAuth 2.0 PKCE.
  static const String tokenEndpoint =
      '$authority/token';

  /// Endpoint de Microsoft Graph API para la foto de perfil en alta resolución.
  static const String graphPhotoEndpoint =
      'https://graph.microsoft.com/v1.0/me/photo/\$value';

  /// Redirect URI oficial para producción en GitHub Pages.
  static const String webProdRedirectUri =
      'https://jesusants.github.io/UM-Studio/';

  /// Redirect URI para plataformas móviles Android / iOS.
  static const String mobileRedirectUri =
      'msauth://co.edu.unimagdalena.um_studio/auth';

  /// Scopes requeridos para perfil institucional y foto.
  static const List<String> scopes = [
    'openid',
    'profile',
    'email',
    'offline_access',
    'User.Read',
  ];

  // Claves de persistencia en SharedPreferences
  static const String prefsAccessToken = 'um_studio_entra_access_token_v1';
  static const String prefsIdToken = 'um_studio_entra_id_token_v1';
  static const String prefsRefreshToken = 'um_studio_entra_refresh_token_v1';
  static const String prefsTokenExp = 'um_studio_entra_token_exp_v1';
  static const String prefsUserOid = 'um_studio_entra_user_oid_v1';
  static const String prefsUserTid = 'um_studio_entra_user_tid_v1';
  static const String prefsUserName = 'um_studio_entra_user_name_v1';
  static const String prefsUserEmail = 'um_studio_entra_user_email_v1';
  static const String prefsProfilePhotoB64 = 'um_studio_user_photo_b64';
  static const String prefsMigrationFlag = 'migrated_to_entra_v1';
  static const String prefsPkceVerifier = 'um_studio_pkce_verifier_temp';
  static const String prefsPkceState = 'um_studio_pkce_state_temp';
}
