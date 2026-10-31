import 'dart:convert';
import 'dart:js_interop';
import 'dart:typed_data';

@JS('document.createElement')
external _JSAnchorElement _createElement(JSString tagName);

@JS('document.body.appendChild')
external JSAny? _appendChild(_JSAnchorElement element);

@JS('document.body.removeChild')
external JSAny? _removeChild(_JSAnchorElement element);

extension type _JSAnchorElement._(JSObject _) implements JSObject {
  external set href(JSString value);
  external set download(JSString value);
  external void click();
}

/// Descarga instantánea de PDF en navegadores Web (Chrome, Safari iOS, Edge)
/// usando Data URI `application/pdf` sin dependencias externas pesadas.
Future<String?> savePdfBytesToPlatform({
  required String fileName,
  required Uint8List bytes,
}) async {
  try {
    final safeName = fileName.replaceAll(RegExp(r'[^a-zA-Z0-9._-]'), '_');
    final b64 = base64Encode(bytes);
    final anchor = _createElement('a'.toJS);
    anchor.href = 'data:application/pdf;base64,$b64'.toJS;
    anchor.download = safeName.toJS;
    _appendChild(anchor);
    anchor.click();
    _removeChild(anchor);
    return safeName;
  } catch (_) {
    return null;
  }
}
