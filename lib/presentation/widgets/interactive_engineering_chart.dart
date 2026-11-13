import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/theme/app_theme.dart';
import 'ios_primitives.dart';
import 'lab/painters_cuatrimestre_1_2.dart';
import 'lab/painters_cuatrimestre_3_4.dart';
import 'lab/subject_lab_registry.dart';

/// Enum legado conservado por compatibilidad con llamadas externas.
enum EngineeringChartMode {
  acPhasor,
  calculusIntegral,
  thermoSolar,
}

/// Abre el Laboratorio Gráfico Interactivo como modal móvil (height: 75%) sin overflows.
Future<void> showSubjectLabBottomSheet({
  required BuildContext context,
  String asignaturaCodigo = '',
  required String asignaturaNombre,
  required String temaTitulo,
  String explicitHint = '',
}) async {
  if (!SubjectLabRegistry.hasLabsForSubject(
    codigo: asignaturaCodigo,
    nombre: asignaturaNombre,
  )) {
    return;
  }

  await showModalBottomSheet<void>(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    builder: (ctx) {
      final p = ctx.palette;
      final h = MediaQuery.sizeOf(ctx).height * 0.75;
      return Container(
        height: h,
        decoration: BoxDecoration(
          color: p.background,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
          border: Border.all(color: p.strongBorder),
        ),
        child: Column(
          children: [
            const SizedBox(height: 10),
            Container(
              width: 38,
              height: 4,
              decoration: BoxDecoration(
                color: p.textSecondary.withValues(alpha: 0.35),
                borderRadius: BorderRadius.circular(99),
              ),
            ),
            const SizedBox(height: 8),
            Expanded(
              child: SingleChildScrollView(
                physics: const BouncingScrollPhysics(),
                padding: const EdgeInsets.fromLTRB(14, 4, 14, 20),
                child: InteractiveEngineeringChart(
                  asignaturaCodigo: asignaturaCodigo,
                  asignaturaNombre: asignaturaNombre,
                  temaTitulo: temaTitulo,
                  explicitHint: explicitHint,
                ),
              ),
            ),
          ],
        ),
      );
    },
  );
}

class _SliderDef {
  const _SliderDef({
    required this.label,
    required this.min,
    required this.max,
    required this.value,
    required this.unit,
    required this.slot,
  });

  final String label;
  final double min;
  final double max;
  final double value;
  final String unit;
  final int slot; // 0 -> paramA, 1 -> paramB, 2 -> paramC
}

/// Laboratorio Gráfico Contextual por Materia y Simulaciones Animadas en Tiempo Real (60 FPS).
class InteractiveEngineeringChart extends StatefulWidget {
  const InteractiveEngineeringChart({
    super.key,
    this.asignaturaCodigo = '',
    required this.asignaturaNombre,
    required this.temaTitulo,
    this.explicitHint = '',
    this.compact = false,
  });

  final String asignaturaCodigo;
  final String asignaturaNombre;
  final String temaTitulo;
  final String explicitHint;
  final bool compact;

  @override
  State<InteractiveEngineeringChart> createState() =>
      _InteractiveEngineeringChartState();
}

class _InteractiveEngineeringChartState
    extends State<InteractiveEngineeringChart>
    with SingleTickerProviderStateMixin {
  SubjectLabConfig? _labConfig;
  late LabSimulatorDescriptor _activeSim;

  late final AnimationController _animController;
  Duration? _lastTickElapsed;
  double _simTimeSec = 0.0;
  bool _isPlaying = true;
  double _speedMultiplier = 1.0;

  double _paramA = 1.0;
  double _paramB = 1.0;
  double _paramC = 1.0;
  int _subMode = 0;
  Offset? _pointerNorm;

  final List<Offset> _customRegressionPoints = <Offset>[
    const Offset(0.12, 0.20),
    const Offset(0.25, 0.34),
    const Offset(0.39, 0.37),
    const Offset(0.54, 0.56),
    const Offset(0.68, 0.65),
    const Offset(0.83, 0.80),
  ];

  static const List<LabSimulatorDescriptor> _fallbackGeneralSims = [
    LabSimulatorDescriptor(
      id: LabSimId.fisicaMasaResorte,
      shortTitle: 'Masa-Resorte y Energía',
      fullTitle: 'Sistema Masa-Resorte y Conservación de la Energía',
      formulaBadge: 'E_m = ½mv² + ½kx² + E_dis',
      icon: Icons.compress_rounded,
      keywords: ['energia', 'resorte'],
    ),
  ];

  @override
  void initState() {
    super.initState();
    _resolveSubjectAndTopic();
    _animController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 3600),
    )..addListener(_onFrameTick);
    _animController.repeat();
  }

  @override
  void didUpdateWidget(covariant InteractiveEngineeringChart oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.asignaturaCodigo != widget.asignaturaCodigo ||
        oldWidget.asignaturaNombre != widget.asignaturaNombre ||
        oldWidget.temaTitulo != widget.temaTitulo ||
        oldWidget.explicitHint != widget.explicitHint) {
      _resolveSubjectAndTopic();
    }
  }

  @override
  void dispose() {
    _animController.removeListener(_onFrameTick);
    _animController.dispose();
    super.dispose();
  }

  void _onFrameTick() {
    if (!_isPlaying || !mounted) return;
    final elapsed = _animController.lastElapsedDuration;
    if (elapsed == null) return;
    final prev = _lastTickElapsed;
    _lastTickElapsed = elapsed;
    if (prev == null) return;

    final dtMicros = (elapsed - prev).inMicroseconds;
    if (dtMicros <= 0) return;
    final dtSec = (dtMicros / 1e6).clamp(0.0, 0.1);
    setState(() {
      _simTimeSec += dtSec * _speedMultiplier;
    });
  }

  void _resolveSubjectAndTopic() {
    final resolved = SubjectLabRegistry.resolve(
      codigo: widget.asignaturaCodigo,
      nombre: widget.asignaturaNombre,
      temaTitulo: widget.temaTitulo,
      explicitHint: widget.explicitHint,
    );
    _labConfig = resolved;
    _activeSim = resolved?.initialSimulator ?? _fallbackGeneralSims.first;
    _applyDefaultsForSimulator(_activeSim.id);
  }

  void _selectSimulator(LabSimulatorDescriptor sim) {
    HapticFeedback.selectionClick();
    setState(() {
      _activeSim = sim;
      _simTimeSec = 0.0;
      _lastTickElapsed = null;
      _pointerNorm = null;
      _applyDefaultsForSimulator(sim.id);
    });
  }

  void _togglePlayPause() {
    HapticFeedback.lightImpact();
    setState(() {
      _isPlaying = !_isPlaying;
      _lastTickElapsed = null;
      if (_isPlaying) {
        _animController.repeat();
      } else {
        _animController.stop();
      }
    });
  }

  void _resetSimulation() {
    HapticFeedback.mediumImpact();
    setState(() {
      _simTimeSec = 0.0;
      _lastTickElapsed = null;
      _applyDefaultsForSimulator(_activeSim.id);
      if (!_isPlaying) {
        _isPlaying = true;
        _animController.repeat();
      }
    });
  }

  void _applyDefaultsForSimulator(LabSimId id) {
    _subMode = 0;
    switch (id) {
      case LabSimId.calcDerivadaTangente:
        _paramA = 0.0;
        _paramB = 1.3;
        _paramC = 1.0;
        break;
      case LabSimId.calcLimites:
        _paramA = 0.2;
        _paramB = 1.8;
        _paramC = 1.0;
        break;
      case LabSimId.algebraTransformaciones2D:
        _paramA = 1.4;
        _paramB = 0.6;
        _paramC = 0.3;
        break;
      case LabSimId.progOrdenamiento:
        _paramA = 12.0;
        _paramB = 1.2;
        _paramC = 1.0;
        break;
      case LabSimId.progRegresionLineal:
        _paramA = 0.55;
        _paramB = 1.0;
        _paramC = 1.0;
        break;
      case LabSimId.introFlujoEnergetico:
        _paramA = 500.0;
        _paramB = 68.0;
        _paramC = 1.0;
        break;
      case LabSimId.fisicaMasaResorte:
        _paramA = 2.0;
        _paramB = 80.0;
        _paramC = 0.08;
        break;
      case LabSimId.fisicaTiroParabolico:
        _paramA = 45.0;
        _paramB = 28.0;
        _paramC = 9.8;
        break;
      case LabSimId.fisicaPlanoInclinadoDcl:
        _paramA = 30.0;
        _paramB = 0.20;
        _paramC = 4.0;
        break;
      case LabSimId.fisicaColisiones1D:
        _paramA = 4.0;
        _paramB = 2.5;
        _paramC = 0.90;
        break;
      case LabSimId.integralRiemann:
        _paramA = 24.0;
        _paramB = 2.6;
        _paramC = 1.0;
        break;
      case LabSimId.integralSolidoRevolucion:
        _paramA = 2.5;
        _paramB = 14.0;
        _paramC = 1.0;
        break;
      case LabSimId.quimicaGasesIdeales:
        _paramA = 350.0;
        _paramB = 5.0;
        _paramC = 1.5;
        break;
      case LabSimId.elec1CircuitoDc:
        _paramA = 24.0;
        _paramB = 20.0;
        _paramC = 30.0;
        break;
      case LabSimId.ondasViajerasArmonicos:
        _paramA = 3.0;
        _paramB = 0.75;
        _paramC = 1.0;
        break;
      case LabSimId.ondasPenduloFase:
        _paramA = 1.4;
        _paramB = 35.0;
        _paramC = 1.0;
        break;
      case LabSimId.modelacionOsciladorAmortiguado:
        _paramA = 0.28;
        _paramB = 2.5;
        _paramC = 1.0;
        break;
      case LabSimId.elec2FasoresCa:
        _paramA = 120.0;
        _paramB = 30.0;
        _paramC = 60.0;
        break;
      case LabSimId.elec2TransitorioRcRl:
        _paramA = 1.0;
        _paramB = 24.0;
        _paramC = 1.0;
        break;
      case LabSimId.disenoProyeccion3D:
        _paramA = 15.0;
        _paramB = 25.0;
        _paramC = 0.0;
        break;
      case LabSimId.emLeyFaraday:
        _paramA = 6.0;
        _paramB = 1.2;
        _paramC = 1.0;
        break;
      case LabSimId.termoCicloPvPiston:
        _paramA = 750.0;
        _paramB = 6.0;
        _paramC = 1.0;
        break;
      case LabSimId.probTableroGalton:
        _paramA = 8.0;
        _paramB = 0.50;
        _paramC = 1.0;
        break;
      case LabSimId.hidraulicaVenturiBernoulli:
        _paramA = 0.55;
        _paramB = 2.8;
        _paramC = 1.0;
        break;
    }
  }

  LabSimParams get _currentParams => LabSimParams(
        timeSec: _simTimeSec,
        paramA: _paramA,
        paramB: _paramB,
        paramC: _paramC,
        subMode: _subMode,
        customPoints: _customRegressionPoints,
        pointerNorm: _pointerNorm,
      );

  bool get _isCuatrimestre1Or2 {
    switch (_activeSim.id) {
      case LabSimId.calcDerivadaTangente:
      case LabSimId.calcLimites:
      case LabSimId.algebraTransformaciones2D:
      case LabSimId.progOrdenamiento:
      case LabSimId.progRegresionLineal:
      case LabSimId.introFlujoEnergetico:
      case LabSimId.fisicaMasaResorte:
      case LabSimId.fisicaTiroParabolico:
      case LabSimId.fisicaPlanoInclinadoDcl:
      case LabSimId.fisicaColisiones1D:
      case LabSimId.integralRiemann:
      case LabSimId.integralSolidoRevolucion:
      case LabSimId.quimicaGasesIdeales:
      case LabSimId.elec1CircuitoDc:
        return true;
      default:
        return false;
    }
  }

  void _handleCanvasTap(Offset localPos, Size size) {
    if (size.width <= 0 || size.height <= 0) return;
    final nx = (localPos.dx / size.width).clamp(0.05, 0.95);
    final ny = (1.0 - (localPos.dy / size.height)).clamp(0.05, 0.95);
    setState(() {
      _pointerNorm = Offset(nx, 1.0 - ny);
      if (_activeSim.id == LabSimId.progRegresionLineal) {
        if (_customRegressionPoints.length >= 16) {
          _customRegressionPoints.removeAt(0);
        }
        _customRegressionPoints.add(Offset(nx, ny));
        _simTimeSec = 0.1;
      } else if (_activeSim.id == LabSimId.elec2TransitorioRcRl) {
        _subMode = (_subMode + 1) % 2;
        _simTimeSec = 0.0;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    if (!SubjectLabRegistry.hasLabsForSubject(
      codigo: widget.asignaturaCodigo,
      nombre: widget.asignaturaNombre,
    )) {
      return const SizedBox.shrink();
    }

    final p = context.palette;
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final sims = _labConfig?.simulators ?? _fallbackGeneralSims;
    final subjectTitle = _labConfig?.subjectName ?? widget.asignaturaNombre;

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.strongBorder),
      ),
      child: Padding(
        padding: EdgeInsets.all(widget.compact ? 11 : 15),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _buildHeader(p, subjectTitle),
            if (sims.length > 1) ...[
              const SizedBox(height: 10),
              _buildSubjectSimulatorChips(p, sims),
            ],
            const SizedBox(height: 10),
            _buildUniversalMotionBar(p),
            const SizedBox(height: 10),
            _buildAnimatedCanvas(p, isDark),
            const SizedBox(height: 10),
            _buildFormulaAndSubModeRow(p),
            const SizedBox(height: 8),
            _buildParameterSliders(p),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader(AppPalette p, String subjectTitle) {
    return Row(
      children: [
        Container(
          width: 30,
          height: 30,
          decoration: BoxDecoration(
            color: p.indigo.o(0.14),
            borderRadius: BorderRadius.circular(9),
            border: Border.all(color: p.indigo.o(0.35)),
          ),
          child: Icon(_activeSim.icon, size: 16, color: p.indigo),
        ),
        const SizedBox(width: 9),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'LABORATORIO GRÁFICO INTERACTIVO • ${subjectTitle.toUpperCase()}',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: mono(
                  fontSize: 9.2,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.7,
                  color: p.indigo,
                ),
              ),
              const SizedBox(height: 1),
              Text(
                _activeSim.fullTitle,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w700,
                  color: p.textPrimary,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildSubjectSimulatorChips(
    AppPalette p,
    List<LabSimulatorDescriptor> sims,
  ) {
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      children: [
        for (final sim in sims)
          TapScale(
            onTap: () => _selectSimulator(sim),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 160),
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              decoration: BoxDecoration(
                color: _activeSim.id == sim.id ? p.indigo.o(0.18) : p.elevated,
                borderRadius: BorderRadius.circular(9),
                border: Border.all(
                  color: _activeSim.id == sim.id ? p.indigo : p.cardBorder,
                ),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(
                    sim.icon,
                    size: 13,
                    color: _activeSim.id == sim.id ? p.indigo : p.textSecondary,
                  ),
                  const SizedBox(width: 5),
                  Flexible(
                    child: Text(
                      sim.shortTitle,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: _activeSim.id == sim.id
                            ? FontWeight.w700
                            : FontWeight.w500,
                        color: _activeSim.id == sim.id
                            ? p.indigo
                            : p.textSecondary,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildUniversalMotionBar(AppPalette p) {
    final telemetry =
        LabTelemetryBuilder.buildReadout(_activeSim.id, _currentParams);

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 6),
      decoration: BoxDecoration(
        color: p.elevated,
        borderRadius: BorderRadius.circular(11),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              // Play / Pause [ ▶ / ⏸ ]
              TapScale(
                onTap: _togglePlayPause,
                child: Container(
                  width: 28,
                  height: 28,
                  decoration: BoxDecoration(
                    color: _isPlaying ? p.green.o(0.18) : p.indigo.o(0.18),
                    shape: BoxShape.circle,
                    border: Border.all(
                      color: _isPlaying ? p.green : p.indigo,
                    ),
                  ),
                  child: Icon(
                    _isPlaying ? Icons.pause_rounded : Icons.play_arrow_rounded,
                    size: 16,
                    color: _isPlaying ? p.green : p.indigo,
                  ),
                ),
              ),
              const SizedBox(width: 6),
              // Reset [ ↺ ]
              TapScale(
                onTap: _resetSimulation,
                child: Container(
                  width: 28,
                  height: 28,
                  decoration: BoxDecoration(
                    color: p.card,
                    shape: BoxShape.circle,
                    border: Border.all(color: p.cardBorder),
                  ),
                  child: Icon(
                    Icons.restart_alt_rounded,
                    size: 15,
                    color: p.textSecondary,
                  ),
                ),
              ),
              const Spacer(),
              // Speed Selector [ 0.5x | 1.0x | 2.0x ]
              for (final spd in const [0.5, 1.0, 2.0]) ...[
                Padding(
                  padding: const EdgeInsets.only(left: 4),
                  child: TapScale(
                    onTap: () => setState(() => _speedMultiplier = spd),
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 7,
                        vertical: 4,
                      ),
                      decoration: BoxDecoration(
                        color: _speedMultiplier == spd
                            ? p.indigo.o(0.20)
                            : p.card,
                        borderRadius: BorderRadius.circular(7),
                        border: Border.all(
                          color: _speedMultiplier == spd
                              ? p.indigo
                              : p.cardBorder,
                        ),
                      ),
                      child: Text(
                        '${spd}x',
                        style: mono(
                          fontSize: 9.5,
                          fontWeight: FontWeight.w700,
                          color: _speedMultiplier == spd
                              ? p.indigo
                              : p.textSecondary,
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ],
          ),
          const SizedBox(height: 6),
          Text(
            telemetry,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: mono(
              fontSize: 10.2,
              fontWeight: FontWeight.w600,
              color: p.green,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildAnimatedCanvas(AppPalette p, bool isDark) {
    final canvasHeight = widget.compact ? 196.0 : 228.0;
    return RepaintBoundary(
      child: LayoutBuilder(
        builder: (ctx, constraints) {
          final size = Size(constraints.maxWidth, canvasHeight);
          return GestureDetector(
            onTapDown: (d) => _handleCanvasTap(d.localPosition, size),
            child: Container(
              height: canvasHeight,
              decoration: BoxDecoration(
                color: isDark
                    ? const Color(0xFF07090E)
                    : const Color(0xFFF6F8FC),
                borderRadius: BorderRadius.circular(14),
                border: Border.all(color: p.cardBorder),
              ),
              child: CustomPaint(
                size: size,
                painter: _isCuatrimestre1Or2
                    ? Cuatrimestre1And2LabPainter(
                        simId: _activeSim.id,
                        params: _currentParams,
                        palette: p,
                        isDark: isDark,
                      )
                    : Cuatrimestre3And4LabPainter(
                        simId: _activeSim.id,
                        params: _currentParams,
                        palette: p,
                        isDark: isDark,
                      ),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildFormulaAndSubModeRow(AppPalette p) {
    final subModes = _subModesFor(_activeSim.id);
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      crossAxisAlignment: WrapCrossAlignment.center,
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: p.indigo.o(0.10),
            borderRadius: BorderRadius.circular(7),
          ),
          child: Text(
            _activeSim.formulaBadge,
            style: mono(
              fontSize: 9.8,
              fontWeight: FontWeight.w700,
              color: p.indigo,
            ),
          ),
        ),
        for (int i = 0; i < subModes.length; i++)
          TapScale(
            onTap: () => setState(() {
              _subMode = i;
              if (_activeSim.id == LabSimId.elec2TransitorioRcRl) {
                _simTimeSec = 0.0;
              }
            }),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: _subMode == i ? p.green.o(0.18) : p.elevated,
                borderRadius: BorderRadius.circular(7),
                border: Border.all(
                  color: _subMode == i ? p.green : p.cardBorder,
                ),
              ),
              child: Text(
                subModes[i],
                style: TextStyle(
                  fontSize: 10.5,
                  fontWeight: FontWeight.w600,
                  color: _subMode == i ? p.green : p.textSecondary,
                ),
              ),
            ),
          ),
      ],
    );
  }

  List<String> _subModesFor(LabSimId id) {
    switch (id) {
      case LabSimId.calcDerivadaTangente:
        return const ['Polinómica', 'Senoidal', 'Exponencial'];
      case LabSimId.calcLimites:
        return const ['Hueco Puntual', 'Salto Lateral'];
      case LabSimId.algebraTransformaciones2D:
        return const ['det > 0', 'Reflexión'];
      case LabSimId.progOrdenamiento:
        return const ['Bubble Sort', 'QuickSort'];
      case LabSimId.elec1CircuitoDc:
        return const ['Serie', 'Paralelo'];
      case LabSimId.ondasViajerasArmonicos:
        return const ['Estacionaria', 'Viajera'];
      case LabSimId.elec2TransitorioRcRl:
        return const ['Carga ON', 'Descarga OFF'];
      default:
        return const [];
    }
  }

  List<_SliderDef> _slidersFor(LabSimId id) {
    switch (id) {
      case LabSimId.calcDerivadaTangente:
        return [
          _SliderDef(
            label: 'Tangente x₀',
            min: -1.5,
            max: 1.5,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Amplitud Oscilación',
            min: 0.2,
            max: 2.0,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.calcLimites:
        return [
          _SliderDef(
            label: 'Punto objetivo a',
            min: -1.2,
            max: 1.2,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Zoom Vecindad (1/δ)',
            min: 1.0,
            max: 6.0,
            value: _paramB,
            unit: 'x',
            slot: 1,
          ),
        ];
      case LabSimId.algebraTransformaciones2D:
        return [
          _SliderDef(
            label: 'a (Escala X)',
            min: -2.0,
            max: 2.0,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'b (Cizalla X)',
            min: -1.5,
            max: 1.5,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
          _SliderDef(
            label: 'c (Cizalla Y)',
            min: -1.5,
            max: 1.5,
            value: _paramC,
            unit: '',
            slot: 2,
          ),
        ];
      case LabSimId.progOrdenamiento:
        return [
          _SliderDef(
            label: 'Elementos N',
            min: 6,
            max: 20,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Ritmo de Pasos',
            min: 0.5,
            max: 3.0,
            value: _paramB,
            unit: 'x',
            slot: 1,
          ),
        ];
      case LabSimId.progRegresionLineal:
        return [
          _SliderDef(
            label: 'Tasa Aprendizaje α',
            min: 0.1,
            max: 1.0,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
        ];
      case LabSimId.introFlujoEnergetico:
        return [
          _SliderDef(
            label: 'Entrada Primaria',
            min: 100,
            max: 1000,
            value: _paramA,
            unit: ' MW',
            slot: 0,
          ),
          _SliderDef(
            label: 'Eficiencia Planta η',
            min: 20,
            max: 95,
            value: _paramB,
            unit: '%',
            slot: 1,
          ),
        ];
      case LabSimId.fisicaMasaResorte:
        return [
          _SliderDef(
            label: 'Masa m',
            min: 0.5,
            max: 8.0,
            value: _paramA,
            unit: ' kg',
            slot: 0,
          ),
          _SliderDef(
            label: 'Constante Resorte k',
            min: 20,
            max: 180,
            value: _paramB,
            unit: ' N/m',
            slot: 1,
          ),
          _SliderDef(
            label: 'Fricción μ_k',
            min: 0.0,
            max: 0.45,
            value: _paramC,
            unit: '',
            slot: 2,
          ),
        ];
      case LabSimId.fisicaTiroParabolico:
        return [
          _SliderDef(
            label: 'Ángulo Disparo θ',
            min: 15,
            max: 80,
            value: _paramA,
            unit: '°',
            slot: 0,
          ),
          _SliderDef(
            label: 'Velocidad Inicial v₀',
            min: 10,
            max: 50,
            value: _paramB,
            unit: ' m/s',
            slot: 1,
          ),
          _SliderDef(
            label: 'Gravedad g',
            min: 4.0,
            max: 20.0,
            value: _paramC,
            unit: ' m/s²',
            slot: 2,
          ),
        ];
      case LabSimId.fisicaPlanoInclinadoDcl:
        return [
          _SliderDef(
            label: 'Inclinación θ',
            min: 10,
            max: 55,
            value: _paramA,
            unit: '°',
            slot: 0,
          ),
          _SliderDef(
            label: 'Fricción μ_k',
            min: 0.0,
            max: 0.75,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
          _SliderDef(
            label: 'Masa Bloque m',
            min: 1.0,
            max: 10.0,
            value: _paramC,
            unit: ' kg',
            slot: 2,
          ),
        ];
      case LabSimId.fisicaColisiones1D:
        return [
          _SliderDef(
            label: 'Masa m₁',
            min: 1.0,
            max: 10.0,
            value: _paramA,
            unit: ' kg',
            slot: 0,
          ),
          _SliderDef(
            label: 'Masa m₂',
            min: 1.0,
            max: 10.0,
            value: _paramB,
            unit: ' kg',
            slot: 1,
          ),
          _SliderDef(
            label: 'Restitución e',
            min: 0.0,
            max: 1.0,
            value: _paramC,
            unit: '',
            slot: 2,
          ),
        ];
      case LabSimId.integralRiemann:
        return [
          _SliderDef(
            label: 'Rectángulos n',
            min: 4,
            max: 100,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Límite Superior b',
            min: 0.8,
            max: 3.0,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.integralSolidoRevolucion:
        return [
          _SliderDef(
            label: 'Longitud Axial b',
            min: 1.0,
            max: 3.0,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Discos / Arandelas',
            min: 6,
            max: 24,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.quimicaGasesIdeales:
        return [
          _SliderDef(
            label: 'Temperatura T',
            min: 150,
            max: 900,
            value: _paramA,
            unit: ' K',
            slot: 0,
          ),
          _SliderDef(
            label: 'Volumen Pistón V',
            min: 1.5,
            max: 10.0,
            value: _paramB,
            unit: ' L',
            slot: 1,
          ),
          _SliderDef(
            label: 'Moles de Gas n',
            min: 0.5,
            max: 3.5,
            value: _paramC,
            unit: ' mol',
            slot: 2,
          ),
        ];
      case LabSimId.elec1CircuitoDc:
        return [
          _SliderDef(
            label: 'Fuente DC V',
            min: 5,
            max: 60,
            value: _paramA,
            unit: ' V',
            slot: 0,
          ),
          _SliderDef(
            label: 'Resistencia R₁',
            min: 5,
            max: 100,
            value: _paramB,
            unit: ' Ω',
            slot: 1,
          ),
          _SliderDef(
            label: 'Resistencia R₂',
            min: 5,
            max: 100,
            value: _paramC,
            unit: ' Ω',
            slot: 2,
          ),
        ];
      case LabSimId.ondasViajerasArmonicos:
        return [
          _SliderDef(
            label: 'Modo Armónico n',
            min: 1,
            max: 6,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Amplitud A',
            min: 0.2,
            max: 1.0,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.ondasPenduloFase:
        return [
          _SliderDef(
            label: 'Longitud Cuerda L',
            min: 0.5,
            max: 3.0,
            value: _paramA,
            unit: ' m',
            slot: 0,
          ),
          _SliderDef(
            label: 'Amplitud θ₀',
            min: 10,
            max: 60,
            value: _paramB,
            unit: '°',
            slot: 1,
          ),
        ];
      case LabSimId.modelacionOsciladorAmortiguado:
        return [
          _SliderDef(
            label: 'Amortiguamiento ζ',
            min: 0.05,
            max: 1.80,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Frecuencia Natural ω_n',
            min: 1.0,
            max: 5.0,
            value: _paramB,
            unit: ' rad/s',
            slot: 1,
          ),
        ];
      case LabSimId.elec2FasoresCa:
        return [
          _SliderDef(
            label: 'Vₘ (Voltaje)',
            min: 40,
            max: 220,
            value: _paramA,
            unit: ' V',
            slot: 0,
          ),
          _SliderDef(
            label: 'Ángulo Desfase φ',
            min: -85,
            max: 85,
            value: _paramB,
            unit: '°',
            slot: 1,
          ),
          _SliderDef(
            label: 'Frecuencia f',
            min: 20,
            max: 120,
            value: _paramC,
            unit: ' Hz',
            slot: 2,
          ),
        ];
      case LabSimId.elec2TransitorioRcRl:
        return [
          _SliderDef(
            label: 'Constante τ = RC',
            min: 0.3,
            max: 2.8,
            value: _paramA,
            unit: ' s',
            slot: 0,
          ),
          _SliderDef(
            label: 'Voltaje Fuente V_s',
            min: 5,
            max: 50,
            value: _paramB,
            unit: ' V',
            slot: 1,
          ),
        ];
      case LabSimId.disenoProyeccion3D:
        return [
          _SliderDef(
            label: 'Inclinación Eje X',
            min: -45,
            max: 45,
            value: _paramA,
            unit: '°',
            slot: 0,
          ),
          _SliderDef(
            label: 'Ángulo Base Eje Y',
            min: -90,
            max: 90,
            value: _paramB,
            unit: '°',
            slot: 1,
          ),
        ];
      case LabSimId.emLeyFaraday:
        return [
          _SliderDef(
            label: 'Espiras Bobina N',
            min: 2,
            max: 12,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Velocidad Imán f',
            min: 0.4,
            max: 3.0,
            value: _paramB,
            unit: ' Hz',
            slot: 1,
          ),
        ];
      case LabSimId.termoCicloPvPiston:
        return [
          _SliderDef(
            label: 'Foco Caliente T_H',
            min: 400,
            max: 1200,
            value: _paramA,
            unit: ' K',
            slot: 0,
          ),
          _SliderDef(
            label: 'Relación Compresión r',
            min: 2.0,
            max: 10.0,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.probTableroGalton:
        return [
          _SliderDef(
            label: 'Niveles Clavijas',
            min: 5,
            max: 10,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Sesgo Binomial p',
            min: 0.25,
            max: 0.75,
            value: _paramB,
            unit: '',
            slot: 1,
          ),
        ];
      case LabSimId.hidraulicaVenturiBernoulli:
        return [
          _SliderDef(
            label: 'Relación Garganta D₂/D₁',
            min: 0.38,
            max: 0.85,
            value: _paramA,
            unit: '',
            slot: 0,
          ),
          _SliderDef(
            label: 'Velocidad Entrada v₁',
            min: 1.0,
            max: 6.0,
            value: _paramB,
            unit: ' m/s',
            slot: 1,
          ),
        ];
    }
  }

  Widget _buildParameterSliders(AppPalette p) {
    final sliders = _slidersFor(_activeSim.id);
    return Column(
      children: [
        for (final s in sliders)
          Padding(
            padding: const EdgeInsets.only(bottom: 4),
            child: Row(
              children: [
                SizedBox(
                  width: 118,
                  child: Text(
                    s.label,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: p.textSecondary,
                    ),
                  ),
                ),
                Expanded(
                  child: SliderTheme(
                    data: SliderTheme.of(context).copyWith(
                      trackHeight: 3,
                      thumbShape: const RoundSliderThumbShape(
                        enabledThumbRadius: 6,
                      ),
                      overlayShape: const RoundSliderOverlayShape(
                        overlayRadius: 12,
                      ),
                      activeTrackColor: p.indigo,
                      thumbColor: p.indigo,
                      inactiveTrackColor: p.cardBorder,
                    ),
                    child: Slider(
                      value: s.value.clamp(s.min, s.max),
                      min: s.min,
                      max: s.max,
                      onChanged: (v) {
                        setState(() {
                          if (s.slot == 0) _paramA = v;
                          if (s.slot == 1) _paramB = v;
                          if (s.slot == 2) _paramC = v;
                        });
                      },
                    ),
                  ),
                ),
                SizedBox(
                  width: 58,
                  child: Text(
                    '${s.value.toStringAsFixed(s.max >= 20 ? 0 : 2)}${s.unit}',
                    textAlign: TextAlign.right,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: mono(
                      fontSize: 10,
                      fontWeight: FontWeight.w700,
                      color: p.textPrimary,
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

/// Tarjeta Radial de Avance por Corte Académico (1°, 2° y 3° Corte).
class RadialCorteProgressCard extends StatelessWidget {
  const RadialCorteProgressCard({
    super.key,
    required this.corte1Progress,
    required this.corte2Progress,
    required this.corte3Progress,
  });

  final double corte1Progress;
  final double corte2Progress;
  final double corte3Progress;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.cardBorder),
      ),
      child: Row(
        children: [
          SizedBox(
            width: 84,
            height: 84,
            child: RepaintBoundary(
              child: CustomPaint(
                painter: _ConcentricRingsPainter(
                  c1: corte1Progress.clamp(0.0, 1.0),
                  c2: corte2Progress.clamp(0.0, 1.0),
                  c3: corte3Progress.clamp(0.0, 1.0),
                  palette: p,
                ),
                child: Center(
                  child: Text(
                    '${(((corte1Progress + corte2Progress + corte3Progress) / 3) * 100).round()}%',
                    style: mono(
                      fontSize: 12,
                      fontWeight: FontWeight.w800,
                      color: p.textPrimary,
                    ),
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'AVANCE POR CORTE ACADÉMICO',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                    color: p.textSecondary,
                    letterSpacing: 0.7,
                  ),
                ),
                const SizedBox(height: 8),
                _buildRingLegend(p, '1° Corte (Fundamentos)', corte1Progress, p.green),
                const SizedBox(height: 5),
                _buildRingLegend(p, '2° Corte (Modelado)', corte2Progress, p.indigo),
                const SizedBox(height: 5),
                _buildRingLegend(p, '3° Corte (Proyecto)', corte3Progress, p.orange),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildRingLegend(AppPalette p, String label, double progress, Color color) {
    return Row(
      children: [
        Container(
          width: 8,
          height: 8,
          decoration: BoxDecoration(color: color, shape: BoxShape.circle),
        ),
        const SizedBox(width: 8),
        Expanded(
          child: Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
              fontSize: 11.5,
              fontWeight: FontWeight.w600,
              color: p.textPrimary,
            ),
          ),
        ),
        Text(
          '${(progress.clamp(0.0, 1.0) * 100).round()}%',
          style: mono(
            fontSize: 10.5,
            fontWeight: FontWeight.w700,
            color: color,
          ),
        ),
      ],
    );
  }
}

class _ConcentricRingsPainter extends CustomPainter {
  const _ConcentricRingsPainter({
    required this.c1,
    required this.c2,
    required this.c3,
    required this.palette,
  });

  final double c1;
  final double c2;
  final double c3;
  final AppPalette palette;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final rings = [
      (radius: size.width * 0.44, progress: c1, color: palette.green),
      (radius: size.width * 0.33, progress: c2, color: palette.indigo),
      (radius: size.width * 0.22, progress: c3, color: palette.orange),
    ];

    for (final r in rings) {
      final bgPaint = Paint()
        ..color = r.color.withValues(alpha: 0.16)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 6.0;
      canvas.drawCircle(center, r.radius, bgPaint);

      final fgPaint = Paint()
        ..color = r.color
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeWidth = 6.0;
      canvas.drawArc(
        Rect.fromCircle(center: center, radius: r.radius),
        -math.pi / 2,
        2 * math.pi * r.progress,
        false,
        fgPaint,
      );
    }
  }

  @override
  bool shouldRepaint(covariant _ConcentricRingsPainter oldDelegate) {
    return oldDelegate.c1 != c1 || oldDelegate.c2 != c2 || oldDelegate.c3 != c3;
  }
}

/// Mapa de Calor de Constancia de Estudio (60 días).
class StudyActivityHeatmapCard extends StatelessWidget {
  const StudyActivityHeatmapCard({
    super.key,
    required this.dailyIntensities,
  });

  final List<int> dailyIntensities;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final cells = List<int>.generate(
      60,
      (i) => i < dailyIntensities.length ? dailyIntensities[i].clamp(0, 4) : 0,
    );

    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.grid_view_rounded, size: 14, color: p.green),
              const SizedBox(width: 6),
              Expanded(
                child: Text(
                  'CONSTANCIA DE ESTUDIO (60 DÍAS)',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                    color: p.textSecondary,
                    letterSpacing: 0.7,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          Wrap(
            spacing: 4,
            runSpacing: 4,
            children: [
              for (final level in cells)
                Container(
                  width: 11,
                  height: 11,
                  decoration: BoxDecoration(
                    color: level == 0
                        ? p.elevated
                        : p.green.withValues(alpha: 0.22 + level * 0.19),
                    borderRadius: BorderRadius.circular(3),
                    border: Border.all(
                      color: level == 0 ? p.cardBorder : Colors.transparent,
                      width: 0.5,
                    ),
                  ),
                ),
            ],
          ),
        ],
      ),
    );
  }
}
