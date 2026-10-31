import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../clases/asignatura_temario_page.dart';

/// Nueva Pestaña "Clases": exploración 100% libre organizada en los 12
/// Cuatrimestres oficiales de Ingeniería Energética para todos los usuarios.
class ClasesTab extends StatefulWidget {
  const ClasesTab({super.key});

  @override
  State<ClasesTab> createState() => _ClasesTabState();
}

class _ClasesTabState extends State<ClasesTab> {
  /// `0` = Todos los Cuatrimestres (`1..12`), `1..12` = Cuatrimestre específico.
  int _selectedCuatrimestre = 0;
  String _searchQuery = '';
  final TextEditingController _searchCtrl = TextEditingController();

  @override
  void dispose() {
    _searchCtrl.dispose();
    super.dispose();
  }

  void _openTemario(AsignaturaModel asignatura) {
    Navigator.of(context).push(AsignaturaTemarioPage.route(asignatura));
  }

  bool _matchesSearch(AsignaturaModel asig, String query) {
    if (query.isEmpty) return true;
    return asig.nombre.toLowerCase().contains(query) ||
        asig.codigo.toLowerCase().contains(query) ||
        asig.categoriaLegible.toLowerCase().contains(query) ||
        asig.temas.any((t) => t.titulo.toLowerCase().contains(query));
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final curriculum = CurriculumScope.maybeOf(context);
    final session = SessionScope.maybeOf(context);
    final cuatrimestres =
        curriculum?.cuatrimestres ?? const <CuatrimestreModel>[];
    final q = _searchQuery.trim().toLowerCase();

    final globalLast = session?.ultimoRevisado;
    final lastAsignatura = globalLast != null
        ? curriculum?.database?.findAsignatura(globalLast.codigoMateria)
        : null;

    final visibleGroups = <CuatrimestreModel>[];
    var totalVisibleSubjects = 0;

    for (final c in cuatrimestres) {
      if (_selectedCuatrimestre != 0 && c.numero != _selectedCuatrimestre) {
        continue;
      }
      final matching = c.asignaturas
          .where((a) => _matchesSearch(a, q))
          .toList(growable: false);
      if (matching.isNotEmpty) {
        totalVisibleSubjects += matching.length;
        visibleGroups.add(
          CuatrimestreModel(
            numero: c.numero,
            creditosTotales: c.creditosTotales,
            asignaturas: matching,
          ),
        );
      }
    }

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
      children: [
        // Encabezado
        Row(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Clases',
                    style: TextStyle(
                      fontSize: 23,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.5,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    'Explora libremente los 12 cuatrimestres y sus temarios',
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
                '$totalVisibleSubjects materias',
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

        // Buscador libre
        TextField(
          controller: _searchCtrl,
          onChanged: (v) => setState(() => _searchQuery = v),
          style: TextStyle(fontSize: 13, color: p.textPrimary),
          decoration: InputDecoration(
            isDense: true,
            filled: true,
            fillColor: p.card,
            hintText: 'Buscar asignatura, tema o código...',
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

        // Píldoras horizontales por Cuatrimestre (1..12) para todos los usuarios
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          child: Row(
            children: [
              _CuatrimestrePill(
                label: 'Todos (12 Cuat.)',
                selected: _selectedCuatrimestre == 0,
                accentColor: p.green,
                onTap: () => setState(() => _selectedCuatrimestre = 0),
              ),
              for (var c = 1; c <= 12; c++) ...[
                const SizedBox(width: 7),
                _CuatrimestrePill(
                  label: 'Cuatrimestre $c',
                  selected: _selectedCuatrimestre == c,
                  onTap: () => setState(() => _selectedCuatrimestre = c),
                ),
              ],
            ],
          ),
        ),

        // Acceso rápido a la última asignatura/tema revisado
        if (lastAsignatura != null &&
            globalLast != null &&
            _selectedCuatrimestre == 0 &&
            q.isEmpty) ...[
          const SizedBox(height: 14),
          TapScale(
            onTap: () => _openTemario(lastAsignatura),
            child: IosCard(
              radius: 16,
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 11),
              borderColor: p.green.o(0.42),
              child: Row(
                children: [
                  Dot(color: p.green, size: 7),
                  const SizedBox(width: 9),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '${lastAsignatura.nombre} • Tema ${globalLast.numeroTema}',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w600,
                            color: p.textPrimary,
                          ),
                        ),
                        Text(
                          '(Último revisado)',
                          style: TextStyle(
                            fontSize: 10.5,
                            color: p.green,
                          ),
                        ),
                      ],
                    ),
                  ),
                  Icon(
                    Icons.chevron_right_rounded,
                    size: 18,
                    color: p.green,
                  ),
                ],
              ),
            ),
          ),
        ],

        const SizedBox(height: 16),

        if (visibleGroups.isEmpty)
          IosCard(
            child: Text(
              'No se encontraron clases para esa búsqueda.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 12.5, color: p.textSecondary),
            ),
          )
        else
          for (final group in visibleGroups) ...[
            Padding(
              padding: const EdgeInsets.only(bottom: 9, top: 4),
              child: Row(
                children: [
                  Expanded(
                    child: Text(
                      'CUATRIMESTRE ${group.numero}',
                      style: sectionMicroStyle(p),
                    ),
                  ),
                  Text(
                    '${group.creditosTotales} créditos • ${group.asignaturas.length} materias',
                    style: mono(fontSize: 10.5, color: p.textTertiary),
                  ),
                ],
              ),
            ),
            for (final asig in group.asignaturas) ...[
              _ClaseAsignaturaRow(
                asignatura: asig,
                lastReviewedTopicNum: session?.lastReviewedTopicFor(
                  asig.codigo,
                ),
                onTap: () => _openTemario(asig),
              ),
              const SizedBox(height: 10),
            ],
            const SizedBox(height: 8),
          ],
      ],
    );
  }
}

class _CuatrimestrePill extends StatelessWidget {
  const _CuatrimestrePill({
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
          border: Border.all(color: selected ? activeBg : p.cardBorder),
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

class _ClaseAsignaturaRow extends StatelessWidget {
  const _ClaseAsignaturaRow({
    required this.asignatura,
    required this.lastReviewedTopicNum,
    required this.onTap,
  });

  final AsignaturaModel asignatura;
  final int? lastReviewedTopicNum;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final accent = asignatura.accentColor;

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
        radius: 17,
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
        borderColor: reviewedTopic != null ? p.green.o(0.35) : p.cardBorder,
        child: Row(
          children: [
            Container(
              width: 36,
              height: 36,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: accent.o(0.14),
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: accent.o(0.3)),
              ),
              child: Text(
                'C${asignatura.cuatrimestre}',
                style: mono(
                  fontSize: 11.5,
                  fontWeight: FontWeight.w700,
                  color: accent,
                ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    asignatura.nombre,
                    style: TextStyle(
                      fontSize: 14.5,
                      fontWeight: FontWeight.w600,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    '${asignatura.categoriaLegible} • ${asignatura.codigo} • ${asignatura.temas.length} ${asignatura.temas.length == 1 ? 'tema' : 'temas'}',
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: mono(fontSize: 10.5, color: p.textSecondary),
                  ),
                  if (reviewedTopic != null) ...[
                    const SizedBox(height: 4),
                    Row(
                      children: [
                        Dot(color: p.green, size: 5),
                        const SizedBox(width: 5),
                        Expanded(
                          child: Text(
                            'Tema ${reviewedTopic.numeroTema}: ${reviewedTopic.titulo} (Último revisado)',
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w500,
                              color: p.green,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ],
              ),
            ),
            const SizedBox(width: 8),
            Icon(
              Icons.chevron_right_rounded,
              size: 18,
              color: p.textSecondary,
            ),
          ],
        ),
      ),
    );
  }
}
