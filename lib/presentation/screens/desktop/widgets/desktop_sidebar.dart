import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/constants/app_constants.dart';
import '../../../../core/theme/app_theme.dart';
import '../../../../core/utils/fullscreen/fullscreen_helper.dart';
import '../../../../data/models/curriculum_models.dart';
import '../../../providers/app_scopes.dart';
import '../../../widgets/ios_primitives.dart';
import '../../../widgets/admin_env_console_modal.dart';
import '../../../widgets/unimagdalena_portal_button.dart';
import '../desktop_theme_tokens.dart';

/// Sidebar izquierdo (24% del ancho) para el Dashboard de Escritorio:
/// - Barra superior de marca institucional y botón animado conmutador de tema (Sol/Luna)
/// - Selector deslizante horizontal compacto de Cuatrimestres (1 al 12)
/// - Lista inercial de asignaturas con hover dinámico y selección Maestro-Detalle
/// - Pie con perfil institucional limpio y toggle de pantalla completa nativa
class DesktopSidebar extends StatefulWidget {
  const DesktopSidebar({
    super.key,
    required this.selectedCuatrimestre,
    required this.onSelectCuatrimestre,
    required this.subjects,
    required this.selectedSubject,
    required this.onSelectSubject,
    required this.onOpenStudentProfile,
    this.onEditMatricula,
    this.isTimerVisible,
    this.onToggleTimer,
  });

  final int selectedCuatrimestre;
  final ValueChanged<int> onSelectCuatrimestre;
  final List<AsignaturaModel> subjects;
  final AsignaturaModel? selectedSubject;
  final ValueChanged<AsignaturaModel> onSelectSubject;
  final VoidCallback onOpenStudentProfile;
  final VoidCallback? onEditMatricula;
  final bool? isTimerVisible;
  final VoidCallback? onToggleTimer;

  @override
  State<DesktopSidebar> createState() => _DesktopSidebarState();
}

class _DesktopSidebarState extends State<DesktopSidebar> {
  bool _isFullscreen = false;

  void _toggleFullscreen() {
    HapticFeedback.lightImpact();
    FullscreenHelper.toggle();
    setState(() {
      _isFullscreen = !_isFullscreen;
    });
  }

  @override
  Widget build(BuildContext context) {
    final tokens = DesktopThemeTokens.of(context);
    final themeController = ThemeScope.maybeOf(context);
    final session = SessionScope.maybeOf(context);
    final userName = session?.currentUser?.nombre ?? 'Estudiante Unimagdalena';
    final userEmail = session?.email ?? 'alumno@unimagdalena.edu.co';

    return Container(
      decoration: BoxDecoration(
        color: tokens.surface,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: tokens.border, width: 1),
        boxShadow: [
          BoxShadow(
            color: tokens.shadowColor,
            blurRadius: 20,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      padding: const EdgeInsets.all(18),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // 1. Barra Superior de Marca & Conmutador de Tema (Sol / Luna)
          Row(
            children: [
              Container(
                width: 38,
                height: 38,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: tokens.accentGreen.o(0.12),
                  border: Border.all(
                    color: tokens.accentGreen.o(0.40),
                    width: 1.5,
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: tokens.accentGreen.o(0.18),
                      blurRadius: 8,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: Center(
                  child: Image.asset(
                    AppConstants.programLogoAsset,
                    width: 22,
                    height: 22,
                    errorBuilder: (_, __, ___) => Icon(
                      Icons.bolt_rounded,
                      color: tokens.accentGreen,
                      size: 20,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'UM STUDIO',
                      maxLines: 1,
                      softWrap: false,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        fontSize: 13.5,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.2,
                        color: tokens.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        PulseDot(color: tokens.accentGreen, size: 6),
                        const SizedBox(width: 5),
                        Flexible(
                          child: Text(
                            'Sincronizado',
                            maxLines: 1,
                            softWrap: false,
                            overflow: TextOverflow.ellipsis,
                            style: mono(
                              fontSize: 9.5,
                              fontWeight: FontWeight.w600,
                              color: tokens.accentGreen,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 6),
              if (kIsWeb && session?.isAdmin == true) ...[
                TapScale(
                  onTap: () {
                    HapticFeedback.selectionClick();
                    AdminEnvConsoleModal.show(context);
                  },
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 5),
                    decoration: BoxDecoration(
                      color: tokens.accentGreen.o(0.15),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: tokens.accentGreen.o(0.50), width: 1.2),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        PulseDot(color: tokens.accentGreen, size: 5),
                        const SizedBox(width: 4),
                        Text(
                          '⚡ Admin',
                          style: mono(
                            fontSize: 9.5,
                            fontWeight: FontWeight.w800,
                            color: tokens.accentGreen,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 6),
              ],
              // Botón Expandible Módulo Estudiantes Unimagdalena (AyRe)
              const UnimagdalenaPortalButton(),
              const SizedBox(width: 6),
              // Conmutador de Tema Dual Dinámico (Sol / Luna)
              _ThemeTogglePill(
                isDark: tokens.isDark,
                onToggle: () {
                  HapticFeedback.lightImpact();
                  themeController?.toggle();
                },
                tokens: tokens,
              ),
            ],
          ),
          const SizedBox(height: 16),

          // 2. Selector Deslizante de Cuatrimestres (1 al 12)
          Text(
            'CUATRIMESTRE',
            style: mono(
              fontSize: 9.5,
              fontWeight: FontWeight.w700,
              letterSpacing: 1.0,
              color: tokens.textSecondary,
            ),
          ),
          const SizedBox(height: 8),
          SizedBox(
            height: 32,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              physics: const BouncingScrollPhysics(),
              itemCount: 13,
              separatorBuilder: (_, __) => const SizedBox(width: 6),
              itemBuilder: (context, index) {
                final cuat = index;
                final isSelected = cuat == widget.selectedCuatrimestre;
                final label = cuat == 0 ? '★ Matrícula' : 'C$cuat';
                return TapScale(
                  onTap: () {
                    HapticFeedback.selectionClick();
                    widget.onSelectCuatrimestre(cuat);
                  },
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 180),
                    padding: const EdgeInsets.symmetric(horizontal: 11),
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: isSelected
                          ? tokens.accentGreen
                          : tokens.surfaceElevated,
                      borderRadius: BorderRadius.circular(10),
                      border: Border.all(
                        color: isSelected
                            ? tokens.accentGreen
                            : tokens.border,
                        width: 1,
                      ),
                    ),
                    child: Text(
                      label,
                      style: mono(
                        fontSize: 11,
                        fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
                        color: isSelected
                            ? (tokens.isDark ? Colors.black : Colors.white)
                            : tokens.textSecondary,
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
          const SizedBox(height: 16),

          // 3. Encabezado de Materias del Cuatrimestre
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Flexible(
                child: Text(
                  widget.selectedCuatrimestre == 0
                      ? 'MATRÍCULA ACTIVA (${widget.subjects.length})'
                      : 'ASIGNATURAS (${widget.subjects.length})',
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w700,
                    letterSpacing: 1.0,
                    color: tokens.textSecondary,
                  ),
                ),
              ),
              const SizedBox(width: 6),
              if (widget.onEditMatricula != null)
                TapScale(
                  onTap: widget.onEditMatricula,
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 2.5),
                    decoration: BoxDecoration(
                      color: tokens.accentGreen.o(0.12),
                      borderRadius: BorderRadius.circular(6),
                      border: Border.all(color: tokens.accentGreen.o(0.35)),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.edit_note_rounded, size: 12, color: tokens.accentGreen),
                        const SizedBox(width: 3),
                        Text(
                          'Editar Matrícula',
                          style: mono(
                            fontSize: 9,
                            fontWeight: FontWeight.w700,
                            color: tokens.accentGreen,
                          ),
                        ),
                      ],
                    ),
                  ),
                )
              else
                Text(
                  widget.selectedCuatrimestre == 0
                      ? 'MATRÍCULA'
                      : 'C${widget.selectedCuatrimestre}',
                  style: mono(
                    fontSize: 9.5,
                    fontWeight: FontWeight.w600,
                    color: tokens.textTertiary,
                  ),
                ),
            ],
          ),
          const SizedBox(height: 10),

          // 4. Lista Inercial de Asignaturas con Hover Suave
          Expanded(
            child: widget.subjects.isEmpty
                ? Center(
                    child: Text(
                      'Sin asignaturas registradas en C${widget.selectedCuatrimestre}',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 12,
                        color: tokens.textSecondary,
                      ),
                    ),
                  )
                : ListView.separated(
                    physics: const BouncingScrollPhysics(),
                    itemCount: widget.subjects.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 8),
                    itemBuilder: (context, index) {
                      final subject = widget.subjects[index];
                      final isSelected =
                          widget.selectedSubject?.codigo == subject.codigo;
                      final progress = session?.subjectProgress(subject.codigo) ?? 0;

                      return _SubjectDesktopCard(
                        subject: subject,
                        progress: progress,
                        isSelected: isSelected,
                        tokens: tokens,
                        onTap: () {
                          HapticFeedback.lightImpact();
                          widget.onSelectSubject(subject);
                        },
                      );
                    },
                  ),
          ),
          const SizedBox(height: 12),

          // 5. Pie del Panel: Perfil Simplificado y Pantalla Completa
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
            decoration: BoxDecoration(
              color: tokens.surfaceElevated,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: tokens.border),
            ),
            child: Row(
              children: [
                TapScale(
                  onTap: widget.onOpenStudentProfile,
                  child: Container(
                    width: 32,
                    height: 32,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      gradient: LinearGradient(
                        colors: [
                          tokens.accentIndigo,
                          tokens.accentGreen,
                        ],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ),
                    ),
                    child: Center(
                      child: Text(
                        userName.isNotEmpty ? userName[0].toUpperCase() : 'U',
                        style: const TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.w800,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 9),
                Expanded(
                  child: TapScale(
                    onTap: widget.onOpenStudentProfile,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
                          userName,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w700,
                            letterSpacing: -0.1,
                            color: tokens.textPrimary,
                          ),
                        ),
                        Text(
                          userEmail,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: mono(
                            fontSize: 9.5,
                            color: tokens.textSecondary,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 6),
                // Botón Pantalla Completa
                TapScale(
                  onTap: _toggleFullscreen,
                  child: Container(
                    padding: const EdgeInsets.all(7),
                    decoration: BoxDecoration(
                      color: tokens.surface,
                      borderRadius: BorderRadius.circular(9),
                      border: Border.all(color: tokens.border),
                    ),
                    child: Icon(
                      _isFullscreen
                          ? Icons.fullscreen_exit_rounded
                          : Icons.fullscreen_rounded,
                      size: 16,
                      color: tokens.textSecondary,
                    ),
                  ),
                ),
                if (widget.onToggleTimer != null) ...[
                  const SizedBox(width: 5),
                  TapScale(
                    onTap: widget.onToggleTimer,
                    child: Tooltip(
                      message: (widget.isTimerVisible ?? true)
                          ? 'Ocultar temporizador Pomodoro (P)'
                          : 'Mostrar temporizador Pomodoro (P)',
                      child: Container(
                        padding: const EdgeInsets.all(7),
                        decoration: BoxDecoration(
                          color: (widget.isTimerVisible ?? true)
                              ? tokens.surface
                              : tokens.accentIndigo.o(0.12),
                          borderRadius: BorderRadius.circular(9),
                          border: Border.all(
                            color: (widget.isTimerVisible ?? true)
                                ? tokens.border
                                : tokens.accentIndigo.o(0.4),
                          ),
                        ),
                        child: Icon(
                          (widget.isTimerVisible ?? true)
                              ? Icons.timer_outlined
                              : Icons.timer_off_outlined,
                          size: 16,
                          color: (widget.isTimerVisible ?? true)
                              ? tokens.textSecondary
                              : tokens.accentIndigo,
                        ),
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }
}

/// Píldora animada para alternar entre Modo Oscuro y Modo Claro
class _ThemeTogglePill extends StatelessWidget {
  const _ThemeTogglePill({
    required this.isDark,
    required this.onToggle,
    required this.tokens,
  });

  final bool isDark;
  final VoidCallback onToggle;
  final DesktopThemeTokens tokens;

  @override
  Widget build(BuildContext context) {
    return TapScale(
      onTap: onToggle,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 5),
        decoration: BoxDecoration(
          color: tokens.surfaceElevated,
          borderRadius: BorderRadius.circular(999),
          border: Border.all(color: tokens.border),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            AnimatedSwitcher(
              duration: const Duration(milliseconds: 220),
              transitionBuilder: (child, anim) => RotationTransition(
                turns: anim,
                child: FadeTransition(opacity: anim, child: child),
              ),
              child: Icon(
                isDark ? Icons.light_mode_rounded : Icons.dark_mode_rounded,
                key: ValueKey(isDark),
                size: 13,
                color: isDark ? const Color(0xFFFFD60A) : tokens.accentIndigo,
              ),
            ),
            const SizedBox(width: 5),
            Text(
              isDark ? 'Claro' : 'Oscuro',
              style: mono(
                fontSize: 10,
                fontWeight: FontWeight.w600,
                color: tokens.textSecondary,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Tarjeta de Asignatura con Hover dinámico y soporte de selección Maestro-Detalle
class _SubjectDesktopCard extends StatefulWidget {
  const _SubjectDesktopCard({
    required this.subject,
    required this.progress,
    required this.isSelected,
    required this.tokens,
    required this.onTap,
  });

  final AsignaturaModel subject;
  final int progress;
  final bool isSelected;
  final DesktopThemeTokens tokens;
  final VoidCallback onTap;

  @override
  State<_SubjectDesktopCard> createState() => _SubjectDesktopCardState();
}

class _SubjectDesktopCardState extends State<_SubjectDesktopCard> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    final t = widget.tokens;
    final subject = widget.subject;
    final isSelected = widget.isSelected;

    final borderColor = isSelected
        ? t.accentGreen
        : (_isHovered ? t.accentGreen.o(0.5) : t.border);
    final bgColor = isSelected
        ? t.accentGreen.o(t.isDark ? 0.12 : 0.08)
        : (_isHovered ? t.surfaceElevated : t.surface);

    return MouseRegion(
      onEnter: (_) => setState(() => _isHovered = true),
      onExit: (_) => setState(() => _isHovered = false),
      cursor: SystemMouseCursors.click,
      child: GestureDetector(
        onTap: widget.onTap,
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 160),
          transform: Matrix4.translationValues(0, _isHovered ? -2 : 0, 0),
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
          decoration: BoxDecoration(
            color: bgColor,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: borderColor, width: isSelected ? 1.4 : 1.0),
            boxShadow: _isHovered || isSelected
                ? [
                    BoxShadow(
                      color: t.accentGreen.o(isSelected ? 0.12 : 0.06),
                      blurRadius: 10,
                      offset: const Offset(0, 3),
                    ),
                  ]
                : null,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1.5),
                    decoration: BoxDecoration(
                      color: t.surfaceElevated,
                      borderRadius: BorderRadius.circular(5),
                      border: Border.all(color: t.borderSubtle),
                    ),
                    child: Text(
                      subject.codigo,
                      style: mono(
                        fontSize: 9,
                        fontWeight: FontWeight.w600,
                        color: t.textSecondary,
                      ),
                    ),
                  ),
                  const Spacer(),
                  Text(
                    '${subject.creditos} créd.',
                    style: mono(
                      fontSize: 9.5,
                      fontWeight: FontWeight.w500,
                      color: t.textTertiary,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 5),
              Text(
                subject.nombre,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w700,
                  letterSpacing: -0.2,
                  height: 1.25,
                  color: isSelected ? t.accentGreen : t.textPrimary,
                ),
              ),
              const SizedBox(height: 7),
              Row(
                children: [
                  Expanded(
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(999),
                      child: LinearProgressIndicator(
                        value: (widget.progress / 100).clamp(0.0, 1.0),
                        minHeight: 4,
                        backgroundColor: t.border,
                        valueColor: AlwaysStoppedAnimation<Color>(
                          widget.progress > 0 ? t.accentGreen : t.border,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    '${widget.progress}%',
                    style: mono(
                      fontSize: 9.5,
                      fontWeight: FontWeight.w700,
                      color: widget.progress > 0 ? t.accentGreen : t.textTertiary,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
