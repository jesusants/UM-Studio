import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import 'core/constants/app_constants.dart';
import 'core/theme/app_theme.dart';
import 'data/repositories/local_clase_viva_repository.dart';
import 'data/repositories/supabase_clase_viva_repository.dart';
import 'domain/repositories/i_clase_viva_repository.dart';
import 'presentation/providers/app_scopes.dart';
import 'presentation/screens/home/home_shell.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final themeController = ThemeController();
  await themeController.load();

  late final IClaseVivaRepository repository;
  if (AppConstants.isSupabaseConfigured) {
    await Supabase.initialize(
      url: AppConstants.supabaseUrl,
      publishableKey: AppConstants.supabaseAnonKey,
    );
    repository = SupabaseClaseVivaRepository(
      client: Supabase.instance.client,
    );
  } else {
    repository = LocalReactiveClaseVivaRepository();
  }

  final sessionController = InstitutionalSessionController(
    repository: repository,
  );
  await sessionController.load();

  runApp(
    UmStudioApp(
      themeController: themeController,
      repository: repository,
      sessionController: sessionController,
    ),
  );
}

class UmStudioApp extends StatelessWidget {
  const UmStudioApp({
    super.key,
    required this.themeController,
    required this.repository,
    this.sessionController,
  });

  final ThemeController themeController;
  final IClaseVivaRepository repository;
  final InstitutionalSessionController? sessionController;

  @override
  Widget build(BuildContext context) {
    final effectiveSession = sessionController ??
        InstitutionalSessionController(repository: repository);

    return ClaseVivaRepositoryScope(
      repository: repository,
      child: SessionScope(
        controller: effectiveSession,
        child: ThemeScope(
          controller: themeController,
          child: ListenableBuilder(
            listenable: themeController,
            builder: (context, _) => MaterialApp(
              title: 'UM STUDIO — iOS Minimalist Edition',
              debugShowCheckedModeBanner: false,
              theme: AppTheme.light,
              darkTheme: AppTheme.dark,
              themeMode: themeController.mode,
              themeAnimationDuration: const Duration(milliseconds: 350),
              themeAnimationCurve: Curves.easeInOut,
              home: const HomeShell(),
            ),
          ),
        ),
      ),
    );
  }
}
