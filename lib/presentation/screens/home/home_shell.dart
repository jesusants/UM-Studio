import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/models/curriculum_models.dart';
import '../../../data/services/github_sync_service.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/header_morph_avatar.dart';
import '../../widgets/ios_primitives.dart';
import '../clase_viva/clase_viva_page.dart';
import '../clases/asignatura_temario_page.dart';
import 'tabs/calendario_tab.dart';
import 'tabs/clases_tab.dart';
import 'tabs/estudio_tab.dart';
import 'tabs/resumen_tab.dart';

/// Contenedor principal de UM STUDIO:
/// Header minimalista con emblema de Ingeniería Energética (`@unimagdalena.edu.co`),
/// estado de sincronización GitHub y 4 pestañas deslizables a 60/120fps
/// (`Hoy`, `Calendario`, `Clases`, `Estudio`).
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  final PageController _pageController = PageController();
  int _tab = 0;

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  void _goToTab(int index) {
    _pageController.animateToPage(
      index,
      duration: const Duration(milliseconds: 280),
      curve: kIosSpring,
    );
  }

  void _openClaseViva(String subjectId) {
    Navigator.of(context).push(ClaseVivaPage.route(subjectId));
  }

  void _openTemario(AsignaturaModel asignatura) {
    Navigator.of(context).push(AsignaturaTemarioPage.route(asignatura));
  }

  Future<void> _openStudentProfileSheet() async {
    final session = SessionScope.maybeOf(context);
    if (session == null) return;

    final p = context.palette;
    var adminTaps = 0;
    DateTime? lastTap;

    await showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      backgroundColor: p.card,
      shape: RoundedRectangleBorder(
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        side: BorderSide(color: p.cardBorder),
      ),
      builder: (sheetCtx) {
        return StatefulBuilder(
          builder: (ctx, setModalState) {
            final bottomInset = MediaQuery.viewInsetsOf(ctx).bottom;
            final user = session.currentUser;
            final currentCuat = session.cuatrimestreActual;

            return SafeArea(
              child: SingleChildScrollView(
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
                        GestureDetector(
                          onTap: () async {
                            final now = DateTime.now();
                            if (lastTap != null &&
                                now.difference(lastTap!).inMilliseconds > 2500) {
                              adminTaps = 0;
                            }
                            lastTap = now;
                            adminTaps++;
                            if (adminTaps >= 7) {
                              adminTaps = 0;
                              HapticFeedback.heavyImpact();
                              await _showSecretAdminSyncDialog(sheetCtx, session);
                            }
                          },
                          child: HeaderMorphAvatar(
                            size: 40,
                            photoBytes: session.userPhotoBytes,
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  PulseDot(color: p.green, size: 7),
                                  const SizedBox(width: 7),
                                  Expanded(
                                    child: Text(
                                      'PERFIL INGENIERÍA ENERGÉTICA',
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                      style: sectionMicroStyle(p),
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 4),
                              Text(
                                session.displayName,
                                style: TextStyle(
                                  fontSize: 18,
                                  fontWeight: FontWeight.w700,
                                  color: p.textPrimary,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 2),
                    Text(
                      session.email,
                      style: mono(fontSize: 12, color: p.green),
                    ),
                    const SizedBox(height: 14),
                    const IosHairline(),
                    const SizedBox(height: 12),

                    Row(
                      children: [
                        Text(
                          'CUATRIMESTRE ACTIVO (PLAN 8108)',
                          style: sectionMicroStyle(p),
                        ),
                        const Spacer(),
                        Text(
                          'Cuatrimestre $currentCuat de 12',
                          style: mono(
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                            color: p.green,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 10),
                    Wrap(
                      spacing: 7,
                      runSpacing: 7,
                      children: List.generate(12, (idx) {
                        final c = idx + 1;
                        final selected = c == currentCuat;
                        return TapScale(
                          onTap: () async {
                            await session.setCuatrimestreActual(c);
                            setModalState(() {});
                          },
                          child: Container(
                            width: 38,
                            height: 32,
                            alignment: Alignment.center,
                            decoration: BoxDecoration(
                              color: selected ? p.green : p.elevated,
                              borderRadius: BorderRadius.circular(10),
                              border: Border.all(
                                color: selected ? p.green : p.cardBorder,
                              ),
                            ),
                            child: Text(
                              '$c',
                              style: mono(
                                fontSize: 12,
                                fontWeight: FontWeight.w600,
                                color: selected
                                    ? Colors.black
                                    : p.textSecondary,
                              ),
                            ),
                          ),
                        );
                      }),
                    ),
                    const SizedBox(height: 16),

                    if (user != null) ...[
                      TapScale(
                        onTap: () async {
                          final ok = await session.syncService.flushNow(
                            user,
                          );
                          if (sheetCtx.mounted) {
                            Navigator.of(sheetCtx).pop();
                          }
                          if (mounted) {
                            showIosToast(
                              context,
                              ok
                                  ? 'Sincronizado con UM Cloud'
                                  : 'Guardado localmente (pendiente de red)',
                              accentColor: ok ? p.green : p.indigo,
                            );
                          }
                        },
                        child: Container(
                          width: double.infinity,
                          padding: const EdgeInsets.symmetric(
                            vertical: 12,
                          ),
                          alignment: Alignment.center,
                          decoration: BoxDecoration(
                            color: p.green,
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: const Text(
                            'Sincronizar ahora',
                            style: TextStyle(
                              fontSize: 12.5,
                              fontWeight: FontWeight.w700,
                              color: Colors.black,
                            ),
                          ),
                        ),
                      ),
                    ],

                    if (session.isAuthenticated) ...[
                      const SizedBox(height: 12),
                      TapScale(
                        onTap: () async {
                          Navigator.of(sheetCtx).pop();
                          await session.logout();
                        },
                        child: Container(
                          width: double.infinity,
                          padding: const EdgeInsets.symmetric(vertical: 10),
                          alignment: Alignment.center,
                          decoration: BoxDecoration(
                            color: p.elevated,
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(color: p.cardBorder),
                          ),
                          child: Text(
                            'Cambiar de cuenta / Cerrar sesión',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                              color: p.orange,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }

  Future<void> _showSecretAdminSyncDialog(
    BuildContext context,
    InstitutionalSessionController session,
  ) async {
    final p = context.palette;
    final pinCtrl = TextEditingController();
    var pinError = false;

    final authorized = await showDialog<bool>(
      context: context,
      builder: (dlgCtx) => StatefulBuilder(
        builder: (ctx, setDlgState) => AlertDialog(
          backgroundColor: p.card,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
            side: BorderSide(color: p.cardBorder),
          ),
          title: Row(
            children: [
              Icon(Icons.admin_panel_settings_rounded, size: 20, color: p.green),
              const SizedBox(width: 8),
              Text(
                'Acceso Técnico Admin',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w700,
                  color: p.textPrimary,
                ),
              ),
            ],
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Ingresa el PIN maestro de administración (Plan 8108) para configurar el Token PAT de GitHub o endpoint.',
                style: TextStyle(fontSize: 12.5, color: p.textSecondary),
              ),
              const SizedBox(height: 14),
              TextField(
                controller: pinCtrl,
                obscureText: true,
                autofocus: true,
                keyboardType: TextInputType.number,
                style: mono(fontSize: 14, color: p.textPrimary),
                decoration: InputDecoration(
                  isDense: true,
                  filled: true,
                  fillColor: p.background.o(0.45),
                  hintText: 'PIN Maestro...',
                  hintStyle: mono(fontSize: 12, color: p.textTertiary),
                  errorText: pinError ? 'PIN incorrecto' : null,
                  contentPadding: const EdgeInsets.all(12),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: p.cardBorder),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: p.green),
                  ),
                ),
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(dlgCtx).pop(false),
              child: Text('Cancelar', style: TextStyle(color: p.textSecondary)),
            ),
            TapScale(
              onTap: () {
                if (pinCtrl.text.trim() == '8108') {
                  Navigator.of(dlgCtx).pop(true);
                } else {
                  setDlgState(() => pinError = true);
                }
              },
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: p.green,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Text(
                  'Entrar',
                  style: TextStyle(
                    fontSize: 12.5,
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

    if (authorized != true || !context.mounted) return;

    final tokenCtrl =
        TextEditingController(text: session.syncService.effectiveToken);
    await showDialog<void>(
      context: context,
      builder: (dlgCtx) => AlertDialog(
        backgroundColor: p.card,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: BorderSide(color: p.cardBorder),
        ),
        title: Text(
          'Configuración Técnica PAT',
          style: TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.w700,
            color: p.textPrimary,
          ),
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Token Personal de GitHub para sincronización en la nube:',
              style: TextStyle(fontSize: 12, color: p.textSecondary),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: tokenCtrl,
              obscureText: true,
              style: mono(fontSize: 12, color: p.textPrimary),
              decoration: InputDecoration(
                isDense: true,
                filled: true,
                fillColor: p.background.o(0.45),
                hintText: 'github_pat_...',
                contentPadding: const EdgeInsets.all(12),
                enabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide(color: p.cardBorder),
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide(color: p.green),
                ),
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(dlgCtx).pop(),
            child: Text('Cerrar', style: TextStyle(color: p.textSecondary)),
          ),
          TapScale(
            onTap: () async {
              await session.syncService.setCustomGitHubToken(tokenCtrl.text);
              if (dlgCtx.mounted) Navigator.of(dlgCtx).pop();
              if (context.mounted) {
                showIosToast(context, 'Token PAT de GitHub actualizado');
              }
            },
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              decoration: BoxDecoration(
                color: p.green,
                borderRadius: BorderRadius.circular(10),
              ),
              child: const Text(
                'Guardar Token',
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: FontWeight.w700,
                  color: Colors.black,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.of(context).isDark;
    final session = SessionScope.maybeOf(context);
    final screenWidth = MediaQuery.sizeOf(context).width;
    final wide = screenWidth > AppConstants.maxPhoneViewportWidth;

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: isDark ? SystemUiOverlayStyle.light : SystemUiOverlayStyle.dark,
      child: Scaffold(
        backgroundColor: p.background,
        body: Center(
          child: Container(
            width: math.min(screenWidth, AppConstants.maxPhoneViewportWidth),
            decoration: BoxDecoration(
              color: p.background,
              border: wide
                  ? Border.symmetric(
                      vertical: BorderSide(color: p.cardBorder.o(0.9)),
                    )
                  : null,
            ),
            child: Column(
              children: [
                _Header(
                  syncStatus:
                      session?.syncService.status ?? GitHubSyncStatus.idle,
                  onTapIdentity: _openStudentProfileSheet,
                ),
                Expanded(
                  child: PageView(
                    controller: _pageController,
                    physics: const BouncingScrollPhysics(),
                    onPageChanged: (i) => setState(() => _tab = i),
                    children: [
                      ResumenTab(onOpenClaseViva: _openClaseViva),
                      CalendarioTab(onOpenClaseViva: _openClaseViva),
                      const ClasesTab(),
                      EstudioTab(
                        onOpenClaseViva: _openClaseViva,
                        onOpenTemario: _openTemario,
                      ),
                    ],
                  ),
                ),
                _BottomNav(current: _tab, onSelect: _goToTab),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Header extends StatelessWidget {
  const _Header({
    required this.syncStatus,
    required this.onTapIdentity,
  });

  final GitHubSyncStatus syncStatus;
  final VoidCallback onTapIdentity;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final top = MediaQuery.paddingOf(context).top;
    final session = SessionScope.maybeOf(context);

    late final Color dotColor;
    late final String badgeText;
    switch (syncStatus) {
      case GitHubSyncStatus.syncing:
        dotColor = p.indigo;
        badgeText = 'Sync...';
      case GitHubSyncStatus.synced:
        dotColor = p.green;
        badgeText = 'UM Cloud • Sync';
      case GitHubSyncStatus.error:
        dotColor = p.orange;
        badgeText = 'Local • Retry';
      case GitHubSyncStatus.localOnly:
      case GitHubSyncStatus.idle:
        dotColor = p.green;
        badgeText = 'Ing. Energética';
    }

    return Container(
      padding: EdgeInsets.fromLTRB(20, 14 + top, 20, 13),
      decoration: BoxDecoration(
        color: p.glass,
        border: Border(bottom: BorderSide(color: p.cardBorder.o(0.8))),
      ),
      child: Row(
        children: [
          HeaderMorphAvatar(
            size: 36,
            photoBytes: session?.userPhotoBytes,
            onTap: () {
              // Alternancia automática e interactiva con lógica anti-tilde
            },
          ),
          const SizedBox(width: 10),
          Expanded(
            child: TapScale(
              onTap: onTapIdentity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    AppConstants.appTitle,
                    style: TextStyle(
                      fontSize: 14,
                      height: 1,
                      fontWeight: FontWeight.w600,
                      letterSpacing: -0.3,
                      color: p.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 3),
                  Text(
                    AppConstants.programSubtitle,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(fontSize: 11, color: p.textSecondary),
                  ),
                ],
              ),
            ),
          ),
          const ThemeToggleButton(),
          const SizedBox(width: 8),
          TapScale(
            onTap: onTapIdentity,
            child: Container(
              padding: const EdgeInsets.symmetric(
                horizontal: 10,
                vertical: 4,
              ),
              decoration: BoxDecoration(
                color: p.card,
                borderRadius: BorderRadius.circular(999),
                border: Border.all(color: p.cardBorder),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  PulseDot(color: dotColor),
                  const SizedBox(width: 6),
                  Text(
                    badgeText,
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w500,
                      color: p.textSecondary,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _BottomNav extends StatelessWidget {
  const _BottomNav({required this.current, required this.onSelect});

  final int current;
  final ValueChanged<int> onSelect;

  static const _items = [
    (Icons.today_rounded, 'Hoy'),
    (Icons.calendar_month_rounded, 'Calendario'),
    (Icons.school_rounded, 'Clases'),
    (Icons.menu_book_rounded, 'Estudio'),
  ];

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    return Container(
      decoration: BoxDecoration(
        color: p.glass,
        border: Border(top: BorderSide(color: p.cardBorder.o(0.8))),
      ),
      child: SafeArea(
        top: false,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 8, 8),
          child: Row(
            children: List.generate(_items.length, (i) {
              final (icon, label) = _items[i];
              final selected = i == current;
              final color = selected ? p.textPrimary : p.textTertiary;
              return Expanded(
                child: TapScale(
                  onTap: () => onSelect(i),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 280),
                    curve: kIosSpring,
                    margin: const EdgeInsets.symmetric(horizontal: 2),
                    padding: const EdgeInsets.symmetric(vertical: 6),
                    decoration: BoxDecoration(
                      color: selected ? p.elevated : Colors.transparent,
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(icon, size: 20, color: color),
                        const SizedBox(height: 2),
                        Text(
                          label,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 9.5,
                            fontWeight:
                                selected ? FontWeight.w600 : FontWeight.w500,
                            color: color,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              );
            }),
          ),
        ),
      ),
    );
  }
}
