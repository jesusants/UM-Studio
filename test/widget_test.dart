import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/core/utils/institutional_validator.dart';
import 'package:um_studio/data/models/nota_adjunto_model.dart';
import 'package:um_studio/data/models/tema_estudio_model.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/domain/entities/nota_adjunto_entity.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/screens/clase_viva/clase_viva_page.dart';
import 'package:um_studio/presentation/widgets/ios_primitives.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  group('Design Tokens, ThemeController & Validación @unimagdalena.edu.co', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test('valida tokens estrictos iOS OLED y modo claro', () {
      expect(AppPalette.dark.background, const Color(0xFF000000));
      expect(AppPalette.dark.card, const Color(0xFF121316));
      expect(AppPalette.dark.cardBorder, const Color(0xFF1F2228));
      expect(AppPalette.dark.green, const Color(0xFF30D158));
      expect(AppPalette.dark.indigo, const Color(0xFF5E5CE6));
      expect(AppPalette.dark.textSecondary, const Color(0xFF8E8E93));
      expect(AppPalette.dark.shimmerBase, const Color(0xFF1A1D24));
      expect(AppPalette.light.card, const Color(0xFFF2F2F7));
    });

    test('restringe estrictamente el dominio a @unimagdalena.edu.co', () async {
      expect(
        InstitutionalValidator.isValidInstitutionalEmail(
          'carlos.mendoza@unimagdalena.edu.co',
        ),
        isTrue,
      );
      expect(
        InstitutionalValidator.isValidInstitutionalEmail('usuario@gmail.com'),
        isFalse,
      );
      expect(
        InstitutionalValidator.isValidInstitutionalEmail(
          'test@unimagdalena.com',
        ),
        isFalse,
      );

      final repo = LocalReactiveClaseVivaRepository(
        initialLatency: Duration.zero,
      );
      final session = InstitutionalSessionController(repository: repo);
      await session.load();

      final err = await session.updateInstitutionalEmail(' intruso@gmail.com ');
      expect(err, isNotNull);
      expect(err, contains('@unimagdalena.edu.co'));

      final ok = await session.updateInstitutionalEmail(
        'energia.2026@unimagdalena.edu.co',
      );
      expect(ok, isNull);
      expect(repo.activeUserId, 'energia.2026@unimagdalena.edu.co');
    });

    test('toggle alterna el tema y lo persiste', () async {
      final c = ThemeController();
      await c.load();
      expect(c.mode, ThemeMode.dark);

      await c.toggle();
      expect(c.mode, ThemeMode.light);

      final c2 = ThemeController();
      await c2.load();
      expect(c2.mode, ThemeMode.light);
    });
  });

  group('Esquema Relacional & Repositorio Reactivo', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test('serializa temas_estudio y formatea pesos KB/MB', () {
      final tema = TemaEstudioModel.fromJson({
        'id': 'fisica',
        'nombre_asignatura': 'Física Mecánica y Termodinámica',
        'numero_tema': 2,
        'objetivo': 'Segunda ley de Newton.',
        'concepto_clave_latex': r'\sum \vec{F} = m \cdot \vec{a}',
        'ejemplo': 'Bloque con fricción.',
      });
      expect(tema.badgeTema, 'Tema 2');
      expect(
        tema.toJson()['concepto_clave_latex'],
        r'\sum \vec{F} = m \cdot \vec{a}',
      );

      final now = DateTime.now();
      final pdfKb = NotaAdjuntoModel(
        id: '1',
        temaId: 'fisica',
        usuarioId: 'alumno@unimagdalena.edu.co',
        tipoArchivo: TipoAdjuntoEstudiante.pdf,
        pesoBytes: 430080,
        createdAt: now,
        updatedAt: now,
      );
      final imgMb = pdfKb.copyWith(
        tipoArchivo: TipoAdjuntoEstudiante.imagen,
        pesoBytes: 2411724,
      );
      expect(pdfKb.pesoFormateado, '420 KB');
      expect(imgMb.pesoFormateado, '2.30 MB');
    });

    test('sube archivos adjuntos, elimina y persiste notas', () async {
      final repo = LocalReactiveClaseVivaRepository(
        initialLatency: Duration.zero,
        userId: 'alumno@unimagdalena.edu.co',
      );

      final sub = await repo.subirArchivoAdjunto(
        temaId: 'fisica',
        tipoArchivo: TipoAdjuntoEstudiante.pdf,
        nombreArchivo: 'Guia_Newton.pdf',
        bytes: Uint8List.fromList(List<int>.filled(2048, 7)),
      );
      expect(sub.tipoArchivo, TipoAdjuntoEstudiante.pdf);
      expect(sub.pesoFormateado, '2.0 KB');

      await repo.guardarNotaPersonal(
        temaId: 'fisica',
        contenido: r'Recordar fricción estática $f_s \le \mu_s N$',
      );

      final snapshot = await repo.watchNotasYAdjuntos(temaId: 'fisica').first;
      expect(snapshot.length, 2);

      await repo.eliminarAdjunto(adjunto: sub);
      final afterDelete =
          await repo.watchNotasYAdjuntos(temaId: 'fisica').first;
      expect(afterDelete.where((e) => e.esArchivo), isEmpty);
      expect(
        afterDelete.single.contenidoNota,
        contains(r'$f_s \le \mu_s N$'),
      );
    });
  });

  group('ClaseVivaPage UI, Shimmer, KaTeX Nativo & Auto-Save', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    testWidgets(
      'muestra Shimmer (#1A1D24) sin spinner, renderiza KaTeX nativo y auto-guarda notas (debounce 1s)',
      (tester) async {
        tester.view.physicalSize = const Size(430, 1400);
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        final themeCtrl = ThemeController();
        final repo = LocalReactiveClaseVivaRepository(
          initialLatency: const Duration(milliseconds: 400),
          userId: 'alumno@unimagdalena.edu.co',
        );

        await repo.subirArchivoAdjunto(
          temaId: 'fisica',
          tipoArchivo: TipoAdjuntoEstudiante.pdf,
          nombreArchivo: 'Taller_Dinamica_U2.pdf',
          bytes: Uint8List.fromList(List<int>.filled(15360, 1)),
        );

        await tester.pumpWidget(
          ClaseVivaRepositoryScope(
            repository: repo,
            child: ThemeScope(
              controller: themeCtrl,
              child: MaterialApp(
                theme: AppTheme.light,
                darkTheme: AppTheme.dark,
                themeMode: ThemeMode.dark,
                home: const ClaseVivaPage(temaId: 'fisica'),
              ),
            ),
          ),
        );

        // 1. En fase de carga inicial debe mostrar IosShimmer y CERO CircularProgressIndicator.
        expect(find.byType(IosShimmer), findsOneWidget);
        expect(find.byType(CircularProgressIndicator), findsNothing);
        expect(find.text('Temario'), findsOneWidget);
        expect(find.text('UM STUDIO'), findsOneWidget);
        expect(find.text('SINCRONIZADO CON AULA'), findsOneWidget);

        // 2. Avanza el stream reactivo para cargar el contenido oficial.
        await tester.pump(const Duration(milliseconds: 450));
        await tester.pump(const Duration(milliseconds: 300));

        expect(find.text('ASIGNATURA'), findsOneWidget);
        expect(find.text('Física Mecánica y Termodinámica'), findsOneWidget);
        expect(find.text('Tema 2'), findsOneWidget);
        expect(find.text('OBJETIVO'), findsOneWidget);
        expect(find.text('CONCEPTO CLAVE'), findsOneWidget);
        expect(find.text('EJEMPLO DE CÁTEDRA'), findsOneWidget);

        // Verifica renderizado matemático nativo flutter_math_fork (sin WebView).
        expect(find.byType(Math), findsWidgets);

        // Verifica sección Mis Apuntes y Archivos + archivo adjunto vinculado.
        expect(find.text('MIS APUNTES Y ARCHIVOS'), findsOneWidget);
        expect(find.text('Adjuntar PDF'), findsOneWidget);
        expect(find.text('Foto Tablero'), findsOneWidget);
        expect(find.text('Taller_Dinamica_U2.pdf'), findsOneWidget);

        // 3. Prueba de auto-save debounce de 1 segundo en Notas Personales.
        final noteField = find.byType(TextField);
        await tester.enterText(
          noteField,
          r'Deducción en clase: $a = g \sin\theta$',
        );
        await tester.pump(const Duration(milliseconds: 500));

        // A los 500ms aún está en debounce (no guardado todavía).
        final itemsMid =
            await repo.watchNotasYAdjuntos(temaId: 'fisica').first;
        expect(
          itemsMid.where((e) => e.tipoArchivo == TipoAdjuntoEstudiante.nota),
          isEmpty,
        );

        // Al completar 1 segundo se sincroniza automáticamente.
        await tester.pump(const Duration(milliseconds: 600));
        final itemsSaved =
            await repo.watchNotasYAdjuntos(temaId: 'fisica').first;
        final savedNote = itemsSaved.firstWhere(
          (e) => e.tipoArchivo == TipoAdjuntoEstudiante.nota,
        );
        expect(
          savedNote.contenidoNota,
          r'Deducción en clase: $a = g \sin\theta$',
        );
      },
    );
  });
}
