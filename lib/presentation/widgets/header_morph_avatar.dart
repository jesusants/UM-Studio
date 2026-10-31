import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import '../../core/constants/app_constants.dart';
import '../../core/theme/app_theme.dart';

/// Avatar dinámico interactivo ubicado en la esquina superior izquierda.
///
/// Alterna automáticamente cada 5 segundos entre:
/// - Estado A (`career_logo`): Emblema oficial circular de Ingeniería Energética.
/// - Estado B (`user_photo`): Foto de perfil de Microsoft Entra ID desde Graph API.
///
/// Si no hay sesión iniciada o el usuario no tiene foto (`photoBytes == null`),
/// se mantiene fijo en el Estado A sin activar ningún temporizador.
/// El toque manual invierte el estado al instante y reinicia el ciclo de 5 segundos
/// garantizando inmunidad a colisiones o desincronizaciones de animación (Anti-tilde).
class HeaderMorphAvatar extends StatefulWidget {
  const HeaderMorphAvatar({
    super.key,
    this.size = 36,
    this.photoBytes,
    this.onTap,
  });

  final double size;
  final Uint8List? photoBytes;
  final VoidCallback? onTap;

  @override
  State<HeaderMorphAvatar> createState() => _HeaderMorphAvatarState();
}

class _HeaderMorphAvatarState extends State<HeaderMorphAvatar> {
  Timer? _timer;
  bool _showUserPhoto = false;

  bool get _hasPhoto =>
      widget.photoBytes != null && widget.photoBytes!.isNotEmpty;

  @override
  void initState() {
    super.initState();
    _syncTimer();
  }

  @override
  void didUpdateWidget(covariant HeaderMorphAvatar oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.photoBytes != widget.photoBytes) {
      if (!_hasPhoto) {
        _timer?.cancel();
        _timer = null;
        if (_showUserPhoto) {
          setState(() => _showUserPhoto = false);
        }
      } else {
        _syncTimer();
      }
    }
  }

  void _syncTimer() {
    _timer?.cancel();
    _timer = null;
    if (_hasPhoto) {
      _startTimer();
    }
  }

  void _startTimer() {
    _timer?.cancel();
    _timer = Timer.periodic(const Duration(seconds: 5), (timer) {
      if (!mounted) {
        timer.cancel();
        return;
      }
      if (!_hasPhoto) {
        timer.cancel();
        return;
      }
      setState(() {
        _showUserPhoto = !_showUserPhoto;
      });
    });
  }

  void _handleManualTap() {
    if (!mounted) return;
    if (!_hasPhoto) {
      widget.onTap?.call();
      return;
    }

    // 1. Cancelar de inmediato el temporizador activo
    _timer?.cancel();
    _timer = null;

    // 2. Invertir el estado visual al instante
    setState(() {
      _showUserPhoto = !_showUserPhoto;
    });

    // 3. Reiniciar desde cero un nuevo temporizador de 5 segundos
    _startTimer();

    // Notificar callback si fue provisto
    widget.onTap?.call();
  }

  @override
  void dispose() {
    _timer?.cancel();
    _timer = null;
    super.dispose();
  }

  Widget _buildCareerLogo(AppPalette p) {
    return Container(
      key: const ValueKey('career_logo'),
      width: widget.size,
      height: widget.size,
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
          width: widget.size,
          height: widget.size,
          fit: BoxFit.cover,
          filterQuality: FilterQuality.high,
          errorBuilder: (_, __, ___) => Container(
            color: p.elevated,
            alignment: Alignment.center,
            child: Icon(
              Icons.bolt_rounded,
              size: widget.size * 0.5,
              color: p.green,
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildUserPhoto(AppPalette p) {
    return Container(
      key: const ValueKey('user_photo'),
      width: widget.size,
      height: widget.size,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        border: Border.all(color: p.green, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: p.green.o(0.35),
            blurRadius: 8,
            offset: const Offset(0, 1),
          ),
        ],
      ),
      child: ClipOval(
        child: Image.memory(
          widget.photoBytes!,
          width: widget.size,
          height: widget.size,
          fit: BoxFit.cover,
          gaplessPlayback: true,
          errorBuilder: (_, __, ___) => _buildCareerLogo(p),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = Theme.of(context).extension<AppPalette>() ??
        (Theme.of(context).brightness == Brightness.dark
            ? AppPalette.dark
            : AppPalette.light);

    final childWidget = (_hasPhoto && _showUserPhoto)
        ? _buildUserPhoto(p)
        : _buildCareerLogo(p);

    return MouseRegion(
      cursor: SystemMouseCursors.click,
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: _handleManualTap,
        child: SizedBox(
          width: widget.size,
          height: widget.size,
          child: AnimatedSwitcher(
            duration: const Duration(milliseconds: 450),
            switchInCurve: Curves.easeOutBack,
            switchOutCurve: Curves.easeInCubic,
            transitionBuilder: (child, animation) {
              return FadeTransition(
                opacity: animation,
                child: ScaleTransition(
                  scale: Tween<double>(begin: 0.88, end: 1.0).animate(animation),
                  child: child,
                ),
              );
            },
            child: childWidget,
          ),
        ),
      ),
    );
  }
}
