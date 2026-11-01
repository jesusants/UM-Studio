import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/screens/clase_viva/clase_viva_page.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  testWidgets('Test scroll on English 1 to 5 in ClaseVivaPage', (tester) async {
    tester.view.physicalSize = const Size(430, 900);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    SharedPreferences.setMockInitialValues({});
    final mdContent = File('assets/data/ingenieria_energetica.md').readAsStringSync();
    final curriculum = MarkdownCurriculumService()
      ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

    final repo = LocalReactiveClaseVivaRepository(
      initialLatency: Duration.zero,
      userId: 'alumno@unimagdalena.edu.co',
      curriculumService: curriculum,
    );

    final englishCodes = ['01021802', '01021803', '01021804', '01021805', '01021806'];

    for (final code in englishCodes) {
      await tester.pumpWidget(
        CurriculumScope(
          service: curriculum,
          child: ClaseVivaRepositoryScope(
            repository: repo,
            child: ThemeScope(
              controller: ThemeController(),
              child: MaterialApp(
                theme: AppTheme.dark,
                home: ClaseVivaPage(temaId: code),
              ),
            ),
          ),
        ),
      );

      await tester.pump(const Duration(milliseconds: 300));
      for (var i = 0; i < 5; i++) {
        await tester.pump(const Duration(milliseconds: 100));
      }

      // Scroll to bottom
      final listFinder = find.byType(ListView).first;
      for (var i = 0; i < 10; i++) {
        await tester.drag(listFinder, const Offset(0, -300));
        await tester.pump(const Duration(milliseconds: 50));
      }

      // Verify no exceptions were thrown
      expect(tester.takeException(), isNull, reason: 'Failed on code $code');

      // Check if ErrorWidget is present
      expect(find.byType(ErrorWidget), findsNothing, reason: 'ErrorWidget found on code $code');
    }
  });
}
