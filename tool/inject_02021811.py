# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after, format_topics_yaml

topics_02021811 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Segunda Ley de la Termodinámica, Entropía y Límites de Carnot en Máquinas Térmicas",
        "objetivo": "Calcular la eficiencia máxima teórica de Carnot, la generación de entropía en procesos irreversibles y la degradación exergética de fuentes térmicas.",
        "concepto_clave_latex": r"\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H} \quad ; \quad \Delta S = \int \frac{\delta Q_{\text{rev}}}{T} \quad [\text{J/K}] \quad ; \quad S_{\text{gen}} = \Delta S_{\text{sistema}} + \Delta S_{\text{alrededores}} \ge 0",
        "ejemplo": """Problema 1: Una planta de energía solar térmica de concentración con torre central opera su ciclo de vapor entre una fuente caliente a T_H = 560 °C (833.15 K) y un condensador refrigerado por aire a T_C = 35 °C (308.15 K). Calcule la eficiencia térmica teórica de Carnot eta_Carnot. Si la planta absorbe dot{Q}_H = 120 MW_th de calor solar concentrado y entrega una potencia neta real de P_e = 48 MW_e, determine la eficiencia real de la planta eta_real y el porcentaje de aproximación a Carnot.
Paso 1: Eficiencia de Carnot: eta_Carnot = 1 - T_C / T_H = 1 - (308.15 / 833.15) = 1 - 0.36986 = 0.6301 (63.01%).
Paso 2: Eficiencia real: eta_real = P_e / dot{Q}_H = 48 MW / 120 MW = 0.4000 (40.00%).
Paso 3: Eficiencia de segunda ley (relación de Carnot): eta_II = eta_real / eta_Carnot = 0.4000 / 0.6301 = 0.6348 (63.48%).

Problema 2: En un intercambiador de calor mal aislado, se transfieren Q = 500 kJ de calor desde un fluido caliente a T_1 = 500 K hacia un fluido frío a T_2 = 300 K. Calcule la variación de entropía del universo S_gen provocada por esta transferencia irreversible.
Paso 1: Delta S_caliente = -Q / T_1 = -500,000 J / 500 K = -1,000 J/K.
Paso 2: Delta S_frío = +Q / T_2 = +500,000 J / 300 K = +1,666.67 J/K.
Paso 3: Generación neta de entropía: S_gen = Delta S_caliente + Delta S_frío = -1,000 + 1,666.67 = +666.67 J/K > 0.
Paso 4: Esta entropía generada representa la destrucción irreversible de 200 kJ de exergía útil a temperatura ambiente.""",
        "bloque_sugerido": "Resolución Termodinámica 35 min • Balances de entropía y límites de Carnot en ciclos de potencia"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Procesos Politrópicos, Trabajo de Expansión y Compresión en Gases Reales",
        "objetivo": "Evaluar el trabajo y calor transferido en compresores y turbinas de gas mediante la relación politrópica P V^n = constante.",
        "concepto_clave_latex": r"P V^n = \text{const.} \quad ; \quad W_{\text{pol}} = \frac{P_2 V_2 - P_1 V_1}{1 - n} = \frac{m R (T_2 - T_1)}{1 - n} \quad [\text{J}] \quad ; \quad Q = m c_v \left(\frac{n - \gamma}{n - 1}\right)(T_2 - T_1)",
        "ejemplo": """Problema 1: Un compresor industrial comprime m = 0.5 kg de aire (R = 287 J/(kg·K), gamma = 1.40, c_v = 718 J/(kg·K)) desde P_1 = 100 kPa y T_1 = 300 K hasta P_2 = 800 kPa siguiendo un proceso politrópico con índice n = 1.30. Calcule la temperatura final T_2, el trabajo mecánico W suministrado al gas y el calor Q disipado a través de las paredes del cilindro.
Paso 1: Temperatura final politrópica:
T_2 = T_1 (P_2 / P_1)^((n-1)/n) = 300 × (800 / 100)^((1.30 - 1)/1.30) = 300 × (8)^(0.30 / 1.30) = 300 × (8)^(0.23077) = 300 × 1.6154 = 484.62 K (211.5 °C).
Paso 2: Trabajo politrópico de frontera móvil:
W = [m R (T_2 - T_1)] / (1 - n) = [(0.5 kg)(287 J/(kg·K))(484.62 - 300 K)] / (1 - 1.30) = [143.5 × 184.62] / (-0.30) = 26,493 / (-0.30) = -88,310 J = -88.31 kJ (trabajo recibido por el gas).
Paso 3: Calor transferido:
Q = m c_v [(n - gamma) / (n - 1)] (T_2 - T_1) = (0.5)(718) [(1.30 - 1.40) / (1.30 - 1)] (184.62) = 359 × [ -0.10 / 0.30 ] × 184.62 = 359 × (-0.3333) × 184.62 = -22,094 J = -22.09 kJ (calor cedido al refrigerante).

Problema 2: ¿Qué significado físico tiene el caso límite n = 1 y n = gamma?
Paso 1: Cuando n = 1, el proceso es isotérmico reversible (P V = cte, W = m R T ln(V_2/V_1)).
Paso 2: Cuando n = gamma = 1.40, el proceso es adiabático reversible o isentrópico (Q = 0, P V^gamma = cte).""",
        "bloque_sugerido": "Cálculo de Máquinas 35 min • Compresión multietapa con enfriamiento intermedio en almacenamiento de aire (CAES)"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Conducción Térmica Unidimensional: Paredes Compuestas, Resistencia Térmica y Aislamiento",
        "objetivo": "Calcular pérdidas de calor por conducción en régimen estacionario y determinar el radio crítico de aislamiento en tuberías de vapor.",
        "concepto_clave_latex": r"\dot{Q} = \frac{T_{\text{int}} - T_{\text{ext}}}{\sum R_{\text{térmica}}} \quad ; \quad R_{\text{plano}} = \frac{L}{k A} \quad ; \quad R_{\text{cilindro}} = \frac{\ln(r_2 / r_1)}{2\pi k L} \quad ; \quad r_{\text{crítico}} = \frac{k}{h_{\text{ext}}} \quad [\text{m}]",
        "ejemplo": """Problema 1: Una tubería de acero al carbono (k_1 = 45 W/(m·K)) de radio interior r_1 = 50 mm (0.05 m) y radio exterior r_2 = 55 mm (0.055 m) transporta vapor a T_int = 250 °C. Se recubre con una capa de lana mineral aislante (k_2 = 0.040 W/(m·K)) de espesor t = 40 mm (r_3 = 95 mm = 0.095 m). Los coeficientes convectivos son h_int = 800 W/(m²·K) y h_ext = 15 W/(m²·K) hacia el aire ambiente a T_amb = 25 °C. Calcule la pérdida de calor por metro de tubería dot{q}' = dot{Q} / L [W/m].
Paso 1: Resistencias térmicas por unidad de longitud (L = 1 m):
Convección interna: R_conv,int = 1 / (2 pi r_1 h_int) = 1 / (2 pi × 0.05 × 800) = 1 / 251.33 = 0.00398 K/W.
Conducción acero: R_cond,acero = ln(0.055 / 0.050) / (2 pi × 45) = ln(1.10) / 282.74 = 0.09531 / 282.74 = 0.00034 K/W.
Conducción aislante: R_cond,aisl = ln(0.095 / 0.055) / (2 pi × 0.040) = ln(1.7273) / 0.25133 = 0.54654 / 0.25133 = 2.1746 K/W.
Convección externa: R_conv,ext = 1 / (2 pi r_3 h_ext) = 1 / (2 pi × 0.095 × 15) = 1 / 8.9535 = 0.11169 K/W.
Paso 2: Resistencia térmica total:
R_tot = 0.00398 + 0.00034 + 2.1746 + 0.11169 = 2.2906 K/W (el aislante domina el 95% del total).
Paso 3: Pérdida térmica por metro:
dot{q}' = (T_int - T_amb) / R_tot = (250 - 25) / 2.2906 = 225 / 2.2906 = 98.23 W/m.

Problema 2: Calcule el radio crítico de aislamiento r_cr para este sistema y justifique por qué añadir aislante reduce la transferencia de calor.
Paso 1: r_cr = k_aisl / h_ext = 0.040 W/(m·K) / 15 W/(m²·K) = 0.00267 m = 2.67 mm.
Paso 2: Como el radio exterior de la tubería desnuda r_2 = 55 mm es mucho mayor que r_cr (55 mm >> 2.67 mm), cualquier adición de espesor aislante incrementará la resistencia total y reducirá unívocamente las pérdidas de calor.""",
        "bloque_sugerido": "Diseño Térmico 35 min • Resistencia térmica de contacto y espesor económico óptimo de aislamiento"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Convección Térmica: Números Adimensionales (Re, Pr, Nu) y Ley de Enfriamiento de Newton",
        "objetivo": "Correlacionar la transferencia de calor convectiva en placas solares y tubos de calderas calculando coeficientes de película h mediante Nusselt.",
        "concepto_clave_latex": r"\text{Nu} = \frac{h L}{k_f} = f(\text{Re}, \text{Pr}) \quad ; \quad \text{Re} = \frac{\rho v L}{\mu} \quad ; \quad \text{Pr} = \frac{c_p \mu}{k_f} = \frac{\nu}{\alpha} \quad ; \quad \dot{Q} = h A (T_s - T_\infty)",
        "ejemplo": """Problema 1: Aire atmosférico a T_inf = 20 °C fluye con velocidad v = 5.0 m/s paralelamente a la cubierta de vidrio de un colector solar plano de longitud L = 2.0 m y ancho W = 1.0 m (área A = 2.0 m²). La superficie del vidrio se encuentra a T_s = 60 °C. Las propiedades del aire a la temperatura de película T_f = (60 + 20)/2 = 40 °C (313.15 K) son: viscosidad cinemática nu = 1.70 × 10⁻⁵ m²/s, conductividad k_f = 0.0270 W/(m·K), y Pr = 0.71. Determine el número de Reynolds Re_L, el número de Nusselt promedio Nu_L mediante la correlación para flujo combinado laminar-turbulento (Re_cr = 5 × 10⁵): Nu = (0.037 Re^0.8 - 871) Pr^(1/3), el coeficiente convectivo h y la tasa de pérdida de calor dot{Q}.
Paso 1: Reynolds al final de la placa:
Re_L = v L / nu = (5.0 m/s × 2.0 m) / (1.70 × 10⁻⁵ m²/s) = 10.0 / (1.70 × 10⁻⁵) = 5.882 × 10⁵ (supera el umbral crítico, flujo mixto).
Paso 2: Cálculo de Nusselt:
Re_L^0.8 = (588,235)^0.8 = 41,208.
Nu_L = [0.037 × 41,208 - 871] × (0.71)^(1/3) = [1,524.7 - 871] × 0.8921 = 653.7 × 0.8921 = 583.2.
Paso 3: Coeficiente de transferencia convectiva promedio:
h = Nu_L k_f / L = 583.2 × 0.0270 W/(m·K) / 2.0 m = 15.75 / 2.0 = 7.873 W/(m²·K).
Paso 4: Pérdida térmica convectiva:
dot{Q} = h A (T_s - T_inf) = 7.873 W/(m²·K) × 2.0 m² × (60 - 20 K) = 7.873 × 2.0 × 40 = 629.8 W.

Problema 2: ¿Qué representa físicamente el número de Prandtl Pr?
Paso 1: Pr = nu / alpha es el cociente entre la difusividad de cantidad de movimiento (viscosidad cinemática) y la difusividad térmica.
Paso 2: Para Pr ≈ 0.7 (gases), la capa límite hidrodinámica y la capa límite térmica crecen a ritmos similares.""",
        "bloque_sugerido": "Resolución Práctica 35 min • Convección forzada en haces de tubos de condensadores térmicos"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Radiación Térmica de Cuerpo Negro: Leyes de Planck, Stefan-Boltzmann y Wien",
        "objetivo": "Calcular la distribución espectral de emisión, la potencia radiante total emitida por el Sol y colectores selectivos aplicando las leyes de cuerpo negro.",
        "concepto_clave_latex": r"E_b = \sigma T^4 \quad [\text{W/m}^2] \quad ; \quad \lambda_{\text{max}} T = b = 2897.8\,\mu\text{m}\cdot\text{K} \quad ; \quad E_{b\lambda}(\lambda, T) = \frac{2\pi h c_0^2}{\lambda^5 \left[\exp\left(\frac{h c_0}{\lambda k_B T}\right) - 1\right]}",
        "ejemplo": """Problema 1: Considere al Sol como un emisor de cuerpo negro esférico con temperatura superficial T_sol = 5,778 K y radio R_sol = 6.96 × 10⁸ m. (Constante de Stefan-Boltzmann sigma = 5.670 × 10⁻⁸ W/(m²·K⁴)). Calcule: a) El poder emisivo total superficial E_b [W/m²]; b) La longitud de onda de máxima emisión lambda_max [nm]; c) La potencia luminosa total emitida (luminosidad solar L_sol [W]); d) La constante solar extraterrestre G_sc que incide en la órbita terrestre a una distancia media Sol-Tierra d_ST = 1.496 × 10¹¹ m (1 UA).
Paso 1: Poder emisivo superficial:
E_b = sigma T^4 = (5.670 × 10⁻⁸ W/(m²·K⁴))(5,778 K)⁴ = (5.670 × 10⁻⁸)(1.1146 × 10¹⁵) = 63.20 × 10⁶ W/m² = 63.20 MW/m².
Paso 2: Ley de desplazamiento de Wien:
lambda_max = 2897.8 micrometros·K / 5,778 K = 0.5015 micrometros = 501.5 nm (espectro visible, color verde-cian).
Paso 3: Luminosidad solar total:
Área solar A_sol = 4 pi R_sol² = 4 pi (6.96 × 10⁸ m)² = 6.087 × 10¹⁸ m².
L_sol = E_b × A_sol = (63.20 × 10⁶ W/m²)(6.087 × 10¹⁸ m²) = 3.847 × 10²⁶ W.
Paso 4: Constante solar a 1 UA:
G_sc = L_sol / (4 pi d_ST²) = 3.847 × 10²⁶ W / [4 pi (1.496 × 10¹¹ m)²] = 3.847 × 10²⁶ / (2.812 × 10²³) = 1,367.8 W/m² ≈ 1,367 W/m².

Problema 2: Una superficie selectiva solar posee una absortancia solar en onda corta alpha = 0.95 (para lambda < 2.5 micrometros) y una emisividad infrarroja en onda larga epsilon = 0.05 (para lambda > 2.5 micrometros). Si opera a T = 373 K (100 °C) en el vacío con T_alrededores = 293 K (20 °C), calcule la radiación neta emitida q_rad''.
Paso 1: q_rad'' = epsilon sigma (T⁴ - T_alr⁴) = 0.05 × (5.670 × 10⁻⁸) [(373)⁴ - (293)⁴].
Paso 2: 373⁴ = 1.935 × 10¹⁰; 293⁴ = 7.370 × 10⁹; Diferencia = 1.198 × 10¹⁰ K⁴.
Paso 3: q_rad'' = 0.05 × (5.670 × 10⁻⁸) × (1.198 × 10¹⁰) = 0.05 × 679.3 = 33.96 W/m² (las pérdidas radiativas se suprimen en un 95%).""",
        "bloque_sugerido": "Física Radiativa 35 min • Superficies selectivas espectrales y efecto invernadero atmosférico"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Oscilaciones Forzadas, Resonancia Mecánica y Factor de Calidad (Q) en Estructuras",
        "objetivo": "Resolver la respuesta en régimen estacionario de sistemas mecánicos amortiguados sometidos a excitación armónica y modelar la amplificación por resonancia.",
        "concepto_clave_latex": r"m \ddot{x} + c \dot{x} + k x = F_0 \cos(\omega t) \quad ; \quad X(\omega) = \frac{F_0 / k}{\sqrt{\left(1 - \frac{\omega^2}{\omega_0^2}\right)^2 + \left(2\zeta \frac{\omega}{\omega_0}\right)^2}} \quad ; \quad Q \approx \frac{1}{2\zeta} = \frac{\omega_0}{\Delta \omega}",
        "ejemplo": """Problema 1: La góndola de un aerogenerador de masa equivalente m = 40,000 kg (40 t) está montada sobre una torre de rigidez lateral k = 1.6 × 10⁶ N/m con amortiguamiento estructural c = 16,000 N·s/m. El desbalance aerodinámico del rotor induce una fuerza armónica F_0 = 8,000 N. Calcule: a) La frecuencia angular natural omega_0 [rad/s] y la frecuencia cíclica f_0 [Hz]; b) El factor de amortiguamiento zeta y el factor de calidad Q; c) La amplitud de deflexión dinámica estática X_est = F_0 / k; d) La amplitud de oscilación en la resonancia exacta (omega = omega_0).
Paso 1: Frecuencia natural: omega_0 = sqrt(k / m) = sqrt(1.6 × 10⁶ / 40,000) = sqrt(40) = 6.3246 rad/s.
f_0 = omega_0 / (2 pi) = 6.3246 / 6.2832 = 1.0066 Hz ≈ 1.0 Hz.
Paso 2: Amortiguamiento crítico: c_c = 2 m omega_0 = 2 × 40,000 × 6.3246 = 505,964 N·s/m.
Factor de amortiguamiento zeta = c / c_c = 16,000 / 505,964 = 0.03162 (3.16% del crítico).
Factor de calidad Q ≈ 1 / (2 zeta) = 1 / (2 × 0.03162) = 1 / 0.06324 = 15.81.
Paso 3: Deflexión estática: X_est = F_0 / k = 8,000 N / (1.6 × 10⁶ N/m) = 0.0050 m = 5.0 mm.
Paso 4: Amplitud en resonancia (omega = omega_0):
X_res = X_est / (2 zeta) = X_est × Q = 5.0 mm × 15.81 = 79.05 mm ≈ 7.91 cm.
Paso 5: La resonancia amplifica la oscilación casi 16 veces respecto a la carga estática, requiriendo amortiguadores de masa sintonizada (TMD).

Problema 2: ¿Cuál es el desfase phi entre la fuerza excitadora y la respuesta del sistema en resonancia exacta?
Paso 1: tan(phi) = [2 zeta (omega / omega_0)] / [1 - (omega / omega_0)^2].
Paso 2: En omega = omega_0, el denominador se hace cero positivo, lo que implica tan(phi) -> +inf => phi = pi/2 rad = 90°.
Paso 3: En resonancia, la velocidad está en fase con la fuerza aplicada, maximizando la inyección de potencia al oscilador.""",
        "bloque_sugerido": "Dinámica Estructural 40 min • Amortiguadores de masa sintonizada (TMD) en torres eólicas"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Osciladores Acoplados, Modos Normales y Coordenadas Normales de Vibración",
        "objetivo": "Determinar frecuencias naturales y modos normales de vibración en sistemas multicuerpo acoplados mediante análisis de autovalores matriciales.",
        "concepto_clave_latex": r"\mathbf{M} \ddot{\mathbf{x}} + \mathbf{K} \mathbf{x} = \mathbf{0} \quad ; \quad \det(\mathbf{K} - \omega^2 \mathbf{M}) = 0 \quad ; \quad \mathbf{x}(t) = \sum_{r=1}^N \mathbf{u}_r \left(A_r \cos(\omega_r t) + B_r \sin(\omega_r t)\right)",
        "ejemplo": """Problema 1: Considere el tren de potencia de una turbina de vapor compuesto por dos masas rotatorias acopladas por un eje torsional flexible: Masa 1 (rotor de turbina) con inercia J_1 = 200 kg·m² y Masa 2 (rotor de generador) con inercia J_2 = 300 kg·m², unidos por un eje con rigidez torsional k_t = 1.2 × 10⁶ N·m/rad. Formule la matriz de masa y rigidez, halle las dos frecuencias naturales de oscilación torsional omega_1 y omega_2, y determine los modos normales asociados.
Paso 1: Ecuaciones de movimiento libre:
J_1 ddot{theta}_1 + k_t (theta_1 - theta_2) = 0
J_2 ddot{theta}_2 + k_t (theta_2 - theta_1) = 0
Paso 2: Determinante característico:
det [ [k_t - J_1 omega^2,  -k_t], [-k_t,  k_t - J_2 omega^2] ] = 0.
(k_t - J_1 omega^2)(k_t - J_2 omega^2) - k_t^2 = 0 => k_t^2 - k_t (J_1 + J_2) omega^2 + J_1 J_2 omega^4 - k_t^2 = 0.
omega^2 [ J_1 J_2 omega^2 - k_t (J_1 + J_2) ] = 0.
Paso 3: Frecuencia 1: omega_1 = 0 rad/s (modo de cuerpo rígido sin deformación torsional del eje).
Modo 1: theta_1 = theta_2 (ambos rotores giran solidariamente en la misma dirección con u_1 = [1, 1]^T).
Paso 4: Frecuencia 2: omega_2^2 = k_t (J_1 + J_2) / (J_1 J_2) = k_t / J_red, donde la inercia reducida es:
J_red = (J_1 J_2) / (J_1 + J_2) = (200 × 300) / (200 + 300) = 60,000 / 500 = 120 kg·m².
omega_2 = sqrt(1.2 × 10⁶ / 120) = sqrt(10,000) = 100 rad/s (f_2 = 100 / (2 pi) = 15.92 Hz).
Paso 5: Modo 2: (k_t - J_1 omega_2^2) theta_1 - k_t theta_2 = 0.
(1.2 × 10⁶ - 200 × 10,000) theta_1 = 1.2 × 10⁶ theta_2 => (1.2 × 10⁶ - 2.0 × 10⁶) theta_1 = 1.2 × 10⁶ theta_2 => -0.8 theta_1 = 1.2 theta_2 => theta_2 = - (2/3) theta_1.
Modo 2: u_2 = [1, -0.667]^T (los rotores oscilan en contrafase respecto a un nodo fijo).

Problema 2: ¿Dónde se ubica el nodo estacionario (punto de deformación angular cero) en el eje de longitud L = 2 m?
Paso 1: Por semejanza de deflexión: x_nodo / (L - x_nodo) = |theta_1 / theta_2| = 1 / (2/3) = 1.5.
Paso 2: x_nodo = 1.5 (2 - x_nodo) = 3.0 - 1.5 x_nodo => 2.5 x_nodo = 3.0 => x_nodo = 1.20 m desde la turbina.""",
        "bloque_sugerido": "Vibraciones Torsionales 40 min • Resonancia sub-síncrona (SSR) en redes con compensación capacitiva serie"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Ecuación de Onda Unidimensional de D'Alembert y Velocidad de Propagación",
        "objetivo": "Deducir la solución general de D'Alembert para ondas viajeras en líneas de transmisión y medios mecánicos continuos.",
        "concepto_clave_latex": r"\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} \quad ; \quad y(x,t) = f(x - vt) + g(x + vt) \quad ; \quad v = \sqrt{\frac{T}{\mu}} = \sqrt{\frac{E}{\rho}} \quad [\text{m/s}]",
        "ejemplo": """Problema 1: Un cable conductor de alta tensión de aluminio con alma de acero (ACSR) tiene una densidad lineal de masa mu = 1.50 kg/m y está tensado en un vano entre torres con una tensión mecánica T_0 = 24,000 N (24 kN). Calcule la velocidad de propagación de ondas mecánicas transversales v y el tiempo tau que tarda una perturbación en viajar a lo largo de un vano de L = 400 metros.
Paso 1: Velocidad de onda transversal:
v = sqrt(T_0 / mu) = sqrt(24,000 N / 1.50 kg/m) = sqrt(16,000) = 126.49 m/s.
Paso 2: Tiempo de tránsito:
tau = L / v = 400 m / 126.49 m/s = 3.162 segundos.

Problema 2: Verifique que la función y(x,t) = 0.05 sin(2x - 8t) satisface la ecuación de onda y halle su velocidad de fase.
Paso 1: Derivadas espaciales: dy/dx = 0.05 × 2 cos(2x - 8t) = 0.10 cos(2x - 8t); d²y/dx² = -0.20 sin(2x - 8t).
Paso 2: Derivadas temporales: dy/dt = 0.05 × (-8) cos(2x - 8t) = -0.40 cos(2x - 8t); d²y/dt² = -3.20 sin(2x - 8t).
Paso 3: Cociente de derivadas segundas: (d²y/dt²) / (d²y/dx²) = (-3.20) / (-0.20) = 16 = v².
Paso 4: Velocidad de fase v = sqrt(16) = 4.0 m/s. Como coincide con omega / k = 8 / 2 = 4 m/s, satisface la ecuación de onda.""",
        "bloque_sugerido": "Propagación de Ondas 35 min • Vibración eólica de conductores y amortiguadores Stockbridge"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Densidad de Energía y Vector de Transporte de Potencia en Ondas Mecánicas",
        "objetivo": "Calcular la energía cinética, energía potencial elástica y el flujo de potencia promedio transmitido por una onda armónica viajera.",
        "concepto_clave_latex": r"u(x,t) = \frac{1}{2}\mu \left(\frac{\partial y}{\partial t}\right)^2 + \frac{1}{2} T \left(\frac{\partial y}{\partial x}\right)^2 \quad ; \quad P_{\text{prom}} = \frac{1}{2}\mu v \omega^2 A^2 \quad [\text{W}] \quad ; \quad I = \frac{P_{\text{prom}}}{\text{Área}} \quad [\text{W/m}^2]",
        "ejemplo": """Problema 1: Una onda mecánica senoidal viaja a lo largo de un tirante de acero de una torre eólica (mu = 2.5 kg/m, T = 40,000 N, v = sqrt(40000/2.5) = 126.5 m/s) con amplitud A = 0.02 m (20 mm) y frecuencia cíclica f = 10 Hz (omega = 20 pi ≈ 62.83 rad/s). Calcule: a) La densidad lineal de energía media bar{u} [J/m]; b) La potencia media transportada por la onda P_prom [W].
Paso 1: Densidad lineal de energía media:
bar{u} = (1/2) mu omega^2 A^2 = 0.5 × 2.5 kg/m × (62.83 rad/s)^2 × (0.02 m)^2 = 1.25 × 3,947.6 × 0.0004 = 1.9738 J/m.
Paso 2: Potencia media transmitida:
P_prom = bar{u} × v = 1.9738 J/m × 126.49 m/s = 249.67 W ≈ 250 W.

Problema 2: Si la frecuencia f se duplica a 20 Hz manteniendo constante la amplitud A y la tensión T, ¿en qué factor se incrementa la potencia transportada?
Paso 1: Dado que P_prom es proporcional a omega^2 (y por ende a f^2):
P_prom(20 Hz) / P_prom(10 Hz) = (20 / 10)^2 = 2^2 = 4.
Paso 2: Duplicar la frecuencia cuadruplica la tasa de transporte energético, alcanzando 1,000 W.""",
        "bloque_sugerido": "Transporte de Energía 30 min • Flujo de energía y disipación en líneas mecánicas y acústicas"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Reflexión, Transmisión e Impedancia Mecánica en Fronteras de Discontinuidad",
        "objetivo": "Calcular los coeficientes de reflexión y transmisión de onda en la unión de dos medios de diferente impedancia característica.",
        "concepto_clave_latex": r"Z = \frac{F}{v_{\text{partícula}}} = \sqrt{\mu T} = \rho v A \quad ; \quad r = \frac{Z_1 - Z_2}{Z_1 + Z_2} \quad ; \quad \tau = \frac{2 Z_1}{Z_1 + Z_2} \quad ; \quad R = r^2 \quad , \quad T_{\text{trans}} = \frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}",
        "ejemplo": """Problema 1: Una onda transversal viaja por una cuerda de densidad lineal mu_1 = 0.10 kg/m unida en x = 0 a una cuerda más pesada de mu_2 = 0.40 kg/m bajo la misma tensión T = 90 N. Calcule las impedancias características Z_1 y Z_2, el coeficiente de reflexión de amplitud r, el coeficiente de transmisión de amplitud tau, y compruebe la conservación de la energía verificando que el coeficiente de reflexión de potencia R más el de transmisión T_trans sumen 1.
Paso 1: Impedancias características:
Z_1 = sqrt(mu_1 T) = sqrt(0.10 × 90) = sqrt(9) = 3.0 N·s/m.
Z_2 = sqrt(mu_2 T) = sqrt(0.40 × 90) = sqrt(36) = 6.0 N·s/m.
Paso 2: Coeficiente de reflexión de amplitud:
r = (Z_1 - Z_2) / (Z_1 + Z_2) = (3.0 - 6.0) / (3.0 + 6.0) = -3.0 / 9.0 = -1/3 ≈ -0.3333.
(El signo negativo indica inversión de fase de 180° de la onda reflejada).
Paso 3: Coeficiente de transmisión de amplitud:
tau = 2 Z_1 / (Z_1 + Z_2) = (2 × 3.0) / (3.0 + 6.0) = 6.0 / 9.0 = 2/3 ≈ +0.6667 (en fase).
Paso 4: Coeficiente de reflexión de potencia:
R = r^2 = (-1/3)^2 = 1/9 ≈ 0.1111 (11.11% de la potencia incidente se refleja).
Paso 5: Coeficiente de transmisión de potencia:
T_trans = (4 Z_1 Z_2) / (Z_1 + Z_2)^2 = (4 × 3.0 × 6.0) / (9.0)^2 = 72.0 / 81.0 = 8/9 ≈ 0.8889 (88.89%).
Paso 6: Verificación de conservación de energía: R + T_trans = 1/9 + 8/9 = 9/9 = 1.000. Q.E.D.

Problema 2: ¿Qué ocurre cuando Z_2 -> inf (extremo perfectamente rígido)?
Paso 1: r = lim_{Z_2 -> inf} (Z_1 - Z_2)/(Z_1 + Z_2) = -1; tau = 0.
Paso 2: La onda se refleja al 100% con inversión de fase total y amplitud nula transmitida.""",
        "bloque_sugerido": "Física de Fronteras 35 min • Adaptación de impedancias acústicas y acoplamiento en transductores de ultrasonido"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Ondas Sonoras en Fluidos: Presión Acústica, Módulo Volumétrico e Impedancia Acústica",
        "objetivo": "Calcular la velocidad del sonido en gases y líquidos a partir del módulo volumétrico adiabático y relacionar presión acústica con desplazamiento de partículas.",
        "concepto_clave_latex": r"v_s = \sqrt{\frac{B_s}{\rho}} = \sqrt{\gamma \frac{R}{M} T} \quad [\text{m/s}] \quad ; \quad \Delta P_{\text{max}} = \rho v_s \omega s_{\text{max}} = Z_{\text{acústica}} \cdot v_{\text{partícula}} \quad [\text{Pa}]",
        "ejemplo": """Problema 1: Calcule la velocidad del sonido v_s en aire seco (gamma = 1.40, constante específica R_esp = 287.05 J/(kg·K)) a una temperatura invernal T_1 = -10 °C (263.15 K) y en una jornada cálida caribeña T_2 = 40 °C (313.15 K).
Paso 1: Para T_1 = 263.15 K:
v_s1 = sqrt(gamma R_esp T_1) = sqrt(1.40 × 287.05 × 263.15) = sqrt(105,753) = 325.20 m/s.
Paso 2: Para T_2 = 313.15 K:
v_s2 = sqrt(1.40 × 287.05 × 313.15) = sqrt(125,846) = 354.75 m/s.
Paso 3: Un aumento térmico de 50 K incrementa la velocidad acústica en casi 30 m/s.

Problema 2: Una onda sonora de frecuencia f = 1,000 Hz viaja en aire con densidad rho = 1.20 kg/m³ y v_s = 343 m/s (impedancia acústica Z = rho v_s = 411.6 Pa·s/m). Si la amplitud de presión acústica es Delta P_max = 2.0 Pa (nivel de conversación alta), calcule la amplitud de desplazamiento de las moléculas de aire s_max [nm].
Paso 1: Frecuencia angular: omega = 2 pi f = 2,000 pi ≈ 6,283.2 rad/s.
Paso 2: s_max = Delta P_max / (rho v_s omega) = 2.0 Pa / [(411.6 Pa·s/m)(6,283.2 rad/s)] = 2.0 / 2,586,165 = 7.733 × 10⁻⁷ m = 773.3 nm.
Paso 3: El desplazamiento molecular es submicrométrico (menos de 1 micrómetro) a pesar de generar una señal auditiva muy potente.""",
        "bloque_sugerido": "Acústica Física 35 min • Propagación acústica en ductos de escape y silenciadores reactivos"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Atenuación Sonora, Escala de Decibelios y Ruido Acústico en Parques Eólicos",
        "objetivo": "Calcular la atenuación geométrica y atmosférica del ruido sonoro emitido por aerogeneradores mediante la escala logarítmica de decibelios dB(A).",
        "concepto_clave_latex": r"\beta = 10 \log_{10}\left(\frac{I}{I_0}\right) \quad [\text{dB}] \quad ; \quad I_0 = 10^{-12}\,\text{W/m}^2 \quad ; \quad L_p(r) = L_w - 10\log_{10}(4\pi r^2) - \alpha_{\text{atm}} r",
        "ejemplo": """Problema 1: Un aerogenerador multimegavatio emite un nivel de potencia acústica global en el buje L_w = 104 dB (referido a 10⁻¹² W). Asumiendo propagación esférica en campo libre y una atenuación atmosférica alpha_atm = 0.005 dB/m, calcule el nivel de presión sonora recibido L_p [dB] por un receptor situado a una distancia r = 350 metros.
Paso 1: Área de la esfera a r = 350 m: A = 4 pi r^2 = 4 pi (350)^2 = 4 pi (122,500) = 1,539,380 m².
Paso 2: Pérdida geométrica de divergencia:
10 log_10(4 pi r^2) = 10 log_10(1,539,380) = 10 × 6.1873 = 61.87 dB.
Paso 3: Atenuación atmosférica:
alpha_atm × r = 0.005 dB/m × 350 m = 1.75 dB.
Paso 4: Nivel sonoro en el receptor:
L_p = L_w - 61.87 - 1.75 = 104 - 63.62 = 40.38 dB ≈ 40.4 dB(A).
Paso 5: Cumple con la normativa ambiental residencial nocturna estándar (límite L_p <= 45 dB(A)).

Problema 2: Si en el mismo punto incide simultáneamente el ruido de dos aerogeneradores idénticos, cada uno aportando L_p1 = L_p2 = 40.4 dB, ¿cuál es el nivel sonoro combinado L_tot?
Paso 1: Las intensidades acústicas se suman directamente: I_tot = I_1 + I_2 = 2 I_1.
Paso 2: L_tot = 10 log_10(I_tot / I_0) = 10 log_10(2 I_1 / I_0) = L_p1 + 10 log_10(2) = 40.4 + 3.01 = 43.41 dB.
Paso 3: Duplicar la fuente sonora añade exactamente +3 dB al nivel sonoro total.""",
        "bloque_sugerido": "Impacto Ambiental 35 min • Modelación de curvas isofónicas en parques eólicos con norma ISO 9613-2"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Efecto Doppler Acústico y Relativista: Aplicaciones en Anemometría Láser (LDA)",
        "objetivo": "Calcular corrimientos Doppler de frecuencia para fuentes y receptores en movimiento en diagnósticos de flujo por Anemometría Doppler Láser (LDA/LiDAR).",
        "concepto_clave_latex": r"f' = f \left(\frac{v_s \pm v_r}{v_s \mp v_f}\right) \quad [\text{Hz}] \quad ; \quad \Delta f_D = 2 f_0 \frac{v}{c} \cos(\theta) \quad [\text{Óptico}]",
        "ejemplo": """Problema 1: Un silbato acústico de emergencia emite una frecuencia f_0 = 800 Hz en aire estático (v_s = 340 m/s). Un vehículo de supervisión de línea de transmisión se aproxima a la estación a una velocidad v_r = 30 m/s (108 km/h). Calcule la frecuencia percibida f' por el conductor al acercarse, y la frecuencia que percibe cuando se aleja tras rebasarla.
Paso 1: Receptor en movimiento hacia fuente en reposo (v_f = 0):
f'_acercamiento = f_0 [(v_s + v_r) / v_s] = 800 × [(340 + 30) / 340] = 800 × (370 / 340) = 800 × 1.08824 = 870.59 Hz.
Paso 2: Receptor alejándose de la fuente en reposo:
f'_alejamiento = f_0 [(v_s - v_r) / v_s] = 800 × [(340 - 30) / 340] = 800 × (310 / 340) = 800 × 0.91176 = 729.41 Hz.
Paso 3: El salto aparente total al rebasar la fuente es Delta f = 870.59 - 729.41 = 141.18 Hz.

Problema 2: Un anemómetro láser óptico LiDAR (longitud de onda lambda_0 = 1,550 nm, frecuencia f_0 = c / lambda_0 = 3 × 10⁸ / (1.55 × 10⁻⁶) = 1.9355 × 10¹⁴ Hz) mide la velocidad del viento en un aerogenerador. El haz choca frontalmente (theta = 0, cos(theta) = 1) contra aerosoles arrastrados por el viento a velocidad v = 12.0 m/s. Calcule el corrimiento de frecuencia Doppler Delta f_D [MHz].
Paso 1: Delta f_D = 2 v / lambda_0 = (2 × 12.0 m/s) / (1.55 × 10⁻⁶ m) = 24.0 / (1.55 × 10⁻⁶) = 1.5484 × 10⁷ Hz = 15.48 MHz.
Paso 2: La detección heterodina del corrimiento de 15.48 MHz permite registrar la velocidad del viento en tiempo real con precisión milimétrica.""",
        "bloque_sugerido": "Instrumentación Óptica 35 min • Medición remota de perfiles de viento con tecnología LiDAR coherente"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Ondas Estacionarias en Columnas de Aire, Resonancia Acústica y Modos de Cavidad",
        "objetivo": "Calcular frecuencias armónicas de resonancia en tubos abiertos y cerrados para mitigar pulsaciones acústicas en ductos de calderas y compresores.",
        "concepto_clave_latex": r"f_n^{\text{abierto}} = n \frac{v_s}{2 L} \quad (n = 1, 2, 3, \dots) \quad ; \quad f_m^{\text{cerrado}} = m \frac{v_s}{4 L} \quad (m = 1, 3, 5, \dots)",
        "ejemplo": """Problema 1: Un ducto de gases calientes de combustión de longitud L = 6.0 m se comporta acústicamente como un tubo abierto en ambos extremos. Los gases circulan a T = 450 K con velocidad del sonido v_s = 425 m/s. Calcule la frecuencia fundamental de resonancia f_1 y las frecuencias de los dos armónicos siguientes f_2 y f_3.
Paso 1: Frecuencia fundamental (n = 1):
f_1 = 1 × v_s / (2 L) = 425 m/s / (2 × 6.0 m) = 425 / 12.0 = 35.42 Hz.
Paso 2: Segundo armónico (n = 2):
f_2 = 2 × f_1 = 2 × 35.42 Hz = 70.83 Hz.
Paso 3: Tercer armónico (n = 3):
f_3 = 3 × f_1 = 3 × 35.42 Hz = 106.25 Hz.
Paso 4: Si el ventilador de tiro forzado opera a 2,125 rpm con 1 aspa (f_excitación = 35.4 Hz), entrará en resonancia acústica catastrófica con el ducto.

Problema 2: Si el ducto tuviera un extremo cerrado (tubo cerrado-abierto), ¿cuál sería su frecuencia fundamental?
Paso 1: f_1,cerrado = v_s / (4 L) = 425 / (4 × 6.0) = 425 / 24.0 = 17.71 Hz (la mitad de la frecuencia del tubo abierto).
Paso 2: Solo resonará en múltiplos impares: f_3 = 3(17.71) = 53.13 Hz, f_5 = 5(17.71) = 88.54 Hz.""",
        "bloque_sugerido": "Dinámica de Fluidos Acústica 30 min • Resonadores de Helmholtz y trampas acústicas en turbomaquinaria"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Ondas de Choque, Número de Mach y Flujo Compresible en Toberas de Vapor",
        "objetivo": "Modelar la formación de ondas de choque normales y discontinuidades de presión en toberas convergentes-divergentes (De Laval) en turbinas térmicas.",
        "concepto_clave_latex": r"M = \frac{v}{v_s} \quad ; \quad \frac{P_{02}}{P_{01}} = \left[\frac{(\gamma+1)M_1^2}{(\gamma-1)M_1^2 + 2}\right]^{\frac{\gamma}{\gamma-1}}\left[\frac{\gamma+1}{2\gamma M_1^2 - (\gamma-1)}\right]^{\frac{1}{\gamma-1}} \quad ; \quad M_2^2 = \frac{(\gamma-1)M_1^2 + 2}{2\gamma M_1^2 - (\gamma-1)}",
        "ejemplo": """Problema 1: Vapor de agua sobrecalentado entra a la sección divergente de una tobera De Laval de una turbina de vapor con velocidad supersónica a Mach M_1 = 1.80 y presión estática P_1 = 120 kPa (gamma = 1.30). Una contrapresión indebida en el condensador fuerza la aparición de una onda de choque normal dentro del ducto. Calcule el número de Mach inmediatamente después del choque M_2 y la presión estática detrás del choque P_2.
Paso 1: Mach posterior al choque M_2:
M_2^2 = [(gamma - 1) M_1^2 + 2] / [2 gamma M_1^2 - (gamma - 1)] = [(1.30 - 1)(1.80)^2 + 2] / [2(1.30)(1.80)^2 - (1.30 - 1)]
= [0.30 × 3.24 + 2] / [2.60 × 3.24 - 0.30] = [0.972 + 2] / [8.424 - 0.30] = 2.972 / 8.124 = 0.3658.
M_2 = sqrt(0.3658) = 0.6048 (el flujo se desacelera abruptamente a régimen subsónico).
Paso 2: Salto de presión estática:
P_2 / P_1 = [2 gamma M_1^2 - (gamma - 1)] / (gamma + 1) = [2(1.30)(3.24) - 0.30] / (1.30 + 1) = 8.124 / 2.30 = 3.532.
Paso 3: Presión estática posterior:
P_2 = 120 kPa × 3.532 = 423.8 kPa.
Paso 4: La onda de choque provoca un salto brusco de presión de 120 kPa a 424 kPa en un espesor de pocas micras, generando una severa pérdida de presión de estancamiento e irreversibilidad entrópica.

Problema 2: ¿Puede ocurrir una onda de choque estable en la sección convergente de una tobera?
Paso 1: No. Las ondas de choque solo se forman en regímenes supersónicos (M_1 > 1), los cuales únicamente se alcanzan aguas abajo de la garganta en el difusor divergente.""",
        "bloque_sugerido": "Gasdinámica 40 min • Toberas convergentes-divergentes y choque oblicuo en etapas de turbina"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Ecuaciones de Maxwell en Medios Dieléctricos y Ondas Electromagnéticas",
        "objetivo": "Deducir la ecuación de onda electromagnética vectorial a partir de las ecuaciones fundamentales de Maxwell en materiales dieléctricos y conductores.",
        "concepto_clave_latex": r"\nabla^2 \mathbf{E} = \mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} + \mu \sigma \frac{\partial \mathbf{E}}{\partial t} \quad ; \quad v = \frac{1}{\sqrt{\mu \varepsilon}} = \frac{c_0}{n} \quad ; \quad \eta = \sqrt{\frac{\mu}{\varepsilon}} \quad [\Omega]",
        "ejemplo": """Problema 1: Una onda electromagnética plana monocromática de frecuencia f = 500 MHz (omega = pi × 10⁹ rad/s) se propaga en un material dieléctrico no magnético (mu_r = 1.0 => mu = mu_0 = 4 pi × 10⁻⁷ H/m) con permitividad relativa epsilon_r = 4.0 (epsilon = 4.0 epsilon_0 = 3.54 × 10⁻¹¹ F/m) y conductividad sigma = 0. Calcule: a) La velocidad de fase v; b) El índice de refracción n; c) La impedancia intrínseca de onda eta [Omega]; d) La longitud de onda en el medio lambda [m].
Paso 1: Velocidad de propagación:
v = 1 / sqrt(mu_0 × 4 epsilon_0) = (1 / sqrt(mu_0 epsilon_0)) × (1 / sqrt(4)) = c_0 / 2 = 3.0 × 10⁸ / 2 = 1.50 × 10⁸ m/s.
Paso 2: Índice de refracción:
n = sqrt(epsilon_r mu_r) = sqrt(4.0 × 1.0) = 2.0.
Paso 3: Impedancia intrínseca:
eta = sqrt(mu / epsilon) = sqrt(mu_0 / (4 epsilon_0)) = (1/2) sqrt(mu_0 / epsilon_0) = (1/2)(376.73 Omega) = 188.37 Omega ≈ 188.4 Omega.
Paso 4: Longitud de onda en el medio:
lambda = v / f = 1.50 × 10⁸ m/s / (500 × 10⁶ s⁻¹) = 0.30 m = 30 cm (frente a 60 cm en el vacío).

Problema 2: En un buen conductor (sigma / (omega epsilon) >> 1), calcule la profundidad de penetración pelicular (skin depth) delta para cobre (sigma = 5.8 × 10⁷ S/m, mu = mu_0) a la frecuencia de red f = 60 Hz.
Paso 1: delta = 1 / sqrt(pi f mu sigma) = 1 / sqrt(pi × 60 × (4 pi × 10⁻⁷) × (5.8 × 10⁷)).
Paso 2: Denominador: sqrt(188.495 × 1.2566 × 10⁻⁶ × 5.8 × 10⁷) = sqrt(13,738) = 117.21 m⁻¹.
Paso 3: delta = 1 / 117.21 = 0.00853 m = 8.53 mm.
Paso 4: A 60 Hz, el 63% de la corriente se concentra en los primeros 8.5 mm de la superficie del conductor.""",
        "bloque_sugerido": "Electromagnetismo Ondulatorio 40 min • Deducción del efecto piel (skin effect) en barras de distribución"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Vector de Poynting, Irradiancia Solar y Presión de Radiación Fotónica",
        "objetivo": "Calcular el flujo de densidad de potencia electromagnética mediante el vector de Poynting y determinar la presión de radiación sobre velas solares.",
        "concepto_clave_latex": r"\mathbf{S} = \mathbf{E} \times \mathbf{H} = \frac{1}{\mu_0}(\mathbf{E} \times \mathbf{B}) \quad [\text{W/m}^2] \quad ; \quad \langle S \rangle = \frac{E_0^2}{2 \eta_0} \quad ; \quad P_{\text{rad}} = \frac{\langle S \rangle}{c}(1 + R) \quad [\text{N/m}^2]",
        "ejemplo": """Problema 1: En la superficie terrestre en un día despejado se registra una irradiancia solar incidente de G = langle S rangle = 1,000 W/m². Sabiendo que la impedancia intrínseca del vacío es eta_0 = 376.73 Omega (≈ 120 pi Omega), calcule la amplitud de pico del campo eléctrico E_0 [V/m] y la amplitud del campo magnético B_0 [microtesla] de la onda electromagnética solar equivalente.
Paso 1: Relación de Poynting para onda plana:
langle S rangle = E_0^2 / (2 eta_0) => E_0^2 = 2 eta_0 langle S rangle = 2 × 376.73 Omega × 1,000 W/m² = 753,460 (V/m)².
Paso 2: Amplitud de campo eléctrico:
E_0 = sqrt(753,460) = 868.02 V/m.
Paso 3: Amplitud de inducción magnética:
B_0 = E_0 / c_0 = 868.02 V/m / (3.0 × 10⁸ m/s) = 2.893 × 10⁻⁶ Tesla = 2.893 microT.
Paso 4: El campo magnético terrestre (aprox. 30 a 50 microT) es un orden de magnitud mayor que la oscilación de alta frecuencia del campo electromagnético solar.

Problema 2: Una vela solar espacial reflectante (reflectancia R = 1.0) de área A = 100,000 m² (0.10 km²) se despliega a 1 UA del Sol donde la irradiancia es langle S rangle = 1,367 W/m². Calcule la fuerza total de propulsión fotónica F_rad ejercida por la presión de radiación.
Paso 1: Presión de radiación con reflexión perfecta:
P_rad = (langle S rangle / c) (1 + R) = (1,367 / 3.0 × 10⁸) × (1 + 1.0) = (4.557 × 10⁻⁶ N/m²) × 2 = 9.113 × 10⁻⁶ N/m² = 9.113 microN/m².
Paso 2: Fuerza propulsora neta:
F_rad = P_rad × A = 9.113 × 10⁻⁶ N/m² × 100,000 m² = 0.9113 N.
Paso 3: Aunque la fuerza parece modesta (aprox. 0.91 N), al actuar sin fricción de manera continua durante meses imparte aceleraciones masivas a sondas espaciales.""",
        "bloque_sugerido": "Óptica Cuántica 35 min • Balances de momentum fotónico y balance de radiación planetaria"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Polarización de Ondas Electromagnéticas: Ley de Malus, Birrefringencia y Ángulo de Brewster",
        "objetivo": "Analizar estados de polarización lineal, circular y elíptica, calculando pérdidas de reflexión por polarización y ángulo de Brewster en cubiertas solares.",
        "concepto_clave_latex": r"I = I_0 \cos^2(\theta) \quad [\text{Ley de Malus}] \quad ; \quad \tan(\theta_B) = \frac{n_2}{n_1} \quad ; \quad r_p = \frac{n_2 \cos\theta_1 - n_1 \cos\theta_2}{n_2 \cos\theta_1 + n_1 \cos\theta_2} = 0 \text{ en } \theta_B",
        "ejemplo": """Problema 1: Un haz de luz no polarizada de intensidad I_0 = 800 W/m² incide sobre un primer filtro polarizador lineal ideal. La luz polarizada resultante atraviesa un segundo polarizador (analizador) cuyo eje de transmisión forma un ángulo theta = 30° respecto al primero, y posteriormente un tercer polarizador orientado a 90° respecto al primero (60° respecto al segundo). Calcule la intensidad emergente tras cada filtro.
Paso 1: Tras el primer polarizador (luz no polarizada):
I_1 = (1/2) I_0 = 0.5 × 800 = 400 W/m² (polarizada linealmente).
Paso 2: Tras el segundo polarizador (Ley de Malus con theta_12 = 30°):
I_2 = I_1 cos^2(30°) = 400 × (sqrt(3)/2)^2 = 400 × (3/4) = 300 W/m².
Paso 3: Tras el tercer polarizador (ángulo relativo entre 2 y 3: theta_23 = 90° - 30° = 60°):
I_3 = I_2 cos^2(60°) = 300 × (1/2)^2 = 300 × (1/4) = 75 W/m².
Paso 4: Sin el segundo filtro intermedio, los polarizadores 1 y 3 cruzados a 90° bloquearían el 100% de la luz (I_3 = 0). La inserción del filtro a 30° reorienta el vector de campo eléctrico permitiendo el paso de 75 W/m².

Problema 2: Calcule el ángulo de polarización de Brewster theta_B para la luz solar que incide desde el aire (n_1 = 1.0) sobre la cubierta de vidrio de un módulo fotovoltaico (n_2 = 1.52).
Paso 1: tan(theta_B) = n_2 / n_1 = 1.52 / 1.0 = 1.52.
Paso 2: theta_B = arctan(1.52) = 56.66° (56° 40').
Paso 3: Consecuencia técnica: A un ángulo de incidencia de 56.7°, la componente de polarización paralela (onda p) penetra el vidrio con cero reflectancia especular (100% de transmisión).""",
        "bloque_sugerido": "Óptica de Películas 35 min • Coeficientes de Fresnel y atenuación de destellos en paneles fotovoltaicos"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Interferencia Óptica: Películas Delgadas y Recubrimientos Antirreflectantes (ARC)",
        "objetivo": "Diseñar recubrimientos antirreflectantes (ARC) de espesor de cuarto de onda (lambda/4) para celdas solares aplicando interferencia destructiva.",
        "concepto_clave_latex": r"n_{\text{ARC}} = \sqrt{n_{\text{aire}} n_{\text{Si}}} \quad ; \quad d_{\text{ARC}} = \frac{\lambda_0}{4 n_{\text{ARC}}} \quad ; \quad 2 n d = \left(m + \frac{1}{2}\right)\lambda_0",
        "ejemplo": """Problema 1: El silicio semiconductor puro tiene un índice de refracción muy alto n_Si = 3.85 a la longitud de onda de pico solar lambda_0 = 600 nm, reflejando el 34.6% de la luz incidente. Para mitigar esta pérdida, se deposita una película delgada de nitruro de silicio Si_3N_4 como capa antirreflectante (ARC) en contacto con el aire (n_aire = 1.0). Calcule: a) El índice de refracción ideal del material n_ARC para interferencia destructiva perfecta; b) El espesor óptimo de la película d_ARC [nm] para lambda_0 = 600 nm.
Paso 1: Índice óptimo de acomodamiento de impedancias ópticas:
n_ARC = sqrt(n_aire × n_Si) = sqrt(1.0 × 3.85) = sqrt(3.85) = 1.962.
(El nitruro de silicio amorfo PECVD SiN_x se sintetiza típicamente con n ≈ 1.95 a 2.05, encajando a la perfección).
Paso 2: Ambos rebotes (aire-ARC y ARC-Si) experimentan salto de fase de pi (180°) porque n_aire < n_ARC < n_Si.
Por tanto, la interferencia destructiva entre ambos haces reflejados requiere una diferencia de camino óptico de media longitud de onda: 2 n_ARC d = lambda_0 / 2.
Paso 3: Espesor de cuarto de onda:
d_ARC = lambda_0 / (4 n_ARC) = 600 nm / (4 × 1.962) = 600 / 7.848 = 76.45 nm.
Paso 4: Un recubrimiento de Si_3N_4 de 76.5 nm reduce la reflectancia del silicio del 35% a menos del 1.5% en el centro del espectro visible.

Problema 2: Demuestre la reflectancia del silicio desnudo al aire en incidencia normal mediante la fórmula de Fresnel.
Paso 1: R = [(n_Si - 1) / (n_Si + 1)]^2 = [(3.85 - 1) / (3.85 + 1)]^2 = (2.85 / 4.85)^2 = (0.5876)^2 = 0.3453 (34.53% de reflexión parásita).""",
        "bloque_sugerido": "Ingeniería Fotónica 35 min • Recubrimientos multicapa de banda ancha (DLARC) en celdas de heterounión"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Difracción de Fraunhofer y Fresnel: Redes de Difracción y Espectrometría Solar",
        "objetivo": "Calcular la resolución angular y dispersión de redes de difracción para analizar el espectro solar y líneas de absorción de Fraunhofer.",
        "concepto_clave_latex": r"d \sin(\theta) = m \lambda \quad (m = 0, \pm 1, \pm 2, \dots) \quad ; \quad R = \frac{\lambda}{\Delta \lambda} = m N \quad ; \quad \theta_{\text{Rayleigh}} = 1.22 \frac{\lambda}{D}",
        "ejemplo": """Problema 1: Un espectrómetro solar de laboratorio utiliza una red de difracción plana con 600 líneas/mm iluminada en incidencia normal por luz solar. Calcule: a) La distancia entre ranuras d [micrómetros]; b) El ángulo de difracción theta_1 para la línea de emisión H-alfa de Balmer (lambda = 656.3 nm) en el primer orden (m = 1); c) El poder de resolución R necesario para resolver el doblete del sodio solar (lambda_1 = 589.00 nm y lambda_2 = 589.59 nm); d) El número mínimo de líneas iluminadas N_min para lograrlo en el segundo orden (m = 2).
Paso 1: Espaciamiento de la red:
d = 1 mm / 600 = 10⁻³ m / 600 = 1.6667 × 10⁻⁶ m = 1.667 micrometros = 1,666.7 nm.
Paso 2: Ángulo de difracción para H-alfa (m = 1):
sin(theta_1) = m lambda / d = (1 × 656.3 nm) / 1,666.7 nm = 0.39378.
theta_1 = arcsin(0.39378) = 23.19° (23° 11').
Paso 3: Poder de resolución cromática para el doblete de sodio:
Delta lambda = 589.59 - 589.00 = 0.59 nm; lambda_medio = 589.30 nm.
R = lambda_medio / Delta lambda = 589.30 / 0.59 = 998.8 ≈ 1,000.
Paso 4: Número mínimo de líneas iluminadas:
R = m N => N_min = R / m = 1000 / 2 = 500 líneas (apenas 0.83 mm de haz iluminando la red).

Problema 2: ¿Cuál es el orden máximo m_max teóricamente visible para lambda = 656.3 nm?
Paso 1: sin(theta) <= 1 => m lambda / d <= 1 => m <= d / lambda.
Paso 2: m <= 1,666.7 nm / 656.3 nm = 2.539 => m_max = 2 (el tercer orden requeriría sin(theta) > 1, no físico).""",
        "bloque_sugerido": "Espectrometría Solar 35 min • Identificación de líneas atmosféricas y calibración de piranómetros espectrales"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Radiación Solar Extraterrestre vs Global: Masa de Aire (AM) y Dispersión Rayleigh y Mie",
        "objetivo": "Modelar la atenuación espectral de la radiación solar a través de la atmósfera evaluando el coeficiente de masa de aire (AM) y scattering.",
        "concepto_clave_latex": r"\text{AM} \approx \frac{1}{\cos(\theta_z) + 0.50572(96.07995^\circ - \theta_z)^{-1.6364}} \quad ; \quad I_{\text{Rayleigh}} \propto \frac{1}{\lambda^4} \quad ; \quad G_b = G_0 \exp(-k \cdot \text{AM})",
        "ejemplo": """Problema 1: En Santa Marta (latitud 11.24° N) a las 9:00 AM el ángulo cenital solar medido es theta_z = 48.0° (elevación solar alpha_s = 42.0°). Sabiendo que la irradiancia solar extraterrestre en ese día es G_0 = 1,367 W/m²: a) Calcule el número de masa de aire AM utilizando la fórmula corregida de Kasten-Young; b) Si el coeficiente de extinción óptica atmosférica de banda ancha es k = 0.22, calcule la irradiancia directa normal de haz G_b [W/m²] que alcanza la superficie terrestre al nivel del mar.
Paso 1: Masa de aire con Kasten-Young para theta_z = 48.0°:
Término de refracción: (96.07995 - 48.0)^(-1.6364) = (48.07995)^(-1.6364) = 1.764 × 10⁻³.
Denominador = cos(48°) + 0.50572 × 1.764 × 10⁻³ = 0.66913 + 0.00089 = 0.67002.
AM = 1 / 0.67002 = 1.4925 ≈ AM 1.5 (muy cercano al estándar universal de ensayo fotovoltaico STC AM 1.5G).
Paso 2: Atenuación exponencial de Beer-Lambert-Bouguer:
G_b = G_0 exp(-k × AM) = 1,367 W/m² × exp(-0.22 × 1.4925) = 1,367 × exp(-0.32835).
exp(-0.32835) = 0.7201.
G_b = 1,367 × 0.7201 = 984.4 W/m².
Paso 3: La atmósfera absorbió y dispersó el 28% de la radiación directa extraterrestre.

Problema 2: Explique por qué el cielo despejado es azul y el Sol al atardecer se ve rojizo a partir de la dispersión de Rayleigh.
Paso 1: La dispersión de Rayleigh por moléculas gaseosas (N_2, O_2 con tamaño d << lambda) es inversamente proporcional a la cuarta potencia de la longitud de onda: I_scatt proportional to 1 / lambda⁴.
Paso 2: La luz azul (lambda ≈ 450 nm) se dispersa (700 / 450)⁴ = (1.555)⁴ ≈ 5.85 veces más intensamente que la luz roja (lambda ≈ 700 nm), bañando la bóveda celeste en azul.
Paso 3: Al atardecer (theta_z -> 90°, AM > 10), la luz directa recorre un camino óptico enorme; la radiación azul es casi totalmente dispersada fuera del haz directo, dejando llegar únicamente las longitudes de onda rojas y doradas.""",
        "bloque_sugerido": "Meteorología Solar 40 min • Simulación de espectros SMARTS para STC (AM 1.5G) y recursos renovables"
    }
]

if __name__ == '__main__':
    yaml_text = format_topics_yaml(topics_02021811)
    inject_topics_after('      - codigo: "03041820"', yaml_text)
    print("02021811 Calor y Ondas now has 30 topics!")
