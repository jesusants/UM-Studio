import 'dart:convert';
import 'dart:typed_data';

import '../../domain/entities/nota_adjunto_entity.dart';

/// DTO con serialización `fromJson` / `toJson` para `notas_adjuntos_estudiante`.
class NotaAdjuntoModel extends NotaAdjuntoEntity {
  const NotaAdjuntoModel({
    required super.id,
    required super.temaId,
    required super.usuarioId,
    required super.tipoArchivo,
    super.urlArchivo,
    super.nombreArchivo,
    super.pesoBytes,
    super.contenidoNota,
    required super.createdAt,
    required super.updatedAt,
    super.localBytes,
  });

  NotaAdjuntoModel copyWith({
    String? id,
    String? temaId,
    String? usuarioId,
    TipoAdjuntoEstudiante? tipoArchivo,
    String? urlArchivo,
    String? nombreArchivo,
    int? pesoBytes,
    String? contenidoNota,
    DateTime? createdAt,
    DateTime? updatedAt,
    Uint8List? localBytes,
  }) {
    return NotaAdjuntoModel(
      id: id ?? this.id,
      temaId: temaId ?? this.temaId,
      usuarioId: usuarioId ?? this.usuarioId,
      tipoArchivo: tipoArchivo ?? this.tipoArchivo,
      urlArchivo: urlArchivo ?? this.urlArchivo,
      nombreArchivo: nombreArchivo ?? this.nombreArchivo,
      pesoBytes: pesoBytes ?? this.pesoBytes,
      contenidoNota: contenidoNota ?? this.contenidoNota,
      createdAt: createdAt ?? this.createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
      localBytes: localBytes ?? this.localBytes,
    );
  }

  factory NotaAdjuntoModel.fromJson(
    Map<String, dynamic> json, {
    Uint8List? cachedBytes,
  }) {
    Uint8List? decoded = cachedBytes;
    final b64 = json['local_bytes_b64'];
    if (decoded == null && b64 is String && b64.isNotEmpty) {
      try {
        decoded = base64Decode(b64);
      } catch (_) {}
    }

    final now = DateTime.now();
    return NotaAdjuntoModel(
      id: (json['id'] ?? '').toString(),
      temaId: (json['tema_id'] ?? '').toString(),
      usuarioId: (json['usuario_id'] ?? '').toString(),
      tipoArchivo: TipoAdjuntoEstudiante.fromDb(
        (json['tipo_archivo'] ?? 'nota').toString(),
      ),
      urlArchivo: json['url_archivo']?.toString(),
      nombreArchivo: json['nombre_archivo']?.toString(),
      pesoBytes: (json['peso_bytes'] is num)
          ? (json['peso_bytes'] as num).toInt()
          : int.tryParse((json['peso_bytes'] ?? '').toString()),
      contenidoNota: json['contenido_nota']?.toString(),
      createdAt:
          DateTime.tryParse((json['created_at'] ?? '').toString()) ?? now,
      updatedAt:
          DateTime.tryParse((json['updated_at'] ?? '').toString()) ?? now,
      localBytes: decoded,
    );
  }

  Map<String, dynamic> toJson({bool includeLocalBytes = false}) {
    final map = <String, dynamic>{
      'id': id,
      'tema_id': temaId,
      'usuario_id': usuarioId,
      'tipo_archivo': tipoArchivo.dbValue,
      'url_archivo': urlArchivo,
      'nombre_archivo': nombreArchivo,
      'peso_bytes': pesoBytes,
      'contenido_nota': contenidoNota,
      'created_at': createdAt.toIso8601String(),
      'updated_at': updatedAt.toIso8601String(),
    };
    if (includeLocalBytes &&
        localBytes != null &&
        localBytes!.length <= 2621440) {
      map['local_bytes_b64'] = base64Encode(localBytes!);
    }
    return map;
  }
}
