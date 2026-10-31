import 'dart:io';
import 'dart:typed_data';

/// Guardado local seguro en plataformas nativas (iOS, Android, Windows, macOS, Linux).
Future<String?> savePdfBytesToPlatform({
  required String fileName,
  required Uint8List bytes,
}) async {
  try {
    final safeName = fileName.replaceAll(RegExp(r'[^a-zA-Z0-9._-]'), '_');
    final dir = Directory('${Directory.systemTemp.path}/um_studio_slides');
    if (!dir.existsSync()) {
      dir.createSync(recursive: true);
    }
    final file = File('${dir.path}/$safeName');
    await file.writeAsBytes(bytes, flush: true);
    return file.path;
  } catch (_) {
    return null;
  }
}
