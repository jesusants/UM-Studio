import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Curvas físicas equivalentes a las transiciones nativas de iOS.
const Cubic kIosSpring = Cubic(0.32, 0.72, 0, 1);
const Cubic kPillEase = Cubic(0.25, 1, 0.5, 1);

extension ColorAlpha on Color {
  /// Aplica opacidad en rango `[0.0, 1.0]` sin pérdida de precisión.
  Color o(double opacity) => withAlpha((opacity * 255).round().clamp(0, 255));
}

/// Design Tokens estrictos iOS Minimalist OLED / Modo Claro.
@immutable
class AppPalette extends ThemeExtension<AppPalette> {
  const AppPalette({
    required this.background,
    required this.card,
    required this.cardBorder,
    required this.elevated,
    required this.strongBorder,
    required this.textPrimary,
    required this.textSecondary,
    required this.textTertiary,
    required this.textBody,
    required this.green,
    required this.orange,
    required this.indigo,
    required this.glass,
    required this.warmTop,
    required this.inverse,
    required this.onInverse,
    required this.shimmerBase,
    required this.shimmerHighlight,
  });

  final Color background;
  final Color card;
  final Color cardBorder;
  final Color elevated;
  final Color strongBorder;
  final Color textPrimary;
  final Color textSecondary;
  final Color textTertiary;
  final Color textBody;
  final Color green;
  final Color orange;
  final Color indigo;
  final Color glass;
  final Color warmTop;
  final Color inverse;
  final Color onInverse;
  final Color shimmerBase;
  final Color shimmerHighlight;

  /// Paleta obligatoria iOS OLED Dark Mode:
  /// Scaffold `#000000`, Card `#121316`, Border `#1F2228`, Esmeralda `#30D158`,
  /// Púrpura notas `#5E5CE6`, Gris neutro `#8E8E93`, Shimmer `#1A1D24`.
  static const dark = AppPalette(
    background: Color(0xFF000000),
    card: Color(0xFF121316),
    cardBorder: Color(0xFF1F2228),
    elevated: Color(0xFF1C1C1E),
    strongBorder: Color(0xFF2C2D35),
    textPrimary: Color(0xFFFFFFFF),
    textSecondary: Color(0xFF8E8E93),
    textTertiary: Color(0xFF636366),
    textBody: Color(0xFFD1D1D6),
    green: Color(0xFF30D158),
    orange: Color(0xFFFF9F0A),
    indigo: Color(0xFF5E5CE6),
    glass: Color(0xCC121316),
    warmTop: Color(0xFF191612),
    inverse: Color(0xFFFFFFFF),
    onInverse: Color(0xFF000000),
    shimmerBase: Color(0xFF1A1D24),
    shimmerHighlight: Color(0xFF252934),
  );

  /// Paleta equivalente iOS Light Mode:
  /// Scaffold `#FFFFFF`, superficies de tarjetas `#F2F2F7`.
  static const light = AppPalette(
    background: Color(0xFFFFFFFF),
    card: Color(0xFFF2F2F7),
    cardBorder: Color(0xFFE5E5EA),
    elevated: Color(0xFFE8E8ED),
    strongBorder: Color(0xFFD1D1D6),
    textPrimary: Color(0xFF000000),
    textSecondary: Color(0xFF6C6C70),
    textTertiary: Color(0xFF8E8E93),
    textBody: Color(0xFF3A3A3C),
    green: Color(0xFF30D158),
    orange: Color(0xFFFF9500),
    indigo: Color(0xFF5E5CE6),
    glass: Color(0xD9FFFFFF),
    warmTop: Color(0xFFFFF4E5),
    inverse: Color(0xFF000000),
    onInverse: Color(0xFFFFFFFF),
    shimmerBase: Color(0xFFE6E6EC),
    shimmerHighlight: Color(0xFFF3F3F8),
  );

  @override
  AppPalette copyWith() => this;

  @override
  AppPalette lerp(ThemeExtension<AppPalette>? other, double t) {
    if (other is! AppPalette) return this;
    Color l(Color a, Color b) => Color.lerp(a, b, t)!;
    return AppPalette(
      background: l(background, other.background),
      card: l(card, other.card),
      cardBorder: l(cardBorder, other.cardBorder),
      elevated: l(elevated, other.elevated),
      strongBorder: l(strongBorder, other.strongBorder),
      textPrimary: l(textPrimary, other.textPrimary),
      textSecondary: l(textSecondary, other.textSecondary),
      textTertiary: l(textTertiary, other.textTertiary),
      textBody: l(textBody, other.textBody),
      green: l(green, other.green),
      orange: l(orange, other.orange),
      indigo: l(indigo, other.indigo),
      glass: l(glass, other.glass),
      warmTop: l(warmTop, other.warmTop),
      inverse: l(inverse, other.inverse),
      onInverse: l(onInverse, other.onInverse),
      shimmerBase: l(shimmerBase, other.shimmerBase),
      shimmerHighlight: l(shimmerHighlight, other.shimmerHighlight),
    );
  }
}

extension PaletteContext on BuildContext {
  AppPalette get palette => Theme.of(this).extension<AppPalette>()!;
}

abstract final class AppTheme {
  static ThemeData get dark => _build(AppPalette.dark, Brightness.dark);
  static ThemeData get light => _build(AppPalette.light, Brightness.light);

  static ThemeData _build(AppPalette p, Brightness brightness) {
    final base = ThemeData(brightness: brightness, useMaterial3: true);
    return base.copyWith(
      scaffoldBackgroundColor: p.background,
      colorScheme: ColorScheme.fromSeed(
        seedColor: p.green,
        brightness: brightness,
      ).copyWith(surface: p.card),
      textTheme: GoogleFonts.interTextTheme(base.textTheme).apply(
        bodyColor: p.textPrimary,
        displayColor: p.textPrimary,
      ),
      splashFactory: NoSplash.splashFactory,
      highlightColor: Colors.transparent,
      hoverColor: Colors.transparent,
      extensions: <ThemeExtension<dynamic>>[p],
    );
  }
}

/// Fuente monoespaciada técnica (`JetBrains Mono`).
TextStyle mono({
  double fontSize = 12,
  FontWeight fontWeight = FontWeight.w400,
  Color? color,
  double? letterSpacing,
  double? height,
}) =>
    GoogleFonts.jetBrainsMono(
      fontSize: fontSize,
      fontWeight: fontWeight,
      color: color,
      letterSpacing: letterSpacing,
      height: height,
    );

/// Etiqueta micro de sección con tracking extendido `1.2px` y color `#8E8E93`.
TextStyle sectionMicroStyle(AppPalette p) => TextStyle(
      fontSize: 10,
      fontWeight: FontWeight.w600,
      letterSpacing: 1.2,
      color: p.textSecondary,
    );

/// Controlador reactivo del tema (Oscuro OLED por defecto / Claro iOS).
class ThemeController extends ChangeNotifier {
  static const String _prefsKey = 'um_studio_theme_mode';

  ThemeMode _mode = ThemeMode.dark;

  ThemeMode get mode => _mode;
  bool get isDark => _mode == ThemeMode.dark;

  Future<void> load() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getString(_prefsKey);
    _mode = saved == 'light' ? ThemeMode.light : ThemeMode.dark;
  }

  Future<void> toggle() async {
    _mode = isDark ? ThemeMode.light : ThemeMode.dark;
    notifyListeners();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_prefsKey, isDark ? 'dark' : 'light');
  }
}
