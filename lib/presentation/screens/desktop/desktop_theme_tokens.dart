import 'package:flutter/material.dart';

import '../../providers/app_scopes.dart';

/// Design tokens oficiales Apple HIG para la interfaz de escritorio de UM Studio.
/// Proporciona soporte bidireccional instantáneo para Modo Oscuro OLED y Modo Claro.
class DesktopThemeTokens {
  const DesktopThemeTokens({
    required this.isDark,
    required this.canvas,
    required this.surface,
    required this.surfaceElevated,
    required this.border,
    required this.borderSubtle,
    required this.textPrimary,
    required this.textSecondary,
    required this.textTertiary,
    required this.accentGreen,
    required this.accentIndigo,
    required this.alertAmber,
    required this.shadowColor,
  });

  final bool isDark;

  /// Fondo base: OLED #000000 / Light #F2F2F7
  final Color canvas;

  /// Superficie de tarjetas: #0D0E12 (85% opacidad) / #FFFFFF (90% opacidad)
  final Color surface;

  /// Superficie elevada: #141720 / #F7F7FA
  final Color surfaceElevated;

  /// Borde estándar de tarjetas: #1A1D24 / #E5E5EA
  final Color border;

  /// Borde sutil: #14161C / #EBEBF0
  final Color borderSubtle;

  /// Texto primario: #FFFFFF / #000000
  final Color textPrimary;

  /// Texto secundario: #8E8E93 / #636366
  final Color textSecondary;

  /// Texto terciario: #636366 / #8E8E93
  final Color textTertiary;

  /// Acento primario (Verde esmeralda): #30D158 / #28CD41
  final Color accentGreen;

  /// Acento secundario (Índigo): #5E5CE6 / #5856D6
  final Color accentIndigo;

  /// Alerta / Examen (Ámbar): #FF9F0A / #FF9500
  final Color alertAmber;

  /// Sombra ambiental
  final Color shadowColor;

  static DesktopThemeTokens of(BuildContext context) {
    final isDark = ThemeScope.maybeOf(context)?.isDark ?? true;
    if (isDark) {
      return const DesktopThemeTokens(
        isDark: true,
        canvas: Color(0xFF000000),
        surface: Color(0xD90A0B0E),
        surfaceElevated: Color(0xFF12141A),
        border: Color(0xFF1E212A),
        borderSubtle: Color(0xFF14161C),
        textPrimary: Color(0xFFFFFFFF),
        textSecondary: Color(0xFF8E8E93),
        textTertiary: Color(0xFF636366),
        accentGreen: Color(0xFF30D158),
        accentIndigo: Color(0xFF5E5CE6),
        alertAmber: Color(0xFFFF9F0A),
        shadowColor: Color(0x66000000),
      );
    } else {
      return const DesktopThemeTokens(
        isDark: false,
        canvas: Color(0xFFF2F2F7),
        surface: Color(0xFFFFFFFF),
        surfaceElevated: Color(0xFFF7F7FA),
        border: Color(0xFFE5E5EA),
        borderSubtle: Color(0xFFEBEBF0),
        textPrimary: Color(0xFF000000),
        textSecondary: Color(0xFF636366),
        textTertiary: Color(0xFF8E8E93),
        accentGreen: Color(0xFF28CD41),
        accentIndigo: Color(0xFF5856D6),
        alertAmber: Color(0xFFFF9500),
        shadowColor: Color(0x0A000000),
      );
    }
  }
}
