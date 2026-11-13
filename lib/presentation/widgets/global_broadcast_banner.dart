import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';
import '../../data/services/global_environment_service.dart';

/// Tarjeta fijada de Comunicado Global Oficial del Administrador (`global_banner_*`).
/// Se inserta como Posición 0 dentro del feed de Noticias tanto en PC como en móvil,
/// eliminando popups intrusivos o banners superiores que roban espacio vertical.
class GlobalBroadcastBanner extends StatelessWidget {
  const GlobalBroadcastBanner({
    super.key,
    this.width,
    this.margin = EdgeInsets.zero,
  });

  final double? width;
  final EdgeInsetsGeometry margin;

  static bool get isActive {
    final config = GlobalEnvironmentService.instance.config;
    return config.globalBannerEnabled &&
        (config.globalBannerTitle.trim().isNotEmpty ||
            config.globalBannerMessage.trim().isNotEmpty);
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: GlobalEnvironmentService.instance,
      builder: (context, _) {
        final config = GlobalEnvironmentService.instance.config;
        if (!config.globalBannerEnabled ||
            (config.globalBannerTitle.trim().isEmpty &&
                config.globalBannerMessage.trim().isEmpty)) {
          return const SizedBox.shrink();
        }

        final title = config.globalBannerTitle.trim().isNotEmpty
            ? config.globalBannerTitle.trim()
            : 'Aviso Oficial';
        final message = config.globalBannerMessage.trim();

        final p = context.palette;
        final isDark = Theme.of(context).brightness == Brightness.dark;
        final Color badgeColor;
        switch (config.globalBannerType) {
          case 'warning':
            badgeColor = p.orange;
            break;
          case 'success':
            badgeColor = p.green;
            break;
          case 'urgent':
            badgeColor = const Color(0xFFFF453A);
            break;
          case 'info':
          default:
            badgeColor = const Color(0xFF5E5CE6);
        }

        return Container(
          width: width ?? double.infinity,
          margin: margin,
          padding: const EdgeInsets.all(13),
          decoration: BoxDecoration(
            color: p.card,
            borderRadius: BorderRadius.circular(width != null ? 18 : 16),
            border: Border.all(color: badgeColor.o(0.45), width: 1),
            boxShadow: !isDark
                ? [
                    BoxShadow(
                      color: Colors.black.withAlpha(10),
                      blurRadius: 16,
                      offset: const Offset(0, 4),
                    ),
                  ]
                : null,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Row(
                children: [
                  Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 7, vertical: 2.5),
                    decoration: BoxDecoration(
                      color: badgeColor.o(0.14),
                      borderRadius: BorderRadius.circular(6),
                      border: Border.all(color: badgeColor.o(0.38)),
                    ),
                    child: Text(
                      '📌 COMUNICADO OFICIAL',
                      style: mono(
                        fontSize: 8.5,
                        fontWeight: FontWeight.w800,
                        letterSpacing: 0.6,
                        color: badgeColor,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                title,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 13,
                  fontWeight: FontWeight.w700,
                  letterSpacing: -0.2,
                  color: p.textPrimary,
                ),
              ),
              if (message.isNotEmpty) ...[
                const SizedBox(height: 4),
                Text(
                  message,
                  maxLines: width != null ? 4 : 6,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 11.5,
                    height: 1.35,
                    color: p.textSecondary,
                  ),
                ),
              ],
            ],
          ),
        );
      },
    );
  }
}
