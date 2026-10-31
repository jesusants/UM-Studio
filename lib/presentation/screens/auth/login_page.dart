import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';

/// Pantalla de acceso rápido y registro instantáneo para compañeros de
/// Ingeniería Energética (`@unimagdalena.edu.co`), respaldada en GitHub
/// (`db/users/{username}.json`) con persistencia permanente.
class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _userCtrl = TextEditingController();
  final TextEditingController _nameCtrl = TextEditingController();
  final TextEditingController _pinCtrl = TextEditingController();

  bool _isRegister = false;
  bool _obscurePin = true;
  bool _submitting = false;
  bool _showLegacyOptions = false;
  int _selectedCuatrimestre = 2;
  String? _errorText;

  Future<void> _loginWithMicrosoft() async {
    if (_submitting) return;
    FocusScope.of(context).unfocus();
    setState(() {
      _submitting = true;
      _errorText = null;
    });

    final session = SessionScope.of(context);
    final err = await session.loginWithMicrosoft();

    if (!mounted) return;
    if (err != null) {
      HapticFeedback.mediumImpact();
      setState(() {
        _submitting = false;
        _errorText = err;
      });
    } else {
      HapticFeedback.lightImpact();
      setState(() => _submitting = false);
    }
  }

  @override
  void dispose() {
    _userCtrl.dispose();
    _nameCtrl.dispose();
    _pinCtrl.dispose();
    super.dispose();
  }

  bool get _typedFullAt => _userCtrl.text.contains('@');

  Future<void> _submit() async {
    if (_submitting) return;
    FocusScope.of(context).unfocus();
    setState(() {
      _submitting = true;
      _errorText = null;
    });

    final session = SessionScope.of(context);
    late final String? err;

    if (_isRegister) {
      err = await session.register(
        userOrEmail: _userCtrl.text,
        nombre: _nameCtrl.text,
        pin: _pinCtrl.text,
        cuatrimestre: _selectedCuatrimestre,
      );
    } else {
      err = await session.login(
        userOrEmail: _userCtrl.text,
        pin: _pinCtrl.text,
      );
    }

    if (!mounted) return;
    if (err != null) {
      HapticFeedback.mediumImpact();
      setState(() {
        _submitting = false;
        _errorText = err;
      });
    } else {
      HapticFeedback.lightImpact();
    }
  }

  Future<void> _openGitHubTokenSheet() async {
    final session = SessionScope.of(context);
    final p = context.palette;
    final tokenCtrl = TextEditingController();

    await showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      backgroundColor: p.card,
      shape: RoundedRectangleBorder(
        borderRadius: const BorderRadius.vertical(top: Radius.circular(22)),
        side: BorderSide(color: p.cardBorder),
      ),
      builder: (sheetCtx) {
        final bottom = MediaQuery.viewInsetsOf(sheetCtx).bottom;
        return SafeArea(
          child: Padding(
            padding: EdgeInsets.fromLTRB(18, 12, 18, 18 + bottom),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Center(
                  child: Container(
                    width: 36,
                    height: 4,
                    decoration: BoxDecoration(
                      color: p.strongBorder,
                      borderRadius: BorderRadius.circular(4),
                    ),
                  ),
                ),
                const SizedBox(height: 14),
                Text('SINCRONIZACIÓN GITHUB', style: sectionMicroStyle(p)),
                const SizedBox(height: 6),
                Text(
                  'Token del Repositorio (Opcional en Local)',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'En la versión web oficial el repositorio ya está vinculado. Si ejecutas en localhost sin variables de entorno, pega aquí el PAT para sincronizar en db/users/.',
                  style: TextStyle(fontSize: 12, color: p.textSecondary),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: tokenCtrl,
                  obscureText: true,
                  autocorrect: false,
                  style: mono(fontSize: 12, color: p.textPrimary),
                  decoration: InputDecoration(
                    isDense: true,
                    filled: true,
                    fillColor: p.background.o(0.45),
                    hintText: 'github_pat_...',
                    hintStyle: mono(fontSize: 12, color: p.textTertiary),
                    contentPadding: const EdgeInsets.all(12),
                    enabledBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                      borderSide: BorderSide(color: p.cardBorder),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                      borderSide: BorderSide(color: p.green),
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                TapScale(
                  onTap: () async {
                    await session.syncService.setCustomGitHubToken(
                      tokenCtrl.text,
                    );
                    if (sheetCtx.mounted) Navigator.of(sheetCtx).pop();
                    if (mounted) {
                      showIosToast(
                        context,
                        session.syncService.hasWriteToken
                            ? 'Token de sincronización guardado'
                            : 'Usando configuración por defecto',
                      );
                    }
                  },
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(vertical: 11),
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: p.green,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: const Text(
                      'Guardar configuración',
                      style: TextStyle(
                        fontSize: 12.5,
                        fontWeight: FontWeight.w600,
                        color: Colors.black,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.of(context).isDark;
    final session = SessionScope.of(context);
    final screenWidth = MediaQuery.sizeOf(context).width;
    final wide = screenWidth > AppConstants.maxPhoneViewportWidth;

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: isDark ? SystemUiOverlayStyle.light : SystemUiOverlayStyle.dark,
      child: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Scaffold(
          backgroundColor: p.background,
          body: Center(
            child: Container(
              width: math.min(screenWidth, AppConstants.maxPhoneViewportWidth),
              height: double.infinity,
              decoration: BoxDecoration(
                color: p.background,
                border: wide
                    ? Border.symmetric(
                        vertical: BorderSide(color: p.cardBorder.o(0.9)),
                      )
                    : null,
              ),
              child: SafeArea(
                child: ListView(
                  physics: const BouncingScrollPhysics(),
                  padding: const EdgeInsets.fromLTRB(22, 18, 22, 28),
                  children: [
                    // Barra superior con emblema oficial y selector de tema
                    Row(
                      children: [
                        const ProgramLogoBadge(size: 38),
                        const SizedBox(width: 10),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                AppConstants.appTitle,
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w700,
                                  letterSpacing: 0.4,
                                  color: p.textPrimary,
                                ),
                              ),
                              Text(
                                AppConstants.programSubtitle,
                                style: TextStyle(
                                  fontSize: 11,
                                  color: p.textSecondary,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const ThemeToggleButton(),
                      ],
                    ),
                    const SizedBox(height: 28),

                    // Encabezado limpio estilo Apple HIG
                    Text(
                      _isRegister
                          ? 'Únete a tu cohorte'
                          : 'Bienvenido de vuelta',
                      style: TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.w700,
                        letterSpacing: -0.6,
                        color: p.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 6),
                    Text(
                      'Espacio colaborativo diario con malla Plan 8108, fórmulas KaTeX y calendario personal sincronizado en GitHub.',
                      style: TextStyle(
                        fontSize: 13,
                        height: 1.42,
                        color: p.textSecondary,
                      ),
                    ),
                    const SizedBox(height: 18),

                    // Píldora bloqueada de Carrera (Ingeniería Energética)
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 14,
                        vertical: 11,
                      ),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: p.green.o(0.35)),
                      ),
                      child: Row(
                        children: [
                          Icon(
                            Icons.bolt_rounded,
                            size: 18,
                            color: p.green,
                          ),
                          const SizedBox(width: 10),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'PROGRAMA ACADÉMICO FIJO',
                                  style: mono(
                                    fontSize: 9.5,
                                    fontWeight: FontWeight.w600,
                                    letterSpacing: 1.0,
                                    color: p.green,
                                  ),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  'Ingeniería Energética • Unimagdalena',
                                  style: TextStyle(
                                    fontSize: 13,
                                    fontWeight: FontWeight.w600,
                                    color: p.textPrimary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Icon(
                            Icons.lock_outline_rounded,
                            size: 15,
                            color: p.textSecondary,
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 18),

                    // Tarjeta Principal: Acceso Institucional Microsoft Entra ID (PKCE)
                    Container(
                      padding: const EdgeInsets.all(18),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(color: p.green.o(0.42), width: 1.2),
                        boxShadow: [
                          BoxShadow(
                            color: p.green.o(0.08),
                            blurRadius: 18,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            children: [
                              const _MicrosoftLogoIcon(size: 20),
                              const SizedBox(width: 9),
                              Expanded(
                                child: Text(
                                  'ACCESO INSTITUCIONAL',
                                  style: mono(
                                    fontSize: 10.5,
                                    fontWeight: FontWeight.w700,
                                    letterSpacing: 1.0,
                                    color: p.green,
                                  ),
                                ),
                              ),
                              Container(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 7,
                                  vertical: 2.5,
                                ),
                                decoration: BoxDecoration(
                                  color: p.elevated,
                                  borderRadius: BorderRadius.circular(6),
                                  border: Border.all(color: p.cardBorder),
                                ),
                                child: Text(
                                  'OIDC • PKCE',
                                  style: mono(
                                    fontSize: 9.5,
                                    fontWeight: FontWeight.w600,
                                    color: p.textSecondary,
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 10),
                          Text(
                            'Ingresa con tu cuenta institucional para vincular tu progreso, notas y horario con tu ID único.',
                            style: TextStyle(
                              fontSize: 12.5,
                              height: 1.4,
                              color: p.textSecondary,
                            ),
                          ),
                          const SizedBox(height: 14),
                          TapScale(
                            onTap: _submitting ? null : _loginWithMicrosoft,
                            child: AnimatedContainer(
                              duration: const Duration(milliseconds: 180),
                              width: double.infinity,
                              padding: const EdgeInsets.symmetric(vertical: 14),
                              alignment: Alignment.center,
                              decoration: BoxDecoration(
                                color: p.green,
                                borderRadius: BorderRadius.circular(14),
                                boxShadow: [
                                  BoxShadow(
                                    color: p.green.o(0.32),
                                    blurRadius: 12,
                                    offset: const Offset(0, 3),
                                  ),
                                ],
                              ),
                              child: _submitting
                                  ? const SizedBox(
                                      width: 20,
                                      height: 20,
                                      child: CircularProgressIndicator(
                                        strokeWidth: 2.2,
                                        valueColor:
                                            AlwaysStoppedAnimation<Color>(
                                          Colors.black,
                                        ),
                                      ),
                                    )
                                  : const FittedBox(
                                      fit: BoxFit.scaleDown,
                                      child: Row(
                                        mainAxisAlignment:
                                            MainAxisAlignment.center,
                                        children: [
                                          _MicrosoftLogoIcon(size: 18),
                                          SizedBox(width: 10),
                                          Text(
                                            'Iniciar sesión con Microsoft',
                                            style: TextStyle(
                                              fontSize: 14.5,
                                              fontWeight: FontWeight.w700,
                                              letterSpacing: -0.2,
                                              color: Colors.black,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 18),

                    // Botón para alternar opciones secundarias
                    Center(
                      child: TapScale(
                        onTap: () => setState(() {
                          _showLegacyOptions = !_showLegacyOptions;
                        }),
                        child: Padding(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 12,
                            vertical: 8,
                          ),
                          child: FittedBox(
                            fit: BoxFit.scaleDown,
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Text(
                                  _showLegacyOptions
                                      ? 'Ocultar acceso con PIN / Local'
                                      : 'Opciones de acceso con PIN / Local',
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w500,
                                    color: p.textTertiary,
                                  ),
                                ),
                                const SizedBox(width: 4),
                                Icon(
                                  _showLegacyOptions
                                      ? Icons.keyboard_arrow_up_rounded
                                      : Icons.keyboard_arrow_down_rounded,
                                  size: 16,
                                  color: p.textTertiary,
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ),

                    if (_showLegacyOptions) ...[
                      const SizedBox(height: 12),
                      // Selector segmentado iOS: Iniciar Sesión / Crear Cuenta
                    Container(
                      padding: const EdgeInsets.all(4),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        children: [
                          Expanded(
                            child: _ModeSegmentButton(
                              label: 'Iniciar Sesión',
                              selected: !_isRegister,
                              onTap: () => setState(() {
                                _isRegister = false;
                                _errorText = null;
                              }),
                            ),
                          ),
                          Expanded(
                            child: _ModeSegmentButton(
                              label: 'Crear Cuenta',
                              selected: _isRegister,
                              onTap: () => setState(() {
                                _isRegister = true;
                                _errorText = null;
                              }),
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),

                    // Tarjeta principal de formulario
                    IosCard(
                      radius: 20,
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          if (_isRegister) ...[
                            Text('NOMBRE COMPLETO', style: sectionMicroStyle(p)),
                            const SizedBox(height: 6),
                            TextField(
                              key: const Key('login_name_field'),
                              controller: _nameCtrl,
                              textCapitalization: TextCapitalization.words,
                              style: TextStyle(
                                fontSize: 13.5,
                                color: p.textPrimary,
                              ),
                              decoration: _inputDecoration(
                                p,
                                hint: 'Ej: Jesús Sierra',
                                prefixIcon: Icons.person_outline_rounded,
                              ),
                            ),
                            const SizedBox(height: 14),
                          ],

                          Text(
                            'USUARIO INSTITUCIONAL',
                            style: sectionMicroStyle(p),
                          ),
                          const SizedBox(height: 6),
                          TextField(
                            key: const Key('login_user_field'),
                            controller: _userCtrl,
                            keyboardType: TextInputType.emailAddress,
                            autocorrect: false,
                            onChanged: (_) => setState(() {}),
                            style: mono(fontSize: 13, color: p.textPrimary),
                            decoration: _inputDecoration(
                              p,
                              hint: 'usuario',
                              prefixIcon: Icons.alternate_email_rounded,
                              suffix: _typedFullAt
                                  ? null
                                  : Padding(
                                      padding: const EdgeInsets.only(right: 10),
                                      child: Text(
                                        AppConstants.institutionalDomain,
                                        style: mono(
                                          fontSize: 11.5,
                                          color: p.green,
                                        ),
                                      ),
                                    ),
                            ),
                          ),
                          const SizedBox(height: 14),

                          Text(
                            'PIN O CONTRASEÑA SIMPLE',
                            style: sectionMicroStyle(p),
                          ),
                          const SizedBox(height: 6),
                          TextField(
                            key: const Key('login_pin_field'),
                            controller: _pinCtrl,
                            obscureText: _obscurePin,
                            autocorrect: false,
                            onSubmitted: (_) => _submit(),
                            style: mono(fontSize: 13.5, color: p.textPrimary),
                            decoration: _inputDecoration(
                              p,
                              hint: 'Mínimo 4 dígitos o letras',
                              prefixIcon: Icons.key_rounded,
                              suffix: GestureDetector(
                                onTap: () =>
                                    setState(() => _obscurePin = !_obscurePin),
                                child: Padding(
                                  padding: const EdgeInsets.only(right: 10),
                                  child: Icon(
                                    _obscurePin
                                        ? Icons.visibility_outlined
                                        : Icons.visibility_off_outlined,
                                    size: 17,
                                    color: p.textSecondary,
                                  ),
                                ),
                              ),
                            ),
                          ),

                          if (_isRegister) ...[
                            const SizedBox(height: 14),
                            Row(
                              children: [
                                Expanded(
                                  child: Text(
                                    'CUATRIMESTRE EN CURSO',
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: sectionMicroStyle(p),
                                  ),
                                ),
                                const SizedBox(width: 8),
                                Text(
                                  'Cuat. $_selectedCuatrimestre',
                                  style: mono(
                                    fontSize: 11,
                                    fontWeight: FontWeight.w600,
                                    color: p.green,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 8),
                            SingleChildScrollView(
                              scrollDirection: Axis.horizontal,
                              physics: const BouncingScrollPhysics(),
                              child: Row(
                                children: List.generate(12, (idx) {
                                  final c = idx + 1;
                                  final selected = c == _selectedCuatrimestre;
                                  return Padding(
                                    padding: const EdgeInsets.only(right: 6),
                                    child: TapScale(
                                      onTap: () => setState(
                                        () => _selectedCuatrimestre = c,
                                      ),
                                      child: AnimatedContainer(
                                        duration: const Duration(
                                          milliseconds: 180,
                                        ),
                                        width: 34,
                                        height: 32,
                                        alignment: Alignment.center,
                                        decoration: BoxDecoration(
                                          color: selected
                                              ? p.green
                                              : p.elevated,
                                          borderRadius: BorderRadius.circular(
                                            10,
                                          ),
                                          border: Border.all(
                                            color: selected
                                                ? p.green
                                                : p.cardBorder,
                                          ),
                                        ),
                                        child: Text(
                                          '$c',
                                          style: mono(
                                            fontSize: 12,
                                            fontWeight: FontWeight.w600,
                                            color: selected
                                                ? Colors.black
                                                : p.textSecondary,
                                          ),
                                        ),
                                      ),
                                    ),
                                  );
                                }),
                              ),
                            ),
                          ],

                          if (_errorText != null) ...[
                            const SizedBox(height: 12),
                            Container(
                              width: double.infinity,
                              padding: const EdgeInsets.symmetric(
                                horizontal: 12,
                                vertical: 9,
                              ),
                              decoration: BoxDecoration(
                                color: p.orange.o(0.12),
                                borderRadius: BorderRadius.circular(11),
                                border: Border.all(color: p.orange.o(0.35)),
                              ),
                              child: Text(
                                _errorText!,
                                style: TextStyle(
                                  fontSize: 12,
                                  color: p.orange,
                                ),
                              ),
                            ),
                          ],

                          const SizedBox(height: 14),
                          Row(
                            children: [
                              Icon(
                                Icons.check_circle_rounded,
                                size: 15,
                                color: p.green,
                              ),
                              const SizedBox(width: 6),
                              Expanded(
                                child: Text(
                                  'Recordar mis datos activo permanentemente',
                                  style: TextStyle(
                                    fontSize: 11.5,
                                    color: p.textSecondary,
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 16),

                          TapScale(
                            onTap: _submitting ? null : _submit,
                            child: Container(
                              key: const Key('login_submit_button'),
                              width: double.infinity,
                              padding: const EdgeInsets.symmetric(vertical: 13),
                              alignment: Alignment.center,
                              decoration: BoxDecoration(
                                color: _submitting ? p.green.o(0.6) : p.green,
                                borderRadius: BorderRadius.circular(14),
                              ),
                              child: Text(
                                _submitting
                                    ? 'Sincronizando con GitHub...'
                                    : (_isRegister
                                          ? 'Crear mi espacio y entrar →'
                                          : 'Entrar a UM STUDIO →'),
                                style: const TextStyle(
                                  fontSize: 13.5,
                                  fontWeight: FontWeight.w700,
                                  color: Colors.black,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),

                    ], // Fin if (_showLegacyOptions)

                    const SizedBox(height: 16),

                    // Estado del backend ligero en GitHub
                    Center(
                      child: TapScale(
                        onTap: _openGitHubTokenSheet,
                        child: Padding(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 10,
                            vertical: 6,
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Dot(
                                color: session.syncService.hasWriteToken
                                    ? p.green
                                    : p.indigo,
                                size: 6,
                              ),
                              const SizedBox(width: 7),
                              Flexible(
                                child: Text(
                                  session.syncService.hasWriteToken
                                      ? 'Conectado a jesusants/UM-Studio (db/users/)'
                                      : 'Almacenamiento Offline-First • Vincular Token GitHub',
                                  style: mono(
                                    fontSize: 10.5,
                                    color: p.textSecondary,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  InputDecoration _inputDecoration(
    AppPalette p, {
    required String hint,
    required IconData prefixIcon,
    Widget? suffix,
  }) {
    return InputDecoration(
      isDense: true,
      filled: true,
      fillColor: p.background.o(0.45),
      hintText: hint,
      hintStyle: TextStyle(fontSize: 12.5, color: p.textTertiary),
      prefixIcon: Icon(prefixIcon, size: 17, color: p.textSecondary),
      prefixIconConstraints: const BoxConstraints(minWidth: 38, minHeight: 38),
      suffixIcon: suffix,
      suffixIconConstraints: const BoxConstraints(minWidth: 24, minHeight: 24),
      contentPadding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide(color: p.cardBorder),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide(color: p.green),
      ),
    );
  }
}

class _ModeSegmentButton extends StatelessWidget {
  const _ModeSegmentButton({
    required this.label,
    required this.selected,
    required this.onTap,
  });

  final String label;
  final bool selected;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return TapScale(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 220),
        curve: kIosSpring,
        padding: const EdgeInsets.symmetric(vertical: 9),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: selected ? p.elevated : Colors.transparent,
          borderRadius: BorderRadius.circular(10),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 12.5,
            fontWeight: selected ? FontWeight.w600 : FontWeight.w500,
            color: selected ? p.textPrimary : p.textSecondary,
          ),
        ),
      ),
    );
  }
}


class _MicrosoftLogoIcon extends StatelessWidget {
  const _MicrosoftLogoIcon({this.size = 18});

  final double size;

  @override
  Widget build(BuildContext context) {
    final sub = size * 0.44;
    final gap = size * 0.12;

    return SizedBox(
      width: size,
      height: size,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(width: sub, height: sub, color: const Color(0xFFF25022)),
              SizedBox(width: gap),
              Container(width: sub, height: sub, color: const Color(0xFF7FBA00)),
            ],
          ),
          SizedBox(height: gap),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(width: sub, height: sub, color: const Color(0xFF00A4EF)),
              SizedBox(width: gap),
              Container(width: sub, height: sub, color: const Color(0xFFFFB900)),
            ],
          ),
        ],
      ),
    );
  }
}
