import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/institutional_validator.dart';
import '../../../data/models/curriculum_models.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/clase_magistral_adjuntos_widget.dart';
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
  String _activeSection = 'temario';
  String _englishModalidad = 'general';
  int _selectedCorte = 0;
  int _selectedMagistralCorte = 0;
  final Set<int> _expandedMagistralAdjuntos = {};

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
    final visibleMagistrales = asignatura.clasesMagistralesPorCorte(
      _selectedMagistralCorte,
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
                          _activeSection == 'magistrales'
                              ? 'CÁTEDRAS MAGISTRALES'
                              : 'TEMARIO',
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

                        // Segmented Switcher: Temario vs Clases Magistrales (o 3 opciones en Inglés)
                        if (asignatura.esIngles) ...[
                          const SizedBox(height: 14),
                          SizedBox(
                            width: double.infinity,
                            child: CupertinoSlidingSegmentedControl<String>(
                              key: const Key('temario_english_switcher'),
                              backgroundColor: p.card,
                              thumbColor: p.elevated,
                              groupValue: _activeSection == 'magistrales'
                                  ? 'magistrales'
                                  : _englishModalidad,
                              onValueChanged: (value) {
                                if (value == null) return;
                                HapticFeedback.lightImpact();
                                setState(() {
                                  if (value == 'magistrales') {
                                    _activeSection = 'magistrales';
                                  } else {
                                    _activeSection = 'temario';
                                    _englishModalidad = value;
                                  }
                                  _selectedCorte = 0;
                                  _selectedMagistralCorte = 0;
                                });
                              },
                              children: {
                                'general': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 4,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Text(
                                      'General (Slides)',
                                      maxLines: 1,
                                      textAlign: TextAlign.center,
                                      style: TextStyle(
                                        fontSize: 11.5,
                                        fontWeight: (_activeSection == 'temario' &&
                                                _englishModalidad == 'general')
                                            ? FontWeight.w700
                                            : FontWeight.w500,
                                        color: (_activeSection == 'temario' &&
                                                _englishModalidad == 'general')
                                            ? p.green
                                            : p.textSecondary,
                                      ),
                                    ),
                                  ),
                                ),
                                'notacion_ingenieria': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 4,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Text(
                                      'Notación (KaTeX)',
                                      maxLines: 1,
                                      textAlign: TextAlign.center,
                                      style: TextStyle(
                                        fontSize: 11.5,
                                        fontWeight: (_activeSection == 'temario' &&
                                                _englishModalidad ==
                                                    'notacion_ingenieria')
                                            ? FontWeight.w700
                                            : FontWeight.w500,
                                        color: (_activeSection == 'temario' &&
                                                _englishModalidad ==
                                                    'notacion_ingenieria')
                                            ? p.indigo
                                            : p.textSecondary,
                                      ),
                                    ),
                                  ),
                                ),
                                'magistrales': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 4,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Row(
                                      mainAxisSize: MainAxisSize.min,
                                      mainAxisAlignment: MainAxisAlignment.center,
                                      children: [
                                        Icon(
                                          Icons.school_rounded,
                                          size: 13,
                                          color: _activeSection == 'magistrales'
                                              ? p.indigo
                                              : p.textSecondary,
                                        ),
                                        const SizedBox(width: 4),
                                        Text(
                                          asignatura.tieneClasesMagistrales
                                              ? 'Cátedras (${asignatura.clasesMagistrales.length})'
                                              : 'Cátedras',
                                          maxLines: 1,
                                          textAlign: TextAlign.center,
                                          style: TextStyle(
                                            fontSize: 11.5,
                                            fontWeight:
                                                _activeSection == 'magistrales'
                                                    ? FontWeight.w700
                                                    : FontWeight.w500,
                                            color:
                                                _activeSection == 'magistrales'
                                                    ? p.indigo
                                                    : p.textSecondary,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              },
                            ),
                          ),
                        ] else ...[
                          const SizedBox(height: 14),
                          SizedBox(
                            width: double.infinity,
                            child: CupertinoSlidingSegmentedControl<String>(
                              key: const Key('temario_section_switcher'),
                              backgroundColor: p.card,
                              thumbColor: p.elevated,
                              groupValue: _activeSection,
                              onValueChanged: (value) {
                                if (value == null) return;
                                HapticFeedback.lightImpact();
                                setState(() {
                                  _activeSection = value;
                                  _selectedCorte = 0;
                                  _selectedMagistralCorte = 0;
                                });
                              },
                              children: {
                                'temario': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 8,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Row(
                                      mainAxisSize: MainAxisSize.min,
                                      mainAxisAlignment: MainAxisAlignment.center,
                                      children: [
                                        Icon(
                                          Icons.menu_book_rounded,
                                          size: 14,
                                          color: _activeSection == 'temario'
                                              ? accent
                                              : p.textSecondary,
                                        ),
                                        const SizedBox(width: 6),
                                        Text(
                                          'Temario Oficial (${asignatura.temas.length})',
                                          maxLines: 1,
                                          style: TextStyle(
                                            fontSize: 12,
                                            fontWeight: _activeSection == 'temario'
                                                ? FontWeight.w700
                                                : FontWeight.w500,
                                            color: _activeSection == 'temario'
                                                ? accent
                                                : p.textSecondary,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                                'magistrales': Padding(
                                  padding: const EdgeInsets.symmetric(
                                    vertical: 8,
                                    horizontal: 8,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Row(
                                      mainAxisSize: MainAxisSize.min,
                                      mainAxisAlignment: MainAxisAlignment.center,
                                      children: [
                                        Icon(
                                          Icons.school_rounded,
                                          size: 14,
                                          color: _activeSection == 'magistrales'
                                              ? p.indigo
                                              : p.textSecondary,
                                        ),
                                        const SizedBox(width: 6),
                                        Text(
                                          asignatura.tieneClasesMagistrales
                                              ? 'Clases Magistrales (${asignatura.clasesMagistrales.length})'
                                              : 'Clases Magistrales',
                                          maxLines: 1,
                                          style: TextStyle(
                                            fontSize: 12,
                                            fontWeight:
                                                _activeSection == 'magistrales'
                                                    ? FontWeight.w700
                                                    : FontWeight.w500,
                                            color:
                                                _activeSection == 'magistrales'
                                                    ? p.indigo
                                                    : p.textSecondary,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              },
                            ),
                          ),
                        ],

                        if (_activeSection == 'temario') ...[
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
                        ] else ...[
                          // Sección: Clases Magistrales
                          const SizedBox(height: 14),

                          if (asignatura.clasesMagistrales.isEmpty) ...[
                            IosCard(
                              radius: 20,
                              padding: const EdgeInsets.all(20),
                              borderColor: p.indigo.o(0.25),
                              child: Column(
                                children: [
                                  Container(
                                    padding: const EdgeInsets.all(14),
                                    decoration: BoxDecoration(
                                      color: p.indigo.o(0.12),
                                      shape: BoxShape.circle,
                                    ),
                                    child: Icon(
                                      Icons.school_outlined,
                                      size: 32,
                                      color: p.indigo,
                                    ),
                                  ),
                                  const SizedBox(height: 14),
                                  Text(
                                    'Aún no hay cátedras magistrales registradas',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 15.5,
                                      fontWeight: FontWeight.w700,
                                      color: p.textPrimary,
                                    ),
                                  ),
                                  const SizedBox(height: 6),
                                  Text(
                                    'Esta materia no cuenta con láminas de cátedra predefinidas por el cuerpo docente. Sin embargo, puedes adjuntar tus fotos de tablero, guías, talleres en PDF o apuntes personales aquí abajo:',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      fontSize: 12.5,
                                      height: 1.45,
                                      color: p.textSecondary,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 16),
                            ClaseMagistralAdjuntosWidget(
                              temaKey: '${asignatura.codigo}_magistrales',
                              tituloClase: '${asignatura.nombre} - Cátedras',
                              accentColor: p.indigo,
                            ),
                          ] else ...[
                            // Filtro por Cortes para Clases Magistrales
                            SingleChildScrollView(
                              scrollDirection: Axis.horizontal,
                              physics: const BouncingScrollPhysics(),
                              child: Row(
                                children: [
                                  for (final entry in const [
                                    (0, 'Todas'),
                                    (1, 'Corte 1'),
                                    (2, 'Corte 2'),
                                    (3, 'Corte 3'),
                                  ])
                                    Padding(
                                      padding: const EdgeInsets.only(right: 8),
                                      child: TapScale(
                                        onTap: () {
                                          HapticFeedback.lightImpact();
                                          setState(
                                            () => _selectedMagistralCorte = entry.$1,
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
                                            color: _selectedMagistralCorte == entry.$1
                                                ? p.indigo.o(0.18)
                                                : p.card,
                                            borderRadius:
                                                BorderRadius.circular(999),
                                            border: Border.all(
                                              color: _selectedMagistralCorte == entry.$1
                                                  ? p.indigo
                                                  : p.cardBorder,
                                            ),
                                          ),
                                          child: Text(
                                            entry.$2,
                                            style: mono(
                                              fontSize: 10.5,
                                              fontWeight: FontWeight.w600,
                                              color: _selectedMagistralCorte == entry.$1
                                                  ? p.indigo
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
                                    'CÁTEDRAS MAGISTRALES',
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: sectionMicroStyle(p),
                                  ),
                                ),
                                Text(
                                  '${visibleMagistrales.length} cátedras',
                                  style: mono(
                                    fontSize: 11,
                                    color: p.textTertiary,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 10),

                            for (final magistral in visibleMagistrales) ...[
                              _MagistralCard(
                                magistral: magistral,
                                codigoAsignatura: asignatura.codigo,
                                isExpanded: _expandedMagistralAdjuntos
                                    .contains(magistral.numeroTema),
                                onToggleExpand: () {
                                  HapticFeedback.lightImpact();
                                  setState(() {
                                    if (_expandedMagistralAdjuntos
                                        .contains(magistral.numeroTema)) {
                                      _expandedMagistralAdjuntos
                                          .remove(magistral.numeroTema);
                                    } else {
                                      _expandedMagistralAdjuntos
                                          .add(magistral.numeroTema);
                                    }
                                  });
                                },
                                onOpenClaseViva: () {
                                  HapticFeedback.lightImpact();
                                  final topicKey =
                                      '${asignatura.codigo}_magistral_${magistral.numeroTema}';
                                  Navigator.of(context)
                                      .push(ClaseVivaPage.route(topicKey));
                                },
                              ),
                              const SizedBox(height: 12),
                            ],
                          ],
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

class _MagistralCard extends StatelessWidget {
  const _MagistralCard({
    required this.magistral,
    required this.codigoAsignatura,
    required this.isExpanded,
    required this.onToggleExpand,
    required this.onOpenClaseViva,
  });

  final TemaClaseVivaModel magistral;
  final String codigoAsignatura;
  final bool isExpanded;
  final VoidCallback onToggleExpand;
  final VoidCallback onOpenClaseViva;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final accent = p.indigo;
    final cleanLatex = InstitutionalValidator.sanitizeLatex(
      magistral.conceptoClaveLatex,
    );
    final temaKey = '${codigoAsignatura}_magistral_${magistral.numeroTema}';

    return IosCard(
      radius: 18,
      padding: const EdgeInsets.all(15),
      borderColor: accent.o(0.28),
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
                  color: accent.o(0.14),
                  borderRadius: BorderRadius.circular(999),
                ),
                child: Text(
                  'Cátedra ${magistral.numeroTema}',
                  style: mono(
                    fontSize: 10.5,
                    fontWeight: FontWeight.w700,
                    color: accent,
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
                  'Corte ${magistral.corte}',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w600,
                    color: p.textSecondary,
                  ),
                ),
              ),
              if (magistral.slides.isNotEmpty) ...[
                const SizedBox(width: 6),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 7,
                    vertical: 2.5,
                  ),
                  decoration: BoxDecoration(
                    color: p.green.o(0.12),
                    borderRadius: BorderRadius.circular(999),
                    border: Border.all(color: p.green.o(0.3)),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.slideshow_rounded, size: 11, color: p.green),
                      const SizedBox(width: 4),
                      Text(
                        '${magistral.slides.length} diapositivas',
                        style: mono(
                          fontSize: 9.5,
                          fontWeight: FontWeight.w600,
                          color: p.green,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ],
          ),
          const SizedBox(height: 9),
          Text(
            magistral.titulo,
            style: TextStyle(
              fontSize: 15.5,
              fontWeight: FontWeight.w700,
              height: 1.25,
              color: p.textPrimary,
            ),
          ),
          if (magistral.objetivo.isNotEmpty) ...[
            const SizedBox(height: 6),
            Text(
              magistral.objetivo,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 12.5,
                height: 1.4,
                color: p.textSecondary,
              ),
            ),
          ],
          if (cleanLatex.isNotEmpty) ...[
            const SizedBox(height: 10),
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
              child: SingleChildScrollView(
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
            ),
          ],
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(
                child: TapScale(
                  onTap: onOpenClaseViva,
                  child: Container(
                    padding: const EdgeInsets.symmetric(vertical: 8.5),
                    decoration: BoxDecoration(
                      color: accent,
                      borderRadius: BorderRadius.circular(10),
                    ),
                    alignment: Alignment.center,
                    child: const Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(
                          Icons.slideshow_rounded,
                          size: 15,
                          color: Colors.white,
                        ),
                        SizedBox(width: 6),
                        Text(
                          'Ver Clase Viva / Slides',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: Colors.white,
                          ),
                        ),
                        SizedBox(width: 4),
                        Icon(
                          Icons.arrow_outward_rounded,
                          size: 13,
                          color: Colors.white70,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 8),
              TapScale(
                onTap: onToggleExpand,
                child: Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 8.5,
                  ),
                  decoration: BoxDecoration(
                    color: isExpanded ? accent.o(0.15) : p.elevated,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(
                      color: isExpanded ? accent : p.cardBorder,
                    ),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(
                        Icons.attach_file_rounded,
                        size: 14,
                        color: isExpanded ? accent : p.textSecondary,
                      ),
                      const SizedBox(width: 4),
                      Text(
                        'Adjuntos',
                        style: TextStyle(
                          fontSize: 11.5,
                          fontWeight: FontWeight.w600,
                          color: isExpanded ? accent : p.textSecondary,
                        ),
                      ),
                      const SizedBox(width: 2),
                      Icon(
                        isExpanded
                            ? Icons.keyboard_arrow_up_rounded
                            : Icons.keyboard_arrow_down_rounded,
                        size: 16,
                        color: isExpanded ? accent : p.textSecondary,
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
          if (isExpanded) ...[
            const SizedBox(height: 12),
            ClaseMagistralAdjuntosWidget(
              temaKey: temaKey,
              tituloClase: magistral.titulo,
              accentColor: accent,
            ),
          ],
        ],
      ),
    );
  }
}
