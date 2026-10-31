import '../constants/app_constants.dart';

/// Utilidades de validación institucional `@unimagdalena.edu.co`,
/// sanitización de expresiones LaTeX y formateo de tamaños de archivo.
abstract final class InstitutionalValidator {
  /// Expresión regular estricta para correos institucionales de Unimagdalena.
  static final RegExp _institutionalEmailRegex = RegExp(
    r'^[a-zA-Z0-9._%+-]+@unimagdalena\.edu\.co$',
    caseSensitive: false,
  );

  /// Expresión regular para detectar fórmulas inline `$...$` en notas.
  static final RegExp inlineLatexRegex = RegExp(r'\$([^$\n]+)\$');

  /// Verifica si el correo pertenece exclusivamente a `@unimagdalena.edu.co`.
  static bool isValidInstitutionalEmail(String email) {
    final trimmed = email.trim();
    if (trimmed.isEmpty) return false;
    return _institutionalEmailRegex.hasMatch(trimmed);
  }

  /// Valida y devuelve un mensaje de error legible o `null` si es válido.
  static String? validateEmailOrError(String email) {
    final trimmed = email.trim();
    if (trimmed.isEmpty) {
      return 'Ingresa tu correo institucional.';
    }
    if (!isValidInstitutionalEmail(trimmed)) {
      return 'Acceso restringido al dominio ${AppConstants.institutionalDomain}';
    }
    return null;
  }

  /// Limpia delimitadores LaTeX envolventes (`$$...$$` o `$...$`) para
  /// compilarlos directamente en `flutter_math_fork`.
  static String sanitizeLatex(String raw) {
    var clean = raw.trim();
    if (clean.startsWith(r'$$') && clean.endsWith(r'$$') && clean.length > 4) {
      clean = clean.substring(2, clean.length - 2).trim();
    } else if (clean.startsWith(r'$') &&
        clean.endsWith(r'$') &&
        clean.length > 2) {
      clean = clean.substring(1, clean.length - 1).trim();
    }
    return clean;
  }

  /// Extrae todas las expresiones matemáticas `$...$` de un bloque de texto.
  static List<String> extractInlineLatexExpressions(String text) {
    return inlineLatexRegex
        .allMatches(text)
        .map((m) => m.group(1)?.trim() ?? '')
        .where((s) => s.isNotEmpty)
        .toList(growable: false);
  }

  /// Formatea un tamaño en bytes a `B`, `KB` o `MB`.
  static String formatByteSize(int? bytes) {
    final total = bytes ?? 0;
    if (total <= 0) return '0 KB';
    if (total < 1024) return '$total B';
    final kb = total / 1024;
    if (kb < 1024) {
      return kb >= 100 ? '${kb.round()} KB' : '${kb.toStringAsFixed(1)} KB';
    }
    final mb = kb / 1024;
    return '${mb.toStringAsFixed(2)} MB';
  }
}
