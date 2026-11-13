import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../../core/theme/app_theme.dart';
import '../../../core/utils/fullscreen/fullscreen_helper.dart';
import '../../../data/models/curriculum_models.dart';
import '../../../data/models/student_user_model.dart';
import '../../../data/services/markdown_curriculum_service.dart';
import '../../../domain/entities/subject_summary.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';
import 'desktop_theme_tokens.dart';
import 'widgets/desktop_focus_timer.dart';
import 'widgets/desktop_live_clock.dart';
import 'widgets/desktop_news_feed.dart';
import 'widgets/desktop_sidebar.dart';
import 'widgets/desktop_spotlight_search.dart';
import 'widgets/desktop_subject_detail_view.dart';

/// Pantalla completa de escritorio (Command Center / Ambient Dashboard)
/// activada cuando `constraints.maxWidth >= 1024`.
///
/// Características clave:
/// - Fija a 100vw × 100vh sin scrollbars globales parásitos.
/// - Soporte bidireccional nativo para Modo Oscuro OLED y Modo Claro.
/// - Navegación Maestro-Detalle continua (al pulsar una materia en la barra lateral,
///   la columna central pasa a detalle panorámico con visores KaTeX/Slides).
/// - Atajos de teclado físicos (`T` tema, `F` fullscreen, `P` temporizador, `Espacio` timer, `Esc` volver).
/// - Cero referencias a "Uso Diario" o cuotas de IA.
class DesktopDashboardScreen extends StatefulWidget {
  const DesktopDashboardScreen({
    super.key,
    required this.onOpenStudentProfile,
    required this.onOpenClaseViva,
    required this.onOpenTemario,
    this.onOpenMiCuatrimestre,
  });

  final VoidCallback onOpenStudentProfile;
  final ValueChanged<String> onOpenClaseViva;
  final ValueChanged<AsignaturaModel> onOpenTemario;
  final VoidCallback? onOpenMiCuatrimestre;

  @override
  State<DesktopDashboardScreen> createState() => _DesktopDashboardScreenState();
}

class _DesktopDashboardScreenState extends State<DesktopDashboardScreen>
    with SingleTickerProviderStateMixin {
  final GlobalKey<DesktopFocusTimerState> _timerKey =
      GlobalKey<DesktopFocusTimerState>();

  static const String _kShowTimerPrefKey = 'desktop_show_focus_timer';
  bool _showFocusTimer = true;

  Future<void> _loadTimerVisibility() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final show = prefs.getBool(_kShowTimerPrefKey);
      if (show != null && mounted) {
        setState(() => _showFocusTimer = show);
      }
    } catch (_) {}
  }

  Future<void> _setTimerVisibility(bool visible) async {
    HapticFeedback.lightImpact();
    setState(() => _showFocusTimer = visible);
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool(_kShowTimerPrefKey, visible);
    } catch (_) {}
  }

  late final AnimationController _staggerController;
  late final Animation<double> _col1Opacity;
  late final Animation<Offset> _col1Slide;
  late final Animation<double> _col2Opacity;
  late final Animation<Offset> _col2Slide;
  late final Animation<double> _col3Opacity;
  late final Animation<Offset> _col3Slide;

  int _selectedCuatrimestre = 2;
  AsignaturaModel? _selectedSubject;
  int? _initialTemaNumero;
  bool _initialMagistral = false;

  Future<void> _openSpotlight(MarkdownCurriculumService? curriculum) async {
    final hit = await DesktopSpotlightSearch.show(
      context,
      curriculum: curriculum,
    );
    if (hit == null || !mounted) return;
    setState(() {
      _selectedSubject = hit.subject;
      _initialTemaNumero = hit.temaNumero;
      _initialMagistral = hit.isMagistral;
    });
  }

  @override
  void initState() {
    super.initState();
    _loadTimerVisibility();
    _staggerController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 550),
    );

    _col1Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.0, 0.65, curve: Curves.easeOutCubic),
    );
    _col1Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.04),
      end: Offset.zero,
    ).animate(_col1Opacity);

    _col2Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.15, 0.80, curve: Curves.easeOutCubic),
    );
    _col2Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.04),
      end: Offset.zero,
    ).animate(_col2Opacity);

    _col3Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.30, 1.0, curve: Curves.easeOutCubic),
    );
    _col3Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.04),
      end: Offset.zero,
    ).animate(_col3Opacity);

    _staggerController.forward();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final session = SessionScope.maybeOf(context);
    if (session != null) {
      if (session.hasMatriculaConfigured && _selectedCuatrimestre != 0) {
        _selectedCuatrimestre = 0;
      } else if (!session.hasMatriculaConfigured && _selectedCuatrimestre == 0) {
        _selectedCuatrimestre = session.cuatrimestreActivo;
      }
    }
  }

  @override
  void dispose() {
    _staggerController.dispose();
    super.dispose();
  }

  List<AsignaturaModel> _resolveSubjectsForCuatrimestre(
    MarkdownCurriculumService? curriculum,
    InstitutionalSessionController? session,
    int cuat,
  ) {
    final db = curriculum?.database;
    if (db == null || db.allAsignaturas.isEmpty) return const [];
    if (cuat == 0) {
      if (session != null && session.hasMatriculaConfigured) {
        final enrolled = session.materiasMatriculadas
            .map((c) => db.findAsignatura(c))
            .whereType<AsignaturaModel>()
            .toList();
        if (enrolled.isNotEmpty) return enrolled;
      }
      return db.byCuatrimestre(session?.cuatrimestreActivo ?? 1);
    }
    return db.byCuatrimestre(cuat);
  }

  KeyEventResult _handleKeyEvent(FocusNode node, KeyEvent event) {
    if (event is KeyDownEvent) {
      final isCtrlOrCmd = HardwareKeyboard.instance.isControlPressed ||
          HardwareKeyboard.instance.isMetaPressed;
      final isAlt = HardwareKeyboard.instance.isAltPressed;

      // Ctrl+K / Cmd+K: Buscador Spotlight Global
      if (isCtrlOrCmd && event.logicalKey == LogicalKeyboardKey.keyK) {
        final curriculum = CurriculumScope.maybeOf(context);
        _openSpotlight(curriculum);
        return KeyEventResult.handled;
      }

      final focusedWidget = FocusManager.instance.primaryFocus?.context?.widget;
      final isTyping = focusedWidget is EditableText;

      // Esc: Volver al Dashboard si hay una materia seleccionada
      if (event.logicalKey == LogicalKeyboardKey.escape) {
        if (_selectedSubject != null) {
          setState(() {
            _selectedSubject = null;
            _initialTemaNumero = null;
            _initialMagistral = false;
          });
          return KeyEventResult.handled;
        }
      }

      if (isTyping) return KeyEventResult.ignored;

      // Alt + 1..9: Cambiar rápidamente entre materias activas
      if (isAlt) {
        final digitMap = <LogicalKeyboardKey, int>{
          LogicalKeyboardKey.digit1: 0,
          LogicalKeyboardKey.digit2: 1,
          LogicalKeyboardKey.digit3: 2,
          LogicalKeyboardKey.digit4: 3,
          LogicalKeyboardKey.digit5: 4,
          LogicalKeyboardKey.digit6: 5,
          LogicalKeyboardKey.digit7: 6,
          LogicalKeyboardKey.digit8: 7,
          LogicalKeyboardKey.digit9: 8,
        };
        final idx = digitMap[event.logicalKey];
        if (idx != null) {
          final session = SessionScope.maybeOf(context);
          final curriculum = CurriculumScope.maybeOf(context);
          final subjects = _resolveSubjectsForCuatrimestre(
            curriculum,
            session,
            _selectedCuatrimestre,
          );
          if (idx < subjects.length) {
            setState(() {
              _selectedSubject = subjects[idx];
              _initialTemaNumero = null;
              _initialMagistral = false;
            });
            return KeyEventResult.handled;
          }
        }
      }

      // T: Alternar Modo Claro / Modo Oscuro
      if (event.logicalKey == LogicalKeyboardKey.keyT) {
        final themeController = ThemeScope.maybeOf(context);
        themeController?.toggle();
        return KeyEventResult.handled;
      }

      // F: Alternar pantalla completa nativa
      if (event.logicalKey == LogicalKeyboardKey.keyF) {
        FullscreenHelper.toggle();
        return KeyEventResult.handled;
      }

      // P: Alternar visibilidad del temporizador Pomodoro
      if (event.logicalKey == LogicalKeyboardKey.keyP) {
        if (_selectedSubject == null) {
          _setTimerVisibility(!_showFocusTimer);
          return KeyEventResult.handled;
        }
      }

      // Espacio: Iniciar / Pausar temporizador Pomodoro (o mostrar si estaba oculto)
      if (event.logicalKey == LogicalKeyboardKey.space) {
        if (_selectedSubject == null) {
          if (!_showFocusTimer) {
            _setTimerVisibility(true);
            return KeyEventResult.handled;
          }
          if (_timerKey.currentState != null) {
            _timerKey.currentState?.togglePlayPause();
            return KeyEventResult.handled;
          }
        }
      }

      // Teclas numéricas 1 a 4: Cambiar cuatrimestre rápido
      if (event.logicalKey == LogicalKeyboardKey.digit1) {
        setState(() => _selectedCuatrimestre = 1);
        return KeyEventResult.handled;
      }
      if (event.logicalKey == LogicalKeyboardKey.digit2) {
        setState(() => _selectedCuatrimestre = 2);
        return KeyEventResult.handled;
      }
      if (event.logicalKey == LogicalKeyboardKey.digit3) {
        setState(() => _selectedCuatrimestre = 3);
        return KeyEventResult.handled;
      }
      if (event.logicalKey == LogicalKeyboardKey.digit4) {
        setState(() => _selectedCuatrimestre = 4);
        return KeyEventResult.handled;
      }
    }
    return KeyEventResult.ignored;
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    final size = MediaQuery.sizeOf(context);
    final session = SessionScope.maybeOf(context);
    final curriculum = CurriculumScope.maybeOf(context);
    final cuatSubjects = _resolveSubjectsForCuatrimestre(
      curriculum,
      session,
      _selectedCuatrimestre,
    );

    // Próximo hito académico para el dashboard
    final userReminders = session?.reminders ?? const <CalendarReminderModel>[];
    CalendarReminderModel? nextExam;
    for (final r in userReminders) {
      if (r.tipo == AcademicEventKind.parcial && !r.completado) {
        nextExam = r;
        break;
      }
    }

    final leadSubject = cuatSubjects.isNotEmpty ? cuatSubjects.first : null;
    final examTitle = nextExam?.titulo ??
        (leadSubject != null
            ? 'Primer Parcial Oficial: ${leadSubject.nombre}'
            : 'Primer Parcial Oficial de Cátedra');
    final examSubjectCode =
        nextExam?.codigoMateria ?? leadSubject?.codigo ?? '02021810';
    final examLocation = nextExam?.subtitulo.isNotEmpty == true
        ? nextExam!.subtitulo
        : 'Edificio Mar Caribe • Salón 304';

    String countdownBadge(String fechaIso) {
      final now = DateTime.now();
      final today = DateTime(now.year, now.month, now.day);
      final target = DateTime.tryParse(fechaIso);
      if (target == null) return fechaIso;
      final cleanTarget = DateTime(target.year, target.month, target.day);
      final diff = cleanTarget.difference(today).inDays;
      if (diff <= 0) return 'Hoy';
      if (diff == 1) return 'Mañana';
      return 'En $diff días';
    }

    final examDateText = nextExam != null
        ? '${countdownBadge(nextExam.fechaIso)} • ${nextExam.hora}'
        : 'En 3 días • 08:00 - 10:00 AM';

    return Focus(
      autofocus: true,
      onKeyEvent: _handleKeyEvent,
      child: SizedBox(
        width: size.width,
        height: size.height,
        child: DecoratedBox(
          decoration: BoxDecoration(
            color: tokens.canvas,
            gradient: tokens.isDark
                ? const RadialGradient(
                    center: Alignment.center,
                    radius: 1.25,
                    colors: [
                      Color(0xFF090B10),
                      Color(0xFF000000),
                    ],
                  )
                : null,
          ),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // 1. Columna Izquierda (24% del ancho): "Navegador de Cátedra & Asignaturas"
                Expanded(
                  flex: 24,
                  child: FadeTransition(
                    opacity: _col1Opacity,
                    child: SlideTransition(
                      position: _col1Slide,
                      child: DesktopSidebar(
                        selectedCuatrimestre: _selectedCuatrimestre,
                        onSelectCuatrimestre: (c) {
                          setState(() {
                            _selectedCuatrimestre = c;
                            _selectedSubject = null;
                          });
                        },
                        subjects: cuatSubjects,
                        selectedSubject: _selectedSubject,
                        onSelectSubject: (subject) {
                          setState(() {
                            _selectedSubject = subject;
                            _initialTemaNumero = null;
                            _initialMagistral = false;
                          });
                        },
                        onOpenStudentProfile: widget.onOpenStudentProfile,
                        onEditMatricula: widget.onOpenMiCuatrimestre,
                        isTimerVisible: _showFocusTimer,
                        onToggleTimer: () => _setTimerVisibility(!_showFocusTimer),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 18),

                // 2. Columna Central (48% del ancho): "Hero Central / Maestro-Detalle"
                Expanded(
                  flex: 48,
                  child: FadeTransition(
                    opacity: _col2Opacity,
                    child: SlideTransition(
                      position: _col2Slide,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          // Píldora discreta de Buscador Rápido estilo Spotlight (Ctrl+K)
                          TapScale(
                            onTap: () => _openSpotlight(curriculum),
                            child: Container(
                              margin: const EdgeInsets.only(bottom: 12),
                              padding: const EdgeInsets.symmetric(
                                horizontal: 14,
                                vertical: 9,
                              ),
                              decoration: BoxDecoration(
                                color: tokens.surface,
                                borderRadius: BorderRadius.circular(14),
                                border: Border.all(color: tokens.border),
                              ),
                              child: Row(
                                children: [
                                  Icon(
                                    Icons.search_rounded,
                                    size: 16,
                                    color: tokens.textSecondary,
                                  ),
                                  const SizedBox(width: 9),
                                  Expanded(
                                    child: Text(
                                      'Buscar materia, tema o cátedra magistral...',
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                      style: TextStyle(
                                        fontSize: 12.5,
                                        color: tokens.textSecondary,
                                      ),
                                    ),
                                  ),
                                  Container(
                                    padding: const EdgeInsets.symmetric(
                                      horizontal: 7,
                                      vertical: 2.5,
                                    ),
                                    decoration: BoxDecoration(
                                      color: tokens.surfaceElevated,
                                      borderRadius: BorderRadius.circular(6),
                                      border: Border.all(color: tokens.border),
                                    ),
                                    child: Text(
                                      '⌘K / Ctrl+K',
                                      style: mono(
                                        fontSize: 9.5,
                                        fontWeight: FontWeight.w700,
                                        color: tokens.textTertiary,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                          Expanded(
                            child: AnimatedSwitcher(
                              duration: const Duration(milliseconds: 240),
                              switchInCurve: Curves.easeOutCubic,
                              switchOutCurve: Curves.easeInCubic,
                              child: _selectedSubject == null
                                  // Modo A: Dashboard General (Reloj + Próximo Hito + Pomodoro)
                                  ? Column(
                                      key: const ValueKey('desktop_mode_dashboard'),
                                      crossAxisAlignment: CrossAxisAlignment.stretch,
                                      children: [
                                        // Reloj Digital Aislado
                                        const RepaintBoundary(
                                          child: DesktopLiveClock(),
                                        ),
                                  const SizedBox(height: 16),

                                  // Próximo Hito Académico
                                  _DesktopNextMilestoneBanner(
                                    title: examTitle,
                                    subjectCode: examSubjectCode,
                                    location: examLocation,
                                    dateText: examDateText,
                                    tokens: tokens,
                                    onEnterClaseViva: () {
                                      final matched = cuatSubjects.firstWhere(
                                        (s) => s.codigo == examSubjectCode,
                                        orElse: () => leadSubject ?? cuatSubjects.first,
                                      );
                                      setState(() => _selectedSubject = matched);
                                    },
                                  ),
                                  const SizedBox(height: 16),

                                  // Bloque de Enfoque Pomodoro O Vista Alternativa Oculta
                                  Expanded(
                                    child: AnimatedSwitcher(
                                      duration: const Duration(milliseconds: 240),
                                      switchInCurve: Curves.easeOutCubic,
                                      switchOutCurve: Curves.easeInCubic,
                                      child: _showFocusTimer
                                          ? RepaintBoundary(
                                              child: DesktopFocusTimer(
                                                key: _timerKey,
                                                activeSubjects: cuatSubjects,
                                                onHideTimer: () =>
                                                    _setTimerVisibility(false),
                                                onOpenClaseViva: (code) {
                                                  final matched =
                                                      cuatSubjects.firstWhere(
                                                    (s) => s.codigo == code,
                                                    orElse: () => leadSubject ??
                                                        cuatSubjects.first,
                                                  );
                                                  setState(() =>
                                                      _selectedSubject = matched);
                                                },
                                              ),
                                            )
                                          : _DesktopTimerHiddenCard(
                                              key: const ValueKey('desktop_timer_hidden_card'),
                                              tokens: tokens,
                                              subjects: cuatSubjects,
                                              reminders: userReminders,
                                              onShowTimer: () => _setTimerVisibility(true),
                                              onSelectSubject: (subject) {
                                                setState(() => _selectedSubject = subject);
                                              },
                                            ),
                                    ),
                                  ),
                                ],
                              )
                            // Modo B: Detalle de Materia Panorámico (Master-Detail)
                            : DesktopSubjectDetailView(
                                key: ValueKey('detail_${_selectedSubject!.codigo}'),
                                subject: _selectedSubject!,
                                initialTemaNumero: _initialTemaNumero,
                                initialMagistral: _initialMagistral,
                                onBackToDashboard: () {
                                  setState(() {
                                    _selectedSubject = null;
                                    _initialTemaNumero = null;
                                    _initialMagistral = false;
                                  });
                                },
                                onOpenClaseViva: widget.onOpenClaseViva,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 18),

                // 3. Columna Derecha (28% del ancho): "Tablón Institucional & Noticias"
                Expanded(
                  flex: 28,
                  child: FadeTransition(
                    opacity: _col3Opacity,
                    child: SlideTransition(
                      position: _col3Slide,
                      child: const DesktopNewsFeed(),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _DesktopNextMilestoneBanner extends StatelessWidget {
  const _DesktopNextMilestoneBanner({
    required this.title,
    required this.subjectCode,
    required this.location,
    required this.dateText,
    required this.tokens,
    required this.onEnterClaseViva,
  });

  final String title;
  final String subjectCode;
  final String location;
  final String dateText;
  final DesktopThemeTokens tokens;
  final VoidCallback onEnterClaseViva;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
      decoration: BoxDecoration(
        color: tokens.surface,
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: tokens.alertAmber.o(0.35),
          width: 1.2,
        ),
        boxShadow: [
          BoxShadow(
            color: tokens.alertAmber.o(0.08),
            blurRadius: 16,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: tokens.alertAmber.o(0.14),
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.event_available_rounded,
              size: 20,
              color: tokens.alertAmber,
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  children: [
                    Dot(color: tokens.alertAmber, size: 6),
                    const SizedBox(width: 6),
                    Expanded(
                      child: Text(
                        'PRÓXIMO HITO OFICIAL DE CÁTEDRA',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: mono(
                          fontSize: 9.5,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 0.9,
                          color: tokens.alertAmber,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 3),
                Text(
                  title,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w700,
                    letterSpacing: -0.2,
                    color: tokens.textPrimary,
                  ),
                ),
                const SizedBox(height: 3),
                Row(
                  children: [
                    Icon(
                      Icons.schedule_rounded,
                      size: 12,
                      color: tokens.textSecondary,
                    ),
                    const SizedBox(width: 4),
                    Text(
                      dateText,
                      style: mono(
                        fontSize: 10,
                        color: tokens.textSecondary,
                      ),
                    ),
                    const SizedBox(width: 10),
                    Icon(
                      Icons.place_outlined,
                      size: 12,
                      color: tokens.textSecondary,
                    ),
                    const SizedBox(width: 4),
                    Expanded(
                      child: Text(
                        location,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          fontSize: 10.5,
                          color: tokens.textSecondary,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(width: 10),
          TapScale(
            onTap: onEnterClaseViva,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 8),
              decoration: BoxDecoration(
                color: tokens.alertAmber,
                borderRadius: BorderRadius.circular(10),
              ),
              child: const Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    'Ver Temas',
                    style: TextStyle(
                      fontSize: 11.5,
                      fontWeight: FontWeight.w700,
                      color: Colors.white,
                    ),
                  ),
                  SizedBox(width: 4),
                  Icon(
                    Icons.chevron_right_rounded,
                    size: 14,
                    color: Colors.white,
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}


/// Tarjeta de modo ambiente y estudio mostrada cuando el usuario oculta el temporizador Pomodoro.
/// Mantiene balance estético en la columna central, da acceso a asignaturas y permite restaurar el temporizador.
class _DesktopTimerHiddenCard extends StatelessWidget {
  const _DesktopTimerHiddenCard({
    super.key,
    required this.tokens,
    required this.subjects,
    required this.reminders,
    required this.onShowTimer,
    required this.onSelectSubject,
  });

  final DesktopThemeTokens tokens;
  final List<AsignaturaModel> subjects;
  final List<CalendarReminderModel> reminders;
  final VoidCallback onShowTimer;
  final ValueChanged<AsignaturaModel> onSelectSubject;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: tokens.surface,
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: tokens.border, width: 1),
        boxShadow: [
          BoxShadow(
            color: tokens.shadowColor,
            blurRadius: 18,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Encabezado con estado y acción de restauración
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(7),
                decoration: BoxDecoration(
                  color: tokens.accentIndigo.o(0.14),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(
                  Icons.timer_off_outlined,
                  size: 16,
                  color: tokens.accentIndigo,
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  physics: const NeverScrollableScrollPhysics(),
                  clipBehavior: Clip.antiAlias,
                  child: Row(
                    children: [
                      Text(
                        'TEMPORIZADOR OCULTO',
                        maxLines: 1,
                        style: mono(
                          fontSize: 10.5,
                          fontWeight: FontWeight.w600,
                          letterSpacing: 0.8,
                          color: tokens.textSecondary,
                        ),
                      ),
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: tokens.accentGreen.o(0.12),
                          borderRadius: BorderRadius.circular(6),
                          border: Border.all(color: tokens.accentGreen.o(0.25)),
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Dot(color: tokens.accentGreen, size: 5),
                            const SizedBox(width: 4),
                            Text(
                              'Modo Ambiente & Estudio',
                              style: mono(
                                fontSize: 9,
                                fontWeight: FontWeight.w700,
                                color: tokens.accentGreen,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(width: 8),
              // Botón Restaurar / Mostrar Temporizador
              TapScale(
                onTap: onShowTimer,
                child: Tooltip(
                  message: 'Mostrar temporizador Pomodoro (P)',
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                    decoration: BoxDecoration(
                      color: tokens.accentIndigo.o(0.12),
                      borderRadius: BorderRadius.circular(9),
                      border: Border.all(color: tokens.accentIndigo.o(0.4)),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.timer_outlined,
                          size: 14,
                          color: tokens.accentIndigo,
                        ),
                        const SizedBox(width: 5),
                        Text(
                          'Mostrar temporizador',
                          style: TextStyle(
                            fontSize: 10.5,
                            fontWeight: FontWeight.w700,
                            color: tokens.accentIndigo,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),

          // Banner Zen descriptivo
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              color: tokens.surfaceElevated,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: tokens.borderSubtle),
            ),
            child: Row(
              children: [
                Icon(Icons.spa_outlined, size: 16, color: tokens.accentIndigo),
                const SizedBox(width: 10),
                Expanded(
                  child: Text(
                    'Espacio de estudio libre de distracciones. Selecciona una asignatura para explorar sus temas y clases vivas.',
                    style: TextStyle(
                      fontSize: 11,
                      color: tokens.textSecondary,
                      height: 1.35,
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  'Atajo: P',
                  style: mono(
                    fontSize: 10,
                    fontWeight: FontWeight.w600,
                    color: tokens.textTertiary,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),

          // Lista de asignaturas con temarios para estudio directo
          Expanded(
            child: subjects.isEmpty
                ? Center(
                    child: Text(
                      'No hay asignaturas disponibles en este cuatrimestre.',
                      style: TextStyle(fontSize: 12, color: tokens.textSecondary),
                    ),
                  )
                : ListView.separated(
                    physics: const BouncingScrollPhysics(),
                    itemCount: subjects.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 8),
                    itemBuilder: (context, index) {
                      final subject = subjects[index];
                      final color = _parseColor(subject.colorHex);
                      return Container(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                        decoration: BoxDecoration(
                          color: tokens.surfaceElevated,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: tokens.borderSubtle),
                        ),
                        child: Row(
                          children: [
                            Container(
                              width: 32,
                              height: 32,
                              decoration: BoxDecoration(
                                color: color.o(0.14),
                                borderRadius: BorderRadius.circular(8),
                                border: Border.all(color: color.o(0.35)),
                              ),
                              child: Center(
                                child: Text(
                                  subject.codigo.length >= 2
                                      ? subject.codigo.substring(subject.codigo.length - 2)
                                      : subject.codigo,
                                  style: mono(
                                    fontSize: 11,
                                    fontWeight: FontWeight.w800,
                                    color: color,
                                  ),
                                ),
                              ),
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Text(
                                    subject.nombre,
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: TextStyle(
                                      fontSize: 12.5,
                                      fontWeight: FontWeight.w700,
                                      color: tokens.textPrimary,
                                    ),
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    '${subject.temas.length} temas • ${subject.creditos} Créditos • ${subject.categoria}',
                                    style: mono(
                                      fontSize: 9.5,
                                      color: tokens.textSecondary,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(width: 10),
                            TapScale(
                              onTap: () => onSelectSubject(subject),
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                                decoration: BoxDecoration(
                                  color: color.o(0.12),
                                  borderRadius: BorderRadius.circular(8),
                                  border: Border.all(color: color.o(0.3)),
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Text(
                                      'Ver Temario',
                                      style: TextStyle(
                                        fontSize: 10.5,
                                        fontWeight: FontWeight.w700,
                                        color: color,
                                      ),
                                    ),
                                    const SizedBox(width: 4),
                                    Icon(
                                      Icons.arrow_forward_rounded,
                                      size: 12,
                                      color: color,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ],
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }

  static Color _parseColor(String hex) {
    final clean = hex.replaceAll('#', '');
    if (clean.length == 6) {
      return Color(int.parse('0xFF$clean'));
    }
    return const Color(0xFF5E5CE6);
  }
}
