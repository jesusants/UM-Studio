import 'dart:ui';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../data/services/global_environment_service.dart';
import '../../domain/entities/topic_chat_message.dart';
import '../providers/app_scopes.dart';
import '../providers/topic_ai_assistant_controller.dart';
import 'ai_graphic_block.dart';
import 'ios_primitives.dart';

/// Botón minimalista de disparo del asistente contextual
class TopicAiTriggerButton extends StatelessWidget {
  const TopicAiTriggerButton({
    super.key,
    required this.onTap,
    this.accentColor,
    this.isOpen = false,
  });

  final VoidCallback onTap;
  final Color? accentColor;
  final bool isOpen;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);
    final accent = accentColor ?? (isDark ? p.indigo : p.green);

    return TapScale(
      onTap: () {
        HapticFeedback.lightImpact();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 9),
        decoration: BoxDecoration(
          color: isOpen ? accent : (isDark ? const Color(0xFF141720) : Colors.white),
          borderRadius: BorderRadius.circular(999),
          border: Border.all(
            color: isOpen ? accent : accent.o(0.45),
            width: 1.2,
          ),
          boxShadow: [
            BoxShadow(
              color: accent.o(isDark ? 0.28 : 0.16),
              blurRadius: 14,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.auto_awesome_rounded,
              size: 15,
              color: isOpen ? Colors.white : accent,
            ),
            const SizedBox(width: 7),
            Text(
              'Preguntar sobre este tema',
              style: TextStyle(
                fontSize: 12.5,
                fontWeight: FontWeight.w600,
                letterSpacing: -0.2,
                color: isOpen ? Colors.white : (isDark ? Colors.white : p.textPrimary),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Panel principal de chat contextual (reutilizable en escritorio y móvil)
class TopicAiChatView extends StatefulWidget {
  const TopicAiChatView({
    super.key,
    required this.topicKey,
    required this.asignaturaNombre,
    required this.temaTitulo,
    required this.temaContextoCompleto,
    this.accentColor,
    this.onClose,
    this.controller,
  });

  final String topicKey;
  final String asignaturaNombre;
  final String temaTitulo;
  final String temaContextoCompleto;
  final Color? accentColor;
  final VoidCallback? onClose;
  final TopicAiAssistantController? controller;

  @override
  State<TopicAiChatView> createState() => _TopicAiChatViewState();
}

class _TopicAiChatViewState extends State<TopicAiChatView> {
  final TextEditingController _textCtrl = TextEditingController();
  final ScrollController _scrollCtrl = ScrollController();
  final FocusNode _focusNode = FocusNode();

  Uint8List? _pendingImageBytes;
  String? _pendingImageMime;
  String? _pendingImageName;

  TopicAiAssistantController get _controller =>
      widget.controller ?? TopicAiAssistantController.instance;

  @override
  void initState() {
    super.initState();
    _controller.addListener(_onControllerUpdate);
  }

  @override
  void didUpdateWidget(covariant TopicAiChatView oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.controller != widget.controller) {
      (oldWidget.controller ?? TopicAiAssistantController.instance)
          .removeListener(_onControllerUpdate);
      _controller.addListener(_onControllerUpdate);
    }
    if (oldWidget.topicKey != widget.topicKey) {
      _textCtrl.clear();
      _pendingImageBytes = null;
      _pendingImageMime = null;
      _pendingImageName = null;
      _scrollToBottom();
    }
  }

  @override
  void dispose() {
    _controller.removeListener(_onControllerUpdate);
    _textCtrl.dispose();
    _scrollCtrl.dispose();
    _focusNode.dispose();
    super.dispose();
  }

  void _onControllerUpdate() {
    if (!mounted) return;
    setState(() {});
    _scrollToBottom();
  }

  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollCtrl.hasClients) {
        _scrollCtrl.animateTo(
          _scrollCtrl.position.maxScrollExtent,
          duration: const Duration(milliseconds: 250),
          curve: Curves.easeOut,
        );
      }
    });
  }

  String _resolveStudentFullName(BuildContext context) {
    final session = SessionScope.maybeOf(context);
    if (session == null || !session.isAuthenticated) return '';
    final full = session.displayName.trim();
    if (full.isNotEmpty) return full;
    return session.primerNombre.trim();
  }

  String _resolveStudentFirstName(BuildContext context) {
    final session = SessionScope.maybeOf(context);
    if (session == null || !session.isAuthenticated) return '';
    final first = session.primerNombre.trim();
    if (first.isNotEmpty) return first;
    return session.displayName.trim();
  }

  Future<void> _pickImageAttachment() async {
    try {
      final result = await FilePicker.pickFile(
        dialogTitle: 'Adjuntar diagrama, ecuación o imagen al asistente',
        type: FileType.image,
      );
      if (result == null) return;
      final bytes = await result.readAsBytes();
      if (bytes.isEmpty) return;
      if (bytes.length > 4 * 1024 * 1024) {
        if (!mounted) return;
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('La imagen supera 4 MB. Selecciona una más liviana.'),
          ),
        );
        return;
      }
      final ext = (result.extension ?? 'png').toLowerCase();
      final mime = (ext == 'jpg' || ext == 'jpeg')
          ? 'image/jpeg'
          : ext == 'webp'
              ? 'image/webp'
              : 'image/png';
      if (!mounted) return;
      setState(() {
        _pendingImageBytes = bytes;
        _pendingImageMime = mime;
        _pendingImageName = result.name;
      });
    } catch (_) {}
  }

  Future<void> _insertGraphicElement() async {
    final generatedPrompt = await showAiGraphicComposerDialog(
      context,
      temaTitulo: widget.temaTitulo,
    );
    if (!mounted || generatedPrompt == null || generatedPrompt.trim().isEmpty) {
      return;
    }
    _submitMessage(generatedPrompt);
  }

  void _submitMessage([String? preset]) {
    final query = (preset ?? _textCtrl.text).trim();
    final imgBytes = _pendingImageBytes;
    final imgMime = _pendingImageMime;
    final imgName = _pendingImageName;
    if (query.isEmpty && (imgBytes == null || imgBytes.isEmpty)) return;

    if (preset == null) {
      _textCtrl.clear();
    }
    if (_pendingImageBytes != null) {
      setState(() {
        _pendingImageBytes = null;
        _pendingImageMime = null;
        _pendingImageName = null;
      });
    }

    final studentName = _resolveStudentFullName(context);
    _controller.sendQuestion(
      topicKey: widget.topicKey,
      asignaturaNombre: widget.asignaturaNombre,
      temaTitulo: widget.temaTitulo,
      temaContextoCompleto: widget.temaContextoCompleto,
      pregunta: query,
      studentName: studentName.isNotEmpty ? studentName : null,
      imageBytes: imgBytes,
      imageMimeType: imgMime,
      imageName: imgName,
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);
    final accent = widget.accentColor ?? (isDark ? p.indigo : p.green);

    final messages = _controller.getHistory(widget.topicKey);
    final isLoading = _controller.isLoading(widget.topicKey);

    return Column(
      children: [
        // 1. Cabecera del Asistente
        Container(
          padding: const EdgeInsets.fromLTRB(14, 12, 10, 12),
          decoration: BoxDecoration(
            border: Border(
              bottom: BorderSide(
                color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE5E5EA),
                width: 1,
              ),
            ),
          ),
          child: Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: accent.o(0.12),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.lock_rounded, size: 12, color: accent),
                    const SizedBox(width: 4),
                    Text(
                      'Contexto:',
                      style: mono(
                        fontSize: 10,
                        fontWeight: FontWeight.w700,
                        color: accent,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  widget.temaTitulo,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 12.5,
                    fontWeight: FontWeight.w600,
                    letterSpacing: -0.2,
                    color: isDark ? Colors.white : p.textPrimary,
                  ),
                ),
              ),
              const SizedBox(width: 4),
              if (messages.isNotEmpty)
                IconButton(
                  icon: Icon(
                    Icons.refresh_rounded,
                    size: 17,
                    color: p.textSecondary,
                  ),
                  tooltip: 'Reiniciar chat del tema',
                  onPressed: () {
                    HapticFeedback.lightImpact();
                    _controller.clearHistory(widget.topicKey);
                  },
                ),
              if (widget.onClose != null)
                IconButton(
                  icon: Icon(
                    Icons.close_rounded,
                    size: 18,
                    color: p.textSecondary,
                  ),
                  tooltip: 'Cerrar',
                  onPressed: widget.onClose,
                ),
            ],
          ),
        ),

        // 2. Área de Mensajes o Chips Iniciales
        Expanded(
          child: messages.isEmpty
              ? _buildEmptyStateWithSuggestions(context, accent, isDark)
              : ListView.builder(
                  controller: _scrollCtrl,
                  physics: const BouncingScrollPhysics(),
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                  itemCount: messages.length + (isLoading ? 1 : 0),
                  itemBuilder: (context, index) {
                    if (index == messages.length && isLoading) {
                      return _buildTypingIndicator(accent, isDark);
                    }
                    final msg = messages[index];
                    return _buildMessageBubble(context, msg, accent, isDark);
                  },
                ),
        ),

        // 3. Barra de Entrada de Texto + Elementos Gráficos
        Container(
          padding: const EdgeInsets.fromLTRB(10, 8, 10, 10),
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF0F1117) : const Color(0xFFF9FAFB),
            border: Border(
              top: BorderSide(
                color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE5E5EA),
                width: 1,
              ),
            ),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              if (_pendingImageBytes != null) ...[
                Container(
                  margin: const EdgeInsets.only(bottom: 8),
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
                  decoration: BoxDecoration(
                    color: isDark ? const Color(0xFF181B24) : Colors.white,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: accent.o(0.35)),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      ClipRRect(
                        borderRadius: BorderRadius.circular(6),
                        child: Image.memory(
                          _pendingImageBytes!,
                          width: 30,
                          height: 30,
                          fit: BoxFit.cover,
                        ),
                      ),
                      const SizedBox(width: 8),
                      Flexible(
                        child: Text(
                          _pendingImageName ?? 'Imagen adjunta',
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 11.5,
                            fontWeight: FontWeight.w600,
                            color: isDark ? Colors.white : p.textPrimary,
                          ),
                        ),
                      ),
                      const SizedBox(width: 4),
                      InkWell(
                        onTap: () => setState(() {
                          _pendingImageBytes = null;
                          _pendingImageMime = null;
                          _pendingImageName = null;
                        }),
                        borderRadius: BorderRadius.circular(10),
                        child: Icon(
                          Icons.close_rounded,
                          size: 16,
                          color: p.textSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
              Row(
                children: [
                  if (GlobalEnvironmentService.instance.config.allowAiGraphics) ...[
                    Tooltip(
                      message: 'Adjuntar imagen o captura',
                      child: TapScale(
                        onTap: isLoading ? null : _pickImageAttachment,
                        child: Container(
                          width: 32,
                          height: 32,
                          decoration: BoxDecoration(
                            color: isDark
                                ? const Color(0xFF181B24)
                                : Colors.white,
                            shape: BoxShape.circle,
                            border: Border.all(
                              color: isDark
                                  ? const Color(0xFF262B38)
                                  : const Color(0xFFE2E4E9),
                            ),
                          ),
                          child: Icon(
                            Icons.add_photo_alternate_outlined,
                            size: 16,
                            color: p.textSecondary,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 5),
                    Tooltip(
                      message: 'Añadir elemento gráfico o diagrama',
                      child: TapScale(
                        onTap: isLoading ? null : _insertGraphicElement,
                        child: Container(
                          width: 32,
                          height: 32,
                          decoration: BoxDecoration(
                            color: accent.o(0.12),
                            shape: BoxShape.circle,
                            border: Border.all(color: accent.o(0.35)),
                          ),
                          child: Icon(
                            Icons.auto_graph_rounded,
                            size: 16,
                            color: accent,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 6),
                  ],
                  Expanded(
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      decoration: BoxDecoration(
                        color: isDark ? const Color(0xFF181B24) : Colors.white,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(
                          color: isDark
                              ? const Color(0xFF262B38)
                              : const Color(0xFFE2E4E9),
                          width: 1,
                        ),
                      ),
                      child: TextField(
                        controller: _textCtrl,
                        focusNode: _focusNode,
                        minLines: 1,
                        maxLines: 4,
                        textInputAction: TextInputAction.send,
                        onSubmitted: (_) => _submitMessage(),
                        style: TextStyle(
                          fontSize: 13,
                          color: isDark ? Colors.white : p.textPrimary,
                        ),
                        decoration: InputDecoration(
                          hintText: 'Preguntar sobre este tema...',
                          hintStyle: TextStyle(
                            fontSize: 12.5,
                            color: p.textSecondary,
                          ),
                          border: InputBorder.none,
                          isDense: true,
                          contentPadding:
                              const EdgeInsets.symmetric(vertical: 9),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 6),
                  TapScale(
                    onTap: isLoading ? null : () => _submitMessage(),
                    child: Container(
                      width: 34,
                      height: 34,
                      decoration: BoxDecoration(
                        color: isLoading ? p.cardBorder : accent,
                        shape: BoxShape.circle,
                      ),
                      child: const Icon(
                        Icons.arrow_upward_rounded,
                        size: 18,
                        color: Colors.white,
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildEmptyStateWithSuggestions(
    BuildContext context,
    Color accent,
    bool isDark,
  ) {
    final p = context.palette;
    final allowGraphics =
        GlobalEnvironmentService.instance.config.allowAiGraphics;
    final registeredFull = _resolveStudentFullName(context);
    final registeredFirst = _resolveStudentFirstName(context);
    final greetingName =
        registeredFull.isNotEmpty ? registeredFull : registeredFirst;

    final suggestions = [
      'Explicar la fórmula principal',
      'Desglosar el ejercicio paso a paso',
      '¿Qué significa cada variable?',
      if (allowGraphics) 'Graficar una función o diagrama del tema',
    ];

    return SingleChildScrollView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: accent.o(0.12),
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.auto_awesome_rounded,
              size: 22,
              color: accent,
            ),
          ),
          const SizedBox(height: 10),
          Text(
            'Asistente de Tema Oficial',
            style: TextStyle(
              fontSize: 13.5,
              fontWeight: FontWeight.w700,
              letterSpacing: -0.2,
              color: isDark ? Colors.white : p.textPrimary,
            ),
          ),
          if (greetingName.isNotEmpty) ...[
            const SizedBox(height: 4),
            Text(
              '¡Hola, $greetingName!',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 12.5,
                fontWeight: FontWeight.w700,
                color: accent,
              ),
            ),
          ],
          const SizedBox(height: 4),
          Text(
            'Respuestas rigurosas basadas únicamente en las diapositivas y notas de esta sesión.',
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 11.5,
              height: 1.35,
              color: p.textSecondary,
            ),
          ),
          const SizedBox(height: 14),
          for (final sug in suggestions) ...[
            TapScale(
              onTap: () => _submitMessage(sug),
              child: Container(
                width: double.infinity,
                margin: const EdgeInsets.only(bottom: 8),
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8.5),
                decoration: BoxDecoration(
                  color: isDark ? const Color(0xFF141720) : Colors.white,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isDark ? const Color(0xFF222632) : const Color(0xFFE2E4E9),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      Icons.chat_bubble_outline_rounded,
                      size: 13,
                      color: accent,
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        sug,
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w500,
                          color: isDark ? const Color(0xFFDCDFE6) : p.textPrimary,
                        ),
                      ),
                    ),
                    Icon(
                      Icons.arrow_forward_ios_rounded,
                      size: 10,
                      color: p.textSecondary,
                    ),
                  ],
                ),
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildTypingIndicator(Color accent, bool isDark) {
    return Align(
      alignment: Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF141720) : const Color(0xFFF2F4F8),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDark ? const Color(0xFF1F2430) : const Color(0xFFE2E4E8),
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            SizedBox(
              width: 12,
              height: 12,
              child: CircularProgressIndicator(
                strokeWidth: 1.8,
                valueColor: AlwaysStoppedAnimation<Color>(accent),
              ),
            ),
            const SizedBox(width: 8),
            Text(
              'Analizando tema con IA...',
              style: TextStyle(
                fontSize: 11.5,
                fontWeight: FontWeight.w500,
                color: accent,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMessageBubble(
    BuildContext context,
    TopicChatMessage msg,
    Color accent,
    bool isDark,
  ) {
    final p = context.palette;
    final isUser = msg.isUser;

    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        mainAxisAlignment:
            isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (!isUser) ...[
            Container(
              margin: const EdgeInsets.only(top: 2, right: 8),
              padding: const EdgeInsets.all(5),
              decoration: BoxDecoration(
                color: accent.o(0.14),
                shape: BoxShape.circle,
              ),
              child: Icon(
                Icons.auto_awesome_rounded,
                size: 12,
                color: accent,
              ),
            ),
          ],
          Flexible(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 13, vertical: 9),
              decoration: BoxDecoration(
                color: isUser
                    ? (isDark ? accent.o(0.24) : accent.o(0.12))
                    : (isDark ? const Color(0xFF141720) : const Color(0xFFF4F6F9)),
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(16),
                  topRight: const Radius.circular(16),
                  bottomLeft: Radius.circular(isUser ? 16 : 4),
                  bottomRight: Radius.circular(isUser ? 4 : 16),
                ),
                border: Border.all(
                  color: isUser
                      ? accent.o(0.4)
                      : (isDark ? const Color(0xFF1E232E) : const Color(0xFFE0E3E8)),
                  width: 1,
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (msg.hasImage) ...[
                    ClipRRect(
                      borderRadius: BorderRadius.circular(10),
                      child: ConstrainedBox(
                        constraints: const BoxConstraints(maxHeight: 190),
                        child: Image.memory(
                          msg.imageBytes!,
                          fit: BoxFit.contain,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),
                  ],
                  if (isUser && !msg.content.contains('```um-grafica'))
                    Text(
                      msg.content,
                      style: TextStyle(
                        fontSize: 13,
                        height: 1.35,
                        color: isDark ? Colors.white : p.textPrimary,
                      ),
                    )
                  else
                    _TopicAiMarkdownRenderer(
                      content: msg.content,
                      accentColor: accent,
                      isDark: isDark,
                      asignaturaNombre: widget.asignaturaNombre,
                      temaTitulo: widget.temaTitulo,
                    ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Renderizador de respuestas con fórmulas KaTeX, elementos gráficos y negritas
class _TopicAiMarkdownRenderer extends StatelessWidget {
  const _TopicAiMarkdownRenderer({
    required this.content,
    required this.accentColor,
    required this.isDark,
    this.asignaturaNombre = 'Ingeniería',
    this.temaTitulo = 'Tema',
  });

  final String content;
  final Color accentColor;
  final bool isDark;
  final String asignaturaNombre;
  final String temaTitulo;

  @override
  Widget build(BuildContext context) {
    final blocks = _splitBlocks(content);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (final block in blocks)
          if (block.type == _AiBlockType.graphic)
            _buildGraphicBlock(block.text)
          else if (block.type == _AiBlockType.displayMath)
            _buildDisplayFormula(block.text)
          else
            _buildParagraph(block.text),
      ],
    );
  }

  Widget _buildGraphicBlock(String rawGraphic) {
    final spec = AiGraphicSpec.tryParse(rawGraphic);
    if (spec != null) {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 6),
        child: AiGraphicBlockWidget(
          spec: spec,
          asignaturaNombre: asignaturaNombre,
          temaTitulo: temaTitulo,
        ),
      );
    }
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.symmetric(vertical: 6),
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF0C0E14) : const Color(0xFFECEFF4),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Text(
        rawGraphic,
        style: mono(fontSize: 11, color: accentColor),
      ),
    );
  }

  Widget _buildDisplayFormula(String formula) {
    final clean = InstitutionalValidator.sanitizeLatex(formula);
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.symmetric(vertical: 6),
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 7),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF0C0E14) : const Color(0xFFECEFF4),
        borderRadius: BorderRadius.circular(8),
        border: Border(
          left: BorderSide(color: accentColor, width: 3),
          top: BorderSide(color: isDark ? const Color(0xFF1A1D27) : const Color(0xFFDEE1E6)),
          right: BorderSide(color: isDark ? const Color(0xFF1A1D27) : const Color(0xFFDEE1E6)),
          bottom: BorderSide(color: isDark ? const Color(0xFF1A1D27) : const Color(0xFFDEE1E6)),
        ),
      ),
      child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        child: Math.tex(
          clean,
          mathStyle: MathStyle.display,
          textStyle: TextStyle(
            fontSize: 13,
            color: isDark ? Colors.white : const Color(0xFF1A1C20),
          ),
          onErrorFallback: (_) => Text(
            clean,
            style: mono(fontSize: 11.5, color: accentColor),
          ),
        ),
      ),
    );
  }

  Widget _buildParagraph(String text) {
    final tokens = _tokenize(text);
    final spans = <InlineSpan>[];

    for (final token in tokens) {
      if (token.type == _AiTokenType.inlineMath) {
        final clean = InstitutionalValidator.sanitizeLatex(token.content);
        spans.add(
          WidgetSpan(
            alignment: PlaceholderAlignment.middle,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 2),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                child: Math.tex(
                  clean,
                  mathStyle: MathStyle.text,
                  textStyle: TextStyle(
                    fontSize: 12.5,
                    color: isDark ? Colors.white : Colors.black,
                  ),
                  onErrorFallback: (_) => Text(
                    clean,
                    style: mono(fontSize: 11, color: accentColor),
                  ),
                ),
              ),
            ),
          ),
        );
      } else if (token.type == _AiTokenType.bold) {
        spans.add(
          TextSpan(
            text: token.content,
            style: TextStyle(
              fontSize: 12.5,
              height: 1.45,
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
              fontSize: 12.5,
              height: 1.45,
              color: isDark ? const Color(0xFFD6DAE3) : const Color(0xFF1F2228),
            ),
          ),
        );
      }
    }

    return Padding(
      padding: const EdgeInsets.only(bottom: 4),
      child: Text.rich(
        TextSpan(children: spans),
        softWrap: true,
      ),
    );
  }

  List<_AiBlock> _splitBlocks(String raw) {
    final list = <_AiBlock>[];
    final graphicPattern = RegExp(
      r'```(?:um-grafica|um_grafica|grafica)\s*([\s\S]*?)```',
      caseSensitive: false,
    );
    int lastEnd = 0;

    for (final gm in graphicPattern.allMatches(raw)) {
      if (gm.start > lastEnd) {
        _appendMathAndTextBlocks(raw.substring(lastEnd, gm.start), list);
      }
      final body = (gm.group(1) ?? '').trim();
      if (body.isNotEmpty) {
        list.add(_AiBlock(text: body, type: _AiBlockType.graphic));
      }
      lastEnd = gm.end;
    }

    if (lastEnd < raw.length) {
      _appendMathAndTextBlocks(raw.substring(lastEnd), list);
    }

    return list.isNotEmpty
        ? list
        : [_AiBlock(text: raw, type: _AiBlockType.paragraph)];
  }

  void _appendMathAndTextBlocks(String segment, List<_AiBlock> out) {
    final pattern = RegExp(r'\$\$(.*?)\$\$', dotAll: true);
    int lastEnd = 0;

    for (final m in pattern.allMatches(segment)) {
      if (m.start > lastEnd) {
        final txt = segment.substring(lastEnd, m.start).trim();
        if (txt.isNotEmpty) {
          out.add(_AiBlock(text: txt, type: _AiBlockType.paragraph));
        }
      }
      final formula = m.group(1)!.trim();
      if (formula.isNotEmpty) {
        out.add(_AiBlock(text: formula, type: _AiBlockType.displayMath));
      }
      lastEnd = m.end;
    }

    if (lastEnd < segment.length) {
      final txt = segment.substring(lastEnd).trim();
      if (txt.isNotEmpty) {
        out.add(_AiBlock(text: txt, type: _AiBlockType.paragraph));
      }
    }
  }

  List<_AiToken> _tokenize(String raw) {
    final tokens = <_AiToken>[];
    final pattern = RegExp(r'(\$.*?\$|\*\*.*?\*\*)', dotAll: true);
    int lastEnd = 0;

    for (final m in pattern.allMatches(raw)) {
      if (m.start > lastEnd) {
        tokens.add(
          _AiToken(
            type: _AiTokenType.text,
            content: raw.substring(lastEnd, m.start),
          ),
        );
      }
      final v = m.group(0)!;
      if (v.startsWith(r'$') && v.endsWith(r'$')) {
        tokens.add(
          _AiToken(
            type: _AiTokenType.inlineMath,
            content: v.substring(1, v.length - 1).trim(),
          ),
        );
      } else if (v.startsWith(r'**') && v.endsWith(r'**')) {
        tokens.add(
          _AiToken(
            type: _AiTokenType.bold,
            content: v.substring(2, v.length - 2),
          ),
        );
      }
      lastEnd = m.end;
    }

    if (lastEnd < raw.length) {
      tokens.add(
        _AiToken(
          type: _AiTokenType.text,
          content: raw.substring(lastEnd),
        ),
      );
    }

    return tokens;
  }
}

enum _AiBlockType { paragraph, displayMath, graphic }

class _AiBlock {
  const _AiBlock({required this.text, required this.type});
  final String text;
  final _AiBlockType type;
}

enum _AiTokenType { text, bold, inlineMath }

class _AiToken {
  const _AiToken({required this.type, required this.content});
  final _AiTokenType type;
  final String content;
}

/// Ventana flotante de chat para escritorio con Glassmorphism
class TopicAiDesktopFloatingWindow extends StatelessWidget {
  const TopicAiDesktopFloatingWindow({
    super.key,
    required this.topicKey,
    required this.asignaturaNombre,
    required this.temaTitulo,
    required this.temaContextoCompleto,
    required this.onClose,
    this.accentColor,
  });

  final String topicKey;
  final String asignaturaNombre;
  final String temaTitulo;
  final String temaContextoCompleto;
  final VoidCallback onClose;
  final Color? accentColor;

  @override
  Widget build(BuildContext context) {
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);

    return ClipRRect(
      borderRadius: BorderRadius.circular(20),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 18, sigmaY: 18),
        child: Container(
          width: 360,
          height: 480,
          decoration: BoxDecoration(
            color: isDark
                ? const Color(0xFF0F121A).withValues(alpha: 0.92)
                : Colors.white.withValues(alpha: 0.94),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE5E5EA),
              width: 1,
            ),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: isDark ? 0.45 : 0.12),
                blurRadius: 28,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          child: TopicAiChatView(
            topicKey: topicKey,
            asignaturaNombre: asignaturaNombre,
            temaTitulo: temaTitulo,
            temaContextoCompleto: temaContextoCompleto,
            accentColor: accentColor,
            onClose: onClose,
          ),
        ),
      ),
    );
  }
}

/// Disparador del ModalBottomSheet para móvil
void showTopicAiBottomSheet({
  required BuildContext context,
  required String topicKey,
  required String asignaturaNombre,
  required String temaTitulo,
  required String temaContextoCompleto,
  Color? accentColor,
}) {
  final isDark = ThemeScope.maybeOf(context)?.isDark ??
      (Theme.of(context).brightness == Brightness.dark);

  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    builder: (ctx) {
      final bottomInset = MediaQuery.of(ctx).viewInsets.bottom;
      final totalHeight = MediaQuery.of(ctx).size.height * 0.72;

      return Padding(
        padding: EdgeInsets.only(bottom: bottomInset),
        child: ClipRRect(
          borderRadius: const BorderRadius.vertical(top: Radius.circular(22)),
          child: Container(
            height: totalHeight,
            decoration: BoxDecoration(
              color: isDark ? const Color(0xFF0E1017) : Colors.white,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(22)),
              border: Border.all(
                color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE5E5EA),
              ),
            ),
            child: Column(
              children: [
                // Manija de arrastre
                Center(
                  child: Container(
                    margin: const EdgeInsets.only(top: 8, bottom: 4),
                    width: 36,
                    height: 4,
                    decoration: BoxDecoration(
                      color: isDark ? const Color(0xFF2E323D) : const Color(0xFFD1D1D6),
                      borderRadius: BorderRadius.circular(99),
                    ),
                  ),
                ),
                Expanded(
                  child: TopicAiChatView(
                    topicKey: topicKey,
                    asignaturaNombre: asignaturaNombre,
                    temaTitulo: temaTitulo,
                    temaContextoCompleto: temaContextoCompleto,
                    accentColor: accentColor,
                    onClose: () => Navigator.of(ctx).pop(),
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    },
  );
}
