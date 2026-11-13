import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/screens/home/home_shell.dart';
import 'package:um_studio/presentation/widgets/collapsible_spaces_dock.dart';
import 'package:um_studio/presentation/widgets/interactive_engineering_chart.dart';

void main() {
  setUpAll(() {
    GoogleFonts.config.allowRuntimeFetching = false;
  });

  Widget wrapWithApp(Widget child, {Brightness brightness = Brightness.dark}) {
    final palette =
        brightness == Brightness.dark ? AppPalette.dark : AppPalette.light;
    return MaterialApp(
      theme: ThemeData(brightness: brightness, extensions: [palette]),
      home: Scaffold(body: child),
    );
  }

  group('FASE 1: CollapsibleSpacesDock & Arquitectura Responsiva', () {
    testWidgets('Dock móvil alterna entre expandido y píldora colapsada de 40px sin overflow en 390px',
        (tester) async {
      await tester.binding.setSurfaceSize(const Size(390, 844));
      addTearDown(() => tester.binding.setSurfaceSize(null));

      var collapsed = false;
      var selected = 0;

      await tester.pumpWidget(
        StatefulBuilder(
          builder: (context, setState) {
            return wrapWithApp(
              Align(
                alignment: Alignment.bottomCenter,
                child: CollapsibleSpacesDock(
                  currentIndex: selected,
                  isCollapsed: collapsed,
                  onSelect: (i) => setState(() => selected = i),
                  onToggleCollapsed: () =>
                      setState(() => collapsed = !collapsed),
                ),
              ),
            );
          },
        ),
      );

      expect(find.byKey(const ValueKey('dock_expanded')), findsOneWidget);
      expect(find.text('Resumen'), findsOneWidget);

      await tester.tap(find.byIcon(Icons.keyboard_arrow_down_rounded));
      await tester.pumpAndSettle();

      expect(find.byKey(const ValueKey('dock_collapsed')), findsOneWidget);
      expect(find.byIcon(Icons.keyboard_arrow_up_rounded), findsOneWidget);
    });

    testWidgets('HomeShell renderiza sin overflow en 390px, 820px y oculta el dock móvil en 1440px',
        (tester) async {
      final repo = LocalReactiveClaseVivaRepository();
      final curriculum = MarkdownCurriculumService();
      final session = InstitutionalSessionController(
        repository: repo,
        curriculumService: curriculum,
      );
      final theme = ThemeController();

      Future<void> pumpAtSize(Size size) async {
        tester.view.devicePixelRatio = 1.0;
        tester.view.physicalSize = size;
        await tester.pumpWidget(
          CurriculumScope(
            service: curriculum,
            child: ClaseVivaRepositoryScope(
              repository: repo,
              child: SessionScope(
                controller: session,
                child: ThemeScope(
                  controller: theme,
                  child: MaterialApp(
                    theme: AppTheme.light,
                    darkTheme: AppTheme.dark,
                    themeMode: ThemeMode.dark,
                    home: const HomeShell(),
                  ),
                ),
              ),
            ),
          ),
        );
        await tester.pump(const Duration(milliseconds: 200));
      }

      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      // Móvil 390px -> Muestra Dock desplegable móvil
      await pumpAtSize(const Size(390, 844));
      expect(find.byType(CollapsibleSpacesDock), findsOneWidget);

      // Tablet 820px (< 1024px) -> Muestra Dock desplegable sin overflow
      await pumpAtSize(const Size(820, 1180));
      expect(find.byType(CollapsibleSpacesDock), findsOneWidget);

      // Escritorio 1440px (>= 1024px) -> Prohibido mostrar Dock móvil
      await pumpAtSize(const Size(1440, 900));
      expect(find.byType(CollapsibleSpacesDock), findsNothing);
    });
  });

  group('FASE 5: Motor de Gráficas Interactivas y Analítica', () {
    testWidgets('InteractiveEngineeringChart cambia entre los 3 laboratorios y sliders sin overflow',
        (tester) async {
      tester.view.devicePixelRatio = 1.0;
      tester.view.physicalSize = const Size(420, 900);
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      await tester.pumpWidget(
        wrapWithApp(
          const SingleChildScrollView(
            padding: EdgeInsets.all(12),
            child: InteractiveEngineeringChart(
              asignaturaNombre: 'Fundamentos de Electricidad II',
              temaTitulo: 'Circuitos CA y Fasores',
            ),
          ),
        ),
      );
      await tester.pump();

      expect(find.text('Vₘ (Voltaje)'), findsOneWidget);

      await tester.ensureVisible(find.text('Cálculo / Tangente'));
      await tester.tap(find.text('Cálculo / Tangente'));
      await tester.pump();
      expect(find.text('Tangente x₀'), findsOneWidget);

      await tester.ensureVisible(find.text('Energía / Termo'));
      await tester.tap(find.text('Energía / Termo'));
      await tester.pump();
      expect(find.text('Irradiancia G'), findsOneWidget);

      await tester.ensureVisible(find.text('Transitorio 2° Orden'));
      await tester.tap(find.text('Transitorio 2° Orden'));
      await tester.pump();
      expect(find.text('Amortiguamiento ζ'), findsOneWidget);
    });

    testWidgets('RadialCorteProgressCard y StudyActivityHeatmapCard renderizan correctamente',
        (tester) async {
      await tester.binding.setSurfaceSize(const Size(390, 844));
      addTearDown(() => tester.binding.setSurfaceSize(null));

      await tester.pumpWidget(
        wrapWithApp(
          SingleChildScrollView(
            padding: const EdgeInsets.all(12),
            child: Column(
              children: [
                const RadialCorteProgressCard(
                  corte1Progress: 0.80,
                  corte2Progress: 0.50,
                  corte3Progress: 0.25,
                ),
                const SizedBox(height: 12),
                StudyActivityHeatmapCard(
                  dailyIntensities: List<int>.generate(60, (i) => i % 5),
                ),
              ],
            ),
          ),
        ),
      );
      await tester.pump();

      expect(find.text('AVANCE POR CORTE ACADÉMICO'), findsOneWidget);
      expect(find.text('CONSTANCIA DE ESTUDIO (60 DÍAS)'), findsOneWidget);
    });
  });
}
