import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../../core/theme/app_theme.dart';
import 'subject_lab_registry.dart';

/// Parámetros universales de estado en vivo para todos los simuladores del Laboratorio Gráfico.
class LabSimParams {
  const LabSimParams({
    required this.timeSec,
    required this.paramA,
    required this.paramB,
    required this.paramC,
    required this.subMode,
    required this.customPoints,
    this.pointerNorm,
  });

  final double timeSec;
  final double paramA;
  final double paramB;
  final double paramC;
  final int subMode;
  final List<Offset> customPoints;
  final Offset? pointerNorm;
}

/// Painter unificado de alto rendimiento (60 FPS) para las asignaturas de Cuatrimestres 1 y 2.
class Cuatrimestre1And2LabPainter extends CustomPainter {
  Cuatrimestre1And2LabPainter({
    required this.simId,
    required this.params,
    required this.palette,
    required this.isDark,
  });

  final LabSimId simId;
  final LabSimParams params;
  final AppPalette palette;
  final bool isDark;

  @override
  void paint(Canvas canvas, Size size) {
    if (size.width <= 10 || size.height <= 10) return;
    canvas.save();
    canvas.clipRect(Offset.zero & size);

    _drawSubtleGrid(canvas, size);

    switch (simId) {
      case LabSimId.calcDerivadaTangente:
        _paintCalcDerivadaTangente(canvas, size);
        break;
      case LabSimId.calcLimites:
        _paintCalcLimites(canvas, size);
        break;
      case LabSimId.algebraTransformaciones2D:
        _paintAlgebraTransformaciones(canvas, size);
        break;
      case LabSimId.progOrdenamiento:
        _paintProgOrdenamiento(canvas, size);
        break;
      case LabSimId.progRegresionLineal:
        _paintProgRegresionLineal(canvas, size);
        break;
      case LabSimId.introFlujoEnergetico:
        _paintIntroFlujoEnergetico(canvas, size);
        break;
      case LabSimId.fisicaMasaResorte:
        _paintFisicaMasaResorte(canvas, size);
        break;
      case LabSimId.fisicaTiroParabolico:
        _paintFisicaTiroParabolico(canvas, size);
        break;
      case LabSimId.fisicaPlanoInclinadoDcl:
        _paintFisicaPlanoInclinado(canvas, size);
        break;
      case LabSimId.fisicaColisiones1D:
        _paintFisicaColisiones1D(canvas, size);
        break;
      case LabSimId.integralRiemann:
        _paintIntegralRiemann(canvas, size);
        break;
      case LabSimId.integralSolidoRevolucion:
        _paintIntegralSolidoRevolucion(canvas, size);
        break;
      case LabSimId.quimicaGasesIdeales:
        _paintQuimicaGasesIdeales(canvas, size);
        break;
      case LabSimId.elec1CircuitoDc:
        _paintElec1CircuitoDc(canvas, size);
        break;
      default:
        break;
    }

    canvas.restore();
  }

  void _drawSubtleGrid(Canvas canvas, Size size) {
    final gridPaint = Paint()
      ..color = isDark
          ? Colors.white.withValues(alpha: 0.045)
          : Colors.black.withValues(alpha: 0.05)
      ..strokeWidth = 1;
    const cols = 8;
    const rows = 5;
    for (int i = 1; i < cols; i++) {
      final x = size.width * i / cols;
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), gridPaint);
    }
    for (int j = 1; j < rows; j++) {
      final y = size.height * j / rows;
      canvas.drawLine(Offset(0, y), Offset(size.width, y), gridPaint);
    }
  }

  void _drawLabel(
    Canvas canvas,
    String text,
    Offset pos, {
    Color? color,
    double fontSize = 10,
    FontWeight weight = FontWeight.w700,
    Color? bgColor,
  }) {
    final tp = TextPainter(
      text: TextSpan(
        text: text,
        style: TextStyle(
          fontSize: fontSize,
          fontWeight: weight,
          fontFamily: 'monospace',
          color: color ?? (isDark ? Colors.white : Colors.black87),
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();

    if (bgColor != null) {
      final rect = RRect.fromRectAndRadius(
        Rect.fromLTWH(pos.dx - 4, pos.dy - 2, tp.width + 8, tp.height + 4),
        const Radius.circular(5),
      );
      canvas.drawRRect(rect, Paint()..color = bgColor);
    }
    tp.paint(canvas, pos);
  }

  void _drawArrow(
    Canvas canvas,
    Offset start,
    Offset end,
    Color color, {
    double strokeWidth = 2.2,
    String? label,
  }) {
    final delta = end - start;
    if (delta.distance < 3) return;
    final paint = Paint()
      ..color = color
      ..strokeWidth = strokeWidth
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(start, end, paint);

    final angle = math.atan2(delta.dy, delta.dx);
    const headLen = 7.5;
    final p1 = Offset(
      end.dx - headLen * math.cos(angle - 0.45),
      end.dy - headLen * math.sin(angle - 0.45),
    );
    final p2 = Offset(
      end.dx - headLen * math.cos(angle + 0.45),
      end.dy - headLen * math.sin(angle + 0.45),
    );
    final path = Path()
      ..moveTo(end.dx, end.dy)
      ..lineTo(p1.dx, p1.dy)
      ..lineTo(p2.dx, p2.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = color);

    if (label != null && label.isNotEmpty) {
      _drawLabel(
        canvas,
        label,
        Offset(end.dx + 4, end.dy - 10),
        color: color,
        fontSize: 9.5,
      );
    }
  }

  // ===========================================================================
  // 1. CÁLCULO DIFERENCIAL — DERIVADA Y RECTA TANGENTE EN MOVIMIENTO
  // ===========================================================================
  double _evalCalcF(double x) {
    switch (params.subMode % 3) {
      case 1:
        return math.sin(x) + 0.35 * math.cos(2 * x);
      case 2:
        return 0.28 * math.exp(0.55 * x) - 0.9;
      case 0:
      default:
        return 0.22 * x * x * x - 0.75 * x;
    }
  }

  double _evalCalcDf(double x) {
    switch (params.subMode % 3) {
      case 1:
        return math.cos(x) - 0.7 * math.sin(2 * x);
      case 2:
        return 0.28 * 0.55 * math.exp(0.55 * x);
      case 0:
      default:
        return 0.66 * x * x - 0.75;
    }
  }

  void _paintCalcDerivadaTangente(Canvas canvas, Size size) {
    final topRect = Rect.fromLTWH(12, 8, size.width - 24, size.height * 0.56);
    final botRect = Rect.fromLTWH(
      12,
      size.height * 0.63,
      size.width - 24,
      size.height * 0.32,
    );

    const xMin = -2.6;
    const xMax = 2.6;
    const yMin = -2.2;
    const yMax = 2.2;

    Offset mapTop(double x, double y) => Offset(
          topRect.left + ((x - xMin) / (xMax - xMin)) * topRect.width,
          topRect.bottom -
              ((y.clamp(yMin, yMax) - yMin) / (yMax - yMin)) * topRect.height,
        );

    Offset mapBot(double x, double y) => Offset(
          botRect.left + ((x - xMin) / (xMax - xMin)) * botRect.width,
          botRect.bottom -
              ((y.clamp(-3.0, 3.0) + 3.0) / 6.0) * botRect.height,
        );

    final axisPaint = Paint()
      ..color = isDark ? Colors.white24 : Colors.black26
      ..strokeWidth = 1;
    canvas.drawLine(mapTop(xMin, 0), mapTop(xMax, 0), axisPaint);
    canvas.drawLine(mapTop(0, yMin), mapTop(0, yMax), axisPaint);
    canvas.drawLine(mapBot(xMin, 0), mapBot(xMax, 0), axisPaint);

    // Curva f(x)
    final fPath = Path();
    final dfPath = Path();
    const steps = 110;
    for (int i = 0; i <= steps; i++) {
      final x = xMin + (xMax - xMin) * (i / steps);
      final pTop = mapTop(x, _evalCalcF(x));
      final pBot = mapBot(x, _evalCalcDf(x));
      if (i == 0) {
        fPath.moveTo(pTop.dx, pTop.dy);
        dfPath.moveTo(pBot.dx, pBot.dy);
      } else {
        fPath.lineTo(pTop.dx, pTop.dy);
        dfPath.lineTo(pBot.dx, pBot.dy);
      }
    }
    canvas.drawPath(
      fPath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5,
    );
    canvas.drawPath(
      dfPath,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );

    // Punto animado x0(t)
    final amp = params.paramB.clamp(0.2, 2.2);
    final x0 = (params.paramA + amp * math.sin(params.timeSec * 1.15))
        .clamp(-2.3, 2.3);
    final y0 = _evalCalcF(x0);
    final m = _evalCalcDf(x0);

    // Recta tangente
    final xLeft = (x0 - 1.15).clamp(xMin, xMax);
    final xRight = (x0 + 1.15).clamp(xMin, xMax);
    final pTan1 = mapTop(xLeft, y0 + m * (xLeft - x0));
    final pTan2 = mapTop(xRight, y0 + m * (xRight - x0));
    canvas.drawLine(
      pTan1,
      pTan2,
      Paint()
        ..color = palette.green
        ..strokeWidth = 2.2,
    );

    final pPoint = mapTop(x0, y0);
    final qPoint = mapBot(x0, m);

    // Línea conectora vertical entre P(x0, f(x0)) y Q(x0, f'(x0))
    canvas.drawLine(
      pPoint,
      qPoint,
      Paint()
        ..color = palette.orange.withValues(alpha: 0.55)
        ..strokeWidth = 1.2,
    );

    canvas.drawCircle(pPoint, 5.5, Paint()..color = palette.green);
    canvas.drawCircle(qPoint, 4.5, Paint()..color = const Color(0xFF64D2FF));

    _drawLabel(
      canvas,
      'f(x) | P(${x0.toStringAsFixed(2)}, ${y0.toStringAsFixed(2)})',
      Offset(topRect.left + 4, topRect.top + 2),
      color: palette.indigo,
    );
    _drawLabel(
      canvas,
      "m = f'(${x0.toStringAsFixed(2)}) = ${m.toStringAsFixed(2)}",
      Offset(botRect.left + 4, botRect.top - 2),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 2. CÁLCULO DIFERENCIAL — APROXIMACIÓN DE LÍMITES x -> a±
  // ===========================================================================
  void _paintCalcLimites(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(16, 12, size.width - 32, size.height - 24);
    final a = params.paramA.clamp(-1.5, 1.5);
    final zoom = params.paramB.clamp(1.0, 6.0);
    final span = 2.6 / zoom;
    final xMin = a - span;
    final xMax = a + span;
    const yMin = -1.5;
    const yMax = 3.5;

    double fLim(double x) {
      // Curva suave con hueco o salto opcional en x = a
      final base = 1.2 + 0.7 * math.sin(x * 1.3) + 0.25 * (x - a) * (x - a);
      if (params.subMode % 2 == 1 && x > a) {
        return base + 0.9; // Salto lateral para ilustrar límite bilateral vs unilateral
      }
      return base;
    }

    Offset map(double x, double y) => Offset(
          rect.left + ((x - xMin) / (xMax - xMin)) * rect.width,
          rect.bottom -
              ((y.clamp(yMin, yMax) - yMin) / (yMax - yMin)) * rect.height,
        );

    final leftPath = Path();
    final rightPath = Path();
    const steps = 60;
    for (int i = 0; i <= steps; i++) {
      final xL = xMin + (a - 0.02 - xMin) * (i / steps);
      final pL = map(xL, fLim(xL));
      if (i == 0) {
        leftPath.moveTo(pL.dx, pL.dy);
      } else {
        leftPath.lineTo(pL.dx, pL.dy);
      }

      final xR = (a + 0.02) + (xMax - (a + 0.02)) * (i / steps);
      final pR = map(xR, fLim(xR));
      if (i == 0) {
        rightPath.moveTo(pR.dx, pR.dy);
      } else {
        rightPath.lineTo(pR.dx, pR.dy);
      }
    }

    canvas.drawPath(
      leftPath,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5,
    );
    canvas.drawPath(
      rightPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5,
    );

    // Puntos móviles acercándose por izquierda y derecha
    final phase = 1.0 - ((params.timeSec * 0.45) % 1.0);
    final delta = (0.04 + 0.85 * phase * span).clamp(0.02, span * 0.92);
    final xLeft = a - delta;
    final xRight = a + delta;
    final yLeft = fLim(xLeft);
    final yRight = fLim(xRight);

    final pLeft = map(xLeft, yLeft);
    final pRight = map(xRight, yRight);
    final pHoleLeft = map(a, fLim(a - 0.001));
    final pHoleRight = map(a, fLim(a + 0.001));

    // Banda vertical delta alrededor de x = a
    canvas.drawRect(
      Rect.fromLTRB(pLeft.dx, rect.top, pRight.dx, rect.bottom),
      Paint()..color = palette.indigo.withValues(alpha: 0.10),
    );

    // Huecos en x = a
    for (final hole in [pHoleLeft, pHoleRight]) {
      canvas.drawCircle(
        hole,
        6,
        Paint()..color = isDark ? const Color(0xFF0E1015) : Colors.white,
      );
      canvas.drawCircle(
        hole,
        6,
        Paint()
          ..color = palette.orange
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2.2,
      );
    }

    canvas.drawCircle(pLeft, 5.5, Paint()..color = const Color(0xFF64D2FF));
    canvas.drawCircle(pRight, 5.5, Paint()..color = palette.green);

    _drawArrow(
      canvas,
      Offset(pLeft.dx, rect.bottom - 14),
      Offset(pHoleLeft.dx - 6, rect.bottom - 14),
      const Color(0xFF64D2FF),
      label: 'x→a⁻',
    );
    _drawArrow(
      canvas,
      Offset(pRight.dx, rect.bottom - 14),
      Offset(pHoleRight.dx + 6, rect.bottom - 14),
      palette.green,
      label: 'x→a⁺',
    );

    _drawLabel(
      canvas,
      'L⁻=${yLeft.toStringAsFixed(3)} | L⁺=${yRight.toStringAsFixed(3)} | δ=${delta.toStringAsFixed(3)}',
      Offset(rect.left + 4, rect.top + 4),
      color: palette.indigo,
    );
  }

  // ===========================================================================
  // 3. ÁLGEBRA LINEAL — TRANSFORMACIONES LINEALES 2D ANIMADAS
  // ===========================================================================
  void _paintAlgebraTransformaciones(Canvas canvas, Size size) {
    final center = Offset(size.width * 0.5, size.height * 0.54);
    final scale = math.min(size.width, size.height) * 0.17;

    // Matriz objetivo A = [[a, b], [c, d]]
    final a = params.paramA;
    final b = params.paramB;
    final c = params.paramC;
    final d = (params.subMode == 0) ? 1.0 : -0.8;

    // Interpolación animada suave alpha(t) en [0, 1]
    final alpha = 0.55 + 0.45 * math.sin(params.timeSec * 1.1);
    final m00 = (1 - alpha) * 1.0 + alpha * a;
    final m01 = (1 - alpha) * 0.0 + alpha * b;
    final m10 = (1 - alpha) * 0.0 + alpha * c;
    final m11 = (1 - alpha) * 1.0 + alpha * d;

    Offset transform(double x, double y) {
      final tx = m00 * x + m01 * y;
      final ty = m10 * x + m11 * y;
      return Offset(center.dx + tx * scale, center.dy - ty * scale);
    }

    // Cuadrícula transformada
    final gridPaint = Paint()
      ..color = palette.indigo.withValues(alpha: 0.28)
      ..strokeWidth = 1.1;
    for (int k = -3; k <= 3; k++) {
      canvas.drawLine(
        transform(k.toDouble(), -3),
        transform(k.toDouble(), 3),
        gridPaint,
      );
      canvas.drawLine(
        transform(-3, k.toDouble()),
        transform(3, k.toDouble()),
        gridPaint,
      );
    }

    // Paralelogramo determinante (área sombreada entre i' y j')
    final p00 = transform(0, 0);
    final p10 = transform(1, 0);
    final p11 = transform(1, 1);
    final p01 = transform(0, 1);
    final detPath = Path()
      ..moveTo(p00.dx, p00.dy)
      ..lineTo(p10.dx, p10.dy)
      ..lineTo(p11.dx, p11.dy)
      ..lineTo(p01.dx, p01.dy)
      ..close();
    final detCurrent = m00 * m11 - m01 * m10;
    final detTarget = a * d - b * c;
    canvas.drawPath(
      detPath,
      Paint()
        ..color = (detCurrent >= 0 ? palette.green : palette.orange)
            .withValues(alpha: 0.24),
    );
    canvas.drawPath(
      detPath,
      Paint()
        ..color = detCurrent >= 0 ? palette.green : palette.orange
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.6,
    );

    // Vectores base transformados i' y j'
    _drawArrow(canvas, p00, p10, palette.green, strokeWidth: 2.8, label: "î'");
    _drawArrow(canvas, p00, p01, palette.orange, strokeWidth: 2.8, label: "ĵ'");

    _drawLabel(
      canvas,
      'A = [${a.toStringAsFixed(1)}, ${b.toStringAsFixed(1)}; ${c.toStringAsFixed(1)}, ${d.toStringAsFixed(1)}] | det(A) = ${detTarget.toStringAsFixed(2)}',
      const Offset(12, 8),
      color: palette.indigo,
    );
  }

  // ===========================================================================
  // 4. PROGRAMACIÓN E IA — ALGORITMOS DE ORDENAMIENTO EN VIVO
  // ===========================================================================
  void _paintProgOrdenamiento(Canvas canvas, Size size) {
    final count = params.paramA.round().clamp(6, 20);
    final speedFactor = params.paramB.clamp(0.5, 3.0);

    // Generamos el arreglo base determinista y aplicamos `stepCount` pasos de Bubble/QuickSort
    final values = List<double>.generate(
      count,
      (i) => 0.18 + 0.78 * (((i * 37 + 13) % count) / count),
    );

    final totalPossibleSteps = count * (count - 1) ~/ 2;
    final currentStep =
        ((params.timeSec * 6.0 * speedFactor).floor()) % (totalPossibleSteps + 8);

    int activeI = -1;
    int activeJ = -1;
    int step = 0;
    for (int pass = 0; pass < count - 1; pass++) {
      for (int j = 0; j < count - 1 - pass; j++) {
        if (step >= currentStep) break;
        activeI = j;
        activeJ = j + 1;
        if (values[j] > values[j + 1]) {
          final tmp = values[j];
          values[j] = values[j + 1];
          values[j + 1] = tmp;
        }
        step++;
      }
      if (step >= currentStep) break;
    }

    final chartRect = Rect.fromLTWH(16, 28, size.width - 32, size.height - 42);
    final barSlot = chartRect.width / count;
    final barWidth = (barSlot * 0.72).clamp(6.0, 28.0);

    for (int i = 0; i < count; i++) {
      final h = values[i] * chartRect.height;
      final x = chartRect.left + i * barSlot + (barSlot - barWidth) / 2;
      final y = chartRect.bottom - h;

      Color barColor = palette.indigo;
      if (i == activeI || i == activeJ) {
        barColor = palette.orange;
      } else if (currentStep >= totalPossibleSteps) {
        barColor = palette.green;
      }

      final rrect = RRect.fromRectAndRadius(
        Rect.fromLTWH(x, y, barWidth, h),
        const Radius.circular(5),
      );
      canvas.drawRRect(rrect, Paint()..color = barColor);
    }

    final algoName = params.subMode % 2 == 0 ? 'Bubble Sort' : 'QuickSort Partition';
    _drawLabel(
      canvas,
      '$algoName | N=$count | Paso ${math.min(currentStep, totalPossibleSteps)}/$totalPossibleSteps',
      const Offset(14, 8),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 5. PROGRAMACIÓN E IA — REGRESIÓN LINEAL Y DESCENSO DE GRADIENTE
  // ===========================================================================
  void _paintProgRegresionLineal(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(18, 24, size.width - 36, size.height - 38);
    final pts = params.customPoints.isNotEmpty
        ? params.customPoints
        : const <Offset>[
            Offset(0.12, 0.20),
            Offset(0.24, 0.34),
            Offset(0.38, 0.36),
            Offset(0.52, 0.55),
            Offset(0.67, 0.63),
            Offset(0.81, 0.78),
            Offset(0.90, 0.85),
          ];

    // Mínimos cuadrados ordinarios exactos (OLS)
    double sumX = 0, sumY = 0;
    for (final p in pts) {
      sumX += p.dx;
      sumY += p.dy;
    }
    final meanX = sumX / pts.length;
    final meanY = sumY / pts.length;
    double num = 0, den = 0;
    for (final p in pts) {
      num += (p.dx - meanX) * (p.dy - meanY);
      den += (p.dx - meanX) * (p.dx - meanX);
    }
    final targetM = den > 1e-6 ? (num / den) : 0.8;
    final targetB = meanY - targetM * meanX;

    // Convergencia animada del descenso de gradiente según tasa de aprendizaje
    final lr = params.paramA.clamp(0.05, 1.0);
    final conv = 1.0 - math.exp(-params.timeSec * 0.9 * lr);
    final currentM = targetM * conv;
    final currentB = 0.5 * (1 - conv) + targetB * conv;

    Offset map(double nx, double ny) => Offset(
          rect.left + nx.clamp(0.0, 1.0) * rect.width,
          rect.bottom - ny.clamp(0.0, 1.0) * rect.height,
        );

    // Línea de regresión actual
    final pStart = map(0.0, currentB);
    final pEnd = map(1.0, currentM * 1.0 + currentB);
    canvas.drawLine(
      pStart,
      pEnd,
      Paint()
        ..color = palette.green
        ..strokeWidth = 2.6,
    );

    // Residuos y puntos
    double mse = 0;
    for (final pt in pts) {
      final predY = currentM * pt.dx + currentB;
      final err = pt.dy - predY;
      mse += err * err;
      final screenPt = map(pt.dx, pt.dy);
      final screenPred = map(pt.dx, predY);
      canvas.drawLine(
        screenPt,
        screenPred,
        Paint()
          ..color = palette.orange.withValues(alpha: 0.55)
          ..strokeWidth = 1.2,
      );
      canvas.drawCircle(screenPt, 4.8, Paint()..color = const Color(0xFF64D2FF));
    }
    mse /= pts.length;

    _drawLabel(
      canvas,
      'ŷ = ${currentM.toStringAsFixed(2)}x + ${currentB.toStringAsFixed(2)} | MSE = ${mse.toStringAsFixed(4)} (Toca para añadir puntos)',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 6. INTRODUCCIÓN A LA ING. ENERGÉTICA — FLUJO ENERGÉTICO Y EFICIENCIA
  // ===========================================================================
  void _paintIntroFlujoEnergetico(Canvas canvas, Size size) {
    final pIn = params.paramA.clamp(100.0, 1000.0); // MW entrada
    final etaGen = (params.paramB / 100.0).clamp(0.20, 0.95);
    final pUseful = pIn * etaGen;
    final pLoss = pIn - pUseful;

    const leftX = 26.0;
    final midX = size.width * 0.46;
    final rightX = size.width - 34.0;
    final centerY = size.height * 0.48;

    // Conducto principal de entrada
    final inPaint = Paint()
      ..color = palette.indigo.withValues(alpha: 0.25)
      ..strokeWidth = 22
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(Offset(leftX, centerY), Offset(midX, centerY), inPaint);

    // Conducto de potencia útil (arriba derecha)
    final utilStroke = (22 * etaGen).clamp(5.0, 22.0);
    canvas.drawLine(
      Offset(midX, centerY),
      Offset(rightX, centerY - 34),
      Paint()
        ..color = palette.green.withValues(alpha: 0.28)
        ..strokeWidth = utilStroke
        ..strokeCap = StrokeCap.round,
    );

    // Conducto de pérdidas térmicas (abajo derecha)
    final lossStroke = (22 * (1 - etaGen)).clamp(4.0, 20.0);
    canvas.drawLine(
      Offset(midX, centerY),
      Offset(rightX, centerY + 42),
      Paint()
        ..color = palette.orange.withValues(alpha: 0.28)
        ..strokeWidth = lossStroke
        ..strokeCap = StrokeCap.round,
    );

    // Partículas animadas de energía
    const particleCount = 14;
    for (int i = 0; i < particleCount; i++) {
      final prog = ((params.timeSec * 0.55 + i / particleCount) % 1.0);
      if (prog < 0.5) {
        final t = prog / 0.5;
        final x = leftX + (midX - leftX) * t;
        canvas.drawCircle(
          Offset(x, centerY),
          4.2,
          Paint()..color = const Color(0xFF64D2FF),
        );
      } else {
        final t = (prog - 0.5) / 0.5;
        final isUseful = (i % 10) < (etaGen * 10).round();
        final x = midX + (rightX - midX) * t;
        final y = centerY + (isUseful ? -34.0 : 42.0) * t;
        canvas.drawCircle(
          Offset(x, y),
          4.0,
          Paint()..color = isUseful ? palette.green : palette.orange,
        );
      }
    }

    // Nodo convertidor central
    final plantRect = RRect.fromRectAndRadius(
      Rect.fromCenter(center: Offset(midX, centerY), width: 64, height: 42),
      const Radius.circular(10),
    );
    canvas.drawRRect(plantRect, Paint()..color = palette.card);
    canvas.drawRRect(
      plantRect,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );
    _drawLabel(
      canvas,
      'η=${(etaGen * 100).toStringAsFixed(0)}%',
      Offset(midX - 22, centerY - 6),
      color: palette.indigo,
    );

    _drawLabel(
      canvas,
      'Entrada: ${pIn.toStringAsFixed(0)} MW',
      Offset(14, centerY - 32),
      color: const Color(0xFF64D2FF),
    );
    _drawLabel(
      canvas,
      'P_útil: ${pUseful.toStringAsFixed(0)} MW',
      Offset(rightX - 115, centerY - 62),
      color: palette.green,
    );
    _drawLabel(
      canvas,
      'Pérdidas: ${pLoss.toStringAsFixed(0)} MW',
      Offset(rightX - 125, centerY + 54),
      color: palette.orange,
    );
  }

  // ===========================================================================
  // 7. FÍSICA MECÁNICA — SISTEMA MASA-RESORTE Y CONSERVACIÓN DE ENERGÍA
  // ===========================================================================
  void _paintFisicaMasaResorte(Canvas canvas, Size size) {
    final mass = params.paramA.clamp(0.5, 10.0);
    final kSpring = params.paramB.clamp(10.0, 200.0);
    final mu = params.paramC.clamp(0.0, 0.5);

    final omega0 = math.sqrt(kSpring / mass);
    final gamma = mu * 0.45;
    final t = params.timeSec % 14.0;
    final env = math.exp(-gamma * t);
    final xNorm = env * math.cos(omega0 * t * 0.45); // [-1..1]
    final vNorm = -env * math.sin(omega0 * t * 0.45);

    final eTotal = 0.5 * kSpring * 1.0;
    final uElastic = 0.5 * kSpring * (xNorm * xNorm);
    final kKinetic = (0.5 * kSpring * (vNorm * vNorm)).clamp(0.0, eTotal);
    final eDiss = (eTotal - uElastic - kKinetic).clamp(0.0, eTotal);

    final floorY = size.height * 0.56;
    const wallX = 22.0;
    final eqX = size.width * 0.46;
    final blockX = eqX + xNorm * (size.width * 0.20);
    const blockW = 42.0;
    const blockH = 34.0;

    // Piso y pared
    final wallPaint = Paint()
      ..color = isDark ? Colors.white38 : Colors.black45
      ..strokeWidth = 2.5;
    canvas.drawLine(Offset(wallX, floorY - 48), Offset(wallX, floorY), wallPaint);
    canvas.drawLine(
      Offset(wallX, floorY),
      Offset(size.width * 0.72, floorY),
      wallPaint,
    );

    // Resorte helicoidal dinámico
    final springPath = Path()..moveTo(wallX, floorY - blockH / 2);
    const coils = 11;
    final springLen = (blockX - blockW / 2) - wallX;
    for (int i = 1; i <= coils; i++) {
      final sx = wallX + springLen * (i - 0.5) / coils;
      final sy =
          (floorY - blockH / 2) + (i.isEven ? -9.0 : 9.0);
      springPath.lineTo(sx, sy);
    }
    springPath.lineTo(blockX - blockW / 2, floorY - blockH / 2);
    canvas.drawPath(
      springPath,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2,
    );

    // Bloque de masa m
    final blockRect = RRect.fromRectAndRadius(
      Rect.fromLTWH(blockX - blockW / 2, floorY - blockH, blockW, blockH),
      const Radius.circular(7),
    );
    canvas.drawRRect(blockRect, Paint()..color = palette.indigo);
    _drawLabel(
      canvas,
      'm',
      Offset(blockX - 5, floorY - blockH / 2 - 6),
      color: Colors.white,
    );

    // Vectores de fuerza restauradora F_s y velocidad v
    _drawArrow(
      canvas,
      Offset(blockX, floorY - blockH - 8),
      Offset(blockX - xNorm * 38, floorY - blockH - 8),
      palette.orange,
      label: 'Fs',
    );
    _drawArrow(
      canvas,
      Offset(blockX, floorY - blockH / 2),
      Offset(blockX + vNorm * 38, floorY - blockH / 2),
      palette.green,
      label: 'v',
    );

    // Barras de energía (K, Ue, E_dis)
    final barAreaY = size.height * 0.70;
    final barMaxW = size.width - 96;
    final bars = <(String, double, Color)>[
      ('K (Cinética)', (kKinetic / eTotal).clamp(0.0, 1.0), palette.green),
      ('Ue (Elástica)', (uElastic / eTotal).clamp(0.0, 1.0), palette.indigo),
      ('E_dis (Fric.)', (eDiss / eTotal).clamp(0.0, 1.0), palette.orange),
    ];

    for (int i = 0; i < bars.length; i++) {
      final y = barAreaY + i * 16.0;
      _drawLabel(canvas, bars[i].$1, Offset(14, y - 2), fontSize: 9.0);
      canvas.drawRRect(
        RRect.fromRectAndRadius(
          Rect.fromLTWH(86, y, barMaxW * bars[i].$2, 9),
          const Radius.circular(4),
        ),
        Paint()..color = bars[i].$3,
      );
    }
  }

  // ===========================================================================
  // 8. FÍSICA MECÁNICA — MOVIMIENTO PARABÓLICO / PROYECTILES
  // ===========================================================================
  void _paintFisicaTiroParabolico(Canvas canvas, Size size) {
    final angleDeg = params.paramA.clamp(15.0, 80.0);
    final v0 = params.paramB.clamp(10.0, 50.0);
    final g = params.paramC.clamp(4.0, 20.0);

    final theta = angleDeg * math.pi / 180.0;
    final vx = v0 * math.cos(theta);
    final vy0 = v0 * math.sin(theta);
    final tFlight = (2 * vy0 / g).clamp(0.4, 20.0);
    final xMax = (vx * tFlight).clamp(5.0, 300.0);
    final yMax = ((vy0 * vy0) / (2 * g)).clamp(2.0, 150.0);

    const padL = 24.0;
    const padB = 24.0;
    final plotW = size.width - padL - 20;
    final plotH = size.height - padB - 26;

    final scaleX = plotW / (xMax * 1.08);
    final scaleY = plotH / (math.max(yMax * 1.25, 12.0));

    Offset map(double x, double y) => Offset(
          padL + x * scaleX,
          size.height - padB - y * scaleY,
        );

    // Suelo
    canvas.drawLine(
      Offset(padL, size.height - padB),
      Offset(size.width - 12, size.height - padB),
      Paint()
        ..color = isDark ? Colors.white30 : Colors.black38
        ..strokeWidth = 1.6,
    );

    // Trayectoria parabólica completa punteada
    final trajPath = Path();
    const steps = 60;
    for (int i = 0; i <= steps; i++) {
      final ti = tFlight * (i / steps);
      final xi = vx * ti;
      final yi = math.max(0.0, vy0 * ti - 0.5 * g * ti * ti);
      final pt = map(xi, yi);
      if (i == 0) {
        trajPath.moveTo(pt.dx, pt.dy);
      } else {
        trajPath.lineTo(pt.dx, pt.dy);
      }
    }
    canvas.drawPath(
      trajPath,
      Paint()
        ..color = palette.indigo.withValues(alpha: 0.45)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );

    // Posición animada actual del proyectil
    final tCur = (params.timeSec * 0.65) % (tFlight * 1.12);
    final tClamped = tCur.clamp(0.0, tFlight);
    final xCur = vx * tClamped;
    final yCur = math.max(0.0, vy0 * tClamped - 0.5 * g * tClamped * tClamped);
    final vyCur = vy0 - g * tClamped;

    final pProj = map(xCur, yCur);
    canvas.drawCircle(pProj, 6.0, Paint()..color = palette.orange);

    // Vectores componentes vx (constante) y vy(t) (variable)
    _drawArrow(
      canvas,
      pProj,
      Offset(pProj.dx + vx * 0.9, pProj.dy),
      palette.green,
      label: 'vx',
    );
    _drawArrow(
      canvas,
      pProj,
      Offset(pProj.dx, pProj.dy - vyCur * 0.9),
      const Color(0xFF64D2FF),
      label: 'vy',
    );

    _drawLabel(
      canvas,
      'H_máx = ${yMax.toStringAsFixed(1)} m | Alcance R = ${xMax.toStringAsFixed(1)} m | θ = ${angleDeg.toStringAsFixed(0)}°',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 9. FÍSICA MECÁNICA — PLANO INCLINADO Y DIAGRAMA DE CUERPO LIBRE (DCL)
  // ===========================================================================
  void _paintFisicaPlanoInclinado(Canvas canvas, Size size) {
    final thetaDeg = params.paramA.clamp(10.0, 55.0);
    final muK = params.paramB.clamp(0.0, 0.8);
    final mass = params.paramC.clamp(1.0, 10.0);
    const g = 9.81;

    final theta = thetaDeg * math.pi / 180.0;
    final fg = mass * g;
    final nForce = fg * math.cos(theta);
    final fkForce = muK * nForce;
    final fDrive = fg * math.sin(theta);
    final netForce = math.max(0.0, fDrive - fkForce);
    final accel = netForce / mass;

    final baseLeft = Offset(28, size.height - 22);
    final baseRight = Offset(size.width - 28, size.height - 22);
    final rampLen = (size.width - 70) * 0.82;
    final topVertex = Offset(
      baseLeft.dx,
      (baseLeft.dy - rampLen * math.sin(theta)).clamp(28.0, baseLeft.dy - 30),
    );
    final bottomVertex = Offset(
      (baseLeft.dx + rampLen * math.cos(theta)).clamp(80.0, baseRight.dx),
      baseLeft.dy,
    );

    final rampPath = Path()
      ..moveTo(topVertex.dx, topVertex.dy)
      ..lineTo(bottomVertex.dx, bottomVertex.dy)
      ..lineTo(topVertex.dx, bottomVertex.dy)
      ..close();
    canvas.drawPath(
      rampPath,
      Paint()..color = palette.indigo.withValues(alpha: 0.16),
    );
    canvas.drawPath(
      rampPath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );

    // Progreso animado del bloque sobre la rampa
    final slideProg = accel > 0.05
        ? ((0.18 + 0.25 * (params.timeSec % 2.8)) % 0.78)
        : 0.35;
    final blockCenter = Offset.lerp(topVertex, bottomVertex, slideProg)!;
    final rampAngle = math.atan2(
      bottomVertex.dy - topVertex.dy,
      bottomVertex.dx - topVertex.dx,
    );

    canvas.save();
    canvas.translate(blockCenter.dx, blockCenter.dy);
    canvas.rotate(rampAngle);
    final blockRect = RRect.fromRectAndRadius(
      const Rect.fromLTWH(-18, -28, 36, 28),
      const Radius.circular(6),
    );
    canvas.drawRRect(blockRect, Paint()..color = palette.indigo);
    canvas.restore();

    final cm = Offset(
      blockCenter.dx + 14 * math.sin(rampAngle),
      blockCenter.dy - 14 * math.cos(rampAngle),
    );

    // Vectores DCL: Peso mg (vertical abajo), Normal N, Fricción fk
    _drawArrow(
      canvas,
      cm,
      Offset(cm.dx, cm.dy + 38),
      palette.orange,
      label: 'mg',
    );
    _drawArrow(
      canvas,
      cm,
      Offset(
        cm.dx + 34 * math.sin(rampAngle),
        cm.dy - 34 * math.cos(rampAngle),
      ),
      palette.green,
      label: 'N',
    );
    _drawArrow(
      canvas,
      cm,
      Offset(
        cm.dx - (16 + muK * 28) * math.cos(rampAngle),
        cm.dy - (16 + muK * 28) * math.sin(rampAngle),
      ),
      const Color(0xFF64D2FF),
      label: 'fk',
    );

    _drawLabel(
      canvas,
      'a = ${accel.toStringAsFixed(2)} m/s² | N = ${nForce.toStringAsFixed(1)} N | fk = ${fkForce.toStringAsFixed(1)} N',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 10. FÍSICA MECÁNICA — COLISIONES 1D Y CONSERVACIÓN DEL MOMENTO
  // ===========================================================================
  void _paintFisicaColisiones1D(Canvas canvas, Size size) {
    final m1 = params.paramA.clamp(1.0, 10.0);
    final m2 = params.paramB.clamp(1.0, 10.0);
    final e = params.paramC.clamp(0.0, 1.0); // restitución

    const v1Init = 4.0;
    const v2Init = -2.0;
    final v1Final = ((m1 - e * m2) * v1Init + (1 + e) * m2 * v2Init) / (m1 + m2);
    final v2Final = ((m2 - e * m1) * v2Init + (1 + e) * m1 * v1Init) / (m1 + m2);

    final trackY = size.height * 0.58;
    final centerX = size.width * 0.5;
    canvas.drawLine(
      Offset(18, trackY + 18),
      Offset(size.width - 18, trackY + 18),
      Paint()
        ..color = isDark ? Colors.white30 : Colors.black38
        ..strokeWidth = 2,
    );

    final cycle = (params.timeSec * 0.65) % 2.4;
    double x1, x2, curV1, curV2;
    if (cycle < 1.0) {
      final rem = 1.0 - cycle;
      x1 = centerX - 18 - rem * (size.width * 0.30);
      x2 = centerX + 18 + rem * (size.width * 0.22);
      curV1 = v1Init;
      curV2 = v2Init;
    } else {
      final post = cycle - 1.0;
      x1 = centerX - 18 + post * v1Final * 22.0;
      x2 = centerX + 18 + post * v2Final * 22.0;
      curV1 = v1Final;
      curV2 = v2Final;
    }

    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Rect.fromCenter(center: Offset(x1, trackY), width: 34, height: 32),
        const Radius.circular(7),
      ),
      Paint()..color = palette.indigo,
    );
    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Rect.fromCenter(center: Offset(x2, trackY), width: 34, height: 32),
        const Radius.circular(7),
      ),
      Paint()..color = palette.orange,
    );

    _drawArrow(
      canvas,
      Offset(x1, trackY - 22),
      Offset(x1 + curV1 * 9, trackY - 22),
      palette.green,
      label: 'v₁=${curV1.toStringAsFixed(1)}',
    );
    _drawArrow(
      canvas,
      Offset(x2, trackY - 22),
      Offset(x2 + curV2 * 9, trackY - 22),
      const Color(0xFF64D2FF),
      label: 'v₂=${curV2.toStringAsFixed(1)}',
    );

    final pTotal = m1 * curV1 + m2 * curV2;
    _drawLabel(
      canvas,
      'p_total = ${pTotal.toStringAsFixed(2)} kg·m/s (Conservado) | e = ${e.toStringAsFixed(2)}',
      const Offset(14, 8),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 11. CÁLCULO INTEGRAL — SUMAS DE RIEMANN Y ÁREA ACUMULADA
  // ===========================================================================
  void _paintIntegralRiemann(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(18, 22, size.width - 36, size.height - 36);
    final nRects = params.paramA.round().clamp(4, 100);
    final bLimit = params.paramB.clamp(0.8, 3.0);

    double fInt(double x) => 0.4 + 0.35 * x * x + 0.55 * math.sin(1.4 * x);

    const xMin = 0.0;
    const xMax = 3.2;
    const yMax = 4.2;

    Offset map(double x, double y) => Offset(
          rect.left + ((x - xMin) / (xMax - xMin)) * rect.width,
          rect.bottom - (y.clamp(0.0, yMax) / yMax) * rect.height,
        );

    // Barrido animado de izquierda a derecha
    final sweepRatio = 0.25 + 0.75 * ((params.timeSec * 0.38) % 1.0);
    final activeB = bLimit * sweepRatio;
    final dx = bLimit / nRects;
    double riemannSum = 0;

    for (int i = 0; i < nRects; i++) {
      final xLeft = i * dx;
      final xMid = xLeft + dx * 0.5;
      final h = fInt(xMid);
      riemannSum += h * dx;

      final isRevealed = xLeft <= activeB;
      final pTopLeft = map(xLeft, h);
      final pBotRight = map(xLeft + dx, 0);
      final rRect = Rect.fromPoints(pTopLeft, pBotRight);

      canvas.drawRect(
        rRect,
        Paint()
          ..color = (isRevealed ? palette.green : palette.indigo)
              .withValues(alpha: isRevealed ? 0.34 : 0.10),
      );
      if (nRects <= 36) {
        canvas.drawRect(
          rRect,
          Paint()
            ..color = palette.green.withValues(alpha: 0.55)
            ..style = PaintingStyle.stroke
            ..strokeWidth = 0.9,
        );
      }
    }

    // Curva exacta f(x)
    final path = Path();
    for (int i = 0; i <= 90; i++) {
      final x = xMax * (i / 90);
      final pt = map(x, fInt(x));
      if (i == 0) {
        path.moveTo(pt.dx, pt.dy);
      } else {
        path.lineTo(pt.dx, pt.dy);
      }
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5,
    );

    _drawLabel(
      canvas,
      'n = $nRects rectángulos | Suma S_n ≈ ${riemannSum.toStringAsFixed(3)} u²',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 12. CÁLCULO INTEGRAL — SÓLIDO DE REVOLUCIÓN 3D
  // ===========================================================================
  void _paintIntegralSolidoRevolucion(Canvas canvas, Size size) {
    final center = Offset(size.width * 0.5, size.height * 0.54);
    final bLim = params.paramA.clamp(1.0, 3.0);
    final nDisks = params.paramB.round().clamp(6, 24);
    final rotPhase = params.timeSec * 1.4;

    double radiusAt(double x) => 0.45 + 0.35 * math.sin(x * 1.4) + 0.18 * x;

    // Eje X central en perspectiva
    canvas.drawLine(
      Offset(22, center.dy),
      Offset(size.width - 22, center.dy),
      Paint()
        ..color = isDark ? Colors.white38 : Colors.black38
        ..strokeWidth = 1.4,
    );

    final usableW = size.width - 76;
    double volume = 0;
    final dx = bLim / nDisks;

    for (int i = 0; i < nDisks; i++) {
      final x = (i + 0.5) * dx;
      final r = radiusAt(x);
      volume += math.pi * r * r * dx;

      final screenX = 38 + (x / 3.0) * usableW;
      final rx = 11.0 + 4.0 * math.cos(rotPhase * 0.5);
      final ry = (r * size.height * 0.30).clamp(8.0, size.height * 0.42);

      final oval = Rect.fromCenter(
        center: Offset(screenX, center.dy),
        width: rx * 2,
        height: ry * 2,
      );

      final isHighlight = i == ((params.timeSec * 3).floor() % nDisks);
      canvas.drawOval(
        oval,
        Paint()
          ..color = (isHighlight ? palette.green : palette.indigo)
              .withValues(alpha: isHighlight ? 0.32 : 0.12),
      );
      canvas.drawOval(
        oval,
        Paint()
          ..color = isHighlight
              ? palette.green
              : palette.indigo.withValues(alpha: 0.55)
          ..style = PaintingStyle.stroke
          ..strokeWidth = isHighlight ? 2.2 : 1.1,
      );
    }

    _drawLabel(
      canvas,
      'V = π ∫ [f(x)]² dx ≈ ${volume.toStringAsFixed(2)} u³ | Discos: $nDisks',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 13. QUÍMICA APLICADA — CÁMARA CINÉTICA DE GASES IDEALES (PV = nRT)
  // ===========================================================================
  void _paintQuimicaGasesIdeales(Canvas canvas, Size size) {
    final tempK = params.paramA.clamp(150.0, 900.0); // Temperatura K
    final volL = params.paramB.clamp(1.0, 10.0); // Volumen L
    final moles = params.paramC.clamp(0.5, 4.0);
    const rGas = 0.08206;
    final pressureAtm = (moles * rGas * tempK) / volL;

    const chamberLeft = 24.0;
    final chamberRight = size.width * 0.68;
    final chamberBottom = size.height - 16.0;
    final maxChamberH = size.height - 42.0;
    final curChamberH = (maxChamberH * (volL / 10.0)).clamp(48.0, maxChamberH);
    final pistonY = chamberBottom - curChamberH;

    final chamberRect = Rect.fromLTRB(
      chamberLeft,
      pistonY,
      chamberRight,
      chamberBottom,
    );
    canvas.drawRect(
      chamberRect,
      Paint()
        ..color = Color.lerp(
          const Color(0xFF64D2FF),
          palette.orange,
          ((tempK - 150) / 750).clamp(0.0, 1.0),
        )!
            .withValues(alpha: 0.12),
    );
    canvas.drawRect(
      chamberRect,
      Paint()
        ..color = isDark ? Colors.white54 : Colors.black54
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );

    // Pistón móvil superior
    canvas.drawRect(
      Rect.fromLTRB(chamberLeft - 2, pistonY - 10, chamberRight + 2, pistonY),
      Paint()..color = palette.indigo,
    );

    // Partículas rebotando con velocidad proporcional a sqrt(T)
    final speedScale = math.sqrt(tempK / 300.0) * 0.85;
    final particleCount = (moles * 10).round().clamp(8, 36);
    for (int i = 0; i < particleCount; i++) {
      final vx = 0.35 + (i % 5) * 0.17;
      final vy = 0.28 + ((i * 3) % 7) * 0.15;
      final rawX = (i * 0.19 + params.timeSec * vx * speedScale) % 2.0;
      final rawY = (i * 0.27 + params.timeSec * vy * speedScale) % 2.0;
      final nx = rawX <= 1.0 ? rawX : 2.0 - rawX;
      final ny = rawY <= 1.0 ? rawY : 2.0 - rawY;

      final px = chamberRect.left + 6 + nx * (chamberRect.width - 12);
      final py = chamberRect.top + 6 + ny * (chamberRect.height - 12);

      canvas.drawCircle(
        Offset(px, py),
        3.6,
        Paint()
          ..color = tempK > 520 ? palette.orange : const Color(0xFF64D2FF),
      );
    }

    // Manómetro lateral
    final gaugeCenter = Offset(size.width * 0.84, size.height * 0.52);
    const gaugeR = 32.0;
    canvas.drawCircle(
      gaugeCenter,
      gaugeR,
      Paint()..color = palette.card,
    );
    canvas.drawCircle(
      gaugeCenter,
      gaugeR,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );
    final needleAngle =
        -math.pi * 0.75 + (pressureAtm / 25.0).clamp(0.0, 1.0) * math.pi * 1.5;
    _drawArrow(
      canvas,
      gaugeCenter,
      Offset(
        gaugeCenter.dx + (gaugeR - 6) * math.cos(needleAngle),
        gaugeCenter.dy + (gaugeR - 6) * math.sin(needleAngle),
      ),
      palette.orange,
    );
    _drawLabel(
      canvas,
      '${pressureAtm.toStringAsFixed(1)} atm',
      Offset(gaugeCenter.dx - 24, gaugeCenter.dy + gaugeR + 4),
      color: palette.orange,
    );
    _drawLabel(
      canvas,
      'T=${tempK.toStringAsFixed(0)} K | V=${volL.toStringAsFixed(1)} L | P=${pressureAtm.toStringAsFixed(2)} atm',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 14. FUNDAMENTOS DE ELECTRICIDAD I — CIRCUITO DC Y FLUJO DE CORRIENTE
  // ===========================================================================
  void _paintElec1CircuitoDc(Canvas canvas, Size size) {
    final voltage = params.paramA.clamp(5.0, 60.0);
    final r1 = params.paramB.clamp(5.0, 100.0);
    final r2 = params.paramC.clamp(5.0, 100.0);
    final isParallel = params.subMode % 2 == 1;

    final rEq = isParallel ? (r1 * r2) / (r1 + r2) : (r1 + r2);
    final iTotal = voltage / rEq;
    final powerW = voltage * iTotal;

    final loopRect = Rect.fromLTWH(
      34,
      28,
      size.width - 68,
      size.height - 46,
    );

    final wirePaint = Paint()
      ..color = isDark ? Colors.white54 : Colors.black54
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.4;
    canvas.drawRRect(
      RRect.fromRectAndRadius(loopRect, const Radius.circular(12)),
      wirePaint,
    );

    if (isParallel) {
      final midX = loopRect.center.dx;
      canvas.drawLine(
        Offset(midX, loopRect.top),
        Offset(midX, loopRect.bottom),
        wirePaint,
      );
    }

    // Portadores de carga animados a velocidad proporcional a la corriente I
    final speed = (iTotal * 0.22).clamp(0.15, 2.2);
    const carriers = 16;
    final perim = 2 * (loopRect.width + loopRect.height);
    for (int i = 0; i < carriers; i++) {
      final dist =
          (((i / carriers) + params.timeSec * speed * 0.25) % 1.0) * perim;
      Offset pos;
      if (dist < loopRect.width) {
        pos = Offset(loopRect.left + dist, loopRect.top);
      } else if (dist < loopRect.width + loopRect.height) {
        pos = Offset(loopRect.right, loopRect.top + (dist - loopRect.width));
      } else if (dist < 2 * loopRect.width + loopRect.height) {
        pos = Offset(
          loopRect.right - (dist - loopRect.width - loopRect.height),
          loopRect.bottom,
        );
      } else {
        pos = Offset(
          loopRect.left,
          loopRect.bottom - (dist - 2 * loopRect.width - loopRect.height),
        );
      }
      canvas.drawCircle(pos, 4.0, Paint()..color = palette.green);
    }

    // Fuente V a la izquierda y resistencias R1, R2
    canvas.drawCircle(
      Offset(loopRect.left, loopRect.center.dy),
      15,
      Paint()..color = palette.indigo,
    );
    _drawLabel(
      canvas,
      '${voltage.toStringAsFixed(0)}V',
      Offset(loopRect.left - 11, loopRect.center.dy - 6),
      color: Colors.white,
      fontSize: 9,
    );

    final r1Center = Offset(loopRect.center.dx, loopRect.top);
    final r2Center = isParallel
        ? Offset(loopRect.center.dx, loopRect.center.dy)
        : Offset(loopRect.right, loopRect.center.dy);

    for (final (center, label) in [
      (r1Center, 'R₁=${r1.toStringAsFixed(0)}Ω'),
      (r2Center, 'R₂=${r2.toStringAsFixed(0)}Ω'),
    ]) {
      final rRect = RRect.fromRectAndRadius(
        Rect.fromCenter(center: center, width: 58, height: 20),
        const Radius.circular(6),
      );
      canvas.drawRRect(rRect, Paint()..color = palette.card);
      canvas.drawRRect(
        rRect,
        Paint()
          ..color = palette.orange
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.8,
      );
      _drawLabel(
        canvas,
        label,
        Offset(center.dx - 24, center.dy - 6),
        color: palette.orange,
        fontSize: 9,
      );
    }

    _drawLabel(
      canvas,
      '${isParallel ? "Paralelo" : "Serie"} | R_eq=${rEq.toStringAsFixed(1)}Ω | I=${iTotal.toStringAsFixed(2)}A | P=${powerW.toStringAsFixed(1)}W',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  @override
  bool shouldRepaint(covariant Cuatrimestre1And2LabPainter oldDelegate) {
    return true;
  }
}
