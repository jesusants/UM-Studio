import 'package:flutter_test/flutter_test.dart';
import 'package:um_studio/core/utils/institutional_validator.dart';
import 'package:um_studio/data/models/global_env_config.dart';
import 'package:um_studio/data/models/student_user_model.dart';

void main() {
  group('Global Environment & Admin Auth Tests', () {
    test('Master Admin jsierra authentication and PIN validation', () {
      expect(InstitutionalValidator.isSuperAdmin('jsierra'), isTrue);
      expect(
        InstitutionalValidator.isSuperAdmin('jsierra@unimagdalena.edu.co'),
        isTrue,
      );
      expect(InstitutionalValidator.isSuperAdmin('estudiante123'), isFalse);

      expect(
        InstitutionalValidator.verifyMasterAdmin(
          userOrEmail: 'jsierra',
          pin: '81991042249674',
        ),
        isTrue,
      );
      expect(
        InstitutionalValidator.verifyMasterAdmin(
          userOrEmail: 'jsierra@unimagdalena.edu.co',
          pin: '81991042249674',
        ),
        isTrue,
      );
      expect(
        InstitutionalValidator.verifyMasterAdmin(
          userOrEmail: 'jsierra',
          pin: 'pin_incorrecto',
        ),
        isFalse,
      );
    });

    test('StudentUserModel serialization preserves isAdmin flag', () {
      const adminUser = StudentUserModel(
        nombre: 'Jesús Sierra',
        email: 'jsierra@unimagdalena.edu.co',
        programa: 'Ingeniería Energética',
        username: 'jsierra',
        pinHash: 'test_hash',
        progresoMaterias: {},
        recordatoriosCalendario: [],
        apuntesPersonales: {},
        isAdmin: true,
      );
      final json = adminUser.toJson();
      expect(json['is_admin'], isTrue);

      final restored = StudentUserModel.fromJson(json);
      expect(restored.isAdmin, isTrue);
      expect(restored.username, equals('jsierra'));

      // Regular user
      const regularUser = StudentUserModel(
        nombre: 'Estudiante Prueba',
        email: '2023114000@unimagdalena.edu.co',
        programa: 'Ingeniería Energética',
        username: '2023114000',
        pinHash: 'test_hash',
        progresoMaterias: {},
        recordatoriosCalendario: [],
        apuntesPersonales: {},
        isAdmin: false,
      );
      final regJson = regularUser.toJson();
      final restoredReg = StudentUserModel.fromJson(regJson);
      expect(restoredReg.isAdmin, isFalse);
    });

    test('GlobalEnvConfig serialization and copyWith clamps', () {
      const config = GlobalEnvConfig(
        aiTemperature: 0.7,
        aiMaxTokens: 2048,
        corteActivoGlobal: 2,
        newsRefreshMinutes: 10,
        maintenanceMode: false,
      );

      final json = config.toJson();
      expect(json['ai_temperature'], equals(0.7));
      expect(json['corte_activo_global'], equals(2));
      expect(json['maintenance_mode'], isFalse);

      final fromJson = GlobalEnvConfig.fromJson(json);
      expect(fromJson.aiTemperature, equals(0.7));
      expect(fromJson.corteActivoGlobal, equals(2));

      // Test clamps
      final clamped = config.copyWith(
        aiTemperature: 2.5, // should clamp to 1.0
        corteActivoGlobal: 5, // should clamp to 3
        newsRefreshMinutes: 0, // should clamp to 1
      );
      expect(clamped.aiTemperature, equals(1.0));
      expect(clamped.corteActivoGlobal, equals(3));
      expect(clamped.newsRefreshMinutes, equals(1));
    });
  });
}
