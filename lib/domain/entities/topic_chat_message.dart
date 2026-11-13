import 'dart:typed_data';

class TopicChatMessage {
  const TopicChatMessage({
    required this.id,
    required this.role,
    required this.content,
    required this.timestamp,
    this.isError = false,
    this.imageBytes,
    this.imageMimeType,
    this.imageName,
  });

  final String id;
  final String role; // 'user' | 'assistant'
  final String content;
  final DateTime timestamp;
  final bool isError;
  final Uint8List? imageBytes;
  final String? imageMimeType;
  final String? imageName;

  bool get isUser => role == 'user';
  bool get isAssistant => role == 'assistant';
  bool get hasImage => imageBytes != null && imageBytes!.isNotEmpty;

  Map<String, String> toApiMap() {
    return {
      'role': role,
      'content': content,
    };
  }
}
