# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, escape_yaml_str, DB_PATH, ASSETS_PATH

# 5 New General English V topics (11 to 15) with >= 5 slides and concepto_clave_latex: ""
new_general_topics = [
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "general",
        "titulo": "Hedging and Cautious Language in Engineering Reports",
        "objetivo": "Utilizar lenguaje tentativo y de matización (hedging) mediante verbos modales, adverbios de probabilidad y verbos epistémicos para calificar afirmaciones científicas según normas IEEE.",
        "concepto_clave_latex": "",
        "ejemplo": "The experimental results appear to indicate a marginal increase in cell degradation under elevated ambient temperatures.",
        "bloque_sugerido": "Hedging Clinic 40 min • Transforming bold claims into cautious academic prose",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR C1 • CORE CONCEPT",
                "titulo": "The Purpose of Hedging in Technical Writing",
                "puntos": [
                    "Engineering claims must reflect appropriate levels of scientific certainty and experimental boundaries.",
                    "Overstating results ('This proves that...') weakens technical credibility and invites reviewer rejection.",
                    "Hedging distinguishes between established physical laws and plausible hypotheses or observed tendencies."
                ]
            },
            {
                "numero": 2,
                "seccion": "CEFR C1 • MODAL AUXILIARIES",
                "titulo": "Graded Modals for Caution",
                "puntos": [
                    "Certainty (100%): 'will produce', 'is determined by'.",
                    "High Probability (~80%): 'should reduce', 'is likely to mitigate'.",
                    "Possibility (~50%): 'may indicate', 'could contribute to'.",
                    "Low Probability (~25%): 'might suggest', 'would appear to follow'."
                ]
            },
            {
                "numero": 3,
                "seccion": "CEFR C1 • EPISTEMIC VERBS",
                "titulo": "Distance-Creating Reporting Verbs",
                "puntos": [
                    "'The data suggests that...' instead of 'The data proves that...'.",
                    "'The simulation tends to underestimate peak load by 4%.'",
                    "'The algorithm appears to converge faster in meshed configurations.'",
                    "'Preliminary measurements seem consistent with the proposed thermal model.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "CEFR C1 • PROBABILITY ADVERBIALS",
                "titulo": "Nuanced Adverbial Modifiers",
                "puntos": [
                    "Frequency/Scope: 'predominantly', 'substantially', 'to a certain extent'.",
                    "Degree: 'marginally', 'moderately', 'noticeably higher'.",
                    "Belief: 'plausibly', 'reportedly', 'arguably the most efficient architecture.'",
                    "Example: 'The efficiency gain was marginally lower than expected due to parasitic losses.'"
                ]
            },
            {
                "numero": 5,
                "seccion": "CEFR C1 • APPLICATION",
                "titulo": "Sentence Transformation Drill",
                "puntos": [
                    "Bold: 'Turbine vibration causes fatigue failure.'",
                    "Hedged: 'Excessive turbine vibration appears to accelerate fatigue failure under cyclic aerodynamic loads.'",
                    "Bold: 'Our converter is 100% stable.'",
                    "Hedged: 'The proposed converter demonstrated robust stability across the evaluated operating envelope.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "general",
        "titulo": "Complex Passives and Impersonal Reporting Structures",
        "objetivo": "Redactar resúmenes ejecutivos y revisiones bibliográficas usando estructuras impersonales de nivel C1 ('It is widely acknowledged that...', 'The prototype is reported to have...').",
        "concepto_clave_latex": "",
        "ejemplo": "It has long been recognized that grid inertia declines as inverter-based resources replace synchronous generators.",
        "bloque_sugerido": "Impersonal Structures 40 min • Passive reporting verbs in state-of-the-art sections",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR C1 • CORE PATTERN",
                "titulo": "Impersonal 'It' Construction",
                "puntos": [
                    "Pattern: 'It is + [past participle] + that-clause'.",
                    "Used to state general consensus or collective research findings objectively.",
                    "Common verbs: acknowledged, argued, believed, estimated, hypothesized, observed.",
                    "Example: 'It is generally estimated that offshore wind capacity will quadruple by 2035.'"
                ]
            },
            {
                "numero": 2,
                "seccion": "CEFR C1 • PERSONAL PASSIVE",
                "titulo": "Subject + Passive Verb + To-Infinitive",
                "puntos": [
                    "Pattern: 'Subject + is/are + [past participle] + to + [infinitive]'.",
                    "More concise and dynamic than the dummy 'it' structure.",
                    "Example: 'The perovskite cell is reported to exceed 28% efficiency under laboratory conditions.'",
                    "Past reference: 'The substation was reported to have tripped at 14:32 UTC.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "CEFR C1 • ACADEMIC OBJECTIVITY",
                "titulo": "Avoiding Personal Pronouns (I, We, You)",
                "puntos": [
                    "Instead of: 'We found that harmonic distortion increased.'",
                    "Use: 'Harmonic distortion was found to increase at high modulation indices.'",
                    "Instead of: 'You can see the voltage drop in Figure 4.'",
                    "Use: 'The voltage drop is clearly evidenced in Figure 4.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "CEFR C1 • CONTINUOUS & PERFECT FORMS",
                "titulo": "Advanced Passive Infinitives",
                "puntos": [
                    "Continuous: 'The transformer is understood to be operating near its thermal limit.'",
                    "Perfect: 'The gas turbine is believed to have undergone scheduled maintenance last month.'",
                    "Passive infinitive: 'The policy is expected to be ratified by the energy commission in Q4.'"
                ]
            },
            {
                "numero": 5,
                "seccion": "CEFR C1 • EDITING PRACTICE",
                "titulo": "Executive Summary Polish",
                "puntos": [
                    "Draft: 'Engineers believe that hydrogen blending causes micro-cracking.'",
                    "Revised: 'Hydrogen blending is hypothesized to induce micro-crack propagation in API 5L line pipes.'",
                    "Maintain formal register, academic detachment, and concise flow throughout the document."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "general",
        "titulo": "Mixed Conditionals in Engineering Failure Analysis and Risk Assessment",
        "objetivo": "Construir oraciones condicionales mixtas para vincular hipótesis pasadas con consecuencias presentes en investigaciones de accidentes y análisis de causas raíz (RCA).",
        "concepto_clave_latex": "",
        "ejemplo": "If the protective relay had cleared the short circuit instantaneously, the transformer would not be out of service today.",
        "bloque_sugerido": "Root-Cause Conditionals 40 min • Mixed conditionals in failure investigation reports",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR C1 • LOGICAL RELATION",
                "titulo": "Past Cause with Present Consequence (Type 3 + Type 2)",
                "puntos": [
                    "Condition in the past (Past Perfect) -> Result in the present (Would + bare infinitive).",
                    "Formula: 'If + had + V3, Subject + would/could/might + V1'.",
                    "Used to explain how a past omission or event directly causes an ongoing operational state.",
                    "Example: 'If the team had installed surge arresters, the inverter would not be offline now.'"
                ]
            },
            {
                "numero": 2,
                "seccion": "CEFR C1 • ALTERNATIVE MIX",
                "titulo": "Present Permanent Trait with Past Consequence (Type 2 + Type 3)",
                "puntos": [
                    "Condition is a permanent state or trait (Past Simple) -> Result was a past event (Would have + V3).",
                    "Formula: 'If + Past Simple, Subject + would have + V3'.",
                    "Used when a permanent system limitation or design flaw caused a specific failure.",
                    "Example: 'If the battery chemistry were inherently non-flammable, thermal runaway would not have occurred.'"
                ]
            },
            {
                "numero": 3,
                "seccion": "CEFR C1 • FORMAL INVERSION",
                "titulo": "Inverted Conditional Forms (Without 'If')",
                "puntos": [
                    "Type 3: 'Had the operator checked the differential pressure, the filter rupture could have been avoided.'",
                    "Type 2: 'Were the conductor diameter larger, joule losses would be significantly lower.'",
                    "Type 1: 'Should the frequency drop below 59.5 Hz, under-frequency shedding will activate.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "CEFR C1 • CONJUNCTIVE VARIANTS",
                "titulo": "Provided that, Unless, and But for",
                "puntos": [
                    "'Provided that cooling water flow is maintained, operating temperature remains stable.'",
                    "'Unless the bypass valve opens, pipeline pressure will exceed safe operating limits.'",
                    "'But for the backup diesel generator, the control center would have lost SCADA telemetry.'"
                ]
            },
            {
                "numero": 5,
                "seccion": "CEFR C1 • ROOT CAUSE ANALYSIS DRILL",
                "titulo": "Drafting Post-Incident Reports",
                "puntos": [
                    "Scenario: A blackout occurred because an aging insulator flashed over during rain.",
                    "Statement: 'Had thermal imaging inspections been performed last quarter, the degraded insulator would have been identified prior to failure.'",
                    "Express precise causal links, counterfactual arguments, and preventive recommendations."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Nominalisation and Information Density in Technical Writing",
        "objetivo": "Optimizar la densidad léxica y concisión estilística transformando estructuras verbales y oraciones subordinadas en sintagmas nominales complejos según estándares de Elsevier y Springer.",
        "concepto_clave_latex": "",
        "ejemplo": "The rapid deployment of distributed battery storage facilitated peak shaving and feeder congestion relief.",
        "bloque_sugerido": "Lexical Density 40 min • Nominalisation techniques for high-impact journal abstracts",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR C1 • STYLISTIC PRINCIPLE",
                "titulo": "What is Nominalisation?",
                "puntos": [
                    "Converting verbs, adjectives, and entire clauses into noun phrases (e.g., 'to combust' -> 'combustion').",
                    "Increases information density: packs more technical content into fewer words.",
                    "Creates thematic cohesion: previous sentence actions become subjects of subsequent sentences.",
                    "hallmark of professional peer-reviewed research papers and engineering standards."
                ]
            },
            {
                "numero": 2,
                "seccion": "CEFR C1 • VERB-TO-NOUN MAPPING",
                "titulo": "Common Derivational Suffixes",
                "puntos": [
                    "-tion / -sion: fluctuate -> fluctuation; convert -> conversion.",
                    "-ance / -ence: resist -> resistance; emit -> emittance / emission.",
                    "-ment: deploy -> deployment; degrade -> degradation.",
                    "-ity: conduct -> conductivity; unstable -> instability."
                ]
            },
            {
                "numero": 3,
                "seccion": "CEFR C1 • COMPLEX COMPOUND NOUNS",
                "titulo": "Pre-modifying Noun Chains",
                "puntos": [
                    "Clause: 'A system that monitors the temperature of batteries in real time.'",
                    "Nominalised: 'A real-time battery temperature monitoring system.'",
                    "Clause: 'When solar irradiation drops intermittently.'",
                    "Nominalised: 'Intermittent solar irradiance attenuation.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "CEFR C1 • AVOIDING PITFALLS",
                "titulo": "Preventing 'Zombie Noun' Clutter",
                "puntos": [
                    "Over-nominalisation can make prose dense, leaden, and difficult to comprehend.",
                    "Weak: 'The implementation of the algorithm was conducted by the research team.'",
                    "Strong: 'The research team implemented the algorithm.'",
                    "Rule: Nominalise to connect concepts and increase flow; keep active verbs for core methodology."
                ]
            },
            {
                "numero": 5,
                "seccion": "CEFR C1 • ABSTRACT REFACTORING",
                "titulo": "Hands-on Density Exercise",
                "puntos": [
                    "Verbose (28 words): 'Because the rotor rotated faster than normal, the bearings began to wear down and this caused the gearbox to fail unexpectedly.'",
                    "Concise (14 words): 'Excessive rotor rotational speed accelerated bearing degradation, culminating in catastrophic gearbox failure.'",
                    "Word count reduced by 50% while elevating academic rigor."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 3,
        "modalidad": "general",
        "titulo": "Structuring Oral Presentations, Keynote Addresses and Q&A Defense",
        "objetivo": "Estructurar exposiciones orales para conferencias internacionales IEEE utilizando frases de señalización (signposting), manejo de preguntas difíciles y refutación diplomática.",
        "concepto_clave_latex": "",
        "ejemplo": "That is an insightful observation; nevertheless, our sensitivity analysis demonstrates that the model remains robust against price fluctuations.",
        "bloque_sugerido": "Conference Keynote 40 min • Signposting phrases and handling peer-review Q&A gracefully",
        "slides": [
            {
                "numero": 1,
                "seccion": "CEFR C1 • PRESENTATION ARCHITECTURE",
                "titulo": "The Three-Part Technical Address",
                "puntos": [
                    "Introduction (15%): Hook the audience, define the research question, outline key takeaways.",
                    "Body (70%): Present methodology, experimental validation, and quantitative outcomes with clear signposts.",
                    "Conclusion (15%): Summarize contributions, state practical implications, propose future work."
                ]
            },
            {
                "numero": 2,
                "seccion": "CEFR C1 • SIGNPOSTING DISCOURSE",
                "titulo": "Navigational Markers for the Audience",
                "puntos": [
                    "Transitioning: 'Turning now to our numerical findings...', 'Let us direct our attention to Table 2.'",
                    "Digressing & Returning: 'To put this into context...', 'Returning to our central hypothesis...'",
                    "Emphasizing: 'What is particularly noteworthy here is...', 'The pivotal takeaway is that...'",
                    "Concluding: 'To recap our main findings...', 'In light of these outcomes, we recommend...'"
                ]
            },
            {
                "numero": 3,
                "seccion": "CEFR C1 • DATA COMMENTARY",
                "titulo": "Verbalizing Graphical Trends",
                "puntos": [
                    "Upward trends: 'plateaued', 'surged', 'experienced steady growth'.",
                    "Fluctuations: 'oscillated within a 5% band', 'exhibited periodic dips'.",
                    "Peaks and troughs: 'peaked at 480 MW', 'bottomed out at zero'.",
                    "Example: 'As illustrated in the contour plot, thermal stress peaks at the blade root.'"
                ]
            },
            {
                "numero": 4,
                "seccion": "CEFR C1 • DEFENDING IN Q&A",
                "titulo": "Tactful Responses to Difficult Questions",
                "puntos": [
                    "Validating the question: 'That is a compelling point...', 'Thank you for raising that crucial aspect.'",
                    "Buying time to formulate: 'If I understand your query correctly, you are asking whether...'",
                    "Conceding gracefully: 'That limitation is acknowledged; we plan to address it in future iterations.'",
                    "Diplomatic disagreement: 'While I see the merit of that approach, our simulations suggest...'"
                ]
            },
            {
                "numero": 5,
                "seccion": "CEFR C1 • CONFERENCING SIMULATION",
                "titulo": "Elevator Pitch & IEEE Closing",
                "puntos": [
                    "Pitch: 'Our framework enables sub-second optimal dispatch of hybrid microgrids, reducing curtailment by 34%.'",
                    "Closing: 'Thank you for your time and attention. I would be delighted to take any questions or comments.'",
                    "Maintains poise, academic integrity, and professional executive presence."
                ]
            }
        ]
    }
]

# 9 New Engineering Notation topics (22 to 30) for General English V
new_notation_topics = [
    {
        "numero_tema": 22,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Compressible Gas Dynamics & Isentropic Flow Notation",
        "objetivo": "Verbalizar en inglés el número de Mach, relaciones de estancamiento isentrópico y el flujo másico crítico en toberas de turbinas de gas.",
        "concepto_clave_latex": r"Ma = \frac{v}{c} \quad ; \quad \frac{T_0}{T} = 1 + \frac{\gamma - 1}{2} Ma^2 \quad ; \quad \frac{P_0}{P} = \left( 1 + \frac{\gamma - 1}{2} Ma^2 \right)^{\frac{\gamma}{\gamma - 1}}",
        "verbalizacion_ingles": "• Ma = v / c -> \"Mach number Ma equals flow velocity v divided by speed of sound c\".\n• T_0 / T = 1 + ((γ - 1)/2) Ma² -> \"stagnation temperature T naught over static temperature T equals one plus quantity gamma minus one over two times Mach number squared\".\n• P_0 / P = (1 + ((γ - 1)/2) Ma²)^(γ/(γ - 1)) -> \"total pressure P naught over static pressure P equals quantity one plus gamma minus one over two times Mach squared, all raised to the power of gamma over gamma minus one\".",
        "ejemplo": "Exposición oral del comportamiento supersónico en la tobera de una turbina de expansión criogénica para licuefacción de gas natural.",
        "bloque_sugerido": "Gas Dynamics Speech 35 min • Stagnation pressure, speed of sound & Mach verbalization",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Compressible Aerodynamics Symbols",
                "puntos": [
                    "Mach number (Ma or M): Subsonic (Ma < 1), Transonic (0.8 < Ma < 1.2), Supersonic (Ma > 1).",
                    "Stagnation or total states are indexed with subscript zero (T_0: 'T naught' or 'T zero').",
                    "Specific heat ratio gamma (gamma = c_p / c_v, typically 1.4 for air and 1.3 for natural gas)."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Nozzle Choking & Shock Waves",
                "puntos": [
                    "Pronounce: 'When back pressure drops below critical pressure ratio P-star over P-naught, the throat chokes at Mach one.'",
                    "Pronounce: 'Normal shock wave entails an abrupt entropy increase with supersonic deceleration.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Navier-Stokes Equations & Boundary Layer Theory Notation",
        "objetivo": "Exponer oralmente en inglés la ecuación vectorial de cantidad de movimiento de Navier-Stokes y los parámetros de capa límite de Prandtl.",
        "concepto_clave_latex": r"\rho \left( \frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} \right) = -\nabla p + \mu \nabla^2 \mathbf{u} + \rho \mathbf{g} \quad ; \quad \delta(x) \approx \frac{5.0 x}{\sqrt{Re_x}}",
        "verbalizacion_ingles": "• ρ (∂u/∂t + u · ∇u) = -∇p + μ ∇²u + ρ g -> \"fluid density rho times open parenthesis partial u by partial t plus velocity vector u dot del u close parenthesis equals minus gradient of pressure del p plus dynamic viscosity mu times laplacian of u del-squared u plus rho times gravity vector g\".\n• δ(x) ≈ 5.0 x / √(Re_x) -> \"laminar boundary layer thickness delta of x equals approximately five point zero times distance x divided by the square root of Reynolds number sub x\".",
        "ejemplo": "Presentación formal de la simulación CFD de desprendimiento de capa límite en el extradós del álabe de una turbina eólica marina.",
        "bloque_sugerido": "Fluid Dynamics Keynote 35 min • Navier-Stokes vector operators & Prandtl boundary layer",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Vector Differential Operators in Fluid Mechanics",
                "puntos": [
                    "Nabla / Del (nabla or nabla-squared): 'grad p' (gradient), 'div u' (divergence), 'laplacian u'.",
                    "Advective acceleration term (u · ∇u): 'u dot grad u' represents non-linear convective inertia.",
                    "Viscous diffusion term: mu times del-squared u accounts for internal shear dissipation."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Boundary Layer Metrics",
                "puntos": [
                    "Displacement thickness delta-star: 'delta star equals integral from zero to infinity of one minus u over U-infinity d y'.",
                    "Momentum thickness theta: 'momentum thickness theta quantifies the loss of momentum flux across the boundary layer.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Radiative Heat Transfer, View Factors & Stefan-Boltzmann Enclosures",
        "objetivo": "Verbalizar en inglés factores de visión radiativa F_ij, radiosidad J, irradiación G y transferencia neta en recintos grises.",
        "concepto_clave_latex": r"F_{12} = \frac{1}{A_1} \int_{A_1} \int_{A_2} \frac{\cos\theta_1 \cos\theta_2}{\pi S^2} dA_1 dA_2 \quad ; \quad q_{12} = \frac{\sigma(T_1^4 - T_2^4)}{\frac{1-\varepsilon_1}{\varepsilon_1 A_1} + \frac{1}{A_1 F_{12}} + \frac{1-\varepsilon_2}{\varepsilon_2 A_2}}",
        "verbalizacion_ingles": "• F_{12} -> \"view factor F one-two equals one over area A one times the double integral over A one and A two of cosine theta one times cosine theta two divided by pi times distance S squared d A one d A two\" (Reciprocity: \"A one times F one-two equals A two times F two-one\").\n• q_{12} -> \"net radiative exchange q one-two equals sigma times difference T one to the fourth minus T two to the fourth, divided by the sum of surface and geometric radiative resistances\".",
        "ejemplo": "Exposición del balance térmico radiativo en la cámara de combustión de una caldera de biomasa con paredes de agua tubulares.",
        "bloque_sugerido": "Radiation Exchange Talk 35 min • View factors, reciprocity rule & surface network resistance",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Radiation Network Analogy",
                "puntos": [
                    "Surface resistance: (1 - epsilon) / (epsilon * A), verbalized as 'one minus emissivity over emissivity times area'.",
                    "Space (geometric) resistance: 1 / (A_1 * F_12), verbalized as 'one over A one times view factor F one-two'.",
                    "Summation rule in enclosures: 'the sum of view factors F sub i j over all enclosing surfaces j equals one'."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Radiosity and Irradiation",
                "puntos": [
                    "Irradiation G: 'total incident radiation flux G in watts per square meter'.",
                    "Radiosity J: 'total radiation flux leaving a surface J equals emitted plus reflected flux'."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 2,
        "modalidad": "notacion_ingenieria",
        "titulo": "Transient Heat Conduction: Biot and Fourier Numbers Notation",
        "objetivo": "Exponer en inglés el análisis de capacidad concentrada (Lumped Capacitance), número de Biot y número de Fourier en enfriamiento transitorio.",
        "concepto_clave_latex": r"Bi = \frac{h L_c}{k} < 0.1 \quad ; \quad \frac{T(t) - T_\infty}{T_i - T_\infty} = \exp\left( -\frac{t}{\tau_t} \right) \quad ; \quad \tau_t = \frac{\rho V c_p}{h A_s} \quad ; \quad Fo = \frac{\alpha t}{L_c^2}",
        "verbalizacion_ingles": "• Bi = h L_c / k -> \"Biot number Bi equals convection coefficient h times characteristic length L sub c divided by thermal conductivity k\" (validity: \"Bi less than zero point one justifies lumped capacitance\").\n• (T(t) - T_∞)/(T_i - T_∞) = exp(-t / τ) -> \"dimensionless temperature ratio theta over theta-initial equals exponential of minus time t over thermal time constant tau\".\n• Fo = α t / L_c² -> \"Fourier number Fo equals thermal diffusivity alpha times time t divided by characteristic length squared\".",
        "ejemplo": "Defensa técnica del enfriamiento térmico de cilindros de almacenamiento de hidrógeno presurizado durante ciclos de llenado rápido.",
        "bloque_sugerido": "Transient Thermal Defense 35 min • Biot number validity, thermal time constant & Fourier number",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Dimensionless Thermal Numbers",
                "puntos": [
                    "Biot number (Bi): Ratio of internal conduction resistance to external convection resistance.",
                    "Fourier number (Fo): Dimensionless time measuring the degree of thermal penetration into a solid.",
                    "Characteristic length L_c: Volume divided by surface area (V / A_s)."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Lumped System Decay",
                "puntos": [
                    "Pronounce: 'When Biot number is below zero point one, temperature gradients inside the body are negligible.'",
                    "Pronounce: 'The thermal time constant tau equals rho times volume times specific heat divided by h times surface area.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Park dq0 Transformation in Synchronous Machines & Inverter Control",
        "objetivo": "Verbalizar en inglés la matriz de transformación d-q-0 de Park para el control vectorial por orientación de campo (FOC) de generadores síncronos e inversores.",
        "concepto_clave_latex": r"\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} = \frac{2}{3} \begin{bmatrix} \cos\theta & \cos(\theta - \frac{2\pi}{3}) & \cos(\theta + \frac{2\pi}{3}) \\ -\sin\theta & -\sin(\theta - \frac{2\pi}{3}) & -\sin(\theta + \frac{2\pi}{3}) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}",
        "verbalizacion_ingles": "• [v_d, v_q, v_0]^T = P(θ) [v_a, v_b, v_c]^T -> \"the direct, quadrature, and zero-sequence voltage vector v d-q-zero equals two-thirds times the Park transformation matrix of electrical rotor angle theta times three-phase voltage vector v a-b-c\".\n• Direct axis d: \"aligns with the rotor magnetic flux path (field excitation)\".\n• Quadrature axis q: \"leads the direct axis by ninety electrical degrees (torque-producing component)\".",
        "ejemplo": "Presentación del lazo de control de corriente desacoplada id-iq en el convertidor del rotor de una turbina eólica DFIG.",
        "bloque_sugerido": "Park Transform Speech 35 min • Direct and quadrature axes, rotating frame & angle theta",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Rotating Reference Frame Concept",
                "puntos": [
                    "Converts three-phase AC sinusoidal quantities (stationary a-b-c frame) into two DC quantities (synchronously rotating d-q frame).",
                    "Enables classical PI controllers to achieve zero steady-state error without requiring complex resonant PR controllers.",
                    "Direct-axis current i_d controls reactive power or flux; quadrature-axis current i_q controls active power or torque."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Phase-Locked Loop (PLL) Locking",
                "puntos": [
                    "Pronounce: 'The phase-locked loop aligns the direct axis with the grid voltage vector by driving v-q to zero.'",
                    "Pronounce: 'Decoupling feedforward terms eliminate cross-coupling between the d-axis and q-axis current loops.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Power Quality: Total Harmonic Distortion (THD) & Distortion Power (IEEE 519)",
        "objetivo": "Exponer oralmente en inglés la distorsión armónica total de tensión y corriente (THD_v, THD_i), factor de potencia de desplazamiento y potencia aparente de Budeanu.",
        "concepto_clave_latex": r"\text{THD}_V = \frac{\sqrt{\sum_{h=2}^{\infty} V_h^2}}{V_1} \times 100\% \quad ; \quad S = \sqrt{P^2 + Q_1^2 + D^2} \quad ; \quad PF = \frac{P}{S} = \frac{1}{\sqrt{1 + \text{THD}_I^2}} \cos\phi_1",
        "verbalizacion_ingles": "• THD_V = (√(Σ V_h²)) / V_1 * 100% -> \"total harmonic voltage distortion T-H-D sub V equals the square root of the sum of harmonic voltages V sub h squared from h equals two to infinity, divided by fundamental voltage V sub one, expressed as a percentage\".\n• S = √(P² + Q_1² + D²) -> \"total apparent power S equals the square root of active power P squared plus fundamental reactive power Q one squared plus distortion power D squared\".\n• PF = (1 / √(1 + THD_I²)) cos φ_1 -> \"true power factor equals distortion factor times displacement power factor cosine phi one\".",
        "ejemplo": "Defensa de cumplimiento de la norma IEEE 519 en el punto de acoplamiento común (PCC) de una planta de carga de autobuses eléctricos.",
        "bloque_sugerido": "Harmonics & IEEE 519 Defense 35 min • Verbalizing THD, distortion power D & true power factor",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "IEEE 519 Harmonic Terminology",
                "puntos": [
                    "Fundamental frequency component (subscript 1): 60 Hz in Colombia/USA, 50 Hz in Europe.",
                    "Harmonic order h: integer multiple of the fundamental (e.g., 5th harmonic = 300 Hz).",
                    "Total Demand Distortion (TDD): THD normalized against maximum demand load current rather than instantaneous current."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "True Power Factor vs Displacement",
                "puntos": [
                    "Pronounce: 'Displacement power factor is cosine phi one; true power factor incorporates harmonic current distortion.'",
                    "Pronounce: 'Active power filters inject anti-phase harmonic currents to cancel non-linear load distortion.'"
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Fuel Cell Polarization Curve & Butler-Volmer Overpotential Notation",
        "objetivo": "Exponer en inglés la curva de polarización de celdas de combustible PEM/SOFC, sobrepotenciales de activación (Tafel), óhmicos y de concentración.",
        "concepto_clave_latex": r"V_{\text{cell}} = E_{\text{Nernst}} - \eta_{\text{act}} - \eta_{\text{ohmic}} - \eta_{\text{conc}} \quad ; \quad \eta_{\text{act}} = \frac{RT}{\alpha F} \ln\left(\frac{j}{j_0}\right) \quad ; \quad \eta_{\text{ohmic}} = j \cdot R_{\text{ohm}}",
        "verbalizacion_ingles": "• V_cell = E_Nernst - η_act - η_ohmic - η_conc -> \"cell operating voltage equals Nernst thermodynamic reversible potential minus activation overpotential eta act minus ohmic loss eta ohmic minus mass-transport concentration overpotential eta conc\".\n• η_act = (RT / αF) ln(j / j_0) -> \"activation overpotential equals R T over transfer coefficient alpha times Faraday constant F times the natural logarithm of current density j over exchange current density j naught (Tafel slope)\".\n• η_ohmic = j * R_ohm -> \"ohmic overpotential equals current density j in amps per square centimeter times area-specific ionic resistance R ohm\".",
        "ejemplo": "Exposición oral del ajuste paramétrico de la curva de polarización experimental de una celda de combustible PEM de automoción.",
        "bloque_sugerido": "Fuel Cell Polarization Talk 35 min • Butler-Volmer kinetics, Tafel slope & mass-transport limit",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "The Three Loss Regimes of Polarization",
                "puntos": [
                    "Low current density: Activation losses dominate due to sluggish oxygen reduction reaction (ORR) kinetics.",
                    "Intermediate current density: Linear slope dominated by ohmic resistance in the proton exchange membrane.",
                    "High current density: Sharp drop dominated by mass-transport limitation and reactant starvation."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Electrochemical Kinetics Terminology",
                "puntos": [
                    "Exchange current density j_0: 'exchange current density j naught reflects the intrinsic electrocatalytic activity'.",
                    "Faraday constant F: 'Faraday constant F equals ninety-six thousand four hundred eighty-five coulombs per mole'."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Life-Cycle Carbon Accounting & Avoided Emissions Notation",
        "objetivo": "Verbalizar en inglés factores de reducción neta de GEI, factor marginal de red, amortización de carbono (CPBT) y créditos de carbono.",
        "concepto_clave_latex": r"\Delta \text{GHG} = E_{\text{gen}} \cdot (\text{EF}_{\text{grid,marg}} - \text{EF}_{\text{tech}}) \quad ; \quad \text{CPBT} = \frac{\text{GHG}_{\text{embodied}}}{\Delta \text{GHG}_{\text{annual}}} \quad [\text{years}]",
        "verbalizacion_ingles": "• ΔGHG = E_gen * (EF_grid,marg - EF_tech) -> \"net greenhouse gas abatement delta G-H-G equals annual energy generation E gen times open parenthesis marginal grid emission factor minus project technology emission factor close parenthesis\".\n• CPBT = GHG_embodied / ΔGHG_annual -> \"carbon payback time C-P-B-T equals total embodied manufacturing emissions in tons of CO2 equivalent divided by annual avoided emissions delta G-H-G annual\".",
        "ejemplo": "Defensa de la certificación de bonos de carbono de un parque solar fotovoltaico de 150 MW ante la metodología ACM0002 de Naciones Unidas.",
        "bloque_sugerido": "Carbon Accounting Defense 35 min • Marginal emission factor, embodied carbon & CPBT verbalization",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "Carbon Metrics & Accounting Standards",
                "puntos": [
                    "Embodied carbon: 'cradle-to-gate greenhouse gas emissions associated with materials and manufacturing'.",
                    "Carbon payback time (CPBT): 'the time required for a renewable asset to offset its own embodied footprint'.",
                    "Scope 1, 2, and 3 emissions: 'direct operational, indirect electricity purchases, and upstream value chain emissions'."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Marginal Abatement Cost Curve (MACC)",
                "puntos": [
                    "Pronounce: 'Marginal abatement cost equals annualized project net cost divided by metric tons of CO2 mitigated per year.'",
                    "Negative abatement cost indicates net-positive economic return through energy efficiency."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "notacion_ingenieria",
        "titulo": "Multi-Criteria Decision Making (MCDM) & TOPSIS Optimization Notation",
        "objetivo": "Exponer en inglés matrices de decisión normalizadas, distancias euclidianas euclidianas a la solución ideal y coeficiente de proximidad relativa (TOPSIS).",
        "concepto_clave_latex": r"r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{k=1}^m x_{kj}^2}} \quad ; \quad S_i^+ = \sqrt{\sum_{j=1}^n (v_{ij} - v_j^+)^2} \quad ; \quad C_i^* = \frac{S_i^-}{S_i^+ + S_i^-}",
        "verbalizacion_ingles": "• r_ij = x_ij / √(Σ x_kj²) -> \"normalized decision element r sub i j equals actual value x sub i j divided by the square root of the sum of squared criteria values x sub k j from k equals one to m\".\n• S_i^+ = √(Σ (v_ij - v_j+)²) -> \"Euclidean separation distance S sub i plus equals the square root of the sum over all criteria j of weighted value v sub i j minus positive ideal value v sub j plus, quantity squared\".\n• C_i* = S_i- / (S_i+ + S_i-) -> \"relative closeness coefficient C sub i star equals separation from negative-ideal solution divided by the sum of separations from positive-ideal and negative-ideal solutions\".",
        "ejemplo": "Defensa de la selección óptima de emplazamiento de un parque eólico marino en Colombia utilizando el algoritmo TOPSIS ponderado por AHP.",
        "bloque_sugerido": "MCDM Keynote 35 min • TOPSIS algorithm, ideal solution distance & closeness coefficient",
        "slides": [
            {
                "numero": 1,
                "seccion": "NOTATION IN ENGLISH",
                "titulo": "MCDM Multi-Criteria Optimization Symbols",
                "puntos": [
                    "Decision matrix X: Alternatives along rows (i = 1...m) and evaluation criteria along columns (j = 1...n).",
                    "Criteria weights w_j: Must satisfy the sum of w_j equals one (derived via Analytic Hierarchy Process - AHP).",
                    "Positive-ideal solution A-plus maximizes benefit criteria and minimizes cost criteria."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERBALIZATION DRILL",
                "titulo": "Ranking Alternatives Out Loud",
                "puntos": [
                    "Pronounce: 'Alternative i is ranked according to its closeness coefficient C sub i star; the option closest to one represents the optimal compromise.'",
                    "Culmination of the English for Engineering sequence at Universidad del Magdalena."
                ]
            }
        ]
    }
]

def main():
    content = open(DB_PATH, 'r', encoding='utf-8').read()
    
    # 1. Subject marker
    subj_marker = '      - codigo: "01021806"'
    if subj_marker not in content:
        print("Error: 01021806 not found.")
        sys.exit(1)
        
    next_subj_marker = '      - codigo: "04021823"'
    if next_subj_marker not in content:
        print("Error: 04021823 not found.")
        sys.exit(1)
        
    idx_start = content.index(subj_marker)
    idx_end = content.index(next_subj_marker)
    
    asig_block = content[idx_start:idx_end]
    
    # 2. Find split marker between general and notacion
    split_marker = '          - numero_tema: 11\n            corte: 1\n            modalidad: "notacion_ingenieria"'
    if split_marker not in asig_block:
        print("Error: split_marker not found in 01021806 block.")
        sys.exit(1)
        
    # Format new general topics (11 to 15)
    new_gen_yaml = format_topics_yaml(new_general_topics)
    
    # Insert new general topics before split_marker
    asig_block = asig_block.replace(split_marker, new_gen_yaml + split_marker, 1)
    
    # Renumber existing notation topics (11..16 -> 16..21) in descending order
    renumbers = [(16, 21), (15, 20), (14, 19), (13, 18), (12, 17), (11, 16)]
    for old_n, new_n in renumbers:
        target = f"          - numero_tema: {old_n}\n"
        repl = f"          - numero_tema: {new_n}\n"
        if target not in asig_block:
            print(f"Error: target {target.strip()} not found during renumbering.")
            sys.exit(1)
        asig_block = asig_block.replace(target, repl, 1)
        
    # Format new notation topics (22 to 30)
    new_not_yaml = format_topics_yaml(new_notation_topics)
    
    # Append new notation topics at the end of the subject block
    if not asig_block.endswith('\n'):
        asig_block += '\n'
    asig_block += new_not_yaml
    
    # Reassemble full content
    new_content = content[:idx_start] + asig_block + content[idx_end:]
    
    open(DB_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    open(ASSETS_PATH, 'w', encoding='utf-8', newline='\n').write(new_content)
    print("01021806 General English V successfully expanded to 30 topics (15 General + 15 Notation)!")

if __name__ == '__main__':
    main()
