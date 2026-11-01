import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/noticia_model.dart';
import '../../../../data/services/unimagdalena_realtime_news_service.dart';
import '../../../widgets/ios_primitives.dart';
import '../desktop_theme_tokens.dart';

/// Tablón Institucional & Feed de Noticias en Vivo desde Unimagdalena para Desktop.
/// Incluye auto-refresco periódico, bypass de CORS, filtrado por categorías,
/// botón de recarga con animación de giro y apertura externa en navegador.
class DesktopNewsFeed extends StatefulWidget {
  const DesktopNewsFeed({super.key});

  @override
  State<DesktopNewsFeed> createState() => _DesktopNewsFeedState();
}

class _DesktopNewsFeedState extends State<DesktopNewsFeed>
    with SingleTickerProviderStateMixin {
  final UnimagdalenaRealtimeNewsService _newsService =
      UnimagdalenaRealtimeNewsService.instance;
  late final AnimationController _spinController;

  String _selectedCategory = 'TODAS';

  @override
  void initState() {
    super.initState();
    _spinController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 900),
    );
    _newsService.init();
  }

  @override
  void dispose() {
    _spinController.dispose();
    super.dispose();
  }

  Future<void> _handleRefresh() async {
    HapticFeedback.lightImpact();
    _spinController.repeat();
    await _newsService.refreshNews(force: true);
    if (mounted) {
      _spinController.stop();
      _spinController.reset();
    }
  }

  Color _categoryColor(String category, DesktopThemeTokens tokens) {
    final cat = category.toUpperCase();
    if (cat.contains('FACULTAD')) return tokens.accentGreen;
    if (cat.contains('ACADÉMICO') || cat.contains('ACADEMICO')) {
      return const Color(0xFFFF9F0A);
    }
    if (cat.contains('INVESTIGA') || cat.contains('SEMILLERO')) {
      return tokens.accentIndigo;
    }
    return const Color(0xFF0A84FF);
  }

  String _formatTime(DateTime? dt) {
    if (dt == null) return 'En vivo';
    final h = dt.hour.toString().padLeft(2, '0');
    final m = dt.minute.toString().padLeft(2, '0');
    return '$h:$m';
  }

  List<NoticiaModel> _filterNews(List<NoticiaModel> news) {
    if (_selectedCategory == 'TODAS') return news;
    return news.where((n) {
      final cat = n.category.toUpperCase();
      if (_selectedCategory == 'FACULTAD') return cat.contains('FACULTAD');
      if (_selectedCategory == 'ACADÉMICO') {
        return cat.contains('ACADÉMICO') || cat.contains('ACADEMICO');
      }
      if (_selectedCategory == 'INVESTIGACIÓN') {
        return cat.contains('INVESTIGA') || cat.contains('SEMILLERO');
      }
      if (_selectedCategory == 'INSTITUCIONAL') {
        return cat.contains('INSTITUCIONAL');
      }
      return cat.contains(_selectedCategory);
    }).toList();
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);

    return ListenableBuilder(
      listenable: _newsService,
      builder: (context, _) {
        final allNews = _newsService.news;
        final filtered = _filterNews(allNews);
        final isLoading = _newsService.isLoading;
        final lastUpdateText = _formatTime(_newsService.lastUpdated);

        return Container(
          decoration: BoxDecoration(
            color: tokens.surface,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: tokens.border, width: 1),
            boxShadow: [
              BoxShadow(
                color: tokens.shadowColor,
                blurRadius: 20,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          padding: const EdgeInsets.all(18),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // 1. Cabecera con Micro-tipografía, En vivo y botón de refresco
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Expanded(
                    child: Row(
                      children: [
                        Dot(color: tokens.accentGreen, size: 6.5),
                        const SizedBox(width: 7),
                        Flexible(
                          child: Text(
                            'NOTICIAS & EVENTOS',
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 10,
                              fontWeight: FontWeight.w700,
                              letterSpacing: 1.1,
                              color: tokens.textSecondary,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    'Actualizado: $lastUpdateText',
                    style: mono(fontSize: 9.5, color: tokens.textTertiary),
                  ),
                  const SizedBox(width: 8),
                  TapScale(
                    onTap: isLoading ? null : _handleRefresh,
                    child: Container(
                      width: 28,
                      height: 28,
                      decoration: BoxDecoration(
                        color: tokens.surfaceElevated,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: tokens.border),
                      ),
                      alignment: Alignment.center,
                      child: isLoading
                          ? SizedBox(
                              width: 13,
                              height: 13,
                              child: CircularProgressIndicator(
                                strokeWidth: 2,
                                color: tokens.accentGreen,
                              ),
                            )
                          : RotationTransition(
                              turns: _spinController,
                              child: Icon(
                                Icons.refresh_rounded,
                                size: 16,
                                color: tokens.textSecondary,
                              ),
                            ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),

              // 2. Selector de Categorías (Todas, Facultad, Académico, Investigación)
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                child: Row(
                  children: [
                    _CategoryPill(
                      label: 'Todas',
                      id: 'TODAS',
                      selectedId: _selectedCategory,
                      tokens: tokens,
                      onSelect: (id) => setState(() => _selectedCategory = id),
                    ),
                    const SizedBox(width: 6),
                    _CategoryPill(
                      label: 'Facultad',
                      id: 'FACULTAD',
                      selectedId: _selectedCategory,
                      tokens: tokens,
                      onSelect: (id) => setState(() => _selectedCategory = id),
                    ),
                    const SizedBox(width: 6),
                    _CategoryPill(
                      label: 'Académico',
                      id: 'ACADÉMICO',
                      selectedId: _selectedCategory,
                      tokens: tokens,
                      onSelect: (id) => setState(() => _selectedCategory = id),
                    ),
                    const SizedBox(width: 6),
                    _CategoryPill(
                      label: 'Investigación',
                      id: 'INVESTIGACIÓN',
                      selectedId: _selectedCategory,
                      tokens: tokens,
                      onSelect: (id) => setState(() => _selectedCategory = id),
                    ),
                    const SizedBox(width: 6),
                    _CategoryPill(
                      label: 'Institucional',
                      id: 'INSTITUCIONAL',
                      selectedId: _selectedCategory,
                      tokens: tokens,
                      onSelect: (id) => setState(() => _selectedCategory = id),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 14),

              // 3. Feed de Noticias con Desplazamiento Interno Inercial
              Expanded(
                child: filtered.isEmpty
                    ? Center(
                        child: Text(
                          'No hay publicaciones en esta categoría',
                          style: TextStyle(
                            fontSize: 12,
                            color: tokens.textSecondary,
                          ),
                        ),
                      )
                    : ListView.separated(
                        physics: const BouncingScrollPhysics(),
                        itemCount: filtered.length,
                        separatorBuilder: (_, __) => const SizedBox(height: 10),
                        itemBuilder: (context, index) {
                          final item = filtered[index];
                          final accent = _categoryColor(item.category, tokens);
                          return _DesktopNewsCard(
                            item: item,
                            accentColor: accent,
                            tokens: tokens,
                          );
                        },
                      ),
              ),
              const SizedBox(height: 12),

              // 4. Barra Inferior de Atajos de Teclado
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                decoration: BoxDecoration(
                  color: tokens.surfaceElevated,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: tokens.border),
                ),
                child: Wrap(
                  alignment: WrapAlignment.spaceAround,
                  crossAxisAlignment: WrapCrossAlignment.center,
                  spacing: 8,
                  runSpacing: 4,
                  children: [
                    _KeyShortcutBadge(keyText: 'T', label: 'Tema', tokens: tokens),
                    _KeyShortcutBadge(keyText: 'F', label: 'Pantalla', tokens: tokens),
                    _KeyShortcutBadge(keyText: 'Espacio', label: 'Timer', tokens: tokens),
                    _KeyShortcutBadge(keyText: 'Esc', label: 'Volver', tokens: tokens),
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

class _CategoryPill extends StatelessWidget {
  const _CategoryPill({
    required this.label,
    required this.id,
    required this.selectedId,
    required this.tokens,
    required this.onSelect,
  });

  final String label;
  final String id;
  final String selectedId;
  final DesktopThemeTokens tokens;
  final ValueChanged<String> onSelect;

  @override
  Widget build(BuildContext context) {
    final isSelected = id == selectedId;
    return TapScale(
      onTap: () {
        HapticFeedback.selectionClick();
        onSelect(id);
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4.5),
        decoration: BoxDecoration(
          color: isSelected ? tokens.accentGreen : tokens.surfaceElevated,
          borderRadius: BorderRadius.circular(8),
          border: Border.all(
            color: isSelected ? tokens.accentGreen : tokens.border,
            width: 1,
          ),
        ),
        child: Text(
          label,
          style: mono(
            fontSize: 10,
            fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
            color: isSelected
                ? (tokens.isDark ? Colors.black : Colors.white)
                : tokens.textSecondary,
          ),
        ),
      ),
    );
  }
}

class _DesktopNewsCard extends StatefulWidget {
  const _DesktopNewsCard({
    required this.item,
    required this.accentColor,
    required this.tokens,
  });

  final NoticiaModel item;
  final Color accentColor;
  final DesktopThemeTokens tokens;

  @override
  State<_DesktopNewsCard> createState() => _DesktopNewsCardState();
}

class _DesktopNewsCardState extends State<_DesktopNewsCard> {
  bool _isHovered = false;

  Future<void> _openNewsUrl() async {
    final url = widget.item.url;
    if (url.isEmpty) return;
    try {
      final uri = Uri.parse(url);
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (_) {}
  }

  @override
  Widget build(BuildContext context) {
    final t = widget.tokens;
    final item = widget.item;

    final borderColor = _isHovered
        ? t.accentGreen
        : (item.isRecent ? t.accentGreen.o(0.4) : t.border);
    final bgColor = _isHovered ? t.surfaceElevated : t.surface;

    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      cursor: SystemMouseCursors.click,
      child: TapScale(
        onTap: _openNewsUrl,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 160),
          transform: Matrix4.translationValues(0, _isHovered ? -2 : 0, 0),
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: bgColor,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(
              color: borderColor,
              width: _isHovered || item.isRecent ? 1.2 : 1.0,
            ),
            boxShadow: _isHovered
                ? [
                    BoxShadow(
                      color: t.accentGreen.o(0.10),
                      blurRadius: 12,
                      offset: const Offset(0, 3),
                    ),
                  ]
                : null,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                    decoration: BoxDecoration(
                      color: widget.accentColor.o(0.12),
                      borderRadius: BorderRadius.circular(5),
                      border: Border.all(
                        color: widget.accentColor.o(0.35),
                        width: 1,
                      ),
                    ),
                    child: Text(
                      item.category.toUpperCase(),
                      style: mono(
                        fontSize: 8.5,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 0.6,
                        color: widget.accentColor,
                      ),
                    ),
                  ),
                  if (item.isRecent) ...[
                    const SizedBox(width: 6),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 5,
                        vertical: 1.5,
                      ),
                      decoration: BoxDecoration(
                        color: t.accentGreen.o(0.18),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Text(
                        'NUEVO',
                        style: mono(
                          fontSize: 8,
                          fontWeight: FontWeight.w800,
                          color: t.accentGreen,
                        ),
                      ),
                    ),
                  ],
                  const Spacer(),
                  Text(
                    item.dateText,
                    style: mono(fontSize: 9.5, color: t.textTertiary),
                  ),
                ],
              ),
              const SizedBox(height: 7),
              Text(
                item.title,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w700,
                  letterSpacing: -0.2,
                  height: 1.25,
                  color: _isHovered ? t.accentGreen : t.textPrimary,
                ),
              ),
              const SizedBox(height: 4),
              Text(
                item.summary,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 11,
                  height: 1.35,
                  color: t.textSecondary,
                ),
              ),
              const SizedBox(height: 6),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Text(
                    'Ver en unimagdalena.edu.co ↗',
                    style: mono(
                      fontSize: 9,
                      fontWeight: FontWeight.w600,
                      color: _isHovered ? t.accentGreen : t.textTertiary,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _KeyShortcutBadge extends StatelessWidget {
  const _KeyShortcutBadge({
    required this.keyText,
    required this.label,
    required this.tokens,
  });

  final String keyText;
  final String label;
  final DesktopThemeTokens tokens;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
          decoration: BoxDecoration(
            color: tokens.surface,
            borderRadius: BorderRadius.circular(4),
            border: Border.all(color: tokens.borderSubtle),
          ),
          child: Text(
            keyText,
            style: mono(
              fontSize: 8.5,
              fontWeight: FontWeight.w700,
              color: tokens.textSecondary,
            ),
          ),
        ),
        const SizedBox(width: 4),
        Text(
          label,
          style: TextStyle(
            fontSize: 9.5,
            color: tokens.textTertiary,
          ),
        ),
      ],
    );
  }
}
