import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/presentation/widgets/unimagdalena_portal_button.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  group('UnimagdalenaPortalButton - Widget y Micro-interacciones', () {
    testWidgets('Estado de reposo renderiza forma compacta con tooltip e icono', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: Center(
              child: UnimagdalenaPortalButton(),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      expect(find.byType(UnimagdalenaPortalButton), findsOneWidget);
      expect(find.byType(Tooltip), findsOneWidget);

      final tooltip = tester.widget<Tooltip>(find.byType(Tooltip));
      expect(tooltip.message, 'Módulo de Estudiantes Unimagdalena (AyRe)');

      // En reposo (sin hover), no debe mostrarse el segundo hijo del crossfade
      final crossFade = tester.widget<AnimatedCrossFade>(find.byType(AnimatedCrossFade));
      expect(crossFade.crossFadeState, CrossFadeState.showFirst);
    });

    testWidgets('Hover expande suavemente el ancho y revela "Portal Estudiantes ↗"', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: Center(
              child: UnimagdalenaPortalButton(),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      final gesture = await tester.createGesture(kind: PointerDeviceKind.mouse);
      await gesture.addPointer(location: Offset.zero);
      addTearDown(gesture.removePointer);

      // Mover el cursor dentro del botón
      await gesture.moveTo(tester.getCenter(find.byType(UnimagdalenaPortalButton)));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 250));

      final crossFade = tester.widget<AnimatedCrossFade>(find.byType(AnimatedCrossFade));
      expect(crossFade.crossFadeState, CrossFadeState.showSecond);
      expect(find.text('Portal Estudiantes'), findsOneWidget);
      expect(find.byIcon(Icons.north_east_rounded), findsOneWidget);

      // Mover el cursor fuera del botón
      await gesture.moveTo(const Offset(5, 5));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 250));

      final crossFadeExit = tester.widget<AnimatedCrossFade>(find.byType(AnimatedCrossFade));
      expect(crossFadeExit.crossFadeState, CrossFadeState.showFirst);
    });

    testWidgets('Tap ejecuta callback de navegación', (tester) async {
      var tapped = false;

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.light,
          home: Scaffold(
            body: Center(
              child: UnimagdalenaPortalButton(
                onTap: () => tapped = true,
              ),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      await tester.tap(find.byType(UnimagdalenaPortalButton));
      await tester.pump();

      expect(tapped, isTrue);
    });

    testWidgets('expandOnHover = false mantiene botón compacto fijo en hover', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: Center(
              child: UnimagdalenaPortalButton(expandOnHover: false),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      final gesture = await tester.createGesture(kind: PointerDeviceKind.mouse);
      await gesture.addPointer(location: Offset.zero);
      addTearDown(gesture.removePointer);

      await gesture.moveTo(tester.getCenter(find.byType(UnimagdalenaPortalButton)));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 250));

      // No debe contener AnimatedCrossFade al estar deshabilitada la expansión
      expect(find.byType(AnimatedCrossFade), findsNothing);
      expect(find.text('Portal Estudiantes'), findsNothing);
    });
  });
}
