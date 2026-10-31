import 'package:flutter/material.dart';

import '../../../../core/theme/app_theme.dart';
import '../../../widgets/ios_primitives.dart';

/// Pestaña 1: "Resumen de hoy".
class ResumenTab extends StatelessWidget {
  const ResumenTab({
    super.key,
    required this.onOpenClaseViva,
    required this.onCompleteBlock,
  });

  final ValueChanged<String> onOpenClaseViva;
  final VoidCallback onCompleteBlock;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;

    return ListView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.baseline,
          textBaseline: TextBaseline.alphabetic,
          children: [
            Text(
              'Resumen de hoy',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.w700,
                letterSpacing: -0.4,
                color: p.textPrimary,
              ),
            ),
            const Spacer(),
            Text(
              'Viernes, 30 Oct',
              style: TextStyle(fontSize: 12, color: p.textSecondary),
            ),
          ],
        ),
        const SizedBox(height: 16),

        // Próximo parcial
        TapScale(
          onTap: () => onOpenClaseViva('calculo'),
          child: IosCard(
            borderColor: p.orange.o(0.4),
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [p.warmTop, p.card],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      'PRÓXIMO PARCIAL',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                        letterSpacing: 0.6,
                        color: p.orange,
                      ),
                    ),
                    const Spacer(),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 2,
                      ),
                      decoration: BoxDecoration(
                        color: p.orange.o(0.15),
                        borderRadius: BorderRadius.circular(999),
                        border: Border.all(color: p.orange.o(0.3)),
                      ),
                      child: Text(
                        'En 3 días',
                        style: mono(fontSize: 11, color: p.orange),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  'Cálculo Integral • Corte 2 (30%)',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: p.textPrimary,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'Salón: A-204 • Docente: C. Mendoza',
                  style: TextStyle(fontSize: 12, color: p.textSecondary),
                ),
                Container(
                  margin: const EdgeInsets.only(top: 12),
                  padding: const EdgeInsets.only(top: 10),
                  decoration: BoxDecoration(
                    border: Border(top: BorderSide(color: p.cardBorder)),
                  ),
                  child: Row(
                    children: [
                      Text(
                        'Meta sugerida según AyRe:',
                        style: TextStyle(fontSize: 12, color: p.textSecondary),
                      ),
                      const Spacer(),
                      Text(
                        '≥ 3.4 / 5.0',
                        style: mono(
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                          color: p.textPrimary,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 16),

        // Siguiente clase magistral
        IosCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Text(
                    'SIGUIENTE CLASE MAGISTRAL',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                      color: p.textSecondary,
                    ),
                  ),
                  const Spacer(),
                  Text('10:00 AM', style: mono(fontSize: 12, color: p.green)),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                'Física Mecánica y Termodinámica',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: p.textPrimary,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                'Bloque C - Salón 102 • Tema: Leyes de Newton y Rozamiento',
                style: TextStyle(fontSize: 12, color: p.textSecondary),
              ),
              const SizedBox(height: 12),
              TapScale(
                onTap: () => onOpenClaseViva('fisica'),
                child: Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 9,
                  ),
                  decoration: BoxDecoration(
                    color: p.elevated,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    children: [
                      Expanded(
                        child: Text(
                          'Ver tema que toca hoy en La Clase Viva',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w500,
                            color: p.textSecondary,
                          ),
                        ),
                      ),
                      Text('→', style: TextStyle(color: p.textPrimary)),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 16),

        // Bloque de enfoque rápido
        IosCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Dot(color: p.indigo),
                  const SizedBox(width: 8),
                  Text(
                    'Bloque de Enfoque Rápido',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: p.textPrimary,
                    ),
                  ),
                  const Spacer(),
                  Text(
                    '+2 consultas al terminar',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                      color: p.indigo,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                'Plantilla Pomodoro 50/10 sincronizada con Unidad 2: Dinámica rotacional y fricción.',
                style: TextStyle(fontSize: 12, color: p.textSecondary),
              ),
              const SizedBox(height: 12),
              TapScale(
                onTap: onCompleteBlock,
                child: Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(vertical: 11),
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: p.indigo,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Text(
                    'Completar bloque de estudio (+2 Uso Diario)',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
