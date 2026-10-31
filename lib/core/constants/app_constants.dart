/// Constantes globales y configuración Serverless en GitHub de UM STUDIO.
abstract final class AppConstants {
  static const String appTitle = 'UM STUDIO';
  static const String universityName = 'Unimagdalena';
  static const String programName = 'Ingeniería Energética';
  static const String programCode = '8108';
  static const String programSnies = '118222';
  static const String programSubtitle = 'Unimagdalena • Ing. Energética';
  static const String programLockedBadge =
      'Unimagdalena • Ingeniería Energética (Plan 8108)';
  static const String institutionalDomain = '@unimagdalena.edu.co';

  /// Dimensiones base del shell móvil iOS.
  static const double maxPhoneViewportWidth = 430.0;

  /// Tiempos de sincronización optimista y animaciones táctiles.
  static const Duration noteAutoSaveDebounce = Duration(seconds: 1);
  static const Duration githubSyncDebounce = Duration(milliseconds: 1200);
  static const Duration tapScaleDuration = Duration(milliseconds: 140);

  /// Base de datos maestra (.md con YAML Frontmatter + KaTeX) y emblema oficial.
  static const String curriculumAssetPath =
      'assets/data/ingenieria_energetica.md';
  static const String programLogoAsset =
      'assets/images/logo_ing_energetica.png';

  /// Repositorio Serverless en GitHub (`jesusants/UM-Studio`).
  static const String githubOwner = 'jesusants';
  static const String githubRepo = 'UM-Studio';
  static const String githubBranch = 'main';

  static const String curriculumRawUrl =
      'https://raw.githubusercontent.com/$githubOwner/$githubRepo/$githubBranch/db/ingenieria_energetica.md';

  static const String githubApiBase =
      'https://api.github.com/repos/$githubOwner/$githubRepo/contents';

  /// Token inyectado en compilación (`--dart-define=UM_GH_TOKEN=...` desde GitHub Secrets).
  static const String envGithubToken = String.fromEnvironment('UM_GH_TOKEN');

  static const String defaultStudentEmail =
      'estudiante.energia@unimagdalena.edu.co';
}
