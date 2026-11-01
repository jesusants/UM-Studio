# -*- coding: utf-8 -*-
import sys
import re
from injector_base import format_topic_yaml, format_topics_yaml, DB_PATH, ASSETS_PATH

# 5 New General English II topics (Temas 11 to 15)
new_general_topics = [
    {
        "numero_tema": 11,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Passive Voice in Technical Workflows & Lab Reports",
        "objetivo": "Describir procedimientos de laboratorio y montajes experimentales en voz pasiva estándar en inglés técnico.",
        "concepto_clave_latex": "",
        "ejemplo": "The high-voltage capacitor is discharged through a bleeder resistor before any measurement is taken.",
        "bloque_sugerido": "Speaking Drill 30 min • Passive voice in industrial lab workflows",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A2 • COMMUNICATIVE PURPOSE",
                "titulo": "Passive Voice: Object Focus & Objectivity",
                "puntos": [
                    "Technical writing prioritizes the action and the component rather than the human actor.",
                    "Active: 'The technician calibrated the pyranometer.' -> Passive: 'The pyranometer was calibrated.'",
                    "Used extensively in scientific abstracts, operation manuals, and audit logs."
                ],
                "ejemplo": "The solar panel was oriented at an optimal tilt of eleven degrees north."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Morphological Blueprint (Be + Past Participle)",
                "puntos": [
                    "Present Simple Passive: Subject + is / are + past participle (V3).",
                    "Past Simple Passive: Subject + was / were + past participle (V3).",
                    "Modal Passive: Subject + must / should / can + be + past participle."
                ]
            },
            {
                "numero": 3,
                "seccion": "TECHNICAL PROCESS DESCRIPTION",
                "titulo": "Step-by-Step Electrical Assembly",
                "puntos": [
                    "First, the circuit breaker is opened and locked out.",
                    "Next, insulated copper conductors are crimped to ring terminals.",
                    "Finally, torque specifications are verified with an electronic wrench."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Avoid Redundant Agent Phrases",
                "puntos": [
                    "Do not include 'by the student' or 'by us' unless the specific investigator is vital.",
                    "Never omit the auxiliary verb 'be' (incorrect: 'The voltage measured at 24 V').",
                    "Irregular participles: run/run/run, build/built/built, choose/chose/chosen."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC LABORATORY SCRIPT",
                "titulo": "Battery Testing Protocol",
                "puntos": [
                    "Lab Supervisor: 'The lithium iron phosphate cells are conditioned at 0.5C.'",
                    "Student: 'Ambient temperature is maintained at twenty-five degrees Celsius throughout the charge cycle.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Fluency Practice: Lab Procedures",
                "puntos": [
                    "Convert 3 active maintenance statements into impersonal passive voice.",
                    "Present the commissioning protocol of a wind turbine nacelle in 4 passive sentences."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Zero & First Conditionals: Cause, Effect & Operational Thresholds",
        "objetivo": "Expresar verdades científicas, leyes físicas y advertencias de umbral operativo mediante condicionales cero y primero.",
        "concepto_clave_latex": "",
        "ejemplo": "If the photovoltaic junction temperature exceeds seventy-five degrees Celsius, system efficiency drops significantly.",
        "bloque_sugerido": "Technical Dialogue 30 min • Cause and effect conditionals in power plants",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A2 • COMMUNICATIVE PURPOSE",
                "titulo": "Conditionals: Scientific Laws & Operational Safeguards",
                "puntos": [
                    "Zero Conditional expresses universal physical phenomena, deterministic rules, and immutable laws.",
                    "First Conditional expresses real, probable future outcomes triggered by a specific operational condition.",
                    "Essential for programmable logic controller (PLC) logic, safety interlocks, and alarm hierarchies."
                ],
                "ejemplo": "If current flows through a resistor, thermal energy is dissipated."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Syntactic Architecture",
                "puntos": [
                    "Zero Conditional: If / When + present simple, ... present simple.",
                    "First Conditional: If + present simple, ... will / can / must + base verb.",
                    "Alternative trigger clauses: 'Unless' (meaning if not), 'Provided that', 'As long as'."
                ]
            },
            {
                "numero": 3,
                "seccion": "SAFETY INTERLOCK SCENARIOS",
                "titulo": "Industrial Substation Safeguards",
                "puntos": [
                    "If oil temperature rises above eighty degrees, the cooling fans engage automatically.",
                    "Unless grounding leads are secured, operators will not energize the busbar.",
                    "If gas pressure drops below nominal, the relay will trip the feeder."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Tense Concordance Hazards",
                "puntos": [
                    "Never use 'will' in the 'if'-clause (incorrect: 'If voltage will rise...').",
                    "Do not confuse cause and effect order: maintain clear logical antecedents.",
                    "Use precise threshold adverbs: 'strictly above', 'substantially lower', 'within limits'."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC CONTROL ROOM DIALOGUE",
                "titulo": "Inverter Alarm Management",
                "puntos": [
                    "Operator: 'What happens if grid frequency drops below 59.5 Hz?'",
                    "Engineer: 'If grid frequency drops below that threshold, the inverter will disconnect within 160 milliseconds.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Live Safety Briefing",
                "puntos": [
                    "Formulate 3 zero-conditional physical principles governing thermodynamic cycles.",
                    "Formulate 3 first-conditional warnings for a biomass gasifier plant."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Describing Trends, Rates of Change & Graphical Data",
        "objetivo": "Describir variaciones dinámicas de potencia, irradiancia y carga eléctrica a partir de curvas y gráficos en inglés.",
        "concepto_clave_latex": "",
        "ejemplo": "Peak electricity demand increased steadily from 6 PM to 9 PM, reaching an all-time high of twelve gigawatts.",
        "bloque_sugerido": "Graph Interpretation 30 min • Describing dynamic load profiles and curves",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A2 • COMMUNICATIVE PURPOSE",
                "titulo": "Communicating Dynamic Trajectories",
                "puntos": [
                    "Engineers must articulate quantitative changes over time during design reviews and generation briefings.",
                    "Distinguish between continuous trends, abrupt spikes, plateau periods, and cyclical fluctuations.",
                    "Pair strong trajectory verbs with precise degree adverbs."
                ],
                "ejemplo": "Solar generation rose sharply at sunrise and plateaued around solar noon."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Vocabulary Toolkit: Verbs & Adverbs",
                "puntos": [
                    "Upward trends: increase, rise, climb, surge, escalate, peak at.",
                    "Downward trends: decrease, drop, fall, plummet, decline, bottom out at.",
                    "Stability & Fluctuation: level off, remain steady, oscillate, fluctuate between X and Y.",
                    "Degree & Speed: sharply, steadily, gradually, marginal, dramatically."
                ]
            },
            {
                "numero": 3,
                "seccion": "DUAL GRAMMATICAL STRUCTURES",
                "titulo": "Verb + Adverb vs Adjective + Noun",
                "puntos": [
                    "Pattern A: 'Wind generation dropped steeply in the early morning.'",
                    "Pattern B: 'There was a steep drop in wind generation in the early morning.'",
                    "Preposition usage: 'an increase OF 15%', 'rose FROM 20 MW TO 35 MW', 'peaked AT 50 MW'."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Prepositional Accuracy in Trends",
                "puntos": [
                    "Do not confuse 'rise' (intransitive) with 'raise' (transitive requiring an object).",
                    "Avoid vague descriptors: quantify magnitude with SI units whenever possible.",
                    "Watch out for false cognates (e.g., 'actual' means present/current, not actual)."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC DISPATCH REPORT",
                "titulo": "National Grid Load Dispatcher Log",
                "puntos": [
                    "Dispatcher: 'Demand showed a moderate recovery following the midday slump.'",
                    "Analyst: 'Hydro reserves fell steadily over the dry quarter, stabilizing at 42% capacity.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Curve Description Practice",
                "puntos": [
                    "Describe the standard duck curve of solar-dominated electric grids in 4 sentences.",
                    "Contrast seasonal irradiance variations between summer and winter solstice."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Expressing Modality: Obligation, Permission & Technical Recommendations",
        "objetivo": "Emplear verbos modales de obligación, permisión y recomendación en normativas eléctricas (RETIE, NEC e IEC).",
        "concepto_clave_latex": "",
        "ejemplo": "All metal enclosures must be solidly bonded to the grounding electrode system under RETIE standards.",
        "bloque_sugerido": "Standards Drill 30 min • Modal verbs in electrical compliance codes",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A2 • COMMUNICATIVE PURPOSE",
                "titulo": "Regulatory Mandates & Safe Practice",
                "puntos": [
                    "Engineering codes enforce distinct levels of necessity: mandatory rules, strong recommendations, and options.",
                    "Clear modal differentiation prevents catastrophic compliance breaches and safety hazards.",
                    "Underpins international norms (IEC 60364, IEEE 1547, Colombian RETIE)."
                ],
                "ejemplo": "Personnel shall wear personal protective equipment rated for arc flash category 2."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Modal Hierarchy in Engineering",
                "puntos": [
                    "Strict Legal Obligation: Must / Shall + base verb ('All conductors must be rated for 90°C').",
                    "Prohibition: Must not / Shall not ('Neutral and ground must not be bonded downstream').",
                    "Best Practice / Recommendation: Should / Ought to ('Inverters should be installed in shaded enclosures').",
                    "Permission / Capability: May / Can ('Conduits may be embedded in concrete slabs')."
                ]
            },
            {
                "numero": 3,
                "seccion": "TECHNICAL REGULATORY CLAUSES",
                "titulo": "RETIE Compliance Examples",
                "puntos": [
                    "Substations must have an emergency shutdown push button near each egress door.",
                    "Engineers should calculate short-circuit duty before selecting switchgear interrupt ratings.",
                    "Technicians may use thermal imaging cameras to inspect busbar terminations."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Modal Confusion Pitfalls",
                "puntos": [
                    "Never add '-s' or 'to' after modal verbs (incorrect: 'He musts to inspect').",
                    "Do not soften mandatory requirements into suggestions: use 'must' for life-safety rules.",
                    "'Have to' vs 'Must': 'Must' denotes internal/authoritative rule; 'Have to' expresses external circumstance."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUDIT INSPECTION SCRIPT",
                "titulo": "Site Safety Compliance Walkthrough",
                "puntos": [
                    "Lead Auditor: 'Does this disconnect meet lockout-tagout requirements?'",
                    "Resident Engineer: 'Yes, it can be padlocked in the open position, and warning tags must be affixed.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Compliance Briefing",
                "puntos": [
                    "State 3 mandatory RETIE rules for residential rooftop PV installations.",
                    "State 2 optional recommendations for optimizing inverter heat dissipation."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Sequencing Complex Engineering Projects & Milestones",
        "objetivo": "Estructurar cronogramas, etapas constructivas y secuencias de energización usando conectores temporales formales.",
        "concepto_clave_latex": "",
        "ejemplo": "Prior to synchronization, phase angle and voltage magnitude were carefully aligned with the utility grid.",
        "bloque_sugerido": "Project Management Drill 30 min • Gantt chart milestones and sequencing",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR A2 • COMMUNICATIVE PURPOSE",
                "titulo": "Temporal Cohesion in Project Execution",
                "puntos": [
                    "Capital energy projects proceed through strict developmental phases (feasibility, EPC, commissioning, COD).",
                    "Engineers must communicate dependencies, critical paths, and milestone completions clearly.",
                    "Enables transparent coordination across multi-disciplinary international teams."
                ],
                "ejemplo": "Following civil foundation curing, steel racking structures were bolted into place."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Chronological & Sequential Discourse Markers",
                "puntos": [
                    "Initiation: Initially, First of all, In the preliminary phase, To begin with.",
                    "Progression: Subsequently, Following that, Concurrently, Meanwhile, In parallel.",
                    "Prerequisites: Prior to + noun / -ing, Before proceeding with, Once the tests are concluded.",
                    "Completion: Eventually, Finally, Upon achieving commercial operation date (COD)."
                ]
            },
            {
                "numero": 3,
                "seccion": "COMMISSIONING SCHEDULE",
                "titulo": "Photovoltaic Farm Energization Steps",
                "puntos": [
                    "First, insulation resistance testing was performed on all direct current strings.",
                    "Subsequently, the medium-voltage transformer was backfed from the substation.",
                    "Concurrently, supervisory control and data acquisition (SCADA) telemetry was validated.",
                    "Finally, inverters were released for grid synchronization."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Punctuation & Syntax of Connectors",
                "puntos": [
                    "Always set off introductory sequential adverbs with a comma (e.g., 'Subsequently, the crew...').",
                    "Do not confuse 'During' (preposition + noun) with 'While' (conjunction + clause).",
                    "Distinguish 'at the end' (point in time) from 'in the end' (ultimate resolution)."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC STAKEHOLDER UPDATE",
                "titulo": "EPC Project Status Meeting",
                "puntos": [
                    "Project Manager: 'Once geotechnical permits are cleared, grading works will commence.'",
                    "Site Engineer: 'Meanwhile, balance-of-system components will be staged at the laydown yard.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Project Milestone Walkthrough",
                "puntos": [
                    "Deliver a 1-minute oral progress report outlining the 4 primary stages of a microgrid project.",
                    "Explain 2 parallel tasks that must occur concurrently during plant commissioning."
                ]
            }
        ]
    }
]

# 9 New Notación de Ingeniería topics (Temas 22 to 30)
new_notacion_topics = [
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Ohm's Law, Joule's Heating & Electrical Power Formulations",
        "objetivo": "Expresar verbalmente formulaciones de potencia eléctrica, caída de tensión y ley de Joule con unidades SI.",
        "concepto_clave_latex": r"P = V I = I^2 R = \frac{V^2}{R} \quad [\text{W}] \quad ; \quad \Delta V = I R \quad [\text{V}] \quad ; \quad E_J = \int_0^t P(\tau) \, d\tau \quad [\text{J}]",
        "verbalizacion_ingles": "• P = V * I -> \"electrical power equals voltage times current, or current squared times resistance, or voltage squared divided by resistance, measured in watts\".\n• Delta V = I * R -> \"voltage drop equals current times resistance, measured in volts\".\n• E_J = integral from 0 to t of P(tau) d tau -> \"energy dissipated as heat equals the integral of instantaneous power with respect to time, measured in joules\".",
        "ejemplo": "En cálculo de conductores: 'The conductor line loss is four hundred watts due to copper resistance of zero point two five ohms under forty amperes of load current'.",
        "bloque_sugerido": "Speaking Drill 30 min • Electric circuit laws, power dissipations and losses"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Kinematic Equations, Gravitational Potential & Kinetic Energy",
        "objetivo": "Articular ecuaciones de movimiento rectilíneo uniformemente acelerado y balances de energía mecánica en inglés.",
        "concepto_clave_latex": r"v(t) = v_0 + a t \quad ; \quad x(t) = x_0 + v_0 t + \frac{1}{2} a t^2 \quad ; \quad E_m = \frac{1}{2} m v^2 + m g h \quad [\text{J}]",
        "verbalizacion_ingles": "• v(t) = v_0 + a * t -> \"velocity as a function of time equals initial velocity plus acceleration times time, measured in meters per second\".\n• x(t) = x_0 + v_0 t + 1/2 a t^2 -> \"position equals initial position plus initial velocity times time plus one-half acceleration times time squared, in meters\".\n• E_m = 1/2 m v^2 + m g h -> \"total mechanical energy equals one-half mass times velocity squared plus mass times gravitational acceleration times height, in joules\".",
        "ejemplo": "En análisis de aerogeneradores: 'Calculate the tip speed ratio where linear blade tip velocity equals angular velocity times rotor radius'.",
        "bloque_sugerido": "Pronunciation Practice 30 min • Kinematic formulas and kinetic energy"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Newton's Second Law, Work Integrals & Conservative Force Fields",
        "objetivo": "Verbalizar dinámica newtoniana, integrales de línea de trabajo mecánico y energía potencial en inglés técnico.",
        "concepto_clave_latex": r"\sum \mathbf{F} = m \mathbf{a} \quad [\text{N}] \quad ; \quad W = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} \quad [\text{J}] \quad ; \quad \mathbf{F} = -\nabla U",
        "verbalizacion_ingles": "• sum F = m * a -> \"the sum of forces equals mass times acceleration, measured in newtons\".\n• W = integral from r_1 to r_2 of F dot d r -> \"work equals the line integral of force dot differential displacement, in joules\".\n• F = - grad U -> \"a conservative force equals the negative gradient of potential energy\".",
        "ejemplo": "En diseño hidroeléctrico: 'The net hydraulic work delivered to the Pelton turbine runner is the integral of the water jet force dot displacement'.",
        "bloque_sugerido": "Technical Dialogue 30 min • Vector forces, line integrals and work"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Universal Gravitation, Centripetal Acceleration & Orbital Dynamics",
        "objetivo": "Expresar en inglés gravitación universal, aceleración centrípeta y velocidades orbitales de satélites terrestres.",
        "concepto_clave_latex": r"F_g = G \frac{m_1 m_2}{r^2} \quad [\text{N}] \quad ; \quad a_c = \frac{v^2}{r} = \omega^2 r \quad [\text{m/s}^2] \quad ; \quad v_{orb} = \sqrt{\frac{G M_E}{r}}",
        "verbalizacion_ingles": "• F_g = G * (m_1 * m_2) / r^2 -> \"gravitational force equals big G times mass one times mass two divided by distance squared, in newtons\".\n• a_c = v^2 / r = omega^2 * r -> \"centripetal acceleration equals linear velocity squared over radius, which equals angular velocity squared times radius\".\n• v_orb = sqrt(G * M_E / r) -> \"orbital velocity equals the square root of universal gravitational constant times Earth's mass divided by orbital radius\".",
        "ejemplo": "En satélites heliosincrónicos: 'Solar monitoring satellites require a circular orbit where centripetal force exactly balances gravitational attraction'.",
        "bloque_sugerido": "Oral Drill 30 min • Orbital mechanics and centripetal acceleration"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Simple Harmonic Motion, Frequency, Period & Damping Envelopes",
        "objetivo": "Articular movimiento armónico simple, frecuencia angular, amortiguamiento y factor de calidad en inglés.",
        "concepto_clave_latex": r"x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi) \quad ; \quad \omega_0 = \sqrt{\frac{k}{m}} \quad [\text{rad/s}] \quad ; \quad f = \frac{1}{T} = \frac{\omega}{2\pi} \quad [\text{Hz}]",
        "verbalizacion_ingles": "• x(t) = A e^(-gamma t) cos(omega_d t + phi) -> \"position equals amplitude times exponential of minus gamma t times cosine of damped angular frequency t plus phase angle phi\".\n• omega_0 = sqrt(k / m) -> \"undamped natural angular frequency equals the square root of spring stiffness k divided by mass m, in radians per second\".\n• f = 1 / T = omega / (2 pi) -> \"cyclic frequency equals one over period T, or angular frequency over two pi, measured in hertz\".",
        "ejemplo": "En vibraciones de aerogeneradores: 'Resonance must be avoided by ensuring the tower natural frequency differs from the rotor passing frequency'.",
        "bloque_sugerido": "Speaking Practice 30 min • Harmonic oscillations, resonance and frequencies"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Linear Momentum, Impulse Theorem & Elastic Collisions",
        "objetivo": "Verbalizar teoremas de cantidad de movimiento lineal, impulso mecánico y coeficientes de restitución en inglés.",
        "concepto_clave_latex": r"\mathbf{p} = m \mathbf{v} \quad [\text{kg}\cdot\text{m/s}] \quad ; \quad \mathbf{J} = \int_{t_1}^{t_2} \mathbf{F} \, dt = \Delta \mathbf{p} \quad [\text{N}\cdot\text{s}] \quad ; \quad e = \frac{v_{2f} - v_{1f}}{v_{1i} - v_{2i}}",
        "verbalizacion_ingles": "• p = m * v -> \"linear momentum equals mass times velocity, measured in kilogram meters per second\".\n• J = integral from t_1 to t_2 of F dt = Delta p -> \"impulse equals the definite integral of force over time, which equals the change in momentum, in newton seconds\".\n• e = (v_2f - v_1f) / (v_1i - v_2i) -> \"coefficient of restitution equals relative separation velocity divided by relative approach velocity\".",
        "ejemplo": "En impacto de fluidos: 'The momentum change of the steam jet against the impulse blade generates the driving torque'.",
        "bloque_sugerido": "Oral Drill 30 min • Impulse-momentum theorem and elastic collisions"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Rotational Dynamics, Moment of Inertia & Angular Momentum",
        "objetivo": "Expresar en inglés torque, momento de inercia y conservación de momento angular en rotores y turbinas.",
        "concepto_clave_latex": r"\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F} \quad [\text{N}\cdot\text{m}] \quad ; \quad I = \int r^2 \, dm \quad [\text{kg}\cdot\text{m}^2] \quad ; \quad \mathbf{L} = I \boldsymbol{\omega} = \text{const.}",
        "verbalizacion_ingles": "• tau = r cross F -> \"torque equals lever arm vector r cross product with force vector F, measured in newton meters\".\n• I = integral of r squared dm -> \"moment of inertia equals the integral of distance squared with respect to mass element dm, in kilogram meters squared\".\n• L = I * omega = const -> \"angular momentum equals moment of inertia times angular velocity vector, which remains constant in an isolated system\".",
        "ejemplo": "En almacenamiento en volantes de inercia (flywheels): 'Rotational kinetic energy stored in the rotor is one-half I omega squared'.",
        "bloque_sugerido": "Pronunciation Drill 30 min • Torques, rotational inertia and angular momentum"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Capacitance, Electric Field Energy Density & Dielectric Breakdown",
        "objetivo": "Verbalizar capacitancia, densidad de energía electrostática y rigidez dieléctrica en inglés técnico.",
        "concepto_clave_latex": r"C = \frac{\varepsilon_0 \varepsilon_r A}{d} \quad [\text{F}] \quad ; \quad u_E = \frac{1}{2} \varepsilon |\mathbf{E}|^2 \quad [\text{J/m}^3] \quad ; \quad U_C = \frac{1}{2} C V^2 \quad [\text{J}]",
        "verbalizacion_ingles": "• C = (epsilon_0 * epsilon_r * A) / d -> \"capacitance equals vacuum permittivity times relative permittivity times plate area divided by separation distance, in farads\".\n• u_E = 1/2 epsilon |E|^2 -> \"electrostatic energy density equals one-half permittivity times electric field magnitude squared, in joules per cubic meter\".\n• U_C = 1/2 C V^2 -> \"energy stored in a capacitor equals one-half capacitance times voltage squared, in joules\".",
        "ejemplo": "En bancos de condensadores para corrección de factor de potencia: 'The reactive power supplied by the capacitor bank is three times omega C times phase voltage squared'.",
        "bloque_sugerido": "Technical Discussion 30 min • Dielectric constants, capacitance and electrostatic energy"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Inductance, Magnetic Flux & Inductive Energy Storage",
        "objetivo": "Articular inductancia, ley de Faraday-Lenz y energía magnética almacenada en devanados e inductores.",
        "concepto_clave_latex": r"\Phi_B = \iint_S \mathbf{B} \cdot d\mathbf{A} \quad [\text{Wb}] \quad ; \quad \mathcal{E} = -L \frac{di}{dt} \quad [\text{V}] \quad ; \quad U_L = \frac{1}{2} L i^2 \quad [\text{J}]",
        "verbalizacion_ingles": "• Phi_B = surface integral of B dot dA -> \"magnetic flux equals the surface integral of magnetic flux density B dot differential area vector dA, in webers\".\n• E = -L * di/dt -> \"induced electromotive force equals minus self-inductance L times the time derivative of current di over dt, in volts\".\n• U_L = 1/2 L i^2 -> \"energy stored in the magnetic field of an inductor equals one-half inductance times current squared, in joules\".",
        "ejemplo": "En filtros LC para inversores: 'The series choke inductor smooths current ripple, storing energy proportional to one-half L i squared'.",
        "bloque_sugerido": "Speaking Drill 30 min • Magnetic flux, inductance and Faraday's law"
    }
]

def upgrade_english_2():
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    
    idx1 = content.find('      - codigo: "01021803"')
    idx2 = content.find('      - codigo: "03031818"')
    if idx1 == -1 or idx2 == -1:
        print("ERROR: Could not find English II section in DB.")
        sys.exit(1)
        
    asig_block = content[idx1:idx2]
    
    # 1. Insert new general topics 11 to 15 right before the first notacion topic (tema 11)
    split_marker = '          - numero_tema: 11\n            corte: 1\n            modalidad: "notacion_ingenieria"'
    if split_marker not in asig_block:
        print("ERROR: Split marker for tema 11 not found.")
        sys.exit(1)
        
    new_gen_yaml = format_topics_yaml(new_general_topics)
    asig_block = asig_block.replace(split_marker, new_gen_yaml + split_marker, 1)
    
    # 2. Renumber existing notacion topics in descending order:
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
    print("01021803 General English II successfully expanded to 30 topics (15 General + 15 Notación)!")

if __name__ == '__main__':
    upgrade_english_2()
