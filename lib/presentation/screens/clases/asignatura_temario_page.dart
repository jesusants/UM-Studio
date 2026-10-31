import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/institutional_validator.dart';
import '../../../data/models/curriculum_models.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';
import '../clase_viva/clase_viva_page.dart';

/// Pantalla de Temario Oficial de una Asignatura con transición elástica iOS,
/// intercambiador interno para los 5 niveles de Inglés (`Inglés General` vs
/// `Notación de Ingeniería`), filtro por Cortes académicos y registro
/// sincronizado en GitHub del `(Último revisado)`.
class AsignaturaTemarioPage extends StatefulWidget {
  const AsignaturaTemarioPage({
    super.key,
    required this.asignatura,
  });

  final AsignaturaModel asignatura;

  /// Transición suave estilo iOS (deslizamiento lateral sutil + escala elástica + fade).
  static Route<void> route(AsignaturaModel asignatura) {
    return PageRouteBuilder<void>(
      transitionDuration: const Duration(milliseconds: 340),
      reverseTransitionDuration: const Duration(milliseconds: 270),
      pageBuilder: (_, __, ___) => AsignaturaTemarioPage(
        asignatura: asignatura,
      ),
      transitionsBuilder: (_, animation, secondaryAnimation, child) {
        final primary = CurvedAnimation(
          parent: animation,
          curve: kIosSpring,
          reverseCurve: kIosSpring.flipped,
        );
        return SlideTransition(
          position: Tween<Offset>(
            begin: const Offset(0.14, 0.02),
            end: Offset.zero,
          ).animate(primary),
          child: ScaleTransition(
            scale: Tween<double>(begin: 0.96, end: 1.0).animate(primary),
            child: FadeTransition(
              opacity: CurvedAnimation(
                parent: animation,
                curve: Curves.easeOutCubic,
              ),
              child: child,
            ),
          ),
        );
      },
    );
  }

  @override
  State<AsignaturaTemarioPage> createState() => _AsignaturaTemarioPageState();
}

class _AsignaturaTemarioPageState extends State<AsignaturaTemarioPage> {
  String _englishModalidad = 'general';
  int _selectedCorte = 0;

  AsignaturaModel get asignatura => widget.asignatura;

  void _openTopic(
    BuildContext context,
    InstitutionalSessionController? session,
    TemaClaseVivaModel tema,
  ) {
    HapticFeedback.lightImpact();
    session?.markTopicReviewed(
      codigoMateria: asignatura.codigo,
      numeroTema: tema.numeroTema,
    );

    final topicKey = tema.numeroTema <= 1
        ? asignatura.codigo
        : '${asignatura.codigo}_t${tema.numeroTema}';

    Navigator.of(context).push(ClaseVivaPage.route(topicKey));
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.of(context).isDark;
    final session = SessionScope.maybeOf(context);
    final lastReviewedNum = session?.lastReviewedTopicFor(asignatura.codigo);
    final isPinned =
        session?.progresoMaterias.containsKey(asignatura.codigo) ?? false;
    final accent = asignatura.accentColor;

    final visibleTemas = asignatura.temasPorCorte(
      _selectedCorte,
      modalidad: asignatura.esIngles ? _englishModalidad : null,
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: isDark ? SystemUiOverlayStyle.light : SystemUiOverlayStyle.dark,
      child: Scaffold(
        backgroundColor: p.background,
        body: SafeArea(
          bottom: false,
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(
                maxWidth: AppConstants.maxPhoneViewportWidth,
              ),
              child: Column(
                children: [
                  // Barra superior minimalista iOS
                  Container(
                    padding: const EdgeInsets.fromLTRB(16, 10, 16, 12),
                    decoration: BoxDecoration(
                      color: p.background,
                      border: Border(
                        bottom: BorderSide(color: p.cardBorder, width: 1),
                      ),
                    ),
                    child: Row(
                      children: [
                        Expanded(
                          child: Align(
                            alignment: Alignment.centerLeft,
                            child: TapScale(
                              onTap: () => Navigator.of(context).pop(),
                              child: Padding(
                                padding: const EdgeInsets.symmetric(
                                  vertical: 2,
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Icon(
                                      Icons.chevron_left_rounded,
                                      size: 21,
                                      color: p.textSecondary,
                                    ),
                                    Text(
                                      'Clases',
                                      style: TextStyle(
                                        fontSize: 14,
                                        color: p.textSecondary,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                        Text(
                          'TEMARIO',
                          style: TextStyle(
                            fontSize: 13.5,
                            fontWeight: FontWeight.w600,
                            letterSpacing: 0.9,
                            color: p.textPrimary,
                          ),
                        ),
                        Expanded(
                          child: Align(
                            alignment: Alignment.centerRight,
                            child: Text(
                              'C${asignatura.cuatrimestre} • ${asignatura.creditos} cr',
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: mono(
                                fontSize: 11,
                                fontWeight: FontWeight.w600,
                                color: accent,
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),

                  // Contenido desplazable del temario
                  Expanded(
                    child: ListView(
                      physics: const BouncingScrollPhysics(
                        parent: AlwaysScrollableScrollPhysics(),
                      ),
                      padding: const EdgeInsets.fromLTRB(18, 16, 18, 40),
                      children: [
                        // Encabezado de la Asignatura
                        IosCard(
                          radius: 20,
                          borderColor: accent.o(0.38),
                          padding: const EdgeInsets.all(16),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  Container(
                                    padding: const EdgeInsets.symmetric(
                                      horizontal: 8,
                                      vertical: 3,
                                    ),
                                    decoration: BoxDecoration(
                                      color: accent.o(0.14),
                                      borderRadius: BorderRadius.circular(7),
                                    ),
                                    child: Text(
                                      asignatura.categoriaLegible.toUpperCase(),
                                      style: mono(
                                        fontSize: 9.5,
                                        fontWeight: FontWeight.w600,
                                        color: accent,
                                      ),
                                    ),
                                  ),
                                  const SizedBox(width: 8),
                                  Expanded(
                                    child: Text(
                                      'Código ${asignatura.codigo}',
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                      style: mono(
                                        fontSize: 10.5,
                                        color: p.textTertiary,
                                      ),
                                    ),
                                  ),
                                  if (session != null)
                                    TapScale(
                                      onTap: () async {
                                        HapticFeedback.lightImpact();
                                        final pinned = await session
                                            .togglePinnedSubject(
                                          asignatura.codigo,
                                        );
                                        if (context.mounted) {
                                          showIosToast(
                                            context,
                                            pinned
                                                ? 'Agregada a Estudio'
                                                : 'Removida de fijadas',
                                          );
                                        }
                                      },
                                      child: Icon(
                                        isPinned
                                            ? Icons.bookmark_rounded
                                            : Icons.bookmark_border_rounded,
                                        size: 19,
                                        color:
                                            isPinned ? accent : p.textSecondary,
                                      ),
                                    ),
                                ],
                              ),
                              const SizedBox(height: 10),
                              Text(
                                asignatura.nombre,
                                style: TextStyle(
                                  fontSize: 21,
                                  height: 1.18,
                                  fontWeight: FontWeight.w700,
                                  letterSpacing: -0.4,
                                  color: p.textPrimary,
                                ),
                              ),
                              const SizedBox(height: 6),
                              Text(
                                asignatura.esIngles
                                    ? 'Cuatrimestre ${asignatura.cuatrimestre} • ${asignatura.temasInglesGeneral.length} temas Slides + ${asignatura.temasNotacionIngenieria.length} temas KaTeX'
                                    : 'Cuatrimestre ${asignatura.cuatrimestre} • ${asignatura.creditos} créditos • ${asignatura.temas.length} ${asignatura.temas.length == 1 ? 'tema disponible' : 'temas disponibles'}',
                                style: TextStyle(
                                  fontSize: 12,
                                  color: p.textSecondary,
                                ),
                              ),
                            ],
                          ),
                        ),

                        // Intercambiador Interno (Segmented Switcher) exclusivo para los 5 niveles de Inglés
                        if (asignatura.esIngles) ...[
                          const SizedBox(height: 14),
                          SizedBox(
                            width: double.infinity,
                            child: CupertinoSlidingSegmentedControl<String>(
                              key: const Key('temario_english_switcher'),
                              backgroundColor: p.card,
                              thumbColor: p.elevated,
                              groupValue: _englishModalidad,
                              onValueChanged: (value) {
                                if (value == null) return;
                                HapticFeedback.lightImpact();
                                setState(() {
                                  _englishModalidad = value;
                                  _selectedCorte = 0;
                                });
                              },
                              children: {
                                'general': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 6,
                                  ),
                                  child: Text(
                                    'Inglés General (Slides)',
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 11.5,
                                      fontWeight: _englishModalidad == 'general'
                                          ? FontWeight.w700
                                          : FontWeight.w500,
                                      color: _englishModalidad == 'general'
                                          ? p.green
                                          : p.textSecondary,
                                    ),
                                  ),
                                ),
                                'notacion_ingenieria': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 6,
                                  ),
                                  child: Text(
                                    'Notación de Ingeniería (KaTeX)',
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 11.5,
                                      fontWeight: _englishModalidad ==
                                              'notacion_ingenieria'
                                          ? FontWeight.w700
                                          : FontWeight.w500,
                                      color: _englishModalidad ==
                                              'notacion_ingenieria'
                                          ? p.indigo
                                          : p.textSecondary,
                                    ),
                                  ),
                                ),
                              },
                            ),
                          ),
                        ],

                        const SizedBox(height: 14),

                        // Filtro rápido por Cortes Académicos (Corte 1 - 30%, Corte 2 - 30%, Corte 3 - 40%)
                        SingleChildScrollView(
                          scrollDirection: Axis.horizontal,
                          physics: const BouncingScrollPhysics(),
                          child: Row(
                            children: [
                              for (final entry in const [
                                (0, 'Todos'),
                                (1, 'Corte 1 • 30%'),
                                (2, 'Corte 2 • 30%'),
                                (3, 'Corte 3 • 40%'),
                              ])
                                Padding(
                                  padding: const EdgeInsets.only(right: 8),
                                  child: TapScale(
                                    onTap: () {
                                      HapticFeedback.lightImpact();
                                      setState(
                                        () => _selectedCorte = entry.$1,
                                      );
                                    },
                                    child: AnimatedContainer(
                                      duration:
                                          const Duration(milliseconds: 180),
                                      padding: const EdgeInsets.symmetric(
                                        horizontal: 11,
                                        vertical: 5.5,
                                      ),
                                      decoration: BoxDecoration(
                                        color: _selectedCorte == entry.$1
                                            ? accent.o(0.18)
                                            : p.card,
                                        borderRadius:
                                            BorderRadius.circular(999),
                                        border: Border.all(
                                          color: _selectedCorte == entry.$1
                                              ? accent
                                              : p.cardBorder,
                                        ),
                                      ),
                                      child: Text(
                                        entry.$2,
                                        style: mono(
                                          fontSize: 10.5,
                                          fontWeight: FontWeight.w600,
                                          color: _selectedCorte == entry.$1
                                              ? accent
                                              : p.textSecondary,
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                            ],
                          ),
                        ),

                        const SizedBox(height: 16),

                        Row(
                          children: [
                            Expanded(
                              child: Text(
                                asignatura.esIngles
                                    ? (_englishModalidad == 'general'
                                        ? 'INGLÉS GENERAL • SLIDES'
                                        : 'NOTACIÓN TÉCNICA • KATEX')
                                    : 'TEMAS DISPONIBLES',
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: sectionMicroStyle(p),
                              ),
                            ),
                            Text(
                              '${visibleTemas.length} temas',
                              style: mono(
                                fontSize: 11,
                                color: p.textTertiary,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),

                        for (final tema in visibleTemas) ...[
                          _TemarioTopicCard(
                            tema: tema,
                            accentColor: asignatura.esIngles
                                ? (tema.esInglesGeneral ? p.green : p.indigo)
                                : accent,
                            isLastReviewed: lastReviewedNum == tema.numeroTema,
                            onTap: () => _openTopic(context, session, tema),
                          ),
                          const SizedBox(height: 12),
                        ],
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class _TemarioTopicCard extends StatelessWidget {
  const _TemarioTopicCard({
    required this.tema,
    required this.accentColor,
    required this.isLastReviewed,
    required this.onTap,
  });

  final TemaClaseVivaModel tema;
  final Color accentColor;
  final bool isLastReviewed;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final cleanLatex = InstitutionalValidator.sanitizeLatex(
      tema.conceptoClaveLatex,
    );

    return TapScale(
      onTap: onTap,
      child: IosCard(
        radius: 18,
        padding: const EdgeInsets.all(15),
        borderColor: isLastReviewed ? p.green.o(0.48) : p.cardBorder,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 9,
                    vertical: 3,
                  ),
                  decoration: BoxDecoration(
                    color: accentColor.o(0.13),
                    borderRadius: BorderRadius.circular(999),
                  ),
                  child: Text(
                    'Tema ${tema.numeroTema}',
                    style: mono(
                      fontSize: 10.5,
                      fontWeight: FontWeight.w600,
                      color: accentColor,
                    ),
                  ),
                ),
                const SizedBox(width: 6),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 7,
                    vertical: 2.5,
                  ),
                  decoration: BoxDecoration(
                    color: p.elevated,
                    borderRadius: BorderRadius.circular(999),
                    border: Border.all(color: p.cardBorder),
                  ),
                  child: Text(
                    tema.etiquetaCorteCorta,
                    style: mono(
                      fontSize: 9.5,
                      color: p.textSecondary,
                    ),
                  ),
                ),
                if (isLastReviewed) ...[
                  const SizedBox(width: 7),
                  Dot(color: p.green, size: 5.5),
                  const SizedBox(width: 5),
                  Expanded(
                    child: Text(
                      '(Último revisado)',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w500,
                        color: p.green,
                      ),
                    ),
                  ),
                ] else
                  const Spacer(),
                Icon(
                  Icons.chevron_right_rounded,
                  size: 19,
                  color: isLastReviewed ? p.green : p.textSecondary,
                ),
              ],
            ),
            const SizedBox(height: 9),
            Text(
              tema.titulo,
              style: TextStyle(
                fontSize: 15.5,
                fontWeight: FontWeight.w600,
                height: 1.25,
                color: p.textPrimary,
              ),
            ),
            const SizedBox(height: 6),
            Text(
              tema.objetivo,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 12.5,
                height: 1.4,
                color: p.textSecondary,
              ),
            ),
            const SizedBox(height: 11),

            // Si es Inglés General: muestra previsualización minimalista de Slides (sin KaTeX)
            if (tema.esInglesGeneral)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(
                  horizontal: 11,
                  vertical: 8,
                ),
                decoration: BoxDecoration(
                  color: p.background.o(0.42),
                  borderRadius: BorderRadius.circular(11),
                  border: Border.all(color: p.cardBorder),
                ),
                child: Row(
                  children: [
                    Icon(
                      Icons.slideshow_rounded,
                      size: 15,
                      color: p.green,
                    ),
                    const SizedBox(width: 7),
                    Expanded(
                      child: Text(
                        '${tema.slides.length} diapositivas interactivas • Exportable PDF (<1.2 MB)',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: mono(
                          fontSize: 10.5,
                          fontWeight: FontWeight.w500,
                          color: p.textPrimary,
                        ),
                      ),
                    ),
                  ],
                ),
              )
            else if (cleanLatex.isNotEmpty)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(
                  horizontal: 11,
                  vertical: 8,
                ),
                decoration: BoxDecoration(
                  color: p.background.o(0.42),
                  borderRadius: BorderRadius.circular(11),
                  border: Border.all(color: p.cardBorder),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SingleChildScrollView(
                      scrollDirection: Axis.horizontal,
                      physics: const BouncingScrollPhysics(),
                      child: Math.tex(
                        cleanLatex,
                        mathStyle: MathStyle.text,
                        textStyle: TextStyle(
                          fontSize: 13.5,
                          color: p.textPrimary,
                        ),
                        onErrorFallback: (_) => Text(
                          cleanLatex,
                          style: mono(fontSize: 12, color: p.textPrimary),
                        ),
                      ),
                    ),
                    if (tema.esNotacionIngenieria &&
                        tema.verbalizacionIngles.isNotEmpty) ...[
                      const SizedBox(height: 6),
                      Text(
                        tema.verbalizacionIngles,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: TextStyle(
                          fontSize: 11,
                          fontStyle: FontStyle.italic,
                          color: p.textSecondary,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }
}
