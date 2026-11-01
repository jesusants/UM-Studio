# -*- coding: utf-8 -*-
import sys
import re
from injector_base import format_topic_yaml, format_topics_yaml, DB_PATH, ASSETS_PATH

# 5 New General English III topics (Temas 11 to 15)
new_general_topics = [
    {
        "numero_tema": 11,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Third Conditional: Counterfactual Analysis & Post-Incident Engineering Reviews",
        "objetivo": "Formular hipótesis sobre eventos pasados que no ocurrieron y analizar fallos técnicos en inglés profesional (If + Past Perfect, would have + past participle).",
        "concepto_clave_latex": "",
        "ejemplo": "If the thermal protection relay had tripped immediately, the power transformer would not have suffered catastrophic insulation breakdown.",
        "bloque_sugerido": "Speaking Drill 30 min • Third conditional in electrical failure analysis",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B1 • COMMUNICATIVE PURPOSE",
                "titulo": "Third Conditional: Past Hypotheticals & Lessons Learned",
                "puntos": [
                    "Used to talk about conditions in the past that did not happen, and their hypothetical past outcomes.",
                    "Crucial for industrial incident investigation reports, safety debriefs, and reliability root-cause analysis.",
                    "Expresses regret, critique, or technical counterfactual logic."
                ],
                "ejemplo": "If the backup diesel generator had started automatically, the university hospital would not have lost critical power."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Morphological Blueprint",
                "puntos": [
                    "Condition Clause: If + subject + had (or hadn't) + past participle (V3).",
                    "Result Clause: Subject + would (or could / might) + have + past participle (V3).",
                    "Contraction Note: 'If we'd known' / 'it would've failed'."
                ]
            },
            {
                "numero": 3,
                "seccion": "TECHNICAL FAILURE AUDIT",
                "titulo": "Turbine Overspeed Investigation",
                "puntos": [
                    "Condition: If the centrifugal governor had responded within fifty milliseconds...",
                    "Consequence: ...the Pelton runner would have avoided severe blade deformation.",
                    "Alternative Modal: The operator might have vented the penstock if the SCADA telemetry had displayed the pressure surge."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Modal Placement & Auxiliary Consistency",
                "puntos": [
                    "Never place 'would have' inside the 'if' clause (incorrect: 'If the team would have replaced the fuse...').",
                    "Correct: 'If the team had replaced the fuse, the circuit would have operated safely.'",
                    "Watch out for double 'had had' when the main verb is 'have': 'If we had had the spare capacitor...'"
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC DEBRIEF DIALOGUE",
                "titulo": "Substation Maintenance Review",
                "puntos": [
                    "Lead Auditor: 'What would have happened if the SF6 circuit breaker had leaked during the storm?'",
                    "Senior Engineer: 'The busbar protection system would have isolated the entire feeder line immediately.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Rapid-Fire Past Scenarios",
                "puntos": [
                    "Prompt: 'Pump cavitation / install booster stage' -> 'If we had installed a booster pump, cavitation would not have eroded the impeller.'",
                    "Prompt: 'Solar inverter overheating / clean heat sink' -> 'If the technicians had cleaned the aluminum heat sink, the inverter would not have derated its output power.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Mixed Conditionals in Technical Contexts & Long-Term System Design",
        "objetivo": "Combinar condiciones hipotéticas pasadas con impactos en el presente, o condiciones presentes permanentes con resultados pasados.",
        "concepto_clave_latex": "",
        "ejemplo": "If the design team had integrated maximum power point tracking five years ago, this solar facility would be generating 15% more revenue today.",
        "bloque_sugerido": "Speaking Drill 30 min • Mixed conditionals in infrastructure planning",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B1 • COMMUNICATIVE PURPOSE",
                "titulo": "Mixed Conditionals: Bridging Past Actions & Present States",
                "puntos": [
                    "Past Action -> Present Result: Evaluating how an earlier engineering decision directly impacts current system performance.",
                    "Present Condition -> Past Result: Showing how an enduring trait or permanent design rule shaped a past event.",
                    "Essential for techno-economic feasibility discussions and retrofitting debates."
                ],
                "ejemplo": "If Unimagdalena had installed lithium-ion battery storage during the initial campus build, our microgrid would operate off-grid right now."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Type A: Past Cause -> Present Outcome",
                "puntos": [
                    "If + Past Perfect (had + V3) -> Subject + would / could + base verb.",
                    "Example: 'If we had calibrated the flowmeter yesterday, our current thermodynamic readings would be accurate.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Type B: Present Trait -> Past Outcome",
                "puntos": [
                    "If + Past Simple (were / had) -> Subject + would have + past participle (V3).",
                    "Example: 'If our campus grid were not interconnected with the national transmission network, the blackout last night would have shut down our servers.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Time Marker Confusion",
                "puntos": [
                    "Ensure the time indicators ('now', 'today', 'last semester') match the respective halves of the sentence.",
                    "Use subjunctive 'were' rather than 'was' in formal engineering reports ('If the line were energized...').",
                    "Do not confuse Third Conditional (pure past) with Mixed (past affecting present)."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC DESIGN DIALOGUE",
                "titulo": "Microgrid Feasibility Meeting",
                "puntos": [
                    "Project Lead: 'If we were more familiar with hydrogen fuel cells, we would have submitted the grant proposal last Friday.'",
                    "Consultant: 'And if the university had allocated budget in January, the prototype electrolyzer would be operational today.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Transition Practice",
                "puntos": [
                    "Convert: 'We did not insulate the pipe. It is cold.' -> 'If we had insulated the steam pipe, it would not be losing thermal energy now.'",
                    "Convert: 'The sensor is waterproof. It did not short-circuit.' -> 'If the pressure sensor were not waterproof, moisture would have destroyed its circuitry.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Reported Speech in Audits, Safety Inspections & Incident Investigations",
        "objetivo": "Transmitir declaraciones técnicas, advertencias de seguridad y hallazgos periciales aplicando las reglas de retrogradación temporal (backshift).",
        "concepto_clave_latex": "",
        "ejemplo": "The lead safety inspector reported that the main gas turbine had exceeded its permissible vibration threshold during the test run.",
        "bloque_sugerido": "Speaking Drill 30 min • Technical reporting and witness debriefs",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B1 • COMMUNICATIVE PURPOSE",
                "titulo": "Reported Speech: Formal Dissemination of Field Findings",
                "puntos": [
                    "In engineering practice, oral instructions and witness statements must be formally documented in written logs.",
                    "Shifting from Direct Quote ('The pressure is climbing dangerously') to Indirect Speech ('The technician stated that the pressure was climbing dangerously').",
                    "Key reporting verbs: stated, reported, confirmed, claimed, warned, emphasized."
                ],
                "ejemplo": "The environmental officer confirmed that the cooling pond discharged zero hazardous chemicals into the bay."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Tense Backshift Rules",
                "puntos": [
                    "Present Simple -> Past Simple: 'The pump operates' -> 'He said the pump operated.'",
                    "Present Continuous -> Past Continuous: 'The battery is charging' -> 'She reported the battery was charging.'",
                    "Past Simple / Present Perfect -> Past Perfect: 'We replaced the seal' -> 'They affirmed they had replaced the seal.'",
                    "Will -> Would, Can -> Could, Must -> Had to."
                ]
            },
            {
                "numero": 3,
                "seccion": "TECHNICAL REPORTING VERBS",
                "titulo": "Precision Reporting Beyond 'Said'",
                "puntos": [
                    "Warn: The superintendent warned the crew that high-voltage busbars were still energized.",
                    "Recommend: The consultant recommended that the plant upgrade its programmable logic controllers.",
                    "Notice: The field team noticed that the oil level had dropped below the minimum sightline."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Pronoun and Time/Place Shifts",
                "puntos": [
                    "Shift deictic markers: 'here' -> 'there', 'today' -> 'that day', 'tomorrow' -> 'the following day'.",
                    "No backshift when reporting a universal physical law: 'The professor explained that water boils at 100 degrees Celsius at sea level.'",
                    "Avoid awkward double negatives in accident reports."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC AUDIT RECORD",
                "titulo": "Field Safety Log Excerpt",
                "puntos": [
                    "Direct: 'We cannot re-energize the feeder until the lockout tag is officially removed.'",
                    "Reported: 'The maintenance supervisor emphasized that the crew could not re-energize the feeder until the lockout tag was officially removed.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Transforming Field Statements",
                "puntos": [
                    "Prompt: 'The harmonic distortion is exceeding IEEE standards.' -> 'The grid analyst reported that harmonic distortion was exceeding IEEE standards.'",
                    "Prompt: 'We will dispatch an emergency crew at sunrise.' -> 'The dispatcher assured the team that they would dispatch an emergency crew at sunrise.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Passive Voice II: Modal Passives & Causative Structures (Have / Get Done)",
        "objetivo": "Describir servicios de mantenimiento externalizados, certificaciones de calibración y mandatos regulatorios utilizando modales pasivos y estructuras causativas.",
        "concepto_clave_latex": "",
        "ejemplo": "The campus substation must be inspected annually by a certified high-voltage contractor, and all protective relays are had calibrated before commissioning.",
        "bloque_sugerido": "Speaking Drill 30 min • Modal passives & third-party service contracts",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B1 • COMMUNICATIVE PURPOSE",
                "titulo": "Modal Passives & Causative Constructions in Engineering Management",
                "puntos": [
                    "Engineering facilities rarely perform all specialized calibrations in-house; they outsource to certified test laboratories.",
                    "Modal Passive expresses obligation, recommendation, or possibility without naming the contractor: 'The system must be serviced.'",
                    "Causative (Have / Get + object + past participle) expresses arranging for third-party execution: 'We had the boiler inspected.'"
                ],
                "ejemplo": "Every three years, Unimagdalena has the solar pyranometers recalibrated by an accredited metrology institute."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Modal Passive Morphological Blueprint",
                "puntos": [
                    "Formula: Subject + modal verb (must / should / can / may) + be + past participle (V3).",
                    "Example 1: 'All confined spaces must be ventilated prior to personnel entry.'",
                    "Example 2: 'High-frequency noise can be mitigated through passive LC filtering.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Causative Blueprint: Have / Get Something Done",
                "puntos": [
                    "Formula: Subject + have / get + object + past participle (V3).",
                    "Professional Formal: 'The plant manager had the vibration sensors checked.'",
                    "Action-Oriented / Informal: 'We got the backup diesel fuel filters replaced yesterday.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Active vs. Causative Confusion",
                "puntos": [
                    "Incorrect: 'We repaired the ultrasonic transducer' (implies our students did the internal crystal repair).",
                    "Correct: 'We had the ultrasonic transducer repaired by the manufacturer.'",
                    "Do not forget 'be' in modal passives: 'The tank must checked' is wrong; write 'must be checked'."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC CONTRACT DIALOGUE",
                "titulo": "Substation Commissioning Call",
                "puntos": [
                    "Operations Manager: 'Has the utility approved our grid tie-in?'",
                    "Electrical Engineer: 'Yes, we had the interconnection study certified last week, and all grounding rods should be tested by Monday.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Prompt & Transformation",
                "puntos": [
                    "Prompt: 'Third party tested the insulation oil.' -> 'We had the transformer insulation oil tested by a laboratory.'",
                    "Prompt: 'Safety code requires earthing all steel structural members.' -> 'All steel structural members must be earthed according to safety codes.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Academic Abstracts & Executive Summaries for Technical Energy Papers",
        "objetivo": "Redactar y sintetizar resúmenes académicos (abstracts) siguiendo la estructura internacional IMRaD (Introduction, Methods, Results, and Discussion).",
        "concepto_clave_latex": "",
        "ejemplo": "This study evaluates the performance of a hybrid photovoltaic-thermal collector under Caribbean tropical conditions, demonstrating a 14.2% increase in total energy conversion efficiency.",
        "bloque_sugerido": "Writing & Presentation 35 min • Crafting an IEEE-style conference abstract",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B1 • COMMUNICATIVE PURPOSE",
                "titulo": "The Structure of an Engineering Abstract (IMRaD)",
                "puntos": [
                    "An abstract is a self-contained, 200-to-250-word synthesis of an entire technical investigation.",
                    "Motivates the reader: Background & Problem Statement (1–2 sentences).",
                    "Specifies the approach: Methodology & Experimental Setup (2–3 sentences).",
                    "Highlights the breakthrough: Key Quantitative Results & Conclusions (2–3 sentences)."
                ],
                "ejemplo": "Energy Engineering undergraduates present their research projects at international conferences using standardized English abstracts."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Verbal Tenses across Abstract Sections",
                "puntos": [
                    "Background: Present Simple ('Global energy demand continues to accelerate...').",
                    "Methodology: Past Simple Passive ('A numerical CFD model was constructed and meshed...').",
                    "Results: Past Simple / Present Simple ('The prototype achieved a coefficient of performance of 3.8...').",
                    "Conclusion / Implications: Present Simple / Modals ('These findings demonstrate that solar absorption cooling is economically viable in coastal climates.')."
                ]
            },
            {
                "numero": 3,
                "seccion": "KEY SIGNPOSTING PHRASES",
                "titulo": "Formulaic Academic Expressions",
                "puntos": [
                    "'This paper proposes a novel dispatch algorithm for...'",
                    "'Experimental validation was conducted using an instrumented test bench...'",
                    "'Results indicate a statistically significant reduction in fuel consumption...'",
                    "'The authors conclude that integrating phase change materials enhances round-trip efficiency.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Conciseness & Objectivity",
                "puntos": [
                    "Never cite bibliographic references or equation numbers directly in an abstract.",
                    "Avoid vague claims: replace 'efficiency was very good' with 'isentropic efficiency improved from 72.1% to 81.4%'.",
                    "Do not use colloquialisms or unsupported future promises."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC ABSTRACT BREAKDOWN",
                "titulo": "Unimagdalena Clean Energy Case Study",
                "puntos": [
                    "Title: 'Thermo-hydraulic characterization of microchannel heat exchangers for waste heat recovery.'",
                    "Key Result: 'An overall heat transfer coefficient of 1,850 W/(m²·K) was obtained with an allowable pressure drop below 12 kPa.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Elevator Pitch from Abstract",
                "puntos": [
                    "Summarize your senior capstone project in 60 seconds using the 4-part formula: 'My research addresses [Problem] by [Method], which achieved [Result], proving that [Impact].'"
                ]
            }
        ]
    }
]

# 9 New Engineering Notation topics (Temas 22 to 30)
new_notacion_topics = [
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Fluid Dynamics, Continuity Equation & Volumetric Flow Rate",
        "objetivo": "Articular la ecuación de continuidad para flujo incompresible, caudal volumétrico y conservación de masa en fluidos.",
        "concepto_clave_latex": r"\dot{V} = A v \quad [\text{m}^3/\text{s}] \quad ; \quad \dot{m} = \rho A v = \rho \dot{V} \quad [\text{kg/s}] \quad ; \quad A_1 v_1 = A_2 v_2",
        "verbalizacion_ingles": "• V_dot = A * v -> \"volumetric flow rate V dot equals cross-sectional area A times average fluid velocity v, in cubic meters per second\".\n• m_dot = rho * A * v -> \"mass flow rate m dot equals fluid density rho times area times velocity, in kilograms per second\".\n• A_1 * v_1 = A_2 * v_2 -> \"area one times velocity one equals area two times velocity two for steady incompressible flow\".",
        "ejemplo": "En tuberías de carga hidroeléctrica: 'The volumetric flow rate into the penstock is thirty-two point five cubic meters per second, accelerating the water velocity as pipe diameter narrows'.",
        "bloque_sugerido": "Speaking Drill 30 min • Continuity equation and mass flow rate verbalization"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Bernoulli's Equation, Pressure Head & Piezometric Head",
        "objetivo": "Verbalizar la conservación de energía mecánica en fluidos ideales a lo largo de una línea de corriente en unidades de presión y altura de columna.",
        "concepto_clave_latex": r"P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2 \quad ; \quad \frac{P_1}{\gamma} + \frac{v_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{v_2^2}{2g} + z_2 = H",
        "verbalizacion_ingles": "• P_1 + 1/2 rho v_1^2 + rho g z_1 -> \"static pressure P sub one plus one-half rho v one squared plus rho g z one equals constant along a streamline, in pascals\".\n• P/gamma + v^2/(2g) + z = H -> \"pressure head P over gamma plus velocity head v squared over two g plus elevation head z equals total hydraulic head H, in meters\".",
        "ejemplo": "En el análisis de un tubo de Venturi: 'The drop in piezometric head between the inlet and the throat yields the differential pressure required to compute flow velocity'.",
        "bloque_sugerido": "Technical Discussion 30 min • Bernoulli's equation, pressure head and kinetic head"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Reynolds Number, Viscous Regimes & Darcy-Weisbach Friction Factor",
        "objetivo": "Expresar regímenes de flujo (laminar vs. turbulento), viscosidad cinemática y pérdidas por fricción en tuberías en inglés técnico.",
        "concepto_clave_latex": r"Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu} \quad [-] \quad ; \quad h_f = f \frac{L}{D} \frac{v^2}{2g} \quad [\text{m}] \quad ; \quad f_{lam} = \frac{64}{Re}",
        "verbalizacion_ingles": "• Re = (rho * v * D) / mu -> \"Reynolds number equals fluid density rho times velocity v times internal diameter D divided by dynamic viscosity mu, dimensionless\".\n• h_f = f * (L / D) * (v^2 / (2g)) -> \"frictional head loss h sub f equals Darcy friction factor f times pipe length over diameter times velocity squared over two g, in meters\".\n• f_lam = 64 / Re -> \"for laminar flow with Reynolds number below two thousand three hundred, the friction factor equals sixty-four divided by Re\".",
        "ejemplo": "En circuitos de bombeo geotérmico: 'Because the Reynolds number exceeds forty thousand, the flow regime is fully turbulent, requiring the Colebrook-White correlation'.",
        "bloque_sugerido": "Speaking Drill 30 min • Reynolds number, turbulent regimes and head loss"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Hydrostatic Pressure, Pascal's Law & Manometry Calculations",
        "objetivo": "Articular presión estática en profundidades sumergidas, principio de transmisión de presión en fluidos confinados y lectura manométrica diferencial.",
        "concepto_clave_latex": r"P(z) = P_0 + \rho g h \quad [\text{Pa}] \quad ; \quad \Delta P = \rho_m g \Delta h \quad ; \quad \frac{F_1}{A_1} = \frac{F_2}{A_2} \implies F_2 = F_1 \left(\frac{A_2}{A_1}\right)",
        "verbalizacion_ingles": "• P(z) = P_0 + rho g h -> \"hydrostatic pressure at depth h equals ambient pressure P nought plus density rho times gravitational acceleration g times depth h, in pascals\".\n• Delta P = rho_m g Delta h -> \"differential pressure equals manometric fluid density times g times deflection height Delta h\".\n• F_1 / A_1 = F_2 / A_2 -> \"input force over input area equals output force over output area in a hydraulic actuator\".",
        "ejemplo": "En compuertas de presas hidroeléctricas: 'The total hydrostatic force acting on the vertical sluice gate equals fluid specific weight times gate centroid depth times submerged gate area'.",
        "bloque_sugerido": "Technical Dialogue 30 min • Hydrostatic pressure, Pascal's law and hydraulic actuators"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "First Law of Thermodynamics for Open Control Volumes (SFEE)",
        "objetivo": "Verbalizar la ecuación de conservación de energía para volúmenes de control en régimen estacionario (turbinas, compresores y toberas).",
        "concepto_clave_latex": r"\dot{Q} - \dot{W}_{cv} = \sum_{out} \dot{m}_e \left(h_e + \frac{v_e^2}{2} + g z_e\right) - \sum_{in} \dot{m}_i \left(h_i + \frac{v_i^2}{2} + g z_i\right) \quad [\text{kW}]",
        "verbalizacion_ingles": "• Q_dot - W_dot_cv = sum(m_dot_out * (h_out + v_out^2/2 + g z_out)) - sum(m_dot_in * (h_in + v_in^2/2 + g z_in)) -> \"rate of net heat input Q dot minus shaft power W dot sub control volume equals total enthalpy, kinetic, and potential energy exiting minus entering the boundary, in kilowatts\".",
        "ejemplo": "En una turbina de vapor adiabática: 'Assuming zero heat loss and negligible kinetic changes, the turbine shaft work equals mass flow rate times specific enthalpy drop: W dot equals m dot times quantity h inlet minus h exit'.",
        "bloque_sugerido": "Speaking Drill 30 min • Steady-flow energy equation and enthalpy verbalization"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Ideal Gas Law, Compressibility Factor Z & Polytropic Processes",
        "objetivo": "Expresar ecuaciones de estado de gases ideales y reales, factor de compresibilidad y transformaciones politrópicas de compresión/expansión.",
        "concepto_clave_latex": r"P V = n R_u T \quad ; \quad P v = R T \quad ; \quad Z = \frac{P v}{R T} \quad [-] \quad ; \quad P v^n = \text{const}",
        "verbalizacion_ingles": "• P * V = n * R_u * T -> \"pressure times volume equals number of moles n times universal gas constant R sub u times absolute temperature T in kelvins\".\n• P * v = R * T -> \"pressure times specific volume v equals specific gas constant R times temperature\".\n• Z = (P * v) / (R * T) -> \"compressibility factor Z equals P v over R T, deviating from unity as gas pressure approaches critical state\".\n• P * v^n = const -> \"polytropic process equation P times specific volume to the power n equals constant\".",
        "ejemplo": "En compresión de biogás: 'At twelve megapascals, methane deviates from ideal gas behavior, exhibiting a compressibility factor Z of approximately zero point eight-eight'.",
        "bloque_sugerido": "Technical Discussion 30 min • Ideal gas law, Z factor and polytropic compression"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Second Law of Thermodynamics, Entropy Generation & Carnot Limit",
        "objetivo": "Verbalizar entropía, generación de entropía por irreversibilidades y eficiencia térmica máxima de ciclos termodinámicos.",
        "concepto_clave_latex": r"\eta_{th, Carnot} = 1 - \frac{T_L}{T_H} \quad ; \quad dS = \frac{\delta Q_{rev}}{T} \quad ; \quad \dot{S}_{gen} = \frac{dS_{sys}}{dt} - \sum \frac{\dot{Q}_k}{T_k} - \sum \dot{m}_i s_i + \sum \dot{m}_e s_e \ge 0",
        "verbalizacion_ingles": "• eta_Carnot = 1 - T_L / T_H -> \"Carnot thermal efficiency equals one minus absolute temperature of the cold sink T sub L divided by hot source T sub H\".\n• dS = delta Q_rev / T -> \"differential entropy dS equals reversible heat transfer delta Q divided by thermodynamic temperature T, in kilojoules per kelvin\".\n• S_dot_gen >= 0 -> \"rate of entropy generation S dot gen is strictly greater than or equal to zero for all spontaneous real processes according to the Second Law\".",
        "ejemplo": "En ciclos combinados de gas y vapor: 'The maximum theoretical efficiency is capped by the Carnot limit between the combustion temperature and the ambient cooling water temperature'.",
        "bloque_sugerido": "Speaking Drill 30 min • Second law of thermodynamics, entropy generation and Carnot limit"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Fourier's Law of Thermal Conduction & 1D Thermal Resistance Networks",
        "objetivo": "Expresar la ley de conducción térmica de Fourier, gradiente de temperatura unidimensional y analogía de circuitos de resistencia térmica.",
        "concepto_clave_latex": r"\dot{Q}_{cond} = -k A \frac{dT}{dx} \quad [\text{W}] \quad ; \quad R_{th, cond} = \frac{L}{k A} \quad [\text{K/W}] \quad ; \quad \dot{Q} = \frac{\Delta T}{R_{th, total}}",
        "verbalizacion_ingles": "• Q_dot_cond = -k * A * (dT / dx) -> \"conductive heat transfer rate Q dot equals minus thermal conductivity k times surface area A times temperature gradient dT over dx, in watts\".\n• R_th_cond = L / (k * A) -> \"conductive thermal resistance equals wall thickness L divided by thermal conductivity k times area A, in kelvins per watt\".\n• Q_dot = Delta T / R_th_total -> \"heat flow equals overall temperature difference Delta T divided by total equivalent thermal resistance\".",
        "ejemplo": "En aislamiento de colectores solares térmicos: 'The heat loss through the mineral wool insulation is calculated as the temperature drop divided by the sum of conductive and convective resistances'.",
        "bloque_sugerido": "Technical Dialogue 30 min • Fourier's law and thermal resistance networks"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Newton's Law of Cooling & Stefan-Boltzmann Surface Radiation",
        "objetivo": "Articular transferencia de calor por convección y radiación térmica superficial de cuerpos negros y grises.",
        "concepto_clave_latex": r"\dot{Q}_{conv} = h A (T_s - T_\infty) \quad [\text{W}] \quad ; \quad \dot{Q}_{rad} = \varepsilon \sigma A (T_s^4 - T_{surr}^4) \quad [\text{W}] \quad ; \quad \sigma = 5.670 \times 10^{-8} \ \frac{\text{W}}{\text{m}^2 \text{K}^4}",
        "verbalizacion_ingles": "• Q_dot_conv = h * A * (T_s - T_infinity) -> \"convective heat transfer rate equals convection heat transfer coefficient h times area A times surface temperature T sub s minus fluid ambient temperature T infinity, in watts\".\n• Q_dot_rad = epsilon * sigma * A * (T_s^4 - T_surr^4) -> \"radiative heat transfer rate equals surface emissivity epsilon times Stefan-Boltzmann constant sigma times area times the difference of fourth powers of surface and surrounding absolute temperatures\".",
        "ejemplo": "En disipadores de inversores fotovoltaicos: 'Natural convection accounts for seventy percent of heat dissipation, while thirty percent is radiated to the ambient enclosure'.",
        "bloque_sugerido": "Speaking Drill 30 min • Convection coefficient, Stefan-Boltzmann law and emissivity"
    }
]

def upgrade_english_3():
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    
    idx1 = content.find('      - codigo: "01021804"')
    idx2 = content.find('\n  - cuatrimestre: 4', idx1)
    if idx1 == -1 or idx2 == -1:
        print("ERROR: Could not find English III section in DB.")
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
    print("01021804 General English III successfully expanded to 30 topics (15 General + 15 Notación)!")

if __name__ == '__main__':
    upgrade_english_3()
