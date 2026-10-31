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

  String get badgeTema => 'Tema $numeroTema';
}
