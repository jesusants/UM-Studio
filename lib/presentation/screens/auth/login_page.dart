import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/institutional_validator.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';

/// Pantalla de acceso rápido y registro instantáneo para compañeros de
/// Ingeniería Energética (`@unimagdalena.edu.co`), respaldada en GitHub
/// (`db/users/{username}.json`) con persistencia permanente y datos cifrados.
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
  int _selectedCuatrimestre = 2;
  String? _errorText;

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

    final rawInput = _userCtrl.text.trim();
    final parsed = InstitutionalValidator.parseInstitutionalUser(rawInput);
    if (parsed.error != null || parsed.identity == null) {
      setState(() {
        _submitting = false;
        _errorText = parsed.error;
      });
      return;
    }

    setState(() {
      _submitting = true;
      _errorText = null;
    });

    final session = SessionScope.of(context);
    late final String? err;

    if (_isRegister) {
      err = await session.register(
        userOrEmail: parsed.identity!.username,
        nombre: _nameCtrl.text,
        pin: _pinCtrl.text,
        cuatrimestre: _selectedCuatrimestre,
      );
    } else {
      err = await session.login(
        userOrEmail: parsed.identity!.username,
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

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return Scaffold(
      backgroundColor: p.background,
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            physics: const BouncingScrollPhysics(),
            padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 24),
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 420),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Encabezado con Emblema Oficial
                  Center(
                    child: Container(
                      width: 64,
                      height: 64,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: p.green.o(0.12),
                        border: Border.all(color: p.green.o(0.38), width: 1.5),
                        boxShadow: [
                          BoxShadow(
                            color: p.green.o(0.15),
                            blurRadius: 18,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: Center(
                        child: Image.asset(
                          AppConstants.programLogoAsset,
                          width: 38,
                          height: 38,
                          errorBuilder: (_, __, ___) => Icon(
                            Icons.bolt_rounded,
                            color: p.green,
                            size: 32,
                          ),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),
                  Center(
                    child: Text(
                      'UM STUDIO',
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.5,
                        color: p.textPrimary,
                      ),
                    ),
                  ),
                  const SizedBox(height: 4),
                  Center(
                    child: Text(
                      'Ingeniería Energética • Unimagdalena',
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w500,
                        color: p.textSecondary,
                      ),
                    ),
                  ),
                  const SizedBox(height: 22),

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
                    padding: const EdgeInsets.all(18),
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
                          'PIN O CONTRASEÑA',
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
                            hint: 'Mínimo 4 caracteres',
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
                          Text(
                            'CUATRIMESTRE INICIAL (PLAN 8108)',
                            style: sectionMicroStyle(p),
                          ),
                          const SizedBox(height: 8),
                          Wrap(
                            spacing: 6,
                            runSpacing: 6,
                            children: List.generate(12, (idx) {
                              final c = idx + 1;
                              final selected = c == _selectedCuatrimestre;
                              return TapScale(
                                onTap: () =>
                                    setState(() => _selectedCuatrimestre = c),
                                child: Container(
                                  width: 36,
                                  height: 30,
                                  alignment: Alignment.center,
                                  decoration: BoxDecoration(
                                    color: selected ? p.green : p.elevated,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(
                                      color: selected ? p.green : p.cardBorder,
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
                              );
                            }),
                          ),
                        ],

                        if (_errorText != null) ...[
                          const SizedBox(height: 14),
                          Container(
                            width: double.infinity,
                            padding: const EdgeInsets.symmetric(
                              horizontal: 12,
                              vertical: 10,
                            ),
                            decoration: BoxDecoration(
                              color: p.orange.o(0.12),
                              borderRadius: BorderRadius.circular(12),
                              border: Border.all(color: p.orange.o(0.38)),
                            ),
                            child: Row(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Icon(
                                  Icons.warning_amber_rounded,
                                  size: 17,
                                  color: p.orange,
                                ),
                                const SizedBox(width: 8),
                                Expanded(
                                  child: Text(
                                    _errorText!,
                                    style: TextStyle(
                                      fontSize: 12,
                                      height: 1.35,
                                      fontWeight: FontWeight.w500,
                                      color: p.orange,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],

                        const SizedBox(height: 14),
                        Row(
                          children: [
                            Icon(
                              Icons.lock_rounded,
                              size: 14,
                              color: p.green,
                            ),
                            const SizedBox(width: 6),
                            Expanded(
                              child: Text(
                                'Datos cifrados simétricamente en UM Cloud',
                                style: TextStyle(
                                  fontSize: 11,
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
                            child: _submitting
                                ? const SizedBox(
                                    width: 18,
                                    height: 18,
                                    child: CircularProgressIndicator(
                                      strokeWidth: 2,
                                      valueColor: AlwaysStoppedAnimation<Color>(
                                        Colors.black,
                                      ),
                                    ),
                                  )
                                : Text(
                                    _isRegister
                                        ? 'Crear mi espacio y entrar →'
                                        : 'Entrar a UM STUDIO →',
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

                  const SizedBox(height: 16),
                  Center(
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Dot(
                            color: p.green,
                            size: 6,
                          ),
                          const SizedBox(width: 7),
                          Text(
                            'UM Cloud • Sincronización Serverless Activa',
                            style: mono(
                              fontSize: 10.5,
                              color: p.textSecondary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
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
