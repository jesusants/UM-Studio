# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after, format_topics_yaml

topics_03021815 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Circuitos Hidráulicos Regenerativos y Multiplicadores de Velocidad en Actuadores",
        "objetivo": "Diseñar circuitos regenerativos conectando la cámara del vástago a la cámara del émbolo para aumentar la velocidad de extensión del cilindro sin aumentar el caudal de bomba.",
        "concepto_clave_latex": r"v_{\text{ext,reg}} = \frac{Q_{\text{bomba}}}{A_r} = \frac{Q_{\text{bomba}}}{\frac{\pi}{4} d_r^2} \quad [\text{m/s}] \quad ; \quad F_{\text{ext,reg}} = P \cdot A_r = P \cdot \frac{\pi}{4} d_r^2 \quad [\text{N}]",
        "ejemplo": """Problema 1: Un cilindro hidráulico diferencial tiene un diámetro de émbolo D_p = 100 mm (área A_p = (pi/4)(0.10)^2 = 7.854 × 10⁻³ m² = 78.54 cm²) y un diámetro de vástago d_r = 70 mm (área del vástago A_r = (pi/4)(0.07)^2 = 3.848 × 10⁻³ m² = 38.48 cm²; área anular A_a = A_p - A_r = 40.06 cm²). La bomba suministra un caudal constante Q_b = 60 L/min (0.0010 m³/s = 1000 cm³/s) a una presión de tarado de la válvula de alivio P = 160 bar (16.0 MPa). Compare la velocidad y fuerza de extensión en modo convencional versus modo regenerativo.
Paso 1: Modo convencional (la cámara del vástago descarga al tanque a presión cero):
Velocidad de avance: v_conv = Q_b / A_p = (1000 cm³/s) / (78.54 cm²) = 12.73 cm/s = 0.1273 m/s.
Fuerza máxima disponible: F_conv = P × A_p = (16.0 × 10⁶ N/m²) × (7.854 × 10⁻³ m²) = 125,664 N = 125.66 kN.
Paso 2: Modo regenerativo (el aceite desplazado de la cámara anular se recircula a la cámara del émbolo):
Caudal efectivo entrante: Q_tot = Q_b + Q_anular = Q_b × (A_p / A_r).
Velocidad de avance regenerativo:
v_reg = Q_b / A_r = (1000 cm³/s) / (38.48 cm²) = 25.99 cm/s = 0.2599 m/s.
Paso 3: Fuerza máxima disponible en modo regenerativo:
F_reg = P × (A_p - A_a) = P × A_r = (16.0 × 10⁶ N/m²) × (3.848 × 10⁻³ m²) = 61,568 N = 61.57 kN.
Paso 4: El modo regenerativo multiplica la velocidad por v_reg / v_conv = 25.99 / 12.73 = 2.04 veces, a expensas de reducir la fuerza máxima en un 51% (ideal para carreras de aproximación rápida).

Problema 2: ¿Cuál debe ser la relación de áreas A_p / A_r para que la velocidad de extensión regenerativa sea exactamente igual a la velocidad de retroceso convencional?
Paso 1: Retroceso convencional: v_ret = Q_b / A_a = Q_b / (A_p - A_r).
Paso 2: Igualando v_reg = v_ret => Q_b / A_r = Q_b / (A_p - A_r) => A_r = A_p - A_r => A_p = 2 A_r.
Paso 3: El área del émbolo debe ser exactamente el doble del área del vástago (relación 2:1), requiriendo d_r = D_p / sqrt(2) ≈ 0.707 D_p.""",
        "bloque_sugerido": "Oleohidráulica Aplicada 35 min • Válvulas de secuencia y circuitos regenerativos automáticos"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Golpe de Ariete y Transitorios Hidráulicos: Ecuación de Joukowsky y Alivio de Presión",
        "objetivo": "Calcular la sobrepresión transitoria de golpe de ariete provocada por el cierre rápido de válvulas en tuberías forzadas de hidroeléctricas.",
        "concepto_clave_latex": r"\Delta P_{\text{ariete}} = \rho c_{\text{onda}} \Delta v \quad [\text{Pa}] \quad ; \quad c_{\text{onda}} = \sqrt{\frac{K / \rho}{1 + \left(\frac{K}{E}\right)\left(\frac{D}{e}\right)}} \quad ; \quad t_{\text{crítico}} = \frac{2 L}{c_{\text{onda}}} \quad [\text{s}]",
        "ejemplo": """Problema 1: Una tubería forzada de acero (módulo de Young E = 200 GPa = 2.0 × 10¹¹ Pa) de una central hidroeléctrica tiene diámetro D = 1.20 m, espesor de pared e = 12 mm (0.012 m) y longitud L = 800 m. Transporta agua (rho = 1,000 kg/m³, módulo de compresibilidad volumétrica K = 2.19 GPa = 2.19 × 10⁹ Pa) con velocidad inicial v_0 = 3.5 m/s. Una válvula esférica de turbina se cierra bruscamente en un tiempo t_c = 1.0 s. Calcule: a) La celeridad de la onda de presión c_onda; b) El tiempo crítico de maniobra t_crítico; c) La sobrepresión máxima de Joukowsky Delta P [bar]; d) La presión total máxima si la presión hidrostática estática previa era P_0 = 25 bar (2.5 MPa).
Paso 1: Celeridad de la onda elástica:
Factor de deformación elástica de la pared: (K / E)(D / e) = (2.19 × 10⁹ / 2.0 × 10¹¹) × (1.20 / 0.012) = (0.01095) × 100 = 1.095.
Denominador = 1 + 1.095 = 2.095.
c_onda = sqrt[(K / rho) / 2.095] = sqrt[(2.19 × 10⁶) / 2.095] = sqrt(1,045,346) = 1,022.4 m/s.
Paso 2: Tiempo crítico de ida y vuelta de la onda:
t_crítico = 2 L / c_onda = (2 × 800 m) / 1,022.4 m/s = 1,600 / 1,022.4 = 1.565 s.
Paso 3: Como el tiempo de cierre t_c = 1.0 s es menor que t_crítico = 1.565 s (t_c < t_crítico), el cierre es rápido (golpe de ariete directo total).
Paso 4: Sobrepresión de Joukowsky:
Delta P = rho c_onda Delta v = (1,000 kg/m³)(1,022.4 m/s)(3.5 m/s) = 3,578,400 Pa = 3.578 MPa = 35.78 bar.
Paso 5: Presión máxima absoluta en la válvula:
P_max = P_0 + Delta P = 25.0 bar + 35.78 bar = 60.78 bar (más de 6 MPa).
Paso 6: La presión se incrementa en un 143%, justificando la instalación obligatoria de una chimenea de equilibrio o válvula disipadora de alivio rápido.

Problema 2: ¿Cuál debe ser el tiempo mínimo de cierre lento t_c para que la sobrepresión no supere 10 bar (1.0 MPa)?
Paso 1: Por la aproximación de Michaud para cierre lento (t_c > t_crítico): Delta P_Michaud = 2 rho L v_0 / t_c.
Paso 2: t_c = 2 rho L v_0 / Delta P_perm = (2 × 1000 × 800 × 3.5) / 1.0 × 10⁶ = 5,600,000 / 1,000,000 = 5.60 segundos.""",
        "bloque_sugerido": "Transitorios Hidráulicos 40 min • Chimeneas de equilibrio y cámaras de aire antibloqueo en centrales hidroeléctricas"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Cavitación en Bombas y Válvulas: Criterio NPSH y Control de Daño por Erosión",
        "objetivo": "Calcular la Carga Neta Positiva de Succión disponible (NPSHa) para garantizar operación libre de cavitación en bombas hidráulicas.",
        "concepto_clave_latex": r"\text{NPSHa} = \frac{P_{\text{amb}} - P_{\text{sat}}(T)}{\rho g} + z_{\text{nivel}} - h_{f,\text{succión}} > \text{NPSHr} + \text{Margen} \quad [\text{m}] \quad ; \quad \sigma_c = \frac{\text{NPSH}}{H}",
        "ejemplo": """Problema 1: Una bomba centrífuga de alimentación de caldera bombea agua a T = 80 °C (densidad rho = 971.8 kg/m³, presión de saturación de vapor P_sat = 47.39 kPa = 47,390 Pa) desde un tanque desaireador abierto a la presión atmosférica P_amb = 101.3 kPa (101,300 Pa). La bomba está instalada a una elevación z_succión = 2.0 m por debajo del nivel libre del líquido en el tanque (succión positiva z = +2.0 m). La pérdida de carga en la línea de succión es h_f = 0.80 m. Si el fabricante exige un NPSHr = 3.2 m a caudal nominal, determine el NPSH disponible (NPSHa) y compruebe si la bomba cavitará. (g = 9.81 m/s²).
Paso 1: Presión atmosférica en metros de columna de agua:
h_amb = P_amb / (rho g) = 101,300 Pa / (971.8 kg/m³ × 9.81 m/s²) = 101,300 / 9,533.36 = 10.626 m.
Paso 2: Presión de vapor saturado en metros de columna de agua:
h_sat = P_sat / (rho g) = 47,390 Pa / 9,533.36 = 4.971 m.
Paso 3: Cálculo del NPSH disponible:
NPSHa = h_amb - h_sat + z_nivel - h_f = 10.626 m - 4.971 m + 2.000 m - 0.800 m = 6.855 m.
Paso 4: Comparación con NPSH requerido:
Margen = NPSHa - NPSHr = 6.855 m - 3.200 m = 3.655 m > 0.
Paso 5: Dado que NPSHa > NPSHr con un margen de seguridad superior a 3.6 m (el estándar API 610 exige margen >= 1.0 m), la bomba operará con total estabilidad y libre de cavitación.

Problema 2: ¿Qué ocurriría si la temperatura del agua subiera a 99 °C (P_sat = 97.77 kPa => h_sat = 10.256 m)?
Paso 1: NPSHa = 10.626 - 10.256 + 2.0 - 0.8 = 1.570 m.
Paso 2: Como NPSHa = 1.57 m < NPSHr = 3.2 m, la bomba entrará en cavitación violenta instantánea, sufriendo picadura erosiva de los álabes del impulsor y colapso de caudal.""",
        "bloque_sugerido": "Turbomaquinaria 35 min • Diagnóstico de vibración y acústica de cavitación según norma ISO 10816"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Válvulas Proporcionales y Servoválvulas Electrohidráulicas: Lazo Cerrado",
        "objetivo": "Modelar servoválvulas electrohidráulicas de dos etapas con retroalimentación mecánica y electrónica para control de posición submilimétrica.",
        "concepto_clave_latex": r"Q = C_d w x_v \sqrt{\frac{2}{\rho}\Delta P_v} \quad [\text{m}^3/\text{s}] \quad ; \quad \frac{X_v(s)}{I(s)} = \frac{K_{sv}}{\frac{s^2}{\omega_n^2} + \frac{2\zeta}{\omega_n}s + 1} \quad ; \quad \tau_{\text{resp}} \approx 5\text{ a }20\,\text{ms}",
        "ejemplo": """Problema 1: Una servoválvula hidráulica de cuatro vías y centro crítico tiene un ancho de lumbrera w = 25 mm (0.025 m), coeficiente de descarga C_d = 0.62 y densidad del aceite hidráulico rho = 870 kg/m³. Opera con una presión de suministro P_s = 210 bar (21.0 MPa) alimentando un cilindro que ejerce una fuerza de carga generando una caída de presión inducida en el actuador Delta P_L = 70 bar (7.0 MPa). La caída de presión en las lumbreras de la válvula es Delta P_v = (P_s - Delta P_L) / 2 = (210 - 70) / 2 = 70 bar = 7.0 × 10⁶ Pa. Calcule el caudal Q entregado al actuador cuando la corredera se desplaza un 40% de su carrera máxima (x_v = 0.40 × 1.0 mm = 0.40 mm = 4.0 × 10⁻⁴ m).
Paso 1: Gradiente de velocidad del flujo:
sqrt[(2 / rho) Delta P_v] = sqrt[(2 / 870 kg/m³) × (7.0 × 10⁶ N/m²)] = sqrt[14.0 × 10⁶ / 870] = sqrt(16,091.95) = 126.85 m/s.
Paso 2: Área de apertura de la lumbrera:
A_v = w × x_v = (0.025 m) × (4.0 × 10⁻⁴ m) = 1.0 × 10⁻⁵ m² = 0.10 cm².
Paso 3: Caudal másico/volumétrico:
Q = C_d A_v sqrt[(2 / rho) Delta P_v] = 0.62 × (1.0 × 10⁻⁵ m²) × 126.85 m/s = 7.865 × 10⁻⁴ m³/s.
Paso 4: Conversión a L/min:
Q = 7.865 × 10⁻⁴ m³/s × 60,000 L/(m³·min) = 47.19 L/min.

Problema 2: ¿A qué caída de presión de carga Delta P_L se maximiza la potencia hidráulica entregada P_hid = Delta P_L × Q al actuador?
Paso 1: P_hid = Delta P_L × k sqrt(P_s - Delta P_L).
Derivando e igualando a cero: d P_hid / d Delta P_L = k [ sqrt(P_s - Delta P_L) - Delta P_L / (2 sqrt(P_s - Delta P_L)) ] = 0.
Paso 2: 2 (P_s - Delta P_L) - Delta P_L = 0 => 2 P_s = 3 Delta P_L => Delta P_L = (2/3) P_s.
Paso 3: La máxima potencia útil se transmite cuando la caída en la carga es exactamente dos tercios de la presión del sistema (Delta P_L = 0.667 P_s), disipando el tercio restante en la servoválvula.""",
        "bloque_sugerido": "Control Electrohidráulico 40 min • Ajuste PID de lazo cerrado en posicionamiento de compuertas hidráulicas"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Hidráulica Proporcional con Control PWM y Compensación de Presión Hidromecánica",
        "objetivo": "Modelar el control de corriente por modulación de ancho de pulso (PWM) con señal dither y válvulas reguladoras de caudal compensadas por presión.",
        "concepto_clave_latex": r"I_{\text{prom}} = \frac{V_{\text{bus}}}{R_{\text{sol}}} \cdot \text{DutyCycle} \quad ; \quad f_{\text{dither}} \approx 100\text{ a }250\,\text{Hz} \quad ; \quad \Delta P_{\text{orificio}} = P_{\text{resorte}} = \text{const.} \implies Q = \text{const.}",
        "ejemplo": """Problema 1: El solenoide proporcional de una válvula direccional tiene una resistencia de bobina R = 12.0 Omega y una inductancia L = 80 mH. Se controla mediante una etapa de potencia PWM con tensión de alimentación continua V_bus = 24 V y frecuencia de conmutación f_pwm = 1,000 Hz. Calcule la corriente media que circula por el solenoide cuando el ciclo de trabajo es D = 65% (0.65), y determine la amplitud de pico a pico del rizado de corriente Delta I_pp [mA].
Paso 1: Corriente media en régimen continuo:
I_prom = (D × V_bus) / R = (0.65 × 24 V) / 12.0 Omega = 15.60 V / 12.0 Omega = 1.30 A (1,300 mA).
Paso 2: Periodo de conmutación T = 1 / f_pwm = 1 / 1000 = 0.001 s = 1.0 ms.
Tiempo de encendido t_on = D × T = 0.65 ms = 0.00065 s.
Tiempo de apagado t_off = (1 - D) × T = 0.35 ms = 0.00035 s.
Paso 3: Constante de tiempo eléctrica: tau = L / R = 0.080 H / 12.0 Omega = 0.00667 s = 6.67 ms.
Como T << tau (1.0 ms << 6.67 ms), la aproximación lineal del rizado es:
Delta I_pp ≈ (V_bus / L) × D (1 - D) T = (24 / 0.080) × (0.65)(0.35)(0.001 s) = 300 × 0.2275 × 0.001 = 0.06825 A = 68.25 mA.
Paso 4: El rizado representa apenas el 5.2% de la corriente media, garantizando posicionamiento suave de la corredera.

Problema 2: ¿Cuál es el propósito de superponer intencionalmente una señal senoidal de baja frecuencia (dither a 120 Hz) sobre la señal PWM?
Paso 1: Mantiene la corredera metálica en una micro-oscilación constante imperceptible que vence la fricción estática (stiction) y el histéresis magnético, asegurando respuesta rápida e hipersensible.""",
        "bloque_sugerido": "Electrónica de Potencia Fluídica 35 min • Tarjetas amplificadoras proporcionales y calibración de rampas"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Filtración y Control de Contaminación de Aceite Hidráulico: Código ISO 4406 y Ratio Beta",
        "objetivo": "Evaluar la limpieza del fluido de potencia según la norma ISO 4406 y seleccionar elementos filtrantes mediante el ratio de filtración Beta.",
        "concepto_clave_latex": r"\text{Código ISO: } X / Y / Z \quad (\ge 4\,\mu\text{m} \,/\, \ge 6\,\mu\text{m} \,/\, \ge 14\,\mu\text{m}) \quad ; \quad \beta_x = \frac{N_{\text{aguas arriba}}}{N_{\text{aguas abajo}}} \quad ; \quad \eta_x = \left(1 - \frac{1}{\beta_x}\right)\times 100\%",
        "ejemplo": """Problema 1: Una muestra de 100 mL de aceite hidráulico de un sistema de control de turbina de gas se analiza mediante contador óptico de partículas, arrojando el siguiente conteo por mililitro:
Partículas >= 4 micrometros: 14,500 partículas/mL
Partículas >= 6 micrometros: 2,800 partículas/mL
Partículas >= 14 micrometros: 95 partículas/mL
Determine el código de limpieza ISO 4406 de la muestra consultando la escala estándar (Rango 21: 10,000-20,000; Rango 19: 2,500-5,000; Rango 14: 80-160). Si la servoválvula exige una clase ISO 16/14/11, ¿es apto el fluido?
Paso 1: Asignación de rangos ISO:
Para >= 4 micrometros: 14,500 cae en rango 21 (10,000 a 20,000).
Para >= 6 micrometros: 2,800 cae en rango 19 (2,500 a 5,000).
Para >= 14 micrometros: 95 cae en rango 14 (80 a 160).
Código ISO resultante: 21/19/14.
Paso 2: Comparación con requerimiento del fabricante (16/14/11):
El aceite tiene 32 veces más partículas de 4 micras (21 vs 16) y 32 veces más de 6 micras (19 vs 14).
Paso 3: El fluido está críticamente contaminado y destruirá las aristas de control de la servoválvula por desgaste abrasivo si no se conecta una unidad de filtración móvil (dializador).

Problema 2: Un filtro de presión tiene una relación beta_10 = 200 (para partículas >= 10 micrometros). Calcule la eficiencia de retención eta_10 [%] y el número de partículas que escapan aguas abajo si aguas arriba inciden 500,000 partículas/mL.
Paso 1: Eficiencia eta_10 = (1 - 1 / beta_10) × 100% = (1 - 1 / 200) × 100% = (1 - 0.005) × 100% = 99.50%.
Paso 2: Partículas aguas abajo: N_down = N_up / beta_10 = 500,000 / 200 = 2,500 partículas/mL.""",
        "bloque_sugerido": "Tribología y Mantenimiento 35 min • Monitoreo de degradación de aditivos y barnices en aceites de turbina"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Termodinámica y Balance Térmico de Centrales Hidráulicas: Intercambiadores de Calor",
        "objetivo": "Calcular la potencia calorífica disipada por pérdidas volumétricas y mecánicas en centrales oleohidráulicas y dimensionar el enfriador.",
        "concepto_clave_latex": r"\dot{Q}_{\text{disipada}} = P_{\text{mec,bomba}} - P_{\text{hid,útil}} = P_{\text{bomba}}(1 - \eta_{\text{global}}) \quad [\text{kW}] \quad ; \quad A_{\text{enfriador}} = \frac{\dot{Q}_{\text{disipada}}}{U \cdot \text{LMTD}}",
        "ejemplo": """Problema 1: Una central hidráulica industrial es accionada por un motor eléctrico de P_in = 45 kW continuo. La eficiencia global del sistema hidráulico (bomba, válvulas de estrangulamiento y tuberías) es eta = 65% (0.65), de modo que el 35% de la potencia se degrada en calor absorbido por el aceite. La temperatura máxima permitida del depósito de aceite es T_aceite = 55 °C y el aire ambiente está a T_amb = 30 °C. Las pérdidas por disipación natural convectiva y radiante del tanque de acero (área superficial A_tanque = 4.0 m², coeficiente global de transferencia h_tanque = 12 W/(m²·K)) no son suficientes. Calcule la potencia calorífica residual que debe remover un intercambiador de calor de tubos y aletas dot{Q}_enfriador [kW].
Paso 1: Calor total generado en el sistema:
dot{Q}_gen = P_in × (1 - eta) = 45 kW × (1 - 0.65) = 45 × 0.35 = 15.75 kW.
Paso 2: Disipación natural del tanque:
dot{Q}_tanque = h_tanque × A_tanque × (T_aceite - T_amb) = 12 W/(m²·K) × 4.0 m² × (55 - 30 K) = 48 × 25 = 1,200 W = 1.20 kW.
Paso 3: Carga térmica neta del enfriador:
dot{Q}_enfriador = dot{Q}_gen - dot{Q}_tanque = 15.75 kW - 1.20 kW = 14.55 kW.

Problema 2: Si se utiliza un intercambiador de placas aceite-agua donde el agua entra a 20 °C y sale a 30 °C, y el aceite entra a 55 °C y sale a 45 °C en contracorriente pura, calcule la diferencia de temperatura media logarítmica (LMTD).
Paso 1: Delta T_1 = T_aceite,in - T_agua,out = 55 - 30 = 25 °C.
Delta T_2 = T_aceite,out - T_agua,in = 45 - 20 = 25 °C.
Paso 2: Como Delta T_1 = Delta T_2 = 25 °C, el flujo es en contracorriente equilibrada y LMTD = 25.0 °C exactamente.""",
        "bloque_sugerido": "Balances Térmicos 35 min • Dimensionamiento de enfriadores de aire forzado vs placas agua-aceite"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Fugas, Pérdidas de Carga y Optimización Energética en Redes de Aire Comprimido",
        "objetivo": "Cuantificar el costo energético y económico de las fugas de aire comprimido y dimensionar redes malladas con velocidad económica.",
        "concepto_clave_latex": r"\dot{V}_{\text{fuga}} = C_d A_{\text{orificio}} P_{\text{abs}} \sqrt{\frac{\gamma}{R T}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{\gamma-1}}} \quad ; \quad \text{Costo}_{\text{anual}} = \dot{W}_{\text{comp}} \cdot t_{\text{op}} \cdot \text{Tarifa}_{\text{kWh}}",
        "ejemplo": """Problema 1: En una auditoría energética a una planta industrial se detectan 20 fugas equivalentes a orificios circulares de diámetro d = 2.0 mm (área unitaria a = (pi/4)(0.002)^2 = 3.142 × 10⁻⁶ m²; área total A_tot = 6.284 × 10⁻⁵ m²) en la red de aire comprimido a una presión manométrica de 6.0 bar (P_abs = 7.0 bar = 700,000 Pa) a T = 293 K. Por flujo sónico bloqueado a través del orificio (C_d = 0.80, gamma = 1.40, R = 287 J/(kg·K)): a) Calcule el caudal másico total fugado dot{m} [kg/s] y el caudal volumétrico de aire libre equivalente (FAD) en Nm³/min; b) Si el compresor de tornillo consume 0.11 kW por cada Nm³/h producido y la planta opera 8,000 horas al año con una tarifa de 0.15 USD/kWh, calcule el costo económico anual de estas fugas.
Paso 1: Flujo crítico bloqueado por orificio:
Factor sónico del aire: sqrt[(gamma / R T) (2 / (gamma + 1))^((gamma+1)/(gamma-1))] = sqrt[(1.40 / (287 × 293)) × (2 / 2.40)^(2.4/0.4)] = sqrt[(1.40 / 84,091) × (0.8333)⁶] = sqrt[1.6649 × 10⁻⁵ × 0.3349] = sqrt(5.576 × 10⁻⁶) = 0.002361 s/m.
Paso 2: Caudal másico total:
dot{m} = C_d A_tot P_abs × 0.002361 = 0.80 × (6.284 × 10⁻⁵ m²) × (700,000 Pa) × 0.002361 = 0.08309 kg/s.
Paso 3: Caudal en condiciones normales (rho_norm = 1.293 kg/Nm³):
dot{V} = (0.08309 kg/s / 1.293 kg/Nm³) × 3,600 s/h = 231.33 Nm³/h = 3.856 Nm³/min.
Paso 4: Potencia eléctrica consumida continuamente por las fugas:
P_elec = 231.33 Nm³/h × 0.11 kW/(Nm³/h) = 25.45 kW.
Paso 5: Costo económico anual del desperdicio:
Costo = 25.45 kW × 8,000 h/año × 0.15 USD/kWh = 30,540 USD/año.
Paso 6: Reparar 20 pequeñas fugas de 2 mm ahorra más de 30,500 dólares anuales directos en la factura eléctrica.

Problema 2: ¿Cuál es la velocidad de flujo recomendada en tuberías principales de aire para limitar pérdidas de carga a menos de 0.1 bar?
Paso 1: Entre 6 m/s y 10 m/s en tuberías de distribución principal; nunca superar 15 m/s.""",
        "bloque_sugerido": "Eficiencia Neumática 35 min • Detección ultrasónica de fugas y optimización de presión de generación"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Tratamiento de Aire Comprimido: Separadores, Filtros Coalescentes y Secadores",
        "objetivo": "Dimensionar sistemas de secado frigorífico y de adsorción por regeneración para alcanzar clases de calidad de aire ISO 8573-1.",
        "concepto_clave_latex": r"\text{Punto de Rocío (PDP)}: T_{\text{rocío}} \le 3^\circ\text{C (Frigo)} \quad \text{o} \quad -40^\circ\text{C (Adsorción)} \quad ; \quad m_{\text{agua,cond}} = \dot{V}(x_{\text{in}} - x_{\text{out}})",
        "ejemplo": """Problema 1: Un compresor aspira V = 10 Nm³/min de aire húmedo a P_amb = 1 bar, T = 30 °C y humedad relativa phi = 80% (presión de vapor saturado P_sat(30°C) = 4.246 kPa). Lo comprime a P = 7 bar manométrico (8 bar absoluto) y lo enfría en el post-enfriador a T_post = 35 °C (P_sat(35°C) = 5.628 kPa). Calcule la masa de agua condensada y drenada por hora dot{m}_cond [kg/h].
Paso 1: Humedad absoluta de entrada a 30 °C:
Presión parcial de vapor: P_v1 = phi × P_sat = 0.80 × 4.246 kPa = 3.397 kPa.
Humedad específica x_1 = 0.622 × P_v1 / (P_amb - P_v1) = 0.622 × 3.397 / (100 - 3.397) = 2.113 / 96.603 = 0.02187 kg agua / kg aire seco.
Paso 2: Masa de aire seco por hora (rho_aire_seco ≈ 1.165 kg/m³ a 30 °C y 96.6 kPa):
dot{m}_aire = 10 m³/min × 60 min/h × 1.165 kg/m³ = 699 kg aire seco/h.
Agua total ingresada = 699 × 0.02187 = 15.29 kg agua/h.
Paso 3: Humedad saturada a la salida del post-enfriador a 8 bar abs y 35 °C:
P_v2 = P_sat(35°C) = 5.628 kPa.
x_2 = 0.622 × P_v2 / (P_tot - P_v2) = 0.622 × 5.628 / (800 - 5.628) = 3.501 / 794.37 = 0.00441 kg agua / kg aire seco.
Agua en estado de vapor a la salida = 699 × 0.00441 = 3.08 kg agua/h.
Paso 4: Masa de agua condensada líquida retirada por el separador ciclónico:
dot{m}_cond = 15.29 - 3.08 = 12.21 kg/h (más de 12 litros de agua condensada cada hora).

Problema 2: ¿Qué clase de pureza ISO 8573-1 se requiere para instrumentación neumática de control en subestaciones y qué secador se debe seleccionar?
Paso 1: Clase 1.2.1 (Punto de rocío a presión PDP <= -40 °C).
Paso 2: Exige un secador de adsorción de doble torre con alúmina activada o tamiz molecular regenerado térmicamente o por purga.""",
        "bloque_sugerido": "Calidad de Aire 35 min • Norma ISO 8573-1 y cálculo de condensados en tanques pulmón"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Diseño de Circuitos Neumáticos Secuenciales: Método Cascada",
        "objetivo": "Diseñar automatizaciones neumáticas puras libres de bloqueos por señales permanentes aplicando el método sistemático de cascada con líneas de presión.",
        "concepto_clave_latex": r"\text{Grupos: } G = \text{Número de particiones sin repetir letra} \quad ; \quad \text{Válvulas inversoras } 5/2 = G - 1",
        "ejemplo": """Problema 1: Se requiere automatizar una máquina transfer de alimentación de biomasa compuesta por dos cilindros de doble efecto A y B que ejecutan la secuencia: A+ B+ A- B-. Aplique el método cascada: a) Divida la secuencia en el número mínimo de grupos; b) Determine el número de válvulas inversoras 5/2 necesarias; c) Liste las señales de cambio de grupo y las señales internas de cada grupo.
Paso 1: Partición en grupos evitando repetir letras en un mismo grupo:
Grupo I:  (A+) (B+)   [no se repite ninguna letra]
Grupo II: (A-) (B-)   [no se repite ninguna letra]
Total de grupos G = 2.
Paso 2: Número de válvulas inversoras de línea:
Válvulas 5/2 biestables de memoria de grupo = G - 1 = 2 - 1 = 1 válvula inversora.
Paso 3: Señales de pilotaje:
- Al activar el pulsador de marcha START y estar el sistema en reposo (final de carrera b0 activo en Línea II): se pilota la válvula inversora a la posición I (habilita la Línea de presión I).
- La Línea I energiza directamente el pilotaje 14 de la válvula de A => avanza A (A+).
- Al llegar A a su final de carrera a1: la señal a1 alimentada desde Línea I pilota el avance de B (B+).
- Al llegar B a su final de carrera b1: pilota la válvula inversora a la posición II (habilita la Línea II y despresuriza Línea I).
- La Línea II energiza directamente el retorno de A (A-).
- Al llegar A al reposo a0: la señal a0 alimentada desde Línea II pilota el retorno de B (B-).
- Al alcanzar b0: la secuencia se completa y queda lista para el siguiente ciclo.

Problema 2: ¿Cuál es el límite práctico del método cascada y por qué se restringe a un máximo de G <= 4 grupos?
Paso 1: Porque las válvulas inversoras se conectan en serie (árbol de cascada). Para G > 4, la caída de presión acumulada a través de las correderas reduce el caudal de pilotaje, provocando conmutaciones lentas o erráticas.""",
        "bloque_sugerido": "Automatización Neumática 40 min • Diagramas espacio-fase y esquemas neumáticos en FluidSIM"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Método Paso a Paso (Paso a Paso Máximo y Anulado) en Lógica Secuencial Neumática",
        "objetivo": "Implementar secuencias complejas multiactuador mediante bloques secuenciadores paso a paso garantizando una única línea activa simultánea.",
        "concepto_clave_latex": r"\text{Módulos Paso a Paso} = \text{Número de Pasos } N \quad ; \quad \text{Línea } n \text{ activada por } (n-1) \text{ y desactivada por } (n+1)",
        "ejemplo": """Problema 1: Considere una secuencia de estampado y expulsión de 3 cilindros: A+ B+ C+ B- A- C-. Desarrolle la arquitectura por el método paso a paso estándar (Paso a Paso Máximo): a) Determine el número de pasos; b) Explique la condición de habilitación y deshabilitación de cada módulo.
Paso 1: Número de acciones = 6 pasos independientes:
Paso 1: A+
Paso 2: B+
Paso 3: C+
Paso 4: B-
Paso 5: A-
Paso 6: C-
Se requieren N = 6 módulos paso a paso (cada uno integrado por una válvula 3/2 normalmente cerrada, una válvula 3/2 de pilotaje de memoria y una función AND interna).
Paso 2: Cada paso 'k' se activa cuando:
1) El paso previo 'k-1' está presurizado;
2) El sensor de fin de carrera del movimiento 'k-1' emite señal neumática.
Paso 3: En el instante en que el paso 'k' conmuta a alta presión, envía una señal de pilotaje al paso 'k-1' para resetearlo inmediatamente a escape.
Paso 4: Ventaja frente a cascada: No hay límite en el número de pasos y la presión de trabajo se toma en paralelo del colector principal, sin pérdidas en serie.

Problema 2: ¿Cómo se garantiza que al energizar el circuito por primera vez el módulo del último paso (Paso 6) esté activo en reposo?
Paso 1: Mediante una válvula biestable de arranque inicial o un pulso de rearme (RESET) que presuriza la línea de preparación del último paso para habilitar el START.""",
        "bloque_sugerido": "Lógica Industrial 40 min • Comparación funcional entre Método Cascada y Paso a Paso Rápido"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Válvulas Lógicas Neumáticas Especiales: OR, AND, Escape Rápido y Temporizadores",
        "objetivo": "Integrar funciones booleanas neumáticas combinando válvulas selectoras (OR), válvulas de simultaneidad (AND) y escapes rápidos para alta velocidad.",
        "concepto_clave_latex": r"\text{OR: } P = A \vee B \quad [\text{Selectora}] \quad ; \quad \text{AND: } P = A \wedge B \quad [\text{Simultaneidad}] \quad ; \quad \tau = R_{\text{estrang}} \cdot C_{\text{cámara}}",
        "ejemplo": """Problema 1: En una prensa neumática de seguridad por mando bimanual: El avance del cilindro solo debe ocurrir si el operador presiona simultáneamente dos pulsadores manuales distanciados (P_1 y P_2). Además, para acelerar la carrera de retorno, se instala una válvula de escape rápido en la cámara del émbolo. Formule el circuito neumático y describa su funcionamiento.
Paso 1: Función de seguridad bimanual:
Los dos pulsadores P_1 y P_2 se conectan a las dos entradas de una válvula de simultaneidad (función lógica AND). Solo cuando ambos pulsadores se activan dentro de un intervalo menor a 0.5 s, la corredera móvil de la válvula AND se equilibra en el centro y envía aire de pilotaje a la válvula distribuidora 5/2. Si se activa un solo pulsador, la presión desplaza la corredera bloqueando su propia salida.
Paso 2: Válvula de escape rápido en el retorno:
La válvula de escape rápido se rosca directamente en la lumbrera frontal de la cámara del émbolo. Durante el retroceso, el aire que es desalojado no viaja a través de la tubería ni de la válvula distribuidora, sino que se evacúa de inmediato a la atmósfera por la tobera silenciada del escape rápido.
Paso 3: Esto reduce la contrapresión a casi cero, incrementando la velocidad de retroceso en más del 250%.

Problema 2: Un temporizador neumático normalmente cerrado (retardo a la conexión) consta de una válvula estranguladora unidireccional, un acumulador de volumen V = 50 cm³ y una válvula 3/2 pilotada con resorte de tarado P_res = 3.0 bar. Si la presión de alimentación es P_0 = 6.0 bar y la resistencia de estrangulamiento equivale a R = 1.2 × 10⁸ Pa·s/m³, calcule el tiempo de retardo tau.
Paso 1: Carga de presión en el acumulador: P(t) = P_0 [1 - exp(-t / (R C_v))].
Paso 2: Disparo en P(tau) = 3.0 bar => 3.0 / 6.0 = 0.50 = 1 - exp(-tau / T_c) => exp(-tau / T_c) = 0.50 => tau = T_c ln(2) = 0.6931 T_c.
Paso 3: Con T_c = R C_v ≈ 4.0 s: tau = 0.6931 × 4.0 s = 2.77 segundos.""",
        "bloque_sugerido": "Lógica Neumática Pura 35 min • Circuitos de seguridad bimanual según norma EN 574"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Sensores en Actuadores Fluídicos: Reed Switches, Inductivos y Presostatos",
        "objetivo": "Seleccionar y conectar sensores de posición magnéticos de estado sólido (GMR), detectores de fin de carrera y presostatos para retroalimentación a PLC.",
        "concepto_clave_latex": r"V_{\text{out}} = \begin{cases} V_{\text{alim}} & \text{si } B > B_{\text{umbral}} \\ 0 & \text{si } B \le B_{\text{umbral}} \end{cases} \quad ; \quad \text{Presostato: } P_{\text{set}} \pm \Delta P_{\text{histéresis}}",
        "ejemplo": """Problema 1: Un cilindro neumático incorpora un imán permanente anular en su émbolo. Para detectar la posición de final de carrera se compara un sensor magnético tipo Reed switch electromecánico versus un sensor magneto-resistivo gigante (GMR) de estado sólido (PNP):
a) Si la frecuencia de ciclado de la máquina es f = 2.0 Hz durante 16 horas/día y 300 días/año, calcule los ciclos anuales que soporta el sensor;
b) Sabiendo que el Reed switch tiene una vida útil media mecánica de 10 millones de ciclos y el sensor GMR es electrónico sin partes móviles (> 100 millones de ciclos), determine el tiempo medio hasta la falla de ambos sensores.
Paso 1: Ciclos anuales de operación:
Ciclos/año = 2.0 ciclos/s × 3,600 s/h × 16 h/día × 300 días/año = 2.0 × 17,280,000 = 34,560,000 ciclos/año (34.56 millones).
Paso 2: Vida útil del Reed switch:
t_falla,Reed = 10,000,000 / 34,560,000 = 0.289 años = 3.47 meses.
El contacto mecánico rebotará y sufrirá microsoldaduras por arco en menos de 4 meses de producción continua.
Paso 3: Vida útil del sensor GMR:
Supera con holgura los 3 años de servicio continuo libre de mantenimiento, haciendo mandatorio el uso de tecnología de estado sólido en líneas de alta cadencia.

Problema 2: Un presostato electromecánico monitorea la presión de un acumulador hidráulico para arrancar la bomba a P_on = 140 bar y apagarla a P_off = 180 bar. Calcule el punto de consigna (setpoint) y la banda de histéresis requerida.
Paso 1: Setpoint superior = 180 bar.
Paso 2: Histéresis Delta P = P_off - P_on = 180 - 140 = 40 bar. La histéresis previene el encendido y apagado oscilatorio de alta frecuencia del contactor del motor.""",
        "bloque_sugerido": "Sensores Industriales 30 min • Conexión NPN vs PNP de detectores y ajuste de presostatos digitales"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Hidráulica Móvil: Sistemas Load Sensing (LS) y Bombas con Compensador de Presión",
        "objetivo": "Modelar el funcionamiento de bombas de pistones axiales de caudal variable con compensador Load Sensing para minimizar pérdidas térmicas por estrangulamiento.",
        "concepto_clave_latex": r"P_{\text{bomba}} = P_{\text{carga,max}} + \Delta P_{\text{margen}} \quad ; \quad \Delta P_{\text{margen}} \approx 15\text{ a }25\,\text{bar} \quad ; \quad \text{Ahorro: } \Delta W = (P_{\text{alivio}} - P_{\text{bomba}}) Q",
        "ejemplo": """Problema 1: Una grúa hidráulica de elevación opera con una carga que requiere una presión de actuador P_carga = 80 bar consumiendo un caudal Q = 40 L/min (0.000667 m³/s). Compare la potencia disipada en calor entre: a) Un sistema de centro abierto convencional con bomba de caudal fijo de Q_bomba = 100 L/min y válvula de alivio tarada a P_max = 210 bar; b) Un sistema Load Sensing (LS) con bomba de pistones de caudal variable que ajusta su carrera para entregar exactamente 40 L/min con un margen LS Delta P_margen = 20 bar (P_bomba = 80 + 20 = 100 bar).
Paso 1: Sistema convencional con bomba fija:
La bomba genera 100 L/min a la presión de alivio de 210 bar:
Potencia consumida por la bomba: P_in = P_max × Q_bomba = (21.0 × 10⁶ Pa) × (100 / 60,000 m³/s) = 21.0 × 10⁶ × 0.001667 = 35.0 kW.
Potencia útil entregada a la carga: P_util = P_carga × Q_carga = (8.0 × 10⁶ Pa) × (40 / 60,000 m³/s) = 8.0 × 10⁶ × 0.000667 = 5.33 kW.
Potencia desperdiciada disipada como calor en el aceite:
P_perdida = P_in - P_util = 35.0 kW - 5.33 kW = 29.67 kW (el 85% de la energía se convierte en calor inútil).
Paso 2: Sistema Load Sensing (LS):
La bomba ajusta su ángulo de plato inclinable entregando exactamente Q = 40 L/min a P_bomba = 100 bar:
Potencia consumida por la bomba LS:
P_in,LS = P_bomba × Q = (10.0 × 10⁶ Pa) × (40 / 60,000 m³/s) = 10.0 × 10⁶ × 0.000667 = 6.67 kW.
Potencia útil entregada: P_util = 5.33 kW.
Potencia disipada en calor en la válvula proporcional:
P_perdida,LS = Delta P_margen × Q = (2.0 × 10⁶ Pa) × (0.000667 m³/s) = 1.33 kW.
Paso 3: Ahorro energético:
Ahorro de potencia = 35.0 kW - 6.67 kW = 28.33 kW (reducción del 81% en consumo de combustible diésel).

Problema 2: ¿Cómo detecta la bomba Load Sensing la presión de carga P_carga en sistemas con múltiples actuadores operando simultáneamente?
Paso 1: Mediante una red de válvulas selectoras de lanzadera (shuttle valves) que compara en cascada todas las presiones de carga y retroalimenta únicamente la mayor de ellas a la válvula compensadora de la bomba.""",
        "bloque_sugerido": "Maquinaria Móvil 40 min • Bombas de plato inclinable Rexroth A10VSO con control DFR/DRG"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Transmisiones Hidrostáticas (HST) en Lazo Cerrado y Generación Eólica Hidráulica",
        "objetivo": "Calcular relaciones de velocidad, par motor y rendimientos volumétrico y mecánico en transmisiones hidrostáticas compuestas por bomba y motor hidráulico.",
        "concepto_clave_latex": r"N_{\text{motor}} = N_{\text{bomba}} \frac{V_{d,\text{bomba}}}{V_{d,\text{motor}}} \eta_{\text{vol,global}} \quad ; \quad T_{\text{motor}} = \frac{\Delta P \cdot V_{d,\text{motor}}}{2\pi} \eta_{\text{mec,motor}} \quad ; \quad \eta_{\text{HST}} = \eta_{\text{bomba}} \cdot \eta_{\text{motor}}",
        "ejemplo": """Problema 1: Una transmisión hidrostática en lazo cerrado conecta un motor diésel que gira a N_bomba = 1,800 rpm con una bomba de pistones axiales de desplazamiento variable V_d,bomba = 125 cm³/rev. La bomba alimenta un motor hidráulico de pistones de desplazamiento fijo V_d,motor = 250 cm³/rev que acciona el tambor de tracción de una máquina de tendido de cables eléctricos. La presión diferencial de trabajo es Delta P = 280 bar (28.0 MPa). Los rendimientos son: eta_vol,bomba = 0.96, eta_mec,bomba = 0.94; eta_vol,motor = 0.95, eta_mec,motor = 0.93. Calcule: a) El caudal real entregado por la bomba Q_real [L/min]; b) La velocidad de giro real del motor hidráulico N_motor [rpm]; c) El par mecánico real entregado por el motor T_motor [N·m]; d) La eficiencia global de la transmisión eta_HST.
Paso 1: Caudal real de la bomba:
Q_real = N_bomba × V_d,bomba × eta_vol,bomba = (1,800 rev/min) × (0.125 L/rev) × 0.96 = 225 × 0.96 = 216.0 L/min (0.0036 m³/s).
Paso 2: Velocidad de rotación del motor hidráulico:
N_motor = (Q_real × eta_vol,motor) / V_d,motor = (216.0 L/min × 0.95) / (0.250 L/rev) = 205.2 / 0.250 = 820.8 rpm.
Paso 3: Par mecánico del motor hidráulico:
T_motor = [(Delta P × V_d,motor) / (2 pi)] × eta_mec,motor
Delta P = 28.0 × 10⁶ N/m²; V_d,motor = 250 × 10⁻⁶ m³/rev.
T_teorico = (28.0 × 10⁶ × 250 × 10⁻⁶) / (2 pi) = 7,000 / 6.2832 = 1,114.08 N·m.
T_motor = 1,114.08 N·m × 0.93 = 1,036.1 N·m.
Paso 4: Potencia mecánica entregada por el motor:
P_out = T_motor × omega_motor = 1,036.1 N·m × (820.8 × 2 pi / 60 rad/s) = 1,036.1 × 85.95 = 89,053 W = 89.05 kW.
Paso 5: Potencia mecánica consumida por la bomba:
P_in = [(Delta P × Q_teorico) / (eta_mec,bomba)] = [(28.0 × 10⁶ × 0.00375) / 0.94] = 105,000 / 0.94 = 111,702 W = 111.7 kW.
Paso 6: Eficiencia global de la transmisión hidrostática:
eta_HST = P_out / P_in = 89.05 kW / 111.7 kW = 0.7972 (79.72%).

Problema 2: ¿Qué función cumple la bomba de carga o sobrealimentación (charge pump) en este lazo cerrado?
Paso 1: Mantiene una presión positiva mínima (15 a 25 bar) en la línea de retorno de baja presión para prevenir cavitación en los pistones de la bomba principal y repone las fugas internas de drenaje continuo.""",
        "bloque_sugerido": "Transmisiones de Potencia 40 min • Concepto de transmisión hidrostática aplicada a aerogeneradores sin caja reductora"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Sistemas Hidráulicos de Pitch y Freno de Emergencia en Aerogeneradores",
        "objetivo": "Diseñar el sistema electrohidráulico de regulación del ángulo de paso de pala (pitch) y frenado mecánico por resortes precomprimidos (falla segura).",
        "concepto_clave_latex": r"\dot{\theta}_{\text{pitch}} = \frac{Q_{\text{acum}}}{A_{\text{cilindro}}} \cdot \text{Brazo} \ge 8^\circ/\text{s} \quad ; \quad F_{\text{freno}} = k_{\text{resorte}} \cdot \Delta x_{\text{precomprimido}} \quad [\text{Fail-Safe}]",
        "ejemplo": """Problema 1: En un aerogenerador marino de 6 MW, el sistema de pitch electrohidráulico de cada pala cuenta con un actuador de radio de manivela r = 1.2 m accionado por un cilindro de área A = 0.015 m². En una condición de desconexión de emergencia de la red (loss of grid), la pala debe pasar de posición de trabajo (theta = 0°) a bandera completa (theta = 90°) en un tiempo t_seguridad <= 10.0 segundos (velocidad angular media de pitch dot{theta} = 9°/s = 0.1571 rad/s). La carrera total del cilindro para 90° es S = 1.05 m. Calcule el volumen de aceite útil que debe suministrar el banco de acumuladores de pistón presurizados con nitrógeno por pala V_util [L] y el caudal medio de descarga requerido Q_descarga [L/min].
Paso 1: Volumen de aceite desplazado por la carrera:
V_cilindro = A × S = (0.015 m²) × (1.05 m) = 0.01575 m³ = 15.75 litros por pala.
Paso 2: Con un factor de seguridad del 25% para compensar compresibilidad y fugas de válvula:
V_util = 15.75 L × 1.25 = 19.69 L ≈ 20.0 Litros por pala.
Paso 3: Caudal medio requerido durante el frenado aerodinámico de emergencia:
Q_descarga = V_util / t_seguridad = 19.69 L / 10.0 s = 1.969 L/s = 1.969 × 60 L/min = 118.1 L/min.
Paso 4: Una válvula proporcional o cartucho de gran caudal comandada por baterías de respaldo de 24 Vdc debe asegurar 120 L/min sin depender de la bomba principal.

Problema 2: ¿Por qué la pinza de freno mecánico del rotor opera bajo el principio 'Fail-Safe' (seguridad positiva)?
Paso 1: La fuerza de frenado la ejercen potentes paquetes de resortes Belleville mecánicos precomprimidos.
Paso 2: La presión hidráulica se utiliza exclusivamente para abrir el freno. Ante cualquier pérdida de presión eléctrica o hidráulica, los resortes aplican de inmediato el freno mecánico sobre el disco sin requerir energía externa.""",
        "bloque_sugerido": "Sistemas Eólicos 40 min • Acumuladores de nitrógeno vejiga y pistón para maniobra de pitch de emergencia"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Sistemas Hidráulicos de Regulación y Gobierno en Turbinas Hidroeléctricas",
        "objetivo": "Modelar el servomotor hidráulico de accionamiento de los álabes directrices (Wicket Gates) en turbinas Francis y agujas de inyectores Pelton.",
        "concepto_clave_latex": r"F_{\text{servomotor}} = P_{\text{hid}} \cdot A_{\text{émbolo}} \ge F_{\text{hidrodinámica}} + F_{\text{fricción}} \quad ; \quad T_{\text{cierre}} = \frac{V_{\text{carrera}}}{Q_{\text{válvula rápida}}} \approx 4\text{ a }8\,\text{s}",
        "ejemplo": """Problema 1: Una turbina Francis de 40 MW en una central hidroeléctrica regula su admisión de agua mediante un anillo distribuidor gobernado por dos servomotores hidráulicos simétricos de doble efecto. La fuerza total máxima hidrodinámica y de fricción que opone el conjunto de álabes directrices durante un rechazo brusco de carga es F_tot = 600 kN (300 kN por servomotor). La presión nominal del aceite de regulación suministrado por el acumulador hidroneumático es P = 64 bar (6.4 MPa). Con un factor de seguridad de diseño del 30% (F_diseño = 300 kN × 1.30 = 390 kN por cilindro), calcule el diámetro de émbolo requerido D_p [mm] de cada servomotor.
Paso 1: Área mínima de émbolo requerida:
A_p = F_diseño / P = 390,000 N / (6.4 × 10⁶ N/m²) = 0.0609375 m² = 609.38 cm².
Paso 2: Diámetro de émbolo:
D_p = sqrt(4 A_p / pi) = sqrt(4 × 0.0609375 / pi) = sqrt(0.077588) = 0.2785 m = 278.5 mm.
Paso 3: Se normaliza a diámetro comercial D_p = 280 mm (área real A_p = 615.75 cm² => fuerza real = 394 kN por servomotor).
Paso 4: Para una carrera total S = 450 mm (0.45 m), el volumen de aceite por servomotor es V = 615.75 cm² × 45 cm = 27,708 cm³ = 27.7 L.

Problema 2: Si el tiempo de cierre de emergencia del distribuidor debe ser T_cierre = 5.0 segundos para evitar sobrevelocidad destructiva del alternador, calcule el caudal medio que debe evacuar la válvula de gobierno rápida por servomotor.
Paso 1: Q = V / T_cierre = 27.7 L / 5.0 s = 5.54 L/s.
Paso 2: En L/min: Q = 5.54 L/s × 60 = 332.4 L/min por servomotor.""",
        "bloque_sugerido": "Regulación Hidroeléctrica 40 min • Gobernador de velocidad electrohidráulico PID y servomotores de distribuidor"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Almacenamiento de Energía por Aire Comprimido (CAES): Termodinámica y Cavernas",
        "objetivo": "Calcular la densidad volumétrica de almacenamiento energético y el rendimiento de ida y vuelta en sistemas CAES isotérmicos y adiabáticos (A-CAES).",
        "concepto_clave_latex": r"W_{\text{iso}} = P_{\text{max}} V \ln\left(\frac{P_{\text{max}}}{P_{\text{min}}}\right) \quad ; \quad \eta_{\text{A-CAES}} = \frac{W_{\text{expansión}}}{W_{\text{compresión}}} \approx 65\text{ a }72\% \quad ; \quad \text{TES: Almacenamiento Térmico}",
        "ejemplo": """Problema 1: Un sistema de almacenamiento de energía por aire comprimido adiabático (A-CAES) almacena aire en una caverna salina subterránea de volumen V = 100,000 m³ entre una presión mínima de operación P_min = 40 bar (4.0 MPa) y una presión máxima de P_max = 75 bar (7.5 MPa) a temperatura media estabilizada T = 310 K (36.85 °C). (R = 287 J/(kg·K)). Calcule: a) La masa de aire útil inyectada Delta m [toneladas]; b) La energía mecánica teórica almacenable en proceso isotérmico W_iso en megavatios-hora [MWh].
Paso 1: Masa de aire a presión máxima:
m_max = (P_max V) / (R T) = (7.5 × 10⁶ Pa × 100,000 m³) / (287 J/(kg·K) × 310 K) = 7.5 × 10¹¹ / 88,970 = 8,429,808 kg = 8,429.8 t.
Paso 2: Masa de aire a presión mínima:
m_min = (P_min V) / (R T) = (4.0 × 10⁶ Pa × 100,000 m³) / 88,970 = 4.0 × 10¹¹ / 88,970 = 4,495,897 kg = 4,495.9 t.
Paso 3: Masa útil de aire ciclada:
Delta m = 8,429.8 - 4,495.9 = 3,933.9 toneladas de aire.
Paso 4: Trabajo de expansión isotérmica ideal del inventario de aire útil:
W_iso = Delta m R T ln(P_max / P_min) = (3,933,911 kg)(287 J/(kg·K))(310 K) ln(75 / 40)
= (3.4999 × 10¹¹ J) × ln(1.875) = (3.4999 × 10¹¹ J) × 0.6286 = 2.200 × 10¹¹ Joules.
Paso 5: Conversión a megavatios-hora (1 MWh = 3.6 × 10⁹ J):
W_iso = 2.200 × 10¹¹ J / (3.6 × 10⁹ J/MWh) = 61.11 MWh de energía mecánica pura.

Problema 2: En la tecnología A-CAES (adiabática avanzada), ¿qué componente clave se añade para eliminar el consumo de gas natural de las plantas CAES convencionales (como Huntorf o McIntosh)?
Paso 1: Un sistema de almacenamiento térmico de alta temperatura (TES, Thermal Energy Storage con lecho de roca o sales fundidas) que almacena el calor de compresión a más de 550 °C durante la carga y lo devuelve al aire antes de la turbina durante la descarga, logrando eficiencias superiores al 70% sin emisiones directas.""",
        "bloque_sugerido": "Almacenamiento a Gran Escala 40 min • Geomecánica de cavernas de sal y termodinámica de ciclos A-CAES"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Generación de Vacío Neumático: Eyectores Venturi, Ventosas y Robótica Solar",
        "objetivo": "Calcular la fuerza de sujeción de ventosas de vacío y dimensionar eyectores neumáticos basados en el efecto Venturi para líneas de ensamblaje fotovoltaico.",
        "concepto_clave_latex": r"F_{\text{sujeción}} = A_{\text{ventosa}} \cdot \Delta P_{\text{vacío}} \cdot \frac{1}{S} \quad [\text{N}] \quad ; \quad \Delta P_{\text{vacío}} = P_{\text{amb}} - P_{\text{vacío}} \quad ; \quad q_{\text{eyector}} = \mu_{\text{vacío}} q_{\text{motriz}}",
        "ejemplo": """Problema 1: Un robot cartesiano manipula paneles solares de vidrio de masa m = 24 kg y dimensiones 2.0 m × 1.0 m en una línea de laminación. La aceleración máxima horizontal durante el traslado rápido es a = 4.0 m/s² (aceleración vertical por gravedad g = 9.81 m/s²). Se emplean 4 ventosas circulares de silicona idénticas con nivel de vacío del 70% (presión absoluta P_vac = 30 kPa => Delta P_vac = 70 kPa = 70,000 Pa). El coeficiente de fricción estática entre ventosa y vidrio limpio es mu = 0.50. Con un factor de seguridad normativo S = 2.0 para manipulación dinámica acelerada, calcule el diámetro mínimo d_v [mm] de cada una de las 4 ventosas.
Paso 1: Fuerzas que actúan sobre la carga total:
Fuerza gravitatoria normal: F_g = m g = 24 kg × 9.81 m/s² = 235.44 N.
Fuerza inercial lateral cortante: F_in = m a = 24 kg × 4.0 m/s² = 96.0 N.
Paso 2: Condición de no deslizamiento lateral por fricción:
Fuerza normal total requerida por las ventosas:
F_norm >= (F_in / mu) × S = (96.0 / 0.50) × 2.0 = 192.0 × 2.0 = 384.0 N.
Condición de no desprendimiento vertical:
F_norm >= F_g × S = 235.44 × 2.0 = 470.88 N (condición más exigente).
Paso 3: Fuerza normal que debe aportar cada una de las 4 ventosas:
F_v = 470.88 N / 4 = 117.72 N por ventosa.
Paso 4: Área requerida por ventosa:
A_v = F_v / Delta P_vac = 117.72 N / 70,000 Pa = 1.6817 × 10⁻³ m² = 16.82 cm².
Paso 5: Diámetro de la ventosa:
d_v = sqrt(4 A_v / pi) = sqrt(4 × 1.6817 × 10⁻³ / pi) = sqrt(0.002141) = 0.04627 m = 46.3 mm.
Se seleccionan ventosas comerciales estándar de diámetro d = 50 mm (área = 19.63 cm² => F_segura = 137 N/ventosa).

Problema 2: ¿Cómo funciona un eyector neumático multietapa Venturi frente a una bomba de vacío de paletas rotativas?
Paso 1: El eyector utiliza aire comprimido motriz a través de toberas supersónicas sucesivas para arrastrar el aire de la cámara por efecto Venturi, logrando vacío en milisegundos sin partes móviles, motor eléctrico ni aceite.""",
        "bloque_sugerido": "Manipulación Automatizada 35 min • Eyectores con control de soplado de expulsión rápida (blow-off)"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Seguridad Funcional en Circuitos Hidráulicos y Neumáticos (ISO 13849 y EN 62061)",
        "objetivo": "Diseñar esquemas de parada de emergencia y control de energía peligrosa alcanzando Niveles de Rendimiento PL d / PL e según norma ISO 13849.",
        "concepto_clave_latex": r"\text{PL: } a \to e \quad ; \quad \text{MTTF}_d = \frac{B_{10d}}{0.1 \cdot n_{\text{op}}} \quad ; \quad \text{DC}_{\text{avg}} = \frac{\sum \frac{\text{DC}_i}{\text{MTTF}_{di}}}{\sum \frac{1}{\text{MTTF}_{di}}} \ge 90\% \quad [\text{Categoría 3/4}]",
        "ejemplo": """Problema 1: En una celda robotizada de corte de lingotes de silicio, una prensa neumática representa un peligro de aplastamiento crítico que exige Nivel de Rendimiento PL d (Categoría 3: redundancia y diagnóstico). El circuito de corte utiliza dos válvulas neumáticas 3/2 normalmente cerradas conectadas en serie con monitoreo de posición por sensores de proximidad inductivos (cobertura de diagnóstico DC = 99%). Cada válvula tiene una durabilidad de vida B_10d = 20 millones de ciclos (2 × 10⁷ ciclos). La máquina opera n_op = 1,000,000 ciclos/año. Calcule el tiempo medio hasta la falla peligrosa MTTF_d de cada canal y verifique si se alcanza el rango 'Alto' (MTTF_d >= 30 años) según ISO 13849-1.
Paso 1: Estimación de MTTF_d por canal:
MTTF_d = B_10d / (0.10 × n_op) = (20,000,000) / (0.10 × 1,000,000) = 20,000,000 / 100,000 = 200 años.
Paso 2: Como el estándar trunca el valor máximo a 100 años (rango Alto: 30 a 100 años), el canal califica como MTTF_d = Alto (100 años).
Paso 3: Con arquitectura de Categoría 3 (dos canales redundantes independientes), DC_avg = 99% (Alto) y MTTF_d = Alto:
La tabla de ISO 13849-1 asigna directamente un Performance Level PL e / PL d con probabilidad de falla peligrosa por hora PFH_d < 10⁻⁷ h⁻¹.
Paso 4: El diseño satisface con creces el requerimiento de seguridad industrial.

Problema 2: ¿Qué función cumple la válvula de seguridad de escape de dos canales con monitorización dinámica de corredera cruzada?
Paso 1: Si una de las dos correderas se traba mecánicamente en posición abierta por impurezas, la otra corredera drena el aire a escape e inhabilita eléctricamente el rearme del relé de seguridad hasta que se resuelva la falla.""",
        "bloque_sugerido": "Seguridad de Máquinas 40 min • Arquitecturas de seguridad hidráulica con válvulas redundantes monitoreadas"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Mantenimiento Predictivo, Monitoreo de Condición y Termografía en Oleohidráulica",
        "objetivo": "Diseñar programas de mantenimiento predictivo basados en firmas de presión acústica, espectros de vibración en bombas y termografía infrarroja.",
        "concepto_clave_latex": r"\Delta T = T_{\text{componente}} - T_{\text{referencia}} \quad ; \quad \text{RMS}_{\text{vib}} = \sqrt{\frac{1}{N}\sum_{i=1}^N x_i^2} \quad ; \quad \text{ISO 10816: Criterios de Severidad}",
        "ejemplo": """Problema 1: Durante una inspección termográfica en una central hidráulica se detecta una válvula limitadora de presión de alivio con una temperatura superficial focalizada T_valvula = 82.0 °C, mientras que la tubería de suministro adyacente se encuentra a T_linea = 46.0 °C (gradiente Delta T = +36.0 °C). La bomba entrega un caudal constante Q = 80 L/min a P = 200 bar. Sabiendo que el sistema debería estar en reposo de alivio (la válvula no debería estar aliviando): a) Interprete la causa raíz física del sobrecalentamiento focalizado; b) Calcule la potencia calorífica parásita generada si el 15% del caudal de bomba está fugando continuamente a través del asiento desgastado de la válvula hacia el tanque.
Paso 1: Diagnóstico termográfico:
Un gradiente Delta T > 20 °C en una válvula de alivio que debería estar cerrada indica fuga interna severa por erosión o fatiga del resorte de asiento (la caída de presión P convierte energía hidráulica directamente en calor por efecto Joule-Thomson).
Paso 2: Caudal fugado: Q_fuga = 0.15 × 80 L/min = 12.0 L/min = 0.00020 m³/s.
Paso 3: Potencia calorífica generada por estrangulamiento:
dot{Q}_fuga = Delta P × Q_fuga = (20.0 × 10⁶ N/m²) × (0.00020 m³/s) = 4,000 W = 4.0 kW.
Paso 4: Esta fuga inyecta continuamente 4.0 kW de calor al depósito y desperdicia energía eléctrica a razón de 4.0 kW × 8,760 h = 35,040 kWh anuales.

Problema 2: En el análisis de vibraciones de una bomba de pistones axiales de 9 émbolos que gira a 1,800 rpm (f_rot = 30 Hz), ¿a qué frecuencias características se manifiestan el fallo de pistones y el paso de émbolos?
Paso 1: Frecuencia de paso de pistones (Piston Pass Frequency, PPF):
PPF = 9 × f_rot = 9 × 30 Hz = 270 Hz y sus armónicos (540 Hz, 810 Hz).
Paso 2: Un incremento repentino en la amplitud de 270 Hz indica desgaste o rotura inminente de la zapata de uno de los pistones sobre el plato oscilante.""",
        "bloque_sugerido": "Mantenimiento 4.0 35 min • Sensores IoT de presión dinámica de alta frecuencia y análisis de degradación"
    }
]

if __name__ == '__main__':
    yaml_text = format_topics_yaml(topics_03021815)
    inject_topics_after('      - codigo: "01021804"', yaml_text)
    print("03021815 Fundamentos de Hidráulica y Neumática now has 30 topics!")
