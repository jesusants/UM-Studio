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
    expect(m7!.tituloTema, contains('Taller de Cátedra'));
  });
}
