import 'dart:async';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/models/curriculum_models.dart';
import '../../../domain/entities/nota_adjunto_entity.dart';
import '../../../domain/entities/subject_summary.dart';
import '../../../domain/entities/tema_estudio_entity.dart';
import '../../../domain/repositories/i_clase_viva_repository.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';
import '../../widgets/katex_formula_card.dart';
import '../../widgets/reminder_creator_sheet.dart';
import 'attachment_viewer_page.dart';

/// Pantalla de detalle dinámico de asignatura ("La Clase Viva" & Adjuntos).
class ClaseVivaPage extends StatefulWidget {
  const ClaseVivaPage({
    super.key,
    required this.temaId,
  });

  final String temaId;

  static Route<void> route(String subjectId) {
    return PageRouteBuilder<void>(
      transitionDuration: const Duration(milliseconds: 280),
      reverseTransitionDuration: const Duration(milliseconds: 260),
      pageBuilder: (_, __, ___) => ClaseVivaPage(temaId: subjectId),
      transitionsBuilder: (_, animation, __, child) {
        final curved = CurvedAnimation(
          parent: animation,
          curve: kIosSpring,
          reverseCurve: kIosSpring.flipped,
        );
        return SlideTransition(
          position: Tween<Offset>(
            begin: const Offset(0, 1),
            end: Offset.zero,
          ).animate(curved),
          child: FadeTransition(
            opacity: CurvedAnimation(parent: animation, curve: Curves.ease),
            child: child,
          ),
        );
      },
    );
  }

  @override
  State<ClaseVivaPage> createState() => _ClaseVivaPageState();
}

class _ClaseVivaPageState extends State<ClaseVivaPage> {
  Stream<TemaEstudioEntity>? _temaStream;
  Stream<List<NotaAdjuntoEntity>>? _adjuntosStream;
  IClaseVivaRepository? _boundRepo;
  String? _boundUser;
  late String _activeTemaKey;

  bool _uploading = false;
  String? _uploadingLabel;
  bool _recordedInitialReview = false;

  @override
  void initState() {
    super.initState();
    _activeTemaKey = widget.temaId;
  }

  void _recordCurrentTopicAsReviewed() {
    if (!mounted) return;
    final session = SessionScope.maybeOf(context);
    if (session == null) return;
    final asig =
        CurriculumScope.maybeOf(context)?.database?.findAsignatura(_activeTemaKey);
    if (asig == null) return;
    var topicNum = 1;
    if (_activeTemaKey.contains('_t')) {
      topicNum = int.tryParse(_activeTemaKey.split('_t').last) ?? 1;
    }
    session.markTopicReviewed(
      codigoMateria: asig.codigo,
      numeroTema: topicNum,
    );
  }

  void _rebindStreams() {
    final repo = ClaseVivaRepositoryScope.of(context);
    final currentUser = repo.activeUserId;
    _boundRepo = repo;
    _boundUser = currentUser;
    _temaStream = repo.watchTemaEstudio(_activeTemaKey);
    _adjuntosStream = repo.watchNotasYAdjuntos(
      temaId: _activeTemaKey,
      usuarioId: currentUser,
    );
  }

  void _selectTopicNumber(AsignaturaModel asignatura, int topicNum) {
    final nextKey = topicNum <= 1
        ? asignatura.codigo
        : '${asignatura.codigo}_t$topicNum';
    SessionScope.maybeOf(context)?.markTopicReviewed(
      codigoMateria: asignatura.codigo,
      numeroTema: topicNum,
    );
    if (nextKey == _activeTemaKey) return;
    HapticFeedback.lightImpact();
    setState(() {
      _activeTemaKey = nextKey;
      _rebindStreams();
    });
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final repo = ClaseVivaRepositoryScope.of(context);
    final currentUser = repo.activeUserId;
    if (_boundRepo != repo || _boundUser != currentUser) {
      _rebindStreams();
    }
    if (!_recordedInitialReview) {
      _recordedInitialReview = true;
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _recordCurrentTopicAsReviewed();
      });
    }
  }

  Future<void> _adjuntarPdf() async {
    if (_uploading) return;
    try {
      final picked = await FilePicker.pickFile(
        dialogTitle: 'Seleccionar documento PDF de estudio',
        type: FileType.custom,
        allowedExtensions: const ['pdf'],
      );
      if (picked == null) return;

      setState(() {
        _uploading = true;
        _uploadingLabel = 'Subiendo ${picked.name}...';
      });

      final bytes = await picked.readAsBytes();
      if (!mounted) return;
      await ClaseVivaRepositoryScope.of(context).subirArchivoAdjunto(
        temaId: _activeTemaKey,
        tipoArchivo: TipoAdjuntoEstudiante.pdf,
        nombreArchivo: picked.name,
        bytes: bytes,
      );
      HapticFeedback.lightImpact();
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'No se pudo adjuntar el documento PDF.',
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

  Future<void> _capturarFotoTablero() async {
    if (_uploading) return;
    final p = context.palette;

    final bool supportsCameraSheet = kIsWeb ||
        defaultTargetPlatform == TargetPlatform.iOS ||
        defaultTargetPlatform == TargetPlatform.android;

    if (!supportsCameraSheet) {
      await _pickImageFromDevice();
      return;
    }

    final choice = await showModalBottomSheet<String>(
      context: context,
      backgroundColor: p.card,
      shape: RoundedRectangleBorder(
        borderRadius: const BorderRadius.vertical(top: Radius.circular(22)),
        side: BorderSide(color: p.cardBorder),
      ),
      builder: (sheetCtx) {
        return SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 36,
                  height: 4,
                  decoration: BoxDecoration(
                    color: p.strongBorder,
                    borderRadius: BorderRadius.circular(4),
                  ),
                ),
                const SizedBox(height: 14),
                Text('CAPTURA DE TABLERO', style: sectionMicroStyle(p)),
                const SizedBox(height: 12),
                _SheetOptionTile(
                  icon: Icons.camera_alt_outlined,
                  accent: p.green,
                  title: 'Tomar foto con cámara',
                  subtitle: 'Captura directa del tablero en el aula',
                  onTap: () => Navigator.of(sheetCtx).pop('camera'),
                ),
                const SizedBox(height: 8),
                _SheetOptionTile(
                  icon: Icons.photo_library_outlined,
                  accent: p.indigo,
                  title: 'Elegir imagen existente',
                  subtitle: 'Importar apunte o captura desde galería',
                  onTap: () => Navigator.of(sheetCtx).pop('gallery'),
                ),
              ],
            ),
          ),
        );
      },
    );

    if (!mounted || choice == null) return;
    if (choice == 'camera') {
      await _pickImageWithCameraFallback();
    } else {
      await _pickImageFromDevice();
    }
  }

  Future<void> _pickImageWithCameraFallback() async {
    try {
      final picker = ImagePicker();
      final XFile? photo = await picker.pickImage(
        source: ImageSource.camera,
        imageQuality: 88,
      );
      if (photo == null) return;
      final bytes = await photo.readAsBytes();
      final name = photo.name.isNotEmpty
          ? photo.name
          : 'tablero_${DateTime.now().millisecondsSinceEpoch}.jpg';
      await _uploadImageBytes(name, bytes);
    } catch (_) {
      await _pickImageFromDevice();
    }
  }

  Future<void> _pickImageFromDevice() async {
    try {
      final picked = await FilePicker.pickFile(
        dialogTitle: 'Seleccionar foto de tablero',
        type: FileType.image,
      );
      if (picked == null) return;
      final bytes = await picked.readAsBytes();
      await _uploadImageBytes(picked.name, bytes);
    } catch (_) {
      if (mounted) {
        showIosToast(
          context,
          'No se pudo cargar la imagen seleccionada.',
          accentColor: context.palette.orange,
        );
      }
    }
  }

  Future<void> _uploadImageBytes(String fileName, Uint8List bytes) async {
    if (!mounted) return;
    setState(() {
      _uploading = true;
      _uploadingLabel = 'Guardando $fileName...';
    });
    try {
      await ClaseVivaRepositoryScope.of(context).subirArchivoAdjunto(
        temaId: _activeTemaKey,
        tipoArchivo: TipoAdjuntoEstudiante.imagen,
        nombreArchivo: fileName,
        bytes: bytes,
      );
      HapticFeedback.lightImpact();
    } finally {
      if (mounted) {
        setState(() {
          _uploading = false;
          _uploadingLabel = null;
        });
      }
    }
  }

  Future<void> _eliminarAdjunto(NotaAdjuntoEntity adjunto) async {
    HapticFeedback.lightImpact();
    await ClaseVivaRepositoryScope.of(context)
        .eliminarAdjunto(adjunto: adjunto);
  }

  void _abrirVisorAdjunto(NotaAdjuntoEntity adjunto) {
    Navigator.of(context).push(
      AttachmentViewerPage.route(
        adjunto: adjunto,
        onDelete: () => _eliminarAdjunto(adjunto),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.of(context).isDark;

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: isDark ? SystemUiOverlayStyle.light : SystemUiOverlayStyle.dark,
      child: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Scaffold(
          backgroundColor: p.background,
          body: SafeArea(
            bottom: false,
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(
                  maxWidth: AppConstants.maxPhoneViewportWidth,
                ),
                child: Column(
                  children: [
                    // A. Barra Superior de Navegación (Persistent Top Bar)
                    const _PersistentTopBar(),

                    // Cuerpo desplazable a 60/120fps
                    Expanded(
                      child: StreamBuilder<TemaEstudioEntity>(
                        stream: _temaStream,
                        builder: (context, temaSnap) {
                          final isLoading =
                              temaSnap.connectionState ==
                                      ConnectionState.waiting &&
                                  !temaSnap.hasData;
                          final tema = temaSnap.data;
                          final syncPct = tema?.sincronizacionPorcentaje ?? 94;

                          return ListView(
                            physics: const BouncingScrollPhysics(
                              parent: AlwaysScrollableScrollPhysics(),
                            ),
                            padding: const EdgeInsets.fromLTRB(16, 14, 16, 48),
                            children: [
                              // B. Píldora de Estado del Aula
                              _AulaStatusPill(percentage: syncPct),
                              const SizedBox(height: 18),

                              // Transición entre Shimmer (#1A1D24) y Tarjetas Oficiales
                              AnimatedSwitcher(
                                duration: const Duration(milliseconds: 260),
                                switchInCurve: Curves.easeOut,
                                switchOutCurve: Curves.easeIn,
                                child: isLoading || tema == null
                                    ? const _ClaseVivaShimmerSkeleton(
                                        key: ValueKey('shimmer_skeleton'),
                                      )
                                    : _OfficialTopicSection(
                                        key: ValueKey('topic_${tema.id}'),
                                        tema: tema,
                                        asignatura: CurriculumScope.maybeOf(
                                          context,
                                        )?.database?.findAsignatura(
                                          widget.temaId,
                                        ),
                                        onSelectTopic: _selectTopicNumber,
                                      ),
                              ),

                              const SizedBox(height: 24),

                              // E. Módulo de Estudio Individual: "Mis Apuntes y Archivos"
                              StreamBuilder<List<NotaAdjuntoEntity>>(
                                stream: _adjuntosStream,
                                builder: (context, adjSnap) {
                                  final records = adjSnap.data ?? const [];
                                  final archivos = records
                                      .where((r) => r.esArchivo)
                                      .toList();
                                  NotaAdjuntoEntity? notaRecord;
                                  for (final r in records) {
                                    if (r.tipoArchivo ==
                                        TipoAdjuntoEstudiante.nota) {
                                      notaRecord = r;
                                      break;
                                    }
                                  }

                                  return _IndividualStudyModule(
                                    temaId: _activeTemaKey,
                                    archivos: archivos,
                                    initialNoteText:
                                        notaRecord?.contenidoNota ?? '',
                                    uploading: _uploading,
                                    uploadingLabel: _uploadingLabel,
                                    onAttachPdf: _adjuntarPdf,
                                    onCaptureBoard: _capturarFotoTablero,
                                    onViewAttachment: _abrirVisorAdjunto,
                                    onDeleteAttachment: _eliminarAdjunto,
                                  );
                                },
                              ),
                            ],
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

/// A. Barra Superior Persistente (Persistent Top Bar).
class _PersistentTopBar extends StatelessWidget {
  const _PersistentTopBar();

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return Container(
      padding: const EdgeInsets.fromLTRB(16, 10, 16, 12),
      decoration: BoxDecoration(
        color: p.background,
        border: Border(bottom: BorderSide(color: p.cardBorder, width: 1)),
      ),
      child: Row(
        children: [
          Expanded(
            child: Align(
              alignment: Alignment.centerLeft,
              child: TapScale(
                onTap: () => Navigator.of(context).pop(),
                child: Padding(
                  padding: const EdgeInsets.symmetric(vertical: 2),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(
                        Icons.chevron_left_rounded,
                        size: 21,
                        color: p.textSecondary,
                      ),
                      Text(
                        'Temario',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w400,
                          letterSpacing: -0.1,
                          color: p.textSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
          Text(
            AppConstants.appTitle,
            style: TextStyle(
              fontSize: 15,
              fontWeight: FontWeight.w600,
              letterSpacing: 0.7,
              color: p.textPrimary,
            ),
          ),
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Dot(color: p.green, size: 7),
                const SizedBox(width: 6),
                Flexible(
                  child: Text(
                    AppConstants.universityName,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                      color: p.textSecondary,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// B. Píldora de Estado del Aula (`borderRadius: 16px`, fondo `#121316`, borde `#1F2228`).
class _AulaStatusPill extends StatelessWidget {
  const _AulaStatusPill({required this.percentage});

  final int percentage;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: p.cardBorder, width: 1),
      ),
      child: Row(
        children: [
          PulseDot(color: p.green, size: 8),
          const SizedBox(width: 9),
          Expanded(
            child: Text(
              'SINCRONIZADO CON AULA',
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 10,
                letterSpacing: 1.4,
                fontWeight: FontWeight.w600,
                color: p.textSecondary,
              ),
            ),
          ),
          const SizedBox(width: 8),
          Text(
            'Live • $percentage%',
            style: TextStyle(
              fontSize: 11,
              fontWeight: FontWeight.w700,
              letterSpacing: 0.2,
              color: p.green,
            ),
          ),
        ],
      ),
    );
  }
}

/// C & D. Encabezado Dinámico + Selector de Temas + Tarjetas Modulares Oficiales.
class _OfficialTopicSection extends StatelessWidget {
  const _OfficialTopicSection({
    super.key,
    required this.tema,
    this.asignatura,
    this.onSelectTopic,
  });

  final TemaEstudioEntity tema;
  final AsignaturaModel? asignatura;
  final void Function(AsignaturaModel asignatura, int topicNum)? onSelectTopic;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final asig = asignatura;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // C. Encabezado Dinámico de Asignatura
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    tema.codigoAsignatura.isNotEmpty
                        ? 'ASIGNATURA • ${tema.codigoAsignatura} • C${tema.cuatrimestre}'
                        : 'ASIGNATURA',
                    style: mono(
                      fontSize: 10,
                      fontWeight: FontWeight.w500,
                      letterSpacing: 1.1,
                      color: p.textSecondary,
                    ),
                  ),
                  const SizedBox(height: 5),
                  Text(
                    tema.nombreAsignatura,
                    style: TextStyle(
                      fontSize: 22,
                      height: 1.18,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.45,
                      color: p.textPrimary,
                    ),
                  ),
                  if (tema.tituloTema.isNotEmpty) ...[
                    const SizedBox(height: 4),
                    Text(
                      tema.tituloTema,
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w500,
                        color: p.green,
                      ),
                    ),
                  ],
                ],
              ),
            ),
            const SizedBox(width: 12),
            Container(
              margin: const EdgeInsets.only(top: 14),
              padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 5),
              decoration: BoxDecoration(
                color: p.green.o(0.10),
                borderRadius: BorderRadius.circular(999),
                border: Border.all(color: p.green, width: 1),
              ),
              child: Text(
                tema.badgeTema,
                style: mono(
                  fontSize: 11,
                  fontWeight: FontWeight.w600,
                  color: p.green,
                ),
              ),
            ),
          ],
        ),

        // Selector horizontal de Temas si la asignatura tiene múltiples temas en el .md
        if (asig != null && asig.temas.length > 1 && onSelectTopic != null) ...[
          const SizedBox(height: 12),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            physics: const BouncingScrollPhysics(),
            child: Row(
              children: [
                for (final t in asig.temas)
                  Padding(
                    padding: const EdgeInsets.only(right: 8),
                    child: TapScale(
                      onTap: () => onSelectTopic!(asig, t.numeroTema),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        padding: const EdgeInsets.symmetric(
                          horizontal: 12,
                          vertical: 6,
                        ),
                        decoration: BoxDecoration(
                          color: t.numeroTema == tema.numeroTema
                              ? p.green
                              : p.card,
                          borderRadius: BorderRadius.circular(999),
                          border: Border.all(
                            color: t.numeroTema == tema.numeroTema
                                ? p.green
                                : p.cardBorder,
                          ),
                        ),
                        child: Text(
                          'Tema ${t.numeroTema}: ${t.titulo}',
                          style: TextStyle(
                            fontSize: 11.5,
                            fontWeight: FontWeight.w600,
                            color: t.numeroTema == tema.numeroTema
                                ? Colors.black
                                : p.textSecondary,
                          ),
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ],

        const SizedBox(height: 18),

        // D.1 Tarjeta Modular: OBJETIVO (radius: 18px)
        _ContentModularCard(
          label: 'OBJETIVO',
          body: tema.objetivo,
        ),
        const SizedBox(height: 12),

        // D.2 Tarjeta Modular: CONCEPTO CLAVE (KaTeX Nativo)
        KatexFormulaCard(
          latex: tema.conceptoClaveLatex,
          label: 'CONCEPTO CLAVE',
        ),
        const SizedBox(height: 12),

        // D.3 Tarjeta Modular: EJEMPLO DE CÁTEDRA (radius: 18px)
        _ContentModularCard(
          label: 'EJEMPLO DE CÁTEDRA',
          body: tema.ejemplo,
        ),

        // D.4 Tarjeta Modular: BLOQUE DE ESTUDIO SUGERIDO (conectado a Calendario y Progreso)
        if (tema.bloqueSugerido.isNotEmpty) ...[
          const SizedBox(height: 12),
          IosCard(
            radius: 18,
            padding: const EdgeInsets.all(15),
            borderColor: p.indigo.o(0.38),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Dot(color: p.indigo, size: 7),
                    const SizedBox(width: 7),
                    Expanded(
                      child: Text(
                        'BLOQUE SUGERIDO',
                        style: sectionMicroStyle(p),
                      ),
                    ),
                    if (tema.codigoAsignatura.isNotEmpty && session != null)
                      Text(
                        'Avance: ${session.subjectProgress(tema.codigoAsignatura)}%',
                        style: mono(
                          fontSize: 10.5,
                          fontWeight: FontWeight.w600,
                          color: p.green,
                        ),
                      ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  tema.bloqueSugerido,
                  style: TextStyle(
                    fontSize: 13.5,
                    height: 1.4,
                    color: p.textBody,
                  ),
                ),
                if (session != null) ...[
                  const SizedBox(height: 12),
                  Row(
                    children: [
                      Expanded(
                        child: TapScale(
                          onTap: () async {
                            HapticFeedback.lightImpact();
                            await session.completeStudyBlock(
                              codigoMateria: tema.codigoAsignatura,
                            );
                            if (context.mounted) {
                              showIosToast(
                                context,
                                '+10% de avance en ${tema.nombreAsignatura}',
                                accentColor: p.green,
                              );
                            }
                          },
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 9),
                            alignment: Alignment.center,
                            decoration: BoxDecoration(
                              color: p.indigo,
                              borderRadius: BorderRadius.circular(11),
                            ),
                            child: const Text(
                              'Completar bloque (+10%)',
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.w600,
                                color: Colors.white,
                              ),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),
                      TapScale(
                        onTap: () => showReminderCreatorSheet(
                          context,
                          initialKind: AcademicEventKind.bloque,
                          preselectedSubject: asig,
                        ),
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 12,
                            vertical: 9,
                          ),
                          decoration: BoxDecoration(
                            color: p.elevated,
                            borderRadius: BorderRadius.circular(11),
                            border: Border.all(color: p.cardBorder),
                          ),
                          child: Text(
                            '+ Agendar',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                              color: p.textPrimary,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ],
            ),
          ),
        ],
      ],
    );
  }
}

class _ContentModularCard extends StatelessWidget {
  const _ContentModularCard({
    required this.label,
    required this.body,
  });

  final String label;
  final String body;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return IosCard(
      radius: 18,
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label, style: sectionMicroStyle(p)),
          const SizedBox(height: 8),
          Text(
            body,
            style: TextStyle(
              fontSize: 14,
              height: 1.48,
              letterSpacing: -0.1,
              color: p.textBody,
            ),
          ),
        ],
      ),
    );
  }
}

/// Esqueleto de carga Shimmer en tonos `#1A1D24` respetando la silueta exacta
/// del encabezado y las 3 tarjetas modulares de 18px.
class _ClaseVivaShimmerSkeleton extends StatelessWidget {
  const _ClaseVivaShimmerSkeleton({super.key});

  @override
  Widget build(BuildContext context) {
    return const IosShimmer(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    ShimmerBlock(height: 10, width: 78, radius: 4),
                    SizedBox(height: 8),
                    ShimmerBlock(height: 22, width: 250, radius: 6),
                    SizedBox(height: 6),
                    ShimmerBlock(height: 22, width: 170, radius: 6),
                  ],
                ),
              ),
              SizedBox(width: 12),
              ShimmerBlock(height: 26, width: 66, radius: 999),
            ],
          ),
          SizedBox(height: 18),
          IosCard(
            radius: 18,
            padding: EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ShimmerBlock(height: 10, width: 64, radius: 4),
                SizedBox(height: 12),
                ShimmerBlock(height: 13, radius: 5),
                SizedBox(height: 8),
                ShimmerBlock(height: 13, width: 290, radius: 5),
              ],
            ),
          ),
          SizedBox(height: 12),
          IosCard(
            radius: 18,
            padding: EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    ShimmerBlock(height: 10, width: 96, radius: 4),
                    ShimmerBlock(height: 18, width: 52, radius: 6),
                  ],
                ),
                SizedBox(height: 12),
                ShimmerBlock(height: 58, radius: 14),
              ],
            ),
          ),
          SizedBox(height: 12),
          IosCard(
            radius: 18,
            padding: EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ShimmerBlock(height: 10, width: 118, radius: 4),
                SizedBox(height: 12),
                ShimmerBlock(height: 13, radius: 5),
                SizedBox(height: 8),
                ShimmerBlock(height: 13, radius: 5),
                SizedBox(height: 8),
                ShimmerBlock(height: 13, width: 220, radius: 5),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// E. Módulo de Estudio Individual: "Mis Apuntes y Archivos".
class _IndividualStudyModule extends StatelessWidget {
  const _IndividualStudyModule({
    required this.temaId,
    required this.archivos,
    required this.initialNoteText,
    required this.uploading,
    required this.uploadingLabel,
    required this.onAttachPdf,
    required this.onCaptureBoard,
    required this.onViewAttachment,
    required this.onDeleteAttachment,
  });

  final String temaId;
  final List<NotaAdjuntoEntity> archivos;
  final String initialNoteText;
  final bool uploading;
  final String? uploadingLabel;
  final VoidCallback onAttachPdf;
  final VoidCallback onCaptureBoard;
  final ValueChanged<NotaAdjuntoEntity> onViewAttachment;
  final ValueChanged<NotaAdjuntoEntity> onDeleteAttachment;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Text('MIS APUNTES Y ARCHIVOS', style: sectionMicroStyle(p)),
            const Spacer(),
            if (archivos.isNotEmpty)
              Text(
                '${archivos.length} ${archivos.length == 1 ? 'archivo' : 'archivos'}',
                style: mono(fontSize: 10, color: p.textSecondary),
              ),
          ],
        ),
        const SizedBox(height: 10),

        // Fila de Acciones Rápidas (2 botones con bordes sutiles y radio de 12px)
        Row(
          children: [
            Expanded(
              child: _QuickActionButton(
                icon: Icons.description_outlined,
                accentColor: p.indigo,
                label: 'Adjuntar PDF',
                onTap: uploading ? null : onAttachPdf,
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: _QuickActionButton(
                icon: Icons.camera_alt_outlined,
                accentColor: p.green,
                label: 'Foto Tablero',
                onTap: uploading ? null : onCaptureBoard,
              ),
            ),
          ],
        ),

        if (uploading && uploadingLabel != null) ...[
          const SizedBox(height: 10),
          IosShimmer(
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
              decoration: BoxDecoration(
                color: p.shimmerBase,
                borderRadius: BorderRadius.circular(12),
              ),
              child: Text(
                uploadingLabel!,
                style: mono(fontSize: 11, color: p.textSecondary),
              ),
            ),
          ),
        ],

        if (archivos.isNotEmpty) ...[
          const SizedBox(height: 12),
          for (var i = 0; i < archivos.length; i++) ...[
            if (i > 0) const SizedBox(height: 8),
            _AttachmentRowItem(
              adjunto: archivos[i],
              onView: () => onViewAttachment(archivos[i]),
              onDelete: () => onDeleteAttachment(archivos[i]),
            ),
          ],
        ],

        const SizedBox(height: 12),

        _PersonalNotesCollapsibleCard(
          key: ValueKey('notes_${temaId}_card'),
          temaId: temaId,
          syncedText: initialNoteText,
        ),
      ],
    );
  }
}

class _QuickActionButton extends StatelessWidget {
  const _QuickActionButton({
    required this.icon,
    required this.accentColor,
    required this.label,
    required this.onTap,
  });

  final IconData icon;
  final Color accentColor;
  final String label;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return TapScale(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 11),
        decoration: BoxDecoration(
          color: p.card,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: p.cardBorder, width: 1),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 17, color: accentColor),
            const SizedBox(width: 8),
            Flexible(
              child: Text(
                label,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w600,
                  letterSpacing: -0.1,
                  color: p.textPrimary,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _AttachmentRowItem extends StatelessWidget {
  const _AttachmentRowItem({
    required this.adjunto,
    required this.onView,
    required this.onDelete,
  });

  final NotaAdjuntoEntity adjunto;
  final VoidCallback onView;
  final VoidCallback onDelete;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isPdf = adjunto.tipoArchivo == TipoAdjuntoEstudiante.pdf;
    final accent = isPdf ? p.indigo : p.green;
    final icon = isPdf
        ? Icons.picture_as_pdf_outlined
        : Icons.image_outlined;
    final displayName =
        adjunto.nombreArchivo ?? (isPdf ? 'Documento.pdf' : 'Tablero.jpg');

    return TapScale(
      onTap: onView,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          color: p.card,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: p.cardBorder, width: 1),
        ),
        child: Row(
          children: [
            Container(
              width: 32,
              height: 32,
              decoration: BoxDecoration(
                color: accent.o(0.12),
                borderRadius: BorderRadius.circular(9),
                border: Border.all(color: accent.o(0.28)),
              ),
              child: Icon(icon, size: 16, color: accent),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    displayName,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.w500,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    '${isPdf ? 'PDF' : 'TABLERO'} • ${adjunto.pesoFormateado}',
                    style: mono(fontSize: 10, color: p.textSecondary),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 6),
            TapScale(
              onTap: onView,
              child: Padding(
                padding: const EdgeInsets.all(6),
                child: Icon(
                  Icons.open_in_full_rounded,
                  size: 15,
                  color: p.textSecondary,
                ),
              ),
            ),
            TapScale(
              onTap: onDelete,
              child: Padding(
                padding: const EdgeInsets.all(6),
                child: Icon(
                  Icons.close_rounded,
                  size: 17,
                  color: p.textSecondary,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

enum _NoteSyncState { idle, typing, syncing, synced }

/// Área de Notas Personales colapsable con auto-save debounce de 1 segundo
/// y sincronización inmediata al perder el foco.
class _PersonalNotesCollapsibleCard extends StatefulWidget {
  const _PersonalNotesCollapsibleCard({
    super.key,
    required this.temaId,
    required this.syncedText,
  });

  final String temaId;
  final String syncedText;

  @override
  State<_PersonalNotesCollapsibleCard> createState() =>
      _PersonalNotesCollapsibleCardState();
}

class _PersonalNotesCollapsibleCardState
    extends State<_PersonalNotesCollapsibleCard> {
  late final TextEditingController _controller;
  final FocusNode _focusNode = FocusNode();

  Timer? _debounceTimer;
  IClaseVivaRepository? _repo;
  bool _expanded = true;
  bool _hasFocus = false;
  bool _dirty = false;
  String _lastSavedText = '';
  _NoteSyncState _syncState = _NoteSyncState.idle;

  @override
  void initState() {
    super.initState();
    _lastSavedText = widget.syncedText;
    _controller = TextEditingController(text: widget.syncedText);
    if (widget.syncedText.isNotEmpty) {
      _syncState = _NoteSyncState.synced;
    }
    _focusNode.addListener(_handleFocusChange);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _repo = ClaseVivaRepositoryScope.of(context);
  }

  @override
  void didUpdateWidget(covariant _PersonalNotesCollapsibleCard oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (!_dirty &&
        !_hasFocus &&
        widget.syncedText != _lastSavedText &&
        widget.syncedText != _controller.text) {
      _lastSavedText = widget.syncedText;
      _controller.text = widget.syncedText;
      if (widget.syncedText.isNotEmpty) {
        _syncState = _NoteSyncState.synced;
      }
    }
  }

  void _handleFocusChange() {
    final focused = _focusNode.hasFocus;
    if (mounted) {
      setState(() => _hasFocus = focused);
    }
    if (!focused && _dirty) {
      _debounceTimer?.cancel();
      _persistNow();
    }
  }

  void _onNoteChanged(String value) {
    _dirty = value != _lastSavedText;
    setState(() {
      _syncState = _dirty ? _NoteSyncState.typing : _NoteSyncState.synced;
    });
    _debounceTimer?.cancel();
    if (!_dirty) return;

    _debounceTimer = Timer(AppConstants.noteAutoSaveDebounce, _persistNow);
  }

  Future<void> _persistNow() async {
    final repo = _repo;
    if (repo == null || !_dirty) return;
    final snapshot = _controller.text;
    _dirty = false;
    if (mounted) {
      setState(() => _syncState = _NoteSyncState.syncing);
    }
    await repo.guardarNotaPersonal(
      temaId: widget.temaId,
      contenido: snapshot,
    );
    _lastSavedText = snapshot;
    if (mounted) {
      setState(() => _syncState = _NoteSyncState.synced);
    }
  }

  void _insertFormattingToken(String prefix, [String suffix = '']) {
    final text = _controller.text;
    final sel = _controller.selection;
    final start = sel.isValid ? sel.start : text.length;
    final end = sel.isValid ? sel.end : text.length;
    final selected = text.substring(start, end);
    final replacement = '$prefix$selected$suffix';
    final updated = text.replaceRange(start, end, replacement);
    final cursorOffset = suffix.isNotEmpty && selected.isEmpty
        ? start + prefix.length
        : start + replacement.length;

    _controller.value = TextEditingValue(
      text: updated,
      selection: TextSelection.collapsed(offset: cursorOffset),
    );
    if (!_focusNode.hasFocus) {
      _focusNode.requestFocus();
    }
    _onNoteChanged(updated);
  }

  @override
  void dispose() {
    _debounceTimer?.cancel();
    if (_dirty && _repo != null) {
      _repo!.guardarNotaPersonal(
        temaId: widget.temaId,
        contenido: _controller.text,
      );
    }
    _focusNode
      ..removeListener(_handleFocusChange)
      ..dispose();
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final borderColor = _hasFocus ? p.indigo.o(0.55) : p.cardBorder;

    return AnimatedContainer(
      duration: const Duration(milliseconds: 200),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: borderColor, width: 1),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TapScale(
            onTap: () {
              if (_expanded && _focusNode.hasFocus) {
                _focusNode.unfocus();
              }
              setState(() => _expanded = !_expanded);
            },
            child: Padding(
              padding: const EdgeInsets.fromLTRB(14, 13, 14, 13),
              child: Row(
                children: [
                  Container(
                    width: 24,
                    height: 24,
                    decoration: BoxDecoration(
                      color: p.indigo.o(0.14),
                      borderRadius: BorderRadius.circular(7),
                    ),
                    child: Icon(
                      Icons.edit_note_rounded,
                      size: 16,
                      color: p.indigo,
                    ),
                  ),
                  const SizedBox(width: 9),
                  Expanded(
                    child: Text(
                      'Notas Personales',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                        color: p.textPrimary,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  _buildSyncIndicator(p),
                  const SizedBox(width: 6),
                  AnimatedRotation(
                    turns: _expanded ? 0.0 : -0.25,
                    duration: const Duration(milliseconds: 220),
                    curve: kIosSpring,
                    child: Icon(
                      Icons.keyboard_arrow_down_rounded,
                      size: 18,
                      color: p.textSecondary,
                    ),
                  ),
                ],
              ),
            ),
          ),
          AnimatedCrossFade(
            firstChild: Padding(
              padding: const EdgeInsets.fromLTRB(14, 0, 14, 14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const IosHairline(),
                  const SizedBox(height: 10),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        _FormatChip(
                          label: '• Viñeta',
                          onTap: () => _insertFormattingToken('\n• '),
                        ),
                        const SizedBox(width: 6),
                        _FormatChip(
                          label: '§ Subtítulo',
                          onTap: () => _insertFormattingToken('\n## '),
                        ),
                        const SizedBox(width: 6),
                        _FormatChip(
                          label: '∑ Fórmula',
                          accent: p.indigo,
                          onTap: () => _insertFormattingToken(r'$', r'$'),
                        ),
                        const SizedBox(width: 6),
                        _FormatChip(
                          label: '★ Clave',
                          onTap: () => _insertFormattingToken('**', '**'),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 10),
                  TextField(
                    controller: _controller,
                    focusNode: _focusNode,
                    onChanged: _onNoteChanged,
                    minLines: 3,
                    maxLines: 8,
                    style: TextStyle(
                      fontSize: 13.5,
                      height: 1.5,
                      color: p.textBody,
                    ),
                    cursorColor: p.indigo,
                    decoration: InputDecoration(
                      isDense: true,
                      filled: true,
                      fillColor: p.background.o(0.35),
                      contentPadding: const EdgeInsets.all(12),
                      hintText:
                          'Añade deducciones, recordatorios del parcial o fórmulas entre \$...\$ (auto-guardado en la nube)...',
                      hintStyle: TextStyle(
                        fontSize: 12.5,
                        height: 1.45,
                        color: p.textTertiary,
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: BorderSide(color: p.cardBorder),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: BorderSide(color: p.indigo.o(0.45)),
                      ),
                    ),
                  ),
                  ValueListenableBuilder<TextEditingValue>(
                    valueListenable: _controller,
                    builder: (context, value, _) {
                      return NoteFormulasPreview(noteText: value.text);
                    },
                  ),
                ],
              ),
            ),
            secondChild: _controller.text.trim().isEmpty
                ? const SizedBox(width: double.infinity, height: 0)
                : Padding(
                    padding: const EdgeInsets.fromLTRB(14, 0, 14, 13),
                    child: Text(
                      _controller.text.trim(),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 12,
                        color: p.textSecondary,
                      ),
                    ),
                  ),
            crossFadeState: _expanded
                ? CrossFadeState.showFirst
                : CrossFadeState.showSecond,
            duration: const Duration(milliseconds: 240),
            sizeCurve: kIosSpring,
          ),
        ],
      ),
    );
  }

  Widget _buildSyncIndicator(AppPalette p) {
    switch (_syncState) {
      case _NoteSyncState.typing:
        return Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Dot(color: p.indigo, size: 6),
            const SizedBox(width: 5),
            Text('Editando...', style: mono(fontSize: 10, color: p.indigo)),
          ],
        );
      case _NoteSyncState.syncing:
        return Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            PulseDot(color: p.indigo, size: 6),
            const SizedBox(width: 5),
            Text('Sincronizando', style: mono(fontSize: 10, color: p.indigo)),
          ],
        );
      case _NoteSyncState.synced:
        return Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Dot(color: p.green, size: 6),
            const SizedBox(width: 5),
            Text(
              'Sincronizado',
              style: mono(fontSize: 10, color: p.textSecondary),
            ),
          ],
        );
      case _NoteSyncState.idle:
        return Text(
          'Auto-save 1s',
          style: mono(fontSize: 10, color: p.textTertiary),
        );
    }
  }
}

class _FormatChip extends StatelessWidget {
  const _FormatChip({
    required this.label,
    required this.onTap,
    this.accent,
  });

  final String label;
  final VoidCallback onTap;
  final Color? accent;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final color = accent ?? p.textSecondary;

    return TapScale(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
        decoration: BoxDecoration(
          color: accent != null ? accent!.o(0.10) : p.elevated,
          borderRadius: BorderRadius.circular(8),
          border: Border.all(
            color: accent != null ? accent!.o(0.28) : p.cardBorder,
          ),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 11,
            fontWeight: FontWeight.w500,
            color: color,
          ),
        ),
      ),
    );
  }
}

class _SheetOptionTile extends StatelessWidget {
  const _SheetOptionTile({
    required this.icon,
    required this.accent,
    required this.title,
    required this.subtitle,
    required this.onTap,
  });

  final IconData icon;
  final Color accent;
  final String title;
  final String subtitle;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return TapScale(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: p.elevated,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: p.cardBorder),
        ),
        child: Row(
          children: [
            Container(
              width: 36,
              height: 36,
              decoration: BoxDecoration(
                color: accent.o(0.12),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, size: 19, color: accent),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: TextStyle(
                      fontSize: 13.5,
                      fontWeight: FontWeight.w600,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: TextStyle(fontSize: 11.5, color: p.textSecondary),
                  ),
                ],
              ),
            ),
            Icon(
              Icons.chevron_right_rounded,
              size: 18,
              color: p.textSecondary,
            ),
          ],
        ),
      ),
    );
  }
}
