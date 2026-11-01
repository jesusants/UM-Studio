import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/constants/app_constants.dart';
import '../../../../core/theme/app_theme.dart';
import '../../../../core/utils/fullscreen/fullscreen_helper.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../../data/models/student_user_model.dart';
import '../../../../domain/entities/subject_summary.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/header_morph_avatar.dart';
import '../../../widgets/ios_primitives.dart';

/// Sidebar izquierdo (25% del ancho) para el Dashboard de Escritorio:
/// - Cabecera institucional
/// - Widget de uso diario con barra redondeada y ampliación de cupo
/// - Acceso rápido a materias activas con avance y parciales
/// - Pie con perfil y toggle de pantalla completa nativa
class DesktopSidebar extends StatefulWidget {
  const DesktopSidebar({
    super.key,
    required this.activeSubjects,
    required this.onOpenClaseViva,
    required this.onOpenTemario,
    required this.onOpenStudentProfile,
  });

  final List<AsignaturaModel> activeSubjects;
  final ValueChanged<String> onOpenClaseViva;
  final ValueChanged<AsignaturaModel> onOpenTemario;
  final VoidCallback onOpenStudentProfile;

  @override
  State<DesktopSidebar> createState() => _DesktopSidebarState();
}

class _DesktopSidebarState extends State<DesktopSidebar> {
  final int _dailyUsed = 42;
  int _dailyMax = 100;
  bool _isFullscreen = false;

  void _expandQuota() {
    HapticFeedback.mediumImpact();
    setState(() {
      _dailyMax += 50;
    });
    showIosToast(
      context,
      'Cupo ampliado: +50 consultas académicas asignadas hoy',
      accentColor: const Color(0xFF30D158),
    );
  }

  void _toggleFullscreen() {
    HapticFeedback.lightImpact();
    FullscreenHelper.toggle();
    setState(() {
      _isFullscreen = !_isFullscreen;
    });
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final session = SessionScope.maybeOf(context);
    final cuat = session?.cuatrimestreActual ?? 2;
    final userReminders = session?.reminders ?? const <CalendarReminderModel>[];

    final usageRatio = (_dailyUsed / _dailyMax).clamp(0.0, 1.0);

    return Container(
      decoration: BoxDecoration(
        color: const Color(0xDC0D0E12),
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: const Color(0xFF1A1D24), width: 1),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // 1. Cabecera Institucional
          Row(
            children: [
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: const Color(0xFF30D158).o(0.12),
                  border: Border.all(
                    color: const Color(0xFF30D158).o(0.40),
                    width: 1.5,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF30D158).o(0.20),
                      blurRadius: 10,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: Center(
                  child: Image.asset(
                    AppConstants.programLogoAsset,
                    width: 24,
                    height: 24,
                    errorBuilder: (_, __, ___) => const Icon(
                      Icons.bolt_rounded,
                      color: Color(0xFF30D158),
                      size: 20,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'UM STUDIO DESKTOP',
                      style: TextStyle(
                        fontSize: 13.5,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.3,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 3),
                    Row(
                      children: [
                        const PulseDot(color: Color(0xFF30D158), size: 6.5),
                        const SizedBox(width: 6),
                        Expanded(
                          child: Text(
                            'En línea • AyRe Sincronizado',
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 9.5,
                              fontWeight: FontWeight.w600,
                              color: const Color(0xFF30D158),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 18),

          // 2. Widget de Uso Diario (Versión expandida pill shape)
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: const Color(0xFF13151B),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: const Color(0xFF1F232D)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'USO DIARIO',
                      style: mono(
                        fontSize: 9.5,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 0.8,
                        color: p.textTertiary,
                      ),
                    ),
                    Flexible(
                      child: Text(
                        '$_dailyUsed / $_dailyMax consultas',
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: mono(
                          fontSize: 10,
                          fontWeight: FontWeight.w600,
                          color: p.textSecondary,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 9),
                // Barra de progreso con puntas 100% redondeadas (pill shape)
                Container(
                  height: 7,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    color: const Color(0xFF1F2228),
                    borderRadius: BorderRadius.circular(999),
                  ),
                  alignment: Alignment.centerLeft,
                  child: FractionallySizedBox(
                    widthFactor: usageRatio,
                    child: Container(
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFF30D158), Color(0xFF34C759)],
                        ),
                        borderRadius: BorderRadius.circular(999),
                        boxShadow: [
                          BoxShadow(
                            color: const Color(0xFF30D158).o(0.35),
                            blurRadius: 6,
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 10),
                Wrap(
                  alignment: WrapAlignment.spaceBetween,
                  crossAxisAlignment: WrapCrossAlignment.center,
                  spacing: 6,
                  runSpacing: 6,
                  children: [
                    Text(
                      '${(usageRatio * 100).toInt()}% consumido',
                      style: mono(
                        fontSize: 10,
                        color: const Color(0xFF30D158),
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                    MouseRegion(
                      cursor: SystemMouseCursors.click,
                      child: GestureDetector(
                        onTap: _expandQuota,
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 9,
                            vertical: 4,
                          ),
                          decoration: BoxDecoration(
                            color: const Color(0xFF30D158).o(0.12),
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(
                              color: const Color(0xFF30D158).o(0.40),
                              width: 1,
                            ),
                          ),
                          child: const Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                Icons.add_rounded,
                                size: 12,
                                color: Color(0xFF30D158),
                              ),
                              SizedBox(width: 4),
                              Text(
                                'Ampliar Cupo',
                                style: TextStyle(
                                  fontSize: 10.5,
                                  fontWeight: FontWeight.w700,
                                  color: Color(0xFF30D158),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 18),

          // 3. Acceso Rápido a Materias Activas
          Row(
            children: [
              Expanded(
                child: Text(
                  'MATERIAS ACTIVAS (C$cuat)',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 0.8,
                    color: p.textTertiary,
                  ),
                ),
              ),
              const SizedBox(width: 6),
              Text(
                '${widget.activeSubjects.length} inscritas',
                style: mono(fontSize: 9.5, color: p.textTertiary),
              ),
            ],
          ),
          const SizedBox(height: 10),

          // Lista de materias con scroll interno
          Expanded(
            child: ScrollConfiguration(
              behavior: ScrollConfiguration.of(context).copyWith(
                scrollbars: false,
              ),
              child: ListView.separated(
                physics: const BouncingScrollPhysics(),
                itemCount: widget.activeSubjects.length,
                separatorBuilder: (_, __) => const SizedBox(height: 9),
                itemBuilder: (context, idx) {
                  final asig = widget.activeSubjects[idx];
                  final progress = session?.subjectProgress(asig.codigo) ?? 0;

                  // Buscar si tiene parcial próximo registrado
                  String? nextPartialLabel;
                  for (final r in userReminders) {
                    if (r.codigoMateria == asig.codigo &&
                        r.tipo == AcademicEventKind.parcial &&
                        !r.completado) {
                      nextPartialLabel = r.titulo;
                      break;
                    }
                  }

                  return _DesktopSubjectItem(
                    asignatura: asig,
                    progressPercent: progress,
                    nextPartialLabel: nextPartialLabel ?? 'Parcial 1 • 25%',
                    onTap: () => widget.onOpenTemario(asig),
                    onDirectClaseViva: () => widget.onOpenClaseViva(asig.codigo),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 16),

          // 4. Pie del Sidebar (Perfil + Fullscreen)
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: const Color(0xFF13151B),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: const Color(0xFF1F232D)),
            ),
            child: Row(
              children: [
                MouseRegion(
                  cursor: SystemMouseCursors.click,
                  child: GestureDetector(
                    onTap: widget.onOpenStudentProfile,
                    child: HeaderMorphAvatar(
                      size: 36,
                      photoBytes: session?.userPhotoBytes,
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: MouseRegion(
                    cursor: SystemMouseCursors.click,
                    child: GestureDetector(
                      onTap: widget.onOpenStudentProfile,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            session?.displayName ?? 'Estudiante Ing. Energética',
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: const TextStyle(
                              fontSize: 12.5,
                              fontWeight: FontWeight.w700,
                              color: Colors.white,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            session?.email ?? AppConstants.defaultStudentEmail,
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 10,
                              color: p.textTertiary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 6),
                // Botón Pantalla Completa Nativa
                MouseRegion(
                  cursor: SystemMouseCursors.click,
                  child: Tooltip(
                    message: _isFullscreen
                        ? 'Salir de pantalla completa'
                        : 'Pantalla completa nativa',
                    child: GestureDetector(
                      onTap: _toggleFullscreen,
                      child: Container(
                        padding: const EdgeInsets.all(7),
                        decoration: BoxDecoration(
                          color: const Color(0xFF1A1D25),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: const Color(0xFF282D38)),
                        ),
                        child: Icon(
                          _isFullscreen
                              ? Icons.fullscreen_exit_rounded
                              : Icons.fullscreen_rounded,
                          size: 16,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _DesktopSubjectItem extends StatefulWidget {
  const _DesktopSubjectItem({
    required this.asignatura,
    required this.progressPercent,
    required this.nextPartialLabel,
    required this.onTap,
    required this.onDirectClaseViva,
  });

  final AsignaturaModel asignatura;
  final int progressPercent;
  final String nextPartialLabel;
  final VoidCallback onTap;
  final VoidCallback onDirectClaseViva;

  @override
  State<_DesktopSubjectItem> createState() => _DesktopSubjectItemState();
}

class _DesktopSubjectItemState extends State<_DesktopSubjectItem> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final asig = widget.asignatura;
    final progress = widget.progressPercent;

    return MouseRegion(
      cursor: SystemMouseCursors.click,
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      child: GestureDetector(
        onTap: widget.onTap,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 180),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
          decoration: BoxDecoration(
            color: _isHovered ? const Color(0xFF151821) : const Color(0xFF101217),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(
              color: _isHovered
                  ? const Color(0xFF30D158).o(0.5)
                  : const Color(0xFF1D212B),
              width: 1,
            ),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 5,
                      vertical: 2,
                    ),
                    decoration: BoxDecoration(
                      color: asig.accentColor.o(0.12),
                      borderRadius: BorderRadius.circular(5),
                    ),
                    child: Text(
                      asig.codigo,
                      style: mono(
                        fontSize: 9.5,
                        fontWeight: FontWeight.w700,
                        color: asig.accentColor,
                      ),
                    ),
                  ),
                  const SizedBox(width: 7),
                  Expanded(
                    child: Text(
                      asig.nombre,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                        color: _isHovered
                            ? const Color(0xFF30D158)
                            : p.textPrimary,
                      ),
                    ),
                  ),
                  const SizedBox(width: 4),
                  Tooltip(
                    message: 'Entrar a La Clase Viva',
                    child: GestureDetector(
                      onTap: widget.onDirectClaseViva,
                      child: Container(
                        padding: const EdgeInsets.all(3),
                        decoration: BoxDecoration(
                          color: const Color(0xFF1E222C),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: const Icon(
                          Icons.play_arrow_rounded,
                          size: 13,
                          color: Color(0xFF30D158),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 7),
              Row(
                children: [
                  Expanded(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(999),
                      child: LinearProgressIndicator(
                        value: (progress / 100).clamp(0.0, 1.0),
                        backgroundColor: const Color(0xFF1C2028),
                        valueColor: const AlwaysStoppedAnimation(Color(0xFF30D158)),
                        minHeight: 4,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    '$progress%',
                    style: mono(
                      fontSize: 10,
                      fontWeight: FontWeight.w700,
                      color: const Color(0xFF30D158),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 4),
              Text(
                widget.nextPartialLabel,
                style: mono(fontSize: 9.5, color: const Color(0xFFFF9F0A)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
