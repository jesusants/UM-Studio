# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_9_to_20 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Termodinámica Básica y Ciclos de Potencia Térmica",
        "objetivo": "Calcular eficiencias térmicas de conversión en ciclos de potencia mediante la Primera y Segunda Ley de la Termodinámica.",
        "concepto_clave_latex": r"\eta_{\text{th}} = \frac{W_{\text{neto}}}{Q_{\text{in}}} = 1 - \frac{Q_{\text{out}}}{Q_{\text{in}}} \quad ; \quad \eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H}",
        "ejemplo": """CLASE MAGISTRAL: CONVERSIÓN TÉRMICA Y LÍMITES TERMODINÁMICOS
1. Primer y Segundo Principio de la Termodinámica:
La Primera Ley establece la conservación de la energía dE = dQ - dW. La Segunda Ley, a través del enunciado de Kelvin-Planck, dicta que es imposible construir un motor térmico cíclico cuyo único efecto sea absorber calor de un foco y transformarlo íntegramente en trabajo mecánico.
2. Ciclo de Carnot y Ciclo Rankine Básico:
El Ciclo de Carnot opera reversiblemente entre dos focos isotermos T_H y T_L, representando la cota teórica máxima absoluta de eficiencia. Las centrales termoeléctricas reales operan bajo el ciclo Rankine con cambio de fase líquida a vapor.
3. Problema Resuelto 1 (Aplicación Directa):
Una central termoeléctrica a carbón quema combustible suministrando calor a la caldera a T_H = 550 °C (823.15 K) y rechaza calor al condensador refrigerado por agua de río a T_L = 25 °C (298.15 K). Si la potencia térmica de entrada es Q_in = 600 MWt y la potencia eléctrica neta producida es W_neto = 210 MWe, calcule la eficiencia real y compárela con el límite de Carnot.
Solución:
Eficiencia real: eta_th = W_neto / Q_in = 210 / 600 = 0.3500 (35.0%).
Eficiencia máxima de Carnot:
eta_Carnot = 1 - (T_L / T_H) = 1 - (298.15 / 823.15) = 1 - 0.3622 = 0.6378 (63.78%).
Rendimiento de Segunda Ley: eta_II = eta_th / eta_Carnot = 0.35 / 0.6378 = 0.5488 (54.88%).
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un ciclo Rankine ideal simple con vapor recalentado, la bomba consume w_b = 4 kJ/kg de trabajo específico y la turbina produce w_t = 1004 kJ/kg. La caldera aporta q_in = 2500 kJ/kg. Determine el trabajo neto específico, la eficiencia térmica del ciclo y el flujo másico de vapor m_dot necesario para una planta de 150 MWe.
Solución:
Trabajo neto: w_neto = w_t - w_b = 1004 - 4 = 1000 kJ/kg.
Eficiencia térmica: eta_th = w_neto / q_in = 1000 / 2500 = 0.4000 (40.0%).
Flujo másico: P_neto = m_dot * w_neto.
m_dot = P_neto / w_neto = 150,000 kW / (1000 kJ/kg) = 150 kg/s de vapor de agua a alta presión.""",
        "bloque_sugerido": "Pomodoro 50/10 • Eficiencia térmica y ciclo Rankine",
        "slides": [
            {"numero": 1, "seccion": "LEYES", "titulo": "Principios Termodinámicos", "puntos": ["Primera Ley: balance estricto dE = dQ - dW.", "Segunda Ley: cota insuperable de Carnot eta = 1 - T_L / T_H."]},
            {"numero": 2, "seccion": "RANKINE", "titulo": "Generación Térmica de Potencia", "puntos": ["Vapor de agua como fluido de trabajo de alta entalpía.", "Cálculo de flujo másico m_dot para generación a escala de MW."]}
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Recursos Hidroeléctricos: Ecuación de Bernoulli y Tipologías",
        "objetivo": "Calcular la potencia hidroeléctrica bruta y neta aprovechando caídas hidráulicas y caudales de cuencas.",
        "concepto_clave_latex": r"P_{\text{hid}} = \rho g Q H_{\text{neto}} \eta_{\text{turb}} \quad ; \quad H_{\text{neto}} = H_{\text{bruta}} - h_f",
        "ejemplo": """CLASE MAGISTRAL: ENERGÍA HIDRÁULICA Y APROVECHAMIENTO DE CUENCAS
1. Potencial Gravitacional del Agua y Teorema de Bernoulli:
El agua retenida a una cota geométrica z posee energía potencial gravitacional. Al canalizarse a través de una tubería forzada, la energía potencial se transforma en energía de presión y cinética según Bernoulli: z_1 + P_1/(rho g) + v_1^2/(2g) = z_2 + P_2/(rho g) + v_2^2/(2g) + h_f.
2. Tipologías de Centrales Hidráulicas:
- Centrales a Filo de Agua (Run-of-River): Sin embalse de regulación; aprovechan el caudal natural instantáneo.
- Centrales con Embalse de Regulación: Almacenan energía potencial estacional para despacho firme.
- Centrales de Bombeo Reversible (Pumped-Storage): Baterías hidroeléctricas a escala gigavatio.
3. Problema Resuelto 1 (Aplicación Directa):
Una pequeña central hidroeléctrica (PCH) en la Sierra Nevada de Santa Marta aprovecha un salto bruto H_bruta = 85 m con un caudal turbinado Q = 1.2 m^3/s. Las pérdidas por fricción en la tubería forzada son h_f = 5 m. Si la turbina Francis tiene una eficiencia eta_t = 0.90 y el generador eta_g = 0.95, calcule la potencia eléctrica neta entregada en kW.
Solución:
Salto neto: H_neto = H_bruta - h_f = 85 - 5 = 80 m.
Densidad del agua rho = 1000 kg/m^3, g = 9.81 m/s^2.
Eficiencia global: eta_global = 0.90 * 0.95 = 0.855.
P_elec = rho * g * Q * H_neto * eta_global
P_elec = 1000 * 9.81 * 1.2 * 80 * 0.855 = 805,185 W = 805.19 kW.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un embalse hidroeléctrico almacena un volumen útil V = 50 millones de m^3 de agua a una altura media H = 150 m. Determine la energía eléctrica potencial total almacenable en GWh asumiendo un rendimiento global del 88%.
Solución:
Energía en Julios: E = rho * g * V * H * eta
E = (1000 kg/m^3) * (9.81 m/s^2) * (50e6 m^3) * (150 m) * 0.88
E = 6.4746 * 10^13 Julios.
Conversión a kWh: 1 kWh = 3.6 * 10^6 J.
E_kWh = 6.4746e13 / 3.6e6 = 17,985,000 kWh = 17.985 GWh.
El embalse equivale a una batería de almacenamiento electroquímico de 17.98 GWh de capacidad.""",
        "bloque_sugerido": "Práctica 50 min • Potencia hidráulica y selección de turbinas",
        "slides": [
            {"numero": 1, "seccion": "HIDRÁULICA", "titulo": "Potencial Hidroeléctrico", "puntos": ["Ecuación P = rho g Q H eta para dimensionamiento de PCHs y macrocentrales.", "Pérdidas de carga distribuidas y localizadas h_f en tuberías forzadas."]},
            {"numero": 2, "seccion": "TIPOLOGÍAS", "titulo": "Embalses y Filo de Agua", "puntos": ["Centrales de pasada vs embalses de regulación interanual.", "Bombeo hidráulico como vector dominante de almacenamiento masivo."]}
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Recurso Solar, Geometría y Horas de Sol Pico (HSP)",
        "objetivo": "Calcular la radiación solar incidente sobre superficies inclinadas mediante geometría solar y conceptos de HSP.",
        "concepto_clave_latex": r"HSP = \frac{H_{\text{diaria}} \left[\frac{\text{kWh}}{\text{m}^2\cdot\text{día}}\right]}{1\,\frac{\text{kW}}{\text{m}^2}} \quad ; \quad G_t = G_b R_b + G_d R_d + G \rho_g R_r",
        "ejemplo": """CLASE MAGISTRAL: RADIACIÓN SOLAR Y GEOMETRÍA ASTRONÓMICA
1. Constante Solar e Interacción Atmosférica:
La irradiancia solar extraterrestre media es la constante solar G_sc = 1361 W/m^2. Al atravesar la atmósfera terrestre, la radiación se atenúa por absorción y dispersión (Rayleigh y Mie), dividiéndose en tres componentes: directa (haz), difusa y de albedo (reflejada en el suelo).
2. Horas de Sol Pico (HSP):
Una Hora de Sol Pico representa la energía solar acumulada durante una hora a una irradiancia constante normalizada de 1000 W/m^2. Si una localidad en Santa Marta recibe 5.5 kWh/(m^2*día), cuenta con exactamente 5.5 HSP/día.
3. Problema Resuelto 1 (Aplicación Directa):
Un tejado en el campus de Unimagdalena recibe una insolación diaria promedio en el plano de los paneles de H = 5.8 kWh/(m^2*día). Si se instala un generador fotovoltaico con potencia pico P_pico = 10 kWp y factor de rendimiento PR = 0.80, calcule la energía diaria esperada en kWh.
Solución:
Energía diaria: E_día = P_pico * HSP * PR
E_día = 10 kWp * (5.8 h/día) * 0.80 = 46.4 kWh/día.
Producción mensual promedio (30 días): 46.4 * 30 = 1392 kWh/mes.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Deduzca la elevación solar solar alfa al mediodía solar para Santa Marta (latitud phi = 11.24° N) en el solsticio de verano (declinación solar delta = +23.45°) y determine el ángulo de inclinación óptimo anual beta para paneles fijos.
Solución:
Al mediodía solar (ángulo horario omega = 0°):
Elevación solar: alfa = 90° - |phi - delta|
alfa = 90° - |11.24° - 23.45°| = 90° - |-12.21°| = 90° - 12.21° = 77.79° sobre el horizonte norte.
Para captación fija anual óptima cerca del ecuador: la inclinación óptima se aproxima a la latitud beta_opt = phi = 11° orientados al sur geográfico (azimut gamma = 0°) con un mínimo de 10° para permitir autolimpieza por lluvia.""",
        "bloque_sugerido": "Laboratorio 50 min • Cálculo de HSP y cartas solares",
        "slides": [
            {"numero": 1, "seccion": "RADIACIÓN", "titulo": "Componentes de Irradiancia", "puntos": ["Constante solar 1361 W/m^2 y masa de aire AM 1.5 global.", "Descomposición en directa, difusa y albedo superficial."]},
            {"numero": 2, "seccion": "GEOMETRÍA", "titulo": "HSP e Inclinación Óptima", "puntos": ["Normalización a 1000 W/m^2 para cálculo directo E = P_pico * HSP * PR.", "Regla de inclinación por latitud para maximización anual."]}
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Principio Fotovoltaico, Curva I-V y Punto de Máxima Potencia (MPPT)",
        "objetivo": "Modelar la física de semiconductores en uniones p-n y determinar el Punto de Máxima Potencia (PMP).",
        "concepto_clave_latex": r"I = I_{\text{ph}} - I_0 \left[\exp\left(\frac{q(V + I R_s)}{n k_B T}\right) - 1\right] - \frac{V + I R_s}{R_{\text{sh}}} \quad ; \quad FF = \frac{P_{\text{mp}}}{V_{\text{oc}} I_{\text{sc}}}",
        "ejemplo": """CLASE MAGISTRAL: DISPOSITIVOS FOTOVOLTAICOS Y CURVA CARACTERÍSTICA
1. Unión P-N y Efecto Fotoeléctrico Interno:
Cuando fotones con energía h*nu superior a la banda prohibida (Bandgap E_g = 1.12 eV en silicio cristalino) impactan la celda, generan pares electrón-hueco. El campo eléctrico de la zona de agotamiento separa los portadores libres, originando la fotocorriente I_ph.
2. Curva Característica I-V y Parámetros Clave:
- Corriente de cortocircuito (I_sc): Máxima corriente con V = 0.
- Tensión de circuito abierto (V_oc): Máxima tensión con I = 0.
- Factor de Llenado (Fill Factor - FF): Rectangularidad de la curva I-V (típicamente 0.75 - 0.83).
- MPPT: Algoritmos (Perturbar y Observar, Conductancia Incremental) que rastrean P_mp = V_mp * I_mp en tiempo real.
3. Problema Resuelto 1 (Aplicación Directa):
Un módulo fotovoltaico de 72 celdas monocristalinas presenta bajo condiciones estándar (STC: 1000 W/m^2, 25 °C): V_oc = 48.5 V, I_sc = 11.2 A, V_mp = 40.2 V e I_mp = 10.6 A. Calcule la potencia pico nominal P_mp y el Factor de Llenado (FF).
Solución:
Potencia pico: P_mp = V_mp * I_mp = 40.2 V * 10.6 A = 426.12 Wp.
Potencia aparente de esquinas: P_teorica = V_oc * I_sc = 48.5 V * 11.2 A = 543.20 W.
Fill Factor: FF = P_mp / (V_oc * I_sc) = 426.12 / 543.20 = 0.7845 (78.45%).
4. Problema Resuelto 2 (Nivel Examen Parcial):
El coeficiente térmico de tensión de un módulo solar es gamma_Voc = -0.28 %/°C referido a 25 °C. Si durante una tarde soleada en el Caribe la temperatura de operación de la celda alcanza T_c = 65 °C, calcule la nueva tensión de circuito abierto real sabiendo que V_oc(25°C) = 48.5 V.
Solución:
delta_T = T_c - 25 °C = 65 - 25 = +40 °C.
Variación porcentual: delta_Voc% = (-0.28 %/°C) * 40 °C = -11.2 %.
Variación absoluta: delta_Voc = 48.5 V * (-0.112) = -5.432 V.
V_oc(65°C) = 48.5 - 5.432 = 43.068 V.
Conclusión: El calentamiento severo reduce notablemente el voltaje de salida, justificando ventilación adecuada bajo los módulos fotovoltaicos.""",
        "bloque_sugerido": "Laboratorio 50 min • Trazado de curva I-V y cálculo de Fill Factor",
        "slides": [
            {"numero": 1, "seccion": "FÍSICA", "titulo": "Semiconductores y Fotocorriente", "puntos": ["Efecto fotovoltaico en unión p-n con bandgap de 1.12 eV.", "Ecuación del diodo con resistencias parásitas R_s y R_sh."]},
            {"numero": 2, "seccion": "OPERACIÓN", "titulo": "Curva I-V y Coeficiente Térmico", "puntos": ["Punto de máxima potencia MPPT y Fill Factor FF.", "Degradación de voltaje por alta temperatura de operación."]}
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Recurso Eólico, Aerodinámica Básica y Límite de Betz",
        "objetivo": "Calcular la densidad de potencia del viento y aplicar el Límite de Betz a turbinas eólicas.",
        "concepto_clave_latex": r"P_{\text{viento}} = \frac{1}{2}\rho A v^3 \quad ; \quad C_p = \frac{P_{\text{mec}}}{P_{\text{viento}}} \le \frac{16}{27} \approx 0.5926",
        "ejemplo": """CLASE MAGISTRAL: ENERGÍA CINÉTICA DEL VIENTO Y LÍMITE DE BETZ
1. Potencia Específica y Ley Cúbica de la Velocidad:
La potencia cinética disponible en una masa de aire en movimiento a través de un área A es proporcional a la densidad rho y al cubo de la velocidad del viento v^3. Un aumento del 26% en la velocidad duplica la potencia disponible (1.26^3 = 2.00).
2. Teoría del Disco Actuador y Límite de Betz:
Albert Betz demostró en 1919 que un rotor eólico ideal no puede extraer el 100% de la energía del viento porque el aire debe salir del rotor con velocidad finita v_2 > 0 para evacuar la zona. El coeficiente de potencia máximo teórico es exactamente C_p,max = 16/27 = 59.26%.
3. Problema Resuelto 1 (Aplicación Directa):
Un aerogenerador instalado en la costa de La Guajira tiene un rotor de diámetro D = 120 m. La velocidad del viento es v = 11 m/s y la densidad del aire al nivel del mar es rho = 1.20 kg/m^3. Calcule la potencia del viento incidente y la potencia mecánica capturada si el rotor opera a C_p = 0.45.
Solución:
Área barrida por el rotor: A = pi * (D/2)^2 = pi * (60)^2 = 11,309.73 m^2.
Potencia total del viento:
P_viento = 0.5 * rho * A * v^3
P_viento = 0.5 * 1.20 * 11,309.73 * (11)^3 = 0.60 * 11,309.73 * 1331 = 9,031,950 W = 9.032 MW.
Potencia mecánica capturada:
P_mec = P_viento * C_p = 9.032 MW * 0.45 = 4.064 MW.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente mediante balance de cantidad de movimiento que el coeficiente de potencia C_p(a) = 4 a (1 - a)^2, donde a = (v_1 - v_rotor)/v_1 es el factor de inducción axial, y obtenga el valor óptimo de a que maximiza C_p.
Solución:
Por conservación de cantidad de movimiento y energía:
La velocidad en el disco es v = v_1 * (1 - a), y aguas abajo v_2 = v_1 * (1 - 2a).
El empuje axial es T = 2 * rho * A * v_1^2 * a * (1 - a).
La potencia extraída es P = T * v = 2 * rho * A * v_1^3 * a * (1 - a)^2.
Dividiendo entre P_viento = 0.5 * rho * A * v_1^3:
C_p(a) = P / P_viento = 4 a (1 - a)^2.
Para maximizar, derivamos respecto a a e igualamos a cero:
dC_p/da = 4 * [ (1 - a)^2 + a * 2(1 - a)(-1) ] = 4 (1 - a) [ (1 - a) - 2a ] = 4 (1 - a)(1 - 3a) = 0.
Raíces: a = 1 (mínimo físico) o a = 1/3.
Evaluando en a = 1/3:
C_p(1/3) = 4 * (1/3) * (1 - 1/3)^2 = (4/3) * (2/3)^2 = (4/3) * (4/9) = 16/27 approx 0.5926. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Ley cúbica del viento y límite de Betz",
        "slides": [
            {"numero": 1, "seccion": "CINÉTICA", "titulo": "Potencia del Viento", "puntos": ["Dependencia cúbica v^3 de la velocidad del viento.", "Densidad del aire rho dependiente de temperatura y presión altimétrica."]},
            {"numero": 2, "seccion": "BETZ", "titulo": "Límite Teórico de Betz", "puntos": ["Factor de inducción axial óptimo a = 1/3.", "Máximo teórico C_p = 16/27 (59.3%) para rotores aerodinámicos."]}
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Biomasa, Biocombustibles y Termoquímica de Conversión",
        "objetivo": "Evaluar el potencial energético de residuos agroindustriales mediante PCS/PCI y balances de combustión.",
        "concepto_clave_latex": r"\text{PCI} = \text{PCS} - 2.442 \left(\frac{9 H\% + W\%}{100}\right) \left[\frac{\text{MJ}}{\text{kg}}\right]",
        "ejemplo": """CLASE MAGISTRAL: RECURSOS BIOMÁSICOS Y CONVERSIÓN ENERGÉTICA
1. Clasificación de la Biomasa:
Residuos agrícolas (bagazo de caña, cascarilla de arroz, cuesco de palma de aceite en el Magdalena), residuos forestales, pecuarios y fracciones orgánicas urbanas.
2. Poder Calorífico Superior (PCS) e Inferior (PCI):
- PCS (High Heating Value - HHV): Considera que el agua condensó cediendo su calor latente de vaporización (2.442 MJ/kg a 25 °C).
- PCI (Low Heating Value - LHV): Considera que el agua escapa en los gases de combustión en fase vapor (el calor latente no se aprovecha en calderas estándar).
3. Problema Resuelto 1 (Aplicación Directa):
Una muestra de cuesco de palma de aceite en la Zona Bananera presenta un PCS base seca de 19.5 MJ/kg, un contenido de hidrógeno H = 6.0% y una humedad residual W = 12.0%. Calcule el Poder Calorífico Inferior (PCI) real disponible.
Solución:
PCI = PCS - 2.442 * [ (9 * H% + W%) / 100 ]
9 * H% + W% = 9 * 6.0 + 12.0 = 54.0 + 12.0 = 66.0 %.
Pérdida por vaporización: 2.442 * (66.0 / 100) = 2.442 * 0.66 = 1.612 MJ/kg.
PCI = 19.5 - 1.612 = 17.888 MJ/kg.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Una planta de beneficio de palma genera 10 toneladas por hora de biomasa residual con PCI = 16 MJ/kg. Si alimenta una caldera de cogeneración de biomasa con eficiencia térmica eta_b = 0.75 acoplada a un turbogenerador con eta_e = 0.25, determine la potencia eléctrica neta producida en MW.
Solución:
Flujo másico: m_dot = 10,000 kg/h = 10,000 / 3600 = 2.7778 kg/s.
Potencia térmica del combustible:
P_comb = m_dot * PCI = 2.7778 kg/s * 16 MJ/kg = 44.444 MWt.
Potencia de vapor producida por la caldera:
P_vapor = P_comb * eta_b = 44.444 * 0.75 = 33.333 MWt.
Potencia eléctrica neta generada:
P_elec = P_vapor * eta_e = 33.333 * 0.25 = 8.333 MWe.""",
        "bloque_sugerido": "Laboratorio 50 min • Caracterización biomásica y PCI",
        "slides": [
            {"numero": 1, "seccion": "BIOMASA", "titulo": "Poder Calorífico y Humedad", "puntos": ["Diferencia entre PCS y PCI debida al calor latente del agua.", "Impacto crítico de la humedad en la temperatura de llama."]},
            {"numero": 2, "seccion": "CONVERSIÓN", "titulo": "Cogeneración Agroindustrial", "puntos": ["Aprovechamiento de biomasa de palma y caña en el Caribe colombiano.", "Generación simultánea de calor de proceso y electricidad neta."]}
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Energías Geotérmica y Marina: Principios de Extracción",
        "objetivo": "Comprender la termodinámica de reservorios geotérmicos y la cinética de mareas y corrientes oceánicas.",
        "concepto_clave_latex": r"E_{\text{marea}} = \frac{1}{2} \rho g A_{\text{cuenca}} R^2 \quad ; \quad \dot{Q}_{\text{geo}} = \dot{m} (h_{\text{pozo}} - h_{\text{retorno}})",
        "ejemplo": """CLASE MAGISTRAL: ENERGÍAS GEOTÉRMICA Y MARINA
1. Gradiente Geotérmico y Reservorios de Entalpía:
La temperatura terrestre aumenta típicamente 30 °C por cada kilómetro de profundidad. En zonas volcánicas (Cordillera Central colombiana, Nevado del Ruiz), el gradiente supera los 100 °C/km, permitiendo reservorios de vapor seco o agua sobrecalentada para ciclos flash o binarios ORC.
2. Recursos Marinos (Mareas, Olas y Gradiente Térmico OTEC):
- Energía Mareomotriz: Aprovecha la amplitud de marea R (diferencia pleamar-bajamar).
- Energía Undimotriz: Captura la oscilación periódica del oleaje en boyas y columnas de agua oscilante (OWC).
3. Problema Resuelto 1 (Aplicación Directa):
Una central mareomotriz aprovecha una bahía estuarina de área A = 15 km^2 con un rango de marea R = 6.0 m. Calcule la energía potencial teórica disponible por ciclo de marea (rho_mar = 1025 kg/m^3).
Solución:
E = 0.5 * rho * g * A * R^2
A = 15 * 10^6 m^2 = 1.5e7 m^2.
E = 0.5 * (1025) * (9.81) * (1.5e7) * (6.0^2)
E = 0.5 * 1025 * 9.81 * 1.5e7 * 36 = 2.714 * 10^12 Julios por ciclo.
En MWh: E = 2.714e12 / 3.6e9 = 753.89 MWh por ciclo de vaciado.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un pozo geotérmico de entalpía media produce m_dot = 50 kg/s de salmuera líquida presurizada a 180 °C (entalpía h_1 = 763 kJ/kg). Se expande en una turbina de ciclo binario ORC que rechaza calor a 50 °C (entalpía h_2 = 209 kJ/kg) con un rendimiento neto de planta de 12%. Calcule la potencia eléctrica neta producida en MWe.
Solución:
Calor térmico transferido al ciclo binario:
Q_dot = m_dot * (h_1 - h_2) = 50 kg/s * (763 - 209 kJ/kg) = 50 * 554 = 27,700 kWt = 27.70 MWt.
Potencia eléctrica neta:
P_elec = Q_dot * eta_planta = 27.70 MWt * 0.12 = 3.324 MWe de generación continua en base (factor de planta > 90%).""",
        "bloque_sugerido": "Pomodoro 50/10 • Potencial geotérmico y mareomotriz",
        "slides": [
            {"numero": 1, "seccion": "GEOTERMIA", "titulo": "Entalpía y Ciclos Binarios", "puntos": ["Gradiente geotérmico y reservorios hidrotermales.", "Ciclos Rankine Orgánicos (ORC) para recursos de baja/media entalpía."]},
            {"numero": 2, "seccion": "MARINA", "titulo": "Energía Mareomotriz y Undimotriz", "puntos": ["Energía potencial de mareas cuadrática con el rango E prop R^2.", "Disponibilidad de energía de olas y corrientes marinas en litorales."]}
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Sistemas de Transmisión y Distribución Eléctrica: Pérdidas y Flujo",
        "objetivo": "Modelar pérdidas Joule en líneas de transmisión y comprender la necesidad del transporte en alta tensión.",
        "concepto_clave_latex": r"P_{\text{loss}} = 3 I^2 R = \frac{P^2 + Q^2}{V_L^2} R \quad ; \quad \Delta V \approx \frac{P R + Q X}{V}",
        "ejemplo": """CLASE MAGISTRAL: REDES DE TRANSPORTE Y DISTRIBUCIÓN ELÉCTRICA
1. Estructura de la Cadena de Suministro Eléctrico:
La electricidad se genera a media tensión (11 - 25 kV), se eleva en subestaciones a Muy Alta Tensión (230 - 500 kV) para transporte a largas distancias, se reduce en subestaciones de subtransmisión (110 - 66 kV) y finalmente se distribuye a usuarios finales (13.2 kV y 220/127 V).
2. Justificación Física del Transporte en Alta Tensión:
Para transmitir una potencia activa P constante, la corriente requerida es I = P / (sqrt(3) V cos phi). Como las pérdidas Joule por efecto conductor son proporcionales a I^2, al multiplicar la tensión V por 10, la corriente se reduce por 10 y las pérdidas se reducen por un factor de 100 (10^2).
3. Problema Resuelto 1 (Aplicación Directa):
Se transmiten P = 100 MW a través de una línea trifásica de 80 km con resistencia por fase R = 4 Ohm y factor de potencia unitario. Calcule las pérdidas Joule si se transmite a: a) 115 kV; b) 230 kV.
Solución:
a) A 115 kV:
I_1 = P / (sqrt(3) * V_1) = 100e6 / (sqrt(3) * 115,000) = 502.04 A.
P_loss_1 = 3 * I_1^2 * R = 3 * (502.04)^2 * 4 = 3,024,545 W = 3.025 MW (3.03% de la potencia transmitida).
b) A 230 kV:
I_2 = P / (sqrt(3) * V_2) = 100e6 / (sqrt(3) * 230,000) = 251.02 A.
P_loss_2 = 3 * I_2^2 * R = 3 * (251.02)^2 * 4 = 756,136 W = 0.756 MW (0.76% de la potencia transmitida).
El aumento a 230 kV redujo las pérdidas a la cuarta parte (75% de ahorro de energía disipada).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Una línea de distribución monofásica de R = 0.5 Ohm y X = 1.2 Ohm alimenta una carga inductiva de P = 50 kW con cos phi = 0.707 inductivo (Q = 50 kVAR) a una tensión nominal de recepción V = 220 V. Calcule la caída de tensión en la línea y determine el impacto de instalar un condensador que compense totalmente la potencia reactiva Q = 0.
Solución:
Caída aproximada: delta_V = (P * R + Q * X) / V.
Con Q = 50 kVAR:
delta_V = (50,000 * 0.5 + 50,000 * 1.2) / 220 = (25,000 + 60,000) / 220 = 85,000 / 220 = 386.36 V.
(Caída inadmisible que superaría el propio voltaje nominal).
Con compensación de reactivos (Q = 0):
delta_V_comp = (50,000 * 0.5 + 0) / 220 = 25,000 / 220 = 113.6 V.
Demuestra la función crítica de los bancos de condensadores en mejorar el perfil de tensión de alimentadores.""",
        "bloque_sugerido": "Laboratorio 50 min • Pérdidas Joule y compensación reactiva",
        "slides": [
            {"numero": 1, "seccion": "TRANSMISIÓN", "titulo": "Pérdidas Joule en Redes", "puntos": ["Reducción de pérdidas cuadrática con el voltaje P_loss prop 1/V^2.", "Estructura jerárquica del SIN: 500 kV, 230 kV, 110 kV y media tensión."]},
            {"numero": 2, "seccion": "REGULACIÓN", "titulo": "Caída de Tensión y Reactivos", "puntos": ["Fórmula de aproximación delta_V = (P R + Q X) / V.", "Compensación capacitiva para control de voltaje y liberación de capacidad."]}
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Centrales Termoeléctricas y Ciclos Combinados Gas-Vapor",
        "objetivo": "Analizar la termodinámica del ciclo Brayton-Rankine integrado y calcular eficiencias superiores al 60%.",
        "concepto_clave_latex": r"\eta_{\text{cc}} = \eta_{\text{gas}} + \eta_{\text{vapor}} - \eta_{\text{gas}}\eta_{\text{vapor}} \quad ; \quad r_p = \frac{P_2}{P_1}",
        "ejemplo": """CLASE MAGISTRAL: TECNOLOGÍA DE CICLOS COMBINADOS
1. Turbinas de Gas y Ciclo Brayton:
El aire atmosférico es comprimido (compresor axial), entra a la cámara de combustión donde se quema gas natural a presión constante, y los gases a alta temperatura (hasta 1400 °C) se expanden en la turbina de gas generando potencia y saliendo a 550 - 600 °C.
2. Integración en Ciclo Combinado:
En lugar de disipar los gases calientes de escape a la atmósfera, se conducen a una Caldera de Recuperación de Calor (Heat Recovery Steam Generator - HRSG) que produce vapor sobrecalentado para impulsar una turbina de vapor (ciclo Rankine secundario).
3. Problema Resuelto 1 (Aplicación Directa):
Una central de ciclo combinado en Termobarranquilla tiene una turbina de gas con eficiencia eta_gas = 38.0% y un ciclo de vapor secundario con eficiencia eta_vapor = 35.0% calculada sobre el calor residual recuperado (con recuperación del 80%). Calcule la eficiencia global del ciclo combinado.
Solución:
Sea Q_in = 100 unidades de calor térmico de gas natural.
Potencia eléctrica de la turbina de gas: W_gas = 100 * 0.38 = 38 unidades.
Calor remanente en gases de escape: Q_escape = 100 - 38 = 62 unidades.
Calor recuperado en la HRSG: Q_hrsg = 62 * 0.80 = 49.6 unidades.
Potencia eléctrica de la turbina de vapor: W_vapor = 49.6 * 0.35 = 17.36 unidades.
Potencia total neta: W_total = 38 + 17.36 = 55.36 unidades.
Eficiencia neta del ciclo combinado: eta_cc = W_total / Q_in = 55.36 / 100 = 0.5536 (55.36%).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre la fórmula de acoplamiento ideal eta_cc = eta_1 + eta_2 - eta_1 * eta_2 asumiendo recuperación perfecta del calor de escape (Q_in2 = Q_out1) y analice por qué un ciclo combinado supera a cualquier ciclo simple.
Solución:
eta_1 = W_1 / Q_in1 ==> W_1 = eta_1 * Q_in1.
Q_out1 = Q_in1 - W_1 = Q_in1 * (1 - eta_1).
Asumiendo Q_in2 = Q_out1:
W_2 = eta_2 * Q_in2 = eta_2 * Q_in1 * (1 - eta_1).
Trabajo total: W_total = W_1 + W_2 = eta_1 * Q_in1 + eta_2 * Q_in1 * (1 - eta_1)
W_total = Q_in1 * [ eta_1 + eta_2 - eta_1 * eta_2 ].
Dividiendo entre Q_in1:
eta_cc = eta_1 + eta_2 - eta_1 * eta_2.
Análisis: Si eta_1 = 0.40 y eta_2 = 0.35:
eta_cc = 0.40 + 0.35 - (0.40 * 0.35) = 0.75 - 0.14 = 0.6100 (61.0%).
Se superan holgadamente las cotas de 40% de plantas térmicas simples convencionales. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Ciclos combinados Brayton-Rankine",
        "slides": [
            {"numero": 1, "seccion": "BRAYTON", "titulo": "Turbinas de Gas de Alta Temperatura", "puntos": ["Compresión y combustión continua de gas natural.", "Escape de gases a 550 - 600 °C con alto potencial exergético."]},
            {"numero": 2, "seccion": "COMBINADO", "titulo": "Calderas HRSG y Alta Eficiencia", "puntos": ["Generación de vapor sin consumo adicional de combustible.", "Eficiencias eléctricas combinadas superiores al 60%."]}
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Combustión, Estequiometría Energética y Emisiones",
        "objetivo": "Calcular relaciones aire-combustible estequiométricas, exceso de aire y emisiones de dióxido de carbono.",
        "concepto_clave_latex": r"\text{CH}_4 + 2(\text{O}_2 + 3.76\text{N}_2) \to \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2 \quad ; \quad \lambda = \frac{(A/C)_{\text{real}}}{(A/C)_{\text{esteq}}}",
        "ejemplo": """CLASE MAGISTRAL: QUÍMICA DE LA COMBUSTIÓN Y EMISIONES
1. Reacciones de Combustión Completa e Incompleta:
La combustión completa oxida totalmente el carbono a CO_2 y el hidrógeno a H_2O. Si hay defecto de oxígeno (lambda < 1), se produce monóxido de carbono tóxico (CO), inquemados y hollín, reduciendo severamente el rendimiento térmico.
2. Relación Aire-Combustible (Air-Fuel Ratio - A/F):
Masa de aire requerida por unidad de masa de combustible. El aire atmosférico contiene en volumen 21% de O_2 y 79% de N_2 (3.76 moles de N_2 por cada mol de O_2; masa molar aparente del aire = 28.97 g/mol).
3. Problema Resuelto 1 (Aplicación Directa):
Calcule la relación másica estequiométrica aire-combustible (A/F)_esteq para la combustión completa de metano puro (CH_4).
Solución:
Reacción estequiométrica: CH_4 + 2(O_2 + 3.76 N_2) -> CO_2 + 2 H_2O + 7.52 N_2.
Masa de 1 mol de metano: M_CH4 = 12.01 + 4 * 1.008 = 16.04 g/mol.
Masa de aire estequiométrico:
Moles de aire = 2 * (1 + 3.76) = 2 * 4.76 = 9.52 moles de aire.
Masa de aire = 9.52 mol * 28.97 g/mol = 275.80 g.
(A/F)_esteq = 275.80 g de aire / 16.04 g de CH4 = 17.19 kg de aire / kg de combustible.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un quemador industrial consume 50 kg/h de gas natural (tratado como CH_4) con un exceso de aire del 20% (lambda = 1.20). Determine el flujo másico real de aire requerido y la masa de CO_2 emitida por hora a la atmósfera.
Solución:
1. Flujo de aire real:
Flujo estequiométrico: m_aire_esteq = 50 kg/h * 17.19 = 859.5 kg/h.
Con lambda = 1.20: m_aire_real = 859.5 * 1.20 = 1031.4 kg/h de aire.
2. Emisiones de CO_2:
Por cada mol de CH_4 (16.04 g) se produce 1 mol de CO_2 (44.01 g).
Factor estequiométrico de CO_2 = 44.01 / 16.04 = 2.744 kg CO_2 / kg CH_4.
Masa emitida por hora:
m_CO2 = 50 kg/h * 2.744 = 137.2 kg de CO_2 por hora de operación.""",
        "bloque_sugerido": "Laboratorio 50 min • Estequiometría de combustión y factor lambda",
        "slides": [
            {"numero": 1, "seccion": "QUÍMICA", "titulo": "Estequiometría y Factor Lambda", "puntos": ["Ecuación balanceada con composición de aire seco (3.76 N_2).", "Exceso de aire lambda > 1 para garantizar combustión completa sin CO."]},
            {"numero": 2, "seccion": "EMISIONES", "titulo": "Huella de CO_2 de Combustibles", "puntos": ["Cálculo estequiométrico de factor de emisión por kg quemado.", "Monitoreo de gases de chimenea (O_2, CO_2, NO_x)."]}
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Auditorías Energéticas, ISO 50001 e Indicadores EnPI",
        "objetivo": "Estructurar auditorías según ISO 50002 y definir Indicadores de Desempeño Energético (EnPI) y Líneas Base (EnB).",
        "concepto_clave_latex": r"\text{EnPI} = \frac{E_{\text{consumida}}}{Q_{\text{producción}}} \quad ; \quad \text{Ahorro} = E_{\text{base}}(x) - E_{\text{real}}(x)",
        "ejemplo": """CLASE MAGISTRAL: GESTIÓN ENERGÉTICA E ISO 50001
1. Sistema de Gestión de la Energía (SGEn) - Ciclo PHVA:
La norma internacional ISO 50001 establece un marco sistemático para Planificar, Hacer, Verificar y Actuar en torno a la eficiencia energética, reduciendo costos operativos y emisiones de carbono.
2. Línea Base Energética (Energy Baseline - EnB) e Indicadores (EnPI):
- EnB: Curva de regresión histórica que modela el consumo en función de variables relevantes (producción industrial, grados-día de refrigeración, ocupación de campus).
- EnPI: Métrica normalizada que permite comparar el desempeño real vs la base eliminando el impacto de fluctuaciones de volumen productivo.
3. Problema Resuelto 1 (Aplicación Directa):
Una planta procesadora de alimentos en Santa Marta consumió 250,000 kWh en un mes donde produjo 500 toneladas de producto. Calcule el EnPI específico. Si el benchmark de la industria es 420 kWh/t, determine la brecha de ineficiencia porcentual.
Solución:
EnPI_actual = 250,000 kWh / 500 t = 500.0 kWh/t.
Brecha vs Benchmark:
delta% = [ (500 - 420) / 420 ] * 100% = (80 / 420) * 100% = +19.05 %.
La planta consume un 19.05% más de energía por tonelada que las mejores prácticas industriales.
4. Problema Resuelto 2 (Nivel Examen Parcial):
La línea base de consumo eléctrico mensual de un edificio universitario se ajustó mediante regresión como: E_base(CDD) = 15,000 + 450 * CDD [kWh/mes], donde CDD son los Grados-Día de Refrigeración. Tras modernizar el sistema de aire acondicionado central (chillers), en un mes con CDD = 120 el consumo real medido fue E_real = 58,000 kWh. Calcule el ahorro energético absoluto y porcentual atribuible a la modernización.
Solución:
Consumo proyectado de la Línea Base:
E_base(120) = 15,000 + 450 * (120) = 15,000 + 54,000 = 69,000 kWh.
Ahorro absoluto normalizado:
Ahorro = E_base - E_real = 69,000 - 58,000 = 11,000 kWh/mes.
Ahorro porcentual verificado:
Ahorro% = (11,000 / 69,000) * 100% = 15.94 % de ahorro real auditado.""",
        "bloque_sugerido": "Taller 50 min • Formulación de EnPI y línea base ISO 50001",
        "slides": [
            {"numero": 1, "seccion": "GESTIÓN", "titulo": "Norma ISO 50001 y PHVA", "puntos": ["Política energética, planeación y revisión de usos significativos (USE).", "Auditorías energéticas de Nivel I, II y III según ISO 50002."]},
            {"numero": 2, "seccion": "MÉTRICAS", "titulo": "Línea Base y Ahorros Verificados", "puntos": ["Regresión multivariable considerando variables climáticas (CDD/HDD).", "Protocolo IPMVP para verificación cuantitativa de ahorros."]}
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Cogeneración, Trigeneración y Recuperación de Calor Residual",
        "objetivo": "Diseñar esquemas de cogeneración CHP y trigeneración CCHP con enfriadores de absorción.",
        "concepto_clave_latex": r"\text{FUE} = \frac{W_{\text{neto}} + Q_{\text{útil}}}{Q_{\text{in}}} \quad ; \quad \text{COP}_{\text{abs}} = \frac{Q_{\text{frío}}}{Q_{\text{calor}}}",
        "ejemplo": """CLASE MAGISTRAL: COGENERACIÓN (CHP) Y TRIGENERACIÓN (CCHP)
1. Principio de la Producción Combinada de Calor y Electricidad (CHP):
En una central convencional se pierde más del 50% de la energía primaria como calor residual en condensadores. La cogeneración produce simultáneamente electricidad y calor útil de proceso (vapor, agua caliente), elevando el Factor de Utilización de Energía (FUE) del 40% a más del 80%.
2. Trigeneración (CCHP):
Acopla un ciclo frigorífico accionado térmicamente (chiller de absorción LiBr-H2O o NH3-H2O) para transformar el calor residual en frío para aire acondicionado o refrigeración industrial.
3. Problema Resuelto 1 (Aplicación Directa):
Un hospital en Santa Marta instala un motogenerador de gas natural de Q_in = 2000 kWt. Produce P_elec = 760 kWe de electricidad y recupera Q_calor = 880 kWt de calor útil para agua caliente sanitaria y esterilización. Calcule el Factor de Utilización de Energía (FUE).
Solución:
FUE = (P_elec + Q_calor) / Q_in
FUE = (760 + 880) / 2000 = 1640 / 2000 = 0.8200 (82.0%).
El sistema aprovecha el 82% de la energía del combustible fósil frente al ~38% de una compra convencional de red.
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un esquema de trigeneración, los 880 kWt de calor recuperado del motor anterior alimentan un enfriador de absorción de bromuro de litio con COP_abs = 0.72. Determine la capacidad frigorífica producida en toneladas de refrigeración (TR, donde 1 TR = 3.517 kW) y la reducción en demanda eléctrica sabiendo que los aires acondicionados reemplazados tenían un COP_electrico = 3.0.
Solución:
Capacidad frigorífica:
Q_frio = Q_calor * COP_abs = 880 kWt * 0.72 = 633.6 kW de frío.
En toneladas de refrigeración: TR = 633.6 / 3.517 = 180.15 TR de climatización.
Demanda eléctrica evitada que consumían los chillers convencionales:
P_elec_evitada = Q_frio / COP_electrico = 633.6 kW / 3.0 = 211.2 kWe.
Aporte total del sistema: 760 kWe generados + 211.2 kWe ahorrados = 971.2 kWe de impacto positivo en la red.""",
        "bloque_sugerido": "Laboratorio 50 min • Balances térmicos en trigeneración CCHP",
        "slides": [
            {"numero": 1, "seccion": "CHP", "titulo": "Factor de Utilización de Energía", "puntos": ["Superación del 80% de aprovechamiento en sistemas de calor y potencia.", "Diagrama de Sankey comparativo frente a generación separada."]},
            {"numero": 2, "seccion": "TRIGENERACIÓN", "titulo": "Enfriadores por Absorción", "puntos": ["Conversión de calor de escape en climatización mediante LiBr-H2O.", "Reducción sustancial del pico eléctrico diurno de aire acondicionado."]}
        ]
    }
]

topics_21_to_30 = [
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Redes Inteligentes (Smart Grids) y Medición Avanzada (AMI)",
        "objetivo": "Comprender la arquitectura bidireccional de potencia y datos en Smart Grids y protocolos de telemetría AMI.",
        "concepto_clave_latex": r"\text{PAR} = \frac{P_{\text{pico}}}{P_{\text{promedio}}} \quad ; \quad \text{DR: } \Delta P(t) = -\varepsilon_d \cdot \frac{\Delta \text{Tarifa}(t)}{\text{Tarifa}_0} P_0",
        "ejemplo": """CLASE MAGISTRAL: REDES ELÉCTRICAS INTELIGENTES Y GESTIÓN DE DEMANDA
1. Transición de la Red Pasiva a la Red Activa:
La red tradicional era unidireccional (de grandes centrales a usuarios pasivos). La Smart Grid integra flujos bidireccionales de electricidad y comunicación digital en tiempo real, permitiendo incorporar masivamente prosumidores, almacenamiento y respuesta a la demanda.
2. Infraestructura de Medición Avanzada (AMI):
Sustituye los medidores electromagnéticos por contadores inteligentes conectados bidireccionalmente por PLC, celular (NB-IoT) o RF Mesh, habilitando tarifas horarias dinámicas (Time-of-Use - TOU) y desconexión remota.
3. Problema Resuelto 1 (Aplicación Directa):
Un alimentador urbano atiende una carga diaria con demanda pico P_pico = 15 MW y consumo de energía total diario E_día = 216 MWh. Calcule la demanda promedio y la Relación Pico a Promedio (Peak-to-Average Ratio - PAR).
Solución:
Demanda promedio: P_prom = E_día / 24 h = 216 / 24 = 9.0 MW.
PAR = P_pico / P_prom = 15.0 / 9.0 = 1.6667.
Un PAR de 1.67 indica que la infraestructura de distribución está sobredimensionada en un 67% sólo para soportar unas pocas horas pico de demanda.
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un esquema de Respuesta a la Demanda (Demand Response) con tarifa horaria dinámica, el precio de la electricidad se duplica durante las horas pico de 18:00 a 21:00 (de 0.15 USD/kWh a 0.30 USD/kWh, variación de +100%). Si la elasticidad precio de la demanda residencial en el Caribe es epsilon_d = -0.15 y la potencia base era 20 MW, calcule la reducción de potencia lograda en el pico y el nuevo pico de potencia.
Solución:
delta_Tarifa / Tarifa_0 = (0.30 - 0.15) / 0.15 = +1.00 (+100%).
Variación de demanda:
delta_P / P_0 = epsilon_d * (delta_Tarifa / Tarifa_0) = (-0.15) * (+1.00) = -0.15 (-15%).
Reducción de potencia:
delta_P = -0.15 * 20 MW = -3.0 MW.
Nueva potencia en horas pico: P_nuevo = 20 - 3 = 17.0 MW (se recortaron 3 MW de generación fósil peaker cara).""",
        "bloque_sugerido": "Pomodoro 50/10 • Redes inteligentes y arquitectura AMI",
        "slides": [
            {"numero": 1, "seccion": "SMART GRIDS", "titulo": "Arquitectura Bidireccional", "puntos": ["Convergencia de flujos de potencia y telecomunicaciones digitales.", "Integración de prosumidores y recursos energéticos distribuidos (DER)."]},
            {"numero": 2, "seccion": "AMI & DR", "titulo": "Medición Avanzada y Flexibilidad", "puntos": ["Monitoreo horario con medidores inteligentes AMI.", "Aplanamiento de la curva de carga reduciendo el factor PAR."]}
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Generación Distribuida (GD), AGPE y Marco Regulatorio CREG",
        "objetivo": "Aplicar la Ley 1715 de 2014 y la Resolución CREG 174 de 2021 para proyectos de autogeneración solar.",
        "concepto_clave_latex": r"\text{AGPE} \le 1\,\text{MW} \quad ; \quad \text{Facturación: } E_{\text{fact}} = E_{\text{importada}} - E_{\text{exportada}} \cdot \text{Crédito}",
        "ejemplo": """CLASE MAGISTRAL: MARCO REGULATORIO DE LA GENERACIÓN DISTRIBUIDA EN COLOMBIA
1. Ley 1715 de 2014 y Ley 2099 de 2021:
Promueven el desarrollo de Fuentes No Convencionales de Energía Renovable (FNCER) en Colombia mediante incentivos tributarios: deducción especial de renta (50% de la inversión), exclusión de IVA, exención de aranceles y depreciación acelerada de activos.
2. Resolución CREG 174 de 2021:
Regula la Autogeneración a Pequeña Escala (AGPE <= 1 MW) y la Generación Distribuida (GD <= 1 MW). Los autogeneradores con capacidad instalada hasta 100 kW no pagan cargos de respaldo y los excedentes se reconocen al costo de comercialización del componente de generación horario.
3. Problema Resuelto 1 (Aplicación Directa):
Un usuario comercial en Santa Marta instala un sistema AGPE solar de 80 kWp sin entrega de excedentes (inyección cero). Su consumo mensual promedio era de 12,000 kWh a una tarifa de 850 COP/kWh. Si el sistema solar genera 9,600 kWh/mes y todo se autoconsume en el sitio, calcule el ahorro mensual en COP y el ahorro anual.
Solución:
Ahorro mensual = 9,600 kWh * 850 COP/kWh = 8,160,000 COP/mes.
Ahorro anual = 8,160,000 COP * 12 meses = 97,920,000 COP/año.
Nueva factura con la red: (12,000 - 9,600) * 850 = 2,400 * 850 = 2,040,000 COP/mes.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un autogenerador residencial (AGPE <= 100 kW) consume 450 kWh en el mes e inyecta a la red 250 kWh de excedentes en horas del día. Si el costo unitario de compra es CU = 800 COP/kWh y los primeros excedentes hasta el nivel de consumo se valoran al costo de compra (1 a 1), calcule el valor a pagar en la factura de energía.
Solución:
Bajo la resolución CREG 174, los excedentes inyectados que compensen el consumo mensual se descuentan 1 a 1 de la energía activa importada:
Energía neta facturable: E_neta = E_consumida - E_excedentes
E_neta = 450 kWh - 250 kWh = 200 kWh.
Facturación neta de energía: Valor = 200 kWh * 800 COP/kWh = 160,000 COP.
(El usuario redujo su factura de 360,000 COP a 160,000 COP aprovechando el balance neto horario).""",
        "bloque_sugerido": "Taller 50 min • Modelado regulatorio AGPE bajo CREG 174",
        "slides": [
            {"numero": 1, "seccion": "LEYES", "titulo": "Ley 1715 de 2014 e Incentivos", "puntos": ["Beneficios tributarios: deducción de renta del 50%, cero IVA y aranceles.", "Impulso estatal a las FNCER en todo el territorio nacional."]},
            {"numero": 2, "seccion": "REGULACIÓN", "titulo": "Resolución CREG 174 de 2021", "puntos": ["Régimen de AGPE <= 100 kW y 100 kW < AGPE <= 1 MW.", "Mecanismo de venta de excedentes e intercambio neto con el comercializador."]}
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Movilidad Eléctrica y Almacenamiento en Baterías para Transporte",
        "objetivo": "Evaluar la eficiencia pozo-a-rueda de vehículos eléctricos frente a combustión y dimensionar cargadores EVSE.",
        "concepto_clave_latex": r"\text{Consumo}_{\text{VE}} \left[\frac{\text{kWh}}{100\,\text{km}}\right] \quad ; \quad t_{\text{carga}} = \frac{E_{\text{bat}} \cdot (\text{SoC}_f - \text{SoC}_i)}{P_{\text{EVSE}} \cdot \eta_{\text{carga}}}",
        "ejemplo": """CLASE MAGISTRAL: ELECTRIFICACIÓN DEL TRANSPORTE
1. Comparación de Eficiencia Pozo-a-Rueda (Well-to-Wheel):
Un motor de combustión interna (MCI) desperdicia el 70-80% de la energía del combustible como calor en el escape y radiador (eficiencia mecánica 20-30%). Un vehículo eléctrico (VE) convierte más del 85-90% de la energía eléctrica de la batería en movimiento en las ruedas.
2. Química de Baterías e Infraestructura EVSE:
- Baterías: Litio-Ferrofosfato (LFP) y Níquel-Manganeso-Cobalto (NMC) con densidades de 160 - 280 Wh/kg.
- Cargadores: Modo 2 (AC monofásico 3.7 kW), Modo 3 (AC trifásico 11-22 kW) y Modo 4 (DC Fast Charging 50 - 350 kW).
3. Problema Resuelto 1 (Aplicación Directa):
Un vehículo eléctrico con batería de 64 kWh tiene un consumo específico de 16 kWh/100 km. Calcule su autonomía máxima con el 100% de carga y el costo por kilómetro recorrido comparado con un vehículo de gasolina que rinde 40 km/galón (1 galón = 15,000 COP; tarifa eléctrica = 800 COP/kWh).
Solución:
1. Autonomía: Distancia = (64 kWh / 16 kWh) * 100 km = 400 km.
2. Costo VE por km: (16 kWh / 100 km) * 800 COP/kWh = 128 COP/km.
3. Costo Gasolina por km: 15,000 COP / 40 km = 375 COP/km.
Ahorro operativo directo: (375 - 128) / 375 = 65.87% de reducción en costo de combustible.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Se desea cargar la batería del vehículo anterior (64 kWh) del 20% al 80% de SoC en una estación rápida DC (Modo 4) con eficiencia del cargador eta = 92%. Si se dispone de una ventana máxima de tiempo de 30 minutos (0.5 horas), determine la potencia mínima que debe suministrar el cargador EVSE.
Solución:
Energía requerida por la batería:
delta_E = E_bat * (SoC_f - SoC_i) = 64 kWh * (0.80 - 0.20) = 64 * 0.60 = 38.4 kWh.
Energía que debe entregar el cargador:
E_suministrada = delta_E / eta = 38.4 / 0.92 = 41.739 kWh.
Potencia promedio requerida:
P_EVSE = E_suministrada / t = 41.739 kWh / 0.5 h = 83.48 kW.
Se requiere un cargador rápido comercial de al menos 90 kW o 100 kW de potencia DC.""",
        "bloque_sugerido": "Laboratorio 50 min • Dimensionamiento de estaciones de carga EVSE",
        "slides": [
            {"numero": 1, "seccion": "TRANSPORTE", "titulo": "Eficiencia Pozo-a-Rueda", "puntos": ["Superación del 85% de eficiencia en tren motriz eléctrico frente a 25% MCI.", "Frenado regenerativo para recuperación de energía cinética en desaceleración."]},
            {"numero": 2, "seccion": "INFRAESTRUCTURA", "titulo": "Carga Rápida DC y Baterías", "puntos": ["Modos de carga AC y estaciones ultra rápidas Modo 4 hasta 350 kW.", "Curva de carga de batería CC-CV y desaceleración por encima del 80% SoC."]}
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Cadena de Valor del Hidrógeno Verde y Electrólisis",
        "objetivo": "Modelar la termodinámica de la electrólisis del agua y calcular el consumo eléctrico por kg de H2.",
        "concepto_clave_latex": r"2\text{H}_2\text{O} + E_{\text{elec}} \to 2\text{H}_2 + \text{O}_2 \quad ; \quad \text{Consumo} \approx 50\text{ a }55\,\frac{\text{kWh}}{\text{kg H}_2}",
        "ejemplo": """CLASE MAGISTRAL: ECONOMÍA DEL HIDRÓGENO Y ELECTROLIZADORES
1. Clasificación por Colores del Hidrógeno:
- Gris: Reformado de gas natural con vapor (SMR), emite 9-11 kg CO2 por kg H2.
- Azul: SMR acoplado a captura y almacenamiento de carbono (CCUS).
- Verde: Electrólisis del agua impulsada exclusivamente por energías renovables (cero emisiones).
2. Tecnologías de Electrolizadores:
- Alcalino (AEL): Electrolito KOH líquido, tecnología madura y de bajo costo de capital.
- Membrana de Intercambio Protónico (PEM): Respuesta dinámica en segundos, ideal para fuentes renovables variables (solar y eólica).
- Óxido Sólido (SOEC): Alta temperatura (700-800 °C), máxima eficiencia termodinámica.
3. Problema Resuelto 1 (Aplicación Directa):
El Poder Calorífico Inferior del hidrógeno molecular es PCI_H2 = 120 MJ/kg (33.33 kWh/kg). Un electrolizador PEM comercial requiere 52 kWh de electricidad para producir 1 kg de H2 a 30 bar. Calcule la eficiencia del electrolizador respecto al PCI.
Solución:
Eficiencia = E_quimica / E_electrica
Eficiencia = (33.33 kWh/kg) / (52.00 kWh/kg) = 0.6410 (64.10%).
El 35.9% restante de la energía eléctrica se disipa como calor de bajo nivel en el agua de refrigeración.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un parque eólico de 50 MW en La Guajira opera a potencia nominal durante 8 horas nocturnas donde la demanda es baja y la red no puede recibir la energía. Si esa energía excedente se desvía íntegramente a una planta de electrólisis con consumo de 50 kWh/kg de H2, calcule la masa de hidrógeno verde producida en toneladas y el volumen que ocupa a condiciones normales (densidad rho_H2_cn = 0.0899 kg/Nm^3).
Solución:
Energía total disponible: E = 50 MW * 8 h = 400 MWh = 400,000 kWh.
Masa de hidrógeno producida:
m_H2 = 400,000 kWh / (50 kWh/kg) = 8,000 kg = 8.0 toneladas de H2 verde.
Volumen en condiciones normales:
V_Nm3 = 8,000 kg / (0.0899 kg/Nm^3) = 88,987.76 Nm^3 de H2.
Se almacena a alta presión (350 o 700 bar) para transporte en isotanques o inyección en gasoductos.""",
        "bloque_sugerido": "Laboratorio 50 min • Eficiencia de electrólisis y balances de masa",
        "slides": [
            {"numero": 1, "seccion": "H2 VERDE", "titulo": "Vector Energético y Colores", "puntos": ["Descarbonización de sectores difíciles de abatir (acero, química, transporte pesado).", "PCI de 120 MJ/kg: triple de densidad energética gravimétrica frente a gasolina."]},
            {"numero": 2, "seccion": "ELECTRÓLISIS", "titulo": "Tecnologías AEL y PEM", "puntos": ["Consumo técnico entre 50 y 55 kWh por kilogramo de hidrógeno.", "Acoplamiento directo con parques solares y eólicos de gran escala."]}
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Pilas de Combustible (Fuel Cells) y Conversión Electroquímica",
        "objetivo": "Calcular la tensión reversible de Nernst y modelar las sobretensiones de activación, óhmica y concentración.",
        "concepto_clave_latex": r"E_{\text{rev}} = -\frac{\Delta G}{n F} \approx 1.229\text{ V} \quad ; \quad V_{\text{celda}} = E_{\text{rev}} - \eta_{\text{act}} - \eta_{\text{ohm}} - \eta_{\text{conc}}",
        "ejemplo": """CLASE MAGISTRAL: PILAS DE COMBUSTIBLE ELECTROQUÍMICAS
1. Principio Electroquímico Inverso a la Electrólisis:
Una pila de combustible combina hidrógeno en el ánodo y oxígeno en el cátodo para generar directamente electricidad DC y agua sin combustión, evitando el límite térmico de Carnot:
- Ánodo: H_2 -> 2H^+ + 2e^-
- Cátodo: (1/2) O_2 + 2H^+ + 2e^- -> H_2O
2. Curva de Polarización y Pérdidas de Tensión:
A circuito abierto, el potencial termodinámico teórico a 25 °C es E_rev = -Delta G / (n F) = 237.2 kJ / (2 * 96485 C) = 1.229 V. Con corriente, la tensión cae por:
- Sobrepotencial de activación (cinética electroquímica en electrodos).
- Pérdidas óhmicas (resistencia iónica de la membrana y electrónica).
- Pérdidas de concentración (transporte de masa a altas densidades de corriente).
3. Problema Resuelto 1 (Aplicación Directa):
Un stack de pilas de combustible PEM opera a una tensión por celda de V_celda = 0.70 V con densidad de corriente nominal. Si el stack consta de 120 celdas en serie y entrega una corriente I = 200 A, calcule la potencia eléctrica generada y la eficiencia eléctrica de la celda respecto al PCS (E_termoneutra = 1.482 V).
Solución:
Tensión total del stack: V_stack = 120 celdas * 0.70 V = 84.0 V.
Potencia eléctrica neta: P_elec = 84.0 V * 200 A = 16,800 W = 16.8 kW.
Eficiencia eléctrica celular:
eta = V_celda / E_termoneutra = 0.70 V / 1.482 V = 0.4723 (47.23%).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un autobús de transporte público eléctrico funciona con un motor de 150 kW accionado por una celda de combustible PEM que opera con eficiencia del 50% (consume 66.66 kWh de H2 por cada 33.33 kWh eléctricos generados). Determine el flujo másico de hidrógeno consumido en kg/h cuando el vehículo opera a velocidad de crucero demandando 60 kW de potencia continua.
Solución:
Potencia eléctrica requerida: P_elec = 60 kW.
Potencia química requerida en H2 (al 50% de eficiencia):
P_quimica = P_elec / eta = 60 kW / 0.50 = 120 kWt.
Dado que el PCI del hidrógeno es 33.33 kWh/kg:
Flujo de consumo: m_dot_H2 = P_quimica / PCI = 120 kW / (33.33 kWh/kg) = 3.60 kg de H2 por hora.
Con un tanque estándar a 350 bar de 35 kg de H2, el autobús tiene una autonomía de crucero de: 35 / 3.6 = 9.72 horas continuas.""",
        "bloque_sugerido": "Laboratorio 50 min • Curva de polarización de celdas de combustible",
        "slides": [
            {"numero": 1, "seccion": "ELECTROQUÍMICA", "titulo": "Pila PEM y Tensión de Nernst", "puntos": ["Reacción electroquímica directa sin ciclo térmico de Carnot.", "Tensión reversible termodinámica de 1.229 V a 25 °C."]},
            {"numero": 2, "seccion": "POLARIZACIÓN", "titulo": "Curva de Voltaje vs Corriente", "puntos": ["Pérdidas de activación, óhmicas y de transferencia de masa.", "Eficiencia eléctrica del stack entre 50% y 60%."]}
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Zonas No Interconectadas (ZNI) y Microrredes Híbridas",
        "objetivo": "Diseñar microrredes híbridas diésel-solar-batería para comunidades rurales y optimizar el LCOE.",
        "concepto_clave_latex": r"\text{LCOE} = \frac{\sum_{t=0}^N \frac{\text{CAPEX}_t + \text{OPEX}_t}{(1 + r)^t}}{\sum_{t=1}^N \frac{E_t}{(1 + r)^t}} \quad ; \quad f_{\text{renov}} = \frac{E_{\text{PV}}}{E_{\text{carga}}}",
        "ejemplo": """CLASE MAGISTRAL: ELECTRIFICACIÓN RURAL Y MICRORREDES EN ZNI
1. El Reto Energético en Zonas No Interconectadas (ZNI):
El 52% del territorio colombiano (Amazonía, Orinoquía, costas pacífica y caribeña aislada) pertenece a las ZNI, caracterizadas por dependencia total de plantas diésel caras, contaminantes y con servicio de pocas horas al día.
2. Arquitectura de Microrredes Híbridas (HRES):
Integran paneles fotovoltaicos, banco de baterías BESS y generador diésel como respaldo, operando con inversores formadores de red (Grid-Forming Inverters) que establecen la referencia de voltaje y frecuencia.
3. Problema Resuelto 1 (Aplicación Directa):
Una comunidad rural aislada en el departamento del Magdalena demanda 120 kWh/día. Actualmente opera con un generador diésel que rinde 3.0 kWh por litro de diésel a un costo de combustible puesto en sitio de 4,500 COP/litro. Calcule el gasto anual exclusivamente en combustible diésel.
Solución:
Litros diarios: 120 kWh/día / (3.0 kWh/litro) = 40 litros/día.
Gasto diario: 40 litros * 4,500 COP = 180,000 COP/día.
Gasto anual en combustible: 180,000 COP/día * 365 días = 65,700,000 COP/año.
(En 10 años gasta 657 millones de COP sólo en combustible fósil, justificando con creces la inversión en solar + baterías).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Se diseña un sistema solar fotovoltaico con acumulación BESS para cubrir el 80% de la demanda de la comunidad anterior (fracción renovable f_renov = 0.80). La inversión inicial es CAPEX = 120 millones de COP, vida útil de 20 años y costos de mantenimiento anual OPEX = 2 millones de COP. Calcule el Costo Nivelado de la Energía (LCOE) en COP/kWh considerando una tasa de descuento r = 8% anual y compare con el costo del kWh diésel (~1,500 COP/kWh).
Solución:
Energía anual generada: E_anual = 120 kWh/día * 365 = 43,800 kWh/año.
Factor de anualidad para r = 8% y N = 20 años:
CRF = [ r * (1 + r)^N ] / [ (1 + r)^N - 1 ] = [ 0.08 * (1.08)^20 ] / [ (1.08)^20 - 1 ] = 0.3728 / 3.6609 = 0.10185.
Costo anual de capital: CAPEX * CRF = 120,000,000 * 0.10185 = 12,222,000 COP/año.
Costo total anual: 12,222,000 + 2,000,000 (OPEX) = 14,222,000 COP/año.
LCOE_solar = 14,222,000 COP / 43,800 kWh = 324.70 COP/kWh.
El LCOE solar (325 COP/kWh) es 4.6 veces más barato que el costo diésel (1500 COP/kWh), demostrando la viabilidad económica rotunda de la transición energética en ZNI.""",
        "bloque_sugerido": "Taller 50 min • Simulación de microrredes híbridas y cálculo LCOE",
        "slides": [
            {"numero": 1, "seccion": "ZNI", "titulo": "Desafío Energético Territorial", "puntos": ["52% del territorio colombiano sin acceso al SIN.", "Sustitución de diésel subsidiado por microrredes renovables autónomas."]},
            {"numero": 2, "seccion": "LCOE", "titulo": "Costo Nivelado de la Energía", "puntos": ["Fórmula de LCOE integrando CAPEX, OPEX y tasa de descuento.", "Reducción de más del 70% del costo del kWh frente a generación fósil."]}
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Mercado de Energía Mayorista (MEM) y Cargo por Confiabilidad",
        "objetivo": "Comprender el despacho económico centralizado de XM, precio de bolsa y función del Cargo por Confiabilidad.",
        "concepto_clave_latex": r"\text{Despacho: } \min \sum_i C_i P_i \quad \text{s.a.} \quad \sum_i P_i = D \quad ; \quad \text{ENFICC} \ge D_{\text{crítica}}",
        "ejemplo": """CLASE MAGISTRAL: MERCADO ELÉCTRICO MAYORISTA EN COLOMBIA (MEM)
1. Estructura y Agentes del MEM:
Operado por XM como Operador del Sistema (CND) y Administrador del Sistema de Intercambios Comerciales (ASIC). Participan Generadores, Transmisores, Distribuidores y Comercializadores.
2. Formación del Precio de Bolsa y Mérito de Despacho:
Cada día los generadores envían sus ofertas de precio para las 24 horas siguientes. El CND ordena las plantas de menor a mayor costo de oferta hasta casar la demanda prevista más pérdidas. El precio marginal de la última planta requerida determina el Precio de Bolsa horario (mercado marginalista).
3. Problema Resuelto 1 (Aplicación Directa):
En una hora determinada la demanda del SIN es D = 8,000 MW. Se reciben las siguientes ofertas:
- Oferta 1 (Solar y Eólica): 1,500 MW a 0 COP/kWh.
- Oferta 2 (Hidroeléctricas filo y embalses): 5,000 MW a 120 COP/kWh.
- Oferta 3 (Térmicas gas ciclo combinado): 2,000 MW a 320 COP/kWh.
- Oferta 4 (Térmicas diésel peakers): 1,000 MW a 850 COP/kWh.
Determine qué plantas se despachan y el Precio de Bolsa de esa hora.
Solución:
Despacho acumulado por mérito económico:
1. Solar/Eólica: 1,500 MW (acumulado: 1,500 MW).
2. Hidráulica: 5,000 MW (acumulado: 6,500 MW). Faltan 1,500 MW para los 8,000 MW.
3. Térmicas Gas: Se despachan 1,500 MW de los 2,000 MW disponibles (acumulado: 8,000 MW, casó la demanda).
4. Térmicas Diésel: No se despachan (0 MW).
Precio Marginal (Precio de Bolsa): Determinado por la última planta despachada (gas), es decir, 320 COP/kWh para todos los generadores despachados en esa hora.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Explique el Cargo por Confiabilidad en Colombia y analice por qué las termoeléctricas reciben una remuneración fija mensual basada en su ENFICC (Energía Firme para el Cargo por Confiabilidad) incluso cuando no están generando durante periodos de lluvias abundantes.
Solución:
Dado que la matriz colombiana es >70% hidroeléctrica, en años húmedos el agua es abundante y el precio de bolsa cae a mínimos, haciendo inviable económicamente a las termoeléctricas si sólo cobraran por energía vendida.
Sin embargo, durante el Fenómeno de El Niño, las sequías vacían los embalses y el país colapsaría en apagones si las térmicas se hubiesen desmantelado por quiebra.
El Cargo por Confiabilidad actúa como una prima de seguro que los usuarios pagan de forma continua a las plantas que certifican ENFICC para asegurar disponibilidad operativa inmediata de encendido obligatorio (al Precio de Escasez) cuando el sistema lo requiera en sequías críticas.""",
        "bloque_sugerido": "Laboratorio 50 min • Simulación de subasta marginalista del MEM",
        "slides": [
            {"numero": 1, "seccion": "MEM", "titulo": "Operación y Mercado Marginalista", "puntos": ["Rol de XM como operador CND y administrador comercial ASIC.", "Orden de mérito y fijación del precio por la planta marginal."]},
            {"numero": 2, "seccion": "CONFIABILIDAD", "titulo": "ENFICC y Fenómeno de El Niño", "puntos": ["Seguro de firmeza ante sequías severas por variabilidad climática.", "Obligaciones de Energía Firme y Precio de Escasez regulado."]}
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Evaluación Financiera de Proyectos: VPN, TIR, Payback y WACC",
        "objetivo": "Evaluar la rentabilidad económica y bancabilidad de proyectos solares y de eficiencia energética.",
        "concepto_clave_latex": r"\text{VPN} = \sum_{t=1}^N \frac{F_t}{(1 + \text{WACC})^t} - I_0 \quad ; \quad \text{VPN}(\text{TIR}) = 0",
        "ejemplo": """CLASE MAGISTRAL: MODELACIÓN FINANCIERA EN INGENIERÍA ENERGÉTICA
1. Criterios de Decisión Financiera:
Un proyecto de ingeniería no sólo debe ser técnicamente viable, sino financieramente rentable para atraer capital de deuda bancaria e inversionistas de capital:
- Valor Presente Neto (VPN): Suma descontada de los flujos de caja netos futuros menos la inversión inicial I_0. Si VPN > 0, el proyecto crea valor.
- Tasa Interna de Retorno (TIR): Tasa de descuento que hace exactamente VPN = 0. Si TIR > WACC, el proyecto se aprueba.
- Periodo de Retorno de la Inversión (Payback Simple y Descontado): Tiempo requerido para recuperar el desembolso inicial.
2. Costo Promedio Ponderado del Capital (WACC):
Costo ponderado entre el costo de la deuda (bancos) y el costo del patrimonio (accionistas).
3. Problema Resuelto 1 (Aplicación Directa):
Una empresa industrial invierte I_0 = 100 millones de COP en un banco de condensadores y luminarias LED que generan un ahorro neto constante de F_t = 30 millones de COP anuales durante 5 años. Si el costo de capital de la empresa es WACC = 12% anual, calcule el VPN del proyecto.
Solución:
Factor de anualidad para N = 5 y r = 12%:
Factor = [ 1 - (1 + 0.12)^(-5) ] / 0.12 = [ 1 - 0.5674 ] / 0.12 = 0.4326 / 0.12 = 3.6048.
Valor presente de los ahorros:
VP_ahorros = 30,000,000 * 3.6048 = 108,144,000 COP.
VPN = VP_ahorros - I_0 = 108,144,000 - 100,000,000 = +8,144,000 COP.
Como VPN > 0 (+8.14 millones), el proyecto es económicamente viable y crea riqueza.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un parque solar de 1 MWp requiere una inversión I_0 = 3,500 millones de COP y genera flujos de caja libres netos de 700 millones de COP anuales durante 25 años. Calcule el periodo de recuperación simple (Payback) y determine la Tasa Interna de Retorno (TIR) analítica del proyecto.
Solución:
1. Payback Simple:
PB = Inversión / Flujo anual = 3,500 / 700 = exactamente 5.0 años.
2. Tasa Interna de Retorno (TIR):
Buscamos r tal que 700 * [ (1 - (1+r)^(-25)) / r ] = 3,500.
Dividiendo entre 700: [ (1 - (1+r)^(-25)) / r ] = 5.000.
Para N = 25 años y razón 5.0:
Probando r = 20%: Factor = [ 1 - (1.20)^(-25) ] / 0.20 = [ 1 - 0.0105 ] / 0.20 = 0.9895 / 0.20 = 4.947.
Probando r = 19.5%: Factor = [ 1 - (1.195)^(-25) ] / 0.195 = 5.068.
Interpolando: TIR approx 19.8% anual.
Dado que la TIR (19.8%) supera con creces el costo típico del crédito comercial (12-14%), el proyecto presenta alta rentabilidad y excelente bancabilidad.""",
        "bloque_sugerido": "Laboratorio 50 min • Flujos de caja y evaluación de proyectos solares",
        "slides": [
            {"numero": 1, "seccion": "FINANZAS", "titulo": "Métricas de Inversión VPN y TIR", "puntos": ["Valor del dinero en el tiempo y descuento de flujos de caja.", "Criterio de aprobación: VPN positivo y TIR superior al WACC."]},
            {"numero": 2, "seccion": "BANCABILIDAD", "titulo": "Payback y Estructuración", "puntos": ["Periodo de recuperación simple y descontado de la inversión.", "Estructuras de financiamiento Project Finance y PPA."]}
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Comunidades Energéticas y Democratización de la Energía",
        "objetivo": "Diseñar modelos asociativos de autogeneración comunitaria según la política de Transición Energética Justa.",
        "concepto_clave_latex": r"E_{\text{comunitaria}} = \sum_{k=1}^U E_k \quad ; \quad \text{Factor Cohesión: } \text{Beneficio Social} \ge \text{Costo Nivelado}",
        "ejemplo": """CLASE MAGISTRAL: COMUNIDADES ENERGÉTICAS EN COLOMBIA
1. Concepto de Comunidad Energética (Decreto 2236 de 2023):
Usuarios finales agrupados (familias, juntas de acción comunal, cooperativas, comunidades étnicas) que se asocian para generar, comercializar y usar energía limpia de forma descentralizada, convirtiéndose en sujetos activos de la política energética.
2. Modelos de Reparto de Excedentes y Gestión Colectiva:
La energía generada por un parque solar comunitario instalado en un tejado colectivo (colegio, polideportivo, terreno comunal) se asigna virtualmente mediante coeficientes de reparto a las facturas individuales de los socios participantes.
3. Problema Resuelto 1 (Aplicación Directa):
Una Comunidad Energética conformada por 50 familias de pescadores en Tasajera (Magdalena) instala un arreglo fotovoltaico comunitario de 60 kWp que genera 8,400 kWh mensuales. Si la energía se distribuye equitativamente entre las 50 familias, calcule el crédito de energía mensual para cada hogar y el ahorro asumiendo una tarifa de 800 COP/kWh.
Solución:
Asignación por familia: E_familia = 8,400 kWh / 50 familias = 168 kWh/familia/mes.
Ahorro económico por familia:
Ahorro = 168 kWh * 800 COP/kWh = 134,400 COP/familia/mes.
Para una familia vulnerable de estrato 1 con consumo típico de 150 kWh/mes, la comunidad cubre el 100% de su consumo básico, erradicando la pobreza energética en el territorio.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Una Comunidad Energética instala un microrred solar con almacenamiento que genera excedentes de 3,000 kWh/mes que no son consumidos por los hogares. Diseñe el mecanismo de gestión de excedentes bajo la regulación CREG para financiar un fondo comunitario de mantenimiento y reposición de baterías.
Solución:
1. Venta de Excedentes al Comercializador de Red:
Los 3,000 kWh se exportan al SIN y se liquidan al costo horario de generación promedio: P_gen = 350 COP/kWh.
Ingreso mensual del fondo: 3,000 kWh * 350 COP = 1,050,000 COP/mes.
Ingreso anual del fondo: 1,050,000 * 12 = 12,600,000 COP/año.
2. Sostenibilidad a Largo Plazo:
En un horizonte de 8 años (vida útil esperada del banco de baterías de litio), el fondo acumula: 12.6 * 8 = 100.8 millones de COP, garantizando la reposición completa de las baterías sin depender de subsidios externos y asegurando gobernanza comunitaria sustentable.""",
        "bloque_sugerido": "Taller 50 min • Diseño y estatutos de Comunidades Energéticas",
        "slides": [
            {"numero": 1, "seccion": "COMUNIDADES", "titulo": "Democratización Energética", "puntos": ["Decreto 2236 de 2023 y Transición Energética Justa.", "Tránsito de usuario pasivo a prosumidor colectivo organizado."]},
            {"numero": 2, "seccion": "SOSTENIBILIDAD", "titulo": "Fondos de Reposición y Equidad", "puntos": ["Asignación de créditos de energía mediante reparto proporcional.", "Creación de fondos comunales para autosuficiencia y mantenimiento."]}
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Prospectiva Energética 2050, Neutralidad de Carbono y el Rol del Ingeniero",
        "objetivo": "Sintetizar la visión del plan de descarbonización a 2050 y el rol profesional del Ingeniero Energético de Unimagdalena.",
        "concepto_clave_latex": r"\text{Net-Zero 2050: } \sum \text{Emisiones GEI} - \sum \text{Capturas} = 0 \quad ; \quad \text{CDIO: Concebir-Diseñar-Implementar-Operar}",
        "ejemplo": """CLASE MAGISTRAL: PROSPECTIVA 2050 Y EL PERFIL PROFESIONAL DEL INGENIERO
1. Rutas Globales hacia Net-Zero y Escenario NZE de la AIE:
El Acuerdo de París y la estrategia nacional Colombia 2050 exigen alcanzar la neutralidad climática a mediados de siglo. Esto implica triplicar la capacidad renovable global, duplicar la tasa de eficiencia energética y descarbonizar el transporte y la industria pesada mediante electrificación e hidrógeno.
2. El Ingeniero Energético de la Universidad del Magdalena:
Formado bajo el estándar internacional CDIO (Concebir, Diseñar, Implementar, Operar), el ingeniero energético de Unimagdalena es un líder técnico ético capacitado para liderar la transición energética en el Caribe y el mundo, integrando modelación matemática, tecnologías limpias de potencia, regulación y responsabilidad social territorial.
3. Problema Resuelto 1 (Aplicación Directa):
La matriz eléctrica colombiana emite anualmente en promedio 0.160 tCO2e/MWh generado (160 g CO2/kWh). Si para el año 2040 el país alcanza una generación 100% limpia mediante hidroelectricidad, solar, eólica marina y almacenamiento BESS en un volumen de 90,000 GWh anuales, calcule las emisiones directas anuales de GEI evitadas frente al factor de referencia actual.
Solución:
Factor de emisión evitado: FE = 160 tCO2e / GWh.
Emisiones evitadas anuales:
E_evitadas = 90,000 GWh * 160 tCO2e/GWh = 14,400,000 tCO2e/año = 14.4 millones de toneladas de CO2 equivalente evitadas anualmente.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Analice cómo el marco CDIO (Concebir, Diseñar, Implementar, Operar) se aplica al ciclo de vida de un proyecto de granja solar flotante de 10 MWp en la Ciénaga Grande de Santa Marta.
Solución:
1. Concebir: Identificar el recurso solar, reducción de evaporación de agua, permisos ambientales y concertación previa con comunidades ribereñas.
2. Diseñar: Dimensionar cadenas de paneles sobre flotadores HDPE, anclajes hidrodinámicos, inversores string, cálculo de pérdidas térmicas con refrigeración pasiva del agua y simulación en PVSyst.
3. Implementar: Construcción de subestación elevadora, cableado sumergible apantallado, pruebas de aislamiento dieléctrico y energización bajo normas RETIE.
4. Operar: Monitoreo SCADA en tiempo real con algoritmos de IA predictiva, limpieza periódica y planes de desmantelamiento y reciclaje de materiales al final de la vida útil.""",
        "bloque_sugerido": "Mesa Redonda 50 min • Net-Zero 2050 y Manifiesto Ético CDIO",
        "slides": [
            {"numero": 1, "seccion": "PROSPECTIVA", "titulo": "Metas Net-Zero 2050", "puntos": ["Descarbonización profunda del sector eléctrico, transporte e industria.", "Integración de renovables no convencionales masivas y almacenamiento."]},
            {"numero": 2, "seccion": "PERFIL", "titulo": "Metodología CDIO y Liderazgo Ético", "puntos": ["Concebir, Diseñar, Implementar y Operar activos de energía del futuro.", "Impacto territorial sostenible en la región Caribe y Colombia."]}
        ]
    }
]

if __name__ == '__main__':
    target = '      - codigo: "01011801"'
    yaml_text = format_topics_yaml(topics_9_to_20 + topics_21_to_30)
    inject_topics_after(target, yaml_text)
    print("04011822 Introducción a la Ingeniería Energética now has 30 topics!")
