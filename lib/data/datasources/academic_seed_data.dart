import '../../domain/entities/subject_summary.dart';
import '../models/tema_estudio_model.dart';

/// Fuente de datos semilla de respaldo para pruebas unitarias.
/// El temario oficial se carga dinámicamente desde `ingenieria_energetica.md`.
@Deprecated('Utilizar MarkdownCurriculumService para cargar el temario real')
abstract final class AcademicSeedData {
  static const Map<String, TemaEstudioModel> temasEstudio = {
    'fisica': TemaEstudioModel(
      id: 'fisica',
      nombreAsignatura: 'Física Mecánica y Termodinámica',
      numeroTema: 2,
      objetivo:
          'Comprender la segunda ley de Newton en sistemas inerciales y cuantificar el efecto disipativo de la fuerza de rozamiento cinético y estático sobre cuerpos rígidos.',
      conceptoClaveLatex:
          r'\sum \vec{F} = m \cdot \vec{a} \quad ; \quad f_k = \mu_k \cdot N',
      ejemplo:
          'Un bloque de masa m sobre una superficie horizontal rugosa experimenta una reacción normal N = m·g y una fuerza de oposición cinética f_k = μ_k·N. Al aplicar una tracción horizontal F, la aceleración neta del bloque queda determinada por a = (F − μ_k·m·g) / m.',
      sincronizacionPorcentaje: 94,
    ),
    'calculo': TemaEstudioModel(
      id: 'calculo',
      nombreAsignatura: 'Cálculo Diferencial e Integral',
      numeroTema: 4,
      objetivo:
          'Dominar la técnica de integración por partes derivada de la regla diferencial del producto para evaluar integrales de funciones trascendentes acopladas con polinomios.',
      conceptoClaveLatex: r'\int u \, dv = u \cdot v - \int v \, du',
      ejemplo:
          'En el cálculo de la integral indefinida de x·e^x dx, se elige u = x (reduciendo el grado algebraico al derivar, du = dx) y dv = e^x dx (cuya antiderivada inmediata es v = e^x), resultando en x·e^x − e^x + C.',
      sincronizacionPorcentaje: 96,
    ),
    'electricidad': TemaEstudioModel(
      id: 'electricidad',
      nombreAsignatura: 'Fundamentos de Electricidad',
      numeroTema: 3,
      objetivo:
          'Reducir cualquier red eléctrica lineal bilateral de dos terminales a un circuito equivalente de Thévenin o Norton para analizar la transferencia máxima de potencia hacia cargas variables.',
      conceptoClaveLatex:
          r'V_{\text{th}} = I_{\text{N}} \cdot R_{\text{th}} \quad ; \quad P_{\max} = \frac{V_{\text{th}}^2}{4 R_{\text{th}}}',
      ejemplo:
          'Retirando la impedancia de carga R_L y pasivando las fuentes independientes (fuentes de tensión en cortocircuito y de corriente en circuito abierto), se calcula la resistencia equivalente R_th vista desde los terminales A-B junto con la tensión en circuito abierto V_th.',
      sincronizacionPorcentaje: 92,
    ),
    'algebra': TemaEstudioModel(
      id: 'algebra',
      nombreAsignatura: 'Álgebra Lineal',
      numeroTema: 5,
      objetivo:
          'Representar transformaciones lineales entre espacios vectoriales de dimensión finita mediante matrices asociadas y caracterizar geométricamente su núcleo (ker) e imagen (im).',
      conceptoClaveLatex:
          r'T(\alpha \vec{u} + \beta \vec{v}) = \alpha T(\vec{u}) + \beta T(\vec{v}) \quad ; \quad \dim(V) = \operatorname{nul}(T) + \operatorname{rg}(T)',
      ejemplo:
          'Una rotación antihoraria de 90° en el plano ℝ² preserva combinaciones lineales y se representa en la base canónica mediante la matriz ortogonal A = [[0, −1], [1, 0]], presentando núcleo trivial ker(T) = {0} y rango completo rg(T) = 2.',
      sincronizacionPorcentaje: 91,
    ),
  };

  static final List<SubjectSummaryEntity> subjects = [
    SubjectSummaryEntity(
      id: 'fisica',
      category: 'Física',
      title: 'Física Mecánica y Termodinámica',
      nextTopic: 'Unidad 2: Leyes de Newton',
      progress: 0.50,
      accentResolver: (p) => p.green,
      active: true,
    ),
    SubjectSummaryEntity(
      id: 'calculo',
      category: 'Matemáticas',
      title: 'Cálculo Diferencial e Integral',
      nextTopic: 'Técnicas de Integración',
      progress: 0.75,
      accentResolver: (p) => p.indigo,
    ),
    SubjectSummaryEntity(
      id: 'electricidad',
      category: 'Ingeniería',
      title: 'Fundamentos de Electricidad',
      nextTopic: 'Teorema de Thévenin y Norton',
      progress: 0.60,
      accentResolver: (p) => p.orange,
    ),
    SubjectSummaryEntity(
      id: 'algebra',
      category: 'Ciencias Básicas',
      title: 'Álgebra Lineal',
      nextTopic: 'Transformaciones Lineales',
      progress: 0.30,
      accentResolver: (p) => p.inverse,
    ),
  ];

  static const List<AcademicEventEntity> calendarEvents = [
    AcademicEventEntity(
      time: '08:00',
      kind: AcademicEventKind.clase,
      title: 'Fundamentos de Electricidad',
      subtitle: 'Tema: Teorema de Thévenin y Norton • Aula C-201',
      days: [26, 28, 30],
    ),
    AcademicEventEntity(
      time: '10:00',
      kind: AcademicEventKind.clase,
      title: 'Física Mecánica y Termodinámica',
      subtitle: 'Tema: Unidad 2 - Leyes de Newton • Aula C-102',
      days: [26, 27, 29, 30],
    ),
    AcademicEventEntity(
      time: '14:00',
      kind: AcademicEventKind.parcial,
      title: 'Parcial Corte 2 • Cálculo Integral (30%)',
      subtitle: 'Salón A-204 • Docente: C. Mendoza',
      days: [31],
    ),
    AcademicEventEntity(
      time: '16:00',
      kind: AcademicEventKind.bloque,
      title: 'Práctica de Integrales por Partes',
      subtitle: 'Plantilla de estudio individual • 50 min',
      days: [27, 28, 30],
    ),
    AcademicEventEntity(
      time: '23:59',
      kind: AcademicEventKind.entrega,
      title: 'Taller #2: Dinámica de Partículas',
      subtitle: 'Sincronizado desde Moodle',
      days: [29, 30, 31],
    ),
  ];
}
