import 'package:flutter/material.dart';

import '../../core/theme/app_theme.dart';

/// Resumen de asignatura para el listado de Estudio Extraclase.
class SubjectSummaryEntity {
  const SubjectSummaryEntity({
    required this.id,
    required this.category,
    required this.title,
    required this.nextTopic,
    required this.progress,
    required this.accentResolver,
    this.active = false,
  });

  final String id;
  final String category;
  final String title;
  final String nextTopic;
  final double progress;
  final Color Function(AppPalette p) accentResolver;
  final bool active;
}

enum AcademicEventKind { clase, bloque, entrega, parcial }

/// Evento del Calendario Académico sincronizado con AyRe / Moodle.
class AcademicEventEntity {
  const AcademicEventEntity({
    required this.time,
    required this.kind,
    required this.title,
    required this.subtitle,
    required this.days,
  });

  final String time;
  final AcademicEventKind kind;
  final String title;
  final String subtitle;
  final List<int> days;
}
