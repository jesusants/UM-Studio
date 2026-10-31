import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../data/services/download_queue_service.dart';
import '../../domain/entities/tema_estudio_entity.dart';
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

    final effectiveSlides = slides.isNotEmpty
        ? slides
        : [
            SlideDeckItem(
              numero: 1,
              seccion: 'OVERVIEW',
              titulo: tituloTema,
              puntos: const ['Core academic presentation for General English.'],
            ),
          ];

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
                          _latin1('UM STUDIO • Universidad del Magdalena • Plan 8108'),
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

  static pw.Widget _buildPdfTable(List<List<String>> rows) {
    final header = rows.first;
    final bodyRows = rows.length > 1 ? rows.sublist(1) : const <List<String>>[];

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

  /// Normaliza símbolos Unicode fuera de ISO-8859-1 para mantener fuentes
  /// vectoriales Type1 puras (0 KB de fuentes incrustadas, 100% compatible con acentos).
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

/// Visor de Presentaciones Ultraminimalista estilo iOS para los 5 niveles
/// de `Inglés General` (sin KaTeX), con exportación vectorial `< 1.2 MB`
/// conectada a [DownloadQueueService] (máximo 20 descargas simultáneas).
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

  void _goToSlide(int target) {
    if (target < 0 || target >= widget.slides.length) return;
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

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final slides = widget.slides;
    final total = slides.length;

    if (total == 0) {
      return const SizedBox.shrink();
    }

    final safeIndex = _currentSlide.clamp(0, total - 1);
    final canGoBack = safeIndex > 0;
    final canGoForward = safeIndex < total - 1;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Lienzo de la Diapositiva (#121316 oscuro / #F2F2F7 claro, 1px #1F2228, radius 20px)
        Container(
          height: (MediaQuery.sizeOf(context).height * 0.44).clamp(380.0, 500.0),
          decoration: BoxDecoration(
            color: p.card,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: p.cardBorder, width: 1),
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
              final slideNumberText =
                  'SLIDE ${(index + 1).toString().padLeft(2, '0')} / ${total.toString().padLeft(2, '0')}';

              return Padding(
                padding: const EdgeInsets.fromLTRB(18, 16, 18, 16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Cabecera micro-tipográfica
                    Row(
                      children: [
                        Dot(color: p.green, size: 6.5),
                        const SizedBox(width: 7),
                        Text(
                          slideNumberText,
                          style: mono(
                            fontSize: 10.5,
                            fontWeight: FontWeight.w600,
                            letterSpacing: 0.9,
                            color: p.green,
                          ),
                        ),
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
                    const SizedBox(height: 11),

                    // Cuerpo desplazable suave dentro del lienzo (60/120 fps, cero overflow)
                    Expanded(
                      child: SingleChildScrollView(
                        physics: const BouncingScrollPhysics(),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              slide.titulo,
                              softWrap: true,
                              style: TextStyle(
                                fontSize: 18,
                                height: 1.22,
                                fontWeight: FontWeight.w700,
                                letterSpacing: -0.35,
                                color: p.textPrimary,
                              ),
                            ),
                            const SizedBox(height: 12),

                            // Puntos clave con viñetas esmeralda (#30D158)
                            for (final punto in slide.puntos)
                              Padding(
                                padding: const EdgeInsets.only(bottom: 8.5),
                                child: Row(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Padding(
                                      padding: const EdgeInsets.only(
                                        top: 6,
                                        right: 9,
                                      ),
                                      child: Dot(color: p.green, size: 6),
                                    ),
                                    Expanded(
                                      child: Text(
                                        punto,
                                        softWrap: true,
                                        style: TextStyle(
                                          fontSize: 13.2,
                                          height: 1.42,
                                          color: p.textBody,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),

                            // Tabla comparativa compacta
                            if (slide.tabla.isNotEmpty) ...[
                              const SizedBox(height: 4),
                              _CompactSlideTable(rows: slide.tabla),
                            ],

                            // Ejemplo contextualizado
                            if (slide.ejemplo.trim().isNotEmpty) ...[
                              const SizedBox(height: 10),
                              Container(
                                width: double.infinity,
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 12,
                                  vertical: 9,
                                ),
                                decoration: BoxDecoration(
                                  color: p.green.o(0.09),
                                  borderRadius: BorderRadius.circular(12),
                                  border: Border.all(
                                    color: p.green.o(0.32),
                                    width: 1,
                                  ),
                                ),
                                child: Text(
                                  slide.ejemplo,
                                  softWrap: true,
                                  style: TextStyle(
                                    fontSize: 12.2,
                                    height: 1.38,
                                    fontWeight: FontWeight.w500,
                                    color: p.textPrimary,
                                  ),
                                ),
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
            // 1. Botón circular pequeño Atrás (←) 32x32px
            _SlideNavCircleButton(
              key: const Key('slide_prev_button'),
              icon: Icons.chevron_left_rounded,
              enabled: canGoBack,
              onTap: canGoBack ? () => _goToSlide(safeIndex - 1) : null,
            ),
            const SizedBox(width: 10),

            // 2. Indicador central discreto en fuente monoespaciada (2 / 6)
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

            // 3. Botón circular pequeño Adelante (→) 32x32px
            _SlideNavCircleButton(
              key: const Key('slide_next_button'),
              icon: Icons.chevron_right_rounded,
              enabled: canGoForward,
              onTap: canGoForward ? () => _goToSlide(safeIndex + 1) : null,
            ),

            const SizedBox(width: 10),

            // 4. A la derecha: Botón píldora minimalista Descargar (↓ PDF)
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
                        ? p.green.o(0.55)
                        : isErr
                            ? p.orange.o(0.55)
                            : p.cardBorder;
                    final bgColor = isDone
                        ? p.green.o(0.13)
                        : isBusy
                            ? p.elevated
                            : p.card;
                    final textColor = isDone
                        ? p.green
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
