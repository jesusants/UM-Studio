import 'package:flutter/material.dart';

/// Identificadores únicos de todos los simuladores interactivos animados (Cuatrimestres 1 a 4).
enum LabSimId {
  // Cuatrimestre 1
  calcDerivadaTangente,
  calcLimites,
  algebraTransformaciones2D,
  progOrdenamiento,
  progRegresionLineal,
  introFlujoEnergetico,

  // Cuatrimestre 2
  fisicaMasaResorte,
  fisicaTiroParabolico,
  fisicaPlanoInclinadoDcl,
  fisicaColisiones1D,
  integralRiemann,
  integralSolidoRevolucion,
  quimicaGasesIdeales,
  elec1CircuitoDc,

  // Cuatrimestre 3
  ondasViajerasArmonicos,
  ondasPenduloFase,
  modelacionOsciladorAmortiguado,
  elec2FasoresCa,
  elec2TransitorioRcRl,
  disenoProyeccion3D,

  // Cuatrimestre 4
  emLeyFaraday,
  termoCicloPvPiston,
  probTableroGalton,
  hidraulicaVenturiBernoulli,
}

/// Metadatos de un simulador específico dentro de una asignatura.
class LabSimulatorDescriptor {
  const LabSimulatorDescriptor({
    required this.id,
    required this.shortTitle,
    required this.fullTitle,
    required this.formulaBadge,
    required this.icon,
    required this.keywords,
  });

  final LabSimId id;
  final String shortTitle;
  final String fullTitle;
  final String formulaBadge;
  final IconData icon;
  final List<String> keywords;
}

/// Configuración resuelta para una asignatura específica sin mezcla de otras materias.
class SubjectLabConfig {
  const SubjectLabConfig({
    required this.subjectCode,
    required this.subjectName,
    required this.cuatrimestre,
    required this.simulators,
    required this.initialSimulator,
  });

  final String subjectCode;
  final String subjectName;
  final int cuatrimestre;
  final List<LabSimulatorDescriptor> simulators;
  final LabSimulatorDescriptor initialSimulator;
}

/// Registro centralizado de enrutamiento contextual de Laboratorios Gráficos por asignatura y tema.
class SubjectLabRegistry {
  const SubjectLabRegistry._();

  static String _norm(String input) {
    return input
        .toLowerCase()
        .trim()
        .replaceAll('á', 'a')
        .replaceAll('é', 'e')
        .replaceAll('í', 'i')
        .replaceAll('ó', 'o')
        .replaceAll('ú', 'u')
        .replaceAll('ü', 'u');
  }

  /// Determina si una asignatura requiere y dispone de Laboratorio Gráfico Interactivo.
  /// Excluye asignaturas humanísticas, idiomas y lectoescritura.
  static bool hasLabsForSubject({
    String codigo = '',
    required String nombre,
  }) {
    final cleanCode = codigo.trim();
    final normName = _norm(nombre);

    // Exclusión explícita de materias no gráficas (Inglés, Procesos Lectores, Constitución, etc.)
    const excludedCodes = <String>{
      '01011801', // Procesos Lectores, Escriturales y Orales
      '01021802', // General English I
      '01021803', // General English II
      '01021804', // General English III
      '01021805', // General English IV
      '01021806', // General English V
      '04031827', // Legislación y Regulación Energética
      '05011831', // Metodología de la Investigación
      '05011832', // Formulación de Proyectos
      '05011833', // Evaluación y Gestión de Proyectos
      '04031829', // Comunidades Energéticas Sostenibles
      '04031830', // Transición Energética Justa
      '07011855', // Inmersión Profesional
      '07021856', // Modalidad de Grado
    };
    if (excludedCodes.contains(cleanCode)) return false;

    const excludedKeywords = <String>[
      'procesos lectores',
      'lectores',
      'english',
      'ingles',
      'constitucion',
      'humanidades',
      'etica',
      'legislacion',
      'metodologia de la investigacion',
      'inmersion profesional',
      'modalidad de grado',
    ];
    for (final kw in excludedKeywords) {
      if (normName.contains(kw)) return false;
    }

    return resolve(codigo: codigo, nombre: nombre) != null;
  }

  /// Resuelve exclusivamente los simuladores de la asignatura activa y preselecciona
  /// el experimento más afín al tema que el estudiante está estudiando.
  static SubjectLabConfig? resolve({
    String codigo = '',
    required String nombre,
    String temaTitulo = '',
    String explicitHint = '',
  }) {
    final cleanCode = codigo.trim();
    final normName = _norm(nombre);
    final normTopic = _norm('$temaTitulo $explicitHint');

    // Verificar primero hints explícitos de anuncios o bloques embebidos
    if (normName.contains('anuncio academico')) {
      if (normTopic.contains('fasor') || normTopic.contains('ac')) {
        return _buildConfig(
          code: '03041820',
          name: 'Fundamentos de Electricidad II',
          cuatrimestre: 3,
          sims: _electricidad2Sims,
          topicNorm: normTopic,
        );
      }
      if (normTopic.contains('integral') || normTopic.contains('derivada')) {
        return _buildConfig(
          code: '02011807',
          name: 'Cálculo Diferencial',
          cuatrimestre: 1,
          sims: _calculoDiferencialSims,
          topicNorm: normTopic,
        );
      }
      if (normTopic.contains('termo') || normTopic.contains('solar')) {
        return _buildConfig(
          code: '03021817',
          name: 'Termodinámica',
          cuatrimestre: 4,
          sims: _termodinamicaSims,
          topicNorm: normTopic,
        );
      }
    }

    // -------------------------------------------------------------------------
    // CUATRIMESTRE 1
    // -------------------------------------------------------------------------
    if (cleanCode == '02011807' || normName.contains('calculo diferencial')) {
      return _buildConfig(
        code: '02011807',
        name: 'Cálculo Diferencial',
        cuatrimestre: 1,
        sims: _calculoDiferencialSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '02011809' || normName.contains('algebra lineal')) {
      return _buildConfig(
        code: '02011809',
        name: 'Álgebra Lineal',
        cuatrimestre: 1,
        sims: _algebraLinealSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03011813' ||
        cleanCode == '03011814' ||
        normName.contains('programacion')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '03011813',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Fundamentos de Programación e IA',
        cuatrimestre: 1,
        sims: _programacionIaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '04011822' ||
        normName.contains('introduccion a la ingenieria energetica') ||
        normName.contains('conversion de energia') ||
        normName.contains('sistemas energeticos') ||
        normName.contains('energia solar') ||
        normName.contains('energia eolica') ||
        normName.contains('energia de biomasa') ||
        normName.contains('energia geotermica') ||
        normName.contains('energia mareomotriz') ||
        normName.contains('eficiencia energetica') ||
        normName.contains('hydrogen')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '04011822',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Introducción a la Ingeniería Energética',
        cuatrimestre: 1,
        sims: _introEnergiaSims,
        topicNorm: normTopic,
      );
    }

    // -------------------------------------------------------------------------
    // CUATRIMESTRE 2
    // -------------------------------------------------------------------------
    if (cleanCode == '02021810' ||
        normName.contains('fisica mecanica') ||
        normName == 'fisica i') {
      return _buildConfig(
        code: '02021810',
        name: 'Física Mecánica',
        cuatrimestre: 2,
        sims: _fisicaMecanicaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '02011808' || normName.contains('calculo integral')) {
      return _buildConfig(
        code: '02011808',
        name: 'Cálculo Integral',
        cuatrimestre: 2,
        sims: _calculoIntegralSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '02031812' || normName.contains('quimica')) {
      return _buildConfig(
        code: '02031812',
        name: 'Química Aplicada',
        cuatrimestre: 2,
        sims: _quimicaAplicadaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03041819' ||
        normName.contains('electricidad i') &&
            !normName.contains('electricidad ii')) {
      return _buildConfig(
        code: '03041819',
        name: 'Fundamentos de la Electricidad I',
        cuatrimestre: 2,
        sims: _electricidad1Sims,
        topicNorm: normTopic,
      );
    }

    // -------------------------------------------------------------------------
    // CUATRIMESTRE 3
    // -------------------------------------------------------------------------
    if (cleanCode == '02021811' || normName.contains('calor y ondas')) {
      return _buildConfig(
        code: '02021811',
        name: 'Calor y Ondas',
        cuatrimestre: 3,
        sims: _calorYOndasSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '04021825' ||
        normName.contains('modelacion matematica') ||
        normName.contains('ecuaciones diferenciales')) {
      return _buildConfig(
        code: '04021825',
        name: 'Modelación Matemática para Ingeniería',
        cuatrimestre: 3,
        sims: _modelacionMatematicaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03041820' ||
        normName.contains('electricidad ii') ||
        normName.contains('maquinas electricas') ||
        normName.contains('instalaciones electricas') ||
        normName.contains('redes de transporte')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '03041820',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Fundamentos de Electricidad II',
        cuatrimestre: 3,
        sims: _electricidad2Sims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '04021823' ||
        normName.contains('diseno y modelado en 3d') ||
        normName.contains('modelado en 3d') ||
        normName.contains('diseno y simulacion')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '04021823',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Ingeniería del Diseño y Modelado en 3D',
        cuatrimestre: 3,
        sims: _diseno3DSims,
        topicNorm: normTopic,
      );
    }

    // -------------------------------------------------------------------------
    // CUATRIMESTRE 4
    // -------------------------------------------------------------------------
    if (cleanCode == '03041821' ||
        normName.contains('electricidad y magnetismo') ||
        normName.contains('magnetismo') ||
        normName.contains('mediciones e instrumentacion')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '03041821',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Electricidad y Magnetismo',
        cuatrimestre: 4,
        sims: _electricidadMagnetismoSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03021817' ||
        normName.contains('termodinamica') ||
        normName.contains('transferencia de calor') ||
        normName.contains('almacenamiento de la energia')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '03021817',
        name: nombre.trim().isNotEmpty ? nombre.trim() : 'Termodinámica',
        cuatrimestre: 4,
        sims: _termodinamicaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03031818' ||
        normName.contains('probabilidad') ||
        normName.contains('estadistica')) {
      return _buildConfig(
        code: '03031818',
        name: 'Probabilidad y Estadística',
        cuatrimestre: 4,
        sims: _probabilidadEstadisticaSims,
        topicNorm: normTopic,
      );
    }

    if (cleanCode == '03021815' ||
        cleanCode == '03021816' ||
        cleanCode == '06021845' ||
        normName.contains('hidraulica') ||
        normName.contains('neumatica') ||
        normName.contains('fluidos')) {
      return _buildConfig(
        code: cleanCode.isNotEmpty ? cleanCode : '03021815',
        name: nombre.trim().isNotEmpty
            ? nombre.trim()
            : 'Fundamentos de Hidráulica y Neumática',
        cuatrimestre: 4,
        sims: _hidraulicaNeumaticaSims,
        topicNorm: normTopic,
      );
    }

    return null;
  }

  static SubjectLabConfig _buildConfig({
    required String code,
    required String name,
    required int cuatrimestre,
    required List<LabSimulatorDescriptor> sims,
    required String topicNorm,
  }) {
    LabSimulatorDescriptor selected = sims.first;
    int bestScore = 0;

    for (final sim in sims) {
      int score = 0;
      for (final kw in sim.keywords) {
        if (topicNorm.contains(kw)) {
          score += kw.length;
        }
      }
      if (score > bestScore) {
        bestScore = score;
        selected = sim;
      }
    }

    return SubjectLabConfig(
      subjectCode: code,
      subjectName: name,
      cuatrimestre: cuatrimestre,
      simulators: sims,
      initialSimulator: selected,
    );
  }

  // ===========================================================================
  // CATÁLOGO POR ASIGNATURA (CUATRIMESTRES 1 AL 4)
  // ===========================================================================

  static const List<LabSimulatorDescriptor> _calculoDiferencialSims = [
    LabSimulatorDescriptor(
      id: LabSimId.calcDerivadaTangente,
      shortTitle: 'Derivada y Tangente',
      fullTitle: 'Derivada y Recta Tangente en Movimiento',
      formulaBadge: "m = f'(x₀) = dy/dx",
      icon: Icons.timeline_rounded,
      keywords: [
        'derivada',
        'tangente',
        'pendiente',
        'razon de cambio',
        'optimizacion',
        'maximo',
        'minimo',
        'regla de la cadena',
        'diferencial',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.calcLimites,
      shortTitle: 'Límites x → a±',
      fullTitle: 'Aproximación Lateral de Límites y Continuidad',
      formulaBadge: 'lim_{x→a⁻} f(x) = lim_{x→a⁺} f(x)',
      icon: Icons.compare_arrows_rounded,
      keywords: [
        'limite',
        'continuidad',
        'asintota',
        'discontinuidad',
        'lateral',
        'indeterminacion',
        'funcion',
        'dominio',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _algebraLinealSims = [
    LabSimulatorDescriptor(
      id: LabSimId.algebraTransformaciones2D,
      shortTitle: 'Transformaciones 2D',
      fullTitle: 'Transformaciones Lineales 2D, Determinante y Autovectores',
      formulaBadge: 'det(A) = a·d − b·c | A·v = λ·v',
      icon: Icons.grid_4x4_rounded,
      keywords: [
        'matriz',
        'matrices',
        'transformacion',
        'determinante',
        'vector',
        'autovalor',
        'autovector',
        'base',
        'espacio',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _programacionIaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.progOrdenamiento,
      shortTitle: 'Ordenamiento en Vivo',
      fullTitle: 'Algoritmos de Ordenamiento (Bubble / QuickSort) Animados',
      formulaBadge: 'O(n log n) vs O(n²)',
      icon: Icons.bar_chart_rounded,
      keywords: [
        'algoritmo',
        'ordenamiento',
        'arreglo',
        'ciclo',
        'bucle',
        'estructura',
        'funcion',
        'python',
        'complejidad',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.progRegresionLineal,
      shortTitle: 'Regresión Lineal IA',
      fullTitle: 'Descenso de Gradiente y Regresión Lineal Interactiva',
      formulaBadge: 'ŷ = m·x + b | ∇MSE',
      icon: Icons.scatter_plot_rounded,
      keywords: [
        'ia',
        'inteligencia artificial',
        'regresion',
        'gradiente',
        'machine learning',
        'datos',
        'modelo',
        'prediccion',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _introEnergiaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.introFlujoEnergetico,
      shortTitle: 'Flujo Energético η',
      fullTitle: 'Diagrama Dinámico de Flujo Energético y Eficiencia Global',
      formulaBadge: 'η = P_útil / P_entrada',
      icon: Icons.bolt_rounded,
      keywords: [
        'energia',
        'eficiencia',
        'solar',
        'hidrica',
        'termica',
        'generacion',
        'perdidas',
        'matriz',
        'renovable',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _fisicaMecanicaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.fisicaMasaResorte,
      shortTitle: 'Masa-Resorte y Energía',
      fullTitle: 'Sistema Masa-Resorte y Conservación de la Energía',
      formulaBadge: 'E_m = ½mv² + ½kx² + E_dis',
      icon: Icons.compress_rounded,
      keywords: [
        'resorte',
        'conservativa',
        'energia',
        'trabajo',
        'hooke',
        'potencial',
        'cinetica',
        'oscila',
        'catedra 7',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.fisicaTiroParabolico,
      shortTitle: 'Tiro Parabólico',
      fullTitle: 'Movimiento Parabólico de Proyectiles y Componentes Vectoriales',
      formulaBadge: 'x(t) = v₀cosθ·t | y(t) = v₀sinθ·t − ½gt²',
      icon: Icons.airplanemode_active_rounded,
      keywords: [
        'parabolico',
        'proyectil',
        'cinematica',
        'velocidad',
        'alcance',
        'caida libre',
        'trayectoria',
        'bidimensional',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.fisicaPlanoInclinadoDcl,
      shortTitle: 'Plano Inclinado y DCL',
      fullTitle: 'Dinámica en Plano Inclinado y Diagrama de Cuerpo Libre',
      formulaBadge: 'ΣF_x = mg·sinθ − μ_k·N = m·a',
      icon: Icons.architecture_rounded,
      keywords: [
        'plano inclinado',
        'dcl',
        'cuerpo libre',
        'newton',
        'fuerza',
        'normal',
        'friccion',
        'rozamiento',
        'dinamica',
        'rampa',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.fisicaColisiones1D,
      shortTitle: 'Colisiones 1D',
      fullTitle: 'Colisiones Elásticas e Inelásticas 1D y Momento Lineal',
      formulaBadge: 'm₁v₁ + m₂v₂ = m₁v₁′ + m₂v₂′',
      icon: Icons.compare_arrows_rounded,
      keywords: [
        'colision',
        'choque',
        'momento',
        'impulso',
        'cantidad de movimiento',
        'elastico',
        'inelastico',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _calculoIntegralSims = [
    LabSimulatorDescriptor(
      id: LabSimId.integralRiemann,
      shortTitle: 'Sumas de Riemann',
      fullTitle: 'Sumas de Riemann y Barrido de Área Acumulada',
      formulaBadge: '∫_a^b f(x)dx ≈ Σ f(x_i)·Δx',
      icon: Icons.area_chart_rounded,
      keywords: [
        'riemann',
        'area',
        'definida',
        'antiderivada',
        'fundamental',
        'acumulada',
        'integral',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.integralSolidoRevolucion,
      shortTitle: 'Sólido de Revolución 3D',
      fullTitle: 'Sólido de Revolución 3D (Método de Discos y Arandelas)',
      formulaBadge: 'V = π ∫_a^b [f(x)]² dx',
      icon: Icons.view_in_ar_rounded,
      keywords: [
        'solido',
        'revolucion',
        'volumen',
        'disco',
        'arandela',
        'casquete',
        '3d',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _quimicaAplicadaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.quimicaGasesIdeales,
      shortTitle: 'Cámara Cinética PV=nRT',
      fullTitle: 'Teoría Cinético-Molecular de Gases Ideales (PV = nRT)',
      formulaBadge: 'P·V = n·R·T | v_rms = √(3RT/M)',
      icon: Icons.bubble_chart_rounded,
      keywords: [
        'gas',
        'gases',
        'presion',
        'volumen',
        'temperatura',
        'cinetica',
        'mol',
        'termoquimica',
        'reaccion',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _electricidad1Sims = [
    LabSimulatorDescriptor(
      id: LabSimId.elec1CircuitoDc,
      shortTitle: 'Circuito DC y Corriente',
      fullTitle: 'Circuito DC Serie/Paralelo y Flujo de Portadores de Carga',
      formulaBadge: 'I = V / R_eq | P = V·I',
      icon: Icons.electrical_services_rounded,
      keywords: [
        'ohm',
        'kirchhoff',
        'resistencia',
        'serie',
        'paralelo',
        'corriente',
        'continua',
        'dc',
        'voltaje',
        'potencia',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _calorYOndasSims = [
    LabSimulatorDescriptor(
      id: LabSimId.ondasViajerasArmonicos,
      shortTitle: 'Ondas y Armónicos',
      fullTitle: 'Ondas Viajeras y Modos Estacionarios en Cuerda Vibrante',
      formulaBadge: 'y(x,t) = A·sin(kx − ωt) | f_n = n·v/(2L)',
      icon: Icons.waves_rounded,
      keywords: [
        'onda',
        'armonic',
        'estacionaria',
        'nodo',
        'antinodo',
        'frecuencia',
        'sonido',
        'cuerda',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.ondasPenduloFase,
      shortTitle: 'Péndulo y Espacio de Fase',
      fullTitle: 'Movimiento Armónico Simple de Péndulo y Retrato de Fase',
      formulaBadge: 'θ(t) = θ₀·cos(ω₀t) | ω₀ = √(g/L)',
      icon: Icons.motion_photos_on_rounded,
      keywords: [
        'pendulo',
        'oscilacion',
        'mas',
        'armonico simple',
        'fase',
        'periodo',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _modelacionMatematicaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.modelacionOsciladorAmortiguado,
      shortTitle: 'EDO Oscilador y Pendientes',
      fullTitle: 'Oscilador Amortiguado de 2° Orden y Campo de Pendientes',
      formulaBadge: 'm·x″ + c·x′ + k·x = 0 | ζ = c/(2√(mk))',
      icon: Icons.functions_rounded,
      keywords: [
        'ecuacion diferencial',
        'amortiguado',
        'subamortiguado',
        'sobreamortiguado',
        'critico',
        'laplace',
        'pendiente',
        'edo',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _electricidad2Sims = [
    LabSimulatorDescriptor(
      id: LabSimId.elec2FasoresCa,
      shortTitle: 'Fasores Rotatorios CA',
      fullTitle: 'Diagrama Fasorial en Giro Continuo y Ondas v(t), i(t), p(t)',
      formulaBadge: 'v(t) = V_m·sin(ωt) | FP = cos(φ)',
      icon: Icons.track_changes_rounded,
      keywords: [
        'fasor',
        'alterna',
        'impedancia',
        'factor de potencia',
        'ac',
        'ca',
        'senoidal',
        'reactancia',
        'trifasic',
      ],
    ),
    LabSimulatorDescriptor(
      id: LabSimId.elec2TransitorioRcRl,
      shortTitle: 'Transitorio RC / RL',
      fullTitle: 'Respuesta Transitoria de Carga y Descarga RC / RL',
      formulaBadge: 'v_C(t) = V_f + (V_0 − V_f)·e^(−t/τ)',
      icon: Icons.trending_up_rounded,
      keywords: [
        'transitorio',
        'capacitor',
        'inductor',
        'constante de tiempo',
        'carga',
        'descarga',
        'rc',
        'rl',
        'rlc',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _diseno3DSims = [
    LabSimulatorDescriptor(
      id: LabSimId.disenoProyeccion3D,
      shortTitle: 'Proyección Isométrica 3D',
      fullTitle: 'Modelado CAD 3D en Rotación y Vistas Ortogonales (Alzado/Planta/Perfil)',
      formulaBadge: 'R_z(γ)·R_y(β)·R_x(α)',
      icon: Icons.view_in_ar_rounded,
      keywords: [
        'isometric',
        'ortogonal',
        'cad',
        'vista',
        'alzado',
        'planta',
        'perfil',
        '3d',
        'pieza',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _electricidadMagnetismoSims = [
    LabSimulatorDescriptor(
      id: LabSimId.emLeyFaraday,
      shortTitle: 'Ley de Faraday y Flujo',
      fullTitle: 'Inducción Electromagnética de Faraday-Lenz y Galvanómetro en Vivo',
      formulaBadge: 'ε = −N · dΦ_B / dt',
      icon: Icons.compass_calibration_rounded,
      keywords: [
        'faraday',
        'lenz',
        'induccion',
        'flujo magnetico',
        'bobina',
        'iman',
        'campo magnetico',
        'fem',
        'maxwell',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _termodinamicaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.termoCicloPvPiston,
      shortTitle: 'Ciclo P-V y Pistón',
      fullTitle: 'Ciclo Termodinámico P-V Sincronizado con Cilindro-Pistón',
      formulaBadge: 'W_neto = ∮ P dV | η = 1 − T_L/T_H',
      icon: Icons.local_fire_department_rounded,
      keywords: [
        'carnot',
        'otto',
        'ciclo',
        'piston',
        'entropia',
        'entalpia',
        'primera ley',
        'segunda ley',
        'trabajo',
        'calor',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _probabilidadEstadisticaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.probTableroGalton,
      shortTitle: 'Tablero de Galton y TLC',
      fullTitle: 'Tablero de Galton en Cascada y Convergencia Gaussiana N(μ, σ²)',
      formulaBadge: 'Z = (X̄ − μ)/(σ/√n) → N(0,1)',
      icon: Icons.equalizer_rounded,
      keywords: [
        'galton',
        'normal',
        'gauss',
        'limite central',
        'histograma',
        'distribucion',
        'probabilidad',
        'varianza',
      ],
    ),
  ];

  static const List<LabSimulatorDescriptor> _hidraulicaNeumaticaSims = [
    LabSimulatorDescriptor(
      id: LabSimId.hidraulicaVenturiBernoulli,
      shortTitle: 'Tubo Venturi y Bernoulli',
      fullTitle: 'Efecto Venturi, Conservación de Caudal y Ecuación de Bernoulli',
      formulaBadge: 'P₁ + ½ρv₁² = P₂ + ½ρv₂² | Q = A·v',
      icon: Icons.water_rounded,
      keywords: [
        'venturi',
        'bernoulli',
        'caudal',
        'continuidad',
        'presion',
        'tuberia',
        'fluido',
        'hidraulica',
        'neumatica',
      ],
    ),
  ];
}
