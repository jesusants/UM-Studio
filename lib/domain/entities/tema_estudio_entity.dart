/// Modelo inmutable de una diapositiva dentro del visor minimalista de Inglés General.
class SlideDeckItem {
  const SlideDeckItem({
    required this.numero,
    required this.seccion,
    required this.titulo,
    required this.puntos,
    this.tabla = const [],
    this.ejemplo = '',
  });

  final int numero;
  final String seccion;
  final String titulo;
  final List<String> puntos;
  final List<List<String>> tabla;
  final String ejemplo;

  factory SlideDeckItem.fromMap(Map<String, dynamic> map, {int fallbackNum = 1}) {
    final rawNum = map['numero'] ?? map['slide'] ?? fallbackNum;
    final parsedNum = rawNum is num
        ? rawNum.toInt()
        : int.tryParse(rawNum.toString()) ?? fallbackNum;

    final rawPuntos = map['puntos'] ?? map['bullets'];
    final parsedPuntos = <String>[];
    if (rawPuntos is Iterable) {
      for (final p in rawPuntos) {
        if (p != null) {
          final text = p.toString().trim();
          if (text.isNotEmpty) parsedPuntos.add(text);
        }
      }
    }

    final rawTabla = map['tabla'] ?? map['table'];
    final parsedTabla = <List<String>>[];
    if (rawTabla is Iterable) {
      for (final row in rawTabla) {
        if (row is Iterable) {
          final cells = row.map((c) => (c ?? '').toString().trim()).toList();
          if (cells.isNotEmpty) parsedTabla.add(List.unmodifiable(cells));
        }
      }
    }

    return SlideDeckItem(
      numero: parsedNum,
      seccion: (map['seccion'] ?? map['etiqueta'] ?? 'SLIDE').toString(),
      titulo: (map['titulo'] ?? '').toString(),
      puntos: List.unmodifiable(parsedPuntos),
      tabla: List.unmodifiable(parsedTabla),
      ejemplo: (map['ejemplo'] ?? '').toString(),
    );
  }

  Map<String, dynamic> toJson() => {
        'numero': numero,
        'seccion': seccion,
        'titulo': titulo,
        'puntos': puntos,
        if (tabla.isNotEmpty) 'tabla': tabla,
        if (ejemplo.isNotEmpty) 'ejemplo': ejemplo,
      };
}

/// Entidad de dominio para un tema oficial de cátedra (`ingenieria_energetica.md`).
class TemaEstudioEntity {
  const TemaEstudioEntity({
    required this.id,
    required this.nombreAsignatura,
    required this.numeroTema,
    required this.objetivo,
    required this.conceptoClaveLatex,
    required this.ejemplo,
    this.tituloTema = '',
    this.bloqueSugerido = '',
    this.codigoAsignatura = '',
    this.cuatrimestre = 1,
    this.creditos = 3,
    this.sincronizacionPorcentaje = 96,
    this.corte = 1,
    this.modalidad = 'tecnica',
    this.verbalizacionIngles = '',
    this.slides = const [],
  });

  final String id;
  final String nombreAsignatura;
  final int numeroTema;
  final String objetivo;
  final String conceptoClaveLatex;
  final String ejemplo;
  final String tituloTema;
  final String bloqueSugerido;
  final String codigoAsignatura;
  final int cuatrimestre;
  final int creditos;
  final int sincronizacionPorcentaje;
  final int corte;
  final String modalidad;
  final String verbalizacionIngles;
  final List<SlideDeckItem> slides;

  String get badgeTema => 'Tema $numeroTema';

  bool get esInglesGeneral => modalidad == 'general';

  bool get esNotacionIngenieria => modalidad == 'notacion_ingenieria';

  bool get usaKatex =>
      !esInglesGeneral && conceptoClaveLatex.trim().isNotEmpty;

  String get etiquetaCorte {
    switch (corte) {
      case 1:
        return 'Corte 1 • 30%';
      case 2:
        return 'Corte 2 • 30%';
      default:
        return 'Corte 3 • 40%';
    }
  }
}
