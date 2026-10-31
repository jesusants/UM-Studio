import 'dart:convert';

import '../../core/constants/app_constants.dart';
import '../../domain/entities/subject_summary.dart';

/// Utilidad de fecha ISO local `YYYY-MM-DD`.
abstract final class IsoDateHelper {
  static String todayIso([DateTime? now]) {
    final d = now ?? DateTime.now();
    final m = d.month.toString().padLeft(2, '0');
    final day = d.day.toString().padLeft(2, '0');
    return '${d.year}-$m-$day';
  }
}

/// Registro global del último tema revisado por el estudiante.
class LastReviewedTopicModel {
  const LastReviewedTopicModel({
    required this.codigoMateria,
    required this.numeroTema,
    required this.actualizadoEn,
  });

  final String codigoMateria;
  final int numeroTema;
  final String actualizadoEn;

  String get temaKey =>
      numeroTema <= 1 ? codigoMateria : '${codigoMateria}_t$numeroTema';

  factory LastReviewedTopicModel.fromJson(Map<String, dynamic> json) {
    final rawNum = json['numero_tema'] ?? 1;
    return LastReviewedTopicModel(
      codigoMateria: (json['codigo_materia'] ?? '').toString(),
      numeroTema: rawNum is num
          ? rawNum.toInt()
          : int.tryParse(rawNum.toString()) ?? 1,
      actualizadoEn:
          (json['actualizado_en'] ?? DateTime.now().toIso8601String())
              .toString(),
    );
  }

  Map<String, dynamic> toJson() => {
        'codigo_materia': codigoMateria,
        'numero_tema': numeroTema,
        'actualizado_en': actualizadoEn,
      };
}

/// Recordatorio, parcial, entrega o bloque personal del estudiante.
class CalendarReminderModel {
  const CalendarReminderModel({
    required this.id,
    required this.titulo,
    required this.subtitulo,
    required this.fechaIso,
    required this.hora,
    required this.tipo,
    this.codigoMateria,
    this.completado = false,
  });

  final String id;
  final String titulo;
  final String subtitulo;

  /// Fecha en formato `YYYY-MM-DD`.
  final String fechaIso;

  /// Hora en formato `HH:MM` (24h).
  final String hora;
  final AcademicEventKind tipo;
  final String? codigoMateria;
  final bool completado;

  DateTime get parsedDate {
    return DateTime.tryParse(fechaIso) ?? DateTime.now();
  }

  String get tipoDb {
    switch (tipo) {
      case AcademicEventKind.parcial:
        return 'parcial';
      case AcademicEventKind.clase:
        return 'clase';
      case AcademicEventKind.bloque:
        return 'bloque';
      case AcademicEventKind.entrega:
        return 'entrega';
    }
  }

  static AcademicEventKind parseTipo(String raw) {
    switch (raw.trim().toLowerCase()) {
      case 'parcial':
        return AcademicEventKind.parcial;
      case 'clase':
        return AcademicEventKind.clase;
      case 'entrega':
        return AcademicEventKind.entrega;
      case 'bloque':
      default:
        return AcademicEventKind.bloque;
    }
  }

  factory CalendarReminderModel.fromJson(Map<String, dynamic> json) {
    return CalendarReminderModel(
      id: (json['id'] ?? 'rem_${DateTime.now().microsecondsSinceEpoch}')
          .toString(),
      titulo: (json['titulo'] ?? 'Recordatorio académico').toString(),
      subtitulo: (json['subtitulo'] ?? '').toString(),
      fechaIso:
          (json['fecha'] ?? json['fecha_iso'] ?? IsoDateHelper.todayIso())
              .toString(),
      hora: (json['hora'] ?? '10:00').toString(),
      tipo: parseTipo((json['tipo'] ?? 'bloque').toString()),
      codigoMateria: json['codigo_materia']?.toString(),
      completado: json['completado'] == true,
    );
  }

  CalendarReminderModel copyWith({
    String? id,
    String? titulo,
    String? subtitulo,
    String? fechaIso,
    String? hora,
    AcademicEventKind? tipo,
    String? codigoMateria,
    bool? completado,
  }) {
    return CalendarReminderModel(
      id: id ?? this.id,
      titulo: titulo ?? this.titulo,
      subtitulo: subtitulo ?? this.subtitulo,
      fechaIso: fechaIso ?? this.fechaIso,
      hora: hora ?? this.hora,
      tipo: tipo ?? this.tipo,
      codigoMateria: codigoMateria ?? this.codigoMateria,
      completado: completado ?? this.completado,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'titulo': titulo,
        'subtitulo': subtitulo,
        'fecha': fechaIso,
        'hora': hora,
        'tipo': tipoDb,
        if (codigoMateria != null && codigoMateria!.isNotEmpty)
          'codigo_materia': codigoMateria,
        'completado': completado,
      };
}

/// Documento JSON individual por estudiante en `db/users/{username}.json`.
class StudentUserModel {
  const StudentUserModel({
    required this.username,
    required this.nombre,
    required this.email,
    required this.programa,
    required this.pinHash,
    required this.progresoMaterias,
    required this.recordatoriosCalendario,
    required this.apuntesPersonales,
    this.ultimosTemasRevisados = const {},
    this.ultimoRevisado,
    this.cuatrimestreActual = 2,
    this.oid,
    this.tid,
  });

  final String username;
  final String nombre;
  final String email;
  final String programa;
  final String pinHash;
  final Map<String, int> progresoMaterias;
  final List<CalendarReminderModel> recordatoriosCalendario;
  final Map<String, dynamic> apuntesPersonales;

  /// Mapa `{ codigo_materia: numero_tema }` con el último tema revisado en cada asignatura.
  final Map<String, int> ultimosTemasRevisados;

  /// Último tema revisado globalmente por el estudiante.
  final LastReviewedTopicModel? ultimoRevisado;

  final int cuatrimestreActual;
  final String? oid;
  final String? tid;

  /// Clave inmutable única del estudiante (${tid}_${oid} o fallback a oid/username).
  String get immutableKey {
    final t = tid;
    final o = oid;
    if (t != null && t.isNotEmpty && o != null && o.isNotEmpty) {
      return '${t}_$o';
    }
    return o ?? username;
  }

  String get primerNombre {
    final parts = nombre.trim().split(RegExp(r'\s+'));
    return parts.isNotEmpty && parts.first.isNotEmpty ? parts.first : username;
  }

  String get iniciales {
    final parts =
        nombre.trim().split(RegExp(r'\s+')).where((s) => s.isNotEmpty).toList();
    if (parts.length >= 2) {
      return '${parts[0][0]}${parts[1][0]}'.toUpperCase();
    }
    if (parts.length == 1 && parts[0].length >= 2) {
      return parts[0].substring(0, 2).toUpperCase();
    }
    return 'UM';
  }

  factory StudentUserModel.createNew({
    required String username,
    required String nombre,
    required String email,
    required String pinHash,
    int cuatrimestreActual = 2,
    List<String> starterSubjectCodes = const ['02021810', '03041819'],
  }) {
    final starterProgress = <String, int>{};
    for (var i = 0; i < starterSubjectCodes.length; i++) {
      starterProgress[starterSubjectCodes[i]] =
          i == 0 ? 50 : (i == 1 ? 60 : 35);
    }

    return StudentUserModel(
      username: username,
      nombre: nombre.trim(),
      email: email.trim().toLowerCase(),
      programa: AppConstants.programName,
      pinHash: pinHash,
      cuatrimestreActual: cuatrimestreActual.clamp(1, 12),
      progresoMaterias: starterProgress,
      recordatoriosCalendario: const [],
      apuntesPersonales: const {},
      ultimosTemasRevisados: const {},
    );
  }

  factory StudentUserModel.fromJson(Map<String, dynamic> json) {
    final progress = <String, int>{};
    final rawProg = json['progreso_materias'];
    if (rawProg is Map) {
      rawProg.forEach((k, v) {
        final pct = v is num ? v.toInt() : int.tryParse(v.toString()) ?? 0;
        progress[k.toString()] = pct.clamp(0, 100);
      });
    }

    final reviewedMap = <String, int>{};
    final rawReviewed = json['ultimos_temas_revisados'];
    if (rawReviewed is Map) {
      rawReviewed.forEach((k, v) {
        final tNum = v is num ? v.toInt() : int.tryParse(v.toString()) ?? 1;
        if (tNum >= 1) {
          reviewedMap[k.toString()] = tNum;
        }
      });
    }

    LastReviewedTopicModel? globalLast;
    final rawLast = json['ultimo_revisado'];
    if (rawLast is Map) {
      final parsed = LastReviewedTopicModel.fromJson(
        rawLast.map((k, v) => MapEntry(k.toString(), v)),
      );
      if (parsed.codigoMateria.isNotEmpty) {
        globalLast = parsed;
      }
    }

    final reminders = <CalendarReminderModel>[];
    final rawRem = json['recordatorios_calendario'];
    if (rawRem is Iterable) {
      for (final item in rawRem) {
        if (item is Map) {
          reminders.add(
            CalendarReminderModel.fromJson(
              item.map((k, v) => MapEntry(k.toString(), v)),
            ),
          );
        }
      }
    }

    final notes = <String, dynamic>{};
    final rawNotes = json['apuntes_personales'];
    if (rawNotes is Map) {
      rawNotes.forEach((k, v) {
        notes[k.toString()] = v;
      });
    }

    final username = (json['username'] ?? '').toString().trim().toLowerCase();
    final email = (json['email'] ??
            (username.isNotEmpty
                ? '$username${AppConstants.institutionalDomain}'
                : AppConstants.defaultStudentEmail))
        .toString();

    return StudentUserModel(
      username: username.isNotEmpty ? username : email.split('@').first,
      nombre: (json['nombre'] ?? username).toString(),
      email: email,
      programa: (json['programa'] ?? AppConstants.programName).toString(),
      pinHash: (json['pin_hash'] ?? '').toString(),
      cuatrimestreActual: (json['cuatrimestre_actual'] is num)
          ? (json['cuatrimestre_actual'] as num).toInt().clamp(1, 12)
          : 2,
      progresoMaterias: progress,
      recordatoriosCalendario: reminders,
      apuntesPersonales: notes,
      ultimosTemasRevisados: reviewedMap,
      ultimoRevisado: globalLast,
      oid: json['oid']?.toString(),
      tid: json['tid']?.toString(),
    );
  }

  StudentUserModel copyWith({
    String? username,
    String? nombre,
    String? email,
    String? programa,
    String? pinHash,
    Map<String, int>? progresoMaterias,
    List<CalendarReminderModel>? recordatoriosCalendario,
    Map<String, dynamic>? apuntesPersonales,
    Map<String, int>? ultimosTemasRevisados,
    LastReviewedTopicModel? ultimoRevisado,
    int? cuatrimestreActual,
    String? oid,
    String? tid,
  }) {
    return StudentUserModel(
      username: username ?? this.username,
      nombre: nombre ?? this.nombre,
      email: email ?? this.email,
      programa: programa ?? this.programa,
      pinHash: pinHash ?? this.pinHash,
      progresoMaterias: progresoMaterias ?? this.progresoMaterias,
      recordatoriosCalendario:
          recordatoriosCalendario ?? this.recordatoriosCalendario,
      apuntesPersonales: apuntesPersonales ?? this.apuntesPersonales,
      ultimosTemasRevisados:
          ultimosTemasRevisados ?? this.ultimosTemasRevisados,
      ultimoRevisado: ultimoRevisado ?? this.ultimoRevisado,
      cuatrimestreActual: cuatrimestreActual ?? this.cuatrimestreActual,
      oid: oid ?? this.oid,
      tid: tid ?? this.tid,
    );
  }

  Map<String, dynamic> toJson() => {
        'username': username,
        'nombre': nombre,
        'email': email,
        'programa': programa,
        'cuatrimestre_actual': cuatrimestreActual,
        'pin_hash': pinHash,
        'progreso_materias': progresoMaterias,
        'ultimos_temas_revisados': ultimosTemasRevisados,
        if (ultimoRevisado != null)
          'ultimo_revisado': ultimoRevisado!.toJson(),
        if (oid != null && oid!.isNotEmpty) 'oid': oid,
        if (tid != null && tid!.isNotEmpty) 'tid': tid,
        'recordatorios_calendario':
            recordatoriosCalendario.map((r) => r.toJson()).toList(),
        'apuntes_personales': apuntesPersonales,
      };

  String toPrettyJsonString() =>
      const JsonEncoder.withIndent('  ').convert(toJson());
}
