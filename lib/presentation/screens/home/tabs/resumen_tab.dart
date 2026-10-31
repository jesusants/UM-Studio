import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../../data/models/student_user_model.dart';
import '../../../../data/services/markdown_curriculum_service.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../../widgets/reminder_creator_sheet.dart';

/// Pestaña 1: "Resumen de hoy" conectada al perfil del estudiante,
/// su calendario personal en GitHub y sus materias activas de Ing. Energética.
class ResumenTab extends StatelessWidget {
  const ResumenTab({
    super.key,
    required this.onOpenClaseViva,
    required this.onCompleteBlock,
  });

  final ValueChanged<String> onOpenClaseViva;
  final VoidCallback onCompleteBlock;

  String _todaySpanishLabel() {
    final now = DateTime.now();
    const weekdays = [
      'Lunes',
      'Martes',
      'Miércoles',
      'Jueves',
      'Viernes',
      'Sábado',
      'Domingo',
    ];
    const months = [
      'Ene',
      'Feb',
      'Mar',
      'Abr',
      'May',
      'Jun',
      'Jul',
      'Ago',
      'Sep',
      'Oct',
      'Nov',
      'Dic',
    ];
    return '${weekdays[now.weekday - 1]}, ${now.day} ${months[now.month - 1]}';
  }

  String _countdownBadge(String fechaIso) {
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

  AsignaturaModel? _resolveLeadSubject(
    InstitutionalSessionController? session,
    MarkdownCurriculumService? curriculum,
  ) {
    final db = curriculum?.database;
    if (db == null || db.allAsignaturas.isEmpty) return null;

    if (session != null) {
      for (final code in session.progresoMaterias.keys) {
        final found = db.findAsignatura(code);
        if (found != null) return found;
      }
      final semList = db.byCuatrimestre(session.cuatrimestreActual);
      if (semList.isNotEmpty) return semList.first;
    }
    return db.findAsignatura('02021810') ?? db.allAsignaturas.first;
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final curriculum = CurriculumScope.maybeOf(context);
    final reminders = session?.reminders ?? const <CalendarReminderModel>[];
    final todayIso = DailyUsageModel.todayIso();

    CalendarReminderModel? nextParcial;
    CalendarReminderModel? nextClaseOrBlock;
    for (final r in reminders) {
      if (r.completado) continue;
      if (r.fechaIso.compareTo(todayIso) < 0) continue;
      if (nextParcial == null &&
          (r.tipo == AcademicEventKind.parcial ||
              r.tipo == AcademicEventKind.entrega)) {
        nextParcial = r;
      }
      if (nextClaseOrBlock == null &&
          (r.tipo == AcademicEventKind.clase ||
              r.tipo == AcademicEventKind.bloque)) {
        nextClaseOrBlock = r;
      }
    }

    final leadSubject = _resolveLeadSubject(session, curriculum);
    final leadCode = leadSubject?.codigo ?? '02021810';
    final leadTitle = leadSubject?.nombre ?? 'Física Mecánica';
    final leadTopic =
        leadSubject?.primerTema.titulo ?? 'Leyes de Newton y Rozamiento';
    final leadBlock = leadSubject?.primerTema.bloqueSugerido ??
        'Pomodoro 50/10 • Diagramas de cuerpo libre con fricción';

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 26),
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.baseline,
          textBaseline: TextBaseline.alphabetic,
          children: [
            Expanded(
              child: Text(
                session != null && session.isAuthenticated
                    ? 'Hola, ${session.primerNombre}'
                    : 'Resumen de hoy',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 21,
                  fontWeight: FontWeight.w700,
                  letterSpacing: -0.4,
                  color: p.textPrimary,
                ),
              ),
            ),
            const SizedBox(width: 8),
            Text(
              _todaySpanishLabel(),
              style: TextStyle(fontSize: 12, color: p.textSecondary),
            ),
          ],
        ),
        const SizedBox(height: 16),

        // 1. Próximo parcial o recordatorio prioritario del estudiante
        TapScale(
          onTap: () {
            if (nextParcial != null && nextParcial.codigoMateria != null) {
              onOpenClaseViva(nextParcial.codigoMateria!);
            } else {
              showReminderCreatorSheet(
                context,
                initialKind: AcademicEventKind.parcial,
                preselectedSubject: leadSubject,
              );
            }
          },
          child: IosCard(
            borderColor: p.orange.o(0.4),
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [p.warmTop, p.card],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Expanded(
                      child: Text(
                        nextParcial?.tipo == AcademicEventKind.entrega
                            ? 'PRÓXIMA ENTREGA MOODLE'
                            : 'PRÓXIMO PARCIAL',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.w600,
                          letterSpacing: 0.6,
                          color: p.orange,
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 2,
                      ),
                      decoration: BoxDecoration(
                        color: p.orange.o(0.15),
                        borderRadius: BorderRadius.circular(999),
                        border: Border.all(color: p.orange.o(0.3)),
                      ),
                      child: Text(
                        nextParcial != null
                            ? '${_countdownBadge(nextParcial.fechaIso)} • ${nextParcial.hora}'
                            : 'Personalizable',
                        style: mono(fontSize: 11, color: p.orange),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  nextParcial != null
                      ? nextParcial.titulo
                      : 'Agenda tus parciales de este corte',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  nextParcial != null
                      ? nextParcial.subtitulo
                      : 'Toca aquí para guardar tu próximo parcial o entrega en tu calendario personal de GitHub.',
                  style: TextStyle(fontSize: 12, color: p.textSecondary),
                ),
                Container(
                  margin: const EdgeInsets.only(top: 12),
                  padding: const EdgeInsets.only(top: 10),
                  decoration: BoxDecoration(
                    border: Border(top: BorderSide(color: p.cardBorder)),
                  ),
                  child: Row(
                    children: [
                      Expanded(
                        child: Text(
                          nextParcial != null
                              ? 'Meta sugerida según AyRe:'
                              : 'Acción rápida:',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 12,
                            color: p.textSecondary,
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        nextParcial != null
                            ? '≥ 3.5 / 5.0'
                            : '+ Agendar parcial →',
                        style: mono(
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                          color: nextParcial != null ? p.textPrimary : p.orange,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 16),

        // 2. Siguiente clase magistral / Materia activa del cuatrimestre
        IosCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(
                      nextClaseOrBlock != null
                          ? 'TU AGENDA DE HOY'
                          : 'CÁTEDRA ACTIVA • CUAT. ${session?.cuatrimestreActual ?? 2}',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w500,
                        color: p.textSecondary,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    nextClaseOrBlock != null
                        ? nextClaseOrBlock.hora
                        : leadCode,
                    style: mono(fontSize: 12, color: p.green),
                  ),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                nextClaseOrBlock?.titulo ?? leadTitle,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: p.textPrimary,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                nextClaseOrBlock?.subtitulo ?? 'Tema KaTeX: $leadTopic',
                style: TextStyle(fontSize: 12, color: p.textSecondary),
              ),
              const SizedBox(height: 12),
              TapScale(
                onTap: () => onOpenClaseViva(
                  nextClaseOrBlock?.codigoMateria ?? leadCode,
                ),
                child: Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 9,
                  ),
                  decoration: BoxDecoration(
                    color: p.elevated,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    children: [
                      Expanded(
                        child: Text(
                          'Abrir fórmula KaTeX y apuntes en La Clase Viva',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w500,
                            color: p.textSecondary,
                          ),
                        ),
                      ),
                      Text('→', style: TextStyle(color: p.textPrimary)),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 16),

        // 3. Bloque de enfoque rápido sincronizado con el .md y GitHub
        IosCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Dot(color: p.indigo),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      'Bloque de Enfoque Rápido',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: p.textPrimary,
                      ),
                    ),
                  ),
                  Text(
                    '+2 Uso • +10% Avance',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                      color: p.indigo,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                '$leadTitle: $leadBlock.',
                style: TextStyle(fontSize: 12, color: p.textSecondary),
              ),
              const SizedBox(height: 12),
              TapScale(
                onTap: () {
                  HapticFeedback.lightImpact();
                  if (session != null) {
                    session.completeStudyBlock(codigoMateria: leadCode);
                    showIosToast(
                      context,
                      '+2 Uso Diario y +10% en $leadTitle',
                      accentColor: p.indigo,
                    );
                  } else {
                    onCompleteBlock();
                  }
                },
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(vertical: 11),
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: p.indigo,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Text(
                    'Completar bloque de estudio (+2 Uso Diario)',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
