import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/models/student_user_model.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../../widgets/reminder_creator_sheet.dart';

const _weekDayLabels = ['L', 'M', 'M', 'J', 'V', 'S', 'D'];
const _filters = [
  'Día',
  'Todos',
  'Parciales',
  'Bloques',
  'Clases',
  'Entregas Moodle',
];

/// Pestaña 2: "Calendario Personal" con soporte Offline-First (0 ms) y
/// sincronización en segundo plano hacia `db/users/{username}.json` en GitHub.
class CalendarioTab extends StatefulWidget {
  const CalendarioTab({
    super.key,
    this.onOpenClaseViva,
  });

  final ValueChanged<String>? onOpenClaseViva;

  @override
  State<CalendarioTab> createState() => _CalendarioTabState();
}

class _CalendarioTabState extends State<CalendarioTab> {
  late DateTime _selectedDate;
  int _weekOffset = 0;
  String _filter = 'Todos';

  @override
  void initState() {
    super.initState();
    final now = DateTime.now();
    _selectedDate = DateTime(now.year, now.month, now.day);
  }

  List<DateTime> get _currentWeekDays {
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final monday = today
        .subtract(Duration(days: today.weekday - 1))
        .add(Duration(days: _weekOffset * 7));
    return List.generate(7, (i) => monday.add(Duration(days: i)));
  }

  bool _matchesFilter(CalendarReminderModel r) {
    final selectedIso = IsoDateHelper.todayIso(_selectedDate);
    if (_filter == 'Día') {
      return r.fechaIso == selectedIso;
    }
    switch (_filter) {
      case 'Parciales':
        return r.tipo == AcademicEventKind.parcial;
      case 'Bloques':
        return r.tipo == AcademicEventKind.bloque;
      case 'Clases':
        return r.tipo == AcademicEventKind.clase;
      case 'Entregas Moodle':
        return r.tipo == AcademicEventKind.entrega;
      case 'Todos':
      default:
        return true;
    }
  }

  String _formatDateShort(String iso) {
    final d = DateTime.tryParse(iso);
    if (d == null) return iso;
    const months = [
      'Ene',
      'Feb',
      'Mar',
      'Abr',
      'May',
      'Jun',
      'Jul',
      'Ago',
      'Sep',
      'Oct',
      'Nov',
      'Dic',
    ];
    return '${d.day} ${months[d.month - 1]}';
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final allReminders = session?.reminders ?? const <CalendarReminderModel>[];
    final visible = allReminders.where(_matchesFilter).toList();
    final weekDays = _currentWeekDays;

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
      children: [
        // Encabezado + botón + Agendar
        Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Calendario Personal',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.4,
                      color: p.textPrimary,
                    ),
                  ),
                  Text(
                    'Parciales, entregas y bloques en tu JSON de GitHub',
                    style: TextStyle(fontSize: 11.5, color: p.textSecondary),
                  ),
                ],
              ),
            ),
            TapScale(
              onTap: () => showReminderCreatorSheet(
                context,
                initialDate: _selectedDate,
              ),
              child: Container(
                key: const Key('calendar_add_button'),
                padding: const EdgeInsets.symmetric(
                  horizontal: 12,
                  vertical: 7,
                ),
                decoration: BoxDecoration(
                  color: p.green,
                  borderRadius: BorderRadius.circular(999),
                ),
                child: const Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.add_rounded, size: 16, color: Colors.black),
                    SizedBox(width: 3),
                    Text(
                      'Agendar',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: Colors.black,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 14),

        // Navegación de semana + tira de 7 días
        Row(
          children: [
            TapScale(
              onTap: () => setState(() => _weekOffset--),
              child: Padding(
                padding: const EdgeInsets.all(4),
                child: Icon(
                  Icons.chevron_left_rounded,
                  size: 18,
                  color: p.textSecondary,
                ),
              ),
            ),
            Expanded(
              child: Text(
                '${_formatDateShort(IsoDateHelper.todayIso(weekDays.first))} — ${_formatDateShort(IsoDateHelper.todayIso(weekDays.last))}',
                textAlign: TextAlign.center,
                style: mono(fontSize: 11, color: p.textSecondary),
              ),
            ),
            if (_weekOffset != 0)
              Padding(
                padding: const EdgeInsets.only(right: 6),
                child: TapScale(
                  onTap: () {
                    final now = DateTime.now();
                    setState(() {
                      _weekOffset = 0;
                      _selectedDate = DateTime(now.year, now.month, now.day);
                    });
                  },
                  child: Text(
                    'Hoy',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: p.green,
                    ),
                  ),
                ),
              ),
            TapScale(
              onTap: () => setState(() => _weekOffset++),
              child: Padding(
                padding: const EdgeInsets.all(4),
                child: Icon(
                  Icons.chevron_right_rounded,
                  size: 18,
                  color: p.textSecondary,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 8),

        Row(
          children: [
            for (var i = 0; i < weekDays.length; i++) ...[
              if (i > 0) const SizedBox(width: 6),
              Expanded(
                child: _dayButton(
                  p,
                  _weekDayLabels[i],
                  weekDays[i],
                  allReminders,
                ),
              ),
            ],
          ],
        ),
        const SizedBox(height: 14),

        // Filtros estilo píldora iOS
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          child: Row(
            children: [
              for (final f in _filters)
                Padding(
                  padding: const EdgeInsets.only(right: 8),
                  child: _chip(
                    p,
                    f == 'Todos' ? 'Todos (${allReminders.length})' : f,
                    f,
                  ),
                ),
            ],
          ),
        ),
        const SizedBox(height: 16),

        if (visible.isEmpty)
          IosCard(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                Icon(
                  Icons.event_note_outlined,
                  size: 26,
                  color: p.textTertiary,
                ),
                const SizedBox(height: 8),
                Text(
                  _filter == 'Día'
                      ? 'Sin recordatorios para el ${_formatDateShort(IsoDateHelper.todayIso(_selectedDate))}.'
                      : 'Aún no tienes recordatorios en "${_filter.toLowerCase()}".',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 12.5, color: p.textSecondary),
                ),
                const SizedBox(height: 12),
                TapScale(
                  onTap: () => showReminderCreatorSheet(
                    context,
                    initialDate: _selectedDate,
                  ),
                  child: Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 14,
                      vertical: 8,
                    ),
                    decoration: BoxDecoration(
                      color: p.elevated,
                      borderRadius: BorderRadius.circular(999),
                      border: Border.all(color: p.green.o(0.45)),
                    ),
                    child: Text(
                      '+ Agendar parcial, entrega o bloque',
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: p.green,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          )
        else
          for (final r in visible) ...[
            _ReminderEventRow(
              reminder: r,
              dateLabel: _formatDateShort(r.fechaIso),
              onToggleComplete: () {
                HapticFeedback.lightImpact();
                session?.toggleReminderCompleted(r.id);
              },
              onDelete: () {
                HapticFeedback.lightImpact();
                session?.deleteCalendarReminder(r.id);
                showIosToast(context, 'Recordatorio eliminado');
              },
              onOpenSubject:
                  (r.codigoMateria != null && widget.onOpenClaseViva != null)
                      ? () => widget.onOpenClaseViva!(r.codigoMateria!)
                      : null,
            ),
            const SizedBox(height: 12),
          ],
      ],
    );
  }

  Widget _dayButton(
    AppPalette p,
    String label,
    DateTime date,
    List<CalendarReminderModel> reminders,
  ) {
    final iso = IsoDateHelper.todayIso(date);
    final selected = iso == IsoDateHelper.todayIso(_selectedDate);
    final dayEvents = reminders.where((r) => r.fechaIso == iso).toList();
    final hasParcial = dayEvents.any(
      (r) =>
          r.tipo == AcademicEventKind.parcial ||
          r.tipo == AcademicEventKind.entrega,
    );
    final hasAny = dayEvents.isNotEmpty;

    final Color bg = selected ? p.inverse : p.card;
    final Color border = selected
        ? p.inverse
        : (hasParcial ? p.orange.o(0.55) : p.cardBorder);
    final Color labelColor = selected
        ? p.onInverse
        : (hasParcial ? p.orange : p.textSecondary);
    final Color numberColor = selected
        ? p.onInverse
        : (hasParcial ? p.orange : p.textPrimary);

    return TapScale(
      onTap: () => setState(() {
        _selectedDate = date;
        _filter = 'Día';
      }),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        curve: kIosSpring,
        padding: const EdgeInsets.symmetric(vertical: 8),
        decoration: BoxDecoration(
          color: bg,
          borderRadius: BorderRadius.circular(15),
          border: Border.all(color: border),
        ),
        child: Column(
          children: [
            Text(label, style: TextStyle(fontSize: 10, color: labelColor)),
            const SizedBox(height: 2),
            Text(
              '${date.day}',
              style: TextStyle(
                fontSize: 12,
                fontWeight: selected ? FontWeight.w700 : FontWeight.w600,
                color: numberColor,
              ),
            ),
            const SizedBox(height: 3),
            Dot(
              color: !hasAny
                  ? Colors.transparent
                  : (hasParcial ? p.orange : p.green),
              size: 4.5,
            ),
          ],
        ),
      ),
    );
  }

  Widget _chip(AppPalette p, String displayLabel, String value) {
    final selected = value == _filter;
    return TapScale(
      onTap: () => setState(() => _filter = value),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 5),
        decoration: BoxDecoration(
          color: selected ? p.inverse : p.card,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(color: selected ? p.inverse : p.cardBorder),
        ),
        child: Text(
          displayLabel,
          style: TextStyle(
            fontSize: 12,
            fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
            color: selected ? p.onInverse : p.textSecondary,
          ),
        ),
      ),
    );
  }
}

class _ReminderEventRow extends StatelessWidget {
  const _ReminderEventRow({
    required this.reminder,
    required this.dateLabel,
    required this.onToggleComplete,
    required this.onDelete,
    this.onOpenSubject,
  });

  final CalendarReminderModel reminder;
  final String dateLabel;
  final VoidCallback onToggleComplete;
  final VoidCallback onDelete;
  final VoidCallback? onOpenSubject;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    late final String kindLabel;
    late final Color kindColor;
    Color? border;

    switch (reminder.tipo) {
      case AcademicEventKind.clase:
        kindLabel = 'CLASE MAGISTRAL';
        kindColor = p.green;
      case AcademicEventKind.bloque:
        kindLabel = 'BLOQUE DE ESTUDIO';
        kindColor = p.indigo;
        border = p.indigo.o(0.45);
      case AcademicEventKind.entrega:
        kindLabel = 'ENTREGA MOODLE';
        kindColor = p.orange;
        border = p.orange.o(0.45);
      case AcademicEventKind.parcial:
        kindLabel = 'EVALUACIÓN PARCIAL';
        kindColor = p.orange;
        border = p.orange.o(0.6);
    }

    return Dismissible(
      key: ValueKey('rem_${reminder.id}'),
      direction: DismissDirection.endToStart,
      onDismissed: (_) => onDelete(),
      background: Container(
        alignment: Alignment.centerRight,
        padding: const EdgeInsets.only(right: 18),
        decoration: BoxDecoration(
          color: p.orange.o(0.18),
          borderRadius: BorderRadius.circular(18),
        ),
        child: Icon(Icons.delete_outline_rounded, color: p.orange),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 52,
            child: Padding(
              padding: const EdgeInsets.only(top: 6),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    reminder.hora,
                    style: mono(
                      fontSize: 11.5,
                      fontWeight: FontWeight.w600,
                      color: reminder.tipo == AcademicEventKind.parcial ||
                              reminder.tipo == AcademicEventKind.entrega
                          ? p.orange
                          : p.textSecondary,
                    ),
                  ),
                  Text(
                    dateLabel,
                    style: mono(fontSize: 9.5, color: p.textTertiary),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: TapScale(
              onTap: onOpenSubject ?? onToggleComplete,
              child: IosCard(
                padding: const EdgeInsets.all(13),
                borderColor: reminder.completado ? p.cardBorder : border,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    GestureDetector(
                      onTap: onToggleComplete,
                      child: Padding(
                        padding: const EdgeInsets.only(top: 2, right: 10),
                        child: Icon(
                          reminder.completado
                              ? Icons.check_circle_rounded
                              : Icons.radio_button_unchecked_rounded,
                          size: 19,
                          color:
                              reminder.completado ? p.green : p.textTertiary,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            kindLabel,
                            style: TextStyle(
                              fontSize: 9.5,
                              letterSpacing: 0.6,
                              fontWeight: FontWeight.w600,
                              color: kindColor,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            reminder.titulo,
                            style: TextStyle(
                              fontSize: 13.5,
                              fontWeight: FontWeight.w600,
                              decoration: reminder.completado
                                  ? TextDecoration.lineThrough
                                  : null,
                              color: reminder.completado
                                  ? p.textSecondary
                                  : p.textPrimary,
                            ),
                          ),
                          if (reminder.subtitulo.isNotEmpty) ...[
                            const SizedBox(height: 2),
                            Text(
                              reminder.subtitulo,
                              style: TextStyle(
                                fontSize: 11.5,
                                color: p.textSecondary,
                              ),
                            ),
                          ],
                        ],
                      ),
                    ),
                    GestureDetector(
                      key: ValueKey('delete_rem_${reminder.id}'),
                      onTap: onDelete,
                      child: Padding(
                        padding: const EdgeInsets.all(4),
                        child: Icon(
                          Icons.close_rounded,
                          size: 16,
                          color: p.textTertiary,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
