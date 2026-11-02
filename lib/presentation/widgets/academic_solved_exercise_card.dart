import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../core/theme/app_theme.dart';
import '../../core/utils/institutional_validator.dart';
import '../providers/app_scopes.dart';

/// Componente de alta legibilidad editorial para la sección
/// "EJERCICIO RESUELTO / NOTAS DE CÁTEDRA".
/// Separa cada problema en sub-tarjetas con cabecera estilizada,
/// badges para cada paso ('PASO 1', 'PASO 2') y bloques KaTeX nativos.
class AcademicSolvedExerciseCard extends StatelessWidget {
  const AcademicSolvedExerciseCard({
    super.key,
    required this.label,
    required this.body,
    this.accentColor,
    this.isDesktop = false,
  });

  final String label;
  final String body;
  final Color? accentColor;
  final bool isDesktop;

  @override
  Widget build(BuildContext context) {
    if (body.trim().isEmpty) return const SizedBox.shrink();

    final p = context.palette;
    final isDark = ThemeScope.maybeOf(context)?.isDark ??
        (Theme.of(context).brightness == Brightness.dark);
    final accent = accentColor ?? (isDark ? p.indigo : p.green);
    final problems = _parseProblems(body);

    return Container(
      width: double.infinity,
      padding: EdgeInsets.all(isDesktop ? 16 : 14),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: p.cardBorder, width: 1),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Cabecera de la sección
          Row(
            children: [
              Icon(
                Icons.calculate_outlined,
                size: 16,
                color: accent,
              ),
              const SizedBox(width: 7),
              Expanded(
                child: Text(
                  label.toUpperCase(),
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.9,
                    color: p.textSecondary,
                  ),
                ),
              ),
              if (problems.length > 1)
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 7,
                    vertical: 2,
                  ),
                  decoration: BoxDecoration(
                    color: accent.o(0.12),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Text(
                    '${problems.length} PROBLEMAS',
                    style: mono(
                      fontSize: 9,
                      fontWeight: FontWeight.w700,
                      color: accent,
                    ),
                  ),
                ),
            ],
          ),
          const SizedBox(height: 12),

          // Lista de Problemas
          for (var i = 0; i < problems.length; i++) ...[
            _ProblemSubCard(
              problem: problems[i],
              index: i + 1,
              accentColor: accent,
              isDark: isDark,
            ),
            if (i < problems.length - 1) const SizedBox(height: 12),
          ],
        ],
      ),
    );
  }

  List<_ParsedProblem> _parseProblems(String raw) {
    final text = raw.trim();
    final problemRegex = RegExp(
      r'(?:^|\n\n+)(?=(?:Problema|Ejercicio|Problem|Case)\s*\d+[:\.]?)',
      caseSensitive: false,
    );

    final chunks = text.split(problemRegex);
    final List<_ParsedProblem> list = [];

    for (final chunk in chunks) {
      final trimmed = chunk.trim();
      if (trimmed.isEmpty) continue;

      final lines = trimmed.split('\n');
      final headerLine = lines.first.trim();

      final headerMatch = RegExp(
        r'^(?:Problema|Ejercicio|Problem)\s*(\d+)(?:\s*\((.*?)\))?[:\.]?\s*(.*)',
        caseSensitive: false,
      ).firstMatch(headerLine);

      int num = list.length + 1;
      String subTitle = '';
      String statement = '';

      if (headerMatch != null) {
        num = int.tryParse(headerMatch.group(1) ?? '') ?? (list.length + 1);
        subTitle = (headerMatch.group(2) ?? '').trim();
        statement = (headerMatch.group(3) ?? '').trim();
      } else {
        statement = headerLine;
      }

      final bodyLines = lines.skip(1).toList();
      final List<_ParsedStep> steps = [];
      _ParsedStep currentStep = _ParsedStep(
        label: '',
        lines: [],
      );

      final stepRegex = RegExp(
        r'^(Paso\s*\d+|Step\s*\d+)[:\.]?\s*(.*)',
        caseSensitive: false,
      );

      for (final bl in bodyLines) {
        final blTrimmed = bl.trim();
        if (blTrimmed.isEmpty) continue;

        final stepMatch = stepRegex.firstMatch(blTrimmed);
        if (stepMatch != null) {
          if (currentStep.lines.isNotEmpty || currentStep.label.isNotEmpty) {
            steps.add(currentStep);
          }
          final stepNum = (stepMatch.group(1) ?? 'PASO').toUpperCase();
          final stepInitial = (stepMatch.group(2) ?? '').trim();
          currentStep = _ParsedStep(
            label: stepNum,
            lines: stepInitial.isNotEmpty ? [stepInitial] : [],
          );
        } else {
          currentStep.lines.add(blTrimmed);
        }
      }

      if (currentStep.lines.isNotEmpty || currentStep.label.isNotEmpty) {
        steps.add(currentStep);
      }

      list.add(
        _ParsedProblem(
          number: num,
          title: subTitle,
          statement: statement,
          steps: steps,
        ),
      );
    }

    if (list.isEmpty) {
      list.add(
        _ParsedProblem(
          number: 1,
          title: '',
          statement: text,
          steps: const [],
        ),
      );
    }

    return list;
  }
}

class _ParsedProblem {
  const _ParsedProblem({
    required this.number,
    required this.title,
    required this.statement,
    required this.steps,
  });

  final int number;
  final String title;
  final String statement;
  final List<_ParsedStep> steps;
}

class _ParsedStep {
  _ParsedStep({
    required this.label,
    required this.lines,
  });

  final String label;
  final List<String> lines;
}

class _ProblemSubCard extends StatelessWidget {
  const _ProblemSubCard({
    required this.problem,
    required this.index,
    required this.accentColor,
    required this.isDark,
  });

  final _ParsedProblem problem;
  final int index;
  final Color accentColor;
  final bool isDark;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final cardBg = isDark ? const Color(0xFF121316) : const Color(0xFFF7F8FA);
    final cardBorder = isDark ? const Color(0xFF1E222B) : const Color(0xFFE2E4E9);

    return Container(
      decoration: BoxDecoration(
        color: cardBg,
        borderRadius: BorderRadius.circular(15),
        border: Border.all(color: cardBorder, width: 1),
      ),
      padding: const EdgeInsets.all(14),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Cabecera del Problema
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 8,
                  vertical: 3,
                ),
                decoration: BoxDecoration(
                  color: accentColor.o(0.15),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  'PROBLEMA ${problem.number.toString().padLeft(2, '0')}',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    color: accentColor,
                  ),
                ),
              ),
              if (problem.title.isNotEmpty) ...[
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    problem.title,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 12.5,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.2,
                      color: p.textPrimary,
                    ),
                  ),
                ),
              ],
            ],
          ),

          // Enunciado del Problema
          if (problem.statement.isNotEmpty) ...[
            const SizedBox(height: 9),
            _AcademicRichText(
              text: problem.statement,
              textColor: p.textPrimary,
              fontSize: 13.5,
              height: 1.6,
              accentColor: accentColor,
              isDark: isDark,
            ),
          ],

          // Pasos del Desarrollo
          if (problem.steps.isNotEmpty) ...[
            const SizedBox(height: 12),
            Container(height: 1, color: cardBorder),
            const SizedBox(height: 10),
            for (var sIdx = 0; sIdx < problem.steps.length; sIdx++) ...[
              _StepView(
                step: problem.steps[sIdx],
                accentColor: accentColor,
                isDark: isDark,
              ),
              if (sIdx < problem.steps.length - 1) ...[
                const SizedBox(height: 10),
                Divider(
                  height: 1,
                  thickness: 0.6,
                  color: cardBorder.o(0.7),
                ),
                const SizedBox(height: 10),
              ],
            ],
          ],
        ],
      ),
    );
  }
}

class _StepView extends StatelessWidget {
  const _StepView({
    required this.step,
    required this.accentColor,
    required this.isDark,
  });

  final _ParsedStep step;
  final Color accentColor;
  final bool isDark;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (step.label.isNotEmpty) ...[
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 2.5),
            decoration: BoxDecoration(
              color: accentColor.o(0.12),
              borderRadius: BorderRadius.circular(5),
              border: Border.all(color: accentColor.o(0.35), width: 0.8),
            ),
            child: Text(
              step.label,
              style: mono(
                fontSize: 9,
                fontWeight: FontWeight.w700,
                color: accentColor,
              ),
            ),
          ),
          const SizedBox(height: 6),
        ],

        for (final line in step.lines)
          _buildLine(context, line),
      ],
    );
  }

  Widget _buildLine(BuildContext context, String line) {
    final p = context.palette;
    final trimmed = line.trim();
    if (trimmed.isEmpty) return const SizedBox.shrink();

    // Comprobar si la línea es un bloque de cálculo matemático puro
    final isCalculationLine = _isMathCalculation(trimmed);

    if (isCalculationLine) {
      final latex = _formatLineToLatex(trimmed);
      return Container(
        width: double.infinity,
        margin: const EdgeInsets.symmetric(vertical: 4),
        padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 7),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF11131A) : const Color(0xFFF1F3F7),
          borderRadius: BorderRadius.circular(8),
          border: Border(
            left: BorderSide(color: accentColor, width: 3),
            top: BorderSide(
              color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE2E4E9),
            ),
            right: BorderSide(
              color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE2E4E9),
            ),
            bottom: BorderSide(
              color: isDark ? const Color(0xFF1E222B) : const Color(0xFFE2E4E9),
            ),
          ),
        ),
        child: SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          child: Math.tex(
            latex,
            mathStyle: MathStyle.display,
            textStyle: TextStyle(
              fontSize: 13,
              color: isDark ? Colors.white : p.textPrimary,
            ),
            onErrorFallback: (_) => Text(
              trimmed,
              style: mono(fontSize: 11.5, color: p.textPrimary),
            ),
          ),
        ),
      );
    }

    return Padding(
      padding: const EdgeInsets.only(bottom: 4),
      child: _AcademicRichText(
        text: trimmed,
        textColor: p.textBody,
        fontSize: 13,
        height: 1.55,
        accentColor: accentColor,
        isDark: isDark,
      ),
    );
  }

  bool _isMathCalculation(String line) {
    if (line.startsWith(r'$$') && line.endsWith(r'$$')) return true;
    if (line.startsWith(r'$') && line.endsWith(r'$')) return true;
    final hasEquals = line.contains('=');
    final hasArrow = line.contains('=>') || line.contains(r'\implies');
    final hasMathSymbols = line.contains(r'\angle') ||
        line.contains('∠') ||
        line.contains(r'\frac') ||
        line.contains(r'\int') ||
        line.contains('dv/dt') ||
        line.contains('di/dt') ||
        line.contains('10⁻³') ||
        line.contains('10⁻²');
    return (hasEquals || hasArrow) && hasMathSymbols;
  }

  String _formatLineToLatex(String line) {
    var s = line.trim();
    if (s.startsWith(r'$$') && s.endsWith(r'$$')) {
      return s.substring(2, s.length - 2).trim();
    }
    if (s.startsWith(r'$') && s.endsWith(r'$')) {
      return s.substring(1, s.length - 1).trim();
    }
    if (s.startsWith('- ')) s = s.substring(2).trim();

    s = s
        .replaceAll('=>', r'\implies ')
        .replaceAll('->', r'\rightarrow ')
        .replaceAll('10⁻⁶', r'10^{-6}')
        .replaceAll('10⁻³', r'10^{-3}')
        .replaceAll('10⁻²', r'10^{-2}')
        .replaceAll('²', '^2')
        .replaceAll('³', '^3')
        .replaceAll('dv(t)/dt', r'\frac{dv(t)}{dt}')
        .replaceAll('di(t)/dt', r'\frac{di(t)}{dt}')
        .replaceAll('dv/dt', r'\frac{dv}{dt}')
        .replaceAll('di/dt', r'\frac{di}{dt}')
        .replaceAll('Ω', r'\ \Omega')
        .replaceAll('∠', r'\angle ')
        .replaceAll(' * ', r' \cdot ');

    return InstitutionalValidator.sanitizeLatex(s);
  }
}

class _AcademicRichText extends StatelessWidget {
  const _AcademicRichText({
    required this.text,
    required this.textColor,
    required this.fontSize,
    required this.height,
    required this.accentColor,
    required this.isDark,
  });

  final String text;
  final Color textColor;
  final double fontSize;
  final double height;
  final Color accentColor;
  final bool isDark;

  @override
  Widget build(BuildContext context) {
    final tokens = _tokenize(text);
    final spans = <InlineSpan>[];

    for (final token in tokens) {
      if (token.type == _AcademicTokenType.inlineMath) {
        final cleanTex = InstitutionalValidator.sanitizeLatex(token.content);
        spans.add(
          WidgetSpan(
            alignment: PlaceholderAlignment.middle,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 2),
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
      } else if (token.type == _AcademicTokenType.bold) {
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

  List<_AcademicToken> _tokenize(String text) {
    final pattern = RegExp(
      r'(\$\$.*?\$\$|\$.*?\$|\*\*.*?\*\*)',
      dotAll: true,
    );

    final List<_AcademicToken> tokens = [];
    int lastEnd = 0;

    for (final match in pattern.allMatches(text)) {
      if (match.start > lastEnd) {
        tokens.add(
          _AcademicToken(
            type: _AcademicTokenType.text,
            content: text.substring(lastEnd, match.start),
          ),
        );
      }

      final raw = match.group(0)!;
      if (raw.startsWith(r'$$') && raw.endsWith(r'$$')) {
        tokens.add(
          _AcademicToken(
            type: _AcademicTokenType.inlineMath,
            content: raw.substring(2, raw.length - 2).trim(),
          ),
        );
      } else if (raw.startsWith(r'$') && raw.endsWith(r'$')) {
        tokens.add(
          _AcademicToken(
            type: _AcademicTokenType.inlineMath,
            content: raw.substring(1, raw.length - 1).trim(),
          ),
        );
      } else if (raw.startsWith(r'**') && raw.endsWith(r'**')) {
        tokens.add(
          _AcademicToken(
            type: _AcademicTokenType.bold,
            content: raw.substring(2, raw.length - 2),
          ),
        );
      }

      lastEnd = match.end;
    }

    if (lastEnd < text.length) {
      tokens.add(
        _AcademicToken(
          type: _AcademicTokenType.text,
          content: text.substring(lastEnd),
        ),
      );
    }

    return tokens;
  }
}

enum _AcademicTokenType { text, bold, inlineMath }

class _AcademicToken {
  const _AcademicToken({
    required this.type,
    required this.content,
  });

  final _AcademicTokenType type;
  final String content;
}
