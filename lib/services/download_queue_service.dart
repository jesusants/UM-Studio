import 'dart:async';
import 'dart:collection';
import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import '../core/utils/institutional_validator.dart';
import 'pdf_saver_stub.dart'
    if (dart.library.js_interop) 'pdf_saver_web.dart'
    if (dart.library.io) 'pdf_saver_io.dart';

/// Excepción estricta cuando un PDF supera el límite de 1.2 MB (1,258,291 bytes).
class PdfSizeLimitExceededException implements Exception {
  const PdfSizeLimitExceededException(this.actualBytes);

  final int actualBytes;

  @override
  String toString() =>
      'El PDF generado ($actualBytes bytes) supera el límite máximo permitido de 1.2 MB (1,258,291 bytes).';
}

/// Fases reactivas de una descarga dentro de [DownloadQueueService].
enum DownloadTaskPhase {
  idle,
  queued,
  downloading,
  completed,
  error,
}

/// Estado observable e inmutable de una tarea de descarga de presentación PDF.
@immutable
class DownloadTaskSnapshot {
  const DownloadTaskSnapshot({
    required this.taskId,
    required this.phase,
    this.queuePosition = 0,
    this.sizeBytes,
    this.fromCache = false,
    this.errorMessage,
  });

  static const idle = DownloadTaskSnapshot(
    taskId: '',
    phase: DownloadTaskPhase.idle,
  );

  final String taskId;
  final DownloadTaskPhase phase;
  final int queuePosition;
  final int? sizeBytes;
  final bool fromCache;
  final String? errorMessage;

  /// Etiqueta minimalista para el botón `↓ PDF` del `MinimalSlideViewer`.
  String get buttonLabel {
    switch (phase) {
      case DownloadTaskPhase.idle:
        return '↓ PDF';
      case DownloadTaskPhase.queued:
        final pos = queuePosition > 0 ? queuePosition : 1;
        return '⏳ En cola (#$pos)...';
      case DownloadTaskPhase.downloading:
        if (sizeBytes != null && sizeBytes! > 0) {
          return '↓ Descargando (${InstitutionalValidator.formatByteSize(sizeBytes)})...';
        }
        return '↓ Descargando...';
      case DownloadTaskPhase.completed:
        return '✓ PDF Guardado';
      case DownloadTaskPhase.error:
        return errorMessage ?? '! Error PDF';
    }
  }
}

class _QueuedDownloadTask {
  _QueuedDownloadTask({
    required this.taskId,
    required this.fileName,
    required this.generator,
    required this.completer,
    required this.saveToPlatform,
    this.remoteGitHubUrl,
  });

  final String taskId;
  final String fileName;
  final Future<Uint8List> Function() generator;
  final String? remoteGitHubUrl;
  final bool saveToPlatform;
  final Completer<Uint8List> completer;
}

/// Gestor singleton de cola FIFO para descargas/exportaciones de diapositivas PDF.
///
/// - Concurrencia máxima estricta: **20 descargas simultáneas** (`maxConcurrentDownloads = 20`)
///   para evitar saturación de GitHub cuando todo un salón descarga material al mismo tiempo.
/// - Validación estricta de peso: **`<= 1,258,291 bytes` (`1.2 MB`)** por presentación.
/// - Caché en memoria de sesión + almacenamiento local persistente para entrega en **0 ms**
///   en pulsaciones repetidas sin realizar nuevas peticiones a GitHub.
class DownloadQueueService extends ChangeNotifier {
  DownloadQueueService({
    this.maxConcurrent = maxConcurrentDownloads,
    http.Client? httpClient,
  }) : _http = httpClient ?? http.Client();

  /// Instancia global compartida por toda la sesión de UM STUDIO.
  static final DownloadQueueService instance = DownloadQueueService();

  /// Límite máximo de descargas activas simultáneas permitido hacia GitHub / compilador.
  static const int maxConcurrentDownloads = 20;

  /// Tope estricto de tamaño por archivo PDF: 1.2 MB = 1,258,291 bytes.
  static const int maxPdfSizeBytes = 1258291;

  static const String _localCachePrefix = 'um_studio_slide_pdf_v1_';
  static const int _maxPersistentEntryBytes = 360000;

  final int maxConcurrent;
  final http.Client _http;

  final Queue<_QueuedDownloadTask> _fifoQueue = Queue<_QueuedDownloadTask>();
  final Map<String, DownloadTaskSnapshot> _states = {};
  final Map<String, Uint8List> _sessionCache = {};
  final Map<String, Future<Uint8List>> _inFlightByTask = {};

  int _activeDownloads = 0;
  DateTime? _githubRateBackoffUntil;

  int get activeDownloads => _activeDownloads;
  int get queuedCount => _fifoQueue.length;

  /// Consulta el estado actual de un tema específico para actualizar la UI.
  DownloadTaskSnapshot stateFor(String taskId) {
    return _states[taskId] ??
        DownloadTaskSnapshot(
          taskId: taskId,
          phase: _sessionCache.containsKey(taskId)
              ? DownloadTaskPhase.completed
              : DownloadTaskPhase.idle,
          sizeBytes: _sessionCache[taskId]?.lengthInBytes,
          fromCache: _sessionCache.containsKey(taskId),
        );
  }

  /// Verifica si el PDF ya reside en la caché en memoria de la sesión.
  bool isCachedInSession(String taskId) => _sessionCache.containsKey(taskId);

  /// Obtiene los bytes desde la caché de sesión en 0 ms si existen.
  Uint8List? getCachedBytes(String taskId) => _sessionCache[taskId];

  /// Limpia la caché y reinicia los estados (útil al cerrar sesión o en tests).
  void clearSessionCache() {
    _sessionCache.clear();
    _states.clear();
    notifyListeners();
  }

  /// Solicita la descarga o compilación vectorial de un PDF respetando:
  /// 1. Entrega instantánea en **0 ms** si ya está en caché.
  /// 2. Límite de **20 slots concurrentes** con cola FIFO numerada (`#1`, `#2`, ...).
  /// 3. Verificación estricta `bytes.lengthInBytes <= 1258291` (`1.2 MB`).
  Future<Uint8List> enqueueDownload({
    required String taskId,
    required String fileName,
    required Future<Uint8List> Function() generator,
    String? remoteGitHubUrl,
    bool saveToPlatform = true,
  }) async {
    // 1. Hit instantáneo en 0 ms desde caché en memoria de la sesión
    final memCached = _sessionCache[taskId];
    if (memCached != null) {
      _validateSize(memCached);
      _states[taskId] = DownloadTaskSnapshot(
        taskId: taskId,
        phase: DownloadTaskPhase.completed,
        sizeBytes: memCached.lengthInBytes,
        fromCache: true,
      );
      notifyListeners();
      if (saveToPlatform) {
        await savePdfBytesToPlatform(fileName: fileName, bytes: memCached);
      }
      return memCached;
    }

    // Evita duplicar la misma tarea si el usuario pulsa varias veces seguidas
    final existingFlight = _inFlightByTask[taskId];
    if (existingFlight != null) {
      return existingFlight;
    }

    final completer = Completer<Uint8List>();
    _inFlightByTask[taskId] = completer.future;

    final task = _QueuedDownloadTask(
      taskId: taskId,
      fileName: fileName,
      generator: generator,
      remoteGitHubUrl: remoteGitHubUrl,
      saveToPlatform: saveToPlatform,
      completer: completer,
    );

    final underBackoff = _githubRateBackoffUntil != null &&
        DateTime.now().isBefore(_githubRateBackoffUntil!) &&
        remoteGitHubUrl != null;

    if (_activeDownloads < maxConcurrent && !underBackoff) {
      _startTask(task);
    } else {
      _fifoQueue.addLast(task);
      _refreshQueuePositions();
      notifyListeners();
    }

    try {
      return await completer.future;
    } finally {
      _inFlightByTask.remove(taskId);
    }
  }

  void _refreshQueuePositions() {
    var position = 1;
    for (final queued in _fifoQueue) {
      _states[queued.taskId] = DownloadTaskSnapshot(
        taskId: queued.taskId,
        phase: DownloadTaskPhase.queued,
        queuePosition: position,
      );
      position++;
    }
  }

  void _startTask(_QueuedDownloadTask task) {
    _activeDownloads++;
    _states[task.taskId] = DownloadTaskSnapshot(
      taskId: task.taskId,
      phase: DownloadTaskPhase.downloading,
    );
    notifyListeners();

    unawaited(_executeTask(task));
  }

  Future<void> _executeTask(_QueuedDownloadTask task) async {
    try {
      // Intenta primero caché local persistente (IndexedDB / SharedPreferences)
      Uint8List? bytes = await _readPersistentCache(task.taskId);
      var servedFromCache = bytes != null;

      // Si hay URL precomprimida en GitHub (`db/slides/...`) y no hay backoff activo
      if (bytes == null &&
          task.remoteGitHubUrl != null &&
          task.remoteGitHubUrl!.isNotEmpty) {
        bytes = await _tryFetchFromGitHub(task.remoteGitHubUrl!);
      }

      // Compilación vectorial en memoria con Deflate activo (`package:pdf`)
      bytes ??= await task.generator();

      // Validación estricta <= 1.2 MB (1,258,291 bytes)
      _validateSize(bytes);

      _states[task.taskId] = DownloadTaskSnapshot(
        taskId: task.taskId,
        phase: DownloadTaskPhase.downloading,
        sizeBytes: bytes.lengthInBytes,
        fromCache: servedFromCache,
      );
      notifyListeners();

      // Guarda en caché de sesión (0 ms para futuras descargas) y caché local
      _sessionCache[task.taskId] = bytes;
      if (!servedFromCache && bytes.lengthInBytes <= _maxPersistentEntryBytes) {
        unawaited(_writePersistentCache(task.taskId, bytes));
      }

      if (task.saveToPlatform) {
        await savePdfBytesToPlatform(
          fileName: task.fileName,
          bytes: bytes,
        );
      }

      _states[task.taskId] = DownloadTaskSnapshot(
        taskId: task.taskId,
        phase: DownloadTaskPhase.completed,
        sizeBytes: bytes.lengthInBytes,
        fromCache: servedFromCache,
      );
      if (!task.completer.isCompleted) {
        task.completer.complete(bytes);
      }
    } on PdfSizeLimitExceededException catch (e) {
      _states[task.taskId] = DownloadTaskSnapshot(
        taskId: task.taskId,
        phase: DownloadTaskPhase.error,
        errorMessage: '! Supera 1.2 MB',
      );
      if (!task.completer.isCompleted) {
        task.completer.completeError(e);
      }
    } catch (e) {
      _states[task.taskId] = DownloadTaskSnapshot(
        taskId: task.taskId,
        phase: DownloadTaskPhase.error,
        errorMessage: '! Error al exportar',
      );
      if (!task.completer.isCompleted) {
        task.completer.completeError(e);
      }
    } finally {
      _activeDownloads = (_activeDownloads - 1).clamp(0, maxConcurrent);
      _pumpQueue();
      notifyListeners();
    }
  }

  void _pumpQueue() {
    while (_activeDownloads < maxConcurrent && _fifoQueue.isNotEmpty) {
      final next = _fifoQueue.removeFirst();
      _refreshQueuePositions();
      _startTask(next);
    }
  }

  Future<Uint8List?> _tryFetchFromGitHub(String url) async {
    final stopwatch = Stopwatch()..start();
    try {
      final response = await _http
          .get(Uri.parse(url))
          .timeout(const Duration(seconds: 5));
      stopwatch.stop();

      if (response.statusCode == 429 || response.statusCode == 503) {
        _githubRateBackoffUntil =
            DateTime.now().add(const Duration(seconds: 10));
        return null;
      }

      if (stopwatch.elapsedMilliseconds > 3200) {
        _githubRateBackoffUntil =
            DateTime.now().add(const Duration(seconds: 4));
      }

      if (response.statusCode == 200 && response.bodyBytes.isNotEmpty) {
        return response.bodyBytes;
      }
    } catch (_) {
      // Fallback transparente al compilador PDF vectorial local.
    }
    return null;
  }

  static void _validateSize(Uint8List bytes) {
    if (bytes.lengthInBytes > maxPdfSizeBytes) {
      throw PdfSizeLimitExceededException(bytes.lengthInBytes);
    }
  }

  Future<Uint8List?> _readPersistentCache(String taskId) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final encoded = prefs.getString('$_localCachePrefix$taskId');
      if (encoded != null && encoded.isNotEmpty) {
        return base64Decode(encoded);
      }
    } catch (_) {}
    return null;
  }

  Future<void> _writePersistentCache(String taskId, Uint8List bytes) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('$_localCachePrefix$taskId', base64Encode(bytes));
    } catch (_) {}
  }
}
