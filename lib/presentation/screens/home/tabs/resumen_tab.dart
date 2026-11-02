import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../../data/models/student_user_model.dart';
import '../../../../data/services/markdown_curriculum_service.dart';
import '../../../../data/services/unimagdalena_realtime_news_service.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../../widgets/reminder_creator_sheet.dart';

/// Pestaña 1: "Resumen de hoy" conectada al perfil del estudiante,
/// su calendario personal en GitHub, el último tema revisado y sus materias activas.
class ResumenTab extends StatelessWidget {
  const ResumenTab({
    super.key,
    required this.onOpenClaseViva,
    this.onCompleteBlock,
  });

  final ValueChanged<String> onOpenClaseViva;
  final VoidCallback? onCompleteBlock;

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
      if (session.hasMatriculaConfigured) {
        final enrolled = session.materiasMatriculadas
            .map((c) => db.findAsignatura(c))
            .whereType<AsignaturaModel>()
            .toList();
        if (enrolled.isNotEmpty) {
          final lastRev = session.ultimoRevisado;
          if (lastRev != null) {
            final fromRev = enrolled.firstWhere(
              (a) => a.codigo == lastRev.codigoMateria,
              orElse: () => enrolled.first,
            );
            return fromRev;
          }
          return enrolled.first;
        }
      }
      final lastRev = session.ultimoRevisado;
      if (lastRev != null) {
        final fromRev = db.findAsignatura(lastRev.codigoMateria);
        if (fromRev != null) return fromRev;
      }
      for (final code in session.progresoMaterias.keys) {
        final found = db.findAsignatura(code);
        if (found != null) return found;
      }
      final semList = db.byCuatrimestre(session.cuatrimestreActivo);
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
    final todayIso = IsoDateHelper.todayIso();

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

    final globalLast = session?.ultimoRevisado;
    final lastAsignatura = globalLast != null
        ? curriculum?.database?.findAsignatura(globalLast.codigoMateria)
        : null;
    TemaClaseVivaModel? lastTema;
    if (lastAsignatura != null && globalLast != null) {
      for (final t in lastAsignatura.temas) {
        if (t.numeroTema == globalLast.numeroTema) {
          lastTema = t;
          break;
        }
      }
    }

    final leadSubject = _resolveLeadSubject(session, curriculum);
    final leadCode = leadSubject?.codigo ?? '02021810';
    final leadTitle = leadSubject?.nombre ?? 'Física Mecánica';
    final leadTopic =
        lastTema?.titulo ??
        leadSubject?.primerTema.titulo ??
        'Leyes de Newton y Rozamiento';
    final leadBlock =
        lastTema?.bloqueSugerido ??
        leadSubject?.primerTema.bloqueSugerido ??
        'Pomodoro 50/10 • Diagramas de cuerpo libre con fricción';
    final resumeKey = (lastAsignatura != null && globalLast != null)
        ? globalLast.temaKey
        : leadCode;

    return RefreshIndicator(
      color: p.green,
      backgroundColor: p.card,
      onRefresh: () =>
          UnimagdalenaRealtimeNewsService.instance.refreshNews(force: true),
      child: ListView(
        physics: const AlwaysScrollableScrollPhysics(
          parent: BouncingScrollPhysics(),
        ),
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 36),
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

        // 2. Siguiente clase / Continuar último tema revisado o cátedra activa
        IosCard(
          borderColor: lastTema != null && nextClaseOrBlock == null
              ? p.green.o(0.38)
              : null,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(
                      nextClaseOrBlock != null
                          ? 'TU AGENDA DE HOY'
                          : (lastTema != null
                              ? 'CONTINUAR TEMA'
                              : (session?.hasMatriculaConfigured == true
                                  ? 'CÁTEDRA ACTIVA • ${session!.materiasMatriculadas.length} MATERIAS'
                                  : 'CÁTEDRA ACTIVA • CUAT. ${session?.cuatrimestreActivo ?? 1}')),
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
                  if (lastTema != null && nextClaseOrBlock == null)
                    Text(
                      '(Último revisado)',
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w500,
                        color: p.green,
                      ),
                    )
                  else
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
                nextClaseOrBlock?.titulo ??
                    (lastAsignatura?.nombre ?? leadTitle),
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: p.textPrimary,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                nextClaseOrBlock?.subtitulo ??
                    (lastTema != null
                        ? 'Tema ${lastTema.numeroTema}: ${lastTema.titulo}'
                        : 'Tema KaTeX: $leadTopic'),
                style: TextStyle(fontSize: 12, color: p.textSecondary),
              ),
              const SizedBox(height: 12),
              TapScale(
                onTap: () => onOpenClaseViva(
                  nextClaseOrBlock?.codigoMateria ?? resumeKey,
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
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: p.textPrimary,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    '+10% Avance',
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
                      '+10% de avance en $leadTitle',
                      accentColor: p.indigo,
                    );
                  } else {
                    onCompleteBlock?.call();
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
                    'Completar bloque de estudio (+10% Avance)',
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
        const SizedBox(height: 20),

        // 4. Noticias en Tiempo Real desde el Portal Unimagdalena
        _UnimagdalenaMobileNewsCarousel(p: p),
      ],
    ),
    );
  }
}

/// Carrusel horizontal iOS de noticias oficiales de Unimagdalena con badge En Vivo
class _UnimagdalenaMobileNewsCarousel extends StatelessWidget {
  const _UnimagdalenaMobileNewsCarousel({required this.p});

  final AppPalette p;

  Color _categoryColor(String category, AppPalette p) {
    final cat = category.toUpperCase();
    if (cat.contains('FACULTAD')) return p.green;
    if (cat.contains('ACADÉMICO') || cat.contains('ACADEMICO')) {
      return p.orange;
    }
    if (cat.contains('INVESTIGA') || cat.contains('SEMILLERO')) {
      return p.indigo;
    }
    return const Color(0xFF0A84FF);
  }

  Future<void> _openNews(String url) async {
    if (url.isEmpty) return;
    try {
      final uri = Uri.parse(url);
      if (uri.scheme == 'https' || uri.scheme == 'http') {
        if (await canLaunchUrl(uri)) {
          await launchUrl(uri, mode: LaunchMode.externalApplication);
        }
      }
    } catch (_) {}
  }

  @override
  Widget build(BuildContext context) {
    final service = UnimagdalenaRealtimeNewsService.instance;

    return ListenableBuilder(
      listenable: service,
      builder: (context, _) {
        final news = service.news;
        final isLoading = service.isLoading;

        if (news.isEmpty && !isLoading) {
          return const SizedBox.shrink();
        }

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Dot(color: p.green, size: 7),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    'NOTICIAS UNIMAGDALENA',
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: mono(
                      fontSize: 11,
                      fontWeight: FontWeight.w700,
                      letterSpacing: 0.9,
                      color: p.textSecondary,
                    ),
                  ),
                ),
                if (isLoading)
                  SizedBox(
                    width: 12,
                    height: 12,
                    child: CircularProgressIndicator(
                      strokeWidth: 1.8,
                      color: p.green,
                    ),
                  )
                else
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 7,
                      vertical: 2,
                    ),
                    decoration: BoxDecoration(
                      color: p.green.o(0.12),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      'En vivo',
                      style: mono(
                        fontSize: 9.5,
                        fontWeight: FontWeight.w700,
                        color: p.green,
                      ),
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 12),
            SizedBox(
              height: 188,
              child: ListView.separated(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                itemCount: news.length,
                separatorBuilder: (_, __) => const SizedBox(width: 12),
                itemBuilder: (context, index) {
                  final item = news[index];
                  final accent = _categoryColor(item.category, p);

                  return TapScale(
                    onTap: () => _openNews(item.url),
                    child: Container(
                      width: 260,
                      padding: const EdgeInsets.all(13),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(
                          color: item.isRecent
                              ? p.green.o(0.55)
                              : p.cardBorder,
                          width: item.isRecent ? 1.3 : 1.0,
                        ),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            children: [
                              Container(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 6,
                                  vertical: 2,
                                ),
                                decoration: BoxDecoration(
                                  color: accent.o(0.12),
                                  borderRadius: BorderRadius.circular(5),
                                  border: Border.all(
                                    color: accent.o(0.35),
                                    width: 1,
                                  ),
                                ),
                                child: Text(
                                  item.category.toUpperCase(),
                                  style: mono(
                                    fontSize: 8.5,
                                    fontWeight: FontWeight.w700,
                                    color: accent,
                                  ),
                                ),
                              ),
                              if (item.isRecent) ...[
                                const SizedBox(width: 6),
                                Container(
                                  padding: const EdgeInsets.symmetric(
                                    horizontal: 5,
                                    vertical: 1.5,
                                  ),
                                  decoration: BoxDecoration(
                                    color: p.green.o(0.20),
                                    borderRadius: BorderRadius.circular(4),
                                  ),
                                  child: Text(
                                    'NUEVO',
                                    style: mono(
                                      fontSize: 8,
                                      fontWeight: FontWeight.w800,
                                      color: p.green,
                                    ),
                                  ),
                                ),
                              ],
                              const Spacer(),
                              Text(
                                item.dateText,
                                style: mono(
                                  fontSize: 9.5,
                                  color: p.textTertiary,
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 8),
                          Text(
                            item.title,
                            maxLines: 2,
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              letterSpacing: -0.2,
                              height: 1.25,
                              color: p.textPrimary,
                            ),
                          ),
                          const SizedBox(height: 5),
                          Expanded(
                            child: Text(
                              item.summary,
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                              style: TextStyle(
                                fontSize: 11.5,
                                height: 1.35,
                                color: p.textSecondary,
                              ),
                            ),
                          ),
                          const SizedBox(height: 6),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.end,
                            children: [
                              Text(
                                'Ver publicación ↗',
                                style: mono(
                                  fontSize: 9,
                                  fontWeight: FontWeight.w600,
                                  color: p.textTertiary,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        );
      },
    );
  }
}
