import 'dart:js_interop';

@JS('eval')
external JSAny? _jsEval(JSString script);

class FullscreenHelper {
  static void toggle() {
    try {
      _jsEval(
        '(function() { '
        'if (!document.fullscreenElement) { '
        '  if (document.documentElement.requestFullscreen) { '
        '    document.documentElement.requestFullscreen().catch(function(){}); '
        '  } '
        '} else { '
        '  if (document.exitFullscreen) { '
        '    document.exitFullscreen().catch(function(){}); '
        '  } '
        '} '
        '})()'.toJS,
      );
    } catch (_) {}
  }

  static bool get isFullscreen {
    try {
      final res = _jsEval('!!document.fullscreenElement'.toJS);
      return (res as JSBoolean?)?.toDart ?? false;
    } catch (_) {
      return false;
    }
  }
}
