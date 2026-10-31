---
database_name: "ingenieria_energetica"
schema_version: "3.0.0"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Funciones Reales, Dominio y Modelos Energéticos"
            objetivo: "Modelar relaciones físicas mediante funciones algebraicas, exponenciales y trigonométricas."
            concepto_clave_latex: "P(T) = P_{\\text{STC}}\\,[1 + \\gamma(T_c - 25)] \\quad ; \\quad (f \\circ g)(x) = f(g(x))"
            ejemplo: "Curva de potencia fotovoltaica en función de la temperatura de celda."
            bloque_sugerido: "Pomodoro 50/10 • Dominio, rango y composición"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Funciones Inversas, Exponenciales y Logarítmicas"
            objetivo: "Aplicar propiedades exponenciales y logarítmicas a fenómenos de carga y enfriamiento."
            concepto_clave_latex: "y = a^x \\iff x = \\log_a(y) \\quad ; \\quad T(t) = T_\\infty + (T_0 - T_\\infty)e^{-kt}"
            ejemplo: "Ley de enfriamiento en transformadores sumergidos en aceite."
            bloque_sugerido: "Práctica 45 min • Ecuaciones exponenciales"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Límites Laterales, Álgebra de Límites e Indeterminaciones"
            objetivo: "Evaluar límites finitos y resolver formas indeterminadas algebraicas y trigonométricas."
            concepto_clave_latex: "\\lim_{x \\to a} f(x) = L \\quad ; \\quad \\lim_{x \\to 0}\\frac{\\sin x}{x} = 1"
            ejemplo: "Comportamiento límite de la impedancia de un filtro cerca de resonancia."
            bloque_sugerido: "Pomodoro 50/10 • 10 límites indeterminados"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Límites al Infinito y Comportamiento Asintótico"
            objetivo: "Determinar asíntotas horizontales, verticales y oblicuas en regímenes estacionarios."
            concepto_clave_latex: "\\lim_{t \\to \\infty} I(t) = \\lim_{t \\to \\infty}\\frac{V}{R}(1 - e^{-Rt/L}) = \\frac{V}{R}"
            ejemplo: "Corriente estacionaria en la bobina de excitación de un generador."
            bloque_sugerido: "Práctica 40 min • Asíntotas y estado estable"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Continuidad Puntual y Teorema del Valor Intermedio"
            objetivo: "Analizar continuidad por tramos y garantizar existencia de raíces reales."
            concepto_clave_latex: "\\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = f(c) \\quad ; \\quad f(a)\\cdot f(b) < 0 \\implies \\exists c \\in (a,b): f(c)=0"
            ejemplo: "Continuidad en la curva de potencia de un aerogenerador entre arranque y corte."
            bloque_sugerido: "Pomodoro 50/10 • Continuidad y bisección"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Definición de Derivada y Reglas de Derivación"
            objetivo: "Calcular tasas instantáneas de cambio de energía, carga y temperatura."
            concepto_clave_latex: "f'(x) = \\lim_{h \\to 0}\\frac{f(x+h)-f(x)}{h} \\quad ; \\quad P(t) = \\frac{dE}{dt}"
            ejemplo: "Obtención de potencia instantánea a partir de la curva de energía acumulada."
            bloque_sugerido: "Pomodoro 50/10 • Producto y cociente"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Regla de la Cadena, Derivación Implícita y Logarítmica"
            objetivo: "Derivar funciones compuestas y relaciones termodinámicas implícitas."
            concepto_clave_latex: "\\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x) \\quad ; \\quad PV^\\gamma = C \\implies \\frac{dP}{dV} = -\\gamma\\frac{P}{V}"
            ejemplo: "Pendiente adiabática presión-volumen en compresión de gases."
            bloque_sugerido: "Práctica 45 min • Regla de la cadena"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Razones de Cambio Relacionadas y Teorema del Valor Medio"
            objetivo: "Vincular tasas temporales acopladas en sistemas hidráulicos y térmicos."
            concepto_clave_latex: "\\frac{dV}{dt} = A(h)\\frac{dh}{dt} \\quad ; \\quad f'(c) = \\frac{f(b)-f(a)}{b-a}"
            ejemplo: "Velocidad de ascenso de nivel en un embalse hidroeléctrico troncocónico."
            bloque_sugerido: "Pomodoro 50/10 • Tasas acopladas"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Regla de L'Hôpital, Criterios de Extremos y Optimización"
            objetivo: "Optimizar diseños energéticos mediante criterios de primera y segunda derivada."
            concepto_clave_latex: "f'(x^*) = 0,\\; f''(x^*) < 0 \\quad ; \\quad P_{\\max} = \\frac{V_{\\text{th}}^2}{4R_{\\text{th}}}\\;\\;(R_L = R_{\\text{th}})"
            ejemplo: "Demostración del teorema de máxima transferencia de potencia DC."
            bloque_sugerido: "Práctica 50 min • Optimización aplicada"
      - codigo: "03011813"
        nombre: "Fundamentos de Programación e IA"
        creditos: 4
        obligatoria: true
        categoria: "PROGRAMACION_IA"
        color: "#0A84FF"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Pensamiento Computacional, Algoritmos y Variables"
            objetivo: "Diseñar algoritmos secuenciales mediante diagramas de flujo, pseudocódigo y tipos de datos."
            concepto_clave_latex: "E_{\\text{kWh}} = \\frac{P_{\\text{W}}\\cdot \\Delta t_{\\text{h}}}{1000} \\quad ; \\quad T(n) = c_1 n + c_0"
            ejemplo: "Script en Python para convertir potencia horaria a energía facturable en kWh."
            bloque_sugerido: "Laboratorio 45 min • Variables y operadores"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Álgebra Booleana y Estructuras Condicionales"
            objetivo: "Implementar lógica de decisión y control operativo mediante compuertas booleanas e if/elif/else."
            concepto_clave_latex: "u(t) = (S_{\\text{PV}} > P_L) \\land (\\text{SoC} < 0.95)"
            ejemplo: "Lógica de carga/descarga automática de baterías en una microrred solar."
            bloque_sugerido: "Práctica 45 min • Condicionales anidados"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Estructuras Iterativas (For/While) y Series Numéricas"
            objetivo: "Automatizar sumatorias, balances horarios y criterios de convergencia con ciclos."
            concepto_clave_latex: "E_{\\text{día}} = \\sum_{k=0}^{23} P_k \\Delta t \\quad ; \\quad |x_{k+1} - x_k| < \\varepsilon"
            ejemplo: "Integración horaria de irradiancia solar de 24 horas en Santa Marta."
            bloque_sugerido: "Pomodoro 50/10 • Ciclos y acumuladores"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Funciones Modulares, Alcance y Recursividad"
            objetivo: "Estructurar código limpio y reutilizable mediante funciones parametrizadas."
            concepto_clave_latex: "\\eta_{\\text{global}} = f_{\\text{inv}}(f_{\\text{PV}}(G, T_c))"
            ejemplo: "Módulo de funciones Python para calcular rendimiento térmico y eléctrico."
            bloque_sugerido: "Laboratorio 45 min • Diseño modular"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Arreglos, Listas, Diccionarios y Matrices de Datos"
            objetivo: "Manipular series de tiempo energéticas mediante estructuras indexadas y vectorizadas."
            concepto_clave_latex: "\\bar{P} = \\frac{1}{N}\\sum_{i=1}^{N} P_i \\quad ; \\quad P_{\\max} = \\max_{1 \\le i \\le N} P_i"
            ejemplo: "Procesamiento de perfiles de demanda de 8760 horas anuales con listas y diccionarios."
            bloque_sugerido: "Práctica 50 min • Series temporales"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Manejo de Archivos CSV/JSON y Visualización Científica"
            objetivo: "Leer telemetría real desde archivos estructurados y graficar curvas de carga."
            concepto_clave_latex: "F_{\\text{carga}} = \\frac{P_{\\text{prom}}}{P_{\\text{pico}}} \\in (0, 1]"
            ejemplo: "Lectura de registros JSON de medidores inteligentes y cálculo del factor de carga."
            bloque_sugerido: "Laboratorio 50 min • Parsing CSV/JSON"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Métodos Numéricos Básicos: Raíces e Interpolación"
            objetivo: "Implementar bisección y Newton-Raphson para resolver ecuaciones no lineales."
            concepto_clave_latex: "x_{k+1} = x_k - \\frac{f(x_k)}{f'(x_k)}"
            ejemplo: "Solución numérica de la ecuación implícita del diodo en una celda solar."
            bloque_sugerido: "Pomodoro 50/10 • Newton-Raphson en Python"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Introducción a Ciencia de Datos y Regresión Lineal"
            objetivo: "Ajustar modelos predictivos básicos minimizando el error cuadrático medio."
            concepto_clave_latex: "\\hat{y} = w_1 x + w_0 \\quad ; \\quad \\text{MSE} = \\frac{1}{N}\\sum_{i=1}^{N}(y_i - \\hat{y}_i)^2"
            ejemplo: "Predicción de generación solar diaria a partir de horas de brillo solar."
            bloque_sugerido: "Laboratorio 50 min • Regresión supervisada"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Fundamentos de IA y Ética Computacional en Energía"
            objetivo: "Comprender el flujo de entrenamiento/validación de IA aplicada a redes inteligentes."
            concepto_clave_latex: "z = \\sum_{j=1}^{m} w_j x_j + b \\quad ; \\quad \\sigma(z) = \\frac{1}{1 + e^{-z}}"
            ejemplo: "Clasificador logístico simple para detección de anomalías de consumo eléctrico."
            bloque_sugerido: "Taller 45 min • Pipeline de IA energética"
      - codigo: "01021802"
        nombre: "General English I"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "general"
            titulo: "Personal Pronouns, Verb To Be & Academic Introductions"
            objetivo: "Presentarse formalmente en contextos universitarios usando pronombres sujeto y el verbo To Be."
            concepto_clave_latex: ""
            ejemplo: "Hello, I am Camila. I am an Energy Engineering student at Unimagdalena."
            bloque_sugerido: "Speaking Drill 35 min • Academic self-introduction & peer interview"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Personal Pronouns, Verb To Be & Academic Introductions: Communicative Purpose"
                puntos:
                  - "Subject pronouns (I, you, he, she, it, we, they) never omit the subject in English."
                  - "Verb To Be links identity, origin, major, and academic role (am / is / are)."
                  - "Use contractions (I'm, she's, we're) in spoken dialogue and full forms in formal writing."
                ejemplo: "Hello, I am Camila. I am an Energy Engineering student at Unimagdalena."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "I am -> first-year Energy Engineering student."
                  - "He / She / It is -> professor, lab equipment, or course."
                  - "You / We / They are -> classmates and research teams."
                tabla:
                  - ["Subject", "Affirmative", "Contraction"]
                  - ["I", "I am", "I'm"]
                  - ["He / She / It", "is", "he's / it's"]
                  - ["We / You / They", "are", "we're / they're"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Negative: place 'not' directly after am/is/are (is not = isn't, are not = aren't)."
                  - "Yes/No Questions: invert verb To Be + subject (Are you in Semester 1? Yes, I am)."
                  - "Never contract affirmative short answers (*Yes, I'm* is incorrect -> use 'Yes, I am')."
                ejemplo: "Is Professor Vargas in the Thermodynamics Lab? Yes, he is."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid using 'have' for age: say 'I am 18 years old', NOT 'I have 18 years'."
                  - "Always include 'it' for singular objects: 'It is a solar panel', NOT 'Is a solar panel'."
                tabla:
                  - ["Spanish Habit", "Incorrect", "Natural English"]
                  - ["Edad", "I have 19 years", "I am 19 years old"]
                  - ["Sujeto tácito", "Is in block C", "It is in Block C"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Hello, I am Camila. I am an Energy Engineering student at Unimagdalena."
                  - "Is Professor Vargas in the Thermodynamics Lab? Yes, he is."
                  - "We are in Classroom C-204 for General English I."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete: '___ they from Santa Marta?' -> 'Are they from Santa Marta?'"
                  - "Correct: 'She have 20 years' -> 'She is 20 years old.'"
                  - "Introduce yourself in 3 sentences: name, hometown, and academic program."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 2
            corte: 1
            modalidad: "general"
            titulo: "Demonstratives (This, That, These, Those) & Classroom/Lab Objects"
            objetivo: "Identificar instrumentos de aula y laboratorio según distancia y número con demostrativos y artículos."
            concepto_clave_latex: ""
            ejemplo: "This is an infrared thermometer and those are safety goggles."
            bloque_sugerido: "Vocabulary Lab 35 min • 20 classroom & engineering lab instruments"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Demonstratives (This, That, These, Those) & Classroom/Lab Objects: Communicative Purpose"
                puntos:
                  - "Near speaker: 'this' (singular) and 'these' (plural)."
                  - "Far from speaker: 'that' (singular) and 'those' (plural)."
                  - "Indefinite articles 'a' (before consonant sound) vs. 'an' (before vowel sound: an oscilloscope, a university)."
                ejemplo: "This is an infrared thermometer and those are safety goggles."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "This + singular noun: 'This multimeter is calibrated.'"
                  - "These + plural noun: 'These cables are insulated.'"
                  - "That / Those + distant items across the bench or room."
                tabla:
                  - ["Distance", "Singular", "Plural"]
                  - ["Near (here)", "this sensor", "these sensors"]
                  - ["Far (there)", "that turbine", "those turbines"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions: 'What is this?' -> 'It is an inverter.' / 'What are those?' -> 'They are batteries.'"
                  - "Negative: 'This isn't my calculator; that one on the desk is mine.'"
                  - "Pronunciation contrast: short /ɪ/ in 'this' vs. long tense /iː/ in 'these'."
                ejemplo: "Are these your lab notebooks on the workbench?"
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Choose 'a' or 'an' by SOUND, not spelling: 'a university' (/juː/), 'an hour' (silent h)."
                  - "Adjectives never take plural -s in English: 'new computers', NOT 'news computers'."
                tabla:
                  - ["Article Rule", "Sound", "Example"]
                  - ["a + consonant sound", "/j/, /w/, /p/", "a unit, a wattmeter"]
                  - ["an + vowel sound", "/a/, /ɪ/, /ʌ/", "an ammeter, an hour"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "This is an infrared thermometer and those are safety goggles."
                  - "Are these your lab notebooks on the workbench?"
                  - "That wind tunnel in the corner is for aerodynamics testing."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Fill in: '___ is ___ oscilloscope (near)' -> 'This is an oscilloscope.'"
                  - "Pluralize: 'That solar cell is efficient' -> 'Those solar cells are efficient.'"
                  - "Name 6 objects around your study desk using this/that/these/those."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 3
            corte: 1
            modalidad: "general"
            titulo: "Present Simple: Affirmative, Negative & Daily University Routines"
            objetivo: "Expresar hábitos, horarios académicos y verdades generales mediante el Presente Simple."
            concepto_clave_latex: ""
            ejemplo: "Classes at Unimagdalena start at 7:00 a.m. and finish in the afternoon."
            bloque_sugerido: "Pomodoro 40/10 • Daily academic routine & 3rd-person -s/-es accuracy"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Present Simple: Affirmative, Negative & Daily University Routines: Communicative Purpose"
                puntos:
                  - "Use Present Simple for daily study routines, timetables, and permanent scientific facts."
                  - "Third-person singular (he/she/it) adds -s, -es (watches, fixes), or -ies (studies)."
                  - "Base verb remains unchanged for I, you, we, they."
                ejemplo: "Classes at Unimagdalena start at 7:00 a.m. and finish in the afternoon."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: Subject + base verb (+s/es for he/she/it)."
                  - "Spelling -es after -ch, -sh, -ss, -x, -o: goes, teaches, mixes."
                  - "Consonant + y -> -ies: study -> studies; vowel + y -> -s: plays."
                tabla:
                  - ["Subject", "Affirmative", "Negative"]
                  - ["I / We / They", "study calculus", "do not (don't) study"]
                  - ["He / She / It", "studies calculus", "does not (doesn't) study"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Negative uses auxiliary 'don't' or 'doesn't' + BASE verb ('She doesn't attend on Fridays')."
                  - "Yes/No Questions: 'Do you take the campus bus?' / 'Does the class start at 7:00 a.m.?'"
                  - "Remove the -s from the main verb whenever 'does/doesn't' is present!"
                ejemplo: "My lab partner reviews her notes every evening before quizzes."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Incorrect: 'He doesn't works here' -> Correct: 'He doesn't work here.'"
                  - "Incorrect: 'Water boil at 100°C' -> Correct: 'Water boils at 100°C.'"
                tabla:
                  - ["Verb Ending", "3rd Person Rule", "Example"]
                  - ["-ch / -sh / -x / -o", "Add -es", "fixes, goes, washes"]
                  - ["Consonant + y", "Change y -> ies", "studies, carries"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Classes at Unimagdalena start at 7:00 a.m. and finish in the afternoon."
                  - "My lab partner reviews her notes every evening before quizzes."
                  - "A photovoltaic module converts sunlight directly into DC electricity."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Transform to negative: 'Carlos lives near campus' -> 'Carlos doesn't live near campus.'"
                  - "Ask a Yes/No question: 'Does the library open on Saturdays?'"
                  - "Write 4 sentences describing your Monday university routine."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 4
            corte: 2
            modalidad: "general"
            titulo: "Information Questions (Wh- Words: What, Where, When, Who, How)"
            objetivo: "Formular preguntas abiertas precisas para solicitar datos personales, horarios y procedimientos."
            concepto_clave_latex: ""
            ejemplo: "What time does our Programming class start on Wednesdays?"
            bloque_sugerido: "Interactive Practice 40 min • Wh- question word order & campus Q&A"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Information Questions (Wh- Words: What, Where, When, Who, How): Communicative Purpose"
                puntos:
                  - "Wh- word comes first: Wh- + Auxiliary (do/does or am/is/are) + Subject + Main Verb?"
                  - "Core question words: What (things), Where (places), When/What time (time), Who (people), Why (reason), How (manner)."
                  - "Compound Wh- phrases: How often, How many, How much, What kind of."
                ejemplo: "What time does our Programming class start on Wednesdays?"
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "With To Be: Wh- + am/is/are + subject? ('Where is the library?')"
                  - "With Action Verbs: Wh- + do/does + subject + base verb? ('When does the exam start?')"
                  - "Subject Questions with Who/What omit do/does: 'Who teaches Calculus I?'"
                tabla:
                  - ["Wh- Word", "Target Info", "Model Question"]
                  - ["Where", "Location", "Where do you study?"]
                  - ["What time", "Exact hour", "What time does lab begin?"]
                  - ["How many", "Quantity", "How many credits do you take?"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Intonation falls at the end of Wh- questions (unlike rising Yes/No questions)."
                  - "Answer 'Why...?' questions with 'Because...' ('Why do you study Energy? Because clean power matters')."
                  - "Distinguish 'What' (open choice) vs. 'Which' (limited options: 'Which group are you in, G1 or G2?')."
                ejemplo: "Where do students print technical reports on campus?"
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never forget the auxiliary 'do/does': say 'Where do you live?', NOT 'Where you live?'."
                  - "Do not invert statements inside answers: 'It starts at 8:00.'"
                tabla:
                  - ["Error", "Correction", "Why"]
                  - ["What means this?", "What does this mean?", "Needs auxiliary 'does'"]
                  - ["How you spell it?", "How do you spell it?", "Wh- + do + subject"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "What time does our Programming class start on Wednesdays?"
                  - "Where do students print technical reports on campus?"
                  - "How many subjects do first-semester students take?"
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Order: 'does / where / work / your advisor / ?' -> 'Where does your advisor work?'"
                  - "Write Wh- questions for: 'At 10:00 a.m.', 'In Lab B-105', 'Five subjects'."
                  - "Role-play a 5-question interview with a new classmate."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 5
            corte: 2
            modalidad: "general"
            titulo: "Adverbs of Frequency & Time Expressions in Schedules"
            objetivo: "Describir la frecuencia exacta de actividades académicas utilizando adverbios y expresiones de tiempo."
            concepto_clave_latex: ""
            ejemplo: "Our study group meets three times a week in the central library."
            bloque_sugerido: "Schedule Drill 35 min • Weekly study planner with frequency adverbs"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Adverbs of Frequency & Time Expressions in Schedules: Communicative Purpose"
                puntos:
                  - "Frequency scale: always (100%), usually (85%), often (70%), sometimes (50%), rarely (15%), never (0%)."
                  - "Position Rule 1: BEFORE main action verbs ('I always back up my code')."
                  - "Position Rule 2: AFTER the verb To Be ('The lab is never unlocked at night')."
                ejemplo: "Our study group meets three times a week in the central library."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Subject + Adverb + Main Verb: 'We usually review before lectures.'"
                  - "Subject + am/is/are + Adverb: 'She is always punctual.'"
                  - "Long expressions go at the end: 'twice a week', 'every Tuesday morning'."
                tabla:
                  - ["Adverb", "Approx. %", "Sentence Position"]
                  - ["always / usually", "100% / 85%", "Before main verb / after Be"]
                  - ["often / sometimes", "70% / 50%", "Before main verb ('Sometimes' can lead)"]
                  - ["hardly ever / never", "10% / 0%", "With affirmative verb only"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Ask frequency with 'How often do you...?' ('How often do you use Python? Every day')."
                  - "'Never' and 'hardly ever' already carry negative meaning -> NEVER use 'don't' with them!"
                  - "In questions: 'Do you ever study in the library?'"
                ejemplo: "Professor Gómez is always available during office hours on Thursdays."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid double negatives: 'I never arrive late', NOT 'I don't never arrive late'."
                  - "Keep 'always' after 'is/are': 'He is always prepared', NOT 'He always is prepared'."
                tabla:
                  - ["Expression", "Placement", "Example"]
                  - ["Adverb (often)", "Mid-position", "We often solve exercises in pairs."]
                  - ["Phrase (twice a week)", "End of clause", "We have English class twice a week."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Our study group meets three times a week in the central library."
                  - "Professor Gómez is always available during office hours on Thursdays."
                  - "I rarely miss a morning lecture during exam weeks."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Insert 'usually': 'They are in the lab at 9' -> 'They are usually in the lab at 9.'"
                  - "Fix: 'She doesn't never forget her ID' -> 'She never forgets her ID.'"
                  - "Answer 'How often...?' for 4 study habits."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 6
            corte: 2
            modalidad: "general"
            titulo: "There is / There are: Describing Campus Facilities & Places"
            objetivo: "Describir la existencia y cantidad de espacios, equipos y servicios del campus universitario."
            concepto_clave_latex: ""
            ejemplo: "There are twelve photovoltaic panels on the roof of the research center."
            bloque_sugerido: "Campus Mapping 35 min • Describing university buildings & laboratories"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "There is / There are: Describing Campus Facilities & Places: Communicative Purpose"
                puntos:
                  - "Use 'There is' (There's) for singular countable nouns and uncountable nouns."
                  - "Use 'There are' for plural countable nouns (no contraction in standard writing)."
                  - "Pair with 'a/an' (singular), 'some' (affirmative plural), and 'any' (negative & questions)."
                ejemplo: "There are twelve photovoltaic panels on the roof of the research center."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Singular: 'There is a solar microgrid on campus.'"
                  - "Plural: 'There are four computer labs in the Engineering building.'"
                  - "Uncountable: 'There is free Wi-Fi in the study hall.'"
                tabla:
                  - ["Form", "Singular / Uncountable", "Plural"]
                  - ["Affirmative", "There is a / some...", "There are some / 12..."]
                  - ["Negative", "There isn't a / any...", "There aren't any..."]
                  - ["Question", "Is there a / any...?", "Are there any...?"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Short answers: 'Is there an auditorium nearby? Yes, there is / No, there isn't.'"
                  - "'How many...?': 'How many workstations are there in Lab 3? There are twenty-four.'"
                  - "Negative alternative with 'no': 'There are no available outlets here.'"
                ejemplo: "Is there a quiet reading room on the second floor? Yes, there is."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Spanish 'Hay' covers both singular and plural; English MUST match number (There is vs. There are)!"
                  - "Do not confuse 'There are' (existence) with 'They are' (identifying previously mentioned items)."
                tabla:
                  - ["Spanish 'Hay'", "Incorrect", "Correct English"]
                  - ["Hay 3 bancos", "There is three benches", "There are three benches"]
                  - ["¿Hay cafetería?", "Have a cafeteria?", "Is there a cafeteria?"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "There are twelve photovoltaic panels on the roof of the research center."
                  - "Is there a quiet reading room on the second floor? Yes, there is."
                  - "There aren't any classes scheduled after 9:00 p.m. on Saturdays."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete: '___ ___ any oscilloscopes in this room?' -> 'Are there any...?'"
                  - "Translate: 'Hay cinco laboratorios en el bloque' -> 'There are five labs in the building.'"
                  - "Describe Unimagdalena campus facilities in 5 sentences."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 7
            corte: 2
            modalidad: "general"
            titulo: "Prepositions of Place, Time & Movement (In, On, At, Across, Through)"
            objetivo: "Ubicar eventos en el tiempo y describir posiciones o desplazamientos espaciales con exactitud."
            concepto_clave_latex: ""
            ejemplo: "Our Calculus midterm is on Wednesday at 8:00 a.m. in Room S-301."
            bloque_sugerido: "Precision Drill 35 min • In/On/At pyramid & spatial movement diagrams"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Prepositions of Place, Time & Movement (In, On, At, Across, Through): Communicative Purpose"
                puntos:
                  - "AT = specific point/exact time (at 7:30 a.m., at the entrance, at the desk, at night)."
                  - "ON = surface/days & dates (on Monday, on October 30th, on the wall, on the second floor)."
                  - "IN = enclosed space/months, years, seasons & parts of day (in 2026, in May, in the lab, in the morning)."
                ejemplo: "Our Calculus midterm is on Wednesday at 8:00 a.m. in Room S-301."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Place: under, next to, between A and B, behind, in front of, opposite."
                  - "Time pyramid: AT (hour) -> ON (day/date) -> IN (month/year/century)."
                  - "Movement: into, out of, across (surface), through (3D tunnel/pipe), towards."
                tabla:
                  - ["Preposition", "Time Use", "Place / Movement Use"]
                  - ["AT", "at 8:00, at noon", "at the door, at campus"]
                  - ["ON", "on Friday, on May 5", "on the table, on Floor 2"]
                  - ["IN", "in July, in 2026", "in the room, in Colombia"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Movement contrast: 'walk across the courtyard' (2D open area) vs. 'flow through a pipe' (enclosed 3D space)."
                  - "No preposition before 'next', 'last', 'every', 'this': 'See you next Tuesday' (NOT 'on next Tuesday')."
                  - "Fixed expressions: 'at the moment', 'on time' (punctual), 'in time' (early enough)."
                ejemplo: "Cooling water circulates through the heat exchanger tubes."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid 'in Monday' -> always use 'ON Monday'."
                  - "Distinguish 'in front of' (delante de) vs. 'opposite/across from' (enfrente, cara a cara)."
                tabla:
                  - ["Movement Verb + Prep", "Visual Path", "Engineering / Campus Example"]
                  - ["go into / out of", "Enter / exit enclosure", "Walk into the auditorium"]
                  - ["flow through", "Inside a channel/pipe", "Steam flows through the nozzle"]
                  - ["walk across", "Side to side on surface", "Walk across the main plaza"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Our Calculus midterm is on Wednesday at 8:00 a.m. in Room S-301."
                  - "Cooling water circulates through the heat exchanger tubes."
                  - "The student lounge is between the cafeteria and the bookstore."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Fill in: '___ Monday morning ___ 7:00 ___ October' -> 'on / at / in'."
                  - "Choose: 'Air passes (across / through) the turbine blades' -> 'through'."
                  - "Give walking directions from the campus gate to your classroom."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 8
            corte: 3
            modalidad: "general"
            titulo: "Possessive Adjectives, Saxon Genitive ('s) & Family/Team Relations"
            objetivo: "Expresar pertenencia, autoría y relaciones de equipo usando adjetivos posesivos y genitivo sajón."
            concepto_clave_latex: ""
            ejemplo: "Our team's prototype won first place at the faculty showcase."
            bloque_sugerido: "Grammar Focus 35 min • Possessive forms & team role descriptions"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Possessive Adjectives, Saxon Genitive ('s) & Family/Team Relations: Communicative Purpose"
                puntos:
                  - "Possessive adjectives precede nouns and agree with the OWNER (my, your, his, her, its, our, their)."
                  - "Saxon Genitive ('s) shows ownership for people, teams, and time: 'Maria's laptop', 'today's lecture'."
                  - "Plural nouns ending in -s take only an apostrophe: 'the students' projects'."
                ejemplo: "Our team's prototype won first place at the faculty showcase."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Singular owner + 's: 'the professor's office'."
                  - "Plural regular + ': 'the engineers' safety helmets'."
                  - "Irregular plural + 's: 'children's books', 'men's team'."
                tabla:
                  - ["Subject", "Possessive Adjective", "Possessive Pronoun"]
                  - ["I / You", "my / your report", "mine / yours"]
                  - ["He / She / It", "his / her / its value", "his / hers / —"]
                  - ["We / They", "our / their lab", "ours / theirs"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Ask ownership with 'Whose...?': 'Whose multimeter is this? It's Javier's (or It's his).'"
                  - "For inanimate parts/systems, prefer 'of' or noun compounds: 'the efficiency of the cycle' / 'system voltage'."
                  - "Distinguish 'its' (possessive, no apostrophe) vs. 'it's' (it is)!"
                ejemplo: "Whose safety glasses are these? They are Sofía's."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Spanish 'su' can mean his, her, its, your, or their -> match the actual owner in English!"
                  - "Never put 'the' before a possessive name: 'Camila's code', NOT 'the Camila's code'."
                tabla:
                  - ["Confusion Pair", "Meaning", "Correct Sentence"]
                  - ["its vs. it's", "Possessive vs. It is", "The motor lost its torque; it's overheating."]
                  - ["Whose vs. Who's", "Ownership vs. Who is", "Whose notebook is this? Who's presenting?"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Our team's prototype won first place at the faculty showcase."
                  - "Whose safety glasses are these? They are Sofía's."
                  - "Each sensor records its temperature data every ten seconds."
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Rewrite: 'The lab reports of the students' -> 'The students' lab reports.'"
                  - "Choose: 'Andrés forgot (his / her / their) charger' -> 'his'."
                  - "Describe 4 roles and belongings in your project group."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 9
            corte: 3
            modalidad: "general"
            titulo: "Can / Can't for Abilities, Permissions & Basic Lab Rules"
            objetivo: "Comunicar habilidades técnicas, permisos institucionales y normas básicas de seguridad en laboratorio."
            concepto_clave_latex: ""
            ejemplo: "Students can access scientific journals using their Unimagdalena credentials."
            bloque_sugerido: "Lab Safety Briefing 35 min • Writing & speaking 8 laboratory rules"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Can / Can't for Abilities, Permissions & Basic Lab Rules: Communicative Purpose"
                puntos:
                  - "Modal 'can' expresses ability ('I can code in Python'), possibility, and permission ('You can borrow 3 books')."
                  - "'Cannot' / 'can't' expresses inability or strict prohibition ('You can't enter without goggles')."
                  - "Modal rule: 'can' never changes form (no -s) and is followed directly by the base verb (no 'to')."
                ejemplo: "Students can access scientific journals using their Unimagdalena credentials."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: Subject + can + base verb."
                  - "Negative: Subject + cannot (can't) + base verb."
                  - "Question: Can + subject + base verb? ('Can you share your screen?')"
                tabla:
                  - ["Function", "Affirmative (Can)", "Negative (Can't / Cannot)"]
                  - ["Ability", "She can solve circuits.", "He can't read schematics yet."]
                  - ["Permission / Rule", "You can use calculators.", "You can't eat in the lab."]
                  - ["Polite Request", "Can you repeat that?", "—"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Pronunciation tip: unstressed 'can' sounds like /kən/ before a verb; negative 'can't' has a clear stressed vowel /kænt/ or /kɑːnt/."
                  - "Polite upgrade: 'Could you please explain Slide 3?' sounds more formal with professors."
                  - "Short answers: 'Can we submit in PDF? Yes, you can / No, you can't.'"
                ejemplo: "You cannot touch energized terminals during circuit experiments."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never write 'to' after can: 'I can swim', NOT 'I can to swim'."
                  - "Never write 'can' as two words in formal negative: write 'cannot', NOT 'can not'."
                tabla:
                  - ["Common Error", "Why It Fails", "Correct Form"]
                  - ["He cans speak English", "Modals take no -s", "He can speak English"]
                  - ["We can to test now", "No 'to' after modal", "We can test now"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Students can access scientific journals using their Unimagdalena credentials."
                  - "You cannot touch energized terminals during circuit experiments."
                  - "Can you export the chart as a vector PDF?"
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Correct: 'She cans program microcontrollers' -> 'She can program microcontrollers.'"
                  - "Write 3 lab safety rules using 'can' and 'cannot'."
                  - "Practice polite classroom requests with 'Can/Could you...?'"
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 10
            corte: 3
            modalidad: "general"
            titulo: "Present Continuous: Actions Happening Now vs. General Habits"
            objetivo: "Contrastar acciones en progreso en el momento de hablar frente a rutinas habituales."
            concepto_clave_latex: ""
            ejemplo: "Right now, our group is measuring the open-circuit voltage of a solar panel."
            bloque_sugerido: "Contrastive Workshop 40 min • Live lab commentary vs. general facts"
            slides:
              - numero: 1
                seccion: "CEFR A1 • CORE CONCEPT"
                titulo: "Present Continuous: Actions Happening Now vs. General Habits: Communicative Purpose"
                puntos:
                  - "Present Continuous = am / is / are + verb-ing for actions happening right now or temporary projects this semester."
                  - "Present Simple = permanent habits, schedules, and scientific laws."
                  - "Stative verbs (know, understand, believe, need, want, belong) normally DO NOT use -ing!"
                ejemplo: "Right now, our group is measuring the open-circuit voltage of a solar panel."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Spelling -ing: drop silent -e (make -> making), double final CVC stressed consonant (run -> running)."
                  - "Signal words NOW: right now, at the moment, currently, today, Look!, Listen!."
                  - "Signal words HABIT: every day, usually, on Mondays, always."
                tabla:
                  - ["Aspect", "Present Simple", "Present Continuous"]
                  - ["Use", "Routine / Permanent law", "Action in progress / Temporary"]
                  - ["Form", "cali-brates / study", "is calibrating / are studying"]
                  - ["Markers", "every week, always", "right now, this week"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions: 'What are you working on right now?' vs. 'What do you study at university?'"
                  - "Negative: 'The inverter isn't generating power right now because it's cloudy.'"
                  - "Stative check: say 'I understand the formula now', NOT 'I am understanding the formula'."
                ejemplo: "Normally we study in the library, but this week we are preparing our poster."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never omit 'am/is/are' before -ing: 'She is presenting', NOT 'She presenting'."
                  - "Do not double final consonant when stress is on 1st syllable: 'open -> opening', 'listen -> listening'."
                tabla:
                  - ["Verb Type", "Example Verbs", "Correct Usage"]
                  - ["Dynamic (Action)", "measure, build, test", "We are testing the battery now."]
                  - ["Stative (Mental)", "know, need, prefer", "We need a voltmeter right now."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Right now, our group is measuring the open-circuit voltage of a solar panel."
                  - "Normally we study in the library, but this week we are preparing our poster."
                  - "Do you understand the difference between power and energy?"
                ejemplo: "Academic Register (CEFR A1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'Listen! The turbine (spins / is spinning) faster now' -> 'is spinning'."
                  - "Fix: 'I am needing help with Question 4' -> 'I need help with Question 4.'"
                  - "Write 2 pairs of sentences contrasting your usual routine vs. this week."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 11
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Cardinals, Decimals, Fractions & Scientific Notation"
            objetivo: "Leer en voz alta cifras decimales, fracciones y notación científica con precisión en inglés técnico."
            concepto_clave_latex: "\\pi \\approx 3.1416 \\quad ; \\quad \\eta = \\frac{3}{4} = 0.75 \\quad ; \\quad N_A = 6.022 \\times 10^{23}"
            verbalizacion_ingles: "• 3.1416 -> \"three point one four one six\" (read each digit individually after \"point\").\n• 3/4 -> \"three quarters\" (or \"three fourths\"); 0.75 -> \"zero point seven five\" (or \"naught point seven five\").\n• 6.022 × 10^23 -> \"six point zero two two times ten to the power of twenty-three\" (or \"ten to the twenty-third\")."
            ejemplo: "En una exposición de laboratorio: una irradiancia de 1.05 × 10^3 W/m² se lee 'one point zero five times ten to the third watts per square meter'."
            bloque_sugerido: "Oral Pronunciation 30 min • Reading 15 engineering constants aloud"
          - numero_tema: 12
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Basic Arithmetic Operations & Equality Symbols"
            objetivo: "Verbalizar operaciones aritméticas fundamentales, igualdades, aproximaciones y cocientes en inglés."
            concepto_clave_latex: "a + b = c \\quad ; \\quad x - y \\neq 0 \\quad ; \\quad p \\cdot q \\approx r \\quad ; \\quad Q = \\frac{u}{v}"
            verbalizacion_ingles: "• a + b = c -> \"a plus b equals c\" (or \"is equal to c\").\n• x - y ≠ 0 -> \"x minus y is not equal to zero\".\n• p · q ≈ r -> \"p times q (or p multiplied by q) is approximately equal to r\".\n• u / v -> \"u divided by v\" or \"u over v\"."
            ejemplo: "Lectura de balance básico de potencia pérdidas: P_in - P_loss = P_out -> 'P in minus P loss equals P out'."
            bloque_sugerido: "Equation Reading 30 min • Dictating algebraic balances to a partner"
          - numero_tema: 13
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Powers, Roots & Subscripts/Superscripts"
            objetivo: "Pronunciar potencias, raíces enésimas y subíndices de entrada/salida en variables energéticas."
            concepto_clave_latex: "A = x^2 \\quad ; \\quad V_c = L^3 \\quad ; \\quad y = x^n \\quad ; \\quad r = \\sqrt{x} \\quad ; \\quad b = \\sqrt[n]{a} \\quad ; \\quad \\Delta T = T_2 - T_1"
            verbalizacion_ingles: "• x^2 -> \"x squared\"  |  L^3 -> \"L cubed\"  |  x^n -> \"x to the n-th power\" (or \"x to the n\").\n• √x -> \"the square root of x\"  |  ³√a -> \"the cube root of a\"  |  ⁿ√a -> \"the n-th root of a\".\n• T_2 - T_1 -> \"T sub two minus T sub one\"  |  V_in, V_out -> \"V sub in\" (or simply \"V in\") and \"V out\"."
            ejemplo: "En conversión fotovoltaica, V_oc y I_sc se leen 'V sub o c (open-circuit voltage)' e 'I sub s c (short-circuit current)'."
            bloque_sugerido: "Notation Drill 30 min • Superscripts, roots & subscripted state variables"
          - numero_tema: 14
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Geometric Shapes, Angles & Greek Alphabet in Engineering"
            objetivo: "Dominar la pronunciación inglesa del alfabeto griego y relaciones trigonométricas en ingeniería."
            concepto_clave_latex: "\\alpha, \\beta, \\theta, \\Delta, \\lambda, \\mu, \\rho, \\sigma, \\omega, \\Omega \\quad ; \\quad \\sin(\\theta) = \\frac{\\text{Opposite}}{\\text{Hypotenuse}}"
            verbalizacion_ingles: "• Greek letters in English: α \"AL-fuh\", β \"BAY-tuh\" (US) / \"BEE-tuh\" (UK), θ \"THAY-tuh\", Δ \"DEL-tuh\", λ \"LAM-duh\" (silent b), μ \"MYOO\", ρ \"ROH\", σ \"SIG-muh\", ω \"oh-MAY-guh\", Ω \"oh-MAY-guh / ohms\".\n• sin(θ) = Opposite / Hypotenuse -> \"sine of theta equals the opposite side over the hypotenuse\"."
            ejemplo: "Lectura del ángulo de inclinación solar β ('tilt angle beta') y acimut γ ('azimuth angle gamma') en colectores solares."
            bloque_sugerido: "Phonetics Lab 30 min • Greek symbols & trigonometry pronunciation"
          - numero_tema: 15
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "SI Base Units & Metric Prefixes"
            objetivo: "Verbalizar unidades del Sistema Internacional, prefijos métricos y unidades compuestas de energía."
            concepto_clave_latex: "1\\text{ GW} = 10^3\\text{ MW} = 10^6\\text{ kW} \\quad ; \\quad C = 47\\,\\mu\\text{F} \\quad ; \\quad c_p = 4186\\text{ J/(kg}\\cdot\\text{K)}"
            verbalizacion_ingles: "• kW -> \"kilowatts\", MW -> \"megawatts\", GW -> \"gigawatts\" (/ˈɡɪɡəwɒts/).\n• mA -> \"milliamperes\" (or \"milliamps\"), μF -> \"microfarads\", kPa -> \"kilopascals\".\n• J/(kg·K) -> \"joules per kilogram kelvin\" (use \"per\" for the division slash /)."
            ejemplo: "Lectura del calor específico del agua: 'four thousand one hundred eighty-six joules per kilogram kelvin'."
            bloque_sugerido: "Unit Fluency 30 min • Reading datasheet specifications in SI units"
          - numero_tema: 16
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Temperature Scales & SI–Imperial Energy Unit Conversions"
            objetivo: "Expresar conversiones entre escalas térmicas (Celsius, Kelvin, Fahrenheit) y unidades BTU, kWh y hp."
            concepto_clave_latex: "T_{\\text{K}} = T_{^\\circ\\text{C}} + 273.15 \\quad ; \\quad T_{^\\circ\\text{F}} = \\frac{9}{5}T_{^\\circ\\text{C}} + 32 \\quad ; \\quad 1\\text{ kWh} = 3.6\\text{ MJ}"
            verbalizacion_ingles: "• T_K = T_°C + 273.15 -> \"Temperature in kelvins equals temperature in degrees Celsius plus two hundred seventy-three point one five\" (note: say \"kelvins\", NOT \"degrees Kelvin\").\n• 1 kWh = 3.6 MJ -> \"one kilowatt-hour equals three point six megajoules\"."
            ejemplo: "Conversión rápida de placas técnicas estadounidenses de aires acondicionados (BTU/h y hp) a kilovatios térmicos y eléctricos."
            bloque_sugerido: "Conversion Practice 30 min • Reading US/IEC equipment nameplates in English"
      - codigo: "04011822"
        nombre: "Introducción a la Ingeniería Energética"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Conceptos de Energía, Potencia, Unidades y Escalas"
            objetivo: "Dominar las magnitudes energéticas fundamentales desde julios hasta teravatios-hora y TEP."
            concepto_clave_latex: "1\\text{ kWh} = 3.6\\text{ MJ} \\quad ; \\quad 1\\text{ TEP} = 41.868\\text{ GJ} \\quad ; \\quad P = \\frac{dE}{dt}"
            ejemplo: "Conversión de la producción anual de una central hidráulica de GWh a TJ y TEP."
            bloque_sugerido: "Pomodoro 40/10 • Factores de conversión SI"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Matriz Energética Mundial y Colombiana (UPME)"
            objetivo: "Analizar oferta primaria, consumo final por sectores y participación renovable en Colombia."
            concepto_clave_latex: "I_E = \\frac{E_{\\text{total}}}{\\text{PIB}} \\quad ; \\quad \\%_{\\text{FNCER}} = \\frac{E_{\\text{solar}}+E_{\\text{eólica}}+E_{\\text{biomasa}}}{E_{\\text{SIN}}}\\times 100\\%"
            ejemplo: "Cálculo de intensidad energética y participación hídrica/térmica/solar en el SIN."
            bloque_sugerido: "Lectura Activa 45 min • Balance UPME"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Fuentes Convencionales vs. Renovables (FNCER)"
            objetivo: "Comparar principios físicos, densidad de potencia y disponibilidad de recursos primarios."
            concepto_clave_latex: "F_p = \\frac{E_{\\text{generada}}}{P_{\\text{nominal}}\\cdot 8760\\text{ h}}"
            ejemplo: "Comparación del factor de planta solar (~22%), eólico en La Guajira (~50%) e hidráulico."
            bloque_sugerido: "Taller 45 min • Factores de planta"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Cadena de Valor de la Energía y Eficiencia en Cascada"
            objetivo: "Evaluar pérdidas en extracción, conversión, transporte, distribución y uso final."
            concepto_clave_latex: "\\eta_{\\text{cadena}} = \\eta_1 \\cdot \\eta_2 \\cdot \\eta_3 \\cdots \\eta_n = \\prod_{k=1}^{n}\\eta_k"
            ejemplo: "Eficiencia total pozo-a-rueda de un vehículo eléctrico vs. combustión interna."
            bloque_sugerido: "Pomodoro 45/10 • Diagramas de Sankey"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Cambio Climático, Huella de Carbono y Acuerdos Globales"
            objetivo: "Cuantificar emisiones de GEI asociadas al consumo de combustibles y electricidad."
            concepto_clave_latex: "m_{\\text{CO}_2} = \\sum_{i} E_i \\cdot FE_i \\quad [\\text{tCO}_2\\text{e}]"
            ejemplo: "Estimación de emisiones evitadas al instalar 500 kWp fotovoltaicos en el campus."
            bloque_sugerido: "Práctica 40 min • Factores de emisión"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Transición Energética, Descarbonización y ODS 7"
            objetivo: "Articular los pilares de seguridad, equidad y sostenibilidad (Trilema Energético)."
            concepto_clave_latex: "\\Delta E_{\\text{ahorro}} = E_{\\text{base}} - E_{\\text{eficiente}} \\quad ; \\quad \\eta_{\\text{ODS7}} \\ge \\eta_{\\text{ref}}"
            ejemplo: "Evaluación de soluciones solares autónomas para Zonas No Interconectadas (ZNI)."
            bloque_sugerido: "Estudio de Caso 45 min • ZNI Caribe"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Introducción al Almacenamiento e Hidrógeno Verde"
            objetivo: "Identificar el rol de baterías BESS, bombeo hidráulico e hidrógeno en redes modernas."
            concepto_clave_latex: "E_{\\text{útil}} = C_{\\text{nom}}\\cdot V_{\\text{nom}}\\cdot \\text{DoD}\\cdot \\eta_{\\text{rt}}"
            ejemplo: "Dimensionamiento preliminar de autonomía nocturna para un puesto de salud rural."
            bloque_sugerido: "Pomodoro 45/10 • Autonomía BESS"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Marco Institucional y Ética del Ingeniero Energético"
            objetivo: "Reconocer entidades del sector (Minenergía, UPME, CREG, XM, IPSE) y código ético COPNIA."
            concepto_clave_latex: "CU = G + T + D + Cv + PR + R \\quad [\\$/\\text{kWh}]"
            ejemplo: "Desglose de los componentes del costo unitario (CU) en una factura eléctrica real."
            bloque_sugerido: "Taller 40 min • Estructura tarifaria"
      - codigo: "01011801"
        nombre: "Procesos Lectores, Escriturales y Orales"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Comprensión Lectora: Niveles Literal, Inferencial y Crítico"
            objetivo: "Desarrollar estrategias de lectura analítica sobre textos académicos y divulgación científica."
            concepto_clave_latex: "I_{\\text{lectura}} = \\text{Literal} \\to \\text{Inferencial} \\to \\text{Crítico-Intertextual}"
            ejemplo: "Análisis crítico de un informe sobre transición energética en el Caribe colombiano."
            bloque_sugerido: "Lectura Crítica 40 min • Mapeo de tesis"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Macroestructura y Microestructura del Texto Académico"
            objetivo: "Identificar tema, idea principal, progresión temática y mecanismos de cohesión."
            concepto_clave_latex: "P_{\\text{coherencia}} = \\text{Tema Central} + \\sum_{k=1}^{n}\\text{Subtema}_k"
            ejemplo: "Descomposición de un artículo de ingeniería en introducción, desarrollo y cierre."
            bloque_sugerido: "Taller 40 min • Cohesión y conectores"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Tipologías Textuales: Expositiva, Explicativa y Argumentativa"
            objetivo: "Distinguir propósitos comunicativos y estructuras retóricas en géneros universitarios."
            concepto_clave_latex: "\\text{Argumento} = \\text{Tesis} + \\text{Evidencia Empírica} + \\text{Garantía}"
            ejemplo: "Construcción de argumentos técnicos respaldados por cifras de la UPME."
            bloque_sugerido: "Práctica 40 min • Matriz argumentativa"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Búsqueda Bibliográfica y Citación Académica (APA / IEEE)"
            objetivo: "Gestionar fuentes arbitradas y aplicar normas éticas de citación evitando el plagio."
            concepto_clave_latex: "\\text{Similitud}_{\\text{Turnitin}} \\le 15\\% \\quad ; \\quad [k] \\in \\text{IEEE}"
            ejemplo: "Formateo correcto de 5 referencias reales sobre energías renovables en estilo IEEE."
            bloque_sugerido: "Laboratorio 45 min • Gestores y citas"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Planeación y Escritura del Ensayo Argumentativo"
            objetivo: "Redactar ensayos universitarios con tesis clara, párrafos deductivos y contrargumentación."
            concepto_clave_latex: "T_{\\text{ensayo}} = T_{\\text{tesis}} + \\sum_{i=1}^n A_i + C_{\\text{síntesis}}"
            ejemplo: "Redacción de un ensayo breve sobre retos socioambientales de parques eólicos."
            bloque_sugerido: "Escritura 50 min • Borrador y rúbrica"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "El Informe Técnico y el Resumen Ejecutivo (Abstract)"
            objetivo: "Estructurar reportes de laboratorio con precisión léxica, impersonalidad y concisión."
            concepto_clave_latex: "\\text{Resumen} \\le 250\\text{ palabras}: \\text{Objetivo} + \\text{Método} + \\text{Resultado} + \\text{Conclusión}"
            ejemplo: "Síntesis ejecutiva de una práctica de medición eléctrica en 180 palabras."
            bloque_sugerido: "Taller 45 min • Edición de informes"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Comunicación Oral Académica, Voz y Lenguaje No Verbal"
            objetivo: "Dominar proyección vocal, ritmo, postura y manejo escénico en exposiciones."
            concepto_clave_latex: "E_{\\text{oral}} = f(\\text{Claridad Verbal},\\; \\text{Prosodia},\\; \\text{Kinésica})"
            ejemplo: "Preparación de una intervención oral de 3 minutos sin lectura literal de diapositivas."
            bloque_sugerido: "Práctica Oral 35 min • Discurso técnico"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Diseño de Apoyos Visuales y Defensa ante Audiencias"
            objetivo: "Integrar diapositivas minimalistas con discurso estructurado y respuesta solvente a preguntas."
            concepto_clave_latex: "R_{\\text{slide}} \\le 6\\text{ líneas} \\quad ; \\quad T_{\\text{exposición}} \\approx 1.5\\text{ min/diapositiva}"
            ejemplo: "Defensa oral de un póster de primer semestre ante docentes y pares."
            bloque_sugerido: "Simulacro 45 min • Pitch y preguntas"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Análisis Dimensional, Vectores y Sistemas de Unidades"
            objetivo: "Verificar homogeneidad dimensional y operar vectores de posición y fuerza en 3D."
            concepto_clave_latex: "\\vec{A} = A_x\\hat{i} + A_y\\hat{j} + A_z\\hat{k} \\quad ; \\quad \\vec{A}\\cdot\\vec{B} = |\\vec{A}||\\vec{B}|\\cos\\theta"
            ejemplo: "Descomposición vectorial de cargas de viento sobre la torre de un aerogenerador."
            bloque_sugerido: "Pomodoro 50/10 • Vectores 3D"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Cinemática Rectilínea y Movimiento en Dos Dimensiones"
            objetivo: "Describir posición, velocidad y aceleración instantánea mediante cálculo diferencial e integral."
            concepto_clave_latex: "\\vec{v} = \\frac{d\\vec{r}}{dt},\\;\\; \\vec{a} = \\frac{d\\vec{v}}{dt} \\quad ; \\quad y(x) = x\\tan\\theta_0 - \\frac{gx^2}{2v_0^2\\cos^2\\theta_0}"
            ejemplo: "Trayectoria de un chorro libre de agua saliendo de un inyector hacia una rueda Pelton."
            bloque_sugerido: "Práctica 50 min • Cinemática vectorial"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Movimiento Circular Uniforme y No Uniforme"
            objetivo: "Relacionar variables angulares con aceleración tangencial y centrípeta en rotores."
            concepto_clave_latex: "a_c = \\frac{v^2}{R} = \\omega^2 R \\quad ; \\quad a_t = \\alpha R \\quad ; \\quad v = \\omega R"
            ejemplo: "Velocidad en la punta de pala (tip-speed) y aceleración centrípeta en turbinas eólicas."
            bloque_sugerido: "Pomodoro 50/10 • Cinemática rotacional"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Leyes de Newton, Diagramas de Cuerpo Libre y Fricción"
            objetivo: "Formular ecuaciones de equilibrio y dinámica traslacional con fuerzas de rozamiento."
            concepto_clave_latex: "\\sum \\vec{F} = m\\vec{a} \\quad ; \\quad f_s \\le \\mu_s N \\quad ; \\quad f_k = \\mu_k N"
            ejemplo: "Análisis de fuerzas de anclaje en estructuras solares inclinadas sobre cubierta."
            bloque_sugerido: "Pomodoro 50/10 • 6 DCL con fricción"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Trabajo Mecánico, Energía Cinética y Potencia"
            objetivo: "Aplicar el teorema trabajo-energía para fuerzas variables y cuantificar potencia mecánica."
            concepto_clave_latex: "W = \\int_{r_1}^{r_2}\\vec{F}\\cdot d\\vec{r} = \\Delta K = \\frac{1}{2}mv_2^2 - \\frac{1}{2}mv_1^2 \\quad ; \\quad P = \\vec{F}\\cdot\\vec{v}"
            ejemplo: "Potencia mecánica requerida por una banda transportadora de biomasa."
            bloque_sugerido: "Práctica 45 min • Integrales de trabajo"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Fuerzas Conservativas y Conservación de la Energía"
            objetivo: "Resolver sistemas mecánicos acoplados considerando energía potencial y pérdidas disipativas."
            concepto_clave_latex: "\\Delta K + \\Delta U_g + \\Delta U_e = W_{\\text{nc}} \\quad ; \\quad \\vec{F}_c = -\\nabla U"
            ejemplo: "Conversión de cabeza potencial mgh en energía cinética en una central de bombeo."
            bloque_sugerido: "Pomodoro 50/10 • Balance energético"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Cantidad de Movimiento Lineal, Impulso y Colisiones"
            objetivo: "Aplicar conservación del momentum lineal e impulso de chorros sobre álabes."
            concepto_clave_latex: "\\vec{J} = \\int_{t_1}^{t_2}\\vec{F}\\,dt = \\Delta\\vec{p} \\quad ; \\quad F_x = \\dot{m}(v_{1x} - v_{2x})"
            ejemplo: "Fuerza hidrodinámica ejercida por un chorro de alta velocidad sobre cangilones Pelton."
            bloque_sugerido: "Práctica 50 min • Impulso y momentum"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Dinámica Rotacional, Momento de Inercia y Torque"
            objetivo: "Calcular momentos de inercia, aceleración angular y energía almacenada en volantes."
            concepto_clave_latex: "\\sum \\tau_z = I\\alpha_z \\quad ; \\quad I = \\int r^2\\,dm \\quad ; \\quad K_{\\text{rot}} = \\frac{1}{2}I\\omega^2 \\quad ; \\quad P = \\tau\\omega"
            ejemplo: "Almacenamiento cinético en un volante de inercia (Flywheel ESS) a 12,000 rpm."
            bloque_sugerido: "Pomodoro 50/10 • Torque e inercia"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Momento Angular y Equilibrio Estático de Cuerpos Rígidos"
            objetivo: "Garantizar estabilidad traslacional y rotacional de estructuras y ejes de transmisión."
            concepto_clave_latex: "\\sum \\vec{F} = \\vec{0},\\;\\; \\sum \\vec{\\tau} = \\vec{0} \\quad ; \\quad \\frac{d\\vec{L}}{dt} = \\sum\\vec{\\tau}_{\\text{ext}}"
            ejemplo: "Reacciones en cojinetes del eje principal de un grupo turbogenerador."
            bloque_sugerido: "Taller 50 min • Estática de estructuras"
      - codigo: "03041819"
        nombre: "Fundamentos de la Electricidad I"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Variables Eléctricas: Carga, Corriente, Tensión y Potencia"
            objetivo: "Aplicar la convención pasiva de signos para distinguir elementos consumidores y generadores."
            concepto_clave_latex: "i(t) = \\frac{dq}{dt},\\;\\; p(t) = v(t)i(t),\\;\\; w = \\int_{t_0}^{t} p(\\tau)\\,d\\tau"
            ejemplo: "Balance instantáneo de potencia durante carga y descarga de una celda LFP."
            bloque_sugerido: "Pomodoro 45/10 • Convención pasiva"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ley de Ohm, Resistividad Térmica y Conductancia"
            objetivo: "Relacionar resistencia eléctrica con geometría del conductor y coeficiente térmico."
            concepto_clave_latex: "V = I R \\quad ; \\quad R(T) = \\rho_0\\frac{L}{A}[1 + \\alpha(T - T_0)] \\quad ; \\quad P_J = I^2 R = \\frac{V^2}{R}"
            ejemplo: "Caída de tensión y pérdidas Joule en acometidas DC solares expuestas a 55 °C."
            bloque_sugerido: "Práctica 45 min • Dimensionamiento DC"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Leyes de Kirchhoff (LCK/LVK) y Divisores"
            objetivo: "Plantear ecuaciones de conservación de carga nodal y energía en lazos cerrados."
            concepto_clave_latex: "\\sum_{k=1}^{n} i_k = 0 \\quad ; \\quad \\sum_{m=1}^{M} v_m = 0 \\quad ; \\quad V_x = V_s\\frac{R_x}{R_{\\text{eq}}}"
            ejemplo: "Acondicionamiento de sensores resistivos PT100 mediante divisores de tensión."
            bloque_sugerido: "Pomodoro 50/10 • LCK y LVK"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Reducción Serie-Paralelo y Transformación Estrella-Delta"
            objetivo: "Simplificar redes resistivas puenteadas mediante equivalencias Y-Δ."
            concepto_clave_latex: "R_a = \\frac{R_1 R_2 + R_2 R_3 + R_3 R_1}{R_1} \\quad ; \\quad R_1 = \\frac{R_b R_c}{R_a + R_b + R_c}"
            ejemplo: "Equilibrio de un puente de Wheatstone usado en extensometría de palas eólicas."
            bloque_sugerido: "Práctica 45 min • Redes puenteadas"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Análisis Sistemático por Tensiones de Nodo y Mallas"
            objetivo: "Formular sistemas matriciales Gv = i y Ri = v con fuentes dependientes."
            concepto_clave_latex: "G\\vec{v}_n = \\vec{i}_s \\quad ; \\quad R\\vec{i}_m = \\vec{v}_s"
            ejemplo: "Cálculo de tensiones de barra en una microrred DC multipunto con dos fuentes."
            bloque_sugerido: "Pomodoro 50/10 • Supernodos y supermallas"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Linealidad, Superposición y Transformación de Fuentes"
            objetivo: "Descomponer la respuesta de redes lineales ante múltiples excitaciones independientes."
            concepto_clave_latex: "v_{\\text{total}} = \\sum_{k=1}^{N} v_k \\quad ; \\quad V_s = I_s R_s"
            ejemplo: "Contribución individual de paneles solares y batería sobre una barra común DC."
            bloque_sugerido: "Práctica 45 min • Superposición"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Teoremas de Thévenin, Norton y Máxima Potencia"
            objetivo: "Reducir redes complejas a su equivalente visto desde los terminales de carga."
            concepto_clave_latex: "V_{\\text{th}} = V_{\\text{oc}},\\;\\; R_{\\text{th}} = \\frac{V_{\\text{oc}}}{I_{\\text{sc}}},\\;\\; P_{L,\\max} = \\frac{V_{\\text{th}}^2}{4R_{\\text{th}}}"
            ejemplo: "Principio de adaptación de impedancia en seguidores MPPT fotovoltaicos."
            bloque_sugerido: "Pomodoro 50/10 • Equivalentes Thévenin"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Capacitores, Inductores y Almacenamiento de Campo"
            objetivo: "Modelar relaciones tensión-corriente diferenciales y energía almacenada en C y L."
            concepto_clave_latex: "i_C = C\\frac{dv_C}{dt},\\;\\; v_L = L\\frac{di_L}{dt},\\;\\; W_C = \\frac{1}{2}Cv^2,\\;\\; W_L = \\frac{1}{2}Li^2"
            ejemplo: "Dimensionamiento del banco capacitivo del enlace DC de un inversor solar."
            bloque_sugerido: "Práctica 45 min • Dualidad L-C"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Circuitos Transitorios de Primer Orden RC y RL"
            objetivo: "Obtener la respuesta natural y al escalón mediante constantes de tiempo τ."
            concepto_clave_latex: "x(t) = x(\\infty) + [x(t_0^+) - x(\\infty)]e^{-(t-t_0)/\\tau} \\quad (\\tau_{RC}=RC,\\; \\tau_{RL}=L/R)"
            ejemplo: "Corriente de energización y extinción de arco en bobinas de relés de protección."
            bloque_sugerido: "Pomodoro 50/10 • Transitorios RC y RL"
      - codigo: "01021803"
        nombre: "General English II"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "general"
            titulo: "Past Simple: Regular & Irregular Verbs in Historical Events"
            objetivo: "Narrar hitos históricos de la ciencia y eventos completados en el pasado usando verbos regulares e irregulares."
            concepto_clave_latex: ""
            ejemplo: "In 1954, Bell Labs demonstrated the first practical silicon solar cell."
            bloque_sugerido: "Timeline Reading 40 min • Milestones in electrical & thermal engineering"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Past Simple: Regular & Irregular Verbs in Historical Events: Communicative Purpose"
                puntos:
                  - "Use Past Simple for completed actions at a definite past time (in 1882, yesterday, last semester, two days ago)."
                  - "Regular verbs add -ed (invented, discovered, studied); irregular verbs change stem (built, wrote, went, found)."
                  - "Past of To Be uses 'was' (I/he/she/it) and 'were' (you/we/they) without 'did'."
                ejemplo: "In 1954, Bell Labs demonstrated the first practical silicon solar cell."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: Subject + V2 (past form) — identical for all persons!"
                  - "-ed pronunciation: /t/ after voiceless (worked), /d/ after voiced (measured), /ɪd/ after t/d (tested, started)."
                  - "Past of Be: 'Tesla was an inventor; his patents were revolutionary.'"
                tabla:
                  - ["Verb Type", "Base -> Past", "-ed Sound / Note"]
                  - ["Regular (/t/, /d/)", "develop -> developed", "No extra syllable (/t/)"]
                  - ["Regular (/ɪd/)", "connect -> connected", "Extra syllable after t/d"]
                  - ["Irregular", "build -> built, rise -> rose", "Memorize stem change"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Negative: Subject + did not (didn't) + BASE verb ('Edison didn't champion AC transmission')."
                  - "Questions: Did + subject + BASE verb? / Wh- + did + subject + BASE verb?"
                  - "With Was/Were: 'Were the measurements accurate? Yes, they were.'"
                ejemplo: "Last week, our team calibrated the pyranometer on the rooftop."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never keep past form after 'did/didn't': say 'Did you finish?', NOT 'Did you finished?'."
                  - "Do not mix 'was/were' with 'did': say 'Were you in class?', NOT 'Did you were in class?'."
                tabla:
                  - ["Incorrect", "Correct", "Rule"]
                  - ["We didn't went", "We didn't go", "Base verb after didn't"]
                  - ["He was graduated in 2024", "He graduated in 2024", "Active Past Simple"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "In 1954, Bell Labs demonstrated the first practical silicon solar cell."
                  - "Last week, our team calibrated the pyranometer on the rooftop."
                  - "Did Faraday discover electromagnetic induction in 1831? Yes, he did."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Pronounce -ed: 'measured (/d/), calculated (/ɪd/), switched (/t/)'."
                  - "Rewrite in negative: 'The voltage dropped' -> 'The voltage didn't drop.'"
                  - "Write a 5-sentence timeline of an energy pioneer."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 2
            corte: 1
            modalidad: "general"
            titulo: "Past Continuous vs. Past Simple (While & When Clauses)"
            objetivo: "Combinar acciones pasadas en desarrollo con eventos puntuales que las interrumpieron."
            concepto_clave_latex: ""
            ejemplo: "While the technician was inspecting the transformer, it started to rain."
            bloque_sugerido: "Narrative Drill 40 min • Reporting past lab procedures & interruptions"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Past Continuous vs. Past Simple (While & When Clauses): Communicative Purpose"
                puntos:
                  - "Past Continuous (was / were + verb-ing) sets the background action in progress at a specific past moment."
                  - "Past Simple (V2) expresses the shorter interrupting event or sequential action."
                  - "Use 'while' / 'as' before Past Continuous, and 'when' typically before Past Simple."
                ejemplo: "While the technician was inspecting the transformer, it started to rain."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Interrupting pattern: 'While we were logging data, the breaker tripped.'"
                  - "Parallel background actions: 'While I was wiring the sensor, Ana was testing the code.'"
                  - "Comma rule: put a comma when the When/While clause comes first."
                tabla:
                  - ["Connector", "Typical Clause", "Example"]
                  - ["While + Past Cont.", "Long action in progress", "While the rotor was spinning..."]
                  - ["When + Past Simple", "Sudden interruption", "...when the alarm sounded."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Negative: 'The generator wasn't running at midnight.'"
                  - "Questions: 'What were you doing when the power went out?'"
                  - "Sequential Past Simple (cause -> effect): 'When I pressed Start, the pump turned on' (one after another)."
                ejemplo: "What parameters were you monitoring when the voltage spike occurred?"
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid using Past Continuous for stative verbs: 'I knew the answer', NOT 'I was knowing'."
                  - "Match subject agreement: 'you/we/they WERE', 'I/he/she/it WAS'."
                tabla:
                  - ["Meaning", "Sentence", "Timeline"]
                  - ["Already in progress", "When I arrived, they were testing.", "Testing started BEFORE arrival"]
                  - ["Happened next", "When I arrived, they started testing.", "Testing started AFTER arrival"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "While the technician was inspecting the transformer, it started to rain."
                  - "What parameters were you monitoring when the voltage spike occurred?"
                  - "At 10:30 a.m. yesterday, we were running a simulation in MATLAB."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Combine with 'while': 'We / record temperature — the sensor / disconnect'."
                  - "Choose: 'When the bell rang, we (wrote / were writing) our conclusion.'"
                  - "Report a laboratory incident in 4 connected sentences."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 3
            corte: 1
            modalidad: "general"
            titulo: "Countable & Uncountable Nouns (Much, Many, A lot of, Few, Little)"
            objetivo: "Cuantificar recursos, materiales, energía, datos y equipos diferenciando sustantivos contables e incontables."
            concepto_clave_latex: ""
            ejemplo: "How much electricity does the university campus consume per month?"
            bloque_sugerido: "Quantifier Practice 35 min • Resource & energy consumption descriptions"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Countable & Uncountable Nouns (Much, Many, A lot of, Few, Little): Communicative Purpose"
                puntos:
                  - "Countable nouns have singular & plural forms (turbines, batteries, watts, hours)."
                  - "Uncountable nouns represent mass, abstract concepts, or liquids/gases (energy, electricity, equipment, information, research, water) -> ALWAYS singular verb!"
                  - "Quantifiers depend on countability: many / (a) few for countable; much / (a) little for uncountable."
                ejemplo: "How much electricity does the university campus consume per month?"
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Large quantity: 'a lot of / plenty of' work with BOTH countable and uncountable nouns."
                  - "Questions & negatives: 'How many cells...?' vs. 'How much power...?'"
                  - "Nuance: 'a few / a little' = positive (some, enough); 'few / little' = negative (almost none)."
                tabla:
                  - ["Category", "Countable Plural", "Uncountable Singular"]
                  - ["Large amount", "many / a lot of panels", "much / a lot of heat"]
                  - ["Small (sufficient)", "a few samples", "a little coolant"]
                  - ["Almost zero", "very few errors", "very little friction"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Count uncountable concepts using measure words: 'a piece of equipment', 'two liters of biodiesel', 'three megawatts of power'."
                  - "Watch out: 'data' and 'media' are treated as uncountable or plural in academic English, while 'information', 'advice', 'hardware', 'software' are strictly uncountable!"
                ejemplo: "We have a few spare fuses, so we can continue the experiment."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never pluralize 'informations', 'equipments', or 'researches'!"
                  - "Say 'How much energy is lost?', NOT 'How many energy are lost?'."
                tabla:
                  - ["Spanish Plural", "Incorrect English", "Correct Academic English"]
                  - ["equipos", "three equipments", "three pieces of equipment"]
                  - ["investigaciones", "many researches", "extensive research / studies"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "How much electricity does the university campus consume per month?"
                  - "We have a few spare fuses, so we can continue the experiment."
                  - "Modern LED systems waste very little energy as heat."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'How (much / many) current flows through R1?' -> 'much'."
                  - "Contrast: 'few students passed' vs. 'a few students passed'."
                  - "Classify 10 engineering nouns as countable or uncountable."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 4
            corte: 2
            modalidad: "general"
            titulo: "Comparative Adjectives: Comparing Performance & Qualities"
            objetivo: "Comparar el desempeño, costo y eficiencia de tecnologías utilizando adjetivos comparativos y modificadores."
            concepto_clave_latex: ""
            ejemplo: "Monocrystalline panels are slightly more efficient than polycrystalline ones."
            bloque_sugerido: "Benchmarking Drill 40 min • Comparing two renewable energy technologies"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Comparative Adjectives: Comparing Performance & Qualities: Communicative Purpose"
                puntos:
                  - "Short adjectives (1 syllable, or 2 ending in -y): add -er + than (cheaper, hotter, noisier)."
                  - "Long adjectives (2+ syllables): more / less + adjective + than (more efficient, less expensive)."
                  - "Irregular comparatives: good -> better, bad -> worse, far -> farther / further."
                ejemplo: "Monocrystalline panels are slightly more efficient than polycrystalline ones."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "CVC doubling: big -> bigger, hot -> hotter, thin -> thinner."
                  - "-y -> -ier: heavy -> heavier, easy -> easier."
                  - "Degree modifiers before comparatives: 'much / far / significantly' (big gap) vs. 'slightly / a bit' (small gap)."
                tabla:
                  - ["Adjective Type", "Base", "Comparative Form"]
                  - ["1-syllable", "fast / hot", "faster than / hotter than"]
                  - ["2-syllable (-y)", "heavy / reliable", "heavier / more reliable"]
                  - ["Irregular", "good / bad / far", "better / worse / further"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Double comparatives for trends: 'Solar modules are becoming cheaper and more efficient.'"
                  - "Proportional correlation ('The... the...'): 'The higher the temperature, the lower the open-circuit voltage.'"
                ejemplo: "Offshore winds are stronger and more consistent than onshore winds."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never combine 'more' + '-er': say 'better' or 'faster', NOT 'more better' or 'more faster'."
                  - "Always use 'than' (with 'a'), NOT 'then' (time sequence) or 'that'."
                tabla:
                  - ["Modifier", "Gap Size", "Technical Comparison"]
                  - ["much / significantly", "Large difference", "Li-ion is significantly lighter than lead-acid."]
                  - ["slightly / marginally", "Small difference", "Prototype B is slightly quieter than A."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Monocrystalline panels are slightly more efficient than polycrystalline ones."
                  - "Offshore winds are stronger and more consistent than onshore winds."
                  - "The higher the wind speed, the greater the power output."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Compare: 'LED bulbs / incandescent bulbs (efficient & durable)'."
                  - "Fix: 'Copper is more cheaper that silver' -> 'Copper is cheaper than silver.'"
                  - "Write 3 'The..., the...' engineering relationships."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 5
            corte: 2
            modalidad: "general"
            titulo: "Superlative Adjectives & Equatives (As... as)"
            objetivo: "Destacar valores extremos y expresar igualdad o proporción entre alternativas técnicas."
            concepto_clave_latex: ""
            ejemplo: "La Guajira has some of the highest wind speeds in South America."
            bloque_sugerido: "Comparison Matrix 35 min • Ranking 4 energy storage systems"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Superlative Adjectives & Equatives (As... as): Communicative Purpose"
                puntos:
                  - "Superlatives compare 3 or more items: 'the + -est' (the fastest) or 'the most / the least + adjective' (the most sustainable)."
                  - "Irregular superlatives: the best, the worst, the farthest/furthest."
                  - "Equatives ('as + adjective/adverb + as') express equality or ratio ('twice as fast as')."
                ejemplo: "La Guajira has some of the highest wind speeds in South America."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Preposition after superlatives: use 'IN' for places/groups ('the largest plant in Colombia') and 'OF' for time/sets ('the hottest day of the year')."
                  - "Negative equative: 'not as (so) expensive as' = cheaper than."
                  - "Multipliers: 'three times as powerful as', 'half as heavy as'."
                tabla:
                  - ["Structure", "Formula", "Example"]
                  - ["Superlative (short)", "the + adj-est", "the highest voltage in the grid"]
                  - ["Superlative (long)", "the most/least + adj", "the most reliable inverter"]
                  - ["Equative", "(not) as + adj + as", "not as noisy as a diesel genset"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Pair superlatives with Present Perfect: 'This is the most accurate model we have ever built.'"
                  - "Use 'one of the + superlative + PLURAL noun': 'one of the sunniest regions in the country'."
                ejemplo: "Hydrogen has the highest gravimetric energy density of common fuels."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never forget 'the' (or a possessive) before a superlative: 'the lowest cost'."
                  - "Use 'in' (NOT 'of') before singular places: 'in Latin America', NOT 'of Latin America'."
                tabla:
                  - ["Equative Multiplier", "Equivalent Meaning", "Example"]
                  - ["as efficient as", "Equal performance", "Unit A is as efficient as Unit B."]
                  - ["twice as large as", "2x capacity", "The new battery bank is twice as large as the old one."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "La Guajira has some of the highest wind speeds in South America."
                  - "Hydrogen has the highest gravimetric energy density of common fuels."
                  - "Biomass gasification is not as widespread as solar PV on campus."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Rewrite using 'not as... as': 'Lead-acid is heavier than lithium' -> 'Lithium isn't as heavy as lead-acid.'"
                  - "Complete: 'One of the most important ___ (factor -> factors) in design.'"
                  - "Write 3 superlatives about Colombian energy geography."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 6
            corte: 2
            modalidad: "general"
            titulo: "Future with Be Going To for Plans & Intentions"
            objetivo: "Expresar planes definidos de estudio, proyectos futuros y predicciones basadas en evidencia visible."
            concepto_clave_latex: ""
            ejemplo: "Next semester, we are going to take Thermodynamics and Linear Algebra."
            bloque_sugerido: "Project Planning 35 min • Outlining next-week experimental roadmap"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Future with Be Going To for Plans & Intentions: Communicative Purpose"
                puntos:
                  - "Form: am / is / are + going to + base verb."
                  - "Use 1 (Prior Intention/Plan): decisions already made before speaking ('We are going to build a solar tracker')."
                  - "Use 2 (Evidence-Based Prediction): present clues show what is imminent ('Look at the dark clouds — irradiance is going to drop')."
                ejemplo: "Next semester, we are going to take Thermodynamics and Linear Algebra."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: 'I am going to specialize in smart grids.'"
                  - "Negative: 'They aren't going to replace the transformer this month.'"
                  - "Question: 'What are you going to present at the symposium?'"
                tabla:
                  - ["Use Case", "Context Clue", "Example"]
                  - ["Prior Plan", "Decided earlier", "We're going to test the circuit tomorrow."]
                  - ["Visible Evidence", "Current sensor/sky", "The motor is at 98°C; it's going to overheat!"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Present Continuous can also express fixed arrangements with time/place: 'We are meeting our advisor at 3:00 p.m.'"
                  - "Avoid 'going to go': native speakers prefer 'We're going to the lab after lunch'."
                ejemplo: "Look at the battery monitor — it's at 4%, so it's going to shut down soon."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never omit 'am/is/are': say 'She is going to present', NOT 'She going to present'."
                  - "Use formal 'going to' in academic writing (avoid casual spoken 'gonna' in essays)."
                tabla:
                  - ["Spoken Informal", "Academic Written", "Register Note"]
                  - ["We're gonna test", "We are going to test", "Never write 'gonna' in reports"]
                  - ["Are you gonna...?", "Are you going to...?", "Keep full spelling in slides"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Next semester, we are going to take Thermodynamics and Linear Algebra."
                  - "Look at the battery monitor — it's at 4%, so it's going to shut down soon."
                  - "Are you going to join the renewable energy seedbed (semillero) this term?"
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Write 3 academic plans for next cuatrimestre using 'be going to'."
                  - "Make 2 predictions from visible lab readings ('Voltage is rising fast...')."
                  - "Ask a partner 3 questions about their weekend study plan."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 7
            corte: 2
            modalidad: "general"
            titulo: "Future with Will / Won't for Predictions & Spontaneous Decisions"
            objetivo: "Formular predicciones tecnológicas, promesas, ofrecimientos y decisiones instantáneas con Will y Won't."
            concepto_clave_latex: ""
            ejemplo: "By 2035, renewable energy will supply a major share of regional electricity."
            bloque_sugerido: "Forecast Workshop 35 min • Energy transition predictions vs. instant lab actions"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Future with Will / Won't for Predictions & Spontaneous Decisions: Communicative Purpose"
                puntos:
                  - "Form: will ('ll) / will not (won't) + base verb (invariable for all subjects)."
                  - "Use 'will' for: (1) instant decisions made while speaking, (2) offers & promises, (3) general predictions/forecasts (often with think, expect, probably)."
                  - "Contrast: 'will' = spontaneous or opinion-based vs. 'be going to' = pre-planned or visible evidence."
                ejemplo: "By 2035, renewable energy will supply a major share of regional electricity."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Adverb placement: 'Solar storage will probably dominate microgrids' (before 'won't': 'probably won't')."
                  - "Spontaneous decision: 'The projector isn't on — I'll connect the HDMI cable.'"
                  - "Forecast verbs: 'Experts predict / expect / believe that demand will grow.'"
                tabla:
                  - ["Trigger", "Best Form", "Example"]
                  - ["Spontaneous offer", "Will ('ll)", "That box looks heavy. I'll help you."]
                  - ["Prior schedule/plan", "Be going to", "I'm going to study with Luis at 5:00."]
                  - ["Long-term forecast", "Will + adverb", "Green hydrogen will likely scale rapidly."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions: 'Will electric vehicles stabilize grid demand?' -> 'Yes, they will / No, they won't.'"
                  - "Polite requests & offers: 'Will you pass me the probe?' / 'Shall we start the simulation?'"
                ejemplo: "Don't worry about the spreadsheet — I'll double-check the formulas right now."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Do not use 'will' after time conjunctions (when, as soon as, before, after, until): say 'I'll call you when the test finishes' (Present Simple!)."
                  - "Never add 'to' after will: 'will increase', NOT 'will to increase'."
                tabla:
                  - ["Time Clause Rule", "Incorrect", "Correct"]
                  - ["when / as soon as", "When it will reach 60 Hz...", "When it reaches 60 Hz, we will sync."]
                  - ["after / before", "Before I will submit...", "Before I submit, I'll check the PDF."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "By 2035, renewable energy will supply a major share of regional electricity."
                  - "Don't worry about the spreadsheet — I'll double-check the formulas right now."
                  - "As soon as the sensor stabilizes, we will record the baseline."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'A: We're out of graph paper. B: Oh! I (will / am going to) get some.' -> 'will'."
                  - "Fix: 'When the class will end, we'll eat' -> 'When the class ends, we'll eat.'"
                  - "Write 3 forecasts for Colombia's energy sector."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 8
            corte: 3
            modalidad: "general"
            titulo: "Modal Verbs of Obligation & Advice (Must, Have to, Should, Ought to)"
            objetivo: "Distinguir entre obligación interna/externa, prohibición, ausencia de necesidad y recomendaciones técnicas."
            concepto_clave_latex: ""
            ejemplo: "Engineers must comply with RETIE electrical safety standards in Colombia."
            bloque_sugerido: "Compliance Briefing 35 min • Safety regulations vs. optional best practices"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Modal Verbs of Obligation & Advice (Must, Have to, Should, Ought to): Communicative Purpose"
                puntos:
                  - "Strong obligation: 'must' (rules, safety notices, speaker's authority) & 'have to / has to' (external regulations, institutional requirements)."
                  - "CRITICAL NEGATIVE CONTRAST: 'mustn't' = PROHIBITED! vs. 'don't/doesn't have to' = NOT NECESSARY (optional)."
                  - "Advice & best practices: 'should / shouldn't' and 'ought to' + base verb."
                ejemplo: "Engineers must comply with RETIE electrical safety standards in Colombia."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: 'All visitors must wear insulated boots.' / 'Students have to pass 162 credits.'"
                  - "Prohibition: 'You must not bypass the circuit breaker.'"
                  - "No obligation: 'You don't have to print the report; digital PDF is fine.'"
                tabla:
                  - ["Modal", "Meaning", "Lab / Campus Example"]
                  - ["must / have to", "100% Mandatory", "You must ground the chassis."]
                  - ["mustn't", "Strictly Forbidden", "You mustn't open live panels."]
                  - ["don't have to", "Optional", "You don't have to memorize constants."]
                  - ["should / shouldn't", "Recommendation", "You should save backups hourly."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions of obligation usually prefer 'Do we have to...?' ('Do we have to wear lab coats today?')."
                  - "Past obligation uses 'had to' (since 'must' has no past form for obligation: 'Yesterday we had to recalibrate twice')."
                ejemplo: "You don't have to bring your own oscilloscope; the lab provides them."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Spanish speakers often confuse 'don't have to' with prohibition -> remember 'mustn't' = forbidden!"
                  - "'Have to' takes do/does in negatives and questions; 'must' and 'should' never use do/does."
                tabla:
                  - ["Situation", "Wrong Choice", "Accurate Modal"]
                  - ["Prohibido tocar", "You don't have to touch", "You mustn't touch"]
                  - ["Opcional asistir", "You mustn't attend", "You don't have to attend"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Engineers must comply with RETIE electrical safety standards in Colombia."
                  - "You don't have to bring your own oscilloscope; the lab provides them."
                  - "We should insulate the steam pipe to reduce thermal losses."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'Entry is free; you (mustn't / don't have to) pay' -> 'don't have to'."
                  - "Past form: 'We must repeat the test yesterday' -> 'We had to repeat the test yesterday.'"
                  - "Write 4 technical recommendations using should/must/mustn't."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 9
            corte: 3
            modalidad: "general"
            titulo: "Present Perfect Simple: Life Experiences (Ever, Never, Already, Yet)"
            objetivo: "Conectar experiencias académicas pasadas con el presente mediante el Presente Perfecto y marcadores clave."
            concepto_clave_latex: ""
            ejemplo: "Have you ever designed a circuit on a breadboard? Yes, several times."
            bloque_sugerido: "Experience Log 40 min • Academic portfolio milestones with Present Perfect"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Present Perfect Simple: Life Experiences (Ever, Never, Already, Yet): Communicative Purpose"
                puntos:
                  - "Form: have / has + Past Participle (V3: worked, measured / built, written, been, gone)."
                  - "Use Present Perfect for: (1) life experiences at an unspecified time (ever / never), (2) recent achievements with present relevance (just, already, yet)."
                  - "Never pair Present Perfect with finished past dates (*yesterday, in 2022*)!"
                ejemplo: "Have you ever designed a circuit on a breadboard? Yes, several times."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "'Already' (sooner than expected): mid-position in affirmative ('We have already submitted the lab')."
                  - "'Yet' (up to now): end of negatives & questions ('Have you checked the results yet? No, not yet')."
                  - "'Just' (moments ago): 'The simulation has just converged.'"
                tabla:
                  - ["Adverb", "Clause Type", "Position & Example"]
                  - ["ever / never", "Question / Affirmative", "Have you ever visited a wind farm?"]
                  - ["just / already", "Affirmative", "She has already finished Topic 9."]
                  - ["yet", "Negative & Question", "We haven't tested the inverter yet."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "'Have been to' vs. 'Have gone to': 'Ana has been to Ituango' (visited and returned) vs. 'Ana has gone to the lab' (she is still there now!)."
                  - "Follow up an 'ever' experience with Past Simple details: 'Have you ever used PVsyst? Yes, I have. I used it last month.'"
                ejemplo: "Our team has already collected 500 irradiance samples, but we haven't plotted them yet."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Do not use Present Simple for 'yet/already': 'I have already eaten', NOT 'I already eat' in formal British/academic English."
                  - "Memorize key V3 forms: write -> written, see -> seen, do -> done, run -> run, choose -> chosen."
                tabla:
                  - ["Verb", "Past Simple (V2)", "Past Participle (V3)"]
                  - ["write / take", "wrote / took", "written / taken"]
                  - ["go / be", "went / was-were", "gone / been"]
                  - ["rise / fall", "rose / fell", "risen / fallen"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Have you ever designed a circuit on a breadboard? Yes, several times."
                  - "Our team has already collected 500 irradiance samples, but we haven't plotted them yet."
                  - "Solar installations on the Caribbean coast have grown rapidly."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Insert 'yet' or 'already': 'Has the lecture started ___?' -> 'yet'."
                  - "Contrast: 'He has been to Bogotá' vs. 'He has gone to Bogotá'."
                  - "Write 3 academic achievements you have completed so far."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 10
            corte: 3
            modalidad: "general"
            titulo: "Zero & First Conditionals: Cause-Effect & Real Future Possibilities"
            objetivo: "Modelar leyes físicas invariables (Condicional Cero) y escenarios reales de contingencia (Primer Condicional)."
            concepto_clave_latex: ""
            ejemplo: "If resistance increases at constant voltage, electric current decreases."
            bloque_sugerido: "Cause-Effect Lab 40 min • Physical laws & automated control logic in English"
            slides:
              - numero: 1
                seccion: "CEFR A2 • CORE CONCEPT"
                titulo: "Zero & First Conditionals: Cause-Effect & Real Future Possibilities: Communicative Purpose"
                puntos:
                  - "Zero Conditional (If/When + Present Simple, Present Simple): 100% true scientific laws and automatic system behaviors."
                  - "First Conditional (If + Present Simple, will / can / must + base verb): real, likely future outcomes and operational protocols."
                  - "Alternatives to 'if': 'unless' (= if... not), 'as long as', 'in case'."
                ejemplo: "If resistance increases at constant voltage, electric current decreases."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Zero: 'If you heat a gas at constant volume, its pressure rises.'"
                  - "First: 'If irradiance drops below 200 W/m², the backup battery will supply the load.'"
                  - "Unless: 'The circuit won't close unless the relay is energized.'"
                tabla:
                  - ["Conditional", "If-Clause", "Main Clause & Certainty"]
                  - ["Zero (Law)", "If + Present Simple", "Present Simple (100% always true)"]
                  - ["First (Future)", "If + Present Simple", "will / may / must + verb (Real possibility)"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Clause order is flexible: put a comma ONLY when the If-clause comes first ('If voltage exceeds 240 V, the surge protector trips' / 'The surge protector trips if voltage exceeds 240 V')."
                  - "Distinguish 'in case' (precaution done BEFORE) vs. 'if' (reaction AFTER): 'Save your file in case the PC crashes'."
                ejemplo: "If we optimize the tilt angle, annual energy yield will rise by 6%."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "GOLDEN RULE: Never put 'will' inside the If-clause! Say 'If it rains tomorrow, output will fall', NOT 'If it will rain...'."
                  - "Avoid double negative after 'unless': 'unless you calibrate it', NOT 'unless you don't calibrate it'."
                tabla:
                  - ["Connector", "Exact Meaning", "Engineering Protocol"]
                  - ["unless", "except if (if... not)", "Don't start unless pressure is normal."]
                  - ["in case", "as a precaution against", "Wear goggles in case sparks fly."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "If resistance increases at constant voltage, electric current decreases."
                  - "If we optimize the tilt angle, annual energy yield will rise by 6%."
                  - "The inverter shuts down automatically unless grid frequency stays stable."
                ejemplo: "Academic Register (CEFR A2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete (Zero): 'If water ___ (reach) 100°C at 1 atm, it ___ (boil).'"
                  - "Rewrite with 'unless': 'If we don't insulate the tank, heat will escape.'"
                  - "Write 2 Zero Conditionals (physics laws) and 2 First Conditionals (lab contingencies)."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 11
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Inequalities, Intervals & Proportionality"
            objetivo: "Verbalizar desigualdades estrictas y no estrictas, órdenes de magnitud y proporcionalidad directa/inversa."
            concepto_clave_latex: "x \\le y \\quad ; \\quad a \\gg b \\quad ; \\quad P \\propto T \\quad ; \\quad I \\propto \\frac{1}{R} \\quad ; \\quad \\eta \\in [0, 1]"
            verbalizacion_ingles: "• x ≤ y -> \"x is less than or equal to y\"  |  x ≥ y -> \"x is greater than or equal to y\".\n• a >> b -> \"a is much greater than b\"  |  a << b -> \"a is much less than b\".\n• P ∝ T -> \"P is directly proportional to T\"  |  I ∝ 1/R -> \"I is inversely proportional to R\".\n• η ∈ [0, 1] -> \"eta belongs to (or lies in) the closed interval from zero to one\"."
            ejemplo: "En gases ideales a volumen constante, P ∝ T se expone oralmente como 'Absolute pressure is directly proportional to absolute temperature'."
            bloque_sugerido: "Symbol Fluency 30 min • Reading domain constraints & scaling laws aloud"
          - numero_tema: 12
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Linear, Quadratic & Polynomial Equations"
            objetivo: "Leer fluidamente ecuaciones lineales, polinomios y la fórmula cuadrática completa con pausas estructurales."
            concepto_clave_latex: "y = mx + b \\quad ; \\quad ax^2 + bx + c = 0 \\implies x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
            verbalizacion_ingles: "• y = mx + b -> \"y equals m x plus b, where m is the slope and b is the y-intercept\".\n• ax² + bx + c = 0 => ... -> \"a x squared plus b x plus c equals zero implies that x equals minus b plus or minus the square root of b squared minus four a c, all over two a\".\n• Tip: saying \"all over two a\" (with a brief pause before \"all over\") signals that the entire numerator is divided by 2a!"
            ejemplo: "Determinación de raíces características en sistemas amortiguados RLC mediante la expresión cuadrática leída en inglés."
            bloque_sugerido: "Oral Algebra 30 min • Grouping numerators & denominators clearly in speech"
          - numero_tema: 13
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Vectors, Dot Product & Cross Product"
            objetivo: "Expresar vectores unitarios cartesianos, magnitud vectorial, producto escalar y producto vectorial."
            concepto_clave_latex: "\\vec{F} = F_x\\hat{i} + F_y\\hat{j} + F_z\\hat{k} \\quad ; \\quad W = \\vec{F} \\cdot \\vec{d} = |\\vec{F}||\\vec{d}|\\cos\\theta \\quad ; \\quad \\vec{\\tau} = \\vec{r} \\times \\vec{F}"
            verbalizacion_ingles: "• F = Fx î + Fy ĵ + Fz k̂ -> \"vector F equals F sub x i-hat plus F sub y j-hat plus F sub z k-hat\".\n• F · d -> \"vector F dot vector d\" (or \"the dot product / scalar product of F and d\") equals \"the magnitude of F times the magnitude of d times cosine theta\".\n• τ = r × F -> \"torque vector tau equals r cross F\" (\"the cross product of position vector r and force F\")."
            ejemplo: "Exposición del par mecánico en el rotor de un aerogenerador: 'Torque equals radius vector r cross tangential aerodynamic force F'."
            bloque_sugerido: "Vector Dictation 30 min • Unit vectors (i-hat, j-hat, k-hat) & products"
          - numero_tema: 14
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Logarithms & Exponential Growth/Decay"
            objetivo: "Verbalizar logaritmos naturales, logaritmos en base diez y funciones de decaimiento o carga exponencial."
            concepto_clave_latex: "y = \\ln(x) \\quad ; \\quad L_{\\text{dB}} = 10\\log_{10}\\left(\\frac{P_2}{P_1}\\right) \\quad ; \\quad N(t) = N_0 e^{-\\lambda t}"
            verbalizacion_ingles: "• ln(x) -> \"the natural log (or natural logarithm) of x\" (also spoken \"lon x\" informally, prefer \"natural log of x\").\n• 10 log₁₀(P₂/P₁) -> \"ten log base ten of the ratio P two over P one\".\n• N(t) = N₀ e^(-λt) -> \"N of t equals N naught (or N sub zero) times e to the minus lambda t\"."
            ejemplo: "Lectura de curvas de descarga transitoria de un supercapacitor V(t) = V_0 e^{-t/(RC)}: 'V naught e to the minus t over R C'."
            bloque_sugerido: "Exponential Reading 30 min • Decibels, time constants & natural logs"
          - numero_tema: 15
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Classical Mechanics & Force Notation"
            objetivo: "Pronunciar ecuaciones vectoriales de dinámica newtoniana, trabajo mecánico, energía cinética y potencia."
            concepto_clave_latex: "\\sum \\vec{F} = m\\vec{a} \\quad ; \\quad W = \\int \\vec{F}\\cdot d\\vec{r} \\quad ; \\quad E_k = \\frac{1}{2}mv^2 \\quad ; \\quad P = \\vec{F}\\cdot\\vec{v}"
            verbalizacion_ingles: "• ΣF = ma -> \"the sum of the forces (or net force vector) equals mass times acceleration vector a\".\n• W = ∫ F · dr -> \"work W equals the line integral of force F dot d r\".\n• E_k = 1/2 m v² -> \"kinetic energy E sub k equals one-half m v squared\".\n• P = F · v -> \"instantaneous power P equals force F dot velocity v\"."
            ejemplo: "Presentación en inglés de la energía cinética de una masa de aire entrando al área barrida de una turbina eólica."
            bloque_sugerido: "Mechanics Seminar 35 min • Newton's laws & work-energy theorem aloud"
          - numero_tema: 16
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Efficiency, Ratios & Percentage Error Verbalization"
            objetivo: "Exponer rendimientos energéticos, razones adimensionales y error porcentual experimental en inglés."
            concepto_clave_latex: "\\eta = \\frac{P_{\\text{out}}}{P_{\\text{in}}} \\times 100\\% \\quad ; \\quad \\varepsilon_{\\%} = \\frac{|x_{\\text{exp}} - x_{\\text{th}}|}{|x_{\\text{th}}|} \\times 100\\%"
            verbalizacion_ingles: "• η = (P_out / P_in) × 100% -> \"efficiency eta equals P out divided by P in, times one hundred percent\".\n• ε_% = |x_exp - x_th| / |x_th| × 100% -> \"percentage error equals the absolute value of experimental x minus theoretical x, divided by the absolute value of theoretical x, times one hundred percent\"."
            ejemplo: "Reporte oral de discrepancia experimental del 2.4% entre el voltaje medido en laboratorio y la simulación teórica."
            bloque_sugerido: "Lab Report Speech 30 min • Presenting experimental accuracy & efficiency"
      - codigo: "03031818"
        nombre: "Probabilidad y Estadística"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Estadística Descriptiva, Cuantiles y Exploración Energética"
            objetivo: "Sintetizar series experimentales con medidas de tendencia central, dispersión y asimetría."
            concepto_clave_latex: "\\bar{x} = \\frac{1}{n}\\sum_{i=1}^{n}x_i \\quad ; \\quad s = \\sqrt{\\frac{1}{n-1}\\sum_{i=1}^{n}(x_i - \\bar{x})^2} \\quad ; \\quad CV = \\frac{s}{\\bar{x}}"
            ejemplo: "Caracterización mensual de irradiancia global horizontal en el Caribe colombiano."
            bloque_sugerido: "Pomodoro 45/10 • Boxplots y dispersión"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Probabilidad Axiomática, Condicional y Teorema de Bayes"
            objetivo: "Actualizar probabilidades de falla y diagnóstico operativo ante nueva evidencia."
            concepto_clave_latex: "P(A|B) = \\frac{P(B|A)P(A)}{P(B)} = \\frac{P(B|A)P(A)}{\\sum_j P(B|A_j)P(A_j)}"
            ejemplo: "Confiabilidad diagnóstica de alarmas DGA de gases disueltos en transformadores."
            bloque_sugerido: "Práctica 50 min • Árboles y Bayes"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Variables Aleatorias Discretas, Esperanza y Varianza"
            objetivo: "Modelar conteos discretos y calcular valores esperados de disponibilidad."
            concepto_clave_latex: "E[X] = \\sum_x x\\,p(x) \\quad ; \\quad \\text{Var}(X) = E[X^2] - (E[X])^2"
            ejemplo: "Número esperado de unidades generadoras disponibles en una central térmica."
            bloque_sugerido: "Pomodoro 45/10 • Momentos discretos"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Distribuciones Binomial, Geométrica y de Poisson"
            objetivo: "Aplicar modelos discretos a tasas de eventos raros, descargas y desconexiones."
            concepto_clave_latex: "P(X=k) = \\binom{n}{k}p^k(1-p)^{n-k} \\quad ; \\quad P(N=k) = \\frac{(\\lambda t)^k e^{-\\lambda t}}{k!}"
            ejemplo: "Probabilidad de impactos de rayo y salidas forzadas por mes en líneas de 110 kV."
            bloque_sugerido: "Práctica 45 min • Poisson y Binomial"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Variables Continuas: Normal, Exponencial y Lognormal"
            objetivo: "Calcular probabilidades sobre densidades continuas y tiempos medios entre fallas (MTBF)."
            concepto_clave_latex: "Z = \\frac{X-\\mu}{\\sigma} \\quad ; \\quad R(t) = e^{-\\lambda t} \\quad ; \\quad \\text{MTBF} = \\frac{1}{\\lambda}"
            ejemplo: "Tiempo de supervivencia sin falla de inversores solares bajo distribución exponencial."
            bloque_sugerido: "Pomodoro 50/10 • Confiabilidad R(t)"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Distribución de Weibull en Evaluación Eólica"
            objetivo: "Ajustar parámetros de forma k y escala c para estimar energía eólica anual."
            concepto_clave_latex: "f(v) = \\frac{k}{c}\\left(\\frac{v}{c}\\right)^{k-1}\\exp\\left[-\\left(\\frac{v}{c}\\right)^k\\right]"
            ejemplo: "Modelado estadístico de rosas de viento en La Guajira (k = 2.4, c = 9.8 m/s)."
            bloque_sugerido: "Laboratorio 50 min • Ajuste Weibull"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Distribuciones Muestrales e Intervalos de Confianza"
            objetivo: "Construir intervalos de confianza con distribución Normal y t-Student."
            concepto_clave_latex: "\\bar{x} \\pm t_{\\alpha/2,\\,n-1}\\frac{s}{\\sqrt{n}} \\quad ; \\quad \\hat{p} \\pm z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}"
            ejemplo: "Estimación al 95% de confianza del ahorro energético medio tras cambio a motores IE4."
            bloque_sugerido: "Pomodoro 45/10 • Intervalos IC 95%"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Pruebas de Hipótesis Paramétricas y Valor-p"
            objetivo: "Contrastar hipótesis estadísticas sobre mejoras de eficiencia y control de calidad."
            concepto_clave_latex: "t_0 = \\frac{\\bar{x} - \\mu_0}{s/\\sqrt{n}} \\quad ; \\quad p\\text{-valor} < \\alpha \\implies \\text{Rechazar } H_0"
            ejemplo: "Verificación estadística de ganancia de rendimiento con recubrimiento antirreflectivo."
            bloque_sugerido: "Práctica 45 min • Pruebas t y z"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Correlación y Regresión Lineal por Mínimos Cuadrados"
            objetivo: "Cuantificar dependencia lineal entre variables climáticas y demanda eléctrica."
            concepto_clave_latex: "\\hat{y} = \\beta_0 + \\beta_1 x \\quad ; \\quad \\beta_1 = \\frac{S_{xy}}{S_{xx}} \\quad ; \\quad R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}}"
            ejemplo: "Modelo lineal de consumo diario de refrigeración respecto a grados-día CDD."
            bloque_sugerido: "Taller 50 min • Regresión y residuales"
      - codigo: "02031812"
        nombre: "Química Aplicada"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Estructura Atómica, Enlace Químico y Semiconductores"
            objetivo: "Relacionar bandas electrónicas y enlaces covalentes/iónicos con materiales fotovoltaicos."
            concepto_clave_latex: "E_{\\text{fotón}} = h\\nu = \\frac{hc}{\\lambda} \\ge E_g \\quad (E_{g,\\text{Si}} \\approx 1.12\\text{ eV})"
            ejemplo: "Longitud de onda umbral capaz de generar pares electrón-hueco en silicio dopado."
            bloque_sugerido: "Pomodoro 45/10 • Band-gap y fotones"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Estequiometría de Combustión y Exceso de Aire"
            objetivo: "Balancear reacciones de oxidación de hidrocarburos, biogás e hidrógeno."
            concepto_clave_latex: "\\text{C}_x\\text{H}_y + a\\left(1+e\\right)(\\text{O}_2 + 3.76\\text{N}_2) \\to x\\text{CO}_2 + \\frac{y}{2}\\text{H}_2\\text{O} + \\cdots"
            ejemplo: "Cálculo de relación aire-combustible y CO2 emitido al quemar gas natural con 15% de exceso."
            bloque_sugerido: "Pomodoro 50/10 • Balances de combustión"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Gases Ideales, Mezclas de Dalton y Gases Reales"
            objetivo: "Calcular presiones parciales y densidades de mezclas gaseosas a alta presión."
            concepto_clave_latex: "PV = nRT \\quad ; \\quad P_i = y_i P_{\\text{tot}} \\quad ; \\quad PV = ZnRT"
            ejemplo: "Almacenamiento comprimido de hidrógeno a 350 bar corregido con factor Z."
            bloque_sugerido: "Práctica 45 min • Mezclas de gases"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Termoquímica, Ley de Hess y Poder Calorífico (PCS/PCI)"
            objetivo: "Determinar entalpías de reacción y diferenciar poder calorífico superior e inferior."
            concepto_clave_latex: "\\Delta H_{\\text{rxn}}^\\circ = \\sum \\nu_p \\Delta H_f^\\circ(\\text{prod}) - \\sum \\nu_r \\Delta H_f^\\circ(\\text{react}) \\quad ; \\quad \\text{PCI} = \\text{PCS} - m_v h_{fg}"
            ejemplo: "Poder calorífico inferior del biogás (60% CH4, 40% CO2) para motogeneradores."
            bloque_sugerido: "Pomodoro 50/10 • Ley de Hess y PCI"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Propiedades de Disoluciones, pH y Tratamiento de Aguas"
            objetivo: "Controlar dureza, alcalinidad, pH y conductividad en circuitos de vapor."
            concepto_clave_latex: "\\text{pH} = -\\log_{10}[\\text{H}^+] \\quad ; \\quad M_1 V_1 = M_2 V_2"
            ejemplo: "Prevención de incrustaciones calcáreas en tubos de calderas industriales."
            bloque_sugerido: "Práctica 40 min • Química de calderas"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Cinética Química, Velocidad de Reacción y Catálisis"
            objetivo: "Modelar el efecto de la temperatura y catalizadores mediante la ecuación de Arrhenius."
            concepto_clave_latex: "k = A\\exp\\left(-\\frac{E_a}{RT}\\right) \\quad ; \\quad r = k[A]^m[B]^n"
            ejemplo: "Cinética de transesterificación catalítica para producción de biodiésel."
            bloque_sugerido: "Pomodoro 45/10 • Ecuación de Arrhenius"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Equilibrio Químico y Principio de Le Chatelier"
            objetivo: "Predecir desplazamientos de conversión en reformado y síntesis de combustibles."
            concepto_clave_latex: "K_p = K_c(RT)^{\\Delta n} \\quad ; \\quad \\Delta G^\\circ = -RT\\ln K"
            ejemplo: "Optimización térmica del desplazamiento gas-agua (Water-Gas Shift) para H2."
            bloque_sugerido: "Práctica 45 min • Constantes Kp y Kc"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Electroquímica, Ecuación de Nernst y Baterías"
            objetivo: "Calcular potenciales de celda en baterías secundarias y celdas de combustible."
            concepto_clave_latex: "E_{\\text{celda}} = E^\\circ - \\frac{RT}{nF}\\ln Q \\quad ; \\quad \\Delta G = -nFE_{\\text{celda}}"
            ejemplo: "Tensión teórica de circuito abierto en celdas LiFePO4 y PEMFC de hidrógeno."
            bloque_sugerido: "Pomodoro 50/10 • Celdas galvánicas"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Electrólisis de Faraday y Control de Corrosión"
            objetivo: "Cuantificar producción electrolítica de hidrógeno y protección catódica."
            concepto_clave_latex: "m = \\frac{I\\cdot t\\cdot M}{n\\cdot F} \\quad (F = 96485\\text{ C/mol})"
            ejemplo: "Masa de H2 producida por hora en un electrolizador alcalino operando a 400 A."
            bloque_sugerido: "Taller 45 min • Leyes de Faraday"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Antiderivadas, Sumas de Riemann e Integral Definida"
            objetivo: "Interpretar la integral definida como acumulación continua de magnitudes físicas."
            concepto_clave_latex: "\\int_a^b f(x)\\,dx = \\lim_{n \\to \\infty}\\sum_{i=1}^{n} f(x_i^*)\\Delta x"
            ejemplo: "Energía total entregada a la red a partir de telemetría discreta de potencia."
            bloque_sugerido: "Pomodoro 50/10 • Sumas de Riemann"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Teorema Fundamental del Cálculo y Valor Promedio"
            objetivo: "Conectar derivación e integración y calcular valores medios y eficaces RMS."
            concepto_clave_latex: "\\frac{d}{dx}\\int_a^x f(t)\\,dt = f(x) \\quad ; \\quad f_{\\text{prom}} = \\frac{1}{b-a}\\int_a^b f(x)\\,dx"
            ejemplo: "Deducción analítica de V_rms = V_m / √2 para una onda sinusoidal de 60 Hz."
            bloque_sugerido: "Pomodoro 50/10 • TFC y valores RMS"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Técnicas de Integración: Sustitución e Integración por Partes"
            objetivo: "Resolver integrales de productos exponenciales-sinusoidales y cambios de variable."
            concepto_clave_latex: "\\int u\\,dv = uv - \\int v\\,du \\quad ; \\quad \\int f(g(x))g'(x)\\,dx = \\int f(u)\\,du"
            ejemplo: "Energía disipada por corrientes transitorias amortiguadas e^{-αt}sin(ωt)."
            bloque_sugerido: "Práctica 50 min • Integración por partes"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Integrales Trigonométricas y Sustitución Trigonométrica"
            objetivo: "Evaluar integrales con radicales cuadráticos propios de campos eléctricos y magnéticos."
            concepto_clave_latex: "\\int \\frac{dx}{(x^2 + a^2)^{3/2}} = \\frac{x}{a^2\\sqrt{x^2 + a^2}} + C"
            ejemplo: "Campo eléctrico axial generado por un anillo o línea cargada uniforme."
            bloque_sugerido: "Pomodoro 50/10 • Sustitución trigonométrica"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Fracciones Parciales e Integración Numérica (Simpson/Trapecio)"
            objetivo: "Integrar funciones racionales y datos tabulados experimentales con alta precisión."
            concepto_clave_latex: "\\int_a^b f(x)\\,dx \\approx \\frac{h}{3}\\left[f(x_0) + 4\\sum_{\\text{imp}}f(x_i) + 2\\sum_{\\text{par}}f(x_i) + f(x_n)\\right]"
            ejemplo: "Cálculo de trabajo frontera P-V a partir de lecturas discretas de presión."
            bloque_sugerido: "Práctica 45 min • Fracciones y Simpson"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Integrales Impropias y Transformadas Integrales"
            objetivo: "Analizar convergencia en intervalos infinitos y discontinuidades singulares."
            concepto_clave_latex: "\\int_0^\\infty e^{-st}\\,dt = \\frac{1}{s}\\;\\;(s>0) \\quad ; \\quad \\int_1^\\infty \\frac{dx}{x^p}\\text{ converge }\\iff p>1"
            ejemplo: " Convergencia de integrales de radiación espectral y definición de Laplace."
            bloque_sugerido: "Pomodoro 50/10 • Criterios de convergencia"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Aplicaciones Geométricas y Físicas: Volúmenes, Trabajo y Presión"
            objetivo: "Calcular volúmenes de revolución, trabajo de bombeo y fuerza hidrostática."
            concepto_clave_latex: "W_{\\text{bombeo}} = \\int_a^b \\rho g A(y)(H - y)\\,dy \\quad ; \\quad F_h = \\int_c^d \\rho g y\\,w(y)\\,dy"
            ejemplo: "Trabajo requerido para vaciar/bombear tanques cilíndricos y fuerza sobre compuertas."
            bloque_sugerido: "Pomodoro 50/10 • Bombeo y presión"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Coordenadas Polares, Longitud de Arco y Centroides"
            objetivo: "Integrar áreas y longitudes de arco en geometrías polares y catenarias."
            concepto_clave_latex: "L = \\int_a^b \\sqrt{1 + [f'(x)]^2}\\,dx \\quad ; \\quad A = \\frac{1}{2}\\int_\\alpha^\\beta r(\\theta)^2\\,d\\theta"
            ejemplo: "Longitud real del conductor con flecha catenaria en un vano de transmisión."
            bloque_sugerido: "Práctica 45 min • Catenarias y polares"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Sucesiones, Series de Taylor y Aproximación Polinómica"
            objetivo: "Linealizar y aproximar modelos físicos no lineales mediante polinomios de Taylor."
            concepto_clave_latex: "f(x) = \\sum_{n=0}^{\\infty}\\frac{f^{(n)}(a)}{n!}(x-a)^n \\quad ; \\quad \\sin\\theta \\approx \\theta - \\frac{\\theta^3}{6}"
            ejemplo: "Linealización de la ecuación de oscilación de potencia síncrona (swing equation)."
            bloque_sugerido: "Pomodoro 50/10 • Series de Taylor"
      - codigo: "02021811"
        nombre: "Calor y Ondas"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Termometría, Dilatación Térmica y Esfuerzos Térmicos"
            objetivo: "Cuantificar deformaciones y esfuerzos mecánicos inducidos por gradientes térmicos."
            concepto_clave_latex: "\\Delta L = \\alpha L_0 \\Delta T \\quad ; \\quad \\Delta V = \\beta V_0 \\Delta T \\quad ; \\quad \\sigma_T = -E\\alpha\\Delta T"
            ejemplo: "Diseño de juntas de expansión en tuberías de vapor geotérmico e industrial."
            bloque_sugerido: "Pomodoro 45/10 • Dilatación lineal/volumétrica"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Calorimetría, Capacidad Calorífica y Cambios de Fase"
            objetivo: "Resolver balances térmicos con calor sensible y calor latente de fusión/vaporización."
            concepto_clave_latex: "Q = mc\\Delta T + mL_f \\quad ; \\quad \\sum Q_{\\text{cedido}} + \\sum Q_{\\text{absorbido}} = 0"
            ejemplo: "Almacenamiento térmico latente con materiales de cambio de fase (PCM) solares."
            bloque_sugerido: "Pomodoro 50/10 • Calorimetría con PCM"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Mecanismos de Transferencia de Calor en Física"
            objetivo: "Aplicar leyes de conducción estacionaria, convección y radiación de cuerpo negro."
            concepto_clave_latex: "\\dot{Q}_{\\text{cond}} = kA\\frac{\\Delta T}{L} \\quad ; \\quad \\dot{Q}_{\\text{rad}} = \\varepsilon\\sigma A(T_s^4 - T_{\\text{alr}}^4)"
            ejemplo: "Pérdida térmica a través del vidrio y aislamiento de un colector solar plano."
            bloque_sugerido: "Práctica 45 min • Resistencias térmicas"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Teoría Cinética de los Gases y Equipartición de Energía"
            objetivo: "Conectar temperatura absoluta con energía cinética traslacional molecular y rapidez RMS."
            concepto_clave_latex: "\\bar{K}_{\\text{tras}} = \\frac{3}{2}k_B T \\quad ; \\quad v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}} \\quad ; \\quad C_P - C_V = R"
            ejemplo: "Velocidad molecular media de H2 frente a CH4 y su impacto en fugas de sellos."
            bloque_sugerido: "Pomodoro 45/10 • Teoría cinética"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Primera Ley en Procesos de Gases Ideales y Ciclos"
            objetivo: "Calcular trabajo, calor y energía interna en procesos isobáricos, isotérmicos y adiabáticos."
            concepto_clave_latex: "\\Delta U = Q - W \\quad ; \\quad W_{\\text{isot}} = nRT\\ln\\left(\\frac{V_2}{V_1}\\right) \\quad ; \\quad PV^\\gamma = C"
            ejemplo: "Eficiencia térmica de un ciclo cerrado de gas ideal en el plano P-V."
            bloque_sugerido: "Pomodoro 50/10 • Procesos politrópicos"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Movimiento Armónico Simple y Oscilaciones Amortiguadas"
            objetivo: "Modelar sistemas masa-resorte-amortiguador y resonancia forzada."
            concepto_clave_latex: "x(t) = A e^{-\\beta t}\\cos(\\omega_d t + \\phi) \\quad ; \\quad \\omega_0 = \\sqrt{\\frac{k}{m}}"
            ejemplo: "Amortiguamiento de vibraciones inducidas por vórtices en torres eólicas."
            bloque_sugerido: "Práctica 50 min • MAS y resonancia"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Ondas Mecánicas, Ecuación de Onda y Potencia Ondulatoria"
            objetivo: "Analizar propagación ondulatoria y flujo de energía en medios continuos."
            concepto_clave_latex: "\\frac{\\partial^2 y}{\\partial x^2} = \\frac{1}{v^2}\\frac{\\partial^2 y}{\\partial t^2} \\quad ; \\quad v = \\lambda f \\quad ; \\quad \\bar{P} = \\frac{1}{2}\\mu\\omega^2 A^2 v"
            ejemplo: "Estimación de potencia por metro de frente de ola en energía undimotriz."
            bloque_sugerido: "Pomodoro 45/10 • Cinemática y energía de ondas"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Acústica, Nivel de Intensidad en Decibelios y Efecto Doppler"
            objetivo: "Evaluar propagación sonora, atenuación esférica y niveles normativos dB."
            concepto_clave_latex: "\\beta = 10\\log_{10}\\left(\\frac{I}{I_0}\\right)\\quad ; \\quad I(r) = \\frac{P_s}{4\\pi r^2}"
            ejemplo: "Mapa de atenuación acústica con la distancia alrededor de aerogeneradores."
            bloque_sugerido: "Práctica 40 min • Decibelios ambientales"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Superposición, Ondas Estacionarias y Óptica Solar Básica"
            objetivo: "Aplicar reflexión, ley de Snell e interferencia a concentradores y recubrimientos."
            concepto_clave_latex: "n_1\\sin\\theta_1 = n_2\\sin\\theta_2 \\quad ; \\quad 2n_c d = \\left(m + \\frac{1}{2}\\right)\\lambda"
            ejemplo: "Espesor cuarto de onda de capa antirreflectiva de Si3N4 sobre celdas solares."
            bloque_sugerido: "Taller 45 min • Óptica fotovoltaica"
      - codigo: "03041820"
        nombre: "Fundamentos de Electricidad II"
        creditos: 2
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Señales Sinusoidales, Fasores e Impedancia Compleja"
            objetivo: "Transformar circuitos excitados en régimen permanente AC al dominio fasorial."
            concepto_clave_latex: "\\tilde{V} = V_{\\text{rms}}\\angle\\phi \\quad ; \\quad Z_L = j\\omega L \\quad ; \\quad Z_C = \\frac{1}{j\\omega C} = -j\\frac{1}{\\omega C}"
            ejemplo: "Impedancia equivalente a 60 Hz de un alimentador industrial inductivo."
            bloque_sugerido: "Pomodoro 50/10 • Álgebra fasorial"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Análisis Nodal, de Mallas y Thévenin en Régimen AC"
            objetivo: "Resolver redes AC multifuente a frecuencia constante con aritmética compleja."
            concepto_clave_latex: "Y\\vec{\\tilde{V}}_n = \\vec{\\tilde{I}}_s \\quad ; \\quad Z_{L,\\text{ópt}} = Z_{\\text{th}}^*"
            ejemplo: "Equivalente Thévenin fasorial en el punto de acoplamiento común (PCC) de un inversor."
            bloque_sugerido: "Pomodoro 50/10 • Redes AC complejas"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Potencia Instantánea, Activa, Reactiva, Aparente y Compleja"
            objetivo: "Construir el triángulo de potencias y cuantificar flujo activo y reactivo."
            concepto_clave_latex: "S = \\tilde{V}_{\\text{rms}}\\tilde{I}_{\\text{rms}}^* = P + jQ \\quad ; \\quad |S| = \\sqrt{P^2 + Q^2} \\quad ; \\quad fp = \\cos(\\theta_v - \\theta_i)"
            ejemplo: "Auditoría de potencia activa (kW) y reactiva (kVAr) en planta de refrigeración."
            bloque_sugerido: "Pomodoro 50/10 • Triángulo de potencias"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Corrección del Factor de Potencia Industrial"
            objetivo: "Dimensionar bancos de capacitores para eliminar penalizaciones por energía reactiva."
            concepto_clave_latex: "Q_C = P(\\tan\\theta_1 - \\tan\\theta_2) \\quad ; \\quad C = \\frac{Q_C}{\\omega V_{\\text{rms}}^2}"
            ejemplo: "Banco de condensadores para elevar el factor de potencia de 0.76 a 0.96 a 440 V."
            bloque_sugerido: "Práctica 45 min • Compensación reactiva"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas Trifásicos Equilibrados (Conexiones Y y Δ)"
            objetivo: "Analizar tensiones y corrientes de línea y de fase en sistemas trifásicos simétricos."
            concepto_clave_latex: "V_L = \\sqrt{3}\\,V_f \\quad ; \\quad I_L = \\sqrt{3}\\,I_f \\quad ; \\quad P_{3\\phi} = \\sqrt{3}\\,V_L I_L\\cos\\theta"
            ejemplo: "Alimentación trifásica de bombas centrífugas de agua helada en conexión Y-Δ."
            bloque_sugerido: "Pomodoro 50/10 • Circuitos 3Φ equilibrados"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas Trifásicos Desequilibrados y Medición de Aron"
            objetivo: "Calcular corrientes de neutro en cargas asimétricas y potencia con dos vatímetros."
            concepto_clave_latex: "\\tilde{I}_N = \\tilde{I}_a + \\tilde{I}_b + \\tilde{I}_c \\quad ; \\quad P_{3\\phi} = W_1 + W_2,\\;\\; Q_{3\\phi} = \\sqrt{3}(W_1 - W_2)"
            ejemplo: "Desbalance de fases en tableros comerciales con cargas monofásicas distribuidas."
            bloque_sugerido: "Práctica 45 min • Desbalance y Aron"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Respuesta en Frecuencia, Resonancia y Diagramas de Bode"
            objetivo: "Diseñar filtros pasivos RLC y determinar frecuencias de corte y factor de calidad Q."
            concepto_clave_latex: "\\omega_0 = \\frac{1}{\\sqrt{LC}} \\quad ; \\quad Q_0 = \\frac{\\omega_0 L}{R} \\quad ; \\quad H_{\\text{dB}}(\\omega) = 20\\log_{10}|H(j\\omega)|"
            ejemplo: "Filtro LCL a la salida de un inversor solar para atenuar rizado de conmutación PWM."
            bloque_sugerido: "Pomodoro 50/10 • Resonancia y filtros LCL"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Acoplamiento Magnético, Inductancia Mutua y Transformador Ideal"
            objetivo: "Analizar bobinas acopladas con convención de puntos y reflejar impedancias."
            concepto_clave_latex: "\\frac{\\tilde{V}_1}{\\tilde{V}_2} = \\frac{N_1}{N_2} = a \\quad ; \\quad Z_{\\text{in}} = a^2 Z_L \\quad ; \\quad k = \\frac{M}{\\sqrt{L_1 L_2}}"
            ejemplo: "Adaptación de niveles de tensión mediante transformador elevador 0.69/34.5 kV."
            bloque_sugerido: "Práctica 45 min • Acoplamiento magnético"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Cuadripolos (Redes de Dos Puertos) y Armónicos Básicos"
            objetivo: "Caracterizar líneas y filtros mediante matrices ABCD y distorsión armónica THD."
            concepto_clave_latex: "\\begin{bmatrix}\\tilde{V}_1 \\\\ \\tilde{I}_1\\end{bmatrix} = \\begin{bmatrix}A & B \\\\ C & D\\end{bmatrix}\\begin{bmatrix}\\tilde{V}_2 \\\\ -\\tilde{I}_2\\end{bmatrix} \\quad ; \\quad \\text{THD}_V = \\frac{\\sqrt{\\sum_{h=2}^{\\infty} V_h^2}}{V_1}"
            ejemplo: "Parámetros ABCD de líneas cortas y evaluación de THD según límite del 5% IEEE 519."
            bloque_sugerido: "Taller 45 min • Cuadripolos y THD"
      - codigo: "03021815"
        nombre: "Fundamentos de Hidráulica y Neumática"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Propiedades de Fluidos Oleohidráulicos y Aire Comprimido"
            objetivo: "Seleccionar viscosidad, módulo volumétrico y calidad de aire ISO 8573-1."
            concepto_clave_latex: "\\nu = \\frac{\\mu}{\\rho} \\quad ; \\quad \\Delta P = -B\\frac{\\Delta V}{V_0}"
            ejemplo: "Efecto de la temperatura de operación sobre la viscosidad ISO VG 46."
            bloque_sugerido: "Pomodoro 40/10 • Propiedades de fluidos"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Principio de Pascal, Multiplicación de Fuerza e Hidrostática"
            objetivo: "Dimensionar prensas y actuadores mediante transmisión hidrostática de presión."
            concepto_clave_latex: "P_1 = P_2 \\implies \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\quad ; \\quad W = F_1 s_1 = F_2 s_2"
            ejemplo: "Multiplicación de fuerza en el sistema hidráulico de freno de un aerogenerador."
            bloque_sugerido: "Práctica 45 min • Multiplicadores hidráulicos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Conservación de Masa, Bernoulli y Pérdidas en Tuberías"
            objetivo: "Calcular caídas de presión y potencia hidráulica neta en líneas de potencia fluida."
            concepto_clave_latex: "Q = A_1 v_1 = A_2 v_2 \\quad ; \\quad P_{\\text{hid}} = \\Delta P \\cdot Q \\quad ; \\quad \\Delta P_f = f\\frac{L}{D}\\frac{\\rho v^2}{2}"
            ejemplo: "Caída de presión en mangueras de alta presión del sistema de pitch eólico."
            bloque_sugerido: "Pomodoro 50/10 • Potencia hidráulica ΔP·Q"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Bombas Hidráulicas de Desplazamiento Positivo y Compresores"
            objetivo: "Evaluar caudal desplazado, eficiencia volumétrica y potencia al eje."
            concepto_clave_latex: "Q_{\\text{real}} = V_d \\cdot n \\cdot \\eta_v \\quad ; \\quad P_{\\text{eje}} = \\frac{\\Delta P \\cdot Q_{\\text{real}}}{\\eta_t}"
            ejemplo: "Selección de bomba de pistones axiales para mecanismo de orientación (yaw)."
            bloque_sugerido: "Práctica 45 min • Curvas de bombas"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Actuadores Lineales (Cilindros) y Motores Hidráulicos/Neumáticos"
            objetivo: "Calcular fuerza de extensión/retracción, velocidad y torque en actuadores."
            concepto_clave_latex: "F_{\\text{ext}} = P A_p \\eta_m \\quad ; \\quad F_{\\text{ret}} = P(A_p - A_v)\\eta_m \\quad ; \\quad \\tau = \\frac{\\Delta P \\cdot V_d}{2\\pi}\\eta_m"
            ejemplo: "Dimensionamiento de cilindros hidráulicos para seguidores solares de un eje."
            bloque_sugerido: "Pomodoro 50/10 • Cilindros doble efecto"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Válvulas Direccionales, de Presión y Reguladoras de Caudal"
            objetivo: "Diseñar circuitos de control de dirección, alivio y regulación de velocidad."
            concepto_clave_latex: "Q_v = C_d A_o \\sqrt{\\frac{2\\Delta P}{\\rho}} \\quad ; \\quad \\Delta P_{\\text{valv}} = \\xi \\frac{\\rho v^2}{2}"
            ejemplo: "Ajuste de válvula limitadora de presión y regulación meter-out en cargas colgantes."
            bloque_sugerido: "Laboratorio 45 min • Esquemas ISO 1219"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Acumuladores Hidráulicos y Redes de Aire Comprimido"
            objetivo: "Dimensionar acumuladores hidroneumáticos para respaldo de emergencia y pulsaciones."
            concepto_clave_latex: "P_0 V_0^n = P_1 V_1^n = P_2 V_2^n \\quad ; \\quad \\Delta V = V_0\\left[\\left(\\frac{P_0}{P_1}\\right)^{1/n} - \\left(\\frac{P_0}{P_2}\\right)^{1/n}\\right]"
            ejemplo: "Acumulador de nitrógeno para cierre seguro de emergencia de álabes distribuidores."
            bloque_sugerido: "Pomodoro 50/10 • Expansión politrópica"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Electroneumática, Electrohidráulica y Lógica Secuencial"
            objetivo: "Automatizar secuencias A+ B+ A- B- con electroválvulas, sensores y PLC."
            concepto_clave_latex: "S_{\\text{A+}} = \\text{Start}\\cdot a_0 \\cdot b_0 \\quad ; \\quad u(t) = K_p e(t) + K_i\\int_0^t e(\\tau)\\,d\\tau"
            ejemplo: "Secuencia electroneumática automatizada de alimentación de pellets de biomasa."
            bloque_sugerido: "Práctica 50 min • Diagramas espacio-fase"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Eficiencia Energética en Sistemas Neumáticos e Hidráulicos"
            objetivo: "Cuantificar pérdidas por fugas en aire comprimido y ahorro con variadores VFD."
            concepto_clave_latex: "\\dot{m}_{\\text{fuga}} \\propto C_d A_{\\text{orificio}} P_{\\text{abs}} \\quad ; \\quad \\frac{P_2}{P_1} \\approx \\left(\\frac{n_2}{n_1}\\right)^3"
            ejemplo: "Auditoría ultrasónica de fugas de aire comprimido a 7 bar en planta industrial."
            bloque_sugerido: "Taller 45 min • Ahorro energético neumático"
      - codigo: "01021804"
        nombre: "General English III"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "general"
            titulo: "Present Perfect vs. Past Simple: Completed vs. Ongoing Timeframes"
            objetivo: "Diferenciar con precisión marcos temporales cerrados (Past Simple) de periodos abiertos o vigentes (Present Perfect)."
            concepto_clave_latex: ""
            ejemplo: "Global battery prices have fallen by over 80% over the last decade."
            bloque_sugerido: "Timeframe Contrast 40 min • Engineering news briefs & progress updates"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Present Perfect vs. Past Simple: Completed vs. Ongoing Timeframes: Communicative Purpose"
                puntos:
                  - "Past Simple anchors an event in a FINISHED timeframe (last year, in 2023, two hours ago, when I was a freshman)."
                  - "Present Perfect links past actions to an UNFINISHED timeframe (this week, so far, since January, over the past decade)."
                  - "News pattern: announce headlines in Present Perfect ('Researchers have developed a new perovskite cell'), then give details in Past Simple ('They tested it in Berlin last May')."
                ejemplo: "Global battery prices have fallen by over 80% over the last decade."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Unfinished time: today, this cuatrimestre, recently, up to now -> Present Perfect."
                  - "Finished time: yesterday, last Friday, in the 19th century -> Past Simple."
                  - "'For' (duration) in Past Simple = finished period; in Present Perfect = still continuing now."
                tabla:
                  - ["Time Expression", "Required Tense", "Example"]
                  - ["in 2021 / last month", "Past Simple", "Colombia passed Law 2099 in 2021."]
                  - ["since 2021 / so far", "Present Perfect", "Solar capacity has tripled since 2021."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Compare: 'Dr. Ruiz worked at CENIT for five years' (he no longer works there) vs. 'Dr. Ruiz has worked here for five years' (he still works here)."
                  - "Questions with 'When...?' or 'What time...?' ALWAYS require Past Simple ('When did you submit it?'), never Present Perfect!"
                ejemplo: "Our team ran three thermal simulations yesterday afternoon."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Incorrect: 'I have finished the code an hour ago' -> Correct: 'I finished the code an hour ago.'"
                  - "Incorrect: 'Did you see the new lab yet?' (academic) -> Prefer: 'Have you seen the new lab yet?'"
                tabla:
                  - ["Question Opener", "Correct Tense", "Model"]
                  - ["When / What time...?", "Past Simple", "When did the outage happen?"]
                  - ["How long... (still active)?", "Present Perfect", "How long has the grid been online?"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Global battery prices have fallen by over 80% over the last decade."
                  - "Our team ran three thermal simulations yesterday afternoon."
                  - "So far this semester, we have completed four laboratory reports."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'In 2024, wind power (reached / has reached) a new record' -> 'reached'."
                  - "Write a 2-sentence engineering news brief (Present Perfect headline + Past Simple detail)."
                  - "Contrast 'for 3 years' in Past Simple vs. Present Perfect."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 2
            corte: 1
            modalidad: "general"
            titulo: "Present Perfect Continuous (For & Since in Long-Term Projects)"
            objetivo: "Enfatizar la duración continua de proyectos, investigaciones y tendencias activas mediante have/has been + -ing."
            concepto_clave_latex: ""
            ejemplo: "Researchers at Unimagdalena have been studying offshore wind potential since 2022."
            bloque_sugerido: "Project Status Drill 40 min • Reporting ongoing R&D milestones"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Present Perfect Continuous (For & Since in Long-Term Projects): Communicative Purpose"
                puntos:
                  - "Form: have / has + been + verb-ing."
                  - "Focuses on the ONGOING ACTIVITY and DURATION ('We have been monitoring solar irradiance since March') or visible recent effort ('The motor is warm because it has been running all morning')."
                  - "Use 'FOR' + length of time (for six months, for three hours) vs. 'SINCE' + starting point (since 2024, since 8:00 a.m.)."
                ejemplo: "Researchers at Unimagdalena have been studying offshore wind potential since 2022."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Activity focus (PPC): 'I have been writing the literature review all week' (in progress)."
                  - "Result/Quantity focus (PPS): 'I have written twelve pages so far' (completed count!)."
                  - "Stative verbs (know, own, be) cannot use Continuous -> use Present Perfect Simple ('We have had this sensor since May')."
                tabla:
                  - ["Focus", "Present Perfect Continuous", "Present Perfect Simple"]
                  - ["Core Question", "How long?", "How many / How much?"]
                  - ["Emphasis", "Unfinished ongoing activity", "Completed measurable result"]
                  - ["Example", "We've been testing all day.", "We've tested 15 modules."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions: 'How long have you been working on your CDIO prototype?'"
                  - "Negative: 'The data logger hasn't been recording properly since yesterday's storm.'"
                ejemplo: "How long has the electrolyzer been operating at steady state?"
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never use Present Simple with 'since/for' for ongoing duration: say 'I have been studying here since 2025', NOT 'I am studying here since 2025'!"
                  - "Whenever you state an exact number of times ('three times'), switch to Present Perfect Simple."
                tabla:
                  - ["Marker", "Follows With", "Examples"]
                  - ["FOR (duration)", "Period of time", "for 45 minutes, for two years, for ages"]
                  - ["SINCE (start point)", "Timestamp / Past clause", "since Monday, since 2023, since class began"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Researchers at Unimagdalena have been studying offshore wind potential since 2022."
                  - "How long has the electrolyzer been operating at steady state?"
                  - "We have been debugging this Python script for two hours, and we've fixed four bugs."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Fix: 'She is working in the lab since 7 a.m.' -> 'She has been working in the lab since 7 a.m.'"
                  - "Choose Simple or Continuous: 'They ___ (publish) three papers this year' -> 'have published'."
                  - "Describe 3 ongoing projects using for and since."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 3
            corte: 1
            modalidad: "general"
            titulo: "Second Conditional: Hypothetical Scenarios & Counterfactuals"
            objetivo: "Analizar escenarios hipotéticos, mejoras de diseño ideales y situaciones contrafactuales en el presente."
            concepto_clave_latex: ""
            ejemplo: "If superconducting cables operated at room temperature, transmission losses would vanish."
            bloque_sugerido: "Thought Experiment 40 min • Idealized physics & engineering design scenarios"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Second Conditional: Hypothetical Scenarios & Counterfactuals: Communicative Purpose"
                puntos:
                  - "Form: If + Past Simple (subjunctive), would / could / might + base verb."
                  - "Expresses unreal, imaginary, or unlikely situations in the present or future ('If our building had solar glass, it would cut cooling loads by 25%')."
                  - "Formal academic subjunctive uses 'were' for ALL subjects: 'If friction were zero, the flywheel would spin indefinitely'."
                ejemplo: "If superconducting cables operated at room temperature, transmission losses would vanish."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Certainty variation: 'would' (predicted hypothetical outcome), 'could' (hypothetical ability/possibility), 'might' (uncertain possibility)."
                  - "Giving advice: 'If I were you, I would double-check the boundary conditions.'"
                  - "Polite hypothetical questions: 'What would happen if we doubled the pressure?'"
                tabla:
                  - ["Conditional", "Reality Status", "Structure"]
                  - ["First Conditional", "Real & plausible future", "If we add insulation, losses will drop."]
                  - ["Second Conditional", "Unreal / Hypothetical now", "If we had a supercomputer, it would run in 1 s."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Alternative openers: 'Suppose / Imagine (that) the grid failed — how would the hospital microgrid respond?'"
                  - "Second Conditional softens engineering proposals: 'It would be more cost-effective if we installed variable-speed drives.'"
                ejemplo: "How much CO2 would Santa Marta avoid if all public buses were electric?"
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never put 'would' inside the If-clause (*If we would have...* is wrong -> 'If we had...')."
                  - "Remember: Past Simple in Second Conditional refers to PRESENT/FUTURE unreality, NOT past time!"
                tabla:
                  - ["Incorrect", "Correct Academic Form", "Why"]
                  - ["If it would fail, we stop", "If it failed, we would stop", "No 'would' in If-clause"]
                  - ["If I was in charge (informal)", "If I were in charge (formal)", "Subjunctive 'were'"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "If superconducting cables operated at room temperature, transmission losses would vanish."
                  - "How much CO2 would Santa Marta avoid if all public buses were electric?"
                  - "If I were the project lead, I would select lithium iron phosphate batteries."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete: 'If wind speed ___ (be) constant, forecasting ___ (be) trivial.'"
                  - "Contrast 1st vs. 2nd Conditional for a real vs. ideal lab budget."
                  - "Answer: 'What would happen if Earth's atmosphere had no greenhouse gases?'"
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 4
            corte: 2
            modalidad: "general"
            titulo: "Passive Voice I (Present & Past Simple): Focusing on Processes & Results"
            objetivo: "Redactar descripciones objetivas de procesos técnicos y reportes de laboratorio utilizando la Voz Pasiva."
            concepto_clave_latex: ""
            ejemplo: "In a Rankine cycle, high-pressure steam is expanded through a turbine."
            bloque_sugerido: "Lab Methods Writing 45 min • Objective process description in Passive Voice"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Passive Voice I (Present & Past Simple): Focusing on Processes & Results: Communicative Purpose"
                puntos:
                  - "Form: Subject (receiver) + am/is/are (Present) or was/were (Past) + Past Participle (V3)."
                  - "Academic & technical English favors Passive Voice when the PROCESS, ACTION, or RESULT matters more than the human actor ('The samples were heated to 450 K')."
                  - "Add 'by + agent' ONLY when the actor provides essential information ('The law was formulated by Fourier')."
                ejemplo: "In a Rankine cycle, high-pressure steam is expanded through a turbine."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Present Simple Passive (processes): 'Biogas is produced through anaerobic digestion.'"
                  - "Past Simple Passive (methods/history): 'Three sensors were mounted along the pipe.'"
                  - "Sequence connectors in process writing: First, Next, Subsequently, Finally."
                tabla:
                  - ["Tense", "Active Voice", "Passive Voice (Objective)"]
                  - ["Present Simple", "Inverters convert DC to AC.", "DC is converted to AC by inverters."]
                  - ["Past Simple", "We calibrated the probe.", "The probe was calibrated prior to testing."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Questions in Passive: 'Where is geothermal energy harvested?' / 'When was the turbine commissioned?'"
                  - "Distinguish 'by' (agent/person/system) vs. 'with' (instrument/tool/material): 'Voltage was measured WITH a digital oscilloscope'."
                ejemplo: "All experimental measurements were recorded at five-second intervals."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Intransitive verbs (happen, occur, arrive, rise, consist) CANNOT be passive! Say 'A voltage drop occurred', NEVER 'was occurred'!"
                  - "Always check V3 accuracy: 'is transmitted', 'was chosen', 'were driven'."
                tabla:
                  - ["Intransitive Trap", "Incorrect Passive", "Correct Active"]
                  - ["occur / happen", "An error was occurred", "An error occurred"]
                  - ["rise (no object)", "Temperature was risen", "Temperature rose (or was raised)"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "In a Rankine cycle, high-pressure steam is expanded through a turbine."
                  - "All experimental measurements were recorded at five-second intervals."
                  - "Voltage was stepped up from 13.8 kV to 220 kV at the substation."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Convert to Passive: 'Technicians inspect the blades every six months.'"
                  - "Fix: 'A short circuit was happened in Node 3' -> 'A short circuit occurred in Node 3.'"
                  - "Describe a 4-step energy conversion process in Present Passive."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 5
            corte: 2
            modalidad: "general"
            titulo: "Defining & Non-Defining Relative Clauses (Who, Which, That, Whose, Where)"
            objetivo: "Construir definiciones técnicas precisas e insertar información explicativa mediante cláusulas relativas."
            concepto_clave_latex: ""
            ejemplo: "An inverter is a power electronic device that converts DC into AC."
            bloque_sugerido: "Technical Definitions 40 min • Writing encyclopedic engineering definitions"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Defining & Non-Defining Relative Clauses (Who, Which, That, Whose, Where): Communicative Purpose"
                puntos:
                  - "Defining Relative Clauses identify WHICH person/thing we mean -> NO commas; 'that' can replace 'who' or 'which'."
                  - "Non-Defining Relative Clauses add extra info to an already identified noun -> MUST use commas; NEVER use 'that'!"
                  - "Relative words: who (people), which (things/whole clause), that (defining only), whose (possession), where (place = in which)."
                ejemplo: "An inverter is a power electronic device that converts DC into AC."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Defining: 'A pyranometer is an instrument that/which measures solar irradiance.'"
                  - "Non-defining: 'Copper, which has low resistivity, is widely used in windings.'"
                  - "Omitting pronoun: you can drop who/which/that in defining clauses ONLY when it is the OBJECT ('The data [that] we collected is clean')."
                tabla:
                  - ["Clause Type", "Commas?", "Allowed Pronouns & Example"]
                  - ["Defining (essential)", "No commas", "Cells that/which use silicon dominate."]
                  - ["Non-defining (extra)", "Commas required", "Silicon, which is abundant, is reliable."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "'Whose' works for BOTH people and inanimate systems: 'A turbine whose blades are pitched optimally captures more power.'"
                  - "Sentential 'which' comments on an entire fact: 'Efficiency rose by 4%, which exceeded our target.'"
                ejemplo: "La Guajira, where trade winds blow steadily all year, hosts wind projects."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "NEVER use 'what' as a relative pronoun after a noun (*the formula what we used* -> 'the formula that we used')!"
                  - "Do not repeat the object pronoun: 'The circuit that we built' (NOT 'that we built it')."
                tabla:
                  - ["Relative Word", "Replaces", "Technical Definition"]
                  - ["where (= in which)", "Place / System zone", "The chamber where combustion occurs..."]
                  - ["whose", "his / her / its", "Materials whose conductivity is high..."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "An inverter is a power electronic device that converts DC into AC."
                  - "La Guajira, where trade winds blow steadily all year, hosts wind projects."
                  - "Engineers select materials whose thermal resistance minimizes heat leakage."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Join (non-defining): 'Law 1715 promotes renewables. It was enacted in 2014.'"
                  - "Can 'that' be omitted? 'The sensor that measures pressure' (No, subject!) vs. 'The sensor that we bought' (Yes, object!)."
                  - "Write 3 formal definitions of energy devices using defining relative clauses."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 6
            corte: 2
            modalidad: "general"
            titulo: "Used to & Would: Describing Past Habits & Technological Evolution"
            objetivo: "Contrastar tecnologías antiguas y hábitos pasados frente a estándares actuales usando used to, would y be/get used to."
            concepto_clave_latex: ""
            ejemplo: "Households used to use 60 W incandescent bulbs, whereas LEDs now use 8 W."
            bloque_sugerido: "Tech Evolution 35 min • Comparing legacy vs. smart energy systems"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Used to & Would: Describing Past Habits & Technological Evolution: Communicative Purpose"
                puntos:
                  - "'Used to + base verb' describes BOTH past habits AND past states that are no longer true ('Power grids used to be strictly unidirectional')."
                  - "'Would + base verb' describes repeated past ACTIONS/routines (NOT states like be, have, own, live) once past context is set."
                  - "Contrast: 'be used to + noun/-ing' (be accustomed to) & 'get used to + noun/-ing' (adapt to)."
                ejemplo: "Households used to use 60 W incandescent bulbs, whereas LEDs now use 8 W."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative: 'Factories used to burn coal directly on site.'"
                  - "Negative & Question drop the -d: 'didn't use to' / 'Did grids use to store solar energy?'"
                  - "'No longer' / 'not... anymore' express the present contrast: 'We no longer rely on analog meters.'"
                tabla:
                  - ["Structure", "Followed By", "Meaning & Example"]
                  - ["used to", "Base verb", "Past habit/state: Grids used to be analog."]
                  - ["be used to", "Noun / Verb-ing", "Accustomed now: I'm used to coding in Python."]
                  - ["get used to", "Noun / Verb-ing", "Adapting: You'll get used to LaTeX fast."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Check state verbs: say 'There used to be a diesel generator here', NEVER 'There would be a diesel generator here'!"
                  - "For a single one-time past event, use Past Simple ('In 2019, we installed LEDs'), NOT 'used to'."
                ejemplo: "Grid operators didn't use to deal with bidirectional prosumer power flows."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Watch the -ing trap after 'be used to': 'She is used to waking up at 5:30 a.m.', NOT 'used to wake up' when 'is' precedes it!"
                  - "Don't use 'use to' for present habits -> use 'usually' ('I usually study at night', NOT 'I use to study')."
                tabla:
                  - ["False Friend Trap", "Incorrect", "Natural English"]
                  - ["Present habit ('suelo')", "I use to study daily", "I usually study daily"]
                  - ["After 'am/is/are'", "I am used to work late", "I am used to working late"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Households used to use 60 W incandescent bulbs, whereas LEDs now use 8 W."
                  - "Grid operators didn't use to deal with bidirectional prosumer power flows."
                  - "First-year students quickly get used to solving equations with SI units."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose: 'Ten years ago, EVs (used to / would) be rare' (state!) -> 'used to'."
                  - "Fix: 'I use to drink coffee every morning' -> 'I usually drink coffee every morning.'"
                  - "Contrast 3 legacy energy technologies with modern equivalents."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 7
            corte: 2
            modalidad: "general"
            titulo: "Modals of Deduction & Probability (Must, Might, Could, Can't)"
            objetivo: "Formular hipótesis diagnósticas y niveles de certeza ante evidencias técnicas en el presente."
            concepto_clave_latex: ""
            ejemplo: "The thermocouple reads -200°C in Santa Marta — the wire must be disconnected."
            bloque_sugerido: "Fault Diagnosis Lab 40 min • Troubleshooting engineering anomalies in English"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Modals of Deduction & Probability (Must, Might, Could, Can't): Communicative Purpose"
                puntos:
                  - "Logical certainty (~95% sure it IS true): 'must + base verb' ('The LED is on, so the supply must be active')."
                  - "Possibility (~30–50% sure): 'may / might / could + base verb' ('The noise might come from a worn bearing')."
                  - "Logical impossibility (~95% sure it is NOT true): 'can't / couldn't + base verb' ('Efficiency can't exceed 100%!')."
                ejemplo: "The thermocouple reads -200°C in Santa Marta — the wire must be disconnected."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Continuous deduction (happening right now): modal + be + verb-ing ('The inverter might be clipping peak power')."
                  - "Negative possibility: use 'might not / may not' ('The sensor may not be calibrated')."
                  - "CRITICAL: 'could not' means 0% impossible, whereas 'might not' means 'maybe not'!"
                tabla:
                  - ["Certainty Level", "Modal Form", "Diagnostic Deduction"]
                  - ["~95% Certain (Yes)", "must + V / be V-ing", "Current is zero; the fuse must be blown."]
                  - ["~40% Possible", "may / might / could", "A loose cable could cause this drop."]
                  - ["~95% Impossible (No)", "can't / couldn't", "That reading can't be right (η > 1)!"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Opposite of deductive 'must' is 'CAN'T', NOT 'mustn't' ('mustn't' is only for prohibition!)."
                  - "Avoid 'can' for specific present possibility: say 'There may/could be a leak', NOT 'There can be a leak right now' (use 'can' for general theoretical possibility: 'Overheating can damage cells')."
                ejemplo: "Harmonic distortion could be causing the transformer vibration."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Incorrect: 'The battery mustn't be full; voltage is 10.5 V' -> Correct: 'The battery can't be full; voltage is 10.5 V.'"
                  - "Keep base verb 'be' after modals: 'It might be faulty', NOT 'It might faulty'."
                tabla:
                  - ["Modal Pair", "Meaning Difference", "Example"]
                  - ["might not", "Uncertain (maybe not)", "The report might not arrive today."]
                  - ["couldn't / can't", "Logically impossible", "Perpetual motion can't work."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "The thermocouple reads -200°C in Santa Marta — the wire must be disconnected."
                  - "Harmonic distortion could be causing the transformer vibration."
                  - "That Carnot efficiency calculation can't be correct for these temperatures."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Diagnose 3 anomalies using must, might/could, and can't."
                  - "Fix: 'It mustn't be copper; it's magnetic!' -> 'It can't be copper; it's magnetic!'"
                  - "Explain the difference between 'might not work' and 'can't work'."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 8
            corte: 3
            modalidad: "general"
            titulo: "Gerunds (-ing) vs. Infinitives (to + verb) after Specific Verbs"
            objetivo: "Emplear correctamente gerundios e infinitivos como sujetos, complementos de preposición y patrones verbales académicos."
            concepto_clave_latex: ""
            ejemplo: "Installing rooftop PV reduces peak air-conditioning demand on campus."
            bloque_sugerido: "Academic Syntax 40 min • Verb complementation in technical writing"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Gerunds (-ing) vs. Infinitives (to + verb) after Specific Verbs: Communicative Purpose"
                puntos:
                  - "Gerund (verb-ing) acts as a noun: (1) sentence subject ('Reducing heat loss saves fuel'), (2) after ALL prepositions ('by optimizing, without losing, interested in modeling'), (3) after verbs like avoid, consider, suggest, recommend, finish, keep, involve."
                  - "To-Infinitive (to + verb): (1) purpose ('in order to cool the core'), (2) after adjectives ('easy to install'), (3) after verbs like decide, expect, manage, fail, afford, plan, tend."
                ejemplo: "Installing rooftop PV reduces peak air-conditioning demand on campus."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Preposition + -ing ALWAYS (even when 'to' is a preposition: 'look forward to presenting', 'lead to overheating')."
                  - "Make / Let + object + BARE infinitive (no 'to'): 'Heat makes gases expand' (Passive adds 'to': 'is made to expand')."
                  - "Meaning-shift verbs: stop, remember, try + -ing vs. + to-infinitive!"
                tabla:
                  - ["Pattern", "Key Academic Verbs", "Example"]
                  - ["Verb + -ing", "avoid, consider, suggest, involve", "We suggest insulating the valve."]
                  - ["Verb + to + V", "aim, tend, fail, manage, enable (+obj)", "Sensors enable us to track loads."]
                  - ["Prep + -ing", "by, for, without, lead to", "Cool the cell by increasing airflow."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Meaning shift: 'stop to check' (pause an activity in order to check) vs. 'stop checking' (quit checking)."
                  - "'Try to solve' (attempt something difficult) vs. 'try restarting' (test an experiment/method to see if it helps)."
                ejemplo: "Our algorithm managed to reduce forecasting error by 14%."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Watch 'suggest / recommend': NEVER say *suggest us to use*! Say 'suggest using' OR 'suggest that we use'."
                  - "Use -ing (not infinitive) as concise technical subjects: 'Storing hydrogen requires compression'."
                tabla:
                  - ["Verb", "+ Gerund (-ing)", "+ Infinitive (to + V)"]
                  - ["remember", "Recall past memory: remember testing it", "Don't forget task: remember to ground it"]
                  - ["try", "Experiment option: try lowering the step", "Make effort: try to converge the solver"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Installing rooftop PV reduces peak air-conditioning demand on campus."
                  - "Our algorithm managed to reduce forecasting error by 14%."
                  - "We improved thermal efficiency by preheating the combustion air."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Fix: 'The advisor suggested us to recalibrate' -> 'suggested recalibrating / that we recalibrate'."
                  - "Complete: 'High resistance leads to ___ (lose) energy as heat' -> 'losing'."
                  - "Write 4 sentences using 'by + -ing', 'in order to', 'enable + obj + to', and 'involve + -ing'."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 9
            corte: 3
            modalidad: "general"
            titulo: "Question Tags & Echo Questions in Academic Discussions"
            objetivo: "Confirmar datos, mantener discusiones fluidas y verificar supuestos técnicos mediante Question Tags."
            concepto_clave_latex: ""
            ejemplo: "Grid frequency in Colombia is 60 Hz, isn't it?"
            bloque_sugerido: "Seminar Dialogue 35 min • Confirming data & active listening in Q&A"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Question Tags & Echo Questions in Academic Discussions: Communicative Purpose"
                puntos:
                  - "Polarity Flip Rule: Affirmative statement -> Negative tag ('is it? -> isn't it?'); Negative statement -> Affirmative tag ('isn't it? -> is it?')."
                  - "Match the auxiliary or modal of the main clause (is -> isn't, can -> can't, have -> haven't; Present/Past Simple -> don't/doesn't/didn't) + pronoun."
                  - "Intonation: FALLING = confirming what you already think is true; RISING = genuine question."
                ejemplo: "Grid frequency in Colombia is 60 Hz, isn't it?"
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "With To Be / Modals: 'Copper is a great conductor, isn't it?' / 'We can export to PDF, can't we?'"
                  - "With Action Verbs: 'The turbine reached 1500 rpm, didn't it?'"
                  - "Special tags: 'I am on Slide 4, aren't I?' | 'Let's start the timer, shall we?' | 'Nothing failed, did it?'"
                tabla:
                  - ["Main Clause", "Question Tag", "Special Note"]
                  - ["I'm next,", "aren't I?", "Never *amn't I*"]
                  - ["Let's test Node 2,", "shall we?", "Collaborative proposal"]
                  - ["There's no current,", "is there?", "Negative word -> positive tag"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Words like never, rarely, hardly, nobody, nothing make the clause NEGATIVE -> use a POSITIVE tag ('The system rarely overheats, does it?')."
                  - "Echo questions show active listening in seminars: 'A: Efficiency hit 46%. B: Did it? That's impressive!'"
                ejemplo: "We haven't exceeded the 1.2 MB PDF limit, have we? No, we haven't."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Spanish uses invariable '¿verdad?' / '¿no?'; English MUST mirror the exact auxiliary and pronoun every time!"
                  - "Answer tags according to the FACT: 'The valve isn't open, is it?' -> If closed: 'No, it isn't' (NOT 'Yes, it isn't'!)."
                tabla:
                  - ["Statement", "Wrong Tag", "Correct Tag"]
                  - ["You calibrated it,", "no? / isn't it?", "didn't you?"]
                  - ["She rarely misses lab,", "doesn't she?", "does she?"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Grid frequency in Colombia is 60 Hz, isn't it?"
                  - "We haven't exceeded the 1.2 MB PDF limit, have we? No, we haven't."
                  - "Let's compare the two thermodynamic cycles, shall we?"
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Add tags: 'They built a prototype, ___?' / 'It hardly ever snows here, ___?'"
                  - "Add tags: 'I'm responsible for Slide 2, ___?' / 'Let's verify the units, ___?'"
                  - "Practice rising vs. falling intonation on 4 technical confirmation questions."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 10
            corte: 3
            modalidad: "general"
            titulo: "Connectors of Contrast, Addition & Cause (Although, Despite, Due to, Therefore)"
            objetivo: "Articular párrafos argumentativos y reportes técnicos con conectores lógicos de contraste, adición, causa y consecuencia."
            concepto_clave_latex: ""
            ejemplo: "Although initial capital costs are high, solar microgrids offer low operating expenses."
            bloque_sugerido: "Cohesion Workshop 40 min • Linking clauses cleanly in engineering reports"
            slides:
              - numero: 1
                seccion: "CEFR B1.1 • CORE CONCEPT"
                titulo: "Connectors of Contrast, Addition & Cause (Although, Despite, Due to, Therefore): Communicative Purpose"
                puntos:
                  - "CONTRAST + Clause (S+V): 'although / even though / whereas / while'. CONTRAST + Noun/-ing: 'despite / in spite of'. Sentence linker: 'However, / Nevertheless,'."
                  - "CAUSE + Clause: 'because / since / as'. CAUSE + Noun/-ing: 'due to / owing to / because of'."
                  - "RESULT (new sentence or after semicolon): 'Therefore, / Consequently, / As a result, / Thus,'."
                ejemplo: "Although initial capital costs are high, solar microgrids offer low operating expenses."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Clause vs. Noun Phrase rule: 'Although wind was low, output remained stable' vs. 'Despite low wind, output remained stable'."
                  - "Bridge trick: 'despite the fact that + S + V' converts a noun preposition into a clause connector!"
                  - "Addition: 'Furthermore, / Moreover, / In addition to + noun/-ing'."
                tabla:
                  - ["Relation", "+ Full Clause (S + V)", "+ Noun Phrase / -ing"]
                  - ["Contrast", "although / even though / whereas", "despite / in spite of"]
                  - ["Cause", "because / since / as", "due to / owing to / because of"]
                  - ["Addition", "Moreover, / Furthermore, (sentence)", "in addition to / besides"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Punctuation mastery: 'Efficiency dropped; therefore, we cleaned the panels.' (semicolon BEFORE 'therefore', comma AFTER!)."
                  - "Use 'whereas / while' to contrast two symmetrical facts: 'PV generates DC, whereas wind turbines typically feed AC systems.'"
                ejemplo: "Voltage fluctuated due to sudden cloud cover over the campus array."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "NEVER write 'despite of' (*in spite of* has 'of', *despite* NEVER takes 'of'!)."
                  - "Never put both 'Although' and 'but' in the same sentence: pick one!"
                tabla:
                  - ["Common Error", "Correction", "Why"]
                  - ["Despite of the heat,", "Despite the heat, / In spite of the heat,", "'Despite' takes no 'of'"]
                  - ["Although it rained, but...", "Although it rained, we tested.", "No 'but' with 'although'"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Although initial capital costs are high, solar microgrids offer low operating expenses."
                  - "Voltage fluctuated due to sudden cloud cover over the campus array."
                  - "Thermal losses exceeded 12%; therefore, additional rock-wool insulation was installed."
                ejemplo: "Academic Register (CEFR B1.1): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Transform 'Although the battery was cold, it delivered full current' -> use 'Despite...'."
                  - "Transform 'Because resistance rose, current fell' -> use 'Due to...' and 'Consequently,'."
                  - "Write a 5-sentence technical paragraph using 4 different logical connectors."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 11
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Limits & Continuity Verbalization"
            objetivo: "Leer rigurosamente límites laterales, límites al infinito y condiciones de continuidad en inglés académico."
            concepto_clave_latex: "\\lim_{x \\to a^+} f(x) = L \\quad ; \\quad \\lim_{t \\to \\infty} e^{-t/\\tau} = 0 \\quad ; \\quad \\lim_{x \\to c} f(x) = f(c)"
            verbalizacion_ingles: "• lim_{x -> a⁺} f(x) = L -> \"the limit of f of x as x approaches a from the right (or from above) equals L\" (for a⁻: \"from the left / from below\").\n• lim_{t -> ∞} e^(-t/τ) = 0 -> \"the limit as t approaches infinity (or tends to infinity) of e to the minus t over tau equals zero\".\n• Continuity: \"f is continuous at c if the limit of f of x as x approaches c equals f of c\"."
            ejemplo: "Exposición del estado estacionario térmico cuando t -> ∞: 'As time tends to infinity, the transient exponential term vanishes'."
            bloque_sugerido: "Calculus Speech 30 min • Verbalizing limits & asymptotic steady states"
          - numero_tema: 12
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Ordinary & Partial Derivatives (Leibniz & Lagrange Notation)"
            objetivo: "Verbalizar derivadas ordinarias, segundas derivadas, notación prima/punto y derivadas parciales."
            concepto_clave_latex: "\\frac{dy}{dx} = f'(x) \\quad ; \\quad a = \\frac{d^2x}{dt^2} = \\ddot{x} \\quad ; \\quad \\left(\\frac{\\partial P}{\\partial T}\\right)_V = \\frac{nR}{V}"
            verbalizacion_ingles: "• dy/dx -> \"d y by d x\" or \"d y over d x\" or formally \"the first derivative of y with respect to x\".\n• f'(x), f''(x) -> \"f prime of x\", \"f double prime of x\"  |  ẋ, ẍ -> \"x dot\", \"x double dot\" (time derivatives).\n• d²x/dt² -> \"d squared x by d t squared\" (\"the second derivative of x with respect to t\").\n• (∂P/∂T)_V -> \"the partial derivative of P with respect to T at constant volume V\" (or \"partial P over partial T, holding V constant\")."
            ejemplo: "Lectura de relaciones termodinámicas de Maxwell y tasas de transferencia de calor dQ/dt ('Q dot')."
            bloque_sugerido: "Derivative Fluency 35 min • Leibniz, Lagrange, Newton-dot & partials aloud"
          - numero_tema: 13
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Indefinite & Definite Integrals"
            objetivo: "Pronunciar integrales indefinidas, integrales definidas con límites e integrales de línea o superficie cerradas."
            concepto_clave_latex: "\\int f(x)\\,dx = F(x) + C \\quad ; \\quad E = \\int_{t_1}^{t_2} P(t)\\,dt \\quad ; \\quad \\oint \\vec{E}\\cdot d\\vec{l} = -\\frac{d\\Phi_B}{dt}"
            verbalizacion_ingles: "• ∫ f(x) dx = F(x) + C -> \"the indefinite integral of f of x d x equals capital F of x plus a constant of integration C\".\n• ∫_{t₁}^{t₂} P(t) dt -> \"the definite integral from t sub one to t sub two of P of t d t\".\n• ∮ E · dl = -dΦ_B/dt -> \"the closed line integral (or contour integral) of vector E dot d l equals minus d Phi sub B by d t\"."
            ejemplo: "Explicación oral en inglés de cómo la energía eléctrica facturada es la integral definida de la potencia activa en el tiempo."
            bloque_sugerido: "Integral Reading 30 min • Definite bounds & Faraday's closed-loop integral"
          - numero_tema: 14
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Electric Circuits & Phasor Notation"
            objetivo: "Leer impedancias complejas, valores eficaces RMS y fasores de tensión/corriente en régimen AC."
            concepto_clave_latex: "Z = R + jX_L \\quad ; \\quad V_{\\text{rms}} = \\frac{V_m}{\\sqrt{2}} \\quad ; \\quad \\tilde{V} = V_0 \\angle \\phi = V_0 e^{j\\phi}"
            verbalizacion_ingles: "• Z = R + j X_L -> \"complex impedance Z equals resistance R plus j times inductive reactance X sub L\" (in Electrical Engineering, j is used instead of i to avoid confusion with current!).\n• V_rms = V_m / √2 -> \"V r-m-s (root-mean-square voltage) equals peak voltage V sub m over the square root of two\".\n• Ṽ = V₀ ∠ φ -> \"phasor V tilde equals V naught at an angle of phi\"."
            ejemplo: "Defensa oral de un análisis fasorial de circuito monofásico a 60 Hz indicando desfase inductivo ('lagging power factor')."
            bloque_sugerido: "AC Phasor Speech 35 min • Complex impedance, RMS & polar phasor reading"
          - numero_tema: 15
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Summations, Products & Series"
            objetivo: "Verbalizar notación sigma de sumatorias, productorias pi y expansiones en series de potencias o Fourier."
            concepto_clave_latex: "\\bar{x} = \\frac{1}{n}\\sum_{i=1}^{n} x_i \\quad ; \\quad \\eta_{\\text{sys}} = \\prod_{k=1}^{m} \\eta_k \\quad ; \\quad e^x = \\sum_{n=0}^{\\infty} \\frac{x^n}{n!}"
            verbalizacion_ingles: "• Σ_{i=1}^n x_i -> \"the sum from i equals one to n of x sub i\".\n• Π_{k=1}^m η_k -> \"the product from k equals one to m of eta sub k\".\n• Σ_{n=0}^∞ x^n / n! -> \"the infinite sum from n equals zero to infinity of x to the n over n factorial\"."
            ejemplo: "Eficiencia global de una cadena energética (caldera × turbina × generador × transformador) leída como productoria Π η_k."
            bloque_sugerido: "Series & Sigma Drill 30 min • Discrete sums, factorials & cascaded efficiencies"
          - numero_tema: 16
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Complex Numbers, Euler's Identity & Harmonic Waveforms"
            objetivo: "Expresar señales sinusoidales en el dominio del tiempo, frecuencia angular, conjugados complejos y fórmula de Euler."
            concepto_clave_latex: "e^{j\\omega t} = \\cos(\\omega t) + j\\sin(\\omega t) \\quad ; \\quad v(t) = V_m\\cos(\\omega t + \\theta_v) \\quad ; \\quad S = \\tilde{V}\\tilde{I}^*"
            verbalizacion_ingles: "• e^(jωt) = cos(ωt) + j sin(ωt) -> \"e to the j omega t equals cosine of omega t plus j sine of omega t\".\n• v(t) = V_m cos(ωt + θ_v) -> \"instantaneous voltage v of t equals V sub m cosine of quantity omega t plus theta sub v\".\n• S = Ṽ Ĩ* -> \"complex power S equals phasor V times the complex conjugate of phasor I (I star)\"."
            ejemplo: "Presentación de potencia compleja trifásica usando el conjugado fasorial de corriente ('I conjugate' o 'I star')."
            bloque_sugerido: "Harmonic Notation 30 min • Euler's identity & complex conjugate power"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Sistemas de Ecuaciones Lineales y Eliminación Gaussiana"
            objetivo: "Resolver sistemas lineales de gran escala mediante reducción por filas Gauss-Jordan."
            concepto_clave_latex: "A\\vec{x} = \\vec{b} \\quad ; \\quad [A \\mid \\vec{b}] \\xrightarrow{\\text{RREF}} [I \\mid \\vec{x}]"
            ejemplo: "Solución de corrientes de malla en una red eléctrica de distribución."
            bloque_sugerido: "Pomodoro 50/10 • Gauss-Jordan"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Álgebra Matricial, Inversas y Factorización LU"
            objetivo: "Operar matrices particionadas, calcular inversas y descomponer A = LU."
            concepto_clave_latex: "A = L U \\quad ; \\quad L\\vec{y} = \\vec{b},\\;\\; U\\vec{x} = \\vec{y} \\quad ; \\quad (AB)^{-1} = B^{-1}A^{-1}"
            ejemplo: "Reutilización de factorización LU en simulaciones horarias de flujo DC."
            bloque_sugerido: "Práctica 45 min • Descomposición LU"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Determinantes, Propiedades y Regla de Cramer"
            objetivo: "Evaluar invertibilidad matricial y sensibilidad mediante determinantes y cofactores."
            concepto_clave_latex: "\\det(A) = \\sum_{j=1}^{n}(-1)^{i+j}a_{ij}M_{ij} \\quad ; \\quad \\det(A) \\neq 0 \\iff A\\text{ es invertible}"
            ejemplo: "Verificación de no singularidad del Jacobiano en Newton-Raphson."
            bloque_sugerido: "Pomodoro 45/10 • Cofactores y Jacobiano"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Espacios Vectoriales, Subespacios, Base y Dimensión"
            objetivo: "Determinar independencia lineal, espacio columna, espacio nulo y rango."
            concepto_clave_latex: "\\dim(\\text{Col } A) + \\dim(\\text{Nul } A) = n \\quad ; \\quad \\text{rango}(A) = \\dim(\\text{Col } A)"
            ejemplo: "Identificación de grados de libertad independientes en balances estequiométricos."
            bloque_sugerido: "Pomodoro 50/10 • Teorema rango-nulidad"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Transformaciones Lineales y Cambio de Base"
            objetivo: "Representar operadores lineales matricialmente y transformar coordenadas."
            concepto_clave_latex: "T(\\alpha\\vec{u} + \\beta\\vec{v}) = \\alpha T(\\vec{u}) + \\beta T(\\vec{v}) \\quad ; \\quad [\\vec{x}]_{\\mathcal{B}} = P_{\\mathcal{B}}^{-1}\\vec{x}"
            ejemplo: "Transformación de Clarke y Park (abc -> dq0) en control de inversores trifásicos."
            bloque_sugerido: "Práctica 50 min • Transformada dq0"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Ortogonalidad, Proceso de Gram-Schmidt y Factorización QR"
            objetivo: "Construir bases ortonormales y proyecciones ortogonales estables."
            concepto_clave_latex: "\\text{proy}_W\\vec{y} = \\sum_{i=1}^{k}(\\vec{y}\\cdot\\vec{u}_i)\\vec{u}_i \\quad ; \\quad A = Q R\\;\\;(Q^T Q = I)"
            ejemplo: "Descomposición ortogonal de armónicos de corriente en calidad de potencia."
            bloque_sugerido: "Pomodoro 50/10 • Gram-Schmidt y QR"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Mínimos Cuadrados Lineales y Estimación de Estado"
            objetivo: "Ajustar sistemas sobredeterminados minimizando la norma euclidiana del residual."
            concepto_clave_latex: "\\hat{x} = (A^T A)^{-1}A^T\\vec{b} \\quad ; \\quad \\|\\vec{b} - A\\hat{x}\\|_2 = \\min"
            ejemplo: "Estimación de estado nodal en redes eléctricas con mediciones redundantes SCADA."
            bloque_sugerido: "Práctica 45 min • Ecuaciones normales"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Valores y Vectores Propios y Diagonalización"
            objetivo: "Calcular el espectro de matrices para desacoplar sistemas dinámicos lineales."
            concepto_clave_latex: "A\\vec{v} = \\lambda\\vec{v} \\quad ; \\quad \\det(A - \\lambda I) = 0 \\quad ; \\quad A = P D P^{-1}"
            ejemplo: "Modos naturales de oscilación electromecánica entre generadores síncronos."
            bloque_sugerido: "Pomodoro 50/10 • Autovalores y estabilidad"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Matrices Simétricas, Formas Cuadráticas y SVD"
            objetivo: "Aplicar diagonalización ortogonal y descomposición en valores singulares."
            concepto_clave_latex: "A = U \\Sigma V^T \\quad ; \\quad Q(\\vec{x}) = \\vec{x}^T A \\vec{x} > 0\\;\\;(\\text{definida positiva})"
            ejemplo: "Reducción de dimensionalidad SVD en mapas espacio-temporales de viento."
            bloque_sugerido: "Taller 45 min • Formas cuadráticas y SVD"
      - codigo: "06011837"
        nombre: "Conversión de Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Clasificación de Recursos y Rutas de Conversión Energética"
            objetivo: "Mapear transformaciones entre energía química, térmica, mecánica, radiante y eléctrica."
            concepto_clave_latex: "E_{\\text{primaria}} \\xrightarrow{\\eta_{\\text{conv}}} E_{\\text{secundaria}} \\xrightarrow{\\eta_{\\text{uso}}} E_{\\text{útil}}"
            ejemplo: "Trazado de cadenas completas de conversión para gas natural, solar e hidráulica."
            bloque_sugerido: "Pomodoro 45/10 • Matriz de conversión"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Balances de Masa, Energía y Exergía en Conversores"
            objetivo: "Cuantificar eficiencia de primera ley y eficiencia exergética de segunda ley."
            concepto_clave_latex: "\\eta_I = \\frac{\\dot{W}_{\\text{útil}}}{\\dot{E}_{\\text{in}}} \\quad ; \\quad \\eta_{II} = \\frac{\\dot{W}_{\\text{útil}}}{\\dot{X}_{\\text{in}}} = 1 - \\frac{\\dot{X}_{\\text{dest}}}{\\dot{X}_{\\text{in}}}"
            ejemplo: "Comparación exergética entre calentamiento resistivo y bomba de calor."
            bloque_sugerido: "Pomodoro 50/10 • Primera vs. Segunda Ley"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Conversión Termoquímica y Eficiencia de Calderas"
            objetivo: "Evaluar pérdidas en gases de chimenea y rendimiento de generadores de vapor."
            concepto_clave_latex: "\\eta_{\\text{caldera}} = \\frac{\\dot{m}_v(h_{\\text{sal}} - h_{\\text{ent}})}{\\dot{m}_c\\cdot\\text{PCI}}"
            ejemplo: "Balance térmico directo e indirecto de una caldera bagacera."
            bloque_sugerido: "Práctica 45 min • Balance de caldera"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Conversión Termomecánica: Turbinas de Vapor y de Gas"
            objetivo: "Analizar conversión de entalpía en potencia mecánica al eje en ciclos térmicos."
            concepto_clave_latex: "\\dot{W}_t = \\dot{m}(h_1 - h_2) \\quad ; \\quad \\eta_{\\text{iso},t} = \\frac{h_1 - h_2}{h_1 - h_{2s}}"
            ejemplo: "Potencia de salida en un ciclo combinado gas-vapor de alta eficiencia (60%)."
            bloque_sugerido: "Pomodoro 50/10 • Ciclos térmicos"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Motores de Combustión Interna y Microcogeneración"
            objetivo: "Evaluar consumo específico de combustible (BSFC) y recuperación de calor residual."
            concepto_clave_latex: "\\text{BSFC} = \\frac{\\dot{m}_c}{\\dot{W}_{\\text{eje}}} \\quad ; \\quad \\eta_{\\text{CHP}} = \\frac{\\dot{W}_e + \\dot{Q}_{\\text{útil}}}{\\dot{m}_c\\cdot\\text{PCI}}"
            ejemplo: " Planta CHP con biogás logrando 38% eléctrico y 44% térmico aprovechable."
            bloque_sugerido: "Práctica 45 min • Cogeneración CHP"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Conversión Electromecánica y Acoplamiento deCampo"
            objetivo: "Relacionar energía de campo magnético con fuerza y par electromagnético."
            concepto_clave_latex: "T_e = \\frac{\\partial W'_{\\text{fld}}(i,\\theta)}{\\partial \\theta} \\quad ; \\quad P_{\\text{em}} = T_e \\omega_m"
            ejemplo: "Conversión de par mecánico a potencia síncrona trifásica."
            bloque_sugerido: "Pomodoro 45/10 • Coenergía magnética"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Conversión Directa: Fotovoltaica y Termoeléctrica (Seebeck)"
            objetivo: "Analizar generación eléctrica de estado sólido sin partes móviles."
            concepto_clave_latex: "V_{\\text{TEG}} = \\alpha_{AB}\\Delta T \\quad ; \\quad ZT = \\frac{\\alpha^2 \\sigma T}{\\kappa} \\quad ; \\quad I = I_L - I_0\\left(e^{qV/nkT}-1\\right)"
            ejemplo: "Recuperación termoeléctrica en ductos de escape y operación de unión p-n."
            bloque_sugerido: "Práctica 45 min • Conversión directa"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Conversión Electroquímica: Celdas Galvánicas y Fuel Cells"
            objetivo: "Contrastar eficiencia máxima de Gibbs frente al límite térmico de Carnot."
            concepto_clave_latex: "\\eta_{\\max,\\text{FC}} = \\frac{\\Delta G}{\\Delta H} = 1 - \\frac{T\\Delta S}{\\Delta H} \\quad ; \\quad V_{\\text{real}} = E_{\\text{Nernst}} - \\eta_{\\text{act}} - \\eta_{\\text{ohm}} - \\eta_{\\text{conc}}"
            ejemplo: "Curva de polarización V-I de una celda PEM alimentada con hidrógeno puro."
            bloque_sugerido: "Pomodoro 50/10 • Polarización electroquímica"
      - codigo: "03041821"
        nombre: "Electricidad y Magnetismo"
        creditos: 4
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Ley de Coulomb y Campo Eléctrico de Distribuciones Continuas"
            objetivo: "Calcular campos vectoriales eléctricos producidos por cargas puntuales y continuas."
            concepto_clave_latex: "\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{\\rho(\\vec{r}')(\\vec{r}-\\vec{r}')}{|\\vec{r}-\\vec{r}'|^3}\\,dV'"
            ejemplo: "Gradiente de campo eléctrico superficial en conductores de alta tensión (efecto corona)."
            bloque_sugerido: "Pomodoro 50/10 • Integrales de campo E"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ley de Gauss en Forma Integral y Diferencial"
            objetivo: "Determinar campos eléctricos con simetría esférica, cilíndrica y planar."
            concepto_clave_latex: "\\oint_S \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{\\text{enc}}}{\\varepsilon_0} \\quad ; \\quad \\nabla\\cdot\\vec{E} = \\frac{\\rho}{\\varepsilon_0}"
            ejemplo: "Campo eléctrico radial dentro del aislamiento XLPE de un cable subterráneo."
            bloque_sugerido: "Pomodoro 50/10 • Superficies gaussianas"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Potencial Eléctrico, Gradiente y Ecuaciones de Poisson/Laplace"
            objetivo: "Obtener el campo eléctrico a partir del potencial escalar y condiciones de frontera."
            concepto_clave_latex: "V_B - V_A = -\\int_A^B \\vec{E}\\cdot d\\vec{l} \\quad ; \\quad \\vec{E} = -\\nabla V \\quad ; \\quad \\nabla^2 V = -\\frac{\\rho}{\\varepsilon}"
            ejemplo: "Distribución equipotencial en cadenas de aisladores de líneas de 220 kV."
            bloque_sugerido: "Práctica 50 min • Potencial y gradiente"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Conductores, Dieléctricos, Capacitancia y Energía Electrostática"
            objetivo: "Calcular capacitancias geométricas, ruptura dieléctrica y densidad de energía."
            concepto_clave_latex: "C = \\frac{Q}{\\Delta V} \\quad ; \\quad C_{\\text{cil}} = \\frac{2\\pi\\varepsilon L}{\\ln(b/a)} \\quad ; \\quad u_E = \\frac{1}{2}\\varepsilon E^2"
            ejemplo: "Capacitancia por kilómetro en cables coaxiales de media tensión."
            bloque_sugerido: "Pomodoro 45/10 • Dieléctricos y energía"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Corriente Estacionaria, Densidad J y Continuidad de Carga"
            objetivo: "Relacionar campo eléctrico interno con densidad de corriente y ley de Ohm puntual."
            concepto_clave_latex: "\\vec{J} = \\sigma\\vec{E} \\quad ; \\quad I = \\int_S \\vec{J}\\cdot d\\vec{A} \\quad ; \\quad \\nabla\\cdot\\vec{J} = -\\frac{\\partial\\rho}{\\partial t}"
            ejemplo: "Resistencia de puesta a tierra hemisférica en subestaciones eléctricas."
            bloque_sugerido: "Práctica 45 min • Mallas de tierra"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Campo Magnético, Fuerza de Lorentz y Ley de Biot-Savart"
            objetivo: "Evaluar fuerzas magnéticas sobre conductores y campos generados por corrientes."
            concepto_clave_latex: "\\vec{F} = q(\\vec{E} + \\vec{v}\\times\\vec{B}) \\quad ; \\quad d\\vec{B} = \\frac{\\mu_0 I}{4\\pi}\\frac{d\\vec{l}\\times\\hat{r}}{r^2}"
            ejemplo: "Esfuerzos electrodinámicos entre barras colectoras durante un cortocircuito."
            bloque_sugerido: "Pomodoro 50/10 • Lorentz y Biot-Savart"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Ley de Ampère, Materiales Magnéticos y Circuitos Magnéticos"
            objetivo: "Resolver núcleos ferromagnéticos con entrehierro aplicando reluctancia e histéresis."
            concepto_clave_latex: "\\oint_C \\vec{H}\\cdot d\\vec{l} = I_{\\text{enc}} \\quad ; \\quad \\mathcal{F} = N I = \\Phi \\mathcal{R} \\quad ; \\quad \\mathcal{R} = \\frac{l}{\\mu A}"
            ejemplo: "Flujo magnético en el núcleo laminado y entrehierro de un reactor o motor."
            bloque_sugerido: "Pomodoro 50/10 • Reluctancia magnética"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Ley de Inducción de Faraday-Lenz e Inductancia"
            objetivo: "Cuantificar FEM inducida por variación de flujo y movimiento de conductores."
            concepto_clave_latex: "\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -\\oint_C \\vec{E}\\cdot d\\vec{l} \\quad ; \\quad L = \\frac{N\\Phi_B}{I} \\quad ; \\quad u_B = \\frac{B^2}{2\\mu}"
            ejemplo: "Principio de generación AC en espiras rotatorias y corrientes parásitas de Foucault."
            bloque_sugerido: "Pomodoro 50/10 • Faraday y FEM motriz"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Ecuaciones de Maxwell, Vector de Poynting y Ondas EM"
            objetivo: "Integrar la corriente de desplazamiento de Maxwell y el flujo de potencia electromagnética."
            concepto_clave_latex: "\\nabla\\times\\vec{H} = \\vec{J} + \\frac{\\partial\\vec{D}}{\\partial t} \\quad ; \\quad \\vec{S} = \\vec{E}\\times\\vec{H}"
            ejemplo: "Transporte de densidad de potencia solar (W/m²) mediante el vector de Poynting."
            bloque_sugerido: "Taller 50 min • Maxwell y Poynting"
      - codigo: "01021805"
        nombre: "General English IV"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "general"
            titulo: "Past Perfect Simple & Continuous: Sequencing Past Events"
            objetivo: "Ordenar cronológicamente antecedentes y causas previas a un evento pasado en reportes de ingeniería."
            concepto_clave_latex: ""
            ejemplo: "By the time we checked the logger, it had already recorded 10,000 data points."
            bloque_sugerido: "Chronology Lab 40 min • Root-cause sequencing in technical incident reports"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Past Perfect Simple & Continuous: Sequencing Past Events: Communicative Purpose"
                puntos:
                  - "Past Perfect Simple (had + V3) marks 'the past before the past' — an action completed BEFORE another past reference point."
                  - "Past Perfect Continuous (had been + V-ing) emphasizes how long an activity had been running before a past event occurred."
                  - "Key triggers: by the time, before, after, already, just, because."
                ejemplo: "By the time we checked the logger, it had already recorded 10,000 data points."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Past Perfect Simple: 'By the time the technician arrived, the breaker had tripped.'"
                  - "Past Perfect Continuous: 'The bearing failed because it had been vibrating for weeks.'"
                  - "Clear chronological chain with 'before/after' can use Past Simple, while 'by the time' strongly prefers Past Perfect."
                tabla:
                  - ["Aspect", "Form", "Diagnostic Meaning"]
                  - ["Past Perfect Simple", "had + V3", "Completed prior event (had overheated)"]
                  - ["Past Perfect Cont.", "had been + V-ing", "Prior duration/cause (had been leaking)"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Negative: 'We hadn't calibrated the zero offset before the first trial.'"
                  - "Question: 'How long had the turbine been operating before the shutdown?'"
                ejemplo: "The battery voltage dropped because the load had been drawing 15 A for three hours."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Don't overuse Past Perfect when events are told in chronological order (A, then B, then C -> Past Simple)."
                  - "Use Past Perfect when looking BACKWARD from event B to earlier cause A!"
                tabla:
                  - ["Sequence", "Tense Choice", "Example"]
                  - ["A -> then B (forward)", "Past Simple + Past Simple", "Pressure rose and the valve opened."]
                  - ["At B, looking back at A", "Past Simple + Past Perfect", "The valve opened because pressure had risen."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "By the time we checked the logger, it had already recorded 10,000 data points."
                  - "The battery voltage dropped because the load had been drawing 15 A for three hours."
                  - "Had you studied Python before you enrolled in Energy Engineering?"
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Combine: 'The grid stabilized. Earlier, operators isolated the fault' (use 'after' or 'because')."
                  - "Choose: 'It was hot because the furnace (ran / had been running) all day' -> 'had been running'."
                  - "Write a 4-sentence root-cause timeline of a past system event."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 2
            corte: 1
            modalidad: "general"
            titulo: "Third Conditional: Regrets, Past Hypotheses & Post-Mortem Analysis"
            objetivo: "Evaluar escenarios pasados contrafactuales y lecciones aprendidas mediante el Tercer Condicional."
            concepto_clave_latex: ""
            ejemplo: "If the operator had noticed the pressure alarm, she would have closed the bypass valve."
            bloque_sugerido: "Post-Mortem Review 40 min • Counterfactual analysis of engineering case studies"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Third Conditional: Regrets, Past Hypotheses & Post-Mortem Analysis: Communicative Purpose"
                puntos:
                  - "Form: If + Past Perfect (had + V3), would / could / might + have + V3."
                  - "Refers 100% to the PAST — imagining how a past outcome would have differed if an earlier condition had changed."
                  - "Essential in engineering post-mortem reviews without assigning personal blame."
                ejemplo: "If the operator had noticed the pressure alarm, she would have closed the bypass valve."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative counterfactual: 'If we had insulated the tank, we would have saved 18% of the heat.'"
                  - "Negative -> Positive flip: 'If the relay hadn't tripped, the motor could have burned out.'"
                  - "Modal nuance: 'would have' (certain result), 'could have' (ability/chance), 'might have' (possibility)."
                tabla:
                  - ["Clause", "Structure", "Example"]
                  - ["Condition (Unreal Past)", "If + had (not) + V3", "If we had checked the polarity,"]
                  - ["Outcome (Unreal Past)", "would/could/might + have + V3", "the fuse wouldn't have blown."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Spoken contraction alert: 'I'd' = 'I had' (before V3) OR 'I would' (before 'have') -> 'If I'd known, I'd have fixed it'."
                  - "Formal inversion (B2 preview): 'Had we used thicker wire, voltage drop would have been negligible.'"
                ejemplo: "The project wouldn't have finished on schedule if the team hadn't automated data cleaning."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "NEVER put 'would have' in the If-clause (*If we would have tested...* -> 'If we had tested...')."
                  - "Never write 'would of' (phonetic spelling error of spoken 'would've' -> ALWAYS write 'would have')!"
                tabla:
                  - ["Spoken Sound", "Wrong Spelling", "Correct Academic Writing"]
                  - ["/ˈwʊdəv/", "would of failed", "would have failed"]
                  - ["If + would have", "If it would have rained", "If it had rained"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "If the operator had noticed the pressure alarm, she would have closed the bypass valve."
                  - "The project wouldn't have finished on schedule if the team hadn't automated data cleaning."
                  - "What could have happened if the grounding cable had been disconnected?"
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Rewrite as 3rd Conditional: 'We didn't clean the panels, so output dropped by 11%.'"
                  - "Fix: 'If you would have saved the file, you wouldn't of lost it.'"
                  - "Write 3 post-mortem lessons from a past exam or lab session."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 3
            corte: 1
            modalidad: "general"
            titulo: "Mixed Conditionals: Past Causes with Present Consequences"
            objetivo: "Conectar decisiones o eventos del pasado con sus efectos actuales mediante condicionales mixtos."
            concepto_clave_latex: ""
            ejemplo: "If we had calibrated the pyranometer this morning, our live readings would be accurate right now."
            bloque_sugerido: "Causal Reasoning 40 min • Linking historical energy choices to today's grid"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Mixed Conditionals: Past Causes with Present Consequences: Communicative Purpose"
                puntos:
                  - "Type A (Most Common — Past Condition -> Present Result): If + Past Perfect (had + V3), would / could + BASE verb (now!)."
                  - "Type B (Permanent Present State -> Past Result): If + Past Simple, would have + V3."
                  - "Signal words like 'now', 'today', 'currently' in the main clause reveal a Mixed Conditional!"
                ejemplo: "If we had calibrated the pyranometer this morning, our live readings would be accurate right now."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Past -> Present: 'If Colombia hadn't invested in hydro power decades ago, grid emissions would be much higher today.'"
                  - "Present -> Past: 'If copper weren't such a good conductor, engineers wouldn't have chosen it for those windings.'"
                  - "Verify the time reference of EACH half independently!"
                tabla:
                  - ["Mixed Pattern", "If-Clause Time", "Main Clause Time & Form"]
                  - ["Past -> Present", "Past (If + had + V3)", "Present (would + base verb now)"]
                  - ["Present -> Past", "General state (If + Past Simple)", "Past (would + have + V3)"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Compare 3rd vs. Mixed: 'If I had taken Programming, I would have passed last year' (3rd: past result) vs. 'If I had taken Programming, I would know Python now' (Mixed: present state!)."
                ejemplo: "If silicon weren't abundant in Earth's crust, solar PV wouldn't have scaled so rapidly."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Watch time markers ('yesterday' vs. 'today') so you don't automatically default to 'would have + V3' when the consequence is happening RIGHT NOW."
                tabla:
                  - ["Time Clue in Result", "Choose Result Form", "Example"]
                  - ["...yesterday / in 2022", "would have + V3 (3rd)", "...costs would have fallen in 2022."]
                  - ["...today / right now", "would + base verb (Mixed)", "...costs would be lower today."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "If we had calibrated the pyranometer this morning, our live readings would be accurate right now."
                  - "If silicon weren't abundant in Earth's crust, solar PV wouldn't have scaled so rapidly."
                  - "I wouldn't be in Semester 4 now if I hadn't passed Calculus I and II."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Build a Mixed Conditional: 'We installed LED lighting last year -> our bill is 35% lower today.'"
                  - "Identify time frames in: 'If she spoke German, she would have applied for the Munich internship.'"
                  - "Write 2 Past->Present mixed conditionals about technology history."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 4
            corte: 2
            modalidad: "general"
            titulo: "Passive Voice II (All Tenses, Modals & Impersonal It is said that...)"
            objetivo: "Dominar construcciones pasivas avanzadas con tiempos continuos, perfectos, verbos modales y estructuras impersonales."
            concepto_clave_latex: ""
            ejemplo: "A new microgrid laboratory is currently being equipped at Unimagdalena."
            bloque_sugerido: "Academic Style Lab 45 min • Impersonal reporting & modal passives in papers"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Passive Voice II (All Tenses, Modals & Impersonal It is said that...): Communicative Purpose"
                puntos:
                  - "Universal Passive Formula: Subject + [any tense/modal of BE] + Past Participle (V3)."
                  - "Continuous Passive: is/are/was/were + BEING + V3 ('Smart meters are being deployed across the coast')."
                  - "Perfect & Modal Passive: has/have/had + BEEN + V3 | must/can/should + BE + V3 ('Hydrogen can be stored in tanks')."
                ejemplo: "A new microgrid laboratory is currently being equipped at Unimagdalena."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Modal Passive in standards: 'All enclosures must be grounded.' / 'Losses can be minimized by...'"
                  - "Impersonal Reporting Pattern 1: 'It is estimated / reported / expected that + clause'."
                  - "Impersonal Reporting Pattern 2: 'Subject + is estimated / known + to V (or to have V3)'!"
                tabla:
                  - ["Active Structure", "Advanced Passive Formula", "Academic Example"]
                  - ["are installing", "are being installed", "New chargers are being installed."]
                  - ["have validated", "has been validated", "The model has been validated."]
                  - ["must verify", "must be verified", "Safety limits must be verified."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Dual impersonal upgrade: 'Experts expect solar costs to fall' -> (1) 'It is expected that solar costs will fall' OR (2) 'Solar costs are expected to fall'."
                  - "For prior actions in Pattern 2, use perfect infinitive: 'The fault is believed to have started in Bus 4.'"
                ejemplo: "Harmonic distortion must be kept below 5% according to IEEE 519."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Don't confuse 'being' (continuous) with 'been' (perfect): 'is being tested' (now) vs. 'has been tested' (already done)!"
                  - "Avoid awkward triple-auxiliary passives like *will have been being tested* -> rewrite cleanly."
                tabla:
                  - ["Impersonal Pattern", "Syntax", "Research Paper Sentence"]
                  - ["It + passive + that", "It is shown that S + V", "It has been shown that tilt affects yield."]
                  - ["S + passive + to-inf", "S is shown to + V", "Tilt angle has been shown to affect yield."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "A new microgrid laboratory is currently being equipped at Unimagdalena."
                  - "Harmonic distortion must be kept below 5% according to IEEE 519."
                  - "Offshore wind capacity is projected to grow substantially by 2035."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Transform: 'People believe that the short circuit started at dawn' (both impersonal ways)."
                  - "Choose: 'The code (is being / has been) compiled right now' -> 'is being'."
                  - "Rewrite 3 active RETIE/IEEE safety rules into Modal Passive."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 5
            corte: 2
            modalidad: "general"
            titulo: "Reported Speech I: Statements & Shifts in Tense/Time"
            objetivo: "Reportar afirmaciones, hallazgos de autores y declaraciones técnicas aplicando backshift y ajustes deícticos."
            concepto_clave_latex: ""
            ejemplo: "The lead engineer reported that the inverter had reached 98.2% peak efficiency."
            bloque_sugerido: "Citation & Reporting 40 min • Summarizing speaker statements accurately"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Reported Speech I: Statements & Shifts in Tense/Time: Communicative Purpose"
                puntos:
                  - "When the reporting verb is in the past (said, stated, reported, explained), shift the original verb ONE step back ('backshift')."
                  - "Backshift chain: Present Simple -> Past Simple; Present Continuous -> Past Continuous; Past Simple / Present Perfect -> Past Perfect; will -> would; can -> could."
                  - "NO backshift needed when reporting timeless scientific truths ('Fourier proved that heat flows from hot to cold')!"
                ejemplo: "The lead engineer reported that the inverter had reached 98.2% peak efficiency."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "'Say' vs. 'Tell': 'say (that)...' (no personal object) vs. 'tell + SOMEONE (that)...' ('She told us that the test passed')."
                  - "Deictic shifts: today -> that day, yesterday -> the day before, tomorrow -> the next/following day, here -> there, this -> that."
                  - "Academic citation often uses Present Reporting ('Çengel states that entropy increases') with zero backshift."
                tabla:
                  - ["Direct Speech", "Reported Speech (Past)", "Example"]
                  - ["Present -> Past", "am/is -> was", "'It is ready' -> He said it was ready."]
                  - ["Pres. Perf. -> Past Perf.", "have tested -> had tested", "'We've tested it' -> They said they had tested it."]
                  - ["Will -> Would", "will rise -> would rise", "'Load will rise' -> She noted load would rise."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "'Must' (obligation) shifts to 'had to'; 'must' (logical deduction) stays 'must'; 'should / might / could / would' stay unchanged!"
                ejemplo: "Professor Martínez told the class that the midterm would cover Chapters 1 to 4."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "NEVER write 'He said me that...' -> either 'He told me that...' OR 'He said (to me) that...'."
                  - "Update pronouns and possessives logically to match the reporter's perspective."
                tabla:
                  - ["Verb Error", "Correction", "Rule"]
                  - ["She said us the results", "She told us the results", "tell + indirect object"]
                  - ["He told that it failed", "He said / stated that it failed", "'tell' requires a listener"]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "The lead engineer reported that the inverter had reached 98.2% peak efficiency."
                  - "Professor Martínez told the class that the midterm would cover Chapters 1 to 4."
                  - "Thermodynamics establishes that energy cannot be created or destroyed."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Report: 'We are calibrating the wind sensor today,' the team said."
                  - "Fix: 'The technician told that the valve was closed' -> 'said that / told us that'."
                  - "Report 3 findings from a scientific lecture."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 6
            corte: 2
            modalidad: "general"
            titulo: "Reported Speech II: Questions, Commands & Requests"
            objetivo: "Reportar preguntas técnicas, instrucciones operativas y solicitudes formales sin inversión interrogativa."
            concepto_clave_latex: ""
            ejemplo: "The reviewer asked whether we had validated the CFD mesh independence."
            bloque_sugerido: "Q&A Reporting 40 min • Turning interview questions & SOPs into formal prose"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Reported Speech II: Questions, Commands & Requests: Communicative Purpose"
                puntos:
                  - "Reported Questions become STATEMENTS: drop 'do/does/did', drop the question mark, and use normal S + V word order!"
                  - "Yes/No Questions use 'if' or 'whether' ('He asked if/whether the grid was stable')."
                  - "Wh- Questions keep the Wh- word + Subject + Verb ('She asked what the cutoff frequency was')."
                ejemplo: "The reviewer asked whether we had validated the CFD mesh independence."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Commands / Instructions: tell / order / instruct + object + (NOT) + TO-infinitive ('The manual warns users not to open the case')."
                  - "Polite Requests: ask + object + (NOT) + TO-infinitive ('She asked me to share the dataset')."
                  - "Reporting verbs with patterns: advise/remind + obj + to V; suggest/recommend + V-ing (or that S + base V)."
                tabla:
                  - ["Direct Utterance", "Reported Structure", "Model Sentence"]
                  - ["'Are the sensors online?'", "asked if/whether + S + V", "He asked whether the sensors were online."]
                  - ["'Where did voltage drop?'", "asked + Wh- + S + V", "She asked where voltage had dropped."]
                  - ["'Do not touch Bus A!'", "warned + obj + not to V", "He warned us not to touch Bus A."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Prefer 'whether' over 'if' in formal academic prose, especially before 'or not' ('We investigated whether humidity affected yield or not')."
                ejemplo: "The lab coordinator reminded students not to leave power supplies switched on."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - " #1 EXAM TRAP: keeping question inversion! NEVER say *He asked where was the lab* -> say 'He asked where the lab was'!"
                  - "Place 'not' BEFORE 'to' in negative commands: 'told us NOT to disconnect', never *to not* in formal tests."
                tabla:
                  - ["Word-Order Trap", "Incorrect", "Correct Statement Order"]
                  - ["Wh- + Be", "She asked what was V_oc.", "She asked what V_oc was."]
                  - ["Auxiliary 'did'", "He asked when did it stop.", "He asked when it had stopped."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "The reviewer asked whether we had validated the CFD mesh independence."
                  - "The lab coordinator reminded students not to leave power supplies switched on."
                  - "A classmate asked how the DownloadQueueService handled twenty concurrent users."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Report: 'How much power does the pump consume?' the auditor asked."
                  - "Report: 'Please upload your slides in PDF format,' the professor told us."
                  - "Fix: 'They asked if did the prototype pass' -> 'They asked whether the prototype had passed.'"
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 7
            corte: 2
            modalidad: "general"
            titulo: "Future Continuous & Future Perfect (By 2030, we will have achieved...)"
            objetivo: "Proyectar metas acumuladas a una fecha límite (Future Perfect) y procesos en curso en el futuro (Future Continuous)."
            concepto_clave_latex: ""
            ejemplo: "By the end of Cuatrimestre 12, you will have completed 162 academic credits."
            bloque_sugerido: "Roadmap Projection 35 min • Writing 2030–2050 Net-Zero milestone statements"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Future Continuous & Future Perfect (By 2030, we will have achieved...): Communicative Purpose"
                puntos:
                  - "Future Continuous (will be + V-ing): an action that will be IN PROGRESS at a specific future moment or part of a natural future trajectory."
                  - "Future Perfect Simple (will have + V3): an action that will be COMPLETED BEFORE a future deadline ('By 2030, ...')."
                  - "Future Perfect Continuous (will have been + V-ing): duration up to a future milestone ('By June, she will have been researching H2 for two years')."
                ejemplo: "By the end of Cuatrimestre 12, you will have completed 162 academic credits."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Signal 'At this time tomorrow / In 2035': Future Continuous ('Grids will be operating with smart inverters')."
                  - "Signal 'By + future date / By the time + Present Simple': Future Perfect ('By Friday, we will have tested all 12 samples')."
                  - "Remember: time clauses after 'by the time' use PRESENT SIMPLE, not 'will'!"
                tabla:
                  - ["Tense", "Formula", "Key Time Marker & Meaning"]
                  - ["Future Continuous", "will be + V-ing", "At 10 a.m. tomorrow (in progress)"]
                  - ["Future Perfect", "will have + V3", "By 2030 / By next month (completed)"]
                  - ["Future Perf. Cont.", "will have been + V-ing", "By May, ...for 3 years (duration)"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Polite non-intrusive inquiry: 'Will you be using the spectrum analyzer this afternoon?' (asking about someone's existing plans)."
                ejemplo: "This time next week, our group will be defending our CDIO project."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Distinguish 'in 2030' (at that year -> will / will be V-ing) vs. 'by 2030' (at or before that deadline -> will have V3)!"
                  - "Never write *by the time you will arrive* -> 'by the time you arrive, the simulation will have finished'."
                tabla:
                  - ["Preposition", "Meaning", "Correct Tense"]
                  - ["BY 2030", "No later than 2030 (cumulative)", "Colombia will have expanded wind farms."]
                  - ["IN 2030", "During the year 2030", "Many plants will be producing green H2."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "By the end of Cuatrimestre 12, you will have completed 162 academic credits."
                  - "This time next week, our group will be defending our CDIO project."
                  - "By 2040, battery storage will have transformed peak-load management worldwide."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete: 'By 5:00 p.m., the solver ___ (converge)' -> 'will have converged'."
                  - "Complete: 'Don't call at 9:00; I ___ (take) my Thermodynamics exam' -> 'will be taking'."
                  - "Write 3 'By 2030 / By graduation...' roadmaps using Future Perfect."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 8
            corte: 3
            modalidad: "general"
            titulo: "Causative Verbs (Have/Get something done, Make, Let, Help)"
            objetivo: "Expresar servicios técnicos delegados (have/get something done) y relaciones de causa, permiso o asistencia."
            concepto_clave_latex: ""
            ejemplo: "The university had fifty solar modules installed on the parking canopy."
            bloque_sugerido: "Maintenance & Control 35 min • Delegated engineering services & causal verbs"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Causative Verbs (Have/Get something done, Make, Let, Help): Communicative Purpose"
                puntos:
                  - "Passive Causative: 'have / get + OBJECT + Past Participle (V3)' means commissioning a specialist/service to perform an action for you ('We had the pyranometer calibrated at IDEAM')."
                  - "Active Causatives: 'make + obj + bare V' (force/cause), 'let + obj + bare V' (allow), 'have + person + bare V' (assign), 'get + person + TO V' (persuade)."
                  - "'Help + obj + (to) V' accepts either bare infinitive or to-infinitive."
                ejemplo: "The university had fifty solar modules installed on the parking canopy."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Have/Get + object + V3 adapts to any tense: 'We get the filters replaced quarterly' / 'They are having the roof reinforced.'"
                  - "Passive of 'make' restores 'to': 'The gas is made TO expand' (vs. active 'Heat makes the gas expand')."
                  - "Formal alternative to 'let': 'allow / permit + object + TO V'."
                tabla:
                  - ["Causative Pattern", "Syntax", "Engineering Meaning"]
                  - ["Service (Passive)", "have/get + thing + V3", "We had the transformer rewound."]
                  - ["Force / Cause", "make + obj + bare V", "Friction makes bearings heat up."]
                  - ["Assign vs. Persuade", "have sb V / get sb TO V", "Have Luis check it / Get him to help."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Watch word order in Passive Causative: 'had + OBJECT + V3' ('We had the inverter repaired') vs. Past Perfect active ('We had repaired the inverter' = we fixed it ourselves!)."
                ejemplo: "Smart thermostats help households reduce cooling electricity bills."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never use bare infinitive after 'get + person': say 'get the vendor TO send the datasheet', NOT *get the vendor send*."
                  - "Don't forget 'to' after 'allow/enable/cause': 'enable the system TO track'."
                tabla:
                  - ["Order Contrast", "Who Did the Work?", "Sentence"]
                  - ["had + V3 + object", "WE did it earlier (Past Perf.)", "We had calibrated the meter before class."]
                  - ["had + object + V3", "A SPECIALIST did it for us", "We had the meter calibrated at the lab."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "The university had fifty solar modules installed on the parking canopy."
                  - "Smart thermostats help households reduce cooling electricity bills."
                  - "A check valve lets fluid flow in one direction and prevents backflow."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Rewrite with causative: 'A certified lab tested our oil samples' -> 'We had our oil samples tested.'"
                  - "Choose: 'High voltage makes current (flow / to flow)' -> 'flow' (active) vs. 'Current is made (to flow)' (passive)."
                  - "Write 3 maintenance sentences using 'have/get something done'."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 9
            corte: 3
            modalidad: "general"
            titulo: "Quantifiers & Determiners (Both, Either, Neither, Each, Every, All)"
            objetivo: "Seleccionar determinantes distributivos y duales con concordancia verbal exacta en textos técnicos."
            concepto_clave_latex: ""
            ejemplo: "Each photovoltaic string is protected by its own DC fuse."
            bloque_sugerido: "Determiner Precision 35 min • Dual vs. plural quantifiers in technical specs"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Quantifiers & Determiners (Both, Either, Neither, Each, Every, All): Communicative Purpose"
                puntos:
                  - "DUAL (exactly 2 items): 'both' (A + B -> plural verb), 'either' (A or B -> singular noun/verb), 'neither' (not A and not B -> singular verb in formal English)."
                  - "DISTRIBUTIVE (2+ or 3+ items): 'each' (individual items, 2 or more -> singular) vs. 'every' (whole group collectively, 3 or more -> singular)."
                  - "TOTALITY: 'all / whole' ('all the data', 'the whole circuit', 'no + noun' = zero)."
                ejemplo: "Each photovoltaic string is protected by its own DC fuse."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Paired correlatives: 'both A and B', 'either A or B', 'neither A nor B' (verb agrees with the CLOSER subject B in formal prose!)."
                  - "With 'of the': 'both (of) the pumps', 'each of the sensors IS...', 'neither of the models CONVERGES' (formal singular)."
                  - "Notice: 'every' CANNOT be followed directly by 'of' -> use 'every one of the cells'!"
                tabla:
                  - ["Determiner", "Set Size", "Noun & Verb Agreement"]
                  - ["both (of the)", "2 items", "Plural noun + Plural verb"]
                  - ["either / neither", "2 items", "Singular noun + Singular verb (+ of plural)"]
                  - ["each / every", "2+ / 3+ items", "Singular noun + Singular verb"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "'None' = 0 out of 3 or more items ('None of the 12 trials failed'), whereas 'neither' = 0 out of 2 items ('Neither of the 2 backups failed')!"
                  - "'All' vs. 'Whole': 'all day / the whole day' (singular countable), 'all electricity' (uncountable — 'whole' doesn't go directly with uncountables)."
                ejemplo: "Neither the primary inverter nor the backup unit was damaged by the surge."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid double negatives with 'neither': say 'Neither sensor worked' OR 'Either sensor didn't work' -> NEVER *Neither sensor didn't work*!"
                  - "Never write *every of the panels* -> write 'each of the panels' or 'every panel'."
                tabla:
                  - ["Count of Items", "100% Affirmative", "0% Negative"]
                  - ["Exactly 2", "Both turbines are online.", "Neither turbine is online."]
                  - ["3 or more", "All (five) turbines are online.", "None of the turbines is/are online."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Each photovoltaic string is protected by its own DC fuse."
                  - "Neither the primary inverter nor the backup unit was damaged by the surge."
                  - "Both designs meet efficiency targets, so either option is acceptable."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Choose (2 batteries): '(Neither / None) of the two batteries was fully charged' -> 'Neither'."
                  - "Fix: 'Every of the equations was verified' -> 'Each of the equations was verified.'"
                  - "Write 3 sentences comparing two prototypes using both, either...or, and neither...nor."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 10
            corte: 3
            modalidad: "general"
            titulo: "Reading Strategies for Academic Abstracts & Technical Articles"
            objetivo: "Extraer con rapidez objetivos, metodología, resultados numéricos y conclusiones de abstracts científicos en inglés."
            concepto_clave_latex: ""
            ejemplo: "This paper investigates the thermal performance of a hybrid PV-thermal collector."
            bloque_sugerido: "IEEE Abstract Lab 45 min • Skimming, scanning & unpacking dense noun phrases"
            slides:
              - numero: 1
                seccion: "CEFR B1.2 • CORE CONCEPT"
                titulo: "Reading Strategies for Academic Abstracts & Technical Articles: Communicative Purpose"
                puntos:
                  - "Every standard engineering abstract mirrors 4–5 micro-moves (~150–250 words): (1) Background/Gap, (2) Objective ('This paper proposes/investigates...'), (3) Methodology ('Using a 3D CFD model...'), (4) Key Quantitative Results ('achieving a 14.2% reduction'), (5) Conclusion/Impact."
                  - "Skimming = reading title, headings, first/last sentences for global gist in 60 seconds."
                  - "Scanning = hunting rapidly for specific numbers, units, equations, acronyms, or benchmarks."
                ejemplo: "This paper investigates the thermal performance of a hybrid PV-thermal collector."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Tense map in abstracts: Background/Gap -> Present Simple / Present Perfect; Objective -> Present Simple ('This study evaluates'); Methods & Specific Results -> Past Simple Passive ('was simulated'); Implications -> Present / Modals ('can accelerate')."
                  - "Gap-signaling words: 'However, little attention has been paid to...', 'remains challenging', 'limited data exist on...'."
                tabla:
                  - ["Abstract Move", "Typical Signal Phrase", "Dominant Tense"]
                  - ["1–2. Gap & Aim", "However,... This study proposes...", "Present Perfect / Present"]
                  - ["3–4. Method & Result", "...was modeled using... reached 94%", "Past Simple (often Passive)"]
                  - ["5. Conclusion", "These findings demonstrate that...", "Present Simple / Modal"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Dense Noun Compounds in English read RIGHT-TO-LEFT: 'a grid-connected solar photovoltaic power plant' -> core noun is 'plant', modified leftward!"
                  - "Track reference words (this, these, such, the former, the latter, respectively) to decode numerical mappings accurately!"
                ejemplo: "Peak efficiencies of 19.4% and 62.0% were achieved for electrical and thermal outputs, respectively."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Pay special attention to 'respectively': 'Peak outputs for Units A and B were 12 kW and 18 kW, respectively' (A = 12 kW, B = 18 kW)."
                  - "Don't translate word-by-word; parse the main verb first, then unpack prepositional phrases."
                tabla:
                  - ["Cohesive Device", "Function", "Technical Example"]
                  - ["the former / the latter", "1st item / 2nd item", "Between PV and wind, the latter runs at night."]
                  - ["respectively", "1-to-1 ordered mapping", "V and I were 48 V and 5 A, respectively."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "This paper investigates the thermal performance of a hybrid PV-thermal collector."
                  - "Peak efficiencies of 19.4% and 62.0% were achieved for electrical and thermal outputs, respectively."
                  - "These results suggest that phase-change materials can mitigate overheating."
                ejemplo: "Academic Register (CEFR B1.2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Unpack the noun phrase: 'high-voltage direct-current transmission line losses'."
                  - "Identify the 5 abstract moves in a sample 150-word IEEE abstract."
                  - "Write a 4-sentence mini-abstract for an Unimagdalena course project."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 11
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Matrices, Determinants & Linear Systems"
            objetivo: "Verbalizar dimensiones matriciales, transpuestas, inversas, determinantes y sistemas lineales Ax = b en inglés."
            concepto_clave_latex: "A \\in \\mathbb{R}^{m \\times n} \\quad ; \\quad A^T A x = A^T b \\quad ; \\quad x = A^{-1}b \\quad ; \\quad \\det(A - \\lambda I) = 0"
            verbalizacion_ingles: "• A ∈ ℝ^(m×n) -> \"A is an m-by-n real matrix\" (read m × n as \"m by n\", rows by columns; a_{ij} is \"entry a sub i j\").\n• A^T -> \"A transpose\"  |  A⁻¹ -> \"A inverse\".\n• det(A - λI) = 0 -> \"the determinant of quantity A minus lambda times the identity matrix I equals zero\" (characteristic equation)."
            ejemplo: "Exposición oral de la matriz de admitancias nodales Y_bus ('an N-by-N complex nodal admittance matrix') en sistemas eléctricos."
            bloque_sugerido: "Matrix Speech 30 min • Dimensions, transposes, inverses & characteristic polynomial"
          - numero_tema: 12
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Vector Calculus Operators (Nabla/Del)"
            objetivo: "Leer con precisión el operador diferencial vectorial Nabla: gradiente, divergencia, rotacional y laplaciano."
            concepto_clave_latex: "\\nabla f \\quad ; \\quad \\nabla \\cdot \\vec{v} = 0 \\quad ; \\quad \\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t} \\quad ; \\quad \\nabla^2 T = \\frac{1}{\\alpha}\\frac{\\partial T}{\\partial t}"
            verbalizacion_ingles: "• ∇f -> \"grad f\", \"the gradient of scalar field f\", or \"del f\".\n• ∇ · v = 0 -> \"the divergence of velocity vector v equals zero\" (or \"del dot v equals zero\", incompressible flow).\n• ∇ × E = -∂B/∂t -> \"the curl of electric field E (or del cross E) equals minus partial B over partial t\".\n• ∇²T -> \"the Laplacian of temperature T\" (or \"del squared T\")."
            ejemplo: "Lectura en inglés de las cuatro ecuaciones diferenciales de Maxwell y de la ecuación de difusión térmica de Fourier."
            bloque_sugerido: "Field Operators 35 min • Verbalizing gradient, divergence, curl & Laplacian"
          - numero_tema: 13
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Thermodynamic Laws & State Properties"
            objetivo: "Verbalizar balances de primera y segunda ley para volúmenes de control, tasas temporales con punto y propiedades específicas."
            concepto_clave_latex: "\\dot{Q}_{\\text{in}} - \\dot{W}_{\\text{net}} = \\frac{dE_{\\text{cv}}}{dt} \\quad ; \\quad h = u + Pv \\quad ; \\quad ds \\ge \\frac{\\delta Q}{T}"
            verbalizacion_ingles: "• Q̇_in - Ẇ_net = dE_cv / dt -> \"Q dot in (rate of heat transfer in) minus W dot net (net power output) equals d E control volume by d t\".\n• h = u + Pv -> \"specific enthalpy lowercase h equals specific internal energy u plus pressure P times specific volume v\" (distinguish capital V \"total volume\" vs. lowercase v \"specific volume\"!).\n• ds ≥ δQ / T -> \"differential entropy d s is greater than or equal to inexact differential delta Q over absolute temperature T\"."
            ejemplo: "Defensa en inglés del balance estacionario de una turbina de vapor adiabática: 'W dot out equals mass flow rate m dot times h one minus h two'."
            bloque_sugerido: "Thermo Seminar 35 min • Control-volume rates (Q-dot, m-dot) & Clausius inequality"
          - numero_tema: 14
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Differential Equations & Laplace Transforms"
            objetivo: "Leer ecuaciones diferenciales ordinarias, transformadas de Laplace y funciones de transferencia en el dominio s."
            concepto_clave_latex: "\\mathcal{L}\\{f(t)\\} = F(s) = \\int_0^\\infty e^{-st}f(t)\\,dt \\quad ; \\quad G(s) = \\frac{Y(s)}{U(s)} = \\frac{K}{\\tau s + 1}"
            verbalizacion_ingles: "• L{f(t)} = F(s) = ∫₀^∞ e^(-st) f(t) dt -> \"the Laplace transform of f of t equals capital F of s, which equals the improper integral from zero to infinity of e to the minus s t times f of t d t\".\n• G(s) = Y(s)/U(s) = K / (τs + 1) -> \"transfer function G of s equals output Y of s over input U of s, equal to steady-state gain K over tau s plus one\"."
            ejemplo: "Presentación del modelo dinámico de primer orden de un sensor térmico o gobernador de velocidad de turbina hidráulica."
            bloque_sugerido: "Control & Laplace 35 min • s-domain transfer functions, poles & time constants"
          - numero_tema: 15
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Fluid Mechanics & Dimensionless Numbers"
            objetivo: "Exponer la ecuación de conservación de Bernoulli y números adimensionales críticos (Reynolds, Nusselt, Prandtl, Mach)."
            concepto_clave_latex: "P + \\frac{1}{2}\\rho v^2 + \\rho gh = \\text{const} \\quad ; \\quad \\text{Re} = \\frac{\\rho v D}{\\mu} \\quad ; \\quad \\Delta h_f = f\\frac{L}{D}\\frac{v^2}{2g}"
            verbalizacion_ingles: "• P + 1/2 ρv² + ρgh = const -> \"static pressure P plus one-half rho v squared (dynamic pressure) plus rho g h (hydrostatic term) is constant along a streamline\".\n• Re = ρvD / μ -> \"the Reynolds number R-e equals fluid density rho times mean velocity v times characteristic diameter D, all over dynamic viscosity mu\".\n• Δh_f = f (L/D) (v² / 2g) -> \"Darcy-Weisbach head loss delta h sub f equals friction factor f times L over D times v squared over two g\"."
            ejemplo: "Clasificación oral de flujo laminar (Re < 2300) frente a flujo turbulento (Re > 4000) en tuberías forzadas hidroeléctricas."
            bloque_sugerido: "Fluids Presentation 35 min • Bernoulli terms, head loss & Reynolds regimes"
          - numero_tema: 16
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "State-Space Representation & Eigenvalue Stability Notation"
            objetivo: "Verbalizar modelos en variables de estado continuos y criterios de estabilidad por autovalores en el semiplano izquierdo."
            concepto_clave_latex: "\\dot{x}(t) = Ax(t) + Bu(t) \\quad ; \\quad y(t) = Cx(t) + Du(t) \\quad ; \\quad \\text{Re}(\\lambda_i) < 0"
            verbalizacion_ingles: "• ẋ(t) = A x(t) + B u(t) -> \"state derivative x dot of t equals state matrix A times state vector x of t plus input matrix B times control vector u of t\".\n• Re(λ_i) < 0 -> \"the real part of every eigenvalue lambda sub i is strictly negative (lies in the open left-half complex plane)\"."
            ejemplo: "Análisis de estabilidad de pequeña señal en inversores conectados a red ('grid-forming vs. grid-following converters')."
            bloque_sugerido: "State-Space Drill 30 min • Eigenvalues, state vectors & stability conditions"
      - codigo: "03021817"
        nombre: "Termodinámica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Conceptos Fundamentales, Sistemas, Estado y Equilibrio"
            objetivo: "Definir sistemas cerrados, volúmenes de control y postulado de estado."
            concepto_clave_latex: "P_{\\text{abs}} = P_{\\text{man}} + P_{\\text{atm}} \\quad ; \\quad v = \\frac{V}{m} = \\frac{1}{\\rho}"
            ejemplo: "Instrumentación de presiones absolutas y de vacío en condensadores de vapor."
            bloque_sugerido: "Pomodoro 45/10 • Estados y propiedades"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Sustancias Puras, Diagramas P-v/T-v y Tablas de Vapor"
            objetivo: "Determinar propiedades termodinámicas en líquido comprimido, mezcla saturada y vapor sobrecalentado."
            concepto_clave_latex: "h = h_f + x\\,h_{fg} \\quad ; \\quad x = \\frac{m_{\\text{vapor}}}{m_{\\text{total}}} \\in [0, 1]"
            ejemplo: "Título de vapor x a la salida de una turbina geotérmica de condensación."
            bloque_sugerido: "Pomodoro 50/10 • Interpolación en tablas"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Primera Ley en Sistemas Cerrados y Trabajo de Frontera"
            objetivo: "Resolver balances energéticos de masa fija con gases ideales y sustancias puras."
            concepto_clave_latex: "Q - W = \\Delta U + \\Delta E_c + \\Delta E_p \\quad ; \\quad W_b = \\int_1^2 P\\,dV"
            ejemplo: "Compresión politrópica de aire en almacenamiento CAES cavernoso."
            bloque_sugerido: "Pomodoro 50/10 • Sistemas cerrados"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Primera Ley en Volúmenes de Control Estacionarios (FEES)"
            objetivo: "Analizar toberas, turbinas, compresores, válvulas de estrangulamiento e intercambiadores."
            concepto_clave_latex: "\\dot{Q}_{\\text{vc}} - \\dot{W}_{\\text{vc}} = \\sum_{\\text{sal}}\\dot{m}\\left(h + \\frac{v^2}{2} + gz\\right) - \\sum_{\\text{ent}}\\dot{m}\\left(h + \\frac{v^2}{2} + gz\\right)"
            ejemplo: "Balance entálpico en turbina de vapor de alta presión y válvula Joule-Thomson."
            bloque_sugerido: "Pomodoro 50/10 • Equipos de flujo estable"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Segunda Ley de la Termodinámica y Ciclo de Carnot"
            objetivo: "Aplicar enunciados de Kelvin-Planck y Clausius a motores térmicos y bombas de calor."
            concepto_clave_latex: "\\eta_{\\text{th},\\max} = 1 - \\frac{T_L}{T_H} \\quad ; \\quad \\text{COP}_{\\text{R},\\max} = \\frac{T_L}{T_H - T_L}"
            ejemplo: "Cota máxima teórica de eficiencia en centrales termosolares de torre central."
            bloque_sugerido: "Práctica 45 min • Límites de Carnot"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Entropía, Relaciones T-ds y Eficiencias Isentrópicas"
            objetivo: "Calcular generación de entropía y eficiencias adiabáticas de turbomáquinas."
            concepto_clave_latex: "T\\,ds = dh - v\\,dP \\quad ; \\quad \\dot{S}_{\\text{gen}} = \\sum\\dot{m}_s s_s - \\sum\\dot{m}_e s_e - \\sum\\frac{\\dot{Q}_k}{T_k} \\ge 0"
            ejemplo: "Cálculo de estado real de descarga de un compresor con η_s = 86%."
            bloque_sugerido: "Pomodoro 50/10 • Diagrama T-s y h-s"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Exergía (Disponibilidad) y Destrucción de Trabajo Útil"
            objetivo: "Identificar los componentes con mayor irreversibilidad mediante el teorema de Gouy-Stodola."
            concepto_clave_latex: "\\psi = (h - h_0) - T_0(s - s_0) + \\frac{v^2}{2} + gz \\quad ; \\quad \\dot{X}_{\\text{dest}} = T_0 \\dot{S}_{\\text{gen}}"
            ejemplo: "Auditoría exergética de una planta térmica identificando irreversibilidad en combustión."
            bloque_sugerido: "Práctica 50 min • Balance de exergía"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Ciclos de Potencia de Gas: Otto, Diesel y Brayton"
            objetivo: "Modelar ciclos de turbinas de gas simples y con regeneración, recalentamiento e interenfriamiento."
            concepto_clave_latex: "\\eta_{\\text{Brayton}} = 1 - \\frac{1}{r_p^{(\\gamma-1)/\\gamma}} \\quad ; \\quad r_p = \\frac{P_2}{P_1}"
            ejemplo: "Optimización de relación de presiones en turbina de gas aeroderivada."
            bloque_sugerido: "Pomodoro 50/10 • Ciclo Brayton"
          - numero_tema: 9
            corte: 3
            modalidad: "tecnica"
            titulo: "Ciclo Rankine de Vapor, Recalentamiento y Refrigeración"
            objetivo: "Evaluar mejoras del ciclo Rankine regenerativo y ciclos inversos por compresión de vapor."
            concepto_clave_latex: "\\eta_{\\text{Rankine}} = \\frac{w_{\\text{turb}} - w_{\\text{bomba}}}{q_{\\text{caldera}}} \\quad ; \\quad \\text{COP}_{\\text{R}} = \\frac{h_1 - h_4}{h_2 - h_1}"
            ejemplo: "Dimensionamiento termodinámico de chiller industrial y planta Rankine con sangrías."
            bloque_sugerido: "Taller 50 min • Rankine y refrigeración"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Hidrología Aplicada, Cuencas y Curva de Duración de Caudales"
            objetivo: "Estimar oferta hídrica aprovechable a partir de series históricas de caudales medios."
            concepto_clave_latex: "Q = C \\cdot I \\cdot A \\quad ; \\quad P(Q \\ge Q_p) = \\frac{m}{N + 1}\\times 100\\%"
            ejemplo: "Construcción de la curva de duración de caudales (CDC) de un río de la Sierra Nevada."
            bloque_sugerido: "Pomodoro 45/10 • Curva CDC"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Potencial Hidroenergético, Salto Bruto y Salto Neto"
            objetivo: "Calcular potencia hidráulica disponible descontando pérdidas continuas y singulares."
            concepto_clave_latex: "H_n = H_b - \\Delta h_{\\text{total}} \\quad ; \\quad P_e = \\eta_t \\eta_g \\rho g Q H_n"
            ejemplo: "Potencia eléctrica firme (Q95) y media de una pequeña central hidroeléctrica (PCH)."
            bloque_sugerido: "Pomodoro 50/10 • Salto neto y potencia"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Obras Civiles: Bocatoma, Desarenador, Canal y Tubería Forzada"
            objetivo: "Dimensionar velocidad económica, espesor de tubería de presión y golpe de ariete."
            concepto_clave_latex: "e = \\frac{P_{\\max} D}{2\\sigma_{\\text{adm}}\\eta_s} + c_{\\text{corr}} \\quad ; \\quad \\Delta H_{\\text{Joukowsky}} = \\frac{a\\,\\Delta v}{g}"
            ejemplo: "Sobrepresión por cierre rápido de distribuidor y requerimiento de chimenea de equilibrio."
            bloque_sugerido: "Práctica 50 min • Tubería forzada y ariete"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Ecuación de Euler de Turbomáquinas y Velocidad Específica"
            objetivo: "Seleccionar la tecnología óptima de turbina mediante triángulos de velocidades y N_s."
            concepto_clave_latex: "W_u = u_1 c_{u1} - u_2 c_{u2} \\quad ; \\quad N_s = \\frac{N\\sqrt{P_{\\text{kW}}}}{H_n^{5/4}}"
            ejemplo: "Clasificación del rodete óptimo (Pelton, Francis o Kaplan) según salto y caudal."
            bloque_sugerido: "Pomodoro 50/10 • Ecuación de Euler"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Turbinas de Acción: Pelton y Turgo / Michell-Banki"
            objetivo: "Diseñar chorros, número de cangilones y relación de velocidad periférica en turbinas de acción."
            concepto_clave_latex: "v_1 = C_v\\sqrt{2gH_n} \\quad ; \\quad u_{\\text{ópt}} \\approx 0.46\\,v_1 \\quad ; \\quad d_{\\text{chorro}} = \\sqrt{\\frac{4Q}{z\\pi v_1}}"
            ejemplo: "Dimensionamiento de turbina Pelton de dos inyectores para salto neto de 280 m."
            bloque_sugerido: "Práctica 45 min • Diseño Pelton"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Turbinas de Reacción: Francis, Kaplan y Bulbo"
            objetivo: "Analizar grado de reacción, tubo de aspiración (draft tube) y curvas colina."
            concepto_clave_latex: "\\eta_h = \\frac{u_1 c_{u1} - u_2 c_{u2}}{gH_n} \\quad ; \\quad \\Delta h_{\\text{dif}} = \\frac{v_2^2 - v_3^2}{2g}"
            ejemplo: "Operación de turbina Kaplan de doble regulación ante variaciones estacionales de caudal."
            bloque_sugerido: "Pomodoro 45/10 • Francis y Kaplan"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Cavitación, NPSH y Altura Máxima de Succión"
            objetivo: "Prevenir erosión por cavitación verificando el coeficiente de Thoma σ y cota de instalación."
            concepto_clave_latex: "z_s \\le \\frac{P_{\\text{atm}} - P_v}{\\rho g} - \\sigma_{\\text{Thoma}}H_n - h_{f,s}"
            ejemplo: "Determinación de la sumersión requerida respecto al nivel aguas abajo en una central Francis."
            bloque_sugerido: "Práctica 45 min • Cálculo de Thoma"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Centrales de Bombeo (PHS), Regulación y Viabilidad"
            objetivo: "Evaluar almacenamiento hidráulico reversible, regulación primaria de frecuencia y LCOE."
            concepto_clave_latex: "\\eta_{\\text{ciclo PHS}} = \\eta_{\\text{bombeo}}\\cdot\\eta_{\\text{turbinado}} \\approx 0.75\\text{--}0.82"
            ejemplo: "Integración de bombeo hidroeléctrico reversible para respaldar parques solares y eólicos."
            bloque_sugerido: "Taller 45 min • Bombeo reversible PHS"
      - codigo: "06021846"
        nombre: "Energía Solar Fotovoltaica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Geometría Solar, Radiación Extraterrestre y Masa de Aire"
            objetivo: "Calcular declinación, ángulo horario, altura solar e irradiancia sobre plano inclinado."
            concepto_clave_latex: "\\delta = 23.45^\\circ\\sin\\left[\\frac{360}{365}(284+n)\\right] \\quad ; \\quad \\text{AM} \\approx \\frac{1}{\\cos\\theta_z}"
            ejemplo: "Optimización de inclinación anual (β ≈ latitud = 11.2°) en Santa Marta."
            bloque_sugerido: "Pomodoro 50/10 • Geometría solar"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Física Fotovoltaica y Modelo Equivalente de Un Diodo"
            objetivo: "Modelar la característica I-V y P-V con resistencias serie R_s y paralelo R_sh."
            concepto_clave_latex: "I = I_{\\text{ph}} - I_0\\left[\\exp\\left(\\frac{q(V + IR_s)}{n k_B T_c}\\right) - 1\\right] - \\frac{V + IR_s}{R_{\\text{sh}}}"
            ejemplo: "Simulación de curvas I-V bajo distinta irradiancia G y temperatura de celda."
            bloque_sugerido: "Pomodoro 50/10 • Ecuación del diodo"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Tecnologías de Celdas (PERC, TOPCon, HJT, Bifacial) y Temperatura"
            objetivo: "Estimar pérdidas térmicas mediante NOCT y ganancia bifacial según albedo."
            concepto_clave_latex: "T_c = T_a + \\frac{\\text{NOCT} - 20}{800}\\,G \\quad ; \\quad P_{\\text{mp}}(T_c) = P_{\\text{STC}}\\frac{G}{1000}[1 + \\gamma(T_c - 25)]"
            ejemplo: "Pérdida de potencia al mediodía en el Caribe cuando T_c alcanza 60 °C."
            bloque_sugerido: "Práctica 45 min • Derating térmico"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Sombreado Parcial, Diodos Bypass y Algoritmos MPPT"
            objetivo: "Analizar múltiples picos locales de potencia y algoritmos Perturb & Observe / Conductancia."
            concepto_clave_latex: "\\frac{dP}{dV} = I + V\\frac{dI}{dV} = 0 \\iff \\frac{dI}{dV} = -\\frac{I}{V}"
            ejemplo: "Operación de diodos de paso ante sombras parciales en arreglos comerciales."
            bloque_sugerido: "Pomodoro 45/10 • Seguimiento MPPT"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Configuración Serie-Paralelo de Strings y Ventana del Inversor"
            objetivo: "Dimensionar número máximo y mínimo de módulos por cadena según límites térmicos V_oc y MPPT."
            concepto_clave_latex: "N_{\\max} \\le \\left\\lfloor\\frac{V_{\\max,\\text{inv}}}{V_{\\text{oc}}(T_{\\min})}\\right\\rfloor \\quad ; \\quad r_{\\text{DC/AC}} = \\frac{P_{\\text{PV,pico}}}{P_{\\text{AC,inv}}}"
            ejemplo: "Arreglo de 100 kWp con módulos de 580 Wp e inversor trifásico de 80 kW."
            bloque_sugerido: "Pomodoro 50/10 • Diseño de strings"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas On-Grid, Off-Grid e Híbridos con Almacenamiento"
            objetivo: "Dimensionar generador solar y banco de baterías mediante horas solares pico (HSP)."
            concepto_clave_latex: "E_{\\text{PV}} = P_{\\text{pico}}\\cdot \\text{HSP}\\cdot PR \\quad ; \\quad C_{\\text{bat}} = \\frac{E_{\\text{día}}\\cdot D_{\\text{aut}}}{V_{\\text{sis}}\\cdot \\text{DoD}\\cdot \\eta_b}"
            ejemplo: "Sistema híbrido autónomo con 2 días de autonomía para escuela rural."
            bloque_sugerido: "Práctica 50 min • Dimensionamiento HSP"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Protecciones DC/AC, Puesta a Tierra y Cumplimiento RETIE"
            objetivo: "Seleccionar fusibles gPV, DPS Tipo I/II, interruptores y calibre por ampacidad y caída < 3%."
            concepto_clave_latex: "I_{\\text{fus}} \\ge 1.56\\,I_{\\text{sc}} \\quad ; \\quad \\%e = \\frac{2\\rho L I}{A V_{\\text{mp}}}\\times 100\\% \\le 1.5\\%"
            ejemplo: "Esquema unifilar de protecciones DC/AC conforme a NTC 2050 Sección 690 y RETIE."
            bloque_sugerido: "Taller 50 min • Protecciones gPV"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Performance Ratio (PR), PVsyst y Viabilidad CREG 174"
            objetivo: "Evaluar el índice de rendimiento anual y la exportación de excedentes de autogeneración."
            concepto_clave_latex: "PR = \\frac{Y_f}{Y_r} = \\frac{E_{\\text{AC}}/P_0}{H_{\\text{POA}}/G_{\\text{STC}}}"
            ejemplo: "Análisis de pérdidas detalladas y flujo de caja de autogenerador AGPE en Colombia."
            bloque_sugerido: "Laboratorio 50 min • Reporte PR y LCOE"
      - codigo: "06011838"
        nombre: "Mediciones e Instrumentación"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Características Estáticas y Dinámicas de Instrumentos"
            objetivo: "Evaluar exactitud, precisión, sensibilidad, histéresis, resolución y respuesta temporal."
            concepto_clave_latex: "G(s) = \\frac{K}{\\tau s + 1} \\quad ; \\quad e_{\\text{din}}(\\omega) = \\frac{1}{\\sqrt{1 + (\\omega\\tau)^2}}"
            ejemplo: "Retardo térmico de una termocupla envainada frente a cambios bruscos de vapor."
            bloque_sugerido: "Pomodoro 45/10 • Metrología estática/dinámica"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Incertidumbre de Medición (Guía GUM) y Calibración"
            objetivo: "Combinar incertidumbres Tipo A y Tipo B con factor de cobertura k para trazabilidad."
            concepto_clave_latex: "u_c^2(y) = \\sum_{i=1}^{N}\\left(\\frac{\\partial f}{\\partial x_i}\\right)^2 u^2(x_i) \\quad ; \\quad U = k\\,u_c(y)"
            ejemplo: "Presupuesto de incertidumbre GUM en ensayo de eficiencia de motor eléctrico."
            bloque_sugerido: "Pomodoro 50/10 • Propagación GUM"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Sensores de Temperatura, Presión, Nivel y Caudal"
            objetivo: "Seleccionar RTD Pt100, termopares, transmisores piezoeléctricos, Coriolis y ultrasónicos."
            concepto_clave_latex: "R(T) = R_0(1 + AT + BT^2) \\quad ; \\quad Q = C_d A_t\\sqrt{\\frac{2\\Delta P}{\\rho(1-\\beta^4)}}"
            ejemplo: "Medición de caudal másico de gas natural y temperatura de sobrecalentamiento."
            bloque_sugerido: "Práctica 45 min • Sensores de proceso"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Instrumentación Eléctrica y Analizadores de Redes (CT/PT)"
            objetivo: "Medir potencia, armónicos, flicker y energía activa/reactiva mediante TC, TP y Rogowski."
            concepto_clave_latex: "P = \\frac{1}{N}\\sum_{k=0}^{N-1} v[k]\\,i[k] \\quad ; \\quad \\text{Clase } 0.2\\text{S IEC 61869}"
            ejemplo: "Instalación de analizador de calidad de energía Clase A (IEC 61000-4-30) en subestación."
            bloque_sugerido: "Pomodoro 45/10 • Transformadores TC/TP"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Acondicionamiento de Señal, Puentes y Amplificadores"
            objetivo: "Diseñar etapas de amplificación de instrumentación, lazos 4–20 mA y filtrado antialiasing."
            concepto_clave_latex: "V_{\\text{out}} = \\left(1 + \\frac{2R_1}{R_G}\\right)\\frac{R_3}{R_2}(V_+ - V_-) \\quad ; \\quad I_{\\text{lazo}} = 4 + 16\\frac{x - x_{\\min}}{x_{\\max}-x_{\\min}}\\text{ mA}"
            ejemplo: "Transmisión inmune a ruido por corriente 4–20 mA desde un pirómetro solar."
            bloque_sugerido: "Laboratorio 50 min • Acondicionamiento 4-20 mA"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Adquisición Digital de Datos (DAQ), Muestreo y Nyquist"
            objetivo: "Configurar frecuencia de muestreo y resolución en bits evitando aliasing espectral."
            concepto_clave_latex: "f_s > 2 f_{\\max} \\quad ; \\quad Q_{\\text{LSB}} = \\frac{V_{\\text{FS}}}{2^N} \\quad ; \\quad \\text{SNR}_{\\text{dB}} \\approx 6.02N + 1.76"
            ejemplo: "Digitalización a 16 bits y 10 kS/s para capturar hasta el armónico 50 de 60 Hz."
            bloque_sugerido: "Pomodoro 45/10 • ADC y Nyquist"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Comunicaciones Industriales, Modbus, IEC 61850 e IoT"
            objetivo: "Integrar medidores inteligentes y RTUs mediante protocolos industriales y telemetría."
            concepto_clave_latex: "T_{\\text{trama}} = \\frac{N_{\\text{bits}}}{R_{\\text{baud}}} \\quad ; \\quad T_{\\text{latencia}} \\le 4\\text{ ms}"
            ejemplo: "Lectura de registros Modbus TCP de un inversor solar hacia dashboard SCADA."
            bloque_sugerido: "Laboratorio 50 min • Tramas Modbus/MQTT"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Sistemas SCADA, Lazos PID Básicos y Seguridad Funcional"
            objetivo: "Estructurar diagramas P&ID ISA-5.1 y supervisión de plantas de generación."
            concepto_clave_latex: "u(t) = K_p e(t) + K_i\\int_0^t e(\\tau)\\,d\\tau + K_d\\frac{de}{dt}"
            ejemplo: "Diagramación ISA-5.1 del lazo de control de nivel de domo en una caldera."
            bloque_sugerido: "Taller 45 min • Simbología ISA P&ID"
      - codigo: "04021825"
        nombre: "Modelación Matemática para Ingeniería"
        creditos: 3
        obligatoria: true
        categoria: "MATEMATICAS"
        color: "#5E5CE6"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Formulación de Modelos Físicos y Leyes de Conservación"
            objetivo: "Traducir fenómenos térmicos, fluidos y eléctricos en ecuaciones diferenciales acopladas."
            concepto_clave_latex: "\\frac{d\\Phi}{dt} = \\dot{\\Phi}_{\\text{ent}} - \\dot{\\Phi}_{\\text{sal}} + \\dot{\\Phi}_{\\text{gen}}"
            ejemplo: "Modelo dinámico térmico RC de una edificación bioclimática."
            bloque_sugerido: "Pomodoro 50/10 • Balances dinámicos"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ecuaciones Diferenciales Ordinarias de Primer Orden"
            objetivo: "Resolver EDOs separables, lineales y de Bernoulli con valores iniciales."
            concepto_clave_latex: "\\frac{dy}{dt} + P(t)y = Q(t) \\implies y(t) = \\frac{1}{\\mu(t)}\\left[\\int \\mu(t)Q(t)\\,dt + C\\right]"
            ejemplo: "Evolución transitoria de concentración de contaminantes o temperatura de tanque."
            bloque_sugerido: "Pomodoro 50/10 • Factor integrante"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "EDOs Lineales de Orden Superior y Oscilaciones Forzadas"
            objetivo: "Analizar respuestas subamortiguadas, críticas y sobreamortiguadas ante excitación externa."
            concepto_clave_latex: "m\\ddot{x} + c\\dot{x} + kx = F_0\\cos(\\omega t) \\quad ; \\quad \\zeta = \\frac{c}{2\\sqrt{mk}}"
            ejemplo: "Ecuación de oscilación rotor-red (swing equation) de un generador síncrono."
            bloque_sugerido: "Pomodoro 50/10 • Sistemas de 2° orden"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Transformada de Laplace y Funciones de Transferencia"
            objetivo: "Resolver problemas de valor inicial con entradas escalón, rampa e impulso de Dirac."
            concepto_clave_latex: "\\mathcal{L}\\{y''\\} = s^2 Y(s) - sy(0) - y'(0) \\quad ; \\quad Y(s) = G(s)U(s)"
            ejemplo: "Respuesta ante escalón de carga del regulador de velocidad de una turbina."
            bloque_sugerido: "Pomodoro 50/10 • Laplace y convolución"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas Acoplados de EDOs y Exponencial Matricial"
            objetivo: "Modelar redes multicompartimentales en espacio de estados y retratos de fase."
            concepto_clave_latex: "\\dot{\\vec{x}} = A\\vec{x} + B\\vec{u} \\quad ; \\quad \\vec{x}(t) = e^{At}\\vec{x}(0) + \\int_0^t e^{A(t-\\tau)}B\\vec{u}(\\tau)\\,d\\tau"
            ejemplo: "Dinámica térmica acoplada núcleo-aceite-ambiente en transformadores de potencia."
            bloque_sugerido: "Práctica 50 min • Sistemas en espacio de estado"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Métodos Numéricos para EDOs: Runge-Kutta y Sistemas Rígidos"
            objetivo: "Integrar numéricamente sistemas diferenciales no lineales controlando error de truncamiento."
            concepto_clave_latex: "y_{n+1} = y_n + \\frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4) \\quad ; \\quad e_{\\text{global}} = \\mathcal{O}(h^4)"
            ejemplo: "Simulación RK4 de un convertidor electrónico con saturación magnética."
            bloque_sugerido: "Laboratorio 50 min • RK4 en Python"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Series de Fourier y Ecuaciones en Derivadas Parciales (EDP)"
            objetivo: "Resolver la ecuación de difusión de calor 1D mediante separación de variables."
            concepto_clave_latex: "\\frac{\\partial T}{\\partial t} = \\alpha\\frac{\\partial^2 T}{\\partial x^2} \\quad ; \\quad T(x,t) = \\sum_{n=1}^{\\infty} B_n\\sin\\left(\\frac{n\\pi x}{L}\\right)e^{-\\alpha(n\\pi/L)^2 t}"
            ejemplo: "Penetración transitoria del pulso térmico solar en un muro acumulador."
            bloque_sugerido: "Pomodoro 50/10 • EDP de calor y Fourier"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Diferencias Finitas y Optimización Matemática Aplicada"
            objetivo: "Discretizar dominios espaciales y formular problemas con multiplicadores de Lagrange."
            concepto_clave_latex: "\\frac{T_i^{k+1}-T_i^k}{\\Delta t} = \\alpha\\frac{T_{i+1}^k - 2T_i^k + T_{i-1}^k}{\\Delta x^2} \\quad ; \\quad \\nabla f = \\lambda\\nabla g"
            ejemplo: "Despacho económico clásico de generadores térmicos por multiplicadores de Lagrange."
            bloque_sugerido: "Taller 50 min • Diferencias finitas y Lagrange"
      - codigo: "06011839"
        nombre: "Sistemas Energéticos"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Arquitectura de Sistemas Energéticos Integrados y Multi-Vector"
            objetivo: "Analizar acoplamiento entre redes eléctricas, térmicas, de gas y transporte."
            concepto_clave_latex: "\\vec{L} = \\mathbf{C}_{\\text{hub}}\\vec{P}_{\\text{in}} \\quad ; \\quad \\sum_{j} c_{ij} \\le 1"
            ejemplo: "Modelado tipo Energy Hub de un campus universitario con PV, red, gas y chillers."
            bloque_sugerido: "Pomodoro 45/10 • Concepto Energy Hub"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Caracterización de la Demanda: Curvas de Carga y Factores"
            objetivo: "Evaluar factor de demanda, diversidad, coincidencia y carga base/pico."
            concepto_clave_latex: "FD = \\frac{D_{\\max}}{P_{\\text{inst}}} \\quad ; \\quad F_{\\text{div}} = \\frac{\\sum D_{\\max,i}}{D_{\\max,\\text{sis}}} \\ge 1"
            ejemplo: "Construcción de la curva monótona de duración de carga anual de 8760 h."
            bloque_sugerido: "Pomodoro 45/10 • Curva monótona"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Cogeneración (CHP) y Trigeneración (CCHP)"
            objetivo: "Dimensionar sistemas combinados de calor, electricidad y frío por absorción."
            concepto_clave_latex: "\\text{PES} = 1 - \\frac{1}{\\frac{\\eta_{e,\\text{CHP}}}{\\eta_{e,\\text{ref}}} + \\frac{\\eta_{q,\\text{CHP}}}{\\eta_{q,\\text{ref}}}} \\times 100\\%"
            ejemplo: "Ahorro de energía primaria (PES) en hospital con microturbina y chiller LiBr-H2O."
            bloque_sugerido: "Práctica 50 min • Índices CHP/PES"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Redes Térmicas de Distrito (District Cooling & Heating)"
            objetivo: "Analizar distribución centralizada de agua helada o vapor para climatización urbana."
            concepto_clave_latex: "\\dot{Q}_{\\text{red}} = \\dot{m} c_p (T_{\\text{ret}} - T_{\\text{sum}}) \\quad ; \\quad \\text{COP}_{\\text{planta}} = \\frac{\\dot{Q}_{\\text{frío}}}{\\sum P_{\\text{eléc}}}"
            ejemplo: "Distrito térmico de enfriamiento para edificios comerciales en clima cálido costero."
            bloque_sugerido: "Pomodoro 45/10 • District Cooling"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Integración de Procesos e Introducción a Tecnología Pinch"
            objetivo: "Minimizar requerimientos externos de calentamiento y enfriamiento mediante curvas compuestas."
            concepto_clave_latex: "\\Delta T \\ge \\Delta T_{\\min} \\quad ; \\quad \\dot{Q}_{\\text{pinch}} = 0"
            ejemplo: "Recuperación cruzada de calor entre efluentes calientes y agua de alimentación."
            bloque_sugerido: "Pomodoro 50/10 • Análisis Pinch"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Despacho Económico y Compromiso de Unidades (Unit Commitment)"
            objetivo: "Optimizar la asignación horaria de recursos minimizando costos operativos y emisiones."
            concepto_clave_latex: "\\min \\sum_{i=1}^{N} C_i(P_i) \\;\\;\\text{s.t.}\\;\\; \\sum_{i=1}^{N} P_i = P_D + P_L,\\;\\; P_{i,\\min}\\le P_i \\le P_{i,\\max}"
            ejemplo: "Igualdad de costos incrementales λ entre tres plantas generadoras."
            bloque_sugerido: "Práctica 50 min • Despacho económico"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Confiabilidad Energética: Índices LOLP, EENS, SAIDI y SAIFI"
            objetivo: "Cuantificar adecuación de generación y continuidad del suministro eléctrico."
            concepto_clave_latex: "\\text{SAIDI} = \\frac{\\sum U_i N_i}{N_T} \\quad ; \\quad \\text{SAIFI} = \\frac{\\sum \\lambda_i N_i}{N_T}"
            ejemplo: "Cálculo de energía esperada no suministrada (EENS) y métricas regulatorias CREG."
            bloque_sugerido: "Pomodoro 45/10 • Índices SAIDI/SAIFI"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Análisis de Ciclo de Vida (ACV) y Retorno Energético (EROI)"
            objetivo: "Evaluar impactos cuna-a-tumba ISO 14040 y tasa de retorno energético."
            concepto_clave_latex: "\\text{EROI} = \\frac{E_{\\text{out,net}}}{E_{\\text{in,inv}}} \\quad ; \\quad \\text{EPBT} = \\frac{E_{\\text{emb}}}{E_{\\text{evitada}}}"
            ejemplo: "Tiempo de retorno energético (EPBT ~ 1.1 años) de un parque solar moderno."
            bloque_sugerido: "Taller 45 min • ACV y EROI"
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
          - numero_tema: 1
            corte: 1
            modalidad: "general"
            titulo: "Inversion with Negative Adverbials (Not only... but also, Rarely, Seldom)"
            objetivo: "Aplicar inversión sujeto-auxiliar tras adverbios negativos y restrictivos para lograr énfasis retórico de nivel B2/C1."
            concepto_clave_latex: ""
            ejemplo: "Not only does cogeneration generate electricity, but it also recovers useful process heat."
            bloque_sugerido: "Rhetorical Emphasis 40 min • C1/B2 inversion in keynote openings & papers"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Inversion with Negative Adverbials (Not only... but also, Rarely, Seldom): Communicative Purpose"
                puntos:
                  - "When a negative or restrictive adverbial opens a sentence for rhetorical emphasis, INVERT the auxiliary and subject (just like a question!)."
                  - "Core triggers: Not only... but (also)..., Rarely, Seldom, Never (before), Little, Under no circumstances, Hardly... when, No sooner... than."
                  - "If no auxiliary is visible (Present/Past Simple), insert DO / DOES / DID + base verb!"
                ejemplo: "Not only does cogeneration generate electricity, but it also recovers useful process heat."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Not only: 'Not only DOES solar PV cut emissions, but it also lowers peak tariffs.'"
                  - "Rarely / Seldom: 'Rarely HAVE battery costs fallen so rapidly.'"
                  - "Only after / Only by + X (invert the MAIN clause!): 'Only by insulating the core CAN we prevent losses.'"
                tabla:
                  - ["Fronted Adverbial", "Inverted Pattern", "High-Impact Academic Example"]
                  - ["Not only...", "Not only + aux + S + V", "Not only did yield rise, but noise fell."]
                  - ["Rarely / Seldom", "Rarely + aux + S + V", "Seldom does efficiency exceed 60%."]
                  - ["Under no circumstances", "Under no... + modal + S + V", "Under no circumstances must fuses be bypassed."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Pairs to memorize: 'Hardly / Scarcely had S + V3 WHEN...' vs. 'No sooner had S + V3 THAN...' ('No sooner had the fault occurred than the relay isolated it')."
                ejemplo: "Seldom do real thermodynamic cycles approach the theoretical Carnot limit."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Watch 'Only when / Not until': do NOT invert the subordinate clause itself — invert the MAIN clause that follows! ('Not until voltage stabilized DID we connect the load')."
                tabla:
                  - ["Trigger Type", "Where Inversion Happens", "Correct Sentence"]
                  - ["Immediate (Never/Rarely)", "Right after adverb", "Never have we observed zero lag."]
                  - ["Delayed (Only when + S+V)", "In the 2nd (main) clause", "Only when T drops DO fans stop."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Not only does cogeneration generate electricity, but it also recovers useful process heat."
                  - "Seldom do real thermodynamic cycles approach the theoretical Carnot limit."
                  - "Only through rigorous grid modeling can high renewable penetration remain stable."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Invert: 'We have never recorded such high irradiance' -> 'Never have we recorded...'"
                  - "Invert: 'The solver converged only after reducing the step size' -> 'Only after reducing the step size did the solver converge.'"
                  - "Write 3 persuasive pitch openings using Not only, Rarely, and Under no circumstances."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 2
            corte: 1
            modalidad: "general"
            titulo: "Cleft Sentences for Emphasis (What we need is..., It was X that...)"
            objetivo: "Reestructurar oraciones mediante It-clefts y Wh-clefts para focalizar hallazgos, causas o soluciones técnicas."
            concepto_clave_latex: ""
            ejemplo: "What distinguishes green hydrogen from gray hydrogen is zero-carbon electrolysis."
            bloque_sugerido: "Pitch Focus Drill 35 min • Highlighting key findings with It- & Wh-clefts"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Cleft Sentences for Emphasis (What we need is..., It was X that...): Communicative Purpose"
                puntos:
                  - "Cleft ('split') sentences divide a single message into two clauses so the spotlight lands squarely on new or contrasting information."
                  - "It-Cleft: 'It is / was + [FOCUSED ELEMENT] + that / who + rest of clause.'"
                  - "Pseudo-Cleft (Wh-Cleft): 'What + S + V + is / was + [FOCUSED ELEMENT / (to) V].'"
                ejemplo: "What distinguishes green hydrogen from gray hydrogen is zero-carbon electrolysis."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Focusing a cause (It-cleft): 'It was harmonic distortion that triggered the inverter trip (not overvoltage).'"
                  - "Focusing an action/need (What-cleft): 'What stabilizes the microgrid is fast battery frequency response.'"
                  - "Noun-head clefts: 'The reason why...', 'The parameter that matters most is...'."
                tabla:
                  - ["Cleft Type", "Blueprint", "Focused Engineering Sentence"]
                  - ["It-cleft", "It is/was + X + that...", "It was in 2021 that Law 2099 took effect."]
                  - ["What-cleft (Noun)", "What + S + V + is + X", "What limits range is energy density."]
                  - ["What-cleft (Verb)", "What + S + do + is (to) V", "What MPPT does is track peak power."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Agreement note: 'It is/was' stays singular even if X is plural ('It is transmission bottlenecks that delay projects')."
                  - "'All (that) S + V + is...' emphasizes simplicity: 'All the operator needs to do is press Reset.'"
                ejemplo: "It was the sudden reactive power imbalance that caused the voltage sag."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Do not use 'what' right after a noun (*The factor what limits...* -> 'The factor that limits...' OR 'What limits yield is...')."
                  - "Use clefts selectively (1–2 per section/slide) for maximum rhetorical contrast!"
                tabla:
                  - ["Neutral Sentence", "Focused Element", "Cleft Transformation"]
                  - ["Fouling reduced heat transfer.", "Fouling (the cause)", "It was fouling that reduced heat transfer."]
                  - ["We need grid-scale storage.", "Grid-scale storage", "What we need is grid-scale storage."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "What distinguishes green hydrogen from gray hydrogen is zero-carbon electrolysis."
                  - "It was the sudden reactive power imbalance that caused the voltage sag."
                  - "What our CDIO prototype demonstrates is low-cost solar desalination for coastal towns."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Focus 'thermal resistance' using an It-cleft: 'Thermal resistance governs heat flux.'"
                  - "Rewrite with 'What...': 'Smart inverters provide reactive voltage support.'"
                  - "Craft 3 punchy presentation takeaways using cleft structures."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 3
            corte: 1
            modalidad: "general"
            titulo: "Participle Clauses (-ing and -ed clauses for Concise Academic Writing)"
            objetivo: "Condensar cláusulas relativas, temporales y causales usando cláusulas de participio para escritura académica concisa."
            concepto_clave_latex: ""
            ejemplo: "Equipped with MPPT tracking, the rooftop array harvested 19% more daily energy."
            bloque_sugerido: "Concise Editing 40 min • Eliminating wordiness & dangling modifiers"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Participle Clauses (-ing and -ed clauses for Concise Academic Writing): Communicative Purpose"
                puntos:
                  - "Present Participle (-ing) carries ACTIVE meaning ('Operating at 600°C, the turbine achieves 44% efficiency')."
                  - "Past Participle (-ed / V3) carries PASSIVE meaning ('Connected in series, the twelve cells deliver 14.4 V')."
                  - "Perfect Participle ('Having + V3' / 'Having been + V3') marks a COMPLETED prior step ('Having validated the mesh, we ran transient cases')."
                ejemplo: "Equipped with MPPT tracking, the rooftop array harvested 19% more daily energy."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Replacing relative clauses: 'fluids flowing (= that flow) through pipes' / 'data collected (= that were collected) at noon'."
                  - "Expressing result at sentence end: 'Irradiance surged to 1050 W/m², boosting output to 5.2 kW.'"
                  - "With conjunctions: 'When heated,...', 'While charging,...', 'Once commissioned,...'."
                tabla:
                  - ["Participle Form", "Voice & Timing", "Concise IEEE-Style Sentence"]
                  - ["Verb-ing", "Active (simultaneous/cause)", "Using Python, we automated the fit."]
                  - ["V3 (-ed)", "Passive (condition/state)", "Cooled by water, the core stays at 320 K."]
                  - ["Having + V3", "Active (completed earlier)", "Having calibrated sensors, we began trials."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "CRITICAL RULE — Avoid Dangling Participles! The implied subject of the introductory participle MUST match the grammatical subject of the main clause!"
                ejemplo: "Having completed all 20 queue slots, DownloadQueueService buffered new tasks in FIFO order."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Dangling error: *Analyzing the graph, a peak appeared at 2 p.m.* (Graphs don't analyze themselves!) -> Fix: 'Analyzing the graph, WE observed a peak at 2 p.m.' OR 'When analyzed, the graph revealed a peak.'"
                tabla:
                  - ["Dangling Participle (Wrong!)", "Aligned Subject (Correct!)"]
                  - ["Testing the circuit, a fuse blew.", "Testing the circuit, we blew a fuse. / While the circuit was being tested, a fuse blew."]
                  - ["Heated to 500 K, we measured expansion.", "Heated to 500 K, the alloy expanded by 0.6%."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Equipped with MPPT tracking, the rooftop array harvested 19% more daily energy."
                  - "Having completed all 20 queue slots, DownloadQueueService buffered new tasks in FIFO order."
                  - "Driven by trade winds, turbines in La Guajira achieve capacity factors above 50%."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Condense: 'Because the steam is superheated to 540°C, it prevents blade erosion.'"
                  - "Fix the dangling participle: 'Using Fourier's law, the heat flux was calculated.'"
                  - "Condense 3 wordy two-clause sentences into crisp IEEE participle clauses."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 4
            corte: 2
            modalidad: "general"
            titulo: "Subjunctive Mood & Formal Recommendations (It is essential that he be...)"
            objetivo: "Redactar recomendaciones normativas, criterios de diseño y cláusulas formales usando el modo subjuntivo mandativo."
            concepto_clave_latex: ""
            ejemplo: "It is essential that emergency backup power be restored within ten seconds."
            bloque_sugerido: "Policy & Standards Writing 35 min • Formal engineering recommendations"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Subjunctive Mood & Formal Recommendations (It is essential that he be...): Communicative Purpose"
                puntos:
                  - "Mandative Subjunctive uses the BARE INFINITIVE (be, remain, operate, NOT be -> 'not exceed') for ALL subjects (including he/she/it!) after 'that'."
                  - "Trigger Verbs: recommend, suggest, insist, demand, require, propose, stipulate."
                  - "Trigger Adjectives: essential, vital, imperative, crucial, mandatory, necessary ('It is imperative that frequency remain within ±0.2 Hz')."
                ejemplo: "It is essential that emergency backup power be restored within ten seconds."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Affirmative Subjunctive: 'IEEE standards require that every inverter BE tested for anti-islanding.'"
                  - "Negative Subjunctive ('not' + bare verb — NO 'do/does'!): 'We recommend that the PDF file NOT exceed 1.2 MB.'"
                  - "British/less formal alternative: 'should + base verb' ('recommend that the valve should be inspected')."
                tabla:
                  - ["Trigger", "Subjunctive Clause", "Key Observation"]
                  - ["insist / require that", "...the chassis BE grounded", "'be', NOT 'is'"]
                  - ["essential / vital that", "...pressure NOT exceed 8 bar", "'not exceed', NOT 'doesn't'"]
                  - ["propose / suggest that", "...each unit UNDERGO testing", "'undergo', NOT 'undergoes'"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Fixed academic subjunctive expressions: 'Suffice it to say...', 'Be that as it may,...', 'If need be,...'"
                ejemplo: "The audit report recommends that the plant replace its steam traps immediately."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "NEVER write *recommend us to install*! Use either 'recommend installing' OR mandative subjunctive 'recommend that the facility install...'!"
                tabla:
                  - ["Common B1 Error", "C1/B2 Mandative Subjunctive"]
                  - ["The code requires that voltage is stable.", "The code requires that voltage be stable."]
                  - ["They suggested that he doesn't change R.", "They suggested that he not change R."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "It is essential that emergency backup power be restored within ten seconds."
                  - "The audit report recommends that the plant replace its steam traps immediately."
                  - "Safety protocols stipulate that no technician work on live high-voltage switchgear alone."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Complete: 'It is crucial that total file size ___ (not surpass) 1.2 MB' -> 'not surpass'."
                  - "Rewrite formally: 'The committee advised the plant to monitor NOx hourly' (use 'recommend that...')."
                  - "Write 3 policy recommendations for campus sustainability using the subjunctive."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 5
            corte: 2
            modalidad: "general"
            titulo: "Advanced Modals in the Past (Should have, Could have, Must have been)"
            objetivo: "Evaluar retrospectivamente fallas, alternativas no ejecutadas y deducciones probables sobre eventos pasados."
            concepto_clave_latex: ""
            ejemplo: "The inverter tripped at noon; cloud-edge lensing must have caused a brief irradiance spike."
            bloque_sugerido: "Forensic Engineering 40 min • Retrospective fault deduction & design review"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Advanced Modals in the Past (Should have, Could have, Must have been): Communicative Purpose"
                puntos:
                  - "PAST DEDUCTION: 'must have + V3' (~95% sure it happened), 'may/might/could have + V3' (possible past cause), 'can't/couldn't have + V3' (impossible in the past)."
                  - "PAST EVALUATION / CRITIQUE: 'should (not) have + V3' / 'ought to have + V3' (something was advisable, but the opposite happened!)."
                  - "UNREALIZED PAST POTENTIAL: 'could have + V3' (had the capability/opportunity, didn't happen) & 'needn't have + V3' (did something unnecessary)."
                ejemplo: "The inverter tripped at noon; cloud-edge lensing must have caused a brief irradiance spike."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Continuous past deduction: 'must / might have been + V-ing' ('The sensor must have been drifting during Trial 2')."
                  - "Passive past modal: 'modal + have been + V3' ('Thermal paste should have been applied evenly')."
                  - "Contrast: 'didn't need to calibrate' (wasn't needed, so we didn't) vs. 'needn't have calibrated' (we calibrated it, then found out it was factory-calibrated!)."
                tabla:
                  - ["Past Modal", "Retrospective Function", "Engineering Diagnostic"]
                  - ["must have + V3", "Strong logical conclusion", "Arc marks show a surge must have hit."]
                  - ["can't have + V3", "Logical impossibility", "The pump can't have run; power was off."]
                  - ["should have + V3", "Missed best practice", "We should have logged ambient humidity."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "In peer reviews and incident reports, prefer impersonal passive ('A snubber circuit should have been included') over blaming individuals!"
                ejemplo: "In hindsight, a larger heat sink should have been selected for the MOSFET stage."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Pronunciation & writing reminder: 'must've, could've, should've' sound like /əv/ in speech, NEVER write 'of'!"
                tabla:
                  - ["Form", "Did the Action Happen?", "Example"]
                  - ["didn't have to / didn't need to", "Usually NO (not required)", "We didn't have to recompile."]
                  - ["needn't have + V3", "YES (done unnecessarily)", "We needn't have printed 30 copies."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "The inverter tripped at noon; cloud-edge lensing must have caused a brief irradiance spike."
                  - "In hindsight, a larger heat sink should have been selected for the MOSFET stage."
                  - "That anomaly couldn't have originated in the battery pack because its breaker was open."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Deduce past cause: 'The fuse is melted and smells burnt' (use 'must have')."
                  - "Critique politely in passive: 'Nobody grounded the shield cable' (use 'should have been')."
                  - "Explain 'could have exploded' vs. 'might have leaked' in an incident briefing."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 6
            corte: 2
            modalidad: "general"
            titulo: "Hedging & Academic Caution (Appears to, Tends to, Suggests that)"
            objetivo: "Modular afirmaciones científicas con cautela epistémica (hedging) para evitar generalizaciones absolutas no demostradas."
            concepto_clave_latex: ""
            ejemplo: "Our findings suggest that hybrid PV-wind sizing can lower LCOE in off-grid communities."
            bloque_sugerido: "Peer-Review Tone 35 min • Calibrating epistemic certainty in discussions"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Hedging & Academic Caution (Appears to, Tends to, Suggests that): Communicative Purpose"
                puntos:
                  - "Scientific integrity requires distinguishing PROVEN LAWS from EMPIRICAL INTERPRETATIONS using 'hedging' (epistemic caution)."
                  - "Lexical hedges: modal verbs (may, might, could), epistemic verbs (appear to, seem to, tend to, suggest, indicate), adverbs (arguably, plausibly, relatively, predominantly), and qualifiers (under tested conditions)."
                  - "Overstating claims ('This proves X solves all grid issues') triggers immediate peer-review rejection!"
                ejemplo: "Our findings suggest that hybrid PV-wind sizing can lower LCOE in off-grid communities."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Strong claim -> Hedged claim: 'Causes corrosion' -> 'Tends to accelerate corrosion under high salinity.'"
                  - "Reporting evidence: 'These results suggest / indicate that...' (softer than 'prove')."
                  - "Probability adjectives: 'It is likely / plausible / conceivable that...'."
                tabla:
                  - ["Device Category", "Hedge Expressions", "Academic Sentence"]
                  - ["Epistemic Verbs", "appear to, tend to, suggest", "Dust accumulation tends to lower yield."]
                  - ["Modal & Adverb", "may potentially, largely", "BESS may substantially curb curtailment."]
                  - ["Scope Limiter", "within this regime, preliminarily", "Preliminary data point to a 9% gain."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Balance caution with confidence: do NOT double- or triple-hedge needlessly (*It might possibly perhaps seem to suggest* is weak); 1–2 precise hedges strike ideal IEEE tone."
                ejemplo: "Cell degradation tends to accelerate when operating temperatures consistently exceed 330 K."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Know WHEN NOT to hedge: established physical laws and your exact experimental actions take direct verbs ('We measured V every 2 s'; 'Energy is conserved')."
                tabla:
                  - ["Too Blunt / Absolute", "Balanced B2/C1 Academic Hedge"]
                  - ["This eliminates blackouts forever.", "This approach can significantly reduce outage risk."]
                  - ["Salt air destroys all inverters.", "Coastal salinity appears to accelerate enclosure degradation."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Our findings suggest that hybrid PV-wind sizing can lower LCOE in off-grid communities."
                  - "Cell degradation tends to accelerate when operating temperatures consistently exceed 330 K."
                  - "This discrepancy may be attributed to unmodeled parasitic capacitance."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Hedge this overclaim: 'Electric vehicles will solve climate change.'"
                  - "Hedge an experimental anomaly explanation using 'may be attributed to' or 'appears to'."
                  - "Identify which sentences in a discussion section need hedging vs. direct statement."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 7
            corte: 2
            modalidad: "general"
            titulo: "Discourse Markers for Data Presentation & Trend Analysis"
            objetivo: "Describir gráficas, tendencias dinámicas, tasas de cambio y correlaciones durante ponencias y análisis de resultados."
            concepto_clave_latex: ""
            ejemplo: "As shown in Figure 3, wind generation climbs steeply above cut-in speed before plateauing at rated power."
            bloque_sugerido: "Data Commentary 40 min • Presenting figures & preposition accuracy (by/to/of/at)"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Discourse Markers for Data Presentation & Trend Analysis: Communicative Purpose"
                puntos:
                  - "Pair precise TREND VERBS (surge, climb, plateau, fluctuate, dip, plummet) with DEGREE ADVERBS (sharply, steadily, marginally, exponentially)."
                  - "Verb + Adverb pattern ('Demand rose sharply by 18%') = Adjective + Noun pattern ('There was a sharp 18% rise in demand')."
                  - "Preposition precision: rise FROM 10 TO 15 (span), increase BY 5 (delta!), peak AT 22 MW (point), an increase OF 5 MW (after noun!)."
                ejemplo: "As shown in Figure 3, wind generation climbs steeply above cut-in speed before plateauing at rated power."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Visual signposting in talks: 'As illustrated in Figure 2,...', 'Turning to the dashed curve,...', 'Notably, a plateau occurs between...'"
                  - "Contrast & correlation: 'In stark contrast,...', 'Conversely,...', 'Closely mirroring irradiance, output peaks at solar noon.'"
                tabla:
                  - ["Movement", "High-Precision Verbs", "Preposition Rule"]
                  - ["Rapid Upward", "surge, soar, jump, climb", "rose BY 14% / FROM 40 TO 46"]
                  - ["Stability / Peak", "level off, plateau, peak", "stabilized AT 60 Hz / peaked AT 9 MW"]
                  - ["Downward", "decline, drop, dip, plummet", "a drop OF 3.2 V (noun + of)"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "CRITICAL PREPOSITION CHECK: 'increased BY 12%' (= delta +12%) vs. 'increased TO 82%' (= final level 82%)! Mixing 'by' and 'to' changes the math completely!"
                ejemplo: "Between 12:00 and 14:00, campus cooling load peaked at 1.8 MW, whereas PV supplied 640 kW."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid repetitive 'went up / went down' in formal talks -> vary between verb+adverb and 'saw/experienced a [adj] [noun]'."
                tabla:
                  - ["Verb Construction", "Equivalent Noun Construction"]
                  - ["LCOE fell dramatically by 70%.", "Solar PV experienced a dramatic 70% fall in LCOE."]
                  - ["Efficiency leveled off at 3000 rpm.", "A clear efficiency plateau was observed at 3000 rpm."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "As shown in Figure 3, wind generation climbs steeply above cut-in speed before plateauing at rated power."
                  - "Between 12:00 and 14:00, campus cooling load peaked at 1.8 MW, whereas PV supplied 640 kW."
                  - "Battery state of charge declined steadily overnight by 42 percentage points."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Convert to Noun Phrase: 'Grid demand rose steadily from 8 GW to 11 GW.'"
                  - "Choose preposition: 'Efficiency improved (by / to) 3.5%, reaching 96.5%' -> 'by'."
                  - "Deliver a 60-second spoken walkthrough of a daily solar duck-curve chart."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 8
            corte: 3
            modalidad: "general"
            titulo: "Structuring an IMRaD Research Paper (Introduction, Methods, Results, Discussion)"
            objetivo: "Dominar la arquitectura retórica IMRaD, tiempos verbales por sección y transiciones de artículos científicos."
            concepto_clave_latex: ""
            ejemplo: "Section II details the governing thermodynamic equations and boundary conditions."
            bloque_sugerido: "IMRaD Blueprint 45 min • Drafting structured sections of an IEEE paper"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Structuring an IMRaD Research Paper (Introduction, Methods, Results, Discussion): Communicative Purpose"
                puntos:
                  - "IMRaD = Introduction (Why did you do it?), Methods (How did you do it?), Results (What did you find?), and Discussion (What does it mean?)."
                  - "CARS Model (Swales) for Introductions: Move 1 Establish territory -> Move 2 Identify research niche/gap -> Move 3 Occupy the niche ('In this work, we present...')."
                  - "Hourglass flow: broad context (Intro) -> narrow reproducible specifics (Methods/Results) -> broad implications & limitations (Discussion/Conclusion)."
                ejemplo: "Section II details the governing thermodynamic equations and boundary conditions."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Methods = Past Simple Passive + exact parameters so peers can replicate ('A 10 kW inverter was tested under IEC 62116')."
                  - "Results = Past Simple for findings + Present Simple to refer to visuals ('Table 2 summarizes...', 'Output reached...')."
                  - "Discussion = interpret mechanisms, compare with literature ('consistent with [14]'), acknowledge limitations, propose future work."
                tabla:
                  - ["IMRaD Section", "Primary Communicative Goal", "Dominant Tenses"]
                  - ["Introduction", "Context -> Gap -> Contribution", "Present Perfect & Present Simple"]
                  - ["Methods", "Reproducible setup & equations", "Past Simple Passive"]
                  - ["Results", "Objective data & figures", "Past Simple (+ Present for Fig/Table)"]
                  - ["Discussion", "Interpretation, comparison, limits", "Present Simple + Hedging Modals"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Keep Results & Discussion distinct when required: Results state WHAT happened ('Voltage dropped 4%'); Discussion explains WHY ('attributable to line inductance')."
                ejemplo: "As summarized in Table 1, the proposed controller outperformed PI tuning by 21%."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never introduce brand-new raw experimental numbers for the first time in the Conclusion!"
                tabla:
                  - ["Section Signpost", "High-Utility Academic Phrase"]
                  - ["Gap (Intro)", "Nevertheless, few studies have addressed transient thermal coupling in..."]
                  - ["Limitation (Disc.)", "A limitation of the present model is the assumption of isotropic conductivity."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Section II details the governing thermodynamic equations and boundary conditions."
                  - "As summarized in Table 1, the proposed controller outperformed PI tuning by 21%."
                  - "Future work will extend this framework to unbalanced three-phase distribution feeders."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Classify 6 sample sentences into I, M, R, or D based on verb tense and rhetoric."
                  - "Write a 3-sentence CARS Introduction (Territory -> Gap -> Contribution) for a renewable topic."
                  - "Draft 1 limitation sentence + 1 future-work sentence."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 9
            corte: 3
            modalidad: "general"
            titulo: "Pitching Projects & Defending Technical Proposals in English"
            objetivo: "Estructurar presentaciones ejecutivas de proyectos energéticos y responder preguntas críticas de jurados en inglés."
            concepto_clave_latex: ""
            ejemplo: "Good morning. Today we present a resilient solar-storage microgrid for rural health centers."
            bloque_sugerido: "Oral Defense Studio 45 min • 3-minute technical pitch & live Q&A simulation"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Pitching Projects & Defending Technical Proposals in English: Communicative Purpose"
                puntos:
                  - "High-impact technical pitch structure (3–5 minutes): (1) Quantified Problem Hook, (2) Proposed Engineering Solution, (3) Technical & Economic Feasibility (KPIs / LCOE / ROI), (4) Validation & Call to Action."
                  - "Signposting guides listeners effortlessly: 'I'll begin by outlining...', 'Moving on to our architecture,...', 'To wrap up,...'."
                  - "Handling tough Q&A: Acknowledge -> Bridge/Clarify -> Answer concisely with evidence!"
                ejemplo: "Good morning. Today we present a resilient solar-storage microgrid for rural health centers."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "Delivery fundamentals: pause before key metrics, stress contrastive numbers ('NOT 12 megabytes, under ONE POINT TWO megabytes'), maintain eye contact instead of reading dense paragraphs."
                  - "Q&A buffers for complex questions: 'That's a crucial point regarding grid inertia. In our simulations,...'"
                  - "Honest boundary handling: 'While harmonic flicker was outside our current scope, preliminary checks suggest...'."
                tabla:
                  - ["Pitch / Q&A Stage", "Professional Phrase", "Purpose"]
                  - ["Hook", "Every year, coastal grids lose 14%...", "Establish urgency with data"]
                  - ["Transition", "Having sized the array, let's examine cost.", "Smooth logical bridge"]
                  - ["Q&A Defense", "That's an insightful question. Our data show...", "Composed, evidence-led reply"]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - "Rule of 6 on slides: concise bullet cues (like UM STUDIO's MinimalSlideViewer!), NEVER walls of text read verbatim."
                ejemplo: "From an economic standpoint, the system achieves payback in 4.2 years."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Avoid defensive fillers ('Eh, no, you didn't understand me') -> reframe diplomatically: 'Allow me to clarify Slide 4...'."
                tabla:
                  - ["Blunt / Informal Q&A", "Diplomatic B2/C1 Defense"]
                  - ["I don't know that number.", "I don't have the exact figure at hand, but it falls near 85%."]
                  - ["You're wrong about the cost.", "Actually, when O&M is factored in, life-cycle cost drops by 18%."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Good morning. Today we present a resilient solar-storage microgrid for rural health centers."
                  - "From an economic standpoint, the system achieves payback in 4.2 years."
                  - "Thank you for raising thermal derating — we accounted for 40°C ambient conditions in Santa Marta."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Write a 45-second Problem-Solution-Impact elevator pitch for an energy project."
                  - "Practice 3 diplomatic Q&A responses to skeptical reviewer questions."
                  - "Deliver a 6-slide presentation aloud using signposting transitions."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 10
            corte: 3
            modalidad: "general"
            titulo: "Critical Synthesis, Paraphrasing & Avoiding Plagiarism in IEEE Style"
            objetivo: "Sintetizar múltiples fuentes académicas, parafrasear estructuralmente y citar rigurosamente bajo formato IEEE."
            concepto_clave_latex: ""
            ejemplo: "Recent studies [1]–[3] converge on green hydrogen as a viable seasonal storage vector."
            bloque_sugerido: "IEEE Synthesis Lab 45 min • Structural paraphrasing & multi-source literature synthesis"
            slides:
              - numero: 1
                seccion: "CEFR B2 • CORE CONCEPT"
                titulo: "Critical Synthesis, Paraphrasing & Avoiding Plagiarism in IEEE Style: Communicative Purpose"
                puntos:
                  - "True paraphrasing transforms BOTH vocabulary AND syntactic structure while preserving exact technical meaning AND citing the source [1]."
                  - "Patchwriting (swapping 2–3 synonyms while copying sentence skeleton) counts as plagiarism in international journals!"
                  - "IEEE Citation Style uses numbered square brackets in order of appearance: '[1]', '[2], [3]', '[4]–[7]' — placed BEFORE punctuation ('...as shown in [3].')."
                ejemplo: "Recent studies [1]–[3] converge on green hydrogen as a viable seasonal storage vector."
              - numero: 2
                seccion: "STRUCTURE & PATTERNS"
                titulo: "Core Grammatical Blueprint"
                puntos:
                  - "4-Step Paraphrase Technique: (1) Read & understand without looking, (2) Change voice/clause structure (Active <-> Passive, Clause <-> Nominalization), (3) Use accurate domain terminology (keep fixed terms like 'Rankine cycle'!), (4) Append '[N]' citation."
                  - "Integral citation (author as subject): 'As Sadiku [2] demonstrates,...' vs. Non-integral (data-focused): 'Losses rise quadratically with current [2].'"
                  - "Synthesis groups multiple studies by theme: 'While [1] and [4] favor Li-ion, [5] advocates flow batteries for >8 h storage.'"
                tabla:
                  - ["Citation Mode", "Focus", "IEEE Format Example"]
                  - ["Non-integral", "Finding / Process", "Perovskite stability has improved markedly [1], [2]."]
                  - ["Integral", "Author / Landmark work", "Çengel and Boles [3] formulate exergy destruction as..."]
                  - ["Numeric Treat", "Grammatical Noun", "In [4], a decentralized OPF algorithm is proposed."]
              - numero: 3
                seccion: "QUESTIONS & NEGATION"
                titulo: "Interrogative, Negative & Short Answers"
                puntos:
                  - " Notice IEEE bracket grammar: '[4]' can act as a noun ('In [4], the authors...' or 'contrary to [4]'), unlike APA '(Smith, 2024)'!"
                ejemplo: "Contrary to earlier assumptions in [4], dynamic line rating unlocked 18% extra capacity [5]."
              - numero: 4
                seccion: "PRECISION & CONTRAST"
                titulo: "Key Distinctions & Common Pitfalls"
                puntos:
                  - "Never translate a Spanish or English source word-for-word without citation (translation plagiarism is detected by cross-language similarity engines!)."
                tabla:
                  - ["Original Source Sentence", "Acceptable Paraphrase + IEEE Citation"]
                  - ["'High cell temperatures severely degrade PV module lifespan' (Duffie, 2020).", "Elevated operating temperatures have been shown to accelerate photovoltaic aging [1]."]
              - numero: 5
                seccion: "CAMPUS & LAB CONTEXT"
                titulo: "Authentic Academic & Engineering Usage"
                puntos:
                  - "Recent studies [1]–[3] converge on green hydrogen as a viable seasonal storage vector."
                  - "Contrary to earlier assumptions in [4], dynamic line rating unlocked 18% extra capacity [5]."
                  - "All external equations, datasets, and conceptual frameworks must be explicitly credited in IEEE references."
                ejemplo: "Academic Register (CEFR B2): Clear, concise communication in Unimagdalena seminars."
              - numero: 6
                seccion: "MASTERY CHECK"
                titulo: "Self-Assessment & Oral Drill"
                puntos:
                  - "Paraphrase structurally + cite [1]: 'Wind speed cubed governs the kinetic power available to a rotor.'"
                  - "Synthesize 2 contrasting findings ([2] = lower cost, [3] = shorter cycle life) in one sentence."
                  - "Check IEEE punctuation placement: '...efficiency reached 92% [6].' (period AFTER bracket!)."
                ejemplo: "Practice reading each model sentence aloud with natural stress and intonation."
          - numero_tema: 11
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Heat Transfer Modes (Conduction, Convection & Radiation)"
            objetivo: "Verbalizar en inglés las ecuaciones constitutivas de Fourier, enfriamiento de Newton y radiación de Stefan-Boltzmann."
            concepto_clave_latex: "q''_x = -k\\frac{dT}{dx} \\quad ; \\quad q'' = h(T_s - T_\\infty) \\quad ; \\quad E_b = \\varepsilon \\sigma T_s^4"
            verbalizacion_ingles: "• q''_x = -k dT/dx -> \"heat flux q double prime sub x (in watts per square meter) equals minus thermal conductivity k times d T by d x\" (note: q = heat rate [W], q' = per unit length [W/m], q'' = heat flux [W/m²], q''' = volumetric generation [W/m³]!).\n• q'' = h (T_s - T_∞) -> \"convective heat flux equals convection coefficient h times surface temperature T sub s minus free-stream temperature T infinity\".\n• E_b = ε σ T_s⁴ -> \"emissive power equals emissivity epsilon times the Stefan-Boltzmann constant sigma times absolute surface temperature T sub s to the fourth power\"."
            ejemplo: "Exposición oral de disipación térmica combinada por convección y radiación en la cubierta posterior de un panel solar."
            bloque_sugerido: "Heat Transfer Speech 35 min • Primes on heat flux (q, q', q'', q''') & T-infinity"
          - numero_tema: 12
            corte: 1
            modalidad: "notacion_ingenieria"
            titulo: "Solar Photovoltaic & Wind Power Equations"
            objetivo: "Exponer con fluidez la potencia eólica, el coeficiente de Betz, el factor de llenado fotovoltaico (FF) y la eficiencia STC."
            concepto_clave_latex: "P_w = \\frac{1}{2} C_p \\rho A v^3 \\quad ; \\quad FF = \\frac{V_{\\text{mp}} I_{\\text{mp}}}{V_{\\text{oc}} I_{\\text{sc}}} \\quad ; \\quad \\eta_{\\text{PV}} = \\frac{V_{\\text{oc}} I_{\\text{sc}} FF}{G \\cdot A_c}"
            verbalizacion_ingles: "• P_w = 1/2 C_p ρ A v³ -> \"extracted wind power P sub w equals one-half times power coefficient C sub p times air density rho times rotor swept area A times wind speed v cubed\" (Betz limit: C_p,max = 16/27 ≈ 0.593).\n• FF = (V_mp I_mp) / (V_oc I_sc) -> \"fill factor F-F equals V at maximum power times I at maximum power, divided by open-circuit voltage V sub o c times short-circuit current I sub s c\"."
            ejemplo: "Defensa técnica en inglés del impacto cúbico de la velocidad del viento en parques eólicos de La Guajira."
            bloque_sugerido: "Renewables Keynote 35 min • Betz power equation & PV I-V curve metrics aloud"
          - numero_tema: 13
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Power Systems & Optimal Power Flow (OPF) Notation"
            objetivo: "Verbalizar potencia compleja, ecuaciones no lineales de flujo de carga AC y magnitudes en el sistema por unidad (p.u.)."
            concepto_clave_latex: "S = P + jQ \\quad ; \\quad P_i = \\sum_{k=1}^{N} |V_i||V_k|(G_{ik}\\cos\\theta_{ik} + B_{ik}\\sin\\theta_{ik}) \\quad ; \\quad X_{\\text{p.u.}} = \\frac{X_{\\text{actual}}}{X_{\\text{base}}}"
            verbalizacion_ingles: "• S = P + jQ -> \"apparent (complex) power S equals active power P (in megawatts) plus j times reactive power Q (in megavars)\".\n• P_i = Σ_{k=1}^N |V_i||V_k| (G_ik cos θ_ik + B_ik sin θ_ik) -> \"active power injection at bus i equals the sum from k equals one to N of voltage magnitude V sub i times V sub k times quantity conductance G sub i k cosine theta sub i k plus susceptance B sub i k sine theta sub i k\".\n• p.u. -> \"per-unit value equals actual quantity divided by base quantity\" (e.g., \"one point zero two per unit\")."
            ejemplo: "Presentación oral de restricciones nodales de despacho óptimo (AC-OPF) en un alimentador IEEE de 14 nodos."
            bloque_sugerido: "Power Systems Talk 35 min • AC power-flow equations & per-unit verbalization"
          - numero_tema: 14
            corte: 2
            modalidad: "notacion_ingenieria"
            titulo: "Electrochemistry, Green Hydrogen & Storage Metrics"
            objetivo: "Leer en inglés la ecuación electroquímica de Nernst, estado de carga (SoC) y costo nivelado de energía (LCOE)."
            concepto_clave_latex: "E = E^\\circ - \\frac{RT}{nF}\\ln(Q) \\quad ; \\quad SoC(t) = SoC_0 - \\frac{1}{C_{\\text{nom}}}\\int_0^t I(\\tau)\\,d\\tau \\quad ; \\quad LCOE = \\frac{\\sum_{t=1}^{n}\\frac{I_t + M_t}{(1+r)^t}}{\\sum_{t=1}^{n}\\frac{E_t}{(1+r)^t}}"
            verbalizacion_ingles: "• E = E° - (RT / nF) ln(Q) -> \"cell potential E equals standard electrode potential E naught (or E standard) minus R T over n F times the natural log of reaction quotient Q\".\n• SoC(t) -> \"state of charge at time t equals initial state of charge minus one over nominal capacity C nom times the integral from zero to t of current I of tau d tau\".\n• LCOE -> \"levelized cost of energy (in dollars per megawatt-hour) equals discounted life-cycle CAPEX plus O-and-M costs divided by discounted lifetime energy generation at discount rate r\"."
            ejemplo: "Evaluación tecnoeconómica oral de un electrolizador PEM acoplado a baterías LFP expresando LCOE y LCOH en inglés."
            bloque_sugerido: "Storage & H2 Defense 35 min • Nernst potential, Coulomb counting & LCOE formula"
          - numero_tema: 15
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Interpreting & Presenting Graphs, Error Bars & Regression (R^2, RMSE)"
            objetivo: "Exponer oralmente pendientes, barras de incertidumbre, desviación estándar, coeficiente R² y error cuadrático medio (RMSE)."
            concepto_clave_latex: "m = \\frac{\\Delta y}{\\Delta x} \\quad ; \\quad \\sigma = \\sqrt{\\frac{1}{N}\\sum_{i=1}^{N}(x_i - \\mu)^2} \\quad ; \\quad R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}} \\quad ; \\quad \\text{RMSE} = \\sqrt{\\frac{1}{N}\\sum_{i=1}^{N}(y_i - \\hat{y}_i)^2}"
            verbalizacion_ingles: "• m = Δy / Δx -> \"the slope m equals delta y over delta x (change in y per unit change in x)\".\n• σ = √[ (1/N) Σ (x_i - μ)² ] -> \"standard deviation sigma equals the square root of one over N times the sum of x sub i minus mean mu, quantity squared\" (error bars: \"mean plus or minus one standard deviation, μ ± σ\").\n• R² -> \"coefficient of determination R-squared\"  |  RMSE (ŷ_i = \"y-hat sub i\") -> \"root-mean-square error equals the square root of the mean of squared residuals y sub i minus y-hat sub i\"."
            ejemplo: "Defensa de validación de un modelo de predicción solar con R² = 0.984 ('R-squared of zero point nine eight four') y barras de error."
            bloque_sugerido: "Regression & Stats Talk 35 min • Describing R-squared, y-hat, RMSE & error bars"
          - numero_tema: 16
            corte: 3
            modalidad: "notacion_ingenieria"
            titulo: "Uncertainty Propagation & Optimization Problem Verbalization"
            objetivo: "Verbalizar formulaciones de optimización con restricciones y propagación gaussiana de incertidumbre experimental."
            concepto_clave_latex: "\\min_{x \\in \\mathbb{R}^n} f(x) \\;\\;\\text{s.t.}\\;\\; g_i(x) \\le 0,\\; h_j(x) = 0 \\quad ; \\quad u_y = \\sqrt{\\sum_{k=1}^{m}\\left(\\frac{\\partial y}{\\partial x_k} u_{x_k}\\right)^2}"
            verbalizacion_ingles: "• min_{x ∈ ℝ^n} f(x) s.t. g_i(x) ≤ 0, h_j(x) = 0 -> \"minimize objective function f of x over x in R-n, subject to inequality constraints g sub i of x less than or equal to zero and equality constraints h sub j of x equal to zero\".\n• u_y = √[ Σ (∂y/∂x_k · u_{x_k})² ] -> \"combined standard uncertainty u sub y equals the square root of the sum of squared sensitivity coefficients partial y over partial x sub k times uncertainty u sub x k\"."
            ejemplo: "Exposición formal en congreso IEEE de un problema de dimensionamiento óptimo sujeto a restricciones operativas e incertidumbre."
            bloque_sugerido: "Conference Defense 35 min • 'Minimize... subject to...' & GUM uncertainty aloud"
      - codigo: "04021823"
        nombre: "Ingeniería del Diseño y Modelado en 3D"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Geometría Descriptiva, Vistas Ortogonales y Normas ISO/ASME"
            objetivo: "Representar componentes mecánicos y energéticos mediante proyecciones normalizadas."
            concepto_clave_latex: "E = \\frac{D_{\\text{dibujo}}}{D_{\\text{real}}} \\quad ; \\quad \\theta_{\\text{diedro}} = 90^\\circ"
            ejemplo: "Lectura e interpretación de planos constructivos de una carcasa de turbina."
            bloque_sugerido: "Laboratorio CAD 45 min • Vistas y cortes"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Modelado Paramétrico 3D de Sólidos y Superficies Complejas"
            objetivo: "Construir piezas paramétricas restringidas y perfiles aerodinámicos 3D en CAD."
            concepto_clave_latex: "\\vec{C}(u) = \\sum_{i=0}^{n} N_{i,p}(u)\\vec{P}_i \\quad ; \\quad u \\in [0, 1]"
            ejemplo: "Modelado 3D de un álabe eólico con torsión variable a lo largo de la envergadura."
            bloque_sugerido: "Laboratorio CAD 50 min • Sólidos y lofting"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Ensamblajes Mecánicos, Grados de Libertad y Cinemática CAD"
            objetivo: "Integrar subensambles verificando colisiones, holguras y movimiento articulado."
            concepto_clave_latex: "\\text{GDL} = 6(N - 1) - \\sum_{i} c_i"
            ejemplo: "Ensamblaje completo de un seguidor solar de dos ejes con actuador lineal."
            bloque_sugerido: "Laboratorio CAD 50 min • Ensambles 3D"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Tolerancias Dimensionales, Ajustes ISO y GD&T"
            objetivo: "Especificar ajustes eje-agujero y tolerancias geométricas para manufacturabilidad."
            concepto_clave_latex: "T = D_{\\max} - D_{\\min} \\quad ; \\quad J = D_{\\text{agujero}} - d_{\\text{eje}}"
            ejemplo: "Tolerancia de concentricidad y ajuste de rodamiento en el eje de un generador."
            bloque_sugerido: "Práctica 45 min • Ajustes ISO y GD&T"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Diseño de Estructuras Metálicas, Soldadura y Tuberías (Piping)"
            objetivo: "Modelar bastidores estructurales solares e isométricos de tuberías térmicas."
            concepto_clave_latex: "\\sigma_{\\max} = \\frac{M_{\\max} c}{I} \\le \\frac{S_y}{FS}"
            ejemplo: "Diseño estructural resistente a ráfagas de viento de 120 km/h para mesas PV."
            bloque_sugerido: "Laboratorio CAD 50 min • Perfiles y piping"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Introducción al Análisis por Elementos Finitos (FEA Estático/Modal)"
            objetivo: "Validar esfuerzos de Von Mises, deformaciones y frecuencias naturales en CAE."
            concepto_clave_latex: "[K]\\vec{u} = \\vec{F} \\quad ; \\quad \\sigma_{\\text{vM}} = \\sqrt{\\sigma_1^2 - \\sigma_1\\sigma_2 + \\sigma_2^2} \\le \\frac{S_y}{FS}"
            ejemplo: "Simulación estructural FEA del soporte de góndola verificando factor de seguridad."
            bloque_sugerido: "Laboratorio CAE 50 min • Esfuerzos Von Mises"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Simulación Térmica y Fluidodinámica Básica en Entorno CAD"
            objetivo: "Evaluar disipación de calor en aletas y caída de presión interna mediante mallas 3D."
            concepto_clave_latex: "\\nabla\\cdot(k\\nabla T) + \\dot{q}_{\\text{gen}} = 0"
            ejemplo: "Optimización geométrica de un disipador de aluminio para módulos IGBT."
            bloque_sugerido: "Laboratorio CAE 50 min • Térmico 3D"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Documentación Ejecutiva, Lista de Materiales (BOM) y Prototipado"
            objetivo: "Generar planos de taller, vistas explosionadas, BOM y archivos STL/STEP para impresión 3D."
            concepto_clave_latex: "m_{\\text{BOM}} = \\sum_{k=1}^N \\rho_k V_k \\quad ; \\quad \\Delta m \\le 0.01\\,m"
            ejemplo: "Paquete técnico completo y prototipo impreso en 3D de un rodete microhidráulico."
            bloque_sugerido: "Taller 45 min • Planos, BOM y manufactura"
      - codigo: "04031827"
        nombre: "Legislación y Regulación Energética"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Constitución, Servicios Públicos y Leyes 142 y 143 de 1994"
            objetivo: "Comprender el régimen jurídico colombiano de servicios públicos domiciliarios y electricidad."
            concepto_clave_latex: "\\text{SAIDI} = \\frac{\\sum U_i N_i}{N_{\\text{tot}}} \\quad ; \\quad \\text{SAIFI} = \\frac{\\sum \\lambda_i N_i}{N_{\\text{tot}}}"
            ejemplo: "Separación legal e integración vertical/horizontal entre G, T, D y C en Colombia."
            bloque_sugerido: "Lectura Jurídica 45 min • Leyes 142 y 143"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Arquitectura Institucional: Minenergía, CREG, UPME, XM y SSPD"
            objetivo: "Identificar competencias regulatorias, planeación indicativa, operación y vigilancia."
            concepto_clave_latex: "CU_{v} = G_m + T_m + D_{n,m} + Cv_m + PR_{n,m} + R_m"
            ejemplo: "Funciones del CND/ASIC en XM y supervisión tarifaria de la SSPD."
            bloque_sugerido: "Pomodoro 45/10 • Mapa institucional"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Marco de Energías Renovables: Ley 1715 de 2014 y Ley 2099 de 2021"
            objetivo: "Aplicar incentivos tributarios para FNCER, eficiencia energética e hidrógeno verde/azul."
            concepto_clave_latex: "\\text{Beneficio}_{\\text{Ley1715}} = 0.50 \\cdot \\text{CAPEX} \\quad ; \\quad \\text{Arancel} = 0\\%"
            ejemplo: "Estructuración de beneficios tributarios UPME para un proyecto solar de 5 MW."
            bloque_sugerido: "Taller 50 min • Certificación UPME Ley 1715"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Autogeneración y Generación Distribuida (CREG 174 de 2021)"
            objetivo: "Gestionar conexión simplificada de AGPE, AGGE y liquidación de excedentes horarios."
            concepto_clave_latex: "VE_{\\text{exc}} = E_{\\text{exp,1}}\\cdot(CU - C_{\\text{inv}}) + E_{\\text{exp,2}}\\cdot P_{\\text{bolsa}}"
            ejemplo: "Liquidación mensual de créditos de energía de un autogenerador comercial < 100 kW."
            bloque_sugerido: "Práctica 45 min • Resolución CREG 174"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Reglamento Técnico de Instalaciones Eléctricas (RETIE / RETILAP)"
            objetivo: "Verificar requisitos obligatorios de seguridad eléctrica, distancias y dictamen de inspección."
            concepto_clave_latex: "I_{\\text{cuerpo}} \\le 25\\text{ mA} \\quad ; \\quad V_{\\text{contacto}} \\le \\frac{0.116}{\\sqrt{t_f}}(1000 + 1.5\\rho_s)"
            ejemplo: "Cumplimiento de distancias mínimas de seguridad y puesta a tierra según RETIE."
            bloque_sugerido: "Pomodoro 45/10 • Conformidad RETIE"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Licenciamiento Ambiental (ANLA / Corpamag) y Consulta Previa"
            objetivo: "Integrar Diagnóstico Ambiental de Alternativas (DAA), EIA y debida diligencia social."
            concepto_clave_latex: "I_{\\text{ambiental}} = \\sum_{k=1}^m w_k \\cdot C_k \\quad ; \\quad \\text{PMA} \\ge 0"
            ejemplo: "Requisitos de licencia ambiental y consulta previa OIT 169 en líneas y parques eólicos."
            bloque_sugerido: "Estudio de Caso 45 min • Licenciamiento"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Regulación de Gas Natural, Combustibles Líquidos y Biocombustibles"
            objetivo: "Analizar transporte de gas, mezclas obligatorias biodiésel/etanol y calidad de combustibles."
            concepto_clave_latex: "P_{\\text{transporte gas}} = f(\\text{Cargos Fijos Par } + \\text{Cargos Variables})"
            ejemplo: "Regulación CREG del mercado primario y secundario de capacidad de transporte de gas."
            bloque_sugerido: "Pomodoro 40/10 • Mercado regulado de gas"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Comunidades Energéticas (Decreto 2236/2023) y Mercados de Carbono"
            objetivo: "Estructurar esquemas asociativos energéticos, bonos de carbono e impuesto al carbono."
            concepto_clave_latex: "I_{\\text{carbono}} = m_{\\text{CO}_2\\text{e}} \\cdot P_{\\text{tCO}_2} \\quad ; \\quad \\Delta\\text{CO}_2 = 0"
            ejemplo: "Constitución jurídica y sostenibilidad tarifaria de una comunidad energética rural."
            bloque_sugerido: "Taller 45 min • Comunidades y carbono"
      - codigo: "06011840"
        nombre: "Máquinas Eléctricas"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Circuitos Magnéticos con Pérdidas en el Hierro (Steinmetz)"
            objetivo: "Cuantificar saturación B-H, pérdidas por histéresis y corrientes parásitas en núcleos."
            concepto_clave_latex: "P_{\\text{Fe}} = P_h + P_e = k_h f B_{\\max}^n + k_e f^2 B_{\\max}^2"
            ejemplo: "Efecto del espesor de chapas de acero al silicio de grano orientado sobre pérdidas en vacío."
            bloque_sugerido: "Pomodoro 45/10 • Pérdidas magnéticas"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Transformadores Monofásicos: Circuito Equivalente y Ensayos"
            objetivo: "Determinar parámetros de cortocircuito y vacío, regulación de tensión y eficiencia máxima."
            concepto_clave_latex: "\\%\\text{Reg} = \\frac{|V_{2,\\text{vacío}}| - |V_{2,\\text{plena}}|}{|V_{2,\\text{plena}}|}\\times 100\\% \\quad ; \\quad \\eta_{\\max}\\iff P_{\\text{Cu}} = P_{\\text{Fe}}"
            ejemplo: "Cálculo del circuito equivalente referido al primario a partir de pruebas OC y SC."
            bloque_sugerido: "Pomodoro 50/10 • Ensayos de transformador"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Transformadores Trifásicos, Grupos de Conexión y Autotransformadores"
            objetivo: "Seleccionar grupos vectoriales (Dyn11, YNd5) y condiciones de operación en paralelo."
            concepto_clave_latex: "S_{\\text{auto}} = S_{\\text{dev}}\\left(\\frac{V_H}{V_H - V_L}\\right) \\quad ; \\quad \\text{Desfase Dyn11} = -30^\\circ"
            ejemplo: "Transformador de subestación solar Dyn11 que bloquea circulación de tercer armónico."
            bloque_sugerido: "Práctica 50 min • Grupos vectoriales 3Φ"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Campo Magnético Giratorio y Fundamentos de Máquinas AC"
            objetivo: "Demostrar el teorema de Ferraris, velocidad síncrona y FEM inducida en devanados."
            concepto_clave_latex: "n_s = \\frac{120 f}{p} \\quad ; \\quad E_{\\text{rms}} = 4.44\\,f\\,N\\,k_w\\,\\Phi_{\\max}"
            ejemplo: "Frecuencia y número de polos en hidrogeneradores lentos frente a turbogeneradores de 2 polos."
            bloque_sugerido: "Pomodoro 45/10 • Campo giratorio"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Motores Asíncronos (Inducción) Trifásicos y Curva Par-Velocidad"
            objetivo: "Analizar deslizamiento, circuito equivalente por fase, par de arranque y par máximo."
            concepto_clave_latex: "s = \\frac{n_s - n_m}{n_s} \\quad ; \\quad P_{\\text{ag}} : P_{\\text{Cu},r} : P_{\\text{mec}} = 1 : s : (1-s)"
            ejemplo: "Flujo de potencias y eficiencia IE3/IE4 de un motor de inducción de 75 hp."
            bloque_sugerido: "Pomodoro 50/10 • Motor de inducción"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Arranque y Control de Velocidad VFD (Relación V/f y Vectorial)"
            objetivo: "Controlar velocidad y par de motores de inducción con convertidores PWM manteniendo flujo nominal."
            concepto_clave_latex: "\\Phi_{\\max} \\propto \\frac{V}{f} = \\text{const} \\quad (f \\le f_{\\text{nom}})"
            ejemplo: "Ahorro del 35% de potencia eléctrica al reducir al 85% la velocidad de un ventilador centrífugo."
            bloque_sugerido: "Práctica 45 min • Variadores VFD"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Generadores Síncronos: Circuito Equivalente y Curvas de Capabilidad"
            objetivo: "Analizar tensión interna E_A, ángulo de potencia δ y límites térmicos P-Q."
            concepto_clave_latex: "P_{3\\phi} = \\frac{3 V_\\phi E_A}{X_s}\\sin\\delta \\quad ; \\quad Q_{3\\phi} = \\frac{3 V_\\phi}{X_s}(E_A\\cos\\delta - V_\\phi)"
            ejemplo: "Sincronización a barra infinita y control de potencia reactiva mediante corriente de campo."
            bloque_sugerido: "Pomodoro 50/10 • Máquina síncrona"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Máquinas Síncronas de Imanes Permanentes (PMSG), DFIG y DC"
            objetivo: "Evaluar generadores modernos empleados en aerogeneradores de velocidad variable y tracción."
            concepto_clave_latex: "P_{\\text{total,DFIG}} = P_s + P_r = (1 - s)P_s \\quad ; \\quad E_a = k_a\\Phi\\omega_m"
            ejemplo: "Operación subsíncrona y supersíncrona de un generador doblemente alimentado (DFIG)."
            bloque_sugerido: "Taller 45 min • Generadores eólicos"
      - codigo: "05011834"
        nombre: "Proyecto Integrador CDIO I"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Marco CDIO (Concebir-Diseñar-Implementar-Operar) en Energía"
            objetivo: "Aplicar la metodología internacional CDIO a retos energéticos reales del entorno."
            concepto_clave_latex: "\\text{Ciclo CDIO: } \\text{Conceive} \\to \\text{Design} \\to \\text{Implement} \\to \\text{Operate}"
            ejemplo: "Identificación de necesidades energéticas reales en comunidades pesqueras o agrícolas del Magdalena."
            bloque_sugerido: "Taller CDIO 45 min • Árbol de problemas"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Levantamiento de Requerimientos y Especificaciones Técnicas (QFD)"
            objetivo: "Traducir necesidades de usuarios en métricas de ingeniería verificables."
            concepto_clave_latex: "S_j = \\sum_{i=1}^{m} w_i R_{ij} \\quad ; \\quad \\sum_{i=1}^m w_i = 1"
            ejemplo: "Definición de potencia pico, autonomía, peso máximo y presupuesto de un prototipo."
            bloque_sugerido: "Práctica 45 min • Matriz de requerimientos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Diseño Conceptual y Matrices Multicriterio (Pugh / AHP)"
            objetivo: "Generar alternativas funcionales y seleccionar el concepto óptimo con criterios ponderados."
            concepto_clave_latex: "V_k = \\sum_{j=1}^{n} w_j s_{kj}\\quad \\left(\\sum w_j = 1\\right)"
            ejemplo: "Evaluación objetiva entre tres arquitecturas de secador solar híbrido."
            bloque_sugerido: "Taller CDIO 45 min • Matriz de Pugh"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Dimensionamiento Preliminar y Balance Energético del Prototipo"
            objetivo: "Ejecutar cálculos de primera ley y dimensionamiento eléctrico/térmico del sistema elegido."
            concepto_clave_latex: "\\dot{E}_{\\text{captada}} \\ge \\frac{\\dot{E}_{\\text{demanda}}}{\\eta_{\\text{sub1}}\\cdot\\eta_{\\text{sub2}}}\\cdot FS"
            ejemplo: "Memoria de cálculo energético preliminar del prototipo de primer nivel CDIO."
            bloque_sugerido: "Pomodoro 50/10 • Memoria de cálculo"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Selección de Componentes Comerciales, Presupuesto y Cronograma"
            objetivo: "Elaborar lista de materiales (BOM), ruta crítica Gantt y gestión de riesgos."
            concepto_clave_latex: "C_{\\text{prototipo}} = \\sum_{i} n_i c_{u,i} + C_{\\text{manuf}} + C_{\\text{contingencia}}"
            ejemplo: "Selección con hojas de datos reales de paneles, controlador, sensores y estructura."
            bloque_sugerido: "Práctica 45 min • BOM y ruta crítica"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Integración de Hardware/Software y Seguridad en Prototipado"
            objetivo: "Construir el prototipo funcional aplicando estándares de cableado, fusibles y seguridad."
            concepto_clave_latex: "I_{\\text{prot}} \\le I_{\\text{adm}} \\quad ; \\quad R_{\\text{aisl}} \\ge 100\\text{ M}\\Omega"
            ejemplo: "Ensamble físico en banco de pruebas con adquisición de datos por microcontrolador."
            bloque_sugerido: "Laboratorio 50 min • Montaje seguro"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Protocolo de Pruebas Experimentales y Validación de Métricas"
            objetivo: "Medir variables de desempeño reales y contrastarlas contra el modelo teórico."
            concepto_clave_latex: "\\varepsilon_{\\text{rel}} = \\frac{|Y_{\\text{medido}} - Y_{\\text{diseño}}|}{|Y_{\\text{diseño}}|}\\times 100\\%"
            ejemplo: "Curva experimental horaria de eficiencia del prototipo con análisis de error."
            bloque_sugerido: "Laboratorio 50 min • Pruebas de aceptación"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Documentación Técnica IEEE y Defensa Ejecutiva del Proyecto"
            objetivo: "Comunicar resultados mediante artículo corto formato IEEE, póster y demostración en vivo."
            concepto_clave_latex: "\\text{TRL}_{\\text{final}} \\ge 4 \\quad ; \\quad \\varepsilon_{\\text{funcional}} \\le 5\\%"
            ejemplo: "Sustentación pública del prototipo CDIO I ante jurado de la Facultad de Ingeniería."
            bloque_sugerido: "Simulacro 45 min • Sustentación CDIO I"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Tipologías de Biomasa y Potencial Agroindustrial en Colombia"
            objetivo: "Cuantificar biomasa residual agrícola, pecuaria, forestal y RSU aprovechable."
            concepto_clave_latex: "E_{\\text{biomasa}} = \\dot{m}_{\\text{res}}\\cdot f_{\\text{disp}}\\cdot (1 - H_w)\\cdot \\text{PCI}"
            ejemplo: "Estimación del potencial energético de raquis de palma y vástago de banano en Magdalena."
            bloque_sugerido: "Pomodoro 45/10 • Potencial regional"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Caracterización Próxima, Última y Poder Calorífico"
            objetivo: "Evaluar humedad, cenizas, volátiles, carbono fijo y relaciones atómicas O/C y H/C."
            concepto_clave_latex: "\\text{PCI}_{\\text{bh}} = \\text{PCI}_{\\text{bs}}(1 - w) - 2.442\\,w \\quad [\\text{MJ/kg}]"
            ejemplo: "Diagrama de Van Krevelen y efecto de la humedad sobre el poder calorífico útil."
            bloque_sugerido: "Práctica 45 min • Análisis próximo/último"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Pretratamiento Físico, Secado y Densificación (Peletizado)"
            objetivo: "Diseñar procesos de astillado, molienda, secado térmico y torrefacción."
            concepto_clave_latex: "m_{\\text{agua evap}} = m_i\\frac{w_i - w_f}{1 - w_f} \\quad ; \\quad \\rho_e \\uparrow (\\text{Pellets } 650\\text{ kg/m}^3)"
            ejemplo: "Balance de masa y calor en secador rotatorio de bagazo previo a combustión."
            bloque_sugerido: "Pomodoro 45/10 • Secado y pellets"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Combustión Directa y Cogeneración en Calderas de Biomasa"
            objetivo: "Analizar parrillas móviles, lecho fluidizado burbujeante y formación de escorias."
            concepto_clave_latex: "\\dot{W}_{\\text{eléc}} = \\eta_e\\,\\dot{m}_b\\,\\text{PCI} \\quad ; \\quad T_{\\text{fusión ceniza}} > T_{\\text{hogar}}"
            ejemplo: "Cogeneración con cuesco y fibra de palma de aceite generando vapor sobrecalentado."
            bloque_sugerido: "Práctica 45 min • Calderas biomásicas"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Gasificación Termoquímica y Gas de Síntesis (Syngas)"
            objetivo: "Modelar zonas de secado, pirólisis, oxidación y reducción con relación de equivalencia ER."
            concepto_clave_latex: "\\text{ER} = \\frac{(A/C)_{\\text{real}}}{(A/C)_{\\text{esteq}}}\\approx 0.25 \\quad ; \\quad \\eta_{\\text{gas frío}} = \\frac{\\dot{V}_g\\,\\text{PCI}_g}{\\dot{m}_b\\,\\text{PCI}_b}"
            ejemplo: "Gasificador downdraft acoplado a motor de combustión interna para generación rural."
            bloque_sugerido: "Pomodoro 50/10 • Eficiencia gas frío"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Pirólisis Rápida, Bioaceite y Biocarbón (Biochar)"
            objetivo: "Optimizar temperatura y tasa de calentamiento para maximizar bio-oil o biochar."
            concepto_clave_latex: "\\text{Biomasa} \\xrightarrow{500^\\circ\\text{C},\\; t < 2\\text{ s},\\; \\text{sin O}_2} \\text{Bio-oil (70\\%)} + \\text{Char (15\\%)} + \\text{Gas (15\\%)}"
            ejemplo: "Valorización de residuos maderables mediante pirólisis rápida y captura de carbono."
            bloque_sugerido: "Pomodoro 45/10 • Rutas pirolíticas"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Digestión Anaerobia, Cinética de Biogás y Upgrading a Biometano"
            objetivo: "Dimensionar biodigestores calculando TRH, carga orgánica volátil y producción de CH4."
            concepto_clave_latex: "V_{\\text{dig}} = Q_{\\text{sustrato}}\\cdot \\text{TRH} \\quad ; \\quad B_0\\,[ \\text{m}^3\\text{CH}_4/\\text{kg SV}]"
            ejemplo: "Biodigestor tubular/laguna cubierta en planta extractora o granja porcina."
            bloque_sugerido: "Pomodoro 50/10 • Diseño biodigestor"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Biocombustibles Líquidos (Bioetanol, Biodiésel, SAF) y Sostenibilidad"
            objetivo: "Evaluar rutas de fermentación, transesterificación e impacto neto de ciclo de vida."
            concepto_clave_latex: "\\text{Triglicérido} + 3\\text{CH}_3\\text{OH} \\xrightarrow{\\text{KOH}} 3\\text{FAME (Biodiésel)} + \\text{Glicerol}"
            ejemplo: "Balance energético y reducción de GEI en mezclas B10 y E10 en transporte."
            bloque_sugerido: "Taller 45 min • Biocombustibles 1G/2G"
      - codigo: "06021848"
        nombre: "Energía Eólica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Física Atmosférica, Capa Límite y Perfil Vertical del Viento"
            objetivo: "Extrapolar velocidades de viento a altura de buje mediante ley logarítmica y potencial."
            concepto_clave_latex: "v(z) = v_{\\text{ref}}\\left(\\frac{z}{z_{\\text{ref}}}\\right)^\\alpha \\quad ; \\quad v(z) = \\frac{u_*}{\\kappa}\\ln\\left(\\frac{z}{z_0}\\right)"
            ejemplo: "Extrapolación de mediciones de torre anemométrica de 40 m a buje de 120 m."
            bloque_sugerido: "Pomodoro 45/10 • Cortante vertical"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Estadística Eólica, Weibull y Producción Anual de Energía (AEP)"
            objetivo: "Integrar la distribución de probabilidad del viento con la curva de potencia."
            concepto_clave_latex: "\\text{AEP} = 8760\\int_{v_{\\text{in}}}^{v_{\\text{out}}} P(v)\\,f(v)\\,dv"
            ejemplo: "Cálculo numérico del AEP y factor de capacidad para turbina de 4.5 MW."
            bloque_sugerido: "Pomodoro 50/10 • Integración AEP"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Teoría de Disco Actuador y Límite Aerodinámico de Betz"
            objetivo: "Demostrar el factor de inducción axial óptimo a = 1/3 y Cp,máx = 16/27."
            concepto_clave_latex: "C_p = 4a(1-a)^2 \\implies C_{p,\\max} = \\frac{16}{27} \\approx 0.5926 \\quad ; \\quad C_T = 4a(1-a)"
            ejemplo: "Fuerza de empuje axial y potencia máxima extraíble sobre un rotor de 150 m."
            bloque_sugerido: "Pomodoro 50/10 • Demostración de Betz"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Aerodinámica de Palas (BEM), TSR y Perfiles Sustentadores"
            objetivo: "Relacionar relación de velocidad de punta λ, ángulo de paso β, sustentación y arrastre."
            concepto_clave_latex: "\\lambda = \\frac{\\omega R}{v_\\infty} \\quad ; \\quad dL = \\frac{1}{2}\\rho w^2 c\\,C_L(\\alpha)\\,dr"
            ejemplo: "Diseño de torsión a lo largo del radio mediante Blade Element Momentum (BEM)."
            bloque_sugerido: "Práctica 50 min • Triángulos BEM"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Regiones de Operación y Control MPPT / Pitch de Turbinas"
            objetivo: "Controlar par óptimo k·ω² bajo velocidad nominal y ángulo de pitch sobre nominal."
            concepto_clave_latex: "\\tau_{\\text{ref}} = K_{\\text{ópt}}\\omega_r^2\\;\\;(v < v_{\\text{nom}}) \\quad ; \\quad P = P_{\\text{nom}}\\;\\;(\\text{Pitch activo } v \\ge v_{\\text{nom}})"
            ejemplo: "Transición suave entre región de carga parcial y regulación de potencia nominal."
            bloque_sugerido: "Pomodoro 45/10 • Curva P-v y control"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Topologías Electromecánicas Tipo 1 a Tipo 4 (DFIG y PMSG)"
            objetivo: "Comparar trenes con multiplicadora y accionamiento directo con convertidor Full-Scale."
            concepto_clave_latex: "f_{\\text{red}} = \\text{const} \\xleftarrow{\\text{Back-to-Back PWM}} f_{\\text{gen}}(\\omega_r)"
            ejemplo: "Capacidad de soporte de huecos de tensión (LVRT) en turbinas Tipo 3 y Tipo 4."
            bloque_sugerido: "Práctica 45 min • Topologías IEC"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Efecto Estela (Wake), Micrositing y Diseño de Parques Eólicos"
            objetivo: "Minimizar pérdidas aerodinámicas entre filas usando el modelo de estela de Jensen."
            concepto_clave_latex: "v_w(x) = v_0\\left[1 - \\frac{1 - \\sqrt{1 - C_T}}{(1 + 2k_w x/D)^2}\\right]"
            ejemplo: "Distanciamiento óptimo 7D × 4D según dirección predominante de vientos alisios."
            bloque_sugerido: "Laboratorio 50 min • Modelo de Jensen"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Energía Eólica Offshore, Cimentaciones y Viabilidad Económica"
            objetivo: "Evaluar parques marinos fijos (monopilotaje) y flotantes frente al Caribe colombiano."
            concepto_clave_latex: "\\text{LCOE}_{\\text{offshore}} = \\frac{\\text{CAPEX}\\cdot\\text{CRF} + \\text{OPEX}}{\\text{AEP}_{\\text{neto}}}"
            ejemplo: "Análisis del potencial eólico marino frente a Atlántico, Bolívar y Magdalena."
            bloque_sugerido: "Taller 45 min • Eólica offshore Caribe"
      - codigo: "06021847"
        nombre: "Energía Geotérmica"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Gradiente Geotérmico, Flujo de Calor Terrestre y Yacimientos"
            objetivo: "Clasificar sistemas hidrotermales de baja, media y alta entalpía y roca caliente seca."
            concepto_clave_latex: "q'' = -k_r\\frac{dT}{dz} \\quad ; \\quad \\frac{dT}{dz}_{\\text{normal}} \\approx 25\\text{--}30\\text{ }^\\circ\\text{C/km}"
            ejemplo: "Anomalías geotérmicas volcánicas en el Macizo Colombiano (Nevado del Ruiz / Azufral)."
            bloque_sugerido: "Pomodoro 45/10 • Gradiente térmico"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Exploración Geotérmica: Geoquímica, Geofísica y Geotermómetros"
            objetivo: "Estimar temperaturas profundas de reservorio mediante geotermómetros de sílice y Na-K."
            concepto_clave_latex: "T_{\\text{SiO}_2}\\,[ ^\\circ\\text{C}] = \\frac{1309}{5.19 - \\log_{10}C_{\\text{SiO}_2}} - 273.15"
            ejemplo: "Exploración magnetotelúrica y muestreo geoquímico de manantiales termales."
            bloque_sugerido: "Práctica 45 min • Geotermometría"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Perforación de Pozos, Flujo Bifásico y Curvas de Productividad"
            objetivo: "Analizar curvas de descarga presión de cabezal vs. flujo másico en pozos productores."
            concepto_clave_latex: "\\dot{m} = PI\\cdot(\\bar{P}_{\\text{res}} - P_{wf}) \\quad ; \\quad h_{\\text{mezcla}} = (1-x)h_f + x\\,h_g"
            ejemplo: "Ensayo de producción e inyectividad en doblete geotérmico profundo."
            bloque_sugerido: "Pomodoro 45/10 • Curva de cabezal"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Plantas de Vapor Seco (Dry Steam) y Simple/Doble Flash"
            objetivo: "Optimizar la presión del separador ciclónico para maximizar potencia específica."
            concepto_clave_latex: "x_{\\text{sep}} = \\frac{h_1 - h_{f,\\text{sep}}}{h_{fg,\\text{sep}}} \\quad ; \\quad T_{\\text{sep,ópt}} \\approx \\frac{T_{\\text{res}} + T_{\\text{cond}}}{2}"
            ejemplo: "Determinación termodinámica de la presión óptima de flash para salmuera a 240 °C."
            bloque_sugerido: "Pomodoro 50/10 • Optimización Flash"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Ciclos Binarios ORC y Ciclo Kalina para Media Entalpía"
            objetivo: "Seleccionar fluidos orgánicos (isobutano, R245fa, mezcla NH3-H2O) y efectividad de pellizco."
            concepto_clave_latex: "\\dot{W}_{\\text{neto,ORC}} = \\dot{m}_{\\text{wf}}[(h_3 - h_4) - (h_2 - h_1)] \\quad ; \\quad \\eta_{II} = \\frac{\\dot{W}_{\\text{neto}}}{\\dot{m}_g e_{\\text{geo}}}"
            ejemplo: "Generación binaria ORC de 5 MW aprovechando coproducción de campos petroleros."
            bloque_sugerido: "Pomodoro 50/10 • Ciclo ORC"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas Geotérmicos Mejorados (EGS) y Reinyección"
            objetivo: "Modelar sostenibilidad térmica del reservorio y prevención de subsidencia o enfriamiento."
            concepto_clave_latex: "t_{\\text{ruptura térmica}} = f(Q_{\\text{reiny}},\\; d_{\\text{pozos}},\\; \\phi_r)"
            ejemplo: "Diseño de reinyección de salmuera para mantener presión del acuífero geotérmico."
            bloque_sugerido: "Práctica 45 min • Gestión de reservorio"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Usos Directos del Calor Geotérmico y Bombas GHP"
            objetivo: "Dimensionar intercambiadores enterrados y bombas de calor geotérmicas someras."
            concepto_clave_latex: "\\text{COP}_{\\text{GHP}} = \\frac{\\dot{Q}_{\\text{climatización}}}{\\dot{W}_{\\text{comp}}} \\approx 4.0\\text{--}5.5"
            ejemplo: "Aprovechamiento en cascada (Líndal): electricidad, secado agrícola e invernaderos."
            bloque_sugerido: "Pomodoro 45/10 • Diagrama de Líndal"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Incrustación (Scaling), Gases No Condensables y Evaluación Económica"
            objetivo: "Mitigar precipitación de sílice/calcita, emisiones de H2S y riesgo exploratorio."
            concepto_clave_latex: "\\text{NPV} = -\\text{CAPEX}_{\\text{perf}} + \\sum_{t=1}^{N}\\frac{CF_t}{(1+r)^t}"
            ejemplo: "Mitigación financiera del riesgo de perforación en proyectos geotérmicos."
            bloque_sugerido: "Taller 45 min • Química y finanzas geo"
      - codigo: "06021849"
        nombre: "Energía Mareomotriz"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Astronomía de Mareas, Armónicos y Rango Mareal"
            objetivo: "Predecir elevaciones de marea astronómica (vivientes y muertas) mediante constituyentes M2 y S2."
            concepto_clave_latex: "\\eta(t) = \\eta_0 + \\sum_{k} A_k\\cos(\\omega_k t - \\phi_k) \\quad ; \\quad E_{\\text{embalse}} = \\frac{1}{2}\\rho g A R^2"
            ejemplo: "Comparación del rango mareal del Pacífico colombiano (~4 m) frente al Caribe (<0.6 m)."
            bloque_sugerido: "Pomodoro 45/10 • Potencial mareal R²"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Presas de Marea (Tidal Barrage) y Lagunas Mareomotrices"
            objetivo: "Evaluar generación en vaciado, llenado y doble efecto con turbinas bulbo reversibles."
            concepto_clave_latex: "P_{\\text{media}} = \\frac{\\eta\\,\\rho g A R^2}{2 T_{\\text{ciclo}}}"
            ejemplo: "Operación bidireccional tipo La Rance / Sihwa Lake y bombeo en pleamar."
            bloque_sugerido: "Práctica 45 min • Ciclos de embalse"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Corrientes de Marea e Hidrodinámica de Turbinas HKT"
            objetivo: "Calcular densidad de potencia cinética marina y riesgo de cavitación en rotores sumergidos."
            concepto_clave_latex: "P_{\\text{HKT}} = \\frac{1}{2}\\rho_{\\text{mar}} C_p A v^3 \\quad (\\rho_{\\text{mar}} \\approx 1025\\text{ kg/m}^3)"
            ejemplo: "Comparación de densidad energética del agua de mar (830× mayor que el aire)."
            bloque_sugerido: "Pomodoro 50/10 • Turbinas hidrocinéticas"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Mecánica de Olas Oceánicas y Potencial Undimotriz"
            objetivo: "Estimar flujo de potencia por metro de cresta en aguas profundas a partir de Hs y Te."
            concepto_clave_latex: "J_{\\text{ola}} = \\frac{\\rho g^2}{64\\pi} H_s^2 T_e \\approx 0.49\\,H_s^2 T_e \\quad [\\text{kW/m}]"
            ejemplo: "Evaluación del recurso de oleaje mediante matrices de dispersión (Hs, Te)."
            bloque_sugerido: "Pomodoro 50/10 • Flujo undimotriz"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Convertidores de Oleaje (WEC): OWC, Atenuadores y Boyas"
            objetivo: "Analizar resonancia hidrodinámica, turbinas Wells bidireccionales y sistemas PTO."
            concepto_clave_latex: "(m + m_a)\\ddot{z} + (b_{\\text{rad}} + b_{\\text{PTO}})\\dot{z} + \\rho g S_w z = F_{\\text{exc}}(t)"
            ejemplo: "Sintonización de amortiguamiento óptimo del Power Take-Off (PTO) con la ola incidente."
            bloque_sugerido: "Práctica 50 min • Columna de agua OWC"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Conversión de Energía Térmica Oceánica (OTEC)"
            objetivo: "Modelar ciclos cerrados de amoníaco e híbridos con desalinización usando ΔT ≥ 20 °C."
            concepto_clave_latex: "\\eta_{\\text{Carnot,OTEC}} = 1 - \\frac{T_{\\text{prof (4 °C)}}}{T_{\\text{sup (28 °C)}}} \\approx 8.0\\% \\quad (\\eta_{\\text{neta}} \\approx 3\\text{--}4\\%)"
            ejemplo: "Potencial OTEC tropical en aguas profundas cercanas a la costa de Santa Marta y San Andrés."
            bloque_sugerido: "Pomodoro 45/10 • Ciclo OTEC tropical"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Gradiente Salino (Energía Azul): PRO y Electrodiálisis Inversa (RED)"
            objetivo: "Cuantificar presión osmótica y densidad de potencia en desembocaduras fluviales."
            concepto_clave_latex: "\\Delta\\Pi = i R T (C_{\\text{mar}} - C_{\\text{río}}) \\approx 26\\text{--}28\\text{ bar}"
            ejemplo: "Potencial de energía osmótica en estuarios como Bocas de Ceniza (Río Magdalena)."
            bloque_sugerido: "Pomodoro 45/10 • Ósmosis retardada PRO"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Ambiente Marino, Biofouling, Cables Submarinos e Impacto Ambiental"
            objetivo: "Diseñar protección anticorrosiva, anclajes e interconexión eléctrica submarina."
            concepto_clave_latex: "E_{\\text{ánodo}} < E_{\\text{cátodo}} \\quad ; \\quad i_{\\text{prot}} \\ge 100\\text{ mA/m}^2"
            ejemplo: "Evaluación ambiental marina, mamíferos acuáticos y logística O&M costa afuera."
            bloque_sugerido: "Taller 45 min • Ingeniería oceánica"
      - codigo: "03021816"
        nombre: "Mecánica de Fluidos"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Propiedades de los Fluidos, Viscosidad de Newton y Tensión Superficial"
            objetivo: "Relacionar esfuerzo cortante con gradiente de velocidad en fluidos newtonianos y no newtonianos."
            concepto_clave_latex: "\\tau = \\mu\\frac{du}{dy} \\quad ; \\quad \\Delta P_{\\text{gota}} = \\frac{4\\sigma_s}{D}"
            ejemplo: "Esfuerzo viscoso en películas lubricantes de cojinetes hidrodinámicos de turbinas."
            bloque_sugerido: "Pomodoro 45/10 • Ley de viscosidad"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Estática de Fluidos, Manometría, Fuerzas Sumergidas y Flotación"
            objetivo: "Calcular fuerzas hidrostáticas y centros de presión sobre superficies planas/curvas y estabilidad."
            concepto_clave_latex: "F_R = \\rho g h_c A \\quad ; \\quad y_R = y_c + \\frac{I_{xc}}{y_c A} \\quad ; \\quad F_B = \\rho_f g V_{\\text{desp}}"
            ejemplo: "Estabilidad metacéntrica de una plataforma eólica marina flotante."
            bloque_sugerido: "Pomodoro 50/10 • Compuertas y flotación"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Cinemática de Fluidos: Descripciones Lagraniana/Euleriana y Vorticidad"
            objetivo: "Analizar líneas de corriente, tensor velocidad de deformación y flujo irrotacional."
            concepto_clave_latex: "\\frac{D\\vec{V}}{Dt} = \\frac{\\partial\\vec{V}}{\\partial t} + (\\vec{V}\\cdot\\nabla)\\vec{V} \\quad ; \\quad \\vec{\\omega} = \\nabla\\times\\vec{V}"
            ejemplo: "Campo de aceleración convectiva en una tobera convergente estacionaria."
            bloque_sugerido: "Práctica 45 min • Derivada material"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Teorema de Transporte de Reynolds y Conservación Integral"
            objetivo: "Aplicar balances integrales de masa, cantidad de movimiento lineal/angular y energía."
            concepto_clave_latex: "\\sum\\vec{F}_{\\text{VC}} = \\frac{\\partial}{\\partial t}\\int_{\\text{VC}}\\rho\\vec{V}\\,d\\mathcal{V} + \\int_{\\text{SC}}\\rho\\vec{V}(\\vec{V}\\cdot\\hat{n})\\,dA"
            ejemplo: "Fuerza de reacción sobre codos reductores de alta presión en centrales hidráulicas."
            bloque_sugerido: "Pomodoro 50/10 • Momentum en VC"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Ecuaciones Diferenciales de Continuidad y Navier-Stokes"
            objetivo: "Resolver flujos viscosos laminares exactos (Couette y Hagen-Poiseuille)."
            concepto_clave_latex: "\\rho\\frac{D\\vec{V}}{Dt} = -\\nabla P + \\rho\\vec{g} + \\mu\\nabla^2\\vec{V} \\quad ; \\quad Q_{\\text{Pois}} = \\frac{\\pi D^4 \\Delta P}{128\\mu L}"
            ejemplo: "Perfil parabólico de velocidades en microcanales de enfriamiento de baterías."
            bloque_sugerido: "Pomodoro 50/10 • Navier-Stokes"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Análisis Dimensional, Teorema Pi de Buckingham y Semejanza"
            objetivo: "Construir grupos adimensionales (Re, Fr, Eu, Ma) para escalar modelos en túnel o canal."
            concepto_clave_latex: "\\Pi_1 = \\phi(\\Pi_2, \\Pi_3, \\dots, \\Pi_{n-k}) \\quad ; \\quad \\text{Re}_m = \\text{Re}_p,\\;\\; \\text{Fr}_m = \\text{Fr}_p"
            ejemplo: "Escalamiento dinámico 1:15 de un vertedero o rotor hidrocinético en laboratorio."
            bloque_sugerido: "Práctica 45 min • Teorema Pi"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Flujo Interno Viscoso, Diagrama de Moody y Redes de Tuberías"
            objetivo: "Dimensionar sistemas de tuberías en serie/paralelo con pérdidas mayores y accesorios."
            concepto_clave_latex: "h_L = \\left(f\\frac{L}{D} + \\sum K_L\\right)\\frac{V^2}{2g} \\quad ; \\quad \\frac{1}{\\sqrt{f}} = -2\\log_{10}\\left(\\frac{\\varepsilon/D}{3.7} + \\frac{2.51}{\\text{Re}\\sqrt{f}}\\right)"
            ejemplo: "Cálculo iterativo de Colebrook-White y punto de operación bomba-sistema."
            bloque_sugerido: "Pomodoro 50/10 • Redes y Moody"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Capa Límite Externa, Sustentación, Arrastre y Flujo Compresible"
            objetivo: "Evaluar separación de capa límite, fuerzas aerodinámicas y número de Mach en toberas."
            concepto_clave_latex: "F_D = \\frac{1}{2}\\rho V_\\infty^2 A C_D \\quad ; \\quad \\text{Ma} = \\frac{V}{\\sqrt{\\gamma R T}}"
            ejemplo: "Flujo estrangulado (Ma = 1) en válvulas de vapor y arrastre sobre seguidores solares."
            bloque_sugerido: "Taller 50 min • Capa límite y Mach"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Metodología de Simulación Multi-Dominio de Sistemas Energéticos"
            objetivo: "Integrar modelos estacionarios, cuasi-estáticos horarios (8760 h) y transitorios dinámicos."
            concepto_clave_latex: "\\vec{y}(t_k) = \\mathcal{M}(\\vec{x}(t_k), \\vec{u}(t_k), \\vec{\\theta}) \\quad (\\Delta t = 1\\text{ s a } 1\\text{ h})"
            ejemplo: "Selección de horizonte y paso temporal entre PVsyst/HOMER, OpenDSS y Simulink."
            bloque_sugerido: "Laboratorio 45 min • Arquitecturas de simulación"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Modelado de Recursos Meteorológicos (TMY) y Perfiles Sintéticos"
            objetivo: "Procesar Año Meteorológico Típico (NSRDB/ERA5) e incertidumbre P50/P90."
            concepto_clave_latex: "E_{P90} = E_{P50}(1 - 1.2816\\,\\sigma_{\\text{total}})"
            ejemplo: "Generación de reporte bancable P50/P90 de producción solar y eólica."
            bloque_sugerido: "Laboratorio 50 min • Datos ERA5 y P90"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Simulación y Dimensionamiento Óptimo de Microrredes Híbridas"
            objetivo: "Minimizar el costo neto presente NPC combinando PV, eólica, BESS y respaldo."
            concepto_clave_latex: "\\min \\text{NPC} = \\frac{C_{\\text{anual,tot}}}{\\text{CRF}(i, N)} \\;\\;\\text{s.t.}\\;\\; \\text{LPSP} \\le \\varepsilon_{\\max}"
            ejemplo: "Optimización tecnoeconómica tipo HOMER para isla energética 100% renovable."
            bloque_sugerido: "Laboratorio 50 min • Optimización microrred"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Simulación de Plantas Térmicas y Procesos en Estado Estacionario"
            objetivo: "Cerrar balances de masa, energía y exergía con recirculaciones y pinch en diagramas de flujo."
            concepto_clave_latex: "\\vec{R}(\\vec{z}) = \\vec{z} - \\vec{G}(\\vec{z}) = \\vec{0} \\quad ; \\quad \\|\\vec{R}\\| < 10^{-6}"
            ejemplo: "Simulación paramétrica de un ciclo combinado con recuperación HRSG."
            bloque_sugerido: "Práctica 50 min • Flowsheet térmico"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Flujo de Potencia AC (Newton-Raphson) y Simulación de Redes"
            objetivo: "Resolver perfiles de tensión y pérdidas técnicas en alimentadores con generación distribuida."
            concepto_clave_latex: "\\begin{bmatrix}\\Delta\\vec{P} \\\\ \\Delta\\vec{Q}\\end{bmatrix} = \\begin{bmatrix}J_{P\\theta} & J_{PV} \\\\ J_{Q\\theta} & J_{QV}\\end{bmatrix}\\begin{bmatrix}\\Delta\\vec{\\theta} \\\\ \\Delta\\vec{V}\\end{bmatrix}"
            ejemplo: "Análisis de hosting capacity fotovoltaico en un circuito de 13.8 kV."
            bloque_sugerido: "Laboratorio 50 min • Flujo de carga NR"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Simulación Térmica Dinámica de Edificaciones (BES)"
            objetivo: "Modelar ganancias solares, envolvente constructiva y cargas horarias HVAC."
            concepto_clave_latex: "C_z\\frac{dT_z}{dt} = \\sum_{i} U_i A_i(T_{s,i} - T_z) + \\dot{Q}_{\\text{int}} + \\dot{Q}_{\\text{solar}} - \\dot{Q}_{\\text{HVAC}}"
            ejemplo: "Reducción del 28% de carga térmica mediante vidrios de control solar en clima cálido."
            bloque_sugerido: "Laboratorio 45 min • Envolvente térmica"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Introducción a Dinámica de Fluidos Computacional (CFD) Aplicada"
            objetivo: "Configurar mallado, modelos de turbulencia RANS (k-ε / k-ω SST) y convergencia."
            concepto_clave_latex: "\\text{Courant } \\text{Co} = \\frac{u\\,\\Delta t}{\\Delta x} \\le 1 \\quad ; \\quad y^+ = \\frac{\\rho u_\\tau y}{\\mu}"
            ejemplo: "Simulación CFD de enfriamiento por aire forzado en un gabinete de baterías BESS."
            bloque_sugerido: "Laboratorio 50 min • Independencia de malla"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Análisis de Sensibilidad, Monte Carlo y Gemelos Digitales"
            objetivo: "Propagar incertidumbre paramétrica y calibrar gemelos digitales con telemetría real."
            concepto_clave_latex: "\\text{Var}(Y) \\implies S_i = \\frac{\\text{Var}_{X_i}(E_{\\sim i}[Y|X_i])}{\\text{Var}(Y)} \\quad (\\text{Índices de Sobol})"
            ejemplo: "Simulación Monte Carlo de 5,000 escenarios sobre el LCOE y gemelo digital operativo."
            bloque_sugerido: "Taller 50 min • Monte Carlo y Digital Twin"
      - codigo: "04031828"
        nombre: "Energy Market"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Microeconomía de la Electricidad, Oferta, Demanda y Bienestar"
            objetivo: "Analizar elasticidad de la demanda eléctrica, excedente del consumidor y fallas de mercado."
            concepto_clave_latex: "\\max \\sum_d U_d(q_d) - \\sum_g C_g(q_g) \\;\\;\\text{s.t.}\\;\\; \\sum_g q_g = \\sum_d q_d"
            ejemplo: "Formación del equilibrio competitivo y precio sombra de la energía."
            bloque_sugerido: "Pomodoro 45/10 • Equilibrio de mercado"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Arquitectura de Mercados Mayoristas (MEM Colombia / Pool / Nodal)"
            objetivo: "Comparar despacho ideal uninodal frente a precios marginales locales (LMP) nodales."
            concepto_clave_latex: "\\text{LMP}_i = \\lambda_{\\text{energía}} + \\lambda_{\\text{pérdidas},i} + \\lambda_{\\text{congestión},i}"
            ejemplo: "Diferencia entre precio de bolsa nacional y reconciliaciones por restricciones en Colombia."
            bloque_sugerido: "Pomodoro 50/10 • Bolsa XM y LMP"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Formación del Precio Marginal (Merit Order) y Efecto Renovable"
            objetivo: "Construir la curva agregada de oferta por orden de mérito y efecto canibalización solar/eólico."
            concepto_clave_latex: "P_{\\text{clearing}} = MC_{\\text{unidad marginal}} \\quad (\\text{Renovables: } MC \\approx 0)"
            ejemplo: "Desplazamiento de plantas térmicas costosas durante horas de máxima irradiancia."
            bloque_sugerido: "Práctica 45 min • Curva Merit Order"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Contratos Bilaterales PPA (Pay-as-Produced vs. Baseload) y Subastas"
            objetivo: "Estructurar contratos de compraventa de energía a largo plazo y cobertura de riesgo de precio."
            concepto_clave_latex: "R_{\\text{generador}} = Q_{\\text{PPA}} P_{\\text{PPA}} + (Q_{\\text{real}} - Q_{\\text{PPA}})P_{\\text{bolsa}}"
            ejemplo: "Exposición al riesgo de bolsa en horas nocturnas de un PPA solar 24/7."
            bloque_sugerido: "Taller 50 min • Modelado financiero PPA"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Cargo por Confiabilidad, ENFICC y Precio de Escasez"
            objetivo: "Comprender el mecanismo colombiano de remuneración de energía firme ante fenómenos de El Niño."
            concepto_clave_latex: "\\text{OEF} \\le \\text{ENFICC} \\quad ; \\quad P_{\\text{bolsa}} > P_{\\text{escasez}} \\implies \\text{Activación OEF}"
            ejemplo: "Cálculo conceptual de ENFICC para plantas hidráulicas, térmicas y solares."
            bloque_sugerido: "Pomodoro 45/10 • Cargo por Confiabilidad"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Servicios Complementarios (Ancillary Services) y Mercados Intradiarios"
            objetivo: "Valorizar regulación primaria/secundaria de frecuencia (AGC), reserva rodante e inercia."
            concepto_clave_latex: "\\Delta f \\implies \\Delta P = -\\frac{1}{R_{\\text{droop}}}\\frac{\\Delta f}{f_0}\\,P_{\\text{nom}}"
            ejemplo: "Apilamiento de ingresos (revenue stacking) de baterías BESS: arbitraje + regulación AGC."
            bloque_sugerido: "Práctica 45 min • Arbitraje BESS"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Mercados de Gas Natural, Hidrógeno, Certificados I-REC y Carbono"
            objetivo: "Integrar ingresos por atributos ambientales certificados y comercio de emisiones ETS."
            concepto_clave_latex: "P_{\\text{efectivo}} = P_{\\text{energía}} + FE_{\\text{red}}\\cdot P_{\\text{I-REC / CO}_2}"
            ejemplo: "Certificación y monetización de certificados de energía renovable I-REC en Colombia."
            bloque_sugerido: "Pomodoro 45/10 • Certificados verdes"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Poder de Mercado, Índice Herfindahl-Hirschman (HHI) y Gestión VaR"
            objetivo: "Detectar concentración oligopólica (HHI, Índice de Lerner) y medir Valor en Riesgo."
            concepto_clave_latex: "\\text{HHI} = \\sum_{i=1}^{N} s_i^2 \\quad ; \\quad L_i = \\frac{P - MC_i}{P} \\quad ; \\quad \\text{VaR}_\\alpha"
            ejemplo: "Evaluación de concentración del parque generador y cobertura financiera hidro-térmica."
            bloque_sugerido: "Taller 45 min • Índices HHI y riesgo"
      - codigo: "05011832"
        nombre: "Formulación de Proyectos"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Identificación del Problema, Marco Lógico y Árbol de Objetivos"
            objetivo: "Estructurar proyectos energéticos alineados con metodologías PMI, MGA e indicadores SMART."
            concepto_clave_latex: "\\text{Causas} \\to \\text{Problema Central} \\to \\text{Efectos} \\implies \\text{Medios} \\to \\text{Propósito} \\to \\text{Fines}"
            ejemplo: "Formulación en Matriz de Marco Lógico (MML) de electrificación solar comunitaria."
            bloque_sugerido: "Taller 45 min • Matriz de Marco Lógico"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Estudio de Mercado, Proyección de Demanda y Tarifas"
            objetivo: "Proyectar demanda energética e ingresos tarifarios a lo largo del horizonte de evaluación."
            concepto_clave_latex: "D_t = D_0(1 + g_D)^t \\quad ; \\quad I_t = E_{\\text{vendida},t}\\cdot P_{0}(1 + \\pi_e)^t"
            ejemplo: "Escenarios pesimista, base y optimista de demanda para un distrito térmico."
            bloque_sugerido: "Pomodoro 45/10 • Proyección de demanda"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Estudio Técnico: Localización, Tamaño Óptimo e Ingeniería Básica"
            objetivo: "Determinar escala óptima, tecnología, logística constructiva y cronograma EPC."
            concepto_clave_latex: "C_{\\text{escala}}(S_2) = C(S_1)\\left(\\frac{S_2}{S_1}\\right)^{0.6\\text{--}0.8}"
            ejemplo: "Economías de escala en plantas solares y subestaciones de interconexión."
            bloque_sugerido: "Práctica 45 min • Factor de escala"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Estructura de Costos CAPEX, OPEX, Depreciación e Impuestos"
            objetivo: "Construir presupuestos detallados incluyendo incentivos fiscales Ley 1715/2099."
            concepto_clave_latex: "FC_t = (\\text{EBITDA}_t - D_t)(1 - \\tau_{\\text{renta}}) + D_t - \\Delta\\text{KT}_t - \\text{CAPEX}_t"
            ejemplo: "Impacto en flujo de caja libre de la depreciación acelerada a 3 años y deducción 50%."
            bloque_sugerido: "Pomodoro 50/10 • Flujo de caja libre"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Costo de Capital (WACC) y Matemáticas Financieras Aplicadas"
            objetivo: "Calcular tasa de descuento ponderada ajustada por riesgo país y estructura deuda/equity."
            concepto_clave_latex: "\\text{WACC} = \\frac{E}{D+E}k_e + \\frac{D}{D+E}k_d(1-\\tau) \\quad ; \\quad k_e = r_f + \\beta(r_m - r_f) + r_p"
            ejemplo: "Determinación del WACC real y nominal para proyectos de infraestructura energética."
            bloque_sugerido: "Pomodoro 45/10 • Cálculo WACC"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Indicadores de Rentabilidad: VPN, TIR, B/C, Payback y LCOE"
            objetivo: "Evaluar viabilidad financiera privada y costo nivelado de energía."
            concepto_clave_latex: "\\text{VPN} = \\sum_{t=0}^{N}\\frac{FC_t}{(1+\\text{WACC})^t} > 0 \\quad ; \\quad \\text{LCOE} = \\frac{\\sum \\frac{I_t + M_t}{(1+r)^t}}{\\sum \\frac{E_t}{(1+r)^t}}"
            ejemplo: "Modelo financiero completo a 25 años con degradación anual de paneles del 0.45%."
            bloque_sugerido: "Laboratorio 50 min • VPN, TIR y LCOE"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Project Finance, Apalancamiento y Ratio de Cobertura DSCR"
            objetivo: "Dimensionar deuda bancaria sin recurso verificando cobertura del servicio de la deuda."
            concepto_clave_latex: "\\text{DSCR}_t = \\frac{\\text{CFADS}_t}{\\text{Principal}_t + \\text{Intereses}_t} \\ge 1.25\\text{--}1.35"
            ejemplo: "Esculpido de deuda (debt sculpting) para un parque solar con contrato PPA a 15 años."
            bloque_sugerido: "Práctica 50 min • Cobertura DSCR"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Evaluación Económica/Social (MGA Regalías) y Análisis de Riesgos"
            objetivo: "Aplicar precios cuenta (RPC), tasa social de descuento y diagramas tornado."
            concepto_clave_latex: "\\text{VPN}_{\\text{social}} = \\sum_{t=0}^{N}\\frac{B_{\\text{soc},t} - C_{\\text{soc},t}}{(1 + \\text{TSD})^t}\\quad (\\text{TSD Colombia} = 9\\%)"
            ejemplo: "Formulación bajo Metodología General Ajustada (MGA) para fondos FENOGE / Regalías."
            bloque_sugerido: "Taller 45 min • MGA y diagrama tornado"
      - codigo: "05011831"
        nombre: "Metodología de la Investigación"
        creditos: 2
        obligatoria: true
        categoria: "FORMACION_GENERAL"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Epistemología de la Ingeniería y Paradigmas de Investigación"
            objetivo: "Diferenciar investigación básica, aplicada y desarrollo tecnológico (escala TRL 1–9)."
            concepto_clave_latex: "1 \\le \\text{TRL} \\le 9 \\quad ; \\quad \\text{TRL}_{k+1} > \\text{TRL}_k"
            ejemplo: "Clasificación del nivel de madurez tecnológica TRL de proyectos de hidrógeno y almacenamiento."
            bloque_sugerido: "Lectura 40 min • Escala NASA/ Minciencias TRL"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Planteamiento del Problema, Pregunta Científica e Hipótesis"
            objetivo: "Formular preguntas de investigación acotadas, variables dependientes/independientes e hipótesis."
            concepto_clave_latex: "H_0: \\beta_i = 0 \\quad \\text{vs.} \\quad H_1: \\beta_i \\neq 0 \\quad ; \\quad p < 0.05"
            ejemplo: "Delimitación espacial, temporal y conceptual de una tesis en Ingeniería Energética."
            bloque_sugerido: "Taller 45 min • Pregunta y objetivos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Vigilancia Tecnológica, Bibliometría y Estado del Arte (PRISMA)"
            objetivo: "Ejecutar ecuaciones booleanas en Scopus/Web of Science y síntesis sistemática."
            concepto_clave_latex: "Q_{\\text{Scopus}} = \\text{TITLE-ABS-KEY}(\\text{``microgrid''} \\land (\\text{``BESS''} \\lor \\text{``hydrogen''}))"
            ejemplo: "Construcción de red bibliométrica e identificación del vacío de conocimiento (research gap)."
            bloque_sugerido: "Laboratorio 45 min • Búsqueda booleana"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Marco Teórico, Conceptual y Operacionalización de Variables"
            objetivo: "Conectar leyes físicas fundamentales con indicadores medibles e instrumentos."
            concepto_clave_latex: "Y = \\alpha + \\sum_{i=1}^p \\beta_i X_i + \\varepsilon \\quad ; \\quad \\varepsilon \\sim \\mathcal{N}(0, \\sigma^2)"
            ejemplo: "Matriz de operacionalización de variables para evaluar desempeño de colectores híbridos."
            bloque_sugerido: "Práctica 40 min • Matriz de variables"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Diseño Experimental, Factorial (DOE) y Tamaño de Muestra"
            objetivo: "Planificar experimentos controlados, aleatorización, réplicas y diseños factoriales 2^k."
            concepto_clave_latex: "N_{\\text{corridas}} = r\\cdot 2^k \\quad ; \\quad n = \\left(\\frac{z_{\\alpha/2}\\sigma}{E_{\\max}}\\right)^2"
            ejemplo: "Diseño factorial 2³ (flujo, inclinación, espesor) con réplicas para optimizar un captador."
            bloque_sugerido: "Pomodoro 50/10 • Diseño factorial 2^k"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Recolección de Datos, Validez, Confiabilidad y Análisis ANOVA"
            objetivo: "Validar instrumentos y ejecutar análisis de varianza para separar efectos principales e interacciones."
            concepto_clave_latex: "F = \\frac{MS_{\\text{tratamiento}}}{MS_{\\text{error}}} \\quad ; \\quad SS_{\\text{total}} = SS_{\\text{trat}} + SS_{\\text{error}}"
            ejemplo: "Interpretación de tabla ANOVA sobre tres configuraciones de turbuladores térmicos."
            bloque_sugerido: "Práctica 45 min • ANOVA experimental"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Ética de la Investigación, Propiedad Intelectual y Patentes"
            objetivo: "Cumplir integridad científica, reproducibilidad de datos abiertos y criterios de patentabilidad."
            concepto_clave_latex: "\\text{IPC} \\in \\text{OMPI} \\quad ; \\quad \\text{Reivindicación } 1 \\to N"
            ejemplo: "Búsqueda de antecedentes de patentes en Espacenet/USPTO antes de divulgar un prototipo."
            bloque_sugerido: "Taller 40 min • Propiedad industrial"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Estructura del Anteproyecto de Grado y Escritura Científica"
            objetivo: "Redactar un anteproyecto completo con cronograma, presupuesto, impactos y bibliografía IEEE."
            concepto_clave_latex: "\\text{Rigor} = \\text{Validez} \\times \\text{Fiabilidad} \\quad ; \\quad \\text{Cronograma} \\le T_{\\text{sem}}"
            ejemplo: "Sustentación ejecutiva de propuesta de investigación ante comité curricular."
            bloque_sugerido: "Simulacro 45 min • Defensa de anteproyecto"
      - codigo: "03011814"
        nombre: "Programación Avanzada y Aplicaciones de IA"
        creditos: 3
        obligatoria: true
        categoria: "PROGRAMACION_IA"
        color: "#0A84FF"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Programación Orientada a Objetos y Vectorización Científica"
            objetivo: "Desarrollar clases modulares y operaciones matriciales de alto rendimiento (NumPy/Pandas)."
            concepto_clave_latex: "T_{\\text{vectorizado}} \\ll T_{\\text{bucle Python}} \\quad ; \\quad \\vec{P} = \\vec{V}\\odot\\vec{I}"
            ejemplo: "Procesamiento vectorizado de 10 millones de registros de medición fasorial PMU."
            bloque_sugerido: "Laboratorio 50 min • NumPy y Pandas"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ingeniería de Características (Feature Engineering) en Series de Tiempo"
            objetivo: "Construir rezagos, ventanas móviles, codificación cíclica horaria y limpieza de outliers."
            concepto_clave_latex: "h_{\\sin} = \\sin\\left(\\frac{2\\pi h}{24}\\right),\\;\\; h_{\\cos} = \\cos\\left(\\frac{2\\pi h}{24}\\right)"
            ejemplo: "Codificación trigonométrica de hora y mes para predicción de irradiancia y carga."
            bloque_sugerido: "Laboratorio 50 min • Series temporales"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Aprendizaje Supervisado: Árboles, Random Forest y Gradient Boosting"
            objetivo: "Entrenar ensambles no lineales con validación cruzada temporal (TimeSeriesSplit)."
            concepto_clave_latex: "\\hat{y}_i = \\sum_{m=1}^{M} \\eta\\,f_m(\\vec{x}_i) \\quad ; \\quad \\text{MAE} = \\frac{1}{N}\\sum_{i=1}^{N}|y_i - \\hat{y}_i|"
            ejemplo: "Pronóstico de generación eólica a 24 horas con XGBoost/LightGBM."
            bloque_sugerido: "Laboratorio 50 min • Gradient Boosting"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Aprendizaje No Supervisado: Clustering de Perfiles y PCA"
            objetivo: "Segmentar curvas típicas de consumidores mediante K-Means y reducción PCA."
            concepto_clave_latex: "\\min \\sum_{k=1}^{K}\\sum_{\\vec{x}_i\\in C_k}\\|\\vec{x}_i - \\vec{\\mu}_k\\|_2^2"
            ejemplo: "Clasificación automática de usuarios residenciales, comerciales e industriales desde AMI."
            bloque_sugerido: "Laboratorio 45 min • Clustering de carga"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Redes Neuronales Profundas, LSTM y Transformers para Pronóstico"
            objetivo: "Modelar dependencias temporales largas en demanda eléctrica y radiación con Deep Learning."
            concepto_clave_latex: "h_t = o_t \\odot \\tanh(c_t) \\quad ; \\quad \\vec{\\theta}_{t+1} = \\vec{\\theta}_t - \\alpha\\nabla_{\\vec{\\theta}}\\mathcal{L}"
            ejemplo: "Red recurrente LSTM multi-horizonte para pronóstico horario de precios y demanda."
            bloque_sugerido: "Laboratorio 50 min • Redes LSTM"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Detección de Anomalías y Mantenimiento Predictivo (PHM)"
            objetivo: "Diagnosticar fallas incipientes y estimar vida útil remanente (RUL) de equipos rotativos y baterías."
            concepto_clave_latex: "s(\\vec{x}) = \\|\\vec{x} - \\mathcal{D}(\\mathcal{E}(\\vec{x}))\\|_2 > \\tau_{\\text{umbral}} \\quad (\\text{Autoencoder})"
            ejemplo: "Detección temprana de sobrecalentamiento en cojinetes SCADA de aerogeneradores."
            bloque_sugerido: "Práctica 50 min • Mantenimiento predictivo"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Optimización Matemática (MILP) y Metaheurísticas (PSO / GA)"
            objetivo: "Formular programación lineal entera mixta y algoritmos evolutivos para despacho energético."
            concepto_clave_latex: "\\min \\vec{c}^T\\vec{x} + \\vec{d}^T\\vec{z} \\;\\;\\text{s.t.}\\;\\; A\\vec{x} + B\\vec{z} \\le \\vec{b},\\;\\; \\vec{z}\\in\\{0,1\\}^p"
            ejemplo: "Programación MILP del horario óptimo carga/descarga de baterías ante tarifas horarias."
            bloque_sugerido: "Laboratorio 50 min • Optimización MILP"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Physics-Informed ML (PINNs), RL y Despliegue de APIs Energéticas"
            objetivo: "Integrar restricciones físicas en redes neuronales y control por aprendizaje por refuerzo."
            concepto_clave_latex: "\\mathcal{L}_{\\text{PINN}} = \\mathcal{L}_{\\text{datos}} + \\lambda_{\\text{física}}\\|\\mathcal{N}[u]\\|_2^2 \\quad ; \\quad Q^*(s,a)"
            ejemplo: "Agente RL para gestión EMS en tiempo real desplegado como microservicio REST."
            bloque_sugerido: "Taller 50 min • PINNs y EMS inteligente"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Concepto, Tipologías y Gobernanza de Comunidades Energéticas"
            objetivo: "Comprender modelos cooperativos ciudadanos, prosumidores colectivos y Decreto 2236 de 2023."
            concepto_clave_latex: "E_{\\text{local}} = \\sum_{i \\in \\mathcal{C}}\\min(G_i, D_i) + E_{\\text{comp}}"
            ejemplo: "Diseño organizacional y estatutos de gobernanza para una comunidad energética en Magdalena."
            bloque_sugerido: "Taller 45 min • Modelos de gobernanza"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Diagnóstico Participativo, Pobreza Energética y Necesidades Locales"
            objetivo: "Medir índices multidimensionales de pobreza energética y mapear actores comunitarios."
            concepto_clave_latex: "I_{\\text{gasto}} = \\frac{C_{\\text{energía}}}{I_{\\text{hogar}}} \\times 100\\% > 10\\%"
            ejemplo: "Censo energético participativo de refrigeración, cocción limpia e iluminación en veredas."
            bloque_sugerido: "Trabajo Campo 45 min • Diagnóstico social"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Cocción Limpia, Bombeo Solar Comunitario y Cadena de Frío"
            objetivo: "Dimensionar usos productivos de la energía (agroindustria, pesca artesanal y agua potable)."
            concepto_clave_latex: "P_{\\text{bomba}} = \\frac{\\rho g Q H_{\\text{TDH}}}{\\eta_b \\eta_m} \\quad ; \\quad E_{\\text{diaria}} = P_{\\text{bomba}} \\cdot t_{\\text{op}}"
            ejemplo: "Planta solar de hielo y cuartos fríos comunitarios para pescadores artesanales."
            bloque_sugerido: "Pomodoro 50/10 • Usos productivos"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Microrredes Comunitarias AC/DC y Reparto de Excedentes"
            objetivo: "Definir coeficientes estáticos y dinámicos de reparto de energía autogenerada."
            concepto_clave_latex: "E_{\\text{asignada},i}(t) = \\beta_i(t)\\,E_{\\text{gen,com}}(t) \\quad \\left(\\sum_{i=1}^{N}\\beta_i(t) = 1\\right)"
            ejemplo: "Esquema de medición inteligente y reparto equitativo entre 40 viviendas y escuela."
            bloque_sugerido: "Práctica 45 min • Coeficientes de reparto"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Modelos de Sostenibilidad Financiera y Fondos Rotatorios O&M"
            objetivo: "Garantizar la operación y reposición de baterías/inversores mediante tarifas solidarias."
            concepto_clave_latex: "T_{\\text{sost}} = \\frac{C_{\\text{O\\&M}} + F_{\\text{reposición}}}{E_{\\text{consumida}}} \\quad [\\$/\\text{kWh}]"
            ejemplo: "Prevención del abandono tecnológico mediante fondo comunitario de reserva para baterías."
            bloque_sugerido: "Taller 45 min • Fondo de reposición"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Apropiación Social del Conocimiento y Capacitación Técnica Local"
            objetivo: "Formar operadores comunitarios locales para mantenimiento preventivo Nivel 1 y 2."
            concepto_clave_latex: "D_{\\text{disponibilidad}} = \\frac{\\text{MTBF}}{\\text{MTBF} + \\text{MTTR}}\\uparrow \\iff \\text{MTTR}_{\\text{local}}\\downarrow"
            ejemplo: "Manual ilustrado de operación segura y limpieza de paneles para técnicos locales."
            bloque_sugerido: "Taller 40 min • Pedagogía comunitaria"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Agregación de Demanda, Respuesta de la Demanda y Plantas Virtuales (VPP)"
            objetivo: "Coordinar recursos distribuidos comunitarios para brindar flexibilidad a la red."
            concepto_clave_latex: "P_{\\text{VPP}}(t) = \\sum_{k=1}^{M}\\left[P_{\\text{PV},k}(t) + P_{\\text{BESS},k}(t) - \\Delta P_{\\text{DR},k}(t)\\right]"
            ejemplo: "Desplazamiento coordinado de bombeo de agua hacia horas de pico solar."
            bloque_sugerido: "Pomodoro 45/10 • Flexibilidad VPP"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Indicadores de Impacto Socioambiental, Género y Escalabilidad"
            objetivo: "Evaluar cobeneficios en salud, equidad de género, ingresos locales y carbono evitado."
            concepto_clave_latex: "\\text{SROI} = \\frac{\\text{VP}_{\\text{social}} + \\text{VP}_{\\text{ambiental}}}{\\text{CAPEX}_{\\text{tot}}}"
            ejemplo: "Evaluación de Retorno Social de la Inversión (SROI) alineada con ODS 5, 7, 8 y 13."
            bloque_sugerido: "Estudio de Caso 45 min • Métricas SROI"
      - codigo: "04031826"
        nombre: "Gestión, Auditoría y Eficiencia Energética"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Sistema de Gestión de la Energía (SGEn) bajo Norma ISO 50001"
            objetivo: "Implementar el ciclo PHVA de mejora continua del desempeño energético organizacional."
            concepto_clave_latex: "\\text{IDEn} = \\frac{E_{\\text{real}}}{E_{\\text{LBEn}}} \\le 1.0"
            ejemplo: "Identificación de Usos Significativos de la Energía (USEs) mediante diagrama de Pareto 80/20."
            bloque_sugerido: "Pomodoro 45/10 • Revisión ISO 50001"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Auditorías Energéticas Tipo 1, 2 y 3 (ASHRAE / ISO 50002)"
            objetivo: "Planificar campañas de medición, balance energético global y portafolio de medidas."
            concepto_clave_latex: "E_{\\text{entrada}} = \\sum E_{\\text{útil},k} + \\sum E_{\\text{pérdidas},j}"
            ejemplo: "Ejecución de auditoría ASHRAE Nivel 2 en un edificio hospitalario o hotelero."
            bloque_sugerido: "Práctica 45 min • Protocolo ISO 50002"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Línea Base Energética (LBEn), Indicadores IDEn y CUSUM"
            objetivo: "Construir modelos estadísticos multivariables y gráficos de sumas acumuladas de ahorro."
            concepto_clave_latex: "E_{\\text{base}} = E_0 + a\\cdot\\text{Producción} + b\\cdot\\text{CDD} \\quad ; \\quad \\text{CUSUM}_k = \\sum_{t=1}^{k}(E_{\\text{real},t} - \\hat{E}_{\\text{base},t})"
            ejemplo: "Detección de ahorros reales normalizados por clima y ocupación con CUSUM."
            bloque_sugerido: "Pomodoro 50/10 • LBEn y CUSUM"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Eficiencia en Sistemas Motrices, Bombeo, Ventilación y Compresores"
            objetivo: "Evaluar sustitución por motores IE4, eliminación de estrangulamiento con VFD y fugas."
            concepto_clave_latex: "\\Delta P_{\\text{ahorro VFD}} = P_{\\text{nom}}\\left[1 - \\left(\\frac{Q_{\\text{req}}}{Q_{\\text{nom}}}\\right)^3\\right]"
            ejemplo: "Retorno de inversión menor a 1.8 años al instalar VFD en bombas de caudal variable."
            bloque_sugerido: "Pomodoro 50/10 • Leyes de afinidad"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Eficiencia en Climatización HVAC, Iluminación y Envolvente"
            objetivo: "Auditar chillers (kW/TR), aislamiento, infiltraciones y actualización lumínica DALI/LED."
            concepto_clave_latex: "\\text{IPLV / kW por TR} = \\frac{P_{\\text{eléc [kW]}}}{\\dot{Q}_{\\text{frío [TR]}}} \\quad (1\\text{ TR} = 3.517\\text{ kW}_t)"
            ejemplo: "Optimización de setpoint de agua helada y recuperación entálpica en aire exterior."
            bloque_sugerido: "Práctica 45 min • Auditoría HVAC"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Eficiencia Térmica en Vapor, Hornos, Trampas y Recuperación de Calor"
            objetivo: "Cuantificar ahorros por economizadores, precalentamiento de aire, aislamiento y condensado."
            concepto_clave_latex: "\\Delta\\eta_{\\text{comb}} \\approx +1\\%\\text{ por cada } 20\\,^\\circ\\text{C de caída en } T_{\\text{chimenea}}"
            ejemplo: "Auditoría termográfica infrarroja de trampas de vapor fallidas y tuberías desnudas."
            bloque_sugerido: "Pomodoro 45/10 • Sistemas de vapor"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Protocolo Internacional de Medida y Verificación (IPMVP)"
            objetivo: "Seleccionar Opciones A, B, C o D de IPMVP para certificar ahorros contractuales."
            concepto_clave_latex: "\\Delta E_{\\text{ahorro}} = (E_{\\text{LBEn,adj}} - E_{\\text{post}}) \\pm \\Delta E_{\\text{no-rut}}"
            ejemplo: "Diseño de plan M&V Opción B para proyecto de modernización de central de frío."
            bloque_sugerido: "Práctica 45 min • Opciones IPMVP"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Modelos ESCO, Contratos por Desempeño (EPC) y Financiación Verde"
            objetivo: "Estructurar contratos de ahorro compartido o garantizado con empresas de servicios energéticos."
            concepto_clave_latex: "\\text{Pago}_{\\text{ESCO}} = \\alpha \\cdot \\Delta \\$_{\\text{ahorro}} \\quad ; \\quad \\alpha \\in [0.6, 0.85]"
            ejemplo: "Viabilidad de contrato EPC sin inversión inicial CAPEX para el cliente industrial."
            bloque_sugerido: "Taller 45 min • Modelo de negocio ESCO"
      - codigo: "06011842"
        nombre: "Instalaciones Eléctricas con Energías Renovables"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Arquitectura de Instalaciones Eléctricas BT/MT y Normativa NTC 2050 / RETIE"
            objetivo: "Clasificar niveles de tensión, acometidas, tableros y esquemas de conexión a tierra (TN-S, TT, IT)."
            concepto_clave_latex: "V_{\\text{BT}} \\le 1000\\text{ V} \\quad ; \\quad 1\\text{ kV} < V_{\\text{MT}} \\le 57.5\\text{ kV}"
            ejemplo: "Selección de esquema TN-S con conductor neutro y tierra separados en edificios con PV."
            bloque_sugerido: "Pomodoro 45/10 • Esquemas NTC 2050"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Cuadros de Cargas, Factores de Demanda y Dimensionamiento de Conductores"
            objetivo: "Calcular alimentadores por capacidad de corriente corregida, caída de tensión e I²t de corto."
            concepto_clave_latex: "I_z = I_0\\cdot f_T\\cdot f_{\\text{agrup}} \\ge 1.25\\,I_{\\text{cont}} \\quad ; \\quad S_{\\min,\\text{cc}} = \\frac{I_{\\text{cc}}\\sqrt{t}}{k}"
            ejemplo: "Dimensionamiento completo de conductores THHN/XHHW-2 en bandejas y ductos."
            bloque_sugerido: "Pomodoro 50/10 • Ampacidad y caída ΔV"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Cálculo de Cortocircuito Simétrico/Asimétrico (IEC 60909) y Coordinación"
            objetivo: "Determinar corrientes de falla máxima/mínima y selectividad amperimétrica/cronométrica."
            concepto_clave_latex: "I''_{k3} = \\frac{c\\,V_n}{\\sqrt{3}\\,|Z_{\\text{eq}}|} \\quad ; \\quad I_{\\text{cu,interruptor}} \\ge I''_{k3}"
            ejemplo: "Coordinación selectiva de curvas tiempo-corriente entre interruptor principal y ramales."
            bloque_sugerido: "Pomodoro 50/10 • Cortocircuito IEC 60909"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Integración de Generación Renovable en BT y MT (Sección 690 / 705)"
            objetivo: "Diseñar acoplamiento en lado carga y lado fuente verificando la regla del 120% en barrajes."
            concepto_clave_latex: "I_{\\text{alim}} + I_{\\text{inv}} \\le 1.20 \\, I_{\\text{barra}} \\quad ; \\quad I_{\\text{inv}} = \\frac{S_{\\text{inv}}}{\\sqrt{3}V_L}"
            ejemplo: "Interconexión segura de 250 kW solares en el tablero general de una industria."
            bloque_sugerido: "Práctica 50 min • Regla del 120%"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Protecciones de Interconexión IEEE 1547 y Anti-Islanding"
            objetivo: "Configurar funciones ANSI 27/59 (tensión), 81O/U (frecuencia), 32 (potencia inversa) y ROCOF."
            concepto_clave_latex: "\\text{ROCOF} = \\left|\\frac{df}{dt}\\right| > \\text{Umbral} \\implies \\text{Disparo anti-isla } < 2\\text{ s}"
            ejemplo: "Ajuste de relé de interconexión para autogenerador conectado a red de 13.2 kV."
            bloque_sugerido: "Pomodoro 45/10 • Funciones ANSI/IEEE 1547"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas de Puesta a Tierra (IEEE 80) y Protección contra Rayos (IEC 62305)"
            objetivo: "Diseñar mallas de tierra equipotenciales, apantallamiento por esfera rodante y cascada DPS."
            concepto_clave_latex: "R_g \\le 10\\,\\Omega\\;\\;(\\text{BT}) \\quad ; \\quad R_{\\text{esfera}} = 20\\,I^{0.65}\\text{ [m]} \\quad (\\text{IEC 62305})"
            ejemplo: "Apantallamiento externo de cubierta solar evitando sombras sobre las cadenas PV."
            bloque_sugerido: "Práctica 50 min • Malla IEEE 80 y DPS"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Infraestructura de Recarga de Vehículos Eléctricos (EVSE) y BESS"
            objetivo: "Integrar cargadores Modo 3 y Modo 4 DC rápidos con gestión dinámica de carga y cuartos BESS."
            concepto_clave_latex: "P_{\\text{EVSE,din}}(t) = P_{\\text{trafo,máx}} - P_{\\text{edificio}}(t) + P_{\\text{PV}}(t)"
            ejemplo: "Diseño eléctrico y ventilación/detección contra fuga térmica UL 9540A para BESS."
            bloque_sugerido: "Pomodoro 45/10 • Electrolineras y BESS"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Calidad de Potencia (IEEE 519), Comisionamiento y Dictamen RETIE"
            objetivo: "Ejecutar pruebas de aislamiento (Megger), termografía, impedancia de lazo y expediente RETIE."
            concepto_clave_latex: "R_{\\text{aislamiento}} \\ge 1\\text{ M}\\Omega/\\text{kV} + 1\\text{ M}\\Omega \\quad ; \\quad \\text{TDD} \\le 5\\%"
            ejemplo: "Protocolo completo IEC 62446 de puesta en marcha y carpeta para inspección RETIE."
            bloque_sugerido: "Taller 45 min • Comisionamiento IEC 62446"
      - codigo: "05011835"
        nombre: "Proyecto Integrador CDIO II"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Ingeniería de Sistemas Complejos y Arquitectura Multi-Subsistema"
            objetivo: "Descomponer un sistema energético integrado en subsistemas térmico, eléctrico, control y estructura."
            concepto_clave_latex: "\\mathcal{S} = \\{\\mathcal{S}_{\\text{potencia}},\\; \\mathcal{S}_{\\text{térmico}},\\; \\mathcal{S}_{\\text{control}},\\; \\mathcal{S}_{\\text{com}}\\}"
            ejemplo: "Diagrama de bloques de arquitectura e interfaces ICD de un prototipo TRL 5."
            bloque_sugerido: "Taller CDIO 45 min • Interfaces ICD"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Co-Diseño Hardware/Software y Control Embebido en Tiempo Real"
            objetivo: "Implementar adquisición multisensor y lazos de control discretos sobre sistemas embebidos."
            concepto_clave_latex: "u[k] = u[k-1] + q_0 e[k] + q_1 e[k-1] + q_2 e[k-2]"
            ejemplo: "Controlador PI digital programado en microcontrolador/PLC para regulación DC."
            bloque_sugerido: "Laboratorio 50 min • Control discreto"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Diseño para Confiabilidad, Mantenibilidad y Seguridad (FMEA)"
            objetivo: "Ejecutar Análisis de Modos y Efectos de Falla calculando Número Prioritario de Riesgo."
            concepto_clave_latex: "\\text{RPN} = \\text{Severidad} \\times \\text{Ocurrencia} \\times \\text{Detección}"
            ejemplo: "Matriz FMEA del prototipo incorporando paradas de emergencia y redundancia."
            bloque_sugerido: "Taller CDIO 45 min • Matriz FMEA"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Optimización Multiobjetivo del Diseño Detallado"
            objetivo: "Balancear eficiencia, costo y peso mediante frente de Pareto antes de fabricar."
            concepto_clave_latex: "\\min_{\\vec{x}} \\left[\\text{Costo}(\\vec{x}),\\; -\\eta(\\vec{x}),\\; m(\\vec{x})\\right]"
            ejemplo: "Selección del punto compromiso en el frente de Pareto para el prototipo CDIO II."
            bloque_sugerido: "Práctica 50 min • Frente de Pareto"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Integración de Electrónica de Potencia, Sensórica y Telemetría IoT"
            objetivo: "Construir tableros limpios con compatibilidad electromagnética (EMC) y monitoreo remoto."
            concepto_clave_latex: "\\text{SNR} = 20\\log_{10}\\left(\\frac{V_{\\text{señal}}}{V_{\\text{ruido}}}\\right) \\ge 40\\text{ dB}"
            ejemplo: "Dashboard web en tiempo real registrando tensión, corriente, temperatura y eficiencia."
            bloque_sugerido: "Laboratorio 50 min • Telemetría IoT"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Pruebas Hardware-in-the-Loop / Banco de Carga y Régimen Transitorio"
            objetivo: "Evaluar respuesta dinámica ante perturbaciones bruscas de carga y entrada renovable."
            concepto_clave_latex: "M_p = \\frac{y_{\\max} - y_{\\text{ss}}}{y_{\\text{ss}}}\\times 100\\% \\quad ; \\quad t_s\\;(2\\%)"
            ejemplo: "Ensayo de escalón de carga 20% -> 90% midiendo sobreimpulso y tiempo de establecimiento."
            bloque_sugerido: "Laboratorio 50 min • Ensayos dinámicos"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Evaluación de Desempeño Energético, Económico y Huella Ambiental"
            objetivo: "Cuantificar rendimiento global, costo unitario escalado y emisiones evitadas del prototipo."
            concepto_clave_latex: "\\eta_{\\text{prot}} = \\frac{\\int P_{\\text{útil}}\\,dt}{\\int P_{\\text{recurso}}\\,dt} \\quad ; \\quad \\Delta\\text{CO}_2\\text{ evitado}"
            ejemplo: "Validación de métricas clave frente a los requisitos iniciales de diseño."
            bloque_sugerido: "Práctica 45 min • Balance integral"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Transferencia Tecnológica, Manual de Operación y Defensa CDIO II"
            objetivo: "Entregar planos as-built, repositorio de código documentado, manual O&M y sustentación."
            concepto_clave_latex: "\\text{TRL}_{\\text{CDIO II}} \\ge 5 \\quad ; \\quad \\text{MTBF} \\ge 1000\\text{ h}"
            ejemplo: "Feria de ingeniería con demostración operativa en vivo ante evaluadores externos."
            bloque_sugerido: "Simulacro 45 min • Defensa CDIO II"
      - codigo: "06011841"
        nombre: "Transferencia de Calor"
        creditos: 3
        obligatoria: true
        categoria: "FISICA_QUIMICA"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Ecuación General de Difusión de Calor y Condiciones de Frontera"
            objetivo: "Derivar la ecuación diferencial 3D de conducción en coordenadas cartesianas, cilíndricas y esféricas."
            concepto_clave_latex: "\\nabla\\cdot(k\\nabla T) + \\dot{q}_{\\text{gen}} = \\rho c_p\\frac{\\partial T}{\\partial t}"
            ejemplo: "Perfil parabólico de temperatura dentro de una barra combustible o conductor con efecto Joule."
            bloque_sugerido: "Pomodoro 50/10 • Ecuación de difusión"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Conducción Estacionaria 1D, Redes Térmicas y Radio Crítico"
            objetivo: "Resolver paredes compuestas, cilindros multicapa, resistencia de contacto y espesor óptimo."
            concepto_clave_latex: "\\dot{Q} = \\frac{T_{\\infty,1} - T_{\\infty,2}}{\\sum R_{\\text{térm}}} \\quad ; \\quad R_{\\text{cil}} = \\frac{\\ln(r_2/r_1)}{2\\pi k L} \\quad ; \\quad r_{\\text{cr}} = \\frac{k}{h}"
            ejemplo: "Cálculo de pérdida lineal W/m en tuberías industriales de vapor aisladas con lana mineral."
            bloque_sugerido: "Pomodoro 50/10 • Circuitos térmicos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Superficies Extendidas (Aletas) y Eficiencia Global de Disipadores"
            objetivo: "Diseñar arreglos de aletas calculando distribución hiperbólica de temperatura y efectividad."
            concepto_clave_latex: "\\eta_f = \\frac{\\tanh(m L_c)}{m L_c},\\;\\; m = \\sqrt{\\frac{h P}{k A_c}} \\quad ; \\quad \\varepsilon_f = \\frac{\\dot{Q}_{\\text{aleta}}}{h A_{c,b}\\theta_b} \\ge 2"
            ejemplo: "Dimensionamiento de disipador aletado para enfriar inversores y LEDs de alta potencia."
            bloque_sugerido: "Pomodoro 50/10 • Eficiencia de aletas"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Conducción Transitoria: Capacitancia Concentrada (Biot) y Heisler"
            objetivo: "Evaluar constantes de tiempo térmicas para Bi < 0.1 y gradientes espaciales internos."
            concepto_clave_latex: "\\text{Bi} = \\frac{h L_c}{k} < 0.1 \\implies \\frac{T(t)-T_\\infty}{T_i - T_\\infty} = \\exp\\left(-\\text{Bi}\\cdot\\text{Fo}\\right),\\;\\; \\text{Fo} = \\frac{\\alpha t}{L_c^2}"
            ejemplo: "Tiempo de calentamiento/enfriamiento transitorio en sensores y tanques acumuladores."
            bloque_sugerido: "Pomodoro 50/10 • Números Bi y Fo"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Convección Forzada Externa: Capa Límite Térmica y Correlaciones"
            objetivo: "Calcular coeficientes convectivos sobre placas planas, cilindros y bancos de tubos."
            concepto_clave_latex: "\\overline{\\text{Nu}}_L = \\frac{\\bar{h}L}{k_f} = 0.037\\,\\text{Re}_L^{4/5}\\text{Pr}^{1/3}"
            ejemplo: "Enfriamiento convectivo por viento sobre paneles solares y bancos de tubos de calderas."
            bloque_sugerido: "Pomodoro 50/10 • Correlaciones Nu-Re-Pr"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Convección Forzada Interna en Ductos y Convección Natural (Rayleigh)"
            objetivo: "Aplicar correlaciones de Dittus-Boelter/Gnielinski y flotabilidad de Churchill-Chu."
            concepto_clave_latex: "\\text{Nu}_D = 0.023\\,\\text{Re}_D^{0.8}\\text{Pr}^n \\quad ; \\quad \\text{Ra}_L = \\text{Gr}_L\\text{Pr} = \\frac{g\\beta(T_s - T_\\infty)L^3}{\\nu\\alpha}"
            ejemplo: "Transferencia de calor en tubos absorbedores solares y enfriamiento natural de transformadores ONAN."
            bloque_sugerido: "Pomodoro 50/10 • Flujo interno y Ra"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Ebullición, Condensación e Intercambiadores de Calor (LMTD y ε-NTU)"
            objetivo: "Dimensionar intercambiadores de coraza y tubos, placas y flujos cruzados con ensuciamiento."
            concepto_clave_latex: "\\dot{Q} = U A F\\,\\Delta T_{\\text{lm}} \\quad ; \\quad \\varepsilon = \\frac{\\dot{Q}}{C_{\\min}(T_{h,i}-T_{c,i})} = f(\\text{NTU}, C_r)"
            ejemplo: "Diseño térmico ε-NTU de un recuperador de calor de gases de escape y condensador."
            bloque_sugerido: "Pomodoro 50/10 • Métodos LMTD y ε-NTU"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Transferencia de Calor por Radiación, Factores de Forma y Escudos"
            objetivo: "Resolver intercambio radiativo en recintos grises difusos mediante redes de radiosidad."
            concepto_clave_latex: "\\dot{Q}_{12} = \\frac{\\sigma(T_1^4 - T_2^4)}{\\frac{1-\\varepsilon_1}{\\varepsilon_1 A_1} + \\frac{1}{A_1 F_{12}} + \\frac{1-\\varepsilon_2}{\\varepsilon_2 A_2}}"
            ejemplo: "Cálculo de pérdidas radiativas en receptores termosolares de alta temperatura y hornos."
            bloque_sugerido: "Taller 50 min • Redes de Oppenheimer"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Clasificación y Diagrama de Ragone del Almacenamiento Energético"
            objetivo: "Comparar densidad de potencia, densidad de energía, tiempo de descarga y eficiencia round-trip."
            concepto_clave_latex: "\\eta_{\\text{rt}} = \\frac{E_{\\text{descarga}}}{E_{\\text{carga}}} \\quad ; \\quad t_{\\text{nom}} = \\frac{E_{\\text{nom}}}{P_{\\text{nom}}}"
            ejemplo: "Selección tecnológica entre supercapacitores (segundos), BESS (horas) e H2 (estacional)."
            bloque_sugerido: "Pomodoro 45/10 • Diagrama de Ragone"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Químicas de Baterías (LFP, NMC, Na-ion, Flujo Redox Vanadio)"
            objetivo: "Evaluar tensión nominal, estabilidad térmica, profundidad DoD y ciclos equivalentes."
            concepto_clave_latex: "E_{\\text{útil}} = N_s N_p V_{\\text{cel}} C_{\\text{Ah}}\\cdot \\text{DoD} \\quad ; \\quad C\\text{-rate} = \\frac{I}{C_{\\text{nom}}}"
            ejemplo: "Comparación LFP vs. Flujo de Vanadio para almacenamiento estacionario de 8 horas."
            bloque_sugerido: "Pomodoro 45/10 • C-rate y químicas"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Modelado Equivalente (Thevenin RC), Estimación SoC y Degradación SoH"
            objetivo: "Estimar estado de carga y envejecimiento calendárico/cíclico mediante modelos equivalentes."
            concepto_clave_latex: "\\text{SoC}(t) = \\text{SoC}_0 - \\frac{\\eta_c}{Q_n}\\int_0^t i(\\tau)\\,d\\tau \\quad ; \\quad \\text{SoH} = \\frac{Q_{\\text{actual}}}{Q_{\\text{nominal}}}"
            ejemplo: "Filtro de Kalman extendido y conteo Rainflow de ciclos en un Battery Management System."
            bloque_sugerido: "Pomodoro 50/10 • Modelos BMS"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Almacenamiento Mecánico: Bombeo PHS, CAES Adiabático y Volantes"
            objetivo: "Dimensionar sistemas mecánicos de gran escala y respuesta inercial rápida."
            concepto_clave_latex: "W_{\\text{CAES,isot}} = m R T\\ln\\left(\\frac{P_2}{P_1}\\right) \\quad ; \\quad \\Delta E_{\\text{flywheel}} = \\frac{1}{2}I(\\omega_{\\max}^2 - \\omega_{\\min}^2)"
            ejemplo: "Recuperación de calor de compresión en sistemas A-CAES sin quema de combustible."
            bloque_sugerido: "Práctica 45 min • PHS, CAES y Flywheels"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Almacenamiento Térmico Sensible, Latente (PCM) y Termoquímico"
            objetivo: "Diseñar tanques de sales fundidas (NaNO3-KNO3), bancos de hielo y materiales PCM."
            concepto_clave_latex: "Q_{\\text{TES}} = m c_{p,s}(T_f - T_i) + m \\Delta h_{\\text{fusión}} + m c_{p,l}(T_{\\max} - T_f)"
            ejemplo: "Tanques de dos niveles de sales fundidas para despacho nocturno en planta CSP."
            bloque_sugerido: "Pomodoro 50/10 • Sales fundidas y PCM"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Supercapacitores (EDLC), SMES y Sistemas Híbridos HESS"
            objetivo: "Combinar alta potencia instantánea de supercapacitores con alta energía de baterías."
            concepto_clave_latex: "E_{\\text{SC}} = \\frac{1}{2}C(V_{\\max}^2 - V_{\\min}^2) \\quad ; \\quad E_{\\text{SMES}} = \\frac{1}{2}L I^2"
            ejemplo: "Filtro paso-bajo de potencia que desvía picos rápidos al supercapacitor protegiendo la batería."
            bloque_sugerido: "Práctica 45 min • Hibridación HESS"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Integración a Red (PCS Grid-Forming), Seguridad Térmica y Reciclaje"
            objetivo: "Analizar inversores formadores de red (inercia virtual), prevención de thermal runaway y 2ª vida."
            concepto_clave_latex: "J_v\\frac{d\\omega}{dt} = P_{\\text{ref}} - P_e - D_v(\\omega - \\omega_0)"
            ejemplo: "Soporte de frecuencia sintética con BESS Grid-Forming y normativa NFPA 855."
            bloque_sugerido: "Pomodoro 45/10 • PCS Grid-Forming"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Costo Nivelado de Almacenamiento (LCOS) y Arbitraje de Mercado"
            objetivo: "Evaluar rentabilidad integral de sistemas de almacenamiento bajo múltiples servicios."
            concepto_clave_latex: "\\text{LCOS} = \\frac{\\text{CAPEX} + \\sum \\frac{\\text{OPEX}_t + C_{\\text{carga},t}}{(1+r)^t}}{\\sum \\frac{E_{\\text{descargada},t}}{(1+r)^t}}"
            ejemplo: "Optimización financiera de BESS combinando peak-shaving industrial y regulación."
            bloque_sugerido: "Taller 45 min • Cálculo LCOS"
      - codigo: "06021851"
        nombre: "Aprovechamiento de Fuentes Energéticas No Renovables"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Reservas, Geopolítica y Caracterización de Carbón, Petróleo y Gas"
            objetivo: "Analizar relación Reservas/Producción (R/P), clasificación API, índice de Wobbe y gas natural."
            concepto_clave_latex: "W_I = \\frac{\\text{PCS}}{\\sqrt{d_{\\text{rel}}}} \\quad ; \\quad ^\\circ\\text{API} = \\frac{141.5}{SG} - 131.5"
            ejemplo: "Intercambiabilidad de gases combustibles mediante el Índice de Wobbe en quemadores."
            bloque_sugerido: "Pomodoro 45/10 • Índice de Wobbe y API"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Termodinámica Avanzada de Combustión y Temperatura Adiabática de Llama"
            objetivo: "Calcular composición de productos en equilibrio y temperatura máxima de cámara."
            concepto_clave_latex: "\\sum_{\\text{react}} n_r(\\bar{h}_f^\\circ + \\Delta\\bar{h})_r = \\sum_{\\text{prod}} n_p(\\bar{h}_f^\\circ + \\Delta\\bar{h}(T_{\\text{ad}}))_p"
            ejemplo: "Efecto del exceso de aire y precalentamiento sobre la temperatura adiabática de llama."
            bloque_sugerido: "Pomodoro 50/10 • Llama adiabática"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Centrales Termoeléctricas Supercríticas y Ciclos Combinados (CCGT)"
            objetivo: "Evaluar regímenes ultrasupercríticos, calderas recuperadoras HRSG de 3 presiones y Heat Rate."
            concepto_clave_latex: "\\text{HR} = \\frac{3600}{\\eta_{\\text{neta}}}\\;\\;[\\text{kJ/kWh}] \\quad ; \\quad \\eta_{\\text{CCGT}} = \\eta_{\\text{GT}} + \\eta_{\\text{ST}}(1 - \\eta_{\\text{GT}})"
            ejemplo: "Planta de ciclo combinado de respaldo térmico con Heat Rate de 6,100 kJ/kWh (η = 59%)."
            bloque_sugerido: "Pomodoro 50/10 • Heat Rate y CCGT"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Cadena del Gas Natural Licuado (GNL), Regasificación y Transporte"
            objetivo: "Analizar licuefacción criogénica (-162 °C), terminales FSRU y estaciones compresoras."
            concepto_clave_latex: "\\frac{V_{\\text{gas std}}}{V_{\\text{GNL}}} \\approx 600 \\quad ; \\quad W_{\\text{comp}} = \\frac{zRT_1\\gamma}{\\gamma-1}\\left[\\left(\\frac{P_2}{P_1}\\right)^{(\\gamma-1)/\\gamma}-1\\right]"
            ejemplo: "Operación de terminal de regasificación FSRU en la costa Caribe como respaldo ante El Niño."
            bloque_sugerido: "Práctica 45 min • Cadena GNL"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Control de Emisiones Atmosféricas (NOx, SOx, Material Particulado)"
            objetivo: "Dimensionar precipitadores electrostáticos, desulfuración FGD y reducción catalítica SCR."
            concepto_clave_latex: "\\eta_{\\text{ESP}} = 1 - \\exp\\left(-\\frac{w_e A_{\\text{col}}}{Q_{\\text{gas}}}\\right)"
            ejemplo: "Abatimiento superior al 99% de cenizas volantes y reducción SCR de NOx con amoníaco."
            bloque_sugerido: "Pomodoro 45/10 • Control ambiental"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Captura, Uso y Almacenamiento de Carbono (CCUS)"
            objetivo: "Evaluar captura postcombustión con aminas, oxicombustión y penalización energética."
            concepto_clave_latex: "\\Delta\\eta_{\\text{penalización CCUS}} = \\eta_{\\text{sin captura}} - \\eta_{\\text{con captura}} \\approx 6\\text{--}9\\text{ pts \\%}"
            ejemplo: "Integración de captura de CO2 en planta industrial o producción de hidrógeno azul."
            bloque_sugerido: "Práctica 45 min • Tecnologías CCUS"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Fundamentos de Energía Nuclear de Fisión y Reactores SMR"
            objetivo: "Comprender defecto de masa, sección eficaz, moderación neutrónica y reactores modulares SMR."
            concepto_clave_latex: "\\Delta E = \\Delta m \\cdot c^2 \\quad ; \\quad k_{\\text{ef}} = \\frac{N_{t+1}}{N_t} = 1"
            ejemplo: "Seguridad pasiva y densidad energética extrema de reactores modulares pequeños (SMR)."
            bloque_sugerido: "Pomodoro 45/10 • Física nuclear y SMR"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Flexibilización Térmica, Rampas y Desmantelamiento en Transición"
            objetivo: "Adaptar plantas térmicas existentes a operación flexible de respaldo y reconversión."
            concepto_clave_latex: "R_{\\text{rampa}}\\,[\\text{MW/min}] \\quad ; \\quad P_{\\min,\\text{técnico}}\\downarrow \\quad ; \\quad \\text{Co-firing } \\text{Gas} + \\text{H}_2"
            ejemplo: "Mezcla gradual (blending) de hasta 20% de hidrógeno verde en turbinas de gas existentes."
            bloque_sugerido: "Taller 45 min • Flexibilidad y blending"
      - codigo: "05011833"
        nombre: "Evaluación y Gestión de Proyectos"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Estándares PMBOK / Ágil Híbrido en Proyectos de Infraestructura"
            objetivo: "Integrar alcance (EDT/WBS), interesados y gobernanza en proyectos EPC energéticos."
            concepto_clave_latex: "\\sum_{k=1}^m \\text{WP}_k = 100\\% \\quad ; \\quad \\text{SPI} = \\frac{\\text{EV}}{\\text{PV}}"
            ejemplo: "Desglose EDT completo para ingeniería, procura, construcción y puesta en marcha (EPC)."
            bloque_sugerido: "Taller 45 min • Estructura EDT/WBS"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Programación de Redes (CPM / PERT) y Nivelación de Recursos"
            objetivo: "Determinar holguras totales/libres, ruta crítica y probabilidad de cumplimiento PERT."
            concepto_clave_latex: "t_e = \\frac{t_o + 4t_m + t_p}{6} \\quad ; \\quad \\sigma_t = \\frac{t_p - t_o}{6} \\quad ; \\quad Z = \\frac{T_{\\text{meta}} - \\sum t_{e,\\text{CP}}}{\\sqrt{\\sum \\sigma_{\\text{CP}}^2}}"
            ejemplo: "Probabilidad de energizar una subestación antes de la fecha límite regulatoria UPME."
            bloque_sugerido: "Pomodoro 50/10 • Ruta crítica CPM/PERT"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Gestión del Valor Ganado (EVM) y Control de Costos/Cronograma"
            objetivo: "Monitorear CPI, SPI y proyecciones EAC/ETC durante la ejecución física de obra."
            concepto_clave_latex: "\\text{CPI} = \\frac{\\text{EV}}{\\text{AC}},\\;\\; \\text{SPI} = \\frac{\\text{EV}}{\\text{PV}},\\;\\; \\text{EAC} = \\frac{\\text{BAC}}{\\text{CPI}}"
            ejemplo: "Diagnóstico temprano de sobrecosto y atraso en el montaje mecánico de un parque solar."
            bloque_sugerido: "Pomodoro 50/10 • Curva S y EVM"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Contratos EPC, BOS, FIDIC, Licitaciones y Gestión de Procura"
            objetivo: "Administrar pliegos técnicos, garantías de desempeño (Performance Ratio) y penalidades LD."
            concepto_clave_latex: "\\text{LD}_{\\text{atraso}} = \\min\\left(d_{\\text{mora}}\\cdot c_{\\text{día}},\\; 0.10\\cdot V_{\\text{contrato}}\\right)"
            ejemplo: "Cláusulas de garantía de PR y disponibilidad en contratos llave en mano FIDIC Silver Book."
            bloque_sugerido: "Práctica 45 min • Contratos EPC/FIDIC"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Gestión Cuantitativa de Riesgos, Opciones Reales y Seguros"
            objetivo: "Valorar flexibilidad gerencial (expandir, diferir, abandonar) y matriz probabilística EMV."
            concepto_clave_latex: "\\text{EMV} = \\sum_{k} p_k \\cdot I_k \\quad ; \\quad V_{\\text{proyecto}} = \\text{VPN}_{\\text{base}} + V_{\\text{opción real}}"
            ejemplo: "Valoración de la opción real de ampliar en Fase 2 la capacidad de almacenamiento BESS."
            bloque_sugerido: "Pomodoro 45/10 • EMV y opciones reales"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Gestión HSE, Seguridad Eléctrica (NFPA 70E) y Calidad ISO 9001"
            objetivo: "Prevenir accidentes laborales mediante bloqueo LOTO, análisis de arco eléctrico y QA/QC."
            concepto_clave_latex: "E_{\\text{arco}} = 4.184 \\cdot C_f \\cdot E_n \\left(\\frac{t}{0.2}\\right)\\left(\\frac{610}{D}\\right)^x"
            ejemplo: "Implementación de procedimiento LOTO (Lockout/Tagout) en maniobras de media tensión."
            bloque_sugerido: "Taller 45 min • Seguridad LOTO/HSE"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Cierre Técnico, Comisionamiento, Punch List y Handover a O&M"
            objetivo: "Gestionar pruebas PAC/FAC (Provisional & Final Acceptance) y transferencia documental."
            concepto_clave_latex: "\\text{PAC} \\xrightarrow{\\text{Garantía 24 meses } (\\text{PR} \\ge \\text{PR}_{\\text{gar}})} \\text{FAC}"
            ejemplo: "Lista de pendientes (Punch List) y recepción formal de planta por el equipo de O&M."
            bloque_sugerido: "Práctica 40 min • Protocolo PAC/FAC"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Gestión de Activos Físicos (ISO 55000) y Costo de Ciclo de Vida (LCC)"
            objetivo: "Optimizar mantenimiento centrado en confiabilidad (RCM) y reposición de activos."
            concepto_clave_latex: "\\text{LCC} = C_{\\text{adq}} + \\text{VP}(C_{\\text{oper}}) + \\text{VP}(C_{\\text{mant}}) + \\text{VP}(C_{\\text{falla}}) - \\text{VP}(V_{\\text{salv}})"
            ejemplo: "Estrategia ISO 55000 para maximizar valor de activos de generación a 30 años."
            bloque_sugerido: "Taller 45 min • Gestión ISO 55000"
      - codigo: "06021852"
        nombre: "Hydrogen Energy"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#0A84FF"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Taxonomía del Hidrógeno (Verde, Azul, Gris), Propiedades y Hoja de Ruta"
            objetivo: "Contrastar densidades gravimétrica (120 MJ/kg) y volumétrica, e intensidad de carbono."
            concepto_clave_latex: "\\text{PCI}_{\\text{H}_2} = 120\\text{ MJ/kg} = 33.33\\text{ kWh/kg} \\quad ; \\quad \\text{PCS}_{\\text{H}_2} = 141.8\\text{ MJ/kg}"
            ejemplo: "Comparación energética de 1 kg de H2 frente a gasolina y metas de la Hoja de Ruta Colombia."
            bloque_sugerido: "Pomodoro 45/10 • Propiedades del H2"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Termodinámica de Electrólisis del Agua: Potencial Reversible y Termoneutro"
            objetivo: "Calcular voltaje reversible (1.23 V) y termoneutro (1.48 V) a distintas temperaturas."
            concepto_clave_latex: "E_{\\text{rev}}^\\circ = \\frac{\\Delta G^\\circ}{2F} = 1.229\\text{ V} \\quad ; \\quad E_{\\text{tn}}^\\circ = \\frac{\\Delta H^\\circ}{2F} = 1.481\\text{ V}"
            ejemplo: "Disminución de demanda eléctrica con aumento de temperatura en electrólisis de vapor SOEC."
            bloque_sugerido: "Pomodoro 50/10 • Termodinámica H2O"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Tecnologías de Electrolizadores: Alcalino (AEL), PEM, AEM y SOEC"
            objetivo: "Modelar sobrepotenciales de activación (Butler-Volmer), óhmicos y consumo específico."
            concepto_clave_latex: "V_{\\text{cel}} = E_{\\text{rev}} + \\frac{RT}{\\alpha F}\\text{arcsinh}\\left(\\frac{j}{2j_0}\\right) + j\\,R_{\\text{ohm}} \\quad ; \\quad e_{\\text{esp}}\\,[\\text{kWh/kg H}_2]"
            ejemplo: "Dimensionamiento de stack PEM (52 kWh/kg H2) acoplado directamente a fluctuaciones eólicas."
            bloque_sugerido: "Pomodoro 50/10 • Curva V-j electrolizador"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Compresión (350/700 bar), Licuefacción Criogénica (20 K) y LOHC/Hidruros"
            objetivo: "Cuantificar la energía parásita requerida para almacenar hidrógeno en alta densidad."
            concepto_clave_latex: "W_{\\text{comp,etapas}} = N_e\\frac{zRT_1\\gamma}{\\gamma-1}\\left[\\left(\\frac{P_f}{P_i}\\right)^{\\frac{\\gamma-1}{N_e\\gamma}}-1\\right]\\quad (\\approx 10\\text{--}15\\%\\text{ PCI})"
            ejemplo: "Penalización energética de compresión a 700 bar frente a licuefacción a -253 °C (30% PCI)."
            bloque_sugerido: "Práctica 45 min • Almacenamiento H2"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Derivados Power-to-X: Amoníaco Verde (Haber-Bosch), Metanol y e-Fuels"
            objetivo: "Evaluar portadores químicos líquidos para exportación marítima y descarbonización industrial."
            concepto_clave_latex: "\\text{N}_2 + 3\\text{H}_2 \\rightleftharpoons 2\\text{NH}_3 \\quad (\\Delta H^\\circ = -92.4\\text{ kJ/mol}) \\quad ; \\quad \\text{CO}_2 + 3\\text{H}_2 \\to \\text{CH}_3\\text{OH} + \\text{H}_2\\text{O}"
            ejemplo: "Planta integrada eólica -> H2 -> NH3 verde en el Caribe para fertilizantes y exportación."
            bloque_sugerido: "Pomodoro 50/10 • Síntesis Power-to-X"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Celdas de Combustible (PEMFC y SOFC) y Balance de Planta (BoP)"
            objetivo: "Analizar eficiencia eléctrica, gestión de agua/calor y cogeneración con celdas de combustible."
            concepto_clave_latex: "\\dot{W}_{\\text{FC}} = N_{\\text{cel}}\\,V_{\\text{cel}}\\,I \\quad ; \\quad \\dot{m}_{\\text{H}_2} = \\frac{N_{\\text{cel}}\\,I\\,M_{\\text{H}_2}}{2F\\,\\mu_f}"
            ejemplo: "Consumo horario de H2 y calor disipado en un módulo PEMFC de 200 kW para transporte pesado."
            bloque_sugerido: "Pomodoro 50/10 • Stack PEMFC y BoP"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Transporte por Ductos (Blending), Fragilización y Seguridad (ISO/TR 15916)"
            objetivo: "Gestionar límites de inflamabilidad (4%–75%), difusión, fragilización de aceros y ventilación."
            concepto_clave_latex: "\\text{LFL}_{\\text{H}_2} = 4\\%\\text{ vol},\\;\\; \\text{UFL}_{\\text{H}_2} = 75\\%\\text{ vol},\\;\\; E_{\\text{ign,mín}} = 0.017\\text{ mJ}"
            ejemplo: "Diseño de detección, venteo seguro y selección de aceros austeníticos 316L anti-fragilización."
            bloque_sugerido: "Práctica 45 min • Seguridad de hidrógeno"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Costo Nivelado del Hidrógeno (LCOH) y Certificación de Origen"
            objetivo: "Modelar sensibilidad del LCOH frente al LCOE eléctrico, CAPEX del electrolizador y factor de planta."
            concepto_clave_latex: "\\text{LCOH}\\,[\\$/\\text{kg}] = \\frac{\\text{CAPEX}_{\\text{el}}\\cdot\\text{CRF} + \\text{OPEX} + E_{\\text{eléc}}\\cdot\\text{LCOE}}{M_{\\text{H}_2,\\text{anual}}}"
            ejemplo: "Optimización del ratio sobredimensionado solar/eólico vs. electrolizador para lograr LCOH < 2.5 $/kg."
            bloque_sugerido: "Taller 50 min • Optimización LCOH"
      - codigo: "07011855"
        nombre: "Inmersión Profesional"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#8E8E93"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Plan de Trabajo Empresarial, Objetivos e Indicadores KPI de Práctica"
            objetivo: "Concertar entregables medibles, cronograma y métricas de impacto con el tutor empresarial."
            concepto_clave_latex: "\\text{KPI}_{\\text{meta}} = \\frac{\\text{Valor Alcanzado}}{\\text{Valor Planificado}}\\times 100\\% \\ge 95\\%"
            ejemplo: "Estructuración formal del plan de inmersión en empresa generadora, distribuidora o consultora."
            bloque_sugerido: "Taller 40 min • Plan KPI de práctica"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ética Profesional, Responsabilidad Legal COPNIA y Confidencialidad"
            objetivo: "Aplicar la Ley 842 de 2003 (Código de Ética Profesional de Ingeniería) y acuerdos NDA."
            concepto_clave_latex: "\\text{CPI} = \\frac{\\text{EV}}{\\text{AC}} \\ge 1.0 \\quad ; \\quad \\text{SPI} = \\frac{\\text{EV}}{\\text{PV}} \\ge 1.0"
            ejemplo: "Análisis de dilemas éticos reales en interventoría, licitaciones y reportes regulatorios."
            bloque_sugerido: "Lectura 40 min • Código ético COPNIA"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Seguridad y Salud en el Trabajo (SG-SST) y Riesgo Eléctrico/Térmico"
            objetivo: "Cumplir protocolos de trabajo en alturas, espacios confinados y riesgo eléctrico en campo."
            concepto_clave_latex: "R = P_{\\text{ocurrencia}} \\times C_{\\text{severidad}} \\quad ; \\quad R \\le R_{\\text{adm}}"
            ejemplo: "Elaboración de ATS (Análisis de Trabajo Seguro) previo a inspección de planta solar o caldera."
            bloque_sugerido: "Práctica 40 min • Matriz ATS campo"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Diagnóstico Técnico en Sitio y Levantamiento de Línea Base Operativa"
            objetivo: "Recopilar información operativa, planos unifilares/P&ID e históricos SCADA de la organización."
            concepto_clave_latex: "\\Delta P_{\\text{pérdida}} = P_{\\text{esperada}}(G, T) - P_{\\text{real,SCADA}}"
            ejemplo: "Identificación en campo de cuellos de botella operativos o bajo rendimiento energético."
            bloque_sugerido: "Trabajo Campo 50 min • Diagnóstico in situ"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Ejecución de Ingeniería Aplicada y Solución de Problemas Reales"
            objetivo: "Desarrollar propuestas de optimización, diseño o automatización validadas con estándares."
            concepto_clave_latex: "B_{\\text{neto}} = \\Delta E \\cdot P_e - \\Delta C_{\\text{O\\&M}} \\quad ; \\quad \\text{TIR} > \\text{WACC}"
            ejemplo: "Implementación de herramienta automatizada o mejora operativa durante la práctica."
            bloque_sugerido: "Práctica 50 min • Desarrollo técnico"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Trabajo Interdisciplinario, Comunicación Ejecutiva y Liderazgo"
            objetivo: "Comunicar avances técnicos de forma asertiva ante gerencia, operaciones y contratistas."
            concepto_clave_latex: "\\Delta \\$ = \\sum_{t=1}^{12} \\Delta E_t \\cdot T_t \\quad ; \\quad \\text{Payback} \\le 3\\text{ años}"
            ejemplo: "Presentación quincenal de indicadores de desempeño en comité técnico de ingeniería."
            bloque_sugerido: "Taller 40 min • Reporte gerencial"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Documentación Técnica, Trazabilidad y Gestión del Conocimiento"
            objetivo: "Estandarizar memorias de cálculo, procedimientos SOP y repositorios entregables para la empresa."
            concepto_clave_latex: "\\Delta\\sigma_{\\text{calidad}} = \\frac{|x_{\\text{audit}} - x_{\\text{nom}}|}{\\sigma} \\le 3"
            ejemplo: "Entrega de manual operativo y hojas de cálculo verificadas sin dependencia de caja negra."
            bloque_sugerido: "Práctica 40 min • Entregables QA/QC"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Informe Final de Inmersión, Cuantificación de Impacto y Sustentación"
            objetivo: "Sintetizar aportes técnicos, económicos y aprendizajes profesionales ante universidad y empresa."
            concepto_clave_latex: "\\text{ROI} = \\frac{\\text{Beneficio Neto}}{\\text{Inversión}} \\times 100\\%"
            ejemplo: "Sustentación final de resultados cuantificados logrados durante el semestre de inmersión."
            bloque_sugerido: "Simulacro 45 min • Defensa de inmersión"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Diseño Bioclimático Pasivo y Confort Higrotérmico (ASHRAE 55)"
            objetivo: "Minimizar ganancias térmicas en clima cálido-húmedo mediante orientación, sombreado y ventilación."
            concepto_clave_latex: "\\text{OTTV} = \\frac{\\sum (A_w U_w \\Delta T_{\\text{eq}}) + \\sum (A_f \\text{SHGC} \\cdot SF)}{A_{\\text{envolvente}}}"
            ejemplo: "Optimización de aleros y coeficiente SHGC para edificios en el trópico costero."
            bloque_sugerido: "Pomodoro 45/10 • Carta psicrométrica"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Psicrometría Aplicada y Sistemas Avanzados de Climatización"
            objetivo: "Calcular cargas sensibles y latentes, enfriamiento evaporativo y sistemas VRF/agua helada."
            concepto_clave_latex: "\\dot{Q}_{\\text{total}} = \\dot{m}_a(h_2 - h_1) = \\dot{Q}_{\\text{sens}} + \\dot{Q}_{\\text{lat}} \\quad ; \\quad \\text{SHR} = \\frac{\\dot{Q}_{\\text{sens}}}{\\dot{Q}_{\\text{total}}}"
            ejemplo: "Deshumidificación eficiente con recuperación de calor en climas con HR > 80%."
            bloque_sugerido: "Pomodoro 50/10 • Procesos psicrométricos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Edificaciones de Energía Cero Neta (NZEB) y Certificación LEED / EDGE"
            objetivo: "Balancear demanda anual ultraeficiente con generación renovable in situ."
            concepto_clave_latex: "E_{\\text{neta anual}} = E_{\\text{exportada,ren}} - E_{\\text{importada,red}} \\ge 0 \\quad ; \\quad \\text{EUI}\\,[\\text{kWh/m}^2\\cdot\\text{año}]"
            ejemplo: "Reducción del índice EUI de 180 a 75 kWh/(m²·año) cumpliendo estándar EDGE Advanced."
            bloque_sugerido: "Taller 50 min • Balance NZEB"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Integración Térmica Industrial Avanzada y Redes HEN (Pinch)"
            objetivo: "Diseñar redes óptimas de intercambiadores de calor maximizando recuperación interna."
            concepto_clave_latex: "N_{\\text{unidades,mín}} = N_{\\text{corrientes}} + N_{\\text{servicios}} - 1"
            ejemplo: "Rediseño de red de intercambiadores reduciendo 32% el consumo de gas en planta alimentaria."
            bloque_sugerido: "Pomodoro 50/10 • Síntesis de redes HEN"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Bombas de Calor Industriales de Alta Temperatura y MVR"
            objetivo: "Valorizar calor residual de baja temperatura mediante bombas de calor y recompresión de vapor."
            concepto_clave_latex: "\\text{COP}_H = \\eta_{\\text{Lorenz}}\\frac{T_{\\text{sum}}}{T_{\\text{sum}} - T_{\\text{fuente}}} \\approx 3.2\\text{--}4.8"
            ejemplo: "Electrificación eficiente de procesos de secado y pasteurización a 90–130 °C."
            bloque_sugerido: "Práctica 45 min • Bombas de calor HT"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Automatización Inmótica (BMS/BAS) y Control Predictivo MPC"
            objetivo: "Optimizar en tiempo real la operación de chillers, almacenamiento térmico e iluminación."
            concepto_clave_latex: "\\min_{\\vec{u}} \\sum_{k=0}^{H_p-1}\\left[c_e(k)P_{\\text{red}}(k) + \\lambda\\|T(k) - T_{\\text{confort}}\\|^2\\right]"
            ejemplo: "Preenfriamiento inteligente del edificio en horas solares usando control predictivo MPC."
            bloque_sugerido: "Laboratorio 50 min • Control MPC"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Movilidad Eléctrica Eficiente, Gestión de Flotas y Vehicle-to-Grid (V2G)"
            objetivo: "Evaluar consumo específico (kWh/km), frenado regenerativo e integración bidireccional V2G."
            concepto_clave_latex: "e_{\\text{veh}} = \\frac{1}{\\eta_{\\text{tren}}}\\left(m g C_r + \\frac{1}{2}\\rho C_d A_f v^2\\right) \\quad [\\text{Wh/km}]"
            ejemplo: "Electrificación de flota de transporte público urbano con carga nocturna inteligente."
            bloque_sugerido: "Pomodoro 45/10 • Eficiencia vehicular"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Descarbonización Industrial Profunda y Economía Circular Energética"
            objetivo: "Construir curvas de costos marginales de abatimiento (MACC) para industrias electrointensivas."
            concepto_clave_latex: "\\text{MAC}_k = \\frac{C_{\\text{neto}, k}}{\\Delta \\text{CO}_{2, k}} \\quad [\\$/\\text{tCO}_2\\text{e}]"
            ejemplo: "Priorización de medidas con costo de abatimiento negativo (ahorro neto) e inversiones ruta Net-Zero."
            bloque_sugerido: "Taller 45 min • Curva MACC"
      - codigo: "06031853"
        nombre: "Electiva Línea de Fuentes de Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Energía Solar Térmica de Concentración (CSP): Cilindro-Parabólico y Torre"
            objetivo: "Analizar relación de concentración geométrica, eficiencia óptica-térmica y campo de heliostatos."
            concepto_clave_latex: "C = \\frac{A_a}{A_r} \\le \\frac{1}{\\sin^2\\theta_s} \\quad ; \\quad \\eta_{\\text{rec}} = \\alpha\\tau - \\frac{\\varepsilon\\sigma(T_r^4 - T_a^4) + h(T_r - T_a)}{C\\cdot\\text{DNI}}"
            ejemplo: "Planta termosolar de torre central con sales fundidas operando a 565 °C y factor de planta 65%."
            bloque_sugerido: "Pomodoro 50/10 • Óptica y térmica CSP"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Celdas Fotovoltaicas Emergentes: Perovskita, Tándem Si-Perovskita y Agrivoltaica"
            objetivo: "Superar el límite de Shockley-Queisser de unión simple (~33.7%) mediante multiunión."
            concepto_clave_latex: "\\eta_{\\text{SQ}}(1.34\\text{ eV}) \\approx 33.7\\% \\quad \\xrightarrow{\\text{Tándem 2J}} \\quad \\eta_{\\max,\\text{teór}} \\approx 45\\%"
            ejemplo: "Sistemas agrivoltaicos elevados que combinan cultivo agrícola, menor evaporación y generación."
            bloque_sugerido: "Pomodoro 45/10 • Tándem y agrivoltaica"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Fotovoltaica Flotante (FPV) en Embalses Hidroeléctricos"
            objetivo: "Evaluar sinergia hidro-solar, enfriamiento convectivo del panel y reducción de evaporación."
            concepto_clave_latex: "E_{\\text{híbrida}} = E_{\\text{hidro}} + E_{\\text{FPV}} \\quad ; \\quad P \\le S_{\\text{subestación}}"
            ejemplo: "Planta solar flotante sobre embalse hidroeléctrico compensando estiajes de El Niño."
            bloque_sugerido: "Práctica 45 min • Hibridación FPV-Hidro"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Aerogeneradores Flotantes Offshore y Sistemas Aerotransportados (AWE)"
            objetivo: "Analizar plataformas Spar, Semisumergible y TLP para aguas profundas (> 60 m)."
            concepto_clave_latex: "P_{\\text{offshore}} = \\frac{1}{2}\\rho C_p(\\lambda,\\beta)\\pi R^2 v_{\\text{hub}}^3 \\quad (D_{\\text{rotor}} > 220\\text{ m})"
            ejemplo: "Evaluación de plataformas flotantes en aguas profundas del Caribe occidental."
            bloque_sugerido: "Pomodoro 45/10 • Eólica flotante"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Biorrefinerías Avanzadas, Biogás a Bio-GNL y Combustibles Sostenibles SAF"
            objetivo: "Integrar rutas Fischer-Tropsch y Alcohol-to-Jet para aviación y transporte marítimo limpio."
            concepto_clave_latex: "(2n+1)\\text{H}_2 + n\\text{CO} \\xrightarrow{\\text{Co / Fe}} \\text{C}_n\\text{H}_{2n+2} + n\\text{H}_2\\text{O}"
            ejemplo: "Biorrefinería integrada cero residuos para producción de SAF aeronáutico y bioproductos."
            bloque_sugerido: "Pomodoro 45/10 • Síntesis Fischer-Tropsch"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Sistemas Híbridos Multi-Fuente (PV + Eólica + BESS + H2) 24/7 Libre de Carbono"
            objetivo: "Aprovechar complementariedad estacional y horaria viento-sol para suministro firme."
            concepto_clave_latex: "r_{W,\\text{PV}} = \\frac{\\text{Cov}(P_W, P_{\\text{PV}})}{\\sigma_W \\sigma_{\\text{PV}}} < 0 \\implies \\sigma_{W+\\text{PV}}^2 < \\sigma_W^2 + \\sigma_{\\text{PV}}^2"
            ejemplo: "Complementariedad diaria y estacional entre radiación diurna y vientos nocturnos en el Caribe."
            bloque_sugerido: "Laboratorio 50 min • Complementariedad"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Cosecha de Energía (Energy Harvesting) Piezoeléctrica, Triboeléctrica y RF"
            objetivo: "Alimentar redes inalámbricas de sensores IoT sin baterías desechables."
            concepto_clave_latex: "P_{\\text{piezo}} = \\frac{d_{33}^2 F^2 \\omega}{2 C_p}\\cdot\\frac{R_L}{(1/\\omega C_p)^2 + R_L^2}"
            ejemplo: "Sensores autónomos de vibración en puentes y subestaciones alimentados por piezoeléctricos."
            bloque_sugerido: "Práctica 40 min • Micro-energy harvesting"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Fusión Nuclear por Confinamiento Magnético (Tokamak) e Inercial"
            objetivo: "Comprender el criterio de triple producto de Lawson y reacciones Deuterio-Tritio."
            concepto_clave_latex: "n_e\\,T\\,\\tau_E \\ge 3\\times 10^{21}\\text{ m}^{-3}\\cdot\\text{keV}\\cdot\\text{s} \\quad ; \\quad Q_{\\text{fusión}} = \\frac{P_{\\text{fusión}}}{P_{\\text{calentamiento}}} > 1"
            ejemplo: "Estado del arte de reactores Tokamak de alto campo HTS y perspectivas de largo plazo."
            bloque_sugerido: "Taller 45 min • Criterio de Lawson"
      - codigo: "05011836"
        nombre: "Proyecto Integrador CDIO III"
        creditos: 2
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#BF5AF2"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Concepción de Solución Capstone a Escala Pre-Comercial (TRL 6–7)"
            objetivo: "Formular un proyecto integrador de fin de ciclo con impacto regional verificable."
            concepto_clave_latex: "\\text{VPN} > 0 \\quad \\land \\quad \\text{TIR} > \\text{WACC} \\quad \\land \\quad \\text{TRL} \\ge 7"
            ejemplo: "Definición de alcance ejecutivo con aliado industrial, institucional o comunitario."
            bloque_sugerido: "Taller CDIO 45 min • Charter Capstone"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Ingeniería de Detalle Multidisciplinaria y Cumplimiento Normativo"
            objetivo: "Elaborar memorias de cálculo completas, diagramas unifilares/P&ID y verificación RETIE/CREG/ISO."
            concepto_clave_latex: "\\Delta V \\le 3\\% \\quad ; \\quad I_{\\text{cable}} \\le I_{\\text{adm}} \\quad ; \\quad R_{\\text{malla}} \\le 5\\,\\Omega"
            ejemplo: "Revisión cruzada por pares de los cálculos eléctricos, térmicos, estructurales y de control."
            bloque_sugerido: "Práctica 50 min • Ingeniería de detalle"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Gemelo Digital / Simulación Integral de 8760 Horas y Contingencias"
            objetivo: "Validar el diseño ante escenarios extremos N-1, variabilidad climática y degradación."
            concepto_clave_latex: "A = \\frac{\\text{MTBF}}{\\text{MTBF} + \\text{MTTR}} \\ge 0.99 \\quad ; \\quad N-1 \\implies \\text{Estable}"
            ejemplo: "Simulación anual completa demostrando resiliencia operativa ante fallas y días nublados."
            bloque_sugerido: "Laboratorio 50 min • Validación N-1"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Implementación de Prototipo Avanzado / Piloto y Pruebas de Campo"
            objetivo: "Desplegar y calibrar el sistema físico o piloto demostrativo en condiciones reales."
            concepto_clave_latex: "U_{95\\%}(\\eta_{\\text{piloto}}) = \\pm k \\, u_c(\\eta) \\quad ; \\quad k = 2"
            ejemplo: "Operación continua del piloto registrando curvas reales de generación, consumo y estabilidad."
            bloque_sugerido: "Laboratorio 50 min • Piloto en campo"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Estructuración Financiera Bancable, LCOE y Modelo de Negocio"
            objetivo: "Cerrar flujo de caja proyectado, análisis Monte Carlo de riesgo y estrategia de financiación."
            concepto_clave_latex: "P(\\text{VPN} > 0) \\ge 90\\% \\quad ; \\quad \\text{DSCR}_{\\min} \\ge 1.30"
            ejemplo: "Pitch financiero para fondos de transición energética (FENOGE, banca multilateral o ESCO)."
            bloque_sugerido: "Taller 50 min • Bancabilidad"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Evaluación Integral de Impacto Ambiental, Huella de Carbono y Social"
            objetivo: "Cuantificar reducción de emisiones tCO2e, circularidad de materiales y aceptación social."
            concepto_clave_latex: "\\Delta\\text{GEI}_{\\text{vida útil}} = \\sum_{t=1}^{N} E_{t}\\cdot FE_{\\text{red}} - \\text{GEI}_{\\text{ACV embebido}}"
            ejemplo: "Matriz socioambiental completa y plan de gestión de residuos RAEE/baterías al final de vida."
            bloque_sugerido: "Práctica 45 min • Huella ACV"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Redacción de Artículo Científico IEEE y Dossier Ejecutivo"
            objetivo: "Sintetizar la innovación y resultados experimentales en formato publicable IEEE."
            concepto_clave_latex: "R^2 \\ge 0.95 \\quad ; \\quad \\text{RMSE} \\le 3.5\\% \\quad ; \\quad p < 0.01"
            ejemplo: "Revisión estilo peer-review de gráficas vectoriales, ecuaciones KaTeX y referencias."
            bloque_sugerido: "Escritura 50 min • Artículo IEEE"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Sustentación Pública Capstone CDIO III ante Panel Evaluador"
            objetivo: "Defender con rigor técnico y solvencia ejecutiva la solución integral desarrollada."
            concepto_clave_latex: "\\text{Puntaje}_{\\text{CDIO}} = \\sum_{k=1}^m w_k \\cdot C_k \\ge 80\\%"
            ejemplo: "Presentación final de cierre de la línea integradora CDIO de Ingeniería Energética."
            bloque_sugerido: "Simulacro 50 min • Defensa Capstone"
      - codigo: "06011844"
        nombre: "Redes de Transporte y Distribución de la Energía"
        creditos: 3
        obligatoria: true
        categoria: "INGENIERIA_ENERGIA"
        color: "#FF9F0A"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Estructura de Sistemas de Potencia (STN, STR, SDL) y Sistema Por Unidad"
            objetivo: "Normalizar redes multitransformador mediante magnitudes base trifásicas en por unidad."
            concepto_clave_latex: "Z_{\\text{base}} = \\frac{V_{L,\\text{base}}^2}{S_{3\\phi,\\text{base}}} \\quad ; \\quad Z_{\\text{p.u.,nuevo}} = Z_{\\text{p.u.,viejo}}\\left(\\frac{V_{b,v}}{V_{b,n}}\\right)^2\\left(\\frac{S_{b,n}}{S_{b,v}}\\right)"
            ejemplo: "Diagrama de impedancias en p.u. de un corredor generador-elevador-línea 220 kV-carga."
            bloque_sugerido: "Pomodoro 50/10 • Sistema p.u."
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Parámetros Físicos de Líneas de Transmisión: R, L, C y Transposición"
            objetivo: "Calcular inductancia y capacitancia por fase en haces de conductores (RMG / RMD)."
            concepto_clave_latex: "L = 2\\times 10^{-7}\\ln\\left(\\frac{\\text{DMG}}{\\text{RMG}_L}\\right)\\text{ [H/m]} \\quad ; \\quad C = \\frac{2\\pi\\varepsilon_0}{\\ln(\\text{DMG}/\\text{RMG}_C)}\\text{ [F/m]}"
            ejemplo: "Efecto de conductores en haz (bundled conductors) reduciendo reactancia y efecto corona."
            bloque_sugerido: "Pomodoro 50/10 • DMG y RMG"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Modelos de Líneas Cortas, Medias (π Nominal) y Largas (Hiperbólico), SIL"
            objetivo: "Evaluar regulación de tensión, efecto Ferranti e impedancia característica (SIL)."
            concepto_clave_latex: "Z_c = \\sqrt{\\frac{z}{y}},\\;\\; \\text{SIL} = \\frac{V_L^2}{Z_c} \\quad ; \\quad \\tilde{V}_S = \\cosh(\\gamma l)\\tilde{V}_R + Z_c\\sinh(\\gamma l)\\tilde{I}_R"
            ejemplo: "Sobretensión por efecto Ferranti en líneas largas de 500 kV en vacío y compensación con reactores."
            bloque_sugerido: "Pomodoro 50/10 • Modelo π y SIL"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Matriz de Admitancias Y_bus y Flujo de Carga (Newton-Raphson / Fast Decoupled)"
            objetivo: "Formular Y_bus dispersa y resolver barras Slack, PV y PQ en redes malladas."
            concepto_clave_latex: "I_i = \\sum_{k=1}^{N} Y_{ik} V_k \\quad ; \\quad P_i = \\sum_{k=1}^{N}|V_i||V_k||Y_{ik}|\\cos(\\theta_i - \\theta_k - \\delta_{ik})"
            ejemplo: "Convergencia cuadrática en 4 iteraciones del sistema de prueba IEEE de 9 o 14 barras."
            bloque_sugerido: "Laboratorio 50 min • Y_bus y Flujo NR"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Fallas Simétricas, Componentes Simétricas de Fortescue y Fallas Asimétricas"
            objetivo: "Descomponer redes desbalanceadas en secuencias positiva, negativa y cero (LG, LL, LLG)."
            concepto_clave_latex: "\\begin{bmatrix}\\tilde{V}_0 \\\\ \\tilde{V}_1 \\\\ \\tilde{V}_2\\end{bmatrix} = \\frac{1}{3}\\begin{bmatrix}1 & 1 & 1 \\\\ 1 & a & a^2 \\\\ 1 & a^2 & a\\end{bmatrix}\\begin{bmatrix}\\tilde{V}_a \\\\ \\tilde{V}_b \\\\ \\tilde{V}_c\\end{bmatrix} \\quad ; \\quad I_{a,\\text{1Φ}} = \\frac{3E_a}{Z_1 + Z_2 + Z_0 + 3Z_f}"
            ejemplo: "Cálculo de falla monofásica a tierra en una línea de 115 kV para ajuste de relés de distancia."
            bloque_sugerido: "Pomodoro 50/10 • Redes de secuencia"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Estabilidad Transitoria (Criterio de Áreas Iguales), Control de Tensión y FACTS"
            objetivo: "Determinar ángulo crítico de despeje de falla y compensación dinámica SVC/STATCOM."
            concepto_clave_latex: "\\frac{2H}{\\omega_s}\\frac{d^2\\delta}{dt^2} = P_m - P_{e,\\max}\\sin\\delta \\quad ; \\quad A_{\\text{aceleración}} = A_{\\text{desaceleración}}"
            ejemplo: "Tiempo crítico de despeje de falla trifásica e inercia equivalente H del sistema."
            bloque_sugerido: "Pomodoro 50/10 • Áreas iguales"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Transmisión en Corriente Directa de Alta Tensión (HVDC LCC y VSC)"
            objetivo: "Comparar enlaces HVDC frente a HVAC por distancia de equilibrio, cables submarinos y control P-Q."
            concepto_clave_latex: "P_{\\text{HVDC}} = V_{d1}\\frac{V_{d1} - V_{d2}}{R_d} \\quad ; \\quad L_{\\text{crit}} \\approx 600\\text{ km}"
            ejemplo: "Interconexión HVDC VSC para evacuar energía eólica desde La Guajira hacia el interior del SIN."
            bloque_sugerido: "Práctica 45 min • Enlaces HVDC VSC"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Redes Activas de Distribución, Reconfiguración, Smart Grids y Hosting Capacity"
            objetivo: "Gestionar flujos bidireccionales, regulación Volt-VAr y automatización FLISR en SDL."
            concepto_clave_latex: "\\Delta V \\approx \\frac{RP + XQ}{V_n} \\quad ; \\quad Q(V) = \\pm f(\\Delta V)"
            ejemplo: "Aumento de capacidad de alojamiento solar en alimentadores radiales con curvas Volt-VAr."
            bloque_sugerido: "Taller 50 min • Smart Grids y Volt-VAr"
      - codigo: "04031830"
        nombre: "Transición Energética Justa"
        creditos: 3
        obligatoria: true
        categoria: "PROYECTOS_GESTION"
        color: "#30D158"
        temas:
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Dimensiones de la Justicia Energética: Distributiva, Procedimental y Reconocimiento"
            objetivo: "Analizar equidad en costos, beneficios, participación informada y derechos territoriales."
            concepto_clave_latex: "J_{\\text{total}} = \\sum_{k=1}^4 w_k \\cdot J_k \\quad ; \\quad \\sum_{k=1}^4 w_k = 1"
            ejemplo: "Evaluación de equidad en megaproyectos renovables ubicados en territorios étnicos."
            bloque_sugerido: "Lectura Crítica 45 min • Marcos de justicia"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Geopolítica de Minerales Críticos (Litio, Cobre, Tierras Raras) y Cadenas Globales"
            objetivo: "Evaluar riesgos de suministro, huella extractiva y reciclaje urbano de minerales estratégicos."
            concepto_clave_latex: "I_{\\text{crit}} = \\sqrt{\\text{EI}^2 + \\text{HHI}^2} \\quad ; \\quad \\text{HHI} = \\sum s_i^2"
            ejemplo: "Demanda intensiva de cobre, litio, níquel y neodimio en baterías, redes y turbinas."
            bloque_sugerido: "Pomodoro 45/10 • Minerales críticos"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Reconversión Laboral, Regiones Carboníferas y Diversificación Productiva"
            objetivo: "Diseñar estrategias de transición laboral y económica para municipios dependientes de fósiles."
            concepto_clave_latex: "\\Delta E_{\\text{empleo}} = E_{\\text{verde}} - E_{\\text{fósil}} \\quad ; \\quad \\Delta E > 0"
            ejemplo: "Rutas de reconversión económica y formación técnica en el corredor minero Cesar-La Guajira."
            bloque_sugerido: "Estudio de Caso 50 min • Regiones carboníferas"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Diálogo Intercultural, Consentimiento Libre, Previo e Informado y Co-propiedad"
            objetivo: "Integrar saberes locales, consulta previa genuina y participación comunitaria en los ingresos."
            concepto_clave_latex: "R_{\\text{territorio}} = 0.06 \\cdot \\text{Venta Bruta} \\quad [\\text{Ley 99/93}]"
            ejemplo: "Modelos de asociación y participación accionaria comunitaria en parques eólicos y solares."
            bloque_sugerido: "Taller 45 min • Gobernanza territorial"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Acceso Universal, Tarifas Diferenciales y Erradicación de Pobreza Energética"
            objetivo: "Formular esquemas de mínimo vital energético, subsidios focalizados y sustitución de leña."
            concepto_clave_latex: "\\text{Pobreza Energética} \\downarrow \\iff \\text{Asequibilidad} \\land \\text{Confiabilidad 24/7} \\land \\text{Cocción Limpia}"
            ejemplo: "Impacto en salud respiratoria femenina e infantil al reemplazar fogones de leña abiertos."
            bloque_sugerido: "Pomodoro 45/10 • Acceso y salud"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Finanzas Climáticas Internacionales, JETP, Taxonomía Verde y Bonos Sostenibles"
            objetivo: "Estructurar acceso a fondos climáticos concesionales, canje de deuda y bonos verdes."
            concepto_clave_latex: "r_{\\text{verde}} = r_{\\text{mercado}} - \\text{Greenium} - \\text{Tramo Concesional}"
            ejemplo: "Alineación de proyectos con la Taxonomía Verde de Colombia y fondos verdes climáticos."
            bloque_sugerido: "Práctica 45 min • Finanzas verdes"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Modelado Integrado Energía-Economía-Clima (IAM / LEAP) y Escenarios Net-Zero"
            objetivo: "Construir trayectorias de descarbonización sectorial a 2050 evaluando costos y cobeneficios."
            concepto_clave_latex: "E_{\\text{CO}_2} = \\text{Población} \\times \\frac{\\text{PIB}}{\\text{Pob}} \\times \\frac{E}{\\text{PIB}} \\times \\frac{\\text{CO}_2}{E}\\quad (\\text{Identidad de Kaya})"
            ejemplo: "Descomposición de la Identidad de Kaya para proyectar carbono neutralidad nacional a 2050."
            bloque_sugerido: "Pomodoro 50/10 • Identidad de Kaya"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Diseño de Política Pública y Hoja de Ruta de Transición Energética Justa"
            objetivo: "Articular instrumentos regulatorios, fiscales, industriales y sociales en hojas de ruta viables."
            concepto_clave_latex: "P_{\\text{renovable}} \\ge P_{\\text{meta}} \\quad ; \\quad \\Delta\\text{CO}_2 \\to 0"
            ejemplo: "Simulación de mesa multiactor negociando una hoja de ruta regional de transición justa."
            bloque_sugerido: "Simulacro 50 min • Política pública TEJ"
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
          - numero_tema: 1
            corte: 1
            modalidad: "tecnica"
            titulo: "Modalidades Reglamentarias de Grado en Unimagdalena y Selección Estratégica"
            objetivo: "Conocer alcances y requisitos de Trabajo de Investigación, Pasantía, Emprendimiento o Posgrado."
            concepto_clave_latex: "M_{\\text{grado}} \\in \\{ \\text{Tesis},\\; \\text{Pasantía},\\; \\text{Spin-off},\\; \\text{Posgrado} \\}"
            ejemplo: "Alineación del perfil profesional del estudiante con la modalidad óptima y director."
            bloque_sugerido: "Taller 40 min • Plan maestro de grado"
          - numero_tema: 2
            corte: 1
            modalidad: "tecnica"
            titulo: "Consolidación del Estado del Arte y Marco Metodológico Reproducible"
            objetivo: "Refinar literatura reciente (últimos 5 años) y protocolo experimental o computacional verificable."
            concepto_clave_latex: "R^2 \\ge 0.98 \\quad ; \\quad \\sigma_{\\text{rep}} \\le 2\\% \\quad ; \\quad p < 0.001"
            ejemplo: "Repositorio estructurado con scripts, parámetros de simulación y cuaderno de laboratorio."
            bloque_sugerido: "Trabajo Grado 50 min • Protocolo reproducible"
          - numero_tema: 3
            corte: 1
            modalidad: "tecnica"
            titulo: "Modelado Matemático, Simulación o Experimentación de Alta Precisión"
            objetivo: "Ejecutar el núcleo técnico del trabajo de grado verificando conservación física y convergencia."
            concepto_clave_latex: "\\|\\vec{R}(\\vec{x})\\|_\\infty < 10^{-6} \\quad ; \\quad \\varepsilon_{\\text{balance}} < 0.5\\%"
            ejemplo: "Verificación de cierre de balances de masa, energía y potencia en los resultados centrales."
            bloque_sugerido: "Trabajo Grado 50 min • Validación numérica/exp"
          - numero_tema: 4
            corte: 2
            modalidad: "tecnica"
            titulo: "Análisis Estadístico de Resultados, Incertidumbre y Sensibilidad"
            objetivo: "Contrastarlos frente a literatura científica internacional cuantificando barras de error y sensibilidad."
            concepto_clave_latex: "\\bar{y} \\pm U_{95\\%} \\quad ; \\quad \\Delta\\%_{\\text{vs. literatura}} = \\frac{y_{\\text{prop}} - y_{\\text{ref}}}{y_{\\text{ref}}}\\times 100\\%"
            ejemplo: "Discusión crítica de ventajas, límites de validez y casos borde de la solución propuesta."
            bloque_sugerido: "Trabajo Grado 50 min • Discusión crítica"
          - numero_tema: 5
            corte: 2
            modalidad: "tecnica"
            titulo: "Evaluación Tecnoeconómica, Regulatoria y Socioambiental del Trabajo de Grado"
            objetivo: "Demostrar la factibilidad integral de implementación en el contexto colombiano o global."
            concepto_clave_latex: "\\text{VPN} > 0 \\quad ; \\quad \\text{LCOE} \\le \\text{LCOE}_{\\text{red}} \\quad ; \\quad \\Delta\\text{CO}_2 < 0"
            ejemplo: "Capítulo de impacto económico, normativo y contribución a los ODS de la propuesta."
            bloque_sugerido: "Trabajo Grado 45 min • Impacto integral"
          - numero_tema: 6
            corte: 2
            modalidad: "tecnica"
            titulo: "Escritura Científica de la Monografía / Artículo y Visualización Vectorial"
            objetivo: "Redactar documento final con tipografía matemática impecable (LaTeX/KaTeX) y figuras de calidad editorial."
            concepto_clave_latex: "N_{\\text{citas}} \\ge 30 \\quad ; \\quad \\text{DPI} \\ge 300 \\quad ; \\quad [1\\dots N] \\in \\text{IEEE}"
            ejemplo: "Edición final libre de ambigüedades, plagio cero y cumplimiento de normas de Biblioteca."
            bloque_sugerido: "Escritura 50 min • Manuscrito final"
          - numero_tema: 7
            corte: 3
            modalidad: "tecnica"
            titulo: "Preparación de Diapositivas Ejecutivas y Discurso de Sustentación"
            objetivo: "Sintetizar 6 meses de trabajo en una presentación de alto impacto visual y claridad conceptual."
            concepto_clave_latex: "T_{\\text{sustentación}} \\le 20\\text{ min} \\quad ; \\quad \\Delta T_{\\text{preguntas}} \\le 10\\text{ min}"
            ejemplo: "Diseño minimalista de diapositivas enfocado en gráficas clave, aportes y conclusiones."
            bloque_sugerido: "Práctica Oral 45 min • Ensayo cronometrado"
          - numero_tema: 8
            corte: 3
            modalidad: "tecnica"
            titulo: "Defensa Pública ante Jurados Calificadores y Proyección Profesional"
            objetivo: "Responder con solvencia científica las preguntas del jurado y proyectar continuidad profesional/posgrado."
            concepto_clave_latex: "\\text{Graduado}_{\\text{Plan 8108}} \\implies \\text{Ingeniero Energético}"
            ejemplo: "Simulacro completo de defensa pública y entrega final a repositorio institucional."
            bloque_sugerido: "Simulacro Final 50 min • Defensa de Grado"
---

# Base de Datos Curricular Maestra — Ingeniería Energética (Plan 8108 / SNIES 118222)

Base de datos académica oficial para **UM STUDIO** (Universidad del Magdalena), estructurada con **YAML Frontmatter v3.0.0**.

- **51 Asignaturas Técnicas y Científicas:** 8 a 9 temas progresivos por asignatura distribuidos en los 3 cortes académicos (`Corte 1: 30%`, `Corte 2: 30%`, `Corte 3: 40%`) con formulación **KaTeX** verificada.
- **5 Niveles de Inglés (`01021802` a `01021806`):** Arquitectura dual con **80 temas totales** (50 temas en `modalidad: general` con presentaciones interactivas exportables a PDF `< 1.2 MB` y 30 temas en `modalidad: notacion_ingenieria` con KaTeX y verbalización técnica en inglés).

## Cuatrimestre 1 (14 créditos)

- **`02011807` — Cálculo Diferencial** (4 cr • 9 temas)
- **`03011813` — Fundamentos de Programación e IA** (4 cr • 9 temas)
- **`01021802` — General English I** (2 cr • 16 temas)
- **`04011822` — Introducción a la Ingeniería Energética** (2 cr • 8 temas)
- **`01011801` — Procesos Lectores, Escriturales y Orales** (2 cr • 8 temas)

## Cuatrimestre 2 (14 créditos)

- **`02021810` — Física Mecánica** (4 cr • 9 temas)
- **`03041819` — Fundamentos de la Electricidad I** (2 cr • 9 temas)
- **`01021803` — General English II** (2 cr • 16 temas)
- **`03031818` — Probabilidad y Estadística** (3 cr • 9 temas)
- **`02031812` — Química Aplicada** (3 cr • 9 temas)

## Cuatrimestre 3 (15 créditos)

- **`02011808` — Cálculo Integral** (4 cr • 9 temas)
- **`02021811` — Calor y Ondas** (4 cr • 9 temas)
- **`03041820` — Fundamentos de Electricidad II** (2 cr • 9 temas)
- **`03021815` — Fundamentos de Hidráulica y Neumática** (3 cr • 9 temas)
- **`01021804` — General English III** (2 cr • 16 temas)

## Cuatrimestre 4 (15 créditos)

- **`02011809` — Álgebra Lineal** (3 cr • 9 temas)
- **`06011837` — Conversión de Energía** (3 cr • 8 temas)
- **`03041821` — Electricidad y Magnetismo** (4 cr • 9 temas)
- **`01021805` — General English IV** (2 cr • 16 temas)
- **`03021817` — Termodinámica** (3 cr • 9 temas)

## Cuatrimestre 5 (15 créditos)

- **`06021845` — Energía Hidráulica** (3 cr • 8 temas)
- **`06021846` — Energía Solar Fotovoltaica** (3 cr • 8 temas)
- **`06011838` — Mediciones e Instrumentación** (3 cr • 8 temas)
- **`04021825` — Modelación Matemática para Ingeniería** (3 cr • 8 temas)
- **`06011839` — Sistemas Energéticos** (3 cr • 8 temas)

## Cuatrimestre 6 (13 créditos)

- **`01021806` — General English V** (2 cr • 16 temas)
- **`04021823` — Ingeniería del Diseño y Modelado en 3D** (3 cr • 8 temas)
- **`04031827` — Legislación y Regulación Energética** (3 cr • 8 temas)
- **`06011840` — Máquinas Eléctricas** (3 cr • 8 temas)
- **`05011834` — Proyecto Integrador CDIO I** (2 cr • 8 temas)

## Cuatrimestre 7 (15 créditos)

- **`06021850` — Energía de Biomasa** (3 cr • 8 temas)
- **`06021848` — Energía Eólica** (3 cr • 8 temas)
- **`06021847` — Energía Geotérmica** (3 cr • 8 temas)
- **`06021849` — Energía Mareomotriz** (3 cr • 8 temas)
- **`03021816` — Mecánica de Fluidos** (3 cr • 8 temas)

## Cuatrimestre 8 (14 créditos)

- **`04021824` — Diseño y Simulación de Sistemas Energéticos** (3 cr • 8 temas)
- **`04031828` — Energy Market** (3 cr • 8 temas)
- **`05011832` — Formulación de Proyectos** (3 cr • 8 temas)
- **`05011831` — Metodología de la Investigación** (2 cr • 8 temas)
- **`03011814` — Programación Avanzada y Aplicaciones de IA** (3 cr • 8 temas)

## Cuatrimestre 9 (14 créditos)

- **`04031829` — Comunidades Energéticas Sostenibles** (3 cr • 8 temas)
- **`04031826` — Gestión, Auditoría y Eficiencia Energética** (3 cr • 8 temas)
- **`06011842` — Instalaciones Eléctricas con Energías Renovables** (3 cr • 8 temas)
- **`05011835` — Proyecto Integrador CDIO II** (2 cr • 8 temas)
- **`06011841` — Transferencia de Calor** (3 cr • 8 temas)

## Cuatrimestre 10 (15 créditos)

- **`06011843` — Almacenamiento de la Energía** (3 cr • 8 temas)
- **`06021851` — Aprovechamiento de Fuentes Energéticas No Renovables** (3 cr • 8 temas)
- **`05011833` — Evaluación y Gestión de Proyectos** (3 cr • 8 temas)
- **`06021852` — Hydrogen Energy** (3 cr • 8 temas)
- **`07011855` — Inmersión Profesional** (3 cr • 8 temas)

## Cuatrimestre 11 (14 créditos)

- **`06031854` — Electiva Línea de Eficiencia Energética** (3 cr • 8 temas)
- **`06031853` — Electiva Línea de Fuentes de Energía** (3 cr • 8 temas)
- **`05011836` — Proyecto Integrador CDIO III** (2 cr • 8 temas)
- **`06011844` — Redes de Transporte y Distribución de la Energía** (3 cr • 8 temas)
- **`04031830` — Transición Energética Justa** (3 cr • 8 temas)

## Cuatrimestre 12 (4 créditos)

- **`07021856` — Modalidad de Grado** (4 cr • 8 temas)

