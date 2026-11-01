# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after, format_topics_yaml

topics_02031812 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Química del Estado Sólido, Redes Cristalinas y Defectos Puntuales en Celdas Solares",
        "objetivo": "Analizar la estructura cristalina del silicio y perovskitas, relacionando defectos de Schottky, Frenkel y dopaje extrínseco con la recombinación de portadores de carga.",
        "concepto_clave_latex": r"n \cdot p = n_i^2 = N_c N_v \exp\left(-\frac{E_g}{k_B T}\right) \quad ; \quad N_d \approx \exp\left(-\frac{\Delta H_f}{2 k_B T}\right) \quad [\text{cm}^{-3}]",
        "ejemplo": """Problema 1: Un cristal de silicio semiconductor puro posee una banda prohibida E_g = 1.12 eV a T = 300 K. Si las densidades efectivas de estados son N_c = 2.8 × 10¹⁹ cm⁻³ y N_v = 1.04 × 10¹⁹ cm⁻³, calcule la concentración intrínseca de portadores n_i y la posición del nivel de Fermi intrínseco E_Fi respecto al centro de la banda prohibida. (Constante de Boltzmann k_B = 8.617 × 10⁻⁵ eV/K).
Paso 1: Energía térmica: k_B T = (8.617 × 10⁻⁵ eV/K)(300 K) = 0.02585 eV.
Paso 2: Exponente: -E_g / (k_B T) = -1.12 / 0.02585 = -43.327.
Paso 3: Producto n_i² = (2.8 × 10¹⁹)(1.04 × 10¹⁹) exp(-43.327) = 2.912 × 10³⁸ × 1.525 × 10⁻¹⁹ = 4.441 × 10¹⁹ cm⁻⁶.
Paso 4: n_i = √(4.441 × 10¹⁹) = 1.05 × 10¹⁰ cm⁻³.
Paso 5: Desplazamiento del nivel intrínseco: E_Fi - E_midgap = (3/4) k_B T ln(m_h* / m_e*) = (1/2) k_B T ln(N_v / N_c) = (0.5)(0.02585) ln(1.04 / 2.8) = 0.012925 × (-0.9904) = -0.0128 eV (apenas 12.8 meV por debajo del centro).

Problema 2: En silicio tipo p dopado con boro a N_A = 5 × 10¹⁶ cm⁻³ a 300 K, calcule la concentración minoritaria de electrones n_p y la conductividad eléctrica sigma sabiendo que la movilidad de huecos es mu_p = 450 cm²/(V·s) y q = 1.602 × 10⁻¹⁹ C.
Paso 1: Por la ley de acción de masas: n_p = n_i² / p_p ≈ n_i² / N_A = (1.05 × 10¹⁰)² / (5 × 10¹⁶) = 1.1025 × 10²⁰ / (5 × 10¹⁶) = 2,205 cm⁻³.
Paso 2: Conductividad sigma ≈ q p mu_p = (1.602 × 10⁻¹⁹ C)(5 × 10¹⁶ cm⁻³)(450 cm²/(V·s)) = 3.6045 (Omega·cm)⁻¹ = 360.5 S/m.""",
        "bloque_sugerido": "Resolución Teórica 40 min • Estructuras cristalinas cúbicas y dopaje en silicio grado solar"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Termodinámica Química: Entropía, Energía Libre de Gibbs y Criterio de Espontaneidad",
        "objetivo": "Calcular la variación de energía libre de Gibbs de reacciones de reformado y combustión para determinar la espontaneidad y temperatura de inversión.",
        "concepto_clave_latex": r"\Delta G^\circ = \Delta H^\circ - T \Delta S^\circ \quad ; \quad \Delta G^\circ = -R T \ln K_p \quad ; \quad T_{\text{inv}} = \frac{\Delta H^\circ}{\Delta S^\circ} \quad [\text{K}]",
        "ejemplo": """Problema 1: Considere la reacción de reformado con vapor del metano: CH_4(g) + H_2O(g) -> CO(g) + 3 H_2(g). A 298.15 K se tienen los datos termodinámicos: Delta H° = +206.1 kJ/mol y Delta S° = +214.7 J/(mol·K). Calcule Delta G° a 298 K, determine si la reacción es espontánea a temperatura ambiente y halle la temperatura mínima a partir de la cual se vuelve termodinámicamente espontánea.
Paso 1: Delta G°(298 K) = Delta H° - T Delta S° = 206,100 J/mol - (298.15 K)(214.7 J/(mol·K)) = 206,100 - 64,013 = +142,087 J/mol = +142.09 kJ/mol.
Paso 2: Como Delta G° > 0, la reacción no es espontánea a 25°C; es fuertemente endotérmica.
Paso 3: Temperatura de inversión T_inv = Delta H° / Delta S° = 206,100 J/mol / 214.7 J/(mol·K) = 959.94 K (686.8 °C).
Paso 4: Por encima de 687 °C, el término entrópico -T Delta S° supera la entalpía y Delta G° se torna negativo, impulsando la producción de H_2.

Problema 2: A T = 1073.15 K (800 °C), calcule el valor de Delta G° y la constante de equilibrio K_p (R = 8.314 J/(mol·K)).
Paso 1: Delta G°(1073 K) ≈ 206,100 - (1073.15)(214.7) = 206,100 - 230,405 = -24,305 J/mol = -24.31 kJ/mol.
Paso 2: ln K_p = -Delta G° / (R T) = -(-24,305) / [(8.314)(1073.15)] = 24,305 / 8922.2 = 2.7241.
Paso 3: K_p = e^(2.7241) = 15.24 atm².""",
        "bloque_sugerido": "Cálculo Termodinámico 35 min • Balances de Gibbs en reacciones de transición energética"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Potencial Químico, Fugacidad y Actividad en Mezclas Reales de Gases y Electrolitos",
        "objetivo": "Determinar coeficientes de fugacidad en gases a alta presión y coeficientes de actividad iónica en electrolitos de baterías.",
        "concepto_clave_latex": r"\mu_i = \mu_i^\circ + R T \ln\left(\frac{f_i}{P^\circ}\right) = \mu_i^\circ + R T \ln(a_i) \quad ; \quad \ln\left(\frac{f}{P}\right) = \int_0^P \frac{Z - 1}{P'} \, dP'",
        "ejemplo": """Problema 1: Se almacena hidrógeno gaseoso H_2 en un tanque de repostaje a P = 350 bar (35.0 MPa) y T = 300 K. A esta presión, el factor de compresibilidad experimental del H_2 es Z = 1.21. Asumiendo una variación lineal Z(P') = 1 + b P' con b = 0.21 / 350 bar = 6.0 × 10⁻⁴ bar⁻¹, calcule el coeficiente de fugacidad phi = f / P y la fugacidad efectiva f.
Paso 1: ln(phi) = ∫_0^P [(Z - 1) / P'] dP' = ∫_0^P b dP' = b P = (6.0 × 10⁻⁴ bar⁻¹)(350 bar) = 0.210.
Paso 2: phi = e^(0.210) = 1.2337.
Paso 3: Fugacidad efectiva: f = phi × P = 1.2337 × 350 bar = 431.8 bar.
Paso 4: El potencial químico del H_2 a 350 bar equivale al de un gas ideal presurizado a 432 bar debido a la repulsión molecular de corto alcance.

Problema 2: En una disolución acuosa 0.05 mol/kg de sulfato de zinc ZnSO_4 (electrolito 2:2) a 25 °C, calcule la fuerza iónica I y el coeficiente medio de actividad gamma_± según la ley limitante de Debye-Hückel (A = 0.509 kg^(1/2)/mol^(1/2)).
Paso 1: I = (1/2) sum m_i z_i² = (1/2) [(0.05)(+2)² + (0.05)(-2)²] = (1/2) [0.20 + 0.20] = 0.20 mol/kg.
Paso 2: log_10(gamma_±) = -A |z_+ z_-| √I = -(0.509)(|(+2)(-2)|) √(0.20) = -(0.509)(4)(0.4472) = -0.9105.
Paso 3: gamma_± = 10^(-0.9105) = 0.1229. Las interacciones electrostáticas reducen la actividad química efectiva a un 12.3% de la concentración nominal.""",
        "bloque_sugerido": "Resolución Analítica 35 min • Modelación de fugacidad en almacenamiento de H2 a 700 bar"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Equilibrio de Fases: Ecuación de Clapeyron, Clausius-Clapeyron y Curvas P-T-x-y",
        "objetivo": "Modelar la presión de vapor de fluidos refrigerantes y caloportadores en función de la temperatura en ciclos de Rankine orgánicos (ORC).",
        "concepto_clave_latex": r"\frac{dP}{dT} = \frac{\Delta H_{\text{vap}}}{T \Delta V} \quad ; \quad \ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) \quad [\text{Pa}]",
        "ejemplo": """Problema 1: El fluido de trabajo R-134a (1,1,1,2-tetrafluoroetano) empleado en ciclos ORC y bombas de calor geotérmicas posee un calor latente de vaporización Delta H_vap = 217.1 kJ/kg (masa molar M = 102.03 g/mol => Delta H_vap = 22.15 kJ/mol) y ebulle a P_1 = 1.013 bar a T_1 = -26.3 °C (246.85 K). Calcule la presión de vapor saturado P_2 en el evaporador a T_2 = 40 °C (313.15 K).
Paso 1: Constante R = 8.314 J/(mol·K); Delta H_vap = 22,150 J/mol.
Paso 2: Diferencia inversa: (1/T_2 - 1/T_1) = (1/313.15 - 1/246.85) = 0.0031934 - 0.0040510 = -0.0008576 K⁻¹.
Paso 3: ln(P_2 / P_1) = -(22,150 / 8.314) × (-0.0008576) = -2664.18 × (-0.0008576) = +2.2848.
Paso 4: P_2 / P_1 = e^(2.2848) = 9.824.
Paso 5: Presión saturada: P_2 = 1.013 bar × 9.824 = 9.95 bar (0.995 MPa).

Problema 2: Deduzca la pendiente dP/dT para el agua pura en su punto de ebullición normal (T = 373.15 K, Delta H_vap = 40.66 kJ/mol, considerando volumen molar del vapor V_m,g ≈ R T / P = 0.0306 m³/mol >> V_m,liq).
Paso 1: dP/dT = Delta H_vap / (T V_m,g) = 40,660 J/mol / [(373.15 K)(0.0306 m³/mol)] = 40,660 / 11.418 = 3,561 Pa/K = 3.56 kPa/K.
Paso 2: Por cada 1 °C de aumento en la temperatura de saturación, la presión de la caldera debe incrementarse en 3.56 kPa.""",
        "bloque_sugerido": "Simulación Termodinámica 30 min • Construcción de diagramas P-xy en mezclas zeotrópicas de fluidos ORC"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Cinética de Reacciones Heterogéneas e Isotermas de Adsorción en Catálisis",
        "objetivo": "Modelar la adsorción física y química de gases reactivos en catalizadores metálicos aplicando las isotermas de Langmuir y Freundlich.",
        "concepto_clave_latex": r"\theta = \frac{K_{\text{ads}} P}{1 + K_{\text{ads}} P} \quad ; \quad r = k \theta_A \theta_B = \frac{k K_A K_B P_A P_B}{(1 + K_A P_A + K_B P_B)^2} \quad [\text{mol}/(\text{s}\cdot\text{g}_{\text{cat}})]",
        "ejemplo": """Problema 1: Se estudia la adsorción de monóxido de carbono CO sobre un catalizador de níquel soportado a 200 °C con constante de adsorción K_ads = 0.040 bar⁻¹. Calcule la fracción de superficie cubierta theta a presiones parciales de P = 5 bar, P = 25 bar y P = 100 bar.
Paso 1: Para P = 5 bar: theta = (0.040 × 5) / (1 + 0.040 × 5) = 0.20 / (1 + 0.20) = 0.20 / 1.20 = 0.1667 (16.7%).
Paso 2: Para P = 25 bar: theta = (0.040 × 25) / (1 + 0.040 × 25) = 1.00 / (1 + 1.00) = 0.5000 (50.0%).
Paso 3: Para P = 100 bar: theta = (0.040 × 100) / (1 + 0.040 × 100) = 4.00 / (1 + 4.00) = 4.00 / 5.00 = 0.8000 (80.0%).
Paso 4: A presiones muy elevadas (K P >> 1), la superficie se satura asintóticamente hacia theta -> 1 (orden cero respecto al reactivo).

Problema 2: En el mecanismo de Langmuir-Hinshelwood para la reacción bimolecular A + B -> C, ¿a qué relación de presiones P_A / P_B se maximiza la velocidad de reacción si K_A = K_B?
Paso 1: r es proporcional a theta_A theta_B = (K P_A)(K P_B) / [1 + K(P_A + P_B)]².
Paso 2: Para una presión total dada P_tot = P_A + P_B, el numerador se maximiza cuando P_A = P_B = P_tot / 2.
Paso 3: La tasa catalítica óptima exige presiones parciales equimolares de ambos reactivos sobre la superficie activa.""",
        "bloque_sugerido": "Ajuste Cinético 30 min • Linealización de Langmuir y cálculo de capacidad de monocapa V_m"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Catálisis Heterogénea en Reactores de Reformado y Gasificación de Biomasa",
        "objetivo": "Evaluar la desactivación catalítica por deposición de carbón (coking) y envenenamiento por azufre en reactores de gas de síntesis.",
        "concepto_clave_latex": r"r_{\text{d}} = -\frac{da}{dt} = k_d a^d \quad ; \quad a(t) = \frac{r(t)}{r_0} = \exp(-k_d t) \quad ; \quad \text{Coking: } 2\text{CO} \rightleftharpoons \text{C}_{(s)} + \text{CO}_2",
        "ejemplo": """Problema 1: Un catalizador comercial de Ni/Al_2O_3 empleado en reformado de metano se desactiva por coquizado siguiendo una cinética de desactivación de primer orden da/dt = -k_d a con k_d = 0.0025 h⁻¹. Calcule el factor de actividad relativa a(t) a las t = 200 horas de operación continua y halle la vida media del catalizador t_{1/2}.
Paso 1: a(t) = exp(-k_d t) = exp(-0.0025 × 200) = exp(-0.50) = 0.6065 (actividad residual del 60.65%).
Paso 2: Vida media: a(t_{1/2}) = 0.50 => -k_d t_{1/2} = ln(0.50) = -0.6931.
Paso 3: t_{1/2} = 0.6931 / 0.0025 = 277.26 horas (11.55 días).

Problema 2: Para inhibir la deposición de carbono por la reacción de Boudouard (2 CO <=> C + CO_2 con Delta H° = -172 kJ/mol), ¿conviene operar el reformador a alta o baja temperatura, y con alta o baja relación Vapor/Carbono (S/C)?
Paso 1: Por el Principio de Le Chatelier, al ser una reacción exotérmica hacia el carbono sólido, operar a alta temperatura (T > 800 °C) desplaza el equilibrio hacia la izquierda (destrucción de coque).
Paso 2: Incrementar la relación vapor/carbono (S/C >= 3.0) promueve la gasificación del carbono depositado mediante C + H_2O -> CO + H_2, blindando el catalizador.""",
        "bloque_sugerido": "Diseño de Reactores 35 min • Modelación de perfiles de actividad catalítica en lecho fijo"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Celdas de Combustible (PEMFC y SOFC): Termodinámica Electroquímica y Rendimiento",
        "objetivo": "Calcular la tensión reversible en circuito abierto (OCV), la eficiencia termodinámica teórica y el calor generado en celdas de combustible de hidrógeno.",
        "concepto_clave_latex": r"E_{\text{rev}} = -\frac{\Delta G^\circ}{n F} \quad ; \quad \eta_{\text{termo}} = \frac{\Delta G^\circ}{\Delta H^\circ} \quad ; \quad \dot{Q} = I\left(\frac{-\Delta H^\circ}{n F} - V_{\text{celda}}\right) \quad [\text{W}]",
        "ejemplo": """Problema 1: En una celda de combustible de membrana de intercambio protónico (PEMFC) que opera con hidrógeno y oxígeno a 25 °C (298.15 K) y 1 atm con producto agua líquida: H_2 + 1/2 O_2 -> H_2O(l). Se tiene Delta H° = -285.83 kJ/mol y Delta G° = -237.13 kJ/mol (con n = 2 electrones transferidos, F = 96,485 C/mol). Calcule el potencial reversible E_rev, el límite de eficiencia termodinámica eta_termo y el voltaje termoneutro E_tn.
Paso 1: Potencial reversible OCV: E_rev = -(-237,130 J/mol) / [2 × 96,485 C/mol] = 237,130 / 192,970 = 1.2288 V ≈ 1.23 V.
Paso 2: Límite termodinámico: eta_termo = Delta G° / Delta H° = -237.13 / -285.83 = 0.8296 (82.96% con base en PCS).
Paso 3: Voltaje termoneutro: E_tn = -Delta H° / (n F) = 285,830 / 192,970 = 1.4812 V.

Problema 2: Si un stack de 60 celdas PEMFC suministra una corriente I = 80 A operando a un voltaje real por celda V_celda = 0.70 V, calcule la potencia eléctrica neta P_elec y la tasa de calor residual dot{Q} disipada por el sistema de refrigeración.
Paso 1: Potencia eléctrica: P_elec = N_celdas × V_celda × I = 60 × 0.70 V × 80 A = 3,360 W = 3.36 kW.
Paso 2: Calor por celda: q_celda = I × (E_tn - V_celda) = 80 A × (1.4812 V - 0.70 V) = 80 × 0.7812 = 62.50 W.
Paso 3: Calor total del stack: dot{Q} = 60 × 62.50 W = 3,750 W = 3.75 kW (se genera más calor que electricidad útil).""",
        "bloque_sugerido": "Balance Energético 35 min • Modelación de curvas de polarización I-V en celdas de combustible"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Cinética Electroquímica: Butler-Volmer y Sobrepotenciales de Activación y Difusión",
        "objetivo": "Cuantificar las pérdidas de potencial por polarización de activación, óhmica y concentración en celdas electroquímicas.",
        "concepto_clave_latex": r"j = j_0 \left[\exp\left(\frac{\alpha_a F \eta_{\text{act}}}{R T}\right) - \exp\left(-\frac{\alpha_c F \eta_{\text{act}}}{R T}\right)\right] \quad ; \quad \eta_{\text{conc}} = \frac{R T}{n F}\ln\left(1 - \frac{j}{j_L}\right)",
        "ejemplo": """Problema 1: Para la reacción de desprendimiento de oxígeno (OER) en el ánodo de un electrolizador, la densidad de corriente de intercambio es j_0 = 1.0 × 10⁻⁴ A/cm² a T = 353 K (80 °C) con coeficiente de transferencia de carga anódico alpha_a = 0.50 (n = 1 para el paso determinante, F = 96,485 C/mol, R = 8.314 J/(mol·K)). Calcule el sobrepotencial de activación eta_act necesario para sostener una densidad de corriente de operación j = 0.50 A/cm² mediante la aproximación de Tafel para altos sobrepotenciales.
Paso 1: Aproximación de Tafel: j ≈ j_0 exp(alpha_a F eta_act / (R T)).
Paso 2: Despeje: eta_act = (R T / (alpha_a F)) ln(j / j_0).
Paso 3: Factor térmico: (R T / (alpha_a F)) = [(8.314)(353)] / [(0.50)(96,485)] = 2934.8 / 48,242.5 = 0.06083 V.
Paso 4: Cociente de corrientes: j / j_0 = 0.50 / (1.0 × 10⁻⁴) = 5,000; ln(5000) = 8.5172.
Paso 5: eta_act = 0.06083 V × 8.5172 = 0.5181 V (518 mV de sobrepotencial anódico).

Problema 2: Si la corriente límite de difusión es j_L = 1.8 A/cm², calcule la caída de potencial por polarización de concentración eta_conc a j = 1.5 A/cm² para n = 2 electrones a T = 353 K.
Paso 1: eta_conc = (R T / (n F)) ln(1 - j / j_L) = [(8.314)(353) / (2 × 96485)] ln(1 - 1.5 / 1.8) = (2934.8 / 192970) ln(0.1667).
Paso 2: eta_conc = 0.01521 V × (-1.7918) = -0.0272 V (-27.2 mV de pérdida por difusión).""",
        "bloque_sugerido": "Taller Electroquímico 35 min • Pendientes de Tafel y ajuste de parámetros j_0 en electrolizadores"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Baterías de Ión-Litio (LFP y NMC): Intercalación, Interfase SEI y Degradación",
        "objetivo": "Explicar los mecanismos electroquímicos de intercalación de litio, crecimiento de la capa de interfase de electrolito sólido (SEI) y desvanecimiento de capacidad.",
        "concepto_clave_latex": r"\text{Cátodo: } \text{LiCoO}_2 \rightleftharpoons \text{Li}_{1-x}\text{CoO}_2 + x\text{Li}^+ + x e^- \quad ; \quad \text{Ánodo: } 6\text{C} + x\text{Li}^+ + x e^- \rightleftharpoons \text{Li}_x\text{C}_6 \quad ; \quad Q_{\text{loss}} = k_{\text{SEI}} \sqrt{t}",
        "ejemplo": """Problema 1: Una celda de fosfato de hierro y litio (LiFePO_4 o LFP) tiene una capacidad nominal de 100 Ah a una tensión nominal de 3.2 V (320 Wh). La degradación por crecimiento parabólico de la interfase pasivante SEI consume capacidad según Q_loss(t) = 0.35 √t [%], donde t es el tiempo en días a 25 °C. Calcule la capacidad residual y la energía útil remanente tras 4 años de operación en reposo (t = 1,460 días).
Paso 1: Raíz del tiempo: √1460 = 38.21 días^(1/2).
Paso 2: Pérdida porcentual: Q_loss = 0.35 × 38.21 = 13.37%.
Paso 3: Capacidad residual: Q_res = 100 Ah × (1 - 0.1337) = 86.63 Ah.
Paso 4: Energía remanente: E = 86.63 Ah × 3.2 V = 277.2 Wh (el estado de salud SoH = 86.6%).

Problema 2: En la celda NMC (LiNi_{0.6}Mn_{0.2}Co_{0.2}O_2) con capacidad específica teórica de 278 mAh/g, se extrae de forma reversible una fracción molar x = 0.70 de iones Li^+ sin provocar colapso de la red laminar. Calcule la capacidad específica práctica disponible [mAh/g].
Paso 1: q_prac = 278 mAh/g × 0.70 = 194.6 mAh/g.
Paso 2: Extraer x > 0.75 induce transiciones de fase irreversibles, liberación de oxígeno reticular y riesgo de fuga térmica (thermal runaway).""",
        "bloque_sugerido": "Modelación de Almacenamiento 35 min • Modelos electroquímicos P2D (Pseudo-2-Dimensional) de baterías"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Baterías de Flujo Redox (Vanadio): Termodinámica y Eficiencia Coulombimétrica",
        "objetivo": "Analizar las reacciones de transferencia electrónica de cuatro estados de oxidación del vanadio, determinando densidades energéticas y eficiencias de ciclo.",
        "concepto_clave_latex": r"\text{Ánodo: } \text{V}^{2+} \rightleftharpoons \text{V}^{3+} + e^- \quad (E^\circ = -0.26\text{ V}) \quad ; \quad \text{Cátodo: } \text{VO}_2^+ + 2\text{H}^+ + e^- \rightleftharpoons \text{VO}^{2+} + \text{H}_2\text{O} \quad (E^\circ = +1.00\text{ V}) \quad ; \quad E_{\text{celda}}^\circ = 1.26\text{ V}",
        "ejemplo": """Problema 1: En una batería de flujo redox de vanadio (VRFB), la concentración de iones de vanadio en cada tanque electrolítico de V = 5,000 litros (5 m³) es C = 2.0 mol/L (2,000 mol/m³). Sabiendo que n = 1 electrón por mol de vanadio, F = 96,485 C/mol y la tensión media de descarga es V_desc = 1.30 V, calcule la capacidad de carga total en amperios-hora [Ah] y la energía eléctrica almacenable [kWh].
Paso 1: Moles totales de vanadio activo: M = C × V = 2.0 mol/L × 5,000 L = 10,000 moles.
Paso 2: Carga teórica Q = M × n × F = 10,000 mol × 96,485 C/mol = 964,850,000 Coulombs.
Paso 3: Conversión a amperios-hora: Q_Ah = 964,850,000 C / 3,600 s/h = 268,014 Ah = 268 kAh.
Paso 4: Energía teórica: E = Q_Ah × V_desc = 268,014 Ah × 1.30 V = 348,418 Wh = 348.4 kWh.
Paso 5: La densidad energética volumétrica es 348.4 kWh / 10 m³ (ambos tanques) = 34.8 kWh/m³.

Problema 2: Si durante un ciclo completo de carga-descarga se inyectan Q_carga = 280 kAh a 1.45 V y se extraen Q_desc = 266 kAh a 1.28 V, calcule la eficiencia coulombimétrica eta_C, la eficiencia de voltaje eta_V y la eficiencia global de ida y vuelta (round-trip) eta_RT.
Paso 1: Eficiencia coulombimétrica: eta_C = Q_desc / Q_carga = 266 / 280 = 0.9500 (95.0%).
Paso 2: Eficiencia de voltaje: eta_V = V_desc / V_carga = 1.28 / 1.45 = 0.8828 (88.3%).
Paso 3: Eficiencia round-trip: eta_RT = eta_C × eta_V = 0.9500 × 0.8828 = 0.8386 (83.86%).""",
        "bloque_sugerido": "Dimensionamiento de Sistemas 35 min • Escalado independiente de potencia (stack) y energía (tanques) en VRFB"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Mecanismos de Corrosión Electroquímica: Diagramas de Pourbaix y Corrosión Galvánica",
        "objetivo": "Interpretar diagramas potencial-pH (Pourbaix) para identificar zonas de inmunidad, corrosión y pasivación en aceros y aleaciones estructurales.",
        "concepto_clave_latex": r"E = E^\circ - \frac{0.0592}{n} \log Q \quad ; \quad \text{Línea H}_2/\text{H}^+: E = 0.000 - 0.0592\,\text{pH} \quad ; \quad \text{Línea O}_2/\text{H}_2\text{O}: E = 1.229 - 0.0592\,\text{pH}",
        "ejemplo": """Problema 1: Considere el equilibrio electroquímico Fe²⁺ + 2 e⁻ <=> Fe(s) con E° = -0.440 V frente a SHE a 25 °C. Calcule el potencial de equilibrio E cuando la concentración de iones ferrosos en agua desmineralizada de una caldera desciende a [Fe²⁺] = 1.0 × 10⁻⁶ mol/L (criterio estándar de inmunidad termodinámica).
Paso 1: Ecuación de Nernst: E = E° - (0.0592 / n) log(1 / [Fe²⁺]) = E° + (0.0592 / 2) log[Fe²⁺].
Paso 2: E = -0.440 + 0.0296 log(10⁻⁶) = -0.440 + 0.0296(-6) = -0.440 - 0.1776 = -0.6176 V vs SHE.
Paso 3: Para que el acero esté completamente inmune a la corrosión acuosa, su potencial electroquímico debe mantenerse por debajo de -0.618 V vs SHE.

Problema 2: En una instalación marina de turbinas eólicas offshore se conectan directamente pernos de acero al carbono (E_corr ≈ -0.60 V) con una placa de bronce marino (E_corr ≈ -0.20 V). Si la relación de áreas cátodo/ánodo es A_c / A_a = 20, explique el riesgo galvánico.
Paso 1: El acero actúa como ánodo galvánico (más negativo) y el bronce como cátodo noble.
Paso 2: La densidad de corriente anódica es j_a = j_c (A_c / A_a). Al ser el cátodo 20 veces más grande que el ánodo, los pernos de acero sufrirán una tasa de disolución metálica acelerada 20 veces, provocando falla catastrófica por cizallamiento en pocos meses si no se aísla dieléctricamente.""",
        "bloque_sugerido": "Evaluación de Integridad 35 min • Lectura de diagramas Pourbaix Fe-H2O y Cu-H2O en ambientes salinos"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Protección Catódica por Corriente Impresa (ICCP) y Ánodos Galvánicos de Sacrificio",
        "objetivo": "Diseñar sistemas de protección catódica para tuberías de gasoductos e infraestructura marina calculando masa de ánodo y corriente requerida.",
        "concepto_clave_latex": r"I_{\text{prot}} = A_{\text{ext}} \cdot j_{\text{req}} \cdot (1 - \eta_{\text{rec}}) \quad ; \quad M_{\text{ánodo}} = \frac{I_{\text{prot}} \cdot t_{\text{diseño}} \cdot 8760}{C_{\text{cap}} \cdot u} \quad [\text{kg}]",
        "ejemplo": """Problema 1: Un gasoducto de acero enterrado de diámetro D = 0.50 m y longitud L = 20 km (área superficial exterior A = pi D L = pi × 0.50 × 20,000 = 31,416 m²) cuenta con un recubrimiento dieléctrico de polietileno con eficiencia del 98% (fracción descubierta por poros = 2%). La densidad de corriente requerida para polarizar el acero desnudo es j_req = 50 mA/m² (0.050 A/m²). Calcule la corriente total de protección catódica I_prot requerida.
Paso 1: Área neta expuesta: A_neta = A × (1 - 0.98) = 31,416 m² × 0.02 = 628.32 m².
Paso 2: Corriente de diseño: I_prot = A_neta × j_req = 628.32 m² × 0.050 A/m² = 31.42 A.
Paso 3: Un único rectificador de corriente impresa (ICCP) de 40 A - 50 V es capaz de proteger los 20 km de tubería.

Problema 2: Para una plataforma eólica offshore con requerimiento de corriente media I_prot = 15 A durante una vida útil de diseño t_diseño = 25 años, dimensione la masa total de ánodos de sacrificio de aleación de Aluminio-Indio-Zinc (capacidad práctica C_cap = 2,600 A·h/kg, factor de utilización u = 0.85).
Paso 1: Horas de servicio: 25 años × 8,760 h/año = 219,000 horas.
Paso 2: Carga requerida: Q = 15 A × 219,000 h = 3,285,000 A·h.
Paso 3: Capacidad efectiva por kg: C_eff = C_cap × u = 2,600 × 0.85 = 2,210 A·h/kg.
Paso 4: Masa requerida de ánodos: M = 3,285,000 / 2,210 = 1,486.4 kg ≈ 1.49 toneladas de ánodos de Al-Zn-In.""",
        "bloque_sugerido": "Diseño de Ingeniería 35 min • Cálculo de lechos de ánodos profundos y perfiles de potencial ON/OFF"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Química de la Combustión Avanzada: Mecanismos Zeldovich de Formación de NOx y SOx",
        "objetivo": "Modelar la cinética de formación de óxidos de nitrógeno térmicos y reducción catalítica selectiva (SCR) en plantas termoeléctricas.",
        "concepto_clave_latex": r"\frac{d[\text{NO}]}{dt} = 2 k_1 [\text{O}][\text{N}_2] \quad ; \quad k_1 = 1.8 \times 10^{14} \exp\left(-\frac{318\,\text{kJ/mol}}{R T}\right) \quad ; \quad 4\text{NO} + 4\text{NH}_3 + \text{O}_2 \xrightarrow{\text{V}_2\text{O}_5} 4\text{N}_2 + 6\text{H}_2\text{O}",
        "ejemplo": """Problema 1: En la zona de llama de una turbina de gas a gas natural operando a T_1 = 1,800 K (1,527 °C), calcule la constante de velocidad de la primera reacción de Zeldovich k_1 (O + N_2 -> NO + N). Compárela con la constante a T_2 = 2,100 K (1,827 °C) para justificar por qué la combustión premezclada pobre (dry low NOx) reduce drásticamente las emisiones. (R = 8.314 J/(mol·K)).
Paso 1: A T_1 = 1,800 K: R T_1 = (8.314)(1800) = 14,965 J/mol.
Exponente: -318,000 / 14,965 = -21.249.
k_1(1800 K) = 1.8 × 10¹⁴ × exp(-21.249) = 1.8 × 10¹⁴ × 5.91 × 10⁻¹⁰ = 106,380 cm³/(mol·s).
Paso 2: A T_2 = 2,100 K: R T_2 = (8.314)(2100) = 17,459 J/mol.
Exponente: -318,000 / 17,459 = -18.214.
k_1(2100 K) = 1.8 × 10¹⁴ × exp(-18.214) = 1.8 × 10¹⁴ × 1.23 × 10⁻⁸ = 2,214,000 cm³/(mol·s).
Paso 3: Cociente k_1(2100 K) / k_1(1800 K) = 2,214,000 / 106,380 = 20.81.
Paso 4: Un incremento de solo 300 K multiplica la tasa cinética de producción de NO por 21 veces, confirmando que mitigar picos de temperatura local es el método primario de control ambiental.

Problema 2: Una caldera emite 200 kg/h de NO. Calcule el consumo estequiométrico horario de amoníaco anhidro NH_3 (M = 17.03 g/mol) para reducir el 90% del NO a nitrógeno molecular en un reactor SCR.
Paso 1: NO a tratar = 200 kg/h × 0.90 = 180 kg/h = 180,000 g/h.
Paso 2: Moles de NO: 180,000 g / 30.01 g/mol = 5,998 mol/h.
Paso 3: Relación estequiométrica NH_3 / NO = 1:1.
Paso 4: Masa de NH_3 = 5,998 mol/h × 17.03 g/mol = 102,146 g/h = 102.15 kg/h.""",
        "bloque_sugerido": "Control de Emisiones 35 min • Balances estequiométricos de sistemas DeNOx y DeSOx (FGD)"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Captura Química de Carbono (CCS): Absorción con Aminas y Regeneración Térmica",
        "objetivo": "Cuantificar el balance de masa y la penalización energética del solvente monoetanolamina (MEA) en la captura post-combustión de CO2.",
        "concepto_clave_latex": r"2\text{R-NH}_2 + \text{CO}_2 \rightleftharpoons \text{R-NHCOO}^- + \text{R-NH}_3^+ \quad ; \quad q_{\text{reb}} = q_{\text{reac}} + q_{\text{sens}} + q_{\text{lat}} \approx 3.2\text{ a }4.0 \quad [\text{MJ}/\text{kg}_{\text{CO}_2}]",
        "ejemplo": """Problema 1: Los gases de escape de una central termoeléctrica contienen un flujo de 100 toneladas/hora de CO_2 (27.78 kg/s). Se implementa una planta de captura con MEA al 30% en peso con una eficiencia de absorción del 90%. Si la energía térmica de regeneración en el hervidor del despojador (stripper reboiler) es q_reb = 3.6 MJ por kg de CO_2 capturado, calcule la potencia térmica requerida dot{Q}_reb [MW_th] y la pérdida equivalente de potencia eléctrica (factor Carnot/eléctrico alpha_penal ≈ 0.25).
Paso 1: Flujo de CO_2 capturado: dot{m}_{CO2} = 100 t/h × 0.90 = 90 t/h = 90,000 kg/h = 25.0 kg/s.
Paso 2: Calor de regeneración: dot{Q}_reb = 25.0 kg/s × 3.6 MJ/kg = 90.0 MJ/s = 90.0 MW_th.
Paso 3: Penalización en la potencia eléctrica de la turbina: P_loss ≈ 90.0 MW_th × 0.25 = 22.5 MW_e.
Paso 4: La central debe desviar 22.5 MW de su generación neta para solventar la desorción de amina.

Problema 2: En la reacción de formación de carbamato con MEA (capacidad máxima estequiométrica de 0.5 mol CO_2 por mol de MEA), calcule la masa mínima de MEA pura (M = 61.08 g/mol) necesaria para ligar 1.0 kg de CO_2 (M = 44.01 g/mol).
Paso 1: Moles de CO_2 en 1 kg: 1,000 g / 44.01 g/mol = 22.72 mol.
Paso 2: Moles de MEA requeridos = 2 × 22.72 mol = 45.44 mol.
Paso 3: Masa de MEA = 45.44 mol × 61.08 g/mol = 2,775.5 g = 2.78 kg de MEA por kg de CO_2.""",
        "bloque_sugerido": "Evaluación Termoquímica 35 min • Modelación de torres de absorción empaquetadas para descarbonización"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Termoquímica de la Gasificación de Biomasa: Gas de Síntesis y Reacción WGS",
        "objetivo": "Calcular la composición de equilibrio del gas de síntesis (H2, CO, CO2, CH4) y evaluar la reacción de desplazamiento de agua-gas (Water-Gas Shift).",
        "concepto_clave_latex": r"\text{CO} + \text{H}_2\text{O} \rightleftharpoons \text{CO}_2 + \text{H}_2 \quad (\Delta H^\circ_{298} = -41.2\text{ kJ/mol}) \quad ; \quad K_p(T) = \exp\left(\frac{4577.8}{T} - 4.33\right)",
        "ejemplo": """Problema 1: En un reactor de desplazamiento de agua-gas (WGS) que opera a T = 600 K (327 °C), se alimenta una mezcla de gas de síntesis con presiones iniciales: P_CO = 10 bar, P_H2O = 20 bar, P_CO2 = 2 bar, P_H2 = 5 bar. Calcule la constante de equilibrio K_p a 600 K y la presión parcial de equilibrio de H_2 si el avance de reacción es xi bar.
Paso 1: K_p(600 K) = exp(4577.8 / 600 - 4.33) = exp(7.6297 - 4.33) = exp(3.2997) = 27.10.
Paso 2: Expresión de equilibrio: K_p = [(P_CO2 + xi)(P_H2 + xi)] / [(P_CO - xi)(P_H2O - xi)].
27.10 = [(2 + xi)(5 + xi)] / [(10 - xi)(20 - xi)] = (10 + 7 xi + xi²) / (200 - 30 xi + xi²).
Paso 3: 27.10 (200 - 30 xi + xi²) = 10 + 7 xi + xi² => 5420 - 813 xi + 27.10 xi² = 10 + 7 xi + xi².
26.10 xi² - 820 xi + 5410 = 0 => xi² - 31.418 xi + 207.28 = 0.
Paso 4: xi = [31.418 - √(31.418² - 4 × 207.28)] / 2 = [31.418 - √(987.09 - 829.12)] / 2 = [31.418 - √157.97] / 2 = [31.418 - 12.569] / 2 = 18.849 / 2 = 9.424 bar.
Paso 5: Presión final de hidrógeno: P_{H2,eq} = 5 + 9.424 = 14.42 bar (se triplica la disponibilidad de H_2).

Problema 2: Dado que la reacción WGS es exotérmica (Delta H° = -41.2 kJ/mol), ¿por qué las plantas industriales emplean una etapa de alta temperatura (HT-WGS a 350-450 °C) seguida de una etapa de baja temperatura (LT-WGS a 200-250 °C)?
Paso 1: La etapa de alta temperatura proporciona rapidez cinética para convertir la mayor parte del CO.
Paso 2: La etapa de baja temperatura desplaza termodinámicamente el equilibrio hacia la derecha, reduciendo el CO residual a menos del 0.2% molar para no envenenar celdas de combustible.""",
        "bloque_sugerido": "Simulación Termoquímica 40 min • Balances de materia y energía en gasificadores de lecho fluidizado"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Producción de Hidrógeno Verde: Electrolizadores Alcalinos (AEL) y PEM",
        "objetivo": "Calcular consumos energéticos específicos [kWh/kg H2], eficiencias de Faraday y eficiencias térmicas en electrolizadores comerciales.",
        "concepto_clave_latex": r"\dot{m}_{\text{H}_2} = \eta_F \frac{I \cdot N_{\text{celdas}} \cdot M_{\text{H}_2}}{2 F} \quad ; \quad w_{\text{esp}} = \frac{V_{\text{celda}} \cdot 2 F}{\eta_F \cdot M_{\text{H}_2} \cdot 3600} \quad [\text{kWh}/\text{kg}_{\text{H}_2}]",
        "ejemplo": """Problema 1: Un electrolizador PEM de 1 MW compuesto por N = 250 celdas opera a una corriente I = 2,000 A con un voltaje medio por celda V_celda = 1.95 V y eficiencia faradaica eta_F = 98.5%. Calcule la tasa de producción horaria de hidrógeno verde dot{m}_{H2} [kg/h] y el consumo específico de energía eléctrica w_esp [kWh/kg H_2]. (M_H2 = 2.016 g/mol = 0.002016 kg/mol, F = 96,485 C/mol).
Paso 1: Producción másica por segundo:
dot{m} = (0.985) × [2000 A × 250 × 0.002016 kg/mol] / [2 × 96,485 C/mol] = (0.985) × [1008] / 192,970 = 0.99288 / 192.97 = 0.005145 kg/s.
Paso 2: Producción horaria: 0.005145 kg/s × 3,600 s/h = 18.52 kg/h de H_2.
Paso 3: Potencia del stack: P = 250 × 1.95 V × 2,000 A = 975,000 W = 975 kW.
Paso 4: Consumo específico: w_esp = P / dot{m}_{hora} = 975 kW / 18.52 kg/h = 52.65 kWh/kg H_2.

Problema 2: Calcule la eficiencia del electrolizador respecto al Poder Calorífico Superior del H_2 (PCS = 141.8 MJ/kg = 39.39 kWh/kg) y respecto al Poder Calorífico Inferior (PCI = 120.0 MJ/kg = 33.33 kWh/kg).
Paso 1: eta_PCS = 39.39 kWh/kg / 52.65 kWh/kg = 0.7481 (74.81%).
Paso 2: eta_PCI = 33.33 kWh/kg / 52.65 kWh/kg = 0.6330 (63.30%).""",
        "bloque_sugerido": "Dimensionamiento Industrial 35 min • Curvas de polarización y acoplamiento directo solar PV - Electrolizador"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Portadores Químicos de Hidrógeno (LOHC) y Amoníaco Verde como Vector Energético",
        "objetivo": "Comparar densidades volumétricas de energía y balances termoquímicos de hidrogenación/deshidrogenación en LOHC y síntesis Haber-Bosch verde.",
        "concepto_clave_latex": r"\text{N}_2 + 3\text{H}_2 \xrightleftharpoons[\text{Fe/Ru}]{450^\circ\text{C},\,200\text{ bar}} 2\text{NH}_3 \quad (\Delta H^\circ = -92.2\text{ kJ/mol}) \quad ; \quad \rho_{\text{vol,H}_2} = \frac{m_{\text{H}_2,\text{lib}}}{V_{\text{portador}}} \quad [\text{kg H}_2/\text{m}^3]",
        "ejemplo": """Problema 1: Compare la densidad volumétrica de almacenamiento de hidrógeno entre: a) Gas comprimido a 700 bar (densidad rho ≈ 42 kg H_2/m³); b) Hidrógeno líquido a -253 °C (rho ≈ 71 kg H_2/m³); c) Amoníaco líquido NH_3 a 20 °C y 8.6 bar (densidad líquida rho_NH3 = 610 kg/m³, fracción másica de hidrógeno = 3 × 1.008 / 17.03 = 17.76% en peso).
Paso 1: Densidad volumétrica de H_2 en amoníaco líquido:
rho_{vol,NH3} = 610 kg NH_3/m³ × 0.1776 kg H_2/kg NH_3 = 108.3 kg H_2/m³.
Paso 2: Comparación relativa: El amoníaco líquido contiene 108.3 / 71 = 1.53 veces más hidrógeno por metro cúbico que el hidrógeno líquido puro criogénico, y 2.58 veces más que el gas a 700 bar, a presiones moderadas de distribución.

Problema 2: En un portador orgánico líquido de hidrógeno (LOHC) basado en dibenciltolueno (H0-DBT / H18-DBT), la deshidrogenación catalítica requiere un calor endotérmico de Delta H_des = 65.4 kJ/mol H_2. Calcule el calor requerido para liberar 1.0 kg de H_2 puro (496 moles de H_2).
Paso 1: Q_term = 496 mol × 65.4 kJ/mol = 32,438 kJ = 32.44 MJ.
Paso 2: En kWh: 32.44 MJ / 3.6 = 9.01 kWh_th por kg de H_2 liberado (equivale al 27% del PCI del hidrógeno desprendido).""",
        "bloque_sugerido": "Análisis Tecnológico 35 min • Logística marítima y reconversión de terminales de amoníaco verde"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Química de Biocombustibles: Transesterificación a Biodiésel y Fermentación a Bioetanol",
        "objetivo": "Formular estequiometrías de transesterificación de triglicéridos con metanol y balances de masa de fermentación anaerobia de glucosa.",
        "concepto_clave_latex": r"\text{Triglicérido} + 3\text{CH}_3\text{OH} \xrightarrow{\text{KOH}} 3\text{FAME (Biodiésel)} + \text{Glicerol} \quad ; \quad \text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{Levadura}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2",
        "ejemplo": """Problema 1: En una planta de biodiésel a partir de aceite de palma (trioleína C_57 H_104 O_6, masa molar M = 885.4 g/mol), se procesa 1.0 tonelada (1,000 kg) de aceite con metanol en exceso molar del 100% (relación metanol:aceite = 6:1; metanol M = 32.04 g/mol). Calcule el rendimiento teórico de oleato de metilo (FAME, C_19 H_36 O_2, M = 296.5 g/mol) y la masa de glicerol subproducto (C_3 H_8 O_3, M = 92.09 g/mol).
Paso 1: Moles de trioleína: 1,000,000 g / 885.4 g/mol = 1,129.4 mol.
Paso 2: Moles de biodiésel producidos = 3 × 1,129.4 mol = 3,388.2 mol.
Paso 3: Masa teórica de biodiésel = 3,388.2 mol × 296.5 g/mol = 1,004,600 g = 1,004.6 kg (rendimiento másico ligeramente superior a 100% por la incorporación del grupo metilo).
Paso 4: Moles de glicerol = 1,129.4 mol. Masa = 1,129.4 mol × 92.09 g/mol = 104,006 g = 104.0 kg de glicerol.

Problema 2: En la fermentación etanólica de 100 kg de glucosa pura con rendimiento real del 92% respecto al límite estequiométrico de Gay-Lussac (51.14% en peso de etanol), calcule la masa de bioetanol anhidro obtenida y el volumen de CO_2 emitido a 25 °C y 1 atm.
Paso 1: Etanol teórico = 100 kg × 0.5114 = 51.14 kg.
Paso 2: Etanol real = 51.14 kg × 0.92 = 47.05 kg de bioetanol.
Paso 3: Moles de CO_2 producidos = (100,000 g / 180.16 g/mol) × 2 × 0.92 = 555.06 × 1.84 = 1,021.3 mol.
Paso 4: Volumen de CO_2: V = n R T / P = (1021.3 mol)(0.08206 atm·L/(mol·K))(298.15 K) / 1.0 atm = 24,987 L = 24.99 m³.""",
        "bloque_sugerido": "Balances Industriales 35 min • Purificación, deshidratación molecular de etanol y glicerina técnica"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Degradación Fotoquímica y Química de Polímeros en Módulos Solares (EVA y Backsheet)",
        "objetivo": "Identificar los mecanismos de fotooxidación UV, hidrólisis y formación de ácido acético en el encapsulante EVA que degradan módulos fotovoltaicos.",
        "concepto_clave_latex": r"\text{EVA} + h\nu (\text{UV}) + \text{H}_2\text{O} \longrightarrow \text{CH}_3\text{COOH} (\text{Ácido acético}) + \text{Polímero insaturado (Polieno)} \quad ; \quad \text{Amarilleamiento (Yellowing)}",
        "ejemplo": """Problema 1: En un parque solar en La Guajira, la radiación UV y la humedad relativa inducen la desacetilación del etileno-vinil-acetato (EVA, copolímero con 33% de peso de acetato de vinilo, VA = C_4 H_6 O_2, M = 86.09 g/mol). Si una lámina de EVA de 2.0 kg por módulo solar pierde el 1.5% de sus grupos acetato por año como ácido acético libre atrapado (CH_3COOH, M = 60.05 g/mol), calcule los gramos de ácido acético generados anualmente por módulo y su efecto corrosivo en las cintas de interconexión (ribbons) de plata/cobre.
Paso 1: Masa de VA en la lámina: 2,000 g × 0.33 = 660 g de grupos acetato de vinilo.
Paso 2: Moles de VA: 660 g / 86.09 g/mol = 7.666 mol.
Paso 3: Moles degradados al 1.5% anual: 7.666 mol × 0.015 = 0.115 mol de ácido acético/año.
Paso 4: Masa de ácido acético generada: 0.115 mol × 60.05 g/mol = 6.91 g/año por módulo.
Paso 5: El ácido acético atrapado desciende el pH interno a valores fuertemente ácidos (pH < 4), disolviendo la capa pasivante de plomo/estaño de los ribbons y corroyendo las metalizaciones frontales de plata, lo que incrementa drásticamente la resistencia serie R_s y degrada el factor de forma (FF).

Problema 2: ¿Qué aditivos químicos se incorporan en formulaciones avanzadas de EVA o POE (Poliolefina Elastómero) para suprimir esta ruta de falla?
Paso 1: Estabilizadores de luz de amina impedida (HALS) que capturan radicales libres peroxilo.
Paso 2: Absorbentes UV (benzofenonas o triazoles) que disipan energía fotónica en calor inocuo.
Paso 3: Sustitución de EVA por POE, el cual carece de enlaces éster susceptibles de hidrólisis ácida.""",
        "bloque_sugerido": "Degradación de Materiales 30 min • Caracterización FTIR y espectroscopía de fluorescencia UV en módulos degradados"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Química del Agua en Ciclos Térmicos: Desmineralización, Desgasificación y Corrosión FAC",
        "objetivo": "Calcular dosificaciones de secuestrantes de oxígeno, aminas neutralizantes y control de sílice para mitigar la corrosión acelerada por flujo (FAC) en calderas.",
        "concepto_clave_latex": r"\text{N}_2\text{H}_4 + \text{O}_2 \longrightarrow \text{N}_2 + 2\text{H}_2\text{O} \quad ; \quad 2\text{Na}_2\text{SO}_3 + \text{O}_2 \longrightarrow 2\text{Na}_2\text{SO}_4 \quad ; \quad 3\text{Fe} + 4\text{H}_2\text{O} \xrightarrow{\text{Schikorr}} \text{Fe}_3\text{O}_4 + 4\text{H}_2",
        "ejemplo": """Problema 1: El agua de reposición de una caldera de vapor de alta presión (P = 80 bar) contiene una concentración de oxígeno disuelto residual tras desgasificación térmica de [O_2] = 15 microgramos/litro (15 ppb). El flujo de agua de alimentación es dot{V} = 120 m³/h (120,000 L/h). Se dosifica hidracina N_2H_4 (M = 32.05 g/mol) con un 20% de exceso estequiométrico para garantizar la reacción completa con O_2 (M = 32.00 g/mol). Calcule el consumo horario de hidracina pura [g/h].
Paso 1: Masa horaria de oxígeno disuelto: 120,000 L/h × 15 × 10⁻⁶ g/L = 1.80 g O_2/h.
Paso 2: Moles de O_2: 1.80 g / 32.00 g/mol = 0.05625 mol/h.
Paso 3: Relación estequiométrica N_2H_4 : O_2 = 1:1.
Moles de hidracina requeridos = 0.05625 mol/h × 1.20 (exceso) = 0.0675 mol/h.
Paso 4: Masa de hidracina: 0.0675 mol/h × 32.05 g/mol = 2.163 g/h.

Problema 2: En la reacción de Schikorr a temperaturas superiores a 200 °C: 3 Fe(OH)_2 -> Fe_3O_4 + 2 H_2O + H_2, ¿por qué es crítico mantener el pH del agua entre 9.2 y 9.6 mediante aminas volátiles (p. ej., ciclohexilamina)?
Paso 1: A pH neutro o ácido (pH < 8.5), la magnetita protectora Fe_3O_4 se disuelve como Fe²⁺.
Paso 2: A pH > 10.5, el ion ferroso forma complejos solubles de ferrito FeO_2²⁻ (ataque cáustico).
Paso 3: El intervalo 9.2 - 9.6 minimiza la solubilidad de la magnetita, creando una película pasivante compacta de pocos micrómetros que detiene la corrosión.""",
        "bloque_sugerido": "Química de Plantas Térmicas 35 min • Monitoreo de conductividad catiónica desgasificada y control de sílice"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Materiales Termoeléctricos y Piezoeléctricos: Efecto Seebeck y Coeficiente de Mérito ZT",
        "objetivo": "Calcular la figura de mérito adimensional ZT y el rendimiento térmico-eléctrico de generadores termoeléctricos (TEG) para recuperación de calor residual.",
        "concepto_clave_latex": r"ZT = \frac{S^2 \sigma}{\kappa} T \quad ; \quad \eta_{\text{TEG}} = \frac{T_h - T_c}{T_h} \frac{\sqrt{1 + Z\bar{T}} - 1}{\sqrt{1 + Z\bar{T}} + \frac{T_c}{T_h}} \quad ; \quad \kappa = \kappa_e + \kappa_{\text{ph}} \quad [\text{W}/(\text{m}\cdot\text{K})]",
        "ejemplo": """Problema 1: Un material termoeléctrico basado en telururo de bismuto Bi_2Te_3 opera a una temperatura media bar{T} = 350 K (77 °C). Sus propiedades de transporte medidas son: Coeficiente Seebeck S = 220 microV/K = 2.2 × 10⁻⁴ V/K, conductividad eléctrica sigma = 1.0 × 10⁵ S/m, y conductividad térmica total kappa = 1.40 W/(m·K). Calcule el factor de potencia (Power Factor, PF = S² sigma), la figura de mérito ZT y la eficiencia teórica máxima de conversión si opera entre T_h = 400 K y T_c = 300 K.
Paso 1: Factor de potencia:
PF = S² sigma = (2.2 × 10⁻⁴ V/K)² × (1.0 × 10⁵ S/m) = (4.84 × 10⁻⁸) × 10⁵ = 4.84 × 10⁻³ W/(m·K²) = 4.84 mW/(m·K²).
Paso 2: Figura de mérito ZT:
ZT = (PF / kappa) × bar{T} = (0.00484 / 1.40) × 350 = 0.003457 × 350 = 1.210.
Paso 3: Eficiencia de Carnot: eta_Carnot = (400 - 300) / 400 = 100 / 400 = 0.25 (25.0%).
Paso 4: Factor multiplicativo termoeléctrico:
M = √(1 + ZT) = √(1 + 1.21) = √2.21 = 1.4866.
eta_TEG = eta_Carnot × [(M - 1) / (M + T_c / T_h)] = 0.25 × [(1.4866 - 1) / (1.4866 + 300/400)] = 0.25 × [0.4866 / (1.4866 + 0.75)] = 0.25 × [0.4866 / 2.2366] = 0.25 × 0.2176 = 0.0544 (5.44%).

Problema 2: En el diseño molecular de termoeléctricos avanzados, ¿por qué se busca desacoplar la conductividad térmica electrónica kappa_e de la fonónica kappa_ph mediante nanoconfinamiento ("phonon glass, electron crystal")?
Paso 1: Porque según la ley de Wiedemann-Franz, kappa_e está indisolublemente ligada a sigma (kappa_e / sigma = L T).
Paso 2: Para maximizar ZT, la única vía física es dispersar los fonones en interfaces nanométricas (reduciendo drásticamente kappa_ph) sin degradar la movilidad electrónica de los portadores.""",
        "bloque_sugerido": "Cosecha de Energía 35 min • Dimensionamiento de módulos TEG acoplados a tubos de escape de motores diésel"
    }
]

if __name__ == '__main__':
    yaml_text = format_topics_yaml(topics_02031812)
    inject_topics_after('  - cuatrimestre: 3', yaml_text)
    print("02031812 Química Aplicada now has 30 topics!")
