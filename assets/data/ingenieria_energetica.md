---
database_name: "ingenieria_energetica"
schema_version: "2.2.0"
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
            titulo: "Funciones Reales, Dominio, Composición e Inversas"
            objetivo: "Modelar relaciones entre variables físicas mediante funciones algebraicas, exponenciales, logarítmicas y trigonométricas."
            concepto_clave_latex: "(f \\circ g)(x) = f(g(x)) \\quad ; \\quad f^{-1}(f(x)) = x \\quad ; \\quad P(T) = P_0 e^{\\beta(T - T_{\\text{STC}})}"
            ejemplo: "Modelado de la variación de potencia de un módulo solar en función de la temperatura de celda."
            bloque_estudio: "Pomodoro 50/10 • Dominio, rango y composición de funciones"
          - numero: 2
            titulo: "Límites Laterales, Indeterminaciones y Asíntotas"
            objetivo: "Analizar el comportamiento local y asintótico de funciones reales mediante definición formal y álgebra de límites."
            concepto_clave_latex: "\\lim_{x \\to a} f(x) = L \\iff \\forall \\varepsilon > 0, \\exists \\delta > 0 : 0 < |x - a| < \\delta \\implies |f(x) - L| < \\varepsilon"
            ejemplo: "Determinación del régimen estacionario asintótico de enfriamiento de un transformador cuando el tiempo tiende a infinito."
            bloque_estudio: "Pomodoro 50/10 • 6 límites algebraicos, trigonométricos y al infinito"
          - numero: 3
            titulo: "Continuidad Puntual y Teorema del Valor Intermedio"
            objetivo: "Evaluar la continuidad en puntos e intervalos cerrados para garantizar existencia de raíces en modelos físicos."
            concepto_clave_latex: "\\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = f(c) \\quad ; \\quad f(a) < N < f(b) \\implies \\exists c \\in (a,b) : f(c) = N"
            ejemplo: "Análisis de continuidad por tramos en la curva de potencia de un aerogenerador entre velocidad de arranque y nominal."
            bloque_estudio: "Práctica 40 min • Clasificación de discontinuidades y TVI"
          - numero: 4
            titulo: "La Derivada, Regla de la Cadena y Derivación Implícita"
            objetivo: "Calcular tasas de cambio instantáneas aplicando reglas de derivación, regla de la cadena y derivadas de orden superior."
            concepto_clave_latex: "f'(x) = \\lim_{h \\to 0}\\frac{f(x+h)-f(x)}{h} \\quad ; \\quad \\frac{d}{dx}[f(g(x))] = f'(g(x)) \\cdot g'(x)"
            ejemplo: "Obtención de la potencia instantánea P(t) = dE/dt entregada por un sistema de almacenamiento a partir de su energía acumulada."
            bloque_estudio: "Pomodoro 50/10 • Regla de la cadena y derivación implícita/logarítmica"
          - numero: 5
            titulo: "Razones de Cambio, Regla de L'Hôpital y Optimización"
            objetivo: "Aplicar criterios de primera y segunda derivada para determinar extremos absolutos y optimizar diseños de ingeniería."
            concepto_clave_latex: "f'(x_c) = 0 \\; \\land \\; f''(x_c) < 0 \\implies x_c \\text{ es máximo} \\quad ; \\quad \\lim_{x \\to a}\\frac{f(x)}{g(x)} = \\lim_{x \\to a}\\frac{f'(x)}{g'(x)}"
            ejemplo: "Cálculo del ángulo de inclinación óptimo para maximizar la irradiancia solar anual captada por un colector."
            bloque_estudio: "Práctica Activa 50 min • Problemas aplicados de optimización y trazado"
      - codigo: "03011813"
        nombre: "Fundamentos de Programación e IA"
        creditos: 4
        obligatoria: true
        categoria: "PROGRAMACION_IA"
        color: "#0A84FF"
        temas:
          - numero: 1
            titulo: "Pensamiento Computacional, Algoritmos y Tipos de Datos"
            objetivo: "Representar soluciones estructuradas mediante pseudocódigo, diagramas de flujo, variables y expresiones lógicas."
            concepto_clave_latex: "y = (A \\land B) \\lor (\\neg C) \\quad ; \\quad E_{\\text{kWh}} = \\frac{P_{\\text{W}} \\cdot \\Delta t_{\\text{h}}}{1000}"
            ejemplo: "Algoritmo secuencial en Python para convertir lecturas crudas de potencia y tiempo a consumo facturable en kWh."
            bloque_estudio: "Pomodoro 45/10 • Pseudocódigo, operadores y tipos primitivos"
          - numero: 2
            titulo: "Estructuras de Control Condicionales, Ciclos y Complejidad"
            objetivo: "Diseñar bloques selectivos e iterativos eficientes evaluando su complejidad temporal asintótica."
            concepto_clave_latex: "T(n) = \\mathcal{O}(n \\log n) \\quad ; \\quad \\bar{x} = \\frac{1}{N}\\sum_{i=1}^{N} x_i"
            ejemplo: "Script iterativo en Python para filtrar registros nocturnos nulos y promediar series horarias de irradiancia solar."
            bloque_estudio: "Pomodoro 50/10 • Condicionales anidados y bucles for/while"
          - numero: 3
            titulo: "Modularidad, Funciones, Vectores y Matrices Numéricas"
            objetivo: "Construir subprogramas reutilizables y procesar arreglos unidimensionales y bidimensionales de mediciones."
            concepto_clave_latex: "E_{\\text{total}} = \\sum_{i=1}^{m}\\sum_{j=1}^{n} P_{ij}\\,\\Delta t \\quad ; \\quad P_k = V_k \\cdot I_k"
            ejemplo: "Procesamiento matricial con NumPy del despacho horario de 5 plantas solares durante los 30 días del mes."
            bloque_estudio: "Práctica 50 min • Funciones parametrizadas y arreglos 2D"
          - numero: 4
            titulo: "Preprocesamiento y Análisis Exploratorio de Datos Energéticos"
            objetivo: "Limpiar series de tiempo, tratar valores atípicos y escalar variables para algoritmos de inteligencia artificial."
            concepto_clave_latex: "x_{\\text{norm}} = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}} \\quad ; \\quad z = \\frac{x - \\mu}{\\sigma}"
            ejemplo: "Normalización Min-Max y estandarización Z-score de temperatura, humedad y velocidad de viento de una estación meteorológica."
            bloque_estudio: "Práctica 40 min • Limpieza de CSV energéticos con Pandas"
          - numero: 5
            titulo: "Introducción a Machine Learning y Regresión Lineal"
            objetivo: "Entrenar y evaluar modelos supervisados básicos de regresión para pronosticar demanda energética."
            concepto_clave_latex: "\\hat{y} = w_1 x + w_0 \\quad ; \\quad \\text{MSE} = \\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2"
            ejemplo: "Predicción del consumo eléctrico diario de un campus universitario en función de la temperatura ambiente."
            bloque_estudio: "Práctica 45 min • Ajuste por descenso de gradiente y métrica MSE"
      - codigo: "01021802"
        nombre: "General English I"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Academic Profiles & Introductions (Verb To Be & Pronouns)"
            objetivo: "Presentar información personal, institucional y perfiles de ingeniería empleando el verbo to be y posesivos (MCER A1)."
            concepto_clave_latex: "\\text{Subject} + \\text{am / is / are} + \\text{Complement}"
            ejemplo: "Presentación oral y escrita como estudiante de Energy Engineering en un encuentro internacional de semilleros."
            bloque_estudio: "Bloque 25 min • Diálogos breves de presentación académica"
          - numero: 2
            titulo: "Technical Vocabulary, SI Units & Datasheets"
            objetivo: "Comprender fichas técnicas de equipos energéticos, cifras y magnitudes del Sistema Internacional en inglés."
            concepto_clave_latex: "P_{\\text{rated}} = V_{\\text{nom}} \\cdot I_{\\text{nom}} \\quad ; \\quad 1\\text{ MW} = 10^6\\text{ W}"
            ejemplo: "Lectura e interpretación de parámetros nominales (Rated Power, Open-Circuit Voltage) en un datasheet fotovoltaico."
            bloque_estudio: "Bloque 25 min • Flashcards de terminología eléctrica y térmica"
          - numero: 3
            titulo: "Engineering Routines & Facts (Present Simple)"
            objetivo: "Describir rutinas de operación, horarios de mantenimiento y leyes físicas permanentes con el Present Simple."
            concepto_clave_latex: "f_{\\text{grid}} = 60\\text{ Hz} \\quad ; \\quad T_{\\text{cycle}} = \\frac{1}{f_{\\text{grid}}}"
            ejemplo: "Redacción en inglés de la rutina diaria de inspección técnica de un cuarto de inversores solares."
            bloque_estudio: "Bloque 30 min • Oraciones afirmativas, negativas y preguntas WH"
          - numero: 4
            titulo: "Live Plant Monitoring (Present Continuous & Prepositions)"
            objetivo: "Reportar acciones en progreso, ubicación de instrumentos y variaciones en tiempo real dentro del laboratorio."
            concepto_clave_latex: "\\Delta P(t) = P_{\\text{gen}}(t) - P_{\\text{load}}(t)"
            ejemplo: "Descripción en vivo del flujo de potencia en sala de control (The solar array is charging the battery bank now)."
            bloque_estudio: "Bloque 25 min • Contraste Present Simple vs. Present Continuous"
      - codigo: "04011822"
        nombre: "Introducción a la Ingeniería Energética"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Formas de Energía, Sistemas de Unidades y Perfil Profesional"
            objetivo: "Diferenciar energía primaria, secundaria, final y útil dominando las equivalencias energéticas internacionales."
            concepto_clave_latex: "1\\text{ kWh} = 3.6\\text{ MJ} \\quad ; \\quad 1\\text{ TEP} = 41.868\\text{ GJ} = 11\\,630\\text{ kWh}"
            ejemplo: "Conversión del consumo anual de combustible de una industria desde BTU y galones de diésel hacia MWh y TEP."
            bloque_estudio: "Pomodoro 45/10 • Conversión dimensional (J, kWh, BTU, kcal, TEP)"
          - numero: 2
            titulo: "Matriz Energética Mundial, Nacional (UPME) y del Caribe"
            objetivo: "Analizar la composición de la oferta y demanda energética colombiana y el potencial renovable de la región Caribe."
            concepto_clave_latex: "\\text{Participación}_i(\\%) = \\frac{E_{\\text{fuente},i}}{\\sum_{k=1}^{n} E_{\\text{fuente},k}} \\times 100\\%"
            ejemplo: "Interpretación del Plan Energético Nacional (UPME) comparando generación hidráulica, térmica y solar en Colombia."
            bloque_estudio: "Bloque 40 min • Análisis de indicadores energéticos per cápita"
          - numero: 3
            titulo: "Cadenas de Conversión, Diagramas de Sankey y Eficiencia Global"
            objetivo: "Cuantificar pérdidas por etapas en sistemas de transformación energética desde la fuente hasta el uso final."
            concepto_clave_latex: "\\eta_{\\text{global}} = \\frac{E_{\\text{útil}}}{E_{\\text{primaria}}} = \\prod_{i=1}^{n} \\eta_i"
            ejemplo: "Cálculo de la eficiencia combinada de una central termoeléctrica integrando caldera (88%), turbina (42%) y generador (97%)."
            bloque_estudio: "Pomodoro 50/10 • Construcción de diagramas de Sankey"
          - numero: 4
            titulo: "Sostenibilidad, ODS 7, Ley 1715 y Transición Energética"
            objetivo: "Comprender los retos ambientales, regulatorios y éticos de la descarbonización y el acceso universal a energía limpia."
            concepto_clave_latex: "E_{\\text{CO}_2} = E_{\\text{eléc}} \\cdot \\text{FE}_{\\text{SIN}}"
            ejemplo: "Estimación de emisiones de CO₂ evitadas anualmente al integrar autogeneración solar fotovoltaica en el campus universitario."
            bloque_estudio: "Bloque 35 min • Mapa conceptual de ODS 7 y Ley 1715"
      - codigo: "01011801"
        nombre: "Procesos Lectores, Escriturales y Orales"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Lectura Crítica, Inferencia y Superestructura Textual"
            objetivo: "Desarrollar comprensión literal, inferencial y crítica identificando tesis, argumentos y contraargumentos en textos académicos."
            concepto_clave_latex: "\\text{Lectura Crítica} = \\text{Literal} + \\text{Inferencial} + \\text{Valorativa}"
            ejemplo: "Desglose argumentativo de un artículo científico sobre comunidades energéticas sostenibles en el Caribe colombiano."
            bloque_estudio: "Bloque 35 min • Fichas de lectura analítica y macroproposiciones"
          - numero: 2
            titulo: "Escritura Académica: Coherencia, Cohesión y Precisión Léxica"
            objetivo: "Producir textos expositivos y argumentativos claros mediante planeación textual, conectores lógicos y revisión estilística."
            concepto_clave_latex: "\\text{Índice de Legibilidad} = 206.835 - 1.015\\left(\\frac{\\text{Palabras}}{\\text{Oraciones}}\\right)"
            ejemplo: "Redacción y depuración de un ensayo argumentativo sobre eficiencia energética y sostenibilidad urbana."
            bloque_estudio: "Bloque 30 min • Construcción de párrafos con oración temática"
          - numero: 3
            titulo: "Informes Técnicos de Ingeniería y Normas de Citación (IEEE / APA)"
            objetivo: "Estructurar artículos e informes de laboratorio bajo el formato IMRyD aplicando referenciación bibliográfica rigurosa."
            concepto_clave_latex: "\\text{IMRyD} : \\text{Introducción} \\longrightarrow \\text{Métodos} \\longrightarrow \\text{Resultados} \\longrightarrow \\text{Discusión}"
            ejemplo: "Estructuración del resumen ejecutivo (Abstract) y bibliografía IEEE para un proyecto de transición energética."
            bloque_estudio: "Bloque 35 min • Citación IEEE numerada y gestión de referencias"
          - numero: 4
            titulo: "Oralidad Académica, Argumentación y Defensa de Proyectos"
            objetivo: "Sustentar ideas técnicas en escenarios universitarios articulando expresión verbal, lenguaje corporal y síntesis visual."
            concepto_clave_latex: "t_{\\text{pitch}} = t_{\\text{problema}} + t_{\\text{solución}} + t_{\\text{evidencia}} + t_{\\text{cierre}}"
            ejemplo: "Sustentación oral estructurada de 5 minutos sobre una propuesta de ahorro energético institucional."
            bloque_estudio: "Bloque 30 min • Ensayo cronometrado de exposición técnica"

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
            titulo: "Análisis Dimensional, Vectores y Cinemática en 1D/2D"
            objetivo: "Describir vectorial y analíticamente el movimiento rectilíneo, parabólico y circular de partículas mediante cálculo."
            concepto_clave_latex: "\\vec{v}(t) = \\frac{d\\vec{r}}{dt} \\quad ; \\quad \\vec{a}(t) = \\frac{d\\vec{v}}{dt} \\quad ; \\quad a_c = \\frac{v^2}{R} = \\omega^2 R"
            ejemplo: "Cálculo de la velocidad lineal y aceleración centrípeta en el extremo de una pala eólica de 50 m de radio."
            bloque_estudio: "Pomodoro 50/10 • Cinemática vectorial y movimiento circular"
          - numero: 2
            titulo: "Leyes de Newton y Dinámica con Rozamiento"
            objetivo: "Aplicar las leyes del movimiento de Newton y diagramas de cuerpo libre con fuerzas de fricción estática y cinética."
            concepto_clave_latex: "\\sum \\vec{F} = m \\cdot \\vec{a} \\quad ; \\quad f_s \\le \\mu_s N \\quad ; \\quad f_k = \\mu_k N"
            ejemplo: "Determinación de la aceleración y tensión de izaje de un bloque sobre un plano inclinado con rozamiento cinético."
            bloque_estudio: "Pomodoro 50/10 • Diagramas de Cuerpo Libre en sistemas acoplados"
          - numero: 3
            titulo: "Trabajo, Energía Mecánica y Potencia"
            objetivo: "Aplicar el teorema del trabajo y la energía cinética, fuerzas conservativas y conservación de la energía mecánica."
            concepto_clave_latex: "W = \\int_{r_1}^{r_2} \\vec{F} \\cdot d\\vec{r} = \\Delta K \\quad ; \\quad E_m = K + U_g + U_e \\quad ; \\quad P = \\vec{F} \\cdot \\vec{v}"
            ejemplo: "Cálculo de la conversión de energía potencial gravitacional a cinética en la descarga de una central hidroeléctrica."
            bloque_estudio: "Práctica Activa 45 min • Conservación de energía con pérdidas no conservativas"
          - numero: 4
            titulo: "Sistemas de Partículas, Impulso, Momentum Lineal y Colisiones"
            objetivo: "Evaluar centro de masa, impulso mecánico y conservación del momentum lineal en choques elásticos e inelásticos."
            concepto_clave_latex: "\\vec{p} = m\\vec{v} \\quad ; \\quad \\vec{J} = \\int_{t_1}^{t_2} \\vec{F}(t)\\,dt = \\Delta\\vec{p} \\quad ; \\quad \\sum \\vec{p}_i = \\sum \\vec{p}_f"
            ejemplo: "Determinación de la fuerza impulsiva transferida por un chorro de agua de alta velocidad sobre un álabe Pelton."
            bloque_estudio: "Pomodoro 50/10 • Colisiones 1D/2D y transferencia de momentum"
          - numero: 5
            titulo: "Dinámica Rotacional, Momento de Inercia y Equilibrio Estático"
            objetivo: "Modelar el torque, momento de inercia (Steiner), energía cinética rotacional y equilibrio de cuerpos rígidos."
            concepto_clave_latex: "\\sum \\tau = I\\alpha \\quad ; \\quad K_{\\text{rot}} = \\frac{1}{2}I\\omega^2 \\quad ; \\quad \\sum \\vec{F} = \\vec{0},\\; \\sum \\vec{\\tau} = \\vec{0}"
            ejemplo: "Cálculo de la energía almacenada en un volante de inercia (flywheel) y reacciones estáticas en estructuras soporte solares."
            bloque_estudio: "Práctica 50 min • Dinámica de rotores y estática estructural básica"
      - codigo: "03041819"
        nombre: "Fundamentos de la Electricidad I"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Variables Eléctricas, Ley de Ohm, Asociaciones y Potencia DC"
            objetivo: "Cuantificar carga, corriente, tensión, resistencias serie/paralelo, divisores y balance de potencia en DC."
            concepto_clave_latex: "i(t) = \\frac{dq}{dt} \\quad ; \\quad V = I \\cdot R \\quad ; \\quad P = V \\cdot I = I^2 R = \\frac{V^2}{R}"
            ejemplo: "Cálculo de caída de tensión, pérdidas Joule y eficiencia en el cableado DC entre un string fotovoltaico y su inversor."
            bloque_estudio: "Pomodoro 45/10 • Reducción serie-paralelo y transformación Y-Delta"
          - numero: 2
            titulo: "Leyes de Kirchhoff y Análisis Sistemático de Nodos y Mallas"
            objetivo: "Resolver circuitos resistivos lineales con fuentes independientes y dependientes mediante LCK y LVK."
            concepto_clave_latex: "\\sum_{k=1}^{n} I_k = 0 \\quad ; \\quad \\sum_{m=1}^{p} V_m = 0 \\quad ; \\quad \\mathbf{G}\\mathbf{v}_n = \\mathbf{i}_s"
            ejemplo: "Determinación de tensiones de nodo y flujos de corriente en una micro-red DC con generación solar, batería y carga."
            bloque_estudio: "Pomodoro 50/10 • Sistemas de ecuaciones por supernodos y supermallas"
          - numero: 3
            titulo: "Linealidad, Superposición, Thévenin, Norton y Máxima Potencia"
            objetivo: "Simplificar redes activas entre dos terminales a circuitos equivalentes para optimizar la transferencia de potencia."
            concepto_clave_latex: "V_{th} = V_{oc} \\quad ; \\quad R_{th} = \\frac{V_{oc}}{I_{sc}} \\quad ; \\quad P_{\\max} = \\frac{V_{th}^2}{4 R_{th}}"
            ejemplo: "Acoplamiento óptimo de carga resistiva para extraer la máxima potencia disponible de una fuente DC equivalente."
            bloque_estudio: "Práctica 45 min • Reducción de Thévenin/Norton con fuentes controladas"
          - numero: 4
            titulo: "Capacitores, Inductores y Transitorios de Primer Orden (RC y RL)"
            objetivo: "Analizar el almacenamiento de energía en campos eléctricos/magnéticos y la respuesta natural y forzada de circuitos RC y RL."
            concepto_clave_latex: "v_C(t) = V_\\infty + [v_C(0) - V_\\infty]e^{-t/\\tau} \\quad ; \\quad \\tau_{RC} = R_{th}C \\quad ; \\quad \\tau_{RL} = \\frac{L}{R_{th}}"
            ejemplo: "Dimensionamiento de la resistencia de precarga del bus DC capacitivo de un convertidor para limitar picos de corriente."
            bloque_estudio: "Pomodoro 50/10 • Constantes de tiempo y curvas de carga/descarga"
      - codigo: "01021803"
        nombre: "General English II"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Energy Milestones & Incident Logs (Past Simple & Continuous)"
            objetivo: "Narrar hitos científicos y redactar bitácoras de eventos operativos pasados combinando Past Simple y Past Continuous (MCER A2)."
            concepto_clave_latex: "\\Delta t_{\\text{outage}} = t_{\\text{restored}} - t_{\\text{fault}}"
            ejemplo: "Reporte breve de falla eléctrica (While the turbine was operating at full load, the grid sensor detected a voltage sag)."
            bloque_estudio: "Bloque 25 min • Verbos regulares/irregulares en reportes técnicos"
          - numero: 2
            titulo: "Comparative Analysis of Power Technologies"
            objetivo: "Comparar rendimientos, costos y vida útil entre tecnologías energéticas mediante estructuras comparativas y superlativas."
            concepto_clave_latex: "\\Delta \\eta = \\eta_{\\text{new}} - \\eta_{\\text{baseline}}"
            ejemplo: "Comparación escrita en inglés entre turbinas hidráulicas Pelton, Francis y Kaplan según salto y eficiencia."
            bloque_estudio: "Bloque 25 min • Tablas comparativas con adjetivos técnicos"
          - numero: 3
            titulo: "Laboratory Safety & Engineering Quantities (Modals & Quantifiers)"
            objetivo: "Expresar obligaciones y recomendaciones de seguridad eléctrica usando verbos modales (must, should, have to)."
            concepto_clave_latex: "V_{\\text{safety}} \\le 50\\text{ V}_{\\text{AC}}"
            ejemplo: "Redacción de normas de seguridad PPE antes de energizar un banco de pruebas en el laboratorio."
            bloque_estudio: "Bloque 25 min • Protocolos de seguridad con modales de obligación"
          - numero: 4
            titulo: "Energy Forecasts & Project Schedules (Future Forms)"
            objetivo: "Describir planes de ingeniería, cronogramas de montaje y proyecciones energéticas con going to y will."
            concepto_clave_latex: "E_{\\text{proj}} = E_0 (1 + g)^n"
            ejemplo: "Presentación corta en inglés sobre la proyección de expansión solar y eólica para la próxima década."
            bloque_estudio: "Bloque 30 min • Redacción de metas y proyecciones futuras"
      - codigo: "03031818"
        nombre: "Probabilidad y Estadística"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero: 1
            titulo: "Estadística Descriptiva, Tendencia Central y Dispersión"
            objetivo: "Resumir series experimentales mediante media, mediana, varianza muestral, cuantiles y coeficiente de variación."
            concepto_clave_latex: "\\bar{x} = \\frac{1}{n}\\sum_{i=1}^{n} x_i \\quad ; \\quad s^2 = \\frac{1}{n-1}\\sum_{i=1}^{n}(x_i - \\bar{x})^2 \\quad ; \\quad \\text{CV} = \\frac{s}{\\bar{x}}"
            ejemplo: "Caracterización estadística de la variabilidad horaria y estacional de radiación solar global en Santa Marta."
            bloque_estudio: "Pomodoro 45/10 • Histogramas, boxplots y medidas de dispersión"
          - numero: 2
            titulo: "Axiomas de Probabilidad, Confiabilidad y Teorema de Bayes"
            objetivo: "Calcular probabilidades condicionales, confiabilidad de sistemas serie/paralelo y actualización bayesiana de riesgos."
            concepto_clave_latex: "P(A \\mid B) = \\frac{P(B \\mid A)P(A)}{\\sum_{j=1}^{k} P(B \\mid A_j)P(A_j)} \\quad ; \\quad R_{\\text{par}} = 1 - \\prod_{i=1}^{n}(1 - R_i)"
            ejemplo: "Evaluación de la disponibilidad probabilística de una planta con inversores redundantes en paralelo."
            bloque_estudio: "Pomodoro 50/10 • Árboles de probabilidad y sistemas redundantes"
          - numero: 3
            titulo: "Variables Aleatorias Discretas (Esperanza, Binomial y Poisson)"
            objetivo: "Modelar conteos de fallas y eventos discretos en ventanas de tiempo mediante distribuciones Binomial y de Poisson."
            concepto_clave_latex: "E[X] = \\sum_{x} x\\,p(x) \\quad ; \\quad P(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}"
            ejemplo: "Estimación de la probabilidad mensual de desconexiones por sobretensión atmosférica en un circuito de distribución."
            bloque_estudio: "Práctica 45 min • Problemas de tasa de llegadas de Poisson"
          - numero: 4
            titulo: "Distribuciones Continuas (Normal, Exponencial y Weibull) e Inferencia"
            objetivo: "Modelar recursos renovables continuos y tiempos de vida útil construyendo intervalos de confianza estadísticos."
            concepto_clave_latex: "f(v) = \\frac{k}{c}\\left(\\frac{v}{c}\\right)^{k-1} \\exp\\left[-\\left(\\frac{v}{c}\\right)^k\\right] \\quad ; \\quad \\bar{x} \\pm z_{\\alpha/2}\\frac{\\sigma}{\\sqrt{n}}"
            ejemplo: "Ajuste de la distribución de Weibull para estimar el potencial energético del viento en la costa Caribe."
            bloque_estudio: "Pomodoro 50/10 • Factores de forma/escala de Weibull y tabla Z"
      - codigo: "02031812"
        nombre: "Química Aplicada"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Estructura Atómica, Enlace Químico y Materiales para Energía"
            objetivo: "Relacionar la configuración electrónica y los enlaces iónico, covalente y metálico con semiconductores y conductores."
            concepto_clave_latex: "E_{\\text{fotón}} = h\\nu = \\frac{hc}{\\lambda} \\ge E_g"
            ejemplo: "Análisis del enlace covalente en redes de silicio dopado (tipo n y p) y su banda prohibida de 1.12 eV en celdas solares."
            bloque_estudio: "Pomodoro 45/10 • Propiedades periódicas y bandas electrónicas"
          - numero: 2
            titulo: "Estequiometría, Reactivo Límite y Balances de Combustión"
            objetivo: "Formular balances másicos y molares en reacciones químicas y procesos de combustión con aire teórico y en exceso."
            concepto_clave_latex: "\\text{CH}_4 + 2(\\text{O}_2 + 3.76\\text{N}_2) \\longrightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O} + 7.52\\text{N}_2"
            ejemplo: "Cálculo de la relación aire-combustible y masa de CO₂ emitida por cada metro cúbico de gas natural quemado."
            bloque_estudio: "Pomodoro 50/10 • Balance estequiométrico con exceso de aire"
          - numero: 3
            titulo: "Gases Ideales y Reales, Disoluciones y Equilibrio Químico"
            objetivo: "Aplicar ecuaciones de estado de gases, mezclas de Dalton, concentración molar y principio de Le Chatelier."
            concepto_clave_latex: "P V = n R T \\quad ; \\quad P_i = y_i P_{\\text{tot}} \\quad ; \\quad K_c = \\frac{[\\text{C}]^c[\\text{D}]^d}{[\\text{A}]^a[\\text{B}]^b}"
            ejemplo: "Determinación de la masa de hidrógeno comprimido almacenada en cilindros de alta presión y preparación de electrolitos KOH."
            bloque_estudio: "Práctica 45 min • Mezclas gaseosas, molaridad y pH"
          - numero: 4
            titulo: "Termoquímica (Ley de Hess), Poder Calorífico y Electroquímica"
            objetivo: "Calcular entalpías de reacción, poder calorífico superior/inferior y potenciales de celda mediante la ecuación de Nernst."
            concepto_clave_latex: "\\Delta H^\\circ_{\\text{rxn}} = \\sum \\nu_p \\Delta H^\\circ_{f,p} - \\sum \\nu_r \\Delta H^\\circ_{f,r} \\quad ; \\quad E_{\\text{celda}} = E^\\circ - \\frac{RT}{nF}\\ln Q"
            ejemplo: "Cálculo del poder calorífico inferior (PCI) de mezclas biogás-metano y tensión reversible en baterías y celdas galvánicas."
            bloque_estudio: "Pomodoro 50/10 • Ley de Hess, Faraday y ecuación de Nernst"

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
            titulo: "Antiderivadas, Integral Indefinida y Método de Sustitución"
            objetivo: "Reconstruir funciones primitivas a partir de sus tasas de variación mediante reglas directas y cambio de variable."
            concepto_clave_latex: "\\int f(g(x))\\,g'(x)\\,dx = \\int f(u)\\,du = F(g(x)) + C"
            ejemplo: "Determinación de la función de carga eléctrica q(t) a partir de una corriente transitoria exponencial i(t)."
            bloque_estudio: "Pomodoro 50/10 • Antiderivadas inmediatas y sustitución simple"
          - numero: 2
            titulo: "Técnicas de Integración: Por Partes, Trigonométricas y Fracciones Parciales"
            objetivo: "Resolver integrales analíticas de productos trascendentes, radicales cuadráticos y funciones racionales."
            concepto_clave_latex: "\\int u \\, dv = u \\cdot v - \\int v \\, du \\quad ; \\quad \\frac{P(x)}{(x-a)(x-b)} = \\frac{A}{x-a} + \\frac{B}{x-b}"
            ejemplo: "Integración analítica de una señal de potencia amortiguada P(t) = P₀·t·e^(-αt) durante una maniobra eléctrica."
            bloque_estudio: "Pomodoro 50/10 • 6 ejercicios mixtos por partes y fracciones parciales"
          - numero: 3
            titulo: "Integral Definida, Teorema Fundamental e Integración Numérica"
            objetivo: "Acumular magnitudes físicas aplicando el Teorema Fundamental del Cálculo y reglas numéricas de Trapecio y Simpson."
            concepto_clave_latex: "E = \\int_{t_1}^{t_2} P(t) \\, dt = F(t_2) - F(t_1) \\quad ; \\quad P_{\\text{prom}} = \\frac{1}{T}\\int_0^T P(t)\\,dt"
            ejemplo: "Integración de la curva diaria de demanda eléctrica (y regla de Simpson sobre lecturas horarias) para obtener MWh consumidos."
            bloque_estudio: "Práctica 45 min • Valor medio, TFC y regla de Simpson 1/3"
          - numero: 4
            titulo: "Aplicaciones Geométricas y Físicas: Áreas, Volúmenes y Trabajo de Bombeo"
            objetivo: "Calcular áreas entre curvas, volúmenes de revolución, centros de masa y trabajo mecánico de vaciado de tanques."
            concepto_clave_latex: "V = \\pi \\int_a^b \\left([R(x)]^2 - [r(x)]^2\\right)dx \\quad ; \\quad W_{\\text{bombeo}} = \\rho g \\int_a^b A(y)(H - y)\\,dy"
            ejemplo: "Cálculo de la energía mínima requerida para bombear la totalidad del agua desde un reservorio subterráneo hacia una torre."
            bloque_estudio: "Pomodoro 50/10 • Sólidos de revolución y trabajo hidrostático"
          - numero: 5
            titulo: "Integrales Impropias, Sucesiones y Series de Taylor"
            objetivo: "Analizar convergencia de integrales con límites infinitos y aproximar funciones mediante desarrollos en serie de potencias."
            concepto_clave_latex: "\\int_a^\\infty f(x)\\,dx = \\lim_{b \\to \\infty}\\int_a^b f(x)\\,dx \\quad ; \\quad f(x) = \\sum_{n=0}^{\\infty}\\frac{f^{(n)}(a)}{n!}(x-a)^n"
            ejemplo: "Evaluación de energía total disipada en horizonte infinito y linealización por serie de Taylor de radiación térmica."
            bloque_estudio: "Práctica 45 min • Criterios de convergencia y polinomios de Taylor"
      - codigo: "02021811"
        nombre: "Calor y Ondas"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Elasticidad y Mecánica de Fluidos Ideal (Arquímedes y Bernoulli)"
            objetivo: "Estudiar deformación elástica en sólidos, hidrostática, flotación y conservación de energía en líneas de corriente."
            concepto_clave_latex: "P = P_0 + \\rho g h \\quad ; \\quad A_1 v_1 = A_2 v_2 \\quad ; \\quad P + \\frac{1}{2}\\rho v^2 + \\rho g y = \\text{cte}"
            ejemplo: "Cálculo del empuje hidrostático sobre estructuras flotantes para paneles solares (floating PV) y caudal en tuberías Venturi."
            bloque_estudio: "Pomodoro 50/10 • Manometría, Arquímedes y tubo de Venturi"
          - numero: 2
            titulo: "Termometría, Dilatación Térmica, Calorimetría y Conducción"
            objetivo: "Cuantificar expansiones térmicas, intercambios de calor sensible/latente y mecanismos básicos de transferencia térmica."
            concepto_clave_latex: "\\Delta L = \\alpha L_0 \\Delta T \\quad ; \\quad Q = m c \\Delta T + m L_f \\quad ; \\quad \\dot{Q} = -k A \\frac{\\Delta T}{\\Delta x}"
            ejemplo: "Cálculo del equilibrio térmico en un tanque de almacenamiento solar con material de cambio de fase (PCM)."
            bloque_estudio: "Pomodoro 50/10 • Balances calorimétricos con cambio de fase"
          - numero: 3
            titulo: "Teoría Cinética de los Gases y Primera Ley en Procesos Ideales"
            objetivo: "Conectar variables microscópicas moleculares con presión, temperatura interna y trabajo en procesos termodinámicos."
            concepto_clave_latex: "v_{\\text{rms}} = \\sqrt{\\frac{3 R T}{M}} \\quad ; \\quad \\Delta E_{\\text{int}} = Q - W \\quad ; \\quad P V^\\gamma = \\text{cte}"
            ejemplo: "Determinación del calor, trabajo y cambio de energía interna en expansiones isotérmicas y adiabáticas de un gas ideal."
            bloque_estudio: "Práctica 45 min • Diagramas P-V y procesos politrópicos"
          - numero: 4
            titulo: "Movimiento Armónico Simple (MAS), Ondas Mecánicas y Acústica"
            objetivo: "Modelar osciladores armónicos, ecuación de onda viajera, ondas estacionarias, resonancia y niveles sonoros en decibeles."
            concepto_clave_latex: "\\frac{\\partial^2 y}{\\partial x^2} = \\frac{1}{v^2}\\frac{\\partial^2 y}{\\partial t^2} \\quad ; \\quad \\omega_0 = \\sqrt{\\frac{k}{m}} \\quad ; \\quad \\beta = 10\\log_{10}\\left(\\frac{I}{I_0}\\right)"
            ejemplo: "Evaluación de frecuencias naturales de vibración en góndolas eólicas y atenuación acústica ambiental en decibeles."
            bloque_estudio: "Pomodoro 50/10 • Ecuación de onda, efecto Doppler y decibeles"
      - codigo: "03041820"
        nombre: "Fundamentos de Electricidad II"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Régimen Sinusoidal, Fasores e Impedancia Compleja"
            objetivo: "Resolver circuitos RLC en corriente alterna estacionaria utilizando álgebra fasorial, impedancia y admitancia."
            concepto_clave_latex: "\\mathbf{Z} = R + j\\left(\\omega L - \\frac{1}{\\omega C}\\right) \\quad ; \\quad \\mathbf{V}_{\\text{rms}} = \\mathbf{Z}\\cdot\\mathbf{I}_{\\text{rms}}"
            ejemplo: "Determinación de magnitud y ángulo de fase de la corriente absorbida por un motor monofásico inductivo a 60 Hz."
            bloque_estudio: "Pomodoro 45/10 • Conversión dominio temporal a fasorial y mallas AC"
          - numero: 2
            titulo: "Potencia Compleja, Triángulo de Potencias y Factor de Potencia"
            objetivo: "Calcular potencia activa, reactiva y aparente, y dimensionar bancos de capacitores para compensación reactiva."
            concepto_clave_latex: "\\mathbf{S} = P + jQ = \\mathbf{V}_{\\text{rms}} \\mathbf{I}_{\\text{rms}}^* \\quad ; \\quad \\text{FP} = \\cos(\\theta_v - \\theta_i) \\quad ; \\quad Q_C = P(\\tan\\theta_1 - \\tan\\theta_2)"
            ejemplo: "Dimensionamiento de un banco de capacitores para elevar el factor de potencia industrial de 0.82 a 0.96 inductivo evitando penalización."
            bloque_estudio: "Práctica Activa 45 min • Triángulo de potencias y compensación kVAr"
          - numero: 3
            titulo: "Sistemas Trifásicos Equilibrados (Estrella Y y Triángulo Delta)"
            objetivo: "Analizar relaciones entre magnitudes de línea y de fase en generadores y cargas conectadas en estrella y delta."
            concepto_clave_latex: "V_L = \\sqrt{3}\\,V_f \\quad ; \\quad I_L = \\sqrt{3}\\,I_f \\quad ; \\quad P_{3\\phi} = \\sqrt{3}\\,V_L I_L \\cos\\theta"
            ejemplo: "Cálculo de corrientes de línea y potencia entregada por un inversor solar trifásico de 100 kW a una barra de 440 V."
            bloque_estudio: "Pomodoro 50/10 • Equivalente monofásico y cargas Y-Delta"
          - numero: 4
            titulo: "Resonancia Eléctrica, Filtros Pasivos y Circuitos Acoplados"
            objetivo: "Analizar la respuesta en frecuencia, resonancia serie/paralelo e inductancia mutua en transformadores ideales y lineales."
            concepto_clave_latex: "\\omega_0 = \\frac{1}{\\sqrt{LC}} \\quad ; \\quad \\frac{V_2}{V_1} = \\frac{N_2}{N_1} \\quad ; \\quad Z_{\\text{in}} = \\left(\\frac{N_1}{N_2}\\right)^2 Z_L"
            ejemplo: "Diseño de un filtro LC sintonizado y reflexión de impedancia a través de un transformador elevador de acoplamiento."
            bloque_estudio: "Práctica 40 min • Regla de los puntos y resonancia RLC"
      - codigo: "03021815"
        nombre: "Fundamentos de Hidráulica y Neumática"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Propiedades de Fluidos de Potencia y Principio de Pascal"
            objetivo: "Evaluar viscosidad, compresibilidad y multiplicación hidrostática de fuerzas en circuitos óleo-hidráulicos y neumáticos."
            concepto_clave_latex: "P = \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\quad ; \\quad \\nu = \\frac{\\mu}{\\rho}"
            ejemplo: "Cálculo de la presión manométrica y ventaja mecánica en una prensa hidráulica de mantenimiento electromecánico."
            bloque_estudio: "Pomodoro 45/10 • Unidades de presión (bar, MPa, psi) y viscosidad ISO"
          - numero: 2
            titulo: "Bombas Oleohidráulicas, Compresores y Unidad FRL"
            objetivo: "Dimensionar bombas de desplazamiento positivo y compresores de aire cuantificando potencia fluida y eficiencias."
            concepto_clave_latex: "Q_{\\text{real}} = V_d \\cdot n \\cdot \\eta_v \\quad ; \\quad N_{\\text{hid}} = \\Delta P \\cdot Q \\quad ; \\quad N_{\\text{eje}} = \\frac{\\Delta P \\cdot Q}{\\eta_{\\text{tot}}}"
            ejemplo: "Cálculo de la potencia eléctrica requerida por la central hidráulica de frenos y orientación (yaw) de un aerogenerador."
            bloque_estudio: "Pomodoro 50/10 • Curvas de bombas, cavitación y preparación de aire FRL"
          - numero: 3
            titulo: "Actuadores Lineales (Cilindros) y Motores Hidráulicos/Neumáticos"
            objetivo: "Determinar fuerzas efectivas de extensión y retracción, caudales requeridos y par torsional en actuadores."
            concepto_clave_latex: "F_{\\text{av}} = P \\frac{\\pi D^2}{4}\\eta_m \\quad ; \\quad F_{\\text{ret}} = P \\frac{\\pi(D^2 - d^2)}{4}\\eta_m \\quad ; \\quad \\tau = \\frac{\\Delta P \\cdot V_d}{2\\pi}"
            ejemplo: "Dimensionamiento del diámetro de émbolo del cilindro hidráulico para el sistema de pitch de palas eólicas."
            bloque_estudio: "Práctica 45 min • Selección comercial de cilindros y verificación de pandeo"
          - numero: 4
            titulo: "Válvulas de Control (ISO 1219) y Circuitos Electro-Hidráulicos"
            objetivo: "Diseñar esquemas con válvulas direccionales, limitadoras de presión, antirretorno y reguladoras de caudal."
            concepto_clave_latex: "Q = C_d A_o \\sqrt{\\frac{2\\,\\Delta P}{\\rho}}"
            ejemplo: "Diseño del circuito electro-hidráulico con válvula de contrabalance para seguidores solares (solar trackers) de gran escala."
            bloque_estudio: "Pomodoro 50/10 • Simbología ISO 1219 y secuencias A+ B+ A- B-"
      - codigo: "01021804"
        nombre: "General English III"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Engineering Progress & Achievements (Present Perfect)"
            objetivo: "Reportar avances de implementación, resultados acumulados y experiencias técnicas empleando el Present Perfect (MCER B1.1)."
            concepto_clave_latex: "\\text{Completion}(\\%) = \\frac{\\text{Installed kW}}{\\text{Planned kW}} \\times 100\\%"
            ejemplo: "Informe de progreso de obra (The engineering team has commissioned twelve string inverters since Monday)."
            bloque_estudio: "Bloque 25 min • Contraste Present Perfect vs. Past Simple"
          - numero: 2
            titulo: "Passive Voice in Technical Manuals & Commissioning Protocols"
            objetivo: "Redactar procedimientos de laboratorio y manuales de mantenimiento enfatizando el proceso mediante la voz pasiva."
            concepto_clave_latex: "\\text{Efficiency}(\\%) = \\left(\\frac{P_{\\text{out}}}{P_{\\text{in}}}\\right) \\times 100\\%"
            ejemplo: "Interpretación y redacción de protocolos de puesta en marcha de inversores solares en inglés técnico."
            bloque_estudio: "Bloque 25 min • Transformación activa-pasiva en manuales O&M"
          - numero: 3
            titulo: "System Contingencies & Cause-Effect (Conditionals 0, 1 & 2)"
            objetivo: "Formular leyes físicas, lógicas de protección y escenarios hipotéticos de operación usando oraciones condicionales."
            concepto_clave_latex: "f < 59.5\\text{ Hz} \\implies \\text{Under-Frequency Relay Trips}"
            ejemplo: "Descripción de protecciones eléctricas (If grid voltage exceeds the upper threshold, the inverter disconnects automatically)."
            bloque_estudio: "Bloque 30 min • Condicionales aplicados a diagnósticos de planta"
          - numero: 4
            titulo: "Component Specifications & Definitions (Relative Clauses)"
            objetivo: "Definir instrumentos, sensores y arquitecturas energéticas con precisión formal mediante cláusulas relativas."
            concepto_clave_latex: "G_{\\text{POA}} = G_b \\cos\\theta_i + G_d\\left(\\frac{1+\\cos\\beta}{2}\\right) + \\rho G_h\\left(\\frac{1-\\cos\\beta}{2}\\right)"
            ejemplo: "Definición técnica formal (A pyranometer is a sensor which measures broadband solar irradiance on a planar surface)."
            bloque_estudio: "Bloque 25 min • Redacción de glosarios de instrumentación en inglés"

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
            titulo: "Sistemas de Ecuaciones Lineales, Matrices y Gauss-Jordan"
            objetivo: "Resolver sistemas lineales de múltiples variables mediante reducción escalonada, álgebra matricial y matriz inversa."
            concepto_clave_latex: "A\\vec{x} = \\vec{b} \\quad ; \\quad A A^{-1} = I \\quad ; \\quad \\mathbf{Y}_{\\text{bus}}\\mathbf{V} = \\mathbf{I}"
            ejemplo: "Formulación y solución del sistema matricial de tensiones nodales en una red eléctrica de distribución de 4 barras."
            bloque_estudio: "Pomodoro 50/10 • Eliminación Gauss-Jordan y factorización LU"
          - numero: 2
            titulo: "Determinantes, Propiedades e Invertibilidad de Sistemas"
            objetivo: "Calcular determinantes por cofactores y operaciones de fila para analizar unicidad de soluciones y matrices Jacobianas."
            concepto_clave_latex: "\\det(A) = \\sum_{j=1}^{n}(-1)^{1+j} a_{1j} M_{1j} \\quad ; \\quad \\det(A) \\neq 0 \\iff A \\text{ es invertible}"
            ejemplo: "Verificación de invertibilidad de la matriz Jacobiana durante una iteración de flujo de potencia."
            bloque_estudio: "Práctica 40 min • Cofactores, regla de Cramer y matriz adjunta"
          - numero: 3
            titulo: "Espacios Vectoriales, Bases, Ortogonalidad y Mínimos Cuadrados"
            objetivo: "Determinar independencia lineal, dimensión, bases ortonormales (Gram-Schmidt) y proyecciones por mínimos cuadrados."
            concepto_clave_latex: "\\vec{u}\\cdot\\vec{v} = \\|\\vec{u}\\|\\|\\vec{v}\\|\\cos\\theta \\quad ; \\quad \\hat{x} = (A^T A)^{-1}A^T\\vec{b}"
            ejemplo: "Estimación matricial por mínimos cuadrados de los coeficientes de pérdida térmica de una edificación a partir de mediciones."
            bloque_estudio: "Pomodoro 50/10 • Independencia lineal y ajuste por mínimos cuadrados"
          - numero: 4
            titulo: "Transformaciones Lineales, Valores Propios y Diagonalización"
            objetivo: "Calcular autovalores y autovectores del polinomio característico para desacoplar sistemas dinámicos y analizar estabilidad."
            concepto_clave_latex: "A\\vec{v} = \\lambda\\vec{v} \\quad ; \\quad \\det(A - \\lambda I) = 0 \\quad ; \\quad A = P D P^{-1}"
            ejemplo: "Evaluación de modos oscilatorios y estabilidad dinámica de un sistema energético linealizado mediante el espectro de autovalores."
            bloque_estudio: "Pomodoro 50/10 • Polinomio característico, autovectores y diagonalización"
      - codigo: "06011837"
        nombre: "Conversión de Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Rutas de Transformación Energética y Rendimiento Exergético"
            objetivo: "Evaluar cadenas de conversión termo-mecánica, electromecánica y electroquímica bajo primera y segunda ley."
            concepto_clave_latex: "\\eta_I = \\frac{\\dot{E}_{\\text{útil}}}{\\dot{E}_{\\text{entrada}}} \\quad ; \\quad \\eta_{II} = 1 - \\frac{\\dot{E}_{\\text{destruida}}}{\\dot{\\Psi}_{\\text{entrada}}}"
            ejemplo: "Comparación de eficiencia de primera y segunda ley entre un motor de combustión, una turbina y una celda de combustible."
            bloque_estudio: "Pomodoro 45/10 • Matriz de acoplamiento entre dominios energéticos"
          - numero: 2
            titulo: "Circuitos Magnéticos, Curva B-H y Pérdidas en Núcleos Ferromagnéticos"
            objetivo: "Resolver circuitos magnéticos con entrehierro mediante reluctancias y cuantificar pérdidas por histéresis y Foucault."
            concepto_clave_latex: "\\mathcal{F} = N I = \\Phi \\mathcal{R} \\quad ; \\quad \\mathcal{R} = \\frac{l}{\\mu_r \\mu_0 A} \\quad ; \\quad P_{\\text{Fe}} = k_h f B_{\\max}^n + k_e f^2 B_{\\max}^2"
            ejemplo: "Cálculo de los amperios-vuelta requeridos para producir un flujo magnético de diseño en el entrehierro de un inductor de potencia."
            bloque_estudio: "Pomodoro 50/10 • Ley de Hopkinson y núcleos con entrehierro"
          - numero: 3
            titulo: "Principios de Conversión Electromecánica: Energía y Coenergía"
            objetivo: "Modelar fuerzas traslacionales y pares electromagnéticos en transductores y máquinas a partir de la coenergía magnética."
            concepto_clave_latex: "dW_{\\text{eléc}} = dW_{\\text{campo}} + dW_{\\text{mec}} \\quad ; \\quad \\tau_e = \\frac{\\partial W'(\\theta, i)}{\\partial \\theta}"
            ejemplo: "Cálculo del par electromagnético desarrollado en función del ángulo rotor en un actuador de reluctancia variable."
            bloque_estudio: "Pomodoro 50/10 • Balance diferencial de energía y coenergía magnética"
          - numero: 4
            titulo: "Conversión Directa: Termoeléctrica (Seebeck), Fotovoltaica y Química"
            objetivo: "Analizar mecanismos de conversión directa sin partes móviles basados en efectos termoeléctricos, fotoeléctricos y Gibbs."
            concepto_clave_latex: "V_{\\text{oc}} = \\alpha_{AB}(T_H - T_C) \\quad ; \\quad ZT = \\frac{\\alpha^2 \\sigma}{\\kappa}T \\quad ; \\quad W_{\\text{eléc,máx}} = -\\Delta G"
            ejemplo: "Estimación de la potencia recuperada con módulos termoeléctricos (TEG) instalados sobre un ducto de gases de escape."
            bloque_estudio: "Práctica 45 min • Efecto Seebeck-Peltier y límite de energía libre de Gibbs"
      - codigo: "03041821"
        nombre: "Electricidad y Magnetismo"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero: 1
            titulo: "Carga Eléctrica, Campo Electrostático, Coulomb y Ley de Gauss"
            objetivo: "Determinar campos eléctricos producidos por distribuciones discretas y continuas de carga empleando integración y simetría."
            concepto_clave_latex: "\\vec{E} = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{r^2}\\hat{r} \\quad ; \\quad \\oint_S \\vec{E} \\cdot d\\vec{A} = \\frac{q_{\\text{enc}}}{\\varepsilon_0}"
            ejemplo: "Cálculo del gradiente de campo eléctrico en la superficie de un conductor cilíndrico de transmisión para prevenir efecto corona."
            bloque_estudio: "Pomodoro 50/10 • Superficies gaussianas esféricas, cilíndricas y planas"
          - numero: 2
            titulo: "Potencial Eléctrico, Capacitancia, Dieléctricos y Energía Electrostática"
            objetivo: "Calcular diferencias de potencial, capacitancia equivalente y densidad de energía almacenada en medios dieléctricos."
            concepto_clave_latex: "V_B - V_A = -\\int_A^B \\vec{E}\\cdot d\\vec{l} \\quad ; \\quad C = \\kappa\\varepsilon_0\\frac{A}{d} \\quad ; \\quad u_E = \\frac{1}{2}\\varepsilon E^2"
            ejemplo: "Dimensionamiento dieléctrico y energía almacenada en bancos de supercapacitores para soporte transitorio de tensión."
            bloque_estudio: "Pomodoro 50/10 • Potencial continuo y condensadores con dieléctrico"
          - numero: 3
            titulo: "Densidad de Corriente, Ley de Ohm Microscópica y Efecto Térmico"
            objetivo: "Relacionar campo eléctrico, velocidad de deriva, conductividad y dependencia térmica de la resistividad en conductores."
            concepto_clave_latex: "\\vec{J} = \\sigma\\vec{E} \\quad ; \\quad R = \\rho\\frac{L}{A} \\quad ; \\quad \\rho(T) = \\rho_0[1 + \\alpha(T - T_0)]"
            ejemplo: "Cálculo del aumento de resistencia óhmica en un conductor de aluminio ACSR operando a 75 °C bajo alta radiación solar."
            bloque_estudio: "Práctica 40 min • Conducción microscópica y variación térmica de R"
          - numero: 4
            titulo: "Campo Magnético, Fuerza de Lorentz, Biot-Savart y Ley de Ampère"
            objetivo: "Analizar fuerzas magnéticas sobre cargas y conductores, y calcular campos generados por corrientes estacionarias."
            concepto_clave_latex: "\\vec{F}_B = q\\vec{v}\\times\\vec{B} + I\\vec{L}\\times\\vec{B} \\quad ; \\quad \\oint_C \\vec{B}\\cdot d\\vec{l} = \\mu_0 I_{\\text{enc}}"
            ejemplo: "Cálculo de esfuerzos electrodinámicos entre barras colectoras paralelas de una subestación ante corrientes de falla."
            bloque_estudio: "Pomodoro 50/10 • Biot-Savart en espiras y Ley de Ampère en solenoides"
          - numero: 5
            titulo: "Inducción de Faraday-Lenz, Inductancia y Ecuaciones de Maxwell"
            objetivo: "Cuantificar fuerzas electromotrices inducidas, autoinductancia, energía magnética y la corriente de desplazamiento de Maxwell."
            concepto_clave_latex: "\\mathcal{E} = -N\\frac{d\\Phi_B}{dt} \\quad ; \\quad u_B = \\frac{B^2}{2\\mu_0} \\quad ; \\quad \\oint_C \\vec{B}\\cdot d\\vec{l} = \\mu_0 I + \\mu_0\\varepsilon_0\\frac{d\\Phi_E}{dt}"
            ejemplo: "Deducción de la fem sinusoidal inducida en el estator de un generador síncrono a partir de un campo magnético rotatorio."
            bloque_estudio: "Pomodoro 50/10 • Ley de Faraday-Lenz y síntesis de Maxwell"
      - codigo: "01021805"
        nombre: "General English IV"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero: 1
            titulo: "Synthesizing Energy Literature (Reported Speech & Citations)"
            objetivo: "Parafrasear hallazgos científicos, normativas e informes internacionales empleando Reported Speech (MCER B1.2)."
            concepto_clave_latex: "\\text{CF}(\\%) = \\frac{E_{\\text{annual}}}{P_{\\text{rated}} \\cdot 8760\\text{ h}} \\times 100\\%"
            ejemplo: "Síntesis bibliográfica en inglés de reportes anuales de IRENA e IEA sobre factores de planta renovables."
            bloque_estudio: "Bloque 25 min • Parafraseo académico y verbos de reporte"
          - numero: 2
            titulo: "Writing Structured Abstracts for Engineering Papers"
            objetivo: "Redactar resúmenes científicos (Background, Methods, Results, Conclusions) con cohesión y estilo académico formal."
            concepto_clave_latex: "e_{\\text{rel}}(\\%) = \\left|\\frac{y_{\\text{sim}} - y_{\\text{exp}}}{y_{\\text{exp}}}\\right| \\times 100\\%"
            ejemplo: "Escritura de un Abstract de 180 palabras para presentar un estudio de micro-redes solares en un congreso estudiantil."
            bloque_estudio: "Bloque 30 min • Redacción de Abstract de 5 movimientos retóricos"
          - numero: 3
            titulo: "Interpreting Load Curves, Sensitivity Graphs & ROI Metrics"
            objetivo: "Exponer tendencias cuantitativas, curvas de demanda y métricas de viabilidad técnica-económica en inglés."
            concepto_clave_latex: "\\text{ROI} = \\frac{\\text{Net Benefit}}{\\text{Total Cost}} \\times 100\\%"
            ejemplo: "Descripción oral y escrita de curvas de carga horaria (duck curve) y análisis de retorno de inversión."
            bloque_estudio: "Bloque 25 min • Vocabulario de tendencias y lectura de gráficas"
          - numero: 4
            titulo: "Academic Presentations, Technical Pitch & Q&A Defense"
            objetivo: "Sustentar proyectos de ingeniería en inglés con fluidez argumentativa y manejo solvente de preguntas técnicas."
            concepto_clave_latex: "\\text{Payback} = \\frac{\\text{CAPEX}}{\\text{Annual Net Savings}}"
            ejemplo: "Presentación oral de 5 minutos defendiendo la factibilidad de una micro-red híbrida solar-almacenamiento."
            bloque_estudio: "Bloque 30 min • Práctica de pronunciación, estructura de pitch y Q&A"
      - codigo: "03021817"
        nombre: "Termodinámica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero: 1
            titulo: "Conceptos Básicos y Propiedades de las Sustancias Puras"
            objetivo: "Identificar estados de equilibrio, fases líquido-vapor, título de calidad y propiedades en tablas termodinámicas y gases."
            concepto_clave_latex: "h = h_f + x\\,h_{fg} \\quad ; \\quad v = v_f + x(v_g - v_f) \\quad ; \\quad P v = Z R T"
            ejemplo: "Interpolación en tablas de vapor sobrecalentado y mezcla saturada para caracterizar el fluido de trabajo en una caldera."
            bloque_estudio: "Pomodoro 50/10 • Manejo de tablas de agua/R134a y diagramas P-v / T-v"
          - numero: 2
            titulo: "Primera Ley de la Termodinámica en Sistemas Cerrados"
            objetivo: "Evaluar trabajo de frontera móvil, transferencia de calor y variaciones de energía interna y entalpía en masa fija."
            concepto_clave_latex: "Q - W = \\Delta U + \\Delta E_c + \\Delta E_p \\quad ; \\quad W_b = \\int_1^2 P\\,dV \\quad ; \\quad \\Delta u = c_v \\Delta T"
            ejemplo: "Cálculo del trabajo de compresión politrópica y transferencia de calor en un conjunto cilindro-émbolo."
            bloque_estudio: "Pomodoro 50/10 • Balances de energía en sistemas cerrados y calores específicos"
          - numero: 3
            titulo: "Primera Ley en Volúmenes de Control (Flujo Estacionario)"
            objetivo: "Aplicar conservación de masa y energía en turbinas, compresores, bombas, toberas e intercambiadores de calor."
            concepto_clave_latex: "\\dot{Q}_{vc} - \\dot{W}_{vc} = \\sum \\dot{m}_s\\left(h_s + \\frac{v_s^2}{2} + gz_s\\right) - \\sum \\dot{m}_e\\left(h_e + \\frac{v_e^2}{2} + gz_e\\right)"
            ejemplo: "Determinación de la potencia generada por una turbina de vapor adiabática y caudal de agua de enfriamiento en el condensador."
            bloque_estudio: "Pomodoro 50/10 • Dispositivos de flujo estacionario (turbinas y compresores)"
          - numero: 4
            titulo: "Segunda Ley de la Termodinámica, Entropía y Eficiencia Isentrópica"
            objetivo: "Analizar máquinas térmicas, límite de Carnot, balance de generación de entropía y eficiencias isentrópicas reales."
            concepto_clave_latex: "\\eta_{\\text{Carnot}} = 1 - \\frac{T_L}{T_H} \\quad ; \\quad \\dot{S}_{\\text{gen}} = \\sum \\dot{m}_s s_s - \\sum \\dot{m}_e s_e - \\sum \\frac{\\dot{Q}_k}{T_k} \\ge 0 \\quad ; \\quad \\eta_{s,T} = \\frac{h_1 - h_{2a}}{h_1 - h_{2s}}"
            ejemplo: "Cálculo de la eficiencia isentrópica e irreversibilidades en una turbina de gas y en una bomba de alimentación."
            bloque_estudio: "Práctica Activa 50 min • Diagramas T-s, relaciones Tds y eficiencias isentrópicas"
          - numero: 5
            titulo: "Ciclos de Potencia (Rankine, Brayton, Otto/Diesel) y Refrigeración"
            objetivo: "Modelar y optimizar ciclos termodinámicos de generación eléctrica a vapor y gas, así como sistemas de refrigeración."
            concepto_clave_latex: "\\eta_{\\text{Rankine}} = \\frac{w_{\\text{turb}} - w_{\\text{bomba}}}{q_{\\text{entrada}}} \\quad ; \\quad \\eta_{\\text{Brayton}} = 1 - \\frac{1}{r_p^{(k-1)/k}} \\quad ; \\quad \\text{COP}_R = \\frac{q_L}{w_{\\text{comp}}}"
            ejemplo: "Determinación de la potencia neta y eficiencia térmica de un ciclo Rankine con sobrecalentamiento y recalentamiento."
            bloque_estudio: "Pomodoro 50/10 • Análisis completo de ciclo Rankine real y ciclo Brayton"

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
* **Tema 1: Funciones Reales, Dominio, Composición e Inversas**
  * **Objetivo:** Modelar relaciones entre variables físicas mediante funciones algebraicas, exponenciales, logarítmicas y trigonométricas.
  * **Concepto Clave:**
    $$(f \circ g)(x) = f(g(x)) \quad ; \quad f^{-1}(f(x)) = x \quad ; \quad P(T) = P_0 e^{\beta(T - T_{\text{STC}})}$$
  * **Ejemplo:** Modelado de la variación de potencia de un módulo solar en función de la temperatura de celda.
* **Tema 2: Límites Laterales, Indeterminaciones y Asíntotas**
  * **Objetivo:** Analizar el comportamiento local y asintótico de funciones reales mediante definición formal y álgebra de límites.
  * **Concepto Clave:**
    $$\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$
  * **Ejemplo:** Determinación del régimen estacionario asintótico de enfriamiento de un transformador cuando el tiempo tiende a infinito.
* **Tema 3: Continuidad Puntual y Teorema del Valor Intermedio**
  * **Objetivo:** Evaluar la continuidad en puntos e intervalos cerrados para garantizar existencia de raíces en modelos físicos.
  * **Concepto Clave:**
    $$\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c) \quad ; \quad f(a) < N < f(b) \implies \exists c \in (a,b) : f(c) = N$$
  * **Ejemplo:** Análisis de continuidad por tramos en la curva de potencia de un aerogenerador entre velocidad de arranque y nominal.
* **Tema 4: La Derivada, Regla de la Cadena y Derivación Implícita**
  * **Objetivo:** Calcular tasas de cambio instantáneas aplicando reglas de derivación, regla de la cadena y derivadas de orden superior.
  * **Concepto Clave:**
    $$f'(x) = \lim_{h \to 0}\frac{f(x+h)-f(x)}{h} \quad ; \quad \frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$
  * **Ejemplo:** Obtención de la potencia instantánea P(t) = dE/dt entregada por un sistema de almacenamiento a partir de su energía acumulada.
* **Tema 5: Razones de Cambio, Regla de L'Hôpital y Optimización**
  * **Objetivo:** Aplicar criterios de primera y segunda derivada para determinar extremos absolutos y optimizar diseños de ingeniería.
  * **Concepto Clave:**
    $$f'(x_c) = 0 \; \land \; f''(x_c) < 0 \implies x_c \text{ es máximo} \quad ; \quad \lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}$$
  * **Ejemplo:** Cálculo del ángulo de inclinación óptimo para maximizar la irradiancia solar anual captada por un colector.

### 2. Fundamentos de Programación e IA (`03011813`)
* **Categoría:** `PROGRAMACION_IA` • **Créditos:** `4` • **Color UI:** `#0A84FF`
* **Tema 1: Pensamiento Computacional, Algoritmos y Tipos de Datos**
  * **Objetivo:** Representar soluciones estructuradas mediante pseudocódigo, diagramas de flujo, variables y expresiones lógicas.
  * **Concepto Clave:**
    $$y = (A \land B) \lor (\neg C) \quad ; \quad E_{\text{kWh}} = \frac{P_{\text{W}} \cdot \Delta t_{\text{h}}}{1000}$$
  * **Ejemplo:** Algoritmo secuencial en Python para convertir lecturas crudas de potencia y tiempo a consumo facturable en kWh.
* **Tema 2: Estructuras de Control Condicionales, Ciclos y Complejidad**
  * **Objetivo:** Diseñar bloques selectivos e iterativos eficientes evaluando su complejidad temporal asintótica.
  * **Concepto Clave:**
    $$T(n) = \mathcal{O}(n \log n) \quad ; \quad \bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$$
  * **Ejemplo:** Script iterativo en Python para filtrar registros nocturnos nulos y promediar series horarias de irradiancia solar.
* **Tema 3: Modularidad, Funciones, Vectores y Matrices Numéricas**
  * **Objetivo:** Construir subprogramas reutilizables y procesar arreglos unidimensionales y bidimensionales de mediciones.
  * **Concepto Clave:**
    $$E_{\text{total}} = \sum_{i=1}^{m}\sum_{j=1}^{n} P_{ij}\,\Delta t \quad ; \quad P_k = V_k \cdot I_k$$
  * **Ejemplo:** Procesamiento matricial con NumPy del despacho horario de 5 plantas solares durante los 30 días del mes.
* **Tema 4: Preprocesamiento y Análisis Exploratorio de Datos Energéticos**
  * **Objetivo:** Limpiar series de tiempo, tratar valores atípicos y escalar variables para algoritmos de inteligencia artificial.
  * **Concepto Clave:**
    $$x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \quad ; \quad z = \frac{x - \mu}{\sigma}$$
  * **Ejemplo:** Normalización Min-Max y estandarización Z-score de temperatura, humedad y velocidad de viento de una estación meteorológica.
* **Tema 5: Introducción a Machine Learning y Regresión Lineal**
  * **Objetivo:** Entrenar y evaluar modelos supervisados básicos de regresión para pronosticar demanda energética.
  * **Concepto Clave:**
    $$\hat{y} = w_1 x + w_0 \quad ; \quad \text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
  * **Ejemplo:** Predicción del consumo eléctrico diario de un campus universitario en función de la temperatura ambiente.

### 3. General English I (`01021802`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Academic Profiles & Introductions (Verb To Be & Pronouns)**
  * **Objetivo:** Presentar información personal, institucional y perfiles de ingeniería empleando el verbo to be y posesivos (MCER A1).
  * **Concepto Clave:**
    $$\text{Subject} + \text{am / is / are} + \text{Complement}$$
  * **Ejemplo:** Presentación oral y escrita como estudiante de Energy Engineering en un encuentro internacional de semilleros.
* **Tema 2: Technical Vocabulary, SI Units & Datasheets**
  * **Objetivo:** Comprender fichas técnicas de equipos energéticos, cifras y magnitudes del Sistema Internacional en inglés.
  * **Concepto Clave:**
    $$P_{\text{rated}} = V_{\text{nom}} \cdot I_{\text{nom}} \quad ; \quad 1\text{ MW} = 10^6\text{ W}$$
  * **Ejemplo:** Lectura e interpretación de parámetros nominales (Rated Power, Open-Circuit Voltage) en un datasheet fotovoltaico.
* **Tema 3: Engineering Routines & Facts (Present Simple)**
  * **Objetivo:** Describir rutinas de operación, horarios de mantenimiento y leyes físicas permanentes con el Present Simple.
  * **Concepto Clave:**
    $$f_{\text{grid}} = 60\text{ Hz} \quad ; \quad T_{\text{cycle}} = \frac{1}{f_{\text{grid}}}$$
  * **Ejemplo:** Redacción en inglés de la rutina diaria de inspección técnica de un cuarto de inversores solares.
* **Tema 4: Live Plant Monitoring (Present Continuous & Prepositions)**
  * **Objetivo:** Reportar acciones en progreso, ubicación de instrumentos y variaciones en tiempo real dentro del laboratorio.
  * **Concepto Clave:**
    $$\Delta P(t) = P_{\text{gen}}(t) - P_{\text{load}}(t)$$
  * **Ejemplo:** Descripción en vivo del flujo de potencia en sala de control (The solar array is charging the battery bank now).

### 4. Introducción a la Ingeniería Energética (`04011822`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Formas de Energía, Sistemas de Unidades y Perfil Profesional**
  * **Objetivo:** Diferenciar energía primaria, secundaria, final y útil dominando las equivalencias energéticas internacionales.
  * **Concepto Clave:**
    $$1\text{ kWh} = 3.6\text{ MJ} \quad ; \quad 1\text{ TEP} = 41.868\text{ GJ} = 11\,630\text{ kWh}$$
  * **Ejemplo:** Conversión del consumo anual de combustible de una industria desde BTU y galones de diésel hacia MWh y TEP.
* **Tema 2: Matriz Energética Mundial, Nacional (UPME) y del Caribe**
  * **Objetivo:** Analizar la composición de la oferta y demanda energética colombiana y el potencial renovable de la región Caribe.
  * **Concepto Clave:**
    $$\text{Participación}_i(\%) = \frac{E_{\text{fuente},i}}{\sum_{k=1}^{n} E_{\text{fuente},k}} \times 100\%$$
  * **Ejemplo:** Interpretación del Plan Energético Nacional (UPME) comparando generación hidráulica, térmica y solar en Colombia.
* **Tema 3: Cadenas de Conversión, Diagramas de Sankey y Eficiencia Global**
  * **Objetivo:** Cuantificar pérdidas por etapas en sistemas de transformación energética desde la fuente hasta el uso final.
  * **Concepto Clave:**
    $$\eta_{\text{global}} = \frac{E_{\text{útil}}}{E_{\text{primaria}}} = \prod_{i=1}^{n} \eta_i$$
  * **Ejemplo:** Cálculo de la eficiencia combinada de una central termoeléctrica integrando caldera (88%), turbina (42%) y generador (97%).
* **Tema 4: Sostenibilidad, ODS 7, Ley 1715 y Transición Energética**
  * **Objetivo:** Comprender los retos ambientales, regulatorios y éticos de la descarbonización y el acceso universal a energía limpia.
  * **Concepto Clave:**
    $$E_{\text{CO}_2} = E_{\text{eléc}} \cdot \text{FE}_{\text{SIN}}$$
  * **Ejemplo:** Estimación de emisiones de CO₂ evitadas anualmente al integrar autogeneración solar fotovoltaica en el campus universitario.

### 5. Procesos Lectores, Escriturales y Orales (`01011801`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Lectura Crítica, Inferencia y Superestructura Textual**
  * **Objetivo:** Desarrollar comprensión literal, inferencial y crítica identificando tesis, argumentos y contraargumentos en textos académicos.
  * **Concepto Clave:**
    $$\text{Lectura Crítica} = \text{Literal} + \text{Inferencial} + \text{Valorativa}$$
  * **Ejemplo:** Desglose argumentativo de un artículo científico sobre comunidades energéticas sostenibles en el Caribe colombiano.
* **Tema 2: Escritura Académica: Coherencia, Cohesión y Precisión Léxica**
  * **Objetivo:** Producir textos expositivos y argumentativos claros mediante planeación textual, conectores lógicos y revisión estilística.
  * **Concepto Clave:**
    $$\text{Índice de Legibilidad} = 206.835 - 1.015\left(\frac{\text{Palabras}}{\text{Oraciones}}\right)$$
  * **Ejemplo:** Redacción y depuración de un ensayo argumentativo sobre eficiencia energética y sostenibilidad urbana.
* **Tema 3: Informes Técnicos de Ingeniería y Normas de Citación (IEEE / APA)**
  * **Objetivo:** Estructurar artículos e informes de laboratorio bajo el formato IMRyD aplicando referenciación bibliográfica rigurosa.
  * **Concepto Clave:**
    $$\text{IMRyD} : \text{Introducción} \longrightarrow \text{Métodos} \longrightarrow \text{Resultados} \longrightarrow \text{Discusión}$$
  * **Ejemplo:** Estructuración del resumen ejecutivo (Abstract) y bibliografía IEEE para un proyecto de transición energética.
* **Tema 4: Oralidad Académica, Argumentación y Defensa de Proyectos**
  * **Objetivo:** Sustentar ideas técnicas en escenarios universitarios articulando expresión verbal, lenguaje corporal y síntesis visual.
  * **Concepto Clave:**
    $$t_{\text{pitch}} = t_{\text{problema}} + t_{\text{solución}} + t_{\text{evidencia}} + t_{\text{cierre}}$$
  * **Ejemplo:** Sustentación oral estructurada de 5 minutos sobre una propuesta de ahorro energético institucional.

---

## Cuatrimestre 2 (14 Créditos)

### 6. Física Mecánica (`02021810`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Análisis Dimensional, Vectores y Cinemática en 1D/2D**
  * **Objetivo:** Describir vectorial y analíticamente el movimiento rectilíneo, parabólico y circular de partículas mediante cálculo.
  * **Concepto Clave:**
    $$\vec{v}(t) = \frac{d\vec{r}}{dt} \quad ; \quad \vec{a}(t) = \frac{d\vec{v}}{dt} \quad ; \quad a_c = \frac{v^2}{R} = \omega^2 R$$
  * **Ejemplo:** Cálculo de la velocidad lineal y aceleración centrípeta en el extremo de una pala eólica de 50 m de radio.
* **Tema 2: Leyes de Newton y Dinámica con Rozamiento**
  * **Objetivo:** Aplicar las leyes del movimiento de Newton y diagramas de cuerpo libre con fuerzas de fricción estática y cinética.
  * **Concepto Clave:**
    $$\sum \vec{F} = m \cdot \vec{a} \quad ; \quad f_s \le \mu_s N \quad ; \quad f_k = \mu_k N$$
  * **Ejemplo:** Determinación de la aceleración y tensión de izaje de un bloque sobre un plano inclinado con rozamiento cinético.
* **Tema 3: Trabajo, Energía Mecánica y Potencia**
  * **Objetivo:** Aplicar el teorema del trabajo y la energía cinética, fuerzas conservativas y conservación de la energía mecánica.
  * **Concepto Clave:**
    $$W = \int_{r_1}^{r_2} \vec{F} \cdot d\vec{r} = \Delta K \quad ; \quad E_m = K + U_g + U_e \quad ; \quad P = \vec{F} \cdot \vec{v}$$
  * **Ejemplo:** Cálculo de la conversión de energía potencial gravitacional a cinética en la descarga de una central hidroeléctrica.
* **Tema 4: Sistemas de Partículas, Impulso, Momentum Lineal y Colisiones**
  * **Objetivo:** Evaluar centro de masa, impulso mecánico y conservación del momentum lineal en choques elásticos e inelásticos.
  * **Concepto Clave:**
    $$\vec{p} = m\vec{v} \quad ; \quad \vec{J} = \int_{t_1}^{t_2} \vec{F}(t)\,dt = \Delta\vec{p} \quad ; \quad \sum \vec{p}_i = \sum \vec{p}_f$$
  * **Ejemplo:** Determinación de la fuerza impulsiva transferida por un chorro de agua de alta velocidad sobre un álabe Pelton.
* **Tema 5: Dinámica Rotacional, Momento de Inercia y Equilibrio Estático**
  * **Objetivo:** Modelar el torque, momento de inercia (Steiner), energía cinética rotacional y equilibrio de cuerpos rígidos.
  * **Concepto Clave:**
    $$\sum \tau = I\alpha \quad ; \quad K_{\text{rot}} = \frac{1}{2}I\omega^2 \quad ; \quad \sum \vec{F} = \vec{0},\; \sum \vec{\tau} = \vec{0}$$
  * **Ejemplo:** Cálculo de la energía almacenada en un volante de inercia (flywheel) y reacciones estáticas en estructuras soporte solares.

### 7. Fundamentos de la Electricidad I (`03041819`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Variables Eléctricas, Ley de Ohm, Asociaciones y Potencia DC**
  * **Objetivo:** Cuantificar carga, corriente, tensión, resistencias serie/paralelo, divisores y balance de potencia en DC.
  * **Concepto Clave:**
    $$i(t) = \frac{dq}{dt} \quad ; \quad V = I \cdot R \quad ; \quad P = V \cdot I = I^2 R = \frac{V^2}{R}$$
  * **Ejemplo:** Cálculo de caída de tensión, pérdidas Joule y eficiencia en el cableado DC entre un string fotovoltaico y su inversor.
* **Tema 2: Leyes de Kirchhoff y Análisis Sistemático de Nodos y Mallas**
  * **Objetivo:** Resolver circuitos resistivos lineales con fuentes independientes y dependientes mediante LCK y LVK.
  * **Concepto Clave:**
    $$\sum_{k=1}^{n} I_k = 0 \quad ; \quad \sum_{m=1}^{p} V_m = 0 \quad ; \quad \mathbf{G}\mathbf{v}_n = \mathbf{i}_s$$
  * **Ejemplo:** Determinación de tensiones de nodo y flujos de corriente en una micro-red DC con generación solar, batería y carga.
* **Tema 3: Linealidad, Superposición, Thévenin, Norton y Máxima Potencia**
  * **Objetivo:** Simplificar redes activas entre dos terminales a circuitos equivalentes para optimizar la transferencia de potencia.
  * **Concepto Clave:**
    $$V_{th} = V_{oc} \quad ; \quad R_{th} = \frac{V_{oc}}{I_{sc}} \quad ; \quad P_{\max} = \frac{V_{th}^2}{4 R_{th}}$$
  * **Ejemplo:** Acoplamiento óptimo de carga resistiva para extraer la máxima potencia disponible de una fuente DC equivalente.
* **Tema 4: Capacitores, Inductores y Transitorios de Primer Orden (RC y RL)**
  * **Objetivo:** Analizar el almacenamiento de energía en campos eléctricos/magnéticos y la respuesta natural y forzada de circuitos RC y RL.
  * **Concepto Clave:**
    $$v_C(t) = V_\infty + [v_C(0) - V_\infty]e^{-t/\tau} \quad ; \quad \tau_{RC} = R_{th}C \quad ; \quad \tau_{RL} = \frac{L}{R_{th}}$$
  * **Ejemplo:** Dimensionamiento de la resistencia de precarga del bus DC capacitivo de un convertidor para limitar picos de corriente.

### 8. General English II (`01021803`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Energy Milestones & Incident Logs (Past Simple & Continuous)**
  * **Objetivo:** Narrar hitos científicos y redactar bitácoras de eventos operativos pasados combinando Past Simple y Past Continuous (MCER A2).
  * **Concepto Clave:**
    $$\Delta t_{\text{outage}} = t_{\text{restored}} - t_{\text{fault}}$$
  * **Ejemplo:** Reporte breve de falla eléctrica (While the turbine was operating at full load, the grid sensor detected a voltage sag).
* **Tema 2: Comparative Analysis of Power Technologies**
  * **Objetivo:** Comparar rendimientos, costos y vida útil entre tecnologías energéticas mediante estructuras comparativas y superlativas.
  * **Concepto Clave:**
    $$\Delta \eta = \eta_{\text{new}} - \eta_{\text{baseline}}$$
  * **Ejemplo:** Comparación escrita en inglés entre turbinas hidráulicas Pelton, Francis y Kaplan según salto y eficiencia.
* **Tema 3: Laboratory Safety & Engineering Quantities (Modals & Quantifiers)**
  * **Objetivo:** Expresar obligaciones y recomendaciones de seguridad eléctrica usando verbos modales (must, should, have to).
  * **Concepto Clave:**
    $$V_{\text{safety}} \le 50\text{ V}_{\text{AC}}$$
  * **Ejemplo:** Redacción de normas de seguridad PPE antes de energizar un banco de pruebas en el laboratorio.
* **Tema 4: Energy Forecasts & Project Schedules (Future Forms)**
  * **Objetivo:** Describir planes de ingeniería, cronogramas de montaje y proyecciones energéticas con going to y will.
  * **Concepto Clave:**
    $$E_{\text{proj}} = E_0 (1 + g)^n$$
  * **Ejemplo:** Presentación corta en inglés sobre la proyección de expansión solar y eólica para la próxima década.

### 9. Probabilidad y Estadística (`03031818`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `3` • **Color UI:** `#5E5CE6`
* **Tema 1: Estadística Descriptiva, Tendencia Central y Dispersión**
  * **Objetivo:** Resumir series experimentales mediante media, mediana, varianza muestral, cuantiles y coeficiente de variación.
  * **Concepto Clave:**
    $$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i \quad ; \quad s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2 \quad ; \quad \text{CV} = \frac{s}{\bar{x}}$$
  * **Ejemplo:** Caracterización estadística de la variabilidad horaria y estacional de radiación solar global en Santa Marta.
* **Tema 2: Axiomas de Probabilidad, Confiabilidad y Teorema de Bayes**
  * **Objetivo:** Calcular probabilidades condicionales, confiabilidad de sistemas serie/paralelo y actualización bayesiana de riesgos.
  * **Concepto Clave:**
    $$P(A \mid B) = \frac{P(B \mid A)P(A)}{\sum_{j=1}^{k} P(B \mid A_j)P(A_j)} \quad ; \quad R_{\text{par}} = 1 - \prod_{i=1}^{n}(1 - R_i)$$
  * **Ejemplo:** Evaluación de la disponibilidad probabilística de una planta con inversores redundantes en paralelo.
* **Tema 3: Variables Aleatorias Discretas (Esperanza, Binomial y Poisson)**
  * **Objetivo:** Modelar conteos de fallas y eventos discretos en ventanas de tiempo mediante distribuciones Binomial y de Poisson.
  * **Concepto Clave:**
    $$E[X] = \sum_{x} x\,p(x) \quad ; \quad P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
  * **Ejemplo:** Estimación de la probabilidad mensual de desconexiones por sobretensión atmosférica en un circuito de distribución.
* **Tema 4: Distribuciones Continuas (Normal, Exponencial y Weibull) e Inferencia**
  * **Objetivo:** Modelar recursos renovables continuos y tiempos de vida útil construyendo intervalos de confianza estadísticos.
  * **Concepto Clave:**
    $$f(v) = \frac{k}{c}\left(\frac{v}{c}\right)^{k-1} \exp\left[-\left(\frac{v}{c}\right)^k\right] \quad ; \quad \bar{x} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$
  * **Ejemplo:** Ajuste de la distribución de Weibull para estimar el potencial energético del viento en la costa Caribe.

### 10. Química Aplicada (`02031812`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `3` • **Color UI:** `#30D158`
* **Tema 1: Estructura Atómica, Enlace Químico y Materiales para Energía**
  * **Objetivo:** Relacionar la configuración electrónica y los enlaces iónico, covalente y metálico con semiconductores y conductores.
  * **Concepto Clave:**
    $$E_{\text{fotón}} = h\nu = \frac{hc}{\lambda} \ge E_g$$
  * **Ejemplo:** Análisis del enlace covalente en redes de silicio dopado (tipo n y p) y su banda prohibida de 1.12 eV en celdas solares.
* **Tema 2: Estequiometría, Reactivo Límite y Balances de Combustión**
  * **Objetivo:** Formular balances másicos y molares en reacciones químicas y procesos de combustión con aire teórico y en exceso.
  * **Concepto Clave:**
    $$\text{CH}_4 + 2(\text{O}_2 + 3.76\text{N}_2) \longrightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2$$
  * **Ejemplo:** Cálculo de la relación aire-combustible y masa de CO₂ emitida por cada metro cúbico de gas natural quemado.
* **Tema 3: Gases Ideales y Reales, Disoluciones y Equilibrio Químico**
  * **Objetivo:** Aplicar ecuaciones de estado de gases, mezclas de Dalton, concentración molar y principio de Le Chatelier.
  * **Concepto Clave:**
    $$P V = n R T \quad ; \quad P_i = y_i P_{\text{tot}} \quad ; \quad K_c = \frac{[\text{C}]^c[\text{D}]^d}{[\text{A}]^a[\text{B}]^b}$$
  * **Ejemplo:** Determinación de la masa de hidrógeno comprimido almacenada en cilindros de alta presión y preparación de electrolitos KOH.
* **Tema 4: Termoquímica (Ley de Hess), Poder Calorífico y Electroquímica**
  * **Objetivo:** Calcular entalpías de reacción, poder calorífico superior/inferior y potenciales de celda mediante la ecuación de Nernst.
  * **Concepto Clave:**
    $$\Delta H^\circ_{\text{rxn}} = \sum \nu_p \Delta H^\circ_{f,p} - \sum \nu_r \Delta H^\circ_{f,r} \quad ; \quad E_{\text{celda}} = E^\circ - \frac{RT}{nF}\ln Q$$
  * **Ejemplo:** Cálculo del poder calorífico inferior (PCI) de mezclas biogás-metano y tensión reversible en baterías y celdas galvánicas.

---

## Cuatrimestre 3 (15 Créditos)

### 11. Cálculo Integral (`02011808`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `4` • **Color UI:** `#5E5CE6`
* **Tema 1: Antiderivadas, Integral Indefinida y Método de Sustitución**
  * **Objetivo:** Reconstruir funciones primitivas a partir de sus tasas de variación mediante reglas directas y cambio de variable.
  * **Concepto Clave:**
    $$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du = F(g(x)) + C$$
  * **Ejemplo:** Determinación de la función de carga eléctrica q(t) a partir de una corriente transitoria exponencial i(t).
* **Tema 2: Técnicas de Integración: Por Partes, Trigonométricas y Fracciones Parciales**
  * **Objetivo:** Resolver integrales analíticas de productos trascendentes, radicales cuadráticos y funciones racionales.
  * **Concepto Clave:**
    $$\int u \, dv = u \cdot v - \int v \, du \quad ; \quad \frac{P(x)}{(x-a)(x-b)} = \frac{A}{x-a} + \frac{B}{x-b}$$
  * **Ejemplo:** Integración analítica de una señal de potencia amortiguada P(t) = P₀·t·e^(-αt) durante una maniobra eléctrica.
* **Tema 3: Integral Definida, Teorema Fundamental e Integración Numérica**
  * **Objetivo:** Acumular magnitudes físicas aplicando el Teorema Fundamental del Cálculo y reglas numéricas de Trapecio y Simpson.
  * **Concepto Clave:**
    $$E = \int_{t_1}^{t_2} P(t) \, dt = F(t_2) - F(t_1) \quad ; \quad P_{\text{prom}} = \frac{1}{T}\int_0^T P(t)\,dt$$
  * **Ejemplo:** Integración de la curva diaria de demanda eléctrica (y regla de Simpson sobre lecturas horarias) para obtener MWh consumidos.
* **Tema 4: Aplicaciones Geométricas y Físicas: Áreas, Volúmenes y Trabajo de Bombeo**
  * **Objetivo:** Calcular áreas entre curvas, volúmenes de revolución, centros de masa y trabajo mecánico de vaciado de tanques.
  * **Concepto Clave:**
    $$V = \pi \int_a^b \left([R(x)]^2 - [r(x)]^2\right)dx \quad ; \quad W_{\text{bombeo}} = \rho g \int_a^b A(y)(H - y)\,dy$$
  * **Ejemplo:** Cálculo de la energía mínima requerida para bombear la totalidad del agua desde un reservorio subterráneo hacia una torre.
* **Tema 5: Integrales Impropias, Sucesiones y Series de Taylor**
  * **Objetivo:** Analizar convergencia de integrales con límites infinitos y aproximar funciones mediante desarrollos en serie de potencias.
  * **Concepto Clave:**
    $$\int_a^\infty f(x)\,dx = \lim_{b \to \infty}\int_a^b f(x)\,dx \quad ; \quad f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$
  * **Ejemplo:** Evaluación de energía total disipada en horizonte infinito y linealización por serie de Taylor de radiación térmica.

### 12. Calor y Ondas (`02021811`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Elasticidad y Mecánica de Fluidos Ideal (Arquímedes y Bernoulli)**
  * **Objetivo:** Estudiar deformación elástica en sólidos, hidrostática, flotación y conservación de energía en líneas de corriente.
  * **Concepto Clave:**
    $$P = P_0 + \rho g h \quad ; \quad A_1 v_1 = A_2 v_2 \quad ; \quad P + \frac{1}{2}\rho v^2 + \rho g y = \text{cte}$$
  * **Ejemplo:** Cálculo del empuje hidrostático sobre estructuras flotantes para paneles solares (floating PV) y caudal en tuberías Venturi.
* **Tema 2: Termometría, Dilatación Térmica, Calorimetría y Conducción**
  * **Objetivo:** Cuantificar expansiones térmicas, intercambios de calor sensible/latente y mecanismos básicos de transferencia térmica.
  * **Concepto Clave:**
    $$\Delta L = \alpha L_0 \Delta T \quad ; \quad Q = m c \Delta T + m L_f \quad ; \quad \dot{Q} = -k A \frac{\Delta T}{\Delta x}$$
  * **Ejemplo:** Cálculo del equilibrio térmico en un tanque de almacenamiento solar con material de cambio de fase (PCM).
* **Tema 3: Teoría Cinética de los Gases y Primera Ley en Procesos Ideales**
  * **Objetivo:** Conectar variables microscópicas moleculares con presión, temperatura interna y trabajo en procesos termodinámicos.
  * **Concepto Clave:**
    $$v_{\text{rms}} = \sqrt{\frac{3 R T}{M}} \quad ; \quad \Delta E_{\text{int}} = Q - W \quad ; \quad P V^\gamma = \text{cte}$$
  * **Ejemplo:** Determinación del calor, trabajo y cambio de energía interna en expansiones isotérmicas y adiabáticas de un gas ideal.
* **Tema 4: Movimiento Armónico Simple (MAS), Ondas Mecánicas y Acústica**
  * **Objetivo:** Modelar osciladores armónicos, ecuación de onda viajera, ondas estacionarias, resonancia y niveles sonoros en decibeles.
  * **Concepto Clave:**
    $$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} \quad ; \quad \omega_0 = \sqrt{\frac{k}{m}} \quad ; \quad \beta = 10\log_{10}\left(\frac{I}{I_0}\right)$$
  * **Ejemplo:** Evaluación de frecuencias naturales de vibración en góndolas eólicas y atenuación acústica ambiental en decibeles.

### 13. Fundamentos de Electricidad II (`03041820`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `2` • **Color UI:** `#FF9F0A`
* **Tema 1: Régimen Sinusoidal, Fasores e Impedancia Compleja**
  * **Objetivo:** Resolver circuitos RLC en corriente alterna estacionaria utilizando álgebra fasorial, impedancia y admitancia.
  * **Concepto Clave:**
    $$\mathbf{Z} = R + j\left(\omega L - \frac{1}{\omega C}\right) \quad ; \quad \mathbf{V}_{\text{rms}} = \mathbf{Z}\cdot\mathbf{I}_{\text{rms}}$$
  * **Ejemplo:** Determinación de magnitud y ángulo de fase de la corriente absorbida por un motor monofásico inductivo a 60 Hz.
* **Tema 2: Potencia Compleja, Triángulo de Potencias y Factor de Potencia**
  * **Objetivo:** Calcular potencia activa, reactiva y aparente, y dimensionar bancos de capacitores para compensación reactiva.
  * **Concepto Clave:**
    $$\mathbf{S} = P + jQ = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* \quad ; \quad \text{FP} = \cos(\theta_v - \theta_i) \quad ; \quad Q_C = P(\tan\theta_1 - \tan\theta_2)$$
  * **Ejemplo:** Dimensionamiento de un banco de capacitores para elevar el factor de potencia industrial de 0.82 a 0.96 inductivo evitando penalización.
* **Tema 3: Sistemas Trifásicos Equilibrados (Estrella Y y Triángulo Delta)**
  * **Objetivo:** Analizar relaciones entre magnitudes de línea y de fase en generadores y cargas conectadas en estrella y delta.
  * **Concepto Clave:**
    $$V_L = \sqrt{3}\,V_f \quad ; \quad I_L = \sqrt{3}\,I_f \quad ; \quad P_{3\phi} = \sqrt{3}\,V_L I_L \cos\theta$$
  * **Ejemplo:** Cálculo de corrientes de línea y potencia entregada por un inversor solar trifásico de 100 kW a una barra de 440 V.
* **Tema 4: Resonancia Eléctrica, Filtros Pasivos y Circuitos Acoplados**
  * **Objetivo:** Analizar la respuesta en frecuencia, resonancia serie/paralelo e inductancia mutua en transformadores ideales y lineales.
  * **Concepto Clave:**
    $$\omega_0 = \frac{1}{\sqrt{LC}} \quad ; \quad \frac{V_2}{V_1} = \frac{N_2}{N_1} \quad ; \quad Z_{\text{in}} = \left(\frac{N_1}{N_2}\right)^2 Z_L$$
  * **Ejemplo:** Diseño de un filtro LC sintonizado y reflexión de impedancia a través de un transformador elevador de acoplamiento.

### 14. Fundamentos de Hidráulica y Neumática (`03021815`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Propiedades de Fluidos de Potencia y Principio de Pascal**
  * **Objetivo:** Evaluar viscosidad, compresibilidad y multiplicación hidrostática de fuerzas en circuitos óleo-hidráulicos y neumáticos.
  * **Concepto Clave:**
    $$P = \frac{F_1}{A_1} = \frac{F_2}{A_2} \quad ; \quad \nu = \frac{\mu}{\rho}$$
  * **Ejemplo:** Cálculo de la presión manométrica y ventaja mecánica en una prensa hidráulica de mantenimiento electromecánico.
* **Tema 2: Bombas Oleohidráulicas, Compresores y Unidad FRL**
  * **Objetivo:** Dimensionar bombas de desplazamiento positivo y compresores de aire cuantificando potencia fluida y eficiencias.
  * **Concepto Clave:**
    $$Q_{\text{real}} = V_d \cdot n \cdot \eta_v \quad ; \quad N_{\text{hid}} = \Delta P \cdot Q \quad ; \quad N_{\text{eje}} = \frac{\Delta P \cdot Q}{\eta_{\text{tot}}}$$
  * **Ejemplo:** Cálculo de la potencia eléctrica requerida por la central hidráulica de frenos y orientación (yaw) de un aerogenerador.
* **Tema 3: Actuadores Lineales (Cilindros) y Motores Hidráulicos/Neumáticos**
  * **Objetivo:** Determinar fuerzas efectivas de extensión y retracción, caudales requeridos y par torsional en actuadores.
  * **Concepto Clave:**
    $$F_{\text{av}} = P \frac{\pi D^2}{4}\eta_m \quad ; \quad F_{\text{ret}} = P \frac{\pi(D^2 - d^2)}{4}\eta_m \quad ; \quad \tau = \frac{\Delta P \cdot V_d}{2\pi}$$
  * **Ejemplo:** Dimensionamiento del diámetro de émbolo del cilindro hidráulico para el sistema de pitch de palas eólicas.
* **Tema 4: Válvulas de Control (ISO 1219) y Circuitos Electro-Hidráulicos**
  * **Objetivo:** Diseñar esquemas con válvulas direccionales, limitadoras de presión, antirretorno y reguladoras de caudal.
  * **Concepto Clave:**
    $$Q = C_d A_o \sqrt{\frac{2\,\Delta P}{\rho}}$$
  * **Ejemplo:** Diseño del circuito electro-hidráulico con válvula de contrabalance para seguidores solares (solar trackers) de gran escala.

### 15. General English III (`01021804`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Engineering Progress & Achievements (Present Perfect)**
  * **Objetivo:** Reportar avances de implementación, resultados acumulados y experiencias técnicas empleando el Present Perfect (MCER B1.1).
  * **Concepto Clave:**
    $$\text{Completion}(\%) = \frac{\text{Installed kW}}{\text{Planned kW}} \times 100\%$$
  * **Ejemplo:** Informe de progreso de obra (The engineering team has commissioned twelve string inverters since Monday).
* **Tema 2: Passive Voice in Technical Manuals & Commissioning Protocols**
  * **Objetivo:** Redactar procedimientos de laboratorio y manuales de mantenimiento enfatizando el proceso mediante la voz pasiva.
  * **Concepto Clave:**
    $$\text{Efficiency}(\%) = \left(\frac{P_{\text{out}}}{P_{\text{in}}}\right) \times 100\%$$
  * **Ejemplo:** Interpretación y redacción de protocolos de puesta en marcha de inversores solares en inglés técnico.
* **Tema 3: System Contingencies & Cause-Effect (Conditionals 0, 1 & 2)**
  * **Objetivo:** Formular leyes físicas, lógicas de protección y escenarios hipotéticos de operación usando oraciones condicionales.
  * **Concepto Clave:**
    $$f < 59.5\text{ Hz} \implies \text{Under-Frequency Relay Trips}$$
  * **Ejemplo:** Descripción de protecciones eléctricas (If grid voltage exceeds the upper threshold, the inverter disconnects automatically).
* **Tema 4: Component Specifications & Definitions (Relative Clauses)**
  * **Objetivo:** Definir instrumentos, sensores y arquitecturas energéticas con precisión formal mediante cláusulas relativas.
  * **Concepto Clave:**
    $$G_{\text{POA}} = G_b \cos\theta_i + G_d\left(\frac{1+\cos\beta}{2}\right) + \rho G_h\left(\frac{1-\cos\beta}{2}\right)$$
  * **Ejemplo:** Definición técnica formal (A pyranometer is a sensor which measures broadband solar irradiance on a planar surface).

---

## Cuatrimestre 4 (15 Créditos)

### 16. Álgebra Lineal (`02011809`)
* **Categoría:** `MATEMATICAS` • **Créditos:** `3` • **Color UI:** `#5E5CE6`
* **Tema 1: Sistemas de Ecuaciones Lineales, Matrices y Gauss-Jordan**
  * **Objetivo:** Resolver sistemas lineales de múltiples variables mediante reducción escalonada, álgebra matricial y matriz inversa.
  * **Concepto Clave:**
    $$A\vec{x} = \vec{b} \quad ; \quad A A^{-1} = I \quad ; \quad \mathbf{Y}_{\text{bus}}\mathbf{V} = \mathbf{I}$$
  * **Ejemplo:** Formulación y solución del sistema matricial de tensiones nodales en una red eléctrica de distribución de 4 barras.
* **Tema 2: Determinantes, Propiedades e Invertibilidad de Sistemas**
  * **Objetivo:** Calcular determinantes por cofactores y operaciones de fila para analizar unicidad de soluciones y matrices Jacobianas.
  * **Concepto Clave:**
    $$\det(A) = \sum_{j=1}^{n}(-1)^{1+j} a_{1j} M_{1j} \quad ; \quad \det(A) \neq 0 \iff A \text{ es invertible}$$
  * **Ejemplo:** Verificación de invertibilidad de la matriz Jacobiana durante una iteración de flujo de potencia.
* **Tema 3: Espacios Vectoriales, Bases, Ortogonalidad y Mínimos Cuadrados**
  * **Objetivo:** Determinar independencia lineal, dimensión, bases ortonormales (Gram-Schmidt) y proyecciones por mínimos cuadrados.
  * **Concepto Clave:**
    $$\vec{u}\cdot\vec{v} = \|\vec{u}\|\|\vec{v}\|\cos\theta \quad ; \quad \hat{x} = (A^T A)^{-1}A^T\vec{b}$$
  * **Ejemplo:** Estimación matricial por mínimos cuadrados de los coeficientes de pérdida térmica de una edificación a partir de mediciones.
* **Tema 4: Transformaciones Lineales, Valores Propios y Diagonalización**
  * **Objetivo:** Calcular autovalores y autovectores del polinomio característico para desacoplar sistemas dinámicos y analizar estabilidad.
  * **Concepto Clave:**
    $$A\vec{v} = \lambda\vec{v} \quad ; \quad \det(A - \lambda I) = 0 \quad ; \quad A = P D P^{-1}$$
  * **Ejemplo:** Evaluación de modos oscilatorios y estabilidad dinámica de un sistema energético linealizado mediante el espectro de autovalores.

### 17. Conversión de Energía (`06011837`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Rutas de Transformación Energética y Rendimiento Exergético**
  * **Objetivo:** Evaluar cadenas de conversión termo-mecánica, electromecánica y electroquímica bajo primera y segunda ley.
  * **Concepto Clave:**
    $$\eta_I = \frac{\dot{E}_{\text{útil}}}{\dot{E}_{\text{entrada}}} \quad ; \quad \eta_{II} = 1 - \frac{\dot{E}_{\text{destruida}}}{\dot{\Psi}_{\text{entrada}}}$$
  * **Ejemplo:** Comparación de eficiencia de primera y segunda ley entre un motor de combustión, una turbina y una celda de combustible.
* **Tema 2: Circuitos Magnéticos, Curva B-H y Pérdidas en Núcleos Ferromagnéticos**
  * **Objetivo:** Resolver circuitos magnéticos con entrehierro mediante reluctancias y cuantificar pérdidas por histéresis y Foucault.
  * **Concepto Clave:**
    $$\mathcal{F} = N I = \Phi \mathcal{R} \quad ; \quad \mathcal{R} = \frac{l}{\mu_r \mu_0 A} \quad ; \quad P_{\text{Fe}} = k_h f B_{\max}^n + k_e f^2 B_{\max}^2$$
  * **Ejemplo:** Cálculo de los amperios-vuelta requeridos para producir un flujo magnético de diseño en el entrehierro de un inductor de potencia.
* **Tema 3: Principios de Conversión Electromecánica: Energía y Coenergía**
  * **Objetivo:** Modelar fuerzas traslacionales y pares electromagnéticos en transductores y máquinas a partir de la coenergía magnética.
  * **Concepto Clave:**
    $$dW_{\text{eléc}} = dW_{\text{campo}} + dW_{\text{mec}} \quad ; \quad \tau_e = \frac{\partial W'(\theta, i)}{\partial \theta}$$
  * **Ejemplo:** Cálculo del par electromagnético desarrollado en función del ángulo rotor en un actuador de reluctancia variable.
* **Tema 4: Conversión Directa: Termoeléctrica (Seebeck), Fotovoltaica y Química**
  * **Objetivo:** Analizar mecanismos de conversión directa sin partes móviles basados en efectos termoeléctricos, fotoeléctricos y Gibbs.
  * **Concepto Clave:**
    $$V_{\text{oc}} = \alpha_{AB}(T_H - T_C) \quad ; \quad ZT = \frac{\alpha^2 \sigma}{\kappa}T \quad ; \quad W_{\text{eléc,máx}} = -\Delta G$$
  * **Ejemplo:** Estimación de la potencia recuperada con módulos termoeléctricos (TEG) instalados sobre un ducto de gases de escape.

### 18. Electricidad y Magnetismo (`03041821`)
* **Categoría:** `FISICA_QUIMICA` • **Créditos:** `4` • **Color UI:** `#30D158`
* **Tema 1: Carga Eléctrica, Campo Electrostático, Coulomb y Ley de Gauss**
  * **Objetivo:** Determinar campos eléctricos producidos por distribuciones discretas y continuas de carga empleando integración y simetría.
  * **Concepto Clave:**
    $$\vec{E} = \frac{1}{4\pi\varepsilon_0}\int \frac{dq}{r^2}\hat{r} \quad ; \quad \oint_S \vec{E} \cdot d\vec{A} = \frac{q_{\text{enc}}}{\varepsilon_0}$$
  * **Ejemplo:** Cálculo del gradiente de campo eléctrico en la superficie de un conductor cilíndrico de transmisión para prevenir efecto corona.
* **Tema 2: Potencial Eléctrico, Capacitancia, Dieléctricos y Energía Electrostática**
  * **Objetivo:** Calcular diferencias de potencial, capacitancia equivalente y densidad de energía almacenada en medios dieléctricos.
  * **Concepto Clave:**
    $$V_B - V_A = -\int_A^B \vec{E}\cdot d\vec{l} \quad ; \quad C = \kappa\varepsilon_0\frac{A}{d} \quad ; \quad u_E = \frac{1}{2}\varepsilon E^2$$
  * **Ejemplo:** Dimensionamiento dieléctrico y energía almacenada en bancos de supercapacitores para soporte transitorio de tensión.
* **Tema 3: Densidad de Corriente, Ley de Ohm Microscópica y Efecto Térmico**
  * **Objetivo:** Relacionar campo eléctrico, velocidad de deriva, conductividad y dependencia térmica de la resistividad en conductores.
  * **Concepto Clave:**
    $$\vec{J} = \sigma\vec{E} \quad ; \quad R = \rho\frac{L}{A} \quad ; \quad \rho(T) = \rho_0[1 + \alpha(T - T_0)]$$
  * **Ejemplo:** Cálculo del aumento de resistencia óhmica en un conductor de aluminio ACSR operando a 75 °C bajo alta radiación solar.
* **Tema 4: Campo Magnético, Fuerza de Lorentz, Biot-Savart y Ley de Ampère**
  * **Objetivo:** Analizar fuerzas magnéticas sobre cargas y conductores, y calcular campos generados por corrientes estacionarias.
  * **Concepto Clave:**
    $$\vec{F}_B = q\vec{v}\times\vec{B} + I\vec{L}\times\vec{B} \quad ; \quad \oint_C \vec{B}\cdot d\vec{l} = \mu_0 I_{\text{enc}}$$
  * **Ejemplo:** Cálculo de esfuerzos electrodinámicos entre barras colectoras paralelas de una subestación ante corrientes de falla.
* **Tema 5: Inducción de Faraday-Lenz, Inductancia y Ecuaciones de Maxwell**
  * **Objetivo:** Cuantificar fuerzas electromotrices inducidas, autoinductancia, energía magnética y la corriente de desplazamiento de Maxwell.
  * **Concepto Clave:**
    $$\mathcal{E} = -N\frac{d\Phi_B}{dt} \quad ; \quad u_B = \frac{B^2}{2\mu_0} \quad ; \quad \oint_C \vec{B}\cdot d\vec{l} = \mu_0 I + \mu_0\varepsilon_0\frac{d\Phi_E}{dt}$$
  * **Ejemplo:** Deducción de la fem sinusoidal inducida en el estator de un generador síncrono a partir de un campo magnético rotatorio.

### 19. General English IV (`01021805`)
* **Categoría:** `FORMACION_GENERAL` • **Créditos:** `2` • **Color UI:** `#8E8E93`
* **Tema 1: Synthesizing Energy Literature (Reported Speech & Citations)**
  * **Objetivo:** Parafrasear hallazgos científicos, normativas e informes internacionales empleando Reported Speech (MCER B1.2).
  * **Concepto Clave:**
    $$\text{CF}(\%) = \frac{E_{\text{annual}}}{P_{\text{rated}} \cdot 8760\text{ h}} \times 100\%$$
  * **Ejemplo:** Síntesis bibliográfica en inglés de reportes anuales de IRENA e IEA sobre factores de planta renovables.
* **Tema 2: Writing Structured Abstracts for Engineering Papers**
  * **Objetivo:** Redactar resúmenes científicos (Background, Methods, Results, Conclusions) con cohesión y estilo académico formal.
  * **Concepto Clave:**
    $$e_{\text{rel}}(\%) = \left|\frac{y_{\text{sim}} - y_{\text{exp}}}{y_{\text{exp}}}\right| \times 100\%$$
  * **Ejemplo:** Escritura de un Abstract de 180 palabras para presentar un estudio de micro-redes solares en un congreso estudiantil.
* **Tema 3: Interpreting Load Curves, Sensitivity Graphs & ROI Metrics**
  * **Objetivo:** Exponer tendencias cuantitativas, curvas de demanda y métricas de viabilidad técnica-económica en inglés.
  * **Concepto Clave:**
    $$\text{ROI} = \frac{\text{Net Benefit}}{\text{Total Cost}} \times 100\%$$
  * **Ejemplo:** Descripción oral y escrita de curvas de carga horaria (duck curve) y análisis de retorno de inversión.
* **Tema 4: Academic Presentations, Technical Pitch & Q&A Defense**
  * **Objetivo:** Sustentar proyectos de ingeniería en inglés con fluidez argumentativa y manejo solvente de preguntas técnicas.
  * **Concepto Clave:**
    $$\text{Payback} = \frac{\text{CAPEX}}{\text{Annual Net Savings}}$$
  * **Ejemplo:** Presentación oral de 5 minutos defendiendo la factibilidad de una micro-red híbrida solar-almacenamiento.

### 20. Termodinámica (`03021817`)
* **Categoría:** `INGENIERIA_ENERGIA` • **Créditos:** `3` • **Color UI:** `#FF9F0A`
* **Tema 1: Conceptos Básicos y Propiedades de las Sustancias Puras**
  * **Objetivo:** Identificar estados de equilibrio, fases líquido-vapor, título de calidad y propiedades en tablas termodinámicas y gases.
  * **Concepto Clave:**
    $$h = h_f + x\,h_{fg} \quad ; \quad v = v_f + x(v_g - v_f) \quad ; \quad P v = Z R T$$
  * **Ejemplo:** Interpolación en tablas de vapor sobrecalentado y mezcla saturada para caracterizar el fluido de trabajo en una caldera.
* **Tema 2: Primera Ley de la Termodinámica en Sistemas Cerrados**
  * **Objetivo:** Evaluar trabajo de frontera móvil, transferencia de calor y variaciones de energía interna y entalpía en masa fija.
  * **Concepto Clave:**
    $$Q - W = \Delta U + \Delta E_c + \Delta E_p \quad ; \quad W_b = \int_1^2 P\,dV \quad ; \quad \Delta u = c_v \Delta T$$
  * **Ejemplo:** Cálculo del trabajo de compresión politrópica y transferencia de calor en un conjunto cilindro-émbolo.
* **Tema 3: Primera Ley en Volúmenes de Control (Flujo Estacionario)**
  * **Objetivo:** Aplicar conservación de masa y energía en turbinas, compresores, bombas, toberas e intercambiadores de calor.
  * **Concepto Clave:**
    $$\dot{Q}_{vc} - \dot{W}_{vc} = \sum \dot{m}_s\left(h_s + \frac{v_s^2}{2} + gz_s\right) - \sum \dot{m}_e\left(h_e + \frac{v_e^2}{2} + gz_e\right)$$
  * **Ejemplo:** Determinación de la potencia generada por una turbina de vapor adiabática y caudal de agua de enfriamiento en el condensador.
* **Tema 4: Segunda Ley de la Termodinámica, Entropía y Eficiencia Isentrópica**
  * **Objetivo:** Analizar máquinas térmicas, límite de Carnot, balance de generación de entropía y eficiencias isentrópicas reales.
  * **Concepto Clave:**
    $$\eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H} \quad ; \quad \dot{S}_{\text{gen}} = \sum \dot{m}_s s_s - \sum \dot{m}_e s_e - \sum \frac{\dot{Q}_k}{T_k} \ge 0 \quad ; \quad \eta_{s,T} = \frac{h_1 - h_{2a}}{h_1 - h_{2s}}$$
  * **Ejemplo:** Cálculo de la eficiencia isentrópica e irreversibilidades en una turbina de gas y en una bomba de alimentación.
* **Tema 5: Ciclos de Potencia (Rankine, Brayton, Otto/Diesel) y Refrigeración**
  * **Objetivo:** Modelar y optimizar ciclos termodinámicos de generación eléctrica a vapor y gas, así como sistemas de refrigeración.
  * **Concepto Clave:**
    $$\eta_{\text{Rankine}} = \frac{w_{\text{turb}} - w_{\text{bomba}}}{q_{\text{entrada}}} \quad ; \quad \eta_{\text{Brayton}} = 1 - \frac{1}{r_p^{(k-1)/k}} \quad ; \quad \text{COP}_R = \frac{q_L}{w_{\text{comp}}}$$
  * **Ejemplo:** Determinación de la potencia neta y eficiencia térmica de un ciclo Rankine con sobrecalentamiento y recalentamiento.

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