import 'dart:convert';

import '../../core/constants/app_constants.dart';
import '../../domain/entities/subject_summary.dart';

/// Cupo diario personal del estudiante en `db/users/{username}.json`.
class DailyUsageModel {
  const DailyUsageModel({
    required this.actual,
    required this.maximo,
    required this.ultimaFecha,
  });

  final int actual;
  final int maximo;
  final String ultimaFecha;

  static String todayIso([DateTime? now]) {
    final d = now ?? DateTime.now();
    final m = d.month.toString().padLeft(2, '0');
    final day = d.day.toString().padLeft(2, '0');
    return '${d.year}-$m-$day';
  }

  factory DailyUsageModel.initial([DateTime? now]) {
    return DailyUsageModel(
      actual: AppConstants.initialDailyUsage,
      maximo: AppConstants.maxDailyUsage,
      ultimaFecha: todayIso(now),
    );
  }

  factory DailyUsageModel.fromJson(Map<String, dynamic> json) {
    return DailyUsageModel(
      actual: (json['actual'] is num)
          ? (json['actual'] as num).toInt()
          : AppConstants.initialDailyUsage,
      maximo: (json['maximo'] is num)
          ? (json['maximo'] as num).toInt()
          : AppConstants.maxDailyUsage,
      ultimaFecha: (json['ultima_fecha'] ?? todayIso()).toString(),
    );
  }

  DailyUsageModel copyWith({
    int? actual,
    int? maximo,
    String? ultimaFecha,
  }) {
    return DailyUsageModel(
      actual: actual ?? this.actual,
      maximo: maximo ?? this.maximo,
      ultimaFecha: ultimaFecha ?? this.ultimaFecha,
    );
  }

  Map<String, dynamic> toJson() => {
        'actual': actual,
        'maximo': maximo,
        'ultima_fecha': ultimaFecha,
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
          (json['fecha'] ?? json['fecha_iso'] ?? DailyUsageModel.todayIso())
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
    required this.usoDiario,
    required this.progresoMaterias,
    required this.recordatoriosCalendario,
    required this.apuntesPersonales,
    this.cuatrimestreActual = 2,
  });

  final String username;
  final String nombre;
  final String email;
  final String programa;
  final String pinHash;
  final DailyUsageModel usoDiario;
  final Map<String, int> progresoMaterias;
  final List<CalendarReminderModel> recordatoriosCalendario;
  final Map<String, dynamic> apuntesPersonales;
  final int cuatrimestreActual;

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
      starterProgress[starterSubjectCodes[i]] = i == 0 ? 50 : (i == 1 ? 60 : 35);
    }

    return StudentUserModel(
      username: username,
      nombre: nombre.trim(),
      email: email.trim().toLowerCase(),
      programa: AppConstants.programName,
      pinHash: pinHash,
      cuatrimestreActual: cuatrimestreActual.clamp(1, 12),
      usoDiario: DailyUsageModel.initial(),
      progresoMaterias: starterProgress,
      recordatoriosCalendario: const [],
      apuntesPersonales: const {},
    );
  }

  factory StudentUserModel.fromJson(Map<String, dynamic> json) {
    final rawUso = json['uso_diario'];
    final uso = rawUso is Map
        ? DailyUsageModel.fromJson(
            rawUso.map((k, v) => MapEntry(k.toString(), v)),
          )
        : DailyUsageModel.initial();

    final progress = <String, int>{};
    final rawProg = json['progreso_materias'];
    if (rawProg is Map) {
      rawProg.forEach((k, v) {
        final pct = v is num ? v.toInt() : int.tryParse(v.toString()) ?? 0;
        progress[k.toString()] = pct.clamp(0, 100);
      });
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
      usoDiario: uso,
      progresoMaterias: progress,
      recordatoriosCalendario: reminders,
      apuntesPersonales: notes,
    );
  }

  StudentUserModel copyWith({
    String? username,
    String? nombre,
    String? email,
    String? programa,
    String? pinHash,
    DailyUsageModel? usoDiario,
    Map<String, int>? progresoMaterias,
    List<CalendarReminderModel>? recordatoriosCalendario,
    Map<String, dynamic>? apuntesPersonales,
    int? cuatrimestreActual,
  }) {
    return StudentUserModel(
      username: username ?? this.username,
      nombre: nombre ?? this.nombre,
      email: email ?? this.email,
      programa: programa ?? this.programa,
      pinHash: pinHash ?? this.pinHash,
      usoDiario: usoDiario ?? this.usoDiario,
      progresoMaterias: progresoMaterias ?? this.progresoMaterias,
      recordatoriosCalendario:
          recordatoriosCalendario ?? this.recordatoriosCalendario,
      apuntesPersonales: apuntesPersonales ?? this.apuntesPersonales,
      cuatrimestreActual: cuatrimestreActual ?? this.cuatrimestreActual,
    );
  }

  Map<String, dynamic> toJson() => {
        'username': username,
        'nombre': nombre,
        'email': email,
        'programa': programa,
        'cuatrimestre_actual': cuatrimestreActual,
        'pin_hash': pinHash,
        'uso_diario': usoDiario.toJson(),
        'progreso_materias': progresoMaterias,
        'recordatorios_calendario':
            recordatoriosCalendario.map((r) => r.toJson()).toList(),
        'apuntes_personales': apuntesPersonales,
      };

  String toPrettyJsonString() =>
      const JsonEncoder.withIndent('  ').convert(toJson());
}
