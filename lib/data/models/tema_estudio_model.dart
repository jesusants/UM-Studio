import '../../domain/entities/tema_estudio_entity.dart';

/// DTO con serialización `fromJson` / `toJson` para un tema de estudio.
class TemaEstudioModel extends TemaEstudioEntity {
  const TemaEstudioModel({
    required super.id,
    required super.nombreAsignatura,
    required super.numeroTema,
    required super.objetivo,
    required super.conceptoClaveLatex,
    required super.ejemplo,
    super.tituloTema = '',
    super.bloqueSugerido = '',
    super.codigoAsignatura = '',
    super.cuatrimestre = 1,
    super.creditos = 3,
    super.sincronizacionPorcentaje = 96,
  });

  factory TemaEstudioModel.fromJson(Map<String, dynamic> json) {
    final rawNum = json['numero_tema'] ?? json['numero'] ?? 1;
    return TemaEstudioModel(
      id: (json['id'] ?? '').toString(),
      nombreAsignatura: (json['nombre_asignatura'] ?? '').toString(),
      numeroTema: rawNum is num
          ? rawNum.toInt()
          : int.tryParse(rawNum.toString()) ?? 1,
      objetivo: (json['objetivo'] ?? '').toString(),
      conceptoClaveLatex: (json['concepto_clave_latex'] ?? '').toString(),
      ejemplo: (json['ejemplo'] ?? '').toString(),
      tituloTema: (json['titulo'] ?? '').toString(),
      bloqueSugerido:
          (json['bloque_sugerido'] ?? json['bloque_estudio'] ?? '').toString(),
      codigoAsignatura: (json['codigo_asignatura'] ?? '').toString(),
      cuatrimestre: json['cuatrimestre'] is num
          ? (json['cuatrimestre'] as num).toInt()
          : 1,
      creditos:
          json['creditos'] is num ? (json['creditos'] as num).toInt() : 3,
      sincronizacionPorcentaje: (json['sincronizacion_porcentaje'] is num)
          ? (json['sincronizacion_porcentaje'] as num).toInt()
          : 96,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'nombre_asignatura': nombreAsignatura,
        'numero_tema': numeroTema,
        'titulo': tituloTema,
        'objetivo': objetivo,
        'concepto_clave_latex': conceptoClaveLatex,
        'ejemplo': ejemplo,
        'bloque_sugerido': bloqueSugerido,
        'codigo_asignatura': codigoAsignatura,
        'cuatrimestre': cuatrimestre,
        'creditos': creditos,
        'sincronizacion_porcentaje': sincronizacionPorcentaje,
      };
}
