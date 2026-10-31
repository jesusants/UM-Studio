import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/services/github_sync_service.dart';
import '../../providers/app_scopes.dart';
import '../../widgets/ios_primitives.dart';
import '../clase_viva/clase_viva_page.dart';
import 'tabs/calendario_tab.dart';
import 'tabs/estudio_tab.dart';
import 'tabs/resumen_tab.dart';

/// Contenedor principal de UM STUDIO:
/// Header con perfil de Ingeniería Energética (`@unimagdalena.edu.co`),
/// estado de sincronización GitHub, barra de Uso Diario (`borderRadius: 999`),
/// 3 pestañas deslizables a 60/120fps y barra inferior iOS.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  final PageController _pageController = PageController();
  int _fallbackUsage = AppConstants.initialDailyUsage;
  int _tab = 0;

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  void _addUsage(int amount) {
    final session = SessionScope.maybeOf(context);
    if (session != null) {
      session.addUsageQuota(amount);
    } else {
      setState(() {
        _fallbackUsage =
            (_fallbackUsage + amount).clamp(0, AppConstants.maxDailyUsage);
      });
    }
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

  Future<void> _openStudentProfileSheet() async {
    final session = SessionScope.maybeOf(context);
    if (session == null) return;

    final p = context.palette;
    final tokenCtrl = TextEditingController();
    var showTokenField = false;

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
                        PulseDot(color: p.green, size: 8),
                        const SizedBox(width: 8),
                        Text(
                          'PERFIL INGENIERÍA ENERGÉTICA',
                          style: sectionMicroStyle(p),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Text(
                      session.displayName,
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w700,
                        color: p.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      session.email,
                      style: mono(fontSize: 12, color: p.green),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'Archivo en GitHub: db/users/${session.username}.json',
                      style: mono(fontSize: 10.5, color: p.textSecondary),
                    ),
                    const SizedBox(height: 14),
                    const IosHairline(),
                    const SizedBox(height: 12),

                    Row(
                      children: [
                        Text(
                          'CUATRIMESTRE ACTIVO',
                          style: sectionMicroStyle(p),
                        ),
                        const Spacer(),
                        Text(
                          'Cuatrimestre $currentCuat',
                          style: mono(
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                            color: p.green,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    SingleChildScrollView(
                      scrollDirection: Axis.horizontal,
                      physics: const BouncingScrollPhysics(),
                      child: Row(
                        children: List.generate(12, (idx) {
                          final c = idx + 1;
                          final selected = c == currentCuat;
                          return Padding(
                            padding: const EdgeInsets.only(right: 6),
                            child: TapScale(
                              onTap: () async {
                                await session.setCuatrimestreActual(c);
                                setModalState(() {});
                              },
                              child: Container(
                                width: 34,
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
                            ),
                          );
                        }),
                      ),
                    ),
                    const SizedBox(height: 14),

                    if (user != null) ...[
                      Row(
                        children: [
                          Expanded(
                            child: TapScale(
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
                                        ? 'Sincronizado con jesusants/UM-Studio'
                                        : 'Guardado localmente (pendiente token/red)',
                                    accentColor: ok ? p.green : p.indigo,
                                  );
                                }
                              },
                              child: Container(
                                padding: const EdgeInsets.symmetric(
                                  vertical: 11,
                                ),
                                alignment: Alignment.center,
                                decoration: BoxDecoration(
                                  color: p.green,
                                  borderRadius: BorderRadius.circular(12),
                                ),
                                child: const Text(
                                  'Sincronizar con GitHub',
                                  style: TextStyle(
                                    fontSize: 12.5,
                                    fontWeight: FontWeight.w700,
                                    color: Colors.black,
                                  ),
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(width: 10),
                          TapScale(
                            onTap: () => setModalState(
                              () => showTokenField = !showTokenField,
                            ),
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 12,
                                vertical: 11,
                              ),
                              decoration: BoxDecoration(
                                color: p.elevated,
                                borderRadius: BorderRadius.circular(12),
                                border: Border.all(color: p.cardBorder),
                              ),
                              child: Icon(
                                Icons.vpn_key_outlined,
                                size: 17,
                                color: p.textSecondary,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],

                    if (showTokenField) ...[
                      const SizedBox(height: 12),
                      TextField(
                        controller: tokenCtrl,
                        obscureText: true,
                        autocorrect: false,
                        style: mono(fontSize: 12, color: p.textPrimary),
                        decoration: InputDecoration(
                          isDense: true,
                          filled: true,
                          fillColor: p.background.o(0.45),
                          hintText: 'Token PAT de GitHub (github_pat_...)',
                          hintStyle: mono(fontSize: 11.5, color: p.textTertiary),
                          contentPadding: const EdgeInsets.all(11),
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
                      const SizedBox(height: 8),
                      TapScale(
                        onTap: () async {
                          await session.syncService.setCustomGitHubToken(
                            tokenCtrl.text,
                          );
                          setModalState(() => showTokenField = false);
                          if (mounted) {
                            showIosToast(context, 'Token GitHub actualizado');
                          }
                        },
                        child: Text(
                          'Guardar Token PAT',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: p.green,
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

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final isDark = ThemeScope.of(context).isDark;
    final session = SessionScope.maybeOf(context);
    final currentUsage = session?.dailyUsage ?? _fallbackUsage;
    final maxUsage = session?.maxDailyUsage ?? AppConstants.maxDailyUsage;
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
                  initials: session?.initials ?? 'UM',
                  syncStatus:
                      session?.syncService.status ?? GitHubSyncStatus.idle,
                  usage: currentUsage,
                  maxUsage: maxUsage,
                  onMerit: () => _addUsage(1),
                  onTapIdentity: _openStudentProfileSheet,
                ),
                Expanded(
                  child: PageView(
                    controller: _pageController,
                    physics: const BouncingScrollPhysics(),
                    onPageChanged: (i) => setState(() => _tab = i),
                    children: [
                      ResumenTab(
                        onOpenClaseViva: _openClaseViva,
                        onCompleteBlock: () => _addUsage(2),
                      ),
                      CalendarioTab(onOpenClaseViva: _openClaseViva),
                      EstudioTab(onOpenClaseViva: _openClaseViva),
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
    required this.initials,
    required this.syncStatus,
    required this.usage,
    required this.maxUsage,
    required this.onMerit,
    required this.onTapIdentity,
  });

  final String initials;
  final GitHubSyncStatus syncStatus;
  final int usage;
  final int maxUsage;
  final VoidCallback onMerit;
  final VoidCallback onTapIdentity;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final top = MediaQuery.paddingOf(context).top;

    late final Color dotColor;
    late final String badgeText;
    switch (syncStatus) {
      case GitHubSyncStatus.syncing:
        dotColor = p.indigo;
        badgeText = 'Sync...';
      case GitHubSyncStatus.synced:
        dotColor = p.green;
        badgeText = 'GitHub • Sync';
      case GitHubSyncStatus.error:
        dotColor = p.orange;
        badgeText = 'Local • Retry';
      case GitHubSyncStatus.localOnly:
      case GitHubSyncStatus.idle:
        dotColor = p.green;
        badgeText = 'Ing. Energética';
    }

    return Container(
      padding: EdgeInsets.fromLTRB(20, 16 + top, 20, 14),
      decoration: BoxDecoration(
        color: p.glass,
        border: Border(bottom: BorderSide(color: p.cardBorder.o(0.8))),
      ),
      child: Column(
        children: [
          Row(
            children: [
              TapScale(
                onTap: onTapIdentity,
                child: Container(
                  width: 32,
                  height: 32,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: p.elevated,
                    shape: BoxShape.circle,
                    border: Border.all(color: p.strongBorder),
                  ),
                  child: Text(
                    initials,
                    style: TextStyle(
                      fontSize: 11.5,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.3,
                      color: p.textPrimary,
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
          const SizedBox(height: 12),
          _DailyUsageCard(usage: usage, maxUsage: maxUsage, onMerit: onMerit),
        ],
      ),
    );
  }
}

class _DailyUsageCard extends StatelessWidget {
  const _DailyUsageCard({
    required this.usage,
    required this.maxUsage,
    required this.onMerit,
  });

  final int usage;
  final int maxUsage;
  final VoidCallback onMerit;

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final barColor =
        usage >= AppConstants.warningDailyThreshold ? p.orange : p.green;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: p.card,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: p.cardBorder),
      ),
      child: Column(
        children: [
          Row(
            children: [
              Icon(Icons.bolt_rounded, size: 15, color: p.green),
              const SizedBox(width: 4),
              Text(
                'USO DIARIO',
                style: TextStyle(
                  fontSize: 11,
                  letterSpacing: 1,
                  fontWeight: FontWeight.w500,
                  color: p.textSecondary,
                ),
              ),
              const Spacer(),
              Text.rich(
                TextSpan(
                  style: mono(fontSize: 11, color: p.textSecondary),
                  children: [
                    TextSpan(
                      text: '$usage',
                      style: TextStyle(
                        color: p.textPrimary,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                    TextSpan(text: ' / $maxUsage consultas'),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          ProgressBar(value: usage / maxUsage, color: barColor, height: 6),
          const SizedBox(height: 6),
          Row(
            children: [
              Expanded(
                child: Text(
                  'Completa bloques de estudio para ampliar tu cupo diario',
                  style: TextStyle(fontSize: 10, color: p.textTertiary),
                ),
              ),
              TapScale(
                onTap: onMerit,
                child: Text(
                  '+ Mérito',
                  style: TextStyle(
                    fontSize: 10,
                    fontWeight: FontWeight.w500,
                    color: p.green,
                  ),
                ),
              ),
            ],
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
          padding: const EdgeInsets.fromLTRB(12, 8, 12, 8),
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
                    margin: const EdgeInsets.symmetric(horizontal: 4),
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
                          style: TextStyle(
                            fontSize: 10,
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
