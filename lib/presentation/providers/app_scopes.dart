import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/app_constants.dart';
import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../domain/repositories/i_clase_viva_repository.dart';

/// Expone el [ThemeController] al árbol de widgets.
class ThemeScope extends InheritedNotifier<ThemeController> {
  const ThemeScope({
    super.key,
    required ThemeController controller,
    required super.child,
  }) : super(notifier: controller);

  static ThemeController of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<ThemeScope>()!.notifier!;
}

/// Expone el contrato [IClaseVivaRepository] en el árbol de widgets.
class ClaseVivaRepositoryScope extends InheritedWidget {
  const ClaseVivaRepositoryScope({
    super.key,
    required this.repository,
    required super.child,
  });

  final IClaseVivaRepository repository;

  static IClaseVivaRepository of(BuildContext context) {
    final scope =
        context.dependOnInheritedWidgetOfExactType<ClaseVivaRepositoryScope>();
    assert(
      scope != null,
      'ClaseVivaRepositoryScope no fue encontrado en el árbol de widgets.',
    );
    return scope!.repository;
  }

  @override
  bool updateShouldNotify(ClaseVivaRepositoryScope oldWidget) =>
      oldWidget.repository != repository;
}

/// Gestiona la sesión institucional (`@unimagdalena.edu.co`) y el cupo
/// de uso diario de forma reactiva y persistente.
class InstitutionalSessionController extends ChangeNotifier {
  InstitutionalSessionController({
    required IClaseVivaRepository repository,
  }) : _repository = repository;

  static const String _emailPrefsKey = 'um_studio_institutional_email';
  static const String _usagePrefsKey = 'um_studio_daily_usage';

  final IClaseVivaRepository _repository;

  String _email = AppConstants.defaultStudentEmail;
  int _dailyUsage = AppConstants.initialDailyUsage;

  String get email => _email;
  int get dailyUsage => _dailyUsage;
  int get maxDailyUsage => AppConstants.maxDailyUsage;

  Future<void> load() async {
    final prefs = await SharedPreferences.getInstance();
    final savedEmail = prefs.getString(_emailPrefsKey);
    if (savedEmail != null &&
        InstitutionalValidator.isValidInstitutionalEmail(savedEmail)) {
      _email = savedEmail;
      _repository.updateActiveUser(savedEmail);
    }
    final savedUsage = prefs.getInt(_usagePrefsKey);
    if (savedUsage != null) {
      _dailyUsage = savedUsage.clamp(0, AppConstants.maxDailyUsage);
    }
  }

  /// Actualiza el correo institucional tras validar el dominio `@unimagdalena.edu.co`.
  Future<String?> updateInstitutionalEmail(String candidateEmail) async {
    final error = InstitutionalValidator.validateEmailOrError(candidateEmail);
    if (error != null) return error;

    final clean = candidateEmail.trim().toLowerCase();
    _email = clean;
    _repository.updateActiveUser(clean);
    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_emailPrefsKey, clean);
    return null;
  }

  Future<void> addUsageQuota(int delta) async {
    final next = (_dailyUsage + delta).clamp(0, AppConstants.maxDailyUsage);
    if (next == _dailyUsage) return;
    _dailyUsage = next;
    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt(_usagePrefsKey, _dailyUsage);
  }
}

/// Expone [InstitutionalSessionController] al árbol de widgets.
class SessionScope extends InheritedNotifier<InstitutionalSessionController> {
  const SessionScope({
    super.key,
    required InstitutionalSessionController controller,
    required super.child,
  }) : super(notifier: controller);

  static InstitutionalSessionController? maybeOf(BuildContext context) =>
      context
          .dependOnInheritedWidgetOfExactType<SessionScope>()
          ?.notifier;

  static InstitutionalSessionController of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<SessionScope>()!.notifier!;
}
