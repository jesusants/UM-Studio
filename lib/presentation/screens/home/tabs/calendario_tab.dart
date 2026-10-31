import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/datasources/academic_seed_data.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../widgets/ios_primitives.dart';

const _days = [
  ('L', 26),
  ('M', 27),
  ('M', 28),
  ('J', 29),
  ('V', 30),
  ('S', 31),
];

const _filters = ['Todo', 'Parciales', 'Clases', 'Entregas Moodle'];

/// Pestaña 2: "Calendario Académico".
class CalendarioTab extends StatefulWidget {
  const CalendarioTab({super.key});

  @override
  State<CalendarioTab> createState() => _CalendarioTabState();
}

class _CalendarioTabState extends State<CalendarioTab> {
  int _selectedDay = 30;
  String _filter = 'Todo';

  bool _matches(AcademicEventEntity e) {
    if (!e.days.contains(_selectedDay)) return false;
    switch (_filter) {
      case 'Clases':
        return e.kind == AcademicEventKind.clase;
      case 'Entregas Moodle':
        return e.kind == AcademicEventKind.entrega;
      case 'Parciales':
        return e.kind == AcademicEventKind.parcial;
      default:
        return true;
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final visible = AcademicSeedData.calendarEvents.where(_matches).toList();

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
      children: [
        Text(
          'Calendario Académico',
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.w700,
            letterSpacing: -0.4,
            color: p.textPrimary,
          ),
        ),
        const SizedBox(height: 16),

        Row(
          children: [
            for (var i = 0; i < _days.length; i++) ...[
              if (i > 0) const SizedBox(width: 8),
              Expanded(child: _dayButton(p, _days[i].$1, _days[i].$2)),
            ],
          ],
        ),
        const SizedBox(height: 16),

        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: Row(
            children: [
              for (final f in _filters)
                Padding(
                  padding: const EdgeInsets.only(right: 8),
                  child: _chip(p, f),
                ),
            ],
          ),
        ),
        const SizedBox(height: 16),

        if (visible.isEmpty)
          IosCard(
            child: Text(
              'No hay ${_filter.toLowerCase()} programados para el día $_selectedDay.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 12, color: p.textSecondary),
            ),
          )
        else
          for (final e in visible) ...[
            _eventRow(p, e),
            const SizedBox(height: 12),
          ],
      ],
    );
  }

  Widget _dayButton(AppPalette p, String label, int day) {
    final selected = day == _selectedDay;
    final highlight = day == 31;

    final Color bg = selected ? p.inverse : p.card;
    final Color? border = selected
        ? null
        : (highlight ? p.orange.o(0.5) : p.cardBorder);
    final Color labelColor = selected
        ? p.onInverse
        : (highlight ? p.orange : p.textSecondary);
    final Color numberColor = selected
        ? p.onInverse
        : (highlight ? p.orange : p.textPrimary);

    return TapScale(
      onTap: () => setState(() => _selectedDay = day),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 220),
        curve: kIosSpring,
        padding: const EdgeInsets.symmetric(vertical: 8),
        decoration: BoxDecoration(
          color: bg,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: border ?? bg),
        ),
        child: Column(
          children: [
            Text(label, style: TextStyle(fontSize: 10, color: labelColor)),
            const SizedBox(height: 2),
            Text(
              '$day',
              style: TextStyle(
                fontSize: 12,
                fontWeight: selected ? FontWeight.w700 : FontWeight.w600,
                color: numberColor,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _chip(AppPalette p, String label) {
    final selected = label == _filter;
    return TapScale(
      onTap: () => setState(() => _filter = label),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 220),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
        decoration: BoxDecoration(
          color: selected ? p.inverse : p.card,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(color: selected ? p.inverse : p.cardBorder),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 12,
            fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
            color: selected ? p.onInverse : p.textSecondary,
          ),
        ),
      ),
    );
  }

  Widget _eventRow(AppPalette p, AcademicEventEntity e) {
    late final String kindLabel;
    late final Color kindColor;
    Color? border;
    switch (e.kind) {
      case AcademicEventKind.clase:
        kindLabel = 'CLASE MAGISTRAL';
        kindColor = p.green;
      case AcademicEventKind.bloque:
        kindLabel = 'BLOQUE PROGRAMADO';
        kindColor = p.indigo;
        border = p.indigo.o(0.5);
      case AcademicEventKind.entrega:
        kindLabel = 'ENTREGA CAMPUS VIRTUAL';
        kindColor = p.orange;
        border = p.orange.o(0.5);
      case AcademicEventKind.parcial:
        kindLabel = 'EVALUACIÓN PARCIAL';
        kindColor = p.orange;
        border = p.orange.o(0.6);
    }

    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(
          width: 48,
          child: Padding(
            padding: const EdgeInsets.only(top: 8),
            child: Text(
              e.time,
              style: mono(
                fontSize: 12,
                color: e.kind == AcademicEventKind.entrega ||
                        e.kind == AcademicEventKind.parcial
                    ? p.orange
                    : p.textTertiary,
              ),
            ),
          ),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: IosCard(
            padding: const EdgeInsets.all(14),
            borderColor: border,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  kindLabel,
                  style: TextStyle(
                    fontSize: 10,
                    letterSpacing: 0.6,
                    fontWeight: FontWeight.w600,
                    color: kindColor,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  e.title,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
                Text(
                  e.subtitle,
                  style: TextStyle(fontSize: 12, color: p.textSecondary),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
