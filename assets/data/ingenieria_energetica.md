---
database_name: "ingenieria_energetica"
schema_version: "2.0.0"
app_target: "UM_STUDIO_IOS_DARK"
programa:
  codigo_interno: "8108"
  codigo_snies: "118222"
  nombre: "Ingeniería Energética"
  facultad: "Facultad de Ingeniería"
  universidad: "Universidad del Magdalena"
  modalidad: "Presencial"
  nivel: "Profesional"
  total_cuatrimestres: 12
  total_asignaturas: 56
  total_creditos: 162
  normatividad: "Acuerdo Académico N° 038 de 2024"
design_tokens:
  background_oled: "#000000"
  card_surface: "#121316"
  card_border: "#1F2228"
  categories:
    MATEMATICAS: "#5E5CE6"
    FISICA_QUIMICA: "#30D158"
    INGENIERIA_ENERGIA: "#FF9F0A"
    PROGRAMACION_IA: "#0A84FF"
    PROYECTOS_GESTION: "#BF5AF2"
    FORMACION_GENERAL: "#8E8E93"
malla_curricular:
  - cuatrimestre: 1
    creditos_totales: 14
    asignaturas:
      - codigo: "02011807"
        nombre: "Cálculo Diferencial"
        creditos: 4
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Límites y Continuidad de Funciones Reales"
            objetivo: "Analizar el comportamiento asintótico y la continuidad de funciones aplicadas a modelos físicos."
            concepto_clave_latex: "\\lim_{x \\to a} f(x) = L \\iff \\forall \\varepsilon > 0, \\exists \\delta > 0 : 0 < |x - a| < \\delta \\implies |f(x) - L| < \\varepsilon"
            ejemplo: "Determinación de la continuidad en la curva de potencia de arranque de un generador."
            bloque_estudio: "Pomodoro 50/10 • 5 ejercicios de límites indeterminados"
          - numero: 2
            titulo: "Derivada, Regla de la Cadena y Optimización"
            objetivo: "Determinar razones de cambio instantáneas y puntos críticos de máxima eficiencia."
            concepto_clave_latex: "\\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x) \\quad ; \\quad f'(x_c) = 0"
            ejemplo: "Cálculo del ángulo de inclinación óptimo para maximizar la radiación captada por un colector solar."
            bloque_estudio: "Práctica Activa 45 min • Problemas de optimización"
      - codigo: "03011813"
        nombre: "Fundamentos de Programación e IA"
        creditos: 4
        obligatoria: true
        categoria: "PROGRAMACION_IA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Algoritmia, Complejidad y Estructuras de Control"
            objetivo: "Diseñar algoritmos eficientes para el procesamiento de datos energéticos y series temporales."
            concepto_clave_latex: "T(n) = \\mathcal{O}(n \\log n) \\quad ; \\quad \\bar{x} = \\frac{1}{N}\\sum_{i=1}^{N} x_i"
            ejemplo: "Script en Python para limpiar y promediar lecturas horarias de irradiancia solar."
            bloque_estudio: "Pomodoro 50/10 • Estructuras iterativas y funciones"
          - numero: 2
            titulo: "Introducción a Regresión y Modelos Predictivos"
            objetivo: "Ajustar modelos lineales básicos para estimar demanda energética."
            concepto_clave_latex: "\\hat{y} = w_1 x + w_0 \\quad ; \\quad \\text{MSE} = \\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2"
            ejemplo: "Predicción del consumo eléctrico diario en función de la temperatura ambiente."
            bloque_estudio: "Práctica 40 min • Minimización del error cuadrático medio"
      - codigo: "01021802"
        nombre: "General English I"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Technical Vocabulary & Present Structures"
            objetivo: "Comprender fichas técnicas de equipos energéticos y magnitudes del Sistema Internacional en inglés."
            concepto_clave_latex: "P_{\\text{rated}} = V_{\\text{nom}} \\cdot I_{\\text{nom}}"
            ejemplo: "Lectura e interpretación de un datasheet de módulos fotovoltaicos en inglés técnico."
            bloque_estudio: "Bloque 25 min • Flashcards de terminología técnica"
      - codigo: "04011822"
        nombre: "Introducción a la Ingeniería Energética"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Matriz Energética, Unidades y Rendimiento Global"
            objetivo: "Comprender las cadenas de conversión de energía primaria a energía útil y su eficiencia."
            concepto_clave_latex: "\\eta_{\\text{global}} = \\frac{E_{\\text{útil}}}{E_{\\text{primaria}}} = \\prod_{i=1}^{n} \\eta_i"
            ejemplo: "Cálculo de la eficiencia combinada de una central térmica considerando caldera, turbina y generador."
            bloque_estudio: "Pomodoro 50/10 • Conversión de unidades (J, kWh, BTU, TEP)"
      - codigo: "01011801"
        nombre: "Procesos Lectores, Escriturales y Orales"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Estructura de Informes Técnicos y Artículos Científicos"
            objetivo: "Redactar documentos de ingeniería con precisión argumentativa, citación IEEE y síntesis."
            concepto_clave_latex: "\\text{Índice de Legibilidad} = 206.835 - 1.015\\left(\\frac{\\text{Palabras}}{\\text{Oraciones}}\\right)"
            ejemplo: "Estructuración del resumen ejecutivo (Abstract) de un proyecto de transición energética."
            bloque_estudio: "Bloque 30 min • Redacción y síntesis conceptual"

  - cuatrimestre: 2
    creditos_totales: 14
    asignaturas:
      - codigo: "02021810"
        nombre: "Física Mecánica"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Leyes de Newton y Dinámica con Rozamiento"
            objetivo: "Entender la segunda ley de Newton y su relación con las fuerzas de fricción estática y cinética."
            concepto_clave_latex: "\\sum \\vec{F} = m \\cdot \\vec{a} \\quad ; \\quad f_k = \\mu_k \\cdot N"
            ejemplo: "Un bloque sobre un plano inclinado experimenta una fuerza de rozamiento opuesta al deslizamiento proporcional a la normal."
            bloque_estudio: "Pomodoro 50/10 • Diagramas de Cuerpo Libre"
          - numero: 2
            titulo: "Trabajo, Energía Mecánica y Potencia"
            objetivo: "Aplicar el teorema del trabajo y la conservación de la energía en sistemas mecánicos."
            concepto_clave_latex: "W = \\int_{r_1}^{r_2} \\vec{F} \\cdot d\\vec{r} = \\Delta K \\quad ; \\quad P = \\vec{F} \\cdot \\vec{v}"
            ejemplo: "Cálculo de la potencia mecánica entregada por un eje rotatorio bajo par constante."
            bloque_estudio: "Práctica Activa 45 min • Conservación de energía"
      - codigo: "03041819"
        nombre: "Fundamentos de la Electricidad I"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Leyes de Ohm, Kirchhoff y Análisis de Nodos/Mallas"
            objetivo: "Resolver circuitos resistivos en corriente continua mediante conservación de carga y energía."
            concepto_clave_latex: "V = I \\cdot R \\quad ; \\quad \\sum_{k=1}^{n} I_k = 0 \\quad ; \\quad \\sum_{m=1}^{p} V_m = 0"
            ejemplo: "Determinación de corrientes de rama y potencia disipada en resistencias de carga."
            bloque_estudio: "Pomodoro 50/10 • Sistemas de ecuaciones de nodos"
          - numero: 2
            titulo: "Teoremas de Thévenin, Norton y Máxima Potencia"
            objetivo: "Simplificar redes lineales activas entre dos terminales a un circuito equivalente."
            concepto_clave_latex: "V_{th} = V_{oc} \\quad ; \\quad R_{th} = \\frac{V_{oc}}{I_{sc}} \\quad ; \\quad P_{\\max} = \\frac{V_{th}^2}{4 R_{th}}"
            ejemplo: "Acoplamiento de impedancia resistiva para extraer la máxima potencia de una celda solar."
            bloque_estudio: "Práctica 45 min • Reducción de Thévenin"
      - codigo: "01021803"
        nombre: "General English II"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Comparative Analysis & Process Descriptions"
            objetivo: "Describir procesos secuenciales y comparar tecnologías energéticas en inglés."
            concepto_clave_latex: "\\Delta \\eta = \\eta_{\\text{new}} - \\eta_{\\text{baseline}}"
            ejemplo: "Comparación escrita entre eficiencia de turbinas Pelton y Francis."
            bloque_estudio: "Bloque 25 min • Redacción de diagramas de flujo en inglés"
      - codigo: "03031818"
        nombre: "Probabilidad y Estadística"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Distribuciones de Probabilidad (Weibull y Normal)"
            objetivo: "Modelar la variabilidad estocástica de recursos renovables como la velocidad del viento."
            concepto_clave_latex: "f(v) = \\frac{k}{c}\\left(\\frac{v}{c}\\right)^{k-1} \\exp\\left[-\\left(\\frac{v}{c}\\right)^k\\right]"
            ejemplo: "Ajuste de la distribución de Weibull para estimar la frecuencia de vientos útiles en la Guajira."
            bloque_estudio: "Pomodoro 50/10 • Cálculo de factores de forma y escala"
      - codigo: "02031812"
        nombre: "Química Aplicada"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Termoquímica, Combustión y Electroquímica"
            objetivo: "Calcular entalpías de reacción, poder calorífico y potenciales de celda."
            concepto_clave_latex: "\\Delta H^\\circ_{\\text{rxn}} = \\sum \\nu_p \\Delta H^\\circ_{f,p} - \\sum \\nu_r \\Delta H^\\circ_{f,r} \\quad ; \\quad E_{\\text{celda}} = E^\\circ - \\frac{RT}{nF}\\ln Q"
            ejemplo: "Cálculo del poder calorífico inferior (PCI) del gas natural y voltaje en una celda galvánica."
            bloque_estudio: "Pomodoro 50/10 • Balance estequiométrico de combustión"

  - cuatrimestre: 3
    creditos_totales: 15
    asignaturas:
      - codigo: "02011808"
        nombre: "Cálculo Integral"
        creditos: 4
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Técnicas de Integración e Integral Definida"
            objetivo: "Resolver integrales por partes, sustitución trigonométrica y fracciones parciales para acumular magnitudes."
            concepto_clave_latex: "\\int u \\, dv = u \\cdot v - \\int v \\, du \\quad ; \\quad E = \\int_{t_1}^{t_2} P(t) \\, dt"
            ejemplo: "Integración de la curva de demanda de potencia diaria para obtener la energía consumida en MWh."
            bloque_estudio: "Pomodoro 50/10 • 4 integrales por partes y definidas"
      - codigo: "02021811"
        nombre: "Calor y Ondas"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Calorimetría, Dilatación Térmica y Movimiento Ondulatorio"
            objetivo: "Analizar el intercambio de calor sensible/latente y la propagación de ondas mecánicas y electromagnéticas."
            concepto_clave_latex: "Q = m c \\Delta T + m L_f \\quad ; \\quad \\frac{\\partial^2 y}{\\partial x^2} = \\frac{1}{v^2}\\frac{\\partial^2 y}{\\partial t^2}"
            ejemplo: "Cálculo del equilibrio térmico en un tanque de almacenamiento de agua caliente y longitud de onda del espectro solar."
            bloque_estudio: "Pomodoro 50/10 • Balances calorimétricos"
      - codigo: "03041820"
        nombre: "Fundamentos de Electricidad II"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Circuitos en Corriente Alterna (AC), Fasores y Potencia Compleja"
            objetivo: "Analizar redes en estado estacionario sinusoidal, triángulo de potencias y corrección del factor de potencia."
            concepto_clave_latex: "\\mathbf{S} = P + jQ = \\mathbf{V}_{\\text{rms}} \\mathbf{I}_{\\text{rms}}^* \\quad ; \\quad \\text{FP} = \\cos(\\theta_v - \\theta_i)"
            ejemplo: "Dimensionamiento de un banco de capacitores para elevar el factor de potencia de 0.82 a 0.96 inductivo."
            bloque_estudio: "Práctica Activa 45 min • Triángulo de potencias y fasores"
      - codigo: "03021815"
        nombre: "Fundamentos de Hidráulica y Neumática"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Principio de Pascal, Actuadores y Potencia Fluida"
            objetivo: "Calcular presiones, caudales y fuerzas en circuitos óleo-hidráulicos y neumáticos."
            concepto_clave_latex: "P = \\frac{F}{A} \\quad ; \\quad N_{\\text{hid}} = \\Delta P \\cdot Q"
            ejemplo: "Cálculo de la fuerza ejercida por el cilindro hidráulico del sistema de pitch en un aerogenerador."
            bloque_estudio: "Pomodoro 50/10 • Diseño de circuitos hidráulicos"
      - codigo: "01021804"
        nombre: "General English III"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Passive Voice in Technical Manuals & Reports"
            objetivo: "Redactar procedimientos de laboratorio y protocolos de mantenimiento usando voz pasiva en inglés."
            concepto_clave_latex: "\\text{Efficiency}(\\%) = \\left(\\frac{P_{\\text{out}}}{P_{\\text{in}}}\\right) \\times 100"
            ejemplo: "Interpretación de manuales de operación de inversores solares en inglés."
            bloque_estudio: "Bloque 25 min • Traducción de protocolos de prueba"

  - cuatrimestre: 4
    creditos_totales: 15
    asignaturas:
      - codigo: "02011809"
        nombre: "Álgebra Lineal"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Sistemas Matriciales, Transformaciones y Valores Propios"
            objetivo: "Resolver sistemas de ecuaciones lineales de gran escala y calcular autovalores de estabilidad."
            concepto_clave_latex: "A\\vec{x} = \\vec{b} \\quad ; \\quad \\det(A - \\lambda I) = 0"
            ejemplo: "Formulación de la matriz de admitancia nodal en una red eléctrica de 4 nodos."
            bloque_estudio: "Pomodoro 50/10 • Eliminación Gaussiana y autovalores"
      - codigo: "06011837"
        nombre: "Conversión de Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Principios Electromecánicos y Termoeléctricos de Conversión"
            objetivo: "Modelar el acoplamiento entre energía térmica, mecánica, química y eléctrica."
            concepto_clave_latex: "dW_{\\text{mec}} = dW_{\\text{campo}} + dW_{\\text{eléc}} \\quad ; \\quad \\tau = \\frac{\\partial W'(\\theta, i)}{\\partial \\theta}"
            ejemplo: "Cálculo del par electromagnético desarrollado en un transductor rotativo."
            bloque_estudio: "Pomodoro 50/10 • Balance de coenergía magnética"
      - codigo: "03041821"
        nombre: "Electricidad y Magnetismo"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Ecuaciones de Maxwell, Ley de Gauss y Ley de Faraday"
            objetivo: "Analizar campos electrostáticos, magnetostáticos y la inducción electromagnética."
            concepto_clave_latex: "\\oint_S \\vec{E} \\cdot d\\vec{A} = \\frac{q_{\\text{enc}}}{\\varepsilon_0} \\quad ; \\quad \\mathcal{E} = -N\\frac{d\\Phi_B}{dt}"
            ejemplo: "Cálculo de la fuerza electromotriz inducida en una espira que rota dentro de un campo magnético uniforme."
            bloque_estudio: "Pomodoro 50/10 • Integrales de flujo eléctrico y magnético"
      - codigo: "01021805"
        nombre: "General English IV"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Academic Presentations & Abstract Writing"
            objetivo: "Exponer resultados de proyectos de ingeniería mediante vocabulario académico formal."
            concepto_clave_latex: "\\text{ROI} = \\frac{\\text{Net Benefit}}{\\text{Total Cost}} \\times 100"
            ejemplo: "Presentación oral de 5 minutos sobre viabilidad de una micro-red solar."
            bloque_estudio: "Bloque 30 min • Práctica de pronunciación y estructura de pitch"
      - codigo: "03021817"
        nombre: "Termodinámica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Primera y Segunda Ley de la Termodinámica y Ciclos de Potencia"
            objetivo: "Evaluar balances de energía y entropía en volúmenes de control (turbinas, compresores, ciclos Rankine y Brayton)."
            concepto_clave_latex: "\\dot{Q}_{vc} - \\dot{W}_{vc} = \\sum \\dot{m}_s\\left(h_s + \\frac{v_s^2}{2} + gz_s\\right) - \\sum \\dot{m}_e\\left(h_e + \\frac{v_e^2}{2} + gz_e\\right) \\quad ; \\quad \\eta_{\\text{Carnot}} = 1 - \\frac{T_L}{T_H}"
            ejemplo: "Determinación de la potencia neta y eficiencia térmica de un ciclo Rankine con sobrecalentamiento."
            bloque_estudio: "Pomodoro 50/10 • Tablas de vapor y diagramas T-s"

  - cuatrimestre: 5
    creditos_totales: 15
    asignaturas:
      - codigo: "06021845"
        nombre: "Energía Hidráulica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Potencia Hidráulica, Altura Neta y Turbinas (Pelton, Francis, Kaplan)"
            objetivo: "Dimensionar pequeñas centrales hidroeléctricas (PCH) a partir del caudal de diseño y salto neto."
            concepto_clave_latex: "P_{\\text{hid}} = \\eta_t \\eta_g \\rho g Q H_n \\quad ; \\quad H_n = H_b - h_f"
            ejemplo: "Selección de turbina y cálculo de potencia eléctrica para un salto neto de 85 m y caudal de 2.5 m³/s."
            bloque_estudio: "Pomodoro 50/10 • Curvas de duración de caudales y velocidad específica"
      - codigo: "06021846"
        nombre: "Energía Solar Fotovoltaica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: " Física de la Celda Solar, Curva I-V y Dimensionamiento FV"
            objetivo: "Modelar el comportamiento eléctrico de arreglos fotovoltaicos bajo condiciones reales de operación (NOCT)."
            concepto_clave_latex: "I = I_L - I_0\\left[\\exp\\left(\\frac{q(V + I R_s)}{n k_B T}\\right) - 1\\right] - \\frac{V + I R_s}{R_{sh}} \\quad ; \\quad \\text{FF} = \\frac{V_{mp} I_{mp}}{V_{oc} I_{sc}}"
            ejemplo: "Cálculo de la caída de tensión de circuito abierto por incremento de temperatura en paneles instalados en Santa Marta."
            bloque_estudio: "Pomodoro 50/10 • Dimensionamiento de strings e inversores"
      - codigo: "06011838"
        nombre: "Mediciones e Instrumentación"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Sensores, Propagación de Incertidumbre y Acondicionamiento de Señal"
            objetivo: "Caracterizar errores estáticos/dinámicos en instrumentos de medición eléctrica y térmica."
            concepto_clave_latex: "u_c(y) = \\sqrt{\\sum_{i=1}^{N}\\left(\\frac{\\partial f}{\\partial x_i}\\right)^2 u^2(x_i)}"
            ejemplo: "Cálculo de la incertidumbre combinada en la medición de potencia activa mediante transformadores de corriente y potencial."
            bloque_estudio: "Práctica 40 min • Puentes de Wheatstone y calibración RTD"
      - codigo: "04021825"
        nombre: "Modelación Matemática para Ingeniería"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Ecuaciones Diferenciales Ordinarias y Transformada de Laplace"
            objetivo: "Formular y resolver sistemas dinámicos de primer y segundo orden en el dominio del tiempo y la frecuencia."
            concepto_clave_latex: "a_2\\frac{d^2y}{dt^2} + a_1\\frac{dy}{dt} + a_0 y = f(t) \\quad ; \\quad \\mathcal{L}\\{f(t)\\} = \\int_0^\\infty e^{-st}f(t)\\,dt"
            ejemplo: "Modelado de la respuesta transitoria de temperatura en un reactor térmico."
            bloque_estudio: "Pomodoro 50/10 • Transformada inversa y funciones de transferencia"
      - codigo: "06011839"
        nombre: "Sistemas Energéticos"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Integración de Sistemas de Generación, Cogeneración y Exergía"
            objetivo: "Analizar sistemas integrados de calor y potencia (CHP) mediante rendimiento exergético."
            concepto_clave_latex: "\\psi = (h - h_0) - T_0(s - s_0) \\quad ; \\quad \\eta_{II} = \\frac{\\dot{W}_{\\text{neto}} + \\dot{E}_{\\text{calor}}}{\\dot{E}_{\\text{combustible}}}"
            ejemplo: "Evaluación de la destrucción de exergía en una planta de cogeneración industrial."
            bloque_estudio: "Pomodoro 50/10 • Balances exergéticos"

  - cuatrimestre: 6
    creditos_totales: 13
    asignaturas:
      - codigo: "01021806"
        nombre: "General English V"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Scientific Debate & International Energy Standards"
            objetivo: "Debatir regulaciones internacionales e informes del IPCC/IEA en inglés avanzado."
            concepto_clave_latex: "\\text{CI} = \\frac{\\text{gCO}_2\\text{eq}}{\\text{kWh}}"
            ejemplo: "Análisis crítico de reportes de la Agencia Internacional de Energía (IEA)."
            bloque_estudio: "Bloque 30 min • Lectura crítica de papers IEEE"
      - codigo: "04021823"
        nombre: "Ingeniería del Diseño y Modelado en 3D"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Modelado Paramétrico CAD y Análisis Geométrico de Componentes"
            objetivo: "Diseñar piezas mecánicas, soportes solares y rotores cumpliendo tolerancias geométricas."
            concepto_clave_latex: "I_x = \\int_A y^2 \\, dA \\quad ; \\quad \\sigma_{\\max} = \\frac{M \\cdot c}{I}"
            ejemplo: "Modelado 3D y verificación de esfuerzos de flexión en una estructura soporte para paneles solares ante cargas de viento."
            bloque_estudio: "Práctica CAD 50 min • Ensamblaje y planos técnicos"
      - codigo: "04031827"
        nombre: "Legislación y Regulación Energética"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Marco Regulatorio (Ley 1715, CREG) e Incentivos Tributarios"
            objetivo: "Aplicar la regulación vigente de autogeneración a pequeña y gran escala (AGPE/AGGE) y beneficios fiscales."
            concepto_clave_latex: "\\text{CU} = G + T + D + Cv + PR + R"
            ejemplo: "Cálculo del Costo Unitario (CU) de prestación del servicio eléctrico y liquidación de excedentes en la matriz CREG 174."
            bloque_estudio: "Pomodoro 50/10 • Liquidación de autogeneración y deducción de renta"
      - codigo: "06011840"
        nombre: "Máquinas Eléctricas"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Transformadores, Generadores Síncronos y Motores de Inducción"
            objetivo: "Modelar el circuito equivalente de máquinas rotativas y estáticas en régimen permanente."
            concepto_clave_latex: "n_s = \\frac{120 f}{P} \\quad ; \\quad s = \\frac{n_s - n_m}{n_s} \\quad ; \\quad E_A = K \\phi \\omega"
            ejemplo: "Determinación del deslizamiento, corriente de estator y par desarrollado por un motor de inducción trifásico."
            bloque_estudio: "Pomodoro 50/10 • Circuito equivalente referido al primario"
      - codigo: "05011834"
        nombre: "Proyecto Integrador CDIO I"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Concebir y Diseñar Soluciones Energéticas Básicas"
            objetivo: "Formular el diseño conceptual de un prototipo energético aplicando la metodología CDIO."
            concepto_clave_latex: "\\text{FOM} = \\sum_{i=1}^{m} w_i \\cdot S_i"
            ejemplo: "Matriz de decisión ponderada (Figure of Merit) para seleccionar la arquitectura de un cargador solar autónomo."
            bloque_estudio: "Bloque 45 min • Definición de requerimientos y alcance"

  - cuatrimestre: 7
    creditos_totales: 15
    asignaturas:
      - codigo: "06021850"
        nombre: "Energía de Biomasa"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Rutas Termoquímicas (Gasificación/Pirólisis) y Bioquímica (Biodigestión)"
            objetivo: "Cuantificar la producción de biogás y syngas a partir de residuos agroindustriales."
            concepto_clave_latex: "\\text{PCI}_{\\text{húmedo}} = \\text{PCI}_{\\text{seco}}(1 - w) - 2.443 \\cdot w"
            ejemplo: "Estimación del potencial energético de generación con raquis de palma de aceite y estiércol bovino en el Magdalena."
            bloque_estudio: "Pomodoro 50/10 • Cinética de digestión anaerobia y relación C/N"
      - codigo: "06021848"
        nombre: "Energía Eólica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Aerodinámica de Turbinas, Límite de Betz y Perfil de Cortante"
            objetivo: "Calcular la potencia extraíble del viento y la extrapolación vertical de velocidad."
            concepto_clave_latex: "P_{\\text{viento}} = \\frac{1}{2} \\rho A v^3 C_p(\\lambda, \\beta) \\quad ; \\quad C_{p,\\max} = \\frac{16}{27} \\approx 0.5926 \\quad ; \\quad v(z) = v_{\\text{ref}}\\left(\\frac{z}{z_{\\text{ref}}}\\right)^\\alpha"
            ejemplo: "Cálculo de la producción anual de energía (AEP) de un aerogenerador de 80 m de altura de buje."
            bloque_estudio: "Pomodoro 50/10 • Ley exponencial de Hellmann y curva de potencia"
      - codigo: "06021847"
        nombre: "Energía Geotérmica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Gradiente Geotérmico, Ciclos Binarios ORC y Bombas de Calor"
            objetivo: "Evaluar yacimientos geotérmicos de baja, media y alta entalpía y ciclos orgánicos de Rankine."
            concepto_clave_latex: "q_{\\text{geo}} = -k_{\\text{roca}} \\frac{dT}{dz} \\quad ; \\quad \\text{COP}_{\\text{BC}} = \\frac{Q_H}{W_{\\text{comp}}}"
            ejemplo: "Diseño termodinámico de una planta binaria con fluido orgánico R245fa para una fuente hidrotermal a 140 °C."
            bloque_estudio: "Pomodoro 50/10 • Evaluación de reservas volumétricas"
      - codigo: "06021849"
        nombre: "Energía Mareomotriz"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Energía de las Mareas, Corrientes Marinas y Undimotriz (Olas)"
            objetivo: "Cuantificar la densidad de potencia de frentes de ola y embalses mareomotrices."
            concepto_clave_latex: "P_{\\text{ola}} = \\frac{\\rho g^2}{64\\pi} H_{m0}^2 T_e \\quad ; \\quad E_{\\text{marea}} = \\frac{1}{2} \\rho g A R^2"
            ejemplo: "Cálculo de la potencia por metro de frente de ola en el litoral Caribe a partir de la altura significativa y periodo energético."
            bloque_estudio: "Pomodoro 50/10 • Hidrodinámica costera y convertidores WEC"
      - codigo: "03021816"
        nombre: "Mecánica de Fluidos"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Ecuación de Bernoulli, Número de Reynolds y Pérdidas en Tuberías"
            objetivo: "Analizar el flujo interno y externo de fluidos viscosos incompresibles aplicando Darcy-Weisbach."
            concepto_clave_latex: "\\frac{P_1}{\\gamma} + \\frac{v_1^2}{2g} + z_1 + h_B = \\frac{P_2}{\\gamma} + \\frac{v_2^2}{2g} + z_2 + h_T + f\\frac{L}{D}\\frac{v^2}{2g}"
            ejemplo: "Cálculo de la caída de presión y potencia de bombeo en una tubería forzada mediante el diagrama de Moody."
            bloque_estudio: "Pomodoro 50/10 • Ecuación de energía y pérdidas por fricción"

  - cuatrimestre: 8
    creditos_totales: 14
    asignaturas:
      - codigo: "04021824"
        nombre: "Diseño y Simulación de Sistemas Energéticos"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Optimización de Micro-redes Híbridas y Costo Nivelado (LCOE)"
            objetivo: "Simular y dimensionar sistemas híbridos (Solar + Eólico + Baterías + Respaldo) minimizando el costo del ciclo de vida."
            concepto_clave_latex: "\\text{LCOE} = \\frac{\\sum_{t=1}^{n} \\frac{I_t + M_t + F_t}{(1 + r)^t}}{\\sum_{t=1}^{n} \\frac{E_t}{(1 + r)^t}} \\quad ; \\quad \\text{LPSP} = \\frac{\\sum \\text{LPS}(t)}{\\sum E_{\\text{demanda}}(t)}"
            ejemplo: "Optimización tecno-económica de una micro-red aislada asegurando una probabilidad de pérdida de carga menor al 1%."
            bloque_estudio: "Práctica de Simulación 50 min • Análisis de sensibilidad LCOE"
      - codigo: "04031828"
        nombre: "Energy Market"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Mercado Mayorista de Energía, Despacho Económico y Contratos PPA"
            objetivo: "Comprender la formación del precio de bolsa (Marginal Clearing Price) y subastas de energías renovables."
            concepto_clave_latex: "\\min \\sum_{i=1}^{N} C_i(P_{G,i}) \\quad \\text{s.a.} \\quad \\sum_{i=1}^{N} P_{G,i} = P_D + P_L"
            ejemplo: "Determinación del precio marginal del sistema a partir de la intersección de las curvas de oferta de generadores y demanda inelástica."
            bloque_estudio: "Pomodoro 50/10 • Liquidación de contratos bilaterales PPA"
      - codigo: "05011832"
        nombre: "Formulación de Proyectos"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Estudio de Mercado, Técnico y Estructura de Desglose de Trabajo (EDT)"
            objetivo: "Estructurar proyectos de ingeniería bajo metodologías de Marco Lógico y PMBOK."
            concepto_clave_latex: "t_e = \\frac{t_o + 4t_m + t_p}{6} \\quad ; \\quad \\sigma^2 = \\left(\\frac{t_p - t_o}{6}\\right)^2"
            ejemplo: "Cálculo de la ruta crítica (CPM/PERT) para el cronograma de construcción de una granja solar de 5 MW."
            bloque_estudio: "Bloque 45 min • Matriz de marco lógico y ruta crítica"
      - codigo: "05011831"
        nombre: "Metodología de la Investigación"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Diseño Experimental, Hipótesis yTamaño de Muestra"
            objetivo: "Plantear problemas de investigación científica con rigor estadístico y validación experimental."
            concepto_clave_latex: "n = \\frac{Z_{\\alpha/2}^2 \\cdot p \\cdot q}{e^2}"
            ejemplo: "Diseño de un experimento factorial para evaluar el efecto del polvo y la humedad sobre paneles bifaciales."
            bloque_estudio: "Bloque 40 min • Formulación de pregunta de investigación y objetivos"
      - codigo: "03011814"
        nombre: "Programación Avanzada y Aplicaciones de IA"
        creditos: 3
        obligatoria: true
        categoria: "PROGRAMACION_IA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Redes Neuronales, Pronóstico de Generación y Optimización Heurística"
            objetivo: "Entrenar modelos de Machine Learning para predecir generación solar/eólica y detección de fallas."
            concepto_clave_latex: "a^{(l)} = \\sigma\\left(W^{(l)} a^{(l-1)} + b^{(l)}\\right) \\quad ; \\quad \\theta_{t+1} = \\theta_t - \\eta \\nabla_\\theta \\mathcal{L}(\\theta_t)"
            ejemplo: "Red neuronal recurrente (LSTM) para el pronóstico de irradiancia solar con horizonte de 24 horas."
            bloque_estudio: "Pomodoro 50/10 • Descenso de gradiente y validación cruzada"

  - cuatrimestre: 9
    creditos_totales: 14
    asignaturas:
      - codigo: "04031829"
        nombre: "Comunidades Energéticas Sostenibles"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Generación Distribuida Colectiva y Reparto de Excedentes"
            objetivo: "Diseñar esquemas técnicos y socioeconómicos de comunidades energéticas bajo criterios de equidad."
            concepto_clave_latex: "E_{\\text{asignada},i}(t) = \\beta_i \\cdot E_{\\text{gen}}(t) \\quad ; \\quad \\sum_{i=1}^{N} \\beta_i = 1"
            ejemplo: "Cálculo de coeficientes de reparto dinámico en una comunidad energética rural en la Sierra Nevada."
            bloque_estudio: "Pomodoro 50/10 • Balance de autoconsumo colectivo"
      - codigo: "04031826"
        nombre: "Gestión, Auditoría y Eficiencia Energética"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Norma ISO 50001, Línea Base Energética e Indicadores EnPI"
            objetivo: "Realizar auditorías energéticas detalladas e identificar oportunidades de ahorro en climatización, motores e iluminación."
            concepto_clave_latex: "E_{\\text{base}} = m \\cdot P_{\\text{producción}} + E_0 \\quad ; \\quad \\text{CUSUM}_t = \\sum_{k=1}^{t} (E_{\\text{real},k} - E_{\\text{esperada},k})"
            ejemplo: "Construcción de la línea base energética y gráfico de sumas acumuladas (CUSUM) en una planta procesadora de alimentos."
            bloque_estudio: "Pomodoro 50/10 • Regresión de línea base y cálculo de ahorros"
      - codigo: "06011842"
        nombre: "Instalaciones Eléctricas con Energías Renovables"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Diseño RETIE, Protecciones DC/AC, Calibre de Conductores y Caída de Tensión"
            objetivo: "Dimensionar conductores, canalizaciones, protecciones termomagnéticas y puestas a tierra según el RETIE y NTC 2050."
            concepto_clave_latex: "\\Delta V(\\%) = \\frac{k \\cdot I \\cdot L \\cdot (R\\cos\\theta + X\\sin\\theta)}{V_{\\text{nom}}} \\times 100 \\le 3\\% \\quad ; \\quad I_{\\text{diseño}} = 1.25 \\cdot 1.25 \\cdot I_{sc}"
            ejemplo: "Selección de calibre AWG y fusibles gPV para un arreglo solar cumpliendo el límite de regulación de tensión del 3%."
            bloque_estudio: "Pomodoro 50/10 • Cálculo de cortocircuito y caída de tensión"
      - codigo: "05011835"
        nombre: "Proyecto Integrador CDIO II"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Implementar y Construir Prototipos Energéticos"
            objetivo: "Integrar hardware, instrumentación y control en un prototipo funcional validado en laboratorio."
            concepto_clave_latex: "e_{\\text{rel}} = \\left|\\frac{X_{\\text{exp}} - X_{\\text{sim}}}{X_{\\text{sim}}}\\right| \\times 100\\%"
            ejemplo: "Pruebas de desempeño en banco de un sistema de seguimiento solar de dos ejes comparado contra el modelo simulado."
            bloque_estudio: "Bloque 45 min • Protocolo de pruebas experimentales"
      - codigo: "06011841"
        nombre: "Transferencia de Calor"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Conducción (Fourier), Convección (Newton), Radiación y Diseño de Intercambiadores"
            objetivo: "Calcular flujos térmicos multimodales y dimensionar intercambiadores de calor mediante el método LMTD y efectividad-NTU."
            concepto_clave_latex: "q = U A \\Delta T_{\\text{lm}} \\quad ; \\quad \\Delta T_{\\text{lm}} = \\frac{\\Delta T_1 - \\Delta T_2}{\\ln(\\Delta T_1 / \\Delta T_2)} \\quad ; \\quad q_{\\text{rad}} = \\varepsilon \\sigma A (T_s^4 - T_{\\text{alr}}^4)"
            ejemplo: "Dimensionamiento del área de transferencia de un intercambiador de coraza y tubos para recuperación de calor residual."
            bloque_estudio: "Pomodoro 50/10 • Resistencias térmicas y método LMTD"

  - cuatrimestre: 10
    creditos_totales: 15
    asignaturas:
      - codigo: "06011843"
        nombre: "Almacenamiento de la Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Sistemas BESS (Litio-Ion), Estado de Carga (SoC), Bombeo y Almacenamiento Térmico"
            objetivo: "Dimensionar bancos de baterías y sistemas de almacenamiento evaluando profundidad de descarga (DoD) y degradación."
            concepto_clave_latex: "\\text{SoC}(t) = \\text{SoC}(t_0) - \\frac{\\eta_{\\text{coul}}}{C_{\\text{nom}}} \\int_{t_0}^{t} I(\\tau)\\,d\\tau \\quad ; \\quad C_{\\text{banco}} = \\frac{E_{\\text{autonomía}}}{V_{\\text{sist}} \\cdot \\text{DoD}_{\\max} \\cdot \\eta_{\\text{inv}}}"
            ejemplo: "Cálculo de la capacidad en MWh de un sistema BESS en tecnología LFP para respaldo de 4 horas con DoD del 85%."
            bloque_estudio: "Pomodoro 50/10 • Dimensionamiento BESS y curvas de ciclado"
      - codigo: "06021851"
        nombre: "Aprovechamiento de Fuentes Energéticas No Renovables"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Ciclos Combinados Gas-Vapor, Combustión Limpia y Captura de Carbono (CCUS)"
            objetivo: "Maximizar el rendimiento térmico de plantas convencionales y cuantificar la reducción de emisiones."
            concepto_clave_latex: "\\eta_{\\text{CC}} = \\eta_B + \\eta_R - \\eta_B \\eta_R"
            ejemplo: "Cálculo de la eficiencia global de una central de ciclo combinado (Turbina de Gas Brayton + Ciclo Rankine con HRSG)."
            bloque_estudio: "Pomodoro 50/10 • Balance térmico de calderas de recuperación HRSG"
      - codigo: "05011833"
        nombre: "Evaluación y Gestión de Proyectos"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Evaluación Financiera (VPN, TIR, WACC) y Análisis de Riesgo"
            objetivo: "Evaluar la viabilidad financiera de proyectos energéticos incorporando incentivos de la Ley 1715 y bonos de carbono."
            concepto_clave_latex: "\\text{VPN} = -I_0 + \\sum_{t=1}^{n} \\frac{\\text{FCL}_t}{(1 + \\text{WACC})^t} \\quad ; \\quad \\sum_{t=0}^{n} \\frac{\\text{FCL}_t}{(1 + \\text{TIR})^t} = 0"
            ejemplo: "Flujo de caja libre descontado a 20 años para un parque solar con depreciación acelerada."
            bloque_estudio: "Pomodoro 50/10 • Modelado financiero de VPN y TIR"
      - codigo: "06021852"
        nombre: "Hydrogen Energy"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Electrólisis del Agua (PEM/Alcalina), Almacenamiento y Celdas de Combustible"
            objetivo: "Calcular el consumo específico de electrolizadores para producción de hidrógeno verde y la curva de polarización de celdas PEMFC."
            concepto_clave_latex: "V_{\\text{celda}} = E_{\\text{Nernst}} - \\eta_{\\text{act}} - \\eta_{\\text{ohm}} - \\eta_{\\text{conc}} \\quad ; \\quad \\dot{m}_{H_2} = \\frac{N_{\\text{celdas}} \\cdot I \\cdot M_{H_2}}{2 F} \\eta_F"
            ejemplo: "Cálculo de los kilogramos por hora de hidrógeno verde producidos por un electrolizador PEM de 2 MW."
            bloque_estudio: "Pomodoro 50/10 • Ley de Faraday en electrólisis y sobrepotenciales"
      - codigo: "07011855"
        nombre: "Inmersión Profesional"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Desempeño en Entornos Reales del Sector Energético e Indicadores KPI"
            objetivo: "Aplicar competencias de ingeniería energética en empresas generadoras, distribuidoras o consultoras."
            concepto_clave_latex: "\\text{PR} = \\frac{Y_f}{Y_r} = \\frac{E_{\\text{entregada}} / P_0}{H_{\\text{POA}} / G_{\\text{STC}}}"
            ejemplo: "Cálculo del Performance Ratio (PR) mensual de una planta solar operativa durante la práctica profesional."
            bloque_estudio: "Bloque 40 min • Reporte técnico de indicadores operativos"

  - cuatrimestre: 11
    creditos_totales: 14
    asignaturas:
      - codigo: "06031854"
        nombre: "Electiva Línea de Eficiencia Energética"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Climatización Eficiente, Distritos Térmicos y Edificaciones Net-Zero"
            objetivo: "Optimizar sistemas HVAC y envolventes arquitectónicas para minimizar la carga térmica."
            concepto_clave_latex: "\\text{EER} = \\frac{\\dot{Q}_{\\text{frío}}\\,[\\text{BTU/h}]}{\\dot{W}_{\\text{eléc}}\\,[\\text{W}]} \\quad ; \\quad \\dot{Q}_{\\text{env}} = U_{\\text{global}} A (T_{\\text{ext}} - T_{\\text{int}})"
            ejemplo: "Evaluación del ahorro energético al reemplazar chillers convencionales por un distrito térmico con enfriamiento magnético/centrífugo."
            bloque_estudio: "Pomodoro 50/10 • Cargas térmicas y coeficiente EER/COP"
      - codigo: "06031853"
        nombre: "Electiva Línea de Fuentes de Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Energía Solar Térmica de Concentración (CSP) y Almacenamiento en Sales Fundidas"
            objetivo: "Analizar colectores cilindro-parabólicos y receptores de torre central para generación despachable."
            concepto_clave_latex: "C = \\frac{A_{\\text{apertura}}}{A_{\\text{receptor}}} \\quad ; \\quad \\eta_{\\text{th}} = \\eta_{\\text{opt}} - \\frac{U_L(T_r - T_a) + \\varepsilon\\sigma(T_r^4 - T_a^4)}{C \\cdot \\text{DNI}}"
            ejemplo: "Cálculo de la eficiencia térmica de un campo solar de torre central en función de la relación de concentración geométrica."
            bloque_estudio: "Pomodoro 50/10 • Balance óptico y térmico en receptores CSP"
      - codigo: "05011836"
        nombre: "Proyecto Integrador CDIO III"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Operar, Optimizar y Escalar Sistemas Energéticos Complejos"
            objetivo: "Validar la operación continua, confiabilidad y escalabilidad comercial del sistema energético desarrollado."
            concepto_clave_latex: "\\text{Disponibilidad} = \\frac{\\text{MTBF}}{\\text{MTBF} + \\text{MTTR}}"
            ejemplo: "Análisis de confiabilidad (MTBF y MTTR) y plan de operación y mantenimiento (O&M) del prototipo final."
            bloque_estudio: "Bloque 45 min • Pruebas de confiabilidad y cierre CDIO"
      - codigo: "06011844"
        nombre: "Redes de Transporte y Distribución de la Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Flujo de Carga (Newton-Raphson), Líneas de Transmisión y Pérdidas Técnicas"
            objetivo: "Modelar líneas de transmisión mediante parámetros distribuidos (ABCD) y calcular flujos de potencia activa y reactiva."
            concepto_clave_latex: "P_i = \\sum_{k=1}^{N} |V_i||V_k|(G_{ik}\\cos\\theta_{ik} + B_{ik}\\sin\\theta_{ik}) \\quad ; \\quad Q_i = \\sum_{k=1}^{N} |V_i||V_k|(G_{ik}\\sin\\theta_{ik} - B_{ik}\\cos\\theta_{ik})"
            ejemplo: "Resolución del flujo de potencia en un sistema de distribución radial con penetración de generación solar distribuida."
            bloque_estudio: "Pomodoro 50/10 • Matriz Jacobiana y regulación de tensión"
      - codigo: "04031830"
        nombre: "Transición Energética Justa"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Descarbonización, Justicia Climática, Pobreza Energética y Huella de Carbono"
            objetivo: "Cuantificar inventarios de gases de efecto invernadero (Alcances 1, 2 y 3) e índices de equidad energética."
            concepto_clave_latex: "E_{\\text{GEI}} = \\sum_{i} \\text{Dato Actividad}_i \\times \\text{FE}_i \\quad ; \\quad \\text{IPE} = \\frac{\\text{Gasto Energético Familiar}}{\\text{Ingreso Total Hogar}}"
            ejemplo: "Cálculo de las toneladas de CO₂ equivalente evitadas anualmente por un proyecto comunitario y evaluación del impacto socioambiental."
            bloque_estudio: "Pomodoro 50/10 • Cálculo de factores de emisión y matriz de impacto"

  - cuatrimestre: 12
    creditos_totales: 4
    asignaturas:
      - codigo: "07021856"
        nombre: "Modalidad de Grado"
        creditos: 4
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero: 1
            titulo: "Sustentación de Trabajo de Grado, Validación Científica y Métricas de Error"
            objetivo: "Demostrar rigurosidad metodológica, técnica y analítica en la solución de un problema real de la ingeniería energética."
            concepto_clave_latex: "R^2 = 1 - \\frac{\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2}{\\sum_{i=1}^{n}(y_i - \\bar{y})^2} \\quad ; \\quad \\text{MAPE} = \\frac{100\\%}{n}\\sum_{i=1}^{n}\\left|\\frac{y_i - \\hat{y}_i}{y_i}\\right|"
            ejemplo: "Validación estadística del modelo o prototipo de grado frente a datos experimentales de campo."
            bloque_estudio: "Pomodoro 50/10 • Defensa técnica y análisis de resultados"
---

# Base de Datos Curricular: Ingeniería Energética (`8108`)

> **Universidad del Magdalena** • Facultad de Ingeniería • Código SNIES: `118222`  
> **Estructura:** 12 Cuatrimestres • 56 Asignaturas Oficiales • 162 Créditos Académicos  
> **Motor Matemático:** Sintaxis nativa $\LaTeX$ / KaTeX compatible con `flutter_math_fork`.

---

## Cuatrimestre 1 (14 Créditos)

### 1. Cálculo Diferencial (`02011807`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `4` • **Color UI:** `#5E5CE6`
* **Tema 1: Límites y Continuidad de Funciones Reales**
  * **Objetivo:** Analizar el comportamiento asintótico y la continuidad de funciones aplicadas a modelos físicos.
  * **Concepto Clave:**
    $$\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$
  * **Ejemplo:** Determinación de la continuidad en la curva de potencia de arranque de un generador.
* **Tema 2: Derivada, Regla de la Cadena y Optimización**
  * **Objetivo:** Determinar razones de cambio instantáneas y puntos críticos de máxima eficiencia.
  * **Concepto Clave:**
    $$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) \quad ; \quad f'(x_c) = 0$$
  * **Ejemplo:** Cálculo del ángulo de inclinación óptimo para maximizar la radiación captada por un colector solar.

### 2. Fundamentos de Programación e IA (`03011813`)
* **Categoría:** `PROGRAMACION_IA` • **Créditos:** `4` • **Color UI:** `#0A84FF`
* **Tema 1: Algoritmia, Complejidad y Estructuras de Control**
  * **Objetivo:** Diseñar algoritmos eficientes para el procesamiento de datos energéticos y series temporales.
  * **Concepto Clave:**
    $$T(n) = \mathcal{O}(n \log n) \quad ; \quad \bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$$
  * **Ejemplo:** Script en Python para limpiar y promediar lecturas horarias de irradiancia solar.
* **Tema 2: Introducción a Regresión y Modelos Predictivos**
  * **Objetivo:** Ajustar modelos lineales básicos para estimar demanda energética.
  * **Concepto Clave:**
    $$\hat{y} = w_1 x + w_0 \quad ; \quad \text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
  * **Ejemplo:** Predicción del consumo eléctrico diario en función de la temperatura ambiente.

### 3. General English I (`01021802`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Technical Vocabulary & Present Structures**
  * **Objetivo:** Comprender fichas técnicas de equipos energéticos y magnitudes del Sistema Internacional en inglés.
  * **Concepto Clave:**
    $$P_{\text{rated}} = V_{\text{nom}} \cdot I_{\text{nom}}$$
  * **Ejemplo:** Lectura e interpretación de un datasheet de módulos fotovoltaicos en inglés técnico.

### 4. Introducción a la Ingeniería Energética (`04011822`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Matriz Energética, Unidades y Rendimiento Global**
  * **Objetivo:** Comprender las cadenas de conversión de energía primaria a energía útil y su eficiencia.
  * **Concepto Clave:**
    $$\eta_{\text{global}} = \frac{E_{\text{útil}}}{E_{\text{primaria}}} = \prod_{i=1}^{n} \eta_i$$
  * **Ejemplo:** Cálculo de la eficiencia combinada de una central térmica considerando caldera, turbina y generador.

### 5. Procesos Lectores, Escriturales y Orales (`01011801`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Estructura de Informes Técnicos y Artículos Científicos**
  * **Objetivo:** Redactar documentos de ingeniería con precisión argumentativa, citación IEEE y síntesis.
  * **Concepto Clave:**
    $$\text{Índice de Legibilidad} = 206.835 - 1.015\left(\frac{\text{Palabras}}{\text{Oraciones}}\right)$$
  * **Ejemplo:** Estructuración del resumen ejecutivo (Abstract) de un proyecto de transición energética.

---

## Cuatrimestre 2 (14 Créditos)

### 6. Física Mecánica (`02021810`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Leyes de Newton y Dinámica con Rozamiento**
  * **Objetivo:** Entender la segunda ley de Newton y su relación con las fuerzas de fricción estática y cinética.
  * **Concepto Clave:**
    $$\sum \vec{F} = m \cdot \vec{a} \quad ; \quad f_k = \mu_k \cdot N$$
  * **Ejemplo:** Un bloque sobre un plano inclinado experimenta una fuerza de rozamiento opuesta al deslizamiento proporcional a la normal.
* **Tema 2: Trabajo, Energía Mecánica y Potencia**
  * **Objetivo:** Aplicar el teorema del trabajo y la conservación de la energía en sistemas mecánicos.
  * **Concepto Clave:**
    $$W = \int_{r_1}^{r_2} \vec{F} \cdot d\vec{r} = \Delta K \quad ; \quad P = \vec{F} \cdot \vec{v}$$
  * **Ejemplo:** Cálculo de la potencia mecánica entregada por un eje rotatorio bajo par constante.

### 7. Fundamentos de la Electricidad I (`03041819`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Leyes de Ohm, Kirchhoff y Análisis de Nodos/Mallas**
  * **Objetivo:** Resolver circuitos resistivos en corriente continua mediante conservación de carga y energía.
  * **Concepto Clave:**
    $$V = I \cdot R \quad ; \quad \sum_{k=1}^{n} I_k = 0 \quad ; \quad \sum_{m=1}^{p} V_m = 0$$
  * **Ejemplo:** Determinación de corrientes de rama y potencia disipada en resistencias de carga.
* **Tema 2: Teoremas de Thévenin, Norton y Máxima Potencia**
  * **Objetivo:** Simplificar redes lineales activas entre dos terminales a un circuito equivalente.
  * **Concepto Clave:**
    $$V_{th} = V_{oc} \quad ; \quad R_{th} = \frac{V_{oc}}{I_{sc}} \quad ; \quad P_{\max} = \frac{V_{th}^2}{4 R_{th}}$$
  * **Ejemplo:** Acoplamiento de impedancia resistiva para extraer la máxima potencia de una celda solar.

### 8. General English II (`01021803`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Comparative Analysis & Process Descriptions**
  * **Objetivo:** Describir procesos secuenciales y comparar tecnologías energéticas en inglés.
  * **Concepto Clave:**
    $$\Delta \eta = \eta_{\text{new}} - \eta_{\text{baseline}}$$
  * **Ejemplo:** Comparación escrita entre eficiencia de turbinas Pelton y Francis.

### 9. Probabilidad y Estadística (`03031818`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `3` • **Color UI:** `#5E5CE6`
* **Tema 1: Distribuciones de Probabilidad (Weibull y Normal)**
  * **Objetivo:** Modelar la variabilidad estocástica de recursos renovables como la velocidad del viento.
  * **Concepto Clave:**
    $$f(v) = \frac{k}{c}\left(\frac{v}{c}\right)^{k-1} \exp\left[-\left(\frac{v}{c}\right)^k\right]$$
  * **Ejemplo:** Ajuste de la distribución de Weibull para estimar la frecuencia de vientos útiles en la región Caribe.

### 10. Química Aplicada (`02031812`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Termoquímica, Combustión y Electroquímica**
  * **Objetivo:** Calcular entalpías de reacción, poder calorífico y potenciales de celda.
  * **Concepto Clave:**
    $$\Delta H^\circ_{\text{rxn}} = \sum \nu_p \Delta H^\circ_{f,p} - \sum \nu_r \Delta H^\circ_{f,r} \quad ; \quad E_{\text{celda}} = E^\circ - \frac{RT}{nF}\ln Q$$
  * **Ejemplo:** Cálculo del poder calorífico inferior (PCI) del metano y potencial en una celda galvánica.

---

## Cuatrimestre 3 (15 Créditos)

### 11. Cálculo Integral (`02011808`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `4` • **Color UI:** `#5E5CE6`
* **Tema 1: Técnicas de Integración e Integral Definida**
  * **Objetivo:** Resolver integrales por partes, sustitución trigonométrica y fracciones parciales para acumular magnitudes.
  * **Concepto Clave:**
    $$\int u \, dv = u \cdot v - \int v \, du \quad ; \quad E = \int_{t_1}^{t_2} P(t) \, dt$$
  * **Ejemplo:** Integración de la curva de demanda de potencia diaria para obtener la energía consumida en $\text{MWh}$.

### 12. Calor y Ondas (`02021811`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Calorimetría, Dilatación Térmica y Movimiento Ondulatorio**
  * **Objetivo:** Analizar el intercambio de calor sensible/latente y la propagación de ondas mecánicas y electromagnéticas.
  * **Concepto Clave:**
    $$Q = m c \Delta T + m L_f \quad ; \quad \frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}$$
  * **Ejemplo:** Cálculo del equilibrio térmico en un tanque de almacenamiento térmico y longitud de onda del espectro solar.

### 13. Fundamentos de Electricidad II (`03041820`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Circuitos en Corriente Alterna (AC), Fasores y Potencia Compleja**
  * **Objetivo:** Analizar redes en estado estacionario sinusoidal, triángulo de potencias y corrección del factor de potencia.
  * **Concepto Clave:**
    $$\mathbf{S} = P + jQ = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* \quad ; \quad \text{FP} = \cos(\theta_v - \theta_i)$$
  * **Ejemplo:** Dimensionamiento de un banco de capacitores para elevar el factor de potencia de $0.82$ a $0.96$ inductivo.

### 14. Fundamentos de Hidráulica y Neumática (`03021815`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Principio de Pascal, Actuadores y Potencia Fluida**
  * **Objetivo:** Calcular presiones, caudales y fuerzas en circuitos óleo-hidráulicos y neumáticos.
  * **Concepto Clave:**
    $$P = \frac{F}{A} \quad ; \quad N_{\text{hid}} = \Delta P \cdot Q$$
  * **Ejemplo:** Cálculo de la fuerza ejercida por el cilindro hidráulico del sistema de *pitch* en un aerogenerador.

### 15. General English III (`01021804`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Passive Voice in Technical Manuals & Reports**
  * **Objetivo:** Redactar procedimientos de laboratorio y protocolos de mantenimiento usando voz pasiva en inglés.
  * **Concepto Clave:**
    $$\text{Efficiency}(\%) = \left(\frac{P_{\text{out}}}{P_{\text{in}}}\right) \times 100$$
  * **Ejemplo:** Interpretación de manuales de operación de inversores solares en inglés.

---

## Cuatrimestre 4 (15 Créditos)

### 16. Álgebra Lineal (`02011809`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `3` • **Color UI:** `#5E5CE6`
* **Tema 1: Sistemas Matriciales, Transformaciones y Valores Propios**
  * **Objetivo:** Resolver sistemas de ecuaciones lineales de gran escala y calcular autovalores de estabilidad.
  * **Concepto Clave:**
    $$A\vec{x} = \vec{b} \quad ; \quad \det(A - \lambda I) = 0$$
  * **Ejemplo:** Formulación de la matriz de admitancia nodal en una red eléctrica de $4$ nodos.

### 17. Conversión de Energía (`06011837`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Principios Electromecánicos y Termoeléctricos de Conversión**
  * **Objetivo:** Modelar el acoplamiento entre energía térmica, mecánica, química y eléctrica.
  * **Concepto Clave:**
    $$dW_{\text{mec}} = dW_{\text{campo}} + dW_{\text{eléc}} \quad ; \quad \tau = \frac{\partial W'(\theta, i)}{\partial \theta}$$
  * **Ejemplo:** Cálculo del par electromagnético desarrollado en un transductor rotativo.

### 18. Electricidad y Magnetismo (`03041821`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Ecuaciones de Maxwell, Ley de Gauss y Ley de Faraday**
  * **Objetivo:** Analizar campos electrostáticos, magnetostáticos y la inducción electromagnética.
  * **Concepto Clave:**
    $$\oint_S \vec{E} \cdot d\vec{A} = \frac{q_{\text{enc}}}{\varepsilon_0} \quad ; \quad \mathcal{E} = -N\frac{d\Phi_B}{dt}$$
  * **Ejemplo:** Cálculo de la fuerza electromotriz inducida en una espira que rota dentro de un campo magnético uniforme.

### 19. General English IV (`01021805`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Academic Presentations & Abstract Writing**
  * **Objetivo:** Exponer resultados de proyectos de ingeniería mediante vocabulario académico formal.
  * **Concepto Clave:**
    $$\text{ROI} = \frac{\text{Net Benefit}}{\text{Total Cost}} \times 100$$
  * **Ejemplo:** Presentación oral de 5 minutos sobre viabilidad de una micro-red solar.

### 20. Termodinámica (`03021817`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Primera y Segunda Ley de la Termodinámica y Ciclos de Potencia**
  * **Objetivo:** Evaluar balances de energía y entropía en volúmenes de control (turbinas, compresores, ciclos Rankine y Brayton).
  * **Concepto Clave:**
    $$\dot{Q}_{vc} - \dot{W}_{vc} = \sum \dot{m}_s\left(h_s + \frac{v_s^2}{2} + gz_s\right) - \sum \dot{m}_e\left(h_e + \frac{v_e^2}{2} + gz_e\right) \quad ; \quad \eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H}$$
  * **Ejemplo:** Determinación de la potencia neta y eficiencia térmica de un ciclo Rankine con sobrecalentamiento.

---

## Cuatrimestre 5 (15 Créditos)

### 21. Energía Hidráulica (`06021845`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Potencia Hidráulica, Altura Neta y Turbinas (Pelton, Francis, Kaplan)**
  * **Objetivo:** Dimensionar pequeñas centrales hidroeléctricas (PCH) a partir del caudal de diseño y salto neto.
  * **Concepto Clave:**
    $$P_{\text{hid}} = \eta_t \eta_g \rho g Q H_n \quad ; \quad H_n = H_b - h_f$$
  * **Ejemplo:** Selección de turbina y cálculo de potencia eléctrica para un salto neto de $85\text{ m}$ y caudal de $2.5\text{ m}^3/\text{s}$.

### 22. Energía Solar Fotovoltaica (`06021846`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Física de la Celda Solar, Curva I-V y Dimensionamiento FV**
  * **Objetivo:** Modelar el comportamiento eléctrico de arreglos fotovoltaicos bajo condiciones reales de operación (NOCT).
  * **Concepto Clave:**
    $$I = I_L - I_0\left[\exp\left(\frac{q(V + I R_s)}{n k_B T}\right) - 1\right] - \frac{V + I R_s}{R_{sh}} \quad ; \quad \text{FF} = \frac{V_{mp} I_{mp}}{V_{oc} I_{sc}}$$
  * **Ejemplo:** Cálculo de la caída de tensión de circuito abierto por incremento de temperatura en paneles instalados en Santa Marta.

### 23. Mediciones e Instrumentación (`06011838`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Sensores, Propagación de Incertidumbre y Acondicionamiento de Señal**
  * **Objetivo:** Caracterizar errores estáticos/dinámicos en instrumentos de medición eléctrica y térmica.
  * **Concepto Clave:**
    $$u_c(y) = \sqrt{\sum_{i=1}^{N}\left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)}$$
  * **Ejemplo:** Cálculo de la incertidumbre combinada en la medición de potencia activa mediante transformadores de instrumentación.

### 24. Modelación Matemática para Ingeniería (`04021825`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `3` • **Color UI:** `#5E5CE6`
* **Tema 1: Ecuaciones Diferenciales Ordinarias y Transformada de Laplace**
  * **Objetivo:** Formular y resolver sistemas dinámicos de primer y segundo orden en el dominio del tiempo y la frecuencia.
  * **Concepto Clave:**
    $$a_2\frac{d^2y}{dt^2} + a_1\frac{dy}{dt} + a_0 y = f(t) \quad ; \quad \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt$$
  * **Ejemplo:** Modelado de la respuesta transitoria de temperatura en un acumulador térmico.

### 25. Sistemas Energéticos (`06011839`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Integración de Sistemas de Generación, Cogeneración y Exergía**
  * **Objetivo:** Analizar sistemas integrados de calor y potencia (CHP) mediante rendimiento exergético.
  * **Concepto Clave:**
    $$\psi = (h - h_0) - T_0(s - s_0) \quad ; \quad \eta_{II} = \frac{\dot{W}_{\text{neto}} + \dot{E}_{\text{calor}}}{\dot{E}_{\text{combustible}}}$$
  * **Ejemplo:** Evaluación de la destrucción de exergía en una planta de cogeneración industrial.

---

## Cuatrimestre 6 (13 Créditos)

### 26. General English V (`01021806`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Scientific Debate & International Energy Standards**
  * **Objetivo:** Debatir regulaciones internacionales e informes del IPCC/IEA en inglés avanzado.
  * **Concepto Clave:**
    $$\text{CI} = \frac{\text{gCO}_2\text{eq}}{\text{kWh}}$$
  * **Ejemplo:** Análisis crítico de reportes de la Agencia Internacional de Energía (IEA).

### 27. Ingeniería del Diseño y Modelado en 3D (`04021823`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#0A84FF`
* **Tema 1: Modelado Paramétrico CAD y Análisis Geométrico de Componentes**
  * **Objetivo:** Diseñar piezas mecánicas, soportes solares y rotores cumpliendo tolerancias geométricas.
  * **Concepto Clave:**
    $$I_x = \int_A y^2 \, dA \quad ; \quad \sigma_{\max} = \frac{M \cdot c}{I}$$
  * **Ejemplo:** Modelado 3D y verificación de esfuerzos de flexión en una estructura soporte para paneles solares ante cargas de viento.

### 28. Legislación y Regulación Energética (`04031827`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#BF5AF2`
* **Tema 1: Marco Regulatorio (Ley 1715, CREG) e Incentivos Tributarios**
  * **Objetivo:** Aplicar la regulación vigente de autogeneración a pequeña y gran escala (AGPE/AGGE) y beneficios fiscales.
  * **Concepto Clave:**
    $$\text{CU} = G + T + D + Cv + PR + R$$
  * **Ejemplo:** Cálculo del Costo Unitario ($\text{CU}$) de prestación del servicio eléctrico y liquidación de excedentes según resolución CREG.

### 29. Máquinas Eléctricas (`06011840`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Transformadores, Generadores Síncronos y Motores de Inducción**
  * **Objetivo:** Modelar el circuito equivalente de máquinas rotativas y estáticas en régimen permanente.
  * **Concepto Clave:**
    $$n_s = \frac{120 f}{P} \quad ; \quad s = \frac{n_s - n_m}{n_s} \quad ; \quad E_A = K \phi \omega$$
  * **Ejemplo:** Determinación del deslizamiento, corriente de estator y par desarrollado por un motor de inducción trifásico.

### 30. Proyecto Integrador CDIO I (`05011834`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `2` • **Color UI:** `#BF5AF2`
* **Tema 1: Concebir y Diseñar Soluciones Energéticas Básicas**
  * **Objetivo:** Formular el diseño conceptual de un prototipo energético aplicando la metodología CDIO.
  * **Concepto Clave:**
    $$\text{FOM} = \sum_{i=1}^{m} w_i \cdot S_i$$
  * **Ejemplo:** Matriz de decisión ponderada (*Figure of Merit*) para seleccionar la arquitectura de un cargador solar autónomo.

---

## Cuatrimestre 7 (15 Créditos)

### 31. Energía de Biomasa (`06021850`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Rutas Termoquímicas (Gasificación/Pirólisis) y Bioquímica (Biodigestión)**
  * **Objetivo:** Cuantificar la producción de biogás y *syngas* a partir de residuos agroindustriales.
  * **Concepto Clave:**
    $$\text{PCI}_{\text{húmedo}} = \text{PCI}_{\text{seco}}(1 - w) - 2.443 \cdot w$$
  * **Ejemplo:** Estimación del potencial energético de generación con raquis de palma de aceite y estiércol bovino en el Magdalena.

### 32. Energía Eólica (`06021848`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Aerodinámica de Turbinas, Límite de Betz y Perfil de Cortante**
  * **Objetivo:** Calcular la potencia extraíble del viento y la extrapolación vertical de velocidad.
  * **Concepto Clave:**
    $$P_{\text{viento}} = \frac{1}{2} \rho A v^3 C_p(\lambda, \beta) \quad ; \quad C_{p,\max} = \frac{16}{27} \approx 0.5926 \quad ; \quad v(z) = v_{\text{ref}}\left(\frac{z}{z_{\text{ref}}}\right)^\alpha$$
  * **Ejemplo:** Cálculo de la producción anual de energía (AEP) de un aerogenerador de $80\text{ m}$ de altura de buje.

### 33. Energía Geotérmica (`06021847`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Gradiente Geotérmico, Ciclos Binarios ORC y Bombas de Calor**
  * **Objetivo:** Evaluar yacimientos geotérmicos de baja, media y alta entalpía y ciclos orgánicos de Rankine.
  * **Concepto Clave:**
    $$q_{\text{geo}} = -k_{\text{roca}} \frac{dT}{dz} \quad ; \quad \text{COP}_{\text{BC}} = \frac{Q_H}{W_{\text{comp}}}$$
  * **Ejemplo:** Diseño termodinámico de una planta binaria con fluido orgánico R245fa para una fuente hidrotermal a $140\,^\circ\text{C}$.

### 34. Energía Mareomotriz (`06021849`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#0A84FF`
* **Tema 1: Energía de las Mareas, Corrientes Marinas y Undimotriz (Olas)**
  * **Objetivo:** Cuantificar la densidad de potencia de frentes de ola y embalses mareomotrices.
  * **Concepto Clave:**
    $$P_{\text{ola}} = \frac{\rho g^2}{64\pi} H_{m0}^2 T_e \quad ; \quad E_{\text{marea}} = \frac{1}{2} \rho g A R^2$$
  * **Ejemplo:** Cálculo de la potencia por metro de frente de ola en el litoral Caribe a partir de la altura significativa y periodo energético.

### 35. Mecánica de Fluidos (`03021816`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Ecuación de Bernoulli, Número de Reynolds y Pérdidas en Tuberías**
  * **Objetivo:** Analizar el flujo interno y externo de fluidos viscosos incompresibles aplicando Darcy-Weisbach.
  * **Concepto Clave:**
    $$\frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 + h_B = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 + h_T + f\frac{L}{D}\frac{v^2}{2g}$$
  * **Ejemplo:** Cálculo de la caída de presión y potencia de bombeo en una tubería forzada mediante el diagrama de Moody.

---

## Cuatrimestre 8 (14 Créditos)

### 36. Diseño y Simulación de Sistemas Energéticos (`04021824`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Optimización de Micro-redes Híbridas y Costo Nivelado (LCOE)**
  * **Objetivo:** Simular y dimensionar sistemas híbridos (Solar + Eólico + Baterías + Respaldo) minimizando el costo del ciclo de vida.
  * **Concepto Clave:**
    $$\text{LCOE} = \frac{\sum_{t=1}^{n} \frac{I_t + M_t + F_t}{(1 + r)^t}}{\sum_{t=1}^{n} \frac{E_t}{(1 + r)^t}} \quad ; \quad \text{LPSP} = \frac{\sum \text{LPS}(t)}{\sum E_{\text{demanda}}(t)}$$
  * **Ejemplo:** Optimización tecno-económica de una micro-red aislada asegurando una probabilidad de pérdida de carga menor al $1\%$.

### 37. Energy Market (`04031828`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#BF5AF2`
* **Tema 1: Mercado Mayorista de Energía, Despacho Económico y Contratos PPA**
  * **Objetivo:** Comprender la formación del precio de bolsa (*Marginal Clearing Price*) y subastas de energías renovables.
  * **Concepto Clave:**
    $$\min \sum_{i=1}^{N} C_i(P_{G,i}) \quad \text{s.a.} \quad \sum_{i=1}^{N} P_{G,i} = P_D + P_L$$
  * **Ejemplo:** Determinación del precio marginal del sistema a partir de la intersección de las curvas de oferta de generadores y demanda.

### 38. Formulación de Proyectos (`05011832`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#BF5AF2`
* **Tema 1: Estudio de Mercado, Técnico y Estructura de Desglose de Trabajo (EDT)**
  * **Objetivo:** Estructurar proyectos de ingeniería bajo metodologías de Marco Lógico y PMBOK.
  * **Concepto Clave:**
    $$t_e = \frac{t_o + 4t_m + t_p}{6} \quad ; \quad \sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$$
  * **Ejemplo:** Cálculo de la ruta crítica (CPM/PERT) para el cronograma de construcción de una granja solar de $5\text{ MW}$.

### 39. Metodología de la Investigación (`05011831`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Diseño Experimental, Hipótesis y Tamaño de Muestra**
  * **Objetivo:** Plantear problemas de investigación científica con rigor estadístico y validación experimental.
  * **Concepto Clave:**
    $$n = \frac{Z_{\alpha/2}^2 \cdot p \cdot q}{e^2}$$
  * **Ejemplo:** Diseño de un experimento factorial para evaluar el efecto de la suciedad (*soiling*) sobre paneles bifaciales.

### 40. Programación Avanzada y Aplicaciones de IA (`03011814`)
* **Categoría:** `PROGRAMACION_IA` • **Créditos:** `3` • **Color UI:** `#0A84FF`
* **Tema 1: Redes Neuronales, Pronóstico de Generación y Optimización Heurística**
  * **Objetivo:** Entrenar modelos de Machine Learning para predecir generación solar/eólica y detección de fallas.
  * **Concepto Clave:**
    $$a^{(l)} = \sigma\left(W^{(l)} a^{(l-1)} + b^{(l)}\right) \quad ; \quad \theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t)$$
  * **Ejemplo:** Red neuronal recurrente (LSTM) para el pronóstico de irradiancia solar con horizonte de $24\text{ horas}$.

---

## Cuatrimestre 9 (14 Créditos)

### 41. Comunidades Energéticas Sostenibles (`04031829`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Generación Distribuida Colectiva y Reparto de Excedentes**
  * **Objetivo:** Diseñar esquemas técnicos y socioeconómicos de comunidades energéticas bajo criterios de equidad.
  * **Concepto Clave:**
    $$E_{\text{asignada},i}(t) = \beta_i \cdot E_{\text{gen}}(t) \quad ; \quad \sum_{i=1}^{N} \beta_i = 1$$
  * **Ejemplo:** Cálculo de coeficientes de reparto dinámico en una comunidad energética rural en la Sierra Nevada.

### 42. Gestión, Auditoría y Eficiencia Energética (`04031826`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Norma ISO 50001, Línea Base Energética e Indicadores EnPI**
  * **Objetivo:** Realizar auditorías energéticas detalladas e identificar oportunidades de ahorro en climatización, motores e iluminación.
  * **Concepto Clave:**
    $$E_{\text{base}} = m \cdot P_{\text{producción}} + E_0 \quad ; \quad \text{CUSUM}_t = \sum_{k=1}^{t} (E_{\text{real},k} - E_{\text{esperada},k})$$
  * **Ejemplo:** Construcción de la línea base energética y gráfico de sumas acumuladas (CUSUM) en una planta industrial.

### 43. Instalaciones Eléctricas con Energías Renovables (`06011842`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Diseño RETIE, Protecciones DC/AC, Calibre de Conductores y Caída de Tensión**
  * **Objetivo:** Dimensionar conductores, canalizaciones, protecciones termomagnéticas y puestas a tierra según el RETIE y NTC 2050.
  * **Concepto Clave:**
    $$\Delta V(\%) = \frac{k \cdot I \cdot L \cdot (R\cos\theta + X\sin\theta)}{V_{\text{nom}}} \times 100 \le 3\% \quad ; \quad I_{\text{diseño}} = 1.25 \cdot 1.25 \cdot I_{sc}$$
  * **Ejemplo:** Selección de calibre AWG y fusibles gPV para un arreglo solar cumpliendo el límite de regulación de tensión del $3\%$.

### 44. Proyecto Integrador CDIO II (`05011835`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `2` • **Color UI:** `#BF5AF2`
* **Tema 1: Implementar y Construir Prototipos Energéticos**
  * **Objetivo:** Integrar hardware, instrumentación y control en un prototipo funcional validado en laboratorio.
  * **Concepto Clave:**
    $$e_{\text{rel}} = \left|\frac{X_{\text{exp}} - X_{\text{sim}}}{X_{\text{sim}}}\right| \times 100\%$$
  * **Ejemplo:** Pruebas de desempeño en banco de un sistema de seguimiento solar de dos ejes comparado contra el modelo simulado.

### 45. Transferencia de Calor (`06011841`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Conducción (Fourier), Convección (Newton), Radiación y Diseño de Intercambiadores**
  * **Objetivo:** Calcular flujos térmicos multimodales y dimensionar intercambiadores de calor mediante el método LMTD y efectividad-NTU.
  * **Concepto Clave:**
    $$q = U A \Delta T_{\text{lm}} \quad ; \quad \Delta T_{\text{lm}} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)} \quad ; \quad q_{\text{rad}} = \varepsilon \sigma A (T_s^4 - T_{\text{alr}}^4)$$
  * **Ejemplo:** Dimensionamiento del área de transferencia de un intercambiador de coraza y tubos para recuperación de calor residual.

---

## Cuatrimestre 10 (15 Créditos)

### 46. Almacenamiento de la Energía (`06011843`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Sistemas BESS (Litio-Ion), Estado de Carga (SoC), Bombeo y Almacenamiento Térmico**
  * **Objetivo:** Dimensionar bancos de baterías y sistemas de almacenamiento evaluando profundidad de descarga (DoD) y degradación.
  * **Concepto Clave:**
    $$\text{SoC}(t) = \text{SoC}(t_0) - \frac{\eta_{\text{coul}}}{C_{\text{nom}}} \int_{t_0}^{t} I(\tau)\,d\tau \quad ; \quad C_{\text{banco}} = \frac{E_{\text{autonomía}}}{V_{\text{sist}} \cdot \text{DoD}_{\max} \cdot \eta_{\text{inv}}}$$
  * **Ejemplo:** Cálculo de la capacidad en $\text{MWh}$ de un sistema BESS en tecnología LFP para respaldo de $4\text{ horas}$ con $\text{DoD}$ del $85\%$.

### 47. Aprovechamiento de Fuentes Energéticas No Renovables (`06021851`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Ciclos Combinados Gas-Vapor, Combustión Limpia y Captura de Carbono (CCUS)**
  * **Objetivo:** Maximizar el rendimiento térmico de plantas convencionales y cuantificar la reducción de emisiones.
  * **Concepto Clave:**
    $$\eta_{\text{CC}} = \eta_B + \eta_R - \eta_B \eta_R$$
  * **Ejemplo:** Cálculo de la eficiencia global de una central de ciclo combinado (Turbina de Gas Brayton + Ciclo Rankine con HRSG).

### 48. Evaluación y Gestión de Proyectos (`05011833`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#BF5AF2`
* **Tema 1: Evaluación Financiera (VPN, TIR, WACC) y Análisis de Riesgo**
  * **Objetivo:** Evaluar la viabilidad financiera de proyectos energéticos incorporando incentivos de la Ley 1715 y bonos de carbono.
  * **Concepto Clave:**
    $$\text{VPN} = -I_0 + \sum_{t=1}^{n} \frac{\text{FCL}_t}{(1 + \text{WACC})^t} \quad ; \quad \sum_{t=0}^{n} \frac{\text{FCL}_t}{(1 + \text{TIR})^t} = 0$$
  * **Ejemplo:** Flujo de caja libre descontado a $20\text{ años}$ para un parque solar con depreciación acelerada.

### 49. Hydrogen Energy (`06021852`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#0A84FF`
* **Tema 1: Electrólisis del Agua (PEM/Alcalina), Almacenamiento y Celdas de Combustible**
  * **Objetivo:** Calcular el consumo específico de electrolizadores para producción de hidrógeno verde y la curva de polarización de celdas PEMFC.
  * **Concepto Clave:**
    $$V_{\text{celda}} = E_{\text{Nernst}} - \eta_{\text{act}} - \eta_{\text{ohm}} - \eta_{\text{conc}} \quad ; \quad \dot{m}_{H_2} = \frac{N_{\text{celdas}} \cdot I \cdot M_{H_2}}{2 F} \eta_F$$
  * **Ejemplo:** Cálculo de los kilogramos por hora de hidrógeno verde producidos por un electrolizador PEM de $2\text{ MW}$.

### 50. Inmersión Profesional (`07011855`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#8E8E93`
* **Tema 1: Desempeño en Entornos Reales del Sector Energético e Indicadores KPI**
  * **Objetivo:** Aplicar competencias de ingeniería energética en empresas generadoras, distribuidoras o consultoras.
  * **Concepto Clave:**
    $$\text{PR} = \frac{Y_f}{Y_r} = \frac{E_{\text{entregada}} / P_0}{H_{\text{POA}} / G_{\text{STC}}}$$
  * **Ejemplo:** Cálculo del *Performance Ratio* ($\text{PR}$) mensual de una planta solar operativa durante la práctica profesional.

---

## Cuatrimestre 11 (14 Créditos)

### 51. Electiva Línea de Eficiencia Energética (`06031854`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Climatización Eficiente, Distritos Térmicos y Edificaciones Net-Zero**
  * **Objetivo:** Optimizar sistemas HVAC y envolventes arquitectónicas para minimizar la carga térmica.
  * **Concepto Clave:**
    $$\text{EER} = \frac{\dot{Q}_{\text{frío}}\,[\text{BTU/h}]}{\dot{W}_{\text{eléc}}\,[\text{W}]} \quad ; \quad \dot{Q}_{\text{env}} = U_{\text{global}} A (T_{\text{ext}} - T_{\text{int}})$$
  * **Ejemplo:** Evaluación del ahorro energético al reemplazar *chillers* convencionales por un distrito térmico de alta eficiencia.

### 52. Electiva Línea de Fuentes de Energía (`06031853`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Energía Solar Térmica de Concentración (CSP) y Almacenamiento en Sales Fundidas**
  * **Objetivo:** Analizar colectores cilindro-parabólicos y receptores de torre central para generación despachable.
  * **Concepto Clave:**
    $$C = \frac{A_{\text{apertura}}}{A_{\text{receptor}}} \quad ; \quad \eta_{\text{th}} = \eta_{\text{opt}} - \frac{U_L(T_r - T_a) + \varepsilon\sigma(T_r^4 - T_a^4)}{C \cdot \text{DNI}}$$
  * **Ejemplo:** Cálculo de la eficiencia térmica de un campo solar de torre central en función de la relación de concentración geométrica.

### 53. Proyecto Integrador CDIO III (`05011836`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `2` • **Color UI:** `#BF5AF2`
* **Tema 1: Operar, Optimizar y Escalar Sistemas Energéticos Complejos**
  * **Objetivo:** Validar la operación continua, confiabilidad y escalabilidad comercial del sistema energético desarrollado.
  * **Concepto Clave:**
    $$\text{Disponibilidad} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
  * **Ejemplo:** Análisis de confiabilidad ($\text{MTBF}$ y $\text{MTTR}$) y plan de operación y mantenimiento (O&M) del prototipo final.

### 54. Redes de Transporte y Distribución de la Energía (`06011844`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Flujo de Carga (Newton-Raphson), Líneas de Transmisión y Pérdidas Técnicas**
  * **Objetivo:** Modelar líneas de transmisión mediante parámetros distribuidos ($ABCD$) y calcular flujos de potencia activa y reactiva.
  * **Concepto Clave:**
    $$P_i = \sum_{k=1}^{N} |V_i||V_k|(G_{ik}\cos\theta_{ik} + B_{ik}\sin\theta_{ik}) \quad ; \quad Q_i = \sum_{k=1}^{N} |V_i||V_k|(G_{ik}\sin\theta_{ik} - B_{ik}\cos\theta_{ik})$$
  * **Ejemplo:** Resolución del flujo de potencia en un sistema de distribución radial con penetración de generación solar distribuida.

### 55. Transición Energética Justa (`04031830`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Descarbonización, Justicia Climática, Pobreza Energética y Huella de Carbono**
  * **Objetivo:** Cuantificar inventarios de gases de efecto invernadero (Alcances 1, 2 y 3) e índices de equidad energética.
  * **Concepto Clave:**
    $$E_{\text{GEI}} = \sum_{i} \text{Dato Actividad}_i \times \text{FE}_i \quad ; \quad \text{IPE} = \frac{\text{Gasto Energético Familiar}}{\text{Ingreso Total Hogar}}$$
  * **Ejemplo:** Cálculo de las toneladas de $\text{CO}_2$ equivalente evitadas anualmente por un proyecto comunitario y evaluación del impacto socioambiental.

---

## Cuatrimestre 12 (4 Créditos)

### 56. Modalidad de Grado (`07021856`)
* **Categoría:** `PROYECTOS_GESTION` • **Créditos:** `4` • **Color UI:** `#BF5AF2`
* **Tema 1: Sustentación de Trabajo de Grado, Validación Científica y Métricas de Error**
  * **Objetivo:** Demostrar rigurosidad metodológica, técnica y analítica en la solución de un problema real de la ingeniería energética.
  * **Concepto Clave:**
    $$R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2} \quad ; \quad \text{MAPE} = \frac{100\%}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|$$
  * **Ejemplo:** Validación estadística del modelo o prototipo de grado frente a datos experimentales de campo.