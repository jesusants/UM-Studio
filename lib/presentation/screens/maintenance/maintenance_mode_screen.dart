import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/theme/app_theme.dart';
import '../../../core/utils/institutional_validator.dart';
import '../../../data/services/global_environment_service.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/admin_env_console_modal.dart';
import '../../widgets/ios_primitives.dart';

/// Pantalla de guardia mostrada cuando `maintenance_mode = true`.
/// Si el usuario es el administrador (`jsierra` / `jasierra`), puede ingresar directamente a la consola.
class MaintenanceModeScreen extends StatefulWidget {
  const MaintenanceModeScreen({super.key});

  @override
  State<MaintenanceModeScreen> createState() => _MaintenanceModeScreenState();
}

class _MaintenanceModeScreenState extends State<MaintenanceModeScreen> {
  bool _isChecking = false;

  Future<void> _checkStatus() async {
    if (_isChecking) return;
    setState(() => _isChecking = true);
    HapticFeedback.lightImpact();

    await GlobalEnvironmentService.instance.fetchRemoteConfig();

    if (mounted) {
      setState(() => _isChecking = false);
      final p = context.palette;
      final cfg = GlobalEnvironmentService.instance.config;
      if (!cfg.maintenanceMode) {
        showIosToast(
          context,
          '¡Mantenimiento finalizado! Bienvenido de nuevo a UM Studio.',
          accentColor: p.green,
        );
      } else {
        showIosToast(
          context,
          'El sistema continúa en mantenimiento. Intenta de nuevo en unos minutos.',
          accentColor: p.orange,
        );
      }
    }
  }

  Future<void> _showAdminLoginDialog() async {
    final p = context.palette;
    final pinCtrl = TextEditingController();

    await showDialog<void>(
      context: context,
      builder: (dlgCtx) {
        bool hasError = false;
        return StatefulBuilder(
          builder: (dlgCtx, setDlgState) {
            Future<void> submit() async {
              final valid = InstitutionalValidator.verifyMasterAdmin(
                userOrEmail: InstitutionalValidator.masterAdminUsername,
                pin: pinCtrl.text.trim(),
              );
              if (!valid) {
                setDlgState(() => hasError = true);
                return;
              }

              Navigator.of(dlgCtx).pop();
              final session = SessionScope.maybeOf(context);
              await session?.login(
                userOrEmail: InstitutionalValidator.masterAdminUsername,
                pin: pinCtrl.text.trim(),
              );

              if (mounted) {
                AdminEnvConsoleModal.show(context);
              }
            }

            return AlertDialog(
              backgroundColor: p.card,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20),
                side: BorderSide(color: p.cardBorder),
              ),
              title: Row(
                children: [
                  PulseDot(color: p.green, size: 8),
                  const SizedBox(width: 8),
                  Text(
                    'Identificación Superadmin',
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w700,
                      color: p.textPrimary,
                    ),
                  ),
                ],
              ),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Ingresa el PIN maestro para administrar las variables de entorno de UM Studio.',
                    style: TextStyle(fontSize: 12, color: p.textSecondary),
                  ),
                  const SizedBox(height: 14),
                  TextField(
                    controller: pinCtrl,
                    obscureText: true,
                    autofocus: true,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      hintText: 'PIN Maestro...',
                      errorText: hasError ? 'PIN maestro incorrecto' : null,
                    ),
                    onSubmitted: (_) => submit(),
                  ),
                ],
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.of(dlgCtx).pop(),
                  child: Text('Cancelar', style: TextStyle(color: p.textSecondary)),
                ),
                TapScale(
                  onTap: submit,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    decoration: BoxDecoration(
                      color: p.green,
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Text(
                      'Entrar',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: Colors.black,
                      ),
                    ),
                  ),
                ),
              ],
            );
          },
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final isAdmin = session?.isAdmin == true;

    return Scaffold(
      backgroundColor: p.background,
      body: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 480),
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                width: 72,
                height: 72,
                decoration: BoxDecoration(
                  color: p.orange.o(0.12),
                  shape: BoxShape.circle,
                  border: Border.all(color: p.orange.o(0.35), width: 2),
                ),
                child: Icon(Icons.build_rounded, size: 36, color: p.orange),
              ),
              const SizedBox(height: 24),
              Text(
                'Mantenimiento en Curso',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 22,
                  fontWeight: FontWeight.w800,
                  color: p.textPrimary,
                  letterSpacing: -0.5,
                ),
              ),
              const SizedBox(height: 10),
              Text(
                'UM Studio se encuentra temporalmente en actualización de cátedra e infraestructura. Volveremos a estar disponibles en breve.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 13.5,
                  height: 1.45,
                  color: p.textSecondary,
                ),
              ),
              const SizedBox(height: 28),
              if (kIsWeb) ...[
                if (isAdmin) ...[
                  TapScale(
                    onTap: () => AdminEnvConsoleModal.show(context),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                      decoration: BoxDecoration(
                        color: p.green,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.admin_panel_settings_rounded, size: 18, color: Colors.black),
                          SizedBox(width: 8),
                          Text(
                            'Abrir Consola Admin (jsierra)',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              color: Colors.black,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ] else ...[
                  TapScale(
                    onTap: _showAdminLoginDialog,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                      decoration: BoxDecoration(
                        color: p.card,
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: p.cardBorder),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          PulseDot(color: p.green, size: 6),
                          const SizedBox(width: 8),
                          Text(
                            '⚡ Acceso Administrador (jsierra)',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w700,
                              color: p.textPrimary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
                const SizedBox(height: 14),
              ],
              TextButton(
                onPressed: _checkStatus,
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    if (_isChecking)
                      SizedBox(
                        width: 14,
                        height: 14,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                          color: p.textSecondary,
                        ),
                      )
                    else
                      Icon(Icons.refresh_rounded, size: 16, color: p.textSecondary),
                    const SizedBox(width: 6),
                    Text(
                      _isChecking ? 'Comprobando...' : 'Comprobar Estado',
                      style: TextStyle(fontSize: 12, color: p.textSecondary),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
