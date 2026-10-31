import 'dart:async';
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
import 'package:um_studio/core/utils/user_payload_cipher.dart';
import 'package:um_studio/data/models/student_user_model.dart';
import 'package:um_studio/data/services/download_queue_service.dart';
import 'package:um_studio/presentation/widgets/header_morph_avatar.dart';
import 'package:um_studio/presentation/widgets/minimal_slide_viewer.dart';

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

  group('Base de Datos .MD v3.0 (51 Técnicas >=8 temas + 5 Inglés >=15 temas + KaTeX)', () {
    test(
      'valida las 56 asignaturas, 80 temas duales de Inglés y 100% de fórmulas KaTeX sin errores',
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

        var techSubjects = 0;
        var englishSubjects = 0;
        var totalEnglishTopics = 0;
        var totalKatexFormulas = 0;
        final failedFormulas = <String>[];

        for (final asig in db.allAsignaturas) {
          if (asig.esIngles) {
            englishSubjects++;
            expect(
              asig.temas.length,
              greaterThanOrEqualTo(15),
              reason: '${asig.nombre} debe tener al menos 15 temas.',
            );
            expect(asig.temasInglesGeneral.length, greaterThanOrEqualTo(10));
            expect(
              asig.temasNotacionIngenieria.length,
              greaterThanOrEqualTo(5),
            );
            totalEnglishTopics += asig.temas.length;

            for (final gen in asig.temasInglesGeneral) {
              expect(gen.conceptoClaveLatex.trim(), isEmpty);
              expect(gen.slides.length, greaterThanOrEqualTo(5));
            }
            for (final not in asig.temasNotacionIngenieria) {
              expect(not.conceptoClaveLatex.trim(), isNotEmpty);
              expect(not.verbalizacionIngles.trim(), isNotEmpty);
            }
          } else {
            techSubjects++;
            expect(
              asig.temas.length,
              inInclusiveRange(8, 12),
              reason:
                  '${asig.codigo} (${asig.nombre}) debe tener entre 8 y 12 temas completos.',
            );
            final cortes = asig.temas.map((t) => t.corte).toSet();
            expect(
              cortes,
              containsAll(<int>[1, 2, 3]),
              reason: '${asig.nombre} debe cubrir los 3 cortes académicos.',
            );
          }

          for (final tema in asig.temas) {
            if (tema.esInglesGeneral) continue;
            totalKatexFormulas++;
            final clean = InstitutionalValidator.sanitizeLatex(
              tema.conceptoClaveLatex,
            );
            expect(
              clean,
              isNotEmpty,
              reason: 'Fórmula vacía en ${asig.codigo} T${tema.numeroTema}',
            );
            final mathWidget = Math.tex(clean);
            if (mathWidget.parseError != null) {
              failedFormulas.add(
                '${asig.codigo} (${asig.nombre}) T${tema.numeroTema}: ${mathWidget.parseError}\n  LaTeX: $clean',
              );
            }
          }
        }

        expect(techSubjects, 51);
        expect(englishSubjects, 5);
        expect(totalEnglishTopics, greaterThanOrEqualTo(75));
        expect(totalKatexFormulas, greaterThanOrEqualTo(440));
        expect(
          failedFormulas,
          isEmpty,
          reason:
              'Fórmulas con error en flutter_math_fork:\n${failedFormulas.join('\n')}',
        );
      },
    );
  });

  group('DownloadQueueService (Máx. 20 simultáneas FIFO + PDF vectorial < 1.2 MB)', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test('compila PDF vectorial < 1.2 MB, encola sobre 20 slots y sirve caché en 0 ms', () async {
      final mdContent = File('assets/data/ingenieria_energetica.md')
          .readAsStringSync();
      final db = CurriculumMarkdownParser.parse(mdContent);
      final eng1 = db.findAsignatura('01021802')!;
      final topic1 = eng1.temasInglesGeneral.first;

      // 1. Compilación real de PDF vectorial con Deflate
      final pdfBytes = await SlideDeckPdfCompiler.compile(
        codigoAsignatura: eng1.codigo,
        nombreAsignatura: eng1.nombre,
        numeroTema: topic1.numeroTema,
        tituloTema: topic1.titulo,
        slides: topic1.slides,
      );
      expect(pdfBytes.lengthInBytes, greaterThan(1024));
      expect(
        pdfBytes.lengthInBytes,
        lessThanOrEqualTo(DownloadQueueService.maxPdfSizeBytes),
      );

      // 2. Control estricto de 20 descargas simultáneas + cola FIFO (#1, #2, #3)
      final queue = DownloadQueueService(maxConcurrent: 20);
      final blockers = List<Completer<Uint8List>>.generate(
        23,
        (_) => Completer<Uint8List>(),
      );
      final futures = <Future<Uint8List>>[];

      for (var i = 0; i < 23; i++) {
        futures.add(
          queue.enqueueDownload(
            taskId: 'batch_$i',
            fileName: 'slide_$i.pdf',
            saveToPlatform: false,
            generator: () => blockers[i].future,
          ),
        );
      }

      // Permite que las tareas 0..19 entren en _executeTask
      await Future<void>.delayed(Duration.zero);
      expect(queue.activeDownloads, 20);
      expect(queue.queuedCount, 3);
      expect(queue.stateFor('batch_20').buttonLabel, '⏳ En cola (#1)...');
      expect(queue.stateFor('batch_21').buttonLabel, '⏳ En cola (#2)...');
      expect(queue.stateFor('batch_22').buttonLabel, '⏳ En cola (#3)...');

      for (final c in blockers) {
        c.complete(pdfBytes);
      }
      await Future.wait(futures);
      expect(queue.activeDownloads, 0);
      expect(queue.queuedCount, 0);
      expect(queue.stateFor('batch_22').buttonLabel, '✓ PDF Guardado');

      // 3. Entrega en 0 ms desde caché de sesión sin volver a invocar generator
      var generatorCalls = 0;
      final cachedHit = await queue.enqueueDownload(
        taskId: 'batch_0',
        fileName: 'slide_0.pdf',
        saveToPlatform: false,
        generator: () async {
          generatorCalls++;
          return pdfBytes;
        },
      );
      expect(generatorCalls, 0);
      expect(cachedHit.lengthInBytes, pdfBytes.lengthInBytes);

      // 4. Bloqueo estricto si un archivo supera 1.2 MB (1,258,291 bytes)
      await expectLater(
        queue.enqueueDownload(
          taskId: 'oversized_test',
          fileName: 'oversized.pdf',
          saveToPlatform: false,
          generator: () async => Uint8List(1300000),
        ),
        throwsA(isA<PdfSizeLimitExceededException>()),
      );
    });
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
        'corte': 2,
        'objetivo': 'Segunda ley de Newton.',
        'concepto_clave_latex': r'\sum \vec{F} = m \cdot \vec{a}',
        'ejemplo': 'Bloque con fricción.',
      });
      expect(tema.badgeTema, 'Tema 2');
      expect(tema.corte, 2);

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
      expect(pdfKb.pesoFormateado, '420 KB');
    });
  });

  group('UI End-to-End: ClaseViva KaTeX, Visor Dual de Inglés & Clases', () {
    setUp(() {
      SharedPreferences.setMockInitialValues({});
      DownloadQueueService.instance.clearSessionCache();
    });

    testWidgets(
      'General English I muestra Segmented Switcher, MinimalSlideViewer sin KaTeX y cambia a Notación de Ingeniería con KaTeX + Pronunciación',
      (tester) async {
        tester.view.physicalSize = const Size(430, 1400);
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        final mdContent = File('assets/data/ingenieria_energetica.md')
            .readAsStringSync();
        final curriculum = MarkdownCurriculumService()
          ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

        final repo = LocalReactiveClaseVivaRepository(
          initialLatency: Duration.zero,
          userId: 'alumno@unimagdalena.edu.co',
          curriculumService: curriculum,
        );

        await tester.pumpWidget(
          CurriculumScope(
            service: curriculum,
            child: ClaseVivaRepositoryScope(
              repository: repo,
              child: ThemeScope(
                controller: ThemeController(),
                child: MaterialApp(
                  theme: AppTheme.light,
                  darkTheme: AppTheme.dark,
                  themeMode: ThemeMode.dark,
                  home: const ClaseVivaPage(temaId: '01021802'),
                ),
              ),
            ),
          ),
        );

        await tester.pump(const Duration(milliseconds: 250));

        // 1. En rama "Inglés General (Slides)": muestra MinimalSlideViewer y oculta KaTeX
        expect(find.text('General English I'), findsOneWidget);
        expect(find.text('Inglés General (Slides)'), findsOneWidget);
        expect(find.text('Notación de Ingeniería (KaTeX)'), findsOneWidget);
        expect(find.byType(MinimalSlideViewer), findsOneWidget);
        expect(find.text('CONCEPTO CLAVE (KATEX)'), findsNothing);
        expect(find.text('1 / 6'), findsOneWidget);

        // 2. Navega a la diapositiva 2 con el botón circular →
        await tester.ensureVisible(find.byKey(const Key('slide_next_button')));
        await tester.tap(find.byKey(const Key('slide_next_button')));
        await tester.pump();
        await tester.pump(const Duration(milliseconds: 300));
        expect(find.text('2 / 6'), findsOneWidget);

        // 3. Exporta PDF (<1.2 MB) con el botón ↓ PDF
        // (La compilación/descarga PDF <1.2 MB se valida en el test de DownloadQueueService)
        expect(
          find.byKey(const Key('slide_download_pdf_button')),
          findsOneWidget,
        );

        // 4. Cambia a la pestaña "Notación de Ingeniería (KaTeX)"
        await tester.drag(find.byType(ListView).first, const Offset(0, 400));
        await tester.pump(const Duration(milliseconds: 300));
        await tester.tap(find.text('Notación de Ingeniería (KaTeX)'));
        for (var i = 0; i < 20; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        expect(find.byType(MinimalSlideViewer), findsNothing);
        expect(
          find.text('CONCEPTO CLAVE (KATEX)', skipOffstage: false),
          findsOneWidget,
        );
        expect(
          find.text('PRONUNCIACIÓN Y LECTURA EN INGLÉS', skipOffstage: false),
          findsOneWidget,
        );
        expect(find.byType(Math, skipOffstage: false), findsWidgets);

        await tester.pump(const Duration(seconds: 4));
      },
    );

    testWidgets(
      'flujo de Registro rápido entra a HomeShell sin Uso Diario, explora Clases -> Temario y sincroniza (Último revisado) con GitHub',
      (tester) async {
        tester.view.physicalSize = const Size(430, 1200);
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        final mdContent = File('assets/data/ingenieria_energetica.md')
            .readAsStringSync();
        final curriculum = MarkdownCurriculumService()
          ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

        final fakeGitHubFiles = <String, String>{};
        final mockHttp = MockClient((http.Request req) async {
          final path = req.url.path;
          if (req.method == 'GET') {
            if (fakeGitHubFiles.containsKey(path)) {
              final rawJson = fakeGitHubFiles[path]!;
              final b64 = base64Encode(utf8.encode(rawJson));
              return http.Response(
                jsonEncode({'sha': 'sha_cospino', 'content': '$b64\n'}),
                200,
              );
            }
            return http.Response(jsonEncode({'message': 'Not Found'}), 404);
          }
          if (req.method == 'PUT') {
            final body = jsonDecode(req.body) as Map<String, dynamic>;
            fakeGitHubFiles[path] = utf8.decode(
              base64Decode(body['content'].toString()),
            );
            return http.Response(
              jsonEncode({
                'content': {'sha': 'sha_cospino_v2'},
              }),
              201,
            );
          }
          return http.Response('Unsupported', 500);
        });

        final sync = GitHubSyncService(httpClient: mockHttp);
        await sync.setCustomGitHubToken('test_token_local_mock');
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

        final legacyToggle = find.text('Opciones de acceso con PIN / Local');
        if (legacyToggle.evaluate().isNotEmpty) {
          await tester.tap(legacyToggle);
          await tester.pumpAndSettle();
        }

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

        expect(find.text('Hola, Camila'), findsOneWidget);
        expect(find.text('Clases'), findsOneWidget);

        await tester.tap(find.text('Clases'));
        await tester.pump(const Duration(milliseconds: 350));
        await tester.pump(const Duration(milliseconds: 350));

        await tester.tap(find.text('Cálculo Diferencial'));
        await tester.pump(const Duration(milliseconds: 200));
        await tester.pump(const Duration(milliseconds: 350));

        expect(find.text('TEMARIO'), findsOneWidget);
        expect(find.text('Tema 2'), findsOneWidget);

        await tester.tap(find.text('Tema 2'));
        await tester.pump(const Duration(milliseconds: 200));
        await tester.pump(const Duration(milliseconds: 350));

        expect(session.lastReviewedTopicFor('02011807'), 2);

        await tester.tap(find.text('Temario'));
        await tester.pump(const Duration(milliseconds: 200));
        await tester.pump(const Duration(milliseconds: 350));

        expect(find.text('(Último revisado)'), findsOneWidget);

        // Drena el debounce (1.2s) de sincronización con GitHub y verifica el PUT remoto
        await tester.pump(const Duration(seconds: 2));
        expect(
          fakeGitHubFiles.keys.any((k) => k.endsWith('/db/users/cospino.json')),
          isTrue,
        );
      },
    );
  });

  group('Blindaje de Seguridad, Cifrado de Datos & Normalización de Usuarios', () {
    test('UserPayloadCipher cifra y descifra estructuras JSON simétricamente con HMAC', () {
      const username = 'jasierra';
      const pin = '8108';
      final testData = {
        '02021810': 75,
        '03041819': 90,
      };

      final encrypted = UserPayloadCipher.encryptJson(
        testData,
        username: username,
        pinOrHash: pin,
      );
      expect(encrypted.startsWith(UserPayloadCipher.prefix), isTrue);

      final decrypted = UserPayloadCipher.decryptJson(
        encrypted,
        username: username,
        pinOrHash: pin,
      );
      expect(decrypted, equals(testData));

      // Descifrado con PIN incorrecto debe fallar (retorna null)
      final failed = UserPayloadCipher.decryptJson(
        encrypted,
        username: username,
        pinOrHash: 'wrong_pin',
      );
      expect(failed, isNull);

      // Retrocompatibilidad con Maps o Lists legados
      expect(
        UserPayloadCipher.decryptJson(
          testData,
          username: username,
          pinOrHash: pin,
        ),
        equals(testData),
      );
    });

    test('StudentUserModel serializa progreso cifrado para GitHub y descifra transparentemente', () {
      final user = StudentUserModel.createNew(
        username: 'jasierra',
        nombre: 'Jesus Sierra',
        email: 'jasierra@unimagdalena.edu.co',
        pinHash: InstitutionalValidator.hashPin('8108'),
        cuatrimestreActual: 3,
      );

      final encryptedJson = user.toEncryptedJson(pinOrHash: '8108');
      expect(
        encryptedJson['progreso_materias'].toString().startsWith(UserPayloadCipher.prefix),
        isTrue,
      );
      expect(
        encryptedJson['recordatorios_calendario'].toString().startsWith(UserPayloadCipher.prefix),
        isTrue,
      );

      // Deserialización automática con PIN
      final restored = StudentUserModel.fromJson(encryptedJson, pinOrHash: '8108');
      expect(restored.username, 'jasierra');
      expect(restored.progresoMaterias.isNotEmpty, isTrue);
    });

    test('InstitutionalValidator normaliza identificadores y elimina caracteres especiales', () {
      final res1 = InstitutionalValidator.parseInstitutionalUser('JaSierra@UniMagdalena.edu.co');
      expect(res1.identity?.username, 'jasierra');
      expect(res1.identity?.email, 'jasierra@unimagdalena.edu.co');

      final res2 = InstitutionalValidator.parseInstitutionalUser('  jasierras#%  ');
      expect(res2.identity?.username, 'jasierras');
    });
  });

  group('HeaderMorphAvatar: Alternancia Dinámica y Anti-Tilde', () {
    testWidgets('muestra emblema institucional y rota a foto de usuario tras 5 segundos', (tester) async {
      final mockBytes = Uint8List.fromList([
        0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
        0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
        0x08, 0x06, 0x00, 0x00, 0x00, 0x1F, 0x15, 0xC4,
        0x89, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
        0x54, 0x78, 0x9C, 0x63, 0x00, 0x01, 0x00, 0x00,
        0x05, 0x00, 0x01, 0x0D, 0x0A, 0x2D, 0xB4, 0x00,
        0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
        0x42, 0x60, 0x82,
      ]);

      await tester.pumpWidget(
        ThemeScope(
          controller: ThemeController(),
          child: MaterialApp(
            theme: AppTheme.dark,
            home: Scaffold(
              body: HeaderMorphAvatar(
                size: 38,
                photoBytes: mockBytes,
              ),
            ),
          ),
        ),
      );
      await tester.pump();

      expect(find.byKey(const ValueKey('career_logo')), findsOneWidget);
      expect(find.byKey(const ValueKey('user_photo')), findsNothing);

      await tester.pump(const Duration(seconds: 5));
      await tester.pump(const Duration(milliseconds: 300));
      expect(find.byKey(const ValueKey('user_photo')), findsOneWidget);

      await tester.tap(find.byType(HeaderMorphAvatar));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 300));
      expect(find.byKey(const ValueKey('career_logo')), findsOneWidget);

      await tester.pump(const Duration(seconds: 5));
      await tester.pump(const Duration(milliseconds: 300));
      expect(find.byKey(const ValueKey('user_photo')), findsOneWidget);
    });

    testWidgets('sin foto permanece estático en career_logo sin timers activos', (tester) async {
      await tester.pumpWidget(
        ThemeScope(
          controller: ThemeController(),
          child: MaterialApp(
            theme: AppTheme.dark,
            home: const Scaffold(
              body: HeaderMorphAvatar(
                size: 38,
                photoBytes: null,
              ),
            ),
          ),
        ),
      );
      await tester.pump();

      expect(find.byKey(const ValueKey('career_logo')), findsOneWidget);
      await tester.pump(const Duration(seconds: 10));
      expect(find.byKey(const ValueKey('career_logo')), findsOneWidget);
      expect(find.byKey(const ValueKey('user_photo')), findsNothing);
    });
  });

  group('Layout & Scroll Overflow: 5 Niveles de Inglés en Pantallas Compactas', () {
    const englishCodes = ['01021802', '01021803', '01021804', '01021805', '01021806'];

    testWidgets('renderiza diapositivas con tablas multicomparativas en 360x640 y 320x568 sin overflow', (tester) async {
      final mdContent = File('assets/data/ingenieria_energetica.md').readAsStringSync();
      final database = CurriculumMarkdownParser.parse(mdContent);

      for (final code in englishCodes) {
        final asig = database.findAsignatura(code);
        expect(asig, isNotNull);
        final generalTopics = asig!.temasPorModalidad('general');
        expect(generalTopics.isNotEmpty, isTrue);

        final sampleTopic = generalTopics.first;
        final slideItems = sampleTopic.slides;

        for (final size in const [Size(360, 640), Size(320, 568)]) {
          tester.view.physicalSize = size;
          tester.view.devicePixelRatio = 1.0;

          await tester.pumpWidget(
            ThemeScope(
              controller: ThemeController(),
              child: MaterialApp(
                theme: AppTheme.dark,
                home: Scaffold(
                  body: MinimalSlideViewer(
                    temaId: '\${code}_\${sampleTopic.numeroTema}',
                    codigoAsignatura: code,
                    nombreAsignatura: asig.nombre,
                    numeroTema: sampleTopic.numeroTema,
                    tituloTema: sampleTopic.titulo,
                    slides: slideItems,
                  ),
                ),
              ),
            ),
          );
          await tester.pump(const Duration(milliseconds: 300));

          expect(find.byType(MinimalSlideViewer), findsOneWidget);
          expect(tester.takeException(), isNull);

          if (slideItems.length > 1) {
            final nextBtn = find.byKey(const Key('slide_next_button'));
            if (nextBtn.evaluate().isNotEmpty) {
              await tester.tap(nextBtn);
              await tester.pump(const Duration(milliseconds: 300));
              expect(tester.takeException(), isNull);
            }
          }
        }
      }
      tester.view.reset();
    });

    testWidgets('ClaseVivaPage en los 5 niveles de inglés hace scroll completo sin desbordamiento ni errores de stream', (tester) async {
      final mdContent = File('assets/data/ingenieria_energetica.md').readAsStringSync();
      final curriculum = MarkdownCurriculumService()
        ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

      final repo = LocalReactiveClaseVivaRepository(
        initialLatency: Duration.zero,
        userId: 'alumno@unimagdalena.edu.co',
        curriculumService: curriculum,
      );

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
        for (var i = 0; i < 4; i++) {
          await tester.pump(const Duration(milliseconds: 100));
        }

        final listFinder = find.byType(ListView).first;
        for (var i = 0; i < 4; i++) {
          await tester.drag(listFinder, const Offset(0, -500));
          await tester.pump(const Duration(milliseconds: 100));
        }

        expect(tester.takeException(), isNull);
        expect(find.text('MIS APUNTES Y ARCHIVOS', skipOffstage: false), findsOneWidget);
      }
    });
  });
}
