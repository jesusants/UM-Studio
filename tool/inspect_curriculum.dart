import 'dart:io';
import 'package:yaml/yaml.dart';

void main() {
  final file = File('db/ingenieria_energetica.md');
  final content = file.readAsStringSync();
  final endYaml = content.indexOf('\n---', 4);
  final yamlText = content.substring(4, endYaml);
  final doc = loadYaml(yamlText) as YamlMap;
  final malla = doc['malla_curricular'] as YamlList;

  print('Total Cuatrimestres: ${malla.length}');
  for (final c in malla) {
    final numCuat = c['cuatrimestre'];
    final asigs = c['asignaturas'] as YamlList;
    print('Cuatrimestre $numCuat (${asigs.length} asignaturas):');
    for (final a in asigs) {
      final cod = a['codigo'];
      final nom = a['nombre'];
      final temas = a['temas'] as YamlList?;
      print('  [$cod] $nom: ${temas?.length ?? 0} temas');
    }
  }
}
