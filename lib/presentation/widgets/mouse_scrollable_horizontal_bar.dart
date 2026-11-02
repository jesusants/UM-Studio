import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';
import 'ios_primitives.dart';

/// Contenedor horizontal adaptable para selectores de temas, cátedras y filtros.
///
/// Resuelve de forma definitiva:
/// 1. Desplazamiento horizontal con la rueda vertical del ratón (`PointerScrollEvent.dy`).
/// 2. Arrastre horizontal con clic sostenido de ratón (mouse drag).
/// 3. Botones de navegación previa y siguiente (`<` y `>`) cuando el contenido desborda la pantalla.
/// 4. Soporte total para gestos táctiles y trackpad / touchpad en todas las plataformas.
///
/// Puede usarse pasando un `child` con su `controller` externo, o usando el patrón `builder`
/// que genera y administra automáticamente el `ScrollController`.
class MouseScrollableHorizontalBar extends StatefulWidget {
  const MouseScrollableHorizontalBar({
    super.key,
    this.child,
    this.builder,
    this.controller,
    this.height = 32.0,
    this.scrollStep = 160.0,
    this.showArrows = true,
    this.arrowAccentColor,
  }) : assert(
          child != null || builder != null,
          'Debes proporcionar child o builder en MouseScrollableHorizontalBar',
        );

  final Widget? child;
  final Widget Function(BuildContext context, ScrollController controller)?
      builder;
  final ScrollController? controller;
  final double height;
  final double scrollStep;
  final bool showArrows;
  final Color? arrowAccentColor;

  @override
  State<MouseScrollableHorizontalBar> createState() =>
      _MouseScrollableHorizontalBarState();
}

class _MouseScrollableHorizontalBarState
    extends State<MouseScrollableHorizontalBar> {
  ScrollController? _internalController;
  ScrollController get _effectiveController =>
      widget.controller ?? _internalController!;

  bool _canScrollLeft = false;
  bool _canScrollRight = false;
  bool _hasOverflow = false;

  @override
  void initState() {
    super.initState();
    if (widget.controller == null) {
      _internalController = ScrollController();
    }
    _effectiveController.addListener(_updateScrollMetrics);
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) _updateScrollMetrics();
    });
  }

  @override
  void didUpdateWidget(covariant MouseScrollableHorizontalBar oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.controller != widget.controller) {
      oldWidget.controller?.removeListener(_updateScrollMetrics);
      _internalController?.removeListener(_updateScrollMetrics);

      if (widget.controller == null && _internalController == null) {
        _internalController = ScrollController();
      } else if (widget.controller != null && _internalController != null) {
        _internalController!.dispose();
        _internalController = null;
      }

      _effectiveController.addListener(_updateScrollMetrics);
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (mounted) _updateScrollMetrics();
      });
    }
  }

  @override
  void dispose() {
    _effectiveController.removeListener(_updateScrollMetrics);
    _internalController?.dispose();
    super.dispose();
  }

  void _updateScrollMetrics() {
    if (!_effectiveController.hasClients) return;
    final pos = _effectiveController.position;
    final maxExtent = pos.maxScrollExtent;
    final offset = pos.pixels;

    final hasOverflow = maxExtent > 2.0;
    final canLeft = hasOverflow && offset > 2.0;
    final canRight = hasOverflow && offset < (maxExtent - 2.0);

    if (hasOverflow != _hasOverflow ||
        canLeft != _canScrollLeft ||
        canRight != _canScrollRight) {
      setState(() {
        _hasOverflow = hasOverflow;
        _canScrollLeft = canLeft;
        _canScrollRight = canRight;
      });
    }
  }

  void _onPointerSignal(PointerSignalEvent event) {
    if (event is PointerScrollEvent) {
      // Si la rueda gira verticalmente (dy != 0) y dx es 0,
      // redirige el delta vertical hacia el desplazamiento horizontal.
      if (event.scrollDelta.dx == 0 && event.scrollDelta.dy != 0) {
        if (_effectiveController.hasClients) {
          final pos = _effectiveController.position;
          final target = (_effectiveController.offset + event.scrollDelta.dy)
              .clamp(pos.minScrollExtent, pos.maxScrollExtent);
          if (target != _effectiveController.offset) {
            _effectiveController.jumpTo(target);
          }
        }
      }
    }
  }

  void _scrollLeft() {
    if (!_effectiveController.hasClients) return;
    final target = (_effectiveController.offset - widget.scrollStep)
        .clamp(0.0, _effectiveController.position.maxScrollExtent);
    _effectiveController.animateTo(
      target,
      duration: const Duration(milliseconds: 220),
      curve: Curves.easeOutCubic,
    );
  }

  void _scrollRight() {
    if (!_effectiveController.hasClients) return;
    final target = (_effectiveController.offset + widget.scrollStep)
        .clamp(0.0, _effectiveController.position.maxScrollExtent);
    _effectiveController.animateTo(
      target,
      duration: const Duration(milliseconds: 220),
      curve: Curves.easeOutCubic,
    );
  }

  @override
  Widget build(BuildContext context) {
    final showArrows = widget.showArrows && _hasOverflow;
    final scrollChild = widget.builder != null
        ? widget.builder!(context, _effectiveController)
        : widget.child!;

    return SizedBox(
      height: widget.height,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          if (showArrows) ...[
            _ArrowButton(
              icon: Icons.chevron_left_rounded,
              enabled: _canScrollLeft,
              onTap: _canScrollLeft ? _scrollLeft : null,
              accentColor: widget.arrowAccentColor,
              tooltip: 'Desplazar a la izquierda',
            ),
            const SizedBox(width: 6),
          ],
          Expanded(
            child: Listener(
              onPointerSignal: _onPointerSignal,
              child: scrollChild,
            ),
          ),
          if (showArrows) ...[
            const SizedBox(width: 6),
            _ArrowButton(
              icon: Icons.chevron_right_rounded,
              enabled: _canScrollRight,
              onTap: _canScrollRight ? _scrollRight : null,
              accentColor: widget.arrowAccentColor,
              tooltip: 'Desplazar a la derecha',
            ),
          ],
        ],
      ),
    );
  }
}

class _ArrowButton extends StatelessWidget {
  const _ArrowButton({
    required this.icon,
    required this.enabled,
    required this.onTap,
    this.accentColor,
    this.tooltip,
  });

  final IconData icon;
  final bool enabled;
  final VoidCallback? onTap;
  final Color? accentColor;
  final String? tooltip;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final activeColor = accentColor ?? p.textPrimary;

    final button = TapScale(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        width: 26,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: enabled ? p.card : p.card.o(0.4),
          borderRadius: BorderRadius.circular(8),
          border: Border.all(
            color: enabled ? p.cardBorder : p.cardBorder.o(0.3),
            width: 1,
          ),
        ),
        child: Icon(
          icon,
          size: 16,
          color: enabled ? activeColor : p.textSecondary.o(0.3),
        ),
      ),
    );

    if (tooltip != null && enabled) {
      return Tooltip(
        message: tooltip!,
        waitDuration: const Duration(milliseconds: 500),
        child: button,
      );
    }

    return button;
  }
}
