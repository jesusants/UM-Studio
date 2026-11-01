# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06011840 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Circuitos Magnéticos y Leyes Fundamentales: Ley de Ampère, Faraday y Curvas B-H",
        "objetivo": "Calcular la fuerza magnetomotriz, reluctancia magnética, flujo y pérdidas por histéresis y corrientes parásitas (Foucault) en núcleos ferromagnéticos de máquinas eléctricas.",
        "concepto_clave_latex": r"\mathcal{F} = N I = \Phi \mathcal{R} \quad ; \quad \mathcal{R} = \frac{l}{\mu A} \quad ; \quad P_{\text{núcleo}} = k_h f B_{max}^n + k_e f^2 B_{max}^2 t^2",
        "ejemplo": "Problema 1: Un circuito magnético simétrico en forma de C con entrehierro de aire (g = 2.5 mm) se fabrica con láminas de acero al silicio M-19 de espesor t = 0.35 mm (longitud media del núcleo de hierro l_fe = 0.85 m, área de sección transversal del núcleo A_c = 0.006 m^2 = 60 cm^2, factor de apilamiento k_st = 0.95, de modo que el área de hierro efectiva es A_fe = 0.006 * 0.95 = 0.0057 m^2). Para considerar el efecto de abombamiento del flujo en el entrehierro (fringing effect), el área efectiva del entrehierro se corrige sumando el entrehierro a cada lado: A_g = (sqrt(0.006) + 0.0025)^2 = (0.07746 + 0.0025)^2 = 0.0800^2 = 0.0064 m^2. Se requiere establecer una densidad de flujo magnético en el entrehierro de B_g = 1.20 Tesla. A este nivel de inducción, la curva B-H del acero al silicio arroja una permeabilidad relativa mu_r = 3200 (H_fe = B / mu = 1.20 / (3200 * 4 * pi * 10^-7) = 298.4 A*vueltas/m). Reluctancia del entrehierro: R_g = g / (mu_0 * A_g) = 0.0025 / (4 * pi * 10^-7 * 0.0064) = 0.0025 / (8.042 * 10^-9) = 310,849 A*vueltas/Weber. Reluctancia del núcleo de hierro: R_fe = l_fe / (mu_r * mu_0 * A_fe) = 0.85 / (3200 * 4 * pi * 10^-7 * 0.0057) = 0.85 / (2.292 * 10^-5) = 37,085 A*vueltas/Weber. Reluctancia total del circuito: R_total = R_g + R_fe = 310,849 + 37,085 = 347,934 A*v/Wb (el entrehierro de solo 2.5 mm concentra el 89.3% de la reluctancia total del circuito). Flujo magnético total: Phi = B_g * A_g = 1.20 * 0.0064 = 0.00768 Weber. Fuerza magnetomotriz total requerida (FMM): F = Phi * R_total = 0.00768 * 347,934 = 2672.1 A*vueltas. Si la bobina tiene N = 500 vueltas, la corriente de excitación necesaria es: I = F / N = 2672.1 / 500 = 5.344 A. Pérdidas en el núcleo a 60 Hz (densidad del acero rho = 7650 kg/m^3, masa m = 0.85 * 0.0057 * 7650 = 37.06 kg): con pérdidas específicas de 1.85 W/kg a 1.2 T y 60 Hz, las pérdidas de vacío son P_fe = 37.06 * 1.85 = 68.56 W. Problema 2: En núcleos toroidales de ferrita sin entrehierro sometidos a alta frecuencia (100 kHz en convertidores de inversores), las pérdidas por corrientes de Foucault dominan si no se fragmenta el material en polvos sinterizados de alta resistividad eléctrica.",
        "bloque_sugerido": "Electromagnetismo de Potencia 45 min • Reluctancia de entrehierro, curva B-H y pérdidas en el hierro",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES FUNDAMENTALES DE CIRCUITOS MAGNÉTICOS",
                "titulo": "Analogía entre Circuitos Eléctricos y Magnéticos",
                "puntos": [
                    "Fuerza Magnetomotriz F = N * I (análoga a la tensión o fem V en voltios).",
                    "Flujo magnético Phi (análogo a la corriente I en amperios); densidad de flujo B = Phi / A en Teslas.",
                    "Reluctancia magnética R = l / (mu * A) (análoga a la resistencia eléctrica R en ohmios).",
                    "Ley de Hopkinson: F = Phi * R (equivalente magnético exacto de la Ley de Ohm)."
                ]
            },
            {
                "numero": 2,
                "seccion": "SATURACIÓN Y PÉRDIDAS MAGNÉTICAS",
                "titulo": "Histéresis y Corrientes Parásitas (Foucault)",
                "puntos": [
                    "Saturación ferromagnética: Más allá de 1.5 - 1.8 T, la permeabilidad mu cae drásticamente requiriendo corrientes magnetizantes gigantescas.",
                    "Pérdidas por Histéresis: Proporcionales al área del ciclo B-H y a la frecuencia (Ecuación de Steinmetz k_h * f * B^n).",
                    "Pérdidas de Foucault (Eddy currents): Proporcionales al espesor al cuadrado (t^2); se minimizan laminando el núcleo en chapas aisladas con barniz Carlite."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Transformadores Monofásicos: Circuito Equivalente Exacto y Ensayos de Vacío/Cortocircuito",
        "objetivo": "Modelar el circuito equivalente exacto referido al primario/secundario de transformadores monofásicos y determinar sus parámetros a partir de los ensayos normalizados de vacío y cortocircuito.",
        "concepto_clave_latex": r"R_{eq1} = R_1 + a^2 R_2 \quad ; \quad X_{eq1} = X_1 + a^2 X_2 \quad ; \quad \eta = \frac{S \cos\theta}{S \cos\theta + P_{fe} + P_{cu}}",
        "ejemplo": "Problema 1: Un transformador monofásico de distribución de 50 kVA, 7200 / 240 V, 60 Hz se somete a ensayos de laboratorio normalizados: 1) Ensayo de Vacío (Open-Circuit Test realizado en el devanado de baja tensión con alta abierta): V_oc = 240 V, I_oc = 4.80 A, P_oc = 210 W. Relación de transformación nominal: a = 7200 / 240 = 30. Factor de potencia de vacío: cos(theta_oc) = P_oc / (V_oc * I_oc) = 210 / (240 * 4.80) = 210 / 1152 = 0.1823 (inductivo). Corriente de pérdidas en el hierro en BT: I_fe,BT = I_oc * cos(theta_oc) = 4.80 * 0.1823 = 0.875 A. Resistencia de magnetización en BT: R_c,BT = V_oc / I_fe,BT = 240 / 0.875 = 274.3 ohms. Corriente magnetizante pura: I_m,BT = I_oc * sin(theta_oc) = 4.80 * sqrt(1 - 0.1823^2) = 4.80 * 0.9832 = 4.719 A. Reactancia de magnetización en BT: X_m,BT = V_oc / I_m,BT = 240 / 4.719 = 50.86 ohms. Referidas al primario de alta tensión (multiplicando por a^2 = 900): R_c,1 = 274.3 * 900 = 246,870 ohms; X_m,1 = 50.86 * 900 = 45,774 ohms. 2) Ensayo de Cortocircuito (Short-Circuit Test realizado en alta tensión con baja cortocircuitada a corriente nominal I_1,nom = 50,000 / 7200 = 6.944 A): V_sc = 260 V, I_sc = 6.944 A, P_sc = 580 W. Impedancia equivalente de cortocircuito referida al primario: Z_eq1 = V_sc / I_sc = 260 / 6.944 = 37.44 ohms. Resistencia equivalente: R_eq1 = P_sc / (I_sc)^2 = 580 / (6.944)^2 = 580 / 48.22 = 12.03 ohms. Reactancia equivalente de dispersión: X_eq1 = sqrt(Z_eq1^2 - R_eq1^2) = sqrt(37.44^2 - 12.03^2) = sqrt(1401.75 - 144.72) = sqrt(1257.03) = 35.45 ohms. 3) Regulación de Tensión a plena carga con factor de potencia 0.8 inductivo: Delta_V = I_1 * (R_eq1 * cos(theta) + X_eq1 * sin(theta)) = 6.944 * (12.03 * 0.8 + 35.45 * 0.6) = 6.944 * (9.624 + 21.27) = 6.944 * 30.894 = 214.53 V. Regulación porcentual: VR% = (214.53 / 7200) * 100% = 2.98%. Eficiencia a plena carga: Potencia de salida P_out = 50,000 * 0.8 = 40,000 W. Pérdidas totales = P_oc + P_sc = 210 + 580 = 790 W. Eficiencia: eta = 40,000 / (40,000 + 790) = 40,000 / 40,790 = 98.06%. Problema 2: El rendimiento máximo de un transformador ocurre cuando las pérdidas variables en el cobre igualan a las pérdidas constantes en el núcleo (P_cu(x) = x^2 * P_sc = P_fe), determinando la fracción de carga óptima de operación x_opt = sqrt(P_fe / P_sc).",
        "bloque_sugerido": "Transformadores Monofásicos 45 min • Circuito equivalente, ensayos OC/SC y cálculo de regulación",
        "slides": [
            {
                "numero": 1,
                "seccion": "MODELADO DE TRANSFORMADORES",
                "titulo": "El Circuito Equivalente en T y Cantilever",
                "puntos": [
                    "R1 y R2: Resistencias óhmicas de los devanados que disipan calor por efecto Joule.",
                    "X1 y X2: Reactancias de dispersión magnética (flujos que no concatenan ambos devanados).",
                    "Rama de Magnetización (Rc || Xm): Modela las pérdidas en el hierro por histéresis/Foucault y la corriente magnetizante del núcleo."
                ]
            },
            {
                "numero": 2,
                "seccion": "DETERMINACIÓN EXPERIMENTAL DE PARÁMETROS",
                "titulo": "Ensayos Normalizados IEEE C57",
                "puntos": [
                    "Ensayo de Vacío (Open Circuit): Se aplica tensión nominal; la corriente es muy baja; mide prácticamente de forma pura las pérdidas en el núcleo (P_fe).",
                    "Ensayo de Cortocircuito (Short Circuit): Se aplica tensión reducida para circular corriente nominal; mide exclusivamente las pérdidas en el cobre (P_cu).",
                    "Permite predecir con total exactitud la caída de tensión y rendimiento bajo cualquier condición de carga."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Transformadores Trifásicos: Grupos de Conexión (Dyn11, Ynd11), Desfase y Paralelo",
        "objetivo": "Analizar los bancos y transformadores trifásicos, identificando grupos de conexión normalizados (índice horario), armónicos de tercera componente y condiciones rigurosas de operación en paralelo.",
        "concepto_clave_latex": r"\text{Índice Horario}: \theta_{\text{desfase}} = h \times 30^\circ \quad ; \quad \text{Reparto}: S_A = S_{\text{total}} \frac{S_{n,A}/Z_{cc,A}}{\sum S_{n,i}/Z_{cc,i}}",
        "ejemplo": "Problema 1: Un transformador elevador de parque solar de 20 MVA, 34.5 kV delta en baja tensión a 115 kV estrella con neutro accesible en alta tensión tiene un grupo de conexión normalizado Dyn11 (índice horario h = 11, lo que indica que las tensiones de línea del secundario adelantan 11 * 30° = 330° o retrasan 30° respecto a las de baja tensión): Se proyecta conectar en paralelo un segundo transformador existente de 15 MVA, 34.5 / 115 kV pero con grupo de conexión Ynd1 (índice horario h = 1, donde el secundario adelanta 30° respecto al primario). Análisis riguroso de factibilidad de paralelo: La diferencia angular entre las tensiones secundarias de ambos transformadores sería Delta_phi = 30° - (-30°) = 60°. Si se cerrara el interruptor de acoplamiento en 115 kV, la tensión diferencial neta entre fases homólogas sería: Delta_V = 2 * V_fase * sin(60°/2) = 2 * (115,000 / sqrt(3)) * sin(30°) = 2 * 66,395 * 0.5 = 66,395 V (tensión de fase plena aplicada directamente a través de las impedancias internas de dispersión). Con impedancias de cortocircuito z_cc = 7.5%, la corriente de circulación resultante sería: I_circ = Delta_V / (Z_A + Z_B) = 66,395 / (3.3 + 4.4) = 8,622 A (más de 11 veces la corriente nominal, provocando la destrucción inmediata por explosión térmica de los devanados). Conclusión: El paralelo es FÍSICAMENTE INVIABLE debido a la discrepancia de grupos horarios (Grupo 4 con h=11 vs Grupo 3 con h=1). Para operar en paralelo se debe adquirir un transformador idéntico Dyn11 con la misma impedancia porcentual Z_cc% = 7.5% para que la potencia de carga se distribuya exactamente proporcional a las capacidades nominales (15 MVA y 20 MVA) sin sobrecargar ninguna unidad. Problema 2: En transformadores estrella-estrella (Yy) sin devanado terciario en delta, los armónicos triples de corriente magnetizante (3°, 9°) no pueden circular, deformando la tensión de fase con sobretensiones de cresta elevadas en el neutro.",
        "bloque_sugerido": "Transformadores Trifásicos 45 min • Grupos de conexión Dyn11, índice horario y condiciones de paralelo",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONEXIONES TRIFÁSICAS Y ARMONIOS",
                "titulo": "Delta (D), Estrella (Y) y Zig-zag (Z)",
                "puntos": [
                    "Conexión Delta: Atrapa los armónicos triples (3er armónico) en una corriente circulante interna, purificando la forma de onda de tensión.",
                    "Conexión Estrella con Neutro: Permite dos niveles de tensión (fase-fase y fase-neutro) y puesta a tierra directa para protección.",
                    "Conexión Zig-zag: Proporciona un camino de baja impedancia a corrientes homopolares de falla a tierra en redes aisladas."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONDICIONES DE PARALELO RIGUROSAS",
                "titulo": "Las 4 Reglas de Acoplamiento en Red",
                "puntos": [
                    "1. Idéntica relación de transformación nominal (evita corrientes de circulación permanentes en vacío).",
                    "2. Pertenecer al mismo grupo de conexión y desfase horario (Dyn11 con Dyn11, nunca con Dyn5 ni Ynd1).",
                    "3. Idéntica impedancia porcentual de cortocircuito Z_cc% (garantiza reparto de carga proporcional a la potencia nominal).",
                    "4. Misma secuencia de fases (positiva A-B-C)."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Autotransformadores y Transformadores de Medida (TC y TP): Saturación y Cargas",
        "objetivo": "Dimensionar transformadores de corriente (TC) y de potencial (TP) para subestaciones eléctricas evaluando la saturación por sobrecorriente (clase 5P20) y límites de carga de precisión (Burden).",
        "concepto_clave_latex": r"\text{Autotransformador}: S_{\text{propia}} = S_{\text{pasante}} \left(1 - \frac{1}{a}\right) \quad ; \quad \text{TC}: \text{Burden} = Z_{\text{cables}} + Z_{\text{relé}} \le Z_{\text{nom}}",
        "ejemplo": "Problema 1: En una subestación elevadora de 115 kV, se dimensiona un transformador de corriente (TC) tipo toroidal de núcleo ferromagnético para protección del alimentador principal frente a cortocircuitos trifásicos de hasta I_cc,max = 24,000 A (24 kA). La corriente nominal de carga del circuito es de 800 A. Se selecciona un TC con relación de transformación nominal 1000/5 A (factor de escala N = 200) con clase de protección 5P20 y potencia de precisión nominal (Burden) de 30 VA a corriente secundaria nominal I_sn = 5 A. Impedancia máxima admisible del secundario: Z_burden,nom = 30 VA / (5 A)^2 = 30 / 25 = 1.20 ohms. La carga secundaria real conectada al TC consta de: resistencia de los devanados secundarios del TC R_ct = 0.25 ohms; resistencia de los cables de cobre de control de calibre 12 AWG (longitud de ida y vuelta L = 80 m a 5.3 ohms/km ==> R_cable = 0.080 * 5.3 = 0.424 ohms); e impedancia de entrada del relé digital de protección de sobrecorriente Z_relé = 0.08 ohms. Impedancia total del bucle de carga conectado: Z_carga_real = R_ct + R_cable + Z_relé = 0.25 + 0.424 + 0.08 = 0.754 ohms. Verificación del Burden: Como Z_carga_real (0.754 ohms) <= Z_burden,nom (1.20 ohms), el TC operará dentro de su clase de precisión sin saturarse térmicamente. Verificación de saturación ante cortocircuito extremo (Factor de Límite de Precisión ALF): La corriente de falla máxima en el primario es 24,000 A (equivalente a 24 veces la corriente nominal, factor de sobrecorriente real ALF_real = 24,000 / 1000 = 24). El factor de precisión nominal garantizado es de 20 (clase 5P20, error compuesto < 5% a 20 veces la corriente nominal bajo Burden nominal de 1.20 ohms). El factor de límite de precisión efectivo real del TC con la carga real reducida es: ALF_efectivo = ALF_nom * [(R_ct + Z_burden,nom) / (R_ct + Z_carga_real)] = 20 * [(0.25 + 1.20) / (0.25 + 0.754)] = 20 * (1.45 / 1.004) = 20 * 1.444 = 28.88. Dado que ALF_efectivo = 28.88 > ALF_real = 24, el núcleo del TC NO se saturará durante la falla de 24 kA, permitiendo que el relé de protección lea la corriente senoidal completa sin distorsión y dispare el interruptor en 40 ms. Problema 2: En autotransformadores con relación de transformación cercana a la unidad (ej. 230/115 kV, a = 2), la potencia electromagnética interna de diseño es exactamente la mitad de la potencia aparente pasante (S_propia = 0.5 * S_pasante), logrando ahorros masivos de núcleo de acero y cobre.",
        "bloque_sugerido": "Instrumentación de Potencia 45 min • Dimensionamiento de TCs clase 5P20, Burden y autotransformadores",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSFORMADORES DE MEDIDA (IT)",
                "titulo": "Transformadores de Corriente (TC) y Potencial (TP)",
                "puntos": [
                    "Aíslan galvánicamente los relés y medidores de los voltajes letales de alta tensión (115 kV / 220 kV).",
                    "Reducen magnitudes a valores normalizados estandarizados: 5 A o 1 A en corriente; 120 V o 115 V en tensión.",
                    "¡PELIGRO MORTAL!: El devanado secundario de un TC en servicio NUNCA debe abrirse; se inducirían miles de voltios destructivos."
                ]
            },
            {
                "numero": 2,
                "seccion": "CLASES DE PRECISIÓN Y BURDEN",
                "titulo": "Medición (0.2S) vs Protección (5P20)",
                "puntos": [
                    "TCs de Medición (Facturación): Ultra-precisos a corrientes bajas (clase 0.2S o 0.5S); deben saturarse intencionalmente ante fallas para proteger el medidor.",
                    "TCs de Protección: Menos precisos en baja carga pero NO deben saturarse bajo cortocircuitos severos (clase 5P20: 5% de error a 20*In).",
                    "Burden: Impedancia de los cables y bobinas conectadas; exceder el Burden nominal provoca saturación prematura y fallas de disparo."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Principios de Conversión Electromecánica: Coenergía Magnética y Fuerza/Par",
        "objetivo": "Calcular fuerzas y momentos de torsión electromagnéticos en actuadores y máquinas rotativas a partir del balance energético del campo magnético y la coenergía magnética.",
        "concepto_clave_latex": r"W_f'(\lambda, i, x) = \int_0^i \lambda(i', x) di' \quad ; \quad F_e = \left. \frac{\partial W_f'(i, x)}{\partial x} \right|_{i = \text{cte}} = \frac{1}{2} i^2 \frac{dL(x)}{dx}",
        "ejemplo": "Problema 1: Un electroimán elevador de chatarra industrial y relé de potencia de núcleo ferromagnético lineal tiene una bobina de N = 800 vueltas con resistencia R = 4.0 ohms. La inductancia del sistema depende fuertemente de la posición del entrehierro variable x (en metros) según la función L(x) = 0.040 / (1 + 250 x) Henrios, donde x es la holgura de separación física del inducido (0 <= x <= 0.02 m). La bobina se conecta a una fuente de tensión continua regulada de V = 48 V DC, estableciendo en régimen permanente una corriente constante de I = V / R = 48 / 4 = 12.0 A. Se requiere calcular la fuerza de atracción electromagnética neta F_e que ejerce el electroimán cuando el inducido se sitúa a una distancia x = 4 mm = 0.004 m: En un sistema magnéticamente lineal, la coenergía magnética W_f' es igual a la energía del campo: W_f'(i, x) = 0.5 * L(x) * i^2. La fuerza electromagnética a corriente constante viene dada por la derivada espacial de la coenergía: F_e = + [partial W_f' / partial x]_i = 0.5 * i^2 * [dL(x) / dx]. Derivando la función de inductancia: dL/dx = d/dx [0.040 * (1 + 250 x)^-1] = 0.040 * (-1) * (1 + 250 x)^-2 * (250) = -10.0 / (1 + 250 x)^2. Para x = 0.004 m: (1 + 250 * 0.004) = 1 + 1.0 = 2.0. Por tanto: dL/dx = -10.0 / (2.0)^2 = -10.0 / 4.0 = -2.50 H/m. Magnitud de la fuerza de atracción magnética: F_e = 0.5 * (12.0)^2 * (-2.50) = 0.5 * 144 * (-2.50) = -180.0 Newtons. El signo negativo indica que la fuerza actúa en el sentido de reducir el entrehierro x (fuerza de atracción hacia el núcleo que tiende a cerrar el entrehierro para maximizar la inductancia del circuito magnético). Capacidad de carga: El actuador puede elevar una masa de M = 180 / 9.81 = 18.35 kg a esa distancia. Problema 2: En máquinas eléctricas rotativas, el torque electromagnético se formula como T_e = 0.5 * i^2 * (dL(theta)/dtheta), demostrando que las máquinas de reluctancia pura generan par intentando alinear la posición de mínima reluctancia (máxima inductancia) con el eje del campo magnético.",
        "bloque_sugerido": "Conversión Electromecánica 45 min • Energía, coenergía magnética y cálculo de fuerzas dL/dx",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA ELECTROMAGNÉTICA",
                "titulo": "Balance de Energía en Sistemas Acoplados",
                "puntos": [
                    "dE_eléctrica = dE_mecánica + dW_campo + dE_pérdidas térmicas.",
                    "El campo magnético actúa como el medio transductor intermedio de almacenamiento y transferencia de energía.",
                    "Coenergía W_f': Artificio matemático definido como el área complementaria bajo la curva lambda-i, ideal cuando la corriente es la variable independiente."
                ]
            },
            {
                "numero": 2,
                "seccion": "ORIGEN FÍSICO DEL TORQUE",
                "titulo": "Torque de Alineamiento y Lorentz",
                "puntos": [
                    "Fuerza de Lorentz (F = I * L x B): Fuerza ejercida sobre conductores con corriente inmersos en un campo magnético exterior.",
                    "Fuerza de Reluctancia: Tendencia natural de todo material ferromagnético a moverse hacia la zona de menor resistencia magnética.",
                    "Todas las máquinas rotativas del planeta operan combinando estos dos mecanismos fundamentales."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Máquinas de Corriente Continua (DC): Devanados, Reacción de Inducido y Ecuaciones",
        "objetivo": "Modelar máquinas de corriente continua evaluando la fuerza contra-electromotriz (FCEM), torque electromagnético inducido, devanados imbricados/ondulados y mitigación de la reacción de inducido mediante polos de conmutación.",
        "concepto_clave_latex": r"E_a = K_a \Phi \omega_m \quad ; \quad T_e = K_a \Phi I_a \quad ; \quad K_a = \frac{Z P}{2\pi a}",
        "ejemplo": "Problema 1: Un generador de corriente continua de 4 polos (P = 4) tiene un inducido con Z = 480 conductores distribuidos en ranuras y conectado con devanado imbricado simple (simplex lap winding, donde el número de ramas en paralelo es igual al número de polos, a = P = 4). El flujo magnético útil por polo producido por el devanado de campo es Phi = 0.025 Weber. La máquina gira a una velocidad mecánica de n = 1500 rpm. 1) Constante constructiva de la máquina: K_a = (Z * P) / (2 * pi * a) = (480 * 4) / (2 * pi * 4) = 480 / (2 * pi) = 76.394 rad^-1. Velocidad angular mecánica del rotor: omega_m = (2 * pi * 1500) / 60 = 50 * pi = 157.08 rad/s. 2) Tensión inducida interna (FCEM): E_a = K_a * Phi * omega_m = 76.394 * 0.025 * 157.08 = 1.9098 * 157.08 = 300.0 V (o directamente E_a = (Z * P * n * Phi) / (60 * a) = (480 * 4 * 1500 * 0.025) / (60 * 4) = 72,000 / 240 = 300 V). 3) Si el generador alimenta una carga que demanda una corriente de inducido de I_a = 60 A, y la resistencia interna del inducido es R_a = 0.25 ohms: Tensión en bornes de salida de la máquina: V_t = E_a - I_a * R_a = 300 - 60 * 0.25 = 300 - 15 = 285.0 V. Torque electromagnético resistente que debe suministrar el motor primario (turbina de vapor): T_e = K_a * Phi * I_a = 76.394 * 0.025 * 60 = 1.9098 * 60 = 114.59 N*m. Potencia mecánica convertida a eléctrica: P_conv = T_e * omega_m = 114.59 * 157.08 = 18,000 W = 18.0 kW (exactamente igual a E_a * I_a = 300 V * 60 A = 18,000 W). Problema 2: En máquinas DC pesadas, la reacción de inducido desvía la zona neutra magnética en sentido del giro en generadores, provocando chispas destructivas en las delgas del colector; para neutralizarla se instalan devanados de compensación en las zapatas polares conectados en serie con el inducido.",
        "bloque_sugerido": "Máquinas de Corriente Continua 45 min • Ecuaciones Ka*Phi, devanados imbricados y reacción de inducido",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONSTITUCIÓN DE LA MÁQUINA DC",
                "titulo": "Estator Inductor y Rotor Inducido",
                "puntos": [
                    "Estator: Contiene los polos principales que producen el campo magnético estacionario B y los polos auxiliares de conmutación.",
                    "Rotor (Inducido): Núcleo laminado ranurado que porta los devanados de corriente alterna interna rectificada mecánicamente.",
                    "Colector de delgas y escobillas de grafito: Conmutador mecánico rotativo que transforma la CA interna en CC externa."
                ]
            },
            {
                "numero": 2,
                "seccion": "REACCIÓN DE INDUCIDO Y CONMUTACIÓN",
                "titulo": "Desviación del Eje Neutro",
                "puntos": [
                    "La corriente del inducido genera su propio campo magnético en cuadratura que distorsiona el flujo principal del estator.",
                    "Debilita el campo bajo las puntas polares y desplaza el plano neutro geométrico, causando chisporroteo en escobillas.",
                    "Solución técnica definitiva: Interpolos (polos de conmutación) en serie que inducen una tensión opuesta que anula la reactancia L*di/dt."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Generadores y Motores DC: Excitación Shunt, Serie y Compound con Control de Velocidad",
        "objetivo": "Modelar el comportamiento en carga de motores DC serie, shunt y compuestos (compound), diseñando sistemas de control de velocidad por debilitamiento de campo y control por tensión de armadura (Ward-Leonard).",
        "concepto_clave_latex": r"\omega_m = \frac{V_t - I_a R_a}{K_a \Phi} \quad ; \quad \text{Motor Serie}: T_e \propto I_a^2 \quad ; \quad \omega_m \to \infty \text{ si } T_L \to 0",
        "ejemplo": "Problema 1: Un motor de corriente continua con excitación en derivación (Shunt) de 25 HP (18.65 kW de salida útil mecánica en el eje), V_t = 240 V, gira a una velocidad nominal de n_1 = 1200 rpm (omega_1 = 125.66 rad/s) cuando consume una corriente de línea total de I_L = 88 A. Resistencia de inducido R_a = 0.15 ohms; resistencia del devanado de campo shunt R_f = 120 ohms. Corriente de campo shunt: I_f = V_t / R_f = 240 / 120 = 2.0 A. Corriente nominal de inducido: I_a1 = I_L - I_f = 88 - 2.0 = 86.0 A. FCEM nominal inicial: E_a1 = V_t - I_a1 * R_a = 240 - (86.0 * 0.15) = 240 - 12.9 = 227.1 V. Se requiere elevar la velocidad de rotación a n_2 = 1500 rpm manteniendo constante el torque resistente de la carga mecánica (T_L = cte). Control por debilitamiento de campo magnético (Field Weakening): Dado que T_L = K_a * Phi * I_a = cte, el producto Phi * I_a permanece constante (Phi_2 * I_a2 = Phi_1 * I_a1 ==> I_a2 = I_a1 * (Phi_1 / Phi_2)). Denotemos la fracción de debilitamiento de flujo k_phi = Phi_2 / Phi_1. Entonces I_a2 = 86.0 / k_phi. Relación de velocidades: n_2 / n_1 = (E_a2 / E_a1) * (Phi_1 / Phi_2) ==> 1500 / 1200 = 1.25 = [(240 - I_a2 * 0.15) / 227.1] * (1 / k_phi). Sustituyendo I_a2: 1.25 * 227.1 * k_phi = 240 - (86.0 / k_phi) * 0.15 ==> 283.875 * k_phi = 240 - 12.9 / k_phi. Multiplicando por k_phi: 283.875 k_phi^2 - 240 k_phi + 12.9 = 0. Resolviendo la ecuación cuadrática: k_phi = [240 +- sqrt(57600 - 14648)] / 567.75 = [240 +- sqrt(42952)] / 567.75 = (240 +- 207.25) / 567.75 ==> k_phi = 447.25 / 567.75 = 0.7877 (el flujo se debilita al 78.77% de su valor nominal). Nueva corriente de inducido requerida: I_a2 = 86.0 / 0.7877 = 109.18 A. Para lograr este debilitamiento en la zona lineal magnética (I_f proporcional a Phi), se inserta un reóstato de campo variable en serie R_ext: I_f2 = 2.0 * 0.7877 = 1.575 A. Resistencia total de campo requerida: R_total = 240 / 1.575 = 152.38 ohms. Resistencia externa agregada: R_ext = 152.38 - 120 = 32.38 ohms. Problema 2: ¡ADVERTENCIA DE SEGURIDAD CRÍTICA EN MOTORES SERIE!: En un motor DC serie, el flujo es proporcional a la corriente de carga (Phi = k_s * I_a); si el motor se opera en vacío (sin carga mecánica, I_a -> 0), el flujo tiende a cero y la velocidad se dispara teóricamente hacia el infinito (omega_m -> inf), provocando el embalamiento descontrolado y la explosión centrífuga del inducido.",
        "bloque_sugerido": "Control de Motores DC 45 min • Curvas par-velocidad shunt/serie y control por debilitamiento de campo",
        "slides": [
            {
                "numero": 1,
                "seccion": "TIPOLOGÍAS DE CONEXIÓN DC",
                "titulo": "Shunt, Serie y Compound",
                "puntos": [
                    "Motor Shunt: Velocidad prácticamente constante ante variaciones de carga; excelente para bombas y cintas transportadoras.",
                    "Motor Serie: Par de arranque gigantesco proporcional al cuadrado de la corriente (T ~ I^2); ideal para tracción ferroviaria pesada.",
                    "Motor Compound (Compuesto): Combina un devanado serie y uno shunt; par de arranque elevado sin riesgo de embalamiento en vacío."
                ]
            },
            {
                "numero": 2,
                "seccion": "TÉCNICAS DE REGULACIÓN DE VELOCIDAD",
                "titulo": "Tensión de Armadura vs Flujo de Campo",
                "puntos": [
                    "Control por Tensión de Armadura (por debajo de la velocidad base): Par constante disponible variando V_t con rectificadores tiristores.",
                    "Debilitamiento de Campo (por encima de la velocidad base): Potencia constante disponible reduciendo I_f mediante resistencias.",
                    "Sistema Ward-Leonard histórico: Precursor analógico de los variadores de frecuencia electrónicos modernos."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Campos Magnéticos Giratorios: Teorema de Ferraris y Devanados Distribuidos",
        "objetivo": "Demostrar matemáticamente el Teorema de Ferraris demostrando que un devanado trifásico simétrico alimentado por corrientes equilibradas genera una onda espacial de campo magnético de magnitud constante que gira a velocidad síncrona.",
        "concepto_clave_latex": r"B_{net}(\theta, t) = \frac{3}{2} B_{max} \cos(\omega t - \theta) \quad ; \quad n_s = \frac{120 f}{P} \quad [\text{Velocidad Síncrona}]",
        "ejemplo": "Problema 1: Un estator trifásico de 4 polos (P = 4, p = 2 pares de polos) alimentado por una red eléctrica balanceada de f = 60 Hz tiene 3 devanados de fase espacialmente desfasados 120° geométricos eléctricos (2 * pi / (3 * p) = 120° / 2 = 60° mecánicos en el espacio cilíndrico del estator). Las densidades de flujo de cada fase en el entrehierro vienen dadas por: B_a(theta, t) = B_max * cos(omega*t) * cos(theta); B_b(theta, t) = B_max * cos(omega*t - 120°) * cos(theta - 120°); B_c(theta, t) = B_max * cos(omega*t - 240°) * cos(theta - 240°). Aplicando identidades trigonométricas de producto a suma: B_a = 0.5 * B_max * [cos(omega*t - theta) + cos(omega*t + theta)]; B_b = 0.5 * B_max * [cos(omega*t - theta) + cos(omega*t + theta - 240°)]; B_c = 0.5 * B_max * [cos(omega*t - theta) + cos(omega*t + theta - 480°)]. Al sumar las tres fases, las componentes retrógradas que giran en sentido inverso (+theta) están desfasadas 120° y 240° en el tiempo, cancelándose exactamente a cero: cos(omega*t + theta) + cos(omega*t + theta - 120°) + cos(omega*t + theta + 120°) = 0. Las componentes directas (-theta) suman en fase: B_net(theta, t) = 3 * [0.5 * B_max * cos(omega*t - theta)] = 1.5 * B_max * cos(omega*t - theta). Demostración: La densidad de flujo resultante tiene una amplitud perfectamente constante igual a 1.5 veces el pico de una fase y gira a velocidad angular síncrona omega_s = omega = 2 * pi * 60 = 377 rad/s eléctrico. En unidades de rpm mecánicas: n_s = 120 * f / P = (120 * 60) / 4 = 1800 rpm (velocidad angular mecánica omega_m,s = 1800 * 2 * pi / 60 = 188.5 rad/s). Si se invierte la secuencia de fases intercambiando dos cables (ej. A-C-B), el campo giratorio invierte instantáneamente su sentido de giro a -1800 rpm. Problema 2: En devanados fraccionarios acortados (chording) con factor de paso k_p = sin(p*pi / (2*tau)), el acortamiento intencional del paso de bobina a 5/6 elimina completamente el 5° y 7° armónico espacial del campo magnético.",
        "bloque_sugerido": "Campos Giratorios 45 min • Deducción analítica del Teorema de Ferraris y devanados acortados",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL DESCUBRIMIENTO DE NIKOLA TESLA",
                "titulo": "El Principio del Motor de Inducción",
                "puntos": [
                    "1888: Galileo Ferraris y Nikola Tesla descubren independientemente el campo magnético giratorio sin partes móviles.",
                    "Convierte corrientes alternas polifásicas estacionarias en un imán invisible que rota a velocidad síncrona n_s = 120*f / P.",
                    "Sustenta el 90% de todo el consumo motriz industrial del planeta Tierra."
                ]
            },
            {
                "numero": 2,
                "seccion": "FACTOR DE DEVANADO",
                "titulo": "Distribución y Paso Acortado",
                "puntos": [
                    "Factor de distribución k_d: Compensa el hecho de que las bobinas están repartidas en ranuras adyacentes y no concentradas.",
                    "Factor de paso k_p: Reduce la longitud de los cabezales de bobina (ahorra cobre) y elimina armónicos espaciales no deseados.",
                    "Factor de devanado total: k_w = k_d * k_p (típicamente entre 0.92 y 0.96 para máquinas trifásicas bien diseñadas)."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Motores de Inducción Trifásicos: Circuito Equivalente y Curva Par-Velocidad de Kloss",
        "objetivo": "Calcular el deslizamiento (slip), balance de potencia activa y torque electromagnético en motores de inducción jaula de ardilla mediante el circuito equivalente por fase y la ecuación analítica de Kloss.",
        "concepto_clave_latex": r"s = \frac{n_s - n_r}{n_s} \quad ; \quad T_e = \frac{2 T_{max}}{\frac{s}{s_{max}} + \frac{s_{max}}{s}} \quad ; \quad P_{conv} = P_{gap} (1 - s)",
        "ejemplo": "Problema 1: Un motor de inducción trifásico de 460 V (tensión de línea), 60 Hz, 4 polos, conectado en estrella, de 50 HP (37.3 kW), opera a una velocidad de rotor de n_r = 1746 rpm. Parámetros del circuito equivalente por fase referidos al estator en ohmios: R_1 = 0.12 ohms, X_1 = 0.55 ohms, R_2' = 0.15 ohms, X_2' = 0.55 ohms, X_m = 18.0 ohms (rama de pérdidas en el hierro R_c despreciada). Velocidad síncrona: n_s = (120 * 60) / 4 = 1800 rpm (omega_s = 188.5 rad/s). 1) Deslizamiento operativo: s = (1800 - 1746) / 1800 = 54 / 1800 = 0.030 (3.0%). Resistencia ficticia de carga que representa la conversión mecánica: R_2' * (1 - s) / s = 0.15 * (1 - 0.03) / 0.03 = 0.15 * (0.97 / 0.03) = 4.85 ohms. Resistencia total de la rama del rotor: R_2'/s = 0.15 / 0.03 = 5.00 ohms. 2) Impedancia equivalente de Thevenin vista desde el rotor (V_th = 460 / sqrt(3) * [X_m / (X_1 + X_m)] = 265.58 * [18.0 / 18.55] = 257.7 V; R_th = R_1 * [X_m / (X_1 + X_m)]^2 = 0.12 * (0.9703)^2 = 0.113 ohms; X_th approx X_1 = 0.55 ohms). Impedancia total del rotor en funcionamiento: Z_tot = (R_th + R_2'/s) + j(X_th + X_2') = (0.113 + 5.00) + j(0.55 + 0.55) = 5.113 + j 1.10 ohms. Magnitud de la corriente del rotor: I_2' = 257.7 / sqrt(5.113^2 + 1.10^2) = 257.7 / sqrt(26.14 + 1.21) = 257.7 / 5.23 = 49.27 A. 3) Potencia transmitida a través del entrehierro (Air-gap Power): P_gap = 3 * (I_2')^2 * (R_2'/s) = 3 * (49.27)^2 * 5.00 = 3 * 2427.5 * 5.00 = 36,413 W. Pérdidas en el cobre del rotor (Joule): P_cu,rotor = s * P_gap = 0.03 * 36,413 = 1092.4 W. Potencia mecánica convertida internamente: P_conv = P_gap - P_cu,rotor = (1 - s) * P_gap = 0.97 * 36,413 = 35,321 W (47.36 HP). Torque electromagnético inducido: T_e = P_gap / omega_s = 36,413 / 188.5 = 193.17 N*m. Deslizamiento de torque máximo (pull-out breakdown slip): s_max = R_2' / sqrt(R_th^2 + (X_th + X_2')^2) = 0.15 / sqrt(0.113^2 + 1.10^2) = 0.15 / 1.106 = 0.1356 (13.56%, a 1556 rpm). Torque máximo de desenganche: T_max = 3 * V_th^2 / [2 * omega_s * (R_th + sqrt(R_th^2 + (X_th + X_2')^2))] = 3 * 257.7^2 / [2 * 188.5 * (0.113 + 1.106)] = 199,224 / [377 * 1.219] = 199,224 / 459.56 = 433.5 N*m (2.24 veces el torque nominal). Problema 2: En motores con rotor de doble jaula de ardilla (Diseños NEMA C y D), el efecto pelicular (skin effect) a frecuencia de arranque (f_r = 60 Hz) fuerza la corriente a circular por la jaula externa de alta resistencia, logrando un alto par de arranque con baja corriente de inserción.",
        "bloque_sugerido": "Motores de Inducción 45 min • Circuito equivalente exacto, flujo de potencia y ecuación de Kloss",
        "slides": [
            {
                "numero": 1,
                "seccion": "TEORÍA DEL MOTOR ASÍNCRONO",
                "titulo": "El Deslizamiento (Slip) como Mecanismo Motor",
                "puntos": [
                    "Si el rotor girara a la misma velocidad que el campo magnético (n_r = n_s, s = 0), no habría variación de flujo en las barras.",
                    "Sin dPhi/dt no se induce tensión ni corriente en el rotor; por tanto el torque sería cero.",
                    "El motor de inducción DEBE girar siempre ligeramente más lento que el campo giratorio para producir torque."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA CURVA PAR-VELOCIDAD DE KLOSS",
                "titulo": "Zonas de Operación y Par Máximo",
                "puntos": [
                    "Zona lineal estable: Operación normal entre vacio (s ~ 0) y plena carga (s = 1-5%); el par es proporcional al deslizamiento.",
                    "Par de desenganche (Breakdown Torque T_max): Límite físico de estabilidad; sobrecargas superiores frenan y bloquean el motor.",
                    "Regímenes de funcionamiento: s in [0, 1] Motor; s < 0 Generador de inducción (eólico); s > 1 Freno por contracorriente (Plugging)."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Arranque y Frenado de Motores de Inducción: Estrella-Triángulo y Soft-Starters",
        "objetivo": "Diseñar esquemas de arranque a tensión reducida (Estrella-Triángulo, autotransformador y arrancadores suaves estáticos por tiristores) calculando la reducción de corriente de inserción y torque de arranque.",
        "concepto_clave_latex": r"I_{\text{arr},Y} = \frac{1}{3} I_{\text{arr},\Delta} \quad ; \quad T_{\text{arr},Y} = \frac{1}{3} T_{\text{arr},\Delta} \quad ; \quad V_{RMS} = V_{in} \sqrt{\frac{1}{\pi} (\pi - \alpha + \frac{\sin 2\alpha}{2})}",
        "ejemplo": "Problema 1: Una estación de bombeo de agua de refrigeración para una central termoeléctrica instala un motor de inducción trifásico de 150 kW, 460 V, 60 Hz, conexión delta nominal. En arranque directo a plena tensión (DOL - Direct-On-Line), los catálogos del fabricante indican una corriente de arranque de 6.5 veces la nominal (I_nom = 230 A ==> I_arr,DOL = 6.5 * 230 = 1495 A) y un torque de arranque de T_arr,DOL = 1.8 * T_nom = 1.8 * 810 N*m = 1458 N*m. La subestación local limita la corriente máxima de arranque a 600 A para evitar caídas de tensión que disparen protecciones de otros usuarios: 1) Análisis de Arranque Estrella-Triángulo (Y-Delta): En conexión estrella, la tensión de fase aplicada se reduce a V_fase = 460 / sqrt(3) = 265.5 V (reducción en 1/sqrt(3)). La corriente de línea en estrella es: I_arr,Y = (1/3) * I_arr,Delta = 1495 / 3 = 498.3 A. El torque de arranque en estrella también cae en 1/3 (proporcional al cuadrado de la tensión): T_arr,Y = (1/3) * T_arr,Delta = 1458 / 3 = 486 N*m (equivalente al 60% del torque nominal T_nom). Como el torque resistente de la bomba centrífuga en vacío al arrancar con válvula de descarga cerrada es solo el 25% del par nominal (T_bomba = 0.25 * 810 = 202.5 N*m), el torque motor T_arr,Y (486 N*m) supera holgadamente la resistencia, garantizando una aceleración suave hasta el 85% de la velocidad nominal antes de conmutar a delta. Corriente dentro del límite permitido (498.3 A < 600 A). 2) Alternativa con Arrancador Suave Electrónico (Soft-Starter por tiristores antiparalelo): Se programa una rampa de tensión lineal de 12 segundos con limitación de corriente programada a I_limit = 2.2 * I_nom = 506 A, eliminando el pico transitorio de conmutación mecánico que se presenta en el contactor estrella-triángulo y suprimiendo el golpe de ariete hidráulico en la tubería mediante parada suave decelerada. Problema 2: En frenado dinámico por inyección de corriente continua (DC Injection Braking), se desconecta la red AC y se inyecta corriente directa en dos bornes del estator, creando un campo magnético estacionario que detiene el rotor por disipación de corrientes parásitas en menos de 2 segundos.",
        "bloque_sugerido": "Sistemas de Arranque 45 min • Comparativa DOL vs Estrella-Triángulo vs Soft-Starter de tiristores",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA PROBLEMÁTICA DEL ARRANQUE",
                "titulo": "Corrientes de Inserción (Inrush Currents)",
                "puntos": [
                    "En el instante t = 0 (rotor bloqueado s = 1), el motor actúa como un transformador en cortocircuito puro.",
                    "Arranque Directo (DOL): Demanda de 5 a 8 veces la corriente nominal; provoca caídas de tensión (flicker) en la red.",
                    "Impacto mecánico: Golpes de torque bruscos que desgastan chavetas, acoplamientos y cadenas de transmisión."
                ]
            },
            {
                "numero": 2,
                "seccion": "TECNOLOGÍAS DE ATENUACIÓN",
                "titulo": "De Contactor Clásico a Electrónica de Potencia",
                "puntos": [
                    "Arrancador Estrella-Triángulo: Solución electromecánica de bajo costo; divide la corriente y el torque exactamente entre 3.",
                    "Arrancador Suave (Soft-Starter): Regula el ángulo de disparo alfa de tiristores SCR; rampa de aceleración continua sin saltos.",
                    "Contactores de Bypass: Cortocircuitan los tiristores tras finalizar el arranque para eliminar pérdidas de conmutación continuas."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Control de Velocidad Escalar V/f (Volts per Hertz) en Motores de Inducción con Inversores PWM",
        "objetivo": "Diseñar la estrategia de control escalar de frecuencia variable V/f manteniendo constante el flujo magnético en el entrehierro para aplicaciones de velocidad variable en bombas y ventiladores.",
        "concepto_clave_latex": r"\frac{V_1}{f_1} = \text{Constante} \implies \Phi_{gap} \approx \text{cte} \quad ; \quad V_1(f) = V_{boost} + \left(\frac{V_{nom} - V_{boost}}{f_{nom}}\right) f",
        "ejemplo": "Problema 1: Un motor de inducción trifásico de 30 kW, 400 V, 50 Hz, 4 polos (velocidad síncrona nominal n_s = 1500 rpm) acciona un ventilador centrífugo industrial de tiro inducido en una caldera de biomasa. La relación de flujo nominal es: V/f = 400 V / 50 Hz = 8.0 V/Hz. Se requiere operar el ventilador al 60% de su velocidad nominal (n_s = 900 rpm, f = 30 Hz). Para mantener el flujo magnético en el entrehierro constante en su valor nominal (evitando que el motor se sature magnéticamente o pierda capacidad de torque), el variador de frecuencia ajusta la tensión proporcionalmente: V_1 = (V/f)_nom * f = 8.0 * 30 = 240.0 V. A frecuencias muy bajas (ej. f = 5 Hz, n_s = 150 rpm), la tensión teórica sería V = 8.0 * 5 = 40 V; sin embargo, la caída de tensión resistiva en el estator (I_1 * R_1) deja de ser despreciable frente a la reactancia (omega * L_1), provocando el debilitamiento del flujo y la pérdida del par de arranque. Se implementa una compensación de tensión de refuerzo (Voltage Boost) fijada en V_boost = 18 V. A 5 Hz, la tensión real sintetizada por modulación de ancho de pulso (PWM) es: V_real = 18 + [(400 - 18) / 50] * 5 = 18 + 7.64 * 5 = 18 + 38.2 = 56.2 V, restaurando el par pleno. Por encima de 50 Hz (operación a 70 Hz, n_s = 2100 rpm): Como la tensión del inversor no puede superar el límite del enlace de continua (V_max = 400 V), la tensión se fija en 400 V constante. La relación cae a V/f = 400 / 70 = 5.71 V/Hz (Régimen de Debilitamiento de Campo o Potencia Constante), donde el par máximo cae con el cuadrado de la frecuencia (T_max ~ 1/f^2). Problema 2: En bombas centrífugas gobernadas por las leyes de afinidad (el caudal varía proporcional a la velocidad y la potencia varía con el cubo de la velocidad, P ~ n^3), reducir la velocidad del motor al 80% mediante control V/f reduce el consumo de energía eléctrica al (0.8)^3 = 51.2% (ahorro energético directo del 48.8% frente al estrangulamiento con válvula).",
        "bloque_sugerido": "Control Escalar V/f 45 min • Relación V/f constante, compensación de boost y modulación PWM",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONTROL ELECTRÓNICO DE VELOCIDAD",
                "titulo": "La Estrategia V/f Constante",
                "puntos": [
                    "La ecuación de fem inducida E = 4.44 * f * N * Phi demuestra que el flujo Phi es directamente proporcional a V/f.",
                    "Si se reduce la frecuencia f sin bajar la tensión V, el núcleo entra en saturación magnética severa y se quema.",
                    "Si se reduce la tensión sin bajar la frecuencia, el motor pierde par y se desengancha.",
                    "Mantener V/f constante preserva el par máximo de la máquina en todo el rango por debajo de la frecuencia base."
                ]
            },
            {
                "numero": 2,
                "seccion": "LEYES DE AFINIDAD Y AHORRO ENERGÉTICO",
                "titulo": "Sustitución de Válvulas por Variadores VFD",
                "puntos": [
                    "El estrangulamiento con válvulas mecánicas disipa energía por fricción hidráulica inútil.",
                    "Leyes de Afinidad: Caudal Q ~ n, Presión H ~ n^2, Potencia P ~ n^3.",
                    "Reducir la velocidad del motor en un 20% reduce el consumo eléctrico a la mitad; retorno de inversión típico < 1.5 años."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Control Vectorial por Orientación de Campo (FOC) en Motores de Inducción",
        "objetivo": "Formular el control orientado al campo del rotor (R-FOC) para desacoplar el control de flujo magnético y par electromagnético en ejes d-q emulando la respuesta dinámica de una máquina DC.",
        "concepto_clave_latex": r"i_{ds} \implies \text{Flujo del Rotor } \lambda_{dr} \quad ; \quad i_{qs} \implies \text{Torque } T_e = \frac{3}{2} p \frac{L_m}{L_r} \lambda_{dr} i_{qs}",
        "ejemplo": "Problema 1: Se diseña el lazo de control vectorial por orientación de campo indirecto (I-FOC) para el motor de tracción de inducción de 100 kW de un camión minero eléctrico en el Cerrejón. Parámetros del motor: p = 2 pares de polos, L_m = 24.5 mH, L_r = 25.8 mH, R_r = 0.055 ohms (constante de tiempo del rotor T_r = L_r / R_r = 0.0258 / 0.055 = 0.469 segundos = 469 ms). Se fija la corriente de magnetización de eje directo en i_ds* = 40.0 A para establecer el flujo de rotor nominal: lambda_dr = L_m * i_ds* = 0.0245 * 40.0 = 0.980 Weber (manteniendo lambda_qr = 0 en el marco síncrono orientado con el flujo de rotor). En un instante t = 2.0 s, el conductor pisa el pedal acelerador demandando un torque de tracción instantáneo de T_e* = 450 N*m. 1) Cálculo de la corriente de eje en cuadratura requerida (i_qs*): T_e = 1.5 * p * (L_m / L_r) * lambda_dr * i_qs ==> 450 = 1.5 * 2 * (0.0245 / 0.0258) * 0.980 * i_qs* ==> 450 = 3 * 0.9496 * 0.980 * i_qs* ==> 450 = 2.7918 * i_qs* ==> i_qs* = 450 / 2.7918 = 161.19 A. 2) Cálculo de la frecuencia de deslizamiento de compensación (Slip Frequency): omega_sl = (L_m / T_r) * (i_qs* / lambda_dr) = (0.0245 / 0.469) * (161.19 / 0.980) = 0.05224 * 164.48 = 8.592 rad/s eléctrico (equivalente a f_sl = 1.367 Hz). 3) Posición del ángulo del vector de flujo de rotor: Se integra la velocidad mecánica medida por el encoder incremental más la frecuencia de deslizamiento: theta_e = int (p * omega_m + omega_sl) dt. 4) Transformación inversa de Park y Clarke: Se convierten las corrientes de referencia (i_ds*, i_qs*) a corrientes trifásicas estatóricas senoidales (i_a*, i_b*, i_c*), moduladas por el inversor trifásico con frecuencia de conmutación de 10 kHz mediante Vector Espacial (SVPWM). Resultado dinámico: El par de 450 N*m se establece en menos de 5 milisegundos sin sobreoscilaciones de corriente ni perturbación del flujo magnético, superando con creces la lenta respuesta dinámica del control escalar V/f. Problema 2: El desacoplamiento FOC falla si la temperatura del devanado del rotor varía sin compensación térmica en el controlador, ya que el aumento de R_r altera la constante de tiempo T_r desalineando el eje de orientación.",
        "bloque_sugerido": "Control Vectorial FOC 45 min • Ejes d-q, cálculo del deslizamiento de desacoplamiento y SVPWM",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONTROL DE ALTO DESEMPEÑO DINÁMICO",
                "titulo": "La Filosofía del Field-Oriented Control (FOC)",
                "puntos": [
                    "En una máquina DC, el flujo de campo y el par de armadura son ortogonales por diseño mecánico de escobillas.",
                    "En el motor de inducción AC, las corrientes de estator alimentan simultáneamente el campo y el par de forma acoplada.",
                    "FOC (Blaschke y Hasse): Transforma matemáticamente el motor AC en una máquina DC equivalente en el marco d-q rotativo."
                ]
            },
            {
                "numero": 2,
                "seccion": "VENTAJAS FRENTE AL CONTROL ESCALAR",
                "titulo": "Respuesta en Milisegundos y Par a Velocidad Cero",
                "puntos": [
                    "Control Escalar V/f: Dinámica lenta (cientos de milisegundos), propenso a oscilaciones de corriente en transitorios.",
                    "Control Vectorial FOC: Respuesta de par instantánea en < 5 ms; entrega el 100% del par nominal a velocidad cero (0 rpm).",
                    "Indispensable para vehículos eléctricos, ascensores, grúas portuarias y robótica industrial de alta precisión."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Generadores Síncronos: Circuito Equivalente, Reactancia Síncrona Xs y Curva de Capabilidad",
        "objetivo": "Modelar el generador síncrono de rotor cilíndrico conectado a red infinita, calculando el ángulo de potencia delta, la reactancia síncrona Xs y los límites de estabilidad térmica y de excitación de la curva de capabilidad P-Q.",
        "concepto_clave_latex": r"P = \frac{E_f V_t}{X_s} \sin\delta \quad ; \quad Q = \frac{E_f V_t}{X_s} \cos\delta - \frac{V_t^2}{X_s} \quad ; \quad \text{Límite Estabilidad}: \delta \le 90^\circ",
        "ejemplo": "Problema 1: Un turbogenerador síncrono de rotor cilíndrico de 100 MVA, 13.8 kV (tensión de línea nominal), 60 Hz, 2 polos, conectado a una barra infinita de 13.8 kV (V_t = 13.8 / sqrt(3) = 7967.4 V fase-neutro) tiene una reactancia síncrona saturada por fase de X_s = 1.60 ohms (resistencia de inducido R_a despreciable). La máquina entrega a la red una potencia activa de P = 80 MW con factor de potencia 0.85 en atraso (inductivo, entregando reactivos a la red): Potencia aparente entregada: S = P / cos(theta) = 80 / 0.85 = 94.12 MVA (dentro de los 100 MVA de límite térmico del estator). Potencia reactiva entregada: Q = P * tan(theta) = 80 * tan(arccos 0.85) = 80 * 0.6197 = 49.58 MVAr. Corriente de línea de estator: I_a = S / (sqrt(3) * V_t) = 94,117,647 / (sqrt(3) * 13,800) = 94,117,647 / 23,899 = 3938.1 A. Ángulo de la corriente: theta = -arccos(0.85) = -31.79°. Tomando la tensión de fase en bornes como referencia fasorial V_t = 7967.4 /_ 0° V: Tensión interna generada por la excitación (FCEM Ef): E_f = V_t + j X_s * I_a = 7967.4 /_ 0° + (1.60 /_ 90°) * (3938.1 /_ -31.79°) = 7967.4 + 6301.0 /_ 58.21° = 7967.4 + 6301.0 * (cos 58.21° + j sin 58.21°) = 7967.4 + (3319.8 + j 5356.1) = 11,287.2 + j 5356.1 = 12,495.8 /_ 25.38° V (tensión de línea inducida E_f,linea = sqrt(3) * 12,495.8 = 21,643 V). Ángulo de carga o potencia de la máquina: delta = 25.38° (confortablemente alejado del límite teórico de inestabilidad transitoria de régimen permanente delta_max = 90°). Potencia máxima estática que la máquina podría entregar con esa excitación antes de perder el sincronismo (Pull-out Power): P_max = 3 * (E_f * V_t) / X_s = 3 * (12495.8 * 7967.4) / 1.60 = 298,693,000 / 1.60 = 186.68 MW. Límites de la Carta de Capabilidad P-Q: 1) Límite de corriente del estator: Círculo centrado en el origen con radio S_nom = 100 MVA; 2) Límite de corriente de campo: Círculo centrado en (0, -V_t^2/X_s = -68.7 MVAr) con radio (3*E_f*V_t/X_s); 3) Límite de subexcitación / estabilidad térmica de extremos de núcleo: Impide operar con absorción de reactivos excesiva (factor de potencia en adelanto). Problema 2: En cortocircuitos bruscos en bornes del generador síncrono, la corriente de falla evoluciona a través de tres periodos caracterizados por reactancias crecientes: reactancia subtransitoria X_d'' (0-50 ms), reactancia transitoria X_d' (50-500 ms) y reactancia síncrona permanente X_d.",
        "bloque_sugerido": "Generadores Síncronos 45 min • Ecuación P-delta, reactancia Xs y carta de capabilidad P-Q",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL CORAZÓN DEL SISTEMA DE POTENCIA",
                "titulo": "Generación Síncrona a Gran Escala",
                "puntos": [
                    "Responsable de suministrar la práctica totalidad de la energía eléctrica de la red convencional e inercia rotacional.",
                    "Rotor cilíndrico (Turbo-alternadores térmicos a 1800/3600 rpm): Diámetro pequeño y gran longitud para resistir fuerzas centrífugas.",
                    "Polos salientes (Hidro-generadores lentos a 100-600 rpm): Gran número de polos (12 a 72 polos) de gran diámetro.",
                    "La frecuencia eléctrica generada está rígidamente sincronizada con la velocidad mecánica (f = P*n / 120)."
                ]
            },
            {
                "numero": 2,
                "seccion": "LÍMITES OPERATIVOS EN LA CARTA P-Q",
                "titulo": "La Curva de Capabilidad",
                "puntos": [
                    "Define la región segura de operación simultánea de potencia activa (P) y reactiva (Q) sin destruir la máquina.",
                    "Sobreexcitación (entregar reactivos): Limitada por el calentamiento Joule del devanado de campo en el rotor.",
                    "Subexcitación (absorber reactivos): Limitada por calentamiento en las cabezas de núcleo del estator y margen de estabilidad estática."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Generadores Síncronos de Polos Salientes: Teoría de las Dos Reacciones de Blondel",
        "objetivo": "Modelar generadores síncronos de polos salientes descomponiendo corrientes y reactancias en los ejes directo (Xd) y en cuadratura (Xq) calculando el torque de reluctancia.",
        "concepto_clave_latex": r"P = \frac{E_f V_t}{X_d} \sin\delta + \frac{V_t^2}{2} \left( \frac{1}{X_q} - \frac{1}{X_d} \right) \sin(2\delta) \quad ; \quad X_d > X_q",
        "ejemplo": "Problema 1: Un hidrogenerador de polos salientes de 150 MVA, 18 kV, 60 Hz conectado a red infinita de 18 kV (V_t = 18 / sqrt(3) = 10,392 V fase-neutro) tiene una reactancia de eje directo X_d = 1.10 p.u. (110% de base) y una reactancia de eje en cuadratura X_q = 0.70 p.u. (70% de base), con resistencia estatórica despreciable. Impedancia base del sistema: Z_base = V_linea^2 / S_base = (18,000)^2 / 150,000,000 = 324,000,000 / 150,000,000 = 2.16 ohms. En unidades físicas: X_d = 1.10 * 2.16 = 2.376 ohms; X_q = 0.70 * 2.16 = 1.512 ohms. Excitación ajustada de modo que la tensión interna de eje directo sea E_f = 1.25 p.u. (1.25 * 10,392 = 12,990 V fase-neutro). Ecuación analítica de potencia de Blondel en por unidad (p.u.): P(delta) = [(E_f * V_t) / X_d] * sin(delta) + [(V_t^2 / 2) * (1/X_q - 1/X_d)] * sin(2*delta) = [(1.25 * 1.0) / 1.10] * sin(delta) + [(1.0^2 / 2) * (1/0.70 - 1/1.10)] * sin(2*delta) = 1.1364 * sin(delta) + [0.5 * (1.4286 - 0.9091)] * sin(2*delta) = 1.1364 * sin(delta) + [0.5 * 0.5195] * sin(2*delta) = 1.1364 * sin(delta) + 0.2597 * sin(2*delta) p.u. Para un ángulo de carga operativo delta = 30°: Componente electromagnética de campo principal: P_campo = 1.1364 * sin(30°) = 1.1364 * 0.5 = 0.5682 p.u. Componente de torque de reluctancia: P_reluctancia = 0.2597 * sin(2 * 30°) = 0.2597 * sin(60°) = 0.2597 * 0.8660 = 0.2249 p.u. Potencia activa total entregada: P_total = 0.5682 + 0.2249 = 0.7931 p.u. = 0.7931 * 150 MW = 118.97 MW. Nótese que el torque de reluctancia aporta el 28.3% de la potencia total entregada en ese punto. Si la excitación de campo se perdiera completamente por fallo del regulador AVR (E_f = 0), el generador continuaría entregando hasta P_rel,max = 0.2597 p.u. (38.95 MW) de potencia a delta = 45° únicamente por la saliencia magnética del rotor, antes de perder el sincronismo por completo. Problema 2: El ángulo de máxima potencia en máquinas de polos salientes se desplaza desde 90° hacia aproximadamente 70°-75° debido a la influencia armónica del término sin(2*delta).",
        "bloque_sugerido": "Polos Salientes 45 min • Teoría de las dos reacciones de Blondel y par de reluctancia",
        "slides": [
            {
                "numero": 1,
                "seccion": "ANISOTROPÍA MAGNÉTICA DEL ROTOR",
                "titulo": "Ejes Directo (d) y en Cuadratura (q)",
                "puntos": [
                    "En rotores de polos salientes, el entrehierro no es uniforme; es mínimo en el eje del polo (eje d) y máximo entre polos (eje q).",
                    "La reluctancia en el eje q es mucho mayor que en el eje d; por tanto, la reactancia síncrona satisface siempre X_d > X_q.",
                    "André Blondel formuló la resolución descomponiendo la corriente del estator en dos componentes ortogonales I_a = I_d + I_q."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL COMPONENTE DE RELUCTANCIA",
                "titulo": "El Doble Término de Potencia sin(2*delta)",
                "puntos": [
                    "El término de potencia principal P_1 ~ sin(delta) depende de la corriente de excitación del rotor (E_f).",
                    "El término de reluctancia P_2 ~ sin(2*delta) es independiente de la excitación; existe incluso con excitación nula.",
                    "Aumenta la rigidez sincronizante del generador, haciendo a las hidroeléctricas más estables dinámicamente que los turbogeneradores."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sincronización y Paralelo de Generadores: Condiciones, Estatismo y Curvas en V",
        "objetivo": "Diseñar procedimientos de sincronización manual y automática mediante sincronoscopio y sincronizadores automáticos, regulando el reparto de potencia activa por estatismo (droop) y potencia reactiva por Curvas en V.",
        "concepto_clave_latex": r"\text{Estatismo}: s_p = \frac{f_{\text{vacío}} - f_{\text{plena}}}{f_{\text{plena}}} \times 100\% \quad ; \quad P = \frac{f_{\text{vacío}} - f_{\text{red}}}{s_p / P_{nom}}",
        "ejemplo": "Problema 1: Dos generadores síncronos operan en paralelo en una micro-red aislada de una isla para abastecer una carga combinada de potencia activa total P_L = 12.0 MW a frecuencia de red f_red = 60.0 Hz. Generador 1: Capacidad nominal P_n1 = 10 MW con estatismo de velocidad del regulador de turbina del s_p1 = 4.0% (0.04). Frecuencia en vacío f_nl,1 = 61.5 Hz. Generador 2: Capacidad nominal P_n2 = 8 MW con estatismo del s_p2 = 3.0% (0.03). Frecuencia en vacío f_nl,2 = 61.2 Hz. Ecuaciones de estatismo de gobernación de cada generador: Pendiente de caída 1: R_1 = (s_p1 * f_nom) / P_n1 = (0.04 * 60) / 10 = 2.4 / 10 = 0.24 Hz/MW. Pendiente de caída 2: R_2 = (s_p2 * f_nom) / P_n2 = (0.03 * 60) / 8 = 1.8 / 8 = 0.225 Hz/MW. Las potencias entregadas se relacionan con la frecuencia común del sistema f_sys por: P_1 = (f_nl,1 - f_sys) / R_1 = (61.5 - f_sys) / 0.24; P_2 = (f_nl,2 - f_sys) / R_2 = (61.2 - f_sys) / 0.225. Condición de balance de potencia activa de la micro-red: P_1 + P_2 = P_L = 12.0 MW. Sustituyendo: (61.5 - f_sys) / 0.24 + (61.2 - f_sys) / 0.225 = 12.0 ==> 4.1667 * (61.5 - f_sys) + 4.4444 * (61.2 - f_sys) = 12.0 ==> (256.25 - 4.1667 f_sys) + (272.0 - 4.4444 f_sys) = 12.0 ==> 528.25 - 8.6111 f_sys = 12.0 ==> 8.6111 f_sys = 516.25 ==> f_sys = 516.25 / 8.6111 = 59.952 Hz. Potencia despachada por el Generador 1: P_1 = (61.5 - 59.952) / 0.24 = 1.548 / 0.24 = 6.45 MW (64.5% de su capacidad). Potencia despachada por el Generador 2: P_2 = (61.2 - 59.952) / 0.225 = 1.248 / 0.225 = 5.55 MW (69.4% de su capacidad). Suma total: 6.45 + 5.55 = 12.00 MW. Si la carga aumenta bruscamente en 2 MW (a 14 MW), la frecuencia cae automáticamente y ambos gobernadores aumentan su potencia según sus pendientes sin necesidad de comunicación por telecomunicaciones. Curvas en V: Al variar la corriente de excitación I_f con potencia activa constante P, la corriente de armadura I_a describe una curva en V con un mínimo en factor de potencia unitario; subexcitar el generador absorbe reactivos y sobreexcitarlo inyecta reactivos para sostener el voltaje. Problema 2: En la maniobra de sincronización manual con lámparas apagadas (dark lamp method), el interruptor de acoplamiento solo debe cerrarse cuando las tres lámparas conectadas entre fases homólogas están completamente apagadas y la aguja del sincronoscopio rota lentamente en sentido horario hacia las 12 en punto.",
        "bloque_sugerido": "Paralelo y Sincronización 45 min • Reparto de carga por estatismo de velocidad y Curvas en V",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONDICIONES DE SINCRONIZACIÓN A RED",
                "titulo": "Las 4 Magnitudes que Deben Coincidir",
                "puntos": [
                    "1. Misma tensión de línea eficaz (V_gen = V_red, verificada por voltímetros duales).",
                    "2. Misma frecuencia fundamental (f_gen approx f_red, con un deslizamiento < 0.05 Hz).",
                    "3. Misma secuencia de fases (A-B-C, comprobada con fasímetro de rotación).",
                    "4. Mismo ángulo de fase instantáneo (desfase Delta_theta = 0°, indicado por el sincronoscopio a las 12)."
                ]
            },
            {
                "numero": 2,
                "seccion": "GOBERNACIÓN POR ESTATISMO (DROOP)",
                "titulo": "Reparto Autónomo de Potencia Activa",
                "puntos": [
                    "El estatismo de velocidad es una característica descendente intencional de la turbina: a mayor potencia, menor frecuencia.",
                    "Permite que múltiples generadores compartan aumentos de demanda en paralelo de forma natural y estable sin 'cazar' oscilaciones.",
                    "Base de la Regulación Primaria de Frecuencia exigida por el Código de Redes a nivel nacional."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Generador de Inducción Doblemente Alimentado (DFIG) en Turbinas Eólicas",
        "objetivo": "Modelar la máquina asíncrona de rotor bobinado doblemente alimentada (DFIG), calculando el flujo de potencia bidireccional por rotor y estator en regímenes subsíncrono y supersíncrono.",
        "concepto_clave_latex": r"P_{\text{rotor}} = -s P_{\text{estator}} \quad ; \quad P_{\text{mec}} = P_{\text{estator}} + P_{\text{rotor}} = (1 - s) P_{\text{estator}}",
        "ejemplo": "Problema 1: Una turbina eólica de 2.0 MW instala un generador de inducción doblemente alimentado (DFIG) de 4 polos, 690 V (estator conectado directamente a la red de 60 Hz, n_s = 1800 rpm). El rotor bobinado se conecta a la red a través de un convertidor electrónico de potencia bidireccional 'Back-to-Back' (RSC + GSC con enlace de corriente continua) dimensionado al 30% de la capacidad nominal de la máquina (600 kVA). Rango de velocidad variable del generador: +-25% respecto a la velocidad síncrona (de 1350 rpm a 2250 rpm, rango de deslizamiento s in [+0.25, -0.25]): 1) Régimen Supersíncrono (Viento alto, n_r = 2160 rpm, 20% por encima de la síncrona): Deslizamiento s = (1800 - 2160) / 1800 = -360 / 1800 = -0.20 (negativo). Potencia mecánica capturada por el rotor eólico: P_mec = 2000 kW (2.0 MW). Balance de potencia: P_mec = P_estator + P_rotor = P_estator + (-s * P_estator) = (1 - s) * P_estator = [1 - (-0.20)] * P_estator = 1.20 * P_estator. Potencia eléctrica entregada por el estator a la red: P_estator = 2000 kW / 1.20 = 1666.67 kW. Potencia entregada por el rotor a través del convertidor back-to-back: P_rotor = -s * P_estator = -(-0.20) * 1666.67 kW = +333.33 kW. Potencia total inyectada a la red eléctrica: P_total = P_estator + P_rotor = 1666.67 + 333.33 = 2000 kW (tanto el estator como el rotor inyectan potencia simultáneamente a la red; el convertidor opera extrayendo energía del rotor). 2) Régimen Subsíncrono (Viento bajo, n_r = 1530 rpm, s = +0.15): P_mec = 800 kW. P_estator = 800 / (1 - 0.15) = 800 / 0.85 = 941.18 kW. Potencia del rotor: P_rotor = -s * P_estator = -0.15 * 941.18 = -141.18 kW (potencia negativa: el convertidor absorbe 141.18 kW de la red y los inyecta al rotor a frecuencia de deslizamiento f_r = s * 60 = 9 Hz para mantener el campo magnético giratorio sincronizado a 60 Hz en el estator). Potencia neta entregada a la red: 941.18 - 141.18 = 800 kW. Ventaja económica revolucionaria: Se logra control de velocidad variable completa en un rango del +-25% con un convertidor electrónico de solo 600 kVA (30% del costo y tamaño de un convertidor de plena potencia 'Full-Converter' de 2000 kVA). Problema 2: Ante fallas severas de cortocircuito en la red que inducen picos de sobretensión en el rotor, el circuito de protección Crowbar (resistencia de frenado en cortocircuito) se dispara en microsegundos para proteger los transistores IGBT del convertidor RSC.",
        "bloque_sugerido": "Tecnología Eólica DFIG 45 min • Flujo de potencia bidireccional subsíncrono/supersíncrono y Crowbar",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURA DE GENERADORES EÓLICOS TIPO 3",
                "titulo": "La Máquina Asíncrona Doblemente Alimentada",
                "puntos": [
                    "El estator se conecta directamente a la red a 60 Hz y entrega la mayor parte de la energía (~70-75%).",
                    "El rotor se alimenta a frecuencia y fase variable mediante un convertidor bidireccional AC/DC/AC (Back-to-Back).",
                    "Permite desacoplar la velocidad mecánica del viento de la frecuencia fija de la red eléctrica nacional."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPERACIÓN SUBSÍNCRONA VS SUPERSÍNCRONA",
                "titulo": "La Dirección del Flujo de Potencia del Rotor",
                "puntos": [
                    "Régimen Subsíncrono (s > 0): El rotor absorbe potencia de la red para excitar el campo a baja velocidad.",
                    "Régimen Supersíncrono (s < 0): El rotor genera y entrega potencia adicional a la red sumada a la del estator.",
                    "Capacidad de control de factor de potencia independiente: inyecta o absorbe reactivos para soporte de red."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Generadores Síncronos de Imanes Permanentes (PMSG) y Accionamiento Directo (Direct-Drive)",
        "objetivo": "Modelar generadores síncronos de imanes permanentes (PMSG) para turbinas eólicas de accionamiento directo (Direct-Drive sin caja multiplicadora), evaluando topologías de flujo radial y convertidores de plena potencia.",
        "concepto_clave_latex": r"E_f = \omega_e \psi_{pm} \quad ; \quad T_e = \frac{3}{2} p [ \psi_{pm} i_q + (L_d - L_q) i_d i_q ] \quad ; \quad \text{Tipo 4}: \text{Full Converter}",
        "ejemplo": "Problema 1: Una turbina eólica marina (Offshore) de 6.0 MW opera con un generador síncrono de imanes permanentes de accionamiento directo (Direct-Drive PMSG sin multiplicadora de engranajes). Como las palas giran lentamente a n_r = 10 rpm nominales para no superar la velocidad sónica en la punta, el generador debe tener un elevado número de polos para generar a frecuencia eléctrica adecuada: Se diseña un estator multipolar con P = 120 polos (p = 60 pares de polos). Frecuencia eléctrica generada a velocidad nominal: f_e = (P * n) / 120 = (120 * 10) / 120 = 10.0 Hz (frecuencia variable de 0 a 12 Hz según el viento). Enlace de flujo magnético de los imanes de tierras raras de Neodimio-Hierro-Boro (NdFeB grado N42SH con inducción remanente B_r = 1.30 T): psi_pm = 95.0 Weber-vuelta. Velocidad angular mecánica del rotor: omega_m = (2 * pi * 10) / 60 = 1.0472 rad/s. Velocidad angular eléctrica: omega_e = p * omega_m = 60 * 1.0472 = 62.83 rad/s. Tensión inducida por fase en circuito abierto (FCEM): E_f = omega_e * psi_pm = 62.83 * 95.0 = 5969 V fase-neutro (tensión de línea E_f,linea = sqrt(3) * 5969 = 10,338 V = 10.34 kV). Torque electromagnético nominal requerido en el eje para absorber los 6.0 MW a 10 rpm: T_nom = P_mec / omega_m = 6,000,000 W / 1.0472 rad/s = 5,729,564 N*m = 5.73 MegaNewtons-metro (un torque colosal que exige un generador de gran diámetro, D_estator = 6.8 metros). Corriente de eje en cuadratura requerida bajo control i_d = 0 (máximo torque por amperio MTPA en rotor de polos lisos L_d = L_q): T_e = 1.5 * p * psi_pm * i_q ==> 5,729,564 = 1.5 * 60 * 95.0 * i_q ==> 5,729,564 = 8550 * i_q ==> i_q = 5,729,564 / 8550 = 670.12 A. La energía generada a 10 Hz se canaliza al 100% a través de un convertidor de plena escala 'Full-Converter' (Tipo 4 de 6.0 MW), que rectifica a corriente continua y la reinvierte a 60 Hz exactos con sincronización perfecta a la red de transmisión submarina. Ventaja decisiva en alta mar: Elimina la caja multiplicadora (gearbox), responsable del 42% del tiempo de inactividad por mantenimiento correctivo de aerogeneradores tradicionales, elevando la disponibilidad de la planta al 98.5%. Problema 2: En generadores PMSG, el riesgo de desmagnetización térmica irreversible de los imanes de neodimio exige no superar la temperatura de Curie (T_curie = 310 °C; temperatura máxima de trabajo de 150 °C) monitoreada mediante sensores PT100 en las zapatas.",
        "bloque_sugerido": "Tecnología Eólica PMSG 45 min • Modelado Direct-Drive, imanes NdFeB y convertidores Tipo 4",
        "slides": [
            {
                "numero": 1,
                "seccion": "AEROGENERADORES TIPO 4 DIRECT-DRIVE",
                "titulo": "Eliminación de la Caja Multiplicadora",
                "puntos": [
                    "La caja de engranajes convencional es costosa, pesada y la mayor fuente de fallas catastróficas en parques offshore.",
                    "Accionamiento Directo: El rotor eólico se acopla directamente al eje del generador síncrono multipolo.",
                    "Exige un diámetro físico grande (6 a 8 metros) y cientos de polos para compensar las bajas revoluciones (8-15 rpm)."
                ]
            },
            {
                "numero": 2,
                "seccion": "IMANES DE TIERRAS RARAS (NdFeB)",
                "titulo": "Densidad de Potencia y Desafíos Críticos",
                "puntos": [
                    "Los imanes de Neodimio-Hierro-Boro aportan un campo B masivo sin consumir corriente de excitación en el rotor.",
                    "Eficiencia eléctrica superior al 97.5% debido a la eliminación total de pérdidas de cobre en el rotor (P_cu,rotor = 0).",
                    "Cadena de suministro y riesgo geopolítico: El 70% de la extracción y refinación de tierras raras está concentrada en Asia."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Motores Especiales de Reluctancia Síncrona (SynRM) y Brushless DC (BLDC) en Movilidad Eléctrica",
        "objetivo": "Modelar motores de reluctancia síncrona asistidos por imanes (PM-SynRM) y motores sin escobillas BLDC, calculando la relación de saliencia Ld/Lq y el accionamiento por conmutación electrónica trapezoidal.",
        "concepto_clave_latex": r"\text{SynRM}: \xi = \frac{L_d}{L_q} \ge 8 - 12 \quad ; \quad T_e = \frac{3}{2} p (L_d - L_q) i_d i_q \quad ; \quad \text{BLDC}: E = 2 B l v N",
        "ejemplo": "Problema 1: Un vehículo eléctrico compacto utiliza un motor de reluctancia síncrona (SynRM de 4 polos, P = 4) de 60 kW para tracción urbana, diseñado sin imanes de tierras raras (reducción de costo de materiales y huella ambiental). El rotor se lamina con barreras de flujo magnético en forma de arco (flux barriers) que maximizan el flujo en el eje directo y estrangulan el paso de líneas de campo en el eje en cuadratura, logrando una relación de anisotropía de inductancias de saliencia xi = L_d / L_q = 42.0 mH / 4.2 mH = 10.0 (L_d = 0.042 H, L_q = 0.0042 H). Para entregar un torque electromagnético de aceleración de T_e = 220 N*m con la máxima eficiencia energética por amperio (MTPA - Maximum Torque Per Ampere, cuya condición analítica para un motor de reluctancia pura sin imanes es orientar el vector de corriente a un ángulo de fase gamma = 45° respecto al eje d, es decir, i_d = i_q): Ecuación de torque de reluctancia: T_e = 1.5 * p * (L_d - L_q) * i_d * i_q ==> Con p = 2 y haciendo i_d = i_q = I_m / sqrt(2): T_e = 1.5 * 2 * (L_d - L_q) * (I_m / sqrt(2))^2 = 3 * (0.042 - 0.0042) * (I_m^2 / 2) = 3 * 0.0378 * 0.5 * I_m^2 = 0.0567 * I_m^2. Despejando la amplitud de la corriente estatórica requerida: I_m = sqrt(T_e / 0.0567) = sqrt(220 / 0.0567) = sqrt(3880.07) = 62.29 A. Corrientes de eje: i_d = i_q = 62.29 / sqrt(2) = 44.05 A. Pérdidas en el rotor: Dado que el rotor de reluctancia no tiene devanados de cobre ni jaula de ardilla, sus pérdidas por efecto Joule son exactamente CERO (P_cu,rotor = 0), permitiendo que el motor alcance una clase de eficiencia energética ultra-alta IE5 ('Ultra-Premium Efficiency') con temperaturas de cojinetes significativamente más frías que un motor de inducción equivalente. Problema 2: En motores Brushless DC (BLDC) con FCEM trapezoidal de 120° planos, la conmutación electrónica de seis pasos (Six-Step Inverter) utiliza 3 sensores de efecto Hall para alimentar únicamente dos de las tres fases en cada intervalo de 60° eléctricos.",
        "bloque_sugerido": "Motores para Movilidad 45 min • Reluctancia síncrona SynRM clase IE5 y motores BLDC de 6 pasos",
        "slides": [
            {
                "numero": 1,
                "seccion": "MOTORES LIBRES DE TIERRAS RARAS",
                "titulo": "La Revolución del SynRM (IE5 Ultra-Premium)",
                "puntos": [
                    "El motor SynRM no utiliza imanes de neodimio ni devanados en el rotor; su rotor es puro acero laminado con barreras de aire.",
                    "Funciona exclusivamente por el principio de alineamiento de mínima reluctancia magnética.",
                    "Al no tener pérdidas Joule en el rotor, supera la eficiencia de los motores de inducción tradicionales en más de un 3% a 5%."
                ]
            },
            {
                "numero": 2,
                "seccion": "MOTORES BRUSHLESS DC (BLDC)",
                "titulo": "Accionamiento Electrónico Trapezoidal",
                "puntos": [
                    "Rotor con imanes permanentes superficiales y estator con bobinado concentrado que produce FCEM trapezoidal plana.",
                    "Control de 6 pasos (Six-Step): Sencillo y robusto; conmuta dos fases a la vez guiado por sensores Hall digitales.",
                    "Dominante en drones, bicicletas eléctricas, patinetas de micromovilidad y ventilación de bajo consumo."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ensayos Térmicos y Calentamiento en Máquinas Eléctricas (IEC 60034-1 y NEMA)",
        "objetivo": "Calcular la elevación de temperatura transitoria y en régimen permanente en máquinas eléctricas, seleccionando clases de aislamiento térmico normalizadas (B, F, H) y métodos de enfriamiento IC.",
        "concepto_clave_latex": r"\Delta T(t) = \Delta T_{ss} \left( 1 - e^{-t/\tau_{th}} \right) \quad ; \quad \tau_{th} = \frac{C_{th}}{R_{th}^{-1}} = \frac{m c_p}{h A_s} \quad ; \quad \text{Clase F}: 155^\circ\text{C}",
        "ejemplo": "Problema 1: Un motor de inducción trifásico de 75 kW totalmente cerrado enfriado por ventilador exterior montado sobre el eje (TEFC - código de refrigeración IC 411 según IEC 60034-6) tiene una masa total de cobre y hierro de m = 480 kg (calor específico promedio ponderado c_p = 450 J/(kg*K), capacidad térmica global C_th = m * c_p = 480 * 450 = 216,000 J/K). Pérdidas totales disipadas en calor a plena carga continua (S1): P_loss = P_fe + P_cu + P_mec = 1100 + 3400 + 500 = 5000 W (5.0 kW térmicos). El coeficiente global de transferencia de calor hacia el aire forzado exterior a través de la carcasa aleteada es h * A_s = 62.5 W/K (resistencia térmica equivalente R_th = 1 / 62.5 = 0.016 K/W). 1) Elevación de temperatura en régimen permanente sobre el ambiente: Delta_T_ss = P_loss * R_th = 5000 * 0.016 = 80.0 °C (80 Kelvin). Constante de tiempo térmica de la máquina: tau_th = C_th * R_th = 216,000 * 0.016 = 3456 segundos = 57.6 minutos (aproximadamente 1 hora). 2) Verificación de Clase de Aislamiento térmico: Operando en una sala de máquinas con temperatura ambiente de diseño de T_amb = 40 °C, la temperatura final de los devanados en régimen permanente será: T_devanados = T_amb + Delta_T_ss = 40 + 80 = 120.0 °C. Se especifica aislamiento térmico de Clase F (temperatura máxima admisible de 155 °C según IEC 60034-1, compuesta por 40 °C ambiente + 105 °C de elevación por ensayo de resistencia + 10 °C de margen por punto caliente hot-spot). Margen de seguridad térmico remanente: Margen = 155 - 120 = 35 °C. Regla de Montsinger / Arrhenius de envejecimiento térmico del aislamiento: Por cada 10 °C de reducción en la temperatura de operación por debajo del límite de la clase de aislamiento, la vida útil del barniz dieléctrico se DUPLICA. Como el motor opera a 120 °C (35 °C por debajo de 155 °C), su vida útil estimada se multiplica por 2^(35/10) = 2^3.5 = 11.3 veces respecto a la vida nominal de diseño, garantizando más de 30 años de operación ininterrumpida. Problema 2: En régimen de servicio intermitente periódico S3 (arranque-parada frecuente en grúas), la constante de tiempo térmica de enfriamiento en parada (tau_enfriamiento) es 3 a 4 veces mayor que la de marcha debido a la detención del ventilador.",
        "bloque_sugerido": "Termodinámica de Máquinas 45 min • Curvas de calentamiento exponencial, clases IEC B/F/H y códigos IC",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITES TÉRMICOS DE LOS AISLAMIENTOS",
                "titulo": "Clases Normalizadas NEMA e IEC",
                "puntos": [
                    "Clase A: 105 °C (obsoleta; algodones y sedas impregnadas).",
                    "Clase B: 130 °C (motores estándar antiguos; mica y fibra de vidrio).",
                    "Clase F: 155 °C (el estándar universal moderno de la industria petroquímica y minera).",
                    "Clase H: 180 °C (aplicaciones severas y tracción; elastómeros de silicona y resinas avanzadas)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CÓDIGOS DE REFRIGERACIÓN IEC 60034-6",
                "titulo": "De Enfriamiento Abierto a Circuito Cerrado",
                "puntos": [
                    "IC 01: Abierto autoventilado; el aire circula libremente por el interior de los bobinados.",
                    "IC 411 (TEFC): Totalmente cerrado enfriado por ventilador exterior acoplado al eje.",
                    "IC 616: Intercambiador de calor aire-aire forzado independiente; para motores de alta potencia en ambientes corrosivos.",
                    "IC 81W: Intercambiador de calor agua-aire integrado en grandes hidrogeneradores."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Protección de Máquinas Eléctricas: Relés Diferenciales (87), Pérdida de Campo (40) y Buchholz",
        "objetivo": "Diseñar el esquema de protecciones eléctricas integrales para generadores y transformadores de potencia, parametrizando relés numéricos de protección diferencial (87G/87T), pérdida de excitación (40) y fallas internas Buchholz (63).",
        "concepto_clave_latex": r"I_{\text{diff}} = |I_1 - I_2| > k \cdot I_{\text{rest}} \quad ; \quad \text{Relé 40}: \text{Círculo en Plano R-X (Offset Mho)}",
        "ejemplo": "Problema 1: Se ajusta el relé de protección diferencial porcentual con doble pendiente (ANSI 87T) para un transformador elevador de subestación de 40 MVA, 13.8 / 115 kV, conexión Dyn11. Corrientes nominales: Lado baja tensión (13.8 kV): I_n1 = 40,000 / (sqrt(3) * 13.8) = 1673.5 A (se instalan TCs de 2000/5 A, corriente secundaria a plena carga I_s1 = 1673.5 * 5 / 2000 = 4.184 A); Lado alta tensión (115 kV): I_n2 = 40,000 / (sqrt(3) * 115) = 200.8 A (se instalan TCs de 250/5 A, corriente secundaria a plena carga I_s2 = 200.8 * 5 / 250 = 4.016 A). El relé digital compensa internamente la diferencia de relación de TCs y el desfase de 30° de la conexión Dyn11 igualando los fasores a 1.0 p.u. Parámetros de la curva de disparo diferencial: Corriente de arranque mínima (Pickup) I_diff,min = 0.20 p.u.; Pendiente 1 (Slope 1) = 30% (para corrientes de restricción de hasta 2.0 p.u., absorbiendo errores de saturación y cambiador de tomas bajo carga LTC); Pendiente 2 (Slope 2) = 70% (para corrientes de restricción > 2.0 p.u.). Durante un cortocircuito exterior en una línea de 115 kV (Through-Fault de 12 kA), la corriente de restricción es de 6.0 p.u. y los errores de los TCs generan una corriente diferencial espuria de I_diff = 0.45 p.u. La corriente de disparo requerida por la curva en esa zona es I_trip = 0.20 + 0.30*(2.0) + 0.70*(6.0 - 2.0) = 0.20 + 0.60 + 2.80 = 3.60 p.u. Como 0.45 p.u. < 3.60 p.u., el relé bloquea el disparo (estabilidad ante fallas pasantes externas garantizada). Si ocurre una falla interna entre espiras dentro de la cuba del transformador (I_diff = 4.2 p.u., I_rest = 2.5 p.u.), el relé dispara los interruptores de BT y AT en 25 milisegundos. Problema 2: En generadores síncronos, el relé de pérdida de campo (ANSI 40) monitorea la impedancia compleja en el plano R-X; si la excitación falla, la máquina absorbe reactivos y la trayectoria de impedancia entra en la característica circular Mho desplazada (Offset Mho con diámetro X_d y desplazamiento -X_d'/2), ordenando el disparo antes de que el rotor se sobrecaliente como generador de inducción.",
        "bloque_sugerido": "Protecciones Eléctricas 45 min • Relé diferencial porcentual 87, pérdida de campo 40 y relé Buchholz",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROTECCIÓN DIFERENCIAL NUMÉRICA",
                "titulo": "La Primera Línea de Defensa (ANSI 87)",
                "puntos": [
                    "Aplica el primer principio de Kirchhoff: la corriente que entra al equipo debe ser exactamente igual a la que sale.",
                    "Protección de Zona Unitaria: Extremadamente rápida y selectiva; no requiere coordinación de tiempos con otras protecciones.",
                    "Restricción de 2do armónico: Bloquea el disparo en frío durante la energización del transformador ante corrientes de inrush (I_2nd > 15%)."
                ]
            },
            {
                "numero": 2,
                "seccion": "PROTECCIONES PROPIAS DEL GENERADOR",
                "titulo": "Pérdida de Excitación (40) y Buchholz (63)",
                "puntos": [
                    "Relé Buchholz (63): Instalado en la tubería hacia el tanque conservador; detecta desprendimiento de gases por fallas de arco en aceite.",
                    "Relé de Pérdida de Campo (40): Protege el generador si se desconecta el puente rectificador de excitación.",
                    "Sobrecorriente con restricción de tensión (51V): Discrimina cortocircuitos reales de sobrecargas pesadas transitorias."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Diagnóstico y Mantenimiento Predictivo: Análisis de Firma de Corriente (MCSA) y Descargas Parciales",
        "objetivo": "Diagnosticar fallas incipientes en máquinas eléctricas en operación (barras rotas en jaula de ardilla, excentricidad de entrehierro y degradación dieléctrica) mediante MCSA, vibraciones y descargas parciales (PD).",
        "concepto_clave_latex": r"f_{sideband} = f_1 (1 \pm 2s) \quad [\text{Barras Rotas MCSA}] \quad ; \quad f_{ecc} = f_1 \left[ \left( k R \pm n_d \right) \frac{1-s}{p} \pm \nu \right]",
        "ejemplo": "Problema 1: Un motor de inducción trifásico de 250 kW, 4160 V, 60 Hz, 4 polos (n_s = 1800 rpm) que acciona una bomba de alimentación de agua de caldera opera a plena carga con deslizamiento s = 0.022 (2.2%, f_1 = 60 Hz). Durante la inspección predictiva periódica de confiabilidad, se registra la corriente del estator de una fase con una pinza de corriente de precisión conectada a un analizador de espectro de transformada rápida de Fourier (FFT con resolución de 0.01 Hz). Análisis de Firma de Corriente del Motor (MCSA - Motor Current Signature Analysis): El espectro FFT de la corriente revela la presencia de dos bandas laterales simétricas prominentes alrededor del pico fundamental de 60.0 Hz ubicadas exactamente en las frecuencias: f_sideband = f_1 * (1 +- 2*s) = 60.0 * (1 +- 2 * 0.022) = 60.0 * (1 +- 0.044) ==> f_inferior = 60.0 * 0.956 = 57.36 Hz; f_superior = 60.0 * 1.044 = 62.64 Hz. La amplitud del pico fundamental a 60 Hz es de A_fund = 0 dB (38 A). La amplitud de la banda lateral inferior a 57.36 Hz se mide en A_sb = -34 dB. Criterio de severidad de barras rotas de jaula de ardilla (Norma IEEE / EPRI): Diferencia Delta_dB = A_fund - A_sb = 0 - (-34) = 34 dB. Tabla de diagnóstico MCSA: Delta_dB > 54 dB: Rotor excelente en perfecto estado; 45 < Delta_dB < 54 dB: Degradación inicial o alta resistencia en anillo de cortocircuito; 36 < Delta_dB < 45 dB: Una barra rota confirmada; 30 < Delta_dB < 36 dB: Dos o más barras rotas contiguas con alto riesgo de rotura catastrófica en cadena y desgarro del entrehierro. Diagnóstico: Con 34 dB de diferencia, el motor tiene al menos dos barras de rotor fracturadas. Se programa de inmediato el paro del motor para el siguiente fin de semana para rebobinar el rotor en taller especializado antes de que los fragmentos de barra salgan despedidos centrífugamente y destruyan el devanado de 4160 V del estator. Problema 2: En transformadores y generadores de media y alta tensión, la monitorización continua de Descargas Parciales (PD) mediante sensores UHF y de corriente de alta frecuencia (HFCT) detecta la formación de árboles eléctricos (electrical treeing) en el aislamiento de resina epoxi epóxica antes de que ocurra la perforación dieléctrica total.",
        "bloque_sugerido": "Diagnóstico Predictivo MCSA 45 min • Detección de barras rotas f1(1+-2s), vibraciones y descargas parciales",
        "slides": [
            {
                "numero": 1,
                "seccion": "MANTENIMIENTO PREDICTIVO NO INVASIVO",
                "titulo": "La Firma Eléctrica del Motor (MCSA)",
                "puntos": [
                    "Aprovecha las propias fases del motor como transductores mecánicos sin detener la máquina ni montar sensores en partes móviles.",
                    "Cualquier asimetría en el rotor o entrehierro modula la inductancia mutua, induciendo bandas laterales en el espectro de corriente.",
                    "Permite detectar barras rotas, excentricidad estática/dinámica, desbalance de fases y holguras mecánicas de cojinetes."
                ]
            },
            {
                "numero": 2,
                "seccion": "MONITOREO DE CONDICIÓN DIELÉCTRICA",
                "titulo": "Descargas Parciales (PD) y Análisis de Aceite",
                "puntos": [
                    "Descargas Parciales: Pequeñas chispas microscópicas que ocurren dentro de burbujas o microvacíos del aislamiento sólido o líquido.",
                    "Análisis de Gases Disueltos (DGA en transformadores): Triángulo de Duval y ratios de Rogers para identificar arcos, sobrecalentamiento térmico o descargas de corona.",
                    "Sustenta la transición de mantenimiento preventivo basado en tiempo a Mantenimiento Basado en Condición (CBM)."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Máquinas Eléctricas Especiales y Tendencias: Motores de Flujo Axial y Superconductores",
        "objetivo": "Evaluar las tecnologías de vanguardia en máquinas eléctricas: topologías de flujo axial (AFPM) para vehículos eléctricos de alto par y generadores con devanados superconductores de alta temperatura (HTS).",
        "concepto_clave_latex": r"\text{Flujo Axial (AFPM)}: T_e = \pi B_{avg} A_{in} (R_{ext}^2 - R_{int}^2) R_{avg} \quad ; \quad \text{Densidad}: > 30 \text{ kW/kg} \text{ (vs 4-6 en Radial)}",
        "ejemplo": "Problema 1: Un fabricante de hiperdeportivos y aeronaves de despegue y aterrizaje vertical eléctrico (eVTOL) compara un motor convencional de flujo radial (RFPM, masa M_radial = 35 kg, par máximo = 420 N*m, densidad de torque = 12 N*m/kg) frente a un motor síncrono de flujo axial de doble rotor y estator central sin núcleo ferromagnético (YASA - Yokeless and Segmented Armature AFPM, diámetro exterior R_ext = 0.14 m, radio interior R_int = 0.09 m, radio medio R_avg = 0.115 m): En la máquina de flujo axial, las líneas de campo magnético viajan paralelamente al eje de rotación (axialmente) en lugar de perpendicularmente (radialmente). Amplitud de inducción magnética en el entrehierro axial: B_avg = 1.15 Tesla. Densidad lineal de corriente eléctrica en la corona: A_in = 65,000 A/m. 1) Par electromagnético generado por el motor de flujo axial: T_e = pi * B_avg * A_in * (R_ext^2 - R_int^2) * R_avg = pi * 1.15 * 65,000 * (0.14^2 - 0.09^2) * 0.115 = 234,834 * (0.0196 - 0.0081) * 0.115 = 234,834 * 0.0115 * 0.115 = 310.5 N*m. En configuración de doble rotor (un rotor a cada lado del estator): T_total = 2 * 310.5 = 621.0 N*m de par continuo. 2) La masa total del motor AFPM ensamblado es de solo M_axial = 18.5 kg. Densidad volumétrica de par: 621.0 / 18.5 = 33.57 N*m/kg (casi el triple que el motor tradicional de flujo radial). Potencia continua a 6000 rpm (omega = 628.3 rad/s): P = T * omega = 621 * 628.3 = 390.1 kW (523 HP). Densidad gravimétrica de potencia: 390.1 kW / 18.5 kg = 21.08 kW/kg (frente a 4.5 kW/kg del motor radial). La ausencia de yugo de hierro en el estator elimina las pérdidas por histéresis estatórica en el retorno de flujo, permitiendo una eficiencia del 97% en todo el mapa de par-velocidad. Problema 2: En generadores eólicos marinos de 20 MW, los devanados superconductores de alta temperatura (cintas HTS de YBCO enfriadas con helio gaseoso a 30 K) permiten densidades de corriente de 400 A/mm^2 sin resistencia óhmica (R = 0), reduciendo la masa de la nacelle de 450 toneladas a menos de 160 toneladas.",
        "bloque_sugerido": "Máquinas de Vanguardia 45 min • Motores de flujo axial YASA y superconductores HTS para aviación",
        "slides": [
            {
                "numero": 1,
                "seccion": "FRONTERAS DEL DISEÑO ELECTROMECÁNICO",
                "titulo": "Flujo Radial vs Flujo Axial",
                "puntos": [
                    "Flujo Radial (convencional): El campo magnético se desplaza perpendicularmente al eje de giro cilíndrico.",
                    "Flujo Axial (disco / pancake): El campo viaja paralelamente al eje rotativo; el rotor y estator son discos enfrentados.",
                    "La arquitectura de flujo axial maximiza el brazo de palanca del par aprovechando el radio exterior del disco al máximo."
                ]
            },
            {
                "numero": 2,
                "seccion": "SUPERCONDUCTIVIDAD Y AVIACIÓN ELÉCTRICA",
                "titulo": "El Futuro HTS (High Temperature Superconductors)",
                "puntos": [
                    "Cintas superconductoras YBCO operando a temperaturas de nitrógeno líquido (-196 °C / 77 K).",
                    "Resistencia eléctrica nula: Pérdidas por efecto Joule cero en el devanado; campos magnéticos de más de 3 a 5 Teslas.",
                    "Pilar indispensable para la electrificación del transporte aéreo pesado y generadores eólicos marinos de más de 20 MW."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06011840)
    marker = '      - codigo: "05011834"'
    inject_topics_after(marker, yaml_text)
    print("06011840 Máquinas Eléctricas successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
