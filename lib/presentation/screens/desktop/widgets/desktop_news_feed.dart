import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../widgets/ios_primitives.dart';
import '../desktop_theme_tokens.dart';

class NewsItemData {
  const NewsItemData({
    required this.id,
    required this.category,
    required this.categoryType,
    required this.relativeDate,
    required this.title,
    required this.summary,
    required this.accentColor,
  });

  final String id;
  final String category;
  final String categoryType; // 'facultad', 'academico', 'semillero'
  final String relativeDate;
  final String title;
  final String summary;
  final Color accentColor;
}

/// Tablón Institucional & Noticias de Ingeniería para Desktop (28% del ancho)
/// con filtro por categorías, desplazamiento inercial interno y barra de atajos de teclado.
class DesktopNewsFeed extends StatefulWidget {
  const DesktopNewsFeed({super.key});

  @override
  State<DesktopNewsFeed> createState() => _DesktopNewsFeedState();
}

class _DesktopNewsFeedState extends State<DesktopNewsFeed> {
  static const List<NewsItemData> _allNews = [
    NewsItemData(
      id: 'news_1',
      category: 'ACADÉMICO',
      categoryType: 'academico',
      relativeDate: 'Hace 2 horas',
      title: 'Actualización de Moodle: Cierre de segundo corte de notas',
      summary:
          'El registro de calificaciones del 30% correspondiente al segundo corte estará habilitado hasta el domingo a medianoche.',
      accentColor: Color(0xFF30D158),
    ),
    NewsItemData(
      id: 'news_2',
      category: 'FACULTAD',
      categoryType: 'facultad',
      relativeDate: 'Hoy 09:30 AM',
      title: 'Seminario de Transición Energética e Hidrógeno Verde',
      summary:
          'Conferencia magistral en el Auditorio Julio Otero sobre integración de microrredes fotovoltaicas en el Caribe colombiano.',
      accentColor: Color(0xFF5E5CE6),
    ),
    NewsItemData(
      id: 'news_3',
      category: 'ACADÉMICO',
      categoryType: 'academico',
      relativeDate: 'Ayer',
      title: 'Cronograma de habilitaciones de ciencias básicas',
      summary:
          'Fechas oficiales para validaciones y suficiencias de Física Mecánica, Cálculo Multivariable y Álgebra Lineal.',
      accentColor: Color(0xFFFF9F0A),
    ),
    NewsItemData(
      id: 'news_4',
      category: 'SEMILLERO',
      categoryType: 'semillero',
      relativeDate: 'Hace 3 días',
      title: 'Semillero de Investigación en Energía Solar & Smart Grids',
      summary:
          'Apertura de cupos para estudiantes de Ingeniería Energética vinculados a modelado de microrredes y baterías de litio.',
      accentColor: Color(0xFF0A84FF),
    ),
    NewsItemData(
      id: 'news_5',
      category: 'FACULTAD',
      categoryType: 'facultad',
      relativeDate: 'Hace 5 días',
      title: 'Nuevo equipamiento para el Laboratorio de Potencia y Máquinas',
      summary:
          'Se instalaron 4 bancos didácticos de motores síncronos y convertidores para prácticas del bloque curricular de máquinas térmicas.',
      accentColor: Color(0xFF30D158),
    ),
  ];

  String _selectedCategory = 'todas';

  List<NewsItemData> get _filteredNews {
    if (_selectedCategory == 'todas') return _allNews;
    return _allNews.where((n) => n.categoryType == _selectedCategory).toList();
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    final newsList = _filteredNews;

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
          // 1. Cabecera con Micro-tipografía
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
              const SizedBox(width: 6),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 2),
                decoration: BoxDecoration(
                  color: tokens.accentGreen.o(0.12),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  'Facultad',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: tokens.accentGreen,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),

          // 2. Selector de Categorías (Todas, Facultad, Académico, Semillero)
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            physics: const BouncingScrollPhysics(),
            child: Row(
              children: [
                _CategoryPill(
                  label: 'Todas',
                  id: 'todas',
                  selectedId: _selectedCategory,
                  tokens: tokens,
                  onSelect: (id) => setState(() => _selectedCategory = id),
                ),
                const SizedBox(width: 6),
                _CategoryPill(
                  label: 'Facultad',
                  id: 'facultad',
                  selectedId: _selectedCategory,
                  tokens: tokens,
                  onSelect: (id) => setState(() => _selectedCategory = id),
                ),
                const SizedBox(width: 6),
                _CategoryPill(
                  label: 'Académico',
                  id: 'academico',
                  selectedId: _selectedCategory,
                  tokens: tokens,
                  onSelect: (id) => setState(() => _selectedCategory = id),
                ),
                const SizedBox(width: 6),
                _CategoryPill(
                  label: 'Semillero',
                  id: 'semillero',
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
            child: newsList.isEmpty
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
                    itemCount: newsList.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 10),
                    itemBuilder: (context, index) {
                      return _NewsCard(
                        item: newsList[index],
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

class _NewsCard extends StatefulWidget {
  const _NewsCard({
    required this.item,
    required this.tokens,
  });

  final NewsItemData item;
  final DesktopThemeTokens tokens;

  @override
  State<_NewsCard> createState() => _NewsCardState();
}

class _NewsCardState extends State<_NewsCard> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final t = widget.tokens;
    final item = widget.item;

    final borderColor = _isHovered ? t.accentGreen : t.border;
    final bgColor = _isHovered ? t.surfaceElevated : t.surface;

    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      cursor: SystemMouseCursors.click,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 160),
        transform: Matrix4.translationValues(0, _isHovered ? -2 : 0, 0),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: borderColor,
            width: _isHovered ? 1.2 : 1.0,
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
                  padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: item.accentColor.o(0.12),
                    borderRadius: BorderRadius.circular(5),
                    border: Border.all(
                      color: item.accentColor.o(0.35),
                      width: 1,
                    ),
                  ),
                  child: Text(
                    item.category,
                    style: mono(
                      fontSize: 8.5,
                      fontWeight: FontWeight.w700,
                      letterSpacing: 0.6,
                      color: item.accentColor,
                    ),
                  ),
                ),
                const Spacer(),
                Text(
                  item.relativeDate,
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
          ],
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
