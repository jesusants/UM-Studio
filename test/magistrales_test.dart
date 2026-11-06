import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:um_studio/data/services/markdown_curriculum_service.dart';

void main() {
  test('Fundamentos de Electricidad II contiene 7 Clases Magistrales con slides y KaTeX', () {
    final content = File('db/ingenieria_energetica.md').readAsStringSync();
    final db = CurriculumMarkdownParser.parse(content);
    final asig = db.findAsignatura('03041820');

    expect(asig, isNotNull);
    expect(asig!.nombre, 'Fundamentos de Electricidad II');
    expect(asig.temas.length >= 9, isTrue);
    expect(asig.clasesMagistrales.length, 7);

    for (final m in asig.clasesMagistrales) {
      expect(m.titulo.isNotEmpty, isTrue);
      expect(m.objetivo.isNotEmpty, isTrue);
      expect(m.conceptoClaveLatex.isNotEmpty, isTrue);
      expect(m.ejemplo.isNotEmpty, isTrue);
      expect(m.modalidad, 'magistral');
    }

    // Comprobar resolución por key compuesto
    final m1 = db.resolveTemaEstudio('03041820_magistral_1');
    expect(m1, isNotNull);
    expect(m1!.tituloTema, contains('Dispositivos de Almacenamiento'));
    expect(m1.slides.isNotEmpty, isTrue);

    final m7 = db.resolveTemaEstudio('03041820_magistral_7');
    expect(m7, isNotNull);
    expect(m7!.tituloTema, contains('Taller'));
  });

  test('Física Mecánica contiene 7 Clases Magistrales con slides y KaTeX desde apuntes de tablero', () {
    final content = File('db/ingenieria_energetica.md').readAsStringSync();
    final db = CurriculumMarkdownParser.parse(content);
    final asig = db.findAsignatura('02021810');

    expect(asig, isNotNull);
    expect(asig!.nombre, 'Física Mecánica');
    expect(asig.clasesMagistrales.length, 7);

    for (final m in asig.clasesMagistrales) {
      expect(m.titulo.isNotEmpty, isTrue);
      expect(m.objetivo.isNotEmpty, isTrue);
      expect(m.conceptoClaveLatex.isNotEmpty, isTrue);
      expect(m.ejemplo.isNotEmpty, isTrue);
      expect(m.modalidad, 'magistral');
      expect(m.slides.length, 8);
    }

    // Comprobar resolución por key compuesto
    final m1 = db.resolveTemaEstudio('02021810_magistral_1');
    expect(m1, isNotNull);
    expect(m1!.tituloTema, contains('Cinemática Diferencial'));
    expect(m1.slides.length, 8);

    final m2 = db.resolveTemaEstudio('02021810_magistral_2');
    expect(m2, isNotNull);
    expect(m2!.tituloTema, contains('Dinámica Circular'));

    final m3 = db.resolveTemaEstudio('02021810_magistral_3');
    expect(m3, isNotNull);
    expect(m3!.tituloTema, contains('Leyes de Newton'));

    final m4 = db.resolveTemaEstudio('02021810_magistral_4');
    expect(m4, isNotNull);
    expect(m4!.tituloTema, contains('Plano Inclinado'));

    final m5 = db.resolveTemaEstudio('02021810_magistral_5');
    expect(m5, isNotNull);
    expect(m5!.tituloTema, contains('Estática de la Partícula'));

    final m6 = db.resolveTemaEstudio('02021810_magistral_6');
    expect(m6, isNotNull);
    expect(m6!.tituloTema, contains('Trabajo Mecánico'));

    final m7 = db.resolveTemaEstudio('02021810_magistral_7');
    expect(m7, isNotNull);
    expect(m7!.tituloTema, contains('Fuerzas Conservativas'));
  });
}
