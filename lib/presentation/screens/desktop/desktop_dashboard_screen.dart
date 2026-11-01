import 'package:flutter/material.dart';

import '../../../core/theme/app_theme.dart';
import '../../../data/models/curriculum_models.dart';
import '../../../data/models/student_user_model.dart';
import '../../../data/services/markdown_curriculum_service.dart';
import '../../../domain/entities/subject_summary.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';
import 'widgets/desktop_focus_timer.dart';
import 'widgets/desktop_live_clock.dart';
import 'widgets/desktop_news_feed.dart';
import 'widgets/desktop_sidebar.dart';

/// Pantalla completa de escritorio (Command Center / Ambient Dashboard)
/// activada cuando `constraints.maxWidth >= 1024`.
///
/// Ocupa el 100vw × 100vh sin scroll global parásito, con fondo OLED `#000000`
/// y gradiente radial sutil, animaciones de entrada escalonadas y distribución
/// simétrica de 3 columnas (25% | 45% | 30%).
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
  late final AnimationController _staggerController;
  late final Animation<double> _col1Opacity;
  late final Animation<Offset> _col1Slide;
  late final Animation<double> _col2Opacity;
  late final Animation<Offset> _col2Slide;
  late final Animation<double> _col3Opacity;
  late final Animation<Offset> _col3Slide;

  @override
  void initState() {
    super.initState();
    _staggerController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 550),
    );

    // Columna 1 (0ms - 350ms)
    _col1Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.0, 0.65, curve: Curves.easeOutCubic),
    );
    _col1Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.05),
      end: Offset.zero,
    ).animate(_col1Opacity);

    // Columna 2 (80ms - 450ms)
    _col2Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.15, 0.80, curve: Curves.easeOutCubic),
    );
    _col2Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.05),
      end: Offset.zero,
    ).animate(_col2Opacity);

    // Columna 3 (160ms - 550ms)
    _col3Opacity = CurvedAnimation(
      parent: _staggerController,
      curve: const Interval(0.30, 1.0, curve: Curves.easeOutCubic),
    );
    _col3Slide = Tween<Offset>(
      begin: const Offset(0.0, 0.05),
      end: Offset.zero,
    ).animate(_col3Opacity);

    _staggerController.forward();
  }

  @override
  void dispose() {
    _staggerController.dispose();
    super.dispose();
  }

  List<AsignaturaModel> _resolveActiveSubjects(
    InstitutionalSessionController? session,
    MarkdownCurriculumService? curriculum,
  ) {
    final db = curriculum?.database;
    if (db == null || db.allAsignaturas.isEmpty) return const [];

    final cuat = session?.cuatrimestreActual ?? 2;
    final subjects = db.byCuatrimestre(cuat);
    if (subjects.isNotEmpty) return subjects;

    return db.allAsignaturas.take(6).toList();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.sizeOf(context);
    final session = SessionScope.maybeOf(context);
    final curriculum = CurriculumScope.maybeOf(context);
    final activeSubjects = _resolveActiveSubjects(session, curriculum);

    // Resolver el próximo parcial oficial / hito
    final userReminders = session?.reminders ?? const <CalendarReminderModel>[];
    CalendarReminderModel? nextExam;
    for (final r in userReminders) {
      if (r.tipo == AcademicEventKind.parcial && !r.completado) {
        nextExam = r;
        break;
      }
    }

    final leadSubject = activeSubjects.isNotEmpty ? activeSubjects.first : null;
    final examTitle = nextExam?.titulo ??
        (leadSubject != null
            ? 'Primer Parcial Oficial: ${leadSubject.nombre}'
            : 'Primer Parcial Oficial de Cátedra');
    final examSubjectCode = nextExam?.codigoMateria ?? leadSubject?.codigo ?? '02021810';
    final examLocation = nextExam?.subtitulo.isNotEmpty == true
        ? nextExam!.subtitulo
        : 'Edificio Mar Caribe • Salón 304';
    final examDateText = nextExam != null
        ? '${nextExam.fechaIso} • ${nextExam.hora}'
        : 'En 3 días • 08:00 - 10:00 AM';

    return SizedBox(
      width: size.width,
      height: size.height,
      child: DecoratedBox(
        decoration: const BoxDecoration(
          color: Color(0xFF000000),
          gradient: RadialGradient(
            center: Alignment.center,
            radius: 1.25,
            colors: [
              Color(0xFF090B10),
              Color(0xFF000000),
            ],
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(22),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // 1. Columna Izquierda (25% del ancho): "Sidebar & Métricas"
              Expanded(
                flex: 25,
                child: FadeTransition(
                  opacity: _col1Opacity,
                  child: SlideTransition(
                    position: _col1Slide,
                    child: DesktopSidebar(
                      activeSubjects: activeSubjects,
                      onOpenClaseViva: widget.onOpenClaseViva,
                      onOpenTemario: widget.onOpenTemario,
                      onOpenStudentProfile: widget.onOpenStudentProfile,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 18),

              // 2. Columna Central (45% del ancho): "Hero: Reloj, Hito & Pomodoro"
              Expanded(
                flex: 45,
                child: FadeTransition(
                  opacity: _col2Opacity,
                  child: SlideTransition(
                    position: _col2Slide,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        // Reloj Digital Aislado
                        const DesktopLiveClock(),
                        const SizedBox(height: 18),

                        // Tarjeta de Estado Diario (Próximo Hito)
                        _DesktopNextMilestoneBanner(
                          title: examTitle,
                          subjectCode: examSubjectCode,
                          location: examLocation,
                          dateText: examDateText,
                          onEnterClaseViva: () =>
                              widget.onOpenClaseViva(examSubjectCode),
                        ),
                        const SizedBox(height: 18),

                        // Pomodoro / Bloque de Enfoque Integrado
                        Expanded(
                          child: DesktopFocusTimer(
                            activeSubjects: activeSubjects,
                            onOpenClaseViva: widget.onOpenClaseViva,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 18),

              // 3. Columna Derecha (30% del ancho): "Noticias y Avisos"
              Expanded(
                flex: 30,
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
    );
  }
}

class _DesktopNextMilestoneBanner extends StatelessWidget {
  const _DesktopNextMilestoneBanner({
    required this.title,
    required this.subjectCode,
    required this.location,
    required this.dateText,
    required this.onEnterClaseViva,
  });

  final String title;
  final String subjectCode;
  final String location;
  final String dateText;
  final VoidCallback onEnterClaseViva;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      decoration: BoxDecoration(
        color: const Color(0xDC0D0E12),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: const Color(0xFFFF9F0A).o(0.35),
          width: 1.2,
        ),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFFFF9F0A).o(0.08),
            blurRadius: 18,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: const Color(0xFFFF9F0A).o(0.14),
              shape: BoxShape.circle,
            ),
            child: const Icon(
              Icons.event_available_rounded,
              size: 22,
              color: Color(0xFFFF9F0A),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  children: [
                    const Dot(color: Color(0xFFFF9F0A), size: 6.5),
                    const SizedBox(width: 6),
                    Expanded(
                      child: Text(
                        'PRÓXIMO HITO OFICIAL DE CÁTEDRA',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: mono(
                          fontSize: 10,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 0.9,
                          color: const Color(0xFFFF9F0A),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  title,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(
                    fontSize: 14.5,
                    fontWeight: FontWeight.w700,
                    letterSpacing: -0.2,
                    color: Colors.white,
                  ),
                ),
                const SizedBox(height: 3),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(
                          Icons.location_on_outlined,
                          size: 13,
                          color: p.textTertiary,
                        ),
                        const SizedBox(width: 4),
                        Expanded(
                          child: Text(
                            location,
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(
                              fontSize: 11,
                              color: p.textSecondary,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 3),
                    Row(
                      children: [
                        Icon(
                          Icons.schedule_rounded,
                          size: 13,
                          color: p.textTertiary,
                        ),
                        const SizedBox(width: 4),
                        Expanded(
                          child: Text(
                            dateText,
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 10.5,
                              color: p.textSecondary,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(width: 14),
          MouseRegion(
            cursor: SystemMouseCursors.click,
            child: TapScale(
              onTap: onEnterClaseViva,
              child: Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 14,
                  vertical: 10,
                ),
                decoration: BoxDecoration(
                  color: const Color(0xFFFF9F0A),
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFFFF9F0A).o(0.30),
                      blurRadius: 10,
                      offset: const Offset(0, 3),
                    ),
                  ],
                ),
                child: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      Icons.play_arrow_rounded,
                      size: 16,
                      color: Colors.black,
                    ),
                    SizedBox(width: 6),
                    Text(
                      'La Clase Viva',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: Colors.black,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
