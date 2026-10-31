import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:yaml/yaml.dart';

import '../../core/constants/app_constants.dart';
import '../models/curriculum_models.dart';

/// Parser puro del archivo `ingenieria_energetica.md` con YAML Frontmatter.
abstract final class CurriculumMarkdownParser {
  /// Extrae el bloque YAML Frontmatter delimitado entre `---` y `---`
  /// y construye el modelo tipado [CurriculumDatabaseModel].
  static CurriculumDatabaseModel parse(String markdownSource) {
    final normalized = markdownSource
        .replaceAll('\r\n', '\n')
        .replaceFirst('\uFEFF', '')
        .trimLeft();

    if (!normalized.startsWith('---\n')) {
      throw const FormatException(
        'El archivo .md no contiene un encabezado YAML Frontmatter válido.',
      );
    }

    final closingIndex = normalized.indexOf('\n---', 4);
    if (closingIndex == -1) {
      throw const FormatException(
        'No se encontró el cierre `---` del YAML Frontmatter.',
      );
    }

    final yamlText = normalized.substring(4, closingIndex);
    final dynamic doc = loadYaml(yamlText);
    if (doc is! YamlMap) {
      throw const FormatException('El YAML Frontmatter no es un mapa válido.');
    }

    final root = _yamlMapToDart(doc);
    final programaMap = root['programa'] is Map<String, dynamic>
        ? root['programa'] as Map<String, dynamic>
        : const <String, dynamic>{};
    final programa = ProgramaInfoModel.fromMap(programaMap);

    final cuatrimestres = <CuatrimestreModel>[];
    final rawMalla = root['malla_curricular'];
    if (rawMalla is List) {
      for (final item in rawMalla) {
        if (item is Map<String, dynamic>) {
          final numCuat = (item['cuatrimestre'] is num)
              ? (item['cuatrimestre'] as num).toInt()
              : int.tryParse((item['cuatrimestre'] ?? '1').toString()) ?? 1;
          final creditosTot = (item['creditos_totales'] is num)
              ? (item['creditos_totales'] as num).toInt()
              : 0;

          final asignaturas = <AsignaturaModel>[];
          final rawAsig = item['asignaturas'];
          if (rawAsig is List) {
            for (final a in rawAsig) {
              if (a is Map<String, dynamic>) {
                asignaturas.add(
                  AsignaturaModel.fromMap(a, cuatrimestre: numCuat),
                );
              }
            }
          }

          cuatrimestres.add(
            CuatrimestreModel(
              numero: numCuat,
              creditosTotales: creditosTot,
              asignaturas: List.unmodifiable(asignaturas),
            ),
          );
        }
      }
    }

    return CurriculumDatabaseModel(
      programa: programa,
      cuatrimestres: List.unmodifiable(cuatrimestres),
    );
  }

  static Map<String, dynamic> _yamlMapToDart(YamlMap yamlMap) {
    final result = <String, dynamic>{};
    yamlMap.forEach((dynamic key, dynamic value) {
      result[key.toString()] = _convertYamlNode(value);
    });
    return result;
  }

  static dynamic _convertYamlNode(dynamic node) {
    if (node is YamlMap) {
      return _yamlMapToDart(node);
    }
    if (node is YamlList) {
      return node.map(_convertYamlNode).toList(growable: false);
    }
    return node;
  }
}

/// Servicio reactivo Offline-First para la malla curricular de Ingeniería Energética.
///
/// 1. Carga instantáneamente `assets/data/ingenieria_energetica.md` al iniciar.
/// 2. Intenta actualizar en segundo plano desde `raw.githubusercontent.com`
///    (`db/ingenieria_energetica.md`) para reflejar nuevos temarios o fórmulas
///    KaTeX sin reinstalar la aplicación.
class MarkdownCurriculumService extends ChangeNotifier {
  MarkdownCurriculumService({http.Client? httpClient})
      : _http = httpClient ?? http.Client();

  static const String _cachedMdKey = 'um_studio_cached_curriculum_md_v4';

  final http.Client _http;

  CurriculumDatabaseModel? _database;
  bool _loaded = false;
  bool _syncedFromGitHub = false;

  CurriculumDatabaseModel? get database => _database;
  bool get isLoaded => _loaded;
  bool get isSyncedFromGitHub => _syncedFromGitHub;

  List<AsignaturaModel> get allAsignaturas =>
      _database?.allAsignaturas ?? const [];

  List<CuatrimestreModel> get cuatrimestres =>
      _database?.cuatrimestres ?? const [];

  ProgramaInfoModel get programa =>
      _database?.programa ?? ProgramaInfoModel.fallback;

  static int _countTopics(CurriculumDatabaseModel? db) {
    if (db == null) return 0;
    var count = 0;
    for (final a in db.allAsignaturas) {
      count += a.temas.length;
    }
    return count;
  }

  /// Carga inmediata desde el bundle local (o caché remoto previo) y lanza
  /// refresco silencioso desde GitHub.
  Future<void> initialize({bool refreshRemote = true}) async {
    try {
      final assetMd = await rootBundle.loadString(
        AppConstants.curriculumAssetPath,
      );
      _database = CurriculumMarkdownParser.parse(assetMd);
      _loaded = true;
      notifyListeners();
    } catch (_) {
      // Si en un test unitario aislado no se cargó el asset aún, intenta caché.
    }

    try {
      final prefs = await SharedPreferences.getInstance();
      final cachedRemote = prefs.getString(_cachedMdKey);
      if (cachedRemote != null && cachedRemote.isNotEmpty) {
        final parsedCached = CurriculumMarkdownParser.parse(cachedRemote);
        if (parsedCached.allAsignaturas.length >=
                (_database?.allAsignaturas.length ?? 0) &&
            _countTopics(parsedCached) >= _countTopics(_database)) {
          _database = parsedCached;
          _loaded = true;
          notifyListeners();
        }
      }
    } catch (_) {}

    if (refreshRemote) {
      unawaited(refreshFromGitHub());
    }
  }

  /// Descarga `db/ingenieria_energetica.md` desde el raw público de GitHub.
  Future<bool> refreshFromGitHub() async {
    try {
      final uri = Uri.parse(AppConstants.curriculumRawUrl);
      final response = await _http
          .get(uri)
          .timeout(const Duration(seconds: 6));

      if (response.statusCode == 200 && response.body.trim().isNotEmpty) {
        final parsed = CurriculumMarkdownParser.parse(response.body);
        if (parsed.allAsignaturas.isNotEmpty &&
            _countTopics(parsed) >= _countTopics(_database)) {
          _database = parsed;
          _loaded = true;
          _syncedFromGitHub = true;
          notifyListeners();

          final prefs = await SharedPreferences.getInstance();
          await prefs.setString(_cachedMdKey, response.body);
          return true;
        }
      }
    } catch (_) {
      // Silencioso en modo offline: conserva la versión local de `assets/`.
    }
    return false;
  }

  /// Permite inyectar una base de datos parseada manualmente (útil en tests).
  void seedDatabase(CurriculumDatabaseModel db) {
    _database = db;
    _loaded = true;
    notifyListeners();
  }
}
