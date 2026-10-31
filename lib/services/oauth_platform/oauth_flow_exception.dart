/// Error controlado del flujo interactivo OAuth (cancelación, rechazo,
/// error devuelto por Microsoft Entra ID o tiempo de espera agotado).
class OAuthFlowException implements Exception {
  const OAuthFlowException(this.message, {this.code});

  /// Mensaje legible en español para mostrar al estudiante.
  final String message;

  /// Código técnico opcional (`access_denied`, `popup_closed`, `timeout`, ...).
  final String? code;

  @override
  String toString() => message;

  /// Traduce los errores estándar de OAuth 2.0 / Entra ID a mensajes claros.
  static OAuthFlowException fromOAuthError(String error, String? description) {
    final desc = (description ?? '').trim();
    String msg;
    switch (error) {
      case 'access_denied':
        msg = 'Cancelaste el inicio de sesión o no se otorgaron los permisos.';
        break;
      case 'consent_required':
      case 'interaction_required':
        msg = 'Tu institución requiere aprobar la app "UM Studio" antes de usarla. '
            'Pide a un administrador de TI que otorgue el consentimiento.';
        break;
      case 'login_required':
        msg = 'Debes iniciar sesión nuevamente con tu cuenta institucional.';
        break;
      case 'invalid_request':
      case 'unauthorized_client':
        msg = 'La configuración de inicio de sesión no es válida para esta dirección.';
        break;
      case 'temporarily_unavailable':
      case 'server_error':
        msg = 'Microsoft no está disponible en este momento. Intenta más tarde.';
        break;
      default:
        msg = 'Microsoft rechazó el inicio de sesión ($error).';
    }
    if (desc.isNotEmpty) {
      // Las descripciones de Entra traen "AADSTSxxxx: texto. Trace ID: ..."
      final short = desc.split(RegExp(r'\r?\n|Trace ID')).first.trim();
      if (short.isNotEmpty) msg = '$msg\n$short';
    }
    return OAuthFlowException(msg, code: error);
  }
}
