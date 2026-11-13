import 'package:flutter/foundation.dart';
import '../../data/services/groq_topic_assistant_service.dart';
import '../../domain/entities/topic_chat_message.dart';

/// Controlador en memoria que gestiona el historial de chat aislado por tema
class TopicAiAssistantController extends ChangeNotifier {
  TopicAiAssistantController({GroqTopicAssistantService? service})
      : _service = service ?? GroqTopicAssistantService();

  static final TopicAiAssistantController instance =
      TopicAiAssistantController();

  final GroqTopicAssistantService _service;

  final Map<String, List<TopicChatMessage>> _historyByTopic = {};
  final Map<String, bool> _loadingByTopic = {};
  final Map<String, String?> _errorByTopic = {};

  List<TopicChatMessage> getHistory(String topicKey) {
    return _historyByTopic[topicKey] ?? const [];
  }

  bool isLoading(String topicKey) {
    return _loadingByTopic[topicKey] ?? false;
  }

  String? getError(String topicKey) {
    return _errorByTopic[topicKey];
  }

  void clearHistory(String topicKey) {
    _historyByTopic[topicKey] = [];
    _errorByTopic[topicKey] = null;
    notifyListeners();
  }

  Future<void> sendQuestion({
    required String topicKey,
    required String asignaturaNombre,
    required String temaTitulo,
    required String temaContextoCompleto,
    required String pregunta,
    String? studentName,
    Uint8List? imageBytes,
    String? imageMimeType,
    String? imageName,
  }) async {
    final query = pregunta.trim();
    if (query.isEmpty && (imageBytes == null || imageBytes.isEmpty)) return;

    final effectiveQuery = query.isNotEmpty
        ? query
        : 'Analiza este elemento gráfico o imagen adjunta respecto al tema actual.';

    final currentList = _historyByTopic.putIfAbsent(topicKey, () => []);

    // 1. Añadir mensaje de usuario (incluyendo imagen si adjuntó elemento gráfico)
    final userMsg = TopicChatMessage(
      id: 'msg_${DateTime.now().microsecondsSinceEpoch}',
      role: 'user',
      content: effectiveQuery,
      timestamp: DateTime.now(),
      imageBytes: imageBytes,
      imageMimeType: imageMimeType,
      imageName: imageName,
    );
    currentList.add(userMsg);
    _loadingByTopic[topicKey] = true;
    _errorByTopic[topicKey] = null;
    notifyListeners();

    // 2. Preparar historial reciente (últimos 6 mensajes para contexto conversacional)
    final recentHistory = currentList
        .where((m) => !m.isError && m != userMsg)
        .take(6)
        .map((m) => m.toApiMap())
        .toList();

    try {
      final reply = await _service.askTopicMultimodal(
        asignaturaNombre: asignaturaNombre,
        temaTitulo: temaTitulo,
        temaContextoCompleto: temaContextoCompleto,
        historialReciente: recentHistory,
        preguntaUsuario: effectiveQuery,
        studentName: studentName,
        imageBytes: imageBytes,
        imageMimeType: imageMimeType,
      );

      final assistantMsg = TopicChatMessage(
        id: 'msg_${DateTime.now().microsecondsSinceEpoch}',
        role: 'assistant',
        content: reply.text,
        timestamp: DateTime.now(),
        imageBytes: reply.imageBytes,
        imageMimeType: reply.imageMimeType,
      );
      currentList.add(assistantMsg);
    } catch (e) {
      final errorMsg = TopicChatMessage(
        id: 'msg_${DateTime.now().microsecondsSinceEpoch}',
        role: 'assistant',
        content:
            '⚠️ No fue posible procesar la consulta: ${e.toString().replaceAll("Exception:", "").trim()}',
        timestamp: DateTime.now(),
        isError: true,
      );
      currentList.add(errorMsg);
      _errorByTopic[topicKey] = e.toString();
    } finally {
      _loadingByTopic[topicKey] = false;
      notifyListeners();
    }
  }
}
