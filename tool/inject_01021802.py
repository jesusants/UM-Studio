# -*- coding: utf-8 -*-
import sys
import re
from injector_base import format_topic_yaml, format_topics_yaml, DB_PATH, ASSETS_PATH

# 5 New General English I topics (Temas 11 to 15)
new_general_topics = [
    {
        "numero_tema": 11,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Countable & Uncountable Nouns, Quantifiers in Technical Inventories",
        "objetivo": "Cuantificar inventarios de laboratorio, consumibles y componentes usando sustantivos contables e incontables.",
        "concepto_clave_latex": "",
        "ejemplo": "How much wire do we need? We need three meters of copper wire and many terminal connectors.",
        "bloque_sugerido": "Vocabulary Drill 30 min • Lab inventory and component quantities",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A1 • COMMUNICATIVE PURPOSE",
                "titulo": "Countable & Uncountable Nouns: Communicative Purpose",
                "puntos": [
                    "Countable nouns have singular and plural forms (one sensor, three sensors).",
                    "Uncountable nouns cannot be counted directly (electricity, water, flux, wire).",
                    "Use quantifiers (how much / how many) to inquire about lab stock."
                ],
                "ejemplo": "How many multimeter probes are in the drawer?"
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Core Grammatical Blueprint",
                "puntos": [
                    "Countable: How many + plural noun + are there?",
                    "Uncountable: How much + singular noun + is there?",
                    "Use 'a few' / 'many' for countable items; 'a little' / 'much' for uncountable matter."
                ]
            },
            {
                "numero": 3,
                "seccion": "INTERROGATIVE & SHORT ANSWERS",
                "titulo": "Inventory Questions and Confirmations",
                "puntos": [
                    "Is there any solder paste left? Yes, there is a little.",
                    "Are there any spare fuses in the toolbox? No, there aren't any."
                ]
            },
            {
                "numero": 4,
                "seccion": "KEY DISTINCTIONS & PITFALLS",
                "titulo": "Common Technical Traps",
                "puntos": [
                    "Never say 'two electricities' or 'three informations' (always uncountable).",
                    "Use partitives for uncountables: 'two reels of wire', 'three liters of oil'."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC USAGE",
                "titulo": "Lab Procurement Dialogue",
                "puntos": [
                    "Lead Engineer: 'We have enough solar cells, but we need more thermal paste.'",
                    "Technician: 'I will order three tubes of silicone adhesive immediately.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Fluency Practice",
                "puntos": [
                    "Practice asking for 5 common electrical workshop consumables.",
                    "State the quantity of components available in your station."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Past Simple: Regular & Irregular Verbs in Engineering History",
        "objetivo": "Describir eventos históricos, hitos energéticos y experimentos pasados usando el Pasado Simple.",
        "concepto_clave_latex": "",
        "ejemplo": "Nikola Tesla developed alternating current induction motors in the late nineteenth century.",
        "bloque_sugerido": "Reading & Speaking 35 min • Historical energy timeline",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A1 • COMMUNICATIVE PURPOSE",
                "titulo": "Past Simple: Communicative Purpose",
                "puntos": [
                    "Narrate completed actions in the past with specific time expressions (in 1888, yesterday, last semester).",
                    "Distinguish between regular (-ed suffix) and irregular verb past forms."
                ],
                "ejemplo": "Michael Faraday discovered electromagnetic induction in 1831."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Core Grammatical Blueprint",
                "puntos": [
                    "Affirmative: Subject + Verb in Past (invented / built / measured) + Complement.",
                    "Negative: Subject + did not (didn't) + base verb (didn't invent).",
                    "Question: Did + Subject + base verb? (Did James Watt invent the steam engine?)"
                ]
            },
            {
                "numero": 3,
                "seccion": "INTERROGATIVE & SHORT ANSWERS",
                "titulo": "Historical Q&A",
                "puntos": [
                    "Did Thomas Edison invent the light bulb? Yes, he improved the commercial filament.",
                    "When did the utility install the wind turbine? They installed it three weeks ago."
                ]
            },
            {
                "numero": 4,
                "seccion": "KEY DISTINCTIONS & PITFALLS",
                "titulo": "Pronunciation of -ed and Common Errors",
                "puntos": [
                    "Voiced /d/ after vowels and voiced consonants (measured, installed).",
                    "Voiceless /t/ after voiceless stops (tripped, checked).",
                    "Extra syllable /ɪd/ only after /t/ and /d/ (connected, recorded)."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC USAGE",
                "titulo": "Project Log History",
                "puntos": [
                    "'Yesterday the crew completed the trenching work and laid forty meters of cable.'",
                    "'The backup generator did not start because the starter battery was depleted.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Historical Milestone Drill",
                "puntos": [
                    "Pronounce 10 regular past verbs with correct /t/, /d/, and /ɪd/ endings.",
                    "Summarize last week's lab session in three past sentences."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Past Simple vs. Past Continuous: Lab Incidents & Field Work",
        "objetivo": "Reportar incidentes e interrupciones en plantas y laboratorios combinando Pasado Simple y Pasado Continuo con while y when.",
        "concepto_clave_latex": "",
        "ejemplo": "The technician was calibrating the inverter when the breaker tripped.",
        "bloque_sugerido": "Incident Reporting 30 min • Lab safety and event chronologies",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A1 • COMMUNICATIVE PURPOSE",
                "titulo": "Past Continuous: Communicative Purpose",
                "puntos": [
                    "Describe an ongoing background activity in the past interrupted by a punctual event.",
                    "Combine Past Continuous (was/were + -ing) with Past Simple using 'when' and 'while'."
                ],
                "ejemplo": "While the battery was charging, the cooling fan stopped."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Core Grammatical Blueprint",
                "puntos": [
                    "Long ongoing action: Subject + was/were + V-ing.",
                    "Short interrupting action: Past Simple.",
                    "While + Past Continuous, Past Simple: 'While we were testing, smoke appeared.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "INTERROGATIVE & SHORT ANSWERS",
                "titulo": "Incident Investigation Dialogue",
                "puntos": [
                    "What were you doing when the alarm sounded? I was recording the bus voltage.",
                    "Were the students wearing safety goggles during the test? Yes, they were."
                ]
            },
            {
                "numero": 4,
                "seccion": "KEY DISTINCTIONS & PITFALLS",
                "titulo": "Common Pitfalls",
                "puntos": [
                    "Do not use stative verbs in continuous form (know, believe, understand).",
                    "Do not confuse 'when' (often with past simple) and 'while' (often with continuous)."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC USAGE",
                "titulo": "Official Maintenance Incident Report",
                "puntos": [
                    "'At 14:30 hours, while technicians were inspecting the gearbox, a high vibration occurred.'",
                    "'The supervisory software was recording telemetry when the serial connection failed.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Safety Scenario Practice",
                "puntos": [
                    "Describe three simultaneous background events in a power station.",
                    "Construct an interruption sentence explaining an equipment trip."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Comparatives & Superlatives: Assessing Materials & Technical Specs",
        "objetivo": "Comparar especificaciones técnicas de paneles, turbinas y baterías usando adjetivos comparativos y superlativos.",
        "concepto_clave_latex": "",
        "ejemplo": "Monocrystalline silicon panels are more efficient than polycrystalline modules, but they are also more expensive.",
        "bloque_sugerido": "Technical Benchmarking 35 min • Comparing clean energy technologies",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A1 • COMMUNICATIVE PURPOSE",
                "titulo": "Comparative & Superlative: Communicative Purpose",
                "puntos": [
                    "Evaluate two technical options using comparatives (better, lighter, more efficient).",
                    "Highlight market leaders and physical limits using superlatives (the highest, the most reliable)."
                ],
                "ejemplo": "Lithium iron phosphate batteries are safer than cobalt-rich chemistries."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Core Grammatical Blueprint",
                "puntos": [
                    "Short adjectives: adj + -er + than (faster than, cheaper than).",
                    "Long adjectives: more + adj + than (more durable than).",
                    "Superlatives: the + adj + -est (the fastest) or the most + adj (the most efficient).",
                    "Irregulars: good -> better -> the best; bad -> worse -> the worst."
                ]
            },
            {
                "numero": 3,
                "seccion": "INTERROGATIVE & SHORT ANSWERS",
                "titulo": "Comparison Questions",
                "puntos": [
                    "Which inverter is more reliable? Model A is slightly more reliable than Model B.",
                    "Is aluminum lighter than copper? Yes, aluminum is significantly lighter than copper."
                ]
            },
            {
                "numero": 4,
                "seccion": "KEY DISTINCTIONS & PITFALLS",
                "titulo": "Common Pitfalls",
                "puntos": [
                    "Never say 'more cheaper' (double comparative error).",
                    "Always use 'than' after comparatives, never 'that' or 'as'."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC USAGE",
                "titulo": "Engineering Datasheet Evaluation",
                "puntos": [
                    "'The Pelton turbine demonstrates the highest hydraulic efficiency for high-head installations.'",
                    "'Optical fibre offers much higher bandwidth than standard coaxial cable.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Datasheet Pitch",
                "puntos": [
                    "Compare two solar panel technologies using 3 comparative adjectives.",
                    "Present the superlative properties of an advanced energy material."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Future Forms (Will, Be Going To) for Project Milestones & Weather",
        "objetivo": "Expresar planes futuros, predicciones climáticas y cronogramas de proyectos energéticos usando will y be going to.",
        "concepto_clave_latex": "",
        "ejemplo": "The solar farm is going to be commissioned next month. Cloud cover will decrease tomorrow afternoon.",
        "bloque_sugerido": "Project Planning 35 min • Timeline presentations and milestone pitches",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A1 • COMMUNICATIVE PURPOSE",
                "titulo": "Future Forms: Communicative Purpose",
                "puntos": [
                    "Use 'will' for spontaneous decisions, objective facts, and predictions.",
                    "Use 'be going to' for planned project milestones and evidence-based predictions."
                ],
                "ejemplo": "Look at the overcast sky; solar output is going to drop in ten minutes."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Core Grammatical Blueprint",
                "puntos": [
                    "Will: Subject + will / won't + base verb.",
                    "Be going to: Subject + am/is/are + going to + base verb.",
                    "Time markers: next week, tomorrow, by the end of the semester."
                ]
            },
            {
                "numero": 3,
                "seccion": "INTERROGATIVE & SHORT ANSWERS",
                "titulo": "Milestone Planning Dialogue",
                "puntos": [
                    "When are you going to present the project draft? We are going to present it on Friday.",
                    "Will the microgrid operate autonomously during the outage? Yes, it will."
                ]
            },
            {
                "numero": 4,
                "seccion": "KEY DISTINCTIONS & PITFALLS",
                "titulo": "Will vs. Be Going To Nuances",
                "puntos": [
                    "Do not use 'will' for established scheduled calendar events with firm prior commitment.",
                    "Always use base form after 'will' (never 'will goes' or 'will to go')."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC USAGE",
                "titulo": "Commissioning Schedule Pitch",
                "puntos": [
                    "'The EPC contractor is going to energize the main transformer tomorrow morning.'",
                    "'Long-term meteorological models predict that annual solar insolation will increase slightly.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Project Roadmap Drill",
                "puntos": [
                    "State three milestones you are going to complete before the final examination.",
                    "Make two future predictions regarding the Colombian national grid."
                ]
            }
        ]
    }
]

# 9 New Notación de Ingeniería topics (Temas 22 to 30)
new_notacion_topics = [
    {
        "numero_tema": 22,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Linear Equations, Proportions & Variations in Physical Systems",
        "objetivo": "Expresar relaciones de proporcionalidad directa e inversa y ecuaciones lineales en inglés técnico.",
        "concepto_clave_latex": r"y = k x \iff \frac{y_1}{x_1} = \frac{y_2}{x_2} \quad ; \quad P \propto \frac{1}{R}",
        "verbalizacion_ingles": "• y = k x -> \"y is directly proportional to x with proportionality constant k\".\n• P ∝ 1/R -> \"power is inversely proportional to resistance\".",
        "ejemplo": "En balances de circuitos: 'Current is directly proportional to voltage and inversely proportional to total circuit resistance'.",
        "bloque_sugerido": "Oral Pronunciation 30 min • Verbalizing proportionality laws"
    },
    {
        "numero_tema": 23,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Algebraic Formulas, Polynomials & Factoring Notation",
        "objetivo": "Verbalizar polinomios, productos notables y factorizaciones algebraicas con precisión fonética.",
        "concepto_clave_latex": r"(a + b)^2 = a^2 + 2ab + b^2 \quad ; \quad a^2 - b^2 = (a - b)(a + b)",
        "verbalizacion_ingles": "• (a + b)^2 -> \"the quantity a plus b squared equals a squared plus two a b plus b squared\".\n• a^2 - b^2 -> \"a squared minus b squared equals the quantity a minus b times the quantity a plus b\".",
        "ejemplo": "En derivaciones analíticas: 'Expand the binomial squared into the square of the first term plus twice the product of both terms plus the square of the second'.",
        "bloque_sugerido": "Oral Drill 30 min • Factoring and polynomial verbalization"
    },
    {
        "numero_tema": 24,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Cartesian Coordinates, Quadrants, Slopes & Linear Graphs",
        "objetivo": "Describir planos cartesianos, pendientes de curvas y puntos de intersección en inglés técnico.",
        "concepto_clave_latex": r"m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x} \quad ; \quad y - y_0 = m(x - x_0)",
        "verbalizacion_ingles": "• m = Δy / Δx -> \"the slope m equals delta y over delta x\" (or \"rise over run\").\n• y - y_0 = m(x - x_0) -> \"point-slope form: y minus y-naught equals m times the quantity x minus x-naught\".",
        "ejemplo": "Al analizar curvas I-V: 'The slope of the linear region represents the internal conductance of the photovoltaic cell'.",
        "bloque_sugerido": "Speaking Practice 30 min • Graph interpretations and slopes"
    },
    {
        "numero_tema": 25,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Trigonometric Ratios (Sine, Cosine, Tangent) & Right-Triangle Triangulation",
        "objetivo": "Pronunciar razones trigonométricas fundamentales e identidades pitagóricas en inglés académico.",
        "concepto_clave_latex": r"\sin(\theta) = \frac{\text{opp}}{\text{hyp}} \quad ; \quad \tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} \quad ; \quad \sin^2(\theta) + \cos^2(\theta) = 1",
        "verbalizacion_ingles": "• sin(θ) = opp / hyp -> \"sine of theta equals opposite over hypotenuse\".\n• tan(θ) -> \"tangent of theta equals sine of theta over cosine of theta\".\n• sin^2(θ) + cos^2(θ) = 1 -> \"sine squared of theta plus cosine squared of theta equals one\".",
        "ejemplo": "En el triángulo de potencias: 'The cosine of angle phi is the power factor of the inductive load'.",
        "bloque_sugerido": "Oral Drill 30 min • Trigonometric functions and power triangle"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Vectors in 2D/3D: Magnitude, Direction, Dot & Cross Product Notation",
        "objetivo": "Verbalizar operaciones vectoriales, producto escalar y producto vectorial en inglés técnico.",
        "concepto_clave_latex": r"\vec{A} \cdot \vec{B} = \|\vec{A}\|\|\vec{B}\|\cos(\theta) \quad ; \quad \vec{\tau} = \vec{r} \times \vec{F}",
        "verbalizacion_ingles": "• A · B -> \"vector A dot vector B equals magnitude of A times magnitude of B times cosine of theta\".\n• r × F -> \"vector r cross vector F yields torque vector tau\".",
        "ejemplo": "En electromagnetismo y mecánica: 'The mechanical torque is computed as the cross product between the position vector and the force vector'.",
        "bloque_sugerido": "Oral Practice 30 min • Vector dot and cross product pronunciation"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Logarithms (Natural & Base-10), Exponential Growth & Decibel Scales",
        "objetivo": "Leer funciones logarítmicas, exponentes neperianos y escalas logarítmicas de decibelios en inglés.",
        "concepto_clave_latex": r"\ln(x) = \log_e(x) \quad ; \quad \text{dB} = 10 \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)",
        "verbalizacion_ingles": "• ln(x) -> \"natural logarithm of x\" (or \"log base e of x\").\n• 10 log_10(P_out / P_in) -> \"ten times the base-ten logarithm of the ratio of output power to input power, measured in decibels\".",
        "ejemplo": "En atenuación de líneas y filtros: 'The gain of the inverter low-pass filter is minus three decibels at the cutoff frequency'.",
        "bloque_sugerido": "Speaking Drill 30 min • Logarithmic and exponential notation"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Summation (Sigma), Products (Pi) & Series Expansion in Calculus",
        "objetivo": "Verbalizar operadores de sumatoria, productorias y expansiones en serie de potencias en inglés.",
        "concepto_clave_latex": r"\sum_{i=1}^n x_i \quad ; \quad \prod_{j=1}^m p_j \quad ; \quad e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}",
        "verbalizacion_ingles": "• sum_{i=1}^n x_i -> \"the summation of x sub i from i equals one to n\".\n• prod_{j=1}^m p_j -> \"the product of p sub j from j equals one to m\".\n• e^x -> \"e to the x equals the sum from k equals zero to infinity of x to the k over k factorial\".",
        "ejemplo": "En balances anuales: 'Total annual solar irradiation is the sum of hourly global horizontal irradiance across all eight thousand seven hundred sixty hours'.",
        "bloque_sugerido": "Oral Practice 30 min • Summation, product and series verbalization"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Complex Numbers, Imaginary Unit (j), Phasors & Polar/Rectangular Forms",
        "objetivo": "Pronunciar números complejos, fasores de corriente alterna y conversiones polar/rectangular en inglés.",
        "concepto_clave_latex": r"\mathbf{Z} = R + jX = |\mathbf{Z}|\angle\theta \quad ; \quad |\mathbf{Z}| = \sqrt{R^2 + X^2}",
        "verbalizacion_ingles": "• Z = R + jX -> \"impedance Z equals resistance R plus j times reactance X in rectangular form\".\n• |Z|∠θ -> \"magnitude of Z at an angle of theta degrees in polar notation\".",
        "ejemplo": "En análisis AC: 'The branch impedance is ten plus j five ohms, or eleven point one eight ohms at an angle of twenty-six point five degrees'.",
        "bloque_sugerido": "Oral Drill 30 min • Complex numbers, phasors and impedance"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Dimensional Analysis, Matrix Dimensions & Engineering Sanity Checks",
        "objetivo": "Verbalizar análisis dimensional de unidades compuestas y dimensiones matriciales en inglés técnico.",
        "concepto_clave_latex": r"[E] = [M][L]^2[T]^{-2} = \text{kg}\cdot\text{m}^2/\text{s}^2 = \text{J} \quad ; \quad \mathbf{A}_{m \times p} \mathbf{B}_{p \times n} = \mathbf{C}_{m \times n}",
        "verbalizacion_ingles": "• [E] = [M][L]^2[T]^-2 -> \"the dimension of energy is mass times length squared times time to the minus two, or kilograms meters squared per second squared, which equals joules\".\n• A_{m x p} B_{p x n} -> \"matrix A of size m by p times matrix B of size p by n yields matrix C of size m by n\".",
        "ejemplo": "En revisión de diseños: 'Perform a dimensional check to confirm that both sides of the energy conservation equation equate to joules'.",
        "bloque_sugerido": "Speaking Practice 30 min • Dimensional units and matrix dimensions"
    }
]

def upgrade_english_1():
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    
    idx1 = content.find('      - codigo: "01021802"')
    idx2 = content.find('      - codigo: "04011822"')
    if idx1 == -1 or idx2 == -1:
        print("ERROR: Could not find English I section in DB.")
        sys.exit(1)
        
    asig_block = content[idx1:idx2]
    
    # 1. Insert new general topics 11 to 15 right before the first notacion topic (tema 11)
    split_marker = '          - numero_tema: 11\n            corte: 1\n            modalidad: "notacion_ingenieria"'
    if split_marker not in asig_block:
        print("ERROR: Split marker for tema 11 not found.")
        sys.exit(1)
        
    new_gen_yaml = format_topics_yaml(new_general_topics)
    asig_block = asig_block.replace(split_marker, new_gen_yaml + split_marker, 1)
    
    # 2. Renumber existing notacion topics:
    # 11 -> 16, 12 -> 17, 13 -> 18, 14 -> 19, 15 -> 20, 16 -> 21
    # Note: renumber in descending order to avoid collisions!
    asig_block = asig_block.replace('numero_tema: 16\n            corte: 3\n            modalidad: "notacion_ingenieria"', 'numero_tema: 21\n            corte: 3\n            modalidad: "notacion_ingenieria"')
    asig_block = asig_block.replace('numero_tema: 15\n            corte: 3\n            modalidad: "notacion_ingenieria"', 'numero_tema: 20\n            corte: 3\n            modalidad: "notacion_ingenieria"')
    asig_block = asig_block.replace('numero_tema: 14\n            corte: 2\n            modalidad: "notacion_ingenieria"', 'numero_tema: 19\n            corte: 2\n            modalidad: "notacion_ingenieria"')
    asig_block = asig_block.replace('numero_tema: 13\n            corte: 2\n            modalidad: "notacion_ingenieria"', 'numero_tema: 18\n            corte: 2\n            modalidad: "notacion_ingenieria"')
    asig_block = asig_block.replace('numero_tema: 12\n            corte: 1\n            modalidad: "notacion_ingenieria"', 'numero_tema: 17\n            corte: 1\n            modalidad: "notacion_ingenieria"')
    asig_block = asig_block.replace('numero_tema: 11\n            corte: 1\n            modalidad: "notacion_ingenieria"', 'numero_tema: 16\n            corte: 1\n            modalidad: "notacion_ingenieria"')
    
    # 3. Append new notacion topics 22 to 30 at the end of asig_block
    new_not_yaml = format_topics_yaml(new_notacion_topics)
    asig_block = asig_block + new_not_yaml
    
    new_content = content[:idx1] + asig_block + content[idx2:]
    
    open(DB_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    open(ASSETS_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    print("01021802 General English I successfully expanded to 30 topics (15 General + 15 Notación)!")

if __name__ == '__main__':
    upgrade_english_1()
