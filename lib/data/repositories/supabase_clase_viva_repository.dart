import 'dart:typed_data';

import 'package:supabase_flutter/supabase_flutter.dart';

import '../../core/constants/app_constants.dart';
import '../../core/utils/institutional_validator.dart';
import '../../domain/entities/nota_adjunto_entity.dart';
import '../../domain/entities/tema_estudio_entity.dart';
import '../../domain/repositories/i_clase_viva_repository.dart';
import '../datasources/academic_seed_data.dart';
import '../models/nota_adjunto_model.dart';
import '../models/tema_estudio_model.dart';

/// Implementación conectada a PostgreSQL Realtime y Storage de Supabase.
class SupabaseClaseVivaRepository implements IClaseVivaRepository {
  SupabaseClaseVivaRepository({
    required SupabaseClient client,
    String? fallbackUserId,
  })  : _client = client,
        _fallbackUserId = fallbackUserId ?? AppConstants.defaultStudentEmail;

  final SupabaseClient _client;
  String _fallbackUserId;

  final Map<String, Uint8List> _sessionBytesCache = {};

  @override
  bool get isCloudBackend => true;

  @override
  String get activeUserId =>
      _client.auth.currentUser?.email ??
      _client.auth.currentUser?.id ??
      _fallbackUserId;

  @override
  void updateActiveUser(String institutionalEmail) {
    final clean = institutionalEmail.trim().toLowerCase();
    if (!InstitutionalValidator.isValidInstitutionalEmail(clean)) {
      throw ArgumentError(
        'Dominio inválido. Se requiere ${AppConstants.institutionalDomain}',
      );
    }
    _fallbackUserId = clean;
  }

  @override
  Stream<TemaEstudioEntity> watchTemaEstudio(String temaId) {
    return _client
        .from('temas_estudio')
        .stream(primaryKey: ['id'])
        .eq('id', temaId)
        .map((rows) {
          if (rows.isEmpty) {
            return AcademicSeedData.temasEstudio[temaId] ??
                AcademicSeedData.temasEstudio['fisica']!;
          }
          return TemaEstudioModel.fromJson(rows.first);
        });
  }

  @override
  Stream<List<NotaAdjuntoEntity>> watchNotasYAdjuntos({
    required String temaId,
    String? usuarioId,
  }) {
    final uid = usuarioId ?? activeUserId;
    return _client
        .from('notas_adjuntos_estudiante')
        .stream(primaryKey: ['id'])
        .eq('tema_id', temaId)
        .map((rows) {
          final filtered = rows
              .where((r) => (r['usuario_id'] ?? '').toString() == uid)
              .map<NotaAdjuntoEntity>(
                (r) => NotaAdjuntoModel.fromJson(
                  r,
                  cachedBytes: _sessionBytesCache[(r['id'] ?? '').toString()],
                ),
              )
              .toList()
            ..sort((a, b) => b.createdAt.compareTo(a.createdAt));
          return filtered;
        });
  }

  @override
  Future<NotaAdjuntoEntity> subirArchivoAdjunto({
    required String temaId,
    required TipoAdjuntoEstudiante tipoArchivo,
    required String nombreArchivo,
    required Uint8List bytes,
    String? usuarioId,
  }) async {
    final uid = usuarioId ?? activeUserId;
    final cleanName =
        nombreArchivo.replaceAll(RegExp(r'[^a-zA-Z0-9._-]'), '_');
    final stamp = DateTime.now().millisecondsSinceEpoch;
    final storagePath = '$uid/$temaId/${stamp}_$cleanName';
    final contentType = _inferMimeType(tipoArchivo, cleanName);

    await _client.storage.from(AppConstants.storageBucket).uploadBinary(
          storagePath,
          bytes,
          fileOptions: FileOptions(contentType: contentType, upsert: true),
        );

    final publicUrl = _client.storage
        .from(AppConstants.storageBucket)
        .getPublicUrl(storagePath);

    final inserted = await _client
        .from('notas_adjuntos_estudiante')
        .insert({
          'tema_id': temaId,
          'usuario_id': uid,
          'tipo_archivo': tipoArchivo.dbValue,
          'url_archivo': publicUrl,
          'nombre_archivo': nombreArchivo,
          'peso_bytes': bytes.length,
        })
        .select()
        .single();

    final id = (inserted['id'] ?? '').toString();
    _sessionBytesCache[id] = bytes;
    return NotaAdjuntoModel.fromJson(inserted, cachedBytes: bytes);
  }

  @override
  Future<void> eliminarAdjunto({
    required NotaAdjuntoEntity adjunto,
  }) async {
    _sessionBytesCache.remove(adjunto.id);
    await _client
        .from('notas_adjuntos_estudiante')
        .delete()
        .eq('id', adjunto.id);
  }

  @override
  Future<NotaAdjuntoEntity> guardarNotaPersonal({
    required String temaId,
    required String contenido,
    String? usuarioId,
  }) async {
    final uid = usuarioId ?? activeUserId;
    final existing = await _client
        .from('notas_adjuntos_estudiante')
        .select()
        .eq('tema_id', temaId)
        .eq('usuario_id', uid)
        .eq('tipo_archivo', TipoAdjuntoEstudiante.nota.dbValue)
        .maybeSingle();

    final nowIso = DateTime.now().toIso8601String();
    if (existing != null) {
      final updated = await _client
          .from('notas_adjuntos_estudiante')
          .update({
            'contenido_nota': contenido,
            'updated_at': nowIso,
          })
          .eq('id', existing['id'] as Object)
          .select()
          .single();
      return NotaAdjuntoModel.fromJson(updated);
    } else {
      final inserted = await _client
          .from('notas_adjuntos_estudiante')
          .insert({
            'tema_id': temaId,
            'usuario_id': uid,
            'tipo_archivo': TipoAdjuntoEstudiante.nota.dbValue,
            'contenido_nota': contenido,
            'updated_at': nowIso,
          })
          .select()
          .single();
      return NotaAdjuntoModel.fromJson(inserted);
    }
  }

  String _inferMimeType(TipoAdjuntoEstudiante tipo, String name) {
    if (tipo == TipoAdjuntoEstudiante.pdf) return 'application/pdf';
    final lower = name.toLowerCase();
    if (lower.endsWith('.png')) return 'image/png';
    if (lower.endsWith('.webp')) return 'image/webp';
    return 'image/jpeg';
  }
}
