import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../../data/services/markdown_curriculum_service.dart';
import '../../../widgets/ios_primitives.dart';
import '../desktop_theme_tokens.dart';

/// Resultado indexado para el buscador rápido estilo Spotlight (`Ctrl/Cmd + K`).
class SpotlightSearchHit {
  const SpotlightSearchHit({
    required this.subject,
    required this.title,
    required this.subtitle,
    this.temaNumero,
    this.isMagistral = false,
  });

  final AsignaturaModel subject;
  final String title;
  final String subtitle;
  final int? temaNumero;
  final bool isMagistral;
}

/// Modal flotante estilo Spotlight (`Ctrl + K` / `Cmd + K`) exclusivo para PC.
class DesktopSpotlightSearch {
  static Future<SpotlightSearchHit?> show(
    BuildContext context, {
    required MarkdownCurriculumService? curriculum,
  }) {
    return showDialog<SpotlightSearchHit>(
      context: context,
      barrierDismissible: true,
      barrierColor: Colors.black.o(0.65),
      builder: (_) => _SpotlightSearchDialog(curriculum: curriculum),
    );
  }
}

class _SpotlightSearchDialog extends StatefulWidget {
  const _SpotlightSearchDialog({required this.curriculum});

  final MarkdownCurriculumService? curriculum;

  @override
  State<_SpotlightSearchDialog> createState() => _SpotlightSearchDialogState();
}

class _SpotlightSearchDialogState extends State<_SpotlightSearchDialog> {
  final TextEditingController _ctrl = TextEditingController();
  final FocusNode _inputFocus = FocusNode();
  late final List<SpotlightSearchHit> _allHits;
  List<SpotlightSearchHit> _filtered = const [];
  int _activeIndex = 0;

  @override
  void initState() {
    super.initState();
    _allHits = _buildIndex();
    _filtered = _allHits.take(18).toList();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) _inputFocus.requestFocus();
    });
  }

  @override
  void dispose() {
    _ctrl.dispose();
    _inputFocus.dispose();
    super.dispose();
  }

  List<SpotlightSearchHit> _buildIndex() {
    final db = widget.curriculum?.database;
    if (db == null) return const [];
    final hits = <SpotlightSearchHit>[];
    for (final s in db.allAsignaturas) {
      hits.add(
        SpotlightSearchHit(
          subject: s,
          title: s.nombre,
          subtitle: '${s.codigo} • Cuatrimestre ${s.cuatrimestre} • Asignatura',
        ),
      );
      for (final m in s.clasesMagistrales) {
        hits.add(
          SpotlightSearchHit(
            subject: s,
            title: m.titulo,
            subtitle:
                '${s.nombre} (${s.codigo}) • Cátedra Magistral ${m.numeroTema}',
            temaNumero: m.numeroTema,
            isMagistral: true,
          ),
        );
      }
      for (final t in s.temas) {
        hits.add(
          SpotlightSearchHit(
            subject: s,
            title: t.titulo,
            subtitle: '${s.nombre} (${s.codigo}) • Tema ${t.numeroTema}',
            temaNumero: t.numeroTema,
            isMagistral: false,
          ),
        );
      }
    }
    return hits;
  }

  void _onQueryChanged(String q) {
    final query = q.trim().toLowerCase();
    setState(() {
      if (query.isEmpty) {
        _filtered = _allHits.take(18).toList();
      } else {
        _filtered = _allHits
            .where(
              (h) =>
                  h.title.toLowerCase().contains(query) ||
                  h.subtitle.toLowerCase().contains(query) ||
                  h.subject.codigo.toLowerCase().contains(query),
            )
            .take(24)
            .toList();
      }
      _activeIndex = 0;
    });
  }

  KeyEventResult _handleKey(FocusNode node, KeyEvent event) {
    if (event is! KeyDownEvent) return KeyEventResult.ignored;
    if (event.logicalKey == LogicalKeyboardKey.escape) {
      Navigator.of(context).pop();
      return KeyEventResult.handled;
    }
    if (event.logicalKey == LogicalKeyboardKey.arrowDown &&
        _filtered.isNotEmpty) {
      setState(() => _activeIndex = (_activeIndex + 1) % _filtered.length);
      return KeyEventResult.handled;
    }
    if (event.logicalKey == LogicalKeyboardKey.arrowUp &&
        _filtered.isNotEmpty) {
      setState(
        () => _activeIndex =
            (_activeIndex - 1 + _filtered.length) % _filtered.length,
      );
      return KeyEventResult.handled;
    }
    if (event.logicalKey == LogicalKeyboardKey.enter &&
        _filtered.isNotEmpty) {
      Navigator.of(context).pop(_filtered[_activeIndex]);
      return KeyEventResult.handled;
    }
    return KeyEventResult.ignored;
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    return Center(
      child: Material(
        color: Colors.transparent,
        child: Focus(
          onKeyEvent: _handleKey,
          child: Container(
            width: 620,
            constraints: const BoxConstraints(maxHeight: 480),
            margin: const EdgeInsets.symmetric(horizontal: 24),
            decoration: BoxDecoration(
              color: tokens.isDark
                  ? const Color(0xFF0A0B0E)
                  : const Color(0xFFFFFFFF),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: tokens.border, width: 1.2),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withAlpha(tokens.isDark ? 160 : 35),
                  blurRadius: 40,
                  offset: const Offset(0, 16),
                ),
              ],
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(16, 14, 16, 12),
                  child: Row(
                    children: [
                      Icon(
                        Icons.search_rounded,
                        size: 20,
                        color: tokens.accentGreen,
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: TextField(
                          controller: _ctrl,
                          focusNode: _inputFocus,
                          onChanged: _onQueryChanged,
                          style: TextStyle(
                            fontSize: 14.5,
                            color: tokens.textPrimary,
                          ),
                          decoration: InputDecoration(
                            isDense: true,
                            border: InputBorder.none,
                            hintText:
                                'Buscar asignatura, código, tema oficial o cátedra magistral...',
                            hintStyle: TextStyle(
                              fontSize: 13.5,
                              color: tokens.textSecondary,
                            ),
                          ),
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 7, vertical: 3),
                        decoration: BoxDecoration(
                          color: tokens.surfaceElevated,
                          borderRadius: BorderRadius.circular(6),
                          border: Border.all(color: tokens.border),
                        ),
                        child: Text(
                          'ESC',
                          style: mono(
                            fontSize: 9.5,
                            fontWeight: FontWeight.w700,
                            color: tokens.textTertiary,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                Divider(height: 1, color: tokens.border),
                Flexible(
                  child: _filtered.isEmpty
                      ? Padding(
                          padding: const EdgeInsets.all(28),
                          child: Text(
                            'No se encontraron asignaturas o temas coincidentes.',
                            style: TextStyle(
                              fontSize: 12.5,
                              color: tokens.textSecondary,
                            ),
                          ),
                        )
                      : ListView.builder(
                          shrinkWrap: true,
                          padding: const EdgeInsets.all(8),
                          itemCount: _filtered.length,
                          itemBuilder: (context, i) {
                            final hit = _filtered[i];
                            final selected = i == _activeIndex;
                            final accent = hit.isMagistral
                                ? tokens.accentIndigo
                                : tokens.accentGreen;
                            return TapScale(
                              onTap: () => Navigator.of(context).pop(hit),
                              child: Container(
                                margin: const EdgeInsets.only(bottom: 3),
                                padding: const EdgeInsets.symmetric(
                                    horizontal: 12, vertical: 9),
                                decoration: BoxDecoration(
                                  color: selected
                                      ? accent.o(0.12)
                                      : Colors.transparent,
                                  borderRadius: BorderRadius.circular(11),
                                  border: Border.all(
                                    color: selected
                                        ? accent.o(0.40)
                                        : Colors.transparent,
                                  ),
                                ),
                                child: Row(
                                  children: [
                                    Icon(
                                      hit.temaNumero == null
                                          ? Icons.folder_rounded
                                          : (hit.isMagistral
                                              ? Icons.auto_stories_rounded
                                              : Icons.article_rounded),
                                      size: 16,
                                      color: accent,
                                    ),
                                    const SizedBox(width: 10),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment:
                                            CrossAxisAlignment.start,
                                        children: [
                                          Text(
                                            hit.title,
                                            maxLines: 1,
                                            overflow: TextOverflow.ellipsis,
                                            style: TextStyle(
                                              fontSize: 13,
                                              fontWeight: FontWeight.w600,
                                              color: tokens.textPrimary,
                                            ),
                                          ),
                                          const SizedBox(height: 2),
                                          Text(
                                            hit.subtitle,
                                            maxLines: 1,
                                            overflow: TextOverflow.ellipsis,
                                            style: mono(
                                              fontSize: 10,
                                              color: tokens.textSecondary,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            );
                          },
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
