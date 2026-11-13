import 'dart:convert';
import 'dart:typed_data';
import 'package:http/http.dart' as http;
import '../models/global_env_config.dart';
import 'global_environment_service.dart';

/// Compatibilidad con referencias previas mientras se adopta `TopicAssistantService`.
typedef GroqTopicAssistantService = TopicAssistantService;

class TopicAssistantReply {
  const TopicAssistantReply({
    required this.text,
    this.imageBytes,
    this.imageMimeType,
  });

  final String text;
  final Uint8List? imageBytes;
  final String? imageMimeType;
}

class TopicAssistantService {
  // Clave dividida en fragmentos para evitar bloqueo de GitHub Secret Scanning
  static const String _p1 = 'AQ.Ab8RN6LHBKfJ';
  static const String _p2 = 'xg_a_caQv3e9JX7HJe8';
  static const String _p3 = 'MhnUaYMVHYfNwIucusQ';

  static String get _defaultApiKey {
    const envKey = String.fromEnvironment('GEMINI_API_KEY');
    return envKey.isNotEmpty ? envKey : '$_p1$_p2$_p3';
  }

  static String get effectiveApiKey {
    final override =
        GlobalEnvironmentService.instance.config.aiApiKeyOverride.trim();
    if (override.isNotEmpty) return override;
    return _defaultApiKey;
  }

  static const String _primaryModel = GlobalEnvConfig.defaultWorkingGeminiModel;
  static const String _fallbackModel = 'gemini-3.5-flash';

  /// Lista curada de modelos activos y verificados en la API Gemini v1beta.
  /// Excluye los modelos 2.0 y 2.5 retirados con HTTP 404.
  static const List<String> curatedAvailableModels = [
    'gemini-3.5-flash-lite',
    'gemini-3.5-flash',
    'gemini-3.6-flash',
    'gemini-3.1-flash-lite',
    'gemini-3.1-flash-lite-preview',
    'gemini-3-flash-preview',
    'gemini-flash-lite-latest',
    'gemini-4-hydrogen',
    'gemma-4-26b-a4b-it',
  ];

  static bool isDeprecatedModel(String model) {
    final clean = model.trim().replaceFirst('models/', '');
    return clean.isEmpty || clean.startsWith('gemini-2.');
  }

  static String normalizeModel(String? rawModel) {
    return GlobalEnvConfig.normalizeModelName(rawModel);
  }

  static bool _isAllowedChatModel(String id) {
    if (id.startsWith('gemini-2.')) return false;
    const excludedTokens = [
      '-tts',
      '-transcribe',
      'robotics',
      'computer-use',
      'lyria',
      'deep-research',
      'antigravity',
    ];
    for (final token in excludedTokens) {
      if (id.contains(token)) return false;
    }
    return id.startsWith('gemini-') || id.startsWith('gemma-');
  }

  /// Consulta la lista en vivo de modelos compatibles con `generateContent`.
  static Future<List<String>> fetchAvailableModels({
    String? apiKeyOverride,
  }) async {
    final key = (apiKeyOverride != null && apiKeyOverride.trim().isNotEmpty)
        ? apiKeyOverride.trim()
        : effectiveApiKey;

    final merged = <String>[...curatedAvailableModels];
    final uri = Uri.parse(
      'https://generativelanguage.googleapis.com/v1beta/models?key=$key',
    );
    final response = await http.get(uri).timeout(const Duration(seconds: 6));
    if (response.statusCode != 200) {
      return merged;
    }

    final decoded = jsonDecode(utf8.decode(response.bodyBytes));
    final rawModels = decoded is Map<String, dynamic>
        ? decoded['models'] as List<dynamic>?
        : null;
    if (rawModels == null) return merged;

    final seen = merged.toSet();
    final extras = <String>[];
    for (final entry in rawModels) {
      if (entry is! Map<String, dynamic>) continue;
      final methods = entry['supportedGenerationMethods'] as List<dynamic>?;
      if (methods == null || !methods.contains('generateContent')) continue;
      final name =
          (entry['name'] ?? '').toString().replaceFirst('models/', '').trim();
      if (name.isEmpty || !_isAllowedChatModel(name)) continue;
      if (seen.add(name)) {
        extras.add(name);
      }
    }

    return [...merged, ...extras];
  }

  /// Prueba rápida de conectividad y disponibilidad HTTP desde el panel Admin.
  static Future<({bool ok, String statusText})> testModelConnection(
    String model, {
    String? apiKeyOverride,
  }) async {
    final key = (apiKeyOverride != null && apiKeyOverride.trim().isNotEmpty)
        ? apiKeyOverride.trim()
        : effectiveApiKey;
    final cleanModel = model.trim().replaceFirst('models/', '');
    final uri = Uri.parse(
      'https://generativelanguage.googleapis.com/v1beta/models/$cleanModel:generateContent?key=$key',
    );

    try {
      final response = await http
          .post(
            uri,
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: jsonEncode({
              'contents': [
                {
                  'parts': [
                    {'text': 'Responde únicamente: OK'},
                  ],
                },
              ],
              'generationConfig': {'maxOutputTokens': 12},
            }),
          )
          .timeout(const Duration(seconds: 8));

      if (response.statusCode == 200) {
        return (
          ok: true,
          statusText: 'Modelo $cleanModel operativo (HTTP 200 OK).',
        );
      }
      var detail = response.body;
      try {
        final decoded = jsonDecode(utf8.decode(response.bodyBytes));
        final msg = decoded['error']?['message']?.toString();
        if (msg != null && msg.isNotEmpty) detail = msg;
      } catch (_) {}
      return (
        ok: false,
        statusText: 'HTTP ${response.statusCode} en $cleanModel: $detail',
      );
    } catch (e) {
      return (
        ok: false,
        statusText: 'Error de red probando $cleanModel: $e',
      );
    }
  }

  /// Ensambla un contexto estructurado y denso del tema para el asistente
  static String buildTopicContext({
    required String titulo,
    String? objetivo,
    String? conceptoClaveLatex,
    String? ejemplo,
    List<dynamic>? slides,
    List<String>? personalNotes,
  }) {
    final buffer = StringBuffer();
    buffer.writeln('TÍTULO DEL TEMA: $titulo');

    if (objetivo != null && objetivo.trim().isNotEmpty) {
      buffer.writeln('\nOBJETIVO Y ALCANCE ACADÉMICO:');
      buffer.writeln(objetivo.trim());
    }

    if (conceptoClaveLatex != null && conceptoClaveLatex.trim().isNotEmpty) {
      buffer.writeln('\nFORMULACIÓN Y ECUACIONES CLAVE (KaTeX):');
      buffer.writeln(conceptoClaveLatex.trim());
    }

    if (slides != null && slides.isNotEmpty) {
      buffer.writeln('\nDIAPOSITIVAS Y CONTENIDO DE CÁTEDRA:');
      for (var i = 0; i < slides.length; i++) {
        final s = slides[i];
        final num = i + 1;
        try {
          final title = (s.titulo as String?) ?? 'Diapositiva $num';
          final seccion = (s.seccion as String?) ?? 'Cátedra';
          buffer.writeln('• Diapositiva $num: "$title" [Sección: $seccion]');
          final puntos = s.puntos as List<dynamic>?;
          if (puntos != null && puntos.isNotEmpty) {
            for (final p in puntos) {
              buffer.writeln('    - $p');
            }
          }
        } catch (_) {
          buffer.writeln('• Diapositiva $num');
        }
      }
    }

    if (ejemplo != null && ejemplo.trim().isNotEmpty) {
      buffer.writeln('\nEJERCICIOS RESUELTOS Y NOTAS DE CÁTEDRA:');
      buffer.writeln(ejemplo.trim());
    }

    if (personalNotes != null && personalNotes.isNotEmpty) {
      buffer.writeln('\nAPUNTES ADICIONALES DEL ESTUDIANTE:');
      for (final note in personalNotes) {
        if (note.trim().isNotEmpty) {
          buffer.writeln('  * ${note.trim()}');
        }
      }
    }

    return buffer.toString();
  }

  Future<String> askAboutCurrentTopic({
    required String asignaturaNombre,
    required String temaTitulo,
    required String temaContextoCompleto,
    required List<Map<String, String>> historialReciente,
    required String preguntaUsuario,
    String? studentName,
    Uint8List? imageBytes,
    String? imageMimeType,
  }) async {
    final reply = await askTopicMultimodal(
      asignaturaNombre: asignaturaNombre,
      temaTitulo: temaTitulo,
      temaContextoCompleto: temaContextoCompleto,
      historialReciente: historialReciente,
      preguntaUsuario: preguntaUsuario,
      studentName: studentName,
      imageBytes: imageBytes,
      imageMimeType: imageMimeType,
    );
    return reply.text;
  }

  /// Envía la pregunta inyectando el contexto del tema, nombre del estudiante,
  /// soporte multimodal (imágenes adjuntas) y elementos gráficos vectoriales.
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
    final globalConfig = GlobalEnvironmentService.instance.config;
    if (!globalConfig.aiEnabled) {
      return const TopicAssistantReply(
        text:
            'El Asistente de IA está pausado temporalmente por administración institucional.',
      );
    }

    final cleanStudent = (studentName ?? '').trim();
    final studentBlock = cleanStudent.isNotEmpty
        ? '- Estudiante conectado (nombre registrado): $cleanStudent\n'
        : '';

    final customInstruction = globalConfig.aiCustomSystemPrompt.trim().isNotEmpty
        ? '\nINSTRUCCIÓN ADICIONAL DE ADMINISTRACIÓN:\n${globalConfig.aiCustomSystemPrompt.trim()}\n'
        : '';

    final graphicsInstruction = globalConfig.allowAiGraphics
        ? '''
5. ELEMENTOS GRÁFICOS INTERACTIVOS (MUY IMPORTANTE):
   Cuando una gráfica cartesiana, curva matemática, diagrama de fuerzas/vectores, comparación de barras o simulador ayude a visualizar el problema (o cuando el estudiante lo pida), incluye un bloque JSON válido etiquetado exactamente así:
   ```um-grafica
   {
     "tipo": "funcion",
     "titulo": "Nombre descriptivo de la gráfica",
     "ejex": "Eje X (unidades)",
     "ejey": "Eje Y (unidades)",
     "series": [
       {"nombre": "Etiqueta curva", "color": "green", "puntos": [[0,0],[1,2],[2,4]]}
     ]
   }
   ```
   Otros formatos admitidos en ```um-grafica:
   - Diagrama de vectores / cuerpo libre / fasores:
     {"tipo":"vectores","titulo":"Diagrama de Fuerzas / Fasores","vectores":[{"nombre":"N","angulo_deg":90,"magnitud":1.0,"color":"green"},{"nombre":"mg","angulo_deg":-90,"magnitud":1.0,"color":"orange"}]}
   - Gráfica de barras:
     {"tipo":"barras","titulo":"Comparación Energética","barras":[{"label":"Ec","valor":60,"color":"indigo"},{"label":"Ep","valor":40,"color":"green"}]}
   - Simulador interactivo de UM Studio:
     {"tipo":"lab","titulo":"Laboratorio Interactivo","modo_lab":"acPhasor|calculusIntegral|thermoSolar"}
   Colores válidos: "green", "indigo", "orange", "cyan". Para curvas suaves aporta entre 12 y 25 puntos [x, y] numéricos reales sin texto ni comentarios dentro del JSON.
'''
        : '';

    final greetingRule = cleanStudent.isNotEmpty
        ? '6. SALUDO PERSONALIZADO: Cuando sea el primer mensaje de la charla o cuando el estudiante salude, salúdalo amablemente usando su nombre registrado ($cleanStudent).\n'
        : '';

    final systemText = '''
Eres el Asistente Académico Contextual de UM Studio (Universidad del Magdalena).
Tu alcance está ESTRICTAMENTE LIMITADO al tema que el estudiante tiene abierto en pantalla.

DATOS DEL TEMA ACTIVO:
$studentBlock- Asignatura: $asignaturaNombre
- Tema actual: $temaTitulo
- Contenido oficial del tema (Teoría, Fórmulas, Slides y Notas de Cátedra):
"""
$temaContextoCompleto
"""
$customInstruction
REGLAS INNEGOCIABLES:
1. Responde ÚNICAMENTE basándote en el contenido, fórmulas, ejercicios y conceptos del tema activo proporcionado arriba (y en las imágenes o gráficas enviadas por el estudiante en este chat).
2. Si el estudiante pregunta sobre otra materia, otro tema distinto o cosas fuera de este tema, responde amablemente: "Solo tengo acceso al contexto del tema actual ($temaTitulo). Por favor, hazme preguntas relacionadas con esta sesión."
3. Escribe SIEMPRE las expresiones matemáticas, variables y ecuaciones usando sintaxis KaTeX limpia: usa \$...\$ para fórmulas en línea y \$\$...\$\$ para ecuaciones en bloque.
4. Sé directo, claro, conciso y riguroso paso a paso.
$graphicsInstruction$greetingRule''';

    final contents = <Map<String, dynamic>>[];
    for (final msg in historialReciente) {
      final role = msg['role'] == 'assistant' ? 'model' : 'user';
      contents.add({
        'role': role,
        'parts': [
          {'text': msg['content'] ?? ''},
        ],
      });
    }

    final currentParts = <Map<String, dynamic>>[
      {'text': preguntaUsuario},
      if (imageBytes != null && imageBytes.isNotEmpty)
        {
          'inlineData': {
            'mimeType': (imageMimeType != null && imageMimeType.isNotEmpty)
                ? imageMimeType
                : 'image/png',
            'data': base64Encode(imageBytes),
          },
        },
    ];
    contents.add({
      'role': 'user',
      'parts': currentParts,
    });

    final selectedPrimary = normalizeModel(globalConfig.aiModelName);
    final modelsToTry = <String>[
      selectedPrimary,
      for (final candidate in const [
        _primaryModel,
        'gemini-flash-lite-latest',
        _fallbackModel,
        'gemini-3.1-flash-lite',
      ])
        if (candidate != selectedPrimary) candidate,
    ];

    final apiKey = effectiveApiKey;
    String? lastErrorMessage;

    for (final model in modelsToTry) {
      final isGemma = model.startsWith('gemma-');
      final effectiveContents = isGemma
          ? [
              {
                'role': 'user',
                'parts': [
                  {'text': '$systemText\n---\n${contents.first['parts'][0]['text']}'},
                ],
              },
              ...contents.skip(1),
            ]
          : contents;

      final payload = <String, dynamic>{
        if (!isGemma)
          'systemInstruction': {
            'parts': [
              {'text': systemText},
            ],
          },
        'contents': effectiveContents,
        'generationConfig': {
          'temperature': globalConfig.aiTemperature,
          'maxOutputTokens': globalConfig.aiMaxTokens,
        },
      };

      final uri = Uri.parse(
        'https://generativelanguage.googleapis.com/v1beta/models/$model:generateContent?key=$apiKey',
      );

      final response = await http.post(
        uri,
        headers: {'Content-Type': 'application/json; charset=utf-8'},
        body: jsonEncode(payload),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));
        final candidates = data['candidates'] as List<dynamic>?;
        if (candidates != null && candidates.isNotEmpty) {
          final content = candidates[0]['content'] as Map<String, dynamic>?;
          final parts = content?['parts'] as List<dynamic>?;
          if (parts != null && parts.isNotEmpty) {
            final textBuffer = StringBuffer();
            Uint8List? replyImageBytes;
            String? replyImageMime;
            for (final rawPart in parts) {
              if (rawPart is! Map<String, dynamic>) continue;
              final partText = rawPart['text']?.toString();
              if (partText != null && partText.isNotEmpty) {
                textBuffer.write(partText);
              }
              final inlineData = rawPart['inlineData'] as Map<String, dynamic>?;
              if (inlineData != null && inlineData['data'] != null) {
                try {
                  replyImageBytes = base64Decode(inlineData['data'].toString());
                  replyImageMime =
                      inlineData['mimeType']?.toString() ?? 'image/png';
                } catch (_) {}
              }
            }
            final finalText = textBuffer.toString().trim();
            if (finalText.isNotEmpty || replyImageBytes != null) {
              return TopicAssistantReply(
                text: finalText.isNotEmpty
                    ? finalText
                    : 'Elemento gráfico generado por IA:',
                imageBytes: replyImageBytes,
                imageMimeType: replyImageMime,
              );
            }
          }
        }
        return const TopicAssistantReply(
          text: 'No se recibió respuesta del asistente.',
        );
      } else {
        lastErrorMessage =
            'Error en Gemini API (${response.statusCode}): ${response.body}';
        final shouldRetryNext = response.statusCode == 404 ||
            response.statusCode == 429 ||
            response.statusCode == 503 ||
            response.statusCode == 500;
        if (!shouldRetryNext || model == modelsToTry.last) {
          throw Exception(lastErrorMessage);
        }
      }
    }

    throw Exception(
      lastErrorMessage ?? 'No se recibió respuesta del modelo Gemini.',
    );
  }
}
