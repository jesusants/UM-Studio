/// Entidad de dominio para un tema oficial de cátedra (`temas_estudio`).
class TemaEstudioEntity {
  const TemaEstudioEntity({
    required this.id,
    required this.nombreAsignatura,
    required this.numeroTema,
    required this.objetivo,
    required this.conceptoClaveLatex,
    required this.ejemplo,
    this.sincronizacionPorcentaje = 94,
  });

  final String id;
  final String nombreAsignatura;
  final int numeroTema;
  final String objetivo;
  final String conceptoClaveLatex;
  final String ejemplo;
  final int sincronizacionPorcentaje;

  String get badgeTema => 'Tema $numeroTema';
}
