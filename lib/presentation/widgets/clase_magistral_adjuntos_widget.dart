import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/theme/app_theme.dart';
import '../../domain/entities/nota_adjunto_entity.dart';
import '../providers/app_scopes.dart';
import '../screens/clase_viva/attachment_viewer_page.dart';
import 'ios_primitives.dart';

/// Módulo interactivo de Mis Apuntes y Archivos Adjuntos para Clases Magistrales.
/// Permite al estudiante adjuntar fotos de tablero/cuaderno, documentos (PDFs, guías, talleres)
/// y notas personales, con persistencia local y sincronización con GitHub.
class ClaseMagistralAdjuntosWidget extends StatefulWidget {
  const ClaseMagistralAdjuntosWidget({
    super.key,
    required this.temaKey,
    required this.tituloClase,
    required this.accentColor,
    this.isDesktop = false,
  });

  final String temaKey;
  final String tituloClase;
  final Color accentColor;
  final bool isDesktop;

  @override
  State<ClaseMagistralAdjuntosWidget> createState() =>
      _ClaseMagistralAdjuntosWidgetState();
}

class _ClaseMagistralAdjuntosWidgetState
    extends State<ClaseMagistralAdjuntosWidget> {
  bool _uploading = false;
  String? _uploadingLabel;
  final TextEditingController _notaController = TextEditingController();
  bool _showingNotaInput = false;

  @override
  void dispose() {
    _notaController.dispose();
    super.dispose();
  }

  Future<void> _subirFotoTablero() async {
    if (_uploading) return;
    try {
      final picked = await FilePicker.pickFile(
        dialogTitle: 'Seleccionar foto de tablero o cuaderno',
        type: FileType.image,
      );
      if (picked == null) return;

      setState(() {
        _uploading = true;
        _uploadingLabel = 'Guardando ${picked.name}...';
      });

      final bytes = await picked.readAsBytes();
      if (!mounted) return;

      await ClaseVivaRepositoryScope.of(context).subirArchivoAdjunto(
        temaId: widget.temaKey,
        tipoArchivo: TipoAdjuntoEstudiante.imagen,
        nombreArchivo: picked.name,
        bytes: bytes,
      );
      HapticFeedback.lightImpact();
      if (mounted) {
        showIosToast(
          context,
          'Foto de clase vinculada correctamente.',
          accentColor: widget.accentColor,
        );
      }
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'No se pudo adjuntar la imagen seleccionada.',
          accentColor: context.palette.orange,
        );
      }
    } finally {
      if (mounted) {
        setState(() {
          _uploading = false;
          _uploadingLabel = null;
        });
      }
    }
  }

  Future<void> _subirDocumento() async {
    if (_uploading) return;
    try {
      final picked = await FilePicker.pickFile(
        dialogTitle: 'Seleccionar documento de estudio (PDF, Guía o Taller)',
        type: FileType.custom,
        allowedExtensions: const ['pdf', 'md', 'doc', 'docx', 'txt'],
      );
      if (picked == null) return;

      setState(() {
        _uploading = true;
        _uploadingLabel = 'Guardando ${picked.name}...';
      });

      final bytes = await picked.readAsBytes();
      if (!mounted) return;

      const tipo = TipoAdjuntoEstudiante.pdf;

      await ClaseVivaRepositoryScope.of(context).subirArchivoAdjunto(
        temaId: widget.temaKey,
        tipoArchivo: tipo,
        nombreArchivo: picked.name,
        bytes: bytes,
      );
      HapticFeedback.lightImpact();
      if (mounted) {
        showIosToast(
          context,
          'Documento adjuntado correctamente.',
          accentColor: widget.accentColor,
        );
      }
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'No se pudo adjuntar el documento.',
          accentColor: context.palette.orange,
        );
      }
    } finally {
      if (mounted) {
        setState(() {
          _uploading = false;
          _uploadingLabel = null;
        });
      }
    }
  }

  Future<void> _guardarNotaTexto() async {
    final text = _notaController.text.trim();
    if (text.isEmpty) return;
    try {
      await ClaseVivaRepositoryScope.of(context).guardarNotaPersonal(
        temaId: widget.temaKey,
        contenido: text,
      );
      _notaController.clear();
      setState(() => _showingNotaInput = false);
      HapticFeedback.lightImpact();
      if (mounted) {
        showIosToast(
          context,
          'Apunte guardado y sincronizado.',
          accentColor: widget.accentColor,
        );
      }
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'Error al guardar el apunte.',
          accentColor: context.palette.orange,
        );
      }
    }
  }

  void _abrirVisor(NotaAdjuntoEntity adjunto) {
    Navigator.of(context).push(
      AttachmentViewerPage.route(
        adjunto: adjunto,
        onDelete: () async {
          HapticFeedback.lightImpact();
          await ClaseVivaRepositoryScope.of(context)
              .eliminarAdjunto(adjunto: adjunto);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final repo = ClaseVivaRepositoryScope.of(context);

    return StreamBuilder<List<NotaAdjuntoEntity>>(
      stream: repo.watchNotasYAdjuntos(temaId: widget.temaKey),
      builder: (context, snapshot) {
        final adjuntos = snapshot.data ?? const <NotaAdjuntoEntity>[];
        final imagenes = adjuntos
            .where((a) => a.tipoArchivo == TipoAdjuntoEstudiante.imagen)
            .toList();
        final documentos = adjuntos
            .where((a) =>
                a.tipoArchivo != TipoAdjuntoEstudiante.imagen &&
                a.tipoArchivo != TipoAdjuntoEstudiante.nota)
            .toList();
        final notas = adjuntos
            .where((a) => a.tipoArchivo == TipoAdjuntoEstudiante.nota)
            .toList();

        return Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: p.card,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: widget.accentColor.o(0.25), width: 1),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              // Barra de título con estado de archivos
              Row(
                children: [
                  Icon(
                    Icons.folder_special_outlined,
                    size: 16,
                    color: widget.accentColor,
                  ),
                  const SizedBox(width: 6),
                  Expanded(
                    child: Text(
                      'MIS APUNTES Y ADJUNTOS DE CLASE',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: mono(
                        fontSize: 10,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 0.8,
                        color: widget.accentColor,
                      ),
                    ),
                  ),
                  if (adjuntos.isNotEmpty)
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 7,
                        vertical: 2,
                      ),
                      decoration: BoxDecoration(
                        color: widget.accentColor.o(0.12),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        '${adjuntos.length} ${adjuntos.length == 1 ? 'archivo' : 'archivos'}',
                        style: mono(
                          fontSize: 9.5,
                          fontWeight: FontWeight.w700,
                          color: widget.accentColor,
                        ),
                      ),
                    ),
                ],
              ),
              const SizedBox(height: 10),

              // Botones de acción rápida: Foto, Documento, Nota
              Wrap(
                spacing: 8,
                runSpacing: 6,
                children: [
                  TapScale(
                    onTap: _subirFotoTablero,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 5.5,
                      ),
                      decoration: BoxDecoration(
                        color: p.elevated,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.camera_alt_outlined,
                            size: 13,
                            color: widget.accentColor,
                          ),
                          const SizedBox(width: 5),
                          Text(
                            'Foto Tablero',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: p.textPrimary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  TapScale(
                    onTap: _subirDocumento,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 5.5,
                      ),
                      decoration: BoxDecoration(
                        color: p.elevated,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.upload_file_outlined,
                            size: 13,
                            color: p.indigo,
                          ),
                          const SizedBox(width: 5),
                          Text(
                            'Adjuntar PDF/Guía',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: p.textPrimary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  TapScale(
                    onTap: () => setState(
                      () => _showingNotaInput = !_showingNotaInput,
                    ),
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 5.5,
                      ),
                      decoration: BoxDecoration(
                        color: _showingNotaInput ? p.elevated : p.card,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(
                          color: _showingNotaInput
                              ? widget.accentColor
                              : p.cardBorder,
                        ),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.edit_note_rounded,
                            size: 14,
                            color: p.green,
                          ),
                          const SizedBox(width: 4),
                          Text(
                            'Escribir Apunte',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: p.textPrimary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),

              // Indicador de subida
              if (_uploading) ...[
                const SizedBox(height: 10),
                Row(
                  children: [
                    SizedBox(
                      width: 13,
                      height: 13,
                      child: CircularProgressIndicator(
                        strokeWidth: 2,
                        valueColor: AlwaysStoppedAnimation(widget.accentColor),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Text(
                      _uploadingLabel ?? 'Procesando archivo...',
                      style: TextStyle(
                        fontSize: 11,
                        color: widget.accentColor,
                        fontStyle: FontStyle.italic,
                      ),
                    ),
                  ],
                ),
              ],

              // Campo de texto para nuevo apunte
              if (_showingNotaInput) ...[
                const SizedBox(height: 10),
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: p.elevated,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: p.cardBorder),
                  ),
                  child: Column(
                    children: [
                      TextField(
                        controller: _notaController,
                        maxLines: 3,
                        style: TextStyle(fontSize: 12, color: p.textPrimary),
                        decoration: InputDecoration(
                          hintText:
                              'Escribe aquí fórmulas, observaciones del profesor o apuntes...',
                          hintStyle: TextStyle(
                            fontSize: 11.5,
                            color: p.textTertiary,
                          ),
                          border: InputBorder.none,
                          isDense: true,
                        ),
                      ),
                      const SizedBox(height: 6),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.end,
                        children: [
                          TextButton(
                            onPressed: () =>
                                setState(() => _showingNotaInput = false),
                            child: Text(
                              'Cancelar',
                              style: TextStyle(
                                fontSize: 11,
                                color: p.textSecondary,
                              ),
                            ),
                          ),
                          const SizedBox(width: 4),
                          TapScale(
                            onTap: _guardarNotaTexto,
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 12,
                                vertical: 5,
                              ),
                              decoration: BoxDecoration(
                                color: widget.accentColor,
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: const Text(
                                'Guardar Apunte',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w700,
                                  color: Colors.white,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],

              // Galería de Imágenes (Fotos de Tablero)
              if (imagenes.isNotEmpty) ...[
                const SizedBox(height: 12),
                Text(
                  'Fotos de Tablero y Cuaderno (${imagenes.length})',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: p.textSecondary,
                  ),
                ),
                const SizedBox(height: 6),
                SizedBox(
                  height: 72,
                  child: ListView.separated(
                    scrollDirection: Axis.horizontal,
                    physics: const BouncingScrollPhysics(),
                    itemCount: imagenes.length,
                    separatorBuilder: (_, __) => const SizedBox(width: 8),
                    itemBuilder: (context, idx) {
                      final item = imagenes[idx];
                      return TapScale(
                        onTap: () => _abrirVisor(item),
                        child: Container(
                          width: 84,
                          decoration: BoxDecoration(
                            color: p.elevated,
                            borderRadius: BorderRadius.circular(10),
                            border: Border.all(
                              color: widget.accentColor.o(0.3),
                            ),
                          ),
                          clipBehavior: Clip.antiAlias,
                          child: Stack(
                            fit: StackFit.expand,
                            children: [
                              if (item.localBytes != null)
                                Image.memory(
                                  item.localBytes!,
                                  fit: BoxFit.cover,
                                )
                              else
                                Center(
                                  child: Icon(
                                    Icons.image_outlined,
                                    size: 24,
                                    color: widget.accentColor,
                                  ),
                                ),
                              Positioned(
                                bottom: 0,
                                left: 0,
                                right: 0,
                                child: Container(
                                  color: Colors.black.o(0.65),
                                  padding: const EdgeInsets.symmetric(
                                    horizontal: 4,
                                    vertical: 2,
                                  ),
                                  child: Text(
                                    item.nombreArchivo ?? 'Foto',
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: const TextStyle(
                                      fontSize: 8.5,
                                      color: Colors.white,
                                    ),
                                  ),
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

              // Lista de Documentos Adjuntos (PDFs / Guías)
              if (documentos.isNotEmpty) ...[
                const SizedBox(height: 10),
                Text(
                  'Documentos y Guías (${documentos.length})',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: p.textSecondary,
                  ),
                ),
                const SizedBox(height: 6),
                for (final doc in documentos)
                  Padding(
                    padding: const EdgeInsets.only(bottom: 6),
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: p.elevated,
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        children: [
                          Icon(
                            doc.tipoArchivo == TipoAdjuntoEstudiante.pdf
                                ? Icons.picture_as_pdf_rounded
                                : Icons.description_rounded,
                            size: 16,
                            color: doc.tipoArchivo == TipoAdjuntoEstudiante.pdf
                                ? Colors.redAccent
                                : p.indigo,
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  doc.nombreArchivo ?? 'Documento',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(
                                    fontSize: 11,
                                    fontWeight: FontWeight.w600,
                                    color: p.textPrimary,
                                  ),
                                ),
                                Text(
                                  doc.pesoFormateado,
                                  style: mono(
                                    fontSize: 8.5,
                                    color: p.textTertiary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          TapScale(
                            onTap: () => _abrirVisor(doc),
                            child: Padding(
                              padding: const EdgeInsets.all(4),
                              child: Icon(
                                Icons.open_in_new_rounded,
                                size: 14,
                                color: widget.accentColor,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
              ],

              // Lista de Notas Personales
              if (notas.isNotEmpty) ...[
                const SizedBox(height: 8),
                Text(
                  'Apuntes del Estudiante (${notas.length})',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: p.textSecondary,
                  ),
                ),
                const SizedBox(height: 6),
                for (final n in notas)
                  Container(
                    margin: const EdgeInsets.only(bottom: 6),
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: widget.accentColor.o(0.06),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: widget.accentColor.o(0.2)),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(
                          Icons.sticky_note_2_outlined,
                          size: 14,
                          color: widget.accentColor,
                        ),
                        const SizedBox(width: 6),
                        Expanded(
                          child: Text(
                            n.contenidoNota ?? '',
                            style: TextStyle(
                              fontSize: 11,
                              color: p.textPrimary,
                              height: 1.3,
                            ),
                          ),
                        ),
                        TapScale(
                          onTap: () async {
                            HapticFeedback.lightImpact();
                            await repo.eliminarAdjunto(adjunto: n);
                          },
                          child: Icon(
                            Icons.close_rounded,
                            size: 13,
                            color: p.textTertiary,
                          ),
                        ),
                      ],
                    ),
                  ),
              ],

              // Estado vacío si no hay archivos aún
              if (adjuntos.isEmpty && !_showingNotaInput) ...[
                const SizedBox(height: 4),
                Text(
                  'Aún no has agregado fotos de tablero ni apuntes a esta cátedra. Pulsa los botones superiores para adjuntar material.',
                  style: TextStyle(
                    fontSize: 10.5,
                    color: p.textTertiary,
                    fontStyle: FontStyle.italic,
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
