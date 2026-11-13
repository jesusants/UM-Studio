import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/models/curriculum_models.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/screens/desktop/widgets/desktop_sidebar.dart';
import 'package:um_studio/presentation/screens/desktop/widgets/desktop_subject_detail_view.dart';
import 'package:um_studio/presentation/screens/home/home_shell.dart';
import 'package:um_studio/presentation/screens/home/tabs/estudio_tab.dart';
import 'package:um_studio/presentation/widgets/admin_env_console_modal.dart';
import 'package:um_studio/presentation/widgets/ai_graphic_block.dart';
import 'package:um_studio/presentation/widgets/collapsible_spaces_dock.dart';
import 'package:um_studio/presentation/widgets/interactive_engineering_chart.dart';
import 'package:um_studio/presentation/widgets/ios_primitives.dart';
import 'package:um_studio/presentation/widgets/lab/subject_lab_registry.dart';

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
    testWidgets('SubjectLabRegistry aísla simuladores por asignatura y oculta materias no gráficas',
        (tester) async {
      // Materias humanísticas / idiomas no tienen laboratorio gráfico
      expect(
        SubjectLabRegistry.hasLabsForSubject(
          codigo: '01011801',
          nombre: 'Procesos Lectores y Escriturales',
        ),
        isFalse,
      );
      expect(
        SubjectLabRegistry.hasLabsForSubject(
          codigo: '01021802',
          nombre: 'General English I',
        ),
        isFalse,
      );
      expect(
        SubjectLabRegistry.hasLabsForSubject(
          codigo: '01011899',
          nombre: 'Constitución Política y Legislación',
        ),
        isFalse,
      );

      // Las 16 asignaturas de Cuatrimestres 1 al 4 cuentan con simuladores aislados
      const codes = [
        '02011807', // Cálculo Diferencial
        '02011809', // Álgebra Lineal
        '03011813', // Fundamentos de Programación e IA
        '04011822', // Introducción a la Ingeniería Energética
        '02021810', // Física Mecánica
        '02011808', // Cálculo Integral
        '02031812', // Química Aplicada
        '03041819', // Fundamentos de la Electricidad I
        '02021811', // Calor y Ondas
        '04021825', // Modelación Matemática para Ingeniería
        '03041820', // Fundamentos de Electricidad II
        '04021823', // Ingeniería del Diseño y Modelado en 3D
        '03041821', // Electricidad y Magnetismo
        '03021817', // Termodinámica
        '03031818', // Probabilidad y Estadística
        '03021815', // Fundamentos de Hidráulica y Neumática
      ];
      for (final code in codes) {
        final cfg = SubjectLabRegistry.resolve(codigo: code, nombre: '');
        expect(cfg, isNotNull, reason: 'Falta configuración de lab para $code');
        expect(cfg!.simulators, isNotEmpty);
      }
    });

    testWidgets('InteractiveEngineeringChart muestra exclusivamente simuladores de la materia activa y controles de movimiento 60 FPS',
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
              asignaturaCodigo: '03041820',
              asignaturaNombre: 'Fundamentos de Electricidad II',
              temaTitulo: 'Circuitos CA y Fasores',
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 50));

      // Solo muestra los 2 simuladores de Electricidad II y NO mezcla Cálculo ni Termodinámica
      expect(find.text('Fasores Rotatorios CA'), findsOneWidget);
      expect(find.text('Transitorio RC / RL'), findsOneWidget);
      expect(find.text('Derivada y Tangente'), findsNothing);
      expect(find.text('Ciclo P-V + Pistón'), findsNothing);
      expect(find.text('Vₘ (Voltaje)'), findsOneWidget);

      // Controles universales de movimiento presentes (0.5x, 1.0x, 2.0x)
      expect(find.text('0.5x'), findsOneWidget);
      expect(find.text('1.0x'), findsOneWidget);
      expect(find.text('2.0x'), findsOneWidget);

      // Cambiar al segundo simulador de la misma materia (Transitorio RC / RL)
      await tester.ensureVisible(find.text('Transitorio RC / RL'));
      await tester.tap(find.text('Transitorio RC / RL'));
      await tester.pump(const Duration(milliseconds: 50));
      expect(find.text('Constante τ = RC'), findsOneWidget);
    });

    testWidgets('Física Mecánica (02021810) carga sus 4 simuladores y preselecciona según el tema sin overflow',
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
              asignaturaCodigo: '02021810',
              asignaturaNombre: 'Física Mecánica',
              temaTitulo: 'Fuerzas Conservativas y Resorte',
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 50));

      expect(find.text('Masa-Resorte y Energía'), findsOneWidget);
      expect(find.text('Tiro Parabólico'), findsOneWidget);
      expect(find.text('Plano Inclinado y DCL'), findsOneWidget);
      expect(find.text('Colisiones 1D'), findsOneWidget);
      expect(find.text('Constante Resorte k'), findsOneWidget);

      // Cambiar a Tiro Parabólico
      await tester.tap(find.text('Tiro Parabólico'));
      await tester.pump(const Duration(milliseconds: 50));
      expect(find.text('Velocidad Inicial v₀'), findsOneWidget);
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

  group('Limpieza UI: Sin barras de avance ni porcentajes de asignaturas', () {
    const sampleSubject = AsignaturaModel(
      codigo: '02011807',
      nombre: 'Física Mecánica',
      cuatrimestre: 2,
      creditos: 4,
      obligatoria: true,
      categoria: 'ciencias_basicas',
      colorHex: '#30D158',
      temas: [
        TemaClaseVivaModel(
          numeroTema: 1,
          titulo: 'Cinemática y Leyes de Newton',
          objetivo: 'Analizar el movimiento y las fuerzas.',
          conceptoClaveLatex: r'\sum \vec{F} = m \vec{a}',
          ejemplo: 'Bloque sobre plano inclinado.',
          bloqueSugerido: 'Pomodoro 50/10',
        ),
      ],
    );

    testWidgets('Escritorio 1440px: DesktopSidebar y DesktopSubjectDetailView omiten barras y píldora de avance',
        (tester) async {
      tester.view.devicePixelRatio = 1.0;
      tester.view.physicalSize = const Size(1440, 900);
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      final repo = LocalReactiveClaseVivaRepository();
      final curriculum = MarkdownCurriculumService();
      final session = InstitutionalSessionController(
        repository: repo,
        curriculumService: curriculum,
      );
      final theme = ThemeController();

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
                  home: Scaffold(
                    body: Row(
                      children: [
                        SizedBox(
                          width: 340,
                          child: DesktopSidebar(
                            selectedCuatrimestre: 2,
                            onSelectCuatrimestre: (_) {},
                            subjects: const [sampleSubject],
                            selectedSubject: sampleSubject,
                            onSelectSubject: (_) {},
                            onOpenStudentProfile: () {},
                          ),
                        ),
                        Expanded(
                          child: DesktopSubjectDetailView(
                            subject: sampleSubject,
                            onBackToDashboard: () {},
                            onOpenClaseViva: (_) {},
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 300));

      expect(find.text('02011807'), findsOneWidget);
      expect(find.text('4 créd.'), findsOneWidget);
      expect(find.text('Física Mecánica'), findsWidgets);
      expect(find.byType(LinearProgressIndicator), findsNothing);
      expect(find.byType(ProgressBar), findsNothing);
      expect(find.textContaining('Avance:'), findsNothing);
      expect(find.text('0%'), findsNothing);
    });

    testWidgets('Móvil 390px: EstudioTab renderiza asignaturas sin ProgressBar ni etiquetas de porcentaje',
        (tester) async {
      tester.view.devicePixelRatio = 1.0;
      tester.view.physicalSize = const Size(390, 844);
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      final repo = LocalReactiveClaseVivaRepository();
      final curriculum = _InMemoryCurriculumService(const [sampleSubject]);
      final session = InstitutionalSessionController(
        repository: repo,
        curriculumService: curriculum,
      );
      final theme = ThemeController();

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
                  home: Scaffold(
                    body: EstudioTab(
                      onOpenClaseViva: (_) {},
                    ),
                  ),
                ),
              ),
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 200));

      await tester.enterText(find.byType(TextField), 'Física');
      await tester.pump(const Duration(milliseconds: 200));

      expect(find.text('Física Mecánica'), findsOneWidget);
      expect(find.textContaining('02011807 • 4 cr'), findsOneWidget);
      expect(find.byType(LinearProgressIndicator), findsNothing);
      expect(find.byType(ProgressBar), findsNothing);
      expect(find.textContaining('Avance:'), findsNothing);
      expect(find.text('0%'), findsNothing);
    });
  });

  group('FASE 5: Menú Admin sin Gemini 2.x y Controles Gráficos', () {
    testWidgets('AdminEnvConsoleModal expone modelos vigentes (sin 2.0/2.5) y elementos gráficos',
        (tester) async {
      tester.view.devicePixelRatio = 1.0;
      tester.view.physicalSize = const Size(1280, 860);
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.light,
          darkTheme: AppTheme.dark,
          themeMode: ThemeMode.dark,
          home: const Scaffold(
            body: AdminEnvConsoleModal(),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 300));

      // Verifica modelos vigentes en Admin y ausencia de modelos 2.x retirados
      expect(find.text('gemini-3.5-flash-lite'), findsOneWidget);
      expect(find.text('gemini-2.5-flash'), findsNothing);
      expect(find.text('gemini-2.0-flash-lite'), findsNothing);
      expect(find.text('Permitir Elementos Gráficos en IA'), findsOneWidget);
      expect(find.text('Sincronizar Modelos en Vivo'), findsOneWidget);

      // Cambia a pestaña Broadcast Global y verifica controles gráficos del banner
      await tester.tap(find.text('Broadcast Global'));
      await tester.pump(const Duration(milliseconds: 200));

      await tester.scrollUntilVisible(
        find.text('Elemento Gráfico del Anuncio (Imagen / Diagrama)'),
        180,
        scrollable: find.byType(Scrollable).last,
      );
      expect(
        find.text('Elemento Gráfico del Anuncio (Imagen / Diagrama)'),
        findsOneWidget,
      );
      await tester.scrollUntilVisible(
        find.text('Gráfica Interactiva Adjunta al Anuncio'),
        180,
        scrollable: find.byType(Scrollable).last,
      );
      expect(
        find.text('Gráfica Interactiva Adjunta al Anuncio'),
        findsOneWidget,
      );
      await tester.scrollUntilVisible(
        find.text('Fasores AC'),
        180,
        scrollable: find.byType(Scrollable).last,
      );
      expect(find.text('Fasores AC'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });

    testWidgets('AiGraphicBlockWidget renderiza vectores y barras sin overflow en 350px',
        (tester) async {
      tester.view.devicePixelRatio = 1.0;
      tester.view.physicalSize = const Size(350, 800);
      addTearDown(() {
        tester.view.resetPhysicalSize();
        tester.view.resetDevicePixelRatio();
      });

      const vectorSpec = AiGraphicSpec(
        tipo: 'vectores',
        titulo: 'Fuerzas en Rampa',
        vectores: [
          AiGraphicVector(name: 'N', angleDeg: 90, magnitude: 1.0, colorKey: 'green'),
          AiGraphicVector(name: 'mg', angleDeg: -90, magnitude: 1.0, colorKey: 'orange'),
        ],
      );

      const barSpec = AiGraphicSpec(
        tipo: 'barras',
        titulo: 'Balance Energético',
        barras: [
          AiGraphicBar(label: 'Ec', value: 70, colorKey: 'indigo'),
          AiGraphicBar(label: 'Ep', value: 30, colorKey: 'green'),
        ],
      );

      await tester.pumpWidget(
        wrapWithApp(
          const SingleChildScrollView(
            padding: EdgeInsets.all(12),
            child: Column(
              children: [
                AiGraphicBlockWidget(spec: vectorSpec),
                SizedBox(height: 12),
                AiGraphicBlockWidget(spec: barSpec),
              ],
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      expect(find.text('Fuerzas en Rampa'), findsOneWidget);
      expect(find.text('Balance Energético'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  });
}

class _InMemoryCurriculumService extends MarkdownCurriculumService {
  _InMemoryCurriculumService(this._subjects);

  final List<AsignaturaModel> _subjects;

  @override
  List<AsignaturaModel> get allAsignaturas => _subjects;
}
