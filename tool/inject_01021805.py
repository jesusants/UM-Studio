# -*- coding: utf-8 -*-
import sys
import re
from injector_base import format_topic_yaml, format_topics_yaml, DB_PATH, ASSETS_PATH

# 5 New General English IV topics (Temas 11 to 15, CEFR B2)
new_general_topics = [
    {
        "numero_tema": 11,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Inversion with Negative & Restrictive Adverbials in Engineering Writing",
        "objetivo": "Utilizar la inversión sintáctica (Auxiliar + Sujeto + Verbo) tras adverbios negativos y restrictivos (Rarely, Seldom, Not only, Under no circumstances) para enfatizar condiciones críticas de seguridad y rendimiento.",
        "concepto_clave_latex": "",
        "ejemplo": "Under no circumstances should the high-voltage disconnect switch be operated under load, nor should maintenance personnel enter the enclosure without grounding the busbars.",
        "bloque_sugerido": "Speaking Drill 30 min • Negative inversion in technical manuals & safety warnings",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B2 • COMMUNICATIVE PURPOSE",
                "titulo": "Inversion for Rhetorical & Safety Emphasis",
                "puntos": [
                    "Standard word order is inverted to create a dramatic, formal, or authoritative tone.",
                    "Frequently used in IEEE journal conclusions, patent documentation, and critical industrial operating instructions.",
                    "Draws immediate listener/reader attention to exceptional events or strict prohibitions."
                ],
                "ejemplo": "Seldom has a combined-cycle power facility achieved an overall thermal efficiency exceeding sixty-three percent."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Morphological Blueprint",
                "puntos": [
                    "Formula: Negative Adverbial + Auxiliary / Modal Verb + Subject + Main Verb.",
                    "Rarely do renewable microgrids experience complete blackouts when equipped with battery storage.",
                    "Not only did the inverter mitigate voltage sags, but it also eliminated harmonic distortion."
                ]
            },
            {
                "numero": 3,
                "seccion": "KEY RESTRICTIVE ADVERBIALS",
                "titulo": "High-Frequency Technical Markers",
                "puntos": [
                    "'Hardly had the steam turbine synchronized when the bearing temperature alarm activated.'",
                    "'Only after conducting a dielectric oil analysis can the transformer be safely re-energized.'",
                    "'At no time must the combustible gas concentration exceed ten percent of the lower explosive limit.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Auxiliary Insertion & Word Order",
                "puntos": [
                    "Incorrect: 'Rarely the generator trips' -> Correct: 'Rarely does the generator trip.'",
                    "Do not forget subject-auxiliary inversion after 'Only when / Only after' clauses: 'Only after the engineers verified the telemetry did they open the valve.'",
                    "Avoid double negatives."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC COMMISSIONING DIALOGUE",
                "titulo": "Grid Tie-in Safety Briefing",
                "puntos": [
                    "Chief Inspector: 'Under no circumstances are technicians to bypass the interlock mechanism.'",
                    "Commissioning Lead: 'Understood. Not until the lockout-tagout log is fully signed will the main breaker close.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Inversion Transformation Drill",
                "puntos": [
                    "Prompt: 'We have never witnessed such severe cavitation.' -> 'Never have we witnessed such severe cavitation in a Francis runner.'",
                    "Prompt: 'The solar farm not only generated surplus power, but it also stabilized local grid frequency.' -> 'Not only did the solar farm generate surplus power, but it also stabilized local grid frequency.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Advanced Cleft Sentences (It-Clefts & Wh-Clefts) to Focus Technical Arguments",
        "objetivo": "Estructurar oraciones hendidas (cleft sentences) para aislar variables determinantes y destacar hallazgos experimentales específicos en presentaciones académicas.",
        "concepto_clave_latex": "",
        "ejemplo": "It was the degradation of the ethylene-vinyl acetate encapsulant that triggered the accelerated delamination in the photovoltaic modules.",
        "bloque_sugerido": "Speaking Drill 30 min • Cleft sentences in scientific presentations",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B2 • COMMUNICATIVE PURPOSE",
                "titulo": "Focalizing Key Engineering Variables",
                "puntos": [
                    "Cleft sentences split a single clause into two parts to highlight the most critical piece of technical information.",
                    "Answers the implicit question: 'What was the exact root cause of the observation?'",
                    "Essential for defending research hypotheses and answering inquisitor panels during thesis defenses."
                ],
                "ejemplo": "What the CFD simulation revealed was an unexpected recirculation vortex near the nozzle throat."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "It-Clefts Blueprint",
                "puntos": [
                    "Formula: It + is / was + focused element + that / which / who + remainder.",
                    "Example 1: 'It was the reactive power deficiency that caused the regional voltage collapse.'",
                    "Example 2: 'It is at temperatures above eight hundred degrees Celsius that SOFC ceramic electrolytes become highly conductive.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Wh-Clefts (Pseudo-Clefts) Blueprint",
                "puntos": [
                    "Formula: What-clause + is / was + focused element / clause.",
                    "Example 1: 'What the university microgrid needs is a localized hydrogen energy storage buffer.'",
                    "Example 2: 'All that the maintenance team replaced was the primary ceramic bushing.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Pronoun Agreement & Overuse",
                "puntos": [
                    "Use 'that' instead of 'which' in modern engineering It-clefts ('It was the pump that failed').",
                    "Ensure subject-verb agreement with the focused noun phrase.",
                    "Do not overuse cleft sentences in every sentence; reserve them for pivotal conclusions and executive summary pivots."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC ACADEMIC DEBATE",
                "titulo": "Conference Q&A Session",
                "puntos": [
                    "Reviewer: 'Did the ambient humidity reduce the solar panel power rating?'",
                    "Presenter: 'No, it was the dust deposition and elevated cell temperature that accounted for the nine percent drop in performance.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Synthesizing Core Insights",
                "puntos": [
                    "Transform: 'The improper torque setting caused the bolt fracture.' -> 'It was the improper torque setting that caused the bolt fracture.'",
                    "Transform: 'We must reduce the levelized cost of energy.' -> 'What we must reduce is the levelized cost of electricity through higher turbine capacity factors.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 3,
        "modalidad": "general",
        "titulo": "The Subjunctive Mood & Mandates in Engineering Standards (IEC / IEEE / ISO)",
        "objetivo": "Formular requerimientos regulatorios, prescripciones de diseño y recomendaciones imperativas utilizando el subjuntivo formal en inglés (base verb invariable).",
        "concepto_clave_latex": "",
        "ejemplo": "The Colombian grid code mandates that every grid-tied inverter remain connected during transient voltage sags of up to 500 milliseconds.",
        "bloque_sugerido": "Speaking Drill 30 min • Subjunctive mood in regulatory compliance audits",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B2 • COMMUNICATIVE PURPOSE",
                "titulo": "Prescriptive Language in International Standards",
                "puntos": [
                    "Used to express requirements, mandates, urgency, or formal recommendations.",
                    "Standard feature of technical specifications, tender documents (RFP), and electrical codes.",
                    "Employs the bare infinitive (base form of the verb) regardless of the subject pronoun (he/she/it)."
                ],
                "ejemplo": "International standard IEC 61400 requires that wind turbine blades be tested for structural fatigue over two million cycles."
            },
            {
                "numero": 2,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Morphological Blueprint",
                "puntos": [
                    "Formula: Subject + mandating verb + that + subject + [base verb] (no -s, no past tense).",
                    "Key Verbs: demand, mandate, stipulate, require, recommend, propose, insist, specify.",
                    "Key Adjectives: imperative, essential, vital, crucial, mandatory."
                ]
            },
            {
                "numero": 3,
                "seccion": "AUTHENTIC CODE CLAUSES",
                "titulo": "RETIE & IEEE Compliance",
                "puntos": [
                    "'The RETIE regulation stipulates that the substation earthing mesh have a resistance of less than one ohm.'",
                    "'It is imperative that the emergency diesel generator start within ten seconds of mains failure.'",
                    "'The standard insists that all SF6 gas handling be executed by certified recovery technicians.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Avoiding Third-Person -s and Modal Intrusion",
                "puntos": [
                    "Incorrect: 'The engineer requires that the contractor tests the pipe.'",
                    "Correct: 'The engineer requires that the contractor test the pipe.'",
                    "Passive Subjunctive: '...that the circuit breaker be opened' (never 'is opened' or 'was opened').",
                    "Negative Subjunctive: '...that the pressure not exceed ten bar' (never 'does not exceed')."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC AUDIT DIALOGUE",
                "titulo": "Factory Acceptance Test (FAT)",
                "puntos": [
                    "Auditor: 'Our contract stipulates that the battery energy storage system be tested at full 1C discharge rate before shipment.'",
                    "Manufacturer: 'Understood. We have arranged that the load bank be connected tomorrow morning.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Regulatory Formulation Drill",
                "puntos": [
                    "Prompt: 'Safety protocol / technician wears arc-flash suit' -> 'Safety protocol requires that the technician wear a 40-calorie arc-flash suit.'",
                    "Prompt: 'Grid standard / frequency does not deviate by 0.5 Hz' -> 'The grid standard mandates that the system frequency not deviate by more than zero point five hertz.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Hedging & Epistemic Stance in Peer-Reviewed Journal Articles",
        "objetivo": "Modular el grado de certeza y el alcance de las afirmaciones científicas mediante técnicas de 'hedging' (atenuación y cautela epistémica) para publicaciones de impacto (Q1/Q2).",
        "concepto_clave_latex": "",
        "ejemplo": "Preliminary computational results suggest that the novel airfoil profile may potentially reduce aerodynamic blade noise by approximately 3.5 decibels.",
        "bloque_sugerido": "Writing & Presentation 35 min • Hedging techniques in IEEE manuscripts",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B2 • COMMUNICATIVE PURPOSE",
                "titulo": "Epistemic Humility & Scientific Rigor",
                "puntos": [
                    "Direct, absolute statements ('This material is completely indestructible') are rejected by peer reviewers.",
                    "Hedging distinguishes between established empirical fact, model extrapolation, and tentative hypothesis.",
                    "Protects the researcher from over-generalization while conveying analytical maturity."
                ],
                "ejemplo": "The data appear to indicate a moderate correlation between solar irradiance fluctuations and grid voltage transients."
            },
            {
                "numero": 2,
                "seccion": "LEXICAL STRATEGIES",
                "titulo": "Hedging Classification",
                "puntos": [
                    "Epistemic Modals: may, might, could, would ('This could explain the observed thermal losses').",
                    "Tentative Verbs: suggest, indicate, imply, tend to, appear to, seem to ('The findings tend to confirm the hypothesis').",
                    "Approximators: approximately, roughly, generally, largely, predominantly, virtually.",
                    "Probability Adverbs: plausibly, presumably, arguably, conceivably."
                ]
            },
            {
                "numero": 3,
                "seccion": "STRUCTURE & PATTERNS",
                "titulo": "Graded Assertion Comparison",
                "puntos": [
                    "Overstated: 'The new battery cathode will revolutionize the energy industry.'",
                    "Appropriately Hedged: 'These electrochemical characteristics indicate that the cathode material has the potential to enhance energy density under laboratory conditions.'",
                    "Notice the careful qualification of scope ('under laboratory conditions')."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Compound Hedges & Under-Confidence",
                "puntos": [
                    "Avoid stacking too many hedges in a single clause ('It might perhaps possibly be suggested that...').",
                    "Do not hedge established thermodynamic laws ('It seems that energy is conserved' is absurd).",
                    "Be bold in the problem statement and methodology, and measured in the discussion and future outlook."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC MANUSCRIPT REVISION",
                "titulo": "Responding to Reviewer Criticisms",
                "puntos": [
                    "Reviewer 2: 'The authors claim 99% efficiency without accounting for parasitic pump losses.'",
                    "Authors' Response: 'We have revised Section 4.2 to clarify that the 99% figure pertains strictly to the electrical converter stage, and that overall balance-of-plant efficiency is estimated to be approximately 91.4%.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Softening Sweeping Statements",
                "puntos": [
                    "Prompt: 'Wind turbines always create acoustic issues for neighboring communities.' -> 'Large-scale wind installations tend to generate localized aerodynamic noise that may affect nearby residents under certain atmospheric conditions.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Technical Debates, Rebuttals & Negotiating EPC Energy Contracts",
        "objetivo": "Participar activamente en debates técnicos, formular refutaciones diplomáticas y negociar cláusulas de desempeño (guaranteed heat rate, availability warranties) en contratos llave en mano (EPC).",
        "concepto_clave_latex": "",
        "ejemplo": "While we acknowledge the supplier's concern regarding raw material inflation, our consortium maintains that the contractual performance ratio must remain at eighty-two percent.",
        "bloque_sugerido": "Role-Play Negotiation 40 min • EPC contract dispute resolution",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR B2 • COMMUNICATIVE PURPOSE",
                "titulo": "Diplomatic Persuasion in Multi-Million Dollar Projects",
                "puntos": [
                    "Engineers must negotiate technical parameters, liquidated damages, and warranties with international contractors.",
                    "Balancing firmness on engineering standards with diplomatic flexibility on commercial schedules.",
                    "Concession-then-counter-assertion strategies: 'While we concede X, we must insist on Y.'"
                ],
                "ejemplo": "Energy Engineering graduates represent project developers in negotiating power purchase agreements (PPAs)."
            },
            {
                "numero": 2,
                "seccion": "FORMULAIC SIGNPOSTING",
                "titulo": "Signposting Technical Disagreement",
                "puntos": [
                    "Polite Disagreement: 'With respect, the telemetry data do not corroborate that interpretation.'",
                    "Reframing: 'From a lifecycle cost perspective, the initial savings are eclipsed by maintenance overhead.'",
                    "Concession: 'We recognize that supply chain delays occurred; nevertheless, the milestone penalty remains binding.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "KEY EPC CONTRACT TERMINOLOGY",
                "titulo": "Guarantees & Liabilities",
                "puntos": [
                    "Liquidated Damages (LDs): Pre-agreed financial penalties for delayed commissioning or performance shortfall.",
                    "Commercial Operation Date (COD): The official milestone when the plant starts commercial export.",
                    "Heat Rate Guarantee: Assured fuel consumption per megawatt-hour generated."
                ]
            },
            {
                "numero": 4,
                "seccion": "COMMON ERRORS & PITFALLS",
                "titulo": "Tone & Ambiguity",
                "puntos": [
                    "Never use aggressive or accusatory language ('You lied about the inverter delivery').",
                    "Use neutral, objective formulations ('The delivery date stipulated in Section 3.1 was not met').",
                    "Avoid ambiguous terms like 'as soon as possible'; specify concrete calendar dates and test metrics."
                ]
            },
            {
                "numero": 5,
                "seccion": "AUTHENTIC CONTRACT NEGOTIATION",
                "titulo": "Solar Farm Warranty Dispute",
                "puntos": [
                    "EPC Contractor: 'The heavy rain season constituted a force majeure event that excuses our two-month delay.'",
                    "Developer Lead: 'While we appreciate that rainfall was higher than average, historical meteorological records demonstrate that such precipitation was fully foreseeable in Santa Marta during October.'"
                ]
            },
            {
                "numero": 6,
                "seccion": "ORAL DRILL",
                "titulo": "Diplomatic Counter-Offer Practice",
                "puntos": [
                    "Scenario: The supplier wants to deliver a 3.0 MW turbine instead of the contracted 3.5 MW unit due to factory backlog.",
                    "Task: Deliver a 60-second rebuttal rejecting the substitution unless accompanied by a compensatory reduction in levelized maintenance fees."
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
        "titulo": "Maxwell's Equations in Differential Form & Poynting Vector",
        "objetivo": "Articular las cuatro ecuaciones de Maxwell diferenciales y el vector de densidad de potencia electromagnética de Poynting en inglés técnico.",
        "concepto_clave_latex": r"\nabla \cdot \mathbf{D} = \rho_v \quad ; \quad \nabla \cdot \mathbf{B} = 0 \quad ; \quad \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad ; \quad \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \quad ; \quad \mathbf{S} = \mathbf{E} \times \mathbf{H}",
        "verbalizacion_ingles": "• div D = rho_v -> \"divergence of electric flux density D equals free volume charge density rho sub v\".\n• div B = 0 -> \"divergence of magnetic flux density B equals zero, confirming the absence of magnetic monopoles\".\n• curl E = -dB/dt -> \"curl of electric field E equals minus the partial time derivative of magnetic flux density B\".\n• curl H = J + dD/dt -> \"curl of magnetic field intensity H equals conduction current density J plus displacement current density partial D over partial t\".\n• S = E x H -> \"Poynting vector S equals the cross product of electric field E and magnetic field H, representing power flow density in watts per square meter\".",
        "ejemplo": "En análisis de radiación electromagnética de antenas: 'The surface integral of the time-averaged Poynting vector over a closed sphere yields the total radiated power'.",
        "bloque_sugerido": "Speaking Drill 30 min • Differential Maxwell's equations and Poynting theorem"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Complex Propagation Constant, Wave Impedance & Skin Depth",
        "objetivo": "Expresar la constante de propagación electromagnética compleja, impedancia intrínseca de medio con pérdidas y profundidad pelicular.",
        "concepto_clave_latex": r"\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)} \quad ; \quad \eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}} \quad ; \quad \delta_s = \frac{1}{\sqrt{\pi f \mu \sigma}} \quad [\text{m}]",
        "verbalizacion_ingles": "• gamma = alpha + j beta -> \"complex propagation constant gamma equals attenuation constant alpha in nepers per meter plus j times phase constant beta in radians per meter\".\n• eta = sqrt(j omega mu / (sigma + j omega epsilon)) -> \"intrinsic wave impedance eta equals the square root of quantity j omega mu divided by quantity sigma plus j omega epsilon, in ohms\".\n• delta_s = 1 / sqrt(pi * f * mu * sigma) -> \"skin depth delta sub s equals one over the square root of pi times frequency f times magnetic permeability mu times electrical conductivity sigma, in meters\".",
        "ejemplo": "En líneas subterráneas de potencia: 'At sixty hertz, the skin depth of commercial copper is approximately eight point five millimeters, causing non-uniform current distribution across large conductor cross-sections'.",
        "bloque_sugerido": "Technical Dialogue 30 min • Skin depth, attenuation constant and phase velocity"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Transmission Line Voltage Reflection Coefficient & VSWR",
        "objetivo": "Verbalizar el coeficiente de reflexión de voltaje en líneas de transmisión desacopladas y la razón de onda estacionaria.",
        "concepto_clave_latex": r"\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_L| e^{j\theta_L} \quad ; \quad \text{VSWR} = \frac{V_{\max}}{V_{\min}} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|} \ge 1 \quad ; \quad Z_{in}(l) = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}",
        "verbalizacion_ingles": "• Gamma_L = (Z_L - Z_0) / (Z_L + Z_0) -> \"voltage reflection coefficient Gamma sub L equals load impedance Z sub L minus characteristic impedance Z nought divided by Z sub L plus Z nought\".\n• VSWR = (1 + |Gamma_L|) / (1 - |Gamma_L|) -> \"voltage standing wave ratio VSWR equals one plus the magnitude of Gamma sub L divided by one minus the magnitude of Gamma sub L, strictly greater than or equal to one\".\n• Z_in(l) -> \"input impedance Z in at distance l equals characteristic impedance Z nought times quantity load impedance plus j Z nought tangent beta l divided by Z nought plus j load impedance tangent beta l\".",
        "ejemplo": "En telecomunicaciones para supervisión SCADA: 'A high voltage standing wave ratio of three point two indicates significant impedance mismatch, requiring an adjustable parallel stub to prevent power reflection back to the transmitter'.",
        "bloque_sugerido": "Speaking Drill 30 min • Reflection coefficient, VSWR and impedance matching"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Combined Cycle & Cogeneration Fuel Utilization Efficiency",
        "objetivo": "Articular fórmulas de eficiencia de ciclos combinados gas-vapor y factor de utilización de combustible en cogeneración.",
        "concepto_clave_latex": r"\eta_{CC} = \eta_{GT} + \eta_{ST}(1 - \eta_{GT}) \quad ; \quad \text{FUE} = \frac{\dot{W}_e + \dot{Q}_{util}}{\dot{m}_f \cdot \text{LHV}} \quad ; \quad \text{PER} = \frac{\dot{W}_e}{\dot{Q}_{util}}",
        "verbalizacion_ingles": "• eta_CC = eta_GT + eta_ST * (1 - eta_GT) -> \"combined cycle thermal efficiency equals gas turbine efficiency plus steam turbine efficiency times quantity one minus gas turbine efficiency\".\n• FUE = (W_dot_e + Q_dot_util) / (m_dot_f * LHV) -> \"fuel utilization effectiveness FUE equals net electrical power output W dot e plus useful thermal output Q dot util divided by fuel mass flow rate times lower heating value\".\n• PER = W_dot_e / Q_dot_util -> \"power-to-heat ratio PER equals net electric power divided by process heat output\".",
        "ejemplo": "En auditorías energéticas industriales: 'By capturing waste heat from the microturbine in an exhaust heat recovery boiler, the cogeneration plant raised its overall fuel utilization efficiency from thirty-eight percent to eighty-six percent'.",
        "bloque_sugerido": "Technical Discussion 30 min • Combined cycles, heat recovery steam generators and CHP ratios"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Photovoltaic Cell Equivalent Circuit & Shockley Diode Equation",
        "objetivo": "Expresar la ecuación no lineal de corriente-voltaje del modelo de un diodo con resistencias serie y paralelo en celdas fotovoltaicas.",
        "concepto_clave_latex": r"I = I_{ph} - I_0 \left[ \exp\left( \frac{q(V + I R_s)}{n k_B T} \right) - 1 \right] - \frac{V + I R_s}{R_{sh}} \quad ; \quad P = V I \quad ; \quad \frac{dP}{dV} = 0 \text{ at MPPT}",
        "verbalizacion_ingles": "• I = I_ph - I_0 * [exp(q(V + I R_s) / (n k_B T)) - 1] - (V + I R_s) / R_sh -> \"terminal current I equals photogenerated photocurrent I sub ph minus reverse saturation current I nought times quantity exponential of elementary charge q times quantity voltage V plus current times series resistance R sub s divided by ideality factor n times Boltzmann constant k sub B times temperature T, minus one, minus quantity V plus I R sub s divided by shunt resistance R sub sh\".\n• dP/dV = 0 -> \"the first derivative of electrical power with respect to voltage equals zero at the maximum power point\".",
        "ejemplo": "En algoritmos MPPT para inversores solares: 'The perturb-and-observe controller continuously tracks the maximum power point by dithering operating voltage until dP over dV approaches zero'.",
        "bloque_sugerido": "Speaking Drill 30 min • Photovoltaic single-diode model, series resistance and MPPT"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Wind Turbine Aerodynamic Power & Betz Limit Equation",
        "objetivo": "Verbalizar la ecuación de potencia eólica capturable, coeficiente de potencia $C_p$ y límite teórico de Betz en inglés.",
        "concepto_clave_latex": r"P_{aero} = \frac{1}{2} \rho A v_w^3 C_p(\lambda, \beta) \quad [\text{W}] \quad ; \quad \lambda = \frac{\omega R}{v_w} \quad ; \quad C_{p, Betz} = \frac{16}{27} \approx 0.5926",
        "verbalizacion_ingles": "• P_aero = 1/2 rho A v_w^3 C_p(lambda, beta) -> \"aerodynamic mechanical power equals one-half air density rho times rotor swept area A times wind velocity v sub w cubed times power coefficient C sub p as a function of tip-speed ratio lambda and blade pitch angle beta, in watts\".\n• lambda = (omega * R) / v_w -> \"tip-speed ratio lambda equals rotor angular velocity omega times blade tip radius R divided by upstream wind velocity v sub w, dimensionless\".\n• C_p_Betz = 16/27 -> \"Betz theoretical limit states that no wind turbine can extract more than sixteen twenty-sevenths, or approximately fifty-nine point twenty-six percent, of kinetic energy in the wind\".",
        "ejemplo": "En parques eólicos de alta mar: 'Because wind power scales with the cube of wind speed, a ten percent increase in velocity yields a thirty-three percent boost in gross power generation'.",
        "bloque_sugerido": "Technical Dialogue 30 min • Aerodynamic power coefficient, tip-speed ratio and Betz limit"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Fuel Cell Polarization Curve & Activation / Ohmic / Concentration Losses",
        "objetivo": "Articular la curva de voltaje de celda de combustible restando sobrepotenciales de activación (Tafel), óhmicos y de concentración del potencial reversible de Nernst.",
        "concepto_clave_latex": r"V_{cell} = E_{Nernst} - \eta_{act} - \eta_{ohm} - \eta_{conc} \quad ; \quad \eta_{act} = \frac{RT}{\alpha F}\ln\left(\frac{i}{i_0}\right) \quad ; \quad \eta_{ohm} = i R_{int} \quad ; \quad \eta_{conc} = -\frac{RT}{nF}\ln\left(1 - \frac{i}{i_L}\right)",
        "verbalizacion_ingles": "• V_cell = E_Nernst - eta_act - eta_ohm - eta_conc -> \"operating cell voltage equals reversible Nernst potential minus activation overpotential eta sub act minus ohmic overpotential eta sub ohm minus mass-transport concentration overpotential eta sub conc\".\n• eta_act = (R T / (alpha F)) * ln(i / i_0) -> \"activation loss follows the Tafel equation: gas constant R times temperature T divided by charge transfer coefficient alpha times Faraday constant F times the natural logarithm of current density i over exchange current density i nought\".\n• eta_ohm = i * R_int -> \"ohmic loss equals current density i times internal area-specific resistance R sub int\".\n• eta_conc -> \"concentration loss equals minus R T over n F times natural log of quantity one minus current density i divided by limiting current density i sub L\".",
        "ejemplo": "En celdas PEM automotrices: 'At high current densities above one point five amperes per square centimeter, concentration overpotential dominates due to liquid water flooding the gas diffusion layer'.",
        "bloque_sugerido": "Speaking Drill 30 min • Fuel cell polarization curve, Tafel slope and limiting current"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Continuous State-Space Representation & Matrix Exponential Solution",
        "objetivo": "Expresar la representación en espacio de estados lineal en tiempo continuo y la solución analítica mediante matriz de transición $e^{At}$.",
        "concepto_clave_latex": r"\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) \quad ; \quad \mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) \quad ; \quad \mathbf{x}(t) = e^{\mathbf{A}t}\mathbf{x}(0) + \int_0^t e^{\mathbf{A}(t-\tau)}\mathbf{B}\mathbf{u}(\tau)d\tau",
        "verbalizacion_ingles": "• x_dot(t) = A x(t) + B u(t) -> \"state vector time derivative x dot of t equals state matrix A times state vector x of t plus input matrix B times control input vector u of t\".\n• y(t) = C x(t) + D u(t) -> \"output vector y of t equals output matrix C times state vector x of t plus feedforward direct transmission matrix D times input vector u of t\".\n• x(t) = exp(At) x(0) + integral -> \"state trajectory x of t equals matrix exponential e to the A t times initial state vector x of zero plus the convolution integral from zero to t of e to the A times quantity t minus tau, times B times control input u of tau d tau\".",
        "ejemplo": "En el control de inversores interconectados a red: 'The internal voltage and current states are represented in a synchronous dq reference frame using a fifth-order state-space model'.",
        "bloque_sugerido": "Technical Discussion 30 min • State-space matrices, controllability and transition matrix"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Exergy Destruction Rate & Gouy-Stodola Irreversibility Theorem",
        "objetivo": "Verbalizar el teorema de Gouy-Stodola que relaciona la tasa de destrucción de exergía con la generación de entropía y temperatura del ambiente de referencia.",
        "concepto_clave_latex": r"\dot{I} = \dot{E}x_D = T_0 \dot{S}_{gen} \quad [\text{kW}] \quad ; \quad \dot{S}_{gen} = \frac{dS_{sys}}{dt} - \sum \frac{\dot{Q}_k}{T_k} - \sum \dot{m}_i s_i + \sum \dot{m}_e s_e \ge 0 \quad ; \quad \psi = (h - h_0) - T_0(s - s_0)",
        "verbalizacion_ingles": "• I_dot = Ex_dot_D = T_0 * S_dot_gen -> \"rate of exergy destruction I dot, or irreversibility rate Ex dot sub D, equals dead-state ambient absolute temperature T nought times rate of entropy generation S dot gen, in kilowatts\".\n• S_dot_gen >= 0 -> \"rate of entropy generation is strictly greater than or equal to zero for all real physical processes according to the Second Law of Thermodynamics\".\n• psi = (h - h_0) - T_0 * (s - s_0) -> \"specific flow exergy psi equals specific enthalpy h minus dead-state enthalpy h nought minus dead-state temperature T nought times specific entropy s minus dead-state entropy s nought, in kilojoules per kilogram\".",
        "ejemplo": "En análisis exergoeconómico de calderas de vapor: 'Because combustion irreversibility accounts for sixty-five percent of overall exergy destruction, preheating combustion air with flue gases directly mitigates Gouy-Stodola losses'.",
        "bloque_sugerido": "Speaking Drill 30 min • Gouy-Stodola theorem, exergy destruction and dead-state reference"
    }
]

def upgrade_english_4():
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    
    idx1 = content.find('      - codigo: "01021805"')
    idx2 = content.find('      - codigo: "03021817"', idx1)
    if idx1 == -1 or idx2 == -1:
        print("ERROR: Could not find English IV section in DB.")
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
    if not asig_block.endswith('\n'):
        asig_block += '\n'
    asig_block = asig_block + new_not_yaml
    
    new_content = content[:idx1] + asig_block + content[idx2:]
    
    open(DB_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    open(ASSETS_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    print("01021805 General English IV successfully expanded to 30 topics (15 General + 15 Notación)!")

if __name__ == '__main__':
    upgrade_english_4()
