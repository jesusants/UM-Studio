class GlobalEnvConfig {
  const GlobalEnvConfig({
    this.aiEnabled = true,
    this.aiProvider = 'gemini',
    this.aiModelName = 'gemini-3.5-flash-lite',
    this.aiApiKeyOverride = '',
    this.aiTemperature = 0.2,
    this.aiMaxTokens = 1024,
    this.aiCustomSystemPrompt = '',
    this.allowAiGraphics = true,
    this.periodoAcademicoActual = '2026-III',
    this.corteActivoGlobal = 1,
    this.portalEstudiantesUrl =
        'https://admisiones.unimagdalena.edu.co/mEstudiantes/indexPrinc.jsp?rnd=315581080',
    this.globalBannerEnabled = false,
    this.globalBannerTitle = 'Bienvenido a UM Studio',
    this.globalBannerMessage =
        'Consulta tus clases magistrales y temas del corte en curso.',
    this.globalBannerType = 'info',
    this.globalBannerImageUrl = '',
    this.globalBannerChartMode = 'none',
    this.newsSourceUrl =
        'https://www.unimagdalena.edu.co/PresentacionPublicacion/ListadoNoticias',
    this.newsCorsProxy = 'https://api.allorigins.win/raw?url=',
    this.newsRefreshMinutes = 15,
    this.allowUserNotesEditing = true,
    this.allowUserAttachments = true,
    this.pomodoroDefaultWorkMin = 25,
    this.pomodoroDefaultBreakMin = 5,
    this.maintenanceMode = false,
    this.updatedAt = '',
    this.updatedBy = '',
  });

  static const String defaultWorkingGeminiModel = 'gemini-3.5-flash-lite';

  /// Normaliza nombres de modelos legados (`gemini-2.0-*`, `gemini-2.5-*`) que ya
  /// devuelven 404 en la API de Google hacia el modelo activo vigente.
  static String normalizeModelName(String? rawModel) {
    final clean = (rawModel ?? '').trim().replaceFirst('models/', '');
    if (clean.isEmpty || clean.startsWith('gemini-2.')) {
      return defaultWorkingGeminiModel;
    }
    return clean;
  }

  final bool aiEnabled;
  final String aiProvider;
  final String aiModelName;
  final String aiApiKeyOverride;
  final double aiTemperature;
  final int aiMaxTokens;
  final String aiCustomSystemPrompt;
  final bool allowAiGraphics;

  final String periodoAcademicoActual;
  final int corteActivoGlobal;
  final String portalEstudiantesUrl;

  final bool globalBannerEnabled;
  final String globalBannerTitle;
  final String globalBannerMessage;
  final String globalBannerType;
  final String globalBannerImageUrl;
  final String globalBannerChartMode;

  final String newsSourceUrl;
  final String newsCorsProxy;
  final int newsRefreshMinutes;
  final bool allowUserNotesEditing;
  final bool allowUserAttachments;
  final int pomodoroDefaultWorkMin;
  final int pomodoroDefaultBreakMin;
  final bool maintenanceMode;

  final String updatedAt;
  final String updatedBy;

  factory GlobalEnvConfig.fromJson(Map<String, dynamic> json) {
    return GlobalEnvConfig(
      aiEnabled: json['ai_enabled'] ?? true,
      aiProvider: (json['ai_provider'] ?? 'gemini').toString(),
      aiModelName: normalizeModelName(json['ai_model_name']?.toString()),
      aiApiKeyOverride: (json['ai_api_key_override'] ?? '').toString(),
      aiTemperature: (json['ai_temperature'] is num)
          ? (json['ai_temperature'] as num).toDouble()
          : 0.2,
      aiMaxTokens: (json['ai_max_tokens'] is num)
          ? (json['ai_max_tokens'] as num).toInt()
          : 1024,
      aiCustomSystemPrompt: (json['ai_custom_system_prompt'] ?? '').toString(),
      allowAiGraphics: json['allow_ai_graphics'] ?? true,
      periodoAcademicoActual:
          (json['periodo_academico_actual'] ?? '2026-III').toString(),
      corteActivoGlobal: (json['corte_activo_global'] is num)
          ? (json['corte_activo_global'] as num).toInt().clamp(1, 3)
          : 1,
      portalEstudiantesUrl: (json['portal_estudiantes_url'] ??
              'https://admisiones.unimagdalena.edu.co/mEstudiantes/indexPrinc.jsp?rnd=315581080')
          .toString(),
      globalBannerEnabled: json['global_banner_enabled'] ?? false,
      globalBannerTitle: (json['global_banner_title'] ?? 'Aviso Oficial').toString(),
      globalBannerMessage: (json['global_banner_message'] ?? '').toString(),
      globalBannerType: (json['global_banner_type'] ?? 'info').toString(),
      globalBannerImageUrl: (json['global_banner_image_url'] ?? '').toString(),
      globalBannerChartMode:
          (json['global_banner_chart_mode'] ?? 'none').toString(),
      newsSourceUrl: (json['news_source_url'] ??
              'https://www.unimagdalena.edu.co/PresentacionPublicacion/ListadoNoticias')
          .toString(),
      newsCorsProxy: (json['news_cors_proxy'] ??
              'https://api.allorigins.win/raw?url=')
          .toString(),
      newsRefreshMinutes: (json['news_refresh_minutes'] is num)
          ? (json['news_refresh_minutes'] as num).toInt().clamp(1, 120)
          : 15,
      allowUserNotesEditing: json['allow_user_notes_editing'] ?? true,
      allowUserAttachments: json['allow_user_attachments'] ?? true,
      pomodoroDefaultWorkMin: (json['pomodoro_default_work_min'] is num)
          ? (json['pomodoro_default_work_min'] as num).toInt().clamp(5, 120)
          : 25,
      pomodoroDefaultBreakMin: (json['pomodoro_default_break_min'] is num)
          ? (json['pomodoro_default_break_min'] as num).toInt().clamp(1, 60)
          : 5,
      maintenanceMode: json['maintenance_mode'] ?? false,
      updatedAt: (json['updated_at'] ?? '').toString(),
      updatedBy: (json['updated_by'] ?? '').toString(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'ai_enabled': aiEnabled,
      'ai_provider': aiProvider,
      'ai_model_name': aiModelName,
      'ai_api_key_override': aiApiKeyOverride,
      'ai_temperature': aiTemperature,
      'ai_max_tokens': aiMaxTokens,
      'ai_custom_system_prompt': aiCustomSystemPrompt,
      'allow_ai_graphics': allowAiGraphics,
      'periodo_academico_actual': periodoAcademicoActual,
      'corte_activo_global': corteActivoGlobal,
      'portal_estudiantes_url': portalEstudiantesUrl,
      'global_banner_enabled': globalBannerEnabled,
      'global_banner_title': globalBannerTitle,
      'global_banner_message': globalBannerMessage,
      'global_banner_type': globalBannerType,
      'global_banner_image_url': globalBannerImageUrl,
      'global_banner_chart_mode': globalBannerChartMode,
      'news_source_url': newsSourceUrl,
      'news_cors_proxy': newsCorsProxy,
      'news_refresh_minutes': newsRefreshMinutes,
      'allow_user_notes_editing': allowUserNotesEditing,
      'allow_user_attachments': allowUserAttachments,
      'pomodoro_default_work_min': pomodoroDefaultWorkMin,
      'pomodoro_default_break_min': pomodoroDefaultBreakMin,
      'maintenance_mode': maintenanceMode,
      'updated_at': updatedAt,
      'updated_by': updatedBy,
    };
  }

  GlobalEnvConfig copyWith({
    bool? aiEnabled,
    String? aiProvider,
    String? aiModelName,
    String? aiApiKeyOverride,
    double? aiTemperature,
    int? aiMaxTokens,
    String? aiCustomSystemPrompt,
    bool? allowAiGraphics,
    String? periodoAcademicoActual,
    int? corteActivoGlobal,
    String? portalEstudiantesUrl,
    bool? globalBannerEnabled,
    String? globalBannerTitle,
    String? globalBannerMessage,
    String? globalBannerType,
    String? globalBannerImageUrl,
    String? globalBannerChartMode,
    String? newsSourceUrl,
    String? newsCorsProxy,
    int? newsRefreshMinutes,
    bool? allowUserNotesEditing,
    bool? allowUserAttachments,
    int? pomodoroDefaultWorkMin,
    int? pomodoroDefaultBreakMin,
    bool? maintenanceMode,
    String? updatedAt,
    String? updatedBy,
  }) {
    return GlobalEnvConfig(
      aiEnabled: aiEnabled ?? this.aiEnabled,
      aiProvider: aiProvider ?? this.aiProvider,
      aiModelName: aiModelName != null
          ? normalizeModelName(aiModelName)
          : this.aiModelName,
      aiApiKeyOverride: aiApiKeyOverride ?? this.aiApiKeyOverride,
      aiTemperature: (aiTemperature ?? this.aiTemperature).clamp(0.0, 1.0),
      aiMaxTokens: (aiMaxTokens ?? this.aiMaxTokens).clamp(256, 4096),
      aiCustomSystemPrompt: aiCustomSystemPrompt ?? this.aiCustomSystemPrompt,
      allowAiGraphics: allowAiGraphics ?? this.allowAiGraphics,
      periodoAcademicoActual:
          periodoAcademicoActual ?? this.periodoAcademicoActual,
      corteActivoGlobal: (corteActivoGlobal ?? this.corteActivoGlobal).clamp(1, 3),
      portalEstudiantesUrl: portalEstudiantesUrl ?? this.portalEstudiantesUrl,
      globalBannerEnabled: globalBannerEnabled ?? this.globalBannerEnabled,
      globalBannerTitle: globalBannerTitle ?? this.globalBannerTitle,
      globalBannerMessage: globalBannerMessage ?? this.globalBannerMessage,
      globalBannerType: globalBannerType ?? this.globalBannerType,
      globalBannerImageUrl: globalBannerImageUrl ?? this.globalBannerImageUrl,
      globalBannerChartMode:
          globalBannerChartMode ?? this.globalBannerChartMode,
      newsSourceUrl: newsSourceUrl ?? this.newsSourceUrl,
      newsCorsProxy: newsCorsProxy ?? this.newsCorsProxy,
      newsRefreshMinutes: (newsRefreshMinutes ?? this.newsRefreshMinutes).clamp(1, 60),
      allowUserNotesEditing:
          allowUserNotesEditing ?? this.allowUserNotesEditing,
      allowUserAttachments: allowUserAttachments ?? this.allowUserAttachments,
      pomodoroDefaultWorkMin:
          (pomodoroDefaultWorkMin ?? this.pomodoroDefaultWorkMin).clamp(1, 120),
      pomodoroDefaultBreakMin:
          (pomodoroDefaultBreakMin ?? this.pomodoroDefaultBreakMin).clamp(1, 60),
      maintenanceMode: maintenanceMode ?? this.maintenanceMode,
      updatedAt: updatedAt ?? this.updatedAt,
      updatedBy: updatedBy ?? this.updatedBy,
    );
  }
}
