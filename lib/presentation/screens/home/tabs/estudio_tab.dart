import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../../data/datasources/academic_seed_data.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../widgets/ios_primitives.dart';

/// Pestaña 3: "Estudio Extraclase".
class EstudioTab extends StatelessWidget {
  const EstudioTab({super.key, required this.onOpenClaseViva});

  final ValueChanged<String> onOpenClaseViva;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
      children: [
        Text(
          'Estudio Extraclase',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.w700,
            letterSpacing: -0.5,
            color: p.textPrimary,
          ),
        ),
        const SizedBox(height: 2),
        Text(
          'Toca cualquier asignatura para abrir su Clase Viva oficial',
          style: TextStyle(fontSize: 12, color: p.textSecondary),
        ),
        const SizedBox(height: 16),
        for (final s in AcademicSeedData.subjects) ...[
          _SubjectCard(subject: s, onTap: () => onOpenClaseViva(s.id)),
          const SizedBox(height: 12),
        ],
      ],
    );
  }
}

class _SubjectCard extends StatelessWidget {
  const _SubjectCard({required this.subject, required this.onTap});

  final SubjectSummaryEntity subject;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final accent = subject.accentResolver(p);
    final percent = '${(subject.progress * 100).round()}%';

    return TapScale(
      onTap: onTap,
      child: IosCard(
        borderColor: subject.active ? p.green.o(0.4) : null,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      if (subject.active)
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 2,
                          ),
                          decoration: BoxDecoration(
                            color: p.green.o(0.1),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            '${subject.category} • En curso'.toUpperCase(),
                            style: mono(fontSize: 10, color: p.green),
                          ),
                        )
                      else
                        Text(
                          subject.category.toUpperCase(),
                          style: mono(fontSize: 10, color: p.textSecondary),
                        ),
                      SizedBox(height: subject.active ? 6 : 4),
                      Text(
                        subject.title,
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w600,
                          color: p.textPrimary,
                        ),
                      ),
                    ],
                  ),
                ),
                Text(
                  percent,
                  style: mono(
                    fontSize: 12,
                    fontWeight:
                        subject.active ? FontWeight.w600 : FontWeight.w400,
                    color: subject.active ? p.textPrimary : p.textSecondary,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            Text.rich(
              TextSpan(
                style: TextStyle(fontSize: 12, color: p.textSecondary),
                children: [
                  const TextSpan(text: 'Próximo tema: '),
                  TextSpan(
                    text: subject.nextTopic,
                    style: TextStyle(
                      fontWeight: FontWeight.w700,
                      color: p.textPrimary,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 12),
            ProgressBar(value: subject.progress, color: accent, height: 6),
          ],
        ),
      ),
    );
  }
}
