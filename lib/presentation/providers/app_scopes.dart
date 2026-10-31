import 'dart:async';

import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/app_constants.dart';
import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../data/models/curriculum_models.dart';
import '../../data/models/student_user_model.dart';
import '../../data/repositories/local_clase_viva_repository.dart';
import '../../data/services/github_sync_service.dart';
import '../../data/services/markdown_curriculum_service.dart';
import '../../domain/entities/subject_summary.dart';
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

/// Expone [MarkdownCurriculumService] al árbol de widgets.
class CurriculumScope extends InheritedNotifier<MarkdownCurriculumService> {
  const CurriculumScope({
    super.key,
    required MarkdownCurriculumService service,
    required super.child,
  }) : super(notifier: service);

  static MarkdownCurriculumService? maybeOf(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<CurriculumScope>()?.notifier;

  static MarkdownCurriculumService of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<CurriculumScope>()!.notifier!;
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

/// Controlador principal de sesión estudiantil de Ingeniería Energética,
/// conectado con `GitHubSyncService` (`db/users/{username}.json`) y
/// almacenamiento local instantáneo (0 ms).
class InstitutionalSessionController extends ChangeNotifier {
  InstitutionalSessionController({
    required IClaseVivaRepository repository,
    GitHubSyncService? syncService,
    MarkdownCurriculumService? curriculumService,
  })  : _repository = repository,
        _syncService = syncService ?? GitHubSyncService(),
        _curriculumService = curriculumService {
    _syncService.addListener(notifyListeners);
    final repo = _repository;
    if (repo is LocalReactiveClaseVivaRepository) {
      repo.onPersonalNoteSynced = syncPersonalNote;
    }
  }

  static const String _legacyEmailPrefsKey = 'um_studio_institutional_email';
  static const String _legacyUsagePrefsKey = 'um_studio_daily_usage';

  final IClaseVivaRepository _repository;
  final GitHubSyncService _syncService;
  final MarkdownCurriculumService? _curriculumService;

  StudentUserModel? _currentUser;
  String _fallbackEmail = AppConstants.defaultStudentEmail;
  int _fallbackUsage = AppConstants.initialDailyUsage;
  bool _initialized = false;

  bool get isInitialized => _initialized;
  bool get isAuthenticated => _currentUser != null;
  StudentUserModel? get currentUser => _currentUser;
  GitHubSyncService get syncService => _syncService;

  String get email => _currentUser?.email ?? _fallbackEmail;
  String get username =>
      _currentUser?.username ?? _fallbackEmail.split('@').first;
  String get displayName => _currentUser?.nombre ?? 'Estudiante Ing. Energética';
  String get primerNombre => _currentUser?.primerNombre ?? 'Ingeniero';
  String get initials => _currentUser?.iniciales ?? 'UM';
  int get cuatrimestreActual => _currentUser?.cuatrimestreActual ?? 2;

  int get dailyUsage => _currentUser?.usoDiario.actual ?? _fallbackUsage;
  int get maxDailyUsage =>
      _currentUser?.usoDiario.maximo ?? AppConstants.maxDailyUsage;

  Map<String, int> get progresoMaterias =>
      _currentUser?.progresoMaterias ?? const {};

  List<CalendarReminderModel> get reminders {
    final list = List<CalendarReminderModel>.from(
      _currentUser?.recordatoriosCalendario ?? const [],
    );
    list.sort((a, b) {
      final dateCmp = a.fechaIso.compareTo(b.fechaIso);
      if (dateCmp != 0) return dateCmp;
      return a.hora.compareTo(b.hora);
    });
    return list;
  }

  @override
  void dispose() {
    _syncService.removeListener(notifyListeners);
    super.dispose();
  }

  /// Carga la sesión persistente ("Recordar mis datos" activo por defecto)
  /// y sincroniza silenciosamente con GitHub en segundo plano.
  Future<void> load({bool syncRemoteOnStartup = true}) async {
    final persisted = await _syncService.loadPersistedSession();
    if (persisted != null) {
      await _activateUser(persisted);
      _initialized = true;
      notifyListeners();

      if (syncRemoteOnStartup) {
        unawaited(_refreshFromGitHubInBackground(persisted));
      }
      return;
    }

    final prefs = await SharedPreferences.getInstance();
    final savedEmail = prefs.getString(_legacyEmailPrefsKey);
    if (savedEmail != null &&
        InstitutionalValidator.isValidInstitutionalEmail(savedEmail)) {
      _fallbackEmail = savedEmail;
      _repository.updateActiveUser(savedEmail);
    }
    final savedUsage = prefs.getInt(_legacyUsagePrefsKey);
    if (savedUsage != null) {
      _fallbackUsage = savedUsage.clamp(0, AppConstants.maxDailyUsage);
    }

    _initialized = true;
    notifyListeners();
  }

  Future<void> _refreshFromGitHubInBackground(
    StudentUserModel localUser,
  ) async {
    final synced = await _syncService.syncOnStartup(localUser);
    if (synced != null && _currentUser?.username == synced.username) {
      await _activateUser(synced);
      notifyListeners();
    }
  }

  Future<void> _activateUser(StudentUserModel user) async {
    _currentUser = user;
    _fallbackEmail = user.email;
    _fallbackUsage = user.usoDiario.actual;
    if (InstitutionalValidator.isValidInstitutionalEmail(user.email)) {
      _repository.updateActiveUser(user.email);
    }
    final repo = _repository;
    if (repo is LocalReactiveClaseVivaRepository &&
        user.apuntesPersonales.isNotEmpty) {
      await repo.hydrateNotesFromGitHub(
        institutionalEmail: user.email,
        apuntesPersonales: user.apuntesPersonales,
      );
    }
  }

  /// Registro instantáneo de compañero de Ingeniería Energética en GitHub.
  Future<String?> register({
    required String userOrEmail,
    required String nombre,
    required String pin,
    int cuatrimestre = 2,
  }) async {
    final starterCodes = _starterCodesForCuatrimestre(cuatrimestre);
    final result = await _syncService.registerStudent(
      rawUserOrEmail: userOrEmail,
      nombre: nombre,
      pin: pin,
      cuatrimestreActual: cuatrimestre,
      starterSubjectCodes: starterCodes,
    );
    if (result.error != null || result.user == null) {
      return result.error ?? 'No se pudo completar el registro.';
    }
    await _activateUser(result.user!);
    notifyListeners();
    return null;
  }

  /// Inicio de sesión simple contra `db/users/{username}.json` con persistencia permanente.
  Future<String?> login({
    required String userOrEmail,
    required String pin,
  }) async {
    final result = await _syncService.loginStudent(
      rawUserOrEmail: userOrEmail,
      pin: pin,
    );
    if (result.error != null || result.user == null) {
      return result.error ?? 'No se pudo iniciar sesión.';
    }
    await _activateUser(result.user!);
    notifyListeners();
    return null;
  }

  /// Cierra la sesión actual para cambiar de estudiante.
  Future<void> logout() async {
    _currentUser = null;
    await _syncService.clearActiveSession();
    notifyListeners();
  }

  List<String> _starterCodesForCuatrimestre(int cuatrimestre) {
    final subjects =
        _curriculumService?.database?.byCuatrimestre(cuatrimestre) ??
            const <AsignaturaModel>[];
    if (subjects.isNotEmpty) {
      return subjects.map((s) => s.codigo).toList(growable: false);
    }
    return const ['02021810', '03041819'];
  }

  /// Compatibilidad para actualización directa de correo institucional.
  Future<String?> updateInstitutionalEmail(String candidateEmail) async {
    final error = InstitutionalValidator.validateEmailOrError(candidateEmail);
    if (error != null) return error;

    final clean = candidateEmail.trim().toLowerCase();
    _fallbackEmail = clean;
    _repository.updateActiveUser(clean);

    if (_currentUser != null) {
      final newUsername = clean.split('@').first;
      final updated = _currentUser!.copyWith(
        username: newUsername,
        email: clean,
      );
      _currentUser = updated;
      notifyListeners();
      await _syncService.saveOptimisticAndSync(updated);
      return null;
    }

    notifyListeners();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_legacyEmailPrefsKey, clean);
    return null;
  }

  /// Suma puntos de cupo diario (`+ Mérito` o bloques completados) en 0 ms.
  Future<void> addUsageQuota(int delta) async {
    if (_currentUser != null) {
      final max = _currentUser!.usoDiario.maximo;
      final next = (_currentUser!.usoDiario.actual + delta).clamp(0, max);
      if (next == _currentUser!.usoDiario.actual) return;

      final updated = _currentUser!.copyWith(
        usoDiario: _currentUser!.usoDiario.copyWith(
          actual: next,
          ultimaFecha: DailyUsageModel.todayIso(),
        ),
      );
      _currentUser = updated;
      notifyListeners();
      await _syncService.saveOptimisticAndSync(updated);
      return;
    }

    final next = (_fallbackUsage + delta).clamp(0, AppConstants.maxDailyUsage);
    if (next == _fallbackUsage) return;
    _fallbackUsage = next;
    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    await prefs.setInt(_legacyUsagePrefsKey, _fallbackUsage);
  }

  /// Cambia el cuatrimestre activo del estudiante y lo sincroniza.
  Future<void> setCuatrimestreActual(int cuatrimestre) async {
    final user = _currentUser;
    if (user == null) return;
    final clamped = cuatrimestre.clamp(1, 12);
    if (user.cuatrimestreActual == clamped) return;

    final updated = user.copyWith(cuatrimestreActual: clamped);
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Obtiene el progreso `0..100` de una asignatura.
  int subjectProgress(String codigo) => progresoMaterias[codigo] ?? 0;

  /// Determina si una asignatura pertenece a "Mis Materias" del estudiante.
  bool isMySubject(AsignaturaModel asignatura) {
    if (progresoMaterias.containsKey(asignatura.codigo)) return true;
    return asignatura.cuatrimestre == cuatrimestreActual;
  }

  /// Actualiza el porcentaje de avance de una asignatura (`0..100`) en 0 ms.
  Future<void> updateSubjectProgress(String codigo, int percent) async {
    final user = _currentUser;
    if (user == null) return;
    final nextMap = Map<String, int>.from(user.progresoMaterias);
    nextMap[codigo] = percent.clamp(0, 100);
    final updated = user.copyWith(progresoMaterias: nextMap);
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Fija o desfija una asignatura dentro de `progreso_materias` ("Mis Materias").
  Future<bool> togglePinnedSubject(String codigo) async {
    final user = _currentUser;
    if (user == null) return false;
    final nextMap = Map<String, int>.from(user.progresoMaterias);
    late final bool pinned;
    if (nextMap.containsKey(codigo)) {
      nextMap.remove(codigo);
      pinned = false;
    } else {
      nextMap[codigo] = 15;
      pinned = true;
    }
    final updated = user.copyWith(progresoMaterias: nextMap);
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
    return pinned;
  }

  /// Completa un bloque de estudio: suma `+2` al Uso Diario y avanza el progreso
  /// de la asignatura vinculada en 0 ms con sincronización en segundo plano.
  Future<void> completeStudyBlock({
    String? codigoMateria,
    int usageBonus = 2,
    int progressDelta = 10,
  }) async {
    final user = _currentUser;
    if (user == null) {
      await addUsageQuota(usageBonus);
      return;
    }

    final max = user.usoDiario.maximo;
    final nextUsage = (user.usoDiario.actual + usageBonus).clamp(0, max);
    final nextMap = Map<String, int>.from(user.progresoMaterias);
    if (codigoMateria != null && codigoMateria.isNotEmpty) {
      final currentPct = nextMap[codigoMateria] ?? 0;
      nextMap[codigoMateria] = (currentPct + progressDelta).clamp(0, 100);
    }

    final updated = user.copyWith(
      usoDiario: user.usoDiario.copyWith(
        actual: nextUsage,
        ultimaFecha: DailyUsageModel.todayIso(),
      ),
      progresoMaterias: nextMap,
    );
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Crea un recordatorio personal en el calendario (0 ms local + PUT GitHub).
  Future<void> addCalendarReminder({
    required String titulo,
    required String subtitulo,
    required String fechaIso,
    required String hora,
    required AcademicEventKind tipo,
    String? codigoMateria,
  }) async {
    final user = _currentUser;
    if (user == null) return;

    final reminder = CalendarReminderModel(
      id: 'rem_${DateTime.now().microsecondsSinceEpoch}',
      titulo: titulo.trim(),
      subtitulo: subtitulo.trim(),
      fechaIso: fechaIso,
      hora: hora,
      tipo: tipo,
      codigoMateria: codigoMateria,
    );

    final nextList = [
      ...user.recordatoriosCalendario,
      reminder,
    ];
    final updated = user.copyWith(recordatoriosCalendario: nextList);
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Alterna el estado completado de un recordatorio (si es bloque suma Uso Diario).
  Future<void> toggleReminderCompleted(String reminderId) async {
    final user = _currentUser;
    if (user == null) return;

    var giveBonus = false;
    String? bonusSubject;
    final nextList = user.recordatoriosCalendario.map((r) {
      if (r.id != reminderId) return r;
      final nowDone = !r.completado;
      if (nowDone && r.tipo == AcademicEventKind.bloque) {
        giveBonus = true;
        bonusSubject = r.codigoMateria;
      }
      return r.copyWith(completado: nowDone);
    }).toList();

    var nextUso = user.usoDiario;
    final nextProg = Map<String, int>.from(user.progresoMaterias);
    if (giveBonus) {
      nextUso = nextUso.copyWith(
        actual: (nextUso.actual + 2).clamp(0, nextUso.maximo),
        ultimaFecha: DailyUsageModel.todayIso(),
      );
      if (bonusSubject != null && bonusSubject!.isNotEmpty) {
        nextProg[bonusSubject!] = ((nextProg[bonusSubject!] ?? 0) + 10).clamp(
          0,
          100,
        );
      }
    }

    final updated = user.copyWith(
      recordatoriosCalendario: nextList,
      usoDiario: nextUso,
      progresoMaterias: nextProg,
    );
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Elimina un recordatorio personal del calendario (0 ms local + PUT GitHub).
  Future<void> deleteCalendarReminder(String reminderId) async {
    final user = _currentUser;
    if (user == null) return;

    final nextList = user.recordatoriosCalendario
        .where((r) => r.id != reminderId)
        .toList();
    final updated = user.copyWith(recordatoriosCalendario: nextList);
    _currentUser = updated;
    notifyListeners();
    await _syncService.saveOptimisticAndSync(updated);
  }

  /// Sincroniza el texto de apuntes personales de un tema en `apuntes_personales`.
  void syncPersonalNote(String temaId, String contenido) {
    final user = _currentUser;
    if (user == null) return;

    final nextNotes = Map<String, dynamic>.from(user.apuntesPersonales);
    if (contenido.trim().isEmpty) {
      nextNotes.remove(temaId);
    } else {
      nextNotes[temaId] = contenido;
    }

    final updated = user.copyWith(apuntesPersonales: nextNotes);
    _currentUser = updated;
    unawaited(_syncService.saveOptimisticAndSync(updated));
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
      context.dependOnInheritedWidgetOfExactType<SessionScope>()?.notifier;

  static InstitutionalSessionController of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<SessionScope>()!.notifier!;
}
