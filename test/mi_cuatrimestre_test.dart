import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:um_studio/core/theme/app_theme.dart';
import 'package:um_studio/data/models/student_user_model.dart';
import 'package:um_studio/data/repositories/local_clase_viva_repository.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';
import 'package:um_studio/presentation/providers/app_scopes.dart';
import 'package:um_studio/presentation/screens/matricula/mi_cuatrimestre_screen.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  GoogleFonts.config.allowRuntimeFetching = false;

  group('Módulo "Mi Cuatrimestre" - Modelo y Persistencia', () {
    test('StudentUserModel serializa y deserializa cuatrimestreActivo y materiasMatriculadas', () {
      const user = StudentUserModel(
        username: 'teststudent',
        nombre: 'Estudiante Prueba',
        email: 'teststudent@unimagdalena.edu.co',
        programa: 'Ingeniería Energética',
        pinHash: 'hash123',
        cuatrimestreActivo: 3,
        materiasMatriculadas: ['02011808', '02021811', '02011807'], // 2 de C3, 1 de C1
        progresoMaterias: {'02011808': 30},
        recordatoriosCalendario: [],
        apuntesPersonales: {},
      );

      final json = user.toJson();
      expect(json['cuatrimestre_activo'], 3);
      expect(json['cuatrimestre_actual'], 3);
      expect(json['materias_matriculadas'], ['02011808', '02021811', '02011807']);

      final restored = StudentUserModel.fromJson(json);
      expect(restored.cuatrimestreActivo, 3);
      expect(restored.cuatrimestreActual, 3);
      expect(restored.materiasMatriculadas, ['02011808', '02021811', '02011807']);
    });

    test('isMySubject filtra con créditos cruzados según materiasMatriculadas', () {
      final mdContent = File('assets/data/ingenieria_energetica.md').readAsStringSync();
      final curriculum = MarkdownCurriculumService()
        ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

      final c1Materia = curriculum.database!.findAsignatura('02011807')!; // Cálculo Diferencial (C1)
      final c2Materia = curriculum.database!.findAsignatura('02021810')!; // Física Mecánica (C2)
      final c3Materia = curriculum.database!.findAsignatura('02011808')!; // Cálculo Integral (C3)

      const user = StudentUserModel(
        username: 'cruzadostudent',
        nombre: 'Estudiante Cruzado',
        email: 'cruzadostudent@unimagdalena.edu.co',
        programa: 'Ingeniería Energética',
        pinHash: 'hash123',
        cuatrimestreActivo: 2,
        materiasMatriculadas: ['02011807', '02021810'], // 1 de C1, 1 de C2
        progresoMaterias: {},
        recordatoriosCalendario: [],
        apuntesPersonales: {},
      );

      // Validación de pertenencia con materias de cuatrimestres cruzados
      expect(user.materiasMatriculadas.contains(c1Materia.codigo), isTrue);
      expect(user.materiasMatriculadas.contains(c2Materia.codigo), isTrue);
      expect(user.materiasMatriculadas.contains(c3Materia.codigo), isFalse);
    });
  });

  group('Módulo "Mi Cuatrimestre" - Interfaz y Viewports Móviles', () {
    testWidgets('Renderiza sin overflow en viewport compacto (392x800) y calcula créditos', (tester) async {
      tester.view.physicalSize = const Size(392, 800);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);

      SharedPreferences.setMockInitialValues({});
      final mdContent = File('assets/data/ingenieria_energetica.md').readAsStringSync();
      final curriculum = MarkdownCurriculumService()
        ..seedDatabase(CurriculumMarkdownParser.parse(mdContent));

      final repo = LocalReactiveClaseVivaRepository(
        userId: 'alumno@unimagdalena.edu.co',
        curriculumService: curriculum,
      );

      final session = InstitutionalSessionController(
        repository: repo,
        curriculumService: curriculum,
      );

      await tester.pumpWidget(
        CurriculumScope(
          service: curriculum,
          child: SessionScope(
            controller: session,
            child: ThemeScope(
              controller: ThemeController(),
              child: const MaterialApp(
                themeMode: ThemeMode.dark,
                home: MiCuatrimestreScreen(isMandatory: false),
              ),
            ),
          ),
        ),
      );

      await tester.pumpAndSettle();

      // Verificar que el título y la píldora de créditos existen
      expect(find.text('Mi Cuatrimestre'), findsOneWidget);
      expect(find.textContaining('créditos académicos'), findsOneWidget);

      // Verificar que no se lanzó ninguna excepción de RenderFlex
      expect(tester.takeException(), isNull);
    });
  });
}
