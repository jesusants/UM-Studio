import sys
from injector_base import inject_topics_after

topics_10_to_20 = """          - numero_tema: 10
            corte: 1
            modalidad: "tecnica"
            titulo: "Definición Formal de Límite (Épsilon-Delta) y Teorema del Emparedado"
            objetivo: "Demostrar rigurosamente la existencia de límites finitos mediante vecindades analíticas y acotación."
            concepto_clave_latex: "\\\\forall \\\\varepsilon > 0, \\\\; \\\\exists \\\\delta > 0 : 0 < |x - c| < \\\\delta \\\\implies |f(x) - L| < \\\\varepsilon"
            ejemplo: |
              CLASE MAGISTRAL: RIGOR DEL ANÁLISIS REAL Y TEOREMA DEL EMPAREDADO
              1. Fundamentos Teóricos y Formalización de Cauchy-Weierstrass:
              La definición intuitiva de límite presentaba inconsistencias analíticas. Cauchy y Weierstrass formalizaron el límite funcional: para cualquier tolerancia vertical epsilon > 0, debe existir una ventana delta > 0 tal que si la variable independiente dista de c menos de delta, la imagen dista de L menos de epsilon.
              2. Teorema de Compresión (Squeeze Theorem):
              Si g(x) <= f(x) <= h(x) en una vecindad de c y lim g(x) = lim h(x) = L, entonces lim f(x) existe y es L.
              3. Problema Resuelto 1 (Aplicación Directa):
              Demuestre mediante épsilon-delta que lim_{x -> 3} (4x - 5) = 7.
              Solución: Dado epsilon > 0, buscamos delta > 0 tal que 0 < |x - 3| < delta implique |(4x - 5) - 7| < epsilon.
              Simplificando: |4x - 12| = 4|x - 3| < epsilon, de donde |x - 3| < epsilon / 4.
              Elegimos delta = epsilon / 4. Si 0 < |x - 3| < delta, 4|x - 3| < 4*(epsilon/4) = epsilon. Q.E.D.
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Calcule lim_{x -> 0} x^4 * cos(2 / x^3) justificando por acotación.
              Solución: La función coseno está acotada: -1 <= cos(2/x^3) <= 1 para x != 0.
              Como x^4 > 0 para todo x != 0, multiplicamos: -x^4 <= x^4 * cos(2/x^3) <= x^4.
              Evaluando límites en las cotas: lim (-x^4) = 0 y lim (x^4) = 0.
              Por el Teorema del Emparedado, se concluye que lim_{x -> 0} x^4 * cos(2 / x^3) = 0.
            bloque_sugerido: "Pomodoro 50/10 • Demostraciones epsilon-delta y emparedado"
            slides:
              - numero: 1
                seccion: "FUNDAMENTOS"
                titulo: "Definición Épsilon-Delta"
                puntos:
                  - "Control estricto de la vecindad de salida mediante delta."
                  - "Eliminación de la ambigüedad intuitiva infinitesimal."
              - numero: 2
                seccion: "TEOREMA"
                titulo: "Teorema del Emparedado"
                puntos:
                  - "Acotación bidireccional g(x) <= f(x) <= h(x)."
                  - "Convergencia obligada de la función intermedia hacia L."
          - numero_tema: 11
            corte: 2
            modalidad: "tecnica"
            titulo: "Teorema de Rolle y Teorema del Valor Medio de Lagrange"
            objetivo: "Garantizar la existencia de puntos con derivada instantánea igual a la tasa promedio o nula."
            concepto_clave_latex: "f'(c) = \\\\frac{f(b) - f(a)}{b - a} \\\\quad ; \\\\quad c \\\\in (a, b)"
            ejemplo: |
              CLASE MAGISTRAL: TEOREMAS FUNDAMENTALES DEL CÁLCULO DIFERENCIAL
              1. Teorema de Rolle:
              Si f es continua en [a, b], diferenciable en (a, b) y f(a) = f(b), entonces existe al menos un c en (a, b) tal que f'(c) = 0.
              2. Teorema del Valor Medio de Lagrange:
              Si f es continua en [a, b] y diferenciable en (a, b), existe al menos un c en (a, b) tal que f'(c) = [f(b) - f(a)] / (b - a).
              3. Problema Resuelto 1 (Aplicación Directa):
              Verifique el TVM para f(x) = x^3 - x en [-1, 2] y halle c.
              Solución: f es polinómica (continua y diferenciable). f(-1) = 0, f(2) = 6.
              Pendiente secante: (6 - 0) / (2 - (-1)) = 6/3 = 2.
              Derivada: f'(x) = 3x^2 - 1. Igualando 3c^2 - 1 = 2 ==> 3c^2 = 3 ==> c = 1 (en (-1, 2)).
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Un móvil recorre 150 km en 1.5 h partiendo del reposo. Demuestre que en algún instante su rapidez instantánea fue exactamente 100 km/h.
              Solución: Por el TVM sobre la función posición continua s(t), existe t_0 en (0, 1.5) tal que v(t_0) = s'(t_0) = [s(1.5) - s(0)] / 1.5 = 150 / 1.5 = 100 km/h.
            bloque_sugerido: "Pomodoro 50/10 • Teorema del Valor Medio"
            slides:
              - numero: 1
                seccion: "TEORÍA"
                titulo: "Teorema de Rolle"
                puntos:
                  - "Continuidad en [a,b], diferenciabilidad en (a,b) y f(a)=f(b)."
                  - "Existencia garantizada de tangente horizontal f'(c) = 0."
              - numero: 2
                seccion: "TEOREMA"
                titulo: "Teorema de Lagrange"
                puntos:
                  - "Tangente paralela a la recta secante global."
                  - "Base matemática de los criterios de monotonía."
          - numero_tema: 12
            corte: 2
            modalidad: "tecnica"
            titulo: "Derivadas de Orden Superior, Concavidad y Puntos de Inflexión"
            objetivo: "Analizar la aceleración de cambio y la geometría de concavidad mediante la segunda derivada."
            concepto_clave_latex: "f''(x) > 0 \\\\implies \\\\text{Cóncava Arriba} \\\\quad ; \\\\quad f''(x_0) = 0 \\\\land \\\\Delta \\\\text{signo}(f'') \\\\implies \\\\text{Inflexión}"
            ejemplo: |
              CLASE MAGISTRAL: CONCAVIDAD E INFLEXIÓN
              1. Criterio de Concavidad:
              Si f''(x) > 0 en un intervalo, la curva es cóncava hacia arriba (la gráfica está sobre sus tangentes). Si f''(x) < 0, es cóncava hacia abajo.
              2. Puntos de Inflexión:
              Puntos donde la curva cambia de concavidad con continuidad garantizada. Condición necesaria: f''(x) = 0 o no existe.
              3. Problema Resuelto 1 (Aplicación Directa):
              Halle los intervalos de concavidad de f(x) = x^4 - 6x^2 + 5.
              Solución: f'(x) = 4x^3 - 12x, f''(x) = 12x^2 - 12 = 12(x - 1)(x + 1).
              Puntos críticos de f'': x = -1, x = 1.
              Concavidad hacia arriba en (-inf, -1) y (1, inf). Cóncava hacia abajo en (-1, 1). Puntos de inflexión en (-1, 0) y (1, 0).
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Demuestre que la curva f(x) = e^{-x^2 / 2} tiene puntos de inflexión en x = +-1.
              Solución: f'(x) = -x e^{-x^2/2}. f''(x) = (x^2 - 1)e^{-x^2/2}.
              Como la exponencial es estrictamente positiva, f''(x) = 0 solo en x = +-1, con cambio estricto de signo.
            bloque_sugerido: "Pomodoro 50/10 • Concavidad e inflexión"
            slides:
              - numero: 1
                seccion: "CRITERIO"
                titulo: "Concavidad y f''(x)"
                puntos:
                  - "f''(x) > 0: Tangentes por debajo de la curva."
                  - "f''(x) < 0: Tangentes por encima de la curva."
              - numero: 2
                seccion: "GEOMETRÍA"
                titulo: "Punto de Inflexión"
                puntos:
                  - "Cambio de signo en f''(x)."
                  - "Tangente que atraviesa la curva en el punto."
          - numero_tema: 13
            corte: 2
            modalidad: "tecnica"
            titulo: "Trazado Riguroso de Curvas: Asíntotas, Intervalos y Extremos"
            objetivo: "Sintetizar dominio, simetría, asíntotas, monotonía y concavidad para graficar funciones analíticas."
            concepto_clave_latex: "m = \\\\lim_{x \\\\to \\\\infty} \\\\frac{f(x)}{x} \\\\quad ; \\\\quad b = \\\\lim_{x \\\\to \\\\infty} [f(x) - mx]"
            ejemplo: |
              CLASE MAGISTRAL: ALGORITMO SISTEMÁTICO DE ANÁLISIS DE CURVAS
              1. Etapas Canónicas:
              Dominio, simetría (par/impar), asíntotas (verticales, horizontales, oblicuas), primera derivada (monotonía y extremos), segunda derivada (concavidad e inflexión).
              2. Problema Resuelto 1 (Aplicación Directa):
              Determine la asíntota oblicua de f(x) = (2x^2 + 3x - 1) / (x + 1).
              Solución: m = lim f(x)/x = 2. b = lim [f(x) - 2x] = lim (x - 1)/(x + 1) = 1.
              Asíntota oblicua: y = 2x + 1.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Bosqueje f(x) = x / (x^2 - 4) identificando extremos y asíntotas.
              Solución: Dominio: R - {-2, 2}. Impar. Asíntotas verticales en x = +-2, horizontal en y = 0.
              f'(x) = -(x^2 + 4) / (x^2 - 4)^2 < 0 en todo el dominio; estrictamente decreciente, sin extremos locales. Inflexión en (0, 0).
            bloque_sugerido: "Práctica 50 min • Bosquejo completo de curvas"
            slides:
              - numero: 1
                seccion: "METODOLOGÍA"
                titulo: "Algoritmo de Trazado"
                puntos:
                  - "1. Dominio y Simetría."
                  - "2. Asíntotas (H, V, Oblicua)."
                  - "3. Monotonía y Concavidad."
              - numero: 2
                seccion: "ASÍNTOTAS"
                titulo: "Asíntotas Oblicuas"
                puntos:
                  - "m = lim [f(x)/x]"
                  - "b = lim [f(x) - mx]"
          - numero_tema: 14
            corte: 2
            modalidad: "tecnica"
            titulo: "Diferenciales, Aproximación Lineal Local y Propagación de Errores"
            objetivo: "Calcular diferenciales totales y acotar el error propagado en mediciones experimentales."
            concepto_clave_latex: "L(x) = f(a) + f'(a)(x - a) \\\\quad ; \\\\quad dy = f'(x)dx"
            ejemplo: |
              CLASE MAGISTRAL: LINEARIZACIÓN Y ERROR PROPAGADO
              1. Aproximación Lineal:
              Cerca de x = a, f(x) se aproxima por su recta tangente L(x).
              2. Problema Resuelto 1 (Aplicación Directa):
              Aproxime sqrt{26} con a = 25.
              Solución: f(x) = sqrt{x}, f'(x) = 1/(2*sqrt{x}). L(x) = 5 + 0.1(x - 25). L(26) = 5.1.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Un cilindro tiene h = 10 m y r = 2.0 +- 0.02 m. Estime el error en el volumen.
              Solución: V = 10*pi*r^2. dV = 20*pi*r*dr = 20*pi*(2)(0.02) = 0.8*pi m^3 (aprox 2.51 m^3, 2%).
            bloque_sugerido: "Pomodoro 50/10 • Diferenciales y estimación de errores"
            slides:
              - numero: 1
                seccion: "LINEALIZACIÓN"
                titulo: "Aproximación Lineal"
                puntos:
                  - "L(x) = f(a) + f'(a)(x - a)"
                  - "Linealización local en un entorno pequeño."
              - numero: 2
                seccion: "INCERTIDUMBRE"
                titulo: "Propagación de Errores"
                puntos:
                  - "Error absoluto: dy = f'(x)dx."
                  - "Error relativo: dy / y = [f'(x)/f(x)] dx."
          - numero_tema: 15
            corte: 2
            modalidad: "tecnica"
            titulo: "Polinomios de Taylor y Maclaurin de Primer y Segundo Orden"
            objetivo: "Construir aproximaciones polinómicas acotando el residuo mediante la fórmula de Lagrange."
            concepto_clave_latex: "P_n(x) = \\\\sum_{k=0}^n \\\\frac{f^{(k)}(a)}{k!}(x - a)^k \\\\quad ; \\\\quad R_n(x) = \\\\frac{f^{(n+1)}(\\\\xi)}{(n+1)!}(x - a)^{n+1}"
            ejemplo: |
              CLASE MAGISTRAL: EXPANSIONES DE TAYLOR Y ANÁLISIS DE RESIDUO
              1. Polinomio Cuadrático de Taylor:
              P_2(x) = f(a) + f'(a)(x - a) + (1/2)f''(a)(x - a)^2.
              2. Problema Resuelto 1 (Aplicación Directa):
              Halle el polinomio de Maclaurin de orden 3 para e^{2x}.
              Solución: f(0)=1, f'(0)=2, f''(0)=4, f'''(0)=8. P_3(x) = 1 + 2x + 2x^2 + (4/3)x^3.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Aproxime cos(x) en a = pi/3 con orden 2 y acote el error en x = 35 grados.
              Solución: P_2(x) = 1/2 - (sqrt(3)/2)(x - pi/3) - (1/4)(x - pi/3)^2. |R_2| <= (1/6)|x - pi/3|^3 <= 0.0138.
            bloque_sugerido: "Práctica 45 min • Polinomios de Taylor y Maclaurin"
            slides:
              - numero: 1
                seccion: "EXPANSIÓN"
                titulo: "Polinomio de Taylor"
                puntos:
                  - "Aproximación polinómica de orden n."
                  - "Coeficientes dependientes de f^(k)(a)/k!."
              - numero: 2
                seccion: "ERROR"
                titulo: "Residuo de Lagrange"
                puntos:
                  - "Acotación formal del error de truncamiento."
                  - "R_n proporcional a (x - a)^(n+1)."
          - numero_tema: 16
            corte: 2
            modalidad: "tecnica"
            titulo: "Derivadas de Funciones Trigonométricas Inversas"
            objetivo: "Deducir y aplicar las derivadas de arcoseno, arcocoseno y arcotangente mediante derivación implícita."
            concepto_clave_latex: "\\\\frac{d}{dx}[\\\\arcsin(x)] = \\\\frac{1}{\\\\sqrt{1 - x^2}} \\\\quad ; \\\\quad \\\\frac{d}{dx}[\\\\arctan(x)] = \\\\frac{1}{1 + x^2}"
            ejemplo: |
              CLASE MAGISTRAL: DERIVACIÓN DE FUNCIONES TRIGONOMÉTRICAS INVERSAS
              1. Deducción Analítica por Derivación Implícita:
              Sea y = arcsin(x) en [-pi/2, pi/2]. Entonces sin(y) = x.
              Derivando implícitamente respecto a x: cos(y) * (dy/dx) = 1 ==> dy/dx = 1 / cos(y).
              Como cos(y) = sqrt(1 - sin^2(y)) = sqrt(1 - x^2) para y en (-pi/2, pi/2), se deduce que d/dx [arcsin(x)] = 1 / sqrt(1 - x^2).
              2. Problema Resuelto 1 (Aplicación Directa):
              Derive f(x) = arctan(3x^2).
              Solución: Por regla de la cadena: f'(x) = [1 / (1 + (3x^2)^2)] * d/dx[3x^2] = 6x / (1 + 9x^4).
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Calcule la recta tangente a y = arcsin(x/2) en el punto donde x = 1.
              Solución: y(1) = arcsin(1/2) = pi/6.
              y'(x) = [1 / sqrt(1 - (x/2)^2)] * (1/2) = 1 / [2*sqrt(1 - x^2/4)] = 1 / sqrt(4 - x^2).
              Pendiente: m = y'(1) = 1 / sqrt(4 - 1) = 1 / sqrt(3) = sqrt(3)/3.
              Ecuación: y - pi/6 = (sqrt(3)/3)(x - 1).
            bloque_sugerido: "Pomodoro 50/10 • Trigonométricas inversas"
            slides:
              - numero: 1
                seccion: "FÓRMULAS"
                titulo: "Derivadas Trigonométricas Inversas"
                puntos:
                  - "d/dx[arcsin x] = 1 / sqrt(1 - x^2)"
                  - "d/dx[arctan x] = 1 / (1 + x^2)"
              - numero: 2
                seccion: "CADENA"
                titulo: "Regla de la Cadena"
                puntos:
                  - "d/dx[arctan u] = u' / (1 + u^2)"
                  - "d/dx[arcsin u] = u' / sqrt(1 - u^2)"
          - numero_tema: 17
            corte: 2
            modalidad: "tecnica"
            titulo: "Derivadas de Funciones Hiperbólicas y sus Inversas"
            objetivo: "Analizar las propiedades diferenciales del seno hiperbólico, coseno hiperbólico y la catenaria."
            concepto_clave_latex: "\\\\frac{d}{dx}[\\\\sinh(x)] = \\\\cosh(x) \\\\quad ; \\\\quad \\\\frac{d}{dx}[\\\\cosh(x)] = \\\\sinh(x) \\\\quad ; \\\\quad \\\\cosh^2(x) - \\\\sinh^2(x) = 1"
            ejemplo: |
              CLASE MAGISTRAL: CÁLCULO CON FUNCIONES HIPERBÓLICAS
              1. Definiciones y Derivadas:
              sinh(x) = (e^x - e^{-x})/2, cosh(x) = (e^x + e^{-x})/2.
              d/dx[sinh x] = cosh x, d/dx[cosh x] = sinh x, d/dx[tanh x] = sech^2 x.
              2. La Catenaria en Ingeniería Eléctrica:
              La curva que adopta un cable de alta tensión suspendido entre dos torres obedece a y = a * cosh(x / a).
              3. Problema Resuelto 1 (Aplicación Directa):
              Derive f(x) = tanh(5x).
              Solución: f'(x) = sech^2(5x) * 5 = 5*sech^2(5x).
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Halle la pendiente de la catenaria y = 20*cosh(x / 20) en el punto x = 20.
              Solución: y'(x) = 20*sinh(x / 20)*(1/20) = sinh(x / 20).
              y'(20) = sinh(1) = (e - 1/e) / 2 aprox (2.71828 - 0.36788) / 2 = 1.1752.
            bloque_sugerido: "Pomodoro 50/10 • Funciones hiperbólicas y catenaria"
            slides:
              - numero: 1
                seccion: "DEFINICIÓN"
                titulo: "Funciones Hiperbólicas"
                puntos:
                  - "Combinaciones lineales de exponenciales e^x y e^{-x}."
                  - "cosh^2(x) - sinh^2(x) = 1."
              - numero: 2
                seccion: "DERIVADAS"
                titulo: "Reglas de Derivación"
                puntos:
                  - "d/dx [sinh x] = cosh x"
                  - "d/dx [cosh x] = sinh x"
          - numero_tema: 18
            corte: 2
            modalidad: "tecnica"
            titulo: "Formas Indeterminadas Exponenciales y Sustituciones Logarítmicas"
            objetivo: "Resolver indeterminaciones de tipos 0^0, 1^inf y inf^0 mediante logaritmo natural y la Regla de L'Hôpital."
            concepto_clave_latex: "L = \\\\lim_{x \\\\to a} [f(x)]^{g(x)} \\\\implies \\\\ln(L) = \\\\lim_{x \\\\to a} [g(x) \\\\ln f(x)]"
            ejemplo: |
              CLASE MAGISTRAL: INDETERMINACIONES EXPONENCIALES
              1. Transformación Logarítmica:
              Si y = [f(x)]^g(x), aplicamos ln(y) = g(x) * ln(f(x)). Convertimos el producto en cociente 0/0 o inf/inf y aplicamos L'Hôpital. Finalmente, L = e^{ln(L)}.
              2. Problema Resuelto 1 (Aplicación Directa):
              Calcule lim_{x -> 0^+} x^x (forma 0^0).
              Solución: Sea y = x^x ==> ln(y) = x * ln(x) = ln(x) / (1/x) (forma -inf/inf).
              Aplicando L'Hôpital: lim (1/x) / (-1/x^2) = lim (-x) = 0.
              Como ln(L) = 0, L = e^0 = 1.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Evalúe lim_{x -> inf} (1 + 3/x)^{2x} (forma 1^inf).
              Solución: ln(y) = 2x * ln(1 + 3/x) = [2 * ln(1 + 3/x)] / (1/x).
              L'Hôpital: numerador derivado: 2 * [1/(1 + 3/x)] * (-3/x^2) = -6 / [x^2(1 + 3/x)].
              Denominador derivado: -1/x^2.
              Cociente: [-6 / x^2(1 + 3/x)] / (-1/x^2) = 6 / (1 + 3/x).
              Cuando x -> inf, ln(L) = 6 / (1 + 0) = 6 ==> L = e^6.
            bloque_sugerido: "Pomodoro 50/10 • Formas indeterminadas exponenciales"
            slides:
              - numero: 1
                seccion: "MÉTODO"
                titulo: "Técnica Logarítmica"
                puntos:
                  - "Paso a logaritmos: ln(y) = g(x) ln(f(x))."
                  - "Conversión a cociente 0/0 o inf/inf."
              - numero: 2
                seccion: "EXPONENCIAL"
                titulo: "Recuperación del Límite"
                puntos:
                  - "Si ln(y) -> k, entonces y -> e^k."
                  - "Fundamental en interés compuesto y dinámica de poblaciones."
          - numero_tema: 19
            corte: 2
            modalidad: "tecnica"
            titulo: "Curvas Paramétricas y Derivadas de Primer y Segundo Orden"
            objetivo: "Determinar tangentes, concavidad y velocidad en curvas definidas paramétricamente x(t) e y(t)."
            concepto_clave_latex: "\\\\frac{dy}{dx} = \\\\frac{y'(t)}{x'(t)} \\\\quad ; \\\\quad \\\\frac{d^2y}{dx^2} = \\\\frac{\\\\frac{d}{dt}[dy/dx]}{x'(t)}"
            ejemplo: |
              CLASE MAGISTRAL: CÁLCULO EN CURVAS PARAMÉTRICAS
              1. Derivadas Paramétricas:
              Si x = f(t) e y = g(t), la pendiente de la recta tangente es dy/dx = g'(t) / f'(t) siempre que f'(t) != 0.
              La segunda derivada mide la concavidad: d^2y/dx^2 = (d/dt [dy/dx]) / (dx/dt).
              2. Problema Resuelto 1 (Aplicación Directa):
              Halle dy/dx para la cicloide x = 2(t - sin t), y = 2(1 - cos t) en t = pi/2.
              Solución: dx/dt = 2(1 - cos t), dy/dt = 2*sin(t).
              dy/dx = (2*sin t) / [2(1 - cos t)] = sin(t) / (1 - cos t).
              En t = pi/2: dy/dx = sin(pi/2) / (1 - cos(pi/2)) = 1 / (1 - 0) = 1.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Determine la concavidad de la curva x = t^2, y = t^3 - 3t en t = 1.
              Solución: dx/dt = 2t, dy/dt = 3t^2 - 3.
              dy/dx = (3t^2 - 3) / (2t) = (3/2)t - 3/(2t).
              d/dt [dy/dx] = 3/2 + 3/(2t^2).
              d^2y/dx^2 = [3/2 + 3/(2t^2)] / (2t).
              En t = 1: d^2y/dx^2 = (3/2 + 3/2) / 2 = 3 / 2 = 1.5 > 0 (Cóncava hacia arriba).
            bloque_sugerido: "Pomodoro 50/10 • Curvas paramétricas"
            slides:
              - numero: 1
                seccion: "PENDIENTE"
                titulo: "Derivada Paramétrica"
                puntos:
                  - "dy/dx = y'(t) / x'(t)."
                  - "Tangente vertical si x'(t) = 0 y y'(t) != 0."
              - numero: 2
                seccion: "CONCAVIDAD"
                titulo: "Segunda Derivada"
                puntos:
                  - "d^2y/dx^2 = (d/dt[dy/dx]) / x'(t)."
                  - "No es simplemente y''(t) / x''(t)."
          - numero_tema: 20
            corte: 2
            modalidad: "tecnica"
            titulo: "Ecuaciones Polares, Tangentes a Curvas Polares y Tasas Angulares"
            objetivo: "Calcular rectas tangentes en coordenadas polares r = f(theta) y analizar tasas de variación radial."
            concepto_clave_latex: "\\\\frac{dy}{dx} = \\\\frac{\\\\frac{dr}{d\\\\theta}\\\\sin\\\\theta + r\\\\cos\\\\theta}{\\\\frac{dr}{d\\\\theta}\\\\cos\\\\theta - r\\\\sin\\\\theta}"
            ejemplo: |
              CLASE MAGISTRAL: CÁLCULO DIFERENCIAL EN COORDENADAS POLARES
              1. Deducción de la Pendiente Polar:
              Con x = r(theta)*cos(theta) e y = r(theta)*sin(theta), tratamos a theta como parámetro y aplicamos la derivada paramétrica dy/dx = (dy/dtheta) / (dx/dtheta).
              2. Problema Resuelto 1 (Aplicación Directa):
              Halle la pendiente de la cardioide r = 1 + cos(theta) en theta = pi/2.
              Solución: r(pi/2) = 1. dr/dtheta = -sin(theta) ==> dr/dtheta(pi/2) = -1.
              dy/dx = [(-1)*sin(pi/2) + 1*cos(pi/2)] / [(-1)*cos(pi/2) - 1*sin(pi/2)]
              dy/dx = [(-1)(1) + 0] / [0 - 1(1)] = -1 / -1 = 1.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Encuentre los puntos de tangencia horizontal de la curva r = 2*sin(theta).
              Solución: r = 2*sin(theta) representa una circunferencia centrada en (0, 1) de radio 1.
              y = r*sin(theta) = 2*sin^2(theta).
              dy/dtheta = 4*sin(theta)*cos(theta) = 2*sin(2*theta) = 0 ==> 2*theta = 0, pi, 2*pi ==> theta = pi/2.
              En theta = pi/2: r = 2, punto coordenado (0, 2) en cartesiano.
            bloque_sugerido: "Práctica 45 min • Cálculo en coordenadas polares"
            slides:
              - numero: 1
                seccion: "TRANSFORMACIÓN"
                titulo: "Coordenadas Polares"
                puntos:
                  - "x = r cos(theta), y = r sin(theta)."
                  - "Pendiente cartesiana dependiente de r y dr/dtheta."
              - numero: 2
                seccion: "TANGENCIA"
                titulo: "Tangentes Horizontales y Verticales"
                puntos:
                  - "Horizontal: dy/dtheta = 0 con dx/dtheta != 0."
                  - "Vertical: dx/dtheta = 0 con dy/dtheta != 0."
"""

topics_21_to_30 = """          - numero_tema: 21
            corte: 3
            modalidad: "tecnica"
            titulo: "Optimización Global Multivariable Reducible y Teorema de Weierstrass"
            objetivo: "Resolver problemas de diseño ingenieril con restricciones cerradas garantizando extremos absolutos."
            concepto_clave_latex: "f(x^*) = \\\\max_{x \\\\in [a, b]} f(x) \\\\quad ; \\\\quad x^* \\\\in \\\\{a, b\\\\} \\\\cup \\\\{c : f'(c) = 0\\\\}"
            ejemplo: |
              CLASE MAGISTRAL: OPTIMIZACIÓN EN INTERVALOS CERRADOS
              1. Teorema del Valor Extremo (Weierstrass):
              Toda función continua en un intervalo cerrado y acotado [a, b] alcanza obligatoriamente un valor máximo absoluto y un valor mínimo absoluto.
              2. Problema Resuelto 1 (Aplicación Directa):
              Halle los extremos absolutos de f(x) = 2x^3 - 3x^2 - 12x + 1 en [-2, 3].
              Solución: f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x - 2)(x + 1) = 0 ==> x = -1, x = 2.
              Evaluando en puntos críticos y fronteras:
              f(-2) = -3; f(-1) = 8; f(2) = -19; f(3) = -8.
              Máximo absoluto: 8 en x = -1. Mínimo absoluto: -19 en x = 2.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Diseñe un contenedor cilíndrico cerrado de volumen fijo V_0 = 1 m^3 que minimice el área superficial total de material.
              Solución: V = pi * r^2 * h = 1 ==> h = 1 / (pi * r^2).
              Área: A(r) = 2*pi*r^2 + 2*pi*r*h = 2*pi*r^2 + 2 / r para r > 0.
              A'(r) = 4*pi*r - 2 / r^2 = 0 ==> 4*pi*r^3 = 2 ==> r = (1 / (2*pi))^(1/3) m.
              A''(r) = 4*pi + 4/r^3 > 0 (Mínimo estricto).
              h = 1 / (pi * r^2) = 2r. El cilindro óptimo tiene altura igual a su diámetro.
            bloque_sugerido: "Pomodoro 50/10 • Optimización con restricciones"
            slides:
              - numero: 1
                seccion: "TEOREMA"
                titulo: "Teorema de Weierstrass"
                puntos:
                  - "Continuidad en conjunto cerrado y acotado."
                  - "Garantía absoluta de existencia de máx y mín."
              - numero: 2
                seccion: "DISEÑO"
                titulo: "Optimización Geométrica"
                puntos:
                  - "Derivación con respecto a variable de decisión."
                  - "Comprobación de concavidad con segunda derivada."
          - numero_tema: 22
            corte: 3
            modalidad: "tecnica"
            titulo: "Método Numérico de Newton-Raphson y Convergencia Cuadrática"
            objetivo: "Implementar el algoritmo iterativo de Newton-Raphson para aproximar ceros de ecuaciones no lineales."
            concepto_clave_latex: "x_{n+1} = x_n - \\\\frac{f(x_n)}{f'(x_n)} \\\\quad ; \\\\quad |e_{n+1}| \\\\approx C |e_n|^2"
            ejemplo: |
              CLASE MAGISTRAL: MÉTODO DE NEWTON-RAPHSON
              1. Deducción Geométrica:
              Aproximamos la curva por la recta tangente en (x_n, f(x_n)): y - f(x_n) = f'(x_n)(x - x_n).
              Haciendo y = 0 para hallar la intersección con el eje x: 0 - f(x_n) = f'(x_n)(x_{n+1} - x_n) ==> x_{n+1} = x_n - f(x_n)/f'(x_n).
              2. Problema Resuelto 1 (Aplicación Directa):
              Aproxime la raíz de f(x) = x^3 - x - 1 partiendo de x_0 = 1.5 hasta dos iteraciones.
              Solución: f'(x) = 3x^2 - 1.
              Iteración 1: f(1.5) = 3.375 - 1.5 - 1 = 0.875. f'(1.5) = 3(2.25) - 1 = 5.75.
              x_1 = 1.5 - 0.875 / 5.75 = 1.5 - 0.15217 = 1.34783.
              Iteración 2: f(1.34783) = 0.10068; f'(1.34783) = 4.4498.
              x_2 = 1.34783 - 0.10068 / 4.4498 = 1.32520 (muy cercano a la raíz exacta 1.3247).
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Demuestre que la fórmula iterativa para calcular la raíz cuadrada 1/sqrt(A) sin divisiones es x_{n+1} = (x_n / 2)(3 - A*x_n^2).
              Solución: Sea f(x) = 1/x^2 - A = 0. f'(x) = -2/x^3.
              x_{n+1} = x_n - (1/x_n^2 - A) / (-2/x_n^3) = x_n + (x_n/2)(1 - A*x_n^2) = (x_n/2)(3 - A*x_n^2). Algoritmo clave en procesadores gráficos (Fast Inverse Square Root).
            bloque_sugerido: "Práctica 45 min • Algoritmo de Newton-Raphson"
            slides:
              - numero: 1
                seccion: "ALGORITMO"
                titulo: "Fórmula de Newton-Raphson"
                puntos:
                  - "x_{n+1} = x_n - f(x_n)/f'(x_n)."
                  - "Aproximación por recta tangente sucesiva."
              - numero: 2
                seccion: "CONVERGENCIA"
                titulo: "Orden Cuadrático"
                puntos:
                  - "Duplica dígitos de precisión por iteración."
                  - "Falla si f'(x_n) = 0 o punto de oscilación."
          - numero_tema: 23
            corte: 3
            modalidad: "tecnica"
            titulo: "Antiderivadas y Problemas de Valor Inicial (PVI) de Primer Orden"
            objetivo: "Reconstruir funciones de estado a partir de tasas de cambio instantáneas sujetas a condiciones iniciales."
            concepto_clave_latex: "\\\\frac{dy}{dt} = g(t), \\\\; y(t_0) = y_0 \\\\implies y(t) = y_0 + \\\\int_{t_0}^t g(\\\\tau) d\\\\tau"
            ejemplo: |
              CLASE MAGISTRAL: ANTIDERIVADAS Y CONDICIÓN INICIAL
              1. Familia de Primitivas:
              Si F'(x) = f(x), la antiderivada general es F(x) + C. La constante de integración se fija unívocamente mediante una condición de frontera y(x_0) = y_0.
              2. Problema Resuelto 1 (Aplicación Directa):
              Halle y(x) sabiendo que dy/dx = 6x^2 - 4x + 1 e y(1) = 5.
              Solución: y(x) = 2x^3 - 2x^2 + x + C.
              Sustituyendo y(1) = 2(1) - 2(1) + 1 + C = 1 + C = 5 ==> C = 4.
              Solución particular única: y(x) = 2x^3 - 2x^2 + x + 4.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              La corriente de carga de una batería es i(t) = 10*e^{-t / 120} A (t en segundos). Si en t = 0 la carga acumulada es Q(0) = 50 Coulombs, determine la carga Q(t) y la carga total asintótica.
              Solución: i(t) = dQ/dt ==> Q(t) = integral(10*e^{-t/120} dt) = -1200*e^{-t/120} + C.
              Q(0) = -1200 + C = 50 ==> C = 1250 C.
              Q(t) = 1250 - 1200*e^{-t/120} C.
              Carga máxima asintótica: lim_{t -> inf} Q(t) = 1250 Coulombs.
            bloque_sugerido: "Pomodoro 50/10 • Problemas de valor inicial"
            slides:
              - numero: 1
                seccion: "CONCEPTO"
                titulo: "Antiderivada General"
                puntos:
                  - "Operación inversa del operador diferencial."
                  - "Constante C representa traslación vertical."
              - numero: 2
                seccion: "PVI"
                titulo: "Condición Inicial"
                puntos:
                  - "Unicidad de la trayectoria física."
                  - "Determinación exacta del valor de C."
          - numero_tema: 24
            corte: 3
            modalidad: "tecnica"
            titulo: "Curvatura, Radio de Curvatura y Círculo Osculador en el Plano"
            objetivo: "Calcular la curvatura intrínseca de trayectorias mecánicas y perfiles de álabes aerodinámicos."
            concepto_clave_latex: "\\\\kappa = \\\\frac{|f''(x)|}{[1 + (f'(x))^2]^{3/2}} \\\\quad ; \\\\quad R = \\\\frac{1}{\\\\kappa}"
            ejemplo: |
              CLASE MAGISTRAL: CURVATURA Y GEOMETRÍA DIFERENCIAL PLANA
              1. Definición de Curvatura:
              La curvatura kappa cuantifica la rapidez de cambio de dirección del vector tangente unitario respecto a la longitud de arco s: kappa = |dT/ds|.
              2. Problema Resuelto 1 (Aplicación Directa):
              Calcule la curvatura de la parábola y = x^2 en el vértice (0, 0).
              Solución: y' = 2x ==> y'(0) = 0. y'' = 2.
              kappa(0) = |2| / [1 + 0^2]^{3/2} = 2.
              Radio de curvatura: R = 1 / kappa = 0.5 unidades. Círculo osculador centrado en (0, 0.5).
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Halle el radio de curvatura mínimo de la función y = ln(cos x) en (-pi/2, pi/2).
              Solución: y' = -tan(x), y'' = -sec^2(x).
              kappa(x) = sec^2(x) / [1 + tan^2(x)]^{3/2} = sec^2(x) / [sec^2(x)]^{3/2} = 1 / sec(x) = cos(x).
              La curvatura es máxima cuando cos(x) es máximo, en x = 0 (kappa = 1).
              El radio de curvatura mínimo es R = 1 / kappa_max = 1 / 1 = 1.
            bloque_sugerido: "Práctica 45 min • Curvatura y radio de curvatura"
            slides:
              - numero: 1
                seccion: "FÓRMULA"
                titulo: "Curvatura Plana"
                puntos:
                  - "kappa = |y''| / [1 + (y')^2]^(3/2)."
                  - "Magnitud invariante ante rotaciones."
              - numero: 2
                seccion: "APLICACIÓN"
                titulo: "Radio de Curvatura"
                puntos:
                  - "R = 1 / kappa."
                  - "Aceleración normal: a_n = v^2 / R."
          - numero_tema: 25
            corte: 3
            modalidad: "tecnica"
            titulo: "Cinemática Diferencial: Velocidad, Aceleración Instantánea y Tirón"
            objetivo: "Modelar el movimiento rectilíneo continuo mediante derivadas sucesivas de la posición temporal."
            concepto_clave_latex: "v(t) = \\\\frac{ds}{dt} \\\\quad ; \\\\quad a(t) = \\\\frac{d^2s}{dt^2} \\\\quad ; \\\\quad j(t) = \\\\frac{d^3s}{dt^3}"
            ejemplo: |
              CLASE MAGISTRAL: CINEMÁTICA Y DERIVADAS TEMPORALES
              1. Jerarquía Cinemática:
              - Posición s(t) [m].
              - Velocidad v(t) = s'(t) [m/s].
              - Aceleración a(t) = v'(t) = s''(t) [m/s^2].
              - Tirón (Jerk) j(t) = a'(t) = s'''(t) [m/s^3], crítico para el confort y desgaste de aerogeneradores y trenes.
              2. Problema Resuelto 1 (Aplicación Directa):
              La posición de un pistón es s(t) = 4*cos(10t) cm. Calcule velocidad y aceleración en t = 0.
              Solución: v(t) = -40*sin(10t) cm/s ==> v(0) = 0 cm/s.
              a(t) = -400*cos(10t) cm/s^2 ==> a(0) = -400 cm/s^2.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              Un perfil de leva se diseña para que el seguidor tenga s(t) = c*t^3(1 - t)^3 en [0, 1]. Halle el instante de aceleración máxima.
              Solución: Derivando sucesivamente y resolviendo s'''(t) = j(t) = 0, se obtienen los puntos críticos de aceleración garantizando suavidad dinámica.
            bloque_sugerido: "Pomodoro 50/10 • Cinemática diferencial y Jerk"
            slides:
              - numero: 1
                seccion: "DERIVADAS"
                titulo: "Derivadas del Movimiento"
                puntos:
                  - "v = ds/dt (tasa instantánea de posición)."
                  - "a = dv/dt (tasa instantánea de velocidad)."
              - numero: 2
                seccion: "DINÁMICA"
                titulo: "Tirón (Jerk)"
                puntos:
                  - "j = da/dt = d^3s/dt^3."
                  - "Impacto en resonancia y vida útil estructural."
          - numero_tema: 26
            corte: 3
            modalidad: "tecnica"
            titulo: "Análisis Marginal en Ingeniería: Costo Marginal y Elasticidad"
            objetivo: "Aplicar la derivada al análisis de sensibilidad económica, costos de producción y despacho energético."
            concepto_clave_latex: "C'(q) = \\\\frac{dC}{dq} \\\\quad ; \\\\quad \\\\varepsilon = \\\\frac{p}{q}\\\\frac{dq}{dp}"
            ejemplo: |
              CLASE MAGISTRAL: ANÁLISIS MARGINAL Y DECISIONES TÉCNICO-ECONÓMICAS
              1. Magnitudes Marginales:
              El costo marginal C'(q) aproxima el costo adicional de producir la unidad q+1. El ingreso marginal I'(q) y beneficio marginal B'(q) = I'(q) - C'(q) determinan el óptimo económico cuando B'(q) = 0.
              2. Problema Resuelto 1 (Aplicación Directa):
              Una planta termoeléctrica tiene costo C(P) = 500 + 30P + 0.05P^2 USD/h para una potencia P en MW. Halle el costo marginal para P = 100 MW.
              Solución: C'(P) = 30 + 0.10*P.
              Para P = 100 MW: C'(100) = 30 + 0.10(100) = 40 USD/MWh.
              3. Problema Resuelto 2 (Nivel Examen Parcial):
              La demanda de energía en una microrred sigue q(p) = 1000 - 20p. Calcule la elasticidad precio de la demanda para p = 25 USD y determine si la demanda es elástica o inelástica.
              Solución: dq/dp = -20. Para p = 25: q = 1000 - 20(25) = 500.
              Elasticidad: varepsilon = (p / q) * (dq/dp) = (25 / 500) * (-20) = -1.0.
              La demanda tiene elasticidad unitaria (|varepsilon| = 1), punto donde se maximiza el ingreso total I(p) = p*q(p).
            bloque_sugerido: "Práctica 45 min • Costo marginal y optimización económica"
            slides:
              - numero: 1
                seccion: "ECONOMÍA"
                titulo: "Costo Marginal"
                puntos:
                  - "C'(q) = dC/dq."
                  - "Base del despacho económico de generadores."
              - numero: 2
                seccion: "SENSIBILIDAD"
                titulo: "Elasticidad Precio"
                puntos:
                  - "varepsilon = (p/q) * (dq/dp)."
                  - "|varepsilon| > 1: Elástica; |varepsilon| < 1: Inelástica."
          - numero_tema: 27
            corte: 3
            modalidad: "tecnica"
            titulo: "Teorema Fundamental del Cálculo: Regla de Leibniz para Derivar Integrales"
            objetivo: "Derivar funciones acumuladas con límites de integración variables mediante la regla de Leibniz."
            concepto_clave_latex: "\\\\frac{d}{dx} \\\\left[ \\\\int_{u(x)}^{v(x)} f(t) dt \\\\right] = f(v(x))v'(x) - f(u(x))u'(x)"
            ejemplo: |
              CLASE MAGISTRAL: TFC PARTE 1 Y REGLA DE LEIBNIZ
              1. Teorema Fundamental del Cálculo (Parte 1):
              Si f es continua en [a, b], la función acumulación g(x) = integral_a^x f(t) dt es diferenciable y g'(x) = f(x).
              2. Regla General de Leibniz:
              Combinando el TFC con la regla de la cadena para límites superior v(x) e inferior u(x).
              3. Problema Resuelto 1 (Aplicación Directa):
              Halle la derivada de g(x) = integral_0^{x^2} sqrt{1 + t^3} dt.
              Solución: v(x) = x^2 ==> v'(x) = 2x. u(x) = 0 ==> u'(x) = 0.
              g'(x) = sqrt{1 + (x^2)^3} * (2x) = 2x * sqrt{1 + x^6}.
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Calcule la derivada de F(x) = integral_{2x}^{x^3} cos(t^2) dt.
              Solución: v(x) = x^3, v'(x) = 3x^2. u(x) = 2x, u'(x) = 2.
              F'(x) = cos((x^3)^2) * (3x^2) - cos((2x)^2) * (2) = 3x^2 * cos(x^6) - 2 * cos(4x^2).
            bloque_sugerido: "Pomodoro 50/10 • Regla de Leibniz y TFC"
            slides:
              - numero: 1
                seccion: "TEOREMA"
                titulo: "TFC Parte 1"
                puntos:
                  - "d/dx [integral_a^x f(t)dt] = f(x)."
                  - "La derivación y la integración son operaciones inversas."
              - numero: 2
                seccion: "REGLA"
                titulo: "Fórmula de Leibniz"
                puntos:
                  - "Límites variables u(x) y v(x)."
                  - "d/dx = f(v)v' - f(u)u'."
          - numero_tema: 28
            corte: 3
            modalidad: "tecnica"
            titulo: "Ecuaciones Diferenciales Ordinarias Separables y Familias Ortogonales"
            objetivo: "Resolver ecuaciones diferenciales de primer orden separando variables y encontrar trayectorias ortogonales."
            concepto_clave_latex: "g(y)dy = h(x)dx \\\\implies \\\\int g(y)dy = \\\\int h(x)dx + C \\\\quad ; \\\\quad m_1 m_2 = -1"
            ejemplo: |
              CLASE MAGISTRAL: EDO SEPARABLES Y TRAYECTORIAS ORTOGONALES
              1. EDO de Variables Separables:
              Toda ecuación de la forma dy/dx = h(x)/g(y) se desacopla algebraicamente como g(y)dy = h(x)dx e integrando ambos lados.
              2. Familias Ortogonales:
              Curvas que se intersecan en ángulo recto en todo punto común. Si la familia dada satisface dy/dx = f(x, y), la familia ortogonal satisface dy/dx = -1 / f(x, y). Fundamental en líneas de campo eléctrico y líneas equipotenciales.
              3. Problema Resuelto 1 (Aplicación Directa):
              Resuelva dy/dx = (x^2 + 1) / (2y) con y(0) = 2.
              Solución: 2y dy = (x^2 + 1) dx.
              y^2 = x^3/3 + x + C. Con y(0) = 2: 4 = C.
              Solución: y(x) = sqrt{x^3/3 + x + 4}.
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Encuentre las trayectorias ortogonales a la familia de hipérbolas x*y = k.
              Solución: Derivando x*y = k implícitamente: y + x*(dy/dx) = 0 ==> dy/dx = -y/x.
              La pendiente ortogonal es dy/dx = -1 / (-y/x) = x/y.
              Separando variables: y dy = x dx ==> y^2 / 2 = x^2 / 2 + C ==> y^2 - x^2 = C'.
              Las trayectorias ortogonales forman una familia conjugada de hipérbolas.
            bloque_sugerido: "Práctica 50 min • EDO separables y trayectorias ortogonales"
            slides:
              - numero: 1
                seccion: "SEPARACIÓN"
                titulo: "EDO Separables"
                puntos:
                  - "Desacoplo: g(y)dy = h(x)dx."
                  - "Integración directa de ambos miembros."
              - numero: 2
                seccion: "GEOMETRÍA"
                titulo: "Familias Ortogonales"
                puntos:
                  - "Pendiente recíproca negativa: -1 / f'(x)."
                  - "Líneas de flujo vs. líneas equipotenciales."
          - numero_tema: 29
            corte: 3
            modalidad: "tecnica"
            titulo: "Modelos Diferenciales de Enfriamiento y Ecuación Logística"
            objetivo: "Formular y resolver analíticamente la Ley de Enfriamiento de Newton y el crecimiento poblacional logístico."
            concepto_clave_latex: "\\\\frac{dT}{dt} = -k(T - T_\\\\infty) \\\\quad ; \\\\quad \\\\frac{dP}{dt} = rP\\\\left(1 - \\\\frac{P}{K}\\\\right)"
            ejemplo: |
              CLASE MAGISTRAL: MODELOS DIFERENCIALES CLÁSICOS DE INGENIERÍA
              1. Ley de Enfriamiento de Newton:
              La tasa de cambio de temperatura de un cuerpo es proporcional a la diferencia de temperatura entre el cuerpo y el medio ambiente circundante: dT/dt = -k(T - T_inf).
              Solución: T(t) = T_inf + (T_0 - T_inf)*e^{-kt}.
              2. Modelo Logístico de Verhulst:
              Introduce una capacidad de carga K que satura el crecimiento malthusiano.
              3. Problema Resuelto 1 (Aplicación Directa):
              Un transformador a 90 °C se apaga en una sala a 25 °C. Tras 20 min su temperatura es de 65 °C. ¿En cuánto tiempo alcanzará 35 °C?
              Solución: T_inf = 25, T_0 = 90. T(t) = 25 + 65*e^{-kt}.
              Para t = 20: 65 = 25 + 65*e^{-20k} ==> 40/65 = e^{-20k} ==> k = -ln(40/65) / 20 aprox 0.02427 min^{-1}.
              Buscamos t para T = 35: 35 = 25 + 65*e^{-kt} ==> 10/65 = e^{-kt}.
              t = -ln(10/65) / k = ln(6.5) / 0.02427 aprox 1.8718 / 0.02427 = 77.1 minutos.
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Halle los puntos de equilibrio de la ecuación logística dP/dt = 0.05P(1 - P/500) y determine su estabilidad mediante el signo de la derivada.
              Solución: Puntos de equilibrio: P = 0 y P = 500.
              Si 0 < P < 500, dP/dt > 0 (P crece hacia 500). Si P > 500, dP/dt < 0 (P decrece hacia 500).
              Por tanto, P = 500 es un punto de equilibrio asintóticamente estable (capacidad de carga), y P = 0 es inestable.
            bloque_sugerido: "Pomodoro 50/10 • Ley de enfriamiento y ecuación logística"
            slides:
              - numero: 1
                seccion: "TÉRMICA"
                titulo: "Enfriamiento de Newton"
                puntos:
                  - "dT/dt = -k(T - T_inf)."
                  - "Decaimiento exponencial de la diferencia térmica."
              - numero: 2
                seccion: "LOGÍSTICA"
                titulo: "Ecuación de Verhulst"
                puntos:
                  - "dP/dt = rP(1 - P/K)."
                  - "Capacidad de carga K como atractor estable."
          - numero_tema: 30
            corte: 3
            modalidad: "tecnica"
            titulo: "Optimización Avanzada de Sistemas Energéticos y Transferencia de Calor"
            objetivo: "Sintetizar el cálculo diferencial para optimizar el rendimiento y aislamientos en ingeniería térmica."
            concepto_clave_latex: "r_{\\\\text{crítico}} = \\\\frac{k_{\\\\text{aislante}}}{h_{\\\\text{convección}}} \\\\quad ; \\\\quad \\\\frac{dq}{dr} = 0"
            ejemplo: |
              CLASE MAGISTRAL: RADIO CRÍTICO DE AISLAMIENTO Y OPTIMIZACIÓN ENERGÉTICA
              1. Paradoja del Radio Crítico en Tuberías Cilíndricas:
              Al añadir aislamiento a un tubo cilíndrico, la resistencia conductiva aumenta (R_cond = ln(r/r_1)/(2*pi*k*L)), pero el área superficial externa aumenta reduciendo la resistencia convectiva (R_conv = 1/(2*pi*r*h*L)).
              La resistencia térmica total es R_total(r) = ln(r/r_1)/(2*pi*k*L) + 1/(2*pi*r*h*L).
              2. Deducción del Radio Crítico:
              Para maximizar la transferencia de calor (o determinar el punto de inflexión donde aislar realmente ahorra energía), derivamos respecto a r:
              dR_total / dr = 1 / (2*pi*k*L*r) - 1 / (2*pi*h*L*r^2) = 0.
              Multiplicando por 2*pi*L*r^2: r / k - 1 / h = 0 ==> r_crítico = k / h.
              3. Problema Resuelto 1 (Aplicación Directa):
              Un cable eléctrico conductor de radio r_1 = 3 mm disipa calor hacia el aire con h = 10 W/(m^2*K). Si se recubre con aislante de k = 0.15 W/(m*K), calcule el radio crítico.
              Solución: r_crítico = k / h = 0.15 / 10 = 0.015 m = 15 mm.
              Como r_1 = 3 mm < r_crítico = 15 mm, agregar aislante hasta 15 mm aumenta la disipación térmica (beneficioso para evitar sobrecalentamiento del conductor eléctrico).
              4. Problema Resuelto 2 (Nivel Examen Parcial):
              Demuestre que para una esfera hueca con convección externa, el radio crítico de aislamiento es r_crítico = 2k / h.
              Solución: Resistencia total esférica: R(r) = (1/r_1 - 1/r)/(4*pi*k) + 1/(4*pi*r^2*h).
              Derivando respecto a r: dR/dr = 1/(4*pi*k*r^2) - 2/(4*pi*h*r^3) = 0.
              Simplificando: 1 / k - 2 / (h*r) = 0 ==> r_crítico = 2k / h. Q.E.D.
            bloque_sugerido: "Práctica 50 min • Radio crítico de aislamiento y optimización"
            slides:
              - numero: 1
                seccion: "FENÓMENO"
                titulo: "Radio Crítico de Aislamiento"
                puntos:
                  - "Compromiso entre conducción interna y convección externa."
                  - "r_crítico = k / h (cilindro); r_crítico = 2k / h (esfera)."
              - numero: 2
                seccion: "CRITERIO"
                titulo: "Estrategia de Diseño"
                puntos:
                  - "r < r_crítico: aislar aumenta la disipación (cables eléctricos)."
                  - "r > r_crítico: aislar reduce la disipación (tuberías de vapor)."
"""

if __name__ == '__main__':
    target = '      - codigo: "03011813"'
    inject_topics_after(target, topics_10_to_20 + topics_21_to_30)
    print("02011807 Cálculo Diferencial now has 30 topics!")
