import 'package:flutter/material.dart';

import 'tema_estudio_model.dart';

/// Información oficial del programa extraída del YAML Frontmatter.
class ProgramaInfoModel {
  const ProgramaInfoModel({
    required this.codigoInterno,
    required this.codigoSnies,
    required this.nombre,
    required this.facultad,
    required this.universidad,
    required this.totalCuatrimestres,
    required this.totalAsignaturas,
    required this.totalCreditos,
    required this.normatividad,
  });

  final String codigoInterno;
  final String codigoSnies;
  final String nombre;
  final String facultad;
  final String universidad;
  final int totalCuatrimestres;
  final int totalAsignaturas;
  final int totalCreditos;
  final String normatividad;

  static const fallback = ProgramaInfoModel(
    codigoInterno: '8108',
    codigoSnies: '118222',
    nombre: 'Ingeniería Energética',
    facultad: 'Facultad de Ingeniería',
    universidad: 'Universidad del Magdalena',
    totalCuatrimestres: 12,
    totalAsignaturas: 56,
    totalCreditos: 162,
    normatividad: 'Acuerdo Académico N° 038 de 2024',
  );

  factory ProgramaInfoModel.fromMap(Map<String, dynamic> map) {
    return ProgramaInfoModel(
      codigoInterno: (map['codigo_interno'] ?? '8108').toString(),
      codigoSnies: (map['codigo_snies'] ?? '118222').toString(),
      nombre: (map['nombre'] ?? 'Ingeniería Energética').toString(),
      facultad: (map['facultad'] ?? 'Facultad de Ingeniería').toString(),
      universidad:
          (map['universidad'] ?? 'Universidad del Magdalena').toString(),
      totalCuatrimestres: _parseInt(map['total_cuatrimestres'], 12),
      totalAsignaturas: _parseInt(map['total_asignaturas'], 56),
      totalCreditos: _parseInt(map['total_creditos'], 162),
      normatividad:
          (map['normatividad'] ?? 'Acuerdo Académico N° 038 de 2024')
              .toString(),
    );
  }
}

/// Modelo tipado de cada tema de "La Clase Viva" dentro de una asignatura.
class TemaClaseVivaModel {
  const TemaClaseVivaModel({
    required this.numeroTema,
    required this.titulo,
    required this.objetivo,
    required this.conceptoClaveLatex,
    required this.ejemplo,
    required this.bloqueSugerido,
  });

  final int numeroTema;
  final String titulo;
  final String objetivo;
  final String conceptoClaveLatex;
  final String ejemplo;
  final String bloqueSugerido;

  factory TemaClaseVivaModel.fromMap(Map<String, dynamic> map) {
    return TemaClaseVivaModel(
      numeroTema: _parseInt(map['numero_tema'] ?? map['numero'], 1),
      titulo: (map['titulo'] ?? 'Tema de Cátedra').toString(),
      objetivo: (map['objetivo'] ?? '').toString(),
      conceptoClaveLatex: (map['concepto_clave_latex'] ?? '').toString(),
      ejemplo: (map['ejemplo'] ?? '').toString(),
      bloqueSugerido:
          (map['bloque_sugerido'] ?? map['bloque_estudio'] ?? 'Pomodoro 50/10')
              .toString(),
    );
  }

  /// Convierte el tema tipado al DTO `TemaEstudioModel` para `ClaseVivaPage`.
  TemaEstudioModel toTemaEstudioModel({
    required String codigoAsignatura,
    required String nombreAsignatura,
    required int cuatrimestre,
    required int creditos,
  }) {
    final topicKey = numeroTema <= 1
        ? codigoAsignatura
        : '${codigoAsignatura}_t$numeroTema';
    return TemaEstudioModel(
      id: topicKey,
      nombreAsignatura: nombreAsignatura,
      numeroTema: numeroTema,
      tituloTema: titulo,
      objetivo: objetivo,
      conceptoClaveLatex: conceptoClaveLatex,
      ejemplo: ejemplo,
      bloqueSugerido: bloqueSugerido,
      codigoAsignatura: codigoAsignatura,
      cuatrimestre: cuatrimestre,
      creditos: creditos,
      sincronizacionPorcentaje: 96,
    );
  }
}

/// Modelo tipado de una asignatura oficial de Ingeniería Energética (Plan 8108).
class AsignaturaModel {
  const AsignaturaModel({
    required this.codigo,
    required this.nombre,
    required this.cuatrimestre,
    required this.creditos,
    required this.obligatoria,
    required this.categoria,
    required this.colorHex,
    required this.temas,
  });

  final String codigo;
  final String nombre;
  final int cuatrimestre;
  final int creditos;
  final bool obligatoria;
  final String categoria;
  final String colorHex;
  final List<TemaClaseVivaModel> temas;

  Color get accentColor => parseHexColor(colorHex);

  String get categoriaLegible {
    switch (categoria.toUpperCase()) {
      case 'MATEMATICAS':
        return 'Matemáticas';
      case 'FISICA_QUIMICA':
        return 'Física y Química';
      case 'INGENIERIA_ENERGIA':
        return 'Ing. Energética';
      case 'PROGRAMACION_IA':
        return 'Programación e IA';
      case 'PROYECTOS_GESTION':
        return 'Proyectos CDIO';
      case 'FORMACION_GENERAL':
        return 'Formación General';
      default:
        return categoria;
    }
  }

  TemaClaseVivaModel get primerTema => temas.isNotEmpty
      ? temas.first
      : const TemaClaseVivaModel(
          numeroTema: 1,
          titulo: 'Introducción a la Asignatura',
          objetivo: 'Comprender los fundamentos teóricos y prácticos.',
          conceptoClaveLatex: r'E = m \cdot c^2',
          ejemplo: 'Aplicación en sistemas energéticos.',
          bloqueSugerido: 'Pomodoro 50/10',
        );

  factory AsignaturaModel.fromMap(
    Map<String, dynamic> map, {
    required int cuatrimestre,
  }) {
    final rawTemas = map['temas'];
    final parsedTemas = <TemaClaseVivaModel>[];
    if (rawTemas is Iterable) {
      for (final item in rawTemas) {
        if (item is Map) {
          parsedTemas.add(
            TemaClaseVivaModel.fromMap(
              item.map((k, v) => MapEntry(k.toString(), v)),
            ),
          );
        }
      }
    }

    return AsignaturaModel(
      codigo: (map['codigo'] ?? '').toString(),
      nombre: (map['nombre'] ?? '').toString(),
      cuatrimestre: _parseInt(map['cuatrimestre'], cuatrimestre),
      creditos: _parseInt(map['creditos'], 3),
      obligatoria: map['obligatoria'] != false,
      categoria: (map['categoria'] ?? 'INGENIERIA_ENERGIA').toString(),
      colorHex:
          (map['color_acento'] ?? map['color'] ?? '#30D158').toString(),
      temas: parsedTemas,
    );
  }

  static Color parseHexColor(String hex) {
    final cleaned = hex.trim().replaceFirst('#', '');
    if (cleaned.length == 6) {
      final value = int.tryParse('FF$cleaned', radix: 16);
      if (value != null) return Color(value);
    } else if (cleaned.length == 8) {
      final value = int.tryParse(cleaned, radix: 16);
      if (value != null) return Color(value);
    }
    return const Color(0xFF30D158);
  }
}

/// Agrupación curricular por cuatrimestre (`1..12`).
class CuatrimestreModel {
  const CuatrimestreModel({
    required this.numero,
    required this.creditosTotales,
    required this.asignaturas,
  });

  final int numero;
  final int creditosTotales;
  final List<AsignaturaModel> asignaturas;
}

/// Base de datos completa en memoria de la malla curricular Plan 8108.
class CurriculumDatabaseModel {
  CurriculumDatabaseModel({
    required this.programa,
    required this.cuatrimestres,
  }) : allAsignaturas = List.unmodifiable(
          cuatrimestres.expand((c) => c.asignaturas),
        ) {
    for (final a in allAsignaturas) {
      _byCodigo[a.codigo] = a;
    }
  }

  final ProgramaInfoModel programa;
  final List<CuatrimestreModel> cuatrimestres;
  final List<AsignaturaModel> allAsignaturas;
  final Map<String, AsignaturaModel> _byCodigo = {};

  /// Alias de compatibilidad rápida para identificadores cortos.
  static const Map<String, String> _legacyAliases = {
    'fisica': '02021810',
    'calculo': '02011808',
    'calculo_dif': '02011807',
    'electricidad': '03041819',
    'algebra': '02011809',
    'termodinamica': '03021817',
  };

  /// Resuelve una asignatura por su código oficial (`02021810`), clave de tema
  /// compuesto (`02021810_t2`) o alias corto (`fisica`).
  AsignaturaModel? findAsignatura(String idOrCode) {
    final clean = idOrCode.trim();
    if (_byCodigo.containsKey(clean)) return _byCodigo[clean];

    final aliased = _legacyAliases[clean.toLowerCase()];
    if (aliased != null && _byCodigo.containsKey(aliased)) {
      return _byCodigo[aliased];
    }

    if (clean.contains('_t')) {
      final baseCode = clean.split('_t').first;
      if (_byCodigo.containsKey(baseCode)) return _byCodigo[baseCode];
    }
    return null;
  }

  /// Resuelve un `TemaEstudioModel` específico (ej. `02021810` o `02021810_t2`).
  TemaEstudioModel? resolveTemaEstudio(String temaKey) {
    final asignatura = findAsignatura(temaKey);
    if (asignatura == null) return null;

    var topicNumber = 1;
    if (temaKey.contains('_t')) {
      topicNumber = int.tryParse(temaKey.split('_t').last) ?? 1;
    }

    TemaClaseVivaModel selected = asignatura.primerTema;
    for (final t in asignatura.temas) {
      if (t.numeroTema == topicNumber) {
        selected = t;
        break;
      }
    }

    return selected.toTemaEstudioModel(
      codigoAsignatura: asignatura.codigo,
      nombreAsignatura: asignatura.nombre,
      cuatrimestre: asignatura.cuatrimestre,
      creditos: asignatura.creditos,
    );
  }

  List<AsignaturaModel> byCuatrimestre(int cuatrimestre) {
    for (final c in cuatrimestres) {
      if (c.numero == cuatrimestre) return c.asignaturas;
    }
    return const [];
  }
}

int _parseInt(Object? raw, int fallback) {
  if (raw is int) return raw;
  if (raw is num) return raw.toInt();
  if (raw != null) return int.tryParse(raw.toString()) ?? fallback;
  return fallback;
}
