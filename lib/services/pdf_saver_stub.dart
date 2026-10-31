import 'dart:typed_data';

/// Fallback multiplataforma para disparo de guardado de PDF.
Future<String?> savePdfBytesToPlatform({
  required String fileName,
  required Uint8List bytes,
}) async {
  return null;
}
