import 'dart:async';
import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';
import '../desktop_theme_tokens.dart';

/// Módulo de Tiempo en Vivo para Desktop con aislamiento de repintado (`RepaintBoundary`)
/// para garantizar 0% de sobrecarga de CPU en el resto del árbol de widgets.
///
/// Renderiza:
/// 1. Reloj digital gigante (72px - 84px) con números monoespaciados (`tabularFigures`).
/// 2. Micro-animación en los dos puntos (`:`) que pulsan suavemente de 1.0 a 0.28 en 500ms.
/// 3. Día y fecha completa en español con tokens duales Dark/Light.
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
    final tokens = DesktopThemeTokens.of(context);
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
                _TimeDigit(text: hh, color: tokens.textPrimary),
                _AnimatedColon(opacity: _colonOpacity, color: tokens.textPrimary),
                _TimeDigit(text: mm, color: tokens.textPrimary),
                _AnimatedColon(opacity: _colonOpacity, color: tokens.textPrimary),
                _TimeDigit(text: ss, color: tokens.textPrimary),
              ],
            ),
          ),
          const SizedBox(height: 8),

          // Día y Fecha Completa
          Text(
            _fullSpanishDate(_now),
            style: TextStyle(
              fontSize: 16.5,
              fontWeight: FontWeight.w600,
              letterSpacing: -0.2,
              color: tokens.textSecondary,
            ),
          ),
        ],
      ),
    );
  }
}

class _TimeDigit extends StatelessWidget {
  const _TimeDigit({
    required this.text,
    required this.color,
  });

  final String text;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: mono(
        fontSize: 74,
        fontWeight: FontWeight.w800,
        color: color,
        letterSpacing: -2.0,
      ),
    );
  }
}

class _AnimatedColon extends StatelessWidget {
  const _AnimatedColon({
    required this.opacity,
    required this.color,
  });

  final Animation<double> opacity;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: opacity,
      builder: (context, _) {
        return Opacity(
          opacity: opacity.value,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4),
            child: Text(
              ':',
              style: mono(
                fontSize: 66,
                fontWeight: FontWeight.w700,
                color: color,
              ),
            ),
          ),
        );
      },
    );
  }
}
