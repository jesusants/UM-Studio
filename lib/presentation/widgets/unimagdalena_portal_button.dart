import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/theme/app_theme.dart';
import '../../data/services/global_environment_service.dart';

/// Botón interactivo y minimalista estilo cápsula que muestra el escudo oficial
/// de la Universidad del Magdalena en estado de reposo y, al pasar el cursor
/// por encima (`onHover`), expande suavemente su ancho revelando el título
/// "Portal Estudiantes" con el indicador externo `↗` para abrir AyRe/Admisiones.
///
/// Ocupa un espacio reservado estricto de 36 x 36 px dentro del [Row] padre,
/// desplegando la vista expandida (160 px) como una capa flotante por encima
/// mediante [Stack] con [Clip.none], eliminando al 100% el layout shift y
/// garantizando que los elementos contiguos permanezcan inmóviles.
class UnimagdalenaPortalButton extends StatefulWidget {
  const UnimagdalenaPortalButton({
    super.key,
    this.expandOnHover = true,
    this.portalUrl,
    this.onTap,
  });

  /// Determina si el botón expande su ancho al recibir hover.
  final bool expandOnHover;

  /// URL oficial de destino (Módulo de Estudiantes / AyRe). Si es null, lee de [GlobalEnvironmentService].
  final String? portalUrl;

  /// Callback opcional que reemplaza la llamada a `launchUrl` (útil para pruebas unitarias).
  final VoidCallback? onTap;

  @override
  State<UnimagdalenaPortalButton> createState() =>
      _UnimagdalenaPortalButtonState();
}

class _UnimagdalenaPortalButtonState extends State<UnimagdalenaPortalButton> {
  bool _isHovered = false;

  String get _effectiveUrl =>
      widget.portalUrl ??
      GlobalEnvironmentService.instance.config.portalEstudiantesUrl;

  Future<void> _abrirPortal() async {
    if (widget.onTap != null) {
      widget.onTap!();
      return;
    }
    final uri = Uri.parse(_effectiveUrl);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final canExpand = widget.expandOnHover;
    final isExpanded = canExpand && _isHovered;

    // Caja fija de 36x36 para que el Row NUNCA cambie de tamaño ni empuje a UM STUDIO
    return SizedBox(
      width: 36,
      height: 36,
      child: Stack(
        clipBehavior: Clip.none,
        alignment: Alignment.centerLeft,
        children: [
          MouseRegion(
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
                message: 'Portal Estudiantes Unimagdalena (AyRe)',
                waitDuration: const Duration(milliseconds: 500),
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 220),
                  curve: Curves.easeOutCubic,
                  height: 36,
                  // Si no hay hover mide 36px, si hay hover flota hacia la derecha a 160px
                  width: isExpanded ? 160 : 36,
                  clipBehavior: Clip.antiAlias,
                  decoration: BoxDecoration(
                    color: isDark
                        ? (isExpanded
                            ? const Color(0xFF1C1E24)
                            : const Color(0xFF121418))
                        : (isExpanded
                            ? Colors.white
                            : const Color(0xFFF2F2F7)),
                    borderRadius: BorderRadius.circular(18),
                    border: Border.all(
                      color: isExpanded
                          ? const Color(0xFF30D158)
                          : (isDark
                              ? const Color(0xFF262930)
                              : const Color(0xFFE5E5EA)),
                      width: 1,
                    ),
                    boxShadow: isExpanded
                        ? [
                            BoxShadow(
                              color: Colors.black.o(isDark ? 0.40 : 0.12),
                              blurRadius: 12,
                              offset: const Offset(0, 3),
                            ),
                          ]
                        : null,
                  ),
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    physics: const NeverScrollableScrollPhysics(),
                    child: SizedBox(
                      height: 34,
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          // Escudo oficial siempre fijo en 34x34 centrado
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
                          // Texto que se revela flotando suavemente
                          if (isExpanded) ...[
                            const SizedBox(width: 4),
                            Text(
                              'Portal Estudiantes',
                              maxLines: 1,
                              softWrap: false,
                              style: TextStyle(
                                fontSize: 11.5,
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
                            const SizedBox(width: 8),
                          ],
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
