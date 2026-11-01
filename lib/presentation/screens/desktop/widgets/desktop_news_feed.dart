import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../widgets/ios_primitives.dart';

class NewsItemData {
  const NewsItemData({
    required this.id,
    required this.category,
    required this.relativeDate,
    required this.title,
    required this.summary,
    required this.accentColor,
  });

  final String id;
  final String category;
  final String relativeDate;
  final String title;
  final String summary;
  final Color accentColor;
}

/// Módulo de Noticias y Avisos de Facultad para Desktop con efecto hover y carrusel automático de 15 segundos.
class DesktopNewsFeed extends StatefulWidget {
  const DesktopNewsFeed({super.key});

  @override
  State<DesktopNewsFeed> createState() => _DesktopNewsFeedState();
}

class _DesktopNewsFeedState extends State<DesktopNewsFeed> {
  static const List<NewsItemData> _news = [
    NewsItemData(
      id: 'news_1',
      category: 'ACADÉMICO',
      relativeDate: 'Hace 2 horas',
      title: 'Actualización de Moodle: Cierre de segundo corte de notas',
      summary:
          'El registro de calificaciones del 30% correspondiente al segundo corte estará habilitado hasta el domingo a medianoche.',
      accentColor: Color(0xFF30D158),
    ),
    NewsItemData(
      id: 'news_2',
      category: 'EVENTO',
      relativeDate: 'Hoy 09:30 AM',
      title: 'Seminario de Transición Energética e Hidrógeno Verde',
      summary:
          'Conferencia magistral en el Auditorio Julio Otero sobre integración de microrredes fotovoltaicas en el Caribe colombiano.',
      accentColor: Color(0xFF5E5CE6),
    ),
    NewsItemData(
      id: 'news_3',
      category: 'CONVOCATORIA',
      relativeDate: 'Ayer',
      title: 'Cronograma de inscripciones y habilitaciones de ciencias básicas',
      summary:
          'Fechas oficiales para el proceso de validaciones y suficiencias de Física Mecánica, Cálculo Multivariable y Álgebra Lineal.',
      accentColor: Color(0xFFFF9F0A),
    ),
    NewsItemData(
      id: 'news_4',
      category: 'INVESTIGACIÓN',
      relativeDate: 'Hace 3 días',
      title: 'Semillero de Investigación en Energía Solar & Smart Grids',
      summary:
          'Apertura de cupos para estudiantes de Ingeniería Energética desde 4.° cuatrimestre vinculados al laboratorio de energías renovables.',
      accentColor: Color(0xFF0A84FF),
    ),
  ];

  int _carouselIndex = 0;
  Timer? _carouselTimer;
  bool _isRefreshing = false;

  @override
  void initState() {
    super.initState();
    _startCarouselTimer();
  }

  void _startCarouselTimer() {
    _carouselTimer = Timer.periodic(const Duration(seconds: 15), (_) {
      if (mounted) {
        setState(() {
          _carouselIndex = (_carouselIndex + 1) % _news.length;
        });
      }
    });
  }

  @override
  void dispose() {
    _carouselTimer?.cancel();
    super.dispose();
  }

  Future<void> _handleRefresh() async {
    HapticFeedback.lightImpact();
    setState(() => _isRefreshing = true);
    await Future<void>.delayed(const Duration(milliseconds: 650));
    if (mounted) {
      setState(() => _isRefreshing = false);
      showIosToast(
        context,
        'Noticias de Facultad actualizadas',
        accentColor: const Color(0xFF30D158),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final featured = _news[_carouselIndex];

    return Container(
      decoration: BoxDecoration(
        color: const Color(0xDC0D0E12),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: const Color(0xFF1A1D24), width: 1),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Encabezado del Feed
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(7),
                decoration: BoxDecoration(
                  color: const Color(0xFF30D158).o(0.14),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Icon(
                  Icons.campaign_rounded,
                  size: 16,
                  color: Color(0xFF30D158),
                ),
              ),
              const SizedBox(width: 9),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'NOTICIAS & CÁTEDRA',
                      style: mono(
                        fontSize: 11,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 1.0,
                        color: p.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      'Facultad de Ingeniería • Unimagdalena',
                      style: TextStyle(
                        fontSize: 10.5,
                        fontWeight: FontWeight.w500,
                        color: p.textSecondary,
                      ),
                    ),
                  ],
                ),
              ),
              MouseRegion(
                cursor: SystemMouseCursors.click,
                child: GestureDetector(
                  onTap: _isRefreshing ? null : _handleRefresh,
                  child: Container(
                    padding: const EdgeInsets.all(6),
                    decoration: BoxDecoration(
                      color: const Color(0xFF14161C),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: const Color(0xFF222630)),
                    ),
                    child: _isRefreshing
                        ? const SizedBox(
                            width: 14,
                            height: 14,
                            child: CircularProgressIndicator(
                              strokeWidth: 2,
                              color: Color(0xFF30D158),
                            ),
                          )
                        : Icon(
                            Icons.refresh_rounded,
                            size: 14,
                            color: p.textSecondary,
                          ),
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),

          // Carrusel de Titular Destacado (Transición cada 15 segundos)
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 9),
            decoration: BoxDecoration(
              color: const Color(0xFF13161F),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: const Color(0xFF1E222C)),
            ),
            child: Row(
              children: [
                PulseDot(color: featured.accentColor, size: 7),
                const SizedBox(width: 8),
                Expanded(
                  child: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 380),
                    transitionBuilder: (child, anim) {
                      return FadeTransition(
                        opacity: anim,
                        child: SlideTransition(
                          position: Tween<Offset>(
                            begin: const Offset(0.0, 0.25),
                            end: Offset.zero,
                          ).animate(anim),
                          child: child,
                        ),
                      );
                    },
                    child: Text(
                      featured.title,
                      key: ValueKey('featured_${featured.id}'),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 11.5,
                        fontWeight: FontWeight.w600,
                        color: p.textPrimary,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  '${_carouselIndex + 1}/${_news.length}',
                  style: mono(fontSize: 10, color: p.textTertiary),
                ),
              ],
            ),
          ),
          const SizedBox(height: 14),

          // Lista de Noticias con Scroll Inercial Limpio
          Expanded(
            child: ScrollConfiguration(
              behavior: ScrollConfiguration.of(context).copyWith(
                scrollbars: false,
              ),
              child: ListView.separated(
                physics: const BouncingScrollPhysics(),
                itemCount: _news.length,
                separatorBuilder: (_, __) => const SizedBox(height: 11),
                itemBuilder: (context, index) {
                  return _DesktopNewsCard(item: _news[index]);
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _DesktopNewsCard extends StatefulWidget {
  const _DesktopNewsCard({required this.item});

  final NewsItemData item;

  @override
  State<_DesktopNewsCard> createState() => _DesktopNewsCardState();
}

class _DesktopNewsCardState extends State<_DesktopNewsCard> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final item = widget.item;

    return MouseRegion(
      cursor: SystemMouseCursors.click,
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        curve: Curves.easeOutCubic,
        transform: Matrix4.translationValues(0, _isHovered ? -2.0 : 0.0, 0),
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: _isHovered ? const Color(0xFF141720) : const Color(0xFF0F1116),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: _isHovered ? const Color(0xFF30D158) : const Color(0xFF1C1F28),
            width: _isHovered ? 1.2 : 1.0,
          ),
          boxShadow: _isHovered
              ? [
                  BoxShadow(
                    color: const Color(0xFF30D158).o(0.12),
                    blurRadius: 14,
                    offset: const Offset(0, 4),
                  ),
                ]
              : null,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                // Categoría en píldora
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 7,
                    vertical: 2.5,
                  ),
                  decoration: BoxDecoration(
                    color: item.accentColor.o(0.12),
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(
                      color: item.accentColor.o(0.35),
                      width: 1,
                    ),
                  ),
                  child: Text(
                    item.category,
                    style: mono(
                      fontSize: 9.5,
                      fontWeight: FontWeight.w700,
                      letterSpacing: 0.8,
                      color: item.accentColor,
                    ),
                  ),
                ),
                const Spacer(),
                Text(
                  item.relativeDate,
                  style: mono(fontSize: 10, color: p.textTertiary),
                ),
              ],
            ),
            const SizedBox(height: 8),

            // Titular
            Text(
              item.title,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w700,
                letterSpacing: -0.2,
                height: 1.3,
                color: _isHovered ? const Color(0xFF30D158) : p.textPrimary,
              ),
            ),
            const SizedBox(height: 5),

            // Resumen
            Text(
              item.summary,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 11.5,
                height: 1.4,
                color: p.textSecondary,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
