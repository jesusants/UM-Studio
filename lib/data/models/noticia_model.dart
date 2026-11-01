/// Modelo representativo de una publicación o noticia oficial de la Universidad del Magdalena.
class NoticiaModel {
  const NoticiaModel({
    required this.id,
    required this.title,
    required this.summary,
    required this.url,
    required this.imageUrl,
    required this.dateText,
    this.category = 'FACULTAD',
    this.publishedAt,
    this.isNew = false,
  });

  final String id;
  final String title;
  final String summary;
  final String url;
  final String imageUrl;
  final String dateText;
  final String category;
  final DateTime? publishedAt;
  final bool isNew;

  /// Retorna si la noticia fue publicada hace menos de 24 horas
  bool get isRecent {
    if (isNew) return true;
    if (publishedAt != null) {
      return DateTime.now().difference(publishedAt!).inHours < 24;
    }
    final lower = dateText.toLowerCase();
    return lower.contains('hoy') || lower.contains('hace') || lower.contains('hora');
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'title': title,
        'summary': summary,
        'url': url,
        'imageUrl': imageUrl,
        'dateText': dateText,
        'category': category,
        'publishedAt': publishedAt?.toIso8601String(),
        'isNew': isNew,
      };

  factory NoticiaModel.fromJson(Map<String, dynamic> json) => NoticiaModel(
        id: json['id'] as String? ?? '',
        title: json['title'] as String? ?? '',
        summary: json['summary'] as String? ?? '',
        url: json['url'] as String? ?? '',
        imageUrl: json['imageUrl'] as String? ?? '',
        dateText: json['dateText'] as String? ?? '',
        category: json['category'] as String? ?? 'FACULTAD',
        publishedAt: json['publishedAt'] != null
            ? DateTime.tryParse(json['publishedAt'] as String)
            : null,
        isNew: json['isNew'] as bool? ?? false,
      );

  NoticiaModel copyWith({
    String? id,
    String? title,
    String? summary,
    String? url,
    String? imageUrl,
    String? dateText,
    String? category,
    DateTime? publishedAt,
    bool? isNew,
  }) {
    return NoticiaModel(
      id: id ?? this.id,
      title: title ?? this.title,
      summary: summary ?? this.summary,
      url: url ?? this.url,
      imageUrl: imageUrl ?? this.imageUrl,
      dateText: dateText ?? this.dateText,
      category: category ?? this.category,
      publishedAt: publishedAt ?? this.publishedAt,
      isNew: isNew ?? this.isNew,
    );
  }
}
