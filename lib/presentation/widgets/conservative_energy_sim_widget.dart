import 'dart:math' as math;

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';

import '../../core/theme/app_theme.dart';
import 'ios_primitives.dart';

/// Identificador del problema de Cátedra 7 a simular.
enum ConservativeProblemType {
  curvedRamp,
  springFriction,
}

/// Perfil geométrico de la rampa en el Problema 1 (demuestra independencia de trayectoria).
enum RampCurveProfile {
  parabola,
  brachistochrone,
  wavy,
}

extension RampCurveProfileLabel on RampCurveProfile {
  String get label {
    switch (this) {
      case RampCurveProfile.parabola:
        return 'Parábola';
      case RampCurveProfile.brachistochrone:
        return 'Braquistócrona';
      case RampCurveProfile.wavy:
        return 'Doble Onda';
    }
  }
}

/// Estado instantáneo de la simulación computacional física.
@immutable
class PhysicsSimSnapshot {
  const PhysicsSimSnapshot({
    required this.time,
    required this.x,
    required this.y,
    required this.speed,
    required this.vx,
    required this.vy,
    required this.kineticEnergy,
    required this.gravitationalEnergy,
    required this.elasticEnergy,
    required this.dissipatedThermalEnergy,
    required this.totalMechanicalEnergy,
    required this.initialMechanicalEnergy,
    required this.normalForce,
    required this.frictionForce,
    required this.isFinished,
    required this.inRoughZone,
  });

  final double time;
  final double x;
  final double y;
  final double speed;
  final double vx;
  final double vy;
  final double kineticEnergy;
  final double gravitationalEnergy;
  final double elasticEnergy;
  final double dissipatedThermalEnergy;
  final double totalMechanicalEnergy;
  final double initialMechanicalEnergy;
  final double normalForce;
  final double frictionForce;
  final bool isFinished;
  final bool inRoughZone;
}

/// Motor físico computacional determinista (RK4 / sub-pasos) para Cátedra 7.
class ConservativeEnergyPhysics {
  static const double gravity = 9.8;
  static const double rampHorizontalSpan = 6.0;
  static const double rampRunoutLength = 1.1;

  /// Evalúa la altura `y(x)` de la rampa sin fricción en `[0, rampHorizontalSpan]`.
  static double rampHeight(
    double x,
    double initialHeight,
    RampCurveProfile profile,
  ) {
    if (x >= rampHorizontalSpan) return 0.0;
    final u = (x / rampHorizontalSpan).clamp(0.0, 1.0);
    switch (profile) {
      case RampCurveProfile.parabola:
        final oneMinusU = 1.0 - u;
        return initialHeight * oneMinusU * oneMinusU;
      case RampCurveProfile.brachistochrone:
        return initialHeight * math.pow(1.0 - u, 2.75).toDouble();
      case RampCurveProfile.wavy:
        return initialHeight *
            ((1.0 - u) + 0.12 * math.sin(2.0 * math.pi * u)).clamp(0.0, 1.2);
    }
  }

  /// Derivada espacial `dy/dx` de la rampa en `[0, rampHorizontalSpan]`.
  static double rampSlope(
    double x,
    double initialHeight,
    RampCurveProfile profile,
  ) {
    if (x >= rampHorizontalSpan) return 0.0;
    final u = (x / rampHorizontalSpan).clamp(0.0, 1.0);
    const l = rampHorizontalSpan;
    switch (profile) {
      case RampCurveProfile.parabola:
        return -2.0 * initialHeight * (1.0 - u) / l;
      case RampCurveProfile.brachistochrone:
        if (u >= 0.9999) return 0.0;
        return -2.75 * initialHeight * math.pow(1.0 - u, 1.75).toDouble() / l;
      case RampCurveProfile.wavy:
        return initialHeight *
            ((-1.0 + 0.12 * 2.0 * math.pi * math.cos(2.0 * math.pi * u)) / l);
    }
  }

  /// Calcula la solución analítica esperada para el Problema 1: `v_f = sqrt(2gh)`.
  static double analyticalRampFinalSpeed(double height) =>
      math.sqrt(2.0 * gravity * height);

  /// Calcula la solución analítica esperada para el Problema 2:
  /// `d = (0.5 * k * x_i^2) / (mu_k * m * g)`.
  static double analyticalStoppingDistance({
    required double mass,
    required double springK,
    required double compression,
    required double muK,
  }) {
    final denom = muK * mass * gravity;
    if (denom <= 1e-9) return 0.0;
    return (0.5 * springK * compression * compression) / denom;
  }

  /// Avanza un paso de tiempo `dt` usando sub-pasos RK4 en la rampa curva (Problema 1).
  static PhysicsSimSnapshot stepRamp(
    PhysicsSimSnapshot current, {
    required double dt,
    required double mass,
    required double initialHeight,
    required RampCurveProfile profile,
  }) {
    final e0 = mass * gravity * initialHeight;
    if (current.isFinished || dt <= 0) {
      return current;
    }

    const subSteps = 8;
    final h = dt / subSteps;
    var x = current.x;
    var v = current.speed;
    var t = current.time;
    const totalX = rampHorizontalSpan + rampRunoutLength;

    for (var i = 0; i < subSteps; i++) {
      if (x >= totalX) break;

      (double dx, double dv) deriv(double px, double pv) {
        if (px >= rampHorizontalSpan) {
          return (pv, 0.0);
        }
        final slope = rampSlope(px, initialHeight, profile);
        final sec = math.sqrt(1.0 + slope * slope);
        final dxDt = pv / sec;
        final sinTheta = -slope / sec;
        final dvDt = gravity * sinTheta;
        return (dxDt, dvDt);
      }

      final k1 = deriv(x, v);
      final k2 = deriv(x + 0.5 * h * k1.$1, v + 0.5 * h * k1.$2);
      final k3 = deriv(x + 0.5 * h * k2.$1, v + 0.5 * h * k2.$2);
      final k4 = deriv(x + h * k3.$1, v + h * k3.$2);

      x += (h / 6.0) * (k1.$1 + 2.0 * k2.$1 + 2.0 * k3.$1 + k4.$1);
      v += (h / 6.0) * (k1.$2 + 2.0 * k2.$2 + 2.0 * k3.$2 + k4.$2);
      t += h;

      // Corrección energética de Gauss-Newton para suprimir deriva numérica en RK4.
      final yCurrent = rampHeight(x, initialHeight, profile);
      final expectedK = (e0 - mass * gravity * yCurrent).clamp(0.0, e0);
      v = math.sqrt(2.0 * expectedK / mass);

      if (x >= totalX) {
        x = totalX;
        break;
      }
    }

    final y = rampHeight(x, initialHeight, profile);
    final slope = rampSlope(x, initialHeight, profile);
    final sec = math.sqrt(1.0 + slope * slope);
    final cosTheta = 1.0 / sec;
    final vx = v * cosTheta;
    final vy = v * slope * cosTheta;

    final ug = mass * gravity * y;
    final k = 0.5 * mass * v * v;
    final em = ug + k;
    final normal = mass * gravity * cosTheta;

    return PhysicsSimSnapshot(
      time: t,
      x: x,
      y: y,
      speed: v,
      vx: vx,
      vy: vy,
      kineticEnergy: k,
      gravitationalEnergy: ug,
      elasticEnergy: 0.0,
      dissipatedThermalEnergy: 0.0,
      totalMechanicalEnergy: em,
      initialMechanicalEnergy: e0,
      normalForce: normal,
      frictionForce: 0.0,
      isFinished: x >= totalX,
      inRoughZone: false,
    );
  }

  /// Avanza un paso de tiempo `dt` con RK4 por tramos para el Problema 2 (Resorte + Pista Rugosa).
  static PhysicsSimSnapshot stepSpringFriction(
    PhysicsSimSnapshot current, {
    required double dt,
    required double mass,
    required double springK,
    required double compression,
    required double muK,
  }) {
    final e0 = 0.5 * springK * compression * compression;
    if (current.isFinished || dt <= 0) {
      return current;
    }

    const subSteps = 10;
    final h = dt / subSteps;
    var x = current.x;
    var v = current.vx;
    var t = current.time;
    var finished = false;
    final frictionMag = muK * mass * gravity;

    for (var i = 0; i < subSteps; i++) {
      if (x < 0.0) {
        // Fase 1: Impulso elástico puro sobre superficie lisa (x <= 0).
        (double dx, double dv) derivSpring(double px, double pv) {
          return (pv, -(springK / mass) * px);
        }

        final k1 = derivSpring(x, v);
        final k2 = derivSpring(x + 0.5 * h * k1.$1, v + 0.5 * h * k1.$2);
        final k3 = derivSpring(x + 0.5 * h * k2.$1, v + 0.5 * h * k2.$2);
        final k4 = derivSpring(x + h * k3.$1, v + h * k3.$2);

        final nextX = x + (h / 6.0) * (k1.$1 + 2.0 * k2.$1 + 2.0 * k3.$1 + k4.$1);
        final nextV = v + (h / 6.0) * (k1.$2 + 2.0 * k2.$2 + 2.0 * k3.$2 + k4.$2);

        if (nextX >= 0.0) {
          // Cruce exacto del punto de equilibrio x = 0: toda Ue pasa a K.
          final frac = (-x) / ((nextX - x).abs().clamp(1e-9, 1e9));
          final vAtZero = math.sqrt((2.0 * e0 / mass).clamp(0.0, double.infinity));
          final remDt = h * (1.0 - frac).clamp(0.0, 1.0);
          final decel = frictionMag / mass;
          final vxAfter = (vAtZero - decel * remDt).clamp(0.0, vAtZero);
          x = vAtZero * remDt - 0.5 * decel * remDt * remDt;
          v = vxAfter;
          t += h;
        } else {
          x = nextX;
          v = nextV;
          t += h;
        }
      } else {
        // Fase 2: Desaceleración constante por fricción cinética (x >= 0).
        final decel = frictionMag / mass;
        if (v - decel * h <= 0.0) {
          final stopDt = v / decel;
          x += v * stopDt - 0.5 * decel * stopDt * stopDt;
          v = 0.0;
          t += stopDt;
          finished = true;
          break;
        } else {
          x += v * h - 0.5 * decel * h * h;
          v -= decel * h;
          t += h;
        }
      }
    }

    final ue = x < 0.0 ? 0.5 * springK * x * x : 0.0;
    final k = 0.5 * mass * v * v;
    final dissipated = x > 0.0 ? (frictionMag * x).clamp(0.0, e0) : 0.0;
    final em = ue + k;

    return PhysicsSimSnapshot(
      time: t,
      x: x,
      y: 0.0,
      speed: v.abs(),
      vx: v,
      vy: 0.0,
      kineticEnergy: k,
      gravitationalEnergy: 0.0,
      elasticEnergy: ue,
      dissipatedThermalEnergy: dissipated,
      totalMechanicalEnergy: em,
      initialMechanicalEnergy: e0,
      normalForce: mass * gravity,
      frictionForce: x >= 0.0 && !finished ? frictionMag : 0.0,
      isFinished: finished,
      inRoughZone: x >= 0.0,
    );
  }

  /// Simula de principio a fin cualquiera de los dos problemas y devuelve la trayectoria.
  static List<PhysicsSimSnapshot> runTrajectory({
    required ConservativeProblemType problem,
    double rampMass = 2.0,
    double rampHeightM = 3.6,
    RampCurveProfile rampProfile = RampCurveProfile.parabola,
    double springMass = 1.5,
    double springK = 400.0,
    double springCompression = 0.20,
    double muK = 0.35,
    double dt = 1.0 / 60.0,
    int maxSteps = 1200,
  }) {
    var snap = initialSnapshot(
      problem: problem,
      rampMass: rampMass,
      rampHeightM: rampHeightM,
      springMass: springMass,
      springK: springK,
      springCompression: springCompression,
    );
    final trace = <PhysicsSimSnapshot>[snap];
    for (var i = 0; i < maxSteps && !snap.isFinished; i++) {
      snap = problem == ConservativeProblemType.curvedRamp
          ? stepRamp(
              snap,
              dt: dt,
              mass: rampMass,
              initialHeight: rampHeightM,
              profile: rampProfile,
            )
          : stepSpringFriction(
              snap,
              dt: dt,
              mass: springMass,
              springK: springK,
              compression: springCompression,
              muK: muK,
            );
      trace.add(snap);
    }
    return trace;
  }

  static PhysicsSimSnapshot initialSnapshot({
    required ConservativeProblemType problem,
    double rampMass = 2.0,
    double rampHeightM = 3.6,
    double springMass = 1.5,
    double springK = 400.0,
    double springCompression = 0.20,
  }) {
    if (problem == ConservativeProblemType.curvedRamp) {
      final e0 = rampMass * gravity * rampHeightM;
      return PhysicsSimSnapshot(
        time: 0.0,
        x: 0.0,
        y: rampHeightM,
        speed: 0.0,
        vx: 0.0,
        vy: 0.0,
        kineticEnergy: 0.0,
        gravitationalEnergy: e0,
        elasticEnergy: 0.0,
        dissipatedThermalEnergy: 0.0,
        totalMechanicalEnergy: e0,
        initialMechanicalEnergy: e0,
        normalForce: rampMass * gravity,
        frictionForce: 0.0,
        isFinished: false,
        inRoughZone: false,
      );
    } else {
      final e0 = 0.5 * springK * springCompression * springCompression;
      return PhysicsSimSnapshot(
        time: 0.0,
        x: -springCompression,
        y: 0.0,
        speed: 0.0,
        vx: 0.0,
        vy: 0.0,
        kineticEnergy: 0.0,
        gravitationalEnergy: 0.0,
        elasticEnergy: e0,
        dissipatedThermalEnergy: 0.0,
        totalMechanicalEnergy: e0,
        initialMechanicalEnergy: e0,
        normalForce: springMass * gravity,
        frictionForce: 0.0,
        isFinished: false,
        inRoughZone: false,
      );
    }
  }
}

class _HeatSpark {
  _HeatSpark({
    required this.wx,
    required this.wy,
    required this.wz,
    required this.vx,
    required this.vy,
    required this.life,
  });

  double wx;
  double wy;
  double wz;
  double vx;
  double vy;
  double life; // 1.0 -> 0.0
}

/// Laboratorio Computacional 2D Semi-3D (2.5D) interactivo para Cátedra 7 de Física Mecánica.
class ConservativeEnergySimWidget extends StatefulWidget {
  const ConservativeEnergySimWidget({
    super.key,
    this.isDesktop = false,
  });

  final bool isDesktop;

  @override
  State<ConservativeEnergySimWidget> createState() =>
      _ConservativeEnergySimWidgetState();
}

class _ConservativeEnergySimWidgetState extends State<ConservativeEnergySimWidget>
    with SingleTickerProviderStateMixin {
  ConservativeProblemType _problem = ConservativeProblemType.curvedRamp;
  RampCurveProfile _rampProfile = RampCurveProfile.parabola;

  // Parámetros Problema 1 (valores por defecto de Cátedra 7)
  double _rampMass = 2.0;
  double _rampHeight = 3.6;

  // Parámetros Problema 2 (valores por defecto de Cátedra 7)
  double _springMass = 1.5;
  double _springK = 400.0;
  double _springCompression = 0.20;
  double _muK = 0.35;

  late PhysicsSimSnapshot _snapshot;
  final List<_HeatSpark> _sparks = <_HeatSpark>[];
  final math.Random _rng = math.Random(7);

  late final Ticker _ticker;
  Duration? _lastElapsed;
  bool _isPlaying = true;
  bool _slowMotion = false;
  bool _showParameters = false;

  @override
  void initState() {
    super.initState();
    _snapshot = _buildInitialSnapshot();
    _ticker = createTicker(_onTick)..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  PhysicsSimSnapshot _buildInitialSnapshot() {
    return ConservativeEnergyPhysics.initialSnapshot(
      problem: _problem,
      rampMass: _rampMass,
      rampHeightM: _rampHeight,
      springMass: _springMass,
      springK: _springK,
      springCompression: _springCompression,
    );
  }

  void _resetSimulation({bool autoPlay = true}) {
    setState(() {
      _sparks.clear();
      _snapshot = _buildInitialSnapshot();
      _lastElapsed = null;
      _isPlaying = autoPlay;
    });
  }

  void _resetToCatedraDefaults() {
    setState(() {
      _rampMass = 2.0;
      _rampHeight = 3.6;
      _rampProfile = RampCurveProfile.parabola;
      _springMass = 1.5;
      _springK = 400.0;
      _springCompression = 0.20;
      _muK = 0.35;
      _sparks.clear();
      _snapshot = _buildInitialSnapshot();
      _lastElapsed = null;
      _isPlaying = true;
    });
  }

  void _onTick(Duration elapsed) {
    final prev = _lastElapsed;
    _lastElapsed = elapsed;
    if (prev == null || !_isPlaying) return;

    final rawDt = (elapsed - prev).inMicroseconds / 1e6;
    final clampedDt = rawDt.clamp(0.0, 0.04);
    if (clampedDt <= 0) return;

    final simDt = clampedDt * (_slowMotion ? 0.35 : 1.0);

    if (_snapshot.isFinished) {
      // Actualiza las chispas restantes hasta disiparse.
      if (_sparks.isNotEmpty) {
        setState(() {
          _updateSparks(clampedDt, emit: false);
        });
      }
      return;
    }

    setState(() {
      _snapshot = _problem == ConservativeProblemType.curvedRamp
          ? ConservativeEnergyPhysics.stepRamp(
              _snapshot,
              dt: simDt,
              mass: _rampMass,
              initialHeight: _rampHeight,
              profile: _rampProfile,
            )
          : ConservativeEnergyPhysics.stepSpringFriction(
              _snapshot,
              dt: simDt,
              mass: _springMass,
              springK: _springK,
              compression: _springCompression,
              muK: _muK,
            );

      _updateSparks(
        simDt,
        emit: _problem == ConservativeProblemType.springFriction &&
            _snapshot.inRoughZone &&
            _snapshot.speed > 0.08,
      );
    });
  }

  void _updateSparks(double dt, {required bool emit}) {
    if (emit && _sparks.length < 28) {
      final count = _snapshot.speed > 1.5 ? 2 : 1;
      for (var i = 0; i < count; i++) {
        _sparks.add(
          _HeatSpark(
            wx: _snapshot.x + (_rng.nextDouble() - 0.5) * 0.08,
            wy: 0.03,
            wz: (_rng.nextDouble() - 0.5) * 0.45,
            vx: -0.35 - _rng.nextDouble() * 0.6,
            vy: 0.25 + _rng.nextDouble() * 0.55,
            life: 1.0,
          ),
        );
      }
    }
    for (var i = _sparks.length - 1; i >= 0; i--) {
      final s = _sparks[i];
      s.wx += s.vx * dt;
      s.wy += s.vy * dt;
      s.vy -= 0.4 * dt;
      s.life -= dt * 1.4;
      if (s.life <= 0) {
        _sparks.removeAt(i);
      }
    }
  }

  void _selectProblem(ConservativeProblemType problem) {
    if (_problem == problem) return;
    setState(() {
      _problem = problem;
      _sparks.clear();
      _snapshot = _buildInitialSnapshot();
      _lastElapsed = null;
      _isPlaying = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final accent = _problem == ConservativeProblemType.curvedRamp
        ? p.green
        : p.orange;

    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.strongBorder),
        boxShadow: isDark
            ? [
                BoxShadow(
                  color: accent.o(0.08),
                  blurRadius: 24,
                  offset: const Offset(0, 8),
                ),
              ]
            : null,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          _buildHeader(p, accent),
          Divider(height: 1, color: p.cardBorder),
          Padding(
            padding: EdgeInsets.all(widget.isDesktop ? 16 : 12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                _buildProblemSelector(p),
                if (_problem == ConservativeProblemType.curvedRamp) ...[
                  const SizedBox(height: 8),
                  _buildCurveProfileSelector(p),
                ],
                const SizedBox(height: 10),
                _buildViewport(p, isDark),
                const SizedBox(height: 10),
                _buildTransportBar(p, accent),
                const SizedBox(height: 12),
                _buildEnergyTelemetry(p),
                if (_showParameters) ...[
                  const SizedBox(height: 12),
                  _buildParameterPanel(p, accent),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHeader(AppPalette p, Color accent) {
    return Padding(
      padding: EdgeInsets.symmetric(
        horizontal: widget.isDesktop ? 16 : 14,
        vertical: 12,
      ),
      child: Row(
        children: [
          Container(
            width: 30,
            height: 30,
            decoration: BoxDecoration(
              color: accent.o(0.14),
              borderRadius: BorderRadius.circular(9),
              border: Border.all(color: accent.o(0.35)),
            ),
            child: Icon(
              CupertinoIcons.cube_box_fill,
              size: 16,
              color: accent,
            ),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'LABORATORIO COMPUTACIONAL 2.5D • CÁTEDRA 7',
                  style: mono(
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 1.0,
                    color: accent,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  _problem == ConservativeProblemType.curvedRamp
                      ? 'Problema 01: Conservación en Rampa Curva sin Fricción'
                      : 'Problema 02: Resorte Comprimido y Pista Rugosa',
                  style: TextStyle(
                    fontSize: 13.5,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: p.elevated,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: p.cardBorder),
            ),
            child: Text(
              'RK4 • 2.5D',
              style: mono(
                fontSize: 10,
                fontWeight: FontWeight.w600,
                color: p.textSecondary,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildProblemSelector(AppPalette p) {
    return Container(
      padding: const EdgeInsets.all(3),
      decoration: BoxDecoration(
        color: p.elevated,
        borderRadius: BorderRadius.circular(11),
        border: Border.all(color: p.cardBorder),
      ),
      child: Row(
        children: [
          Expanded(
            child: _SegmentButton(
              label: 'P1 • Rampa Curva (FNC = 0)',
              selected: _problem == ConservativeProblemType.curvedRamp,
              accent: p.green,
              onTap: () => _selectProblem(ConservativeProblemType.curvedRamp),
            ),
          ),
          const SizedBox(width: 4),
          Expanded(
            child: _SegmentButton(
              label: 'P2 • Resorte + Fricción (fk ≠ 0)',
              selected: _problem == ConservativeProblemType.springFriction,
              accent: p.orange,
              onTap: () =>
                  _selectProblem(ConservativeProblemType.springFriction),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCurveProfileSelector(AppPalette p) {
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      crossAxisAlignment: WrapCrossAlignment.center,
      children: [
        Text(
          'Trayectoria:',
          style: mono(fontSize: 10.5, color: p.textSecondary),
        ),
        for (final profile in RampCurveProfile.values)
          TapScale(
            onTap: () {
              if (_rampProfile == profile) return;
              setState(() {
                _rampProfile = profile;
                _snapshot = _buildInitialSnapshot();
                _lastElapsed = null;
                _isPlaying = true;
              });
            },
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 180),
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
              decoration: BoxDecoration(
                color: _rampProfile == profile
                    ? p.green.o(0.18)
                    : p.elevated,
                borderRadius: BorderRadius.circular(999),
                border: Border.all(
                  color: _rampProfile == profile ? p.green : p.cardBorder,
                ),
              ),
              child: Text(
                profile.label,
                style: TextStyle(
                  fontSize: 11.5,
                  fontWeight: _rampProfile == profile
                      ? FontWeight.w600
                      : FontWeight.w500,
                  color: _rampProfile == profile ? p.green : p.textSecondary,
                ),
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildViewport(AppPalette p, bool isDark) {
    final viewportHeight = widget.isDesktop ? 280.0 : 230.0;
    return ClipRRect(
      borderRadius: BorderRadius.circular(14),
      child: GestureDetector(
        onTap: () {
          setState(() {
            if (_snapshot.isFinished) {
              _sparks.clear();
              _snapshot = _buildInitialSnapshot();
              _isPlaying = true;
            } else {
              _isPlaying = !_isPlaying;
            }
          });
        },
        child: Container(
          height: viewportHeight,
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: isDark
                  ? const [Color(0xFF0A0D14), Color(0xFF121622)]
                  : const [Color(0xFFF6F8FC), Color(0xFFE9EEF7)],
            ),
            border: Border.all(color: p.strongBorder),
            borderRadius: BorderRadius.circular(14),
          ),
          child: Stack(
            children: [
              Positioned.fill(
                child: RepaintBoundary(
                  child: CustomPaint(
                    painter: _Semi3DPhysicsPainter(
                      problem: _problem,
                      rampProfile: _rampProfile,
                      snapshot: _snapshot,
                      sparks: _sparks,
                      rampHeight: _rampHeight,
                      rampMass: _rampMass,
                      springMass: _springMass,
                      springK: _springK,
                      springCompression: _springCompression,
                      muK: _muK,
                      palette: p,
                      isDark: isDark,
                    ),
                  ),
                ),
              ),
              Positioned(
                top: 10,
                left: 10,
                child: _OverlayHudPill(
                  palette: p,
                  text:
                      't = ${_snapshot.time.toStringAsFixed(2)} s  •  v = ${_snapshot.speed.toStringAsFixed(2)} m/s',
                ),
              ),
              Positioned(
                top: 10,
                right: 10,
                child: _OverlayHudPill(
                  palette: p,
                  text: _problem == ConservativeProblemType.curvedRamp
                      ? 'y = ${_snapshot.y.toStringAsFixed(2)} m'
                      : 'x = ${_snapshot.x >= 0 ? '+' : ''}${_snapshot.x.toStringAsFixed(3)} m',
                ),
              ),
              if (!_isPlaying || _snapshot.isFinished)
                Positioned(
                  bottom: 10,
                  right: 10,
                  child: _OverlayHudPill(
                    palette: p,
                    accent: _snapshot.isFinished
                        ? (_problem == ConservativeProblemType.curvedRamp
                            ? p.green
                            : p.orange)
                        : null,
                    text: _snapshot.isFinished
                        ? 'COMPLETADO • Toca para repetir'
                        : 'PAUSADO • Toca para continuar',
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTransportBar(AppPalette p, Color accent) {
    return Wrap(
      spacing: 8,
      runSpacing: 8,
      crossAxisAlignment: WrapCrossAlignment.center,
      children: [
        _ActionChip(
          icon: _snapshot.isFinished
              ? CupertinoIcons.arrow_counterclockwise
              : (_isPlaying ? CupertinoIcons.pause_fill : CupertinoIcons.play_fill),
          label: _snapshot.isFinished
              ? 'Repetir'
              : (_isPlaying ? 'Pausar' : 'Simular'),
          color: accent,
          filled: true,
          onTap: () {
            if (_snapshot.isFinished) {
              _resetSimulation(autoPlay: true);
            } else {
              setState(() => _isPlaying = !_isPlaying);
            }
          },
        ),
        _ActionChip(
          icon: CupertinoIcons.restart,
          label: 'Reiniciar',
          color: p.textSecondary,
          onTap: () => _resetSimulation(autoPlay: true),
        ),
        _ActionChip(
          icon: CupertinoIcons.tortoise_fill,
          label: _slowMotion ? '0.35× Lento' : '1.0× Real',
          color: _slowMotion ? p.indigo : p.textSecondary,
          filled: _slowMotion,
          onTap: () => setState(() => _slowMotion = !_slowMotion),
        ),
        _ActionChip(
          icon: CupertinoIcons.slider_horizontal_3,
          label: _showParameters ? 'Ocultar Parámetros' : 'Ajustar Variables',
          color: _showParameters ? accent : p.textSecondary,
          filled: _showParameters,
          onTap: () => setState(() => _showParameters = !_showParameters),
        ),
      ],
    );
  }

  Widget _buildEnergyTelemetry(AppPalette p) {
    final e0 = _snapshot.initialMechanicalEnergy.clamp(1e-6, double.infinity);
    final kFrac = (_snapshot.kineticEnergy / e0).clamp(0.0, 1.0);
    final ugFrac = (_snapshot.gravitationalEnergy / e0).clamp(0.0, 1.0);
    final ueFrac = (_snapshot.elasticEnergy / e0).clamp(0.0, 1.0);
    final qFrac = (_snapshot.dissipatedThermalEnergy / e0).clamp(0.0, 1.0);
    final emFrac = (_snapshot.totalMechanicalEnergy / e0).clamp(0.0, 1.0);

    final verificationText = _problem == ConservativeProblemType.curvedRamp
        ? 'Teoría vs Cómputo: v_f = √(2gh) = ${ConservativeEnergyPhysics.analyticalRampFinalSpeed(_rampHeight).toStringAsFixed(2)} m/s • EM = ${e0.toStringAsFixed(2)} J constante (independiente de m y trayectoria)'
        : 'Teoría vs Cómputo: d = ½kxᵢ² / (μₖmg) = ${ConservativeEnergyPhysics.analyticalStoppingDistance(mass: _springMass, springK: _springK, compression: _springCompression, muK: _muK).toStringAsFixed(3)} m • |W_FNC| = ${e0.toStringAsFixed(2)} J disipados';

    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: p.elevated,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Wrap(
            alignment: WrapAlignment.spaceBetween,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 8,
            runSpacing: 4,
            children: [
              Text(
                'BALANCE ENERGÉTICO EN TIEMPO REAL',
                style: mono(
                  fontSize: 10,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.8,
                  color: p.textSecondary,
                ),
              ),
              Text(
                'E_inicial = ${e0.toStringAsFixed(2)} J',
                style: mono(
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  color: p.textPrimary,
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          _EnergyBarRow(
            label: 'K (Cinética)',
            valueText: '${_snapshot.kineticEnergy.toStringAsFixed(2)} J',
            fraction: kFrac,
            color: const Color(0xFF0A84FF),
            palette: p,
          ),
          const SizedBox(height: 6),
          if (_problem == ConservativeProblemType.curvedRamp) ...[
            _EnergyBarRow(
              label: 'Ug (Gravitatoria)',
              valueText: '${_snapshot.gravitationalEnergy.toStringAsFixed(2)} J',
              fraction: ugFrac,
              color: p.green,
              palette: p,
            ),
            const SizedBox(height: 6),
          ] else ...[
            _EnergyBarRow(
              label: 'Ue (Elástica)',
              valueText: '${_snapshot.elasticEnergy.toStringAsFixed(2)} J',
              fraction: ueFrac,
              color: p.indigo,
              palette: p,
            ),
            const SizedBox(height: 6),
            _EnergyBarRow(
              label: '|W_FNC| (Calor Q)',
              valueText:
                  '${_snapshot.dissipatedThermalEnergy.toStringAsFixed(2)} J',
              fraction: qFrac,
              color: const Color(0xFFFF453A),
              palette: p,
            ),
            const SizedBox(height: 6),
          ],
          _EnergyBarRow(
            label: 'EM (Mecánica Total)',
            valueText:
                '${_snapshot.totalMechanicalEnergy.toStringAsFixed(2)} J',
            fraction: emFrac,
            color: p.orange,
            palette: p,
          ),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
            decoration: BoxDecoration(
              color: p.card,
              borderRadius: BorderRadius.circular(9),
              border: Border.all(color: p.cardBorder),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(
                  CupertinoIcons.checkmark_seal_fill,
                  size: 14,
                  color: _problem == ConservativeProblemType.curvedRamp
                      ? p.green
                      : p.orange,
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    verificationText,
                    style: mono(
                      fontSize: 10.5,
                      height: 1.35,
                      color: p.textBody,
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

  Widget _buildParameterPanel(AppPalette p, Color accent) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: p.elevated,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Wrap(
            alignment: WrapAlignment.spaceBetween,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 8,
            runSpacing: 6,
            children: [
              Text(
                'PARÁMETROS EXPERIMENTALES',
                style: mono(
                  fontSize: 10,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.8,
                  color: p.textSecondary,
                ),
              ),
              TapScale(
                onTap: _resetToCatedraDefaults,
                child: Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: accent.o(0.14),
                    borderRadius: BorderRadius.circular(7),
                  ),
                  child: Text(
                    'Valores Cátedra 7',
                    style: mono(
                      fontSize: 10,
                      fontWeight: FontWeight.w700,
                      color: accent,
                    ),
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          if (_problem == ConservativeProblemType.curvedRamp) ...[
            _ParamSliderRow(
              label: 'Masa m',
              valueLabel: '${_rampMass.toStringAsFixed(1)} kg',
              value: _rampMass,
              min: 0.5,
              max: 8.0,
              accent: accent,
              palette: p,
              onChanged: (val) {
                setState(() {
                  _rampMass = val;
                  _snapshot = _buildInitialSnapshot();
                  _lastElapsed = null;
                });
              },
            ),
            _ParamSliderRow(
              label: 'Altura h',
              valueLabel: '${_rampHeight.toStringAsFixed(1)} m',
              value: _rampHeight,
              min: 1.0,
              max: 5.5,
              accent: accent,
              palette: p,
              onChanged: (val) {
                setState(() {
                  _rampHeight = val;
                  _snapshot = _buildInitialSnapshot();
                  _lastElapsed = null;
                });
              },
            ),
          ] else ...[
            _ParamSliderRow(
              label: 'Constante k',
              valueLabel: '${_springK.toStringAsFixed(0)} N/m',
              value: _springK,
              min: 150,
              max: 700,
              accent: accent,
              palette: p,
              onChanged: (val) {
                setState(() {
                  _springK = val;
                  _snapshot = _buildInitialSnapshot();
                  _lastElapsed = null;
                });
              },
            ),
            _ParamSliderRow(
              label: 'Compresión xᵢ',
              valueLabel: '${_springCompression.toStringAsFixed(2)} m',
              value: _springCompression,
              min: 0.10,
              max: 0.35,
              accent: accent,
              palette: p,
              onChanged: (val) {
                setState(() {
                  _springCompression = val;
                  _snapshot = _buildInitialSnapshot();
                  _lastElapsed = null;
                });
              },
            ),
            _ParamSliderRow(
              label: 'Fricción μₖ',
              valueLabel: _muK.toStringAsFixed(2),
              value: _muK,
              min: 0.12,
              max: 0.65,
              accent: accent,
              palette: p,
              onChanged: (val) {
                setState(() {
                  _muK = val;
                  _snapshot = _buildInitialSnapshot();
                  _lastElapsed = null;
                });
              },
            ),
          ],
        ],
      ),
    );
  }
}

class _SegmentButton extends StatelessWidget {
  const _SegmentButton({
    required this.label,
    required this.selected,
    required this.accent,
    required this.onTap,
  });

  final String label;
  final bool selected;
  final Color accent;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return TapScale(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
        decoration: BoxDecoration(
          color: selected ? p.card : Colors.transparent,
          borderRadius: BorderRadius.circular(9),
          border: Border.all(
            color: selected ? accent.o(0.6) : Colors.transparent,
          ),
        ),
        child: Text(
          label,
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: 11.5,
            fontWeight: selected ? FontWeight.w700 : FontWeight.w500,
            color: selected ? accent : p.textSecondary,
          ),
        ),
      ),
    );
  }
}

class _ActionChip extends StatelessWidget {
  const _ActionChip({
    required this.icon,
    required this.label,
    required this.color,
    required this.onTap,
    this.filled = false,
  });

  final IconData icon;
  final String label;
  final Color color;
  final VoidCallback onTap;
  final bool filled;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return TapScale(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 7),
        decoration: BoxDecoration(
          color: filled ? color.o(0.16) : p.elevated,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(
            color: filled ? color.o(0.55) : p.cardBorder,
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, size: 13, color: color),
            const SizedBox(width: 6),
            Text(
              label,
              style: TextStyle(
                fontSize: 11.5,
                fontWeight: FontWeight.w600,
                color: filled ? color : p.textBody,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _OverlayHudPill extends StatelessWidget {
  const _OverlayHudPill({
    required this.palette,
    required this.text,
    this.accent,
  });

  final AppPalette palette;
  final String text;
  final Color? accent;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: palette.glass,
        borderRadius: BorderRadius.circular(8),
        border: Border.all(
          color: accent != null ? accent!.o(0.55) : palette.cardBorder,
        ),
      ),
      child: Text(
        text,
        style: mono(
          fontSize: 10,
          fontWeight: FontWeight.w600,
          color: accent ?? palette.textPrimary,
        ),
      ),
    );
  }
}

class _EnergyBarRow extends StatelessWidget {
  const _EnergyBarRow({
    required this.label,
    required this.valueText,
    required this.fraction,
    required this.color,
    required this.palette,
  });

  final String label;
  final String valueText;
  final double fraction;
  final Color color;
  final AppPalette palette;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        SizedBox(
          width: 118,
          child: Text(
            label,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
              fontSize: 11,
              fontWeight: FontWeight.w500,
              color: palette.textBody,
            ),
          ),
        ),
        const SizedBox(width: 8),
        Expanded(
          child: ClipRRect(
            borderRadius: BorderRadius.circular(999),
            child: Container(
              height: 8,
              color: palette.card,
              alignment: Alignment.centerLeft,
              child: FractionallySizedBox(
                widthFactor: fraction.clamp(0.0, 1.0),
                child: Container(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [color.o(0.75), color],
                    ),
                    borderRadius: BorderRadius.circular(999),
                  ),
                ),
              ),
            ),
          ),
        ),
        const SizedBox(width: 8),
        SizedBox(
          width: 62,
          child: Text(
            valueText,
            textAlign: TextAlign.right,
            style: mono(
              fontSize: 10.5,
              fontWeight: FontWeight.w700,
              color: color,
            ),
          ),
        ),
      ],
    );
  }
}

class _ParamSliderRow extends StatelessWidget {
  const _ParamSliderRow({
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
          width: 88,
          child: Text(
            label,
            style: TextStyle(fontSize: 11.5, color: palette.textBody),
          ),
        ),
        Expanded(
          child: SliderTheme(
            data: SliderTheme.of(context).copyWith(
              trackHeight: 3,
              thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 6),
              overlayShape: const RoundSliderOverlayShape(overlayRadius: 12),
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
          width: 64,
          child: Text(
            valueLabel,
            textAlign: TextAlign.right,
            style: mono(
              fontSize: 10.5,
              fontWeight: FontWeight.w600,
              color: palette.textPrimary,
            ),
          ),
        ),
      ],
    );
  }
}

/// Renderizador 2D Semi-3D (Proyección Oblicua Isométrica 2.5D) con sombras,
/// volúmenes extruidos, resorte helicoidal dinámico, vectores y partículas de calor.
class _Semi3DPhysicsPainter extends CustomPainter {
  _Semi3DPhysicsPainter({
    required this.problem,
    required this.rampProfile,
    required this.snapshot,
    required this.sparks,
    required this.rampHeight,
    required this.rampMass,
    required this.springMass,
    required this.springK,
    required this.springCompression,
    required this.muK,
    required this.palette,
    required this.isDark,
  });

  final ConservativeProblemType problem;
  final RampCurveProfile rampProfile;
  final PhysicsSimSnapshot snapshot;
  final List<_HeatSpark> sparks;
  final double rampHeight;
  final double rampMass;
  final double springMass;
  final double springK;
  final double springCompression;
  final double muK;
  final AppPalette palette;
  final bool isDark;

  @override
  void paint(Canvas canvas, Size size) {
    if (problem == ConservativeProblemType.curvedRamp) {
      _paintCurvedRampScene(canvas, size);
    } else {
      _paintSpringFrictionScene(canvas, size);
    }
  }

  /// Proyección oblicua 2.5D: X derecha, Y arriba, Z profundidad (+dx, -dy).
  Offset _proj(
    double wx,
    double wy,
    double wz, {
    required Offset origin,
    required double scaleX,
    required double scaleY,
    double depthRatioX = 0.42,
    double depthRatioY = 0.28,
  }) {
    final px = origin.dx + wx * scaleX + wz * scaleX * depthRatioX;
    final py = origin.dy - wy * scaleY - wz * scaleY * depthRatioY;
    return Offset(px, py);
  }

  void _paintCurvedRampScene(Canvas canvas, Size size) {
    const totalX =
        ConservativeEnergyPhysics.rampHorizontalSpan +
        ConservativeEnergyPhysics.rampRunoutLength;
    final usableW = size.width * 0.74;
    final scaleX = usableW / totalX;
    final scaleY = (size.height * 0.56) / math.max(rampHeight, 2.5);
    final origin = Offset(size.width * 0.10, size.height * 0.80);
    const zFront = 0.0;
    const zBack = 1.15;

    // 1. Piso 2.5D con grilla de perspectiva y bisel inferior
    _drawFloorSlab(
      canvas,
      origin: origin,
      minX: -0.3,
      maxX: totalX + 0.4,
      zFront: -0.25,
      zBack: 1.5,
      scaleX: scaleX,
      scaleY: scaleY,
    );

    // 2. Superficie y volumen extruido de la rampa curva
    const samples = 56;
    final frontTop = <Offset>[];
    final backTop = <Offset>[];
    for (var i = 0; i <= samples; i++) {
      final wx = (totalX * i) / samples;
      final wy = ConservativeEnergyPhysics.rampHeight(wx, rampHeight, rampProfile);
      frontTop.add(_proj(wx, wy, zFront, origin: origin, scaleX: scaleX, scaleY: scaleY));
      backTop.add(_proj(wx, wy, zBack, origin: origin, scaleX: scaleX, scaleY: scaleY));
    }

    // Cara lateral frontal extruida hasta y = 0
    final frontWallPath = Path()..moveTo(frontTop.first.dx, frontTop.first.dy);
    for (final pt in frontTop.skip(1)) {
      frontWallPath.lineTo(pt.dx, pt.dy);
    }
    final frontBaseRight = _proj(totalX, 0, zFront, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final frontBaseLeft = _proj(0, 0, zFront, origin: origin, scaleX: scaleX, scaleY: scaleY);
    frontWallPath
      ..lineTo(frontBaseRight.dx, frontBaseRight.dy)
      ..lineTo(frontBaseLeft.dx, frontBaseLeft.dy)
      ..close();

    canvas.drawPath(
      frontWallPath,
      Paint()
        ..shader = LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: isDark
              ? [const Color(0xFF1E3228), const Color(0xFF101916)]
              : [const Color(0xFFD5EEDD), const Color(0xFFBBDCC7)],
        ).createShader(Rect.fromLTWH(0, 0, size.width, size.height)),
    );

    // Cara lateral izquierda (inicio en x=0, altura h)
    final leftCapPath = Path()
      ..moveTo(frontBaseLeft.dx, frontBaseLeft.dy)
      ..lineTo(frontTop.first.dx, frontTop.first.dy)
      ..lineTo(backTop.first.dx, backTop.first.dy)
      ..lineTo(
        _proj(0, 0, zBack, origin: origin, scaleX: scaleX, scaleY: scaleY).dx,
        _proj(0, 0, zBack, origin: origin, scaleX: scaleX, scaleY: scaleY).dy,
      )
      ..close();
    canvas.drawPath(
      leftCapPath,
      Paint()..color = isDark ? const Color(0xFF17261F) : const Color(0xFFC6E3D0),
    );

    // Superficie superior de la pista curva
    final topSurfacePath = Path()..moveTo(frontTop.first.dx, frontTop.first.dy);
    for (final pt in frontTop.skip(1)) {
      topSurfacePath.lineTo(pt.dx, pt.dy);
    }
    for (final pt in backTop.reversed) {
      topSurfacePath.lineTo(pt.dx, pt.dy);
    }
    topSurfacePath.close();

    canvas.drawPath(
      topSurfacePath,
      Paint()
        ..shader = LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: isDark
              ? [const Color(0xFF284738), const Color(0xFF1C2F27)]
              : [const Color(0xFFE5F6EC), const Color(0xFFCDE9D8)],
        ).createShader(Rect.fromLTWH(0, 0, size.width, size.height)),
    );

    // Contornos y costillas 3D de la pista
    final edgePaint = Paint()
      ..color = palette.green.o(0.65)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.6;
    final frontLine = Path()..moveTo(frontTop.first.dx, frontTop.first.dy);
    for (final pt in frontTop.skip(1)) {
      frontLine.lineTo(pt.dx, pt.dy);
    }
    final backLine = Path()..moveTo(backTop.first.dx, backTop.first.dy);
    for (final pt in backTop.skip(1)) {
      backLine.lineTo(pt.dx, pt.dy);
    }
    canvas.drawPath(backLine, Paint()..color = palette.green.o(0.32)..style = PaintingStyle.stroke..strokeWidth = 1.2);
    canvas.drawPath(frontLine, edgePaint);

    // Costillas transversales para acentuar el efecto 3D
    for (var i = 0; i <= samples; i += 7) {
      canvas.drawLine(
        frontTop[i],
        backTop[i],
        Paint()..color = palette.green.o(0.18)..strokeWidth = 1.0,
      );
    }

    // Indicador de altura inicial h = 3.6 m
    final hBottom = _proj(-0.22, 0, 0.55, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final hTop = _proj(-0.22, rampHeight, 0.55, origin: origin, scaleX: scaleX, scaleY: scaleY);
    _drawDashedLine(canvas, hBottom, hTop, palette.green.o(0.7));
    _drawCanvasLabel(
      canvas,
      'h = ${rampHeight.toStringAsFixed(1)} m',
      Offset(hTop.dx - 8, (hBottom.dy + hTop.dy) * 0.5 - 6),
      palette.green,
    );

    // 3. Sombra proyectada y Bloque 3D sobre la curva
    final bx = snapshot.x;
    final by = snapshot.y;
    final slope = ConservativeEnergyPhysics.rampSlope(bx, rampHeight, rampProfile);
    final angle = math.atan(slope); // rad respecto al eje horizontal

    const blockHalfW = 0.24;
    const blockH = 0.36;
    const zCenter = 0.58;
    const zHalf = 0.32;

    final shadowCenter = _proj(bx, by + 0.01, zCenter, origin: origin, scaleX: scaleX, scaleY: scaleY);
    canvas.drawOval(
      Rect.fromCenter(center: shadowCenter, width: 32, height: 10),
      Paint()..color = Colors.black.withAlpha(isDark ? 110 : 45),
    );

    _drawOrientedCube3D(
      canvas,
      wx: bx,
      wy: by,
      wzCenter: zCenter,
      halfWidth: blockHalfW,
      height: blockH,
      halfDepth: zHalf,
      slopeAngle: angle,
      origin: origin,
      scaleX: scaleX,
      scaleY: scaleY,
      topColor: const Color(0xFF4CD97B),
      frontColor: palette.green,
      sideColor: const Color(0xFF1E8F43),
      borderColor: isDark ? Colors.white.o(0.45) : Colors.black.o(0.25),
    );

    // 4. Vectores de Fuerza y Velocidad
    final blockCenter = _proj(
      bx - math.sin(angle) * (blockH * 0.5),
      by + math.cos(angle) * (blockH * 0.5),
      zCenter,
      origin: origin,
      scaleX: scaleX,
      scaleY: scaleY,
    );

    // Vector velocidad tangencial
    if (snapshot.speed > 0.05) {
      final vLen = (snapshot.speed / 9.0).clamp(0.15, 1.0) * 52.0;
      final dir = Offset(math.cos(angle), -math.sin(angle));
      _drawVectorArrow(
        canvas,
        blockCenter,
        blockCenter + dir * vLen,
        const Color(0xFF32ADE6),
        label: 'v⃗',
      );
    }

    // Vector Peso mg hacia abajo
    _drawVectorArrow(
      canvas,
      blockCenter,
      blockCenter + const Offset(0, 34),
      const Color(0xFFFF6961),
      label: 'mg',
    );
  }

  void _paintSpringFrictionScene(Canvas canvas, Size size) {
    final analyticalD = ConservativeEnergyPhysics.analyticalStoppingDistance(
      mass: springMass,
      springK: springK,
      compression: springCompression,
      muK: muK,
    );
    final maxTrackX = math.max(analyticalD + 0.35, 1.8);
    const minWorldX = -0.58;
    final worldSpan = maxTrackX - minWorldX;

    final scaleX = (size.width * 0.76) / worldSpan;
    final scaleY = size.height * 0.42;
    final origin = Offset(size.width * 0.10 - minWorldX * scaleX, size.height * 0.76);

    // 1. Piso 2.5D dividido en zona lisa (x < 0) y zona rugosa (x >= 0)
    _drawFloorSlab(
      canvas,
      origin: origin,
      minX: minWorldX,
      maxX: 0.0,
      zFront: -0.25,
      zBack: 1.15,
      scaleX: scaleX,
      scaleY: scaleY,
      customTopColors: isDark
          ? [const Color(0xFF152236), const Color(0xFF101928)]
          : [const Color(0xFFE3ECFA), const Color(0xFFD2E0F5)],
      accentBorder: palette.indigo.o(0.45),
    );

    _drawFloorSlab(
      canvas,
      origin: origin,
      minX: 0.0,
      maxX: maxTrackX,
      zFront: -0.25,
      zBack: 1.15,
      scaleX: scaleX,
      scaleY: scaleY,
      customTopColors: isDark
          ? [const Color(0xFF2B1C16), const Color(0xFF1E1410)]
          : [const Color(0xFFFAE8DC), const Color(0xFFF3D5C2)],
      accentBorder: palette.orange.o(0.55),
    );

    // Textura visual de aspereza (rugosidad mu_k) sobre x >= 0
    for (var rx = 0.06; rx < maxTrackX - 0.05; rx += 0.11) {
      final p1 = _proj(rx, 0.005, 0.02, origin: origin, scaleX: scaleX, scaleY: scaleY);
      final p2 = _proj(rx + 0.04, 0.005, 0.88, origin: origin, scaleX: scaleX, scaleY: scaleY);
      canvas.drawLine(
        p1,
        p2,
        Paint()..color = palette.orange.o(isDark ? 0.24 : 0.30)..strokeWidth = 1.1,
      );
    }

    // Línea divisoria x = 0 (fin de resorte / inicio zona rugosa)
    final zeroFront = _proj(0, 0.01, -0.25, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final zeroBack = _proj(0, 0.01, 1.15, origin: origin, scaleX: scaleX, scaleY: scaleY);
    canvas.drawLine(
      zeroFront,
      zeroBack,
      Paint()..color = palette.indigo..strokeWidth = 2.0,
    );
    _drawCanvasLabel(canvas, 'x = 0', zeroFront + const Offset(-14, 14), palette.indigo);

    // Marcador de distancia teórica d
    final stopFront = _proj(analyticalD, 0.01, -0.25, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final stopBack = _proj(analyticalD, 0.01, 1.15, origin: origin, scaleX: scaleX, scaleY: scaleY);
    _drawDashedLine(canvas, stopFront, stopBack, palette.orange.o(0.85));
    _drawCanvasLabel(
      canvas,
      'd = ${analyticalD.toStringAsFixed(3)} m',
      stopFront + const Offset(-26, 14),
      palette.orange,
    );

    // 2. Pared fija izquierda 3D donde ancla el resorte
    const wallX = minWorldX + 0.06;
    _drawOrientedCube3D(
      canvas,
      wx: wallX,
      wy: 0.0,
      wzCenter: 0.45,
      halfWidth: 0.06,
      height: 0.62,
      halfDepth: 0.42,
      slopeAngle: 0.0,
      origin: origin,
      scaleX: scaleX,
      scaleY: scaleY,
      topColor: isDark ? const Color(0xFF3A3D4A) : const Color(0xFFB5BAC7),
      frontColor: isDark ? const Color(0xFF282B36) : const Color(0xFF989EAE),
      sideColor: isDark ? const Color(0xFF1D1F28) : const Color(0xFF7C8292),
      borderColor: palette.strongBorder,
    );

    // 3. Resorte helicoidal 2.5D dinámico (se comprime hasta x < 0, descansa en x = 0 si bloque ya despegó)
    const blockHalfW = 0.11;
    const blockH = 0.34;
    const zCenter = 0.45;
    final springRightWorldX = (snapshot.x < 0.0 ? snapshot.x : 0.0) - blockHalfW;
    _drawHelicalSpring3D(
      canvas,
      startX: wallX + 0.06,
      endX: math.max(wallX + 0.14, springRightWorldX),
      centerY: blockH * 0.48,
      centerZ: zCenter,
      radius: 0.10,
      coils: 8,
      origin: origin,
      scaleX: scaleX,
      scaleY: scaleY,
      color: snapshot.x < 0.0 ? palette.indigo : palette.textSecondary,
    );

    // 4. Sombra y Bloque 3D
    final bx = snapshot.x;
    final shadowPos = _proj(bx, 0.01, zCenter, origin: origin, scaleX: scaleX, scaleY: scaleY);
    canvas.drawOval(
      Rect.fromCenter(center: shadowPos, width: 34, height: 11),
      Paint()..color = Colors.black.withAlpha(isDark ? 115 : 45),
    );

    _drawOrientedCube3D(
      canvas,
      wx: bx,
      wy: 0.0,
      wzCenter: zCenter,
      halfWidth: blockHalfW,
      height: blockH,
      halfDepth: 0.28,
      slopeAngle: 0.0,
      origin: origin,
      scaleX: scaleX,
      scaleY: scaleY,
      topColor: const Color(0xFFFFB340),
      frontColor: palette.orange,
      sideColor: const Color(0xFFC67200),
      borderColor: isDark ? Colors.white.o(0.45) : Colors.black.o(0.25),
    );

    // 5. Chispas térmicas de energía disipada por fricción
    for (final s in sparks) {
      final pt = _proj(s.wx, s.wy, zCenter + s.wz * 0.4, origin: origin, scaleX: scaleX, scaleY: scaleY);
      canvas.drawCircle(
        pt,
        2.2 * s.life + 0.6,
        Paint()..color = Color.lerp(const Color(0xFFFF453A), const Color(0xFFFFD60A), s.life)!.o(s.life),
      );
    }

    // 6. Vectores de velocidad y fuerza de fricción
    final blockMid = _proj(bx, blockH * 0.55, zCenter, origin: origin, scaleX: scaleX, scaleY: scaleY);
    if (snapshot.speed > 0.06) {
      final vLen = (snapshot.speed / 4.0).clamp(0.18, 1.0) * 48.0;
      _drawVectorArrow(
        canvas,
        blockMid,
        blockMid + Offset(vLen, 0),
        const Color(0xFF32ADE6),
        label: 'v⃗',
      );
    }
    if (snapshot.inRoughZone && !snapshot.isFinished) {
      _drawVectorArrow(
        canvas,
        _proj(bx, 0.06, zCenter, origin: origin, scaleX: scaleX, scaleY: scaleY),
        _proj(bx, 0.06, zCenter, origin: origin, scaleX: scaleX, scaleY: scaleY) +
            const Offset(-38, 0),
        const Color(0xFFFF453A),
        label: 'fₖ',
      );
    }
  }

  void _drawFloorSlab(
    Canvas canvas, {
    required Offset origin,
    required double minX,
    required double maxX,
    required double zFront,
    required double zBack,
    required double scaleX,
    required double scaleY,
    List<Color>? customTopColors,
    Color? accentBorder,
  }) {
    final fl = _proj(minX, 0, zFront, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final fr = _proj(maxX, 0, zFront, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final br = _proj(maxX, 0, zBack, origin: origin, scaleX: scaleX, scaleY: scaleY);
    final bl = _proj(minX, 0, zBack, origin: origin, scaleX: scaleX, scaleY: scaleY);

    const slabThick = 10.0;
    final topPath = Path()
      ..moveTo(fl.dx, fl.dy)
      ..lineTo(fr.dx, fr.dy)
      ..lineTo(br.dx, br.dy)
      ..lineTo(bl.dx, bl.dy)
      ..close();

    final topColors = customTopColors ??
        (isDark
            ? [const Color(0xFF171B26), const Color(0xFF11151E)]
            : [const Color(0xFFEAEEF6), const Color(0xFFDDE3EE)]);

    canvas.drawPath(
      topPath,
      Paint()
        ..shader = LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: topColors,
        ).createShader(Rect.fromPoints(fl, br)),
    );

    // Bisel frontal del piso 3D
    final bevelPath = Path()
      ..moveTo(fl.dx, fl.dy)
      ..lineTo(fr.dx, fr.dy)
      ..lineTo(fr.dx, fr.dy + slabThick)
      ..lineTo(fl.dx, fl.dy + slabThick)
      ..close();
    canvas.drawPath(
      bevelPath,
      Paint()..color = isDark ? const Color(0xFF0C0E15) : const Color(0xFFC5CDDC),
    );

    // Borde lateral derecho del piso
    final sideBevelPath = Path()
      ..moveTo(fr.dx, fr.dy)
      ..lineTo(br.dx, br.dy)
      ..lineTo(br.dx, br.dy + slabThick)
      ..lineTo(fr.dx, fr.dy + slabThick)
      ..close();
    canvas.drawPath(
      sideBevelPath,
      Paint()..color = isDark ? const Color(0xFF080A0F) : const Color(0xFFB3BCCF),
    );

    canvas.drawPath(
      topPath,
      Paint()
        ..color = accentBorder ?? palette.strongBorder
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.0,
    );
  }

  void _drawOrientedCube3D(
    Canvas canvas, {
    required double wx,
    required double wy,
    required double wzCenter,
    required double halfWidth,
    required double height,
    required double halfDepth,
    required double slopeAngle,
    required Offset origin,
    required double scaleX,
    required double scaleY,
    required Color topColor,
    required Color frontColor,
    required Color sideColor,
    required Color borderColor,
  }) {
    final cosA = math.cos(slopeAngle);
    final sinA = math.sin(slopeAngle);

    Offset pt(double localX, double localY, double localZ) {
      // Rotación local por pendiente de la rampa en el plano X-Y
      final rx = wx + localX * cosA - localY * sinA;
      final ry = wy + localX * sinA + localY * cosA;
      return _proj(rx, ry, wzCenter + localZ, origin: origin, scaleX: scaleX, scaleY: scaleY);
    }

    final fbl = pt(-halfWidth, 0, -halfDepth);
    final fbr = pt(halfWidth, 0, -halfDepth);
    final ftr = pt(halfWidth, height, -halfDepth);
    final ftl = pt(-halfWidth, height, -halfDepth);

    final bbr = pt(halfWidth, 0, halfDepth);
    final btr = pt(halfWidth, height, halfDepth);
    final btl = pt(-halfWidth, height, halfDepth);

    // Cara superior
    final topFace = Path()
      ..moveTo(ftl.dx, ftl.dy)
      ..lineTo(ftr.dx, ftr.dy)
      ..lineTo(btr.dx, btr.dy)
      ..lineTo(btl.dx, btl.dy)
      ..close();
    canvas.drawPath(topFace, Paint()..color = topColor);

    // Cara lateral derecha
    final rightFace = Path()
      ..moveTo(fbr.dx, fbr.dy)
      ..lineTo(bbr.dx, bbr.dy)
      ..lineTo(btr.dx, btr.dy)
      ..lineTo(ftr.dx, ftr.dy)
      ..close();
    canvas.drawPath(rightFace, Paint()..color = sideColor);

    // Cara frontal
    final frontFace = Path()
      ..moveTo(fbl.dx, fbl.dy)
      ..lineTo(fbr.dx, fbr.dy)
      ..lineTo(ftr.dx, ftr.dy)
      ..lineTo(ftl.dx, ftl.dy)
      ..close();
    canvas.drawPath(frontFace, Paint()..color = frontColor);

    final stroke = Paint()
      ..color = borderColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.1;
    canvas.drawPath(topFace, stroke);
    canvas.drawPath(rightFace, stroke);
    canvas.drawPath(frontFace, stroke);
  }

  void _drawHelicalSpring3D(
    Canvas canvas, {
    required double startX,
    required double endX,
    required double centerY,
    required double centerZ,
    required double radius,
    required int coils,
    required Offset origin,
    required double scaleX,
    required double scaleY,
    required Color color,
  }) {
    const steps = 96;
    final path = Path();
    for (var i = 0; i <= steps; i++) {
      final t = i / steps;
      final angle = t * coils * 2.0 * math.pi;
      final wx = startX + (endX - startX) * t;
      final wy = centerY + math.sin(angle) * radius;
      final wz = centerZ + math.cos(angle) * radius * 0.85;
      final pt = _proj(wx, wy, wz, origin: origin, scaleX: scaleX, scaleY: scaleY);
      if (i == 0) {
        path.moveTo(pt.dx, pt.dy);
      } else {
        path.lineTo(pt.dx, pt.dy);
      }
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = color
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.6
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round,
    );
  }

  void _drawVectorArrow(
    Canvas canvas,
    Offset start,
    Offset end,
    Color color, {
    String? label,
  }) {
    final delta = end - start;
    final dist = delta.distance;
    if (dist < 4.0) return;

    final paint = Paint()
      ..color = color
      ..strokeWidth = 2.2
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(start, end, paint);

    final angle = math.atan2(delta.dy, delta.dx);
    const headLen = 7.0;
    final p1 = Offset(
      end.dx - headLen * math.cos(angle - math.pi / 6),
      end.dy - headLen * math.sin(angle - math.pi / 6),
    );
    final p2 = Offset(
      end.dx - headLen * math.cos(angle + math.pi / 6),
      end.dy - headLen * math.sin(angle + math.pi / 6),
    );
    final head = Path()
      ..moveTo(end.dx, end.dy)
      ..lineTo(p1.dx, p1.dy)
      ..lineTo(p2.dx, p2.dy)
      ..close();
    canvas.drawPath(head, Paint()..color = color);

    if (label != null) {
      _drawCanvasLabel(
        canvas,
        label,
        end + Offset(delta.dx >= 0 ? 4 : -14, delta.dy >= 0 ? 2 : -13),
        color,
      );
    }
  }

  void _drawDashedLine(Canvas canvas, Offset a, Offset b, Color color) {
    final total = (b - a).distance;
    if (total <= 1) return;
    final dir = (b - a) / total;
    const dash = 4.0;
    const gap = 4.0;
    var pos = 0.0;
    final paint = Paint()
      ..color = color
      ..strokeWidth = 1.4;
    while (pos < total) {
      final next = math.min(pos + dash, total);
      canvas.drawLine(a + dir * pos, a + dir * next, paint);
      pos += dash + gap;
    }
  }

  void _drawCanvasLabel(Canvas canvas, String text, Offset pos, Color color) {
    final tp = TextPainter(
      text: TextSpan(
        text: text,
        style: mono(
          fontSize: 9.5,
          fontWeight: FontWeight.w700,
          color: color,
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant _Semi3DPhysicsPainter oldDelegate) {
    return oldDelegate.snapshot != snapshot ||
        oldDelegate.problem != problem ||
        oldDelegate.rampProfile != rampProfile ||
        oldDelegate.rampHeight != rampHeight ||
        oldDelegate.rampMass != rampMass ||
        oldDelegate.springMass != springMass ||
        oldDelegate.springK != springK ||
        oldDelegate.springCompression != springCompression ||
        oldDelegate.muK != muK ||
        oldDelegate.isDark != isDark ||
        oldDelegate.sparks.length != sparks.length;
  }
}
