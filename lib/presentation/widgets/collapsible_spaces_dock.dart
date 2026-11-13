import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/theme/app_theme.dart';
import 'ios_primitives.dart';

/// Metadatos de un espacio de navegación en la barra desplegable móvil.
class DockSpaceItem {
  const DockSpaceItem({
    required this.icon,
    required this.label,
    this.accentColor,
  });

  final IconData icon;
  final String label;
  final Color? accentColor;
}

/// Barra de Espacios Desplegable exclusiva para dispositivos móviles (`< 1024px`).
/// Alterna suavemente (`240ms`, `Curves.easeOutCubic`) entre una cápsula
/// *glassmorphism* completa y una píldora compacta de `40px` al hacer scroll o minimizar.
class CollapsibleSpacesDock extends StatelessWidget {
  const CollapsibleSpacesDock({
    super.key,
    required this.currentIndex,
    required this.isCollapsed,
    required this.onSelect,
    required this.onToggleCollapsed,
    this.items = defaultItems,
  });

  final int currentIndex;
  final bool isCollapsed;
  final ValueChanged<int> onSelect;
  final VoidCallback onToggleCollapsed;
  final List<DockSpaceItem> items;

  static const List<DockSpaceItem> defaultItems = [
    DockSpaceItem(icon: Icons.today_rounded, label: 'Resumen'),
    DockSpaceItem(icon: Icons.calendar_month_rounded, label: 'Calendario'),
    DockSpaceItem(icon: Icons.school_rounded, label: 'Clases'),
    DockSpaceItem(icon: Icons.menu_book_rounded, label: 'Estudio'),
  ];

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final safeBottom = MediaQuery.paddingOf(context).bottom;
    final activeItem = items[currentIndex.clamp(0, items.length - 1)];
    final activeAccent = activeItem.accentColor ?? p.green;

    final bgColor = isDark
        ? const Color(0xEB0D0E12) // ~92%
        : const Color(0xF0FFFFFF); // ~94%
    final borderColor = isDark
        ? const Color(0xFF1E212A)
        : const Color(0xFFE5E5EA);

    return Padding(
      padding: EdgeInsets.fromLTRB(14, 0, 14, safeBottom + 10),
      child: AnimatedSwitcher(
        duration: const Duration(milliseconds: 240),
        switchInCurve: Curves.easeOutCubic,
        switchOutCurve: Curves.easeInCubic,
        transitionBuilder: (child, anim) => FadeTransition(
          opacity: anim,
          child: ScaleTransition(
            scale: Tween<double>(begin: 0.94, end: 1.0).animate(anim),
            alignment: Alignment.bottomRight,
            child: child,
          ),
        ),
        child: isCollapsed
            ? Align(
                key: const ValueKey('dock_collapsed'),
                alignment: Alignment.bottomRight,
                child: TapScale(
                  onTap: () {
                    HapticFeedback.lightImpact();
                    onToggleCollapsed();
                  },
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(999),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 16, sigmaY: 16),
                      child: Container(
                        height: 40,
                        padding: const EdgeInsets.symmetric(horizontal: 14),
                        decoration: BoxDecoration(
                          color: bgColor,
                          borderRadius: BorderRadius.circular(999),
                          border: Border.all(color: borderColor, width: 1),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withAlpha(isDark ? 110 : 22),
                              blurRadius: 18,
                              offset: const Offset(0, 6),
                            ),
                          ],
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(activeItem.icon, size: 17, color: activeAccent),
                            const SizedBox(width: 7),
                            Text(
                              activeItem.label,
                              maxLines: 1,
                              softWrap: false,
                              overflow: TextOverflow.ellipsis,
                              style: TextStyle(
                                fontSize: 12.5,
                                fontWeight: FontWeight.w600,
                                color: p.textPrimary,
                              ),
                            ),
                            const SizedBox(width: 4),
                            Icon(
                              Icons.keyboard_arrow_up_rounded,
                              size: 18,
                              color: p.textSecondary,
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              )
            : ClipRRect(
                key: const ValueKey('dock_expanded'),
                borderRadius: BorderRadius.circular(24),
                child: BackdropFilter(
                  filter: ImageFilter.blur(sigmaX: 18, sigmaY: 18),
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 7),
                    decoration: BoxDecoration(
                      color: bgColor,
                      borderRadius: BorderRadius.circular(24),
                      border: Border.all(color: borderColor, width: 1),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withAlpha(isDark ? 120 : 24),
                          blurRadius: 22,
                          offset: const Offset(0, 8),
                        ),
                      ],
                    ),
                    child: Row(
                      children: [
                        for (var i = 0; i < items.length; i++)
                          Expanded(
                            child: TapScale(
                              onTap: () => onSelect(i),
                              child: AnimatedContainer(
                                duration: const Duration(milliseconds: 220),
                                curve: Curves.easeOutCubic,
                                margin: const EdgeInsets.symmetric(horizontal: 2),
                                padding: const EdgeInsets.symmetric(vertical: 6),
                                decoration: BoxDecoration(
                                  color: i == currentIndex
                                      ? (isDark
                                          ? const Color(0xFF191C24)
                                          : const Color(0xFFF2F2F7))
                                      : Colors.transparent,
                                  borderRadius: BorderRadius.circular(16),
                                ),
                                child: Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Icon(
                                      items[i].icon,
                                      size: 20,
                                      color: i == currentIndex
                                          ? (items[i].accentColor ?? p.green)
                                          : p.textTertiary,
                                    ),
                                    const SizedBox(height: 2),
                                    Text(
                                      items[i].label,
                                      maxLines: 1,
                                      softWrap: false,
                                      overflow: TextOverflow.ellipsis,
                                      style: TextStyle(
                                        fontSize: 10,
                                        fontWeight: i == currentIndex
                                            ? FontWeight.w600
                                            : FontWeight.w500,
                                        color: i == currentIndex
                                            ? p.textPrimary
                                            : p.textTertiary,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        const SizedBox(width: 4),
                        TapScale(
                          onTap: () {
                            HapticFeedback.lightImpact();
                            onToggleCollapsed();
                          },
                          child: Container(
                            width: 34,
                            height: 34,
                            decoration: BoxDecoration(
                              color: isDark
                                  ? const Color(0xFF191C24)
                                  : const Color(0xFFF2F2F7),
                              shape: BoxShape.circle,
                              border: Border.all(color: borderColor, width: 1),
                            ),
                            child: Icon(
                              Icons.keyboard_arrow_down_rounded,
                              size: 20,
                              color: p.textSecondary,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
      ),
    );
  }
}
