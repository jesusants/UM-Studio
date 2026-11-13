import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../../domain/entities/topic_chat_message.dart';
import '../providers/app_scopes.dart';
import '../providers/topic_ai_assistant_controller.dart';
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
  });

  final String topicKey;
  final String asignaturaNombre;
  final String temaTitulo;
  final String temaContextoCompleto;
  final Color? accentColor;
  final VoidCallback? onClose;

  @override
  State<TopicAiChatView> createState() => _TopicAiChatViewState();
}

class _TopicAiChatViewState extends State<TopicAiChatView> {
  final TextEditingController _textCtrl = TextEditingController();
  final ScrollController _scrollCtrl = ScrollController();
  final FocusNode _focusNode = FocusNode();

  final TopicAiAssistantController _controller =
      TopicAiAssistantController.instance;

  @override
  void initState() {
    super.initState();
    _controller.addListener(_onControllerUpdate);
  }

  @override
  void didUpdateWidget(covariant TopicAiChatView oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.topicKey != widget.topicKey) {
      _textCtrl.clear();
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

  void _submitMessage([String? preset]) {
    final query = preset ?? _textCtrl.text.trim();
    if (query.isEmpty) return;

    if (preset == null) {
      _textCtrl.clear();
    }

    _controller.sendQuestion(
      topicKey: widget.topicKey,
      asignaturaNombre: widget.asignaturaNombre,
      temaTitulo: widget.temaTitulo,
      temaContextoCompleto: widget.temaContextoCompleto,
      pregunta: query,
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

        // 3. Barra de Entrada de Texto
        Container(
          padding: const EdgeInsets.fromLTRB(12, 8, 10, 10),
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF0F1117) : const Color(0xFFF9FAFB),
            border: Border(
              top: BorderSide(
                color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE5E5EA),
                width: 1,
              ),
            ),
          ),
          child: Row(
            children: [
              Expanded(
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 12),
                  decoration: BoxDecoration(
                    color: isDark ? const Color(0xFF181B24) : Colors.white,
                    borderRadius: BorderRadius.circular(14),
                    border: Border.all(
                      color: isDark ? const Color(0xFF262B38) : const Color(0xFFE2E4E9),
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
                      contentPadding: const EdgeInsets.symmetric(vertical: 9),
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 8),
              TapScale(
                onTap: isLoading ? null : () => _submitMessage(),
                child: Container(
                  width: 36,
                  height: 36,
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
    final suggestions = [
      'Explicar la fórmula principal',
      'Desglosar el ejercicio paso a paso',
      '¿Qué significa cada variable?',
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
              child: isUser
                  ? Text(
                      msg.content,
                      style: TextStyle(
                        fontSize: 13,
                        height: 1.35,
                        color: isDark ? Colors.white : p.textPrimary,
                      ),
                    )
                  : _TopicAiMarkdownRenderer(
                      content: msg.content,
                      accentColor: accent,
                      isDark: isDark,
                    ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Renderizador de respuestas con fórmulas KaTeX y negritas
class _TopicAiMarkdownRenderer extends StatelessWidget {
  const _TopicAiMarkdownRenderer({
    required this.content,
    required this.accentColor,
    required this.isDark,
  });

  final String content;
  final Color accentColor;
  final bool isDark;

  @override
  Widget build(BuildContext context) {
    // Dividir contenido en bloques de display math $$...$$ y texto
    final blocks = _splitBlocks(content);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (final block in blocks)
          if (block.isDisplayMath)
            _buildDisplayFormula(block.text)
          else
            _buildParagraph(block.text),
      ],
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
    final pattern = RegExp(r'\$\$(.*?)\$\$', dotAll: true);
    int lastEnd = 0;

    for (final m in pattern.allMatches(raw)) {
      if (m.start > lastEnd) {
        final txt = raw.substring(lastEnd, m.start).trim();
        if (txt.isNotEmpty) {
          list.add(_AiBlock(text: txt, isDisplayMath: false));
        }
      }
      final formula = m.group(1)!.trim();
      if (formula.isNotEmpty) {
        list.add(_AiBlock(text: formula, isDisplayMath: true));
      }
      lastEnd = m.end;
    }

    if (lastEnd < raw.length) {
      final txt = raw.substring(lastEnd).trim();
      if (txt.isNotEmpty) {
        list.add(_AiBlock(text: txt, isDisplayMath: false));
      }
    }

    return list.isNotEmpty ? list : [_AiBlock(text: raw, isDisplayMath: false)];
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

class _AiBlock {
  const _AiBlock({required this.text, required this.isDisplayMath});
  final String text;
  final bool isDisplayMath;
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
