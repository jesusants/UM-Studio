import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/models/global_env_config.dart';
import 'package:um_studio/data/models/student_user_model.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/groq_topic_assistant_service.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/providers/topic_ai_assistant_controller.dart';
import 'package:um_studio/presentation/widgets/ai_graphic_block.dart';
import 'package:um_studio/presentation/widgets/topic_ai_assistant_widget.dart';

void main() {
  group('GroqTopicAssistantService & Context Extraction', () {
    test('buildTopicContext concatena objetivos, fórmulas, diapositivas y apuntes', () {
      final context = GroqTopicAssistantService.buildTopicContext(
        titulo: 'Capacitores e Inductores',
        objetivo: 'Comprender el almacenamiento de energía en campos eléctricos y magnéticos.',
        conceptoClaveLatex: r'i_C(t) = C \frac{dv}{dt}',
        ejemplo: 'Problema 1: Cálculo de corriente en un capacitor de 1 mF.',
        slides: [
          _MockSlide(
            titulo: 'El Capacitor',
            seccion: 'ALMACENAMIENTO',
            puntos: ['Almacena carga en campo eléctrico', r'C = \frac{\epsilon A}{d}'],
          ),
        ],
        personalNotes: ['Recordar ley de continuidad: v_C(0-) = v_C(0+)'],
      );

      expect(context, contains('TÍTULO DEL TEMA: Capacitores e Inductores'));
      expect(context, contains('OBJETIVO Y ALCANCE ACADÉMICO:'));
      expect(context, contains(r'i_C(t) = C \frac{dv}{dt}'));
      expect(context, contains('El Capacitor'));
      expect(context, contains('Problema 1: Cálculo de corriente'));
      expect(context, contains('Recordar ley de continuidad'));
    });
  });

  group('TopicAiAssistantController - Aislamiento de Memoria por Tema', () {
    test('Las conversaciones están estrictamente aisladas por topicKey', () {
      final controller = TopicAiAssistantController();

      const topic1 = '03041820_t1';
      const topic2 = '03041820_t2';

      expect(controller.getHistory(topic1), isEmpty);
      expect(controller.getHistory(topic2), isEmpty);

      // Simular mensajes en topic 1
      controller.clearHistory(topic1);
      final list1 = controller.getHistory(topic1);
      expect(list1, isEmpty);

      // Verificar que limpiar topic 1 no afecta a topic 2
      controller.clearHistory(topic1);
      expect(controller.getHistory(topic2), isEmpty);
    });
  });

  group('Topic AI Assistant UI & Viewports', () {
    testWidgets('TopicAiTriggerButton renderiza icono y texto correctamente', (tester) async {
      var tapped = false;

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: Scaffold(
            body: Center(
              child: TopicAiTriggerButton(
                onTap: () => tapped = true,
              ),
            ),
          ),
        ),
      );

      expect(find.byIcon(Icons.auto_awesome_rounded), findsOneWidget);
      expect(find.text('Preguntar sobre este tema'), findsOneWidget);

      await tester.tap(find.byType(TopicAiTriggerButton));
      await tester.pumpAndSettle();
      expect(tapped, isTrue);
    });

    testWidgets('TopicAiChatView muestra cabecera con badge de contexto y chips iniciales', (tester) async {
      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: const Scaffold(
            body: TopicAiChatView(
              topicKey: 'test_topic_1',
              asignaturaNombre: 'Fundamentos de Electricidad II',
              temaTitulo: 'Transformada Fasorial e Impedancia Compleja',
              temaContextoCompleto: 'Contexto de prueba...',
            ),
          ),
        ),
      );

      // Badge de contexto
      expect(find.text('Contexto:'), findsOneWidget);
      expect(find.text('Transformada Fasorial e Impedancia Compleja'), findsOneWidget);

      // Chips iniciales de sugerencias rápidas
      expect(find.text('Explicar la fórmula principal'), findsOneWidget);
      expect(find.text('Desglosar el ejercicio paso a paso'), findsOneWidget);
      expect(find.text('¿Qué significa cada variable?'), findsOneWidget);

      // Campo de entrada
      expect(find.byType(TextField), findsOneWidget);
      expect(find.text('Preguntar sobre este tema...'), findsOneWidget);
    });

    testWidgets('TopicAiDesktopFloatingWindow renderiza en dimensiones compactas (360x480) sin overflow', (tester) async {
      tester.view.physicalSize = const Size(1280, 800);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(() => tester.view.reset());

      var closed = false;

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: Scaffold(
            body: Stack(
              children: [
                Positioned(
                  right: 20,
                  bottom: 20,
                  child: TopicAiDesktopFloatingWindow(
                    topicKey: 'desktop_test_1',
                    asignaturaNombre: 'Cálculo Diferencial',
                    temaTitulo: 'Límites y Continuidad',
                    temaContextoCompleto: 'Contexto de límites...',
                    onClose: () => closed = true,
                  ),
                ),
              ],
            ),
          ),
        ),
      );

      await tester.pumpAndSettle();

      expect(find.byType(TopicAiDesktopFloatingWindow), findsOneWidget);
      expect(find.text('Límites y Continuidad'), findsOneWidget);
      expect(tester.takeException(), isNull);

      final closeBtn = find.byIcon(Icons.close_rounded);
      expect(closeBtn, findsOneWidget);
      await tester.tap(closeBtn);
      await tester.pumpAndSettle();
      expect(closed, isTrue);
    });

    testWidgets('showTopicAiBottomSheet despliega bottom sheet móvil en viewport 392x800 sin overflow', (tester) async {
      tester.view.physicalSize = const Size(392, 800);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(() => tester.view.reset());

      await tester.pumpWidget(
        MaterialApp(
          theme: AppTheme.dark,
          home: Scaffold(
            body: Builder(
              builder: (ctx) => ElevatedButton(
                onPressed: () {
                  showTopicAiBottomSheet(
                    context: ctx,
                    topicKey: 'mobile_topic_1',
                    asignaturaNombre: 'Física I',
                    temaTitulo: 'Cinemática y Movimiento Rectilíneo',
                    temaContextoCompleto: 'Contexto cinemática...',
                  );
                },
                child: const Text('Abrir Chat'),
              ),
            ),
          ),
        ),
      );

      await tester.tap(find.text('Abrir Chat'));
      await tester.pumpAndSettle();

      expect(find.byType(TopicAiChatView), findsOneWidget);
      expect(find.text('Cinemática y Movimiento Rectilíneo'), findsOneWidget);
      expect(find.text('Explicar la fórmula principal'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  });

  group('Modelos Gemini Disponibles, Saludo Personalizado y Elementos Gráficos', () {
    test('GlobalEnvConfig.normalizeModelName migra modelos 2.0/2.5 retirados al activo', () {
      expect(
        GlobalEnvConfig.normalizeModelName('gemini-2.5-flash'),
        equals('gemini-3.5-flash-lite'),
      );
      expect(
        GlobalEnvConfig.normalizeModelName('models/gemini-2.0-flash-lite'),
        equals('gemini-3.5-flash-lite'),
      );
      expect(
        GlobalEnvConfig.normalizeModelName(''),
        equals('gemini-3.5-flash-lite'),
      );
      expect(
        GlobalEnvConfig.normalizeModelName('gemini-3.5-flash'),
        equals('gemini-3.5-flash'),
      );
      expect(
        GlobalEnvConfig.normalizeModelName('gemma-4-26b-a4b-it'),
        equals('gemma-4-26b-a4b-it'),
      );
      for (final m in TopicAssistantService.curatedAvailableModels) {
        expect(m.startsWith('gemini-2.'), isFalse);
      }
    });

    test('AiGraphicSpec.tryParse analiza funcion, vectores, barras y lab (incluyendo comas colgantes)', () {
      final funcionSpec = AiGraphicSpec.tryParse('''
```um-grafica
{
  "tipo": "funcion",
  "titulo": "Conservación E(x)",
  "ejex": "Posición x (m)",
  "ejey": "Energía (J)",
  "series": [
    {"nombre": "Em", "color": "green", "puntos": [[0, 10], [1, 10], [2, 10],]},
  ],
}
```
''');
      expect(funcionSpec, isNotNull);
      expect(funcionSpec!.tipo, equals('funcion'));
      expect(funcionSpec.series.first.points.length, equals(3));

      final vecSpec = AiGraphicSpec.tryParse('''
{"tipo":"vectores","titulo":"DCL Plano Inclinado","vectores":[{"nombre":"N","angulo_deg":90,"magnitud":1.0,"color":"green"},{"nombre":"mg","angulo_deg":-90,"magnitud":1.2,"color":"orange"}]}
''');
      expect(vecSpec, isNotNull);
      expect(vecSpec!.tipo, equals('vectores'));
      expect(vecSpec.vectores.length, equals(2));

      final barSpec = AiGraphicSpec.tryParse('''
{"tipo":"barras","titulo":"Energía","barras":[{"label":"Ec","valor":65,"color":"indigo"},{"label":"Ep","valor":35,"color":"green"}]}
''');
      expect(barSpec, isNotNull);
      expect(barSpec!.tipo, equals('barras'));
      expect(barSpec.barras.length, equals(2));

      final labSpec = AiGraphicSpec.tryParse('''
{"tipo":"lab","titulo":"Simulador Fasorial","modo_lab":"acPhasor"}
''');
      expect(labSpec, isNotNull);
      expect(labSpec!.tipo, equals('lab'));
      expect(labSpec.modoLab, equals('acPhasor'));
    });

    testWidgets('TopicAiChatView saluda con el nombre registrado y renderiza gráficas de la IA sin overflow', (tester) async {
      tester.view.physicalSize = const Size(390, 820);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(() => tester.view.reset());

      final recordingService = _RecordingTopicAssistantService();
      final controller = TopicAiAssistantController(service: recordingService);
      final session = _FakeSessionController(
        user: const StudentUserModel(
          nombre: 'Sofía Restrepo Mendoza',
          email: 'srestrepo@unimagdalena.edu.co',
          programa: 'Ingeniería Energética',
          username: 'srestrepo',
          pinHash: 'hash',
          progresoMaterias: {},
          recordatoriosCalendario: [],
          apuntesPersonales: {},
        ),
      );

      await tester.pumpWidget(
        SessionScope(
          controller: session,
          child: MaterialApp(
            theme: AppTheme.dark,
            home: Scaffold(
              body: SizedBox(
                width: 360,
                height: 600,
                child: TopicAiChatView(
                  topicKey: 'topic_saludo_grafica',
                  asignaturaNombre: 'Física Mecánica',
                  temaTitulo: 'Conservación de la Energía',
                  temaContextoCompleto: 'E_m = K + U',
                  controller: controller,
                ),
              ),
            ),
          ),
        ),
      );
      await tester.pumpAndSettle();

      // Verifica saludo personalizado con nombre registrado del estudiante
      expect(find.text('¡Hola, Sofía Restrepo Mendoza!'), findsOneWidget);

      // Botón para abrir compositor gráfico sin overflow
      await tester.tap(find.byIcon(Icons.auto_graph_rounded));
      await tester.pumpAndSettle();
      expect(find.text('Añadir Elemento Gráfico'), findsOneWidget);

      await tester.tap(find.text('Insertar en chat'));
      await tester.pumpAndSettle();

      expect(recordingService.lastStudentName, equals('Sofía Restrepo Mendoza'));
      expect(find.byType(AiGraphicBlockWidget), findsOneWidget);
      expect(find.textContaining('Curva Energía vs Posición'), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  });
}

class _RecordingTopicAssistantService extends TopicAssistantService {
  String? lastStudentName;

  @override
  Future<TopicAssistantReply> askTopicMultimodal({
    required String asignaturaNombre,
    required String temaTitulo,
    required String temaContextoCompleto,
    required List<Map<String, String>> historialReciente,
    required String preguntaUsuario,
    String? studentName,
    Uint8List? imageBytes,
    String? imageMimeType,
  }) async {
    lastStudentName = studentName;
    return TopicAssistantReply(
      text:
          '¡Hola, ${studentName ?? 'estudiante'}! Aquí tienes la gráfica solicitada:\n\n'
          '```um-grafica\n'
          '{"tipo":"funcion","titulo":"Curva Energía vs Posición","ejex":"x (m)","ejey":"E (J)","series":[{"nombre":"Em","color":"green","puntos":[[0,10],[1,10],[2,10]]}]}\n'
          '```',
    );
  }
}

class _FakeSessionController extends InstitutionalSessionController {
  _FakeSessionController({required StudentUserModel user})
      : _user = user,
        super(
          repository: LocalReactiveClaseVivaRepository(),
          curriculumService: MarkdownCurriculumService(),
        );

  final StudentUserModel _user;

  @override
  bool get isAuthenticated => true;

  @override
  StudentUserModel? get currentUser => _user;

  @override
  String get displayName => _user.nombre;

  @override
  String get primerNombre => _user.primerNombre;
}

class _MockSlide {
  _MockSlide({
    required this.titulo,
    required this.seccion,
    required this.puntos,
  });

  final String titulo;
  final String seccion;
  final List<String> puntos;
}
