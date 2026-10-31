import 'dart:convert';
import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/core/utils/institutional_validator.dart';
import 'package:um_studio/data/models/nota_adjunto_model.dart';
import 'package:um_studio/data/models/tema_estudio_model.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/github_sync_service.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/domain/entities/nota_adjunto_entity.dart';
import 'package:um_studio/domain/entities/subject_summary.dart';
import 'package:um_studio/main.dart';
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

    test('autocompleta prefijo institucional y bloquea dominios externos', () async {
      final okPrefix = InstitutionalValidator.parseInstitutionalUser('jsierra');
      expect(okPrefix.error, isNull);
      expect(okPrefix.identity?.username, 'jsierra');
      expect(okPrefix.identity?.email, 'jsierra@unimagdalena.edu.co');

      final badDomain =
          InstitutionalValidator.parseInstitutionalUser('intruso@gmail.com');
      expect(badDomain.identity, isNull);
      expect(badDomain.error, contains('@unimagdalena.edu.co'));

      final pinHash = InstitutionalValidator.hashPin('2026');
      expect(pinHash, isNot('2026'));
      expect(InstitutionalValidator.verifyPin('2026', pinHash), isTrue);
      expect(InstitutionalValidator.verifyPin('9999', pinHash), isFalse);
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

  group('Base de Datos .MD Ingeniería Energética (Plan 8108 + KaTeX)', () {
    test(
      'parsea las 56 asignaturas (12 cuatrimestres) y compila el 100% de fórmulas KaTeX sin errores',
      () {
        final mdContent = File('assets/data/ingenieria_energetica.md')
            .readAsStringSync();
        final dbContent = File('db/ingenieria_energetica.md')
            .readAsStringSync();
        expect(mdContent, equals(dbContent));

        final db = CurriculumMarkdownParser.parse(mdContent);
        expect(db.programa.codigoInterno, '8108');
        expect(db.programa.codigoSnies, '118222');
        expect(db.programa.nombre, 'Ingeniería Energética');
        expect(db.cuatrimestres.length, 12);
        expect(db.allAsignaturas.length, 56);

        var totalFormulas = 0;
        final failedFormulas = <String>[];

        for (final asig in db.allAsignaturas) {
          expect(asig.temas, isNotEmpty, reason: 'Sin temas en ${asig.nombre}');
          for (final tema in asig.temas) {
            totalFormulas++;
            final clean = InstitutionalValidator.sanitizeLatex(
              tema.conceptoClaveLatex,
            );
            final mathWidget = Math.tex(clean);
            if (mathWidget.parseError != null) {
              failedFormulas.add(
                '${asig.codigo} (${asig.nombre}) T${tema.numeroTema}: ${mathWidget.parseError}',
              );
            }
          }
        }

        expect(totalFormulas, greaterThanOrEqualTo(56));
        expect(
          failedFormulas,
          isEmpty,
          reason:
              'Fórmulas con error en flutter_math_fork:\n${failedFormulas.join('\n')}',
        );
      },
    );
  });

  group('GitHubSyncService Serverless (db/users/{username}.json)', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test(
      'registra usuario en GitHub (404 -> PUT Base64), persiste sesión y sincroniza recordatorios',
      () async {
        final fakeGitHubFiles = <String, String>{};
        var putCount = 0;

        final mockHttp = MockClient((http.Request req) async {
          final path = req.url.path;
          if (req.method == 'GET') {
            if (fakeGitHubFiles.containsKey(path)) {
              final rawJson = fakeGitHubFiles[path]!;
              final b64WithNewlines = base64Encode(utf8.encode(rawJson));
              return http.Response(
                jsonEncode({
                  'sha': 'sha_mock_$putCount',
                  'content': '$b64WithNewlines\n',
                }),
                200,
              );
            }
            return http.Response(jsonEncode({'message': 'Not Found'}), 404);
          }

          if (req.method == 'PUT') {
            putCount++;
            final body = jsonDecode(req.body) as Map<String, dynamic>;
            final decodedContent = utf8.decode(
              base64Decode(body['content'].toString()),
            );
            fakeGitHubFiles[path] = decodedContent;
            return http.Response(
              jsonEncode({
                'content': {'sha': 'sha_mock_$putCount'},
              }),
              201,
            );
          }

          return http.Response('Unsupported', 500);
        });

        final syncService = GitHubSyncService(httpClient: mockHttp);
        await syncService.setCustomGitHubToken('test_token_local_mock');

        final repo = LocalReactiveClaseVivaRepository(
          initialLatency: Duration.zero,
        );
        final session = InstitutionalSessionController(
          repository: repo,
          syncService: syncService,
        );

        // 1. Registro instantáneo con prefijo `jsierra`
        final regErr = await session.register(
          userOrEmail: 'jsierra',
          nombre: 'Jesús Sierra',
          pin: '8108',
          cuatrimestre: 2,
        );
        expect(regErr, isNull);
        expect(session.isAuthenticated, isTrue);
        expect(session.email, 'jsierra@unimagdalena.edu.co');
        expect(putCount, 1);

        final savedRemoteJson = jsonDecode(
          fakeGitHubFiles['/repos/jesusants/UM-Studio/contents/db/users/jsierra.json']!,
        ) as Map<String, dynamic>;
        expect(savedRemoteJson['username'], 'jsierra');
        expect(savedRemoteJson['programa'], 'Ingeniería Energética');

        // 2. Crear recordatorio personal en 0 ms + sincronización con GitHub
        await session.addCalendarReminder(
          titulo: 'Parcial Física Mecánica',
          subtitulo: 'Salón C-102',
          fechaIso: '2026-11-05',
          hora: '10:00',
          tipo: AcademicEventKind.parcial,
          codigoMateria: '02021810',
        );
        expect(session.reminders.length, 1);
        await syncService.flushNow(session.currentUser!);
        expect(putCount, 2);

        final afterRemJson = jsonDecode(
          fakeGitHubFiles['/repos/jesusants/UM-Studio/contents/db/users/jsierra.json']!,
        ) as Map<String, dynamic>;
        expect(
          (afterRemJson['recordatorios_calendario'] as List).single['titulo'],
          'Parcial Física Mecánica',
        );

        // 3. Nueva instancia recuerda la sesión automáticamente sin pedir login
        final syncService2 = GitHubSyncService(httpClient: mockHttp);
        final session2 = InstitutionalSessionController(
          repository: repo,
          syncService: syncService2,
        );
        await session2.load(syncRemoteOnStartup: false);
        expect(session2.isAuthenticated, isTrue);
        expect(session2.primerNombre, 'Jesús');
        expect(session2.reminders.single.titulo, 'Parcial Física Mecánica');
      },
    );
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

  group('UI End-to-End: Login Ing. Energética, ClaseViva KaTeX & Auto-Save', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    testWidgets(
      'muestra Shimmer (#1A1D24) sin spinner, renderiza KaTeX nativo desde .md y auto-guarda notas',
      (tester) async {
        tester.view.physicalSize = const Size(430, 1400);
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        final mdContent = File('assets/data/ingenieria_energetica.md')
            .readAsStringSync();
        final curriculum = MarkdownCurriculumService()
          ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

        final themeCtrl = ThemeController();
        final repo = LocalReactiveClaseVivaRepository(
          initialLatency: const Duration(milliseconds: 350),
          userId: 'alumno@unimagdalena.edu.co',
          curriculumService: curriculum,
        );

        await repo.subirArchivoAdjunto(
          temaId: '02021810',
          tipoArchivo: TipoAdjuntoEstudiante.pdf,
          nombreArchivo: 'Taller_Dinamica_U2.pdf',
          bytes: Uint8List.fromList(List<int>.filled(15360, 1)),
        );

        await tester.pumpWidget(
          CurriculumScope(
            service: curriculum,
            child: ClaseVivaRepositoryScope(
              repository: repo,
              child: ThemeScope(
                controller: themeCtrl,
                child: MaterialApp(
                  theme: AppTheme.light,
                  darkTheme: AppTheme.dark,
                  themeMode: ThemeMode.dark,
                  home: const ClaseVivaPage(temaId: '02021810'),
                ),
              ),
            ),
          ),
        );

        // 1. Shimmer inicial sin CircularProgressIndicator
        expect(find.byType(IosShimmer), findsOneWidget);
        expect(find.byType(CircularProgressIndicator), findsNothing);
        expect(find.text('Temario'), findsOneWidget);
        expect(find.text('UM STUDIO'), findsOneWidget);

        // 2. Avanza stream reactivo y muestra Física Mecánica (02021810) con sus 2 temas
        await tester.pump(const Duration(milliseconds: 400));
        await tester.pump(const Duration(milliseconds: 300));

        expect(find.text('Física Mecánica'), findsOneWidget);
        expect(find.textContaining('Tema 1:'), findsOneWidget);
        expect(find.textContaining('Tema 2:'), findsOneWidget);
        expect(find.text('OBJETIVO'), findsOneWidget);
        expect(find.text('CONCEPTO CLAVE'), findsOneWidget);
        expect(find.text('EJEMPLO DE CÁTEDRA'), findsOneWidget);
        expect(find.byType(Math), findsWidgets);
        expect(find.text('Taller_Dinamica_U2.pdf'), findsOneWidget);

        // 3. Auto-save debounce de 1 segundo en Notas Personales
        final noteField = find.byType(TextField);
        await tester.enterText(
          noteField,
          r'Deducción en clase: $a = g \sin\theta$',
        );
        await tester.pump(const Duration(milliseconds: 500));
        await tester.pump(const Duration(milliseconds: 600));

        final itemsSaved =
            await repo.watchNotasYAdjuntos(temaId: '02021810').first;
        final savedNote = itemsSaved.firstWhere(
          (e) => e.tipoArchivo == TipoAdjuntoEstudiante.nota,
        );
        expect(
          savedNote.contenidoNota,
          r'Deducción en clase: $a = g \sin\theta$',
        );
      },
    );

    testWidgets(
      'flujo de Registro rápido en LoginPage entra a HomeShell y filtra malla por Cuatrimestre',
      (tester) async {
        tester.view.physicalSize = const Size(430, 1100);
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        final mdContent = File('assets/data/ingenieria_energetica.md')
            .readAsStringSync();
        final curriculum = MarkdownCurriculumService()
          ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

        final mockHttp = MockClient(
          (_) async => http.Response(jsonEncode({'message': 'Not Found'}), 404),
        );
        final sync = GitHubSyncService(httpClient: mockHttp);
        final repo = LocalReactiveClaseVivaRepository(
          initialLatency: Duration.zero,
          curriculumService: curriculum,
        );
        final session = InstitutionalSessionController(
          repository: repo,
          syncService: sync,
          curriculumService: curriculum,
        );
        await session.load(syncRemoteOnStartup: false);

        await tester.pumpWidget(
          UmStudioApp(
            themeController: ThemeController(),
            repository: repo,
            curriculumService: curriculum,
            sessionController: session,
          ),
        );

        // Debe iniciar en LoginPage con emblema oficial y carrera bloqueada
        expect(find.byType(ProgramLogoBadge), findsOneWidget);
        expect(
          find.text('Ingeniería Energética • Unimagdalena'),
          findsOneWidget,
        );
        await tester.tap(find.text('Crear Cuenta'));
        await tester.pump(const Duration(milliseconds: 250));

        await tester.enterText(
          find.byKey(const Key('login_name_field')),
          'Camila Ospino',
        );
        await tester.enterText(
          find.byKey(const Key('login_user_field')),
          'cospino',
        );
        await tester.enterText(
          find.byKey(const Key('login_pin_field')),
          '1234',
        );
        await tester.tap(find.byKey(const Key('login_submit_button')));
        await tester.pump(const Duration(milliseconds: 350));
        await tester.pump(const Duration(milliseconds: 350));

        // Entró automáticamente a HomeShell con emblema oficial arriba a la izquierda
        expect(find.text('Hola, Camila'), findsOneWidget);
        expect(find.byType(ProgramLogoBadge), findsOneWidget);

        // Navega a la pestaña Estudio y verifica filtro por Cuatrimestre
        await tester.tap(find.text('Estudio'));
        await tester.pump(const Duration(milliseconds: 350));
        await tester.pump(const Duration(milliseconds: 350));

        expect(find.text('Estudio Extraclase'), findsOneWidget);
        expect(find.text('Física Mecánica'), findsOneWidget);

        await tester.ensureVisible(find.text('Cuatrimestre 1'));
        await tester.pump();
        await tester.tap(find.text('Cuatrimestre 1'));
        await tester.pump(const Duration(milliseconds: 250));
        expect(find.text('Cálculo Diferencial'), findsOneWidget);
      },
    );
  });
}
