import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import 'ios_primitives.dart';

/// Tarjeta modular de `CONCEPTO CLAVE` con renderizado matemático KaTeX nativo
/// (`flutter_math_fork`), compilando el árbol directamente en widgets de Flutter
/// a 60/120fps sin WebViews ni imágenes fijas.
class KatexFormulaCard extends StatefulWidget {
  const KatexFormulaCard({
    super.key,
    required this.latex,
    this.label = 'CONCEPTO CLAVE',
  });

  final String latex;
  final String label;

  @override
  State<KatexFormulaCard> createState() => _KatexFormulaCardState();
}

class _KatexFormulaCardState extends State<KatexFormulaCard> {
  bool _copied = false;

  Future<void> _copyLatex() async {
    await Clipboard.setData(ClipboardData(text: widget.latex));
    if (!mounted) return;
    setState(() => _copied = true);
    await Future<void>.delayed(const Duration(milliseconds: 1600));
    if (mounted) {
      setState(() => _copied = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final cleanLatex = InstitutionalValidator.sanitizeLatex(widget.latex);

    return IosCard(
      radius: 18,
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text(widget.label.toUpperCase(), style: sectionMicroStyle(p)),
              const Spacer(),
              TapScale(
                onTap: _copyLatex,
                child: Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                  decoration: BoxDecoration(
                    color: _copied ? p.green.o(0.12) : p.elevated,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(
                      color: _copied ? p.green.o(0.35) : p.cardBorder,
                    ),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(
                        _copied ? Icons.check_rounded : Icons.copy_rounded,
                        size: 11,
                        color: _copied ? p.green : p.textSecondary,
                      ),
                      const SizedBox(width: 4),
                      Text(
                        _copied ? 'Copiado' : 'KaTeX',
                        style: mono(
                          fontSize: 9.5,
                          fontWeight: FontWeight.w500,
                          color: _copied ? p.green : p.textSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 16),
            decoration: BoxDecoration(
              color: p.background.o(0.45),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: p.cardBorder),
            ),
            alignment: Alignment.center,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              physics: const BouncingScrollPhysics(),
              child: Math.tex(
                cleanLatex,
                mathStyle: MathStyle.display,
                textStyle: TextStyle(
                  fontSize: 18.5,
                  color: p.textPrimary,
                ),
                onErrorFallback: (_) => Text(
                  cleanLatex,
                  style: mono(fontSize: 15, color: p.textPrimary),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// Extrae y renderiza en vivo fórmulas `$...$` escritas dentro de las notas
/// personales del estudiante usando KaTeX nativo (`flutter_math_fork`).
class NoteFormulasPreview extends StatelessWidget {
  const NoteFormulasPreview({super.key, required this.noteText});

  final String noteText;

  @override
  Widget build(BuildContext context) {
    final matches =
        InstitutionalValidator.extractInlineLatexExpressions(noteText);
    if (matches.isEmpty) return const SizedBox.shrink();

    final p = context.palette;
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(top: 10),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: p.indigo.o(0.07),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: p.indigo.o(0.24)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'VISTA MATEMÁTICA EN NOTAS',
            style: TextStyle(
              fontSize: 9.5,
              fontWeight: FontWeight.w600,
              letterSpacing: 1.1,
              color: p.indigo,
            ),
          ),
          const SizedBox(height: 8),
          Wrap(
            spacing: 12,
            runSpacing: 8,
            children: [
              for (final expr in matches)
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Math.tex(
                    expr,
                    mathStyle: MathStyle.text,
                    textStyle: TextStyle(
                      fontSize: 14.5,
                      color: p.textPrimary,
                    ),
                    onErrorFallback: (_) => Text(
                      expr,
                      style: mono(fontSize: 12.5, color: p.textBody),
                    ),
                  ),
                ),
            ],
          ),
        ],
      ),
    );
  }
}
