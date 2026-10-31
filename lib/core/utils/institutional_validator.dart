import 'dart:convert';

import 'package:crypto/crypto.dart';

import '../constants/app_constants.dart';

/// Resultado normalizado de credencial institucional `@unimagdalena.edu.co`.
class InstitutionalIdentity {
  const InstitutionalIdentity({
    required this.username,
    required this.email,
  });

  final String username;
  final String email;
}

/// Utilidades de validación institucional `@unimagdalena.edu.co`,
/// hashing ligero de PIN, sanitización de expresiones LaTeX y tamaños de archivo.
abstract final class InstitutionalValidator {
  /// Expresión regular estricta para correos institucionales de Unimagdalena.
  static final RegExp _institutionalEmailRegex = RegExp(
    r'^[a-zA-Z0-9._%+-]+@unimagdalena\.edu\.co$',
    caseSensitive: false,
  );

  /// Expresión regular para prefijo de usuario / código estudiantil seguro para ruta JSON.
  static final RegExp _usernameRegex = RegExp(r'^[a-zA-Z0-9._-]+$');

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
      return 'Ingresa tu usuario o correo institucional.';
    }
    if (!isValidInstitutionalEmail(trimmed)) {
      return 'Acceso restringido al dominio ${AppConstants.institutionalDomain}';
    }
    return null;
  }

  /// Acepta tanto el prefijo (`jsierra` o código `2024118001`) como el correo
  /// completo (`jsierra@unimagdalena.edu.co`), autocompletando el dominio
  /// oficial y bloqueando cualquier otro dominio externo.
  static ({InstitutionalIdentity? identity, String? error})
      parseInstitutionalUser(String rawInput) {
    final trimmed = rawInput.trim().toLowerCase();
    if (trimmed.isEmpty) {
      return (
        identity: null,
        error: 'Ingresa tu usuario o correo institucional.',
      );
    }

    String rawUsername;
    if (trimmed.contains('@')) {
      if (!isValidInstitutionalEmail(trimmed)) {
        return (
          identity: null,
          error:
              'Solo se permiten cuentas ${AppConstants.institutionalDomain}.',
        );
      }
      rawUsername = trimmed.split('@').first;
    } else {
      rawUsername = trimmed;
    }

    final username = rawUsername.replaceAll(RegExp(r'[^a-z0-9._-]'), '');
    final email = '$username${AppConstants.institutionalDomain}';

    if (username.length < 2 || !_usernameRegex.hasMatch(username)) {
      return (
        identity: null,
        error: 'Usa solo letras, números, punto o guion en tu usuario.',
      );
    }

    return (
      identity: InstitutionalIdentity(username: username, email: email),
      error: null,
    );
  }

  /// Genera un hash SHA-256 determinista para no exponer el PIN en texto plano
  /// dentro de `db/users/{username}.json`.
  static String hashPin(String rawPin) {
    final clean = rawPin.trim();
    final bytes = utf8.encode('um_studio_8108:$clean');
    return sha256.convert(bytes).toString();
  }

  /// Verifica un PIN contra `pin_hash` (soporta hash SHA-256 o PIN plano legado).
  static bool verifyPin(String inputPin, String storedPinHash) {
    final cleanInput = inputPin.trim();
    final cleanStored = storedPinHash.trim();
    if (cleanInput.isEmpty || cleanStored.isEmpty) return false;
    return hashPin(cleanInput) == cleanStored || cleanInput == cleanStored;
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
