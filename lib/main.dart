import 'dart:ui';
import 'package:flutter/material.dart';

import 'core/theme/app_theme.dart';
import 'data/repositories/local_clase_viva_repository.dart';
import 'data/services/global_environment_service.dart';
import 'data/services/markdown_curriculum_service.dart';
import 'data/services/unimagdalena_realtime_news_service.dart';
import 'domain/repositories/i_clase_viva_repository.dart';
import 'presentation/providers/app_scopes.dart';
import 'presentation/screens/auth/login_page.dart';
import 'presentation/screens/home/home_shell.dart';
import 'presentation/screens/maintenance/maintenance_mode_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  ErrorWidget.builder = (FlutterErrorDetails details) {
    FlutterError.dumpErrorToConsole(details);
    return const SizedBox.shrink();
  };

  final themeController = ThemeController();
  await themeController.load();

  // Inicializar variables globales de entorno en tiempo real (Offline-First + GitHub API)
  await GlobalEnvironmentService.instance.initialize();

  final curriculumService = MarkdownCurriculumService();
  await curriculumService.initialize();

  final repository = LocalReactiveClaseVivaRepository(
    curriculumService: curriculumService,
  );

  final sessionController = InstitutionalSessionController(
    repository: repository,
    curriculumService: curriculumService,
  );
  await sessionController.load();

  // Inicializar servicio de noticias en tiempo real
  UnimagdalenaRealtimeNewsService.instance.init();

  runApp(
    UmStudioApp(
      themeController: themeController,
      repository: repository,
      curriculumService: curriculumService,
      sessionController: sessionController,
    ),
  );
}

class UmStudioApp extends StatelessWidget {
  const UmStudioApp({
    super.key,
    required this.themeController,
    required this.repository,
    this.curriculumService,
    this.sessionController,
    this.requireAuth = true,
  });

  final ThemeController themeController;
  final IClaseVivaRepository repository;
  final MarkdownCurriculumService? curriculumService;
  final InstitutionalSessionController? sessionController;
  final bool requireAuth;

  @override
  Widget build(BuildContext context) {
    final effectiveCurriculum =
        curriculumService ?? MarkdownCurriculumService();
    final effectiveSession = sessionController ??
        InstitutionalSessionController(
          repository: repository,
          curriculumService: effectiveCurriculum,
        );

    return CurriculumScope(
      service: effectiveCurriculum,
      child: ClaseVivaRepositoryScope(
        repository: repository,
        child: SessionScope(
          controller: effectiveSession,
          child: ThemeScope(
            controller: themeController,
            child: ListenableBuilder(
              listenable: Listenable.merge([
                themeController,
                effectiveSession,
                GlobalEnvironmentService.instance,
              ]),
              builder: (context, _) {
                final envConfig = GlobalEnvironmentService.instance.config;
                final isAdmin = effectiveSession.isAdmin;
                final isUnderMaintenance = envConfig.maintenanceMode && !isAdmin;

                final showHome =
                    !requireAuth || effectiveSession.isAuthenticated;

                final Widget activeScreen;
                if (isUnderMaintenance) {
                  activeScreen = const MaintenanceModeScreen(key: ValueKey('maintenance_mode'));
                } else if (showHome) {
                  activeScreen = const HomeShell(key: ValueKey('home_shell'));
                } else {
                  activeScreen = const LoginPage(key: ValueKey('login_page'));
                }

                return MaterialApp(
                  title: 'UM STUDIO — Ingeniería Energética',
                  debugShowCheckedModeBanner: false,
                  scrollBehavior: const AppScrollBehavior(),
                  theme: AppTheme.light,
                  darkTheme: AppTheme.dark,
                  themeMode: themeController.mode,
                  themeAnimationDuration: const Duration(milliseconds: 350),
                  themeAnimationCurve: Curves.easeInOut,
                  home: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 280),
                    switchInCurve: kIosSpring,
                    child: activeScreen,
                  ),
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}

/// Comportamiento de desplazamiento global que habilita arrastre con ratón (mouse drag),
/// trackpad, stylus y táctil en todas las plataformas y vistas de la aplicación.
class AppScrollBehavior extends MaterialScrollBehavior {
  const AppScrollBehavior();

  @override
  Set<PointerDeviceKind> get dragDevices => {
        PointerDeviceKind.touch,
        PointerDeviceKind.mouse,
        PointerDeviceKind.stylus,
        PointerDeviceKind.invertedStylus,
        PointerDeviceKind.trackpad,
        PointerDeviceKind.unknown,
      };
}
