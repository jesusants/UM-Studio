import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/theme/app_theme.dart';
import '../../../data/models/curriculum_models.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';

/// Pantalla y Modal Adaptativo "Mi Cuatrimestre" (Selección Manual de Matrícula).
///
/// Permite al estudiante seleccionar manualmente su cuatrimestre base y marcar/desmarcar
/// las asignaturas matriculadas (incluso créditos cruzados entre cuatrimestres).
/// Diseñado bajo la estética Apple Minimalist Dark OLED (#000000) y Crisp Light Mode (#F2F2F7).
class MiCuatrimestreScreen extends StatefulWidget {
  const MiCuatrimestreScreen({
    super.key,
    this.isMandatory = false,
  });

  /// Si es obligatorio (ej. onboarding inicial sin materias), impide cerrar
  /// hasta que el estudiante seleccione y confirme al menos 1 asignatura.
  final bool isMandatory;

  /// Abre la vista en modo modal responsivo (Sheet en móvil / Diálogo en escritorio).
  static Future<void> show(
    BuildContext context, {
    bool isMandatory = false,
  }) async {
    final width = MediaQuery.sizeOf(context).width;
    final isDesktop = width >= 1024;
    final p = context.palette;

    if (isDesktop) {
      await showDialog<void>(
        context: context,
        barrierDismissible: !isMandatory,
        barrierColor: const Color(0xB8000000),
        builder: (dlgCtx) => Dialog(
          backgroundColor: p.background,
          insetPadding: const EdgeInsets.symmetric(horizontal: 24, vertical: 24),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(24),
            side: BorderSide(color: p.cardBorder, width: 1.2),
          ),
          child: ConstrainedBox(
            constraints: const BoxConstraints(
              maxWidth: 680,
              maxHeight: 820,
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(24),
              child: MiCuatrimestreScreen(isMandatory: isMandatory),
            ),
          ),
        ),
      );
    } else {
      await showModalBottomSheet<void>(
        context: context,
        isScrollControlled: true,
        enableDrag: !isMandatory,
        isDismissible: !isMandatory,
        backgroundColor: p.background,
        barrierColor: const Color(0xBF000000),
        shape: RoundedRectangleBorder(
          borderRadius: const BorderRadius.vertical(top: Radius.circular(26)),
          side: BorderSide(color: p.cardBorder, width: 1),
        ),
        builder: (sheetCtx) => SafeArea(
          child: SizedBox(
            height: MediaQuery.sizeOf(context).height * 0.94,
            child: ClipRRect(
              borderRadius: const BorderRadius.vertical(top: Radius.circular(26)),
              child: MiCuatrimestreScreen(isMandatory: isMandatory),
            ),
          ),
        ),
      );
    }
  }

  @override
  State<MiCuatrimestreScreen> createState() => _MiCuatrimestreScreenState();
}

class _MiCuatrimestreScreenState extends State<MiCuatrimestreScreen> {
  /// `0` = Todas las asignaturas (1..12), `1..12` = Cuatrimestre seleccionado en el filtro.
  late int _activeCuatFilter;
  late Set<String> _selectedCodes;
  bool _initialized = false;
  String _searchQuery = '';
  final TextEditingController _searchCtrl = TextEditingController();

  @override
  void dispose() {
    _searchCtrl.dispose();
    super.dispose();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_initialized) {
      final session = SessionScope.maybeOf(context);
      _activeCuatFilter = session?.cuatrimestreActivo ?? 1;
      _selectedCodes = Set<String>.from(session?.materiasMatriculadas ?? const []);
      _initialized = true;
    }
  }

  void _toggleSubject(String code) {
    HapticFeedback.lightImpact();
    setState(() {
      if (_selectedCodes.contains(code)) {
        _selectedCodes.remove(code);
      } else {
        _selectedCodes.add(code);
      }
    });
  }

  void _selectAllInCurrentFilter(List<AsignaturaModel> visible) {
    HapticFeedback.mediumImpact();
    setState(() {
      final visibleCodes = visible.map((a) => a.codigo);
      final allSelected = visibleCodes.every(_selectedCodes.contains);
      if (allSelected) {
        _selectedCodes.removeAll(visibleCodes);
      } else {
        _selectedCodes.addAll(visibleCodes);
      }
    });
  }

  Future<void> _confirmMatricula() async {
    if (_selectedCodes.isEmpty) return;
    HapticFeedback.heavyImpact();

    final session = SessionScope.maybeOf(context);
    if (session != null) {
      final baseCuat = _activeCuatFilter > 0 ? _activeCuatFilter : session.cuatrimestreActivo;
      await session.updateMatricula(
        cuatrimestre: baseCuat,
        materias: _selectedCodes.toList(),
      );
    }

    if (mounted) {
      Navigator.of(context).pop();
      showIosToast(
        context,
        'Matrícula configurada: ${_selectedCodes.length} asignaturas guardadas',
        accentColor: context.palette.green,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final curriculum = CurriculumScope.maybeOf(context);
    final allSubjects = curriculum?.allAsignaturas ?? const <AsignaturaModel>[];

    // Cálculo dinámico en tiempo real de asignaturas y créditos
    final selectedSubjects = allSubjects
        .where((a) => _selectedCodes.contains(a.codigo))
        .toList(growable: false);
    final totalCreditos = selectedSubjects.fold<int>(
      0,
      (sum, a) => sum + a.creditos,
    );
    final totalSelectedCount = selectedSubjects.length;

    // Filtrar lista según cuatrimestre seleccionado y búsqueda
    final query = _searchQuery.trim().toLowerCase();
    final displayedSubjects = allSubjects.where((a) {
      if (_activeCuatFilter > 0 && a.cuatrimestre != _activeCuatFilter) {
        return false;
      }
      if (query.isNotEmpty) {
        final matches = a.nombre.toLowerCase().contains(query) ||
            a.codigo.toLowerCase().contains(query) ||
            a.categoriaLegible.toLowerCase().contains(query);
        if (!matches) return false;
      }
      return true;
    }).toList(growable: false);

    // Contar cuántas asignaturas de cada cuatrimestre están marcadas
    final countByCuat = <int, int>{};
    for (final s in selectedSubjects) {
      countByCuat[s.cuatrimestre] = (countByCuat[s.cuatrimestre] ?? 0) + 1;
    }

    final canConfirm = totalSelectedCount > 0;

    return PopScope(
      canPop: !widget.isMandatory,
      child: Scaffold(
        backgroundColor: p.background,
        body: Column(
          children: [
            // 1. Barra de Agarre / Título Superior
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 14, 16, 10),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Tirador táctil iOS
                  Center(
                    child: Container(
                      width: 38,
                      height: 4.5,
                      margin: const EdgeInsets.only(bottom: 12),
                      decoration: BoxDecoration(
                        color: p.strongBorder,
                        borderRadius: BorderRadius.circular(4),
                      ),
                    ),
                  ),

                  // Fila de Título y Botón Cerrar (si no es obligatorio)
                  Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Mi Cuatrimestre',
                              style: TextStyle(
                                fontSize: 22,
                                fontWeight: FontWeight.w800,
                                letterSpacing: -0.5,
                                color: p.textPrimary,
                              ),
                            ),
                            const SizedBox(height: 3),
                            Text(
                              'Selecciona las asignaturas que tienes inscritas este periodo en Unimagdalena.',
                              style: TextStyle(
                                fontSize: 12,
                                height: 1.35,
                                color: p.textSecondary,
                              ),
                            ),
                          ],
                        ),
                      ),
                      if (!widget.isMandatory) ...[
                        const SizedBox(width: 10),
                        TapScale(
                          onTap: () => Navigator.of(context).pop(),
                          child: Container(
                            width: 32,
                            height: 32,
                            decoration: BoxDecoration(
                              color: p.card,
                              shape: BoxShape.circle,
                              border: Border.all(color: p.cardBorder),
                            ),
                            child: Icon(
                              Icons.close_rounded,
                              size: 18,
                              color: p.textSecondary,
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                  const SizedBox(height: 12),

                  // Contador Flotante en Tiempo Real (Píldora Esmeralda #30D158)
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8.5),
                    decoration: BoxDecoration(
                      color: p.green.o(0.12),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: p.green.o(0.35), width: 1),
                    ),
                    child: Row(
                      children: [
                        Dot(color: p.green, size: 7.5),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            '$totalSelectedCount asignaturas • $totalCreditos créditos académicos',
                            style: mono(
                              fontSize: 11.5,
                              fontWeight: FontWeight.w700,
                              color: p.green,
                              letterSpacing: 0.2,
                            ),
                          ),
                        ),
                        if (displayedSubjects.isNotEmpty && _activeCuatFilter > 0)
                          TapScale(
                            onTap: () => _selectAllInCurrentFilter(displayedSubjects),
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 4),
                              child: Text(
                                displayedSubjects.every((a) => _selectedCodes.contains(a.codigo))
                                    ? 'Deseleccionar C$_activeCuatFilter'
                                    : 'Todo C$_activeCuatFilter',
                                style: mono(
                                  fontSize: 10.5,
                                  fontWeight: FontWeight.w600,
                                  color: p.textPrimary,
                                ),
                              ),
                            ),
                          ),
                      ],
                    ),
                  ),
                ],
              ),
            ),

            // 2. Buscador Dinámico
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: TextField(
                controller: _searchCtrl,
                onChanged: (v) => setState(() => _searchQuery = v),
                style: TextStyle(fontSize: 12.5, color: p.textPrimary),
                decoration: InputDecoration(
                  isDense: true,
                  filled: true,
                  fillColor: p.card,
                  hintText: 'Filtrar por nombre, código (02021810) o área...',
                  hintStyle: TextStyle(fontSize: 12, color: p.textTertiary),
                  prefixIcon: Icon(
                    Icons.search_rounded,
                    size: 16,
                    color: p.textSecondary,
                  ),
                  prefixIconConstraints: const BoxConstraints(
                    minWidth: 34,
                    minHeight: 34,
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
                            size: 15,
                            color: p.textSecondary,
                          ),
                        ),
                  contentPadding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 8,
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: p.cardBorder),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: p.green.o(0.55)),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 10),

            // 3. Selector de Cuatrimestre Rápido (1..12 + Todas)
            SizedBox(
              height: 34,
              child: ListView.separated(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                padding: const EdgeInsets.symmetric(horizontal: 20),
                itemCount: 13,
                separatorBuilder: (_, __) => const SizedBox(width: 6),
                itemBuilder: (context, idx) {
                  final cuat = idx; // 0 = Todas, 1..12 = Cuatrimestre
                  final isSelected = cuat == _activeCuatFilter;
                  final label = cuat == 0 ? 'Todas (56)' : 'C$cuat';
                  final countInCuat = cuat == 0 ? totalSelectedCount : (countByCuat[cuat] ?? 0);

                  return TapScale(
                    onTap: () {
                      HapticFeedback.selectionClick();
                      setState(() => _activeCuatFilter = cuat);
                    },
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 180),
                      padding: const EdgeInsets.symmetric(horizontal: 10),
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: isSelected ? p.green : p.card,
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(
                          color: isSelected ? p.green : p.cardBorder,
                          width: 1,
                        ),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            label,
                            style: mono(
                              fontSize: 11,
                              fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
                              color: isSelected ? Colors.black : p.textSecondary,
                            ),
                          ),
                          if (countInCuat > 0 && cuat > 0) ...[
                            const SizedBox(width: 5),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1.5),
                              decoration: BoxDecoration(
                                color: isSelected
                                    ? const Color(0x2E000000)
                                    : p.green.o(0.20),
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: Text(
                                '$countInCuat',
                                style: mono(
                                  fontSize: 9.5,
                                  fontWeight: FontWeight.w700,
                                  color: isSelected ? Colors.black : p.green,
                                ),
                              ),
                            ),
                          ],
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
            const SizedBox(height: 10),

            // 4. Lista de Asignaturas con Checkboxes Táctiles
            Expanded(
              child: displayedSubjects.isEmpty
                  ? Center(
                      child: Padding(
                        padding: const EdgeInsets.all(24),
                        child: Text(
                          'No hay asignaturas que coincidan con el filtro actual.',
                          textAlign: TextAlign.center,
                          style: TextStyle(fontSize: 12.5, color: p.textSecondary),
                        ),
                      ),
                    )
                  : ListView.separated(
                      physics: const BouncingScrollPhysics(),
                      padding: const EdgeInsets.fromLTRB(20, 4, 20, 20),
                      itemCount: displayedSubjects.length,
                      separatorBuilder: (_, __) => const SizedBox(height: 9),
                      itemBuilder: (context, index) {
                        final subject = displayedSubjects[index];
                        final isChecked = _selectedCodes.contains(subject.codigo);

                        return _SubjectEnrollmentCard(
                          subject: subject,
                          isChecked: isChecked,
                          palette: p,
                          onTap: () => _toggleSubject(subject.codigo),
                        );
                      },
                    ),
            ),

            // 5. Botón Inferior Anclado de Confirmación
            Container(
              padding: const EdgeInsets.fromLTRB(20, 12, 20, 16),
              decoration: BoxDecoration(
                color: p.glass,
                border: Border(top: BorderSide(color: p.cardBorder, width: 1)),
              ),
              child: SafeArea(
                top: false,
                child: TapScale(
                  onTap: canConfirm ? _confirmMatricula : null,
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(vertical: 13),
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: canConfirm ? p.green : p.elevated,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(
                        color: canConfirm ? p.green : p.cardBorder,
                        width: 1,
                      ),
                      boxShadow: canConfirm
                          ? [
                              BoxShadow(
                                color: p.green.o(0.25),
                                blurRadius: 14,
                                offset: const Offset(0, 3),
                              ),
                            ]
                          : null,
                    ),
                    child: Text(
                      canConfirm
                          ? 'Confirmar mi matrícula ($totalSelectedCount materias) →'
                          : 'Selecciona al menos 1 asignatura',
                      style: TextStyle(
                        fontSize: 13.5,
                        fontWeight: FontWeight.w700,
                        color: canConfirm ? Colors.black : p.textTertiary,
                        letterSpacing: -0.2,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Tarjeta Táctil Minimalista de Asignatura para Selección de Matrícula
class _SubjectEnrollmentCard extends StatelessWidget {
  const _SubjectEnrollmentCard({
    required this.subject,
    required this.isChecked,
    required this.palette,
    required this.onTap,
  });

  final AsignaturaModel subject;
  final bool isChecked;
  final AppPalette palette;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = palette;
    final isDualEnglish = subject.esIngles;

    final borderColor = isChecked ? p.green : p.cardBorder;
    final bgColor = isChecked ? p.green.o(0.08) : p.card;

    return TapScale(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: borderColor, width: isChecked ? 1.4 : 1),
        ),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Checkbox circular minimalista
            AnimatedContainer(
              duration: const Duration(milliseconds: 180),
              width: 24,
              height: 24,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: isChecked ? p.green : Colors.transparent,
                border: Border.all(
                  color: isChecked ? p.green : p.textTertiary,
                  width: 1.6,
                ),
              ),
              child: isChecked
                  ? const Center(
                      child: Icon(
                        Icons.check_rounded,
                        size: 16,
                        color: Colors.black,
                      ),
                    )
                  : null,
            ),
            const SizedBox(width: 12),

            // Contenido informativo de la asignatura
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      // Código de la materia
                      Text(
                        subject.codigo,
                        style: mono(
                          fontSize: 10,
                          fontWeight: FontWeight.w700,
                          color: isChecked ? p.green : p.textSecondary,
                        ),
                      ),
                      const SizedBox(width: 6),
                      // Cuatrimestre
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                        decoration: BoxDecoration(
                          color: p.elevated,
                          borderRadius: BorderRadius.circular(5),
                          border: Border.all(color: p.cardBorder),
                        ),
                        child: Text(
                          'C${subject.cuatrimestre}',
                          style: mono(
                            fontSize: 9,
                            fontWeight: FontWeight.w600,
                            color: p.textSecondary,
                          ),
                        ),
                      ),
                      const SizedBox(width: 6),
                      // Créditos
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                        decoration: BoxDecoration(
                          color: p.green.o(0.12),
                          borderRadius: BorderRadius.circular(5),
                        ),
                        child: Text(
                          '${subject.creditos} cr',
                          style: mono(
                            fontSize: 9,
                            fontWeight: FontWeight.w700,
                            color: p.green,
                          ),
                        ),
                      ),
                      if (isDualEnglish) ...[
                        const SizedBox(width: 6),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                          decoration: BoxDecoration(
                            color: p.indigo.o(0.14),
                            borderRadius: BorderRadius.circular(5),
                          ),
                          child: Text(
                            'DUAL',
                            style: mono(
                              fontSize: 9,
                              fontWeight: FontWeight.w700,
                              color: p.indigo,
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                  const SizedBox(height: 4),
                  // Nombre oficial de la materia
                  Text(
                    subject.nombre,
                    style: TextStyle(
                      fontSize: 13.5,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.2,
                      color: isChecked ? p.textPrimary : p.textBody,
                    ),
                  ),
                  const SizedBox(height: 3),
                  // Área y cantidad de temas
                  Text(
                    '${subject.categoriaLegible} • ${subject.temas.length} temas magistrales',
                    style: TextStyle(
                      fontSize: 11,
                      color: p.textSecondary,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
