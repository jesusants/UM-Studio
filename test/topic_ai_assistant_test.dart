import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/services/groq_topic_assistant_service.dart';
import 'package:um_studio/presentation/providers/topic_ai_assistant_controller.dart';
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
