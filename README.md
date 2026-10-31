# UM STUDIO — iOS Minimalist Edition (Flutter)

Plataforma académica de estudio activo (**Unimagdalena • Ing. Energética**) diseñada bajo los principios de **Apple Human Interface Guidelines (iOS OLED Minimalist)** y **Clean Architecture**.

## Arquitectura Limpia (`lib/`)

```text
lib/
├── main.dart
├── core/
│   ├── constants/app_constants.dart            # Constantes, dominio @unimagdalena.edu.co, variables de entorno
│   ├── theme/app_theme.dart                    # Design Tokens iOS OLED (#000000, #121316, #1F2228, #30D158, #5E5CE6, #1A1D24) y Light (#F2F2F7)
│   └── utils/institutional_validator.dart      # Regex estricta @unimagdalena.edu.co, sanitizador LaTeX, formateador KB/MB
├── domain/
│   ├── entities/
│   │   ├── nota_adjunto_entity.dart            # Entidad ('pdf' | 'imagen' | 'nota')
│   │   ├── subject_summary.dart                # Entidades de asignatura y calendario
│   │   └── tema_estudio_entity.dart            # Entidad de temas_estudio
│   └── repositories/
│       └── i_clase_viva_repository.dart        # Contrato reactivo del dominio
├── data/
│   ├── datasources/academic_seed_data.dart     # Semilla oficial de asignaturas y fórmulas LaTeX
│   ├── models/
│   │   ├── nota_adjunto_model.dart             # DTO fromJson/toJson (notas_adjuntos_estudiante)
│   │   └── tema_estudio_model.dart             # DTO fromJson/toJson (temas_estudio)
│   └── repositories/
│       ├── local_clase_viva_repository.dart    # Motor reactivo offline-first (SharedPreferences + Shimmer latency)
│       └── supabase_clase_viva_repository.dart # Sincronización PostgreSQL Realtime + Supabase Storage
└── presentation/
    ├── providers/app_scopes.dart               # ThemeScope, ClaseVivaRepositoryScope, SessionScope
    ├── screens/
    │   ├── clase_viva/
    │   │   ├── attachment_viewer_page.dart     # Visor fullscreen con zoom InteractiveViewer e inspector PDF
    │   │   └── clase_viva_page.dart            # La Clase Viva, Shimmer #1A1D24, KaTeX nativo, adjuntos y auto-save 1s
    │   └── home/
    │       ├── home_shell.dart                 # Shell principal, uso diario y credencial @unimagdalena.edu.co
    │       └── tabs/
    │           ├── calendario_tab.dart
    │           ├── estudio_tab.dart
    │           └── resumen_tab.dart
    └── widgets/
        ├── ios_primitives.dart                 # TapScale (0.97 + HapticFeedback.lightImpact), IosCard, IosShimmer
        └── katex_formula_card.dart             # Renderizado matemático nativo flutter_math_fork
```

## Ejecución

```bash
cd "C:\Users\ESTUDIANTE\OneDrive\U Studio"
flutter pub get
flutter run -d chrome
```

Para conectar a **Supabase (PostgreSQL + Storage)**:
1. Ejecuta el script SQL [supabase/schema.sql](./supabase/schema.sql) en el editor SQL de tu proyecto Supabase.
2. Inicia la aplicación pasando las variables `--dart-define`:
```bash
flutter run -d chrome --dart-define=SUPABASE_URL=https://tu-proyecto.supabase.co --dart-define=SUPABASE_ANON_KEY=tu-anon-key
```
