import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/theme/app_theme.dart';
import 'ios_primitives.dart';

/// Área de ingeniería soportada por el motor de gráficas interactivas.
enum EngineeringChartMode {
  acPhasor,
  calculusIntegral,
  thermoSolar,
}

extension EngineeringChartModeInfo on EngineeringChartMode {
  String get shortLabel {
    switch (this) {
      case EngineeringChartMode.acPhasor:
        return 'CA & Fasores';
      case EngineeringChartMode.calculusIntegral:
        return 'Cálculo / Tangente';
      case EngineeringChartMode.thermoSolar:
        return 'Energía / Termo';
    }
  }

  /// Determina automáticamente la gráfica más afín según YAML o nombre de materia/tema.
  static EngineeringChartMode resolve({
    required String asignaturaNombre,
    required String temaTitulo,
    String explicitHint = '',
  }) {
    final hint = explicitHint.toLowerCase().trim();
    if (hint.contains('fasor') ||
        hint.contains('ac') ||
        hint.contains('ca') ||
        hint.contains('circuito')) {
      return EngineeringChartMode.acPhasor;
    }
    if (hint.contains('calculo') ||
        hint.contains('integral') ||
        hint.contains('derivada') ||
        hint.contains('model')) {
      return EngineeringChartMode.calculusIntegral;
    }
    if (hint.contains('solar') ||
        hint.contains('termo') ||
        hint.contains('transitorio') ||
        hint.contains('energia')) {
      return EngineeringChartMode.thermoSolar;
    }

    final text = '${asignaturaNombre.toLowerCase()} ${temaTitulo.toLowerCase()}';
    if (text.contains('electric') ||
        text.contains('circuito') ||
        text.contains('fasor') ||
        text.contains('potencia') ||
        text.contains('electromag')) {
      return EngineeringChartMode.acPhasor;
    }
    if (text.contains('cálculo') ||
        text.contains('calculo') ||
        text.contains('ecuaciones') ||
        text.contains('álgebra') ||
        text.contains('algebra') ||
        text.contains('modelación') ||
        text.contains('modelacion') ||
        text.contains('integral') ||
        text.contains('derivada')) {
      return EngineeringChartMode.calculusIntegral;
    }
    return EngineeringChartMode.thermoSolar;
  }
}

/// Motor de Gráficas Interactivas de Ingeniería en Flutter nativo (`CustomPainter`).
/// Soporta retícula táctica/cursor (*crosshair*) con coordenadas `(x, y)` en vivo
/// y sliders parametrizados a 60–120 FPS en Web, Desktop y Móvil.
class InteractiveEngineeringChart extends StatefulWidget {
  const InteractiveEngineeringChart({
    super.key,
    required this.asignaturaNombre,
    required this.temaTitulo,
    this.explicitHint = '',
    this.compact = false,
  });

  final String asignaturaNombre;
  final String temaTitulo;
  final String explicitHint;
  final bool compact;

  @override
  State<InteractiveEngineeringChart> createState() =>
      _InteractiveEngineeringChartState();
}

class _InteractiveEngineeringChartState
    extends State<InteractiveEngineeringChart> {
  late EngineeringChartMode _mode;
  Offset? _pointerNormalized; // [0..1, 0..1] dentro del área de gráfica

  // Parámetros CA & Fasores
  double _vm = 120.0;
  final double _im = 8.0;
  double _freqHz = 60.0;
  double _phaseDeg = 30.0;

  // Parámetros Cálculo (Tangente + Integral)
  int _calcFuncIndex = 0; // 0: cuadrática, 1: senoidal, 2: gaussiana
  double _tangentX0 = 1.4;
  double _integralB = 2.6;
  double _calcZoom = 1.0;

  // Parámetros Termo / Solar / Transitorio
  bool _thermoShowTransient = false;
  double _irradiance = 1000.0; // W/m^2
  double _cellTempC = 25.0; // °C
  double _dampingZeta = 0.28;

  @override
  void initState() {
    super.initState();
    _mode = EngineeringChartModeInfo.resolve(
      asignaturaNombre: widget.asignaturaNombre,
      temaTitulo: widget.temaTitulo,
      explicitHint: widget.explicitHint,
    );
  }

  void _updatePointer(Offset localPos, Size size) {
    if (size.width <= 0 || size.height <= 0) return;
    setState(() {
      _pointerNormalized = Offset(
        (localPos.dx / size.width).clamp(0.0, 1.0),
        (localPos.dy / size.height).clamp(0.0, 1.0),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = Theme.of(context).brightness == Brightness.dark;

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.strongBorder),
      ),
      child: Padding(
        padding: EdgeInsets.all(widget.compact ? 12 : 16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _buildHeader(p),
            const SizedBox(height: 10),
            _buildModePills(p),
            const SizedBox(height: 12),
            _buildChartCanvas(p, isDark),
            const SizedBox(height: 10),
            _buildControlsAndMetrics(p),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader(AppPalette p) {
    return Row(
      children: [
        Container(
          width: 28,
          height: 28,
          decoration: BoxDecoration(
            color: p.indigo.o(0.14),
            borderRadius: BorderRadius.circular(8),
            border: Border.all(color: p.indigo.o(0.35)),
          ),
          child: Icon(Icons.insights_rounded, size: 16, color: p.indigo),
        ),
        const SizedBox(width: 9),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'LABORATORIO GRÁFICO INTERACTIVO',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: mono(
                  fontSize: 9.5,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.9,
                  color: p.indigo,
                ),
              ),
              Text(
                widget.temaTitulo,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w600,
                  color: p.textPrimary,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildModePills(AppPalette p) {
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      children: [
        for (final mode in EngineeringChartMode.values)
          TapScale(
            onTap: () => setState(() {
              _mode = mode;
              _pointerNormalized = null;
            }),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 180),
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              decoration: BoxDecoration(
                color: _mode == mode ? p.indigo.o(0.18) : p.elevated,
                borderRadius: BorderRadius.circular(9),
                border: Border.all(
                  color: _mode == mode ? p.indigo : p.cardBorder,
                ),
              ),
              child: Text(
                mode.shortLabel,
                style: TextStyle(
                  fontSize: 11.5,
                  fontWeight: _mode == mode ? FontWeight.w700 : FontWeight.w500,
                  color: _mode == mode ? p.indigo : p.textSecondary,
                ),
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildChartCanvas(AppPalette p, bool isDark) {
    final chartHeight = widget.compact ? 205.0 : 235.0;
    final readout = _computePointerReadout();

    return ClipRRect(
      borderRadius: BorderRadius.circular(14),
      child: Container(
        height: chartHeight,
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF0A0B0E) : const Color(0xFFF8F9FC),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: p.cardBorder),
        ),
        child: LayoutBuilder(
          builder: (context, constraints) {
            final canvasSize = Size(constraints.maxWidth, chartHeight);
            return MouseRegion(
              cursor: SystemMouseCursors.precise,
              onHover: (e) => _updatePointer(e.localPosition, canvasSize),
              onExit: (_) => setState(() => _pointerNormalized = null),
              child: GestureDetector(
                onTapDown: (d) => _updatePointer(d.localPosition, canvasSize),
                onPanUpdate: (d) => _updatePointer(d.localPosition, canvasSize),
                onPanEnd: (_) {},
                child: Stack(
                  children: [
                    Positioned.fill(
                      child: RepaintBoundary(
                        child: CustomPaint(
                          painter: _EngineeringPlotPainter(
                            mode: _mode,
                            pointerNormalized: _pointerNormalized,
                            palette: p,
                            isDark: isDark,
                            vm: _vm,
                            im: _im,
                            freqHz: _freqHz,
                            phaseDeg: _phaseDeg,
                            calcFuncIndex: _calcFuncIndex,
                            tangentX0: _tangentX0,
                            integralB: _integralB,
                            calcZoom: _calcZoom,
                            thermoShowTransient: _thermoShowTransient,
                            irradiance: _irradiance,
                            cellTempC: _cellTempC,
                            dampingZeta: _dampingZeta,
                          ),
                        ),
                      ),
                    ),
                    Positioned(
                      top: 8,
                      left: 8,
                      child: Container(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 8, vertical: 4),
                        decoration: BoxDecoration(
                          color: p.glass,
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: p.cardBorder),
                        ),
                        child: Text(
                          readout,
                          style: mono(
                            fontSize: 9.5,
                            fontWeight: FontWeight.w600,
                            color: p.textPrimary,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }

  String _computePointerReadout() {
    switch (_mode) {
      case EngineeringChartMode.acPhasor:
        final tMs = (_pointerNormalized?.dx ?? 0.25) * 33.3;
        final w = 2 * math.pi * _freqHz;
        final vVal = _vm * math.sin(w * (tMs / 1000.0));
        final phaseRad = _phaseDeg * math.pi / 180.0;
        final pf = math.cos(phaseRad);
        return 't=${tMs.toStringAsFixed(1)} ms • v(t)=${vVal.toStringAsFixed(1)} V • FP=${pf.toStringAsFixed(2)}';
      case EngineeringChartMode.calculusIntegral:
        final xMin = -0.5 / _calcZoom;
        final xMax = 3.5 / _calcZoom;
        final x = xMin + (_pointerNormalized?.dx ?? 0.5) * (xMax - xMin);
        final y = _evalCalc(_calcFuncIndex, x);
        final integral = _integrateCalc(_calcFuncIndex, 0.0, _integralB);
        return '(${x.toStringAsFixed(2)}, ${y.toStringAsFixed(2)}) • ∫₀ᵇf(x)dx = ${integral.toStringAsFixed(2)}';
      case EngineeringChartMode.thermoSolar:
        if (_thermoShowTransient) {
          final t = (_pointerNormalized?.dx ?? 0.4) * 10.0;
          final y = _evalTransient(t, _dampingZeta);
          return 't=${t.toStringAsFixed(2)} s • y(t)=${y.toStringAsFixed(3)} • ζ=${_dampingZeta.toStringAsFixed(2)}';
        } else {
          final voc = (38.0 - 0.12 * (_cellTempC - 25.0)).clamp(20.0, 45.0);
          final v = (_pointerNormalized?.dx ?? 0.78) * voc;
          final iVal = _evalSolarCurrent(v, _irradiance, _cellTempC);
          final pVal = v * iVal;
          return 'V=${v.toStringAsFixed(1)} V • I=${iVal.toStringAsFixed(2)} A • P=${pVal.toStringAsFixed(1)} W';
        }
    }
  }

  Widget _buildControlsAndMetrics(AppPalette p) {
    return Container(
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: p.elevated,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          if (_mode == EngineeringChartMode.acPhasor) ...[
            _ChartSlider(
              label: 'Vₘ (Voltaje)',
              valueLabel: '${_vm.toStringAsFixed(0)} V',
              value: _vm,
              min: 20,
              max: 220,
              accent: p.green,
              palette: p,
              onChanged: (v) => setState(() => _vm = v),
            ),
            _ChartSlider(
              label: 'Desfase φ',
              valueLabel: '${_phaseDeg.toStringAsFixed(0)}°',
              value: _phaseDeg,
              min: -85,
              max: 85,
              accent: p.indigo,
              palette: p,
              onChanged: (v) => setState(() => _phaseDeg = v),
            ),
            _ChartSlider(
              label: 'Frecuencia f',
              valueLabel: '${_freqHz.toStringAsFixed(0)} Hz',
              value: _freqHz,
              min: 20,
              max: 120,
              accent: p.orange,
              palette: p,
              onChanged: (v) => setState(() => _freqHz = v),
            ),
          ] else if (_mode == EngineeringChartMode.calculusIntegral) ...[
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: [
                for (final entry in const [
                  (0, '0.25x² + 0.5'),
                  (1, 'sin(x) + 1.5'),
                  (2, '2.5·e^(-0.3x²)'),
                ])
                  TapScale(
                    onTap: () => setState(() => _calcFuncIndex = entry.$1),
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 4),
                      decoration: BoxDecoration(
                        color: _calcFuncIndex == entry.$1
                            ? p.indigo.o(0.18)
                            : p.card,
                        borderRadius: BorderRadius.circular(7),
                        border: Border.all(
                          color: _calcFuncIndex == entry.$1
                              ? p.indigo
                              : p.cardBorder,
                        ),
                      ),
                      child: Text(
                        entry.$2,
                        style: mono(
                          fontSize: 10,
                          fontWeight: FontWeight.w600,
                          color: _calcFuncIndex == entry.$1
                              ? p.indigo
                              : p.textSecondary,
                        ),
                      ),
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 6),
            _ChartSlider(
              label: 'Tangente x₀',
              valueLabel: _tangentX0.toStringAsFixed(2),
              value: _tangentX0,
              min: 0.0,
              max: 3.0,
              accent: p.orange,
              palette: p,
              onChanged: (v) => setState(() => _tangentX0 = v),
            ),
            _ChartSlider(
              label: 'Límite ∫₀ᵇ b',
              valueLabel: _integralB.toStringAsFixed(2),
              value: _integralB,
              min: 0.4,
              max: 3.2,
              accent: p.green,
              palette: p,
              onChanged: (v) => setState(() => _integralB = v),
            ),
            _ChartSlider(
              label: 'Zoom',
              valueLabel: '${_calcZoom.toStringAsFixed(1)}×',
              value: _calcZoom,
              min: 0.6,
              max: 1.8,
              accent: p.indigo,
              palette: p,
              onChanged: (v) => setState(() => _calcZoom = v),
            ),
          ] else ...[
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: [
                TapScale(
                  onTap: () => setState(() => _thermoShowTransient = false),
                  child: Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                    decoration: BoxDecoration(
                      color: !_thermoShowTransient ? p.green.o(0.18) : p.card,
                      borderRadius: BorderRadius.circular(7),
                      border: Border.all(
                        color: !_thermoShowTransient ? p.green : p.cardBorder,
                      ),
                    ),
                    child: Text(
                      'Panel Solar I-V / P-V',
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w600,
                        color:
                            !_thermoShowTransient ? p.green : p.textSecondary,
                      ),
                    ),
                  ),
                ),
                TapScale(
                  onTap: () => setState(() => _thermoShowTransient = true),
                  child: Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                    decoration: BoxDecoration(
                      color: _thermoShowTransient ? p.orange.o(0.18) : p.card,
                      borderRadius: BorderRadius.circular(7),
                      border: Border.all(
                        color: _thermoShowTransient ? p.orange : p.cardBorder,
                      ),
                    ),
                    child: Text(
                      'Transitorio 2° Orden',
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w600,
                        color:
                            _thermoShowTransient ? p.orange : p.textSecondary,
                      ),
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 6),
            if (!_thermoShowTransient) ...[
              _ChartSlider(
                label: 'Irradiancia G',
                valueLabel: '${_irradiance.toStringAsFixed(0)} W/m²',
                value: _irradiance,
                min: 200,
                max: 1100,
                accent: p.green,
                palette: p,
                onChanged: (v) => setState(() => _irradiance = v),
              ),
              _ChartSlider(
                label: 'Temp. Celda T',
                valueLabel: '${_cellTempC.toStringAsFixed(0)} °C',
                value: _cellTempC,
                min: 15,
                max: 65,
                accent: p.orange,
                palette: p,
                onChanged: (v) => setState(() => _cellTempC = v),
              ),
            ] else ...[
              _ChartSlider(
                label: 'Amortiguamiento ζ',
                valueLabel: _dampingZeta.toStringAsFixed(2),
                value: _dampingZeta,
                min: 0.08,
                max: 1.40,
                accent: p.orange,
                palette: p,
                onChanged: (v) => setState(() => _dampingZeta = v),
              ),
            ],
          ],
        ],
      ),
    );
  }
}

double _evalCalc(int fnIndex, double x) {
  switch (fnIndex) {
    case 1:
      return math.sin(x * 1.4) + 1.5;
    case 2:
      return 2.5 * math.exp(-0.32 * x * x);
    case 0:
    default:
      return 0.25 * x * x + 0.5;
  }
}

double _evalCalcDerivative(int fnIndex, double x) {
  const h = 1e-4;
  return (_evalCalc(fnIndex, x + h) - _evalCalc(fnIndex, x - h)) / (2 * h);
}

double _integrateCalc(int fnIndex, double a, double b) {
  const steps = 60;
  final h = (b - a) / steps;
  var sum = 0.0;
  for (var i = 0; i < steps; i++) {
    final x0 = a + i * h;
    final x1 = x0 + h;
    sum += 0.5 * (_evalCalc(fnIndex, x0) + _evalCalc(fnIndex, x1)) * h;
  }
  return sum;
}

double _evalSolarCurrent(double v, double irradiance, double tempC) {
  final voc = (38.0 - 0.12 * (tempC - 25.0)).clamp(20.0, 45.0);
  final isc = 9.2 * (irradiance / 1000.0);
  if (v >= voc || v < 0) return 0.0;
  final norm = (v / voc).clamp(0.0, 1.0);
  return isc * (1.0 - math.pow(norm, 7.5).toDouble());
}

double _evalTransient(double t, double zeta) {
  const wn = 2.2;
  if (t <= 0) return 0.0;
  if (zeta < 0.99) {
    final wd = wn * math.sqrt(1.0 - zeta * zeta);
    return 1.0 -
        math.exp(-zeta * wn * t) *
            (math.cos(wd * t) +
                (zeta / math.sqrt(1.0 - zeta * zeta)) * math.sin(wd * t));
  } else if ((zeta - 1.0).abs() <= 0.02) {
    return 1.0 - math.exp(-wn * t) * (1.0 + wn * t);
  } else {
    final sq = math.sqrt(zeta * zeta - 1.0);
    final s1 = wn * (-zeta + sq);
    final s2 = wn * (-zeta - sq);
    return 1.0 + (s2 * math.exp(s1 * t) - s1 * math.exp(s2 * t)) / (s1 - s2);
  }
}

class _ChartSlider extends StatelessWidget {
  const _ChartSlider({
    required this.label,
    required this.valueLabel,
    required this.value,
    required this.min,
    required this.max,
    required this.accent,
    required this.palette,
    required this.onChanged,
  });

  final String label;
  final String valueLabel;
  final double value;
  final double min;
  final double max;
  final Color accent;
  final AppPalette palette;
  final ValueChanged<double> onChanged;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        SizedBox(
          width: 102,
          child: Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(fontSize: 11, color: palette.textBody),
          ),
        ),
        Expanded(
          child: SliderTheme(
            data: SliderTheme.of(context).copyWith(
              trackHeight: 3,
              thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 6),
              overlayShape: const RoundSliderOverlayShape(overlayRadius: 11),
              activeTrackColor: accent,
              inactiveTrackColor: palette.cardBorder,
              thumbColor: accent,
            ),
            child: Slider(
              value: value.clamp(min, max),
              min: min,
              max: max,
              onChanged: onChanged,
            ),
          ),
        ),
        SizedBox(
          width: 66,
          child: Text(
            valueLabel,
            textAlign: TextAlign.right,
            style: mono(
              fontSize: 10.5,
              fontWeight: FontWeight.w700,
              color: palette.textPrimary,
            ),
          ),
        ),
      ],
    );
  }
}

class _EngineeringPlotPainter extends CustomPainter {
  _EngineeringPlotPainter({
    required this.mode,
    required this.pointerNormalized,
    required this.palette,
    required this.isDark,
    required this.vm,
    required this.im,
    required this.freqHz,
    required this.phaseDeg,
    required this.calcFuncIndex,
    required this.tangentX0,
    required this.integralB,
    required this.calcZoom,
    required this.thermoShowTransient,
    required this.irradiance,
    required this.cellTempC,
    required this.dampingZeta,
  });

  final EngineeringChartMode mode;
  final Offset? pointerNormalized;
  final AppPalette palette;
  final bool isDark;
  final double vm;
  final double im;
  final double freqHz;
  final double phaseDeg;
  final int calcFuncIndex;
  final double tangentX0;
  final double integralB;
  final double calcZoom;
  final bool thermoShowTransient;
  final double irradiance;
  final double cellTempC;
  final double dampingZeta;

  @override
  void paint(Canvas canvas, Size size) {
    _paintGrid(canvas, size);

    switch (mode) {
      case EngineeringChartMode.acPhasor:
        _paintAcAndPhasor(canvas, size);
      case EngineeringChartMode.calculusIntegral:
        _paintCalculus(canvas, size);
      case EngineeringChartMode.thermoSolar:
        if (thermoShowTransient) {
          _paintTransient(canvas, size);
        } else {
          _paintSolarCurves(canvas, size);
        }
    }

    if (pointerNormalized != null) {
      final px = pointerNormalized!.dx * size.width;
      final py = pointerNormalized!.dy * size.height;
      final crossPaint = Paint()
        ..color = palette.textSecondary.o(0.45)
        ..strokeWidth = 1.0;
      canvas.drawLine(Offset(px, 0), Offset(px, size.height), crossPaint);
      canvas.drawLine(Offset(0, py), Offset(size.width, py), crossPaint);
      canvas.drawCircle(Offset(px, py), 4, Paint()..color = palette.indigo);
    }
  }

  void _paintGrid(Canvas canvas, Size size) {
    final gridPaint = Paint()
      ..color = palette.cardBorder.o(isDark ? 0.5 : 0.7)
      ..strokeWidth = 0.8;
    const cols = 8;
    const rows = 5;
    for (var i = 1; i < cols; i++) {
      final x = size.width * (i / cols);
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), gridPaint);
    }
    for (var j = 1; j < rows; j++) {
      final y = size.height * (j / rows);
      canvas.drawLine(Offset(0, y), Offset(size.width, y), gridPaint);
    }
  }

  void _paintAcAndPhasor(Canvas canvas, Size size) {
    final waveWidth = size.width * 0.66;
    final midY = size.height * 0.54;
    final maxAmpPx = size.height * 0.36;

    // Eje cero horizontal
    canvas.drawLine(
      Offset(10, midY),
      Offset(waveWidth - 8, midY),
      Paint()..color = palette.strongBorder..strokeWidth = 1.2,
    );

    final w = 2 * math.pi * freqHz;
    final phaseRad = phaseDeg * math.pi / 180.0;
    final vPath = Path();
    final iPath = Path();
    const steps = 120;
    for (var k = 0; k <= steps; k++) {
      final u = k / steps;
      final t = u * 0.0333; // ~33.3 ms ventana
      final x = 10 + u * (waveWidth - 18);
      final vy = midY - (vm / 220.0) * maxAmpPx * math.sin(w * t);
      final iy = midY - (im / 25.0) * maxAmpPx * 0.85 * math.sin(w * t - phaseRad);
      if (k == 0) {
        vPath.moveTo(x, vy);
        iPath.moveTo(x, iy);
      } else {
        vPath.lineTo(x, vy);
        iPath.lineTo(x, iy);
      }
    }

    canvas.drawPath(
      vPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2,
    );
    canvas.drawPath(
      iPath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );

    // Diagrama fasorial complejo a la derecha
    final phasorCenter = Offset(waveWidth + (size.width - waveWidth) * 0.5, midY);
    final radius = math.min((size.width - waveWidth) * 0.38, size.height * 0.34);

    canvas.drawCircle(
      phasorCenter,
      radius,
      Paint()
        ..color = palette.strongBorder
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.0,
    );
    canvas.drawLine(
      phasorCenter - Offset(radius, 0),
      phasorCenter + Offset(radius, 0),
      Paint()..color = palette.cardBorder,
    );
    canvas.drawLine(
      phasorCenter - Offset(0, radius),
      phasorCenter + Offset(0, radius),
      Paint()..color = palette.cardBorder,
    );

    final vLen = radius * (vm / 220.0).clamp(0.35, 1.0);
    final iLen = radius * 0.82;
    final vTip = phasorCenter + Offset(vLen, 0);
    final iTip = phasorCenter +
        Offset(iLen * math.cos(phaseRad), iLen * math.sin(phaseRad));

    _arrow(canvas, phasorCenter, vTip, palette.green);
    _arrow(canvas, phasorCenter, iTip, palette.indigo);
  }

  void _paintCalculus(Canvas canvas, Size size) {
    final xMin = -0.5 / calcZoom;
    final xMax = 3.5 / calcZoom;
    const yMin = -0.3;
    const yMax = 3.6;

    double toSx(double x) => 16 + ((x - xMin) / (xMax - xMin)) * (size.width - 32);
    double toSy(double y) =>
        size.height - 16 - ((y - yMin) / (yMax - yMin)) * (size.height - 44);

    // Ejes X/Y
    final y0 = toSy(0).clamp(12.0, size.height - 12);
    final x0Px = toSx(0).clamp(12.0, size.width - 12);
    final axisPaint = Paint()..color = palette.strongBorder..strokeWidth = 1.2;
    canvas.drawLine(Offset(12, y0), Offset(size.width - 12, y0), axisPaint);
    canvas.drawLine(Offset(x0Px, 24), Offset(x0Px, size.height - 12), axisPaint);

    // Área bajo la curva [0, integralB]
    final shadePath = Path()..moveTo(toSx(0), y0);
    const areaSteps = 60;
    for (var i = 0; i <= areaSteps; i++) {
      final x = (integralB * i) / areaSteps;
      shadePath.lineTo(toSx(x), toSy(_evalCalc(calcFuncIndex, x)));
    }
    shadePath
      ..lineTo(toSx(integralB), y0)
      ..close();
    canvas.drawPath(shadePath, Paint()..color = palette.green.o(0.22));

    // Curva principal f(x)
    final curvePath = Path();
    const curveSteps = 100;
    for (var i = 0; i <= curveSteps; i++) {
      final x = xMin + (xMax - xMin) * (i / curveSteps);
      final sx = toSx(x);
      final sy = toSy(_evalCalc(calcFuncIndex, x));
      if (i == 0) {
        curvePath.moveTo(sx, sy);
      } else {
        curvePath.lineTo(sx, sy);
      }
    }
    canvas.drawPath(
      curvePath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );

    // Recta tangente móvil en tangentX0
    final f0 = _evalCalc(calcFuncIndex, tangentX0);
    final slope = _evalCalcDerivative(calcFuncIndex, tangentX0);
    const dxSpan = 0.85;
    final t1 = Offset(toSx(tangentX0 - dxSpan), toSy(f0 - slope * dxSpan));
    final t2 = Offset(toSx(tangentX0 + dxSpan), toSy(f0 + slope * dxSpan));
    canvas.drawLine(
      t1,
      t2,
      Paint()
        ..color = palette.orange
        ..strokeWidth = 2.0,
    );
    canvas.drawCircle(
      Offset(toSx(tangentX0), toSy(f0)),
      4.5,
      Paint()..color = palette.orange,
    );
  }

  void _paintSolarCurves(Canvas canvas, Size size) {
    final voc = (38.0 - 0.12 * (cellTempC - 25.0)).clamp(20.0, 45.0);
    const maxP = 340.0;
    const maxI = 11.0;

    double toSx(double v) => 16 + (v / 44.0) * (size.width - 32);
    double toSyI(double i) => size.height - 16 - (i / maxI) * (size.height - 46);
    double toSyP(double p) => size.height - 16 - (p / maxP) * (size.height - 46);

    final iPath = Path();
    final pPath = Path();
    var mppV = 0.0;
    var mppP = 0.0;
    const steps = 90;
    for (var k = 0; k <= steps; k++) {
      final v = (voc * k) / steps;
      final cur = _evalSolarCurrent(v, irradiance, cellTempC);
      final pow = v * cur;
      if (pow > mppP) {
        mppP = pow;
        mppV = v;
      }
      final sx = toSx(v);
      final syI = toSyI(cur);
      final syP = toSyP(pow);
      if (k == 0) {
        iPath.moveTo(sx, syI);
        pPath.moveTo(sx, syP);
      } else {
        iPath.lineTo(sx, syI);
        pPath.lineTo(sx, syP);
      }
    }

    canvas.drawPath(
      iPath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2,
    );
    canvas.drawPath(
      pPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );

    final mppOffset = Offset(toSx(mppV), toSyP(mppP));
    canvas.drawCircle(mppOffset, 5, Paint()..color = palette.orange);
  }

  void _paintTransient(Canvas canvas, Size size) {
    const tMax = 10.0;
    double toSx(double t) => 16 + (t / tMax) * (size.width - 32);
    double toSy(double y) => size.height - 16 - (y / 1.8) * (size.height - 44);

    // Línea de referencia unitaria (y = 1.0)
    final yRef = toSy(1.0);
    canvas.drawLine(
      Offset(16, yRef),
      Offset(size.width - 16, yRef),
      Paint()..color = palette.green.o(0.55)..strokeWidth = 1.2,
    );

    final path = Path();
    const steps = 120;
    for (var k = 0; k <= steps; k++) {
      final t = (tMax * k) / steps;
      final sx = toSx(t);
      final sy = toSy(_evalTransient(t, dampingZeta));
      if (k == 0) {
        path.moveTo(sx, sy);
      } else {
        path.lineTo(sx, sy);
      }
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = palette.orange
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color c) {
    canvas.drawLine(a, b, Paint()..color = c..strokeWidth = 2.2);
    canvas.drawCircle(b, 3.2, Paint()..color = c);
  }

  @override
  bool shouldRepaint(covariant _EngineeringPlotPainter oldDelegate) {
    return oldDelegate.mode != mode ||
        oldDelegate.pointerNormalized != pointerNormalized ||
        oldDelegate.isDark != isDark ||
        oldDelegate.vm != vm ||
        oldDelegate.im != im ||
        oldDelegate.freqHz != freqHz ||
        oldDelegate.phaseDeg != phaseDeg ||
        oldDelegate.calcFuncIndex != calcFuncIndex ||
        oldDelegate.tangentX0 != tangentX0 ||
        oldDelegate.integralB != integralB ||
        oldDelegate.calcZoom != calcZoom ||
        oldDelegate.thermoShowTransient != thermoShowTransient ||
        oldDelegate.irradiance != irradiance ||
        oldDelegate.cellTempC != cellTempC ||
        oldDelegate.dampingZeta != dampingZeta;
  }
}

/// Gráfica Radial interactiva de progreso acumulado por Corte (30% / 30% / 40%).
class RadialCorteProgressCard extends StatefulWidget {
  const RadialCorteProgressCard({
    super.key,
    required this.corte1Progress,
    required this.corte2Progress,
    required this.corte3Progress,
  });

  final double corte1Progress; // 0..1
  final double corte2Progress; // 0..1
  final double corte3Progress; // 0..1

  @override
  State<RadialCorteProgressCard> createState() =>
      _RadialCorteProgressCardState();
}

class _RadialCorteProgressCardState extends State<RadialCorteProgressCard> {
  int? _hoveredIndex;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final segments = [
      ('Corte 1 • 30%', widget.corte1Progress, p.green),
      ('Corte 2 • 30%', widget.corte2Progress, p.indigo),
      ('Corte 3 • 40%', widget.corte3Progress, p.orange),
    ];
    final overall = (widget.corte1Progress * 0.30 +
            widget.corte2Progress * 0.30 +
            widget.corte3Progress * 0.40) *
        100;

    return IosCard(
      radius: 18,
      padding: const EdgeInsets.all(14),
      child: Row(
        children: [
          RepaintBoundary(
            child: SizedBox(
              width: 92,
              height: 92,
              child: CustomPaint(
                painter: _RadialCortePainter(
                  c1: widget.corte1Progress,
                  c2: widget.corte2Progress,
                  c3: widget.corte3Progress,
                  hoveredIndex: _hoveredIndex,
                  palette: p,
                ),
                child: Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        '${overall.round()}%',
                        style: mono(
                          fontSize: 16,
                          fontWeight: FontWeight.w800,
                          color: p.textPrimary,
                        ),
                      ),
                      Text(
                        'Global',
                        style: TextStyle(fontSize: 9.5, color: p.textSecondary),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'AVANCE POR CORTE ACADÉMICO',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.9,
                    color: p.textSecondary,
                  ),
                ),
                const SizedBox(height: 8),
                for (var i = 0; i < segments.length; i++)
                  MouseRegion(
                    cursor: SystemMouseCursors.click,
                    onEnter: (_) => setState(() => _hoveredIndex = i),
                    onExit: (_) => setState(() => _hoveredIndex = null),
                    child: GestureDetector(
                      onTap: () {
                        HapticFeedback.selectionClick();
                        setState(() => _hoveredIndex = _hoveredIndex == i ? null : i);
                      },
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 160),
                        margin: const EdgeInsets.only(bottom: 5),
                        padding: const EdgeInsets.symmetric(
                            horizontal: 8, vertical: 4),
                        decoration: BoxDecoration(
                          color: _hoveredIndex == i
                              ? segments[i].$3.o(0.14)
                              : p.elevated,
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Row(
                          children: [
                            Dot(color: segments[i].$3, size: 7),
                            const SizedBox(width: 7),
                            Expanded(
                              child: Text(
                                segments[i].$1,
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  color: p.textPrimary,
                                ),
                              ),
                            ),
                            Text(
                              '${(segments[i].$2 * 100).round()}%',
                              style: mono(
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                color: segments[i].$3,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _RadialCortePainter extends CustomPainter {
  _RadialCortePainter({
    required this.c1,
    required this.c2,
    required this.c3,
    required this.hoveredIndex,
    required this.palette,
  });

  final double c1;
  final double c2;
  final double c3;
  final int? hoveredIndex;
  final AppPalette palette;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width * 0.5, size.height * 0.5);
    final radius = math.min(size.width, size.height) * 0.42;
    const strokeW = 9.0;

    canvas.drawCircle(
      center,
      radius,
      Paint()
        ..color = palette.cardBorder
        ..style = PaintingStyle.stroke
        ..strokeWidth = strokeW,
    );

    final rect = Rect.fromCircle(center: center, radius: radius);
    const totalGap = 0.18;
    final sweepSlots = [
      (0.30 * 2 * math.pi - totalGap / 3, c1.clamp(0.05, 1.0), palette.green),
      (0.30 * 2 * math.pi - totalGap / 3, c2.clamp(0.05, 1.0), palette.indigo),
      (0.40 * 2 * math.pi - totalGap / 3, c3.clamp(0.05, 1.0), palette.orange),
    ];

    var start = -math.pi / 2;
    for (var i = 0; i < sweepSlots.length; i++) {
      final (slotSpan, fillFrac, color) = sweepSlots[i];
      canvas.drawArc(
        rect,
        start,
        slotSpan * fillFrac,
        false,
        Paint()
          ..color = hoveredIndex == null || hoveredIndex == i
              ? color
              : color.o(0.35)
          ..style = PaintingStyle.stroke
          ..strokeCap = StrokeCap.round
          ..strokeWidth = hoveredIndex == i ? strokeW + 2.5 : strokeW,
      );
      start += slotSpan + totalGap / 3;
    }
  }

  @override
  bool shouldRepaint(covariant _RadialCortePainter oldDelegate) {
    return oldDelegate.c1 != c1 ||
        oldDelegate.c2 != c2 ||
        oldDelegate.c3 != c3 ||
        oldDelegate.hoveredIndex != hoveredIndex;
  }
}

/// Mapa de Calor minimalista de constancia de estudio (últimos 60 días) en esmeralda.
class StudyActivityHeatmapCard extends StatefulWidget {
  const StudyActivityHeatmapCard({
    super.key,
    required this.dailyIntensities, // longitud <= 60, valores 0..4
  });

  final List<int> dailyIntensities;

  @override
  State<StudyActivityHeatmapCard> createState() =>
      _StudyActivityHeatmapCardState();
}

class _StudyActivityHeatmapCardState extends State<StudyActivityHeatmapCard> {
  int? _selectedDayIndex;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final cells = List<int>.generate(
      60,
      (i) => i < widget.dailyIntensities.length
          ? widget.dailyIntensities[i].clamp(0, 4)
          : 0,
    );
    final activeDays = cells.where((v) => v > 0).length;

    return IosCard(
      radius: 18,
      padding: const EdgeInsets.all(14),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Dot(color: p.green, size: 7),
              const SizedBox(width: 7),
              Expanded(
                child: Text(
                  'CONSTANCIA DE ESTUDIO (60 DÍAS)',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.9,
                    color: p.textSecondary,
                  ),
                ),
              ),
              Text(
                _selectedDayIndex != null
                    ? 'Día -${59 - _selectedDayIndex!}: Niv. ${cells[_selectedDayIndex!]}'
                    : '$activeDays/60 días activos',
                style: mono(
                  fontSize: 10,
                  fontWeight: FontWeight.w600,
                  color: p.green,
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          RepaintBoundary(
            child: LayoutBuilder(
              builder: (context, constraints) {
                const cols = 12;
                const rows = 5;
                return GridView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: cols,
                    mainAxisSpacing: 4,
                    crossAxisSpacing: 4,
                    childAspectRatio: 1.35,
                  ),
                  itemCount: cols * rows,
                  itemBuilder: (context, index) {
                    final level = cells[index];
                    final cellColor = level == 0
                        ? p.elevated
                        : p.green.o(0.22 + level * 0.19);
                    return MouseRegion(
                      onEnter: (_) => setState(() => _selectedDayIndex = index),
                      onExit: (_) => setState(() => _selectedDayIndex = null),
                      child: GestureDetector(
                        onTap: () => setState(() => _selectedDayIndex = index),
                        child: Container(
                          decoration: BoxDecoration(
                            color: cellColor,
                            borderRadius: BorderRadius.circular(4),
                            border: Border.all(
                              color: _selectedDayIndex == index
                                  ? p.textPrimary
                                  : p.cardBorder,
                              width: _selectedDayIndex == index ? 1.2 : 0.6,
                            ),
                          ),
                        ),
                      ),
                    );
                  },
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
