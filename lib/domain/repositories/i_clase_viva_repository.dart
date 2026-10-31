import 'dart:typed_data';

import '../entities/nota_adjunto_entity.dart';
import '../entities/tema_estudio_entity.dart';

/// Contrato de repositorio en el dominio para "La Clase Viva" & Adjuntos.
abstract class IClaseVivaRepository {
  String get activeUserId;
  bool get isCloudBackend;

  /// Actualiza el identificador institucional activo (restringido a `@unimagdalena.edu.co`).
  void updateActiveUser(String institutionalEmail);

  /// Lectura reactiva del tema oficial desde `temas_estudio`.
  Stream<TemaEstudioEntity> watchTemaEstudio(String temaId);

  /// Lectura reactiva de archivos (`pdf`, `imagen`) y `nota` del estudiante
  /// desde `notas_adjuntos_estudiante`.
  Stream<List<NotaAdjuntoEntity>> watchNotasYAdjuntos({
    required String temaId,
    String? usuarioId,
  });

  /// Sube un archivo (`pdf` o `imagen`) y crea el registro en `notas_adjuntos_estudiante`.
  Future<NotaAdjuntoEntity> subirArchivoAdjunto({
    required String temaId,
    required TipoAdjuntoEstudiante tipoArchivo,
    required String nombreArchivo,
    required Uint8List bytes,
    String? usuarioId,
  });

  /// Elimina un archivo vinculado.
  Future<void> eliminarAdjunto({
    required NotaAdjuntoEntity adjunto,
  });

  /// Guarda o actualiza la nota personal (`tipo_archivo = 'nota'`) del alumno.
  Future<NotaAdjuntoEntity> guardarNotaPersonal({
    required String temaId,
    required String contenido,
    String? usuarioId,
  });
}
