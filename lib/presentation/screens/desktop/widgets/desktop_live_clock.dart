import 'dart:async';
import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';

/// Módulo de Tiempo en Vivo para Desktop con aislamiento de repintado (`RepaintBoundary`)
/// para garantizar 0% de sobrecarga de CPU en el resto del árbol de widgets.
///
/// Renderiza:
/// 1. Reloj digital gigante (72px - 84px) con números monoespaciados (`tabularFigures`).
/// 2. Micro-animación en los dos puntos (`:`) que pulsan suavemente de 1.0 a 0.3 en 500ms.
/// 3. Día y fecha completa en español en `#8E8E93` (ej. "Sábado, 31 de Octubre de 2026").
class DesktopLiveClock extends StatefulWidget {
  const DesktopLiveClock({super.key});

  @override
  State<DesktopLiveClock> createState() => _DesktopLiveClockState();
}

class _DesktopLiveClockState extends State<DesktopLiveClock>
    with SingleTickerProviderStateMixin {
  late DateTime _now;
  late final Timer _timer;
  late final AnimationController _pulseController;
  late final Animation<double> _colonOpacity;

  static const List<String> _diasSemana = [
    'Lunes',
    'Martes',
    'Miércoles',
    'Jueves',
    'Viernes',
    'Sábado',
    'Domingo',
  ];

  static const List<String> _meses = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre',
  ];

  @override
  void initState() {
    super.initState();
    _now = DateTime.now();

    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 500),
    )..repeat(reverse: true);

    _colonOpacity = Tween<double>(begin: 1.0, end: 0.28).animate(
      CurvedAnimation(
        parent: _pulseController,
        curve: Curves.easeInOut,
      ),
    );

    _timer = Timer.periodic(const Duration(seconds: 1), (_) {
      if (mounted) {
        setState(() => _now = DateTime.now());
      }
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    _pulseController.dispose();
    super.dispose();
  }

  String _formatTwoDigits(int n) => n.toString().padLeft(2, '0');

  String _fullSpanishDate(DateTime d) {
    final diaNombre = _diasSemana[d.weekday - 1];
    final mesNombre = _meses[d.month - 1];
    return '$diaNombre, ${d.day} de $mesNombre de ${d.year}';
  }

  @override
  Widget build(BuildContext context) {
    final hh = _formatTwoDigits(_now.hour);
    final mm = _formatTwoDigits(_now.minute);
    final ss = _formatTwoDigits(_now.second);

    return RepaintBoundary(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          // Hora Digital Gigante con Tabular Figures
          FittedBox(
            fit: BoxFit.scaleDown,
            child: Row(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.baseline,
              textBaseline: TextBaseline.alphabetic,
              children: [
                _TimeDigit(text: hh),
                _AnimatedColon(opacity: _colonOpacity),
                _TimeDigit(text: mm),
                _AnimatedColon(opacity: _colonOpacity),
                _TimeDigit(text: ss),
              ],
            ),
          ),
          const SizedBox(height: 10),

          // Día y Fecha Completa
          Text(
            _fullSpanishDate(_now),
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w600,
              letterSpacing: -0.3,
              color: Color(0xFF8E8E93),
            ),
          ),
        ],
      ),
    );
  }
}

class _TimeDigit extends StatelessWidget {
  const _TimeDigit({required this.text});

  final String text;

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: mono(
        fontSize: 78,
        fontWeight: FontWeight.w800,
        color: Colors.white,
        letterSpacing: -2.0,
      ),
    );
  }
}

class _AnimatedColon extends StatelessWidget {
  const _AnimatedColon({required this.opacity});

  final Animation<double> opacity;

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: opacity,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 4),
        child: Text(
          ':',
          style: mono(
            fontSize: 72,
            fontWeight: FontWeight.w700,
            color: const Color(0xFF30D158),
          ),
        ),
      ),
    );
  }
}
