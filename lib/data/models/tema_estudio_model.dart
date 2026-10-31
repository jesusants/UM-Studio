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
    super.corte = 1,
    super.modalidad = 'tecnica',
    super.verbalizacionIngles = '',
    super.slides = const [],
  });

  factory TemaEstudioModel.fromJson(Map<String, dynamic> json) {
    final rawNum = json['numero_tema'] ?? json['numero'] ?? 1;
    final rawCorte = json['corte'] ?? 1;
    final rawSlides = json['slides'];
    final parsedSlides = <SlideDeckItem>[];
    if (rawSlides is Iterable) {
      var idx = 1;
      for (final s in rawSlides) {
        if (s is Map) {
          parsedSlides.add(
            SlideDeckItem.fromMap(
              s.map((k, v) => MapEntry(k.toString(), v)),
              fallbackNum: idx,
            ),
          );
          idx++;
        }
      }
    }

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
      corte: rawCorte is num
          ? rawCorte.toInt().clamp(1, 3)
          : (int.tryParse(rawCorte.toString()) ?? 1).clamp(1, 3),
      modalidad: (json['modalidad'] ?? 'tecnica').toString(),
      verbalizacionIngles: (json['verbalizacion_ingles'] ?? '').toString(),
      slides: List.unmodifiable(parsedSlides),
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'nombre_asignatura': nombreAsignatura,
        'numero_tema': numeroTema,
        'corte': corte,
        'modalidad': modalidad,
        'titulo': tituloTema,
        'objetivo': objetivo,
        'concepto_clave_latex': conceptoClaveLatex,
        if (verbalizacionIngles.isNotEmpty)
          'verbalizacion_ingles': verbalizacionIngles,
        'ejemplo': ejemplo,
        'bloque_sugerido': bloqueSugerido,
        'codigo_asignatura': codigoAsignatura,
        'cuatrimestre': cuatrimestre,
        'creditos': creditos,
        'sincronizacion_porcentaje': sincronizacionPorcentaje,
        if (slides.isNotEmpty)
          'slides': slides.map((s) => s.toJson()).toList(growable: false),
      };
}
