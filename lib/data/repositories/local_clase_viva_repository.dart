import 'dart:async';
import 'dart:convert';
import 'dart:typed_data';

import 'package:shared_preferences/shared_preferences.dart';

import '../../core/constants/app_constants.dart';
import '../../core/utils/institutional_validator.dart';
import '../../domain/entities/nota_adjunto_entity.dart';
import '../../domain/entities/tema_estudio_entity.dart';
import '../../domain/repositories/i_clase_viva_repository.dart';
import '../datasources/academic_seed_data.dart';
import '../models/nota_adjunto_model.dart';
import '../services/markdown_curriculum_service.dart';

/// Repositorio reactivo Offline-First conectado a `MarkdownCurriculumService`
/// (`ingenieria_energetica.md`) y sincronizado con `db/users/{username}.json`.
class LocalReactiveClaseVivaRepository implements IClaseVivaRepository {
  LocalReactiveClaseVivaRepository({
    this.initialLatency = const Duration(milliseconds: 220),
    String? userId,
    MarkdownCurriculumService? curriculumService,
    this.onPersonalNoteSynced,
  })  : _userId = userId ?? AppConstants.defaultStudentEmail,
        _curriculumService = curriculumService;

  static const String _storagePrefix = 'um_studio_notas_adjuntos_v2_';

  final Duration initialLatency;
  final MarkdownCurriculumService? _curriculumService;

  /// Callback opcional para replicar apuntes en `db/users/{username}.json` en GitHub.
  void Function(String temaId, String contenido)? onPersonalNoteSynced;

  String _userId;

  final Map<String, StreamController<List<NotaAdjuntoEntity>>> _controllers =
      {};
  final Map<String, List<NotaAdjuntoModel>> _cache = {};
  final Map<String, Uint8List> _memoryBytes = {};
  int _idSeq = 0;

  @override
  bool get isCloudBackend => true;

  @override
  String get activeUserId => _userId;

  @override
  void updateActiveUser(String institutionalEmail) {
    final clean = institutionalEmail.trim().toLowerCase();
    if (!InstitutionalValidator.isValidInstitutionalEmail(clean)) {
      throw ArgumentError(
        'Dominio inválido. Se requiere ${AppConstants.institutionalDomain}',
      );
    }
    _userId = clean;
  }

  String _key(String temaId, String uid) => '$_storagePrefix${uid}_$temaId';

  TemaEstudioEntity _resolveCurrentTema(String temaId) {
    final fromMd = _curriculumService?.database?.resolveTemaEstudio(temaId);
    if (fromMd != null) return fromMd;
    return AcademicSeedData.temasEstudio[temaId] ??
        AcademicSeedData.temasEstudio['fisica']!;
  }

  @override
  Stream<TemaEstudioEntity> watchTemaEstudio(String temaId) {
    late final StreamController<TemaEstudioEntity> controller;
    void onCurriculumChanged() {
      if (!controller.isClosed) {
        controller.add(_resolveCurrentTema(temaId));
      }
    }

    controller = StreamController<TemaEstudioEntity>(
      onListen: () async {
        if (initialLatency > Duration.zero) {
          await Future<void>.delayed(initialLatency);
        }
        if (!controller.isClosed) {
          controller.add(_resolveCurrentTema(temaId));
        }
        _curriculumService?.addListener(onCurriculumChanged);
      },
      onCancel: () {
        _curriculumService?.removeListener(onCurriculumChanged);
      },
    );

    return controller.stream;
  }

  /// Hidrata apuntes descargados desde `db/users/{username}.json` en GitHub.
  Future<void> hydrateNotesFromGitHub({
    required String institutionalEmail,
    required Map<String, dynamic> apuntesPersonales,
  }) async {
    final uid = institutionalEmail.trim().toLowerCase();
    for (final entry in apuntesPersonales.entries) {
      final temaId = entry.key;
      final value = entry.value;
      final noteText = value is Map
          ? (value['nota'] ?? '').toString()
          : (value ?? '').toString();
      if (noteText.trim().isEmpty) continue;

      final items = List<NotaAdjuntoModel>.from(await _loadItems(temaId, uid));
      final existingIdx = items.indexWhere(
        (e) => e.tipoArchivo == TipoAdjuntoEstudiante.nota,
      );
      if (existingIdx == -1) {
        final now = DateTime.now();
        _idSeq++;
        items.add(
          NotaAdjuntoModel(
            id: 'nota_gh_${now.microsecondsSinceEpoch}_$_idSeq',
            temaId: temaId,
            usuarioId: uid,
            tipoArchivo: TipoAdjuntoEstudiante.nota,
            contenidoNota: noteText,
            createdAt: now,
            updatedAt: now,
          ),
        );
        await _persistAndEmit(temaId, uid, items);
      }
    }
  }

  @override
  Stream<List<NotaAdjuntoEntity>> watchNotasYAdjuntos({
    required String temaId,
    String? usuarioId,
  }) {
    final uid = usuarioId ?? activeUserId;
    final key = _key(temaId, uid);
    final ctrl = _controllers.putIfAbsent(
      key,
      () => StreamController<List<NotaAdjuntoEntity>>.broadcast(),
    );
    return _createInitialPlusUpdatesStream(temaId, uid, ctrl);
  }

  Stream<List<NotaAdjuntoEntity>> _createInitialPlusUpdatesStream(
    String temaId,
    String uid,
    StreamController<List<NotaAdjuntoEntity>> broadcastCtrl,
  ) async* {
    final initial = await _loadItems(temaId, uid);
    yield List<NotaAdjuntoEntity>.unmodifiable(initial);
    yield* broadcastCtrl.stream;
  }

  Future<List<NotaAdjuntoModel>> _loadItems(
    String temaId,
    String uid,
  ) async {
    final key = _key(temaId, uid);
    if (_cache.containsKey(key)) {
      return _cache[key]!;
    }
    final prefs = await SharedPreferences.getInstance();
    final raw = prefs.getString(key);
    if (raw == null || raw.isEmpty) {
      _cache[key] = <NotaAdjuntoModel>[];
      return _cache[key]!;
    }
    try {
      final decoded = jsonDecode(raw) as List<dynamic>;
      final list = decoded
          .whereType<Map<String, dynamic>>()
          .map(
            (m) => NotaAdjuntoModel.fromJson(
              m,
              cachedBytes: _memoryBytes[(m['id'] ?? '').toString()],
            ),
          )
          .toList()
        ..sort((a, b) => b.createdAt.compareTo(a.createdAt));
      for (final item in list) {
        if (item.localBytes != null) {
          _memoryBytes[item.id] = item.localBytes!;
        }
      }
      _cache[key] = list;
      return list;
    } catch (_) {
      _cache[key] = <NotaAdjuntoModel>[];
      return _cache[key]!;
    }
  }

  Future<void> _persistAndEmit(
    String temaId,
    String uid,
    List<NotaAdjuntoModel> items,
  ) async {
    final key = _key(temaId, uid);
    items.sort((a, b) => b.createdAt.compareTo(a.createdAt));
    _cache[key] = items;

    final prefs = await SharedPreferences.getInstance();
    final encoded = jsonEncode(
      items.map((e) => e.toJson(includeLocalBytes: true)).toList(),
    );
    await prefs.setString(key, encoded);

    final ctrl = _controllers[key];
    if (ctrl != null && !ctrl.isClosed) {
      ctrl.add(List<NotaAdjuntoEntity>.unmodifiable(items));
    }
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
    final items = List<NotaAdjuntoModel>.from(await _loadItems(temaId, uid));
    final now = DateTime.now();
    _idSeq++;
    final id = 'adj_${now.microsecondsSinceEpoch}_$_idSeq';
    _memoryBytes[id] = bytes;

    final safeName = Uri.encodeComponent(nombreArchivo);
    final localRefUrl =
        'https://github.com/${AppConstants.githubOwner}/${AppConstants.githubRepo}/tree/${AppConstants.githubBranch}/db/users/$uid/$temaId/$safeName';

    final nuevo = NotaAdjuntoModel(
      id: id,
      temaId: temaId,
      usuarioId: uid,
      tipoArchivo: tipoArchivo,
      urlArchivo: localRefUrl,
      nombreArchivo: nombreArchivo,
      pesoBytes: bytes.length,
      createdAt: now,
      updatedAt: now,
      localBytes: bytes,
    );

    items.insert(0, nuevo);
    await _persistAndEmit(temaId, uid, items);
    return nuevo;
  }

  @override
  Future<void> eliminarAdjunto({
    required NotaAdjuntoEntity adjunto,
  }) async {
    _memoryBytes.remove(adjunto.id);
    final items = List<NotaAdjuntoModel>.from(
      await _loadItems(adjunto.temaId, adjunto.usuarioId),
    )..removeWhere((e) => e.id == adjunto.id);
    await _persistAndEmit(adjunto.temaId, adjunto.usuarioId, items);
  }

  @override
  Future<NotaAdjuntoEntity> guardarNotaPersonal({
    required String temaId,
    required String contenido,
    String? usuarioId,
  }) async {
    final uid = usuarioId ?? activeUserId;
    final items = List<NotaAdjuntoModel>.from(await _loadItems(temaId, uid));
    final now = DateTime.now();
    final idx = items.indexWhere(
      (e) => e.tipoArchivo == TipoAdjuntoEstudiante.nota,
    );

    late final NotaAdjuntoModel saved;
    if (idx >= 0) {
      saved = items[idx].copyWith(
        contenidoNota: contenido,
        updatedAt: now,
      );
      items[idx] = saved;
    } else {
      _idSeq++;
      saved = NotaAdjuntoModel(
        id: 'nota_${now.microsecondsSinceEpoch}_$_idSeq',
        temaId: temaId,
        usuarioId: uid,
        tipoArchivo: TipoAdjuntoEstudiante.nota,
        contenidoNota: contenido,
        createdAt: now,
        updatedAt: now,
      );
      items.add(saved);
    }

    await _persistAndEmit(temaId, uid, items);
    onPersonalNoteSynced?.call(temaId, contenido);
    return saved;
  }
}
