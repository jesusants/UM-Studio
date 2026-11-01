# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after, format_topics_yaml

topics_02011808 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Integración por Partes Tabular, Fórmulas de Reducción y Valor Cuadrático Medio (RMS)",
        "objetivo": "Aplicar el método tabular de integración por partes y fórmulas de reducción para calcular el valor eficaz (RMS) de señales de corriente y potencia periódica.",
        "concepto_clave_latex": r"\int u \, dv = u v - \int v \, du \quad ; \quad V_{\text{RMS}} = \sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt} \quad [\text{V}] \quad ; \quad \int \sin^n(x)\,dx = -\frac{\sin^{n-1}(x)\cos(x)}{n} + \frac{n-1}{n}\int \sin^{n-2}(x)\,dx",
        "ejemplo": """Problema 1: Una forma de onda de tensión no senoidal generada por un convertidor electrónico de potencia viene dada por v(t) = 100 t e^(-2t) [V] en el intervalo de medio ciclo t en [0, 1] s. Calcule la integral indefinida I = int t^2 e^(-4t) dt mediante el método de integración por partes tabular y halle la energía total disipada en un resistor de 1 Omega.
Paso 1: Tabla de derivadas sucesivas de u = t^2 y antiderivadas sucesivas de dv = e^(-4t) dt:
Signo (+): u = t^2,       v = -(1/4) e^(-4t)
Signo (-): u' = 2t,       v_1 = (1/16) e^(-4t)
Signo (+): u'' = 2,       v_2 = -(1/64) e^(-4t)
Signo (-): u''' = 0,      v_3 = (1/256) e^(-4t)
Paso 2: Suma de productos cruzados:
int t^2 e^(-4t) dt = -(1/4) t^2 e^(-4t) - (2/16) t e^(-4t) - (2/64) e^(-4t) = -e^(-4t) [(1/4) t^2 + (1/8) t + (1/32)] + C.
Paso 3: Evaluación definida entre 0 y 1:
En t = 1: -e^(-4) [1/4 + 1/8 + 1/32] = -e^(-4) [8/32 + 4/32 + 1/32] = -(13/32) e^(-4) = -0.40625 × 0.0183156 = -0.0074408.
En t = 0: -e^(0) [0 + 0 + 1/32] = -1/32 = -0.03125.
Paso 4: Integral = -0.0074408 - (-0.03125) = 0.023809.
Paso 5: Con v(t) = 100 t e^(-2t), v^2(t) = 10,000 t^2 e^(-4t).
Energía E = int_0^1 (v^2(t)/1) dt = 10,000 × 0.023809 = 238.09 J.

Problema 2: Deduzca el valor RMS de una corriente senoidal pura i(t) = I_m sin(omega t) de período T = 2pi/omega.
Paso 1: I_RMS^2 = (1/T) int_0^T I_m^2 sin^2(omega t) dt = (I_m^2 / T) int_0^T [(1 - cos(2 omega t)) / 2] dt.
Paso 2: (I_m^2 / (2T)) [t - sin(2 omega t)/(2 omega)]_0^T = (I_m^2 / (2T)) [T - 0] = I_m^2 / 2.
Paso 3: I_RMS = sqrt(I_m^2 / 2) = I_m / sqrt(2) ≈ 0.7071 I_m. Q.E.D.""",
        "bloque_sugerido": "Cálculo Simbólico 35 min • Métodos tabulares y deducción de valores RMS en convertidores"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Sustitución Universal de Weierstrass (Tangente del Ángulo Medio) en Circuitos AC",
        "objetivo": "Resolver integrales racionales trigonométricas complejas en análisis de potencia eléctrica mediante la sustitución t = tan(theta/2).",
        "concepto_clave_latex": r"t = \tan\left(\frac{\theta}{2}\right) \quad \Longrightarrow \quad \sin(\theta) = \frac{2t}{1+t^2} \quad , \quad \cos(\theta) = \frac{1-t^2}{1+t^2} \quad , \quad d\theta = \frac{2\,dt}{1+t^2}",
        "ejemplo": """Problema 1: En el cálculo del par electromagnético medio en un motor de reluctancia síncrona, se requiere resolver la integral I = int_0^(pi/2) [1 / (3 + 5 cos(theta))] d theta. Aplique la sustitución de Weierstrass t = tan(theta/2).
Paso 1: Para theta = 0 => t = tan(0) = 0; para theta = pi/2 => t = tan(pi/4) = 1.
Paso 2: Sustitución: cos(theta) = (1 - t^2)/(1 + t^2) y d theta = 2 dt / (1 + t^2).
Paso 3: Denominador: 3 + 5 cos(theta) = 3 + 5(1 - t^2)/(1 + t^2) = [3(1 + t^2) + 5 - 5t^2] / (1 + t^2) = (8 - 2t^2) / (1 + t^2) = 2(4 - t^2) / (1 + t^2).
Paso 4: Integrando: I = int_0^1 [ (2 dt / (1 + t^2)) / (2(4 - t^2) / (1 + t^2)) ] = int_0^1 [dt / (4 - t^2)].
Paso 5: Fracciones parciales: 1 / (4 - t^2) = 1 / [(2 - t)(2 + t)] = (1/4)[1/(2 - t) + 1/(2 + t)].
Paso 6: Antiderivada: (1/4) [ -ln|2 - t| + ln|2 + t| ] = (1/4) ln|(2 + t)/(2 - t)|.
Paso 7: Evaluando en 0 y 1: (1/4) [ ln(3/1) - ln(2/2) ] = (1/4) ln(3) ≈ 0.25 × 1.0986 = 0.2747.

Problema 2: Resuelva la integral indefinida int [d theta / (1 + sin(theta) + cos(theta))].
Paso 1: Denominador: 1 + 2t/(1+t^2) + (1-t^2)/(1+t^2) = (1 + t^2 + 2t + 1 - t^2) / (1+t^2) = (2 + 2t) / (1+t^2) = 2(1 + t) / (1+t^2).
Paso 2: Integral: int [ (2 dt / (1+t^2)) / (2(1+t) / (1+t^2)) ] = int [dt / (1 + t)] = ln|1 + t| + C.
Paso 3: Retornando a theta: ln|1 + tan(theta/2)| + C.""",
        "bloque_sugerido": "Taller Analítico 35 min • Transformaciones racionales trigonométricas en armónicos de red"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Integrales Impropias con Límites Infinitos y Criterios de Convergencia",
        "objetivo": "Determinar la convergencia o divergencia de integrales de primera especie en energía disipada en líneas infinitas y funciones de probabilidad.",
        "concepto_clave_latex": r"\int_a^\infty f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx \quad ; \quad \int_1^\infty \frac{dx}{x^p} = \begin{cases} \frac{1}{p-1} & \text{si } p > 1 \\ \text{diverge} & \text{si } p \le 1 \end{cases}",
        "ejemplo": """Problema 1: Un generador de impulsos tipo rayo descarga a tierra una corriente modelada como i(t) = I_0 e^(-t/tau) [A] para t en [0, inf), con I_0 = 10 kA (10,000 A) y constante de tiempo tau = 50 microsegundos (50 × 10^(-6) s). Calcule la carga eléctrica total Q = int_0^inf i(t) dt transferida a tierra y la energía total disipada W_R en un electrodo de puesta a tierra con resistencia R = 5 Omega.
Paso 1: Carga total: Q = lim_{b -> inf} int_0^b 10000 e^(-t / (50 × 10^(-6))) dt.
Paso 2: Antiderivada: [-10000 × (50 × 10^(-6)) e^(-t/tau)]_0^b = -0.50 [e^(-b/tau) - e^(0)] = -0.50 [0 - 1] = 0.50 Coulombs.
Paso 3: Potencia instantánea p(t) = i^2(t) R = (10,000)^2 e^(-2t/tau) × 5 = 5 × 10^8 e^(-2t/tau) [W].
Paso 4: Energía W_R = int_0^inf 5 × 10^8 e^(-2t/tau) dt = 5 × 10^8 × (tau / 2) = 5 × 10^8 × (25 × 10^(-6)) = 12,500 J = 12.5 kJ.

Problema 2: Determine mediante el criterio de comparación directa si converge la integral I = int_1^inf [(x + 2) / (x^3 + 4x + 1)] dx.
Paso 1: Comportamiento asintótico para x grande: (x + 2) / (x^3 + 4x + 1) ≈ x / x^3 = 1 / x^2.
Paso 2: Para x >= 1: x + 2 <= 3x, y x^3 + 4x + 1 > x^3. Luego (x + 2) / (x^3 + 4x + 1) < 3x / x^3 = 3 / x^2.
Paso 3: Como int_1^inf (3 / x^2) dx = 3 [ -1/x ]_1^inf = 3 [0 - (-1)] = 3 (converge con p = 2 > 1).
Paso 4: Por el teorema de comparación directa, la integral original converge estrictamente a un valor finito menor a 3.""",
        "bloque_sugerido": "Resolución Formal 30 min • Criterios de comparación en el límite y p-integrales en potencia"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Integrales Impropias con Integrandos Discontinuos y Valor Principal de Cauchy",
        "objetivo": "Evaluar integrales de segunda especie con asíntotas verticales en la frontera o el interior y calcular el Valor Principal de Cauchy en dieléctricos.",
        "concepto_clave_latex": r"\text{P.V.} \int_{-\infty}^\infty f(x)\,dx = \lim_{R \to \infty} \int_{-R}^R f(x)\,dx \quad ; \quad \text{P.V.} \int_a^b \frac{g(x)}{x - c}\,dx = \lim_{\varepsilon \to 0^+} \left[\int_a^{c-\varepsilon} \frac{g(x)}{x-c}\,dx + \int_{c+\varepsilon}^b \frac{g(x)}{x-c}\,dx\right]",
        "ejemplo": """Problema 1: Analice la convergencia de la integral impropia de segunda especie I = int_0^4 [1 / sqrt(4 - x)] dx, que presenta una discontinuidad infinita en el límite superior x = 4.
Paso 1: Expresión de límite: I = lim_{b -> 4^-} int_0^b (4 - x)^(-1/2) dx.
Paso 2: Cambio de variable u = 4 - x, du = -dx: int -(u)^(-1/2) du = -2 u^(1/2) = -2 sqrt(4 - x).
Paso 3: Evaluación de límites: lim_{b -> 4^-} [ -2 sqrt(4 - b) - (-2 sqrt(4 - 0)) ].
Paso 4: lim_{b -> 4^-} [ -2 sqrt(4 - b) + 2(2) ] = 0 + 4 = 4.
Paso 5: La integral converge a 4.

Problema 2: Calcule el Valor Principal de Cauchy de la integral I = int_(-1)^2 (1/x) dx, la cual diverge en el sentido clásico de Riemann debido a la singularidad no integrable en x = 0.
Paso 1: Por definición de Valor Principal de Cauchy con epsilon simétrico:
P.V. int_(-1)^2 (1/x) dx = lim_{epsilon -> 0^+} [ int_(-1)^(-epsilon) (1/x) dx + int_epsilon^2 (1/x) dx ].
Paso 2: Primera parte: [ln|x|]_(-1)^(-epsilon) = ln|-epsilon| - ln|-1| = ln(epsilon) - 0 = ln(epsilon).
Paso 3: Segunda parte: [ln|x|]_epsilon^2 = ln(2) - ln(epsilon).
Paso 4: Suma de contribuciones: lim_{epsilon -> 0^+} [ ln(epsilon) + ln(2) - ln(epsilon) ] = ln(2) ≈ 0.69315.
Paso 5: Las divergencias simétricas hacia -inf y +inf se anulan exactamente, arrojando el valor principal finito ln(2).""",
        "bloque_sugerido": "Análisis Riguroso 35 min • Singularidades de Cauchy y relaciones de Kramers-Kronig en materiales"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Cálculo de Volúmenes por Secciones Transversales y Capas Cilíndricas (Cascarones)",
        "objetivo": "Calcular volúmenes de sólidos de revolución en diseño de rotores de turbinas y recipientes a presión mediante discos, arandelas y cascarones cilíndricos.",
        "concepto_clave_latex": r"V_{\text{arandelas}} = \pi \int_a^b \left[R_{\text{ext}}^2(x) - R_{\text{int}}^2(x)\right]\,dx \quad ; \quad V_{\text{cascarones}} = 2\pi \int_a^b x \cdot [y_{\text{sup}}(x) - y_{\text{inf}}(x)]\,dx",
        "ejemplo": """Problema 1: El perfil de la carcasa de una microturbina hidráulica se genera al rotar la región delimitada por y = sqrt(x), la recta y = x/2, entre x = 0 y x = 4, alrededor del eje x. Calcule el volumen interior del sólido mediante el método de las arandelas.
Paso 1: Puntos de intersección: sqrt(x) = x/2 => x = x^2 / 4 => x^2 - 4x = 0 => x = 0 y x = 4.
Paso 2: En el intervalo [0, 4], sqrt(x) >= x/2.
Radio exterior R_ext(x) = sqrt(x); Radio interior R_int(x) = x/2.
Paso 3: Diferencial de volumen: dV = pi [ (sqrt(x))^2 - (x/2)^2 ] dx = pi [ x - x^2 / 4 ] dx.
Paso 4: Integración: V = pi int_0^4 (x - x^2 / 4) dx = pi [ x^2 / 2 - x^3 / 12 ]_0^4.
Paso 5: V = pi [ 16/2 - 64/12 ] = pi [ 8 - 16/3 ] = pi [ 24/3 - 16/3 ] = (8/3) pi ≈ 8.3776 m³.

Problema 2: Calcule el volumen del mismo sólido cuando la región se rota alrededor del eje y mediante el método de cascarones cilíndricos.
Paso 1: Radio de la capa r(x) = x; Altura h(x) = sqrt(x) - x/2.
Paso 2: dV = 2 pi x (sqrt(x) - x/2) dx = 2 pi (x^(3/2) - x^2 / 2) dx.
Paso 3: V = 2 pi int_0^4 (x^(3/2) - x^2 / 2) dx = 2 pi [ (2/5) x^(5/2) - x^3 / 6 ]_0^4.
Paso 4: Evaluando en x = 4: 4^(5/2) = (sqrt(4))^5 = 32.
V = 2 pi [ (2/5)(32) - 64/6 ] = 2 pi [ 64/5 - 32/3 ] = 2 pi [ (192 - 160) / 15 ] = 2 pi [ 32 / 15 ] = (64/15) pi ≈ 13.404 m³.""",
        "bloque_sugerido": "Modelación Geométrica 35 min • Integrales de volumen aplicadas a toberas y carcasas de turbinas"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Longitud de Curva Paramétrica y Superficie de Revolución en Álabes Eólicos",
        "objetivo": "Calcular la longitud de arco y área superficial exterior de perfiles aerodinámicos y conos de buje rotatorios mediante integrales de línea.",
        "concepto_clave_latex": r"L = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt \quad ; \quad S = 2\pi \int_{t_1}^{t_2} y(t) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt",
        "ejemplo": """Problema 1: El borde de ataque de un álabe eólico de geometría toroidal se parametriza como x(t) = 3 cos^3(t), y(t) = 3 sin^3(t) (astroide) para t en [0, pi/2]. Calcule la longitud de arco L de este segmento.
Paso 1: Derivadas: dx/dt = 3 × 3 cos^2(t)(-sin(t)) = -9 cos^2(t) sin(t).
dy/dt = 3 × 3 sin^2(t) cos(t) = 9 sin^2(t) cos(t).
Paso 2: Suma de cuadrados: (dx/dt)^2 + (dy/dt)^2 = 81 cos^4(t) sin^2(t) + 81 sin^4(t) cos^2(t) = 81 sin^2(t) cos^2(t) [ cos^2(t) + sin^2(t) ] = 81 sin^2(t) cos^2(t).
Paso 3: Raíz cuadrada: sqrt(81 sin^2(t) cos^2(t)) = 9 sin(t) cos(t) (positivo en [0, pi/2]).
Paso 4: Integral: L = int_0^(pi/2) 9 sin(t) cos(t) dt = 9 [ sin^2(t) / 2 ]_0^(pi/2) = (9/2)[ 1^2 - 0 ] = 4.5 metros.

Problema 2: Se genera el cono de ojiva de la turbina al rotar el segmento de recta y = (1/3) x desde x = 0 hasta x = 6 metros alrededor del eje x. Calcule el área lateral de la superficie de revolución S.
Paso 1: dy/dx = 1/3 => sqrt(1 + (dy/dx)^2) = sqrt(1 + 1/9) = sqrt(10/9) = sqrt(10) / 3.
Paso 2: S = 2 pi int_0^6 y sqrt(1 + (dy/dx)^2) dx = 2 pi int_0^6 ((1/3) x) (sqrt(10) / 3) dx = (2 pi sqrt(10) / 9) int_0^6 x dx.
Paso 3: S = (2 pi sqrt(10) / 9) [ x^2 / 2 ]_0^6 = (2 pi sqrt(10) / 9) [ 36 / 2 ] = (2 pi sqrt(10) / 9) × 18 = 4 pi sqrt(10) ≈ 39.738 m².""",
        "bloque_sugerido": "Cálculo Geométrico 35 min • Integrales de superficie y longitud de álabe eólico con curvatura 3D"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Trabajo Mecánico Variable, Bombeo en Embalses Hidroeléctricos y Presión Hidrostática",
        "objetivo": "Plantear integrales definidas de trabajo para el vaciado/llenado de tanques y presas hidráulicas, y calcular la fuerza neta hidrostática contra compuertas.",
        "concepto_clave_latex": r"W = \int_{y_1}^{y_2} \rho g A(y) \cdot [d - y]\,dy \quad [\text{J}] \quad ; \quad F_{\text{hidro}} = \rho g \int_{y_1}^{y_2} y \cdot w(y)\,dy \quad [\text{N}]",
        "ejemplo": """Problema 1: Un embalse de bombeo hidroeléctrico tiene la forma de un cono invertido de radio superior R = 30 m y profundidad H = 20 m lleno de agua (rho = 1,000 kg/m³, g = 9.81 m/s²). Calcule el trabajo mecánico W necesario para bombear toda el agua hasta el borde superior del embalse.
Paso 1: A una altura y desde el fondo (0 <= y <= 20), el radio del disco horizontal es por triángulos semejantes: r(y) / y = R / H = 30 / 20 = 1.5 => r(y) = 1.5 y.
Paso 2: Área de la rebanada horizontal: A(y) = pi r^2(y) = pi (1.5 y)^2 = 2.25 pi y^2.
Paso 3: Masa del elemento: dm = rho A(y) dy = 1000 × 2.25 pi y^2 dy = 2250 pi y^2 dy.
Paso 4: Distancia que debe elevarse el elemento hasta el borde superior (y = 20): d(y) = 20 - y.
Paso 5: Diferencial de trabajo: dW = dm g d(y) = (2250 pi y^2 dy)(9.81)(20 - y) = 22,072.5 pi (20 y^2 - y^3) dy.
Paso 6: Integral: W = 22,072.5 pi int_0^20 (20 y^2 - y^3) dy = 22,072.5 pi [ (20/3) y^3 - y^4 / 4 ]_0^20.
Paso 7: W = 22,072.5 pi [ (20/3)(8000) - 160000 / 4 ] = 22,072.5 pi [ 53,333.33 - 40,000 ] = 22,072.5 pi × 13,333.33 = 2.943 × 10^8 pi ≈ 9.245 × 10^8 J = 924.5 MJ = 256.8 kWh.

Problema 2: Una compuerta vertical rectangular de una represa tiene un ancho b = 8 m y una altura h = 5 m, con su borde superior sumergido a 10 m de la superficie libre del agua. Calcule la fuerza hidrostática total F ejercida contra la compuerta.
Paso 1: Profundidad h(y) varía de y = 10 m hasta y = 15 m.
Paso 2: Elemento de fuerza: dF = P(y) dA = (rho g y) (b dy) = (1000 × 9.81 × 8) y dy = 78,480 y dy.
Paso 3: F = 78,480 int_10^15 y dy = 78,480 [ y^2 / 2 ]_10^15 = 39,240 [ 225 - 100 ] = 39,240 × 125 = 4,905,000 N = 4.905 MN.""",
        "bloque_sugerido": "Aplicaciones Físicas 40 min • Balances de bombeo en centrales de almacenamiento por bombeo (PHES)"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Centroides de Regiones Planas, Teoremas de Pappus-Guldin y Momentos de Inercia",
        "objetivo": "Determinar las coordenadas del centro de masa, momentos de inercia y áreas/volúmenes de revolución mediante los teoremas geométricos de Pappus.",
        "concepto_clave_latex": r"\bar{x} = \frac{\int x \, dA}{A} \quad , \quad \bar{y} = \frac{\int y \, dA}{A} \quad ; \quad V = 2\pi \bar{r} A \quad ; \quad I_x = \iint y^2 \, dA \quad [\text{m}^4]",
        "ejemplo": """Problema 1: Halle las coordenadas del centroide (x_bar, y_bar) de la región parabólica delimitada por y = 4 - x^2 y el eje x (y = 0).
Paso 1: Límites: 4 - x^2 = 0 => x = -2 y x = +2.
Por simetría respecto al eje y, x_bar = 0.
Paso 2: Área total: A = int_(-2)^2 (4 - x^2) dx = 2 int_0^2 (4 - x^2) dx = 2 [ 4x - x^3 / 3 ]_0^2 = 2 [ 8 - 8/3 ] = 2(16/3) = 32/3.
Paso 3: Momento respecto al eje x: M_x = (1/2) int_(-2)^2 y^2 dx = (1/2) int_(-2)^2 (4 - x^2)^2 dx = int_0^2 (16 - 8x^2 + x^4) dx.
Paso 4: M_x = [ 16x - (8/3) x^3 + x^5 / 5 ]_0^2 = [ 32 - 64/3 + 32/5 ] = 32 [ 1 - 2/3 + 1/5 ] = 32 [ (15 - 10 + 3) / 15 ] = 32 [ 8 / 15 ] = 256 / 15.
Paso 5: Coordenada y_bar = M_x / A = (256 / 15) / (32 / 3) = (256 / 15) × (3 / 32) = 8 / 5 = 1.60.
Centroide: (0, 1.60).

Problema 2: Un toro de almacenamiento de gas se genera al rotar un círculo de radio r = 2 m cuyo centro dista R = 7 m del eje de rotación. Calcule el volumen y el área exterior del toro mediante los teoremas de Pappus.
Paso 1: Por el primer teorema de Pappus: Área exterior S = 2 pi R_c L_perímetro = 2 pi (7) × (2 pi × 2) = 14 pi × 4 pi = 56 pi^2 ≈ 552.74 m².
Paso 2: Por el segundo teorema de Pappus: Volumen V = 2 pi R_c A_círculo = 2 pi (7) × (pi × 2^2) = 14 pi × 4 pi = 56 pi^2 ≈ 552.74 m³.""",
        "bloque_sugerido": "Mecánica Geométrica 35 min • Cálculo de momentos de inercia I_xx e I_yy en perfiles estructurales"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Funciones Gamma y Beta de Euler: Propiedades y Solución de Integrales Trascendentes",
        "objetivo": "Resolver integrales definidas trascendentes complejas mediante las funciones Gamma Gamma(z) y Beta B(p,q) de Euler.",
        "concepto_clave_latex": r"\Gamma(z) = \int_0^\infty t^{z-1} e^{-t}\,dt \quad ; \quad \mathrm{B}(p,q) = \int_0^1 x^{p-1} (1-x)^{q-1}\,dx = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)} \quad ; \quad \Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}",
        "ejemplo": """Problema 1: En mecánica cuántica y física de semiconductores se presenta la integral gaussiana I = int_0^inf x^4 e^(-2 x^2) dx. Resuélvala mediante la función Gamma.
Paso 1: Cambio de variable: sea t = 2 x^2 => x = (t/2)^(1/2) => x^4 = t^2 / 4.
Diferencial: dt = 4x dx => dx = dt / (4x) = dt / [4 (t/2)^(1/2)] = (1 / (4 sqrt(2))) t^(-1/2) dt.
Paso 2: Sustituyendo: I = int_0^inf (t^2 / 4) e^(-t) [ (1 / (4 sqrt(2))) t^(-1/2) dt ] = (1 / (16 sqrt(2))) int_0^inf t^(3/2) e^(-t) dt.
Paso 3: Reconociendo la función Gamma con z - 1 = 3/2 => z = 5/2:
int_0^inf t^(3/2) e^(-t) dt = Gamma(5/2).
Paso 4: Propiedad recursiva: Gamma(5/2) = (3/2) Gamma(3/2) = (3/2)(1/2) Gamma(1/2) = (3/4) sqrt(pi).
Paso 5: I = (1 / (16 sqrt(2))) × (3/4) sqrt(pi) = 3 sqrt(pi) / (64 sqrt(2)) = 3 sqrt(2 pi) / 128 ≈ 0.05875.

Problema 2: Evalúe la integral trigonométrica I = int_0^(pi/2) sin^5(theta) cos^3(theta) d theta usando la función Beta.
Paso 1: Identidad Beta: int_0^(pi/2) sin^(2p-1)(theta) cos^(2q-1)(theta) d theta = (1/2) B(p, q).
Paso 2: Igualando exponentes: 2p - 1 = 5 => 2p = 6 => p = 3; 2q - 1 = 3 => 2q = 4 => q = 2.
Paso 3: I = (1/2) B(3, 2) = (1/2) [ Gamma(3) Gamma(2) / Gamma(3 + 2) ] = (1/2) [ 2! × 1! / 4! ] = (1/2) [ 2 × 1 / 24 ] = (1/2)(1/12) = 1/24 ≈ 0.04167.""",
        "bloque_sugerido": "Funciones Especiales 35 min • Integrales de Wallis y aplicaciones de Gamma en termodinámica estadística"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Transformada de Laplace por Integración Impropia y Transitorios Eléctricos RL y RC",
        "objetivo": "Deducir analíticamente transformadas de Laplace mediante su integral impropia de definición y resolver ecuaciones diferenciales de circuitos transitorios.",
        "concepto_clave_latex": r"\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t) e^{-st}\,dt \quad ; \quad \mathcal{L}\{f'(t)\} = s F(s) - f(0^-) \quad ; \quad i(t) = \frac{V_0}{R}\left(1 - e^{-t/\tau}\right)",
        "ejemplo": """Problema 1: Deduzca a partir de la definición de integral impropia la transformada de Laplace de la función f(t) = e^(a t).
Paso 1: F(s) = int_0^inf e^(a t) e^(-s t) dt = int_0^inf e^(-(s - a) t) dt.
Paso 2: Con s > a (región de convergencia): lim_{b -> inf} [ -e^(-(s - a) t) / (s - a) ]_0^b.
Paso 3: [ 0 - (-1 / (s - a)) ] = 1 / (s - a). Q.E.D.

Problema 2: Un circuito serie RL (R = 10 Omega, L = 0.5 H) con corriente inicial i(0) = 0 se conecta a una fuente continua V_0 = 24 V en t = 0. Formule la ecuación diferencial L (di/dt) + R i = V_0, aplique la transformada de Laplace y halle la expresión temporal de la corriente i(t).
Paso 1: E.D.: 0.5 (di/dt) + 10 i = 24.
Paso 2: Transformando: 0.5 [ s I(s) - 0 ] + 10 I(s) = 24 / s.
I(s) [ 0.5 s + 10 ] = 24 / s => I(s) [ s + 20 ] = 48 / s => I(s) = 48 / [ s (s + 20) ].
Paso 3: Fracciones parciales: 48 / [ s (s + 20) ] = A / s + B / (s + 20).
A = 48 / 20 = 2.4; B = 48 / (-20) = -2.4.
Paso 4: I(s) = 2.4 / s - 2.4 / (s + 20).
Paso 5: Antitransformada inmediata: i(t) = 2.4 (1 - e^(-20 t)) A.
La corriente de estado estacionario es 2.4 A y la constante de tiempo es tau = L / R = 0.5 / 10 = 0.05 s (1/20 s).""",
        "bloque_sugerido": "Resolución Operacional 40 min • Transitorios de segundo orden RLC y polos en el semiplano izquierdo"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Criterios de Convergencia de Series Numéricas: Integral, Razón y Raíz",
        "objetivo": "Evaluar la convergencia de series infinitas que modelan discretizaciones de potencia aplicando los criterios de Cauchy, d'Alembert y la raíz.",
        "concepto_clave_latex": r"L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| \quad ; \quad \rho = \lim_{n \to \infty} \sqrt[n]{|a_n|} \quad ; \quad \sum_{n=1}^\infty a_n \text{ converge si } L < 1 \text{ o } \rho < 1",
        "ejemplo": """Problema 1: Determine la convergencia de la serie sum_{n=1}^inf [n^3 / 3^n] mediante el criterio de la razón de d'Alembert.
Paso 1: Término n-ésimo a_n = n^3 / 3^n; a_{n+1} = (n + 1)^3 / 3^(n+1).
Paso 2: Cociente: a_{n+1} / a_n = [ (n + 1)^3 / 3^(n+1) ] × [ 3^n / n^3 ] = [ (n + 1) / n ]^3 × (3^n / 3^(n+1)) = (1 + 1/n)^3 × (1/3).
Paso 3: Límite: L = lim_{n -> inf} [ (1 + 1/n)^3 × (1/3) ] = 1^3 × (1/3) = 1/3.
Paso 4: Como L = 1/3 < 1, la serie converge absolutamente.

Problema 2: Evalúe mediante el criterio integral de Cauchy la convergencia de la serie sum_{n=2}^inf [1 / (n ln(n))].
Paso 1: La función f(x) = 1 / (x ln(x)) es positiva, continua y estrictamente decreciente para x >= 2.
Paso 2: Integral impropia: I = int_2^inf [1 / (x ln(x))] dx.
Paso 3: Cambio de variable u = ln(x), du = dx / x:
int [du / u] = ln|u| = ln(ln(x)).
Paso 4: Límite: lim_{b -> inf} [ ln(ln(b)) - ln(ln(2)) ] = inf.
Paso 5: Como la integral diverge, la serie sum_{n=2}^inf [1 / (n ln(n))] diverge irremediablemente.""",
        "bloque_sugerido": "Demostración Rigurosa 30 min • Comparación de convergencia en series armónicas generalizadas"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Series Alternadas, Criterio de Leibniz y Estimación del Error por Truncamiento",
        "objetivo": "Determinar convergencia condicional y acotar el error de truncamiento al aproximar flujos de potencia mediante series alternadas.",
        "concepto_clave_latex": r"\sum_{n=1}^\infty (-1)^{n+1} b_n \quad \text{converge si } b_{n+1} \le b_n \text{ y } \lim_{n \to \infty} b_n = 0 \quad ; \quad |R_N| = |S - S_N| \le b_{N+1}",
        "ejemplo": """Problema 1: Demuestre que la serie alternada sum_{n=1}^inf [(-1)^(n+1) / n^2] converge y determine el número mínimo de términos N necesarios para que el error de la suma parcial sea estrictamente menor a 10^(-4) (0.0001).
Paso 1: b_n = 1 / n^2 > 0 para todo n >= 1.
Paso 2: Decrecimiento: b_{n+1} = 1 / (n+1)^2 < 1 / n^2 = b_n.
Paso 3: Límite: lim_{n -> inf} (1 / n^2) = 0. Por el criterio de Leibniz, la serie converge.
Paso 4: Cota de error alternante: |R_N| <= b_{N+1} = 1 / (N + 1)^2.
Paso 5: Desigualdad: 1 / (N + 1)^2 < 10^(-4) => (N + 1)^2 > 10,000 => N + 1 > 100 => N >= 100.
Paso 6: Con N = 100 términos se garantiza una precisión superior a 4 cifras decimales.

Problema 2: Clasifique la serie sum_{n=1}^inf [(-1)^(n+1) / sqrt(n)] como absolutamente convergente, condicionalmente convergente o divergente.
Paso 1: La serie de valores absolutos sum_{n=1}^inf |(-1)^(n+1) / sqrt(n)| = sum_{n=1}^inf (1 / n^(1/2)) es una p-serie con p = 1/2 <= 1, la cual diverge.
Paso 2: La serie alternada original cumple Leibniz: 1/sqrt(n) decrece a cero, luego converge.
Paso 3: Al converger la serie alternada pero divergir su valor absoluto, la serie es condicionalmente convergente.""",
        "bloque_sugerido": "Análisis Numérico 30 min • Acotación de errores de truncamiento en algoritmos de control digital"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Series de Potencias, Radio e Intervalo de Convergencia en Modelado de Semiconductores",
        "objetivo": "Calcular el radio e intervalo de convergencia de series de potencias para aproximar características no lineales de diodos y celdas solares.",
        "concepto_clave_latex": r"\sum_{n=0}^\infty c_n (x - a)^n \quad ; \quad R = \lim_{n \to \infty} \left|\frac{c_n}{c_{n+1}}\right| \quad ; \quad I = (a - R, a + R)",
        "ejemplo": """Problema 1: Halle el centro a, el radio de convergencia R y el intervalo de convergencia I de la serie de potencias sum_{n=1}^inf [ (2x - 3)^n / (n 4^n) ].
Paso 1: Reescritura: (2x - 3)^n = 2^n (x - 1.5)^n. Centro a = 3/2 = 1.5.
Término general a_n = [ 2^n (x - 1.5)^n ] / [ n 4^n ] = (x - 1.5)^n / [ n 2^n ].
Paso 2: Criterio de la razón: |a_{n+1} / a_n| = |x - 1.5| × [ n / (n + 1) ] × (1/2).
Paso 3: Límite: L = (|x - 1.5| / 2) lim [ n / (n + 1) ] = |x - 1.5| / 2.
Paso 4: Convergencia: L < 1 => |x - 1.5| / 2 < 1 => |x - 1.5| < 2. Radio R = 2.
Paso 5: Extremos del intervalo provisional: 1.5 - 2 = -0.5; 1.5 + 2 = 3.5.
Paso 6: En x = 3.5 (x - 1.5 = 2): sum 2^n / (n 2^n) = sum (1/n) (serie armónica diverge).
Paso 7: En x = -0.5 (x - 1.5 = -2): sum (-2)^n / (n 2^n) = sum (-1)^n / n (serie armónica alternada converge).
Paso 8: Intervalo exacto de convergencia: I = [-0.5, 3.5) o [-1/2, 7/2).

Problema 2: Halle el radio de convergencia de la serie de Bessel J_0(x) = sum_{k=0}^inf [ (-1)^k x^(2k) ] / [ 2^(2k) (k!)^2 ].
Paso 1: Criterio de la razón con a_k = x^(2k) / [ 4^k (k!)^2 ]:
|a_{k+1} / a_k| = x^2 / [ 4 (k + 1)^2 ].
Paso 2: Para cualquier x fijo, lim_{k -> inf} [ x^2 / (4 (k + 1)^2) ] = 0 < 1.
Paso 3: La serie converge para todo x real: radio R = inf.""",
        "bloque_sugerido": "Aproximación Analítica 35 min • Expansión en serie del diodo de Shockley en el punto de máxima potencia"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Derivación e Integración Término a Término de Series de Potencias",
        "objetivo": "Obtener representaciones analíticas de integrales no elementales mediante derivación e integración término a término dentro del radio de convergencia.",
        "concepto_clave_latex": r"\frac{d}{dx}\left[\sum_{n=0}^\infty c_n (x-a)^n\right] = \sum_{n=1}^\infty n c_n (x-a)^{n-1} \quad ; \quad \int \left[\sum_{n=0}^\infty c_n (x-a)^n\right]dx = C + \sum_{n=0}^\infty \frac{c_n}{n+1}(x-a)^{n+1}",
        "ejemplo": """Problema 1: A partir de la serie geométrica 1 / (1 + x) = sum_{n=0}^inf (-1)^n x^n para |x| < 1, deduzca la serie de potencias de ln(1 + x) y calcule una aproximación de ln(1.2) con 4 términos.
Paso 1: Integrando término a término: ln(1 + x) = int_0^x [ 1 / (1 + t) ] dt = sum_{n=0}^inf (-1)^n int_0^x t^n dt.
Paso 2: ln(1 + x) = sum_{n=0}^inf (-1)^n [ x^(n+1) / (n + 1) ] = x - x^2/2 + x^3/3 - x^4/4 + ... para -1 < x <= 1.
Paso 3: Para x = 0.2:
Término 1: +0.200000
Término 2: -(0.2)^2 / 2 = -0.04 / 2 = -0.020000
Término 3: +(0.2)^3 / 3 = +0.008 / 3 = +0.002667
Término 4: -(0.2)^4 / 4 = -0.0016 / 4 = -0.000400
Paso 4: Suma = 0.200000 - 0.020000 + 0.002667 - 0.000400 = 0.182267.
Paso 5: Valor exacto: ln(1.2) = 0.182321 (error < 0.03%).

Problema 2: Exprese la integral no elemental de la función de error Gaussiana erf(x) = (2 / sqrt(pi)) int_0^x e^(-t^2) dt en serie de potencias.
Paso 1: e^(-t^2) = sum_{n=0}^inf [ (-t^2)^n / n! ] = sum_{n=0}^inf [ (-1)^n t^(2n) / n! ].
Paso 2: Integrando: int_0^x e^(-t^2) dt = sum_{n=0}^inf [ (-1)^n x^(2n+1) / (n! (2n + 1)) ] = x - x^3/3 + x^5/10 - x^7/42 + ...
Paso 3: erf(x) = (2 / sqrt(pi)) [ x - x^3/3 + x^5/10 - x^7/42 + ... ] para todo x en R.""",
        "bloque_sugerido": "Resolución Matemática 35 min • Integración de perfiles térmicos no gaussianos en cables subterráneos"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Series de Fourier para Funciones Periódicas de Período Arbitrario en Sistemas de Potencia",
        "objetivo": "Descomponer ondas periódicas distorsionadas en armónicos senoidales calculando los coeficientes de Fourier a_0, a_n y b_n.",
        "concepto_clave_latex": r"f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[a_n \cos\left(\frac{n\pi t}{L}\right) + b_n \sin\left(\frac{n\pi t}{L}\right)\right] \quad ; \quad a_n = \frac{1}{L}\int_{-L}^L f(t)\cos\left(\frac{n\pi t}{L}\right)dt",
        "ejemplo": """Problema 1: Una onda de tensión cuadrada simétrica de período T = 20 ms (f = 50 Hz, semiperíodo L = 10 ms = 0.01 s) generada por un inversor conmuta entre +100 V en [-L, 0) y -100 V en [0, L) (función impar). Halle los coeficientes de Fourier a_0, a_n y b_n, y exprese los primeros 3 armónicos no nulos.
Paso 1: Por ser función impar: a_0 = 0 y a_n = 0 para todo n.
Paso 2: Coeficiente b_n por simetría impar:
b_n = (2/L) int_0^L (-100) sin(n pi t / L) dt = (-200 / L) [ -L / (n pi) cos(n pi t / L) ]_0^L = (200 / (n pi)) [ cos(n pi) - 1 ].
Paso 3: Para n par: cos(n pi) = 1 => b_n = 0.
Para n impar: cos(n pi) = -1 => b_n = (200 / (n pi)) (-2) = -400 / (n pi).
Paso 4: Serie de Fourier: v(t) = -(400 / pi) sum_{k=1}^inf [1 / (2k - 1)] sin((2k - 1) pi t / L).
Paso 5: Tres primeros armónicos:
Fundamental (n = 1): b_1 = -400 / pi ≈ -127.32 V.
Tercer armónico (n = 3): b_3 = -400 / (3 pi) ≈ -42.44 V.
Quinto armónico (n = 5): b_5 = -400 / (5 pi) ≈ -25.46 V.

Problema 2: ¿Cuál es el valor medio de tensión de esta forma de onda?
Paso 1: V_dc = a_0 / 2 = 0 V (onda de corriente alterna sin componente continua).""",
        "bloque_sugerido": "Análisis Armónico 40 min • Descomposición de ondas de inversores PWM mediante series de Fourier"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Simetrías Par e Impar en Series de Fourier y Extensiones de Medio Rango",
        "objetivo": "Explotar simetrías par, impar y de media onda para simplificar el cálculo de coeficientes de Fourier y construir extensiones de medio rango.",
        "concepto_clave_latex": r"\text{Par: } b_n = 0 \implies f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos\left(\frac{n\pi t}{L}\right) \quad ; \quad \text{Impar: } a_n = 0 \implies f(t) = \sum_{n=1}^\infty b_n \sin\left(\frac{n\pi t}{L}\right)",
        "ejemplo": """Problema 1: Una onda triangular simétrica par de tensión rectificada v(t) = |t| para t en [-pi, pi] tiene período T = 2pi (L = pi). Halle su desarrollo en serie de cosenos de Fourier.
Paso 1: Por ser función par: b_n = 0.
Paso 2: a_0 = (2/pi) int_0^pi t dt = (2/pi) [ t^2 / 2 ]_0^pi = pi. (Valor constante = a_0 / 2 = pi/2).
Paso 3: a_n = (2/pi) int_0^pi t cos(nt) dt.
Integrando por partes con u = t, dv = cos(nt) dt:
a_n = (2/pi) [ t sin(nt)/n + cos(nt)/n^2 ]_0^pi = (2/pi) [ 0 + cos(n pi)/n^2 - 1/n^2 ] = (2 / (pi n^2)) [ (-1)^n - 1 ].
Paso 4: Para n par: (-1)^n - 1 = 0 => a_n = 0.
Para n impar: (-1)^n - 1 = -2 => a_n = -4 / (pi n^2).
Paso 5: v(t) = pi/2 - (4/pi) [ cos(t) + cos(3t)/9 + cos(5t)/25 + cos(7t)/49 + ... ].

Problema 2: Evaluando la serie en t = 0, deduzca la suma de la serie numérica de inversos de cuadrados impares: 1 + 1/9 + 1/25 + 1/49 + ...
Paso 1: v(0) = 0 = pi/2 - (4/pi) [ 1 + 1/9 + 1/25 + ... ].
Paso 2: (4/pi) sum_{k=0}^inf 1 / (2k + 1)^2 = pi/2.
Paso 3: sum_{k=0}^inf 1 / (2k + 1)^2 = (pi/2) × (pi/4) = pi^2 / 8 ≈ 1.2337. Q.E.D.""",
        "bloque_sugerido": "Taller Teórico 35 min • Identidades de Euler y simetría de media onda en rectificadores hexafásicos"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Forma Compleja de la Serie de Fourier y Espectro de Potencia Discreto",
        "objetivo": "Expresar señales periódicas en forma exponencial compleja y construir espectros discretos de magnitud y fase.",
        "concepto_clave_latex": r"f(t) = \sum_{n=-\infty}^\infty c_n e^{j n \omega_0 t} \quad ; \quad c_n = \frac{1}{T}\int_0^T f(t) e^{-j n \omega_0 t}\,dt \quad ; \quad |c_n|^2 = \frac{a_n^2 + b_n^2}{4}",
        "ejemplo": """Problema 1: Considere un tren de pulsos rectangulares periódicos de amplitud V_0 = 10 V, ancho de pulso tau = 2 ms y período T = 10 ms (f_0 = 100 Hz, omega_0 = 200 pi rad/s), centrado en t = 0 (t en [-tau/2, +tau/2]). Calcule los coeficientes complejos c_n.
Paso 1: c_n = (1/T) int_(-tau/2)^(+tau/2) V_0 e^(-j n omega_0 t) dt.
Paso 2: Integrando: c_n = (V_0 / T) [ e^(-j n omega_0 t) / (-j n omega_0) ]_(-tau/2)^(+tau/2) = (V_0 / (n omega_0 T)) [ (e^(j n omega_0 tau / 2) - e^(-j n omega_0 tau / 2)) / (2 j) ] × 2.
Paso 3: Reconociendo la función seno: c_n = (V_0 tau / T) [ sin(n omega_0 tau / 2) / (n omega_0 tau / 2) ] = (V_0 tau / T) sinc(n f_0 tau).
Paso 4: Factor de ciclo de trabajo D = tau / T = 2/10 = 0.20:
c_n = 10 × 0.20 × sinc(0.20 n) = 2.0 sinc(0.20 n) [V].
Paso 5: c_0 = 2.0 V (valor medio continuo).
c_1 = 2.0 sinc(0.20) = 2.0 [ sin(0.20 pi) / (0.20 pi) ] = 2.0 × [ 0.5878 / 0.6283 ] = 1.871 V.
c_5 = 2.0 sinc(1.0) = 0 V (cruce por cero del espectro).

Problema 2: Verifique la relación entre c_n y los coeficientes reales a_n y b_n para una función par.
Paso 1: Al ser par, b_n = 0 y c_n es puramente real: c_n = a_n / 2 para n >= 1.
Paso 2: a_1 = 2 c_1 = 2 × 1.871 = 3.742 V.""",
        "bloque_sugerido": "Espectros Digitales 35 min • FFT vs Serie Exponencial de Fourier en analizadores de redes"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Fenómeno de Gibbs, Distorsión Armónica Total (THD) y Teorema de Parseval",
        "objetivo": "Cuantificar el sobreimpulso del fenómeno de Gibbs en discontinuidades y calcular la Distorsión Armónica Total (THD) mediante el Teorema de Parseval.",
        "concepto_clave_latex": r"\text{Parseval: } \frac{1}{T}\int_0^T |f(t)|^2\,dt = \sum_{n=-\infty}^\infty |c_n|^2 = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^\infty (a_n^2 + b_n^2) \quad ; \quad \text{THD} = \frac{\sqrt{\sum_{n=2}^\infty V_n^2}}{V_1}",
        "ejemplo": """Problema 1: La tensión de salida de un inversor monofásico contiene un armónico fundamental V_1 = 230 V RMS, un tercer armónico V_3 = 46 V RMS, y un quinto armónico V_5 = 23 V RMS (con armónicos superiores despreciables). Calcule la tensión RMS total V_RMS aplicando el teorema de Parseval y determine la Distorsión Armónica Total de tensión (THD_V).
Paso 1: Por Parseval: V_RMS^2 = V_1^2 + V_3^2 + V_5^2 = 230^2 + 46^2 + 23^2 = 52,900 + 2,116 + 529 = 55,545 V^2.
Paso 2: Tensión RMS total: V_RMS = sqrt(55,545) = 235.68 V.
Paso 3: Tensión armónica cuadrática: V_harm = sqrt(V_3^2 + V_5^2) = sqrt(2,116 + 529) = sqrt(2,645) = 51.43 V.
Paso 4: THD_V = V_harm / V_1 = 51.43 / 230 = 0.2236 (22.36%).
Paso 5: Concluya según la norma IEEE 519 (límite THD_V < 5%): El inversor viola severamente el estándar y requiere filtrado pasivo LC o activo shunt.

Problema 2: En la aproximación de Fourier de una onda cuadrada, ¿cuál es el porcentaje de sobreimpulso persistente del Fenómeno de Gibbs en las discontinuidades al tender n -> inf?
Paso 1: El límite del sobreimpulso es (2/pi) int_0^pi (sin(t)/t) dt - 1 = (2/pi)(1.8519) - 1 = 1.17898 - 1 = 0.17898 ≈ 8.95% de la mitad del salto total (aprox. 17.9% del escalón total).
Paso 2: Este sobreimpulso no desaparece aumentando el número de armónicos; solo se confina a una vecindad infinitesimal de la discontinuidad.""",
        "bloque_sugerido": "Calidad de Energía 35 min • Medición de THD y factor de potencia de desplazamiento (DPF) bajo IEEE 519"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Integrales Dobles sobre Regiones Generales e Integrales Iteradas (Teorema de Fubini)",
        "objetivo": "Evaluar integrales dobles en regiones de Tipo I y Tipo II aplicando el Teorema de Fubini e intercambio del orden de integración.",
        "concepto_clave_latex": r"\iint_D f(x,y)\,dA = \int_a^b \left[\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\right]dx = \int_c^d \left[\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\right]dy",
        "ejemplo": """Problema 1: Evalúe la integral doble I = int_0^1 int_(x^2)^1 [ x^3 sin(y^3) ] dy dx invirtiendo el orden de integración, dado que la integral interna respecto a y no es elemental.
Paso 1: La región D está descrita como Tipo I: 0 <= x <= 1, x^2 <= y <= 1.
Paso 2: Fronteras: y = x^2 => x = sqrt(y); y = 1; x = 0.
Paso 3: Descripción como Tipo II: 0 <= y <= 1, 0 <= x <= sqrt(y).
Paso 4: Nueva integral iterada: I = int_0^1 int_0^(sqrt(y)) [ x^3 sin(y^3) ] dx dy.
Paso 5: Integral interna respecto a x:
int_0^(sqrt(y)) x^3 dx = [ x^4 / 4 ]_0^(sqrt(y)) = (sqrt(y))^4 / 4 = y^2 / 4.
Paso 6: Integral externa: I = int_0^1 [ (y^2 / 4) sin(y^3) ] dy.
Paso 7: Cambio de variable u = y^3, du = 3 y^2 dy => y^2 dy = du / 3:
I = (1/4)(1/3) int_0^1 sin(u) du = (1/12) [ -cos(u) ]_0^1 = (1/12) [ -cos(1) - (-cos(0)) ] = (1 - cos(1)) / 12.
Paso 8: Con cos(1 rad) ≈ 0.54030: I = (1 - 0.54030) / 12 = 0.45970 / 12 = 0.03831.

Problema 2: Calcule el volumen bajo la superficie z = x y sobre la región triangular con vértices (0,0), (1,0) y (1,2).
Paso 1: La recta que une (0,0) con (1,2) es y = 2x. Región: 0 <= x <= 1, 0 <= y <= 2x.
Paso 2: V = int_0^1 int_0^(2x) x y dy dx = int_0^1 x [ y^2 / 2 ]_0^(2x) dx = int_0^1 x [ 4x^2 / 2 ] dx = int_0^1 2 x^3 dx.
Paso 3: V = 2 [ x^4 / 4 ]_0^1 = 2/4 = 0.50 m³.""",
        "bloque_sugerido": "Cálculo Multivariable 35 min • Inversión de orden en integrales de flujo de densidad superficial"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Integrales Dobles en Coordenadas Polares y Momentos Polares de Inercia",
        "objetivo": "Transformar integrales cartesianas a polares mediante el factor de escala jacobiano r dr dtheta y calcular momentos polares de inercia en rotores.",
        "concepto_clave_latex": r"\iint_D f(x,y)\,dx\,dy = \iint_{D^*} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta \quad ; \quad J_z = \iint_D r^2 (\rho\,r\,dr\,d\theta) = \frac{\pi \rho R^4}{2} \quad [\text{kg}\cdot\text{m}^2]",
        "ejemplo": """Problema 1: Calcule la integral gaussiana bidimensional I = int_(-inf)^inf int_(-inf)^inf e^(-(x^2 + y^2)) dx dy convirtiéndola a coordenadas polares, y a partir de ella demuestre formalmente que int_0^inf e^(-x^2) dx = sqrt(pi) / 2.
Paso 1: En coordenadas polares: x^2 + y^2 = r^2, dA = r dr dtheta, con r en [0, inf) y theta en [0, 2pi].
Paso 2: I = int_0^(2pi) int_0^inf e^(-r^2) r dr dtheta = (int_0^(2pi) dtheta) (int_0^inf e^(-r^2) r dr).
Paso 3: Integral angular = 2pi.
Paso 4: Integral radial con u = r^2, du = 2r dr: int_0^inf (1/2) e^(-u) du = (1/2)[ -e^(-u) ]_0^inf = 1/2.
Paso 5: I = 2pi × (1/2) = pi.
Paso 6: Por Fubini, I = (int_(-inf)^inf e^(-x^2) dx)(int_(-inf)^inf e^(-y^2) dy) = J^2.
Luego J^2 = pi => J = int_(-inf)^inf e^(-x^2) dx = sqrt(pi).
Paso 7: Por simetría par: int_0^inf e^(-x^2) dx = J / 2 = sqrt(pi) / 2. Q.E.D.

Problema 2: Calcule el momento polar de inercia J_z de un disco circular plano homogéneo de radio R = 1.2 m, espesor t = 0.05 m y densidad de masa rho = 7,850 kg/m³ (acero).
Paso 1: Masa total M = rho pi R^2 t = 7850 × pi × (1.2)^2 × 0.05 = 7850 × pi × 1.44 × 0.05 = 1,775.5 kg.
Paso 2: Momento polar J_z = (1/2) M R^2 = (1/2)(1775.5)(1.2)^2 = 0.5 × 1775.5 × 1.44 = 1,278.36 kg·m².""",
        "bloque_sugerido": "Mecánica Rotacional 35 min • Momentos polares de inercia en volantes de inercia (flywheels)"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Integrales Triples en Coordenadas Cilíndricas y Esféricas: Masa y Potencial",
        "objetivo": "Calcular integrales volumétricas en coordenadas cilíndricas y esféricas para determinar masa, centros de masa y campos gravitatorios/electrostáticos.",
        "concepto_clave_latex": r"dV_{\text{cil}} = r\,dr\,d\theta\,dz \quad ; \quad dV_{\text{esf}} = \rho^2 \sin(\phi)\,d\rho\,d\phi\,d\theta \quad ; \quad M = \iiint_V \delta(x,y,z)\,dV",
        "ejemplo": """Problema 1: Un domo esférico semiesférico de gas a alta presión de radio R = 4 m tiene una densidad de masa espacial variable dada por delta(rho, phi, theta) = k / rho [kg/m³], donde k = 150 kg/m². Calcule la masa total M contenida en el hemisferio superior (0 <= rho <= R, 0 <= phi <= pi/2, 0 <= theta <= 2pi).
Paso 1: Elemento de volumen esférico: dV = rho^2 sin(phi) d rho d phi d theta.
Paso 2: Masa: M = int_0^(2pi) int_0^(pi/2) int_0^4 [ (k / rho) rho^2 sin(phi) ] d rho d phi d theta = k (int_0^(2pi) d theta) (int_0^(pi/2) sin(phi) d phi) (int_0^4 rho d rho).
Paso 3: Integral angular: int_0^(2pi) d theta = 2pi.
Paso 4: Integral colatitud: int_0^(pi/2) sin(phi) d phi = [ -cos(phi) ]_0^(pi/2) = -0 - (-1) = 1.
Paso 5: Integral radial: int_0^4 rho d rho = [ rho^2 / 2 ]_0^4 = 16 / 2 = 8.
Paso 6: Masa total M = 150 × 2pi × 1 × 8 = 2,400 pi ≈ 7,539.82 kg = 7.54 toneladas.

Problema 2: Un tanque de combustible cilíndrico está acotado por x^2 + y^2 = 9 (radio R = 3 m), por debajo por el plano z = 0 y por arriba por el paraboloide z = 18 - (x^2 + y^2). Calcule el volumen interior en coordenadas cilíndricas.
Paso 1: Región: 0 <= r <= 3, 0 <= theta <= 2pi, 0 <= z <= 18 - r^2.
Paso 2: V = int_0^(2pi) int_0^3 int_0^(18 - r^2) r dz dr dtheta = (2pi) int_0^3 r (18 - r^2) dr.
Paso 3: V = 2pi int_0^3 (18 r - r^3) dr = 2pi [ 9 r^2 - r^4 / 4 ]_0^3.
Paso 4: V = 2pi [ 9(9) - 81/4 ] = 2pi [ 81 - 20.25 ] = 2pi [ 60.75 ] = 121.5 pi ≈ 381.70 m³.""",
        "bloque_sugerido": "Cálculo Volumétrico 40 min • Jacobiano esférico y potencial newtoniano en cuerpos celestes y reactores"
    }
]

if __name__ == '__main__':
    yaml_text = format_topics_yaml(topics_02011808)
    inject_topics_after('      - codigo: "02021811"', yaml_text)
    print("02011808 Cálculo Integral now has 30 topics!")
