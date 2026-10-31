import 'dart:async';
import 'dart:js_interop';

@JS('window.open')
external JSObject? _windowOpen(JSString url, JSString target, JSString features);

@JS('window.addEventListener')
external void _addEventListener(JSString type, JSFunction listener);

@JS('window.removeEventListener')
external void _removeEventListener(JSString type, JSFunction listener);

@JS('window.location.search')
external JSString get _windowSearch;

@JS('window.location.href')
external set _windowHref(JSString url);

@JS('window.history.replaceState')
external void _replaceState(JSAny? state, JSString title, JSString url);

extension type _JSMessageEvent(JSObject _) implements JSObject {
  external JSAny? get data;
}

extension type _JSAuthMessageData(JSObject _) implements JSObject {
  external JSString? get type;
  external JSString? get search;
  external JSString? get hash;
}

class OAuthPlatformDelegate {
  Future<String?> authorize({
    required String authUrl,
    required String redirectUri,
    required String expectedState,
  }) async {
    final completer = Completer<String?>();

    final listener = ((_JSMessageEvent event) {
      try {
        final data = event.data;
        if (data != null) {
          final obj = _JSAuthMessageData(data as JSObject);
          final type = obj.type?.toDart;
          if (type == 'MS_ENTRA_AUTH_CALLBACK') {
            final search = obj.search?.toDart ?? '';
            final uri = Uri.parse('https://dummy.local/$search');
            final code = uri.queryParameters['code'];
            final state = uri.queryParameters['state'];
            if (state == expectedState && code != null && !completer.isCompleted) {
              completer.complete(code);
            }
          }
        }
      } catch (_) {}
    }).toJS;

    _addEventListener('message'.toJS, listener);

    try {
      final popup = _windowOpen(
        authUrl.toJS,
        'MicrosoftEntraAuth'.toJS,
        'width=600,height=720,menubar=no,toolbar=no,status=no'.toJS,
      );

      // Si el navegador bloqueó el popup, redirigimos en la misma ventana
      if (popup == null) {
        _windowHref = authUrl.toJS;
        return null;
      }
    } catch (_) {
      _windowHref = authUrl.toJS;
      return null;
    }

    // Timeout de 3 minutos por si el usuario cierra el popup manualmente
    final timer = Timer(const Duration(minutes: 3), () {
      if (!completer.isCompleted) {
        completer.complete(null);
      }
    });

    final result = await completer.future;
    timer.cancel();
    _removeEventListener('message'.toJS, listener);
    return result;
  }

  String? getInitialAuthCode() {
    try {
      final search = _windowSearch.toDart;
      if (search.contains('code=')) {
        final uri = Uri.parse('https://dummy.local/$search');
        return uri.queryParameters['code'];
      }
    } catch (_) {}
    return null;
  }

  String? getInitialState() {
    try {
      final search = _windowSearch.toDart;
      if (search.contains('state=')) {
        final uri = Uri.parse('https://dummy.local/$search');
        return uri.queryParameters['state'];
      }
    } catch (_) {}
    return null;
  }

  void cleanUrl(String cleanPath) {
    try {
      _replaceState(null, ''.toJS, cleanPath.toJS);
    } catch (_) {}
  }
}

OAuthPlatformDelegate getOAuthPlatformDelegate() => OAuthPlatformDelegate();
