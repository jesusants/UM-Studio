import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../../core/theme/app_theme.dart';
import 'painters_cuatrimestre_1_2.dart';
import 'subject_lab_registry.dart';

/// Painter unificado de alto rendimiento (60 FPS) para las asignaturas de Cuatrimestres 3 y 4.
class Cuatrimestre3And4LabPainter extends CustomPainter {
  Cuatrimestre3And4LabPainter({
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
      case LabSimId.ondasViajerasArmonicos:
        _paintOndasViajerasArmonicos(canvas, size);
        break;
      case LabSimId.ondasPenduloFase:
        _paintOndasPenduloFase(canvas, size);
        break;
      case LabSimId.modelacionOsciladorAmortiguado:
        _paintModelacionOscilador(canvas, size);
        break;
      case LabSimId.elec2FasoresCa:
        _paintElec2FasoresCa(canvas, size);
        break;
      case LabSimId.elec2TransitorioRcRl:
        _paintElec2TransitorioRcRl(canvas, size);
        break;
      case LabSimId.disenoProyeccion3D:
        _paintDisenoProyeccion3D(canvas, size);
        break;
      case LabSimId.emLeyFaraday:
        _paintEmLeyFaraday(canvas, size);
        break;
      case LabSimId.termoCicloPvPiston:
        _paintTermoCicloPvPiston(canvas, size);
        break;
      case LabSimId.probTableroGalton:
        _paintProbTableroGalton(canvas, size);
        break;
      case LabSimId.hidraulicaVenturiBernoulli:
        _paintHidraulicaVenturi(canvas, size);
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
    const headLen = 7.0;
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
        fontSize: 9.2,
      );
    }
  }

  // ===========================================================================
  // 15. CALOR Y ONDAS — ONDAS VIAJERAS Y ARMÓNICOS ESTACIONARIOS
  // ===========================================================================
  void _paintOndasViajerasArmonicos(Canvas canvas, Size size) {
    final harmonicN = params.paramA.round().clamp(1, 6);
    final amp = params.paramB.clamp(0.2, 1.0);
    final isStanding = params.subMode % 2 == 0;

    final midY = size.height * 0.54;
    const leftX = 22.0;
    final rightX = size.width - 22.0;
    final length = rightX - leftX;
    final maxAmpPx = size.height * 0.34 * amp;

    // Línea de equilibrio
    canvas.drawLine(
      Offset(leftX, midY),
      Offset(rightX, midY),
      Paint()
        ..color = isDark ? Colors.white24 : Colors.black26
        ..strokeWidth = 1,
    );

    final wavePath = Path();
    final envPathTop = Path();
    final envPathBot = Path();
    const steps = 120;

    for (int i = 0; i <= steps; i++) {
      final nx = i / steps;
      final x = leftX + nx * length;
      double yVal;
      if (isStanding) {
        final spatial = math.sin(harmonicN * math.pi * nx);
        yVal = spatial * math.cos(params.timeSec * 3.2);
        final eyTop = midY - spatial.abs() * maxAmpPx;
        final eyBot = midY + spatial.abs() * maxAmpPx;
        if (i == 0) {
          envPathTop.moveTo(x, eyTop);
          envPathBot.moveTo(x, eyBot);
        } else {
          envPathTop.lineTo(x, eyTop);
          envPathBot.lineTo(x, eyBot);
        }
      } else {
        yVal = math.sin(harmonicN * math.pi * nx - params.timeSec * 3.5);
      }

      final py = midY - yVal * maxAmpPx;
      if (i == 0) {
        wavePath.moveTo(x, py);
      } else {
        wavePath.lineTo(x, py);
      }
    }

    if (isStanding) {
      final envPaint = Paint()
        ..color = palette.indigo.withValues(alpha: 0.28)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.2;
      canvas.drawPath(envPathTop, envPaint);
      canvas.drawPath(envPathBot, envPaint);
    }

    canvas.drawPath(
      wavePath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.6,
    );

    // Nodos y antinodos en modo estacionario
    if (isStanding) {
      for (int k = 0; k <= harmonicN; k++) {
        final nodeX = leftX + (k / harmonicN) * length;
        canvas.drawCircle(
          Offset(nodeX, midY),
          4.5,
          Paint()..color = palette.orange,
        );
      }
    }

    _drawLabel(
      canvas,
      '${isStanding ? "Modo Estacionario" : "Onda Viajera"} | Armónico n = $harmonicN | Nodos = ${harmonicN + 1}',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 16. CALOR Y ONDAS — PÉNDULO SIMPLE Y ESPACIO DE FASE
  // ===========================================================================
  void _paintOndasPenduloFase(Canvas canvas, Size size) {
    final lengthM = params.paramA.clamp(0.5, 3.0);
    final theta0Deg = params.paramB.clamp(10.0, 60.0);
    const g = 9.81;

    final omega0 = math.sqrt(g / lengthM);
    final theta0Rad = theta0Deg * math.pi / 180.0;
    final theta = theta0Rad * math.cos(omega0 * params.timeSec);
    final omega = -theta0Rad * omega0 * math.sin(omega0 * params.timeSec);

    // Mitad izquierda: Péndulo oscilando
    final pivot = Offset(size.width * 0.25, 28);
    final rodPx = (size.height * 0.56) * (0.55 + 0.45 * (lengthM / 3.0));
    final bob = Offset(
      pivot.dx + rodPx * math.sin(theta),
      pivot.dy + rodPx * math.cos(theta),
    );

    canvas.drawLine(
      Offset(pivot.dx - 24, pivot.dy),
      Offset(pivot.dx + 24, pivot.dy),
      Paint()
        ..color = isDark ? Colors.white54 : Colors.black54
        ..strokeWidth = 3,
    );
    canvas.drawLine(
      pivot,
      bob,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..strokeWidth = 2.2,
    );
    canvas.drawCircle(bob, 10, Paint()..color = palette.indigo);

    // Mitad derecha: Retrato de fase (theta vs omega)
    final phaseCenter = Offset(size.width * 0.72, size.height * 0.54);
    final rx = (size.width * 0.19) * (theta0Deg / 60.0);
    final ry = (size.height * 0.32) * (theta0Deg / 60.0);

    canvas.drawLine(
      Offset(phaseCenter.dx - size.width * 0.22, phaseCenter.dy),
      Offset(phaseCenter.dx + size.width * 0.22, phaseCenter.dy),
      Paint()..color = isDark ? Colors.white24 : Colors.black26,
    );
    canvas.drawLine(
      Offset(phaseCenter.dx, phaseCenter.dy - size.height * 0.36),
      Offset(phaseCenter.dx, phaseCenter.dy + size.height * 0.36),
      Paint()..color = isDark ? Colors.white24 : Colors.black26,
    );

    final ellipseRect = Rect.fromCenter(
      center: phaseCenter,
      width: rx * 2,
      height: ry * 2,
    );
    canvas.drawOval(
      ellipseRect,
      Paint()
        ..color = palette.green.withValues(alpha: 0.65)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );

    final statePt = Offset(
      phaseCenter.dx + (theta / theta0Rad) * rx,
      phaseCenter.dy - (omega / (theta0Rad * omega0)) * ry,
    );
    canvas.drawCircle(statePt, 5.5, Paint()..color = palette.orange);

    _drawLabel(
      canvas,
      'L=${lengthM.toStringAsFixed(1)}m | T=${(2 * math.pi / omega0).toStringAsFixed(2)}s | θ(t)=${(theta * 180 / math.pi).toStringAsFixed(1)}°',
      const Offset(14, 6),
      color: palette.green,
    );
    _drawLabel(
      canvas,
      'Espacio de Fase (θ, ω)',
      Offset(phaseCenter.dx - 54, size.height - 18),
      color: palette.indigo,
      fontSize: 9,
    );
  }

  // ===========================================================================
  // 17. MODELACIÓN MATEMÁTICA — OSCILADOR AMORTIGUADO Y CAMPO DE PENDIENTES
  // ===========================================================================
  double _evalDampedX(double t, double zeta, double wn) {
    if (zeta < 0.99) {
      final wd = wn * math.sqrt(1 - zeta * zeta);
      return math.exp(-zeta * wn * t) *
          (math.cos(wd * t) + (zeta / math.sqrt(1 - zeta * zeta)) * math.sin(wd * t));
    } else if (zeta <= 1.01) {
      return (1 + wn * t) * math.exp(-wn * t);
    } else {
      final s = math.sqrt(zeta * zeta - 1);
      final r1 = -wn * (zeta - s);
      final r2 = -wn * (zeta + s);
      return (r2 * math.exp(r1 * t) - r1 * math.exp(r2 * t)) / (r2 - r1);
    }
  }

  void _paintModelacionOscilador(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(18, 22, size.width - 36, size.height - 34);
    final zeta = params.paramA.clamp(0.05, 2.0);
    final wn = params.paramB.clamp(1.0, 5.0);
    const tMax = 8.0;

    Offset map(double t, double x) => Offset(
          rect.left + (t / tMax) * rect.width,
          rect.center.dy - (x.clamp(-1.2, 1.2) / 1.2) * (rect.height * 0.45),
        );

    // Campo de pendientes de fondo
    final slopePaint = Paint()
      ..color = palette.indigo.withValues(alpha: 0.22)
      ..strokeWidth = 1.0;
    for (int ti = 1; ti < 10; ti++) {
      for (int yi = -2; yi <= 2; yi++) {
        final t0 = tMax * (ti / 10);
        final y0 = yi * 0.4;
        final slope = -zeta * wn * y0;
        final pCenter = map(t0, y0);
        final angle = math.atan(-slope * 0.35);
        canvas.drawLine(
          Offset(pCenter.dx - 6 * math.cos(angle), pCenter.dy - 6 * math.sin(angle)),
          Offset(pCenter.dx + 6 * math.cos(angle), pCenter.dy + 6 * math.sin(angle)),
          slopePaint,
        );
      }
    }

    // Curvas de referencia: Crítico (zeta=1.0) y Sobreamortiguado (zeta=1.6)
    for (final (refZeta, color) in [
      (1.0, const Color(0xFF64D2FF).withValues(alpha: 0.42)),
      (1.6, palette.orange.withValues(alpha: 0.42)),
    ]) {
      final refPath = Path();
      for (int i = 0; i <= 90; i++) {
        final t = tMax * (i / 90);
        final pt = map(t, _evalDampedX(t, refZeta, wn));
        if (i == 0) {
          refPath.moveTo(pt.dx, pt.dy);
        } else {
          refPath.lineTo(pt.dx, pt.dy);
        }
      }
      canvas.drawPath(
        refPath,
        Paint()
          ..color = color
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.4,
      );
    }

    // Curva principal activa según slider zeta
    final activePath = Path();
    for (int i = 0; i <= 120; i++) {
      final t = tMax * (i / 120);
      final pt = map(t, _evalDampedX(t, zeta, wn));
      if (i == 0) {
        activePath.moveTo(pt.dx, pt.dy);
      } else {
        activePath.lineTo(pt.dx, pt.dy);
      }
    }
    canvas.drawPath(
      activePath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.6,
    );

    // Partícula trazadora en movimiento
    final tTracer = (params.timeSec * 1.1) % tMax;
    final xTracer = _evalDampedX(tTracer, zeta, wn);
    canvas.drawCircle(map(tTracer, xTracer), 5.5, Paint()..color = palette.green);

    final regime = zeta < 0.98
        ? 'Subamortiguado (ζ<1)'
        : (zeta <= 1.05 ? 'Crítico (ζ≈1)' : 'Sobreamortiguado (ζ>1)');
    _drawLabel(
      canvas,
      '$regime | ζ = ${zeta.toStringAsFixed(2)} | ω_n = ${wn.toStringAsFixed(1)} rad/s',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 18. FUNDAMENTOS DE ELECTRICIDAD II — FASORES ROTATORIOS Y ONDAS CA
  // ===========================================================================
  void _paintElec2FasoresCa(Canvas canvas, Size size) {
    final vm = params.paramA.clamp(20.0, 220.0);
    final phaseDeg = params.paramB.clamp(-90.0, 90.0);
    final freq = params.paramC.clamp(10.0, 120.0);

    final phiRad = phaseDeg * math.pi / 180.0;
    final pf = math.cos(phiRad);
    final omegaT = params.timeSec * 2.4 * (freq / 60.0);

    // Izquierda: Círculo fasorial
    final cCenter = Offset(size.width * 0.22, size.height * 0.55);
    final radius = math.min(size.width * 0.17, size.height * 0.34);

    canvas.drawCircle(
      cCenter,
      radius,
      Paint()
        ..color = isDark ? Colors.white24 : Colors.black26
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.2,
    );

    final vTip = Offset(
      cCenter.dx + radius * math.cos(omegaT),
      cCenter.dy - radius * math.sin(omegaT),
    );
    final iRadius = radius * 0.72;
    final iTip = Offset(
      cCenter.dx + iRadius * math.cos(omegaT - phiRad),
      cCenter.dy - iRadius * math.sin(omegaT - phiRad),
    );

    _drawArrow(canvas, cCenter, vTip, palette.green, strokeWidth: 2.6, label: 'V');
    _drawArrow(canvas, cCenter, iTip, palette.indigo, strokeWidth: 2.4, label: 'I');

    // Derecha: Ondas senoidales v(t), i(t), p(t) en movimiento
    final waveRect = Rect.fromLTWH(
      size.width * 0.44,
      24,
      size.width * 0.52,
      size.height - 38,
    );

    // Proyección horizontal punteada desde la punta del fasor V al inicio de la onda
    canvas.drawLine(
      vTip,
      Offset(waveRect.left, vTip.dy),
      Paint()
        ..color = palette.green.withValues(alpha: 0.45)
        ..strokeWidth = 1.1,
    );

    final vPath = Path();
    final iPath = Path();
    final pPath = Path();
    const steps = 90;

    for (int k = 0; k <= steps; k++) {
      final frac = k / steps;
      final angle = omegaT - frac * 2 * math.pi;
      final x = waveRect.left + frac * waveRect.width;
      final vy = cCenter.dy - radius * math.sin(angle);
      final iy = cCenter.dy - iRadius * math.sin(angle - phiRad);
      final pInst = math.sin(angle) * math.sin(angle - phiRad);
      final py = cCenter.dy - (radius * 0.55) * pInst;

      if (k == 0) {
        vPath.moveTo(x, vy);
        iPath.moveTo(x, iy);
        pPath.moveTo(x, py);
      } else {
        vPath.lineTo(x, vy);
        iPath.lineTo(x, iy);
        pPath.lineTo(x, py);
      }
    }

    canvas.drawPath(
      pPath,
      Paint()
        ..color = palette.orange.withValues(alpha: 0.55)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.5,
    );
    canvas.drawPath(
      iPath,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.0,
    );
    canvas.drawPath(
      vPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );

    _drawLabel(
      canvas,
      'V_rms=${(vm / math.sqrt2).toStringAsFixed(1)}V | φ=${phaseDeg.toStringAsFixed(0)}° | FP=cosφ=${pf.toStringAsFixed(2)}',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 19. FUNDAMENTOS DE ELECTRICIDAD II — RESPUESTA TRANSITORIA RC Y RL
  // ===========================================================================
  void _paintElec2TransitorioRcRl(Canvas canvas, Size size) {
    final rect = Rect.fromLTWH(22, 26, size.width - 44, size.height - 40);
    final tau = params.paramA.clamp(0.3, 3.0);
    final vSource = params.paramB.clamp(5.0, 50.0);
    final isCharging = params.subMode % 2 == 0;
    const tMax = 6.0;

    Offset map(double t, double vNorm) => Offset(
          rect.left + (t / tMax) * rect.width,
          rect.bottom - vNorm.clamp(0.0, 1.05) * rect.height,
        );

    // Línea vertical de constante de tiempo tau (63.2% o 36.8%)
    final tauX = map(tau.clamp(0.0, tMax), 0).dx;
    canvas.drawLine(
      Offset(tauX, rect.top),
      Offset(tauX, rect.bottom),
      Paint()
        ..color = palette.orange.withValues(alpha: 0.65)
        ..strokeWidth = 1.4,
    );
    _drawLabel(
      canvas,
      'τ=${tau.toStringAsFixed(2)}s',
      Offset(tauX + 4, rect.bottom - 16),
      color: palette.orange,
      fontSize: 9,
    );

    final vPath = Path();
    final iPath = Path();
    const steps = 100;
    for (int i = 0; i <= steps; i++) {
      final t = tMax * (i / steps);
      final expVal = math.exp(-t / tau);
      final vNorm = isCharging ? (1.0 - expVal) : expVal;
      final iNorm = expVal;

      final pv = map(t, vNorm);
      final pi = map(t, iNorm);
      if (i == 0) {
        vPath.moveTo(pv.dx, pv.dy);
        iPath.moveTo(pi.dx, pi.dy);
      } else {
        vPath.lineTo(pv.dx, pv.dy);
        iPath.lineTo(pi.dx, pi.dy);
      }
    }

    canvas.drawPath(
      iPath,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.8,
    );
    canvas.drawPath(
      vPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.6,
    );

    final tCur = (params.timeSec * 0.9) % tMax;
    final expCur = math.exp(-tCur / tau);
    final vCurNorm = isCharging ? (1.0 - expCur) : expCur;
    canvas.drawCircle(map(tCur, vCurNorm), 5.5, Paint()..color = palette.green);

    _drawLabel(
      canvas,
      '${isCharging ? "Carga" : "Descarga"} | v_C(t) = ${(vCurNorm * vSource).toStringAsFixed(1)}V / ${vSource.toStringAsFixed(0)}V | 5τ = ${(5 * tau).toStringAsFixed(1)}s',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 20. INGENIERÍA DEL DISEÑO Y MODELADO 3D — PROYECCIÓN ISOMÉTRICA Y VISTAS
  // ===========================================================================
  void _paintDisenoProyeccion3D(Canvas canvas, Size size) {
    final rotX = (params.paramA * math.pi / 180.0) + 0.45;
    final rotY = (params.paramB * math.pi / 180.0) + params.timeSec * 0.75;
    final scale = math.min(size.width * 0.30, size.height * 0.42) * 0.46;
    final isoCenter = Offset(size.width * 0.32, size.height * 0.56);

    // Vértices de una pieza mecánica escalonada (bloque en L 3D)
    const verts = <List<double>>[
      [-1, -1, -1],
      [1, -1, -1],
      [1, 0, -1],
      [0, 0, -1],
      [0, 1, -1],
      [-1, 1, -1],
      [-1, -1, 1],
      [1, -1, 1],
      [1, 0, 1],
      [0, 0, 1],
      [0, 1, 1],
      [-1, 1, 1],
    ];

    const edges = <List<int>>[
      [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], // cara trasera
      [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6], // cara frontal
      [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], // conectores Z
    ];

    Offset project(List<double> v) {
      final x = v[0];
      final y = v[1];
      final z = v[2];
      // Rotación Y luego X
      final x1 = x * math.cos(rotY) + z * math.sin(rotY);
      final z1 = -x * math.sin(rotY) + z * math.cos(rotY);
      final y2 = y * math.cos(rotX) - z1 * math.sin(rotX);
      return Offset(isoCenter.dx + x1 * scale, isoCenter.dy - y2 * scale);
    }

    final projected = verts.map(project).toList();
    final edgePaint = Paint()
      ..color = const Color(0xFF64D2FF)
      ..strokeWidth = 2.0
      ..strokeCap = StrokeCap.round;

    for (final e in edges) {
      canvas.drawLine(projected[e[0]], projected[e[1]], edgePaint);
    }

    // Panel derecho: 3 Vistas ortogonales (Alzado, Planta, Perfil)
    final rightX = size.width * 0.65;
    final boxW = (size.width * 0.30).clamp(64.0, 120.0);
    final boxH = (size.height - 40) / 3.2;

    final views = <(String, Color)>[
      ('ALZADO (Frontal)', palette.green),
      ('PLANTA (Superior)', palette.indigo),
      ('PERFIL (Lateral)', palette.orange),
    ];

    for (int i = 0; i < views.length; i++) {
      final top = 24.0 + i * (boxH + 6);
      final r = Rect.fromLTWH(rightX, top, boxW, boxH);
      canvas.drawRRect(
        RRect.fromRectAndRadius(r, const Radius.circular(6)),
        Paint()..color = palette.card,
      );
      canvas.drawRRect(
        RRect.fromRectAndRadius(r, const Radius.circular(6)),
        Paint()
          ..color = views[i].$2.withValues(alpha: 0.7)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.4,
      );
      _drawLabel(
        canvas,
        views[i].$1,
        Offset(r.left + 6, r.top + 3),
        color: views[i].$2,
        fontSize: 8.5,
      );

      // Silueta L ortogonal dentro de cada caja
      final inner = r.deflate(14);
      final lPath = Path()
        ..moveTo(inner.left, inner.top + 4)
        ..lineTo(inner.center.dx, inner.top + 4)
        ..lineTo(inner.center.dx, inner.center.dy)
        ..lineTo(inner.right, inner.center.dy)
        ..lineTo(inner.right, inner.bottom)
        ..lineTo(inner.left, inner.bottom)
        ..close();
      canvas.drawPath(
        lPath,
        Paint()
          ..color = views[i].$2
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.5,
      );
    }

    _drawLabel(
      canvas,
      'CAD 3D Isométrico + Proyección Ortogonal DIN/ISO',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 21. ELECTRICIDAD Y MAGNETISMO — LEY DE FARADAY E INDUCCIÓN
  // ===========================================================================
  void _paintEmLeyFaraday(Canvas canvas, Size size) {
    final turnsN = params.paramA.round().clamp(2, 12);
    final speedFreq = params.paramB.clamp(0.4, 3.0);

    final coilCenter = Offset(size.width * 0.48, size.height * 0.56);
    final phase = params.timeSec * 2.0 * speedFreq;
    final magnetX = coilCenter.dx - 55 + 62 * math.sin(phase);
    // Derivada del flujo dPhi/dt proporcional a la velocidad del imán
    final femNormalized =
        (turnsN / 12.0) * speedFreq * math.cos(phase); // [-2..2]

    // Líneas de campo magnético alrededor del imán
    final fieldPaint = Paint()
      ..color = const Color(0xFF64D2FF).withValues(alpha: 0.28)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.2;
    for (final dy in [-26.0, 26.0]) {
      canvas.drawOval(
        Rect.fromCenter(
          center: Offset(magnetX, coilCenter.dy + dy * 0.7),
          width: 96,
          height: 36,
        ),
        fieldPaint,
      );
    }

    // Imán permanente (N rojo/naranja, S azul/indigo)
    final nRect = Rect.fromLTWH(magnetX, coilCenter.dy - 14, 34, 28);
    final sRect = Rect.fromLTWH(magnetX - 34, coilCenter.dy - 14, 34, 28);
    canvas.drawRect(nRect, Paint()..color = palette.orange);
    canvas.drawRect(sRect, Paint()..color = palette.indigo);
    _drawLabel(canvas, 'N', Offset(magnetX + 12, coilCenter.dy - 6), color: Colors.white);
    _drawLabel(canvas, 'S', Offset(magnetX - 22, coilCenter.dy - 6), color: Colors.white);

    // Bobina de N espiras
    final coilPaint = Paint()
      ..color = palette.green
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.2;
    for (int i = 0; i < turnsN; i++) {
      final cx = coilCenter.dx - 24 + (i / math.max(1, turnsN - 1)) * 56;
      canvas.drawOval(
        Rect.fromCenter(center: Offset(cx, coilCenter.dy), width: 16, height: 64),
        coilPaint,
      );
    }

    // Galvanómetro analógico a la derecha
    final galvCenter = Offset(size.width * 0.84, size.height * 0.56);
    const galvR = 30.0;
    canvas.drawCircle(galvCenter, galvR, Paint()..color = palette.card);
    canvas.drawCircle(
      galvCenter,
      galvR,
      Paint()
        ..color = palette.indigo
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );
    final needleAngle =
        -math.pi / 2 + femNormalized.clamp(-1.4, 1.4) * 0.75;
    _drawArrow(
      canvas,
      galvCenter,
      Offset(
        galvCenter.dx + (galvR - 6) * math.cos(needleAngle),
        galvCenter.dy + (galvR - 6) * math.sin(needleAngle),
      ),
      palette.orange,
    );

    _drawLabel(
      canvas,
      'N = $turnsN espiras | ε = −N·dΦ/dt = ${(femNormalized * 12.0).toStringAsFixed(1)} V',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 22. TERMODINÁMICA — CICLO P-V Y PISTÓN SINCRONIZADO
  // ===========================================================================
  void _paintTermoCicloPvPiston(Canvas canvas, Size size) {
    final tHot = params.paramA.clamp(400.0, 1200.0);
    final compRatio = params.paramB.clamp(2.0, 10.0);
    const tCold = 300.0;
    final etaCarnot = 1.0 - (tCold / tHot);

    // Izquierda: Diagrama P-V
    final pvRect = Rect.fromLTWH(24, 24, size.width * 0.54, size.height - 38);
    canvas.drawLine(
      Offset(pvRect.left, pvRect.bottom),
      Offset(pvRect.right, pvRect.bottom),
      Paint()..color = isDark ? Colors.white38 : Colors.black38,
    );
    canvas.drawLine(
      Offset(pvRect.left, pvRect.top),
      Offset(pvRect.left, pvRect.bottom),
      Paint()..color = isDark ? Colors.white38 : Colors.black38,
    );

    final p1 = Offset(pvRect.left + pvRect.width * 0.16, pvRect.top + pvRect.height * 0.16);
    final p2 = Offset(pvRect.left + pvRect.width * 0.58, pvRect.top + pvRect.height * 0.34);
    final p3 = Offset(pvRect.left + pvRect.width * 0.88, pvRect.top + pvRect.height * 0.78);
    final p4 = Offset(pvRect.left + pvRect.width * 0.34, pvRect.top + pvRect.height * 0.64);

    final cyclePath = Path()
      ..moveTo(p1.dx, p1.dy)
      ..quadraticBezierTo(
        (p1.dx + p2.dx) / 2,
        p1.dy + 18,
        p2.dx,
        p2.dy,
      )
      ..lineTo(p3.dx, p3.dy)
      ..quadraticBezierTo(
        (p3.dx + p4.dx) / 2,
        p3.dy - 10,
        p4.dx,
        p4.dy,
      )
      ..close();

    canvas.drawPath(
      cyclePath,
      Paint()..color = palette.green.withValues(alpha: 0.18),
    );
    canvas.drawPath(
      cyclePath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2,
    );

    // Estado móvil alrededor del ciclo (4 etapas)
    final stage = (params.timeSec * 0.75) % 4.0;
    final vertices = [p1, p2, p3, p4];
    final idx = stage.floor();
    final frac = stage - idx;
    final statePos = Offset.lerp(vertices[idx], vertices[(idx + 1) % 4], frac)!;
    canvas.drawCircle(statePos, 5.5, Paint()..color = palette.orange);

    // Derecha: Cilindro-Pistón sincronizado con el volumen V(t)
    final volNorm = ((statePos.dx - pvRect.left) / pvRect.width).clamp(0.15, 0.92);
    final cylRect = Rect.fromLTWH(
      size.width * 0.68,
      30,
      size.width * 0.24,
      size.height - 46,
    );
    final pistonY = cylRect.top + 12 + (1.0 - volNorm) * (cylRect.height - 34);

    final gasColor = Color.lerp(
      const Color(0xFF64D2FF),
      palette.orange,
      (1.0 - volNorm).clamp(0.0, 1.0),
    )!;
    canvas.drawRect(
      Rect.fromLTRB(cylRect.left, pistonY, cylRect.right, cylRect.bottom),
      Paint()..color = gasColor.withValues(alpha: 0.28),
    );
    canvas.drawRect(
      cylRect,
      Paint()
        ..color = isDark ? Colors.white54 : Colors.black54
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );
    canvas.drawRect(
      Rect.fromLTRB(cylRect.left, pistonY - 10, cylRect.right, pistonY),
      Paint()..color = palette.indigo,
    );

    _drawLabel(
      canvas,
      'T_H=${tHot.toStringAsFixed(0)}K | r=${compRatio.toStringAsFixed(1)} | η_máx=${(etaCarnot * 100).toStringAsFixed(1)}%',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 23. PROBABILIDAD Y ESTADÍSTICA — TABLERO DE GALTON Y TLC
  // ===========================================================================
  void _paintProbTableroGalton(Canvas canvas, Size size) {
    final rows = params.paramA.round().clamp(5, 10);
    final pRight = params.paramB.clamp(0.25, 0.75);

    const topY = 26.0;
    final pegAreaH = size.height * 0.44;
    final histAreaTop = topY + pegAreaH + 8;
    final histAreaBottom = size.height - 14;
    final histH = histAreaBottom - histAreaTop;
    final centerX = size.width * 0.5;
    final spanW = size.width * 0.76;

    // Clavijas del tablero de Galton
    final pegPaint = Paint()
      ..color = isDark ? Colors.white54 : Colors.black45;
    for (int r = 0; r < rows; r++) {
      final y = topY + (r / rows) * pegAreaH;
      final rowW = (r / rows) * (spanW * 0.68);
      for (int c = 0; c <= r; c++) {
        final x = r == 0 ? centerX : (centerX - rowW / 2 + (c / r) * rowW);
        canvas.drawCircle(Offset(x, y), 2.4, pegPaint);
      }
    }

    // Bolitas cayendo en cascada
    const balls = 14;
    for (int b = 0; b < balls; b++) {
      final fallProg = ((params.timeSec * 0.65 + b / balls) % 1.0);
      final curRow = fallProg * rows;
      // Desviación hacia la media pRight
      final drift = (pRight - 0.5) * 2.0 * fallProg * (spanW * 0.25);
      final jitter =
          math.sin(b * 2.7 + curRow * 1.9) * (fallProg * spanW * 0.16);
      final bx = centerX + drift + jitter;
      final by = topY + fallProg * pegAreaH;
      canvas.drawCircle(
        Offset(bx, by),
        3.5,
        Paint()..color = palette.orange,
      );
    }

    // Histograma Binomial convergiendo a la Campana de Gauss N(μ, σ²)
    final bins = rows + 1;
    final mu = rows * pRight;
    final sigma = math.sqrt(rows * pRight * (1 - pRight)).clamp(0.6, 10.0);
    final binW = spanW / bins;
    final startX = centerX - spanW / 2;

    final gaussPath = Path();
    for (int i = 0; i < bins; i++) {
      final z = (i - mu) / sigma;
      final density = math.exp(-0.5 * z * z);
      final barH = density * histH * 0.88;
      final x = startX + i * binW;
      canvas.drawRRect(
        RRect.fromRectAndRadius(
          Rect.fromLTWH(x + 2, histAreaBottom - barH, binW - 4, barH),
          const Radius.circular(4),
        ),
        Paint()..color = palette.indigo.withValues(alpha: 0.55),
      );
    }

    for (int k = 0; k <= 80; k++) {
      final frac = k / 80;
      final val = frac * rows;
      final z = (val - mu) / sigma;
      final density = math.exp(-0.5 * z * z);
      final gx = startX + (frac * spanW);
      final gy = histAreaBottom - density * histH * 0.90;
      if (k == 0) {
        gaussPath.moveTo(gx, gy);
      } else {
        gaussPath.lineTo(gx, gy);
      }
    }
    canvas.drawPath(
      gaussPath,
      Paint()
        ..color = palette.green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.4,
    );

    _drawLabel(
      canvas,
      'N($rows, p=${pRight.toStringAsFixed(2)}) → μ=${mu.toStringAsFixed(2)}, σ=${sigma.toStringAsFixed(2)}',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  // ===========================================================================
  // 24. HIDRÁULICA Y NEUMÁTICA — EFECTO VENTURI Y ECUACIÓN DE BERNOULLI
  // ===========================================================================
  void _paintHidraulicaVenturi(Canvas canvas, Size size) {
    final throatRatio = params.paramA.clamp(0.35, 0.85); // D2 / D1
    final v1 = params.paramB.clamp(1.0, 6.0); // m/s
    // Por continuidad A1*v1 = A2*v2
    final areaRatio = 1.0 / (throatRatio * throatRatio);
    final v2 = v1 * areaRatio;
    const p1Kpa = 180.0;
    // Bernoulli (rho = 1000 kg/m3 -> en kPa: 0.5 * 1.0 * (v2^2 - v1^2))
    final deltaPKpa = 0.5 * (v2 * v2 - v1 * v1);
    final p2Kpa = math.max(15.0, p1Kpa - deltaPKpa);

    final tubeCenterY = size.height * 0.64;
    final halfH1 = size.height * 0.21;
    final halfH2 = halfH1 * throatRatio;
    const leftX = 18.0;
    final rightX = size.width - 18.0;
    final midX = size.width * 0.52;

    double halfHeightAt(double x) {
      final dist = ((x - midX).abs() / (size.width * 0.24)).clamp(0.0, 1.0);
      final smooth = dist * dist * (3 - 2 * dist);
      return halfH2 + (halfH1 - halfH2) * smooth;
    }

    // Tubo Venturi superior e inferior
    final tubePath = Path();
    const steps = 70;
    for (int i = 0; i <= steps; i++) {
      final x = leftX + (rightX - leftX) * (i / steps);
      final yTop = tubeCenterY - halfHeightAt(x);
      if (i == 0) {
        tubePath.moveTo(x, yTop);
      } else {
        tubePath.lineTo(x, yTop);
      }
    }
    for (int i = steps; i >= 0; i--) {
      final x = leftX + (rightX - leftX) * (i / steps);
      final yBot = tubeCenterY + halfHeightAt(x);
      tubePath.lineTo(x, yBot);
    }
    tubePath.close();

    canvas.drawPath(
      tubePath,
      Paint()..color = const Color(0xFF64D2FF).withValues(alpha: 0.16),
    );
    canvas.drawPath(
      tubePath,
      Paint()
        ..color = const Color(0xFF64D2FF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.2,
    );

    // Columnas manométricas P1 (entrada) y P2 (garganta)
    final p1X = size.width * 0.22;
    final p2X = midX;
    final maxColH = tubeCenterY - halfH1 - 24;
    final col1H = maxColH * (p1Kpa / 200.0).clamp(0.15, 1.0);
    final col2H = maxColH * (p2Kpa / 200.0).clamp(0.10, 1.0);

    for (final (cx, ch, baseHalf, label, col) in [
      (p1X, col1H, halfH1, 'P₁=${p1Kpa.toStringAsFixed(0)}kPa', palette.green),
      (p2X, col2H, halfH2, 'P₂=${p2Kpa.toStringAsFixed(0)}kPa', palette.orange),
    ]) {
      final colBottom = tubeCenterY - baseHalf;
      canvas.drawRect(
        Rect.fromLTWH(cx - 7, colBottom - ch, 14, ch),
        Paint()..color = col.withValues(alpha: 0.55),
      );
      _drawLabel(
        canvas,
        label,
        Offset(cx - 28, colBottom - ch - 14),
        color: col,
        fontSize: 9,
      );
    }

    // Partículas de fluido acelerando al cruzar la garganta
    const particles = 18;
    for (int i = 0; i < particles; i++) {
      final prog = ((params.timeSec * 0.22 * v1 + i / particles) % 1.0);
      final px = leftX + prog * (rightX - leftX);
      final hh = halfHeightAt(px);
      final lane = ((i % 3) - 1) * 0.48;
      final py = tubeCenterY + lane * hh;
      canvas.drawCircle(
        Offset(px, py),
        3.5,
        Paint()
          ..color = (px - midX).abs() < 42 ? palette.orange : palette.green,
      );
    }

    _drawLabel(
      canvas,
      'v₁=${v1.toStringAsFixed(1)} m/s → v₂=${v2.toStringAsFixed(1)} m/s | ΔP=${(p1Kpa - p2Kpa).toStringAsFixed(1)} kPa',
      const Offset(14, 6),
      color: palette.green,
    );
  }

  @override
  bool shouldRepaint(covariant Cuatrimestre3And4LabPainter oldDelegate) {
    return true;
  }
}

/// Generador de telemetría monoespaciada en vivo para la barra universal de movimiento.
class LabTelemetryBuilder {
  const LabTelemetryBuilder._();

  static String buildReadout(LabSimId id, LabSimParams p) {
    final tStr = 't=${p.timeSec.toStringAsFixed(1)}s';
    switch (id) {
      case LabSimId.calcDerivadaTangente:
        final x0 = (p.paramA + p.paramB * math.sin(p.timeSec * 1.15)).clamp(-2.3, 2.3);
        return '$tStr | x₀=${x0.toStringAsFixed(2)}';
      case LabSimId.calcLimites:
        return '$tStr | a=${p.paramA.toStringAsFixed(2)} | Zoom=${p.paramB.toStringAsFixed(1)}x';
      case LabSimId.algebraTransformaciones2D:
        final d = (p.subMode == 0) ? 1.0 : -0.8;
        final det = p.paramA * d - p.paramB * p.paramC;
        return '$tStr | det(A)=${det.toStringAsFixed(2)}';
      case LabSimId.progOrdenamiento:
        return '$tStr | N=${p.paramA.round()} barras';
      case LabSimId.progRegresionLineal:
        return '$tStr | α=${p.paramA.toStringAsFixed(2)} | Puntos=${p.customPoints.length}';
      case LabSimId.introFlujoEnergetico:
        final pUtil = p.paramA * (p.paramB / 100.0);
        return '$tStr | P_útil=${pUtil.toStringAsFixed(0)} MW (η=${p.paramB.toStringAsFixed(0)}%)';
      case LabSimId.fisicaMasaResorte:
        final w0 = math.sqrt(p.paramB / p.paramA);
        return '$tStr | ω₀=${w0.toStringAsFixed(2)} rad/s | μ=${p.paramC.toStringAsFixed(2)}';
      case LabSimId.fisicaTiroParabolico:
        final th = p.paramA * math.pi / 180.0;
        final r = (p.paramB * p.paramB * math.sin(2 * th)) / p.paramC;
        return '$tStr | R=${r.toStringAsFixed(1)}m | v₀=${p.paramB.toStringAsFixed(0)}m/s';
      case LabSimId.fisicaPlanoInclinadoDcl:
        final th = p.paramA * math.pi / 180.0;
        final a = math.max(0.0, 9.81 * (math.sin(th) - p.paramB * math.cos(th)));
        return '$tStr | a=${a.toStringAsFixed(2)} m/s² | θ=${p.paramA.toStringAsFixed(0)}°';
      case LabSimId.fisicaColisiones1D:
        return '$tStr | m₁=${p.paramA.toStringAsFixed(1)}kg, m₂=${p.paramB.toStringAsFixed(1)}kg | e=${p.paramC.toStringAsFixed(2)}';
      case LabSimId.integralRiemann:
        return '$tStr | n=${p.paramA.round()} rectángulos | b=${p.paramB.toStringAsFixed(1)}';
      case LabSimId.integralSolidoRevolucion:
        return '$tStr | b=${p.paramA.toStringAsFixed(1)} | Discos=${p.paramB.round()}';
      case LabSimId.quimicaGasesIdeales:
        final pres = (p.paramC * 0.08206 * p.paramA) / p.paramB;
        return '$tStr | P=${pres.toStringAsFixed(2)} atm | T=${p.paramA.toStringAsFixed(0)}K';
      case LabSimId.elec1CircuitoDc:
        final isPar = p.subMode % 2 == 1;
        final rEq = isPar
            ? (p.paramB * p.paramC) / (p.paramB + p.paramC)
            : (p.paramB + p.paramC);
        final cur = p.paramA / rEq;
        return '$tStr | I=${cur.toStringAsFixed(2)}A | R_eq=${rEq.toStringAsFixed(1)}Ω';
      case LabSimId.ondasViajerasArmonicos:
        return '$tStr | Armónico n=${p.paramA.round()} | A=${p.paramB.toStringAsFixed(2)}';
      case LabSimId.ondasPenduloFase:
        final w0 = math.sqrt(9.81 / p.paramA);
        return '$tStr | ω₀=${w0.toStringAsFixed(2)} rad/s | θ₀=${p.paramB.toStringAsFixed(0)}°';
      case LabSimId.modelacionOsciladorAmortiguado:
        return '$tStr | ζ=${p.paramA.toStringAsFixed(2)} | ω_n=${p.paramB.toStringAsFixed(1)}';
      case LabSimId.elec2FasoresCa:
        final fp = math.cos(p.paramB * math.pi / 180.0);
        return '$tStr | FP=${fp.toStringAsFixed(2)} | f=${p.paramC.toStringAsFixed(0)}Hz';
      case LabSimId.elec2TransitorioRcRl:
        return '$tStr | τ=${p.paramA.toStringAsFixed(2)}s | V_s=${p.paramB.toStringAsFixed(0)}V';
      case LabSimId.disenoProyeccion3D:
        return '$tStr | α=${p.paramA.toStringAsFixed(0)}° | β=${p.paramB.toStringAsFixed(0)}°';
      case LabSimId.emLeyFaraday:
        return '$tStr | N=${p.paramA.round()} esp | f=${p.paramB.toStringAsFixed(1)}Hz';
      case LabSimId.termoCicloPvPiston:
        final eta = (1.0 - 300.0 / p.paramA) * 100;
        return '$tStr | η_Carnot=${eta.toStringAsFixed(1)}% | r=${p.paramB.toStringAsFixed(1)}';
      case LabSimId.probTableroGalton:
        return '$tStr | Niveles=${p.paramA.round()} | p=${p.paramB.toStringAsFixed(2)}';
      case LabSimId.hidraulicaVenturiBernoulli:
        final v2 = p.paramB / (p.paramA * p.paramA);
        return '$tStr | v₂=${v2.toStringAsFixed(1)} m/s | D₂/D₁=${p.paramA.toStringAsFixed(2)}';
    }
  }
}
