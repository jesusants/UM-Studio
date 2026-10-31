import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../../core/theme/app_theme.dart';
import '../../../domain/entities/nota_adjunto_entity.dart';
import '../../widgets/ios_primitives.dart';

/// Visor a pantalla completa estilo iOS OLED para archivos vinculados
/// (Imágenes de Tablero con zoom interactivo y documentos PDF).
class AttachmentViewerPage extends StatelessWidget {
  const AttachmentViewerPage({
    super.key,
    required this.adjunto,
    required this.onDelete,
  });

  final NotaAdjuntoEntity adjunto;
  final VoidCallback onDelete;

  static Route<void> route({
    required NotaAdjuntoEntity adjunto,
    required VoidCallback onDelete,
  }) {
    return PageRouteBuilder<void>(
      opaque: true,
      transitionDuration: const Duration(milliseconds: 260),
      reverseTransitionDuration: const Duration(milliseconds: 220),
      pageBuilder: (_, __, ___) => AttachmentViewerPage(
        adjunto: adjunto,
        onDelete: onDelete,
      ),
      transitionsBuilder: (_, animation, __, child) {
        final curved = CurvedAnimation(parent: animation, curve: kIosSpring);
        return FadeTransition(
          opacity: curved,
          child: ScaleTransition(
            scale: Tween<double>(begin: 0.96, end: 1.0).animate(curved),
            child: child,
          ),
        );
      },
    );
  }

  Future<void> _openExternalUrl(BuildContext context) async {
    final rawUrl = adjunto.urlArchivo;
    if (rawUrl == null || rawUrl.isEmpty) return;
    final uri = Uri.tryParse(rawUrl);
    if (uri == null) return;

    if (rawUrl.contains('storage.unimagdalena.edu.co')) {
      showIosToast(
        context,
        'Archivo sincronizado en almacenamiento local (${adjunto.pesoFormateado}).',
        accentColor: context.palette.indigo,
      );
      return;
    }

    await launchUrl(uri, mode: LaunchMode.externalApplication);
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isImage = adjunto.tipoArchivo == TipoAdjuntoEstudiante.imagen;
    final title = adjunto.nombreArchivo ??
        (isImage ? 'Foto de Tablero' : 'Documento PDF');

    return Scaffold(
      backgroundColor: p.background,
      body: SafeArea(
        child: Column(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                color: p.background,
                border: Border(bottom: BorderSide(color: p.cardBorder)),
              ),
              child: Row(
                children: [
                  TapScale(
                    onTap: () => Navigator.of(context).pop(),
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.chevron_left_rounded,
                            size: 18,
                            color: p.textSecondary,
                          ),
                          const SizedBox(width: 2),
                          Text(
                            'Cerrar',
                            style: TextStyle(
                              fontSize: 13,
                              color: p.textSecondary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      children: [
                        Text(
                          title,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 13.5,
                            fontWeight: FontWeight.w600,
                            color: p.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 2),
                        Text(
                          '${adjunto.tipoArchivo.dbValue.toUpperCase()} • ${adjunto.pesoFormateado}',
                          style: mono(fontSize: 10, color: p.textSecondary),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 12),
                  TapScale(
                    onTap: () {
                      Navigator.of(context).pop();
                      onDelete();
                    },
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Icon(
                        Icons.delete_outline_rounded,
                        size: 17,
                        color: p.textSecondary,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              child: isImage
                  ? _buildImageCanvas(context, p)
                  : _buildPdfInspector(context, p, title),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildImageCanvas(BuildContext context, AppPalette p) {
    final bytes = adjunto.localBytes;
    final url = adjunto.urlArchivo;

    Widget imageWidget;
    if (bytes != null && bytes.isNotEmpty) {
      imageWidget = Image.memory(
        bytes,
        fit: BoxFit.contain,
        filterQuality: FilterQuality.high,
      );
    } else if (url != null &&
        url.isNotEmpty &&
        !url.contains('storage.unimagdalena.edu.co')) {
      imageWidget = Image.network(
        url,
        fit: BoxFit.contain,
        errorBuilder: (_, __, ___) => _missingPreviewPlaceholder(p, true),
      );
    } else {
      imageWidget = _missingPreviewPlaceholder(p, true);
    }

    return Stack(
      children: [
        Positioned.fill(
          child: InteractiveViewer(
            minScale: 0.8,
            maxScale: 5.0,
            boundaryMargin: const EdgeInsets.all(32),
            child: Center(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(16),
                  child: imageWidget,
                ),
              ),
            ),
          ),
        ),
        Positioned(
          left: 0,
          right: 0,
          bottom: 20,
          child: Center(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
              decoration: BoxDecoration(
                color: p.card.o(0.9),
                borderRadius: BorderRadius.circular(999),
                border: Border.all(color: p.cardBorder),
              ),
              child: Text(
                'Pellizca o desplaza para inspeccionar el tablero',
                style: TextStyle(fontSize: 11, color: p.textSecondary),
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildPdfInspector(
    BuildContext context,
    AppPalette p,
    String title,
  ) {
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 390),
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: IosCard(
            radius: 22,
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 56,
                  height: 56,
                  decoration: BoxDecoration(
                    color: p.indigo.o(0.12),
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: p.indigo.o(0.35)),
                  ),
                  child: Icon(
                    Icons.picture_as_pdf_outlined,
                    size: 28,
                    color: p.indigo,
                  ),
                ),
                const SizedBox(height: 16),
                Text(
                  title,
                  textAlign: TextAlign.center,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  'Documento PDF • ${adjunto.pesoFormateado}',
                  style: mono(fontSize: 11.5, color: p.textSecondary),
                ),
                const SizedBox(height: 16),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: p.elevated,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: p.cardBorder),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('ENLACE DE BUCKET', style: sectionMicroStyle(p)),
                      const SizedBox(height: 4),
                      Text(
                        adjunto.urlArchivo ?? 'Repositorio local sincronizado',
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: mono(fontSize: 10.5, color: p.textBody),
                      ),
                    ],
                  ),
                ),
                if (adjunto.urlArchivo != null) ...[
                  const SizedBox(height: 18),
                  TapScale(
                    onTap: () => _openExternalUrl(context),
                    child: Container(
                      width: double.infinity,
                      padding: const EdgeInsets.symmetric(vertical: 12),
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: p.indigo,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.open_in_new_rounded,
                            size: 15,
                            color: Colors.white,
                          ),
                          SizedBox(width: 8),
                          Text(
                            'Abrir documento completo',
                            style: TextStyle(
                              fontSize: 12.5,
                              fontWeight: FontWeight.w600,
                              color: Colors.white,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _missingPreviewPlaceholder(AppPalette p, bool isImage) {
    return Container(
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            isImage ? Icons.image_outlined : Icons.description_outlined,
            size: 36,
            color: p.textSecondary,
          ),
          const SizedBox(height: 10),
          Text(
            adjunto.nombreArchivo ?? 'Archivo adjunto',
            style: TextStyle(
              fontSize: 13,
              fontWeight: FontWeight.w600,
              color: p.textPrimary,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            adjunto.pesoFormateado,
            style: mono(fontSize: 11, color: p.textSecondary),
          ),
        ],
      ),
    );
  }
}
