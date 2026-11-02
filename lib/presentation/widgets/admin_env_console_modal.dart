import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../core/theme/app_theme.dart';
import '../../data/models/global_env_config.dart';
import '../../data/services/global_environment_service.dart';
import '../providers/app_scopes.dart';
import 'ios_primitives.dart';

/// Modal centralizado y restringido exclusivamente a Web (kIsWeb) para el
/// administrador (jsierra), permitiendo manipular en tiempo real todas las
/// variables globales de entorno de UM Studio y publicarlas a GitHub (db/global_config.json).
class AdminEnvConsoleModal extends StatefulWidget {
  const AdminEnvConsoleModal({super.key});

  static Future<void> show(BuildContext context) async {
    if (!kIsWeb) return;
    final session = SessionScope.maybeOf(context);
    if (session == null || !session.isAdmin) return;
    return showDialog<void>(
      context: context,
      barrierDismissible: true,
      barrierColor: Colors.black.o(0.70),
      builder: (_) => const AdminEnvConsoleModal(),
    );
  }

  @override
  State<AdminEnvConsoleModal> createState() => _AdminEnvConsoleModalState();
}

class _AdminEnvConsoleModalState extends State<AdminEnvConsoleModal> {
  int _selectedCategoryIndex = 0;
  bool _isPublishing = false;
  bool _hideApiKey = true;
  String? _statusMessage;
  bool _statusIsError = false;

  late GlobalEnvConfig _config;

  // Controllers
  late TextEditingController _aiApiKeyCtrl;
  late TextEditingController _aiSystemPromptCtrl;
  late TextEditingController _periodoCtrl;
  late TextEditingController _portalUrlCtrl;
  late TextEditingController _bannerTitleCtrl;
  late TextEditingController _bannerMessageCtrl;
  late TextEditingController _newsUrlCtrl;
  late TextEditingController _newsCorsCtrl;

  final List<String> _categories = const [
    'Motor IA & Modelos',
    'Académico & Periodo',
    'Broadcast Global',
    'Noticias & Red',
    'Flags del Sistema',
    'Inspector JSON',
  ];

  final List<String> _aiModels = const [
    'llama-3.3-70b-versatile',
    'llama-3.1-8b-instant',
    'mixtral-8x7b-32768',
    'gemma2-9b-it',
  ];

  @override
  void initState() {
    super.initState();
    _config = GlobalEnvironmentService.instance.config;
    _initControllers();
  }

  void _initControllers() {
    _aiApiKeyCtrl = TextEditingController(text: _config.aiApiKeyOverride);
    _aiSystemPromptCtrl = TextEditingController(text: _config.aiCustomSystemPrompt);
    _periodoCtrl = TextEditingController(text: _config.periodoAcademicoActual);
    _portalUrlCtrl = TextEditingController(text: _config.portalEstudiantesUrl);
    _bannerTitleCtrl = TextEditingController(text: _config.globalBannerTitle);
    _bannerMessageCtrl = TextEditingController(text: _config.globalBannerMessage);
    _newsUrlCtrl = TextEditingController(text: _config.newsSourceUrl);
    _newsCorsCtrl = TextEditingController(text: _config.newsCorsProxy);
  }

  @override
  void dispose() {
    _aiApiKeyCtrl.dispose();
    _aiSystemPromptCtrl.dispose();
    _periodoCtrl.dispose();
    _portalUrlCtrl.dispose();
    _bannerTitleCtrl.dispose();
    _bannerMessageCtrl.dispose();
    _newsUrlCtrl.dispose();
    _newsCorsCtrl.dispose();
    super.dispose();
  }

  void _resetToDefaults() {
    setState(() {
      _config = const GlobalEnvConfig();
      _initControllers();
      _statusMessage = 'Restablecido a valores predeterminados (sin publicar).';
      _statusIsError = false;
    });
  }

  Future<void> _publish() async {
    setState(() {
      _isPublishing = true;
      _statusMessage = null;
    });

    final session = SessionScope.maybeOf(context);
    final adminUsername = session?.currentUser?.username ?? '';
    final result = await GlobalEnvironmentService.instance.publishGlobalConfig(
      newConfig: _config,
      adminUsername: adminUsername,
      adminPin: '81991042249674',
      syncService: session?.syncService,
    );

    if (mounted) {
      setState(() {
        _isPublishing = false;
        if (result.success) {
          _statusMessage = '¡Configuración sincronizada exitosamente con GitHub!';
          _statusIsError = false;
        } else {
          _statusMessage = result.error ??
              GlobalEnvironmentService.instance.lastError ??
              'Error al sincronizar con GitHub. Verifica el PAT.';
          _statusIsError = true;
        }
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final p = context.palette;
    final size = MediaQuery.sizeOf(context);
    final dialogWidth = size.width > 960 ? 920.0 : size.width * 0.94;
    final dialogHeight = size.height > 720 ? 680.0 : size.height * 0.90;

    return Center(
      child: Material(
        color: Colors.transparent,
        child: Container(
          width: dialogWidth,
          height: dialogHeight,
          decoration: BoxDecoration(
            color: p.background,
            borderRadius: BorderRadius.circular(24),
            border: Border.all(color: p.cardBorder, width: 1.5),
            boxShadow: [
              BoxShadow(
                color: Colors.black.o(0.40),
                blurRadius: 36,
                offset: const Offset(0, 16),
              ),
            ],
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(24),
            child: Column(
              children: [
                // Header
                _buildHeader(p),
                // Body (Categorías + Editor)
                Expanded(
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      // Panel lateral de categorías
                      _buildSidebar(p),
                      // Contenido de la categoría seleccionada
                      Expanded(
                        child: Container(
                          color: p.card.o(0.35),
                          child: _buildCategoryContent(p),
                        ),
                      ),
                    ],
                  ),
                ),
                // Footer con estado y botón de publicar
                _buildFooter(p),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildHeader(AppPalette p) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      decoration: BoxDecoration(
        color: p.glass,
        border: Border(bottom: BorderSide(color: p.cardBorder)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            decoration: BoxDecoration(
              color: p.green.o(0.12),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: p.green.o(0.35)),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                PulseDot(color: p.green, size: 7),
                const SizedBox(width: 7),
                Text(
                  '⚡ WEB ADMIN CONSOLE',
                  style: mono(
                    fontSize: 10.5,
                    fontWeight: FontWeight.w800,
                    color: p.green,
                    letterSpacing: 0.8,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  'Variables Globales de Entorno',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                    color: p.textPrimary,
                  ),
                ),
                Text(
                  'Sesión activa: jsierra@unimagdalena.edu.co • Sincronización GitHub en vivo',
                  style: TextStyle(
                    fontSize: 11,
                    color: p.textSecondary,
                  ),
                ),
              ],
            ),
          ),
          IconButton(
            icon: Icon(Icons.close_rounded, color: p.textSecondary, size: 20),
            onPressed: () => Navigator.of(context).pop(),
            splashRadius: 18,
          ),
        ],
      ),
    );
  }

  Widget _buildSidebar(AppPalette p) {
    return Container(
      width: 220,
      decoration: BoxDecoration(
        color: p.background,
        border: Border(right: BorderSide(color: p.cardBorder)),
      ),
      child: ListView.separated(
        padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 8),
        itemCount: _categories.length,
        separatorBuilder: (_, __) => const SizedBox(height: 4),
        itemBuilder: (context, i) {
          final isSelected = _selectedCategoryIndex == i;
          return TapScale(
            onTap: () => setState(() => _selectedCategoryIndex = i),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
              decoration: BoxDecoration(
                color: isSelected ? p.green.o(0.12) : Colors.transparent,
                borderRadius: BorderRadius.circular(10),
                border: Border.all(
                  color: isSelected ? p.green.o(0.35) : Colors.transparent,
                ),
              ),
              child: Text(
                _categories[i],
                style: TextStyle(
                  fontSize: 12.5,
                  fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                  color: isSelected ? p.green : p.textPrimary,
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildCategoryContent(AppPalette p) {
    switch (_selectedCategoryIndex) {
      case 0:
        return _buildAiSection(p);
      case 1:
        return _buildAcademicSection(p);
      case 2:
        return _buildBroadcastSection(p);
      case 3:
        return _buildNewsSection(p);
      case 4:
        return _buildSystemSection(p);
      case 5:
        return _buildJsonInspector(p);
      default:
        return const SizedBox();
    }
  }

  Widget _buildAiSection(AppPalette p) {
    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        _buildSwitchRow(
          title: 'Habilitar Asistente de IA (Groq)',
          subtitle: 'Desactivar para pausar respuestas automáticas globalmente.',
          value: _config.aiEnabled,
          onChanged: (val) => setState(() => _config = _config.copyWith(aiEnabled: val)),
          p: p,
        ),
        const SizedBox(height: 18),
        _buildDropdownRow(
          title: 'Modelo Groq Activo',
          subtitle: 'LLM utilizado para tutorías y resúmenes de temas.',
          value: _config.aiModelName,
          items: _aiModels,
          onChanged: (val) {
            if (val != null) setState(() => _config = _config.copyWith(aiModelName: val));
          },
          p: p,
        ),
        const SizedBox(height: 18),
        Text('API Key Override (Opcional)', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Reemplaza la clave de Groq por defecto si se agotan tokens.', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _aiApiKeyCtrl,
          obscureText: _hideApiKey,
          onChanged: (v) => _config = _config.copyWith(
            aiApiKeyOverride: v.trim(),
          ),
          decoration: InputDecoration(
            hintText: 'gsk_...',
            hintStyle: TextStyle(color: p.textSecondary.o(0.5)),
            suffixIcon: IconButton(
              icon: Icon(_hideApiKey ? Icons.visibility_off_rounded : Icons.visibility_rounded, size: 18),
              onPressed: () => setState(() => _hideApiKey = !_hideApiKey),
            ),
          ),
        ),
        const SizedBox(height: 18),
        _buildSliderRow(
          title: 'Temperatura (${_config.aiTemperature.toStringAsFixed(2)})',
          subtitle: 'Valores bajos son más precisos y analíticos; altos son más creativos.',
          value: _config.aiTemperature,
          min: 0.0,
          max: 1.0,
          divisions: 20,
          onChanged: (val) => setState(() => _config = _config.copyWith(aiTemperature: val)),
          p: p,
        ),
        const SizedBox(height: 18),
        _buildSliderRow(
          title: 'Tokens Máximos (${_config.aiMaxTokens})',
          subtitle: 'Límite de longitud por respuesta del asistente.',
          value: _config.aiMaxTokens.toDouble(),
          min: 256,
          max: 4096,
          divisions: 15,
          onChanged: (val) => setState(() => _config = _config.copyWith(aiMaxTokens: val.toInt())),
          p: p,
        ),
        const SizedBox(height: 18),
        Text('Prompt del Sistema Personalizado', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Reglas de pedagogía e identidad para el asistente de cátedra.', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _aiSystemPromptCtrl,
          maxLines: 4,
          onChanged: (v) => _config = _config.copyWith(
            aiCustomSystemPrompt: v.trim(),
          ),
          decoration: const InputDecoration(
            hintText: 'Eres el Asistente Académico de Cátedra de Ingeniería Energética...',
          ),
        ),
      ],
    );
  }

  Widget _buildAcademicSection(AppPalette p) {
    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        Text('Periodo Académico Oficial', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Periodo mostrado a nivel institucional (ej. 2026-I, 2026-II).', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _periodoCtrl,
          onChanged: (v) => _config = _config.copyWith(periodoAcademicoActual: v.trim()),
        ),
        const SizedBox(height: 20),
        Text('Corte Académico Activo (1, 2 o 3)', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Filtra ponderaciones y estado de calificaciones en el calendario.', style: _subStyle(p)),
        const SizedBox(height: 10),
        Row(
          children: [1, 2, 3].map((corte) {
            final isSel = _config.corteActivoGlobal == corte;
            return Padding(
              padding: const EdgeInsets.only(right: 12),
              child: TapScale(
                onTap: () => setState(() => _config = _config.copyWith(corteActivoGlobal: corte)),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                  decoration: BoxDecoration(
                    color: isSel ? p.green : p.card,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: isSel ? p.green : p.cardBorder),
                  ),
                  child: Text(
                    'Corte ',
                    style: TextStyle(
                      fontWeight: FontWeight.w700,
                      color: isSel ? Colors.black : p.textPrimary,
                    ),
                  ),
                ),
              ),
            );
          }).toList(),
        ),
        const SizedBox(height: 20),
        Text('URL Portal de Estudiantes (AyRe)', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Enlace directo del botón flotante y accesos institucionales.', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _portalUrlCtrl,
          onChanged: (v) => _config = _config.copyWith(portalEstudiantesUrl: v.trim()),
        ),
      ],
    );
  }

  Widget _buildBroadcastSection(AppPalette p) {
    const urgentColor = Color(0xFFFF453A);
    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        _buildSwitchRow(
          title: 'Activar Banner de Anuncio Global',
          subtitle: 'Muestra un aviso visible para todos los estudiantes al entrar a la app.',
          value: _config.globalBannerEnabled,
          onChanged: (val) => setState(() => _config = _config.copyWith(globalBannerEnabled: val)),
          p: p,
        ),
        const SizedBox(height: 18),
        Text('Tipo / Severidad del Banner', style: _titleStyle(p)),
        const SizedBox(height: 8),
        Row(
          children: ['info', 'warning', 'success', 'urgent'].map((type) {
            final isSel = _config.globalBannerType == type;
            Color typeColor;
            switch (type) {
              case 'warning':
                typeColor = p.orange;
                break;
              case 'success':
                typeColor = p.green;
                break;
              case 'urgent':
                typeColor = urgentColor;
                break;
              case 'info':
              default:
                typeColor = p.indigo;
            }
            return Padding(
              padding: const EdgeInsets.only(right: 10),
              child: TapScale(
                onTap: () => setState(() => _config = _config.copyWith(globalBannerType: type)),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  decoration: BoxDecoration(
                    color: isSel ? typeColor.o(0.2) : p.card,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: isSel ? typeColor : p.cardBorder),
                  ),
                  child: Text(
                    type.toUpperCase(),
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w700,
                      color: isSel ? typeColor : p.textSecondary,
                    ),
                  ),
                ),
              ),
            );
          }).toList(),
        ),
        const SizedBox(height: 18),
        Text('Título del Anuncio', style: _titleStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _bannerTitleCtrl,
          onChanged: (v) => _config = _config.copyWith(globalBannerTitle: v.trim()),
          decoration: const InputDecoration(hintText: 'Aviso Importante de Cátedra'),
        ),
        const SizedBox(height: 18),
        Text('Mensaje del Anuncio', style: _titleStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _bannerMessageCtrl,
          maxLines: 3,
          onChanged: (v) => _config = _config.copyWith(globalBannerMessage: v.trim()),
          decoration: const InputDecoration(
            hintText: 'Se ha habilitado la descarga de apuntes y ejercicios resueltos...',
          ),
        ),
      ],
    );
  }

  Widget _buildNewsSection(AppPalette p) {
    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        Text('URL de Fuente de Noticias', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Ruta web a la sección de publicaciones o noticias institucionales.', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _newsUrlCtrl,
          onChanged: (v) => _config = _config.copyWith(newsSourceUrl: v.trim()),
        ),
        const SizedBox(height: 18),
        Text('CORS Proxy Primario (Opcional)', style: _titleStyle(p)),
        const SizedBox(height: 4),
        Text('Proxy utilizado para sobrepasar bloqueos CORS en navegadores.', style: _subStyle(p)),
        const SizedBox(height: 8),
        TextField(
          controller: _newsCorsCtrl,
          onChanged: (v) => _config = _config.copyWith(
            newsCorsProxy: v.trim(),
          ),
          decoration: const InputDecoration(hintText: 'https://corsproxy.io/?url='),
        ),
        const SizedBox(height: 18),
        _buildSliderRow(
          title: 'Intervalo de Refresco (${_config.newsRefreshMinutes} min)',
          subtitle: 'Frecuencia con la que el feed consulta novedades en segundo plano.',
          value: _config.newsRefreshMinutes.toDouble(),
          min: 1,
          max: 60,
          divisions: 59,
          onChanged: (val) => setState(() => _config = _config.copyWith(newsRefreshMinutes: val.toInt())),
          p: p,
        ),
      ],
    );
  }

  Widget _buildSystemSection(AppPalette p) {
    const errorColor = Color(0xFFFF453A);
    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        _buildSwitchRow(
          title: 'Permitir Edición de Notas de Cátedra',
          subtitle: 'Permite que los alumnos personalicen y redacten sus propios apuntes.',
          value: _config.allowUserNotesEditing,
          onChanged: (val) => setState(() => _config = _config.copyWith(allowUserNotesEditing: val)),
          p: p,
        ),
        const SizedBox(height: 16),
        _buildSwitchRow(
          title: 'Permitir Adjuntos Multimedia en Temas',
          subtitle: 'Permite subir o vincular fotos, tableros y PDFs a los temas.',
          value: _config.allowUserAttachments,
          onChanged: (val) => setState(() => _config = _config.copyWith(allowUserAttachments: val)),
          p: p,
        ),
        const SizedBox(height: 18),
        _buildSliderRow(
          title: 'Pomodoro: Duración de Enfoque (${_config.pomodoroDefaultWorkMin} min)',
          subtitle: 'Minutos predeterminados para sesiones de estudio concentrado.',
          value: _config.pomodoroDefaultWorkMin.toDouble(),
          min: 10,
          max: 60,
          divisions: 10,
          onChanged: (val) => setState(() => _config = _config.copyWith(pomodoroDefaultWorkMin: val.toInt())),
          p: p,
        ),
        const SizedBox(height: 18),
        _buildSliderRow(
          title: 'Pomodoro: Pausa Corta (${_config.pomodoroDefaultBreakMin} min)',
          subtitle: 'Minutos predeterminados para descanso entre bloques de estudio.',
          value: _config.pomodoroDefaultBreakMin.toDouble(),
          min: 1,
          max: 15,
          divisions: 14,
          onChanged: (val) => setState(() => _config = _config.copyWith(pomodoroDefaultBreakMin: val.toInt())),
          p: p,
        ),
        const SizedBox(height: 24),
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: errorColor.o(0.08),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: errorColor.o(0.35)),
          ),
          child: _buildSwitchRow(
            title: 'MODO MANTENIMIENTO GLOBAL',
            subtitle: 'Bloquea el acceso a todos los estudiantes mientras se actualiza el sistema.',
            value: _config.maintenanceMode,
            onChanged: (val) => setState(() => _config = _config.copyWith(maintenanceMode: val)),
            p: p,
            activeColor: errorColor,
          ),
        ),
      ],
    );
  }

  Widget _buildJsonInspector(AppPalette p) {
    final prettyJson = const JsonEncoder.withIndent('  ').convert(_config.toJson());
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Text(
                'SERIALIZACIÓN JSON EN VIVO (db/global_config.json)',
                style: mono(
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  color: p.textSecondary,
                  letterSpacing: 0.5,
                ),
              ),
              const Spacer(),
              TapScale(
                onTap: () {
                  Clipboard.setData(ClipboardData(text: prettyJson));
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text('JSON copiado al portapapeles'),
                      duration: Duration(seconds: 2),
                    ),
                  );
                },
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: p.card,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: p.cardBorder),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.copy_rounded, size: 14, color: p.textPrimary),
                      const SizedBox(width: 5),
                      Text('Copiar JSON', style: TextStyle(fontSize: 11, color: p.textPrimary)),
                    ],
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Expanded(
            child: Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0xFF0D1117),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: p.cardBorder),
              ),
              child: SingleChildScrollView(
                child: SelectableText(
                  prettyJson,
                  style: GoogleFonts.jetBrainsMono(
                    fontSize: 12,
                    height: 1.45,
                    color: const Color(0xFF7EE787),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFooter(AppPalette p) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
      decoration: BoxDecoration(
        color: p.glass,
        border: Border(top: BorderSide(color: p.cardBorder)),
      ),
      child: Row(
        children: [
          TextButton(
            onPressed: _resetToDefaults,
            child: Text('Restablecer Defaults', style: TextStyle(color: p.textSecondary)),
          ),
          const SizedBox(width: 14),
          if (_statusMessage != null)
            Expanded(
              child: Text(
                _statusMessage!,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w600,
                  color: _statusIsError ? const Color(0xFFFF453A) : p.green,
                ),
              ),
            )
          else
            const Spacer(),
          TapScale(
            onTap: _isPublishing ? null : _publish,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 11),
              decoration: BoxDecoration(
                color: _isPublishing ? p.textSecondary : p.green,
                borderRadius: BorderRadius.circular(12),
                boxShadow: [
                  BoxShadow(
                    color: p.green.o(0.30),
                    blurRadius: 10,
                    offset: const Offset(0, 3),
                  ),
                ],
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (_isPublishing)
                    const SizedBox(
                      width: 16,
                      height: 16,
                      child: CircularProgressIndicator(strokeWidth: 2, color: Colors.black),
                    )
                  else
                    const Icon(Icons.rocket_launch_rounded, size: 16, color: Colors.black),
                  const SizedBox(width: 8),
                  Text(
                    _isPublishing ? 'Publicando a GitHub...' : 'Publicar para Todos',
                    style: const TextStyle(
                      fontSize: 13,
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
    );
  }

  Widget _buildSwitchRow({
    required String title,
    required String subtitle,
    required bool value,
    required ValueChanged<bool> onChanged,
    required AppPalette p,
    Color? activeColor,
  }) {
    return Row(
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title, style: _titleStyle(p)),
              const SizedBox(height: 2),
              Text(subtitle, style: _subStyle(p)),
            ],
          ),
        ),
        Switch.adaptive(
          value: value,
          activeThumbColor: activeColor ?? p.green,
          onChanged: onChanged,
        ),
      ],
    );
  }

  Widget _buildDropdownRow({
    required String title,
    required String subtitle,
    required String value,
    required List<String> items,
    required ValueChanged<String?> onChanged,
    required AppPalette p,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: _titleStyle(p)),
        const SizedBox(height: 2),
        Text(subtitle, style: _subStyle(p)),
        const SizedBox(height: 8),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 14),
          decoration: BoxDecoration(
            color: p.card,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: p.cardBorder),
          ),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<String>(
              value: items.contains(value) ? value : items.first,
              isExpanded: true,
              dropdownColor: p.card,
              style: TextStyle(color: p.textPrimary, fontSize: 13),
              items: items.map((m) => DropdownMenuItem(value: m, child: Text(m))).toList(),
              onChanged: onChanged,
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildSliderRow({
    required String title,
    required String subtitle,
    required double value,
    required double min,
    required double max,
    required int divisions,
    required ValueChanged<double> onChanged,
    required AppPalette p,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: _titleStyle(p)),
        const SizedBox(height: 2),
        Text(subtitle, style: _subStyle(p)),
        SliderTheme(
          data: SliderThemeData(
            activeTrackColor: p.green,
            thumbColor: p.green,
            inactiveTrackColor: p.cardBorder,
            overlayColor: p.green.o(0.15),
          ),
          child: Slider(
            value: value.clamp(min, max),
            min: min,
            max: max,
            divisions: divisions,
            onChanged: onChanged,
          ),
        ),
      ],
    );
  }

  TextStyle _titleStyle(AppPalette p) => TextStyle(
        fontSize: 13.5,
        fontWeight: FontWeight.w700,
        color: p.textPrimary,
      );

  TextStyle _subStyle(AppPalette p) => TextStyle(
        fontSize: 11,
        color: p.textSecondary,
      );
}
