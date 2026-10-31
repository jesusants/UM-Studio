import 'package:flutter/material.dart';

import 'core/theme/app_theme.dart';
import 'data/repositories/local_clase_viva_repository.dart';
import 'data/services/markdown_curriculum_service.dart';
import 'domain/repositories/i_clase_viva_repository.dart';
import 'presentation/providers/app_scopes.dart';
import 'presentation/screens/auth/login_page.dart';
import 'presentation/screens/home/home_shell.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  ErrorWidget.builder = (FlutterErrorDetails details) {
    FlutterError.dumpErrorToConsole(details);
    return const SizedBox.shrink();
  };

  final themeController = ThemeController();
  await themeController.load();

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
              listenable: Listenable.merge([themeController, effectiveSession]),
              builder: (context, _) {
                final showHome =
                    !requireAuth || effectiveSession.isAuthenticated;

                return MaterialApp(
                  title: 'UM STUDIO — Ingeniería Energética',
                  debugShowCheckedModeBanner: false,
                  theme: AppTheme.light,
                  darkTheme: AppTheme.dark,
                  themeMode: themeController.mode,
                  themeAnimationDuration: const Duration(milliseconds: 350),
                  themeAnimationCurve: Curves.easeInOut,
                  home: AnimatedSwitcher(
                    duration: const Duration(milliseconds: 280),
                    switchInCurve: kIosSpring,
                    child: showHome
                        ? const HomeShell(key: ValueKey('home_shell'))
                        : const LoginPage(key: ValueKey('login_page')),
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
