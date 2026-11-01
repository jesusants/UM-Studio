import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

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
import 'widgets/desktop_subject_detail_view.dart';

/// Pantalla completa de escritorio (Command Center / Ambient Dashboard)
/// activada cuando `constraints.maxWidth >= 1024`.
///
/// Características clave:
/// - Fija a 100vw × 100vh sin scrollbars globales parásitos.
/// - Soporte bidireccional nativo para Modo Oscuro OLED y Modo Claro.
/// - Navegación Maestro-Detalle continua (al pulsar una materia en la barra lateral,
///   la columna central pasa a detalle panorámico con visores KaTeX/Slides).
/// - Atajos de teclado físicos (`T` tema, `F` fullscreen, `Espacio` timer, `Esc` volver).
/// - Cero referencias a "Uso Diario" o cuotas de IA.
class DesktopDashboardScreen extends StatefulWidget {
  const DesktopDashboardScreen({
    super.key,
    required this.onOpenStudentProfile,
    required this.onOpenClaseViva,
    required this.onOpenTemario,
  });

  final VoidCallback onOpenStudentProfile;
  final ValueChanged<String> onOpenClaseViva;
  final ValueChanged<AsignaturaModel> onOpenTemario;

  @override
  State<DesktopDashboardScreen> createState() => _DesktopDashboardScreenState();
}

class _DesktopDashboardScreenState extends State<DesktopDashboardScreen>
    with SingleTickerProviderStateMixin {
  final GlobalKey<DesktopFocusTimerState> _timerKey =
      GlobalKey<DesktopFocusTimerState>();

  late final AnimationController _staggerController;
  late final Animation<double> _col1Opacity;
  late final Animation<Offset> _col1Slide;
  late final Animation<double> _col2Opacity;
  late final Animation<Offset> _col2Slide;
  late final Animation<double> _col3Opacity;
  late final Animation<Offset> _col3Slide;

  int _selectedCuatrimestre = 2;
  AsignaturaModel? _selectedSubject;

  @override
  void initState() {
    super.initState();
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
    if (session != null && session.cuatrimestreActual != _selectedCuatrimestre) {
      _selectedCuatrimestre = session.cuatrimestreActual;
    }
  }

  @override
  void dispose() {
    _staggerController.dispose();
    super.dispose();
  }

  List<AsignaturaModel> _resolveSubjectsForCuatrimestre(
    MarkdownCurriculumService? curriculum,
    int cuat,
  ) {
    final db = curriculum?.database;
    if (db == null || db.allAsignaturas.isEmpty) return const [];
    return db.byCuatrimestre(cuat);
  }

  KeyEventResult _handleKeyEvent(FocusNode node, KeyEvent event) {
    if (event is KeyDownEvent) {
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

      // Esc: Volver al Dashboard si hay una materia seleccionada
      if (event.logicalKey == LogicalKeyboardKey.escape) {
        if (_selectedSubject != null) {
          setState(() => _selectedSubject = null);
          return KeyEventResult.handled;
        }
      }

      // Espacio: Iniciar / Pausar temporizador Pomodoro
      if (event.logicalKey == LogicalKeyboardKey.space) {
        if (_selectedSubject == null && _timerKey.currentState != null) {
          _timerKey.currentState?.togglePlayPause();
          return KeyEventResult.handled;
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
    final examDateText = nextExam != null
        ? '${nextExam.fechaIso} • ${nextExam.hora}'
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
                          setState(() => _selectedSubject = subject);
                        },
                        onOpenStudentProfile: widget.onOpenStudentProfile,
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
                                  const DesktopLiveClock(),
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

                                  // Bloque de Enfoque Pomodoro
                                  Expanded(
                                    child: DesktopFocusTimer(
                                      key: _timerKey,
                                      activeSubjects: cuatSubjects,
                                      onOpenClaseViva: (code) {
                                        final matched = cuatSubjects.firstWhere(
                                          (s) => s.codigo == code,
                                          orElse: () => leadSubject ?? cuatSubjects.first,
                                        );
                                        setState(() => _selectedSubject = matched);
                                      },
                                    ),
                                  ),
                                ],
                              )
                            // Modo B: Detalle de Materia Panorámico (Master-Detail)
                            : DesktopSubjectDetailView(
                                key: ValueKey('detail_${_selectedSubject!.codigo}'),
                                subject: _selectedSubject!,
                                onBackToDashboard: () {
                                  setState(() => _selectedSubject = null);
                                },
                                onOpenClaseViva: widget.onOpenClaseViva,
                              ),
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
