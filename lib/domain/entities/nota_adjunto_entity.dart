import 'dart:typed_data';

import '../../core/utils/institutional_validator.dart';

/// Tipos de registro soportados en `notas_adjuntos_estudiante`.
enum TipoAdjuntoEstudiante {
  pdf('pdf'),
  imagen('imagen'),
  nota('nota');

  const TipoAdjuntoEstudiante(this.dbValue);
  final String dbValue;

  static TipoAdjuntoEstudiante fromDb(String raw) {
    switch (raw.trim().toLowerCase()) {
      case 'pdf':
        return TipoAdjuntoEstudiante.pdf;
      case 'imagen':
        return TipoAdjuntoEstudiante.imagen;
      case 'nota':
      default:
        return TipoAdjuntoEstudiante.nota;
    }
  }
}

/// Entidad de dominio para notas y adjuntos vinculados a un estudiante.
class NotaAdjuntoEntity {
  const NotaAdjuntoEntity({
    required this.id,
    required this.temaId,
    required this.usuarioId,
    required this.tipoArchivo,
    this.urlArchivo,
    this.nombreArchivo,
    this.pesoBytes,
    this.contenidoNota,
    required this.createdAt,
    required this.updatedAt,
    this.localBytes,
  });

  final String id;
  final String temaId;
  final String usuarioId;
  final TipoAdjuntoEstudiante tipoArchivo;
  final String? urlArchivo;
  final String? nombreArchivo;
  final int? pesoBytes;
  final String? contenidoNota;
  final DateTime createdAt;
  final DateTime updatedAt;
  final Uint8List? localBytes;

  bool get esArchivo =>
      tipoArchivo == TipoAdjuntoEstudiante.pdf ||
      tipoArchivo == TipoAdjuntoEstudiante.imagen;

  String get pesoFormateado =>
      InstitutionalValidator.formatByteSize(pesoBytes ?? localBytes?.length);
}
