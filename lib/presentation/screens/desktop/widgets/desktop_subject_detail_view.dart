import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../../widgets/katex_formula_card.dart';
import '../../../widgets/minimal_slide_viewer.dart';
import '../desktop_theme_tokens.dart';

/// Vista de Detalle Panorámica de Asignatura (Master-Detail) en la columna central.
/// Muestra selector de cuatrimestre/temas, visor dual (Slides vs KaTeX) y bloques sugeridos.
class DesktopSubjectDetailView extends StatefulWidget {
  const DesktopSubjectDetailView({
    super.key,
    required this.subject,
    required this.onBackToDashboard,
    required this.onOpenClaseViva,
  });

  final AsignaturaModel subject;
  final VoidCallback onBackToDashboard;
  final ValueChanged<String> onOpenClaseViva;

  @override
  State<DesktopSubjectDetailView> createState() =>
      _DesktopSubjectDetailViewState();
}

class _DesktopSubjectDetailViewState extends State<DesktopSubjectDetailView> {
  int _selectedTopicNumber = 1;
  String _activeEnglishBranch = 'general';

  @override
  void initState() {
    super.initState();
    _initSelectedTopic();
  }

  @override
  void didUpdateWidget(covariant DesktopSubjectDetailView oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.subject.codigo != widget.subject.codigo) {
      _initSelectedTopic();
    }
  }

  void _initSelectedTopic() {
    final temas = widget.subject.esIngles
        ? widget.subject.temasPorModalidad(_activeEnglishBranch)
        : widget.subject.temas;
    if (temas.isNotEmpty) {
      _selectedTopicNumber = temas.first.numeroTema;
    } else {
      _selectedTopicNumber = 1;
    }
  }

  TemaClaseVivaModel? get _currentTema {
    final temas = widget.subject.esIngles
        ? widget.subject.temasPorModalidad(_activeEnglishBranch)
        : widget.subject.temas;
    try {
      return temas.firstWhere(
        (t) => t.numeroTema == _selectedTopicNumber,
        orElse: () => temas.isNotEmpty ? temas.first : widget.subject.primerTema,
      );
    } catch (_) {
      return widget.subject.primerTema;
    }
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    final session = SessionScope.maybeOf(context);
    final subject = widget.subject;
    final isIngles = subject.esIngles;

    final temasDisponibles = isIngles
        ? subject.temasPorModalidad(_activeEnglishBranch)
        : subject.temas;
    final currentTema = _currentTema;
    final progress = session?.subjectProgress(subject.codigo) ?? 0;

    return Container(
      decoration: BoxDecoration(
        color: tokens.surface,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: tokens.border, width: 1),
        boxShadow: [
          BoxShadow(
            color: tokens.shadowColor,
            blurRadius: 20,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // 1. Barra de Encabezado con Botón de Regreso & Acciones
          Row(
            children: [
              TapScale(
                onTap: () {
                  HapticFeedback.lightImpact();
                  widget.onBackToDashboard();
                },
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: tokens.surfaceElevated,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: tokens.border),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(
                        Icons.arrow_back_rounded,
                        size: 15,
                        color: tokens.textSecondary,
                      ),
                      const SizedBox(width: 5),
                      Text(
                        'Dashboard',
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                          color: tokens.textSecondary,
                        ),
                      ),
                      const SizedBox(width: 4),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 1),
                        decoration: BoxDecoration(
                          color: tokens.surface,
                          borderRadius: BorderRadius.circular(4),
                          border: Border.all(color: tokens.borderSubtle),
                        ),
                        child: Text(
                          'Esc',
                          style: mono(
                            fontSize: 8.5,
                            fontWeight: FontWeight.w700,
                            color: tokens.textTertiary,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const Spacer(),
              // Píldora de avance de la materia
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                decoration: BoxDecoration(
                  color: tokens.accentGreen.o(0.12),
                  borderRadius: BorderRadius.circular(999),
                  border: Border.all(color: tokens.accentGreen.o(0.35)),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Dot(color: tokens.accentGreen, size: 6),
                    const SizedBox(width: 6),
                    Text(
                      'Avance: $progress%',
                      style: mono(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        color: tokens.accentGreen,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),

          // 2. Información de la Asignatura
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      '${subject.codigo} • CUATRIMESTRE ${subject.cuatrimestre} • ${subject.creditos} CRÉDITOS',
                      style: mono(
                        fontSize: 10,
                        fontWeight: FontWeight.w600,
                        letterSpacing: 0.9,
                        color: tokens.textSecondary,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      subject.nombre,
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.3,
                        color: tokens.textPrimary,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),

          // 3. Selector Cupertino si es Asignatura de Inglés
          if (isIngles) ...[
            SizedBox(
              width: double.infinity,
              child: CupertinoSlidingSegmentedControl<String>(
                backgroundColor: tokens.surfaceElevated,
                thumbColor: tokens.surface,
                groupValue: _activeEnglishBranch,
                onValueChanged: (branch) {
                  if (branch == null || branch == _activeEnglishBranch) return;
                  HapticFeedback.selectionClick();
                  setState(() {
                    _activeEnglishBranch = branch;
                    final branchTopics = subject.temasPorModalidad(branch);
                    if (branchTopics.isNotEmpty) {
                      _selectedTopicNumber = branchTopics.first.numeroTema;
                    }
                  });
                },
                children: {
                  'general': Padding(
                    padding: const EdgeInsets.symmetric(vertical: 6, horizontal: 8),
                    child: Text(
                      'Inglés General (Slides)',
                      style: TextStyle(
                        fontSize: 11.5,
                        fontWeight: _activeEnglishBranch == 'general'
                            ? FontWeight.w700
                            : FontWeight.w500,
                        color: _activeEnglishBranch == 'general'
                            ? tokens.accentGreen
                            : tokens.textSecondary,
                      ),
                    ),
                  ),
                  'notacion_ingenieria': Padding(
                    padding: const EdgeInsets.symmetric(vertical: 6, horizontal: 8),
                    child: Text(
                      'Notación de Ingeniería (KaTeX)',
                      style: TextStyle(
                        fontSize: 11.5,
                        fontWeight: _activeEnglishBranch == 'notacion_ingenieria'
                            ? FontWeight.w700
                            : FontWeight.w500,
                        color: _activeEnglishBranch == 'notacion_ingenieria'
                            ? tokens.accentIndigo
                            : tokens.textSecondary,
                      ),
                    ),
                  ),
                },
              ),
            ),
            const SizedBox(height: 12),
          ],

          // 4. Selector Horizontal de Temas
          if (temasDisponibles.isNotEmpty) ...[
            SizedBox(
              height: 30,
              child: ListView.separated(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                itemCount: temasDisponibles.length,
                separatorBuilder: (_, __) => const SizedBox(width: 6),
                itemBuilder: (context, index) {
                  final t = temasDisponibles[index];
                  final isSelected = t.numeroTema == _selectedTopicNumber;
                  final accent = t.esNotacionIngenieria
                      ? tokens.accentIndigo
                      : tokens.accentGreen;

                  return TapScale(
                    onTap: () {
                      HapticFeedback.selectionClick();
                      setState(() => _selectedTopicNumber = t.numeroTema);
                    },
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 180),
                      padding: const EdgeInsets.symmetric(horizontal: 10),
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: isSelected ? accent : tokens.surfaceElevated,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(
                          color: isSelected ? accent : tokens.border,
                          width: 1,
                        ),
                      ),
                      child: Text(
                        t.badgeTema,
                        style: mono(
                          fontSize: 10.5,
                          fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                          color: isSelected
                              ? (t.esNotacionIngenieria
                                  ? Colors.white
                                  : (tokens.isDark ? Colors.black : Colors.white))
                              : tokens.textSecondary,
                        ),
                      ),
                    ),
                  );
                },
              ),
            ),
            const SizedBox(height: 14),
          ],

          // 5. Contenido Desplazable del Tema Seleccionado (Scroll interno suave)
          Expanded(
            child: currentTema == null
                ? Center(
                    child: Text(
                      'No hay información para este tema',
                      style: TextStyle(color: tokens.textSecondary),
                    ),
                  )
                : SingleChildScrollView(
                    physics: const BouncingScrollPhysics(),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        // Título del Tema
                        Container(
                          padding: const EdgeInsets.all(14),
                          decoration: BoxDecoration(
                            color: tokens.surfaceElevated,
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(color: tokens.border),
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  Text(
                                    currentTema.etiquetaCorte.toUpperCase(),
                                    style: mono(
                                      fontSize: 9.5,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 0.8,
                                      color: tokens.accentGreen,
                                    ),
                                  ),
                                  const Spacer(),
                                  Text(
                                    currentTema.badgeTema,
                                    style: mono(
                                      fontSize: 10,
                                      fontWeight: FontWeight.w600,
                                      color: tokens.textSecondary,
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 6),
                              Text(
                                currentTema.titulo,
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w700,
                                  letterSpacing: -0.2,
                                  color: tokens.textPrimary,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 12),

                        // Tarjeta: OBJETIVO
                        if (currentTema.objetivo.isNotEmpty) ...[
                          _ModularTopicCard(
                            label: 'OBJETIVO',
                            body: currentTema.objetivo,
                            tokens: tokens,
                          ),
                          const SizedBox(height: 12),
                        ],

                        // Contenido Condicional: Slides vs KaTeX
                        if (currentTema.esInglesGeneral) ...[
                          MinimalSlideViewer(
                            temaId: '${subject.codigo}_t${currentTema.numeroTema}',
                            codigoAsignatura: subject.codigo,
                            nombreAsignatura: subject.nombre,
                            numeroTema: currentTema.numeroTema,
                            tituloTema: currentTema.titulo,
                            slides: currentTema.slides,
                          ),
                          const SizedBox(height: 12),
                        ] else ...[
                          KatexFormulaCard(
                            latex: currentTema.conceptoClaveLatex,
                            label: currentTema.esNotacionIngenieria
                                ? 'CONCEPTO CLAVE (KaTeX)'
                                : 'CONCEPTO CLAVE',
                          ),
                          const SizedBox(height: 12),
                          if (currentTema.verbalizacionIngles.trim().isNotEmpty) ...[
                            Container(
                              padding: const EdgeInsets.all(14),
                              decoration: BoxDecoration(
                                color: tokens.surfaceElevated,
                                borderRadius: BorderRadius.circular(16),
                                border: Border.all(
                                  color: tokens.accentGreen.o(0.35),
                                ),
                              ),
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Row(
                                    children: [
                                      Icon(
                                        Icons.record_voice_over_rounded,
                                        size: 15,
                                        color: tokens.accentGreen,
                                      ),
                                      const SizedBox(width: 7),
                                      Text(
                                        'PRONUNCIACIÓN Y LECTURA EN INGLÉS',
                                        style: mono(
                                          fontSize: 9.5,
                                          fontWeight: FontWeight.w700,
                                          letterSpacing: 0.8,
                                          color: tokens.accentGreen,
                                        ),
                                      ),
                                    ],
                                  ),
                                  const SizedBox(height: 8),
                                  Text(
                                    currentTema.verbalizacionIngles,
                                    style: TextStyle(
                                      fontSize: 13,
                                      height: 1.45,
                                      fontWeight: FontWeight.w500,
                                      color: tokens.textPrimary,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 12),
                          ],
                        ],

                        // Tarjeta: EJEMPLO DE CÁTEDRA
                        if (currentTema.ejemplo.isNotEmpty) ...[
                          _ModularTopicCard(
                            label: 'EJEMPLO DE CÁTEDRA',
                            body: currentTema.ejemplo,
                            tokens: tokens,
                          ),
                          const SizedBox(height: 12),
                        ],

                        // Tarjeta: BLOQUE SUGERIDO
                        if (currentTema.bloqueSugerido.isNotEmpty) ...[
                          Container(
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              color: tokens.surfaceElevated,
                              borderRadius: BorderRadius.circular(16),
                              border: Border.all(
                                color: tokens.accentIndigo.o(0.4),
                              ),
                            ),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    Dot(color: tokens.accentIndigo, size: 6.5),
                                    const SizedBox(width: 6),
                                    Text(
                                      'BLOQUE DE ESTUDIO SUGERIDO',
                                      style: mono(
                                        fontSize: 9.5,
                                        fontWeight: FontWeight.w700,
                                        letterSpacing: 0.8,
                                        color: tokens.accentIndigo,
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 8),
                                Text(
                                  currentTema.bloqueSugerido,
                                  style: TextStyle(
                                    fontSize: 13,
                                    height: 1.4,
                                    color: tokens.textSecondary,
                                  ),
                                ),
                                if (session != null) ...[
                                  const SizedBox(height: 10),
                                  Row(
                                    children: [
                                      TapScale(
                                        onTap: () async {
                                          HapticFeedback.lightImpact();
                                          await session.completeStudyBlock(
                                            codigoMateria: subject.codigo,
                                          );
                                          if (context.mounted) {
                                            showIosToast(
                                              context,
                                              '+10% de avance en ${subject.nombre}',
                                              accentColor: tokens.accentGreen,
                                            );
                                          }
                                        },
                                        child: Container(
                                          padding: const EdgeInsets.symmetric(
                                            horizontal: 14,
                                            vertical: 8,
                                          ),
                                          decoration: BoxDecoration(
                                            color: tokens.accentIndigo,
                                            borderRadius: BorderRadius.circular(10),
                                          ),
                                          child: const Text(
                                            'Completar bloque (+10%)',
                                            style: TextStyle(
                                              fontSize: 11.5,
                                              fontWeight: FontWeight.w600,
                                              color: Colors.white,
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ],
                              ],
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
          ),
        ],
      ),
    );
  }
}

class _ModularTopicCard extends StatelessWidget {
  const _ModularTopicCard({
    required this.label,
    required this.body,
    required this.tokens,
  });

  final String label;
  final String body;
  final DesktopThemeTokens tokens;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: tokens.surfaceElevated,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: tokens.border),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            label,
            style: mono(
              fontSize: 9.5,
              fontWeight: FontWeight.w700,
              letterSpacing: 0.9,
              color: tokens.textSecondary,
            ),
          ),
          const SizedBox(height: 6),
          Text(
            body,
            style: TextStyle(
              fontSize: 13,
              height: 1.45,
              color: tokens.textPrimary,
            ),
          ),
        ],
      ),
    );
  }
}
