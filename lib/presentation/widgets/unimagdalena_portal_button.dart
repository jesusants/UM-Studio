import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/theme/app_theme.dart';

/// Botón interactivo y minimalista estilo cápsula que muestra el escudo oficial
/// de la Universidad del Magdalena en estado de reposo y, al pasar el cursor
/// por encima (`onHover`), expande suavemente su ancho revelando el título
/// "Portal Estudiantes" con el indicador externo `↗` para abrir AyRe/Admisiones.
class UnimagdalenaPortalButton extends StatefulWidget {
  const UnimagdalenaPortalButton({
    super.key,
    this.expandOnHover = true,
    this.portalUrl =
        'https://admisiones.unimagdalena.edu.co/mEstudiantes/indexPrinc.jsp?rnd=315581080',
    this.onTap,
  });

  /// Determina si el botón expande su ancho al recibir hover.
  final bool expandOnHover;

  /// URL oficial de destino (Módulo de Estudiantes / AyRe).
  final String portalUrl;

  /// Callback opcional que reemplaza la llamada a `launchUrl` (útil para pruebas unitarias).
  final VoidCallback? onTap;

  @override
  State<UnimagdalenaPortalButton> createState() =>
      _UnimagdalenaPortalButtonState();
}

class _UnimagdalenaPortalButtonState extends State<UnimagdalenaPortalButton> {
  bool _isHovered = false;

  Future<void> _abrirPortal() async {
    if (widget.onTap != null) {
      widget.onTap!();
      return;
    }
    final uri = Uri.parse(widget.portalUrl);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final canExpand = widget.expandOnHover;
    final isExpanded = canExpand && _isHovered;

    return MouseRegion(
      cursor: SystemMouseCursors.click,
      onEnter: (_) {
        if (mounted && canExpand) setState(() => _isHovered = true);
      },
      onExit: (_) {
        if (mounted && canExpand) setState(() => _isHovered = false);
      },
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: _abrirPortal,
        child: Tooltip(
          message: 'Módulo de Estudiantes Unimagdalena (AyRe)',
          waitDuration: const Duration(milliseconds: 600),
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 240),
            curve: Curves.easeOutCubic,
            height: 36,
            padding: const EdgeInsets.symmetric(horizontal: 8),
            decoration: BoxDecoration(
              color: isDark
                  ? (_isHovered
                      ? const Color(0xFF16181D)
                      : const Color(0xFF0F1014).o(0.85))
                  : (_isHovered
                      ? const Color(0xFFF2F2F7)
                      : Colors.white.o(0.90)),
              borderRadius: BorderRadius.circular(18),
              border: Border.all(
                color: _isHovered
                    ? const Color(0xFF30D158).o(0.60)
                    : (isDark
                        ? const Color(0xFF1E2128)
                        : const Color(0xFFE5E5EA)),
                width: 1,
              ),
              boxShadow: _isHovered
                  ? [
                      BoxShadow(
                        color: const Color(0xFF30D158).o(0.15),
                        blurRadius: 10,
                        offset: const Offset(0, 2),
                      ),
                    ]
                  : null,
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                // Logo oficial Unimagdalena
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: Image.network(
                    'https://cdn.unimagdalena.edu.co/images/escudo/bg_dark/default.png',
                    width: 20,
                    height: 20,
                    fit: BoxFit.contain,
                    errorBuilder: (_, __, ___) => const Icon(
                      Icons.school_outlined,
                      size: 18,
                      color: Color(0xFF30D158),
                    ),
                  ),
                ),
                // Contenido expandible en Hover
                if (canExpand)
                  AnimatedCrossFade(
                    duration: const Duration(milliseconds: 200),
                    firstCurve: Curves.easeOut,
                    secondCurve: Curves.easeIn,
                    crossFadeState: isExpanded
                        ? CrossFadeState.showSecond
                        : CrossFadeState.showFirst,
                    firstChild: const SizedBox(width: 0),
                    secondChild: Padding(
                      padding: const EdgeInsets.only(left: 8, right: 2),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            'Portal Estudiantes',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                              letterSpacing: -0.2,
                              color: isDark ? Colors.white : Colors.black87,
                            ),
                          ),
                          const SizedBox(width: 4),
                          Icon(
                            Icons.north_east_rounded,
                            size: 11,
                            color: isDark
                                ? const Color(0xFF8E8E93)
                                : const Color(0xFF636366),
                          ),
                        ],
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
}
