import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/theme/app_theme.dart';

/// Botón interactivo y minimalista estilo cápsula que muestra el escudo oficial
/// de la Universidad del Magdalena en estado de reposo y, al pasar el cursor
/// por encima (`onHover`), expande suavemente su ancho revelando el título
/// "Portal Estudiantes" con el indicador externo `↗` para abrir AyRe/Admisiones.
///
/// Implementa un anclaje inmutable (34x34 fijo para el logo) y ancho explícito
/// en el [AnimatedContainer] con [HitTestBehavior.opaque] para evitar bucles
/// de oscilación de hit-test ("palpitar" o layout shift loop).
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
      hitTestBehavior: HitTestBehavior.opaque,
      onEnter: (_) {
        if (canExpand && !_isHovered && mounted) {
          setState(() => _isHovered = true);
        }
      },
      onExit: (_) {
        if (canExpand && _isHovered && mounted) {
          setState(() => _isHovered = false);
        }
      },
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: _abrirPortal,
        child: Tooltip(
          message: 'Módulo de Estudiantes Unimagdalena (AyRe)',
          waitDuration: const Duration(milliseconds: 500),
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 220),
            curve: Curves.easeOutCubic,
            height: 36,
            width: isExpanded ? 162 : 36, // Ancho fijo explícito para evitar layout shift
            clipBehavior: Clip.antiAlias,
            decoration: BoxDecoration(
              color: isDark
                  ? (isExpanded
                      ? const Color(0xFF16181D)
                      : const Color(0xFF0F1014).o(0.85))
                  : (isExpanded
                      ? const Color(0xFFE5E5EA)
                      : Colors.white.o(0.95)),
              borderRadius: BorderRadius.circular(18),
              border: Border.all(
                color: isExpanded
                    ? const Color(0xFF30D158)
                    : (isDark
                        ? const Color(0xFF1E2128)
                        : const Color(0xFFE5E5EA)),
                width: 1,
              ),
              boxShadow: isExpanded
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
                // Logo fijo siempre de 34x34 centrado (anclaje inmutable)
                SizedBox(
                  width: 34,
                  height: 34,
                  child: Center(
                    child: ClipRRect(
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
                  ),
                ),
                // Texto revelado que se desliza sin empujar el logo
                Expanded(
                  child: ClipRect(
                    child: OverflowBox(
                      minWidth: 0,
                      maxWidth: 260,
                      alignment: Alignment.centerLeft,
                      child: AnimatedOpacity(
                        duration: const Duration(milliseconds: 180),
                        opacity: isExpanded ? 1.0 : 0.0,
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(
                              'Portal Estudiantes',
                              maxLines: 1,
                              style: TextStyle(
                                fontSize: 11.5,
                                fontWeight: FontWeight.w600,
                                letterSpacing: -0.2,
                                color: isDark ? Colors.white : Colors.black87,
                              ),
                            ),
                            const SizedBox(width: 3),
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
