import 'dart:async';
import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../desktop_theme_tokens.dart';

/// Modo del temporizador Pomodoro
enum FocusTimerMode {
  focus('Enfoque', 25 * 60, Color(0xFF5E5CE6)),
  shortBreak('Pausa corta', 5 * 60, Color(0xFF30D158)),
  longBreak('Pausa larga', 15 * 60, Color(0xFF0A84FF));

  const FocusTimerMode(this.label, this.seconds, this.accentColor);
  final String label;
  final int seconds;
  final Color accentColor;
}

/// Temporizador circular de enfoque ultraliviano para estudiar temas de la base de datos `.md`
/// directamente en el Dashboard de Escritorio con soporte dual Dark OLED y Light Mode.
class DesktopFocusTimer extends StatefulWidget {
  const DesktopFocusTimer({
    super.key,
    required this.activeSubjects,
    this.onOpenClaseViva,
    this.onHideTimer,
  });

  final List<AsignaturaModel> activeSubjects;
  final ValueChanged<String>? onOpenClaseViva;
  final VoidCallback? onHideTimer;

  @override
  DesktopFocusTimerState createState() => DesktopFocusTimerState();
}

class DesktopFocusTimerState extends State<DesktopFocusTimer> {
  FocusTimerMode _mode = FocusTimerMode.focus;
  late int _remainingSeconds;
  Timer? _ticker;
  bool _isRunning = false;
  String? _selectedSubjectCode;

  bool get isRunning => _isRunning;

  @override
  void initState() {
    super.initState();
    _remainingSeconds = _mode.seconds;
    if (widget.activeSubjects.isNotEmpty) {
      _selectedSubjectCode = widget.activeSubjects.first.codigo;
    }
  }

  @override
  void didUpdateWidget(covariant DesktopFocusTimer oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (_selectedSubjectCode == null && widget.activeSubjects.isNotEmpty) {
      _selectedSubjectCode = widget.activeSubjects.first.codigo;
    }
  }

  @override
  void dispose() {
    _ticker?.cancel();
    super.dispose();
  }

  void switchMode(FocusTimerMode newMode) {
    if (_mode == newMode) return;
    HapticFeedback.selectionClick();
    _ticker?.cancel();
    setState(() {
      _mode = newMode;
      _remainingSeconds = newMode.seconds;
      _isRunning = false;
    });
  }

  void togglePlayPause() {
    HapticFeedback.mediumImpact();
    if (_isRunning) {
      _ticker?.cancel();
      setState(() => _isRunning = false);
    } else {
      setState(() => _isRunning = true);
      _ticker = Timer.periodic(const Duration(seconds: 1), (t) {
        if (!mounted) {
          t.cancel();
          return;
        }
        if (_remainingSeconds > 0) {
          setState(() => _remainingSeconds--);
        } else {
          t.cancel();
          _handleTimerCompleted();
        }
      });
    }
  }

  void resetTimer() {
    HapticFeedback.lightImpact();
    _ticker?.cancel();
    setState(() {
      _remainingSeconds = _mode.seconds;
      _isRunning = false;
    });
  }

  Future<void> _handleTimerCompleted() async {
    setState(() {
      _isRunning = false;
      _remainingSeconds = _mode.seconds;
    });
    HapticFeedback.heavyImpact();

    final session = SessionScope.maybeOf(context);
    final subjectCode = _selectedSubjectCode;

    if (session != null && subjectCode != null && _mode == FocusTimerMode.focus) {
      await session.completeStudyBlock(codigoMateria: subjectCode);
      if (mounted) {
        showIosToast(
          context,
          '¡Bloque de estudio completado! +10% de avance registrado',
          accentColor: const Color(0xFF30D158),
        );
      }
    } else if (mounted) {
      showIosToast(
        context,
        'Tiempo de descanso finalizado. ¡Listo para volver a enfocar!',
        accentColor: const Color(0xFF5E5CE6),
      );
    }
  }

  String _formatTime(int totalSecs) {
    final m = (totalSecs ~/ 60).toString().padLeft(2, '0');
    final s = (totalSecs % 60).toString().padLeft(2, '0');
    return '$m:$s';
  }

  double get _progressRatio {
    final total = _mode.seconds;
    if (total == 0) return 0.0;
    return 1.0 - (_remainingSeconds / total);
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    final activeSubject = widget.activeSubjects.firstWhere(
      (s) => s.codigo == _selectedSubjectCode,
      orElse: () => widget.activeSubjects.isNotEmpty
          ? widget.activeSubjects.first
          : const AsignaturaModel(
              codigo: '02021810',
              nombre: 'Circuitos Eléctricos y Redes',
              cuatrimestre: 2,
              creditos: 3,
              obligatoria: true,
              categoria: 'PROFESIONAL',
              colorHex: '#30D158',
              temas: [],
            ),
    );

    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: tokens.surface,
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: tokens.border, width: 1),
        boxShadow: [
          BoxShadow(
            color: tokens.shadowColor,
            blurRadius: 18,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          // Encabezado con selector de modo
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(7),
                decoration: BoxDecoration(
                  color: _mode.accentColor.o(0.14),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(
                  Icons.timer_outlined,
                  size: 16,
                  color: _mode.accentColor,
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  'BLOQUE DE ENFOQUE',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 10.5,
                    fontWeight: FontWeight.w600,
                    letterSpacing: 0.8,
                    color: tokens.textSecondary,
                  ),
                ),
              ),
              const SizedBox(width: 8),
              // Píldoras de selección de modo
              Container(
                padding: const EdgeInsets.all(3),
                decoration: BoxDecoration(
                  color: tokens.surfaceElevated,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: tokens.borderSubtle),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: FocusTimerMode.values.map((mode) {
                    final isSel = mode == _mode;
                    return MouseRegion(
                      cursor: SystemMouseCursors.click,
                      child: GestureDetector(
                        onTap: () => switchMode(mode),
                        child: AnimatedContainer(
                          duration: const Duration(milliseconds: 180),
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 4,
                          ),
                          decoration: BoxDecoration(
                            color: isSel ? mode.accentColor : Colors.transparent,
                            borderRadius: BorderRadius.circular(7),
                          ),
                          child: Text(
                            mode.label,
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: isSel ? FontWeight.w700 : FontWeight.w500,
                              color: isSel ? Colors.white : tokens.textSecondary,
                            ),
                          ),
                        ),
                      ),
                    );
                  }).toList(),
                ),
              ),
              if (widget.onHideTimer != null) ...[
                const SizedBox(width: 8),
                TapScale(
                  onTap: widget.onHideTimer,
                  child: Tooltip(
                    message: 'Ocultar temporizador (P)',
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 5),
                      decoration: BoxDecoration(
                        color: tokens.surfaceElevated,
                        borderRadius: BorderRadius.circular(9),
                        border: Border.all(color: tokens.borderSubtle),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.visibility_off_outlined,
                            size: 14,
                            color: tokens.textSecondary,
                          ),
                          const SizedBox(width: 4),
                          Text(
                            'Ocultar',
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w600,
                              color: tokens.textSecondary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ],
          ),
          const SizedBox(height: 16),

          // Selector de materia asociada al bloque
          if (widget.activeSubjects.isNotEmpty) ...[
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
              decoration: BoxDecoration(
                color: tokens.surfaceElevated,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: tokens.borderSubtle),
              ),
              child: Row(
                children: [
                  Text(
                    'Materia:',
                    style: mono(fontSize: 11, color: tokens.textTertiary),
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: DropdownButtonHideUnderline(
                      child: DropdownButton<String>(
                        value: _selectedSubjectCode,
                        isDense: true,
                        isExpanded: true,
                        dropdownColor: tokens.isDark
                            ? const Color(0xFF14161C)
                            : Colors.white,
                        borderRadius: BorderRadius.circular(12),
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                          color: tokens.textPrimary,
                        ),
                        icon: Icon(
                          Icons.keyboard_arrow_down_rounded,
                          size: 16,
                          color: tokens.textSecondary,
                        ),
                        items: widget.activeSubjects.map((s) {
                          return DropdownMenuItem<String>(
                            value: s.codigo,
                            child: Text(
                              '${s.codigo} • ${s.nombre}',
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          );
                        }).toList(),
                        onChanged: (val) {
                          if (val != null) {
                            setState(() => _selectedSubjectCode = val);
                          }
                        },
                      ),
                    ),
                  ),
                  const SizedBox(width: 6),
                  if (widget.onOpenClaseViva != null)
                    MouseRegion(
                      cursor: SystemMouseCursors.click,
                      child: GestureDetector(
                        onTap: () => widget.onOpenClaseViva!(activeSubject.codigo),
                        child: Tooltip(
                          message: 'Abrir en La Clase Viva',
                          child: Container(
                            padding: const EdgeInsets.all(4),
                            decoration: BoxDecoration(
                              color: tokens.accentIndigo.o(0.15),
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Icon(
                              Icons.arrow_outward_rounded,
                              size: 13,
                              color: tokens.accentIndigo,
                            ),
                          ),
                        ),
                      ),
                    ),
                ],
              ),
            ),
            const SizedBox(height: 16),
          ],

          // Timer Circular Central
          Wrap(
            alignment: WrapAlignment.center,
            crossAxisAlignment: WrapCrossAlignment.center,
            spacing: 24,
            runSpacing: 14,
            children: [
              SizedBox(
                width: 135,
                height: 135,
                child: Stack(
                  alignment: Alignment.center,
                  children: [
                    CustomPaint(
                      size: const Size(135, 135),
                      painter: _CircularProgressPainter(
                        progress: _progressRatio,
                        accentColor: _mode.accentColor,
                        trackColor: tokens.border,
                      ),
                    ),
                    Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
                          _formatTime(_remainingSeconds),
                          style: mono(
                            fontSize: 32,
                            fontWeight: FontWeight.w800,
                            letterSpacing: -1.0,
                            color: tokens.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          _isRunning ? 'ACTIVO' : 'PAUSADO',
                          style: mono(
                            fontSize: 10,
                            fontWeight: FontWeight.w700,
                            letterSpacing: 1.0,
                            color: _isRunning
                                ? _mode.accentColor
                                : tokens.textTertiary,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 20),

              // Controles de Acción Lateral
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  MouseRegion(
                    cursor: SystemMouseCursors.click,
                    child: TapScale(
                      onTap: togglePlayPause,
                      child: Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 20,
                          vertical: 12,
                        ),
                        decoration: BoxDecoration(
                          color: _isRunning
                              ? tokens.surfaceElevated
                              : _mode.accentColor,
                          borderRadius: BorderRadius.circular(14),
                          border: _isRunning
                              ? Border.all(color: tokens.border)
                              : null,
                          boxShadow: _isRunning
                              ? null
                              : [
                                  BoxShadow(
                                    color: _mode.accentColor.o(0.35),
                                    blurRadius: 14,
                                    offset: const Offset(0, 4),
                                  ),
                                ],
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              _isRunning
                                  ? Icons.pause_rounded
                                  : Icons.play_arrow_rounded,
                              size: 19,
                              color: _isRunning
                                  ? tokens.textPrimary
                                  : Colors.white,
                            ),
                            const SizedBox(width: 8),
                            Text(
                              _isRunning ? 'Pausar' : 'Comenzar',
                              style: TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w700,
                                color: _isRunning
                                    ? tokens.textPrimary
                                    : Colors.white,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 10),
                  Row(
                    children: [
                      MouseRegion(
                        cursor: SystemMouseCursors.click,
                        child: TapScale(
                          onTap: resetTimer,
                          child: Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 14,
                              vertical: 10,
                            ),
                            decoration: BoxDecoration(
                              color: tokens.surfaceElevated,
                              borderRadius: BorderRadius.circular(12),
                              border: Border.all(color: tokens.border),
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Icon(
                                  Icons.refresh_rounded,
                                  size: 15,
                                  color: tokens.textSecondary,
                                ),
                                const SizedBox(width: 6),
                                Text(
                                  'Reiniciar',
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w600,
                                    color: tokens.textSecondary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _CircularProgressPainter extends CustomPainter {
  const _CircularProgressPainter({
    required this.progress,
    required this.accentColor,
    required this.trackColor,
  });

  final double progress;
  final Color accentColor;
  final Color trackColor;

  @override
  void paint(Canvas canvas, Size size) {
    const strokeWidth = 9.0;
    final center = Offset(size.width / 2, size.height / 2);
    final radius = (size.width - strokeWidth) / 2;

    // Track de fondo
    final trackPaint = Paint()
      ..color = trackColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = strokeWidth
      ..strokeCap = StrokeCap.round;

    canvas.drawCircle(center, radius, trackPaint);

    if (progress <= 0.0) return;

    // Anillo de progreso con gradiente
    final progressPaint = Paint()
      ..shader = SweepGradient(
        colors: [accentColor.o(0.65), accentColor],
        startAngle: 0.0,
        endAngle: math.pi * 2,
      ).createShader(Rect.fromCircle(center: center, radius: radius))
      ..style = PaintingStyle.stroke
      ..strokeWidth = strokeWidth
      ..strokeCap = StrokeCap.round;

    final sweepAngle = math.pi * 2 * progress.clamp(0.0, 1.0);

    canvas.save();
    canvas.translate(center.dx, center.dy);
    canvas.rotate(-math.pi / 2); // Empezar arriba a las 12 en punto
    canvas.translate(-center.dx, -center.dy);
    canvas.drawArc(
      Rect.fromCircle(center: center, radius: radius),
      0,
      sweepAngle,
      false,
      progressPaint,
    );
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant _CircularProgressPainter oldDelegate) {
    return oldDelegate.progress != progress ||
        oldDelegate.accentColor != accentColor ||
        oldDelegate.trackColor != trackColor;
  }
}
