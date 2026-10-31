# UM STUDIO — Ingeniería Energética (Plan 8108 • SNIES 118222)

Plataforma académica diaria de estudio activo dedicada a **Ingeniería Energética — Universidad del Magdalena**, diseñada bajo **Apple Human Interface Guidelines (iOS Minimalist OLED Dark & Light Mode)**, **Clean Architecture** y un backend **Serverless ultraligero alojado en GitHub**.

🌐 **Web App en vivo:** https://jesusants.github.io/UM-Studio/

---

## Estructura de Datos Serverless y Arquitectura

```text
UM-Studio/
├── db/
│   ├── ingenieria_energetica.md       # Base de datos maestra Plan 8108 (YAML Frontmatter + KaTeX, 12 cuatrimestres, 56 materias)
│   └── users/                         # Un archivo JSON independiente por estudiante ({username}.json)
├── assets/
│   └── data/ingenieria_energetica.md  # Copia local Offline-First para carga en 0 ms
└── lib/
    ├── core/                          # Design tokens OLED (#000000, #121316, #1F2228, #30D158), validador @unimagdalena.edu.co + SHA-256
    ├── domain/                        # Entidades y contratos reactivos de La Clase Viva
    ├── data/
    │   ├── models/                    # Modelos tipados (CurriculumDatabaseModel, StudentUserModel, CalendarReminderModel)
    │   ├── repositories/              # LocalReactiveClaseVivaRepository (Offline-First + sincronización de apuntes)
    │   └── services/
    │       ├── github_sync_service.dart         # Autenticación simple y sincronización optimista (GET/PUT Contents API)
    │       └── markdown_curriculum_service.dart # Parser YAML Frontmatter + actualización OTA desde GitHub Raw
    └── presentation/                  # Login rápido Ing. Energética, HomeShell, Calendario Personal, Estudio Extraclase y La Clase Viva (KaTeX nativo)
```

## Ejecución Local

```bash
flutter pub get
flutter run -d chrome
```
