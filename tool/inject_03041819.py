# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_10_to_20 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Fuentes Dependientes y Modelado de Dispositivos Activos en DC",
        "objetivo": "Resolver redes con fuentes controladas por tensión y corriente (VCVS, VCCS, CCVS, CCCS) mediante análisis sistemático.",
        "concepto_clave_latex": r"v_{\text{dep}} = \mu v_x \quad ; \quad i_{\text{dep}} = g_m v_x \quad ; \quad v_{\text{dep}} = r_m i_x \quad ; \quad i_{\text{dep}} = \beta i_x",
        "ejemplo": """CLASE MAGISTRAL: FUENTES CONTROLADAS Y MODELADO LINEAL
1. Las Cuatro Tipologías de Fuentes Dependientes:
A diferencia de las fuentes independientes cuyo valor es autónomo, las fuentes dependientes entregan una tensión o corriente proporcional a una variable x (voltaje o corriente) medida en otra rama del circuito:
- VCVS (Tensión controlada por tensión): Ganancia adimensional mu.
- VCCS (Corriente controlada por tensión): Transconductancia g_m en Siemens (A/V).
- CCVS (Tensión controlada por corriente): Transresistencia r_m en Ohmios (V/A).
- CCCS (Corriente controlada por corriente): Ganancia de corriente beta.
2. Tratamiento en Teoremas de Redes:
En el Teorema de Superposición y en el cálculo de la resistencia de Thévenin R_th, las fuentes dependientes NUNCA se apagan (no se cortocircuitan ni se abren); deben permanecer activas porque representan acoplamientos físicos internos (transistores BJT, MOSFETs, amplificadores).
3. Problema Resuelto 1 (Aplicación Directa):
En un circuito con una fuente independiente V_s = 24 V en serie con R_1 = 4 Ohm y una fuente dependiente de corriente en paralelo con R_2 = 8 Ohm que inyecta i_dep = 2 * i_1 (donde i_1 es la corriente que pasa por R_1). Calcule la corriente i_1 y el voltaje v_2 sobre R_2.
Solución:
Por la Ley de Corrientes de Kirchhoff en el nodo superior de R_2:
i_1 + i_dep = i_2 ==> i_1 + 2 * i_1 = i_2 ==> i_2 = 3 * i_1.
El voltaje en el nodo es v_2 = i_2 * R_2 = (3 * i_1) * 8 = 24 * i_1.
Por la Ley de Voltajes de Kirchhoff en la malla de entrada:
V_s - i_1 * R_1 - v_2 = 0
24 - 4 * i_1 - 24 * i_1 = 0 ==> 24 - 28 * i_1 = 0
i_1 = 24 / 28 = 6 / 7 approx 0.8571 A.
Voltaje sobre R_2:
v_2 = 24 * (6 / 7) = 144 / 7 approx 20.57 V.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Determine la resistencia de Thévenin R_th vista desde los terminales a-b de un circuito que contiene una resistencia R = 10 Ohm en paralelo con una fuente dependiente de corriente CCCS i_dep = 0.6 * i_test, aplicando una fuente de prueba externa v_test = 1 V.
Solución:
Conectamos una fuente de prueba v_test = 1.0 V entre los terminales a-b e inyectamos una corriente de prueba i_test.
La tensión en bornes de la resistencia R es exactamente v_test = 1.0 V.
Corriente que baja por la resistencia R:
i_R = v_test / R = 1.0 V / 10 Ohm = 0.10 A.
Por LCK en el nodo de prueba:
i_test + i_dep = i_R
i_test + 0.6 * i_test = i_R ==> 1.6 * i_test = 0.10 A.
i_test = 0.10 / 1.6 = 0.0625 A = 62.5 mA.
Resistencia de Thévenin equivalente:
R_th = v_test / i_test = 1.0 V / 0.0625 A = 16.0 Ohmios.
(La presencia de la fuente dependiente elevó la resistencia aparente de 10 Ohm a 16 Ohm debido a la realimentación negativa de corriente).""",
        "bloque_sugerido": "Laboratorio 50 min • Fuentes dependientes y resistencia de Thévenin",
        "slides": [
            {"numero": 1, "seccion": "FUENTES DEP", "titulo": "Tipologías VCVS, VCCS, CCVS, CCCS", "puntos": ["Representación de transistores y etapas de amplificación electrónica.", "Prohibición estricta de apagar fuentes dependientes en Thévenin."]},
            {"numero": 2, "seccion": "MÉTODO", "titulo": "Técnica de la Fuente de Prueba", "puntos": ["Inyección de v_test = 1 V o i_test = 1 A para medir R_th = v_test / i_test.", "Impacto de la realimentación activa en la impedancia equivalente de entrada."]}
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Teorema de Tellegen y Conservación de Potencia en Redes",
        "objetivo": "Demostrar el balance de potencia global sum p_k = 0 en redes arbitrarias lineales y no lineales mediante Tellegen.",
        "concepto_clave_latex": r"\sum_{k=1}^b v_k i_k = 0 \quad ; \quad \sum_{k=1}^b v_k' i_k'' = 0 \quad (\forall \text{ topología común})",
        "ejemplo": """CLASE MAGISTRAL: TEOREMA DE TELLEGEN Y CONSERVACIÓN TOPOLÓGICA
1. Enunciado Fundamental de Bernard Tellegen (1952):
En cualquier red eléctrica concentrada de b ramas que cumpla las leyes de Kirchhoff (LCK y LVK), la suma algebraica de los productos de tensión e intensidad de rama tomados con la convención pasiva de signos es idénticamente nula: sum_{k=1}^b v_k * i_k = 0.
2. Universalidad del Teorema:
Tellegen no depende de la naturaleza de los elementos: es válido para redes lineales o no lineales, pasivas o activas, variantes o invariantes en el tiempo. Se sustenta únicamente en la ortogonalidad topológica entre el espacio vectorial de tensiones de lazo y corrientes nodales (KCL y KVL).
3. Forma Cuasi-Potencial (Doble Red):
Si dos redes tienen exactamente la misma topología de grafo pero diferentes elementos (red ' y red ''), entonces sum v_k' * i_k'' = 0.
4. Problema Resuelto 1 (Aplicación Directa):
Un circuito de 5 ramas reporta las siguientes mediciones:
- Rama 1 (Fuente): v_1 = -48 V, i_1 = 2.5 A.
- Rama 2 (Resistor): v_2 = 20 V, i_2 = 1.0 A.
- Rama 3 (Resistor): v_3 = 28 V, i_3 = 1.5 A.
- Rama 4 (Carga activa): v_4 = 18 V, i_4 = 2.0 A.
- Rama 5 (Elemento X desconocido): v_5 = -10 V.
Determine la corriente i_5 que fluye por la rama 5 y valide el Teorema de Tellegen.
Solución:
Cálculo de potencias por convención pasiva (p = v * i):
p_1 = (-48 V) * (2.5 A) = -120.0 W (entrega 120 W).
p_2 = (20 V) * (1.0 A) = +20.0 W (consume 20 W).
p_3 = (28 V) * (1.5 A) = +42.0 W (consume 42 W).
p_4 = (18 V) * (2.0 A) = +36.0 W (consume 36 W).
Por el Teorema de Tellegen:
sum p_k = 0 ==> p_1 + p_2 + p_3 + p_4 + p_5 = 0
-120.0 + 20.0 + 42.0 + 36.0 + p_5 = 0
-120.0 + 98.0 + p_5 = 0 ==> -22.0 + p_5 = 0 ==> p_5 = +22.0 W.
Como p_5 = v_5 * i_5:
+22.0 W = (-10 V) * i_5 ==> i_5 = 22.0 / (-10) = -2.2 A.
El elemento 5 consume 22 W de potencia con una corriente de -2.2 A.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente el Teorema de Tellegen sum v_k * i_k = 0 utilizando la matriz de incidencia nodal A de dimensiones (n-1) x b del grafo del circuito.
Solución:
Por la Ley de Corrientes de Kirchhoff en forma matricial: A * i = 0, donde i es el vector columna de corrientes de rama de dimensión (b x 1).
Por la Ley de Voltajes de Kirchhoff, las tensiones de rama v se expresan en función de los potenciales nodales e de dimensión ((n-1) x 1) como: v = A^T * e.
Calculamos la potencia total como el producto escalar matricial v^T * i:
v^T * i = (A^T * e)^T * i = (e^T * A) * i = e^T * (A * i).
Sustituyendo la LCK (A * i = 0):
v^T * i = e^T * (0) = 0.
Dado que v^T * i = sum_{k=1}^b v_k * i_k, se concluye rigurosamente que sum v_k * i_k = 0 para cualquier red que satisfaga las leyes de Kirchhoff. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Teorema de Tellegen y balance topológico",
        "slides": [
            {"numero": 1, "seccion": "TELLEGEN", "titulo": "Conservación de Potencia de Tellegen", "puntos": ["Ecuación universal sum v_k i_k = 0 válida para cualquier tecnología de red.", "Independencia de la linealidad: aplicable a diodos, baterías y cargas no lineales."]},
            {"numero": 2, "seccion": "TOPOLOGÍA", "titulo": "Ortogonalidad Espacial", "puntos": ["Demostración matemática mediante la matriz de incidencia nodal A.", "Base conceptual para teoremas de sensibilidad y reciprocidad."]}
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Métodos Avanzados de Supernodos y Supermallas con Fuentes Flotantes",
        "objetivo": "Formular ecuaciones nodales y de malla en circuitos con fuentes ideales independientes y dependientes no referenciadas.",
        "concepto_clave_latex": r"\text{Supernodo: } v_A - v_B = V_s \quad ; \quad \text{Supermalla: } i_2 - i_1 = I_s",
        "ejemplo": """CLASE MAGISTRAL: SUPERNODOS Y SUPERMALLAS EN ANÁLISIS SISTEMÁTICO
1. El Problema de las Fuentes Flotantes:
- Si una fuente de tensión ideal está conectada entre dos nodos no de referencia (nodo flotante), la corriente a través de la fuente no se puede determinar directamente por la Ley de Ohm (resistencia interna nula). Se define un Supernodo encerrando la fuente y los dos nodos en una superficie gaussiana cerrada, aplicando LCK al supernodo y complementando con la ecuación de restricción v_A - v_B = V_s.
- Si una fuente de corriente ideal pertenece a dos mallas contiguas, su voltaje es desconocido. Se crea una Supermalla eliminando visualmente la rama de corriente común, aplicando LVK al lazo exterior y complementando con la restricción i_2 - i_1 = I_s.
2. Problema Resuelto 1 (Aplicación Directa):
En un circuito de dos nodos esenciales 1 y 2 con referencia 0, una fuente de tensión ideal V_s = 12 V está conectada entre el nodo 1 y el nodo 2 (polo positivo en 1). Desde el nodo 1 hay un resistor R_1 = 2 Ohm a tierra, y desde el nodo 2 hay un resistor R_2 = 4 Ohm a tierra. Una fuente de corriente independiente inyecta 6 A al nodo 1. Calcule las tensiones de nodo v_1 y v_2.
Solución:
1. Ecuación de restricción del Supernodo (1-2):
v_1 - v_2 = 12 V ==> v_1 = v_2 + 12.
2. LCK en el Supernodo (1-2):
Suma de corrientes que salen:
(v_1 / R_1) + (v_2 / R_2) - 6 = 0
(v_1 / 2) + (v_2 / 4) = 6.
Multiplicando por 4:
2 * v_1 + v_2 = 24.
Sustituyendo v_1 = v_2 + 12:
2 * (v_2 + 12) + v_2 = 24
2 * v_2 + 24 + v_2 = 24 ==> 3 * v_2 = 0 ==> v_2 = 0.0 V.
Tensión en el nodo 1:
v_1 = 0 + 12 = 12.0 V.
Corrientes: i_R1 = 12 / 2 = 6 A (toda la corriente de la fuente de 6A se drena por R1).
3. Problema Resuelto 2 (Nivel Examen Parcial):
Resuelva mediante Supermalla un circuito con dos mallas donde la rama compartida contiene una fuente dependiente de corriente CCCS de valor i_s = 3 * i_1 dirigida hacia arriba. La malla 1 tiene una fuente de voltaje V_1 = 30 V en serie con R_1 = 5 Ohm. La malla 2 tiene un resistor R_2 = 10 Ohm y una fuente de voltaje V_2 = 15 V. Determine las corrientes de malla i_1 e i_2.
Solución:
1. Ecuación de restricción de la rama compartida:
La fuente apunta en el sentido de la malla 2 y en contra de la malla 1:
i_2 - i_1 = i_s = 3 * i_1 ==> i_2 = 4 * i_1.
2. LVK en la Supermalla exterior (omitiendo la rama compartida):
- 30 + i_1 * R_1 + i_2 * R_2 + 15 = 0
- 15 + 5 * i_1 + 10 * i_2 = 0
5 * i_1 + 10 * i_2 = 15.
Sustituyendo i_2 = 4 * i_1:
5 * i_1 + 10 * (4 * i_1) = 15
5 * i_1 + 40 * i_1 = 15 ==> 45 * i_1 = 15.
i_1 = 15 / 45 = 1 / 3 A approx 0.3333 A.
Corriente de la malla 2:
i_2 = 4 * (1 / 3) = 4 / 3 A approx 1.3333 A.""",
        "bloque_sugerido": "Laboratorio 50 min • Formulación matricial de supernodos y supermallas",
        "slides": [
            {"numero": 1, "seccion": "SUPERNODOS", "titulo": "Fuentes Flotantes de Tensión", "puntos": ["Superficie gaussiana englobando la fuente y sus dos nodos contiguos.", "Ecuación constitutiva de restricción de potencial v_A - v_B = V_s."]},
            {"numero": 2, "seccion": "SUPERMALLAS", "titulo": "Fuentes Comunes de Corriente", "puntos": ["Omisión visual de la rama compartida para aplicar LVK al lazo exterior.", "Ecuación de ligadura entre corrientes de malla adyacentes i_2 - i_1 = I_s."]}
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Teorema de Reciprocidad y Dualidad en Redes Resistivas",
        "objetivo": "Aplicar el principio de reciprocidad en cuadripolos pasivos y transformar circuitos a sus topologías duales.",
        "concepto_clave_latex": r"\frac{I_2}{V_1} = \frac{I_1'}{V_2'} \quad ; \quad \text{Dualidad: } V \leftrightarrow I,\; R \leftrightarrow G,\; C \leftrightarrow L,\; \text{Malla} \leftrightarrow \text{Nodo}",
        "ejemplo": """CLASE MAGISTRAL: RECIPROCIDAD Y DUALIDAD EN CIRCUITOS
1. Teorema de Reciprocidad de Lorentz:
En cualquier red lineal, pasiva y bilateral con una única fuente independiente, si una fuente de tensión V aplicada en la rama 1 produce una corriente I en la rama 2, al trasladar la misma fuente V a la rama 2, se medirá exactamente la misma corriente I en la rama 1 (I_2 / V_1 = I_1' / V_2').
2. Principio de Dualidad Topológica:
Dos circuitos son duales si las ecuaciones de malla de uno tienen exactamente la misma forma matemática que las ecuaciones nodales del otro. La transformación dual mapea:
- Tensión (V) <-> Corriente (I)
- Resistencia (R) <-> Conductancia (G)
- Inductancia (L) <-> Capacitancia (C)
- Conexión Serie <-> Conexión Paralelo
- Lazo / Malla <-> Nodo esencial
3. Problema Resuelto 1 (Aplicación Directa):
Una red resistiva pasiva en T tiene R_1 = 10 Ohm, R_2 = 20 Ohm y rama central R_3 = 30 Ohm. Al aplicar una fuente V_1 = 60 V en la entrada 1, la corriente medida en cortocircuito en los terminales de salida 2 es I_2. Verifique analíticamente la reciprocidad calculando I_2 y luego I_1' al conectar 60 V en la salida 2 con la entrada 1 en cortocircuito.
Solución:
Caso A (Fuente en 1, corto en 2):
La resistencia en 2 está en paralelo con R_3: R_2 // R_3 = (20 * 30) / (20 + 30) = 600 / 50 = 12 Ohm.
Resistencia total vista por la fuente 1: R_in = R_1 + (R_2 // R_3) = 10 + 12 = 22 Ohm.
Corriente total suministrada: I_in = 60 V / 22 Ohm = 30 / 11 A.
Por divisor de corriente hacia la rama 2:
I_2 = I_in * [ R_3 / (R_2 + R_3) ] = (30 / 11) * [ 30 / 50 ] = (30 / 11) * (3 / 5) = 18 / 11 A approx 1.6364 A.
Caso B (Fuente en 2, corto en 1):
La rama 1 está en paralelo con R_3: R_1 // R_3 = (10 * 30) / (10 + 30) = 300 / 40 = 7.5 Ohm.
Resistencia total vista por la fuente 2: R_in' = R_2 + (R_1 // R_3) = 20 + 7.5 = 27.5 Ohm = 55 / 2 Ohm.
Corriente total suministrada: I_in' = 60 / (55 / 2) = 120 / 55 = 24 / 11 A.
Por divisor de corriente hacia la rama 1:
I_1' = I_in' * [ R_3 / (R_1 + R_3) ] = (24 / 11) * [ 30 / 40 ] = (24 / 11) * (3 / 4) = 18 / 11 A approx 1.6364 A.
Resultado: I_2 = I_1' = 18/11 A. El Teorema de Reciprocidad se cumple de forma exacta.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Dibuje el circuito dual de una malla simple compuesta por una fuente de tensión V_s = 100 V en serie con un resistor R = 50 Ohm y un inductor L = 2.0 H.
Solución:
Aplicando las reglas canónicas de dualidad:
1. La malla única se transforma en un par de nodos esenciales (un nodo no de referencia y tierra).
2. La fuente de tensión V_s = 100 V en serie se convierte en una fuente de corriente independiente I_s = 100 A en paralelo.
3. El resistor en serie R = 50 Ohm se convierte en una conductancia en paralelo G = 50 Siemens (resistencia R_dual = 1/50 = 0.02 Ohm).
4. El inductor en serie L = 2.0 H se convierte en un capacitor en paralelo C = 2.0 Faradios.
Ecuación diferencial original de malla: L * di/dt + R * i = V_s(t).
Ecuación diferencial del circuito dual nodal: C * dv/dt + G * v = I_s(t).
Ambas ecuaciones son formalmente idénticas bajo el isomorfismo i <-> v.""",
        "bloque_sugerido": "Laboratorio 50 min • Validación de reciprocidad y mapeo dual",
        "slides": [
            {"numero": 1, "seccion": "RECIPROCIDAD", "titulo": "Teorema de Reciprocidad", "puntos": ["Invarianza de la función de transferencia al permutar fuente y detector.", "Propiedad exclusiva de medios bilaterales lineales sin fuentes dependientes."]},
            {"numero": 2, "seccion": "DUALIDAD", "titulo": "Transformación Topológica Dual", "puntos": ["Correspondencia biyectiva entre mallas y nodos (V <-> I, R <-> G, L <-> C).", "Solución de redes complejas mediante transposición a su circuito dual."]}
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Amplificadores Operacionales Ideales I: Configuraciones Básicas",
        "objetivo": "Modelar el cortocircuito virtual y diseñar etapas inversoras, no inversoras, seguidores y sumadores.",
        "concepto_clave_latex": r"v_+ = v_- \quad (\text{Cortocircuito Virtual}) \quad ; \quad i_+ = i_- = 0 \quad ; \quad \frac{v_o}{v_i} = -\frac{R_f}{R_1} \quad ; \quad \frac{v_o}{v_i} = 1 + \frac{R_f}{R_1}",
        "ejemplo": """CLASE MAGISTRAL: AMPLIFICADORES OPERACIONALES (OP-AMP) IDEALES
1. Las Reglas de Oro del Op-Amp Ideal con Realimentación Negativa:
- Ganancia de tensión en lazo abierto infinita (A_OL -> infinito): Obliga a que la tensión diferencial de entrada sea nula en zona lineal: v_+ - v_- = 0 => v_+ = v_- (Cortocircuito Virtual).
- Impedancia de entrada infinita (R_in -> infinito): Ninguna corriente ingresa a los terminales de entrada: i_+ = i_- = 0.
- Impedancia de salida nula (R_out -> 0): La tensión de salida v_o es independiente de la corriente que demande la carga.
2. Configuraciones Lineales Fundamentales:
- Inversora: v_o = - (R_f / R_1) * v_i.
- No Inversora: v_o = (1 + R_f / R_1) * v_i.
- Seguidor de Tensión (Buffer de ganancia unitaria R_f = 0): v_o = v_i (aísla etapas sin efecto de carga).
- Sumador Inversor: v_o = - R_f * sum (v_k / R_k).
3. Problema Resuelto 1 (Aplicación Directa):
Diseñe un amplificador no inversor que acondicione la señal de un sensor de irradiancia solar de salida v_in = 0 a 100 mV para entregar una señal estandarizada de v_out = 0 a 5.0 V a la entrada analógica de un microcontrolador (ADC). Calcule los resistores R_1 y R_f considerando R_1 = 2.0 kOhm.
Solución:
Ganancia de tensión requerida:
A_v = v_out / v_in = 5.0 V / 0.100 V = 50.0.
Para configuración no inversora:
A_v = 1 + (R_f / R_1) = 50.0
R_f / R_1 = 49.0 ==> R_f = 49.0 * R_1.
Con R_1 = 2.0 kOhm:
R_f = 49.0 * 2.0 kOhm = 98.0 kOhm (se selecciona resistor de precisión al 0.1% de 98 kOhm o un potenciómetro multivuelta de 100 kOhm).
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un sumador inversor con R_f = 100 kOhm, se tienen tres entradas de telemetría de red: v_1 = 0.5 V con R_1 = 20 kOhm; v_2 = -1.2 V con R_2 = 40 kOhm; y v_3 = 0.8 V con R_3 = 50 kOhm. Calcule la tensión de salida v_o y determine la corriente que debe drenar la salida del amplificador si se conecta una carga R_L = 10 kOhm.
Solución:
1. Tensión de salida:
v_o = - R_f * [ (v_1 / R_1) + (v_2 / R_2) + (v_3 / R_3) ]
v_o = - 100 k * [ (0.5 / 20 k) + (-1.2 / 40 k) + (0.8 / 50 k) ]
v_o = - [ 5 * (0.5) + 2.5 * (-1.2) + 2 * (0.8) ]
v_o = - [ 2.5 - 3.0 + 1.6 ] = - [ 1.1 ] = -1.10 V.
2. Corrientes:
Corriente a través de la resistencia de realimentación R_f (nodo inversor a salida):
i_f = (v_- - v_o) / R_f = (0 - (-1.10 V)) / 100 kOhm = +1.10 V / 100 kOhm = 0.011 mA = 11.0 uA.
Corriente que drena la carga R_L conectada a la salida:
i_L = v_o / R_L = -1.10 V / 10 kOhm = -0.11 mA = -110.0 uA.
Por LCK en el nodo de salida del op-amp:
i_salida = i_f + i_L = 11.0 uA - 110.0 uA = -99.0 uA.
La salida del amplificador absorbe (hunde) 99 microamperios hacia sus rieles de alimentación negativos.""",
        "bloque_sugerido": "Laboratorio 50 min • Acondicionamiento de señales con Op-Amps",
        "slides": [
            {"numero": 1, "seccion": "OP-AMP", "titulo": "Reglas de Oro del Amplificador Ideal", "puntos": ["Cortocircuito virtual v_+ = v_- bajo realimentación negativa.", "Corrientes de polarización nulas i_+ = i_- = 0 por impedancia infinita."]},
            {"numero": 2, "seccion": "TOPOLOGÍAS", "titulo": "Inversor, No Inversor y Buffer", "puntos": ["Ganancia precisa fijada exclusivamente por la relación de resistencias externas.", "Seguidor de tensión para eliminar caídas por efecto de carga."]}
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Amplificadores Operacionales II: Diferencial, Instrumentación y CMRR",
        "objetivo": "Diseñar amplificadores de instrumentación de alta impedancia y modelar el Rechazo en Modo Común (CMRR).",
        "concepto_clave_latex": r"v_o = \frac{R_2}{R_1}(v_2 - v_1) \quad ; \quad A_d = \left(1 + \frac{2 R_1}{R_{\text{gain}}}\right)\frac{R_3}{R_2} \quad ; \quad \text{CMRR} = 20 \log_{10}\left|\frac{A_d}{A_{cm}}\right|",
        "ejemplo": """CLASE MAGISTRAL: AMPLIFICADORES DE INSTRUMENTACIÓN Y RECHAZO DE RUIDO
1. El Desafío del Ruido en Modo Común:
En entornos de subestaciones y plantas solares, las interferencias electromagnéticas de 60 Hz inducen ruidos idénticos en ambos conductores del cable apantallado (tensión en modo común v_cm). El amplificador debe amplificar únicamente la diferencia útil v_d = v_2 - v_1 y atenuar a cero el ruido común:
CMRR = 20 * log_10(|A_d / A_cm|) [dB]. Un valor superior a 100 dB es indispensable en instrumentación.
2. El Amplificador de Instrumentación Clásico de Tres Op-Amps (INA):
Consta de dos etapas:
- Etapa de entrada (dos buffers con ganancia cruzada): Proporciona impedancia de entrada diferencial casi infinita (del orden de Gigaohmios) y amplifica la señal diferencial mediante un único resistor ajustable R_gain: A_d1 = 1 + 2 R_1 / R_gain, dejando el modo común con ganancia unitaria.
- Etapa de salida (amplificador diferencial): Resta las señales y rechaza el modo común remanente.
3. Problema Resuelto 1 (Aplicación Directa):
Un amplificador diferencial estándar tiene R_1 = 10 kOhm y R_2 = 100 kOhm. Los resistores presentan una tolerancia del 0.1% garantizando una ganancia en modo diferencial A_d = 10.0 y una ganancia en modo común A_cm = 0.002. Calcule el CMRR en decibeles.
Solución:
CMRR = 20 * log_10( |A_d / A_cm| )
Relación de rechazo: A_d / A_cm = 10.0 / 0.002 = 5,000.
En decibeles:
CMRR = 20 * log_10(5000) = 20 * (3.69897) = 73.98 dB.
(Atenúa el ruido de modo común en 5,000 veces respecto a la señal útil).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Se acondiciona un puente de Wheatstone de un sensor de radiación solar usando un circuito integrado INA128 donde R_1 = 25 kOhm y la etapa de salida tiene ganancia unitaria (R_3 / R_2 = 1.0). La fórmula de ganancia del fabricante es A_d = 1 + (50 kOhm / R_gain). Si el sensor entrega una señal de desbalance v_d = 2.5 mV y se requiere v_out = 2.5 V:
a) Calcule la ganancia diferencial total A_d requerida.
b) Determine el valor exacto de la resistencia de calibración R_gain.
c) Si una interferencia de red induce v_cm = 1.0 V en modo común y el INA128 tiene CMRR = 120 dB, calcule la amplitud del error residual de modo común que aparece en la salida v_out.
Solución:
a) Ganancia diferencial:
A_d = v_out / v_d = 2.5 V / (2.5 * 10^-3 V) = 1,000.0.
b) Resistencia R_gain:
1,000 = 1 + (50,000 / R_gain) ==> 50,000 / R_gain = 999.
R_gain = 50,000 / 999 = 50.05 Ohmios.
c) Error de modo común en salida:
CMRR = 120 dB ==> 20 * log_10(A_d / A_cm) = 120 ==> log_10(A_d / A_cm) = 6 ==> A_d / A_cm = 10^6 = 1,000,000.
Ganancia en modo común: A_cm = A_d / 10^6 = 1,000 / 10^6 = 0.001 (10^-3).
Tensión de error en modo común en la salida:
v_o,cm = A_cm * v_cm = 0.001 * 1.0 V = 1.0 mV.
El ruido de 1 V inducido por la red de 60 Hz se redujo a solo 1 mV en la salida, representando un error relativo de apenas (1 mV / 2.5 V) = 0.04%.""",
        "bloque_sugerido": "Laboratorio 50 min • Amplificador de instrumentación INA y CMRR",
        "slides": [
            {"numero": 1, "seccion": "DIFERENCIAL", "titulo": "Rechazo de Modo Común (CMRR)", "puntos": ["Eliminación de ruido electromagnético de 60 Hz en cables apantallados.", "Métrica logarítmica CMRR = 20 log_10(A_d / A_cm) en decibeles."]},
            {"numero": 2, "seccion": "INA", "titulo": "Amplificador de Tres Op-Amps", "puntos": ["Impedancia de entrada en el orden de Gigaohmios sin efecto de carga.", "Sintonización de ganancia precisa mediante un único resistor R_gain."]}
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Mediciones Eléctricas en DC y Efecto de Carga de Instrumentos",
        "objetivo": "Cuantificar el error sistemático por inserción de voltímetros y amperímetros reales en circuitos DC.",
        "concepto_clave_latex": r"V_{\text{medido}} = V_{\text{th}} \frac{R_m}{R_m + R_{\text{th}}} \quad ; \quad I_{\text{medido}} = \frac{V_{\text{th}}}{R_{\text{th}} + R_a} \quad ; \quad \epsilon_{\text{rel}} = \frac{x_{\text{med}} - x_{\text{real}}}{x_{\text{real}}}\times 100\%",
        "ejemplo": """CLASE MAGISTRAL: METROLOGÍA ELÉCTRICA Y EFECTO DE CARGA
1. Instrumentos Ideales vs Instrumentos Reales:
- Voltímetro ideal: Resistencia interna infinita (R_m -> infinito), no extrae corriente del circuito al conectarse en paralelo.
- Voltímetro real: Resistencia interna finita (típicamente 10 MOhm en multímetros digitales DMM; 20 kOhm/V en analógicos). Al conectarse en paralelo con resistores de alto valor, altera la resistencia equivalente del circuito, midiendo una tensión menor a la real (Efecto de Carga).
- Amperímetro ideal: Resistencia interna nula (R_a -> 0).
- Amperímetro real: Resistencia serie finita (shunts internos). Introduce una caída de tensión adicional (Burden Voltage) que reduce la corriente del lazo.
2. Problema Resuelto 1 (Aplicación Directa):
Un divisor de tensión está formado por dos resistores idénticos R_1 = R_2 = 1.0 MOhm conectados a una fuente V_s = 20.0 V. El voltaje teórico de circuito abierto sobre R_2 es V_real = 10.0 V. Se mide con un multímetro digital cuya resistencia interna es R_m = 10 MOhm. Calcule el voltaje medido y el error relativo porcentual.
Solución:
Resistencia equivalente de R_2 en paralelo con el voltímetro:
R_eq = (R_2 * R_m) / (R_2 + R_m) = (1.0e6 * 10.0e6) / (1.0e6 + 10.0e6) = 10e12 / 11e6 = (10 / 11) MOhm approx 0.9091 MOhm.
Voltaje medido por el divisor con el instrumento conectado:
V_med = V_s * [ R_eq / (R_1 + R_eq) ]
V_med = 20.0 * [ 0.9091 / (1.0 + 0.9091) ] = 20.0 * [ 0.9091 / 1.9091 ] = 20.0 * 0.47619 = 9.524 V.
Error sistemático de inserción:
epsilon_rel = [ (V_med - V_real) / V_real ] * 100%
epsilon_rel = [ (9.524 - 10.0) / 10.0 ] * 100% = - 4.76 %.
El instrumento introduce un error por efecto de carga de casi el 5% debido a la alta impedancia de Thévenin de la red.
3. Problema Resuelto 2 (Nivel Examen Parcial):
Un lazo de corriente industrial de 4-20 mA en una subestación opera con V_th = 24 V y resistencia de línea y transmisor R_th = 1,200 Ohm. La corriente real es I_real = 24 V / 1,200 Ohm = 20.0 mA. Un técnico conecta un amperímetro analógico barato cuya resistencia interna es R_a = 50 Ohm para medir la corriente. Calcule la corriente medida y el voltaje de carga (Burden Voltage) que cae en el instrumento.
Solución:
Corriente medida con el amperímetro en serie:
I_med = V_th / (R_th + R_a) = 24 V / (1,200 + 50 Ohm) = 24 / 1,250 = 0.0192 A = 19.20 mA.
Error relativo:
epsilon_rel = [ (19.20 - 20.0) / 20.0 ] * 100% = - 4.00 %.
Voltaje de carga sobre el amperímetro (Burden Voltage):
V_burden = I_med * R_a = (0.0192 A) * (50 Ohm) = 0.960 V.
Casi 1 voltio se pierde en el propio instrumento, falseando la lectura del sensor.""",
        "bloque_sugerido": "Laboratorio 50 min • Medición de impedancia interna y efecto de carga",
        "slides": [
            {"numero": 1, "seccion": "METROLOGÍA", "titulo": "Efecto de Carga de Voltímetros", "puntos": ["Resistencia interna finita R_m en paralelo con la red.", "Fórmula de corrección de error sistemático V_med = V_th R_m / (R_m + R_th)."]},
            {"numero": 2, "seccion": "AMPERÍMETROS", "titulo": "Burden Voltage en Lazos de Corriente", "puntos": ["Resistencia serie R_a introduciendo caídas de voltaje parásitas.", "Selección de multímetros con categoría de seguridad CAT III/IV."]}
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Redes de Dos Puertos (Two-Port Networks) en DC",
        "objetivo": "Modelar cuadripolos lineales mediante parámetros de impedancia (z), admitancia (y) y transmisión (ABCD).",
        "concepto_clave_latex": r"\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} z_{11} & z_{12} \\ z_{21} & z_{22} \end{bmatrix}\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} \quad ; \quad \begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix}\begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}",
        "ejemplo": """CLASE MAGISTRAL: TEORÍA DE CUADRIPOLOS (TWO-PORT NETWORKS)
1. Representación Matricial de Redes de Dos Puertos:
Permite tratar bloques circuitales complejos (filtros, líneas de transmisión, transformadores) como cajas negras caracterizadas exclusivamente por la relación entre las variables en los terminales del puerto 1 (V_1, I_1) y del puerto 2 (V_2, I_2).
2. Parámetros de Impedancia (Z-parameters - circuito abierto):
V_1 = z_11 * I_1 + z_12 * I_2
V_2 = z_21 * I_1 + z_22 * I_2
z_11 = (V_1 / I_1)|_{I_2=0} ; z_12 = (V_1 / I_2)|_{I_1=0} ; z_21 = (V_2 / I_1)|_{I_2=0} ; z_22 = (V_2 / I_2)|_{I_1=0}.
Si la red es recíproca: z_12 = z_21. Si es simétrica: z_11 = z_22.
3. Parámetros de Transmisión (ABCD - cascada):
Fundamentales para modelar líneas de transmisión eléctricas:
V_1 = A * V_2 + B * (-I_2)
I_1 = C * V_2 + D * (-I_2). Condición de reciprocidad: A*D - B*C = 1.
4. Problema Resuelto 1 (Aplicación Directa):
Determine la matriz de parámetros Z para una red resistiva pasiva en T simétrica con dos ramas serie R_s = 20 Ohm y una rama paralelo central R_p = 40 Ohm.
Solución:
1. z_11 (resistencia de entrada con puerto 2 abierto, I_2 = 0):
z_11 = V_1 / I_1 = R_s + R_p = 20 + 40 = 60.0 Ohmios.
2. z_22 (resistencia de salida con puerto 1 abierto, I_1 = 0):
z_22 = V_2 / I_2 = R_s + R_p = 20 + 40 = 60.0 Ohmios.
3. z_12 (voltaje en puerto 1 con I_1 = 0 e inyección I_2):
V_1 = R_p * I_2 ==> z_12 = V_1 / I_2 = R_p = 40.0 Ohmios.
4. z_21 (voltaje en puerto 2 con I_2 = 0 e inyección I_1):
V_2 = R_p * I_1 ==> z_21 = V_2 / I_1 = R_p = 40.0 Ohmios.
Matriz Z:
[ [ 60, 40 ],
  [ 40, 60 ] ] Ohmios.
Como z_12 = z_21 = 40, la red es recíproca; como z_11 = z_22 = 60, es simétrica.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Convierta los parámetros Z de la red anterior a parámetros de transmisión ABCD y verifique la condición de reciprocidad A*D - B*C = 1.
Solución:
Fórmulas de conversión analítica:
Delta_z = z_11 * z_22 - z_12 * z_21 = (60 * 60) - (40 * 40) = 3600 - 1600 = 2000 Ohm^2.
A = z_11 / z_21 = 60 / 40 = 1.50 (adimensional).
B = Delta_z / z_21 = 2000 / 40 = 50.0 Ohmios.
C = 1 / z_21 = 1 / 40 = 0.025 Siemens.
D = z_22 / z_21 = 60 / 40 = 1.50 (adimensional).
Matriz de transmisión ABCD:
[ [ 1.50, 50.0 ],
  [ 0.025, 1.50 ] ].
Verificación del determinante:
A * D - B * C = (1.50 * 1.50) - (50.0 * 0.025) = 2.25 - 1.25 = 1.000.
La condición A*D - B*C = 1.0 se satisface de forma exacta, confirmando la validez analítica del modelo de dos puertos.""",
        "bloque_sugerido": "Laboratorio 50 min • Caracterización matricial de cuadripolos Z y ABCD",
        "slides": [
            {"numero": 1, "seccion": "CUADRIPOLOS", "titulo": "Parámetros Z e Y", "puntos": ["Representación modular de bloques circuitales de dos puertos.", "Cálculo de impedancias bajo condiciones de circuito abierto y cortocircuito."]},
            {"numero": 2, "seccion": "TRANSMISIÓN", "titulo": "Matriz ABCD y Conexión Cascada", "puntos": ["Parámetros ABCD para conexión en cascada de etapas por producto matricial.", "Condición estricta de reciprocidad det(ABCD) = A D - B C = 1."]}
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Análisis de Sensibilidad y Tolerancias en Circuitos DC",
        "objetivo": "Calcular la sensibilidad de funciones de transferencia ante variaciones paramétricas y evaluar peores casos (Worst-Case).",
        "concepto_clave_latex": r"S_x^y = \frac{\partial y}{\partial x}\frac{x}{y} = \frac{\partial \ln(y)}{\partial \ln(x)} \quad ; \quad \Delta y_{\text{max}} \approx \sum_{i=1}^n \left|\frac{\partial y}{\partial x_i}\right| \Delta x_i",
        "ejemplo": """CLASE MAGISTRAL: SENSIBILIDAD PARAMÉTRICA Y DISEÑO POR TOLERANCIAS
1. Definición de Sensibilidad Normalizada de Bode:
Mide la variación porcentual de una variable de salida y ante una variación porcentual del parámetro x:
S_x^y = (dy / dx) * (x / y).
Si S_R^V = 0.5, un incremento del 2% en el resistor R provocará un incremento del 1% en el voltaje V.
2. Análisis de Peor Caso (Worst-Case Analysis - WCA):
Determina los valores extremos absolutos (mínimo y máximo) de la salida cuando todos los componentes se desvían simultáneamente hacia sus límites de tolerancia más desfavorables.
3. Análisis de Monte Carlo:
Simulación estadística donde los valores de los componentes se seleccionan aleatoriamente según distribuciones gaussianas o uniformes, prediciendo la tasa de rendimiento industrial (yield).
4. Problema Resuelto 1 (Aplicación Directa):
Para un divisor de tensión resistivo no cargado v_o = V_s * R_2 / (R_1 + R_2), deduzca las expresiones analíticas de la sensibilidad de la salida respecto a R_1 y respecto a R_2.
Solución:
1. Sensibilidad respecto a R_2:
dv_o / dR_2 = V_s * [ (1 * (R_1 + R_2) - R_2 * 1) / (R_1 + R_2)^2 ] = V_s * R_1 / (R_1 + R_2)^2.
S_R2^vo = (dv_o / dR_2) * (R_2 / v_o) = [ V_s * R_1 / (R_1 + R_2)^2 ] * [ R_2 / (V_s * R_2 / (R_1 + R_2)) ]
S_R2^vo = R_1 / (R_1 + R_2).
2. Sensibilidad respecto a R_1:
dv_o / dR_1 = - V_s * R_2 / (R_1 + R_2)^2.
S_R1^vo = (dv_o / dR_1) * (R_1 / v_o) = - [ V_s * R_2 / (R_1 + R_2)^2 ] * [ R_1 / (V_s * R_2 / (R_1 + R_2)) ]
S_R1^vo = - R_1 / (R_1 + R_2).
Propiedad notable: S_R2^vo + S_R1^vo = R_1 / (R_1 + R_2) - R_1 / (R_1 + R_2) = 0.
Si ambos resistores varían en el mismo porcentaje (ej. por coeficiente térmico idéntico), la tensión de salida permanece inalterada.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Un sensor de referencia de tensión entrega V_s = 10.0 V nominales (+-1%) y alimenta un divisor con R_1 = 1000 Ohm (+-5%) y R_2 = 1000 Ohm (+-5%). Calcule la tensión nominal de salida v_o y determine los límites extremos absolutos de tensión [v_o,min ; v_o,max] bajo el análisis de Peor Caso (Worst-Case).
Solución:
Tensión nominal: v_o = 10.0 * 1000 / (1000 + 1000) = 5.000 V.
Rangos de componentes:
V_s in [9.9 V ; 10.1 V] (+-1%).
R_1 in [950 Ohm ; 1050 Ohm] (+-5%).
R_2 in [950 Ohm ; 1050 Ohm] (+-5%).
Para obtener v_o,max:
Se requiere V_s máximo (10.1 V), R_2 máximo (1050 Ohm) y R_1 mínimo (950 Ohm):
v_o,max = 10.1 * [ 1050 / (950 + 1050) ] = 10.1 * [ 1050 / 2000 ] = 10.1 * 0.525 = 5.3025 V.
Para obtener v_o,min:
Se requiere V_s mínimo (9.9 V), R_2 mínimo (950 Ohm) y R_1 máximo (1050 Ohm):
v_o,min = 9.9 * [ 950 / (1050 + 950) ] = 9.9 * [ 950 / 2000 ] = 9.9 * 0.475 = 4.7025 V.
Rango de peor caso: [4.703 V ; 5.303 V].
Variación porcentual máxima en la salida: Delta% = (5.3025 - 5.0) / 5.0 = + 6.05 %.
El análisis de peor caso demuestra que tolerancias del 5% en resistores y 1% en fuente generan una desviación acumulada del 6% en la salida.""",
        "bloque_sugerido": "Laboratorio 50 min • Análisis de sensibilidad y simulación Monte Carlo",
        "slides": [
            {"numero": 1, "seccion": "SENSIBILIDAD", "titulo": "Sensibilidad Normalizada de Bode", "puntos": ["Definición S_x^y = (dy/dx) (x/y) para propagación de tolerancias.", "Compensación natural de deriva térmica en divisores simétricos."]},
            {"numero": 2, "seccion": "WORST-CASE", "titulo": "Análisis de Peor Caso y Monte Carlo", "puntos": ["Cálculo de extremos absolutos maximizando desviaciones simultáneas.", "Garantía de bancabilidad y robustez en electrónica de potencia."]}
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Circuitos Transitorios de Primer Orden con Conmutación Secuencial",
        "objetivo": "Resolver respuestas transitorias paso a paso ante múltiples eventos de conmutación en tiempos t_1, t_2 > 0.",
        "concepto_clave_latex": r"x(t) = x(\infty_k) + [x(t_k^+) - x(\infty_k)]e^{-(t - t_k)/\tau_k} \quad (t_k \le t < t_{k+1})",
        "ejemplo": """CLASE MAGISTRAL: CONMUTACIÓN SECUENCIAL Y CONDICIONES DE FRONTERA
1. Continuidad de Variables de Estado:
En circuitos transitorios con inductores y condensadores, las leyes físicas de conservación de energía impiden saltos discontinuos en:
- La tensión en bornes de un capacitor: v_C(t^+) = v_C(t^-) (requeriría corriente infinita).
- La corriente a través de un inductor: i_L(t^+) = i_L(t^-) (requeriría voltaje infinito).
2. Metodología de Intervalos Secuenciales:
Cuando ocurren múltiples aperturas o cierres de interruptores en instantes sucesivos (ej. t = 0 y t = t_1):
- Intervalo 1 (0 <= t < t_1): Se determina la condición inicial x(0^+), el valor asintótico x(inf_1) y la constante de tiempo tau_1 = R_th1 * C.
- En t = t_1: El valor alcanzado x(t_1^-) se convierte en la condición inicial x(t_1^+) para el siguiente intervalo.
- Intervalo 2 (t >= t_1): Se recalcula x(inf_2) y tau_2 = R_th2 * C para la nueva topología.
3. Problema Resuelto 1 (Aplicación Directa):
Un circuito RC tiene C = 10 uF. Para t < 0 el interruptor estuvo abierto y v_C(0) = 0 V. En t = 0 se cierra conectando el capacitor a una fuente V_1 = 100 V a través de R_1 = 10 kOhm (tau_1 = R_1 * C = 0.10 s). En t_1 = 0.20 s (dos constantes de tiempo después), el interruptor conmuta a una segunda posición conectando el capacitor a una fuente V_2 = 40 V a través de R_2 = 20 kOhm (tau_2 = 0.20 s). Calcule v_C(0.20 s) y v_C(0.40 s).
Solución:
1. Para 0 <= t < 0.20 s:
tau_1 = 10,000 * 10e-6 = 0.10 s. Valor final x(inf_1) = 100 V.
v_C(t) = 100 + [ 0 - 100 ] * exp(-t / 0.10) = 100 * [ 1 - exp(-10 t) ].
En t = 0.20 s:
v_C(0.20^-) = 100 * [ 1 - exp(-10 * 0.20) ] = 100 * [ 1 - exp(-2) ] = 100 * [ 1 - 0.13534 ] = 86.47 V.
Por continuidad: v_C(0.20^+) = 86.47 V.
2. Para t >= 0.20 s:
tau_2 = R_2 * C = 20,000 * 10e-6 = 0.20 s. Valor final x(inf_2) = 40 V.
Ecuación general con t_0 = 0.20 s:
v_C(t) = 40 + [ 86.47 - 40 ] * exp(-(t - 0.20) / 0.20)
v_C(t) = 40 + 46.47 * exp(-5 (t - 0.20)).
En t = 0.40 s (delta_t = 0.20 s, una constante de tiempo tau_2 después):
v_C(0.40) = 40 + 46.47 * exp(-5 * (0.20)) = 40 + 46.47 * exp(-1) = 40 + 46.47 * 0.36788 = 40 + 17.09 = 57.09 V.
El capacitor se cargó hasta 86.5 V y luego se descargó parcialmente hasta 57.1 V.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un solenoide de relé de protección inductivo con L = 0.5 H y resistencia interna R = 25 Ohm (tau = L/R = 0.02 s) conduce una corriente estacionaria I_0 = 2.0 A desde una fuente DC de 50 V. En t = 0 se desconecta súbitamente la fuente mediante un interruptor que abre el circuito, dejando un resistor de descarga flyback R_d = 225 Ohm en paralelo con la bobina. Calcule el voltaje pico instantáneo en bornes del interruptor al abrirse y el tiempo que tarda la corriente en caer al 1% de su valor inicial.
Solución:
1. Condición inicial: i_L(0^-) = 2.0 A.
Por continuidad: i_L(0^+) = 2.0 A forzada a circular a través de R + R_d.
Resistencia total del lazo de descarga: R_total = R + R_d = 25 + 225 = 250 Ohm.
Voltaje inducido en el resistor de descarga en t = 0^+:
v_Rd(0^+) = i_L(0^+) * R_d = 2.0 A * 225 Ohm = 450.0 V.
Tensión total sobre los contactos del interruptor al abrirse:
V_contacto = V_fuente + v_Rd = 50 V + 450 V = 500.0 V.
(Demuestra cómo la desconexión inductiva induce sobretensiones de 10x que destruyen contactos si no se coloca diodo flyback).
2. Tiempo de descarga al 1%:
Nueva constante de tiempo: tau_desc = L / R_total = 0.5 H / 250 Ohm = 0.002 s = 2.0 ms.
Corriente: i_L(t) = 2.0 * exp(-t / 0.002) = 0.01 * 2.0 ==> exp(-t / 0.002) = 0.01.
- t / 0.002 = ln(0.01) = -4.605.
t = 0.002 * 4.605 = 0.00921 s = 9.21 milisegundos.""",
        "bloque_sugerido": "Laboratorio 50 min • Simulación de conmutación múltiple y diodos flyback",
        "slides": [
            {"numero": 1, "seccion": "CONTINUIDAD", "titulo": "Variables de Estado y Condiciones de Frontera", "puntos": ["Continuidad de tensión v_C(0^+) = v_C(0^-) y corriente i_L(0^+) = i_L(0^-).", "Encadenamiento de intervalos temporales secuenciales [t_k, t_{k+1}]."]},
            {"numero": 2, "seccion": "SOBRETENSIÓN", "titulo": "Transitorios Inductivos de Apertura", "puntos": ["Sobretensiones masivas v_L = L di/dt al interrumpir corriente continua.", "Diseño de redes de protección snubber y diodos de libre circulación (Flyback)."]}
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Circuitos Transitorios de Segundo Orden RLC Serie",
        "objetivo": "Formular la ecuación diferencial de segundo orden en mallas RLC serie y resolver los tres regímenes de amortiguamiento.",
        "concepto_clave_latex": r"\frac{d^2 v_C}{dt^2} + 2\alpha\frac{dv_C}{dt} + \omega_0^2 v_C = \omega_0^2 V_s \quad ; \quad \alpha = \frac{R}{2L} \quad ; \quad \omega_0 = \frac{1}{\sqrt{LC}}",
        "ejemplo": """CLASE MAGISTRAL: DINÁMICA DE CIRCUITOS DE SEGUNDO ORDEN RLC SERIE
1. Deducción de la Ecuación Diferencial:
En una malla RLC serie conectada a una fuente V_s:
v_R + v_L + v_C = V_s.
Como i = C * dv_C/dt: v_R = R C * dv_C/dt, y v_L = L * di/dt = L C * d^2v_C/dt^2.
Sustituyendo: L C * d^2v_C/dt^2 + R C * dv_C/dt + v_C = V_s.
Dividiendo entre LC:
d^2v_C/dt^2 + (R/L) * dv_C/dt + (1 / LC) * v_C = V_s / LC.
Definiendo:
- Coeficiente de amortiguamiento de Neper: alpha = R / (2L) [Np/s].
- Frecuencia de resonancia no amortiguada: omega_0 = 1 / sqrt(LC) [rad/s].
Ecuación característica: s^2 + 2 alpha s + omega_0^2 = 0, con raíces s_1,2 = -alpha +- sqrt(alpha^2 - omega_0^2).
2. Los Tres Regímenes de Respuesta:
- Sobreamortiguado (alpha > omega_0): Dos raíces reales negativas s_1 != s_2.
- Críticamente amortiguado (alpha = omega_0): Raíz real doble s_1 = s_2 = -alpha. Transición más rápida sin sobreimpulso.
- Subamortiguado (alpha < omega_0): Raíces complejas conjugadas s_1,2 = -alpha +- j omega_d, con omega_d = sqrt(omega_0^2 - alpha^2). Oscilatorio amortiguado con sobreelongación (overshoot).
3. Problema Resuelto 1 (Aplicación Directa):
Un circuito RLC serie desenergizado tiene R = 40 Ohm, L = 0.10 H y C = 10 uF. Se conecta en t = 0 a una fuente constante V_s = 50 V.
a) Determine alpha y omega_0, y clasifique el tipo de respuesta transitoria.
b) Calcule la frecuencia oscilatoria amortiguada omega_d y el periodo de oscilación T_d.
Solución:
a) alpha = R / (2L) = 40 / (2 * 0.10) = 40 / 0.20 = 200.0 Np/s.
omega_0 = 1 / sqrt(L * C) = 1 / sqrt(0.10 * 10e-6) = 1 / sqrt(10^-6) = 1 / 10^-3 = 1000.0 rad/s.
Como alpha = 200.0 < omega_0 = 1000.0, la respuesta es SUBAMORTIGUADA (oscilatoria).
b) Frecuencia amortiguada:
omega_d = sqrt(omega_0^2 - alpha^2) = sqrt( (1000)^2 - (200)^2 ) = sqrt( 1,000,000 - 40,000 ) = sqrt(960,000) = 979.80 rad/s.
Periodo de oscilación:
T_d = 2 pi / omega_d = (2 * 3.1416) / 979.80 = 6.413 * 10^-3 s = 6.41 milisegundos.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Obtenga la solución analítica completa para v_C(t) del circuito anterior sujeta a condiciones iniciales de reposo v_C(0^+) = 0 V e i_L(0^+) = 0 A, y determine el primer pico máximo de sobretensión (Overshoot) sobre el capacitor.
Solución:
Forma de la solución subamortiguada al escalón:
v_C(t) = V_s + exp(-alpha t) * [ A_1 cos(omega_d t) + A_2 sin(omega_d t) ].
En t = 0: v_C(0^+) = 0 = 50 + A_1 ==> A_1 = -50.0 V.
Derivada: dv_C/dt = i_C / C. En t = 0^+: dv_C/dt(0^+) = i_L(0^+) / C = 0 / C = 0.
Derivando analíticamente:
dv_C/dt(0) = -alpha A_1 + omega_d A_2 = 0 ==> A_2 = (alpha / omega_d) * A_1.
A_2 = (200 / 979.80) * (-50) = 0.20412 * (-50) = -10.206 V.
Ecuación completa:
v_C(t) = 50 - exp(-200 t) * [ 50 cos(979.8 t) + 10.21 sin(979.8 t) ] V.
El primer pico de sobreimpulso ocurre en t_pico = pi / omega_d:
t_pico = 3.1416 / 979.80 = 3.206 * 10^-3 s (3.21 ms).
Evaluando en t_pico (donde cos(pi) = -1 y sin(pi) = 0):
v_C(t_pico) = 50 - exp(-200 * 0.003206) * [ 50 * (-1) + 0 ]
v_C(t_pico) = 50 + 50 * exp(-0.6412) = 50 + 50 * (0.52666) = 50 + 26.33 = 76.33 V.
Sobretensión porcentual: Overshoot = (76.33 - 50) / 50 = +52.66%.
El capacitor soporta un pico transitorio de 76.3 V (52.7% superior a la tensión de la fuente), justificando el dimensionamiento dieléctrico de protecciones.""",
        "bloque_sugerido": "Laboratorio 50 min • Respuesta transitoria RLC serie y cálculo de sobreimpulso",
        "slides": [
            {"numero": 1, "seccion": "RLC SERIE", "titulo": "Ecuación de Segundo Orden", "puntos": ["Parámetros alpha = R / (2L) y omega_0 = 1 / sqrt(LC).", "Raíces características s^2 + 2 alpha s + omega_0^2 = 0."]},
            {"numero": 2, "seccion": "SOBREIMPULSO", "titulo": "Respuesta Subamortiguada y Pico", "puntos": ["Frecuencia oscilatoria omega_d = sqrt(omega_0^2 - alpha^2).", "Pico de sobretensión transitoria t_pico = pi / omega_d superior a la fuente."]}
        ]
    }
]

topics_21_to_30 = [
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Circuitos Transitorios de Segundo Orden RLC Paralelo",
        "objetivo": "Formular la dualidad en redes RLC paralelo y resolver respuestas naturales y al escalón de corriente.",
        "concepto_clave_latex": r"\frac{d^2 i_L}{dt^2} + 2\alpha\frac{di_L}{dt} + \omega_0^2 i_L = \omega_0^2 I_s \quad ; \quad \alpha = \frac{1}{2RC} \quad ; \quad \omega_0 = \frac{1}{\sqrt{LC}}",
        "ejemplo": """CLASE MAGISTRAL: RLC PARALELO Y DUALIDAD DE SEGUNDO ORDEN
1. Formulación Dual del RLC Paralelo:
En un nodo con un resistor R, un inductor L y un capacitor C conectados en paralelo alimentados por una fuente de corriente I_s:
i_R + i_L + i_C = I_s.
Como v = L * di_L/dt: i_R = v / R = (L / R) * di_L/dt, e i_C = C * dv/dt = L C * d^2i_L/dt^2.
Dividiendo entre LC:
d^2i_L/dt^2 + (1 / (RC)) * di_L/dt + (1 / LC) * i_L = I_s / LC.
2. Comparación de Amortiguamiento Serie vs Paralelo:
- RLC Serie: alpha_serie = R / (2L). Reducir R reduce alpha (hace el circuito más oscilatorio).
- RLC Paralelo: alpha_paralelo = 1 / (2RC). ¡Aumentar R reduce alpha! (R grande hace el circuito más oscilatorio porque drena menos corriente de disipación).
3. Problema Resuelto 1 (Aplicación Directa):
Un circuito RLC paralelo tiene L = 50 mH y C = 2.0 uF. Determine el valor de la resistencia R que produce exactamente amortiguamiento crítico (alpha = omega_0).
Solución:
omega_0 = 1 / sqrt(L * C) = 1 / sqrt(0.050 * 2.0e-6) = 1 / sqrt(10^-7) = 1 / (3.1623 * 10^-4) = 3162.28 rad/s.
Condición crítica: alpha = omega_0 ==> 1 / (2 * R_crit * C) = omega_0.
Despejando R_crit:
R_crit = 1 / (2 * omega_0 * C)
R_crit = 1 / [ 2 * (3162.28) * (2.0 * 10^-6 F) ] = 1 / [ 0.012649 ] = 79.06 Ohmios.
Si R > 79.1 Ohm, el circuito será subamortiguado; si R < 79.1 Ohm, será sobreamortiguado.
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un circuito RLC paralelo subamortiguado con R = 500 Ohm, L = 20 mH y C = 5 uF excitado por un pulso de corriente de corta duración, calcule el factor de calidad Q del circuito y compárelo con el de su dual serie.
Solución:
omega_0 = 1 / sqrt(L * C) = 1 / sqrt(0.020 * 5.0e-6) = 1 / sqrt(10^-7) = 3162.28 rad/s.
alpha_paralelo = 1 / (2 * R * C) = 1 / (2 * 500 * 5.0e-6) = 1 / (0.005) = 200.0 Np/s.
Factor de calidad para RLC paralelo:
Q_paralelo = omega_0 / (2 * alpha) = R * sqrt(C / L) = omega_0 * R * C.
Q_paralelo = 3162.28 / (2 * 200) = 3162.28 / 400 = 7.906.
Para el circuito serie dual con los mismos valores R, L, C:
Q_serie = (1 / R) * sqrt(L / C) = omega_0 * L / R = (3162.28 * 0.020) / 500 = 63.245 / 500 = 0.1265.
Nótese la inversión total: una resistencia de 500 Ohm produce un circuito altamente oscilatorio en paralelo (Q = 7.91), pero fuertemente sobreamortiguado en serie (Q = 0.126).""",
        "bloque_sugerido": "Pomodoro 50/10 • RLC paralelo y resistencia crítica",
        "slides": [
            {"numero": 1, "seccion": "PARALELO", "titulo": "Dinámica RLC Paralelo", "puntos": ["Ecuación diferencial dual en función de la corriente del inductor i_L.", "Amortiguamiento alpha = 1 / (2RC): resistencia grande favorece oscilaciones."]},
            {"numero": 2, "seccion": "FACTOR Q", "titulo": "Factor de Calidad Paralelo", "puntos": ["Fórmula Q = R sqrt(C/L) inversa a la configuración serie.", "Aplicación en filtros sintonizados de armónicos y tanques resonantes."]}
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Funciones Singulares en Circuitos: Escalón Unitario, Impulso y Rampa",
        "objetivo": "Modelar conmutaciones instantáneas y descargas transitorias mediante funciones singulares generalizadas.",
        "concepto_clave_latex": r"u(t) = \begin{cases} 0, & t < 0 \\ 1, & t > 0 \end{cases} \quad ; \quad \delta(t) = \frac{du(t)}{dt} \quad ; \quad r(t) = \int_{-\infty}^t u(\tau)\,d\tau = t \cdot u(t)",
        "ejemplo": """CLASE MAGISTRAL: FUNCIONES SINGULARES Y DISTRIBUCIONES
1. Jerarquía de Funciones Singulares:
Permiten describir matemáticamente perturbaciones discontinuas sin recurrir a análisis por partes engorrosos:
- Función Escalón Unitario u(t) (Heaviside): Modela el encendido de un interruptor en t = 0.
- Función Impulso de Dirac delta(t): Derivada distribucional del escalón. Duración infinitesimal con área unitaria int_{-inf}^{+inf} delta(t) dt = 1. Modela descargas de rayos o arcos eléctricos ultrarrápidos.
- Función Rampa r(t) = t * u(t): Integral del escalón. Modela arranque suave de motores e inversores.
2. Propiedad de Muestreo (Sifting Property) de la Delta de Dirac:
int_{-inf}^{+inf} f(t) * delta(t - t_0) dt = f(t_0).
3. Problema Resuelto 1 (Aplicación Directa):
Exprese analíticamente como una única combinación lineal de funciones escalón un pulso rectangular de tensión v(t) de amplitud V_0 = 24 V que se enciende en t_1 = 2.0 ms y se apaga en t_2 = 7.0 ms.
Solución:
El encendido en t = 2.0 ms se modela con + V_0 * u(t - 2.0 ms).
El apagado en t = 7.0 ms se modela sumando un escalón negativo - V_0 * u(t - 7.0 ms).
Expresión analítica:
v(t) = 24.0 * [ u(t - 2.0 * 10^-3) - u(t - 7.0 * 10^-3) ] Voltios.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un rayo deposita una corriente impulsiva modelada como i(t) = Q_0 * delta(t) con carga neta Q_0 = 5.0 Coulombs sobre un banco de condensadores desenergizado de capacidad C = 250 uF en paralelo con una resistencia R = 200 Ohm. Determine el voltaje en el capacitor inmediatamente después del impacto v_C(0^+) y la expresión temporal v_C(t) para todo t > 0.
Solución:
1. Relación constitutiva del capacitor: i_C(t) = C * dv_C/dt.
Integrando a través del instante del impacto desde t = 0^- hasta t = 0^+:
v_C(0^+) - v_C(0^-) = (1 / C) * int_{0^-}^{0^+} i(t) dt = (1 / C) * int_{0^-}^{0^+} [ Q_0 * delta(t) ] dt = Q_0 / C.
Como v_C(0^-) = 0:
v_C(0^+) = Q_0 / C = 5.0 C / (250 * 10^-6 F) = 20,000 V = 20.0 kV.
El impulso de corriente salta instantáneamente el voltaje del capacitor a 20 kV.
2. Respuesta para t > 0:
Con el capacitor cargado a 20 kV, se descarga a través de R:
tau = R * C = 200 Ohm * (250 * 10^-6 F) = 0.050 s = 50.0 ms.
v_C(t) = 20,000 * exp(-t / 0.050) * u(t) = 20,000 * exp(-20 t) * u(t) Voltios.
El circuito absorbió el pulso impulsivo y lo disipa exponencialmente en 50 milisegundos.""",
        "bloque_sugerido": "Laboratorio 50 min • Funciones singulares y respuesta a impulsos",
        "slides": [
            {"numero": 1, "seccion": "SINGULARES", "titulo": "Escalón, Impulso y Rampa", "puntos": ["Función de Heaviside u(t) y delta de Dirac delta(t) = du/dt.", "Propiedad de tamizado int f(t) delta(t - t_0) dt = f(t_0)."]},
            {"numero": 2, "seccion": "IMPULSO", "titulo": "Modelado de Sobretensiones por Rayo", "puntos": ["Inyección de carga instantánea v_C(0^+) = Q_0 / C.", "Disipación transitoria exponencial en descargadores de sobretensión (DPS)."]}
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Respuesta al Impulso y Convolución Temporal en Redes Lineales",
        "objetivo": "Calcular la salida de una red ante cualquier excitación arbitraria mediante la integral de convolución temporal.",
        "concepto_clave_latex": r"y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau)\,d\tau \quad ; \quad h(t) = \left.\frac{ds(t)}{dt}\right|_{s(t)=\text{resp. escalón}}",
        "ejemplo": """CLASE MAGISTRAL: CONVOLUCIÓN TEMPORAL Y CARACTERIZACIÓN LTI
1. La Respuesta al Impulso h(t) como Huella Dactilar del Circuito:
En un sistema lineal e invariante en el tiempo (LTI), la respuesta al impulso h(t) caracteriza por completo la dinámica del circuito. Por el principio de superposición e invariancia, cualquier señal de entrada continua x(t) puede descomponerse en una suma infinita de impulsos ponderados.
2. La Integral de Convolución:
y(t) = int_{-inf}^{+inf} x(tau) * h(t - tau) dtau.
Propiedad operativa fundamental: La respuesta al impulso es la derivada temporal exacta de la respuesta al escalón unitario s(t): h(t) = ds(t)/dt.
3. Problema Resuelto 1 (Aplicación Directa):
Un circuito RC pasabajas tiene una respuesta al escalón s(t) = (1 - exp(-t / tau)) * u(t) con tau = 0.01 s. Determine su respuesta al impulso h(t).
Solución:
h(t) = d/dt [ s(t) ] = d/dt [ (1 - exp(-100 t)) * u(t) ].
Aplicando la regla del producto:
h(t) = [ 0 - (-100 exp(-100 t)) ] * u(t) + [ 1 - exp(-100 t) ] * delta(t).
Evaluando el segundo término con la propiedad de muestreo en t = 0: [ 1 - exp(0) ] * delta(t) = [ 1 - 1 ] * delta(t) = 0.
Por lo tanto:
h(t) = 100.0 * exp(-100 t) * u(t) [s^-1].
4. Problema Resuelto 2 (Nivel Examen Parcial):
Se aplica una rampa truncada de tensión x(t) = 10 * t para 0 <= t <= 0.02 s (y cero para t > 0.02 s) a un filtro con respuesta al impulso h(t) = exp(-50 t) * u(t). Calcule la tensión de salida y(t) en el instante t = 0.01 s mediante la integral de convolución.
Solución:
Para 0 <= t <= 0.02 s, la entrada es x(tau) = 10 tau.
Por la integral de convolución:
y(t) = int_0^t x(tau) * h(t - tau) dtau = int_0^t (10 tau) * exp(-50 (t - tau)) dtau
y(t) = 10 * exp(-50 t) * int_0^t tau * exp(50 tau) dtau.
Integrando por partes: int u dv con u = tau, dv = exp(50 tau) dtau:
int tau exp(50 tau) dtau = [ tau * exp(50 tau) / 50 ] - int [ exp(50 tau) / 50 ] dtau = (tau / 50) exp(50 tau) - (1 / 2500) exp(50 tau).
Evaluando entre 0 y t:
[ (t / 50) exp(50 t) - (1 / 2500) exp(50 t) ] - [ 0 - 1 / 2500 ] = exp(50 t) * [ t / 50 - 1 / 2500 ] + 1 / 2500.
Multiplicando por 10 * exp(-50 t):
y(t) = 10 * [ t / 50 - 1 / 2500 ] + (10 / 2500) * exp(-50 t)
y(t) = 0.20 * t - 0.004 + 0.004 * exp(-50 t).
Evaluando en t = 0.01 s:
y(0.01) = 0.20 * (0.01) - 0.004 + 0.004 * exp(-50 * 0.01)
y(0.01) = 0.002 - 0.004 + 0.004 * exp(-0.5) = -0.002 + 0.004 * (0.60653) = -0.002 + 0.002426 = 0.000426 V = 0.426 mV.
La convolución entrega la respuesta exacta en el dominio del tiempo continuo.""",
        "bloque_sugerido": "Laboratorio 50 min • Integral de convolución temporal en redes LTI",
        "slides": [
            {"numero": 1, "seccion": "CONVOLUCIÓN", "titulo": "Integral de Superposición LTI", "puntos": ["Respuesta al impulso h(t) como caracterización completa del sistema.", "Operación y(t) = int x(tau) h(t - tau) dtau en el dominio temporal."]},
            {"numero": 2, "seccion": "CÁLCULO", "titulo": "Relación Escalón-Impulso", "puntos": ["Derivada de la respuesta al escalón h(t) = ds(t)/dt.", "Solución analítica de redes ante entradas arbitrarias continuas."]}
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Régimen Permanente Sinusoidal y Dominio Fasorial",
        "objetivo": "Transformar señales sinusoidales al dominio fasorial mediante la identidad de Euler y simplificar derivadas a productos jw.",
        "concepto_clave_latex": r"v(t) = V_m \cos(\omega t + \phi) \longleftrightarrow \mathbf{V} = V_m e^{j\phi} = V_m \angle\phi \quad ; \quad \frac{d}{dt} \longleftrightarrow j\omega",
        "ejemplo": """CLASE MAGISTRAL: EL DOMINIO FASORIAL DE CHARLES PROTEUS STEINMETZ
1. La Revolución Fasorial en Ingeniería Eléctrica:
Resolver circuitos AC con bobinas y condensadores en el dominio del tiempo requiere resolver sistemas de ecuaciones diferenciales integro-diferenciales acopladas. Steinmetz introdujo el concepto de Fasor: una transformación lineal biyectiva que convierte ecuaciones diferenciales en ecuaciones algebraicas complejas simples.
2. Identidad de Euler y Proyección en la Recta Real:
e^{j theta} = cos(theta) + j sin(theta).
v(t) = V_m * cos(omega t + phi) = Re{ V_m * exp(j phi) * exp(j omega t) } = Re{ V_fasor * exp(j omega t) }.
Al derivar en el tiempo: d/dt [ Re{ V * exp(j omega t) } ] = Re{ j omega * V * exp(j omega t) }.
La derivada temporal se transforma en una multiplicación algebraica por j omega.
3. Problema Resuelto 1 (Aplicación Directa):
Transforme al dominio fasorial las siguientes dos señales de red:
a) v(t) = 170.0 * cos(377 t - 30°) V.
b) i(t) = - 12.0 * sin(377 t + 45°) A.
Solución:
a) v(t) ya está en función coseno con amplitud positiva:
Fasor de voltaje pico: V = 170.0 angle(-30°) V.
Fasor eficaz (RMS = V_m / sqrt(2) = 170 / 1.4142 = 120.2 V):
V_rms = 120.0 angle(-30°) V.
b) i(t) está en seno negativo. Convertimos a coseno aplicando identidades trigonométricas:
- sin(alpha) = cos(alpha + 90°).
i(t) = 12.0 * cos(377 t + 45° + 90°) = 12.0 * cos(377 t + 135°) A.
Fasor pico: I = 12.0 angle(135°) A.
Fasor RMS: I_rms = (12.0 / sqrt(2)) angle(135°) = 8.485 angle(135°) A.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Dada la ecuación diferencial de un circuito RL alimentado por una fuente AC: L * di/dt + R * i = V_m * cos(omega t), demuestre analíticamente mediante fasores que la amplitud de corriente en régimen permanente es I_m = V_m / sqrt(R^2 + (omega L)^2) con un ángulo de atraso phi = - arctan(omega L / R).
Solución:
Transformando la ecuación diferencial al dominio fasorial:
L * (j omega * I) + R * I = V, donde V = V_m angle(0°).
Factorizando el fasor de corriente I:
(R + j omega L) * I = V.
Definiendo la impedancia compleja Z = R + j omega L:
I = V / Z = (V_m angle(0°)) / ( |Z| angle(theta_z) ).
Magnitud de Z: |Z| = sqrt( R^2 + (omega L)^2 ).
Ángulo de Z: theta_z = arctan(omega L / R).
Fasor de corriente resultante:
I = [ V_m / sqrt(R^2 + (omega L)^2) ] angle( - arctan(omega L / R) ).
Regresando al dominio temporal:
i(t) = I_m * cos(omega t - theta_z) = [ V_m / sqrt(R^2 + (omega L)^2) ] * cos(omega t - arctan(omega L / R)).
La corriente en régimen permanente se obtuvo mediante simple álgebra compleja sin integrar ninguna ecuación diferencial. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Transformación fasorial y álgebra de números complejos",
        "slides": [
            {"numero": 1, "seccion": "FASORES", "titulo": "Transformación de Steinmetz", "puntos": ["Identidad de Euler y mapeo v(t) = V_m cos(omega t + phi) <-> V_m angle(phi).", "Sustitución de la derivada d/dt por el operador algebraico j omega."]},
            {"numero": 2, "seccion": "ESTADO ESTABLE", "titulo": "Solución Algebraica en AC", "puntos": ["Conversión de ecuaciones diferenciales en sistemas algebraicos Z I = V.", "Cálculo de desfasajes inductivos y capacitivos en régimen permanente."]}
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Impedancia y Admitancia Compleja de R, L y C",
        "objetivo": "Calcular reactancias inductivas y capacitivas y modelar impedancias equivalentes serie-paralelo en AC.",
        "concepto_clave_latex": r"\mathbf{Z}_R = R \quad ; \quad \mathbf{Z}_L = j\omega L = \omega L\angle 90^\circ \quad ; \quad \mathbf{Z}_C = \frac{1}{j\omega C} = -j\frac{1}{\omega C} = \frac{1}{\omega C}\angle -90^\circ",
        "ejemplo": """CLASE MAGISTRAL: IMPEDANCIA Y ADMITANCIA COMPLEJA
1. Ley de Ohm Fasorial Universal:
V = Z * I, donde la Impedancia Z = R + jX [Ohmios] es un número complejo que relaciona los fasores de tensión y corriente:
- Parte Real R: Resistencia óhmica (disipa energía en calor).
- Parte Imaginaria X: Reactancia (almacena energía reactiva reversible en campos electromagnéticos).
  * Reactancia Inductiva: X_L = omega * L (crece linealmente con la frecuencia). En un inductor puro, la tensión adelanta a la corriente en 90° (ELI).
  * Reactancia Capacitiva: X_C = -1 / (omega * C) (decae inversamente con la frecuencia). En un capacitor puro, la corriente adelanta a la tensión en 90° (ICE).
2. Admitancia Compleja (Y = 1 / Z = G + jB):
- G: Conductancia en Siemens.
- B: Susceptancia en Siemens (B_C = omega C > 0; B_L = -1 / (omega L) < 0).
3. Problema Resuelto 1 (Aplicación Directa):
Calcule la impedancia de un inductor L = 50 mH y de un condensador C = 100 uF para una red eléctrica colombiana a frecuencia industrial f = 60 Hz (omega = 2 pi * 60 = 376.99 rad/s).
Solución:
1. Inductor:
X_L = omega * L = (376.99 rad/s) * (0.050 H) = 18.85 Ohmios.
Z_L = j 18.85 Ohm = 18.85 angle(90°) Ohm.
2. Capacitor:
X_C = - 1 / (omega * C) = - 1 / [ (376.99) * (100 * 10^-6) ] = - 1 / 0.037699 = - 26.53 Ohmios.
Z_C = -j 26.53 Ohm = 26.53 angle(-90°) Ohm.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un alimentador AC de 120 V RMS a 60 Hz alimenta una carga conectada en paralelo formada por una rama resistiva R = 30 Ohm y una rama inductiva con L = 106.1 mH (X_L = 40 Ohm). Calcule: a) La admitancia total Y_total; b) La impedancia equivalente Z_eq; c) La corriente total RMS I_total absorbida de la red y el ángulo de desfase respecto a la tensión.
Solución:
a) Admitancias de rama:
Y_R = 1 / R = 1 / 30 = 0.03333 S.
Y_L = 1 / (j X_L) = -j / 40 = -j 0.02500 S.
Admitancia total en paralelo:
Y_total = Y_R + Y_L = (0.03333 - j 0.02500) Siemens.
En forma polar:
|Y_total| = sqrt( (0.03333)^2 + (-0.025)^2 ) = sqrt( 0.001111 + 0.000625 ) = sqrt( 0.001736 ) = 0.04167 S.
theta_Y = arctan(-0.025 / 0.03333) = arctan(-0.75) = -36.87°.
Y_total = 0.04167 angle(-36.87°) Siemens.
b) Impedancia equivalente:
Z_eq = 1 / Y_total = (1 / 0.04167) angle(+36.87°) = 24.0 angle(+36.87°) Ohm.
En forma rectangular:
Z_eq = 24.0 * cos(36.87°) + j 24.0 * sin(36.87°) = (19.20 + j 14.40) Ohmios.
c) Corriente total RMS (asumiendo V = 120 angle(0°) V):
I_total = V * Y_total = (120 angle(0°)) * (0.04167 angle(-36.87°)) = 5.0 angle(-36.87°) A.
La corriente total es de 5.0 A RMS y se encuentra en atraso de 36.87° respecto a la tensión (carga inductiva).""",
        "bloque_sugerido": "Laboratorio 50 min • Impedancia y admitancia en circuitos RLC a 60 Hz",
        "slides": [
            {"numero": 1, "seccion": "IMPEDANCIA", "titulo": "Reactancia Inductiva y Capacitiva", "puntos": ["Z_L = j omega L: la tensión adelanta 90° a la corriente.", "Z_C = -j / (omega C): la corriente adelanta 90° a la tensión."]},
            {"numero": 2, "seccion": "ADMITANCIA", "titulo": "Asociación Serie y Paralelo en AC", "puntos": ["Suma de impedancias en serie Z_total = Z_1 + Z_2.", "Suma de admitancias en paralelo Y_total = Y_1 + Y_2 para análisis directo."]}
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Teoremas de Thévenin y Norton en el Dominio Fasorial AC",
        "objetivo": "Reducir redes de corriente alterna a sus circuitos equivalentes Thévenin y Norton complejos.",
        "concepto_clave_latex": r"\mathbf{V}_{\text{th}} = \mathbf{V}_{\text{oc}} \quad ; \quad \mathbf{Z}_{\text{th}} = \frac{\mathbf{V}_{\text{oc}}}{\mathbf{I}_{\text{sc}}} \quad ; \quad \mathbf{I}_N = \frac{\mathbf{V}_{\text{th}}}{\mathbf{Z}_{\text{th}}}",
        "ejemplo": """CLASE MAGISTRAL: EQUIVALENTES THÉVENIN Y NORTON EN CORRIENTE ALTERNA
1. Extensión de Thévenin al Dominio Complejo:
Cualquier red lineal AC vista desde dos terminales a-b puede reemplazarse por una única fuente de tensión fasorial V_th en serie con una impedancia compleja Z_th = R_th + j X_th.
2. Procedimiento de Cálculo Fasorial:
- V_th: Tensión fasorial de circuito abierto entre a y b.
- I_sc: Corriente fasorial de cortocircuito entre a y b.
- Z_th = V_th / I_sc (o apagando fuentes independientes si no hay dependientes).
3. Problema Resuelto 1 (Aplicación Directa):
Una red AC alimentada por V_s = 100 angle(0°) V a 60 Hz tiene un resistor R = 10 Ohm en serie con un capacitor Z_C = -j 10 Ohm. Entre los terminales a-b de salida está conectado un inductor Z_L = j 20 Ohm. Encuentre el equivalente Thévenin visto desde los terminales a-b.
Solución:
1. Voltaje de circuito abierto V_th (divisor de tensión entre R-Z_C y Z_L):
V_th = V_s * [ Z_L / (R + Z_C + Z_L) ]
Z_total = 10 - j 10 + j 20 = (10 + j 10) Ohm = 14.142 angle(45°) Ohm.
V_th = (100 angle(0°)) * [ (j 20) / (10 + j 10) ]
Numerador: (100 angle(0°)) * (20 angle(90°)) = 2000 angle(90°).
V_th = (2000 angle(90°)) / (14.142 angle(45°)) = 141.42 angle(45°) V.
En rectangular: V_th = (100 + j 100) V.
2. Impedancia de Thévenin Z_th (apagando V_s, paralelo entre (R + Z_C) y Z_L):
Z_th = (R + Z_C) // Z_L = [ (10 - j 10) * (j 20) ] / [ (10 - j 10) + j 20 ]
Numerador: (10 - j 10) * (j 20) = j 200 - j^2 200 = 200 + j 200 = 282.84 angle(45°).
Denominador: 10 + j 10 = 14.142 angle(45°).
Z_th = (282.84 angle(45°)) / (14.142 angle(45°)) = 20.0 angle(0°) Ohm = 20.0 Ohmios puramente resistivos.
Equivalente: Fuente V_th = 141.42 angle(45°) V en serie con Z_th = 20 Ohm.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente el Teorema de Máxima Transferencia de Potencia en AC: la carga compleja Z_L = R_L + j X_L que absorbe la máxima potencia activa media de un circuito Thévenin Z_th = R_th + j X_th debe ser exactamente su conjugado complejo: Z_L = Z_th^* = R_th - j X_th.
Solución:
La corriente en la carga es:
I = V_th / (Z_th + Z_L) = V_th / [ (R_th + R_L) + j(X_th + X_L) ].
Magnitud de corriente al cuadrado:
|I|^2 = |V_th|^2 / [ (R_th + R_L)^2 + (X_th + X_L)^2 ].
Potencia activa media disipada en la carga:
P_L = |I|^2 * R_L = [ |V_th|^2 * R_L ] / [ (R_th + R_L)^2 + (X_th + X_L)^2 ].
1. Maximizando respecto a la reactancia X_L:
Para cualquier valor de R_L, el denominador se minimiza cuando el término cuadrático es nulo:
(X_th + X_L)^2 = 0 ==> X_L = - X_th. (La reactancia de la carga cancela por resonancia la reactancia interna).
2. Maximizando respecto a R_L con X_L = -X_th:
P_L = |V_th|^2 * R_L / (R_th + R_L)^2.
Derivando dP_L / dR_L e igualando a cero:
dP_L / dR_L = |V_th|^2 * [ (R_th + R_L)^2 - R_L * 2(R_th + R_L) ] / (R_th + R_L)^4 = 0
(R_th + R_L) - 2 R_L = 0 ==> R_L = R_th.
Combinando ambas condiciones:
Z_L = R_L + j X_L = R_th - j X_th = Z_th^*.
La potencia máxima activa transferible es:
P_max = |V_th|^2 / (4 R_th). Q.E.D.""",
        "bloque_sugerido": "Laboratorio 50 min • Teorema de Thévenin fasorial y conjugado complejo",
        "slides": [
            {"numero": 1, "seccion": "THÉVENIN AC", "titulo": "Equivalente Thévenin Fasorial", "puntos": ["Reducción de redes complejas a V_th angle(theta) y Z_th = R_th + j X_th.", "Cálculo mediante cociente de tensión en vacío y corriente de cortocircuito."]},
            {"numero": 2, "seccion": "MÁXIMA POTENCIA", "titulo": "Adaptación por Complejo Conjugado", "puntos": ["Condición óptima de transferencia activa Z_L = Z_th^* = R_th - j X_th.", "Cancelación de reactancias por resonancia y adaptación de resistencias."]}
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Potencia Instantánea y Potencia Media en Régimen Permanente AC",
        "objetivo": "Descomponer la potencia instantánea p(t) en término constante activo y término fluctuante a 2w.",
        "concepto_clave_latex": r"p(t) = P [1 + \cos(2\omega t)] + Q \sin(2\omega t) \quad ; \quad P = V_{\text{rms}} I_{\text{rms}} \cos(\theta_v - \theta_i)",
        "ejemplo": """CLASE MAGISTRAL: DINÁMICA DE LA POTENCIA INSTANTÁNEA EN AC
1. Deducción Trigonométrica de p(t):
Sean v(t) = V_m cos(omega t + theta_v) e i(t) = I_m cos(omega t + theta_i).
La potencia instantánea es el producto directo p(t) = v(t) * i(t):
p(t) = V_m I_m cos(omega t + theta_v) cos(omega t + theta_i).
Aplicando la identidad 2 cos(A) cos(B) = cos(A - B) + cos(A + B):
p(t) = (1/2) V_m I_m cos(theta_v - theta_i) + (1/2) V_m I_m cos(2 omega t + theta_v + theta_i).
Expresado en valores eficaces (V_rms = V_m / sqrt(2), I_rms = I_m / sqrt(2)):
p(t) = V_rms I_rms cos(phi) [ 1 + cos(2 omega t) ] + V_rms I_rms sin(phi) sin(2 omega t).
2. Significado Físico de los Dos Términos:
- Potencia Activa P = V_rms I_rms cos(phi): Término medio unidireccional constante que se transforma en trabajo útil y calor.
- Potencia Reactiva Q = V_rms I_rms sin(phi): Componente oscilatoria a frecuencia doble 2 omega que viaja y regresa entre la fuente y los campos reactivos de la red con valor medio neto exactamente nulo.
3. Problema Resuelto 1 (Aplicación Directa):
Un motor monofásico de inducción conectado a v(t) = 170 cos(377 t) V consume una corriente i(t) = 10 cos(377 t - 36.87°) A. Calcule la potencia media activa P, la potencia reactiva Q y exprese la potencia instantánea p(t).
Solución:
Valores RMS: V_rms = 170 / sqrt(2) = 120.21 V, I_rms = 10 / sqrt(2) = 7.071 A.
Desfase: phi = theta_v - theta_i = 0 - (-36.87°) = +36.87°.
cos(36.87°) = 0.80 ; sin(36.87°) = 0.60.
1. Potencia Activa:
P = V_rms * I_rms * cos(phi) = (120.21) * (7.071) * 0.80 = 680.0 W.
2. Potencia Reactiva:
Q = V_rms * I_rms * sin(phi) = (120.21) * (7.071) * 0.60 = 510.0 VAR inductivos.
3. Potencia instantánea p(t):
p(t) = 680 * [ 1 + cos(754 t) ] + 510 * sin(754 t)
p(t) = 680 + 680 cos(754 t) + 510 sin(754 t) Watts.
(La potencia oscila a 120 Hz, el doble de la frecuencia fundamental de 60 Hz).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente por qué un sistema trifásico equilibrado entrega una potencia instantánea total estrictamente constante en el tiempo p_3phi(t) = 3 P, eliminando las oscilaciones a 2 omega presentes en sistemas monofásicos y evitando vibraciones mecánicas en generadores.
Solución:
En un sistema trifásico equilibrado:
p_a(t) = P + P cos(2 omega t) + Q sin(2 omega t).
p_b(t) = P + P cos(2 omega t - 240°) + Q sin(2 omega t - 240°).
p_c(t) = P + P cos(2 omega t - 120°) + Q sin(2 omega t - 120°).
Potencia instantánea total: p_3phi(t) = p_a(t) + p_b(t) + p_c(t)
p_3phi(t) = 3 P + P [ cos(2 omega t) + cos(2 omega t - 120°) + cos(2 omega t + 120°) ] + Q [ sin(2 omega t) + sin(2 omega t - 120°) + sin(2 omega t + 120°) ].
Por simetría trigonométrica de tres fasores desfasados 120° en el plano complejo:
sum_{k=0}^2 cos(alpha - k * 120°) = 0, y sum_{k=0}^2 sin(alpha - k * 120°) = 0.
Ambos términos oscilatorios se anulan idénticamente a cero para todo t.
Por lo tanto:
p_3phi(t) = 3 P = constante.
Esto demuestra la superioridad fundamental de los sistemas trifásicos en generación y motores industriales: entregan torque continuo y libre de pulsaciones mecánicas de doble frecuencia. Q.E.D.""",
        "bloque_sugerido": "Laboratorio 50 min • Potencia instantánea a doble frecuencia y ventaja trifásica",
        "slides": [
            {"numero": 1, "seccion": "INSTANTÁNEA", "titulo": "Descomposición de p(t)", "puntos": ["Término constante de potencia activa P = V_rms I_rms cos(phi).", "Fluctuación a frecuencia doble 2 omega debida a intercambio reactivo."]},
            {"numero": 2, "seccion": "TRIFÁSICA", "titulo": "Invarianza Temporal Trifásica", "puntos": ["Cancelación analítica de oscilaciones de 120 Hz en redes equilibradas.", "Torque electromagnético constante libre de vibraciones de fatiga."]}
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Potencia Compleja, Activa, Reactiva y el Triángulo de Potencias",
        "objetivo": "Modelar el balance de potencia compleja S = P + jQ y aplicar el Teorema de Conservación de la Potencia Compleja.",
        "concepto_clave_latex": r"\mathbf{S} = \mathbf{V}_{\text{rms}} \mathbf{I}_{\text{rms}}^* = P + jQ = |\mathbf{S}|\angle\theta \quad ; \quad |\mathbf{S}| = \sqrt{P^2 + Q^2} \quad ; \quad \text{FP} = \frac{P}{|\mathbf{S}|} = \cos(\theta)",
        "ejemplo": """CLASE MAGISTRAL: EL TRIÁNGULO DE POTENCIAS Y POTENCIA COMPLEJA
1. Definición Formal de la Potencia Compleja S:
S = V_rms * I_rms^*, donde I_rms^* es el conjugado complejo del fasor de corriente (el conjugado es matemáticamente necesario para que la potencia reactiva inductiva sea positiva Q > 0).
- Parte Real: Potencia Activa P en Vatios (W).
- Parte Imaginaria: Potencia Reactiva Q en Voltio-Amperios Reactivos (VAR).
  * Cargas inductivas (motores): Q > 0 (absorben reactivos).
  * Cargas capacitivas (bancos de condensadores): Q < 0 (generan reactivos).
- Magnitud |S|: Potencia Aparente en Voltio-Amperios (VA).
2. Factor de Potencia (FP = cos phi):
Razón entre la potencia activa que realiza trabajo útil y la potencia aparente total demandada a la red (FP = P / |S| in [0, 1]).
3. Conservación de la Potencia Compleja (Teorema de Boucherot):
En cualquier red eléctrica AC, la potencia compleja total entregada por las fuentes es igual a la suma fasorial de las potencias complejas absorbidas por cada rama:
sum S_fuentes = sum S_cargas => sum P_fuentes = sum P_cargas, y sum Q_fuentes = sum Q_cargas.
4. Problema Resuelto 1 (Aplicación Directa):
Una instalación comercial se alimenta a V = 220 angle(0°) V RMS y absorbe una corriente I = 25 angle(-36.87°) A RMS. Calcule la potencia compleja S, la potencia activa P, la potencia reactiva Q, la potencia aparente |S| y el factor de potencia FP indicando si está en adelanto o atraso.
Solución:
Conjugado de la corriente: I^* = 25 angle(+36.87°) A.
Potencia compleja:
S = V * I^* = (220 angle(0°)) * (25 angle(36.87°)) = 5500 angle(36.87°) VA.
En forma rectangular:
P = 5500 * cos(36.87°) = 5500 * 0.80 = 4,400.0 W = 4.40 kW.
Q = 5500 * sin(36.87°) = 5500 * 0.60 = + 3,300.0 VAR = + 3.30 kVAR.
Potencia aparente: |S| = 5,500 VA = 5.50 kVA.
Factor de potencia: FP = P / |S| = 4400 / 5500 = 0.80 en atraso (inductivo).
5. Problema Resuelto 2 (Nivel Examen Parcial):
Una fábrica en la zona industrial de Santa Marta tiene dos cargas en paralelo alimentadas a 440 V RMS a 60 Hz:
- Carga 1: Motor de inducción que consume P_1 = 40 kW con FP_1 = 0.707 inductivo (en atraso).
- Carga 2: Horno de resistencia eléctrica pura que consume P_2 = 30 kW con FP_2 = 1.0.
Aplique el Teorema de Boucherot para determinar: a) La potencia activa total P_total; b) La potencia reactiva total Q_total; c) La potencia aparente combinada |S_total|; d) El factor de potencia global de la planta.
Solución:
1. Para Carga 1:
P_1 = 40 kW.
Como FP_1 = cos(phi_1) = 0.707 ==> phi_1 = 45.0°.
Q_1 = P_1 * tan(phi_1) = 40 kW * tan(45°) = 40.0 kVAR.
S_1 = (40 + j 40) kVA.
2. Para Carga 2:
P_2 = 30 kW.
Como FP_2 = 1.0 ==> phi_2 = 0° ==> Q_2 = 0 kVAR.
S_2 = (30 + j 0) kVA.
3. Balance de Boucherot:
P_total = P_1 + P_2 = 40 + 30 = 70.0 kW.
Q_total = Q_1 + Q_2 = 40 + 0 = 40.0 kVAR.
Potencia compleja total: S_total = (70.0 + j 40.0) kVA.
4. Magnitud aparente total:
|S_total| = sqrt( (70)^2 + (40)^2 ) = sqrt( 4900 + 1600 ) = sqrt(6500) = 80.62 kVA.
5. Factor de potencia global:
FP_global = P_total / |S_total| = 70.0 / 80.62 = 0.8683 en atraso (86.83% inductivo).""",
        "bloque_sugerido": "Laboratorio 50 min • Triángulo de potencias y teorema de Boucherot",
        "slides": [
            {"numero": 1, "seccion": "POTENCIA COMPLEJA", "titulo": "Definición S = V I*", "puntos": ["Uso del conjugado de corriente para convención de signo inductivo Q > 0.", "Descomposición rectangular S = P + jQ y magnitud aparente |S| en kVA."]},
            {"numero": 2, "seccion": "BOUCHEROT", "titulo": "Teorema de Boucherot", "puntos": ["Conservación independiente de potencia activa P y reactiva Q.", "Cálculo directo de factor de potencia global en redes industriales."]}
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Compensación y Corrección del Factor de Potencia",
        "objetivo": "Dimensionar bancos de condensadores para corregir el factor de potencia a FP >= 0.95 y evitar penalizaciones CREG.",
        "concepto_clave_latex": r"Q_C = P [\tan(\theta_1) - \tan(\theta_2)] \quad ; \quad C = \frac{Q_C}{\omega V_{\text{rms}}^2} \quad ; \quad \text{Penalización CREG: } Q_{\text{ind}} > 0.5 P",
        "ejemplo": """CLASE MAGISTRAL: COMPENSACIÓN REACTIVA Y REGULACIÓN CREG 015
1. Justificación Técnica y Económica de la Compensación:
Un bajo factor de potencia (FP < 0.90) obliga al operador de red a transportar corrientes elevadas que saturan transformadores y aumentan las pérdidas Joule sin generar trabajo facturable. La regulación colombiana (Resolución CREG 015 de 2018) penaliza severamente el consumo de energía reactiva inductiva cuando supera el 50% de la energía activa (tan phi > 0.5, equivalente a FP < 0.894), y penaliza la inyección de reactiva capacitiva a cualquier nivel horario.
2. Principio de Compensación en Paralelo:
Se conectan condensadores en paralelo con la carga. Como el condensador suministra reactivos localmente (Q_C < 0), la red externa sólo tiene que suministrar la diferencia neta reducida Q_2 = Q_1 - Q_C, elevando el factor de potencia a cos(phi_2) >= 0.95 sin alterar la potencia activa P consumida por la maquinaria.
3. Problema Resuelto 1 (Aplicación Directa):
Una pequeña industria tiene una carga de P = 120 kW con FP_1 = 0.75 inductivo (tan phi_1 = 0.8819) conectada a V = 220 V RMS a 60 Hz. Se requiere elevar el factor de potencia a FP_2 = 0.95 inductivo (tan phi_2 = 0.3287) para eliminar cobros de energía reactiva en la factura. Calcule la potencia reactiva Q_C del banco de condensadores y la capacitancia total C necesaria.
Solución:
Potencia reactiva del banco de condensadores:
Q_C = P * [ tan(phi_1) - tan(phi_2) ]
Q_C = 120 kW * [ 0.8819 - 0.3287 ] = 120 * [ 0.5532 ] = 66.384 kVAR.
Cálculo de la capacitancia C (asumiendo conexión monofásica equivalente a 220 V y omega = 376.99 rad/s):
Q_C = omega * C * V^2 ==> C = Q_C / (omega * V^2)
C = 66,384 VAR / [ 376.99 rad/s * (220 V)^2 ]
C = 66,384 / [ 376.99 * 48,400 ] = 66,384 / 18,246,316 = 3.638 * 10^-3 Faradios = 3,638 uF.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre cuantitativamente el impacto de la compensación anterior sobre: a) La reducción de la corriente demandada a la red; b) La reducción porcentual en las pérdidas Joule I^2 R en la acometida eléctrica de alimentación.
Solución:
a) Corriente antes de compensar (FP_1 = 0.75):
S_1 = P / FP_1 = 120 kW / 0.75 = 160.0 kVA.
I_1 = S_1 / V = 160,000 VA / 220 V = 727.27 A.
Corriente después de compensar (FP_2 = 0.95):
S_2 = P / FP_2 = 120 kW / 0.95 = 126.316 kVA.
I_2 = S_2 / V = 126,316 VA / 220 V = 574.16 A.
Reducción de corriente: delta_I = 727.27 - 574.16 = 153.11 A (reducción del 21.05%).
b) Pérdidas Joule en el conductor de resistencia R:
Pérdidas antes: P_loss,1 = I_1^2 * R.
Pérdidas después: P_loss,2 = I_2^2 * R.
Relación de pérdidas:
P_loss,2 / P_loss,1 = (I_2 / I_1)^2 = (574.16 / 727.27)^2 = (0.7895)^2 = 0.6233 (62.33%).
Reducción de pérdidas en la acometida:
Ahorro = (1 - 0.6233) * 100% = 37.67% de reducción permanente de pérdidas térmicas.
Se liberaron 33.7 kVA de capacidad en el transformador de distribución y se redujo el calentamiento de cables en más de un tercio.""",
        "bloque_sugerido": "Laboratorio 50 min • Dimensionamiento de banco de condensadores y análisis CREG",
        "slides": [
            {"numero": 1, "seccion": "COMPENSACIÓN", "titulo": "Corrección de Factor de Potencia", "puntos": ["Ecuación de dimensionamiento Q_C = P [tan(phi_1) - tan(phi_2)].", "Suministro local de reactivos sin alterar la potencia activa P de trabajo."]},
            {"numero": 2, "seccion": "BENEFICIOS", "titulo": "Liberación de Capacidad y CREG 015", "puntos": ["Reducción de más del 35% en pérdidas Joule de acometidas.", "Eliminación de penalizaciones tarifarias por energía reactiva inductiva."]}
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Seguridad Eléctrica en DC/AC: Efectos Fisiológicos y Puesta a Tierra",
        "objetivo": "Aplicar la norma técnica RETIE e IEC 60479-1 sobre zonas de riesgo eléctrico y dimensionar sistemas de puesta a tierra.",
        "concepto_clave_latex": r"R_{\text{pat}} \le 10\,\Omega \quad ; \quad I_{\text{body}} = \frac{V_{\text{toque}}}{R_{\text{cuerpo}}} \quad ; \quad t_{\text{disparo}} \le 30\,\text{ms a } 30\,\text{mA (RCD)}",
        "ejemplo": """CLASE MAGISTRAL: SEGURIDAD ELÉCTRICA, EFECTOS BIOLÓGICOS Y RETIE
1. Efectos Fisiológicos de la Corriente Eléctrica (Norma IEC 60479-1):
No es el voltaje lo que mata a una persona, sino la intensidad de corriente que atraviesa el cuerpo humano y su duración temporal t:
- Zona 1 (< 0.5 mA): Imperceptible.
- Zona 2 (0.5 mA a 10 mA): Umbral de percepción y cosquilleo; sin efectos dañinos.
- Zona 3 (10 mA a 30 mA): Umbral de no soltar (tetanización muscular); la persona no puede abrir la mano para soltar el cable energizado; dificultad respiratoria.
- Zona 4 (> 30 mA para t > 0.5 s o > 500 mA instantáneo): Fibrilación ventricular del corazón (descoordinación irreversible del miocardio que detiene el bombeo sanguíneo, mortal en pocos minutos sin desfibrilador).
2. Tensión de Contacto (Paso y Toque):
- Resistencia del cuerpo humano: Típicamente considerada en 1000 Ohmios bajo piel húmeda según RETIE.
- Disyuntores Diferenciales (RCD / GFCI): Detectan corrientes de fuga a tierra desconectando en menos de 30 milisegundos cuando I_fuga >= 30 mA.
3. Sistemas de Puesta a Tierra (SPT):
Proporcionan una trayectoria de bajísima impedancia (R_pat <= 10 Ohm en subestaciones y edificios) para disipar corrientes de falla a tierra y descargas de rayos, limitando las tensiones de paso y toque a niveles no letales.
4. Problema Resuelto 1 (Aplicación Directa):
Una persona con piel húmeda y pies descalzos (resistencia total equivalente R_cuerpo = 1,000 Ohm) toca accidentalmente la carcasa metálica no conectada a tierra de una bomba que presenta una falla de aislamiento a V = 120 V AC. Calcule la corriente que atraviesa el cuerpo, clasifique la zona de riesgo según IEC 60479 y dictamine si existe peligro mortal.
Solución:
Corriente a través del cuerpo:
I_cuerpo = V / R_cuerpo = 120 V / 1,000 Ohm = 0.120 A = 120.0 mA.
Clasificación de riesgo:
120 mA supera con creces el umbral de tetanización muscular (10-30 mA) y penetra directamente en la Zona 4 de Fibrilación Ventricular (para t > 100 ms).
Dictamen de seguridad:
Peligro mortal inminente por paro cardíaco en menos de 1 segundo si el circuito no cuenta con un interruptor diferencial RCD de 30 mA.
5. Problema Resuelto 2 (Nivel Examen Parcial):
En la instalación anterior, se conecta la carcasa metálica de la bomba a un Sistema de Puesta a Tierra con resistencia R_pat = 5.0 Ohm. El circuito está protegido por un interruptor termomagnético de 20 A y aguas arriba por un interruptor diferencial RCD de 30 mA.
a) Cuando ocurre el contacto a masa de 120 V, calcule la corriente de falla a tierra que circula por el electrodo.
b) Calcule la tensión de contacto residual V_toque que aparece en la carcasa.
c) Determine la corriente residual que atravesaría a una persona de 1,000 Ohm que toque la carcasa en ese instante antes de que dispare la protección.
Solución:
a) Corriente de falla franca a tierra:
I_falla = V / R_pat = 120 V / 5.0 Ohm = 24.0 A.
(Como 24 A > 30 mA, el interruptor diferencial RCD detecta el desbalance instantáneamente y abre el circuito en menos de 25 milisegundos).
b) Tensión de contacto en la carcasa metálica durante los 25 ms de falla:
V_toque = I_falla * R_pat... ¡pero la carcasa está al potencial del divisor de tierra!
Considerando impedancia de la fuente despreciable frente a R_pat: la tensión es V_toque = 120 V si no hay retorno metálico, o si hay conductor de protección PE de R_PE = 0.5 Ohm: V_toque = 120 * (R_pat / (R_fase + R_pat)).
En el peor caso sin conductor neutro de retorno: V_toque = 120 V.
c) Corriente que derivaría por la persona:
Como el cuerpo (1000 Ohm) está en paralelo con la puesta a tierra (5 Ohm):
Por divisor de corriente:
I_persona = I_falla * [ R_pat / (R_cuerpo + R_pat) ] = 24.0 A * [ 5 / (1000 + 5) ] = 24.0 * (5 / 1005) = 0.119 A.
Sin embargo, el diferencial RCD corta en 20 ms.
Según la curva de la IEC 60479, para t = 20 ms, el umbral de fibrilación ventricular exige más de 500 mA. Por lo tanto, 119 mA durante 20 ms se ubica en la Zona 2 segura (shock perceptible pero sin daño biológico permanente), salvando la vida del operador.""",
        "bloque_sugerido": "Laboratorio 50 min • Curvas de disparo RCD y resistencia de puesta a tierra",
        "slides": [
            {"numero": 1, "seccion": "RETIE", "titulo": "Efectos Fisiológicos de la Corriente", "puntos": ["Curvas IEC 60479-1: umbral de no soltar (10-30 mA) y fibrilación (>50 mA).", "Resistencia del cuerpo humano normalizada en 1000 Ohmios bajo humedad."]},
            {"numero": 2, "seccion": "PROTECCIÓN", "titulo": "Puesta a Tierra y Disyuntor RCD", "puntos": ["Disyuntores diferenciales de 30 mA con tiempo de corte < 30 ms.", "Resistencia de puesta a tierra R_pat <= 10 Ohm según reglamento RETIE."]}
        ]
    }
]

if __name__ == '__main__':
    target = '      - codigo: "01021803"'
    yaml_text = format_topics_yaml(topics_10_to_20 + topics_21_to_30)
    inject_topics_after(target, yaml_text)
    print("03041819 Fundamentos de la Electricidad I now has 30 topics!")
