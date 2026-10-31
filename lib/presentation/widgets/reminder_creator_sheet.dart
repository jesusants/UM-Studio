import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../core/theme/app_theme.dart';
import '../../data/models/curriculum_models.dart';
import '../../data/models/student_user_model.dart';
import '../../domain/entities/subject_summary.dart';
import '../providers/app_scopes.dart';
import 'ios_primitives.dart';

/// Abre una hoja modal iOS minimalista para agendar un parcial, clase,
/// bloque de estudio o entrega sincronizada con `db/users/{username}.json`.
Future<void> showReminderCreatorSheet(
  BuildContext context, {
  AcademicEventKind initialKind = AcademicEventKind.parcial,
  DateTime? initialDate,
  AsignaturaModel? preselectedSubject,
}) async {
  final p = context.palette;

  await showModalBottomSheet<void>(
    context: context,
    isScrollControlled: true,
    backgroundColor: p.card,
    shape: RoundedRectangleBorder(
      borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
      side: BorderSide(color: p.cardBorder),
    ),
    builder: (sheetCtx) {
      return _ReminderCreatorSheetBody(
        initialKind: initialKind,
        initialDate: initialDate ?? DateTime.now(),
        preselectedSubject: preselectedSubject,
      );
    },
  );
}

class _ReminderCreatorSheetBody extends StatefulWidget {
  const _ReminderCreatorSheetBody({
    required this.initialKind,
    required this.initialDate,
    this.preselectedSubject,
  });

  final AcademicEventKind initialKind;
  final DateTime initialDate;
  final AsignaturaModel? preselectedSubject;

  @override
  State<_ReminderCreatorSheetBody> createState() =>
      _ReminderCreatorSheetBodyState();
}

class _ReminderCreatorSheetBodyState extends State<_ReminderCreatorSheetBody> {
  late AcademicEventKind _kind;
  late DateTime _selectedDate;
  String _selectedTime = '10:00';
  AsignaturaModel? _subject;

  final TextEditingController _titleCtrl = TextEditingController();
  final TextEditingController _subtitleCtrl = TextEditingController();
  String? _error;

  static const _times = [
    '07:00',
    '08:00',
    '10:00',
    '14:00',
    '16:00',
    '18:00',
    '20:00',
    '23:59',
  ];

  @override
  void initState() {
    super.initState();
    _kind = widget.initialKind;
    _selectedDate = DateTime(
      widget.initialDate.year,
      widget.initialDate.month,
      widget.initialDate.day,
    );
    _subject = widget.preselectedSubject;
    if (_kind == AcademicEventKind.entrega) {
      _selectedTime = '23:59';
    }
    if (_subject != null) {
      _applySubjectSuggestion(_subject!);
    }
  }

  @override
  void dispose() {
    _titleCtrl.dispose();
    _subtitleCtrl.dispose();
    super.dispose();
  }

  String _prefixForKind(AcademicEventKind k) {
    switch (k) {
      case AcademicEventKind.parcial:
        return 'Parcial';
      case AcademicEventKind.bloque:
        return 'Bloque Estudio:';
      case AcademicEventKind.clase:
        return 'Clase';
      case AcademicEventKind.entrega:
        return 'Entrega Moodle:';
    }
  }

  void _applySubjectSuggestion(AsignaturaModel asig) {
    final prefix = _prefixForKind(_kind);
    _titleCtrl.text = '$prefix ${asig.nombre}';
    if (_subtitleCtrl.text.trim().isEmpty) {
      _subtitleCtrl.text = _kind == AcademicEventKind.bloque
          ? asig.primerTema.bloqueSugerido
          : 'Salón C-102 • ${asig.primerTema.titulo}';
    }
  }

  String _formatDateLabel(DateTime d) {
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

  Future<void> _pickCustomDate() async {
    final now = DateTime.now();
    final picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(now.year - 1),
      lastDate: DateTime(now.year + 2),
    );
    if (picked != null && mounted) {
      setState(() {
        _selectedDate = DateTime(picked.year, picked.month, picked.day);
      });
    }
  }

  Future<void> _save() async {
    final title = _titleCtrl.text.trim();
    if (title.isEmpty) {
      setState(() => _error = 'Escribe un título (ej. Parcial Física Mecánica).');
      return;
    }

    final session = SessionScope.of(context);
    final subtitle = _subtitleCtrl.text.trim().isEmpty
        ? 'Ingeniería Energética • Unimagdalena'
        : _subtitleCtrl.text.trim();

    await session.addCalendarReminder(
      titulo: title,
      subtitulo: subtitle,
      fechaIso: DailyUsageModel.todayIso(_selectedDate),
      hora: _selectedTime,
      tipo: _kind,
      codigoMateria: _subject?.codigo,
    );

    HapticFeedback.lightImpact();
    if (mounted) {
      Navigator.of(context).pop();
      showIosToast(
        context,
        'Guardado y sincronizando con GitHub',
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final curriculum = CurriculumScope.maybeOf(context);
    final bottomInset = MediaQuery.viewInsetsOf(context).bottom;

    final allSubjects = curriculum?.allAsignaturas ?? const <AsignaturaModel>[];
    final mySubjects = session == null
        ? allSubjects.take(6).toList()
        : allSubjects.where(session.isMySubject).toList();
    final suggestedSubjects =
        mySubjects.isNotEmpty ? mySubjects : allSubjects.take(6).toList();

    final today = DateTime.now();
    final cleanToday = DateTime(today.year, today.month, today.day);
    final quickDates = [
      ('Hoy', cleanToday),
      ('Mañana', cleanToday.add(const Duration(days: 1))),
      ('En 3 días', cleanToday.add(const Duration(days: 3))),
      ('En 7 días', cleanToday.add(const Duration(days: 7))),
    ];

    return SafeArea(
      child: SingleChildScrollView(
        physics: const BouncingScrollPhysics(),
        padding: EdgeInsets.fromLTRB(18, 12, 18, 18 + bottomInset),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Container(
                width: 36,
                height: 4,
                decoration: BoxDecoration(
                  color: p.strongBorder,
                  borderRadius: BorderRadius.circular(4),
                ),
              ),
            ),
            const SizedBox(height: 14),
            Row(
              children: [
                Text('NUEVO RECORDATORIO PERSONAL', style: sectionMicroStyle(p)),
                const Spacer(),
                Text(
                  _formatDateLabel(_selectedDate),
                  style: mono(
                    fontSize: 11,
                    fontWeight: FontWeight.w600,
                    color: p.green,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 10),

            // Selector de tipo
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  _kindChip(p, AcademicEventKind.parcial, 'Parcial', p.orange),
                  const SizedBox(width: 6),
                  _kindChip(
                    p,
                    AcademicEventKind.bloque,
                    'Bloque Estudio',
                    p.indigo,
                  ),
                  const SizedBox(width: 6),
                  _kindChip(p, AcademicEventKind.clase, 'Clase', p.green),
                  const SizedBox(width: 6),
                  _kindChip(
                    p,
                    AcademicEventKind.entrega,
                    'Entrega Moodle',
                    p.orange,
                  ),
                ],
              ),
            ),

            if (suggestedSubjects.isNotEmpty) ...[
              const SizedBox(height: 14),
              Text('VINCULAR MATERIA (OPCIONAL)', style: sectionMicroStyle(p)),
              const SizedBox(height: 8),
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                child: Row(
                  children: [
                    for (final asig in suggestedSubjects)
                      Padding(
                        padding: const EdgeInsets.only(right: 6),
                        child: TapScale(
                          onTap: () {
                            setState(() {
                              if (_subject?.codigo == asig.codigo) {
                                _subject = null;
                              } else {
                                _subject = asig;
                                _applySubjectSuggestion(asig);
                              }
                            });
                          },
                          child: Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 10,
                              vertical: 6,
                            ),
                            decoration: BoxDecoration(
                              color: _subject?.codigo == asig.codigo
                                  ? asig.accentColor.o(0.16)
                                  : p.elevated,
                              borderRadius: BorderRadius.circular(999),
                              border: Border.all(
                                color: _subject?.codigo == asig.codigo
                                    ? asig.accentColor
                                    : p.cardBorder,
                              ),
                            ),
                            child: Text(
                              asig.nombre,
                              style: TextStyle(
                                fontSize: 11.5,
                                fontWeight: _subject?.codigo == asig.codigo
                                    ? FontWeight.w600
                                    : FontWeight.w400,
                                color: _subject?.codigo == asig.codigo
                                    ? p.textPrimary
                                    : p.textSecondary,
                              ),
                            ),
                          ),
                        ),
                      ),
                  ],
                ),
              ),
            ],

            const SizedBox(height: 14),
            Text('TÍTULO', style: sectionMicroStyle(p)),
            const SizedBox(height: 6),
            TextField(
              key: const Key('reminder_title_field'),
              controller: _titleCtrl,
              style: TextStyle(fontSize: 13.5, color: p.textPrimary),
              decoration: _fieldDecoration(
                p,
                hint: 'Ej: Parcial Física Mecánica - Corte 2',
              ),
            ),
            const SizedBox(height: 12),

            Text('SALÓN, TEMA O NOTA', style: sectionMicroStyle(p)),
            const SizedBox(height: 6),
            TextField(
              key: const Key('reminder_subtitle_field'),
              controller: _subtitleCtrl,
              style: TextStyle(fontSize: 13, color: p.textPrimary),
              decoration: _fieldDecoration(
                p,
                hint: 'Ej: Bloque C - Salón 102 • Leyes de Newton',
              ),
            ),
            const SizedBox(height: 14),

            Text('FECHA Y HORA', style: sectionMicroStyle(p)),
            const SizedBox(height: 8),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  for (final (label, d) in quickDates)
                    Padding(
                      padding: const EdgeInsets.only(right: 6),
                      child: TapScale(
                        onTap: () => setState(() => _selectedDate = d),
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 11,
                            vertical: 6,
                          ),
                          decoration: BoxDecoration(
                            color: DailyUsageModel.todayIso(_selectedDate) ==
                                    DailyUsageModel.todayIso(d)
                                ? p.inverse
                                : p.elevated,
                            borderRadius: BorderRadius.circular(999),
                            border: Border.all(color: p.cardBorder),
                          ),
                          child: Text(
                            label,
                            style: TextStyle(
                              fontSize: 11.5,
                              fontWeight: FontWeight.w600,
                              color: DailyUsageModel.todayIso(_selectedDate) ==
                                      DailyUsageModel.todayIso(d)
                                  ? p.onInverse
                                  : p.textSecondary,
                            ),
                          ),
                        ),
                      ),
                    ),
                  TapScale(
                    onTap: _pickCustomDate,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 11,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: p.elevated,
                        borderRadius: BorderRadius.circular(999),
                        border: Border.all(color: p.green.o(0.45)),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.calendar_today_rounded,
                            size: 12,
                            color: p.green,
                          ),
                          const SizedBox(width: 5),
                          Text(
                            _formatDateLabel(_selectedDate),
                            style: mono(fontSize: 11, color: p.green),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 8),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  for (final t in _times)
                    Padding(
                      padding: const EdgeInsets.only(right: 6),
                      child: TapScale(
                        onTap: () => setState(() => _selectedTime = t),
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 10,
                            vertical: 5,
                          ),
                          decoration: BoxDecoration(
                            color: _selectedTime == t
                                ? p.green.o(0.16)
                                : p.elevated,
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(
                              color:
                                  _selectedTime == t ? p.green : p.cardBorder,
                            ),
                          ),
                          child: Text(
                            t,
                            style: mono(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: _selectedTime == t
                                  ? p.green
                                  : p.textSecondary,
                            ),
                          ),
                        ),
                      ),
                    ),
                ],
              ),
            ),

            if (_error != null) ...[
              const SizedBox(height: 10),
              Text(
                _error!,
                style: TextStyle(fontSize: 11.5, color: p.orange),
              ),
            ],

            const SizedBox(height: 16),
            TapScale(
              onTap: _save,
              child: Container(
                key: const Key('reminder_save_button'),
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 12),
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: p.green,
                  borderRadius: BorderRadius.circular(13),
                ),
                child: const Text(
                  'Guardar en mi calendario personal',
                  style: TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w700,
                    color: Colors.black,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _kindChip(
    AppPalette p,
    AcademicEventKind kind,
    String label,
    Color accent,
  ) {
    final selected = _kind == kind;
    return TapScale(
      onTap: () {
        setState(() {
          _kind = kind;
          if (kind == AcademicEventKind.entrega) {
            _selectedTime = '23:59';
          }
          if (_subject != null) {
            _applySubjectSuggestion(_subject!);
          }
        });
      },
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 6),
        decoration: BoxDecoration(
          color: selected ? accent.o(0.16) : p.elevated,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(color: selected ? accent : p.cardBorder),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Dot(color: accent, size: 6),
            const SizedBox(width: 6),
            Text(
              label,
              style: TextStyle(
                fontSize: 12,
                fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
                color: selected ? p.textPrimary : p.textSecondary,
              ),
            ),
          ],
        ),
      ),
    );
  }

  InputDecoration _fieldDecoration(AppPalette p, {required String hint}) {
    return InputDecoration(
      isDense: true,
      filled: true,
      fillColor: p.background.o(0.45),
      hintText: hint,
      hintStyle: TextStyle(fontSize: 12.5, color: p.textTertiary),
      contentPadding: const EdgeInsets.symmetric(horizontal: 12, vertical: 11),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide(color: p.cardBorder),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide(color: p.green),
      ),
    );
  }
}
