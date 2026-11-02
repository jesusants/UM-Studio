import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';
import '../../data/services/global_environment_service.dart';

/// Banner de difusión global (Broadcast Banner) visible en la parte superior
/// del dashboard cuando el administrador lo habilita vía db/global_config.json.
class GlobalBroadcastBanner extends StatelessWidget {
  const GlobalBroadcastBanner({super.key});

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
        Color badgeColor;
        IconData badgeIcon;

        switch (config.globalBannerType) {
          case 'warning':
            badgeColor = p.orange;
            badgeIcon = Icons.warning_amber_rounded;
            break;
          case 'success':
            badgeColor = p.green;
            badgeIcon = Icons.check_circle_outline_rounded;
            break;
          case 'urgent':
            badgeColor = const Color(0xFFFF453A);
            badgeIcon = Icons.priority_high_rounded;
            break;
          case 'info':
          default:
            badgeColor = p.indigo;
            badgeIcon = Icons.campaign_rounded;
        }

        return Container(
          width: double.infinity,
          margin: const EdgeInsets.only(bottom: 12),
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
          decoration: BoxDecoration(
            color: badgeColor.o(0.10),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: badgeColor.o(0.35)),
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Icon(badgeIcon, size: 18, color: badgeColor),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      title,
                      style: TextStyle(
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: badgeColor,
                      ),
                    ),
                    if (message.isNotEmpty) ...[
                      const SizedBox(height: 2),
                      Text(
                        message,
                        style: TextStyle(
                          fontSize: 11.5,
                          color: p.textPrimary,
                          height: 1.3,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
