# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after, format_topics_yaml

topics_03041820 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Máxima Transferencia de Potencia Compleja y Teorema de Tellegen en Régimen AC",
        "objetivo": "Calcular la impedancia de carga óptima conjugada para maximizar la potencia activa entregada y verificar la conservación de potencia compleja mediante Tellegen.",
        "concepto_clave_latex": r"\mathbf{Z}_L = \mathbf{Z}_{\text{th}}^* = R_{\text{th}} - j X_{\text{th}} \quad ; \quad P_{\text{max}} = \frac{|\mathbf{V}_{\text{th}}|^2}{4 R_{\text{th}}} \quad [\text{W}] \quad ; \quad \sum_{k=1}^B \mathbf{S}_k = \sum_{k=1}^B \mathbf{V}_k \mathbf{I}_k^* = 0",
        "ejemplo": """Problema 1: Un generador de inducción eólico conectado a una barra de media tensión presenta un equivalente de Thévenin con tensión de circuito abierto V_th = 690 / sqrt(3) = 398.37 V RMS (fase-neutro a 0°) e impedancia interna Z_th = 0.8 + j 1.5 Omega. Calcule la impedancia de carga Z_L requerida para absorber la máxima potencia activa posible y el valor numérico de dicha potencia P_max por fase.
Paso 1: Condición de máxima transferencia de potencia activa en AC:
Z_L = Z_th* = R_th - j X_th = 0.8 - j 1.5 Omega (carga capacitiva que cancela exactamente la reactancia inductiva interna).
Paso 2: Resistencia total de la malla R_tot = R_th + R_L = 0.8 + 0.8 = 1.6 Omega.
Reactancia neta X_tot = 1.5 - 1.5 = 0 Omega (resonancia serie).
Paso 3: Corriente de carga: I_L = V_th / R_tot = 398.37 / 1.6 = 248.98 A RMS.
Paso 4: Potencia activa máxima por fase:
P_max = |I_L|^2 R_L = (248.98)^2 × 0.8 = 61,991 × 0.8 = 49,593 W = 49.59 kW/fase.
Comprobación por fórmula directa: P_max = |V_th|^2 / (4 R_th) = (398.37)^2 / (4 × 0.8) = 158,700 / 3.2 = 49,593.7 W = 49.59 kW.
Paso 5: Para el sistema trifásico equilibrado total: P_3f = 3 × 49.59 kW = 148.78 kW.

Problema 2: En un circuito de 3 ramas paralelas alimentado por V = 120 V a 0° RMS: Rama 1 tiene Z_1 = 10 Omega (resistor puro, I_1 = 12 A); Rama 2 tiene Z_2 = j 20 Omega (inductor puro, I_2 = -j 6 A); Rama 3 tiene Z_3 = -j 30 Omega (capacitor puro, I_3 = +j 4 A). Verifique el Teorema de Tellegen sumando las potencias complejas de los elementos y la fuente.
Paso 1: Corriente total entregada por la fuente: I_tot = I_1 + I_2 + I_3 = 12 - j 6 + j 4 = 12 - j 2 A.
Paso 2: Potencia compleja suministrada por la fuente:
S_fuente = V × I_tot* = 120 × (12 + j 2) = 1,440 + j 240 VA.
Paso 3: Potencias complejas consumidas en las ramas:
S_1 = V × I_1* = 120 × 12 = 1,440 + j 0 VA.
S_2 = V × I_2* = 120 × (+j 6) = 0 + j 720 VA.
S_3 = V × I_3* = 120 × (-j 4) = 0 - j 480 VA.
Paso 4: Suma consumida: S_cons = (1440 + 0 + 0) + j (0 + 720 - 480) = 1,440 + j 240 VA.
Paso 5: Balance neto: sum S_k = S_cons - S_fuente = 0 + j 0 VA. Tellegen se cumple con rigurosa exactitud.""",
        "bloque_sugerido": "Resolución de Redes 35 min • Máxima transferencia con restricciones en el factor de potencia de carga"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Circuitos Resonantes Serie y Paralelo: Ancho de Banda, Selectividad y Factor de Calidad (Q)",
        "objetivo": "Calcular la frecuencia de resonancia, frecuencias de media potencia y factor de calidad Q en filtros resonantes de redes eléctricas.",
        "concepto_clave_latex": r"\omega_0 = \frac{1}{\sqrt{LC}} \quad [\text{rad/s}] \quad ; \quad Q_{\text{serie}} = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 R C} \quad ; \quad \text{BW} = \Delta \omega = \frac{\omega_0}{Q} = \frac{R}{L} \quad [\text{rad/s}]",
        "ejemplo": """Problema 1: Un filtro pasa-banda sintonizado para eliminar armónicos de conmutación en una planta fotovoltaica consta de una rama RLC serie con R = 2.0 Omega, L = 5.0 mH (0.005 H) y C = 2.0 microfaradios (2.0 × 10⁻⁶ F). Calcule: a) La frecuencia angular de resonancia omega_0 y la frecuencia cíclica f_0; b) El factor de calidad Q; c) El ancho de banda BW [rad/s] y Delta f [Hz]; d) Las frecuencias de corte de media potencia f_1 y f_2; e) La tensión en bornes del condensador en resonancia si se aplica una tensión de entrada V_in = 230 V RMS a f_0.
Paso 1: Frecuencia de resonancia:
omega_0 = 1 / sqrt(L C) = 1 / sqrt(0.005 × 2.0 × 10⁻⁶) = 1 / sqrt(1.0 × 10⁻⁸) = 1 / 10⁻⁴ = 10,000 rad/s.
f_0 = omega_0 / (2 pi) = 10,000 / 6.2832 = 1,591.55 Hz ≈ 1.59 kHz.
Paso 2: Factor de calidad:
Q = omega_0 L / R = (10,000 rad/s × 0.005 H) / 2.0 Omega = 50 / 2.0 = 25.0.
Paso 3: Ancho de banda:
BW = omega_0 / Q = 10,000 / 25.0 = 400 rad/s.
Delta f = BW / (2 pi) = 400 / 6.2832 = 63.66 Hz.
Paso 4: Frecuencias de media potencia (con Q >= 10, aproximación simétrica):
f_1 ≈ f_0 - Delta f / 2 = 1,591.55 - 31.83 = 1,559.72 Hz.
f_2 ≈ f_0 + Delta f / 2 = 1,591.55 + 31.83 = 1,623.38 Hz.
Paso 5: Tensión en el condensador en resonancia:
En resonancia, la corriente es I = V_in / R = 230 V / 2.0 Omega = 115 A RMS.
Reactancia capacitiva X_C = 1 / (omega_0 C) = 1 / (10,000 × 2 × 10⁻⁶) = 1 / 0.02 = 50 Omega.
V_C = I × X_C = 115 A × 50 Omega = 5,750 V = 5.75 kV RMS.
(Nótese que V_C = Q × V_in = 25 × 230 V = 5,750 V; el factor Q actúa como multiplicador de sobretensión en bornes reactivos).

Problema 2: En un circuito RLC paralelo con R = 5,000 Omega, L = 10 mH y C = 0.1 microfaradios, calcule el factor de calidad Q_paralelo.
Paso 1: omega_0 = 1 / sqrt(0.010 × 10⁻⁷) = 1 / sqrt(10⁻⁹) = 31,622.78 rad/s.
Paso 2: Q_paralelo = R / (omega_0 L) = 5,000 / (31,622.78 × 0.010) = 5,000 / 316.23 = 15.81.""",
        "bloque_sugerido": "Laboratorio AC 35 min • Resonancia serie y paralelo con barrido en frecuencia y curvas de admitancia"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Filtros Pasivos Pasa-Bajos, Pasa-Altos, Pasa-Banda y Notch en Redes Eléctricas",
        "objetivo": "Diseñar filtros de potencia pasivos de primer y segundo orden calculando funciones de transferencia H(s) y atenuación en armónicos.",
        "concepto_clave_latex": r"H_{\text{LP}}(s) = \frac{\omega_c}{s + \omega_c} \quad ; \quad H_{\text{HP}}(s) = \frac{s}{s + \omega_c} \quad ; \quad H_{\text{notch}}(s) = \frac{s^2 + \omega_0^2}{s^2 + \frac{\omega_0}{Q}s + \omega_0^2}",
        "ejemplo": """Problema 1: Se requiere diseñar un filtro notch pasivo (trampa de armónico) para eliminar el 5° armónico de red (f_0 = 300 Hz en sistema de 60 Hz, omega_0 = 2 pi × 300 = 600 pi ≈ 1,884.96 rad/s). Si se dispone de un condensador de C = 10 microfaradios (10 × 10⁻⁶ F) y se busca un factor de calidad Q = 20, calcule la inductancia requerida L [mH], la resistencia equivalente R [Omega] y el ancho de banda del notch BW [Hz].
Paso 1: Inductancia resonante:
omega_0 = 1 / sqrt(L C) => L = 1 / (omega_0^2 C) = 1 / [(1,884.96)^2 × (10 × 10⁻⁶)] = 1 / [3,553,074 × 10⁻⁵] = 1 / 35.531 = 0.02814 H = 28.14 mH.
Paso 2: Resistencia para Q = 20:
Q = omega_0 L / R => R = omega_0 L / Q = (1,884.96 × 0.02814) / 20 = 53.04 / 20 = 2.652 Omega.
Paso 3: Ancho de banda de rechazo:
Delta f = f_0 / Q = 300 Hz / 20 = 15.0 Hz (el filtro atenúa fuertemente entre 292.5 Hz y 307.5 Hz).

Problema 2: En un filtro pasa-bajos RC de primer orden con R = 1,000 Omega y C = 1.0 microfaradios, calcule la frecuencia de corte f_c [Hz] y la atenuación de ganancia en dB a una frecuencia de ruido de f = 10 f_c.
Paso 1: f_c = 1 / (2 pi R C) = 1 / (2 pi × 1000 × 10⁻⁶) = 1 / 0.006283 = 159.15 Hz.
Paso 2: Función de transferencia |H(j omega)| = 1 / sqrt(1 + (f / f_c)^2).
A f = 10 f_c: |H| = 1 / sqrt(1 + 10^2) = 1 / sqrt(101) = 1 / 10.0499 = 0.0995.
Paso 3: Ganancia en decibelios: 20 log_10(0.0995) = -20.04 dB ≈ -20 dB (pendiente asintótica de -20 dB/década).""",
        "bloque_sugerido": "Diseño de Filtros 35 min • Supresión de armónicos 5° y 7° en puentes rectificadores de 6 pulsos"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Transformadores Reales: Circuito Equivalente en T, Ensayos de Vacío y Cortocircuito",
        "objetivo": "Determinar los parámetros de resistencia, reactancia de dispersión y rama de magnetización a partir de pruebas estándar de laboratorio.",
        "concepto_clave_latex": r"R_{\text{fe}} = \frac{V_{\text{oc}}^2}{P_{\text{oc}}} \quad , \quad X_m = \frac{V_{\text{oc}}^2}{Q_{\text{oc}}} \quad ; \quad R_{\text{eq}} = \frac{P_{\text{sc}}}{I_{\text{sc}}^2} \quad , \quad X_{\text{eq}} = \sqrt{Z_{\text{sc}}^2 - R_{\text{eq}}^2} \quad [\Omega]",
        "ejemplo": """Problema 1: Un transformador de distribución monofásico de 50 kVA, 2,400 / 240 V, 60 Hz se somete a ensayos de laboratorio:
1. Ensayo de Vacío (Open Circuit, medido en el devanado de baja tensión 240 V):
V_oc = 240 V, I_oc = 4.5 A, P_oc = 320 W.
2. Ensayo de Cortocircuito (Short Circuit, medido en el devanado de alta tensión 2,400 V):
V_sc = 110 V, I_sc = 20.83 A (corriente nominal de AT), P_sc = 650 W.
Calcule los parámetros del circuito equivalente referidos al lado de alta tensión (relación de transformación a = 2,400 / 240 = 10).
Paso 1: Rama de excitación en BT:
Factor de potencia en vacío: cos(phi_oc) = P_oc / (V_oc I_oc) = 320 / (240 × 4.5) = 320 / 1080 = 0.2963.
phi_oc = arccos(0.2963) = 72.76°; sin(phi_oc) = 0.9551.
Paso 2: Parámetros en BT:
R_fe,BT = V_oc^2 / P_oc = (240)^2 / 320 = 57,600 / 320 = 180.0 Omega.
Q_oc = V_oc I_oc sin(phi_oc) = 1080 × 0.9551 = 1,031.5 VAR.
X_m,BT = V_oc^2 / Q_oc = 57,600 / 1031.5 = 55.84 Omega.
Paso 3: Rama de excitación referida a AT (multiplicar por a^2 = 100):
R_fe,AT = a^2 R_fe,BT = 100 × 180.0 = 18,000 Omega = 18.0 kOmega.
X_m,AT = a^2 X_m,BT = 100 × 55.84 = 5,584 Omega = 5.58 kOmega.
Paso 4: Impedancia equivalente de dispersión en AT:
R_eq,AT = P_sc / I_sc^2 = 650 / (20.83)^2 = 650 / 433.89 = 1.498 Omega ≈ 1.50 Omega.
Impedancia total: Z_sc,AT = V_sc / I_sc = 110 V / 20.83 A = 5.281 Omega.
Reactancia de dispersión: X_eq,AT = sqrt(Z_sc^2 - R_eq^2) = sqrt((5.281)^2 - (1.498)^2) = sqrt(27.889 - 2.244) = sqrt(25.645) = 5.064 Omega.

Problema 2: Calcule la regulación de tensión porcentual del transformador operando a plena carga nominal (S = 50 kVA, I_AT = 20.83 A) con factor de potencia 0.80 en atraso.
Paso 1: Delta V ≈ I_AT (R_eq cos(phi) + X_eq sin(phi)) = 20.83 × [1.498 × 0.80 + 5.064 × 0.60] = 20.83 × [1.1984 + 3.0384] = 20.83 × 4.2368 = 88.25 V.
Paso 2: Regulación = (Delta V / V_nominal) × 100 = (88.25 / 2400) × 100 = 3.68%.""",
        "bloque_sugerido": "Ensayos de Máquinas 40 min • Pruebas de vacío y cortocircuito según norma IEEE C57.12"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Transformadores Trifásicos: Grupos de Conexión (Dyn11, YNd11, Yy0) y Desfase Angular",
        "objetivo": "Analizar las conexiones trifásicas Y-Delta y Delta-Y, determinando el desfase angular horario en el diagrama fasorial.",
        "concepto_clave_latex": r"a_{\text{banco}} = \frac{V_{LL,\text{prim}}}{V_{LL,\text{sec}}} \quad ; \quad \text{Dyn11: BT adelanta } 330^\circ \equiv -30^\circ \text{ a AT} \quad ; \quad \mathbf{V}_{an} = \frac{1}{\sqrt{3}} \mathbf{V}_{ab} e^{-j 30^\circ}",
        "ejemplo": """Problema 1: Un transformador trifásico elevador de un parque eólico tiene una potencia de 5 MVA y relación de tensiones compuestas (línea-línea) de 0.69 kV / 34.5 kV conectado en grupo Dyn11 (primario en Delta en BT, secundario en Estrella con neutro accesible en MT, índice horario 11). Si la tensión de línea del secundario es V_AB = 34,500 V a 0° RMS: a) Halle la tensión simple de fase del secundario V_AN; b) Calcule la tensión de línea del primario V_ab y su ángulo de desfase exacto según el índice horario 11; c) Calcule las corrientes de línea nominales en ambos devanados.
Paso 1: Tensión fase-neutro en el secundario (Estrella):
|V_AN| = 34,500 / sqrt(3) = 19,918.6 V RMS.
Fasor V_AN = 19,918.6 a -30° V (en Estrella equilibrada, la fase atrasa 30° respecto a la línea V_AB).
Paso 2: Desfase angular por grupo Dyn11:
El índice horario 11 indica que la tensión de fase de BT atrasa (o adelanta según convención horaria de reloj: 11 horas = 11 × 30° = 330° atraso = 30° adelanto).
En Dyn11: la fase de baja tensión adelanta 30° a la fase correspondiente de alta tensión: V_an = (V_AN / a) e^(+j 30°).
Con V_AN a -30°: V_an = |V_an| a (-30° + 30°) = |V_an| a 0°.
Paso 3: Tensión de línea del primario: Como el primario está en Delta, V_ab = V_an = 690 a 0° V.
Paso 4: Corrientes de línea nominales:
I_L,MT = S_3f / (sqrt(3) V_LL,MT) = 5,000,000 VA / (sqrt(3) × 34,500 V) = 5,000,000 / 59,755 = 83.67 A.
I_L,BT = S_3f / (sqrt(3) V_LL,BT) = 5,000,000 VA / (sqrt(3) × 690 V) = 5,000,000 / 1,195.1 = 4,183.7 A.

Problema 2: ¿Pueden operar en paralelo dos transformadores trifásicos con grupos de conexión Yy0 y Dyn11?
Paso 1: No. El transformador Yy0 tiene un desfase de 0° entre tensiones homólogas, mientras que el Dyn11 tiene un desfase de 30°.
Paso 2: Conectar ambos secundarios en paralelo generaría una diferencia de potencial Delta V = 2 V_nom sin(30°/2) = 0.518 V_nom, lo que provocaría corrientes de circulación destructivas de cortocircuito.""",
        "bloque_sugerido": "Subestaciones Eléctricas 35 min • Verificación de polaridad y condiciones de paralelo de transformadores"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Componentes Simétricas de Fortescue: Secuencia Positiva, Negativa y Cero",
        "objetivo": "Descomponer fasores trifásicos desequilibrados de tensión y corriente en sus componentes desacopladas de secuencia positiva, negativa y cero.",
        "concepto_clave_latex": r"\begin{bmatrix} \mathbf{V}_0 \\ \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix}\begin{bmatrix} \mathbf{V}_a \\ \mathbf{V}_b \\ \mathbf{V}_c \end{bmatrix} \quad ; \quad a = e^{j 120^\circ} = -\frac{1}{2} + j\frac{\sqrt{3}}{2} \quad , \quad a^2 = e^{j 240^\circ}",
        "ejemplo": """Problema 1: En un sistema trifásico tetrafilar desbalanceado se miden las corrientes de fase a tierra: I_a = 100 a 0° A, I_b = 80 a -110° A, I_c = 60 a +130° A. Calcule las componentes simétricas de secuencia cero I_0, secuencia positiva I_1 y secuencia negativa I_2, y determine la corriente que retorna por el neutro I_n.
Paso 1: Conversión a rectangular:
I_a = 100 + j 0 A.
I_b = 80 [cos(-110°) + j sin(-110°)] = 80 [-0.3420 - j 0.9397] = -27.36 - j 75.18 A.
I_c = 60 [cos(130°) + j sin(130°)] = 60 [-0.6428 + j 0.7660] = -38.57 + j 45.96 A.
Paso 2: Secuencia cero I_0 = (1/3)(I_a + I_b + I_c):
Suma = (100 - 27.36 - 38.57) + j (0 - 75.18 + 45.96) = 34.07 - j 29.22 A = 44.89 a -40.6° A.
I_0 = (1/3)(34.07 - j 29.22) = 11.36 - j 9.74 A = 14.96 a -40.6° A.
Paso 3: Corriente de neutro:
I_n = I_a + I_b + I_c = 3 I_0 = 34.07 - j 29.22 A = 44.89 a -40.6° A.
Paso 4: Secuencia positiva I_1 = (1/3)(I_a + a I_b + a^2 I_c):
a I_b = (1 a 120°) × (80 a -110°) = 80 a 10° = 78.78 + j 13.89 A.
a^2 I_c = (1 a 240°) × (60 a 130°) = 60 a 370° = 60 a 10° = 59.09 + j 10.42 A.
Suma_1 = (100 + 78.78 + 59.09) + j (0 + 13.89 + 10.42) = 237.87 + j 24.31 A = 239.11 a 5.83° A.
I_1 = (1/3) Suma_1 = 79.29 + j 8.10 A = 79.70 a 5.83° A.
Paso 5: Secuencia negativa I_2 = (1/3)(I_a + a^2 I_b + a I_c):
a^2 I_b = (1 a 240°) × (80 a -110°) = 80 a 130° = -51.42 + j 61.28 A.
a I_c = (1 a 120°) × (60 a 130°) = 60 a 250° = -20.52 - j 56.38 A.
Suma_2 = (100 - 51.42 - 20.52) + j (0 + 61.28 - 56.38) = 28.06 + j 4.90 A.
I_2 = (1/3) Suma_2 = 9.35 + j 1.63 A = 9.49 a 9.9° A.

Problema 2: ¿En qué caso la secuencia cero es idénticamente nula?
Paso 1: En sistemas trifásicos trifilares sin conexión a neutro ni a tierra (Delta o Estrella aislada), donde I_a + I_b + I_c = 0 por la LCK, la corriente de secuencia cero es exactamente cero (I_0 = 0).""",
        "bloque_sugerido": "Análisis de Fortescue 40 min • Matriz de transformación de componentes simétricas en MATLAB/Python"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Redes de Secuencia y Matrices de Impedancia en Generadores y Transformadores",
        "objetivo": "Construir los diagramas unifilares de secuencia positiva, negativa y cero para generadores síncronos, transformadores y líneas aéreas.",
        "concepto_clave_latex": r"\begin{bmatrix} \mathbf{V}_{a0} \\ \mathbf{V}_{a1} \\ \mathbf{V}_{a2} \end{bmatrix} = \begin{bmatrix} 0 \\ \mathbf{E}_a \\ 0 \end{bmatrix} - \begin{bmatrix} \mathbf{Z}_0 & 0 & 0 \\ 0 & \mathbf{Z}_1 & 0 \\ 0 & 0 & \mathbf{Z}_2 \end{bmatrix}\begin{bmatrix} \mathbf{I}_{a0} \\ \mathbf{I}_{a1} \\ \mathbf{I}_{a2} \end{bmatrix} \quad ; \quad \mathbf{Z}_0^{\text{gen}} = j X_0 + 3 Z_n",
        "ejemplo": """Problema 1: Un generador síncrono de 100 MVA, 13.8 kV tiene reactancias de secuencia referidas a su base: X_1 = 0.20 p.u., X_2 = 0.15 p.u., y X_0 = 0.05 p.u. El neutro del generador está conectado a tierra a través de una reactancia limitadora X_n = 0.05 p.u. (Z_n = j 0.05 p.u.). Formule la matriz de impedancias de secuencia del generador visto desde sus terminales.
Paso 1: Impedancia de secuencia positiva:
Z_1 = j X_1 = j 0.20 p.u.
Paso 2: Impedancia de secuencia negativa:
Z_2 = j X_2 = j 0.15 p.u.
Paso 3: Impedancia de secuencia cero:
Z_0 = j X_0 + 3 Z_n = j 0.05 + 3 (j 0.05) = j 0.05 + j 0.15 = j 0.20 p.u.
(El factor 3 proviene de que la corriente que fluye por el neutro es I_n = 3 I_0).
Paso 4: Matriz diagonal de secuencia desacoplada:
Z_seq = diag [j 0.20,  j 0.20,  j 0.15] p.u.
Paso 5: Ecuaciones de tensión en terminales:
V_a0 = -Z_0 I_a0 = -j 0.20 I_a0.
V_a1 = E_a - Z_1 I_a1 = 1.0 a 0° - j 0.20 I_a1.
V_a2 = -Z_2 I_a2 = -j 0.15 I_a2.

Problema 2: ¿Cómo se modela la red de secuencia cero de un transformador Delta-Estrella con neutro sólidamente aterrizado (Dyn)?
Paso 1: El lado en Estrella aterrizada se conecta a la barra de referencia a través de la reactancia de fuga Z_0 = Z_1.
Paso 2: El lado en Delta crea un cortocircuito a tierra para la circulación interna de corrientes de secuencia cero, pero deja el circuito abierto hacia el sistema externo (aísla la secuencia cero).""",
        "bloque_sugerido": "Modelado de Sistemas de Potencia 35 min • Modelación de redes de secuencia de transformadores en ATP/EMTP"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Análisis de Cortocircuitos Simétricos: Fallas Trifásicas Francas y Corriente Subtransitoria",
        "objetivo": "Calcular corrientes de falla trifásica simétrica, reactancias subtransitorias X'' y capacidad de interrupción en interruptores de potencia.",
        "concepto_clave_latex": r"I_{\text{sc}}'' = \frac{E_a}{X_d''} \quad ; \quad S_{\text{sc}} = \sqrt{3} V_{LL,\text{nom}} I_{\text{sc}}'' = \frac{S_{\text{base}}}{X_{\text{th}}''} \quad [\text{MVA}] \quad ; \quad i(t) = \sqrt{2} I_{\text{sc}} \sin(\omega t - \theta) + \sqrt{2} I_{\text{sc}} \sin(\theta) e^{-t/\tau}",
        "ejemplo": """Problema 1: Un generador síncrono de 50 MVA, 13.8 kV con reactancia subtransitoria X_d'' = 0.12 p.u. alimenta un transformador elevador de 50 MVA, 13.8 / 115 kV con reactancia de fuga X_t = 0.08 p.u. Se produce una falla trifásica franca (impedancia de falla Z_f = 0) en el lado de 115 kV del transformador. Asumiendo tensión prefalla nominal E_a = 1.0 p.u.: a) Calcule la reactancia total Thévenin de la red; b) Calcule la corriente subtransitoria de falla en p.u. y en amperios reales RMS; c) Determine la potencia de cortocircuito S_sc [MVA].
Paso 1: Reactancia Thévenin en p.u. en base común de 50 MVA:
X_th'' = X_d'' + X_t = 0.12 + 0.08 = 0.20 p.u.
Paso 2: Corriente subtransitoria en p.u.:
I_sc'' = E_a / X_th'' = 1.0 / 0.20 = 5.0 p.u.
Paso 3: Corriente base en el lado de 115 kV:
I_base = S_base / (sqrt(3) V_base) = 50,000,000 VA / (sqrt(3) × 115,000 V) = 50,000 / 199.186 = 251.02 A.
Paso 4: Corriente subtransitoria real simétrica:
I_sc'' = 5.0 × 251.02 A = 1,255.1 A = 1.255 kA RMS.
Paso 5: Potencia de cortocircuito:
S_sc = S_base / X_th'' = 50 MVA / 0.20 = 250 MVA.
(Equivalente: sqrt(3) × 115 kV × 1.2551 kA = 250.0 MVA).

Problema 2: Calcule el valor de pico máximo absoluto que puede alcanzar la corriente de falla considerando la asimetría total por componente continua (offset de DC con factor de cresta 1.8 × sqrt(2)).
Paso 1: Corriente de pico máxima:
i_pico = sqrt(2) × I_sc'' × [1 + exp(-pi R / X)] ≈ 1.8 × sqrt(2) × I_sc'' = 2.545 × 1,255.1 A = 3,194 A = 3.19 kA pico.
Paso 2: Este valor pico dimensiona el esfuerzo electrodinámico que deben soportar los aisladores y barras de la subestación.""",
        "bloque_sugerido": "Protecciones Eléctricas 40 min • Cálculo de corrientes de cortocircuito según estándar IEEE C37 / IEC 60909"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Cortocircuito Asimétrico Monofásico a Tierra mediante Redes de Secuencia en Serie",
        "objetivo": "Calcular corrientes de falla y sobretensiones en fases sanas durante fallas monofásicas a tierra interconectando las redes de secuencia en serie.",
        "concepto_clave_latex": r"I_{a1} = I_{a2} = I_{a0} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f} \quad ; \quad I_{\text{falla}} = I_a = 3 I_{a0} \quad ; \quad \text{Redes en Serie}",
        "ejemplo": """Problema 1: En una barra de 13.8 kV de una central de generación (E_a = 1.0 a 0° p.u., S_base = 25 MVA) las impedancias de secuencia vistas desde la falla son: Z_1 = j 0.15 p.u., Z_2 = j 0.15 p.u., Z_0 = j 0.10 p.u. Ocurre una falla monofásica franca a tierra en la fase a (Z_f = 0). Calcule: a) Las corrientes de secuencia I_a1, I_a2, I_a0; b) La corriente de falla a tierra real I_falla [A]; c) Las tensiones de las fases sanas V_b y V_c en p.u. para evaluar el factor de sobretensión.
Paso 1: Corriente de secuencia positiva (redes 0, 1 y 2 en serie):
I_a1 = E_a / (Z_1 + Z_2 + Z_0) = 1.0 a 0° / (j 0.15 + j 0.15 + j 0.10) = 1.0 / (j 0.40) = -j 2.50 p.u. = 2.50 a -90° p.u.
Paso 2: I_a0 = I_a1 = I_a2 = -j 2.50 p.u.
Paso 3: Corriente total de falla en fase a:
I_a = I_a0 + I_a1 + I_a2 = 3 I_a0 = 3 × (-j 2.50) = -j 7.50 p.u.
Paso 4: Corriente base a 13.8 kV:
I_base = 25,000,000 / (sqrt(3) × 13,800) = 1,045.92 A.
Corriente real de falla: |I_falla| = 7.50 × 1,045.92 A = 7,844.4 A = 7.84 kA.
Paso 5: Tensiones de secuencia en el punto de falla:
V_a1 = E_a - Z_1 I_a1 = 1.0 - (j 0.15)(-j 2.50) = 1.0 - 0.375 = 0.625 p.u.
V_a2 = -Z_2 I_a2 = -(j 0.15)(-j 2.50) = -0.375 p.u.
V_a0 = -Z_0 I_a0 = -(j 0.10)(-j 2.50) = -0.250 p.u.
Comprobación fase a: V_a = V_a0 + V_a1 + V_a2 = -0.250 + 0.625 - 0.375 = 0 p.u. (tensión cero en la falla franca).
Paso 6: Tensiones de fases sanas:
V_b = V_a0 + a^2 V_a1 + a V_a2 = -0.250 + (1 a 240°)(0.625) + (1 a 120°)(-0.375)
= -0.250 + 0.625(-0.5 - j 0.866) - 0.375(-0.5 + j 0.866)
= -0.250 - 0.3125 - j 0.5413 + 0.1875 - j 0.3248 = -0.375 - j 0.8661 = 0.944 a -113.4° p.u.
Paso 7: Como |V_b| = 0.944 p.u. < 1.0 p.u., el sistema es sólidamente aterrizado y no sufre sobretensión perjudicial.

Problema 2: ¿Qué ocurriría con la tensión de las fases sanas si el neutro estuviese totalmente aislado (Z_0 -> inf)?
Paso 1: I_falla -> 0, pero la tensión de las fases sanas se eleva a la tensión compuesta: |V_b| = |V_c| = sqrt(3) V_fase ≈ 1.732 p.u. (sobretensión del 73%).""",
        "bloque_sugerido": "Análisis de Fallas 40 min • Ajuste de relés de sobrecorriente de tierra (51N/50N)"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Cortocircuitos Bifásico y Bifásico a Tierra: Redes de Secuencia en Paralelo",
        "objetivo": "Calcular corrientes y tensiones en fallas entre fases y bifásicas a tierra mediante la interconexión en paralelo de redes de secuencia.",
        "concepto_clave_latex": r"\text{Falla LL: } I_{a1} = -I_{a2} = \frac{E_a}{Z_1 + Z_2} \quad , \quad I_{a0} = 0 \quad ; \quad \text{Falla LLG: } I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 Z_0}{Z_2 + Z_0}}",
        "ejemplo": """Problema 1: En un sistema de potencia con E_a = 1.0 p.u., Z_1 = j 0.20 p.u. y Z_2 = j 0.20 p.u., ocurre una falla bifásica franca entre las fases b y c (falla línea-línea sin contacto a tierra, Z_f = 0). Calcule: a) Las corrientes de secuencia; b) Las corrientes en cada una de las fases a, b y c en p.u.
Paso 1: Por ser falla bifásica aislada de tierra, la corriente de secuencia cero es nula: I_a0 = 0.
Paso 2: Corriente de secuencia positiva (redes 1 y 2 en paralelo inverso):
I_a1 = E_a / (Z_1 + Z_2) = 1.0 a 0° / (j 0.20 + j 0.20) = 1.0 / (j 0.40) = -j 2.50 p.u.
Paso 3: Corriente de secuencia negativa:
I_a2 = -I_a1 = +j 2.50 p.u.
Paso 4: Corrientes de fase:
Fase sana a: I_a = I_a0 + I_a1 + I_a2 = 0 - j 2.50 + j 2.50 = 0 p.u. (sin corriente, correcto).
Fase b: I_b = I_a0 + a^2 I_a1 + a I_a2 = 0 + (1 a 240°)(-j 2.50) + (1 a 120°)(+j 2.50)
= (-0.5 - j 0.866)(-j 2.50) + (-0.5 + j 0.866)(j 2.50)
= (j 1.25 - 2.165) + (-j 1.25 - 2.165) = -4.33 p.u. = 4.33 a 180° p.u.
Fase c: I_c = -I_b = +4.33 p.u. = 4.33 a 0° p.u.
Paso 5: Magnitud de corriente de falla: |I_b| = |I_c| = sqrt(3) |I_a1| = 1.732 × 2.50 = 4.33 p.u.
Nótese que |I_LL| = (sqrt(3)/2) |I_3f| = 0.866 × 5.0 p.u. = 4.33 p.u. (la falla bifásica entrega el 86.6% de la falla trifásica).

Problema 2: En una falla bifásica a tierra (LLG), ¿cómo se conectan las redes de secuencia?
Paso 1: Las tres redes de secuencia (positiva, negativa y cero) se conectan en paralelo en el punto de falla:
V_a1 = V_a2 = V_a0, e I_a1 + I_a2 + I_a0 = 0.""",
        "bloque_sugerido": "Esquemas de Protección 35 min • Coordinación de relés de distancia (21) en fallas entre fases"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Sistema Por Unidad (p.u.): Cambio de Base y Normalización de Redes Eléctricas",
        "objetivo": "Transformar impedancias, potencias, tensiones y corrientes a valores normalizados por unidad y ejecutar cambios de base en sistemas multielevación.",
        "concepto_clave_latex": r"Z_{\text{base}} = \frac{V_{\text{base}}^2}{S_{\text{base}}} \quad [\Omega] \quad ; \quad Z_{\text{pu}}^{\text{nuevo}} = Z_{\text{pu}}^{\text{dado}} \left(\frac{V_{\text{base}}^{\text{dado}}}{V_{\text{base}}^{\text{nuevo}}}\right)^2 \left(\frac{S_{\text{base}}^{\text{nuevo}}}{S_{\text{base}}^{\text{dado}}}\right)",
        "ejemplo": """Problema 1: Un generador síncrono tiene datos de placa: S_nom = 30 MVA, V_nom = 13.8 kV, reactancia subtransitoria X_d'' = 0.18 p.u. (en su propia base). Se integra a un estudio de estabilidad del sistema eléctrico nacional donde las bases globales del sistema son S_base,sys = 100 MVA y V_base,sys = 13.2 kV en la barra de generación. Calcule la reactancia subtransitoria del generador X_d,sys'' expresada en la base del sistema.
Paso 1: Fórmula de cambio de base general:
X_pu,nuevo = X_pu,dado × (V_base,dado / V_base,nuevo)^2 × (S_base,nuevo / S_base,dado).
Paso 2: Relación de tensiones: (13.8 / 13.2)^2 = (1.04545)^2 = 1.0930.
Paso 3: Relación de potencias: (100 MVA / 30 MVA) = 3.3333.
Paso 4: Nueva reactancia en p.u.:
X_d,sys'' = 0.18 × 1.0930 × 3.3333 = 0.18 × 3.6433 = 0.6558 p.u.
Paso 5: La reactancia en la nueva base es 0.656 p.u. (aumenta porque la potencia base se incrementó en más de 3 veces).

Problema 2: Calcule el valor óhmico real de la reactancia del generador X_d'' [Omega] para verificar que el valor físico absoluto no cambia con la base elegida.
Paso 1: Impedancia base original:
Z_base,orig = V_base,orig^2 / S_base,orig = (13,800)^2 / 30,000,000 = 190,440,000 / 30,000,000 = 6.348 Omega.
Reactancia real: X = 0.18 × 6.348 Omega = 1.1426 Omega.
Paso 2: Comprobación con base nueva del sistema:
Z_base,nuevo = (13,200)^2 / 100,000,000 = 174,240,000 / 100,000,000 = 1.7424 Omega.
Reactancia real: X = 0.6558 × 1.7424 Omega = 1.1427 Omega. Los valores óhmicos reales coinciden al 100%.""",
        "bloque_sugerido": "Modelación p.u. 35 min • Diagrama de reactancias unifilar en sistemas de 4 zonas de tensión"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Líneas de Transmisión: Modelos Corto, Medio (Circuito Pi) y Largo con Parámetros Distribuidos",
        "objetivo": "Calcular la regulación de tensión, eficiencia y pérdidas en líneas de transporte de energía eléctrica utilizando los modelos equivalentes Pi nominal y exacto.",
        "concepto_clave_latex": r"\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix}\begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix} \quad ; \quad \mathbf{A} = \mathbf{D} = 1 + \frac{\mathbf{Z}\mathbf{Y}}{2} \quad , \quad \mathbf{B} = \mathbf{Z} \quad , \quad \mathbf{C} = \mathbf{Y}\left(1 + \frac{\mathbf{Z}\mathbf{Y}}{4}\right)",
        "ejemplo": """Problema 1: Una línea de transmisión trifásica de 230 kV, 60 Hz y longitud L = 100 km (línea de longitud media) tiene una impedancia serie total Z = 10 + j 40 Omega (0.10 + j 0.40 Omega/km) y una admitancia en paralelo total debida a la capacitancia distribuida Y = j 3.0 × 10⁻⁴ S (j 3.0 × 10⁻⁶ S/km). Alimentando en el extremo receptor una carga de 150 MVA con factor de potencia 0.85 en atraso a tensión nominal de 230 kV (V_R,LL = 230 kV): a) Calcule los parámetros ABCD del modelo Pi nominal; b) Determine la tensión de fase-neutro en el extremo emisor V_S; c) Calcule la regulación de tensión porcentual.
Paso 1: Parámetros ABCD:
Z Y = (10 + j 40)(j 3.0 × 10⁻⁴) = -0.012 + j 0.003.
A = D = 1 + Z Y / 2 = 1 + (-0.006 + j 0.0015) = 0.994 + j 0.0015 ≈ 0.994 a 0.086°.
B = Z = 10 + j 40 Omega = 41.23 a 75.96° Omega.
C = Y (1 + Z Y / 4) ≈ Y = j 3.0 × 10⁻⁴ S.
Paso 2: Tensión y corriente en el extremo receptor (fase-neutro):
V_R = 230,000 / sqrt(3) = 132,790.6 a 0° V.
I_R = S / (sqrt(3) V_LL) = 150,000,000 / (sqrt(3) × 230,000) = 376.53 A.
Con fp = 0.85 en atraso (phi = -31.79°): I_R = 376.53 a -31.79° A = 320.05 - j 198.37 A.
Paso 3: Tensión en el extremo emisor V_S = A V_R + B I_R:
A V_R = (0.994 + j 0.0015)(132,790.6) = 131,993.8 + j 199.2 V.
B I_R = (41.23 a 75.96°)(376.53 a -31.79°) = 15,524.3 a 44.17° V = 11,135.2 + j 10,816.5 V.
V_S = (131,993.8 + 11,135.2) + j (199.2 + 10,816.5) = 143,129.0 + j 11,015.7 V = 143,551.9 a 4.40° V.
Tensión compuesta en el emisor: V_S,LL = sqrt(3) × 143.55 kV = 248.64 kV.
Paso 4: Regulación de tensión:
Tensión en vacío en el receptor V_R,nl = |V_S| / |A| = 143,551.9 / 0.994 = 144,418.4 V.
Regulación = (|V_R,nl| - |V_R,fl|) / |V_R,fl| × 100 = (144,418.4 - 132,790.6) / 132,790.6 × 100 = (11,627.8 / 132,790.6) × 100 = 8.76%.

Problema 2: ¿Qué condición matemática deben cumplir los parámetros de cuadripolo ABCD para que una red sea recíproca y simétrica?
Paso 1: Reciprocidad: A D - B C = 1 (determinante unitario).
Paso 2: Simetría: A = D (los extremos emisor y receptor son físicamente intercambiables).""",
        "bloque_sugerido": "Líneas de Potencia 40 min • Modelo distribuido hiperbólico (cosh, sinh) en líneas de más de 250 km"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Efecto Ferranti y Sobretensiones en Vacío en Líneas de Transmisión Largas",
        "objetivo": "Cuantificar el incremento de tensión en el extremo receptor abierto de líneas de alta tensión debido a corrientes capacitivas de carga.",
        "concepto_clave_latex": r"V_R = \frac{V_S}{\cos(\beta L)} \approx V_S \left(1 + \frac{\omega^2 L^2}{2 v^2}\right) = V_S \left(1 + \frac{\omega^2 L^2 \mu \varepsilon}{2}\right) \quad ; \quad \Delta V \approx \frac{V_S \cdot \omega^2 L^2 l c}{2}",
        "ejemplo": """Problema 1: Una línea de transmisión de 500 kV, 60 Hz y longitud L = 300 km opera en vacío (extremo receptor desconectado, I_R = 0). La velocidad de propagación de la onda electromagnética es v ≈ c_0 = 300,000 km/s. La constante de fase es beta = omega / v = (2 pi × 60) / 300,000 = 377 / 300,000 = 1.2566 × 10⁻³ rad/km. Si la tensión en el extremo emisor se fija en V_S = 500 / sqrt(3) = 288.68 kV: a) Calcule el ángulo eléctrico total beta L en radianes y grados; b) Calcule la tensión de línea en el extremo abierto receptor V_R,LL por efecto Ferranti; c) Determine la potencia reactiva inductiva que debe absorber un reactor shunt en el receptor para neutralizar la sobretensión.
Paso 1: Longitud eléctrica:
beta L = (1.2566 × 10⁻³ rad/km)(300 km) = 0.3770 rad = 21.60°.
Paso 2: Tensión en el extremo receptor en vacío (I_R = 0 => V_S = A V_R = cos(beta L) V_R):
V_R = V_S / cos(beta L) = 288.68 kV / cos(21.60°) = 288.68 / 0.9298 = 310.47 kV (fase-neutro).
Tensión de línea compuesta: V_R,LL = sqrt(3) × 310.47 kV = 537.75 kV.
Paso 3: Sobretensión en vacío:
Delta V = 537.75 kV - 500.0 kV = +37.75 kV (sobretensión estacionaria del 7.55% que estresa los pararrayos y el aislamiento).
Paso 4: Si la admitancia capacitiva total es Y = j 1.5 × 10⁻³ S:
Potencia reactiva capacitiva generada en vacío: Q_c = 3 × |V_R|² × (Y/2) = 3 × (310.47 × 10³)² × (0.75 × 10⁻³) = 216.9 MVAr.
Paso 5: Se requiere conectar un banco de reactores shunt de aprox. 220 MVAr inductivos en la subestación receptora para fijar la tensión en 500 kV nominales.

Problema 2: ¿A qué longitud L la tensión en vacío tendería teóricamente al infinito por resonancia de cuarto de onda?
Paso 1: Cuando beta L = pi / 2 rad (90°): cos(beta L) = 0 => V_R -> inf.
Paso 2: L = (pi / 2) / beta = (pi / 2) / (1.2566 × 10⁻³) = 1.5708 / 0.0012566 = 1,250 km.""",
        "bloque_sugerido": "Compensación de Redes 35 min • Dimensionamiento de reactores de compensación shunt de núcleo de aire"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Compensación Reactiva Serie y Paralelo: FACTS y Capacidad de Transferencia (SIL)",
        "objetivo": "Calcular el incremento en el límite de potencia transferible y la impedancia natural de carga (SIL) mediante condensadores serie y compensadores estáticos (SVC).",
        "concepto_clave_latex": r"P_{\text{max}} = \frac{V_S V_R}{X_L (1 - k_{\text{se}})} \sin(\delta) \quad ; \quad k_{\text{se}} = \frac{X_C}{X_L} \quad ; \quad \text{SIL} = \frac{V_{\text{nom}}^2}{Z_0} = \frac{V_{\text{nom}}^2}{\sqrt{L/C}} \quad [\text{MW}]",
        "ejemplo": """Problema 1: Una línea de transmisión de 500 kV tiene una reactancia inductiva serie neta X_L = 50 Omega y una impedancia característica de onda Z_0 = sqrt(l/c) = 280 Omega. Calcule: a) La impedancia natural de carga (Surge Impedance Loading, SIL) en MW; b) El límite de estabilidad estática de potencia P_max para un ángulo de transmisión delta = 35° sin compensación; c) El nuevo valor de P_max si se instala un banco de condensadores serie con un grado de compensación del k_se = 40% (0.40).
Paso 1: Capacidad natural SIL:
SIL = V_nom^2 / Z_0 = (500 kV)^2 / 280 Omega = 250,000 / 280 = 892.86 MW.
(Cuando la línea transporta 893 MW, los reactivos inductivos consumidos en serie I² X_L equilibran exactamente los reactivos capacitivos generados en paralelo V² Y, logrando perfil plano de tensión).
Paso 2: Potencia transmitida sin compensación (delta = 35°):
P = (V_S V_R / X_L) sin(delta) = [(500 × 500) / 50] sin(35°) = (250,000 / 50) × 0.57358 = 5,000 × 0.57358 = 2,867.9 MW.
Paso 3: Con compensación serie del 40%:
Reactancia neta compensada X_comp = X_L (1 - k_se) = 50 × (1 - 0.40) = 50 × 0.60 = 30 Omega.
Paso 4: Nueva potencia transferible:
P_comp = [(500 × 500) / 30] sin(35°) = (250,000 / 30) × 0.57358 = 8,333.3 × 0.57358 = 4,779.8 MW.
Paso 5: La compensación serie incrementa la capacidad de transmisión en un 66.7% sin necesidad de tender nuevas líneas de alta tensión.

Problema 2: ¿Qué fenómeno dinámico perjudicial puede desencadenar la compensación serie en turbogeneradores térmicos?
Paso 1: Resonancia subsíncrona (SSR), donde la frecuencia natural del circuito eléctrico f_err = f_0 sqrt(k_se) coincide con los modos de vibración torsional del eje turbina-generador, provocando fracturas mecánicas si no se instala un filtro TCSC o relé subsíncrono.""",
        "bloque_sugerido": "Sistemas FACTS 40 min • STATCOM y TCSC para control dinámico de flujo de potencia"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Formulación de Flujo de Carga: Matriz de Admitancia de Barra Y_bus",
        "objetivo": "Construir sistemáticamente la matriz de admitancia nodal Y_bus incorporando líneas, transformadores con tomas no nominales y elementos en derivación.",
        "concepto_clave_latex": r"\mathbf{I}_{\text{bus}} = \mathbf{Y}_{\text{bus}} \mathbf{V}_{\text{bus}} \quad ; \quad Y_{ii} = \sum_{k \ne i} y_{ik} + y_{i0} \quad ; \quad Y_{ik} = -y_{ik} \quad (i \ne k)",
        "ejemplo": """Problema 1: Considere un sistema de potencia de 3 barras con las siguientes admitancias de línea serie: entre barra 1 y 2: y_12 = 2 - j 8 S; entre barra 1 y 3: y_13 = 1 - j 4 S; entre barra 2 y 3: y_23 = 1.5 - j 6 S. Cada línea aporta una admitancia capacitiva a tierra en derivación de y_sh / 2 = j 0.05 S en cada uno de sus extremos. Construya la matriz de admitancias de barra Y_bus [3x3].
Paso 1: Elementos diagonales Y_ii (suma de admitancias conectadas a la barra i incluyendo capacitancia a tierra):
Barra 1: Y_11 = y_12 + y_13 + y_c1 = (2 - j 8) + (1 - j 4) + j (0.05 + 0.05) = 3 - j 12 + j 0.10 = 3 - j 11.90 S.
Barra 2: Y_22 = y_12 + y_23 + y_c2 = (2 - j 8) + (1.5 - j 6) + j (0.05 + 0.05) = 3.5 - j 14 + j 0.10 = 3.5 - j 13.90 S.
Barra 3: Y_33 = y_13 + y_23 + y_c3 = (1 - j 4) + (1.5 - j 6) + j (0.05 + 0.05) = 2.5 - j 10 + j 0.10 = 2.5 - j 9.90 S.
Paso 2: Elementos fuera de la diagonal Y_ik = -y_ik:
Y_12 = Y_21 = -(2 - j 8) = -2 + j 8 S.
Y_13 = Y_31 = -(1 - j 4) = -1 + j 4 S.
Y_23 = Y_32 = -(1.5 - j 6) = -1.5 + j 6 S.
Paso 3: Ensamblaje de la matriz Y_bus:
Y_bus = [
  [3 - j 11.9,  -2 + j 8,    -1 + j 4],
  [-2 + j 8,    3.5 - j 13.9, -1.5 + j 6],
  [-1 + j 4,    -1.5 + j 6,   2.5 - j 9.9]
] S.

Problema 2: ¿Qué propiedad matemática exhibe la matriz Y_bus que facilita su almacenamiento y solución computacional en redes con miles de barras?
Paso 1: Es simétrica (Y_ik = Y_ki para redes sin transformadores desfasadores) y altamente dispersa (sparse, con más del 98% de elementos nulos), permitiendo algoritmos de factorización LU dispersa.""",
        "bloque_sugerido": "Algoritmos Matriciales 35 min • Modelación computacional de Y_bus en formato CSR (Compressed Sparse Row)"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Flujo de Carga Numérico: Métodos de Gauss-Seidel, Newton-Raphson y Desacoplado Rápido",
        "objetivo": "Formular las ecuaciones no lineales de balance de potencia activa y reactiva y resolverlas mediante el Jacobiano de Newton-Raphson.",
        "concepto_clave_latex": r"\begin{bmatrix} \Delta \mathbf{P} \\ \Delta \mathbf{Q} \end{bmatrix} = \begin{bmatrix} \mathbf{J}_1 & \mathbf{J}_2 \\ \mathbf{J}_3 & \mathbf{J}_4 \end{bmatrix}\begin{bmatrix} \Delta \boldsymbol{\theta} \\ \Delta |\mathbf{V}| \end{bmatrix} \quad ; \quad P_i = \sum_{k=1}^N |V_i||V_k|(G_{ik}\cos\theta_{ik} + B_{ik}\sin\theta_{ik})",
        "ejemplo": """Problema 1: En un sistema de potencia de 2 barras:
Barra 1: Barra oscilante (Slack bus): V_1 = 1.0 a 0° p.u.
Barra 2: Barra de carga (PQ bus): P_D2 = 1.2 p.u., Q_D2 = 0.6 p.u. (P_2 = -1.2 p.u., Q_2 = -0.6 p.u.).
La impedancia de la línea es Z = j 0.10 p.u. => Y_bus = [ [-j 10, j 10], [j 10, -j 10] ] p.u. (G_ik = 0, B_22 = -10, B_21 = 10).
Con valor inicial de arranque plano (flat start): |V_2|^(0) = 1.0 p.u., theta_2^(0) = 0 rad. Calcule los residuos de potencia Delta P_2 y Delta Q_2, evalúe los 4 términos del Jacobiano y halle las correcciones Delta theta_2 y Delta |V_2| en la primera iteración de Newton-Raphson.
Paso 1: Potencias calculadas en la iteración inicial:
P_2^(0) = |V_2||V_1| B_21 sin(theta_2 - theta_1) + |V_2|² B_22 sin(0) = (1)(1)(10) sin(0) = 0 p.u.
Q_2^(0) = -|V_2||V_1| B_21 cos(theta_2 - theta_1) - |V_2|² B_22 cos(0) = -(1)(1)(10)(1) - (1)²(-10)(1) = -10 + 10 = 0 p.u.
Paso 2: Residuos de potencia:
Delta P_2^(0) = P_2,prog - P_2^(0) = -1.2 - 0 = -1.2 p.u.
Delta Q_2^(0) = Q_2,prog - Q_2^(0) = -0.6 - 0 = -0.6 p.u.
Paso 3: Elementos del Jacobiano J = [ [J_1, J_2], [J_3, J_4] ]:
J_1 = d P_2 / d theta_2 = |V_2||V_1| B_21 cos(theta_2 - theta_1) = (1)(1)(10) cos(0) = 10.0.
J_2 = d P_2 / d |V_2| = |V_1| B_21 sin(0) = 0.
J_3 = d Q_2 / d theta_2 = |V_2||V_1| B_21 sin(0) = 0.
J_4 = d Q_2 / d |V_2| = -|V_1| B_21 cos(0) - 2 |V_2| B_22 = -(1)(10)(1) - 2(1)(-10) = -10 + 20 = 10.0.
Matriz Jacobiana diagonal desacoplada: J = [ [10, 0], [0, 10] ].
Paso 4: Solución del sistema lineal J [Delta theta_2, Delta |V_2|]^T = [Delta P_2, Delta Q_2]^T:
10 Delta theta_2 = -1.2 => Delta theta_2 = -0.120 rad (-6.88°).
10 Delta |V_2| = -0.6 => Delta |V_2| = -0.060 p.u.
Paso 5: Nuevos valores para la iteración 1:
theta_2^(1) = 0 + (-0.120) = -0.120 rad.
|V_2|^(1) = 1.0 + (-0.060) = 0.940 p.u.

Problema 2: ¿Por qué el método Desacoplado Rápido (FDLF) omite las submatrices J_2 y J_3?
Paso 1: Porque en líneas de alta tensión la relación X/R >> 1 desacopla fuertemente el flujo de potencia: la potencia activa P depende casi exclusivamente de los ángulos theta, y la potencia reactiva Q depende de las magnitudes de tensión |V|.""",
        "bloque_sugerido": "Simulación Numérica 40 min • Implementación del algoritmo Newton-Raphson de flujo de potencia en Python"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Despacho Económico de Generación: Costos Incrementales y Factores de Penalización",
        "objetivo": "Optimizar el reparto de carga entre unidades generadoras térmicas y renovables minimizando costos de combustible mediante multiplicadores de Lagrange.",
        "concepto_clave_latex": r"\frac{d C_i}{d P_{G i}} \cdot L_i = \lambda \quad [\text{\$/MWh}] \quad ; \quad L_i = \frac{1}{1 - \frac{\partial P_{\text{pérdidas}}}{\partial P_{G i}}} \quad ; \quad \sum_{i=1}^N P_{G i} = P_{\text{demanda}} + P_{\text{pérdidas}}",
        "ejemplo": """Problema 1: Una central térmica cuenta con dos turbogeneradores cuyos costos horarios de combustible vienen dados por:
C_1(P_1) = 0.004 P_1^2 + 8.0 P_1 + 200 [USD/h]
C_2(P_2) = 0.006 P_2^2 + 7.0 P_2 + 150 [USD/h]
donde P_1 y P_2 están en MW. La demanda total del sistema es P_D = 500 MW (despreciando pérdidas de transmisión). Calcule el despacho óptimo P_1 y P_2, el costo marginal del sistema lambda [USD/MWh] y el costo total de operación horario.
Paso 1: Funciones de costo incremental:
IC_1 = d C_1 / d P_1 = 0.008 P_1 + 8.0 [USD/MWh].
IC_2 = d C_2 / d P_2 = 0.012 P_2 + 7.0 [USD/MWh].
Paso 2: Criterio de costo incremental igual:
IC_1 = IC_2 = lambda =>
0.008 P_1 + 8.0 = lambda => P_1 = (lambda - 8.0) / 0.008 = 125 lambda - 1000.
0.012 P_2 + 7.0 = lambda => P_2 = (lambda - 7.0) / 0.012 = 83.333 lambda - 583.33.
Paso 3: Balance de potencia:
P_1 + P_2 = 500 => (125 lambda - 1000) + (83.333 lambda - 583.33) = 500.
208.333 lambda - 1583.33 = 500 => 208.333 lambda = 2083.33.
Paso 4: Multiplicador de Lagrange: lambda = 2083.33 / 208.333 = 10.00 USD/MWh.
Paso 5: Potencias despachadas:
P_1 = 125(10.00) - 1000 = 1250 - 1000 = 250 MW.
P_2 = 83.333(10.00) - 583.33 = 833.33 - 583.33 = 250 MW.
Paso 6: Costo total horario:
C_1(250) = 0.004(250)^2 + 8.0(250) + 200 = 250 + 2000 + 200 = 2,450 USD/h.
C_2(250) = 0.006(250)^2 + 7.0(250) + 150 = 375 + 1750 + 150 = 2,275 USD/h.
C_tot = 2,450 + 2,275 = 4,725 USD/h.

Problema 2: Si el generador 1 tiene pérdidas de transmisión con derivada marginal d P_loss / d P_1 = 0.05, halle su factor de penalización L_1.
Paso 1: L_1 = 1 / (1 - 0.05) = 1 / 0.95 = 1.0526.
Paso 2: Su costo incremental efectivo se penaliza en 5.26%, reduciendo su asignación en favor del generador más cercano a la carga.""",
        "bloque_sugerido": "Economía de la Energía 35 min • Despacho hidrotérmico y curvas de oferta en el mercado mayorista"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Estabilidad de Tensión: Curvas P-V y V-Q, y Margen de Colapso de Tensión",
        "objetivo": "Evaluar la estabilidad de tensión en barras receptoras mediante curvas nariz P-V y determinar el punto de colapso por bifucación silla-nodo.",
        "concepto_clave_latex": r"P_{\text{crítico}} = \frac{V_S^2}{2 X}\left(1 - \sin\phi\right) \quad ; \quad V_{\text{crítico}} = \frac{V_S}{\sqrt{2(1 + \sin\phi)}} \quad ; \quad \frac{dQ}{dV} < 0 \implies \text{Inestabilidad}",
        "ejemplo": """Problema 1: Una barra de carga está alimentada por una línea puramente inductiva con reactancia X = 0.25 p.u. desde una barra infinita con tensión V_S = 1.0 p.u. La carga opera con factor de potencia unitario (cos(phi) = 1, sin(phi) = 0, Q = 0). Calcule: a) La potencia activa máxima transferible P_crit (punto de inflexión de la curva nariz P-V); b) La tensión en la barra en el punto crítico V_crit; c) Los dos valores posibles de tensión para una demanda submáxima P = 1.5 p.u. (solución de alto y bajo voltaje).
Paso 1: Potencia crítica de colapso con fp = 1:
P_crit = V_S^2 / (2 X) = (1.0)^2 / [2 × 0.25] = 1.0 / 0.50 = 2.0 p.u.
Paso 2: Tensión en el colapso:
V_crit = V_S / sqrt(2) = 1.0 / 1.4142 = 0.7071 p.u.
Paso 3: Ecuación cuadrática para V^2 con P = 1.5 p.u.:
La relación P-V para línea puramente inductiva es: V^4 - V_S^2 V^2 + (P X)^2 = 0.
V^4 - (1.0)^2 V^2 + (1.5 × 0.25)^2 = 0 => V^4 - V^2 + (0.375)^2 = 0 => V^4 - V^2 + 0.140625 = 0.
Paso 4: Raíces de V^2:
V^2 = [1.0 ± sqrt(1.0^2 - 4 × 1 × 0.140625)] / 2 = [1.0 ± sqrt(1.0 - 0.5625)] / 2 = [1.0 ± sqrt(0.4375)] / 2 = [1.0 ± 0.66144] / 2.
Raíz superior: V_sup^2 = 1.66144 / 2 = 0.83072 => V_sup = sqrt(0.83072) = 0.9114 p.u. (punto de operación estable).
Raíz inferior: V_inf^2 = 0.33856 / 2 = 0.16928 => V_inf = sqrt(0.16928) = 0.4114 p.u. (punto inestable).

Problema 2: ¿Cómo desplaza una carga inductiva con fp = 0.8 atraso (sin(phi) = 0.6) el límite de colapso?
Paso 1: P_crit = [V_S^2 / (2 X)] (1 - sin(phi)) = 2.0 × (1 - 0.6) = 2.0 × 0.4 = 0.80 p.u.
Paso 2: La demanda inductiva reduce la capacidad máxima de la línea de 2.0 p.u. a solo 0.80 p.u., demostrando que el consumo reactivo precipita el colapso de tensión.""",
        "bloque_sugerido": "Seguridad Eléctrica 40 min • Curvas V-Q y dimensionamiento de márgenes de reserva de potencia reactiva"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Transitorios Electromagnéticos: Maniobras de Interruptores y Ondas Viajeras (Bergeron)",
        "objetivo": "Calcular sobretensiones de maniobra por energización de líneas en vacío y modelar la propagación de ondas viajeras mediante el método de Bergeron.",
        "concepto_clave_latex": r"i(x,t) + \frac{v(x,t)}{Z_c} = \text{const.} \quad [\text{Invariante de Riemann}] \quad ; \quad V_{\text{max}} = 2 V_{\text{pico}} \quad ; \quad Z_c = \sqrt{\frac{L}{C}} \approx 300\text{ a }400\,\Omega",
        "ejemplo": """Problema 1: Se energiza una línea de transmisión aérea de 230 kV (V_pico = 230 × sqrt(2/3) = 187.8 kV fase-neutro) en vacío en el instante de máximo voltaje senoidal (tensión escalón V_0 = 187.8 kV). La impedancia de onda de la línea es Z_c = 350 Omega y la impedancia interna de la fuente es despreciable. Calcule el voltaje en el extremo abierto receptor tras el primer rebote de la onda viajera.
Paso 1: Coeficiente de reflexión en el extremo receptor abierto (Z_L = inf):
r_R = (Z_L - Z_c) / (Z_L + Z_c) = (inf - 350) / (inf + 350) = +1.0.
Paso 2: Voltaje incidente hacia el receptor: V_inc = V_0 = 187.8 kV.
Paso 3: Voltaje reflejado: V_ref = r_R × V_inc = +1.0 × 187.8 = 187.8 kV.
Paso 4: Voltaje total en el extremo receptor al llegar la onda (t = tau):
V_R = V_inc + V_ref = 187.8 + 187.8 = 375.6 kV (exactamente el doble del voltaje pico).
Paso 5: La sobretensión transitoria duplica la tensión nominal, requiriendo resistencias de pre-inserción en el interruptor de maniobra.

Problema 2: En el extremo de la fuente ideal (Z_S = 0), ¿cuál es el coeficiente de reflexión para la onda que regresa?
Paso 1: r_S = (Z_S - Z_c) / (Z_S + Z_c) = (0 - 350) / (0 + 350) = -1.0.
Paso 2: La onda se refleja con polaridad invertida, estabilizando progresivamente la tensión en el valor de la fuente tras múltiples tránsitos amortiguados por pérdidas.""",
        "bloque_sugerido": "Simulación EMTP 35 min • Diagramas de celosía de Bewley y amortiguamiento por efecto corona"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Armónicos en Redes Industriales: Resonancia Paralela y Filtros Activos de Potencia (APF)",
        "objetivo": "Evaluar el riesgo de resonancia armónica paralela entre bancos de condensadores y el transformador de alimentación, diseñando filtros activos shunt.",
        "concepto_clave_latex": r"h_{\text{res}} = \sqrt{\frac{S_{\text{sc}}}{Q_C}} = \sqrt{\frac{X_C}{X_{\text{sc}}}} \quad ; \quad \text{THD}_I = \frac{\sqrt{\sum_{h=2}^\infty I_h^2}}{I_1} \quad ; \quad \mathbf{i}_{\text{filtro}}(t) = -\sum_{h=2}^\infty \mathbf{i}_h(t)",
        "ejemplo": """Problema 1: Una planta industrial alimentada por un transformador de 2,000 kVA (impedancia de cortocircuito en bornes S_sc = 40 MVA = 40,000 kVA a 480 V) instala un banco de condensadores de Q_C = 600 kVAR para corregir el factor de potencia. Una carga no lineal de rectificadores de 6 pulsos inyecta armónicos de orden h = 5, 7, 11, 13. Calcule: a) El orden armónico de resonancia paralela h_res; b) Verifique si existe coincidencia peligrosa con algún armónico característico de la carga; c) Determine la inductancia de choque anti-resonante desintonizada (reactor al 7%) requerida para desplazar la resonancia a una zona segura.
Paso 1: Orden armónico de resonancia paralela:
h_res = sqrt(S_sc / Q_C) = sqrt(40,000 / 600) = sqrt(66.67) = 8.16.
Paso 2: Como h_res = 8.16 está muy próximo al 7° armónico inyectado (h = 7), el banco y el transformador forman un circuito tanque paralelo de altísima impedancia para 420 Hz, lo que causará severas sobretensiones y quemado de fusibles por amplificación armónica.
Paso 3: Para evitar resonancia en h >= 5, se desintoniza el banco conectando un reactor serie con factor p = X_L / X_C = 0.07 (7%):
h_sintonía = 1 / sqrt(p) = 1 / sqrt(0.07) = 1 / 0.2646 = 3.78 (226.8 Hz).
Paso 4: Al estar sintonizado en 3.78 (por debajo del 5° armónico h = 5), el conjunto reactor-condensador es inductivo para todos los armónicos h >= 5, imposibilitando físicamente la resonancia paralela.

Problema 2: ¿Cómo neutraliza un Filtro Activo de Potencia (Shunt Active Power Filter) la distorsión armónica?
Paso 1: Mide en tiempo real la corriente de carga no lineal, extrae la componente fundamental mediante la teoría p-q de Akagi, y genera mediante un inversor IGBT una corriente en contrafase exacta i_filtro = -i_armónicos, logrando que la corriente vista por la red sea puramente senoidal.""",
        "bloque_sugerido": "Calidad de Energía 40 min • Filtros pasivos desintonizados vs filtros activos shunt (APF)"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Sistemas de Puesta a Tierra en Subestaciones: Tensiones de Paso y Contacto (IEEE 80)",
        "objetivo": "Dimensionar mallas de puesta a tierra para subestaciones eléctricas calculando resistencia de dispersión, tensión de paso y tensión de contacto tolerables.",
        "concepto_clave_latex": r"R_g = \rho \left[\frac{1}{L_T} + \frac{1}{\sqrt{20 A}}\left(1 + \frac{1}{1 + h\sqrt{20/A}}\right)\right] \quad ; \quad E_{\text{contacto}} = \left(1000 + 1.5 C_s \rho_s\right)\frac{0.116}{\sqrt{t_s}} \quad [\text{V}]",
        "ejemplo": """Problema 1: Una subestación eléctrica de 115/13.8 kV ocupa un área de malla de A = 2,500 m² (50 m × 50 m) con conductores de cobre enterrados a una profundidad h = 0.50 m, con una longitud total de conductores de malla L_T = 1,200 metros. La resistividad del terreno homogéneo es rho = 80 Omega·m. La corriente máxima de falla monofásica que disipa la malla a tierra es I_G = 4,000 A (4.0 kA) con un tiempo de despeje de las protecciones t_s = 0.50 s. La superficie de la subestación está cubierta con una capa de grava triturada de 10 cm con resistividad húmeda rho_s = 2,500 Omega·m (factor de reducción C_s = 0.75). Calcule: a) La resistencia de puesta a tierra de la malla R_g mediante la fórmula simplificada de Sverak; b) La elevación de potencial de tierra de la malla (Ground Potential Rise, GPR) [kV]; c) La tensión de contacto máxima tolerable para un cuerpo humano de 50 kg según la norma IEEE 80.
Paso 1: Resistencia de puesta a tierra de la malla (Sverak):
Término 1: 1 / L_T = 1 / 1,200 = 0.000833 m⁻¹.
Término 2: sqrt(20 A) = sqrt(20 × 2,500) = sqrt(50,000) = 223.61 m.
1 / sqrt(20 A) = 1 / 223.61 = 0.004472 m⁻¹.
Término 3: h sqrt(20 / A) = 0.50 × sqrt(20 / 2500) = 0.50 × sqrt(0.008) = 0.50 × 0.08944 = 0.04472.
Factor paréntesis = 1 + 1 / (1 + 0.04472) = 1 + 1 / 1.04472 = 1 + 0.95719 = 1.9572.
Producto: (0.004472)(1.9572) = 0.008752 m⁻¹.
Suma dentro del corchete: 0.000833 + 0.008752 = 0.009585 m⁻¹.
Resistencia de la malla: R_g = rho × 0.009585 = 80 × 0.009585 = 0.7668 Omega ≈ 0.77 Omega (cumple con R_g < 1.0 Omega exigido por RETIE).
Paso 2: Elevación de potencial de tierra (GPR):
GPR = I_G × R_g = 4,000 A × 0.7668 Omega = 3,067.2 V ≈ 3.07 kV.
Paso 3: Tensión de contacto máxima tolerable para persona de 50 kg (IEEE 80):
E_contacto = [1,000 + 1.5 C_s rho_s] × (0.116 / sqrt(t_s))
= [1,000 + 1.5 × 0.75 × 2,500] × (0.116 / sqrt(0.50))
= [1,000 + 2,812.5] × (0.116 / 0.7071)
= 3,812.5 × 0.16405 = 625.4 V.

Problema 2: Si el potencial de toque calculado en el borde exterior de la cerca perimetral es E_t = 480 V, ¿es segura la instalación?
Paso 1: Como E_t = 480 V < E_contacto,tolerable = 625.4 V, la instalación garantiza la seguridad de la vida humana y no provocará fibrilación ventricular durante la falla.""",
        "bloque_sugerido": "Seguridad en Subestaciones 40 min • Diseño computacional de mallas de puesta a tierra con norma IEEE 80"
    }
]

if __name__ == '__main__':
    yaml_text = format_topics_yaml(topics_03041820)
    inject_topics_after('      - codigo: "03021815"', yaml_text)
    print("03041820 Fundamentos de Electricidad II now has 30 topics!")
