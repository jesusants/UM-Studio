/// Constantes globales y configuración de entorno de UM STUDIO.
abstract final class AppConstants {
  static const String appTitle = 'UM STUDIO';
  static const String universityName = 'Unimagdalena';
  static const String programSubtitle = 'Unimagdalena • Ing. Energética';
  static const String institutionalDomain = '@unimagdalena.edu.co';

  /// Cupo diario de consultas académicas.
  static const int initialDailyUsage = 9;
  static const int warningDailyThreshold = 12;
  static const int maxDailyUsage = 15;

  /// Dimensiones base del shell móvil iOS.
  static const double maxPhoneViewportWidth = 430.0;

  /// Tiempos de sincronización y debounce.
  static const Duration noteAutoSaveDebounce = Duration(seconds: 1);
  static const Duration tapScaleDuration = Duration(milliseconds: 140);

  /// Configuración de backend (Supabase PostgreSQL + Storage).
  static const String supabaseUrl = String.fromEnvironment('SUPABASE_URL');
  static const String supabaseAnonKey =
      String.fromEnvironment('SUPABASE_ANON_KEY');
  static const String defaultStudentEmail = String.fromEnvironment(
    'UM_USER_EMAIL',
    defaultValue: 'estudiante.energia@unimagdalena.edu.co',
  );
  static const String storageBucket = 'adjuntos_estudio';

  static bool get isSupabaseConfigured =>
      supabaseUrl.isNotEmpty && supabaseAnonKey.isNotEmpty;
}
