import '../../domain/entities/tema_estudio_entity.dart';

/// DTO con serialización `fromJson` / `toJson` para la tabla `temas_estudio`.
class TemaEstudioModel extends TemaEstudioEntity {
  const TemaEstudioModel({
    required super.id,
    required super.nombreAsignatura,
    required super.numeroTema,
    required super.objetivo,
    required super.conceptoClaveLatex,
    required super.ejemplo,
    super.sincronizacionPorcentaje = 94,
  });

  factory TemaEstudioModel.fromJson(Map<String, dynamic> json) {
    return TemaEstudioModel(
      id: (json['id'] ?? '').toString(),
      nombreAsignatura: (json['nombre_asignatura'] ?? '').toString(),
      numeroTema: (json['numero_tema'] is num)
          ? (json['numero_tema'] as num).toInt()
          : int.tryParse((json['numero_tema'] ?? '1').toString()) ?? 1,
      objetivo: (json['objetivo'] ?? '').toString(),
      conceptoClaveLatex: (json['concepto_clave_latex'] ?? '').toString(),
      ejemplo: (json['ejemplo'] ?? '').toString(),
      sincronizacionPorcentaje: (json['sincronizacion_porcentaje'] is num)
          ? (json['sincronizacion_porcentaje'] as num).toInt()
          : 94,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'nombre_asignatura': nombreAsignatura,
        'numero_tema': numeroTema,
        'objetivo': objetivo,
        'concepto_clave_latex': conceptoClaveLatex,
        'ejemplo': ejemplo,
        'sincronizacion_porcentaje': sincronizacionPorcentaje,
      };
}
