import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../data/services/download_queue_service.dart';
import '../../domain/entities/tema_estudio_entity.dart';
import '../providers/app_scopes.dart';
import 'ios_primitives.dart';

/// Compilador vectorial minimalista de presentaciones PDF (< 1.2 MB con Deflate).
abstract final class SlideDeckPdfCompiler {
  static const PdfColor _bgDark = PdfColor.fromInt(0xFF0B0C0E);
  static const PdfColor _cardDark = PdfColor.fromInt(0xFF121316);
  static const PdfColor _borderDark = PdfColor.fromInt(0xFF1F2228);
  static const PdfColor _emerald = PdfColor.fromInt(0xFF30D158);
  static const PdfColor _emeraldSoft = PdfColor.fromInt(0xFF153220);
  static const PdfColor _textWhite = PdfColor.fromInt(0xFFFFFFFF);
  static const PdfColor _textBody = PdfColor.fromInt(0xFFD6D6DC);
  static const PdfColor _textMuted = PdfColor.fromInt(0xFF8E8E93);
  static const PdfColor _tableHeader = PdfColor.fromInt(0xFF1A1C22);

  /// Compila un conjunto de diapositivas en un PDF vectorial comprimido en memoria
  /// (típicamente 25 KB – 180 KB, muy por debajo del tope de 1.2 MB = 1,258,291 bytes).
  static Future<Uint8List> compile({
    required String codigoAsignatura,
    required String nombreAsignatura,
    required int numeroTema,
    required String tituloTema,
    required List<SlideDeckItem> slides,
  }) async {
    final doc = pw.Document(
      compress: true,
      title: _latin1('$nombreAsignatura - Tema $numeroTema: $tituloTema'),
      author: 'UM STUDIO - Ingenieria Energetica - Unimagdalena',
      creator: 'UM STUDIO iOS Minimalist Slide Engine',
    );

    final effectiveSlides = _sanitizeSlidesForPdf(slides, tituloTema);

    const pageFormat = PdfPageFormat(842, 474, marginAll: 0);
    final total = effectiveSlides.length;

    for (var i = 0; i < total; i++) {
      final slide = effectiveSlides[i];
      final slideIndexLabel =
          'SLIDE ${(i + 1).toString().padLeft(2, '0')} / ${total.toString().padLeft(2, '0')}';

      doc.addPage(
        pw.Page(
          pageFormat: pageFormat,
          build: (context) {
            return pw.Container(
              color: _bgDark,
              padding: const pw.EdgeInsets.all(22),
              child: pw.Container(
                padding: const pw.EdgeInsets.fromLTRB(30, 24, 30, 20),
                decoration: pw.BoxDecoration(
                  color: _cardDark,
                  borderRadius: pw.BorderRadius.circular(18),
                  border: pw.Border.all(color: _borderDark, width: 1.2),
                ),
                child: pw.Column(
                  crossAxisAlignment: pw.CrossAxisAlignment.start,
                  children: [
                    // Cabecera micro-tipográfica
                    pw.Row(
                      mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                      children: [
                        pw.Row(
                          children: [
                            pw.Container(
                              width: 7,
                              height: 7,
                              decoration: const pw.BoxDecoration(
                                color: _emerald,
                                shape: pw.BoxShape.circle,
                              ),
                            ),
                            pw.SizedBox(width: 8),
                            pw.Text(
                              _latin1(
                                '$slideIndexLabel  |  ${slide.seccion.toUpperCase()}',
                              ),
                              style: pw.TextStyle(
                                font: pw.Font.courierBold(),
                                fontSize: 9.5,
                                color: _emerald,
                              ),
                            ),
                          ],
                        ),
                        pw.Text(
                          _latin1(
                            '$nombreAsignatura ($codigoAsignatura) - Topic $numeroTema',
                          ),
                          style: pw.TextStyle(
                            font: pw.Font.courier(),
                            fontSize: 9,
                            color: _textMuted,
                          ),
                        ),
                      ],
                    ),
                    pw.SizedBox(height: 12),

                    // Título principal de alto contraste
                    pw.Text(
                      _latin1(slide.titulo),
                      style: pw.TextStyle(
                        font: pw.Font.helveticaBold(),
                        fontSize: 21,
                        color: _textWhite,
                      ),
                    ),
                    pw.SizedBox(height: 12),

                    // Viñetas esmeralda vectoriales
                    ...slide.puntos.map(
                      (punto) => pw.Padding(
                        padding: const pw.EdgeInsets.only(bottom: 7),
                        child: pw.Row(
                          crossAxisAlignment: pw.CrossAxisAlignment.start,
                          children: [
                            pw.Padding(
                              padding: const pw.EdgeInsets.only(
                                top: 4.5,
                                right: 9,
                              ),
                              child: pw.Container(
                                width: 5.5,
                                height: 5.5,
                                decoration: const pw.BoxDecoration(
                                  color: _emerald,
                                  shape: pw.BoxShape.circle,
                                ),
                              ),
                            ),
                            pw.Expanded(
                              child: pw.Text(
                                _latin1(punto),
                                style: pw.TextStyle(
                                  font: pw.Font.helvetica(),
                                  fontSize: 11.5,
                                  lineSpacing: 2.2,
                                  color: _textBody,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),

                    // Tabla comparativa compacta si existe
                    if (slide.tabla.isNotEmpty) ...[
                      pw.SizedBox(height: 8),
                      _buildPdfTable(slide.tabla),
                    ],

                    pw.Spacer(),

                    // Ejemplo contextualizado
                    if (slide.ejemplo.trim().isNotEmpty) ...[
                      pw.Container(
                        width: double.infinity,
                        padding: const pw.EdgeInsets.symmetric(
                          horizontal: 14,
                          vertical: 9,
                        ),
                        decoration: pw.BoxDecoration(
                          color: _emeraldSoft,
                          borderRadius: pw.BorderRadius.circular(10),
                          border: pw.Border.all(color: _emerald, width: 0.7),
                        ),
                        child: pw.Text(
                          _latin1('Example: ${slide.ejemplo}'),
                          style: pw.TextStyle(
                            font: pw.Font.helveticaOblique(),
                            fontSize: 10.5,
                            color: _textWhite,
                          ),
                        ),
                      ),
                      pw.SizedBox(height: 10),
                    ],

                    // Pie institucional minimalista
                    pw.Row(
                      mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                      children: [
                        pw.Text(
                          _latin1(
                            'UM STUDIO • Universidad del Magdalena • Plan 8108',
                          ),
                          style: pw.TextStyle(
                            font: pw.Font.helvetica(),
                            fontSize: 8.5,
                            color: _textMuted,
                          ),
                        ),
                        pw.Text(
                          '${i + 1} / $total',
                          style: pw.TextStyle(
                            font: pw.Font.courierBold(),
                            fontSize: 9,
                            color: _textMuted,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      );
    }

    final bytes = await doc.save();
    if (bytes.lengthInBytes > DownloadQueueService.maxPdfSizeBytes) {
      throw PdfSizeLimitExceededException(bytes.lengthInBytes);
    }
    return bytes;
  }

  static List<SlideDeckItem> _sanitizeSlidesForPdf(
    List<SlideDeckItem> slides,
    String fallbackTitle,
  ) {
    if (slides.isEmpty) {
      return [
        SlideDeckItem(
          numero: 1,
          seccion: 'OVERVIEW',
          titulo: fallbackTitle,
          puntos: const ['Presentación académica oficial • UM Studio.'],
        ),
      ];
    }

    final result = <SlideDeckItem>[];
    for (var i = 0; i < slides.length; i++) {
      final s = slides[i];
      var cleanTitle = s.titulo.trim();
      while (cleanTitle.startsWith('#')) {
        cleanTitle = cleanTitle.substring(1).trim();
      }
      if (cleanTitle.endsWith('.md')) {
        cleanTitle = cleanTitle.replaceAll('.md', '').replaceAll('_', ' ');
      }
      if (cleanTitle.isEmpty || cleanTitle.toLowerCase().contains('.md')) {
        cleanTitle = i == 0 ? fallbackTitle : 'Contenido ${i + 1}';
      }

      final cleanPuntos = <String>[];
      for (final p in s.puntos) {
        var pt = p.trim();
        while (pt.startsWith('#') ||
            pt.startsWith('* ') ||
            pt.startsWith('- ')) {
          pt = pt.substring(pt.startsWith('#') ? 1 : 2).trim();
        }
        if (pt.endsWith('.md')) continue;
        if (pt.toLowerCase().startsWith('martes,') ||
            pt.toLowerCase().startsWith('lunes,') ||
            pt.toLowerCase().startsWith('miércoles,')) {
          continue;
        }
        if (pt.isNotEmpty) cleanPuntos.add(pt);
      }

      final isJunkHeader = (s.titulo.contains('.md') || s.titulo.startsWith('#')) && cleanPuntos.isEmpty;
      if (isJunkHeader) continue;

      result.add(
        SlideDeckItem(
          numero: result.length + 1,
          seccion: s.seccion,
          titulo: cleanTitle,
          puntos: cleanPuntos.isNotEmpty
              ? cleanPuntos
              : const ['Notas de cátedra magistral.'],
          tabla: s.tabla,
          ejemplo: s.ejemplo,
        ),
      );
    }

    return result.isNotEmpty
        ? result
        : [
            SlideDeckItem(
              numero: 1,
              seccion: 'OVERVIEW',
              titulo: fallbackTitle,
              puntos: const ['Presentación académica oficial • UM Studio.'],
            ),
          ];
  }

  static pw.Widget _buildPdfTable(List<List<String>> rows) {
    final header = rows.first;
    final bodyRows =
        rows.length > 1 ? rows.sublist(1) : const <List<String>>[];

    return pw.Table(
      border: pw.TableBorder.all(color: _borderDark, width: 0.8),
      children: [
        pw.TableRow(
          decoration: const pw.BoxDecoration(color: _tableHeader),
          children: [
            for (final cell in header)
              pw.Padding(
                padding: const pw.EdgeInsets.symmetric(
                  horizontal: 8,
                  vertical: 5,
                ),
                child: pw.Text(
                  _latin1(cell),
                  style: pw.TextStyle(
                    font: pw.Font.helveticaBold(),
                    fontSize: 9.5,
                    color: _emerald,
                  ),
                ),
              ),
          ],
        ),
        for (final row in bodyRows)
          pw.TableRow(
            children: [
              for (var c = 0; c < header.length; c++)
                pw.Padding(
                  padding: const pw.EdgeInsets.symmetric(
                    horizontal: 8,
                    vertical: 4.5,
                  ),
                  child: pw.Text(
                    _latin1(c < row.length ? row[c] : ''),
                    style: pw.TextStyle(
                      font: pw.Font.helvetica(),
                      fontSize: 9.5,
                      color: _textBody,
                    ),
                  ),
                ),
            ],
          ),
      ],
    );
  }

  static String _latin1(String raw) {
    final normalized = raw
        .replaceAll('→', '->')
        .replaceAll('←', '<-')
        .replaceAll('↔', '<->')
        .replaceAll('⇒', '=>')
        .replaceAll('•', '-')
        .replaceAll('—', '-')
        .replaceAll('–', '-')
        .replaceAll('“', '"')
        .replaceAll('”', '"')
        .replaceAll('‘', "'")
        .replaceAll('’', "'")
        .replaceAll('…', '...')
        .replaceAll('✓', 'OK')
        .replaceAll('✗', 'X')
        .replaceAll('×', 'x')
        .replaceAll('≠', '!=')
        .replaceAll('≤', '<=')
        .replaceAll('≥', '>=');

    final buffer = StringBuffer();
    for (final rune in normalized.runes) {
      if (rune <= 0xFF) {
        buffer.writeCharCode(rune);
      } else {
        buffer.write(' ');
      }
    }
    return buffer.toString();
  }
}

/// Visor de Presentaciones Ultraminimalista estilo Apple Keynote (Dark OLED / Light Mode)
/// para asignaturas y Clases Magistrales con renderizado mixto (Texto, KaTeX, Callout Boxes).
class MinimalSlideViewer extends StatefulWidget {
  const MinimalSlideViewer({
    super.key,
    required this.temaId,
    required this.codigoAsignatura,
    required this.nombreAsignatura,
    required this.numeroTema,
    required this.tituloTema,
    required this.slides,
    this.queueService,
  });

  final String temaId;
  final String codigoAsignatura;
  final String nombreAsignatura;
  final int numeroTema;
  final String tituloTema;
  final List<SlideDeckItem> slides;
  final DownloadQueueService? queueService;

  @override
  State<MinimalSlideViewer> createState() => _MinimalSlideViewerState();
}

class _MinimalSlideViewerState extends State<MinimalSlideViewer> {
  late final PageController _pageController;
  int _currentSlide = 0;

  DownloadQueueService get _queue =>
      widget.queueService ?? DownloadQueueService.instance;

  String get _downloadTaskId =>
      'slide_${widget.codigoAsignatura}_t${widget.numeroTema}';

  String get _pdfFileName =>
      'UM_Studio_${widget.codigoAsignatura}_Topic_${widget.numeroTema}.pdf';

  @override
  void initState() {
    super.initState();
    _pageController = PageController();
  }

  @override
  void didUpdateWidget(covariant MinimalSlideViewer oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.temaId != widget.temaId ||
        oldWidget.numeroTema != widget.numeroTema) {
      _currentSlide = 0;
      if (_pageController.hasClients) {
        _pageController.jumpToPage(0);
      }
    }
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  void _goToSlide(int target, int total) {
    if (target < 0 || target >= total) return;
    HapticFeedback.lightImpact();
    setState(() => _currentSlide = target);
    if (_pageController.hasClients) {
      _pageController.animateToPage(
        target,
        duration: const Duration(milliseconds: 260),
        curve: kIosSpring,
      );
    }
  }

  Future<void> _handleDownloadPdf() async {
    HapticFeedback.lightImpact();
    try {
      final bytes = await _queue.enqueueDownload(
        taskId: _downloadTaskId,
        fileName: _pdfFileName,
        generator: () => SlideDeckPdfCompiler.compile(
          codigoAsignatura: widget.codigoAsignatura,
          nombreAsignatura: widget.nombreAsignatura,
          numeroTema: widget.numeroTema,
          tituloTema: widget.tituloTema,
          slides: widget.slides,
        ),
      );
      if (mounted) {
        final formattedSize =
            InstitutionalValidator.formatByteSize(bytes.lengthInBytes);
        showIosToast(
          context,
          'Presentación PDF lista ($formattedSize • <1.2 MB)',
          accentColor: context.palette.green,
        );
      }
    } on PdfSizeLimitExceededException {
      if (mounted) {
        showIosToast(
          context,
          'El PDF supera el límite estricto de 1.2 MB.',
          accentColor: context.palette.orange,
        );
      }
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'No se pudo exportar la presentación PDF.',
          accentColor: context.palette.orange,
        );
      }
    }
  }

  List<SlideDeckItem> _getSanitizedSlides() {
    if (widget.slides.isEmpty) {
      return [
        SlideDeckItem(
          numero: 1,
          seccion: 'CÁTEDRA',
          titulo: widget.tituloTema,
          puntos: const ['Cátedra magistral oficial • UM Studio.'],
        ),
      ];
    }

    final List<SlideDeckItem> cleaned = [];
    for (var i = 0; i < widget.slides.length; i++) {
      final s = widget.slides[i];
      var rawTitle = s.titulo.trim();
      while (rawTitle.startsWith('#')) {
        rawTitle = rawTitle.substring(1).trim();
      }
      if (rawTitle.endsWith('.md')) {
        rawTitle = rawTitle.replaceAll('.md', '').replaceAll('_', ' ').trim();
      }

      final cleanPuntos = <String>[];
      for (final p in s.puntos) {
        var pt = p.trim();
        while (pt.startsWith('#') ||
            pt.startsWith('* ') ||
            pt.startsWith('- ')) {
          pt = pt.substring(pt.startsWith('#') ? 1 : 2).trim();
        }
        if (pt.endsWith('.md')) continue;
        if (pt.toLowerCase().startsWith('martes,') ||
            pt.toLowerCase().startsWith('lunes,') ||
            pt.toLowerCase().startsWith('miércoles,')) {
          continue;
        }
        if (pt.isNotEmpty) cleanPuntos.add(pt);
      }

      final isJunkHeader = (s.titulo.contains('.md') || s.titulo.startsWith('#')) && cleanPuntos.isEmpty;
      if (isJunkHeader) continue;

      var finalTitle = rawTitle;
      if (cleaned.isEmpty &&
          (finalTitle.isEmpty ||
              finalTitle.toLowerCase().contains('.md') ||
              finalTitle.length < 3)) {
        finalTitle = widget.tituloTema;
      }

      cleaned.add(
        SlideDeckItem(
          numero: cleaned.length + 1,
          seccion: s.seccion,
          titulo: finalTitle.isNotEmpty
              ? finalTitle
              : (i == 0 ? widget.tituloTema : 'Contenido ${cleaned.length + 1}'),
          puntos: cleanPuntos.isNotEmpty
              ? cleanPuntos
              : const ['Fundamento conceptual de cátedra magistral.'],
          tabla: s.tabla,
          ejemplo: s.ejemplo,
        ),
      );
    }

    return cleaned.isNotEmpty
        ? cleaned
        : [
            SlideDeckItem(
              numero: 1,
              seccion: 'CÁTEDRA',
              titulo: widget.tituloTema,
              puntos: const ['Cátedra magistral oficial • UM Studio.'],
            ),
          ];
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);
    final slides = _getSanitizedSlides();
    final total = slides.length;

    final safeIndex = _currentSlide.clamp(0, total - 1);
    final canGoBack = safeIndex > 0;
    final canGoForward = safeIndex < total - 1;
    final isMagistral = widget.temaId.contains('_magistral_');
    final accent = isMagistral ? p.indigo : p.green;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Lienzo de la Diapositiva (Keynote Dark OLED / Light Mode)
        Container(
          height:
              (MediaQuery.sizeOf(context).height * 0.44).clamp(380.0, 500.0),
          decoration: BoxDecoration(
            color: p.card,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: p.cardBorder, width: 1),
            boxShadow: [
              BoxShadow(
                color: isDark
                    ? Colors.black.o(0.55)
                    : Colors.black.o(0.04),
                blurRadius: 16,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          clipBehavior: Clip.antiAlias,
          child: PageView.builder(
            controller: _pageController,
            physics: const BouncingScrollPhysics(),
            itemCount: total,
            onPageChanged: (index) {
              if (_currentSlide != index) {
                setState(() => _currentSlide = index);
              }
            },
            itemBuilder: (context, index) {
              final slide = slides[index];
              final isCover = index == 0 && isMagistral;

              return Padding(
                padding: const EdgeInsets.fromLTRB(18, 16, 18, 16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Cabecera superior micro-tipográfica (cero overflow)
                    Row(
                      children: [
                        if (isCover) ...[
                          Icon(
                            Icons.school_rounded,
                            size: 14,
                            color: accent,
                          ),
                          const SizedBox(width: 6),
                          Flexible(
                            child: Text(
                              'CÁTEDRA • ${widget.codigoAsignatura}',
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: mono(
                                fontSize: 10,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 0.8,
                                color: accent,
                              ),
                            ),
                          ),
                        ] else ...[
                          Dot(color: accent, size: 6.5),
                          const SizedBox(width: 7),
                          Text(
                            'SLIDE ${(index + 1).toString().padLeft(2, '0')} / ${total.toString().padLeft(2, '0')}',
                            maxLines: 1,
                            style: mono(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w600,
                              letterSpacing: 0.9,
                              color: accent,
                            ),
                          ),
                        ],
                        const SizedBox(width: 8),
                        Expanded(
                          child: Align(
                            alignment: Alignment.centerRight,
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 8,
                                vertical: 2.5,
                              ),
                              decoration: BoxDecoration(
                                color: p.elevated,
                                borderRadius: BorderRadius.circular(6),
                                border: Border.all(color: p.cardBorder),
                              ),
                              child: Text(
                                slide.seccion.toUpperCase(),
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: mono(
                                  fontSize: 9.5,
                                  fontWeight: FontWeight.w600,
                                  color: p.textSecondary,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 12),

                    // Cuerpo desplazable de la lámina
                    Expanded(
                      child: SingleChildScrollView(
                        physics: const BouncingScrollPhysics(),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            // Título de la diapositiva
                            Text(
                              slide.titulo,
                              softWrap: true,
                              style: TextStyle(
                                fontSize: isCover ? 21.5 : 18.5,
                                height: 1.22,
                                fontWeight: FontWeight.w800,
                                letterSpacing: -0.4,
                                color: p.textPrimary,
                              ),
                            ),
                            const SizedBox(height: 14),

                            // Puntos y bloques de la diapositiva
                            for (var pIdx = 0; pIdx < slide.puntos.length; pIdx++) ...[
                              _buildPointItem(
                                context,
                                slide.puntos[pIdx],
                                pIdx + 1,
                                accent,
                                isDark,
                              ),
                              const SizedBox(height: 8.5),
                            ],

                            // Tabla comparativa si existe
                            if (slide.tabla.isNotEmpty) ...[
                              const SizedBox(height: 4),
                              _CompactSlideTable(rows: slide.tabla),
                              const SizedBox(height: 10),
                            ],

                            // Ejemplo contextualizado al pie de la slide
                            if (slide.ejemplo.trim().isNotEmpty) ...[
                              const SizedBox(height: 8),
                              _buildSlideFooterNote(
                                context,
                                slide.ejemplo,
                                accent,
                                isDark,
                              ),
                            ],
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              );
            },
          ),
        ),
        const SizedBox(height: 10),

        // Barra de Controles Ultraminimalista (Pie del Visor)
        Row(
          children: [
            _SlideNavCircleButton(
              key: const Key('slide_prev_button'),
              icon: Icons.chevron_left_rounded,
              enabled: canGoBack,
              onTap: canGoBack ? () => _goToSlide(safeIndex - 1, total) : null,
            ),
            const SizedBox(width: 10),

            Text(
              '${safeIndex + 1} / $total',
              key: const Key('slide_counter_label'),
              style: mono(
                fontSize: 12,
                fontWeight: FontWeight.w600,
                color: p.textSecondary,
              ),
            ),
            const SizedBox(width: 10),

            _SlideNavCircleButton(
              key: const Key('slide_next_button'),
              icon: Icons.chevron_right_rounded,
              enabled: canGoForward,
              onTap: canGoForward ? () => _goToSlide(safeIndex + 1, total) : null,
            ),

            const SizedBox(width: 10),

            // Botón de exportación PDF
            Expanded(
              child: Align(
                alignment: Alignment.centerRight,
                child: FittedBox(
                  fit: BoxFit.scaleDown,
                  child: ListenableBuilder(
                    listenable: _queue,
                    builder: (context, _) {
                      final snap = _queue.stateFor(_downloadTaskId);
                      final isDone = snap.phase == DownloadTaskPhase.completed;
                      final isBusy = snap.phase == DownloadTaskPhase.queued ||
                          snap.phase == DownloadTaskPhase.downloading;
                      final isErr = snap.phase == DownloadTaskPhase.error;

                      final borderColor = isDone
                          ? accent.o(0.55)
                          : isErr
                              ? p.orange.o(0.55)
                              : p.cardBorder;
                      final bgColor = isDone
                          ? accent.o(0.13)
                          : isBusy
                              ? p.elevated
                              : p.card;
                      final textColor = isDone
                          ? accent
                          : isErr
                              ? p.orange
                              : p.textPrimary;

                      return TapScale(
                        onTap: isBusy ? null : _handleDownloadPdf,
                        child: AnimatedContainer(
                          key: const Key('slide_download_pdf_button'),
                          duration: const Duration(milliseconds: 180),
                          padding: const EdgeInsets.symmetric(
                            horizontal: 13,
                            vertical: 7,
                          ),
                          decoration: BoxDecoration(
                            color: bgColor,
                            borderRadius: BorderRadius.circular(999),
                            border: Border.all(color: borderColor, width: 1),
                          ),
                          child: Text(
                            snap.buttonLabel,
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: textColor,
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildPointItem(
    BuildContext context,
    String punto,
    int index,
    Color accent,
    bool isDark,
  ) {
    final trimmed = punto.trim();

    // Si el punto es una ecuación de visualización completa ($$ ... $$)
    if (trimmed.startsWith(r'$$') && trimmed.endsWith(r'$$')) {
      final latex = trimmed.substring(2, trimmed.length - 2).trim();
      return _FormulaCalloutBox(
        latex: latex,
        accentColor: accent,
        isDark: isDark,
      );
    }

    // Puntos normales con numeración estilizada y soporte KaTeX / Bold
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          margin: const EdgeInsets.only(top: 3.5, right: 10),
          padding: const EdgeInsets.symmetric(horizontal: 5.5, vertical: 2),
          decoration: BoxDecoration(
            color: accent.o(0.13),
            borderRadius: BorderRadius.circular(6),
          ),
          child: Text(
            index.toString().padLeft(2, '0'),
            style: mono(
              fontSize: 9,
              fontWeight: FontWeight.w700,
              color: accent,
            ),
          ),
        ),
        Expanded(
          child: _SlideRichText(
            text: trimmed,
            textColor: isDark ? const Color(0xFFE5E5EA) : const Color(0xFF1C1C1E),
            fontSize: 14.5,
            height: 1.55,
            accentColor: accent,
          ),
        ),
      ],
    );
  }

  Widget _buildSlideFooterNote(
    BuildContext context,
    String ejemplo,
    Color accent,
    bool isDark,
  ) {
    final p = context.palette;

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 13, vertical: 10),
      decoration: BoxDecoration(
        color: accent.o(0.08),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: accent.o(0.3), width: 1),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.lightbulb_outline_rounded, size: 14, color: accent),
              const SizedBox(width: 5),
              Text(
                'NOTA DE APLICACIÓN',
                style: mono(
                  fontSize: 9,
                  fontWeight: FontWeight.w700,
                  color: accent,
                ),
              ),
            ],
          ),
          const SizedBox(height: 5),
          _SlideRichText(
            text: ejemplo,
            textColor: p.textPrimary,
            fontSize: 12.8,
            height: 1.45,
            accentColor: accent,
          ),
        ],
      ),
    );
  }
}

/// Caja destacada para fórmulas KaTeX dentro de diapositivas (Formula Callout Box)
class _FormulaCalloutBox extends StatelessWidget {
  const _FormulaCalloutBox({
    required this.latex,
    required this.accentColor,
    required this.isDark,
  });

  final String latex;
  final Color accentColor;
  final bool isDark;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final clean = InstitutionalValidator.sanitizeLatex(latex);

    return Container(
      width: double.infinity,
      margin: const EdgeInsets.symmetric(vertical: 4),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF11131A) : const Color(0xFFF2F4F8),
        borderRadius: BorderRadius.circular(10),
        border: Border(
          left: BorderSide(color: accentColor, width: 3.5),
          top: BorderSide(
            color: isDark ? const Color(0xFF1F2228) : const Color(0xFFE2E4E9),
          ),
          right: BorderSide(
            color: isDark ? const Color(0xFF1F2228) : const Color(0xFFE2E4E9),
          ),
          bottom: BorderSide(
            color: isDark ? const Color(0xFF1F2228) : const Color(0xFFE2E4E9),
          ),
        ),
      ),
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        child: Math.tex(
          clean,
          mathStyle: MathStyle.display,
          textStyle: TextStyle(
            fontSize: 14.5,
            color: isDark ? Colors.white : p.textPrimary,
          ),
          onErrorFallback: (_) => Text(
            clean,
            style: mono(fontSize: 12.5, color: p.textPrimary),
          ),
        ),
      ),
    );
  }
}

/// Renderizador de texto mixto: maneja negritas `**...**` y expresiones KaTeX inline `$ ... $`.
class _SlideRichText extends StatelessWidget {
  const _SlideRichText({
    required this.text,
    required this.textColor,
    this.fontSize = 14.5,
    this.height = 1.55,
    this.accentColor,
  });

  final String text;
  final Color textColor;
  final double fontSize;
  final double height;
  final Color? accentColor;

  @override
  Widget build(BuildContext context) {
    final tokens = _tokenize(text);
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);
    final spans = <InlineSpan>[];

    for (final token in tokens) {
      if (token.type == _SlideTokenType.inlineMath) {
        final cleanTex = InstitutionalValidator.sanitizeLatex(token.content);
        spans.add(
          WidgetSpan(
            alignment: PlaceholderAlignment.middle,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 2.5),
              child: Math.tex(
                cleanTex,
                mathStyle: MathStyle.text,
                textStyle: TextStyle(
                  fontSize: fontSize,
                  color: isDark ? Colors.white : Colors.black,
                ),
                onErrorFallback: (_) => Text(
                  cleanTex,
                  style: mono(fontSize: fontSize - 1, color: textColor),
                ),
              ),
            ),
          ),
        );
      } else if (token.type == _SlideTokenType.bold) {
        spans.add(
          TextSpan(
            text: token.content,
            style: TextStyle(
              fontSize: fontSize,
              height: height,
              fontWeight: FontWeight.w700,
              color: isDark ? Colors.white : Colors.black,
            ),
          ),
        );
      } else {
        spans.add(
          TextSpan(
            text: token.content,
            style: TextStyle(
              fontSize: fontSize,
              height: height,
              color: textColor,
            ),
          ),
        );
      }
    }

    return Text.rich(
      TextSpan(children: spans),
      softWrap: true,
    );
  }

  List<_SlideToken> _tokenize(String raw) {
    final pattern = RegExp(
      r'(\$\$.*?\$\$|\$.*?\$|\*\*.*?\*\*)',
      dotAll: true,
    );

    final List<_SlideToken> tokens = [];
    int lastEnd = 0;

    for (final match in pattern.allMatches(raw)) {
      if (match.start > lastEnd) {
        tokens.add(
          _SlideToken(
            type: _SlideTokenType.text,
            content: raw.substring(lastEnd, match.start),
          ),
        );
      }

      final val = match.group(0)!;
      if (val.startsWith(r'$$') && val.endsWith(r'$$')) {
        tokens.add(
          _SlideToken(
            type: _SlideTokenType.inlineMath,
            content: val.substring(2, val.length - 2).trim(),
          ),
        );
      } else if (val.startsWith(r'$') && val.endsWith(r'$')) {
        tokens.add(
          _SlideToken(
            type: _SlideTokenType.inlineMath,
            content: val.substring(1, val.length - 1).trim(),
          ),
        );
      } else if (val.startsWith(r'**') && val.endsWith(r'**')) {
        tokens.add(
          _SlideToken(
            type: _SlideTokenType.bold,
            content: val.substring(2, val.length - 2),
          ),
        );
      }

      lastEnd = match.end;
    }

    if (lastEnd < raw.length) {
      tokens.add(
        _SlideToken(
          type: _SlideTokenType.text,
          content: raw.substring(lastEnd),
        ),
      );
    }

    return tokens;
  }
}

enum _SlideTokenType { text, bold, inlineMath }

class _SlideToken {
  const _SlideToken({
    required this.type,
    required this.content,
  });

  final _SlideTokenType type;
  final String content;
}

class _SlideNavCircleButton extends StatelessWidget {
  const _SlideNavCircleButton({
    super.key,
    required this.icon,
    required this.enabled,
    this.onTap,
  });

  final IconData icon;
  final bool enabled;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return TapScale(
      onTap: onTap,
      child: AnimatedOpacity(
        duration: const Duration(milliseconds: 150),
        opacity: enabled ? 1.0 : 0.36,
        child: Container(
          width: 32,
          height: 32,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: p.card,
            shape: BoxShape.circle,
            border: Border.all(color: p.cardBorder, width: 1),
          ),
          child: Icon(
            icon,
            size: 18,
            color: p.textPrimary,
          ),
        ),
      ),
    );
  }
}

class _CompactSlideTable extends StatelessWidget {
  const _CompactSlideTable({required this.rows});

  final List<List<String>> rows;

  @override
  Widget build(BuildContext context) {
    if (rows.isEmpty) return const SizedBox.shrink();
    final p = context.palette;
    final header = rows.first;
    final body = rows.length > 1 ? rows.sublist(1) : const <List<String>>[];
    final colCount = header.length;

    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(11),
        border: Border.all(color: p.cardBorder, width: 1),
      ),
      clipBehavior: Clip.antiAlias,
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        child: ConstrainedBox(
          constraints: BoxConstraints(
            minWidth: math.max(280.0, colCount * 95.0),
          ),
          child: Table(
            defaultColumnWidth: const IntrinsicColumnWidth(),
            border: TableBorder(
              horizontalInside: BorderSide(color: p.cardBorder, width: 1),
              verticalInside: BorderSide(color: p.cardBorder, width: 1),
            ),
            children: [
              TableRow(
                decoration: BoxDecoration(color: p.green.o(0.12)),
                children: [
                  for (final cell in header)
                    Padding(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 7,
                      ),
                      child: Text(
                        cell,
                        softWrap: true,
                        style: mono(
                          fontSize: 10.5,
                          fontWeight: FontWeight.w700,
                          color: p.green,
                        ),
                      ),
                    ),
                ],
              ),
              for (final r in body)
                TableRow(
                  children: [
                    for (var i = 0; i < colCount; i++)
                      Padding(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 10,
                          vertical: 7,
                        ),
                        child: Text(
                          i < r.length ? r[i] : '',
                          softWrap: true,
                          style: TextStyle(
                            fontSize: 11.5,
                            height: 1.35,
                            color: p.textBody,
                          ),
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
