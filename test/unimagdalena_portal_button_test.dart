import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/presentation/widgets/unimagdalena_portal_button.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  group('UnimagdalenaPortalButton - Widget, Flotabilidad y Cero Layout Shift', () {
    testWidgets('Estado de reposo renderiza forma compacta (36x36) con tooltip y sin texto expandido', (tester) async {
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
      expect(tooltip.message, 'Portal Estudiantes Unimagdalena (AyRe)');

      // La huella en el layout tree debe ser exactamente 36x36
      final outerSize = tester.getSize(find.byType(UnimagdalenaPortalButton));
      expect(outerSize.width, 36.0);
      expect(outerSize.height, 36.0);

      // En reposo no debe haber texto de 'Portal Estudiantes'
      expect(find.text('Portal Estudiantes'), findsNothing);
    });

    testWidgets('Hover expande flotando hacia 160px mientras la huella en el Row permanece fija en 36px', (tester) async {
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

      // La huella del widget UnimagdalenaPortalButton permanece estrictamente en 36x36 px
      final outerSize = tester.getSize(find.byType(UnimagdalenaPortalButton));
      expect(outerSize.width, 36.0);
      expect(outerSize.height, 36.0);

      // El AnimatedContainer interno flotante expande a 160 px
      final animContainer = tester.widget<AnimatedContainer>(find.byType(AnimatedContainer));
      expect(animContainer.constraints?.maxWidth, 160.0);
      expect(find.text('Portal Estudiantes'), findsOneWidget);
      expect(find.byIcon(Icons.north_east_rounded), findsOneWidget);

      // Mover el cursor fuera del botón
      await gesture.moveTo(const Offset(5, 5));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 250));

      final animContainerExit = tester.widget<AnimatedContainer>(find.byType(AnimatedContainer));
      expect(animContainerExit.constraints?.maxWidth, 36.0);
      expect(find.text('Portal Estudiantes'), findsNothing);
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

    testWidgets('expandOnHover = false mantiene botón compacto fijo en 36px en hover', (tester) async {
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

      final animContainer = tester.widget<AnimatedContainer>(find.byType(AnimatedContainer));
      expect(animContainer.constraints?.maxWidth, 36.0);
      expect(find.text('Portal Estudiantes'), findsNothing);
    });

    testWidgets('Dentro de un Row estrecho (280px), el hover NUNCA desplaza a "UM STUDIO"', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: Center(
              child: SizedBox(
                width: 280,
                child: Row(
                  children: [
                    Expanded(
                      child: Text(
                        'UM STUDIO',
                        maxLines: 1,
                        softWrap: false,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                    SizedBox(width: 6),
                    UnimagdalenaPortalButton(),
                    SizedBox(width: 6),
                    Text('🌙 Oscuro'),
                  ],
                ),
              ),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      final titleRectBefore = tester.getRect(find.text('UM STUDIO'));

      final gesture = await tester.createGesture(kind: PointerDeviceKind.mouse);
      await gesture.addPointer(location: Offset.zero);
      addTearDown(gesture.removePointer);

      await gesture.moveTo(tester.getCenter(find.byType(UnimagdalenaPortalButton)));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 250));

      final titleRectAfter = tester.getRect(find.text('UM STUDIO'));

      // Las coordenadas y tamaño de 'UM STUDIO' deben ser 100% idénticas
      expect(titleRectAfter, equals(titleRectBefore));
      expect(tester.takeException(), isNull);
    });
  });
}
