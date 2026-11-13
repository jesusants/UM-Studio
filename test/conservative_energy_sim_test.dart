import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/presentation/widgets/conservative_energy_sim_widget.dart';

void main() {
  setUpAll(() {
    GoogleFonts.config.allowRuntimeFetching = false;
  });

  group('ConservativeEnergyPhysics - Cátedra 7', () {
    test('Problema 01 alcanza v_f = 8.40 m/s y conserva EM = 70.56 J en todas las trayectorias', () {
      for (final profile in RampCurveProfile.values) {
        final trace = ConservativeEnergyPhysics.runTrajectory(
          problem: ConservativeProblemType.curvedRamp,
          rampMass: 2.0,
          rampHeightM: 3.6,
          rampProfile: profile,
        );

        expect(trace, isNotEmpty);
        final first = trace.first;
        final last = trace.last;

        expect(first.gravitationalEnergy, closeTo(70.56, 1e-3));
        expect(first.kineticEnergy, closeTo(0.0, 1e-3));
        expect(last.isFinished, isTrue);
        expect(last.y, closeTo(0.0, 1e-3));
        expect(last.speed, closeTo(8.40, 0.02));
        expect(last.kineticEnergy, closeTo(70.56, 0.05));

        for (final step in trace) {
          expect(step.totalMechanicalEnergy, closeTo(70.56, 0.05));
          expect(step.dissipatedThermalEnergy, 0.0);
        }
      }
    });

    test('Problema 02 convierte Ue = 8.0 J y se detiene por fricción en d ≈ 1.555 m', () {
      final trace = ConservativeEnergyPhysics.runTrajectory(
        problem: ConservativeProblemType.springFriction,
        springMass: 1.5,
        springK: 400.0,
        springCompression: 0.20,
        muK: 0.35,
      );

      expect(trace, isNotEmpty);
      final first = trace.first;
      final last = trace.last;

      expect(first.elasticEnergy, closeTo(8.0, 1e-3));
      expect(first.x, closeTo(-0.20, 1e-6));
      expect(last.isFinished, isTrue);
      expect(last.speed, closeTo(0.0, 1e-3));
      expect(last.x, closeTo(1.555, 0.015));
      expect(last.dissipatedThermalEnergy, closeTo(8.0, 0.05));
      expect(last.totalMechanicalEnergy, closeTo(0.0, 0.05));

      for (final step in trace) {
        expect(
          step.totalMechanicalEnergy + step.dissipatedThermalEnergy,
          closeTo(8.0, 0.08),
        );
      }
    });
  });

  group('ConservativeEnergySimWidget UI', () {
    Widget buildHarness({
      required double width,
      required bool isDesktop,
      Brightness brightness = Brightness.dark,
    }) {
      final palette =
          brightness == Brightness.dark ? AppPalette.dark : AppPalette.light;
      final theme = ThemeData(
        brightness: brightness,
        extensions: [palette],
      );
      return MaterialApp(
        theme: theme,
        home: Scaffold(
          body: SingleChildScrollView(
            padding: const EdgeInsets.all(12),
            child: Center(
              child: SizedBox(
                width: width,
                child: ConservativeEnergySimWidget(isDesktop: isDesktop),
              ),
            ),
          ),
        ),
      );
    }

    testWidgets('renderiza en viewport móvil y alterna entre P1 y P2 sin overflow',
        (tester) async {
      await tester.binding.setSurfaceSize(const Size(390, 844));
      addTearDown(() => tester.binding.setSurfaceSize(null));

      await tester.pumpWidget(buildHarness(width: 360, isDesktop: false));
      await tester.pump(const Duration(milliseconds: 100));

      expect(find.textContaining('Problema 01'), findsOneWidget);
      expect(find.textContaining('8.40 m/s'), findsOneWidget);

      await tester.tap(find.textContaining('P2 • Resorte + Fricción'));
      await tester.pump(const Duration(milliseconds: 120));

      expect(find.textContaining('Problema 02'), findsOneWidget);
      expect(find.textContaining('1.555 m'), findsOneWidget);

      await tester.tap(find.text('Ajustar Variables'));
      await tester.pump(const Duration(milliseconds: 80));
      expect(find.text('Valores Cátedra 7'), findsOneWidget);
    });

    testWidgets('renderiza en viewport desktop y tema claro sin errores',
        (tester) async {
      await tester.binding.setSurfaceSize(const Size(1280, 800));
      addTearDown(() => tester.binding.setSurfaceSize(null));

      await tester.pumpWidget(
        buildHarness(
          width: 720,
          isDesktop: true,
          brightness: Brightness.light,
        ),
      );
      await tester.pump(const Duration(milliseconds: 150));

      expect(find.text('Braquistócrona'), findsOneWidget);
      await tester.tap(find.text('Braquistócrona'));
      await tester.pump(const Duration(milliseconds: 150));

      expect(find.textContaining('70.56 J'), findsWidgets);
    });
  });
}
