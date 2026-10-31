import 'dart:convert';
import 'dart:math' as math;
import 'package:crypto/crypto.dart';

/// Sistema de cifrado autenticado simétrico (CTR + HMAC-SHA256 Encrypt-then-MAC)
/// para proteger los datos privados de los estudiantes (`progreso_materias`,
/// `recordatorios_calendario` y `apuntes_personales`) antes de guardarlos
/// en el repositorio público de GitHub (`db/users/{username}.json`).
abstract final class UserPayloadCipher {
  /// Prefijo de versión de payload cifrado.
  static const String prefix = 'enc:v1:';

  /// Salt de aplicación para derivación de claves simétricas.
  static const String appSalt = 'um_studio_plan8108_salt_2026';

  /// Deriva una clave de 256 bits a partir de `salt + username + pinOrHash`.
  static List<int> deriveKey(String username, String pinOrHash) {
    final cleanUser = username.trim().toLowerCase();
    final cleanPin = pinOrHash.trim();
    final seed = '$appSalt:$cleanUser:$cleanPin';
    return sha256.convert(utf8.encode(seed)).bytes;
  }

  /// Cifra cualquier estructura JSON (Map, List, String) devolviendo una cadena
  /// `enc:v1:<base64(IV || HMAC_TAG_16 || CIPHERTEXT)>`.
  static String encryptJson(
    dynamic data, {
    required String username,
    required String pinOrHash,
  }) {
    if (data == null) return '';
    final plaintext = jsonEncode(data);
    final plainBytes = utf8.encode(plaintext);
    if (plainBytes.isEmpty) return '';

    final key = deriveKey(username, pinOrHash);
    final hmac = Hmac(sha256, key);

    // Generar IV seguro de 16 bytes
    final rand = math.Random.secure();
    final iv = List<int>.generate(16, (_) => rand.nextInt(256));

    final cipherBytes = List<int>.filled(plainBytes.length, 0);

    // CTR Keystream con HMAC-SHA256
    var blockIndex = 0;
    for (var offset = 0; offset < plainBytes.length; offset += 32) {
      final counterBytes = _uint32ToBytes(blockIndex);
      final blockKey = hmac.convert([...iv, ...counterBytes]).bytes;
      for (var i = 0; i < 32 && (offset + i) < plainBytes.length; i++) {
        cipherBytes[offset + i] = plainBytes[offset + i] ^ blockKey[i];
      }
      blockIndex++;
    }

    // Tag autenticado HMAC-SHA256 (16 bytes) sobre IV + Ciphertext
    final tag = hmac.convert([...iv, ...cipherBytes]).bytes.sublist(0, 16);
    final combined = [...iv, ...tag, ...cipherBytes];

    return '$prefix${base64Encode(combined)}';
  }

  /// Descifra un payload cifrado. Si `raw` no está cifrado (es un Map o List legado),
  /// lo devuelve directamente sin alterar para retrocompatibilidad total.
  static dynamic decryptJson(
    dynamic raw, {
    required String username,
    required String pinOrHash,
  }) {
    if (raw == null) return null;
    if (raw is! String) {
      // Dato legado en texto plano (Map o List)
      return raw;
    }

    final str = raw.trim();
    if (!str.startsWith(prefix)) {
      // Cadena en texto plano o JSON serializado
      try {
        return jsonDecode(str);
      } catch (_) {
        return str;
      }
    }

    try {
      final b64 = str.substring(prefix.length);
      final rawBytes = base64Decode(b64);
      if (rawBytes.length < 32) return null;

      final iv = rawBytes.sublist(0, 16);
      final tag = rawBytes.sublist(16, 32);
      final cipherBytes = rawBytes.sublist(32);

      final key = deriveKey(username, pinOrHash);
      final hmac = Hmac(sha256, key);

      // Verificación de integridad y autenticidad (Encrypt-then-MAC)
      final expectedTag =
          hmac.convert([...iv, ...cipherBytes]).bytes.sublist(0, 16);
      if (!_constantTimeCompare(tag, expectedTag)) {
        return null;
      }

      final plainBytes = List<int>.filled(cipherBytes.length, 0);
      var blockIndex = 0;
      for (var offset = 0; offset < cipherBytes.length; offset += 32) {
        final counterBytes = _uint32ToBytes(blockIndex);
        final blockKey = hmac.convert([...iv, ...counterBytes]).bytes;
        for (var i = 0; i < 32 && (offset + i) < cipherBytes.length; i++) {
          plainBytes[offset + i] = cipherBytes[offset + i] ^ blockKey[i];
        }
        blockIndex++;
      }

      final jsonStr = utf8.decode(plainBytes);
      return jsonDecode(jsonStr);
    } catch (_) {
      return null;
    }
  }

  static List<int> _uint32ToBytes(int value) {
    return [
      (value >> 24) & 0xFF,
      (value >> 16) & 0xFF,
      (value >> 8) & 0xFF,
      value & 0xFF,
    ];
  }

  static bool _constantTimeCompare(List<int> a, List<int> b) {
    if (a.length != b.length) return false;
    var result = 0;
    for (var i = 0; i < a.length; i++) {
      result |= a[i] ^ b[i];
    }
    return result == 0;
  }
}
