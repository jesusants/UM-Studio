import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/datasources/academic_seed_data.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';

/// Pestaña 4: "Estudio Extraclase" alimentada desde `ingenieria_energetica.md`
/// con filtro horizontal estilo píldora iOS por Cuatrimestre (`1..12`), `Mis Materias`
/// y registro sincronizado en GitHub de `(Último revisado)`.
class EstudioTab extends StatefulWidget {
  const EstudioTab({
    super.key,
    required this.onOpenClaseViva,
    this.onOpenTemario,
  });

  final ValueChanged<String> onOpenClaseViva;
  final ValueChanged<AsignaturaModel>? onOpenTemario;

  @override
  State<EstudioTab> createState() => _EstudioTabState();
}

class _EstudioTabState extends State<EstudioTab> {
  /// `-1` = Mis Materias, `0` = Todas (56), `1..12` = Cuatrimestre específico.
  int _selectedFilter = -1;
  String _searchQuery = '';
  final TextEditingController _searchCtrl = TextEditingController();

  @override
  void dispose() {
    _searchCtrl.dispose();
    super.dispose();
  }

  List<AsignaturaModel> _filterSubjects(
    List<AsignaturaModel> all,
    InstitutionalSessionController? session,
  ) {
    final q = _searchQuery.trim().toLowerCase();
    return all.where((asig) {
      if (q.isNotEmpty) {
        final matchesText = asig.nombre.toLowerCase().contains(q) ||
            asig.codigo.toLowerCase().contains(q) ||
            asig.categoriaLegible.toLowerCase().contains(q) ||
            asig.temas.any((t) => t.titulo.toLowerCase().contains(q));
        if (!matchesText) return false;
      }

      if (_selectedFilter == 0 || q.isNotEmpty) {
        if (_selectedFilter <= 0) return true;
      }

      if (_selectedFilter == -1) {
        if (session == null) return asig.cuatrimestre <= 2;
        return session.isMySubject(asig);
      }

      return asig.cuatrimestre == _selectedFilter;
    }).toList(growable: false);
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final curriculum = CurriculumScope.maybeOf(context);
    final session = SessionScope.maybeOf(context);
    final allSubjects = curriculum?.allAsignaturas ?? const <AsignaturaModel>[];

    // Respaldo para tests aislados donde no se inyectó CurriculumScope.
    if (allSubjects.isEmpty) {
      return _LegacyFallbackEstudioList(onOpenClaseViva: widget.onOpenClaseViva);
    }

    final filtered = _filterSubjects(allSubjects, session);
    final currentCuat = session?.cuatrimestreActual ?? 2;

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Estudio Extraclase',
                    style: TextStyle(
                      fontSize: 23,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.5,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    'Malla Oficial Ing. Energética • Plan ${curriculum?.programa.codigoInterno ?? '8108'}',
                    style: TextStyle(fontSize: 12, color: p.textSecondary),
                  ),
                ],
              ),
            ),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
              decoration: BoxDecoration(
                color: p.card,
                borderRadius: BorderRadius.circular(999),
                border: Border.all(color: p.cardBorder),
              ),
              child: Text(
                '${filtered.length} / ${allSubjects.length}',
                style: mono(
                  fontSize: 10.5,
                  fontWeight: FontWeight.w600,
                  color: p.green,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 12),

        // Buscador minimalista estilo iOS Spotlight
        TextField(
          controller: _searchCtrl,
          onChanged: (v) => setState(() => _searchQuery = v),
          style: TextStyle(fontSize: 13, color: p.textPrimary),
          decoration: InputDecoration(
            isDense: true,
            filled: true,
            fillColor: p.card,
            hintText: 'Buscar asignatura, tema o código (ej. 02021810)...',
            hintStyle: TextStyle(fontSize: 12, color: p.textTertiary),
            prefixIcon: Icon(
              Icons.search_rounded,
              size: 17,
              color: p.textSecondary,
            ),
            prefixIconConstraints: const BoxConstraints(
              minWidth: 36,
              minHeight: 36,
            ),
            suffixIcon: _searchQuery.isEmpty
                ? null
                : GestureDetector(
                    onTap: () {
                      _searchCtrl.clear();
                      setState(() => _searchQuery = '');
                    },
                    child: Icon(
                      Icons.cancel_rounded,
                      size: 16,
                      color: p.textSecondary,
                    ),
                  ),
            contentPadding: const EdgeInsets.symmetric(
              horizontal: 12,
              vertical: 10,
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(13),
              borderSide: BorderSide(color: p.cardBorder),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(13),
              borderSide: BorderSide(color: p.green.o(0.6)),
            ),
          ),
        ),
        const SizedBox(height: 12),

        // Selector horizontal minimalista estilo píldora iOS por Cuatrimestre
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          child: Row(
            children: [
              _FilterPill(
                label: 'Mis Materias',
                selected: _selectedFilter == -1,
                accentColor: p.green,
                onTap: () => setState(() => _selectedFilter = -1),
              ),
              for (var c = 1; c <= 12; c++) ...[
                const SizedBox(width: 7),
                _FilterPill(
                  label: 'Cuatrimestre $c',
                  selected: _selectedFilter == c,
                  onTap: () => setState(() => _selectedFilter = c),
                ),
              ],
              const SizedBox(width: 7),
              _FilterPill(
                label: 'Todas (${allSubjects.length})',
                selected: _selectedFilter == 0,
                onTap: () => setState(() => _selectedFilter = 0),
              ),
            ],
          ),
        ),
        const SizedBox(height: 14),

        if (filtered.isEmpty)
          IosCard(
            child: Column(
              children: [
                Text(
                  'No se encontraron asignaturas con ese filtro.',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 12.5, color: p.textSecondary),
                ),
                const SizedBox(height: 8),
                TapScale(
                  onTap: () {
                    _searchCtrl.clear();
                    setState(() {
                      _searchQuery = '';
                      _selectedFilter = 0;
                    });
                  },
                  child: Text(
                    'Ver las 56 asignaturas del Plan 8108',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: p.green,
                    ),
                  ),
                ),
              ],
            ),
          )
        else
          for (final asignatura in filtered) ...[
            _CurriculumSubjectCard(
              asignatura: asignatura,
              progressPercent: session?.subjectProgress(asignatura.codigo) ?? 0,
              lastReviewedTopicNum: session?.lastReviewedTopicFor(
                asignatura.codigo,
              ),
              isPinned:
                  session?.progresoMaterias.containsKey(asignatura.codigo) ??
                      false,
              isCurrentSemester: asignatura.cuatrimestre == currentCuat,
              onTap: () {
                if (widget.onOpenTemario != null) {
                  widget.onOpenTemario!(asignatura);
                } else {
                  widget.onOpenClaseViva(asignatura.codigo);
                }
              },
              onTogglePin: session == null
                  ? null
                  : () async {
                      HapticFeedback.lightImpact();
                      final pinned = await session.togglePinnedSubject(
                        asignatura.codigo,
                      );
                      if (context.mounted) {
                        showIosToast(
                          context,
                          pinned
                              ? '${asignatura.nombre} fijada en Mis Materias'
                              : '${asignatura.nombre} removida de fijadas',
                        );
                      }
                    },
            ),
            const SizedBox(height: 12),
          ],
      ],
    );
  }
}

class _FilterPill extends StatelessWidget {
  const _FilterPill({
    required this.label,
    required this.selected,
    required this.onTap,
    this.accentColor,
  });

  final String label;
  final bool selected;
  final VoidCallback onTap;
  final Color? accentColor;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final activeBg = accentColor ?? p.inverse;
    final activeText = accentColor != null ? Colors.black : p.onInverse;

    return TapScale(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        curve: kIosSpring,
        padding: const EdgeInsets.symmetric(horizontal: 13, vertical: 6),
        decoration: BoxDecoration(
          color: selected ? activeBg : p.card,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(
            color: selected ? activeBg : p.cardBorder,
          ),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 12,
            fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
            color: selected ? activeText : p.textSecondary,
          ),
        ),
      ),
    );
  }
}

class _CurriculumSubjectCard extends StatelessWidget {
  const _CurriculumSubjectCard({
    required this.asignatura,
    required this.progressPercent,
    required this.lastReviewedTopicNum,
    required this.isPinned,
    required this.isCurrentSemester,
    required this.onTap,
    this.onTogglePin,
  });

  final AsignaturaModel asignatura;
  final int progressPercent;
  final int? lastReviewedTopicNum;
  final bool isPinned;
  final bool isCurrentSemester;
  final VoidCallback onTap;
  final VoidCallback? onTogglePin;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final accent = asignatura.accentColor;
    final active = isPinned || isCurrentSemester;

    TemaClaseVivaModel? reviewedTopic;
    if (lastReviewedTopicNum != null) {
      for (final t in asignatura.temas) {
        if (t.numeroTema == lastReviewedTopicNum) {
          reviewedTopic = t;
          break;
        }
      }
    }

    return TapScale(
      onTap: onTap,
      child: IosCard(
        borderColor: isPinned ? accent.o(0.45) : null,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Wrap(
                    spacing: 6,
                    runSpacing: 4,
                    crossAxisAlignment: WrapCrossAlignment.center,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 7,
                          vertical: 2,
                        ),
                        decoration: BoxDecoration(
                          color: accent.o(0.13),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          '${asignatura.categoriaLegible} • C${asignatura.cuatrimestre}'
                              .toUpperCase(),
                          style: mono(
                            fontSize: 9.5,
                            fontWeight: FontWeight.w600,
                            color: accent,
                          ),
                        ),
                      ),
                      Text(
                        '${asignatura.codigo} • ${asignatura.creditos} cr',
                        style: mono(fontSize: 10, color: p.textTertiary),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 6),
                Text(
                  '$progressPercent%',
                  style: mono(
                    fontSize: 12,
                    fontWeight: active ? FontWeight.w600 : FontWeight.w400,
                    color: active ? p.textPrimary : p.textSecondary,
                  ),
                ),
                if (onTogglePin != null) ...[
                  const SizedBox(width: 6),
                  GestureDetector(
                    onTap: onTogglePin,
                    child: Icon(
                      isPinned
                          ? Icons.bookmark_rounded
                          : Icons.bookmark_border_rounded,
                      size: 17,
                      color: isPinned ? accent : p.textTertiary,
                    ),
                  ),
                ],
              ],
            ),
            const SizedBox(height: 8),
            Text(
              asignatura.nombre,
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w600,
                color: p.textPrimary,
              ),
            ),
            const SizedBox(height: 6),
            Text.rich(
              TextSpan(
                style: TextStyle(fontSize: 12, color: p.textSecondary),
                children: [
                  TextSpan(
                    text: reviewedTopic != null
                        ? 'Tema ${reviewedTopic.numeroTema}: '
                        : (asignatura.temas.length > 1
                            ? 'Temas (${asignatura.temas.length}): '
                            : 'Tema KaTeX: '),
                  ),
                  TextSpan(
                    text: (reviewedTopic ?? asignatura.primerTema).titulo,
                    style: TextStyle(
                      fontWeight: FontWeight.w600,
                      color: p.textPrimary,
                    ),
                  ),
                  if (reviewedTopic != null)
                    TextSpan(
                      text: '  (Último revisado)',
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w500,
                        color: p.green,
                      ),
                    ),
                ],
              ),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: 11),
            ProgressBar(
              value: (progressPercent / 100).clamp(0.04, 1.0),
              color: accent,
              height: 6,
            ),
          ],
        ),
      ),
    );
  }
}

class _LegacyFallbackEstudioList extends StatelessWidget {
  const _LegacyFallbackEstudioList({required this.onOpenClaseViva});

  final ValueChanged<String> onOpenClaseViva;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
      children: [
        Text(
          'Estudio Extraclase',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.w700,
            color: p.textPrimary,
          ),
        ),
        const SizedBox(height: 16),
        for (final s in AcademicSeedData.subjects) ...[
          TapScale(
            onTap: () => onOpenClaseViva(s.id),
            child: IosCard(
              child: Text(
                s.title,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: p.textPrimary,
                ),
              ),
            ),
          ),
          const SizedBox(height: 12),
        ],
      ],
    );
  }
}
