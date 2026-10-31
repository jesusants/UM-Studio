import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/constants/app_constants.dart';
import '../../core/theme/app_theme.dart';
import '../providers/app_scopes.dart';

/// Comportamiento táctil iOS Minimalist:
/// Escalado elástico `scale(0.97)` de 140ms + `HapticFeedback.lightImpact()`.
class TapScale extends StatefulWidget {
  const TapScale({
    super.key,
    required this.child,
    this.onTap,
    this.enableHaptics = true,
  });

  final Widget child;
  final VoidCallback? onTap;
  final bool enableHaptics;

  @override
  State<TapScale> createState() => _TapScaleState();
}

class _TapScaleState extends State<TapScale> {
  bool _pressed = false;

  void _set(bool v) {
    if (_pressed != v) setState(() => _pressed = v);
  }

  void _handleTap() {
    if (widget.onTap == null) return;
    if (widget.enableHaptics) {
      HapticFeedback.lightImpact();
    }
    widget.onTap!();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      behavior: HitTestBehavior.opaque,
      onTapDown: widget.onTap != null ? (_) => _set(true) : null,
      onTapUp: widget.onTap != null ? (_) => _set(false) : null,
      onTapCancel: widget.onTap != null ? () => _set(false) : null,
      onTap: widget.onTap != null ? _handleTap : null,
      child: AnimatedScale(
        scale: _pressed ? 0.97 : 1.0,
        duration: AppConstants.tapScaleDuration,
        curve: kIosSpring,
        child: AnimatedOpacity(
          opacity: _pressed ? 0.92 : 1.0,
          duration: AppConstants.tapScaleDuration,
          child: widget.child,
        ),
      ),
    );
  }
}

/// Superficie modular iOS con fondo `#121316` (oscuro) o `#F2F2F7` (claro)
/// y borde limpio de 1px `#1F2228`.
class IosCard extends StatelessWidget {
  const IosCard({
    super.key,
    required this.child,
    this.padding = const EdgeInsets.all(16),
    this.borderColor,
    this.backgroundColor,
    this.gradient,
    this.radius = 20,
  });

  final Widget child;
  final EdgeInsetsGeometry padding;
  final Color? borderColor;
  final Color? backgroundColor;
  final Gradient? gradient;
  final double radius;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return Container(
      width: double.infinity,
      padding: padding,
      decoration: BoxDecoration(
        color: gradient == null ? (backgroundColor ?? p.card) : null,
        gradient: gradient,
        borderRadius: BorderRadius.circular(radius),
        border: Border.all(color: borderColor ?? p.cardBorder, width: 1),
      ),
      child: child,
    );
  }
}

/// Separador hairline de 1px estilo iOS (evita el `Divider` de Material).
class IosHairline extends StatelessWidget {
  const IosHairline({super.key, this.color});

  final Color? color;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 1,
      color: color ?? context.palette.cardBorder,
    );
  }
}

/// Punto de color circular.
class Dot extends StatelessWidget {
  const Dot({super.key, required this.color, this.size = 8});

  final Color color;
  final double size;

  @override
  Widget build(BuildContext context) => Container(
        width: size,
        height: size,
        decoration: BoxDecoration(color: color, shape: BoxShape.circle),
      );
}

/// Punto con animación de pulso suave a 60/120fps.
class PulseDot extends StatefulWidget {
  const PulseDot({super.key, required this.color, this.size = 8});

  final Color color;
  final double size;

  @override
  State<PulseDot> createState() => _PulseDotState();
}

class _PulseDotState extends State<PulseDot>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c = AnimationController(
    vsync: this,
    duration: const Duration(milliseconds: 1100),
  )..repeat(reverse: true);

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return RepaintBoundary(
      child: FadeTransition(
        opacity: Tween<double>(begin: 1.0, end: 0.35)
            .animate(CurvedAnimation(parent: _c, curve: Curves.easeInOut)),
        child: Dot(color: widget.color, size: widget.size),
      ),
    );
  }
}

/// Barra de progreso redondeada con transición elástica.
class ProgressBar extends StatelessWidget {
  const ProgressBar({
    super.key,
    required this.value,
    required this.color,
    this.height = 6,
  });

  final double value;
  final Color color;
  final double height;

  @override
  Widget build(BuildContext context) {
    final radius = BorderRadius.circular(999);
    return Container(
      height: height,
      width: double.infinity,
      decoration: BoxDecoration(
        color: context.palette.elevated,
        borderRadius: radius,
      ),
      alignment: Alignment.centerLeft,
      child: AnimatedFractionallySizedBox(
        widthFactor: value.clamp(0.0, 1.0),
        duration: const Duration(milliseconds: 500),
        curve: kPillEase,
        child: AnimatedContainer(
          height: height,
          duration: const Duration(milliseconds: 300),
          decoration: BoxDecoration(color: color, borderRadius: radius),
        ),
      ),
    );
  }
}

/// Motor de Shimmer nativo a 60/120fps en tonos `#1A1D24` (modo oscuro)
/// para esqueletos de carga sin ruedas giratorias.
class IosShimmer extends StatefulWidget {
  const IosShimmer({super.key, required this.child});

  final Widget child;

  @override
  State<IosShimmer> createState() => _IosShimmerState();
}

class _IosShimmerState extends State<IosShimmer>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller = AnimationController(
    vsync: this,
    duration: const Duration(milliseconds: 1350),
  )..repeat();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return RepaintBoundary(
      child: AnimatedBuilder(
        animation: _controller,
        child: widget.child,
        builder: (context, child) {
          final slide = _controller.value * 2.4 - 1.2;
          return ShaderMask(
            blendMode: BlendMode.srcATop,
            shaderCallback: (bounds) {
              return LinearGradient(
                begin: Alignment(slide - 1.0, -0.2),
                end: Alignment(slide + 1.0, 0.2),
                colors: [
                  p.shimmerBase,
                  p.shimmerHighlight,
                  p.shimmerBase,
                ],
                stops: const [0.15, 0.5, 0.85],
              ).createShader(bounds);
            },
            child: child,
          );
        },
      ),
    );
  }
}

/// Silueta primitiva para esqueletos de carga Shimmer.
class ShimmerBlock extends StatelessWidget {
  const ShimmerBlock({
    super.key,
    required this.height,
    this.width = double.infinity,
    this.radius = 8,
  });

  final double height;
  final double width;
  final double radius;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: width,
      height: height,
      decoration: BoxDecoration(
        color: context.palette.shimmerBase,
        borderRadius: BorderRadius.circular(radius),
      ),
    );
  }
}

/// Emblema circular oficial de Ingeniería Energética — Unimagdalena.
class ProgramLogoBadge extends StatelessWidget {
  const ProgramLogoBadge({
    super.key,
    this.size = 36,
  });

  final double size;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        boxShadow: [
          BoxShadow(
            color: Colors.black.o(0.28),
            blurRadius: 6,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: ClipOval(
        child: Image.asset(
          AppConstants.programLogoAsset,
          width: size,
          height: size,
          fit: BoxFit.cover,
          filterQuality: FilterQuality.high,
          errorBuilder: (_, __, ___) => Container(
            color: p.elevated,
            alignment: Alignment.center,
            child: Icon(Icons.bolt_rounded, size: size * 0.5, color: p.green),
          ),
        ),
      ),
    );
  }
}

/// Botón circular iOS para intercambiar entre tema oscuro OLED y tema claro.
class ThemeToggleButton extends StatelessWidget {
  const ThemeToggleButton({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = ThemeScope.of(context);
    final p = context.palette;
    final isDark = controller.isDark;

    return Tooltip(
      message: isDark ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro',
      child: TapScale(
        onTap: controller.toggle,
        child: Container(
          width: 32,
          height: 32,
          decoration: BoxDecoration(
            color: p.elevated,
            shape: BoxShape.circle,
            border: Border.all(color: p.strongBorder),
          ),
          child: AnimatedSwitcher(
            duration: const Duration(milliseconds: 320),
            switchInCurve: kIosSpring,
            switchOutCurve: kIosSpring,
            transitionBuilder: (child, anim) => RotationTransition(
              turns: Tween<double>(begin: 0.5, end: 1).animate(anim),
              child: ScaleTransition(scale: anim, child: child),
            ),
            child: Icon(
              isDark ? Icons.light_mode_rounded : Icons.dark_mode_rounded,
              key: ValueKey(isDark),
              size: 16,
              color: isDark ? p.orange : p.indigo,
            ),
          ),
        ),
      ),
    );
  }
}

/// Muestra un aviso flotante minimalista estilo cápsula iOS.
void showIosToast(BuildContext context, String message, {Color? accentColor}) {
  final p = context.palette;
  final messenger = ScaffoldMessenger.maybeOf(context);
  if (messenger == null) return;
  messenger
    ..hideCurrentSnackBar()
    ..showSnackBar(
      SnackBar(
        elevation: 0,
        backgroundColor: Colors.transparent,
        behavior: SnackBarBehavior.floating,
        duration: const Duration(seconds: 2),
        content: Center(
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              color: p.card,
              borderRadius: BorderRadius.circular(999),
              border: Border.all(color: accentColor ?? p.cardBorder),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Dot(color: accentColor ?? p.green, size: 7),
                const SizedBox(width: 8),
                Flexible(
                  child: Text(
                    message,
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w500,
                      color: p.textPrimary,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
}
