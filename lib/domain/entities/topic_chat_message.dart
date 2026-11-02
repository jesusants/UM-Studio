class TopicChatMessage {
  const TopicChatMessage({
    required this.id,
    required this.role,
    required this.content,
    required this.timestamp,
    this.isError = false,
  });

  final String id;
  final String role; // 'user' | 'assistant'
  final String content;
  final DateTime timestamp;
  final bool isError;

  bool get isUser => role == 'user';
  bool get isAssistant => role == 'assistant';

  Map<String, String> toApiMap() {
    return {
      'role': role,
      'content': content,
    };
  }
}
