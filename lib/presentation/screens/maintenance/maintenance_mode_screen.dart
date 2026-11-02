import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import '../../../core/theme/app_theme.dart';
import '../../../data/services/global_environment_service.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/admin_env_console_modal.dart';
import '../../widgets/ios_primitives.dart';

/// Pantalla de guardia mostrada cuando maintenance_mode = true.
/// Si el usuario es el administrador (jsierra), puede ingresar directamente a la consola.
class MaintenanceModeScreen extends StatelessWidget {
  const MaintenanceModeScreen({super.key});

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
              if (kIsWeb && isAdmin) ...[
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
                const SizedBox(height: 12),
              ],
              TextButton(
                onPressed: () {
                  GlobalEnvironmentService.instance.fetchRemoteConfig();
                },
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.refresh_rounded, size: 16, color: p.textSecondary),
                    const SizedBox(width: 6),
                    Text(
                      'Comprobar Estado',
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
