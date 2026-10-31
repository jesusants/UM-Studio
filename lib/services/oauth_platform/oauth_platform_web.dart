import 'dart:async';
import 'dart:js_interop';

import 'oauth_flow_exception.dart';

@JS('window.open')
external _JSWindow? _windowOpen(JSString url, JSString target, JSString features);

@JS('window.addEventListener')
external void _addEventListener(JSString type, JSFunction listener);

@JS('window.removeEventListener')
external void _removeEventListener(JSString type, JSFunction listener);

@JS('window.location.search')
external JSString get _windowSearch;

@JS('window.__UM_INITIAL_SEARCH__')
external JSString? get _initialSearch;

@JS('window.location.href')
external set _windowHref(JSString url);

@JS('window.history.replaceState')
external void _replaceState(JSAny? state, JSString title, JSString url);

@JS('window.localStorage.getItem')
external JSString? _lsGet(JSString key);

@JS('window.localStorage.setItem')
external void _lsSet(JSString key, JSString value);

@JS('window.localStorage.removeItem')
external void _lsRemove(JSString key);

extension type _JSWindow(JSObject _) implements JSObject {
  external bool get closed;
  external void close();
  external void focus();
  external _JSLocation get location;
}

extension type _JSLocation(JSObject _) implements JSObject {
  external JSString get href;
}

extension type _JSMessageEvent(JSObject _) implements JSObject {
  external JSAny? get data;
}

extension type _JSAuthMessageData(JSObject _) implements JSObject {
  external JSString? get type;
  external JSString? get search;
  external JSString? get hash;
}

/// Claves compartidas con el interceptor pre-Flutter de `web/index.html`.
const _kPendingState = 'um_entra_pending_state';
const _kAuthResult = 'um_entra_auth_result';
const _kAuthMode = 'um_entra_auth_mode';

class OAuthPlatformDelegate {
  /// Tiempo máximo total que se espera la respuesta de Microsoft.
  static const Duration _overallTimeout = Duration(minutes: 2);

  /// Margen tras detectar el popup cerrado para recibir un resultado tardío.
  static const Duration _closedGrace = Duration(milliseconds: 1500);

  void _safeLsSet(String k, String v) {
    try {
      _lsSet(k.toJS, v.toJS);
    } catch (_) {}
  }

  String? _safeLsGet(String k) {
    try {
      return _lsGet(k.toJS)?.toDart;
    } catch (_) {
      return null;
    }
  }

  void _safeLsRemove(String k) {
    try {
      _lsRemove(k.toJS);
    } catch (_) {}
  }

  Future<String?> authorize({
    required String authUrl,
    required String redirectUri,
    required String expectedState,
  }) async {
    final completer = Completer<String?>();

    // Limpia restos de intentos anteriores y registra el intento actual.
    _safeLsRemove(_kAuthResult);
    _safeLsSet(_kPendingState, expectedState);
    _safeLsSet(_kAuthMode, 'popup');

    /// Procesa una query `?code=...&state=...` o `?error=...` venga de donde venga.
    void handleSearch(String search) {
      if (completer.isCompleted || search.isEmpty) return;
      final uri = Uri.parse(
        'https://dummy.local/${search.startsWith('?') ? search : '?$search'}',
      );
      final qp = uri.queryParameters;
      final state = qp['state'];
      if (state != null && state != expectedState) return; // otro intento
      final error = qp['error'];
      if (error != null && error.isNotEmpty) {
        completer.completeError(
          OAuthFlowException.fromOAuthError(error, qp['error_description']),
        );
        return;
      }
      final code = qp['code'];
      if (code != null && code.isNotEmpty) {
        completer.complete(code);
      }
    }

    final listener = ((_JSMessageEvent event) {
      try {
        final data = event.data;
        if (data == null) return;
        final obj = _JSAuthMessageData(data as JSObject);
        if (obj.type?.toDart == 'MS_ENTRA_AUTH_CALLBACK') {
          handleSearch(obj.search?.toDart ?? '');
        }
      } catch (_) {}
    }).toJS;

    _addEventListener('message'.toJS, listener);

    _JSWindow? popup;
    try {
      popup = _windowOpen(
        authUrl.toJS,
        'MicrosoftEntraAuth'.toJS,
        'width=600,height=720,menubar=no,toolbar=no,status=no'.toJS,
      );
    } catch (_) {
      popup = null;
    }

    // Si el navegador bloqueó el popup, redirigimos en la misma ventana.
    // Al volver, `SessionController.load()` canjea el código o muestra el error.
    if (popup == null) {
      _removeEventListener('message'.toJS, listener);
      _safeLsSet(_kAuthMode, 'redirect');
      _windowHref = authUrl.toJS;
      return null;
    }

    final startedAt = DateTime.now();
    DateTime? closedAt;

    // Sondeo cada 500 ms: resultado por localStorage, URL del popup al volver
    // a nuestro dominio, cierre manual de la ventana y tiempo de espera.
    final poller = Timer.periodic(const Duration(milliseconds: 500), (t) {
      if (completer.isCompleted) {
        t.cancel();
        return;
      }

      // 1. Resultado escrito por el interceptor de index.html
      final stored = _safeLsGet(_kAuthResult);
      if (stored != null && stored.isNotEmpty) {
        handleSearch(stored);
        if (completer.isCompleted) return;
      }

      // 2. El popup volvió a nuestro origen (lectura same-origin permitida)
      try {
        final href = popup!.location.href.toDart;
        final idx = href.indexOf('?');
        if (idx != -1 &&
            (href.contains('code=') || href.contains('error='))) {
          handleSearch(href.substring(idx).split('#').first);
          if (completer.isCompleted) {
            try {
              popup.close();
            } catch (_) {}
            return;
          }
        }
      } catch (_) {
        // Cross-origin mientras está en login.microsoftonline.com: normal.
      }

      // 3. Ventana cerrada por el usuario (o tras un error mostrado por Microsoft)
      bool isClosed = false;
      try {
        isClosed = popup!.closed;
      } catch (_) {}
      if (isClosed) {
        closedAt ??= DateTime.now();
        if (DateTime.now().difference(closedAt!) >= _closedGrace) {
          completer.completeError(const OAuthFlowException(
            'Se cerró la ventana de Microsoft antes de completar el inicio de sesión.',
            code: 'popup_closed',
          ));
        }
        return;
      }

      // 4. Tiempo máximo agotado
      if (DateTime.now().difference(startedAt) >= _overallTimeout) {
        try {
          popup!.close();
        } catch (_) {}
        completer.completeError(const OAuthFlowException(
          'El inicio de sesión con Microsoft tardó demasiado. Inténtalo de nuevo.',
          code: 'timeout',
        ));
      }
    });

    try {
      return await completer.future;
    } finally {
      poller.cancel();
      _removeEventListener('message'.toJS, listener);
      _safeLsRemove(_kAuthResult);
      _safeLsRemove(_kPendingState);
      _safeLsRemove(_kAuthMode);
    }
  }

  String _bootSearch() {
    try {
      final initial = _initialSearch?.toDart ?? '';
      if (initial.isNotEmpty) return initial;
    } catch (_) {}
    try {
      return _windowSearch.toDart;
    } catch (_) {
      return '';
    }
  }

  Map<String, String> _bootParams() {
    final search = _bootSearch();
    if (search.isEmpty) return const {};
    try {
      return Uri.parse(
        'https://dummy.local/${search.startsWith('?') ? search : '?$search'}',
      ).queryParameters;
    } catch (_) {
      return const {};
    }
  }

  String? getInitialAuthCode() => _bootParams()['code'];

  String? getInitialState() => _bootParams()['state'];

  OAuthFlowException? getInitialError() {
    final qp = _bootParams();
    final error = qp['error'];
    if (error == null || error.isEmpty) return null;
    return OAuthFlowException.fromOAuthError(error, qp['error_description']);
  }

  void cleanUrl(String cleanPath) {
    try {
      _replaceState(null, ''.toJS, cleanPath.toJS);
    } catch (_) {}
    _safeLsRemove(_kAuthResult);
    _safeLsRemove(_kPendingState);
    _safeLsRemove(_kAuthMode);
  }
}

OAuthPlatformDelegate getOAuthPlatformDelegate() => OAuthPlatformDelegate();
