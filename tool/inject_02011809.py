# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_02011809 = [
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Descomposición en Valores Singulares (SVD) y Pseudoinversa de Moore-Penrose",
        "objetivo": "Dominar la descomposición SVD $A = U \\Sigma V^T$ y el cálculo de la pseudoinversa de Moore-Penrose $A^+$ para la resolución óptima de sistemas lineales sobredeterminados e indeterminados.",
        "concepto_clave_latex": r"A = U \Sigma V^T = \sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^T \quad ; \quad A^+ = V \Sigma^+ U^T \quad [\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0]",
        "ejemplo": "Problema 1: Dada la matriz $A = \\begin{pmatrix} 3 & 0 \\\\ 0 & -2 \\end{pmatrix}$, hallar sus valores singulares y pseudoinversa. Calculamos $A^T A = \\begin{pmatrix} 9 & 0 \\\\ 0 & 4 \\end{pmatrix}$, con autovalores $\\lambda_1 = 9, \\lambda_2 = 4$, por lo que $\\sigma_1 = 3, \\sigma_2 = 2$. Así $U = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}, V = I$, y $A^+ = \\begin{pmatrix} 1/3 & 0 \\\\ 0 & -1/2 \\end{pmatrix}$. Problema 2: En un sistema de estimación de estado $A\\mathbf{x} = \\mathbf{b}$ con rango deficiente, la solución de norma euclidiana mínima única es $\\hat{\\mathbf{x}} = A^+ \\mathbf{b}$.",
        "bloque_sugerido": "Taller SVD 45 min • Factorización singular y pseudoinversa en MATLAB/Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "FUNDAMENTOS MATRICIALES",
                "titulo": "Estructura Geométrica de la SVD",
                "puntos": [
                    "Toda matriz real $A \\in \\mathbb{R}^{m \\times n}$ mapea esferas unitarias de $\\mathbb{R}^n$ en hiperelipsoides en $\\mathbb{R}^m$.",
                    "Las columnas de $V$ son autovectores ortonormales de $A^T A$, mientras que las columnas de $U$ lo son de $A A^T$.",
                    "Los valores singulares $\\sigma_i = \\sqrt{\\lambda_i(A^T A)}$ representan las longitudes de los semiejes del elipsoide resultante."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPTIMIZACIÓN Y PSEUDOINVERSA",
                "titulo": "Propiedades de Moore-Penrose",
                "puntos": [
                    "La matriz pseudoinversa satisface las 4 condiciones de Penrose: $A A^+ A = A$, $A^+ A A^+ = A^+$, $(AA^+)^T = AA^+$, $(A^+ A)^T = A^+ A$.",
                    "Permite comprimir datos y matrices de impedancia reteniendo los $k$ valores singulares dominantes (Teorema de Eckart-Young-Mirsky).",
                    "Garantiza soluciones estables incluso cuando $\\det(A^T A) \\approx 0$ mediante truncamiento de valores singulares (TSVD)."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Teorema de Cayley-Hamilton y Cálculo de Funciones Matriciales",
        "objetivo": "Aplicar el Teorema de Cayley-Hamilton para expresar polinomios y potencias de matrices $A^k$ en función de potencias de orden menor que $n$, simplificando la evaluación de operadores dinámicos.",
        "concepto_clave_latex": r"p(\lambda) = \det(\lambda I - A) = 0 \implies p(A) = A^n + c_{n-1}A^{n-1} + \dots + c_1 A + c_0 I = \mathbf{0}",
        "ejemplo": "Problema 1: Sea $A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$. El polinomio característico es $p(\\lambda) = \\lambda^2 - 5\\lambda - 2$. Por Cayley-Hamilton: $A^2 - 5A - 2I = 0 \\implies A^2 = 5A + 2I$. Hallar $A^3$: $A^3 = 5A^2 + 2A = 5(5A + 2I) + 2A = 27A + 10I = \\begin{pmatrix} 37 & 54 \\\\ 81 & 118 \\end{pmatrix}$. Problema 2: Inversa mediante Cayley-Hamilton: $A(A - 5I) = 2I \\implies A^{-1} = \\frac{1}{2}(A - 5I) = \\frac{1}{2}\\begin{pmatrix} -4 & 2 \\\\ 3 & -1 \\end{pmatrix} = \\begin{pmatrix} -2 & 1 \\\\ 1.5 & -0.5 \\end{pmatrix}$.",
        "bloque_sugerido": "Cálculo Simbólico 40 min • Potencias matriciales y verificación con Cayley-Hamilton",
        "slides": [
            {
                "numero": 1,
                "seccion": "TEOREMA FUNDAMENTAL",
                "titulo": "Anulación del Polinomio Característico",
                "puntos": [
                    "Toda matriz cuadrada satisface su propia ecuación característica: $p(A) = 0$.",
                    "Cualquier potencia arbitraria $A^m$ ($m \\ge n$) puede reducirse exactamente a un polinomio de grado a lo sumo $n-1$: $A^m = \\sum_{j=0}^{n-1} \\alpha_j A^j$.",
                    "Los coeficientes $\\alpha_j$ se determinan evaluando la relación en los $n$ autovalores $\\lambda_i$ de $A$."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIONES DINÁMICAS",
                "titulo": "Inversas y Series de Operadores",
                "puntos": [
                    "Si $c_0 = (-1)^n \\det(A) \\ne 0$, la matriz es invertible y $A^{-1} = -\\frac{1}{c_0}(A^{n-1} + c_{n-1}A^{n-2} + \\dots + c_1 I)$.",
                    "Base conceptual para el algoritmo de Faddeev-LeVerrier en control y dinámica de redes eléctricas.",
                    "Evita el cálculo directo de determinantes gigantes de orden superior."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Exponencial de Matrices y Sistemas Dinámicos Lineales Continuos",
        "objetivo": "Calcular la matriz de transición de estados $e^{At}$ mediante serie infinita, diagonalización y transformada de Laplace para resolver sistemas diferenciales $\\dot{\\mathbf{x}} = A\\mathbf{x}$.",
        "concepto_clave_latex": r"e^{At} = \sum_{k=0}^\infty \frac{(At)^k}{k!} = P e^{Dt} P^{-1} \quad ; \quad \mathbf{x}(t) = e^{At} \mathbf{x}(0) + \int_0^t e^{A(t-\tau)} \mathbf{B}\mathbf{u}(\tau) d\tau",
        "ejemplo": "Problema 1: Hallar $e^{At}$ para $A = \\begin{pmatrix} 0 & 1 \\\\ -2 & -3 \\end{pmatrix}$. Autovalores: $\\det(\\lambda I - A) = \\lambda^2 + 3\\lambda + 2 = 0 \\implies \\lambda_1 = -1, \\lambda_2 = -2$. Autovectores: $\\mathbf{v}_1 = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}, \\mathbf{v}_2 = \\begin{pmatrix} 1 \\\\ -2 \\end{pmatrix}$. Matriz modal $P = \\begin{pmatrix} 1 & 1 \\\\ -1 & -2 \\end{pmatrix}, P^{-1} = \\begin{pmatrix} 2 & 1 \\\\ -1 & -1 \\end{pmatrix}$. Luego $e^{At} = P \\begin{pmatrix} e^{-t} & 0 \\\\ 0 & e^{-2t} \\end{pmatrix} P^{-1} = \\begin{pmatrix} 2e^{-t}-e^{-2t} & e^{-t}-e^{-2t} \\\\ -2e^{-t}+2e^{-2t} & -e^{-t}+2e^{-2t} \\end{pmatrix}$. Problema 2: Con $\\mathbf{x}(0) = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$, la trayectoria temporal homogénea es $\\mathbf{x}(t) = \\begin{pmatrix} 2e^{-t}-e^{-2t} \\\\ -2e^{-t}+2e^{-2t} \\end{pmatrix}$.",
        "bloque_sugerido": "Simulación Dinámica 45 min • Trayectorias en espacio de estado y diagramas de fase",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESPACIO DE ESTADOS",
                "titulo": "La Matriz Fundamental de Transición",
                "puntos": [
                    "La ecuación diferencial vectorial $\\dot{\\mathbf{x}} = A\\mathbf{x}$ gobierna transitorios en circuitos RLC y oscilaciones de rotores en generadores sincrónicos.",
                    "La serie de Taylor converge absolutamente para cualquier matriz $A$ y todo tiempo $t \\in \\mathbb{R}$.",
                    "Propiedades esenciales: $e^{A(t_1+t_2)} = e^{At_1} e^{At_2}$, $(e^{At})^{-1} = e^{-At}$, y $\\frac{d}{dt} e^{At} = A e^{At} = e^{At} A$."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTABILIDAD ASINTÓTICA",
                "titulo": "Criterio Espectral de Lyapunov",
                "puntos": [
                    "El sistema es asintóticamente estable si y solo si todos los autovalores de $A$ tienen parte real estrictamente negativa: $\\text{Re}(\\lambda_i) < 0$.",
                    "Autovalores imaginarios puros $\\pm j\\omega$ representan modos oscilatorios no amortiguados continuos.",
                    "La fórmula de variación de parámetros evalúa respuestas ante entradas forzadas de control $\\mathbf{u}(t)$."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Los Cuatro Subespacios Fundamentales de Strang y Dualidad Ortogonal",
        "objetivo": "Comprender la estructura geométrica integral del Teorema Fundamental del Álgebra Lineal: espacio columna, espacio nulo, espacio fila y espacio nulo izquierdo.",
        "concepto_clave_latex": r"\mathcal{C}(A) \perp \mathcal{N}(A^T) \quad [\mathbb{R}^m = \mathcal{C}(A) \oplus \mathcal{N}(A^T)] \quad ; \quad \mathcal{C}(A^T) \perp \mathcal{N}(A) \quad [\mathbb{R}^n = \mathcal{C}(A^T) \oplus \mathcal{N}(A)]",
        "ejemplo": "Problema 1: Sea $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 4 & 6 \\end{pmatrix}$. Hallar bases para los 4 subespacios. Rango $r = 1$. $\\mathcal{C}(A) = \\text{span}\\left\\{\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}\\right\\}$ (dim 1). $\\mathcal{C}(A^T) = \\text{span}\\left\\{\\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}\\right\\}$ (dim 1). Para $\\mathcal{N}(A)$, $x_1 + 2x_2 + 3x_3 = 0 \\implies$ base $\\left\\{\\begin{pmatrix} -2 \\\\ 1 \\\\ 0 \\end{pmatrix}, \\begin{pmatrix} -3 \\\\ 0 \\\\ 1 \\end{pmatrix}\\right\\}$ (dim $3-1=2$). Para $\\mathcal{N}(A^T)$, base $\\left\\{\\begin{pmatrix} -2 \\\\ 1 \\end{pmatrix}\\right\\}$ (dim $2-1=1$). Problema 2: Comprobar ortogonalidad: $\\begin{pmatrix} -2 & 1 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = -2(1) + 1(2) = 0$.",
        "bloque_sugerido": "Visualización 40 min • Diagrama maestro de los cuatro subespacios de Gilbert Strang",
        "slides": [
            {
                "numero": 1,
                "seccion": "GEOMETRÍA VECTORIAL",
                "titulo": "Ortogonalidad y Complementos Directos",
                "puntos": [
                    "Toda transformación matricial descompone el dominio $\\mathbb{R}^n$ en el espacio fila $\\mathcal{C}(A^T)$ y su complemento ortogonal $\\mathcal{N}(A)$.",
                    "El codominio $\\mathbb{R}^m$ se descompone en el espacio columna $\\mathcal{C}(A)$ y el espacio nulo izquierdo $\\mathcal{N}(A^T)$.",
                    "Teorema del Rango: $\\dim(\\mathcal{C}(A)) = \\dim(\\mathcal{C}(A^T)) = r$, $\\dim(\\mathcal{N}(A)) = n - r$, $\\dim(\\mathcal{N}(A^T)) = m - r$."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIÓN EN CIRCUITOS",
                "titulo": "Leyes de Kirchhoff Topológicas",
                "puntos": [
                    "En una red eléctrica modelada por su matriz de incidencia nodo-rama $A$, el espacio nulo $\\mathcal{N}(A)$ define las corrientes de lazo válidas (LVK).",
                    "El espacio columna $\\mathcal{C}(A^T)$ modela las tensiones de rama a partir de los potenciales nodales.",
                    "El teorema de Tellegen es una consecuencia directa de la ortogonalidad entre $\\mathcal{C}(A^T)$ y $\\mathcal{N}(A)$."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Espacios con Producto Interno Generalizado, Normas Inducidas y Cauchy-Schwarz",
        "objetivo": "Generalizar el concepto de producto interno a través de matrices de ponderación definidas positivas y espacios funcionales, evaluando ángulos y distancias en sistemas energéticos.",
        "concepto_clave_latex": r"\langle \mathbf{u}, \mathbf{v} \rangle_W = \mathbf{u}^T W \mathbf{v} \quad [W = W^T > 0] \quad ; \quad |\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\| \quad ; \quad \cos \theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \|\mathbf{v}\|}",
        "ejemplo": "Problema 1: Sean $\\mathbf{u} = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}, \\mathbf{v} = \\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix}$ y la matriz de ponderación $W = \\begin{pmatrix} 2 & 1 \\\\ 1 & 4 \\end{pmatrix}$. Calcular $\\langle \\mathbf{u}, \\mathbf{v} \\rangle_W$. Producto: $\\mathbf{u}^T W = \\begin{pmatrix} 1 & 2 \\end{pmatrix} \\begin{pmatrix} 2 & 1 \\\\ 1 & 4 \\end{pmatrix} = \\begin{pmatrix} 4 & 9 \\end{pmatrix}$. Luego $\\begin{pmatrix} 4 & 9 \\end{pmatrix} \\begin{pmatrix} 3 \\\\ -1 \\end{pmatrix} = 12 - 9 = 3$. Problema 2: Hallar $\|\mathbf{u}\|_W$: $\\mathbf{u}^T W \\mathbf{u} = \\begin{pmatrix} 4 & 9 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = 4 + 18 = 22 \\implies \\|\\mathbf{u}\\|_W = \\sqrt{22} \\approx 4.69$.",
        "bloque_sugerido": "Taller Analítico 35 min • Métricas ponderadas en filtrado de Kalman y mínimos cuadrados pesados",
        "slides": [
            {
                "numero": 1,
                "seccion": "AXIOMÁTICA VECTORIAL",
                "titulo": "Propiedades del Producto Interno",
                "puntos": [
                    "Linealidad en el primer argumento: $\\langle \\alpha \\mathbf{u} + \\beta \\mathbf{w}, \\mathbf{v} \\rangle = \\alpha \\langle \\mathbf{u}, \\mathbf{v} \\rangle + \\beta \\langle \\mathbf{w}, \\mathbf{v} \\rangle$.",
                    "Simetría (o simetría conjugada en complejos): $\\langle \\mathbf{u}, \\mathbf{v} \\rangle = \\langle \\mathbf{v}, \\mathbf{u} \\rangle$.",
                    "Positividad estricta: $\\langle \\mathbf{u}, \\mathbf{u} \\rangle > 0$ para todo $\\mathbf{u} \\ne \\mathbf{0}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "INGENIERÍA ENERGÉTICA",
                "titulo": "Energía y Métricas Ponderadas",
                "puntos": [
                    "La energía electrostática $U = \\frac{1}{2}\\mathbf{v}^T C \\mathbf{v}$ define una norma inducida por la matriz de capacitancias de nodo.",
                    "En estimación de estado de redes de potencia (WLS), la matriz de ponderación $W = R^{-1}$ corresponde a la inversa de la matriz de covarianzas de ruido de los medidores.",
                    "La desigualdad de Cauchy-Schwarz impone cotas teóricas estrictas sobre correlaciones cruzadas en señales de voltaje y corriente."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Factorización de Cholesky para Matrices Definidas Positivas",
        "objetivo": "Descomponer matrices simétricas definidas positivas en la forma $A = L L^T$ para acelerar la resolución numérica de ecuaciones normales y flujos de carga.",
        "concepto_clave_latex": r"A = L L^T \quad [L \text{ triangular inferior con } l_{ii} > 0] \quad ; \quad l_{jj} = \sqrt{a_{jj} - \sum_{k=1}^{j-1} l_{jk}^2}",
        "ejemplo": "Problema 1: Factorizar $A = \\begin{pmatrix} 4 & 12 \\\\ 12 & 45 \\end{pmatrix}$. $l_{11} = \\sqrt{4} = 2$. $l_{21} = \\frac{12}{2} = 6$. $l_{22} = \\sqrt{45 - 6^2} = \\sqrt{9} = 3$. Por tanto $L = \\begin{pmatrix} 2 & 0 \\\\ 6 & 3 \\end{pmatrix}$. Verificación: $L L^T = \\begin{pmatrix} 2 & 0 \\\\ 6 & 3 \\end{pmatrix} \\begin{pmatrix} 2 & 6 \\\\ 0 & 3 \\end{pmatrix} = \\begin{pmatrix} 4 & 12 \\\\ 12 & 45 \\end{pmatrix}$. Problema 2: Resolver $A\\mathbf{x} = \\begin{pmatrix} 16 \\\\ 57 \\end{pmatrix}$. Sustitución progresiva en $L\\mathbf{y} = \\mathbf{b}$: $2y_1 = 16 \\implies y_1 = 8$; $6(8) + 3y_2 = 57 \\implies 3y_2 = 9 \\implies y_2 = 3$. Sustitución regresiva en $L^T\\mathbf{x} = \\mathbf{y}$: $3x_2 = 3 \\implies x_2 = 1$; $2x_1 + 6(1) = 8 \\implies 2x_1 = 2 \\implies x_1 = 1$. Solución $\\mathbf{x} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.",
        "bloque_sugerido": "Laboratorio Numérico 40 min • Eficiencia de Cholesky vs Eliminación Gaussiana estándar",
        "slides": [
            {
                "numero": 1,
                "seccion": "COMPLEJIDAD COMPUTACIONAL",
                "titulo": "Ventajas Algorítmicas de Cholesky",
                "puntos": [
                    "Requiere aproximadamente $\\frac{1}{3} n^3$ operaciones de coma flotante, la mitad de operaciones que la factorización LU general.",
                    "Es numéricamente incondicionalmente estable: no requiere pivoteo parcial ni intercambio de filas.",
                    "Si un elemento diagonal resulta negativo o cero durante el proceso, la matriz no es definida positiva."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIÓN EN SIMULACIÓN",
                "titulo": "Ecuaciones Normales y Flujo Óptimo",
                "puntos": [
                    "Fundamental para resolver el sistema de ecuaciones normales $(A^T A)\\mathbf{x} = A^T \\mathbf{b}$ en mínimos cuadrados.",
                    "Se aplica directamente a la matriz de admitancia nodal y a la matriz Hessiana en optimizaciones no lineales de despacho económico.",
                    "Permite generar vectores aleatorios gaussianos multivariados correlacionados $\\mathbf{x} = \\boldsymbol{\\mu} + L\\mathbf{z}$ en estudios probabilísticos de Monte Carlo."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Transformaciones de Householder y Rotaciones de Givens",
        "objetivo": "Aplicar reflexiones ortogonales de Householder y rotaciones planas de Givens para la anulación selectiva de componentes y la factorización QR estable.",
        "concepto_clave_latex": r"H = I - 2 \frac{\mathbf{v} \mathbf{v}^T}{\mathbf{v}^T \mathbf{v}} \quad [H = H^T = H^{-1}] \quad ; \quad G(i,j,\theta) = \begin{pmatrix} c & s \\ -s & c \end{pmatrix}",
        "ejemplo": "Problema 1: Construir el reflector de Householder que transforma $\\mathbf{x} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}$ en un múltiplo del primer vector canónico $\\mathbf{e}_1$. Norma $\|\mathbf{x}\| = \\sqrt{3^2 + 4^2} = 5$. Vector normal $\\mathbf{v} = \\mathbf{x} + \\text{sign}(x_1)\\|\mathbf{x}\\|\\mathbf{e}_1 = \\begin{pmatrix} 3+5 \\\\ 4 \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ 4 \\end{pmatrix}$. Normalizando: $\\mathbf{v}^T\\mathbf{v} = 64 + 16 = 80$. $H = I - \\frac{2}{80} \\begin{pmatrix} 64 & 32 \\\\ 32 & 16 \\end{pmatrix} = \\begin{pmatrix} -0.6 & -0.8 \\\\ -0.8 & 0.6 \\end{pmatrix}$. Comprobación: $H\\mathbf{x} = \\begin{pmatrix} -0.6(3)-0.8(4) \\\\ -0.8(3)+0.6(4) \\end{pmatrix} = \\begin{pmatrix} -5 \\\\ 0 \\end{pmatrix}$. Problema 2: En matrices dispersas de redes eléctricas, una rotación de Givens anula una entrada individual $(i,j)$ sin destruir los ceros vecinos.",
        "bloque_sugerido": "Taller Numérico 45 min • Factorización QR mediante Householder y Givens",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSFORMACIONES ORTOGONALES",
                "titulo": "Preservación Estricta de Normas",
                "puntos": [
                    "Las matrices ortogonales conservan longitudes euclidianas y ángulos: $\|Q\\mathbf{x}\| = \\|\\mathbf{x}\\|$, garantizando que el error de redondeo jamás crezca.",
                    "Householder anula bloques enteros de columnas debajo de la diagonal con una sola reflexión.",
                    "Givens opera de manera localizada en el plano bidimensional $(i,j)$, ideal para actualización en tiempo real de matrices triangulares."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTABILIDAD NUMÉRICA",
                "titulo": "Superioridad sobre Gram-Schmidt Clásico",
                "puntos": [
                    "El método clásico de Gram-Schmidt sufre de pérdida catastrófica de ortogonalidad ante errores de redondeo en computadores.",
                    "Los reflectores de Householder logran una ortogonalidad $Q^T Q = I$ con precisión a nivel de épsilon de máquina.",
                    "Es el núcleo de los algoritmos modernos de cálculo de valores singulares y autovalores QR."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis de Sensibilidad, Número de Condición y Estabilidad Numérica",
        "objetivo": "Cuantificar la propagación del error y la sensibilidad en la solución de sistemas lineales $A\\mathbf{x} = \\mathbf{b}$ mediante normas matriciales inducidas y el número de condición $\\kappa(A)$.",
        "concepto_clave_latex": r"\kappa(A) = \|A\| \|A^{-1}\| = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)} \quad ; \quad \frac{\|\delta \mathbf{x}\|}{\|\mathbf{x}\|} \le \kappa(A) \left( \frac{\|\delta A\|}{\|A\|} + \frac{\|\delta \mathbf{b}\|}{\|\mathbf{b}\|} \right)",
        "ejemplo": "Problema 1: Sea $A = \\begin{pmatrix} 1 & 1 \\\\ 1 & 1.001 \\end{pmatrix}$. Hallar $\\det(A) = 1.001 - 1 = 0.001$. Inversa: $A^{-1} = 1000 \\begin{pmatrix} 1.001 & -1 \\\\ -1 & 1 \\end{pmatrix}$. Norma infinito: $\|A\|_\\infty = 2.001$, $\|A^{-1}\|_\\infty = 2001$. Número de condición: $\\kappa_\\infty(A) = 2.001 \\times 2001 \\approx 4004$. Un error relativo del $0.1\\%$ en las mediciones puede inducir hasta un $400\\%$ de error en la solución calculada. Problema 2: En la matriz de Hilbert $H_n$, $\\kappa(H_n)$ crece exponencialmente con $n$, mostrando un mal condicionamiento extremo que requiere regularización de Tikhonov.",
        "bloque_sugerido": "Análisis de Error 40 min • Sensibilidad paramétrica en el cálculo de flujos de carga",
        "slides": [
            {
                "numero": 1,
                "seccion": "MÉTRICA DE CONDICIONAMIENTO",
                "titulo": "El Número de Condición Espectral",
                "puntos": [
                    "Si $\\kappa(A) \\approx 1$, el problema está perfectamente bien condicionado (matriz ortogonal).",
                    "Si $\\kappa(A) \\approx 10^k$, se pierden aproximadamente $k$ dígitos significativos de precisión en aritmética de punto flotante.",
                    "Si $A$ es singular, $\\sigma_{\\min}(A) = 0$ y $\\kappa(A) = \\infty$."
                ]
            },
            {
                "numero": 2,
                "seccion": "REDES DE TRANSMISIÓN",
                "titulo": "Condicionamiento de Matrices de Admitancia",
                "puntos": [
                    "Líneas de transmisión con relaciones $R/X$ muy dispares entre ramas generan matrices de admitancia mal condicionadas.",
                    "El precondicionamiento matricial transforma el sistema en $M^{-1}A\\mathbf{x} = M^{-1}\\mathbf{b}$ con $\\kappa(M^{-1}A) \\ll \\kappa(A)$.",
                    "Crítico para garantizar la convergencia de métodos de Newton-Raphson desacoplados rápidos."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Forma Canónica de Jordan y Matrices Defectuosas",
        "objetivo": "Determinar la estructura modal completa de operadores lineales no diagonalizables mediante autovectores generalizados y bloques elementales de Jordan.",
        "concepto_clave_latex": r"J = P^{-1} A P = \text{diag}(J_1, J_2, \dots, J_k) \quad ; \quad J_i = \begin{pmatrix} \lambda_i & 1 & 0 \\ 0 & \lambda_i & 1 \\ 0 & 0 & \lambda_i \end{pmatrix}",
        "ejemplo": "Problema 1: Sea $A = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$. Autovalor $\\lambda = 2$ con multiplicidad algebraica 2. Espacio propio: $(A - 2I)\\mathbf{v} = \\mathbf{0} \\implies \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\mathbf{v} = \\mathbf{0} \\implies \\mathbf{v}_1 = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$. Multiplicidad geométrica es 1 (matriz defectuosa). Hallar autovector generalizado $\\mathbf{v}_2$: $(A - 2I)\\mathbf{v}_2 = \\mathbf{v}_1 \\implies \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} \\implies x_2 = 1, x_1 = 0 \\implies \\mathbf{v}_2 = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix}$. Matriz modal $P = I$, $J = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$. Problema 2: Exponencial matricial de un bloque de Jordan: $e^{J_i t} = e^{\\lambda_i t} \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix}$, mostrando la aparición de términos polinomiales seculares $t e^{\\lambda t}$ en la respuesta temporal.",
        "bloque_sugerido": "Taller Teórico 40 min • Cadena de autovectores generalizados y modos seculares",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRUCTURA ALGEBRAICA",
                "titulo": "Multiplicidad Algebraica vs Geométrica",
                "puntos": [
                    "Multiplicidad Algebraica $m_a(\\lambda)$: potencia del factor $(\\lambda - \\lambda_i)$ en el polinomio característico.",
                    "Multiplicidad Geométrica $m_g(\\lambda) = \\dim(\\mathcal{N}(A - \\lambda I))$: número de autovectores linealmente independientes.",
                    "Una matriz es defectuosa si $m_g(\\lambda) < m_a(\\lambda)$ para algún autovalor, imposibilitando la diagonalización simple."
                ]
            },
            {
                "numero": 2,
                "seccion": "RESPUESTA TEMPORAL",
                "titulo": "Modos Críticamente Amortiguados",
                "puntos": [
                    "Aparece naturalmente en circuitos RLC en condición de amortiguamiento crítico ($R = 2\\sqrt{L/C}$).",
                    "Los términos temporales proporcionales a $t^k e^{\\lambda t}$ rigen la respuesta al escalón más rápida sin sobrepaso oscilatorio.",
                    "Permite comprender la estabilidad estructural ante perturbaciones infinitésimas en los coeficientes matriciales."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Teorema de Perron-Frobenius y Matrices Estocásticas en Redes",
        "objetivo": "Aplicar la teoría de matrices no negativas y el Teorema de Perron-Frobenius para analizar la convergencia en cadenas de Markov y ranking de nodos en redes eléctricas.",
        "concepto_clave_latex": r"A \ge 0 \implies \exists \lambda_{PF} = \rho(A) > 0 \quad ; \quad A \mathbf{v}_{PF} = \lambda_{PF} \mathbf{v}_{PF} \quad [\mathbf{v}_{PF} > 0] \quad ; \quad \sum_{j} P_{ij} = 1",
        "ejemplo": "Problema 1: Sea la matriz de transición estocástica de estados de confiabilidad de una turbina eólica: $P = \\begin{pmatrix} 0.9 & 0.1 \\\\ 0.4 & 0.6 \\end{pmatrix}$, donde el estado 1 es operación normal y el estado 2 es mantenimiento. Hallar la distribución estacionaria $\\boldsymbol{\\pi} P = \\boldsymbol{\\pi}$. Sistema: $\\begin{pmatrix} \\pi_1 & \\pi_2 \\end{pmatrix} \\begin{pmatrix} 0.9 & 0.1 \\\\ 0.4 & 0.6 \\end{pmatrix} = \\begin{pmatrix} \\pi_1 & \\pi_2 \\end{pmatrix}$ con $\\pi_1 + \\pi_2 = 1$. Ecuación: $0.9\\pi_1 + 0.4\\pi_2 = \\pi_1 \\implies 0.4\\pi_2 = 0.1\\pi_1 \\implies \\pi_1 = 4\\pi_2$. Como $4\\pi_2 + \\pi_2 = 1 \\implies \\pi_2 = 0.2, \\pi_1 = 0.8$. Disponibilidad a largo plazo: $80\\%$. Problema 2: El radio espectral de toda matriz estocástica por filas es idénticamente $\\lambda = 1$.",
        "bloque_sugerido": "Modelado Markoviano 40 min • Confiabilidad de activos de generación y distribución",
        "slides": [
            {
                "numero": 1,
                "seccion": "TEORÍA NO NEGATIVA",
                "titulo": "Propiedades Espectrales de Perron",
                "puntos": [
                    "Si $A$ es una matriz cuadrada irreductible con entradas no negativas, su radio espectral $\\rho(A)$ es un autovalor simple positivo.",
                    "El autovector asociado de Perron $\\mathbf{v}_{PF}$ tiene todas sus componentes estrictamente positivas.",
                    "Ningún otro autovalor tiene un módulo superior a $\\rho(A)$."
                ]
            },
            {
                "numero": 2,
                "seccion": "CENTRALIDAD EN GRAFOS",
                "titulo": "Topología y Vulnerabilidad de Red",
                "puntos": [
                    "El autovector de Perron de la matriz de adyacencia cuantifica la 'centralidad de autovector' de cada subestación eléctrica.",
                    "Subestaciones con valores altos en el autovector son nodos críticos cuya desconexión induce mayores riesgos de colapso en cascada.",
                    "Base del algoritmo PageRank adaptado al flujo de influencia en redes inteligentes (Smart Grids)."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis de Componentes Principales (PCA) y Reducción de Dimensionalidad",
        "objetivo": "Reducir la dimensionalidad de grandes conjuntos de datos de monitoreo energético preservando la máxima varianza mediante la diagonalización de la matriz de covarianza.",
        "concepto_clave_latex": r"\Sigma = \frac{1}{N-1} X^T X = W \Lambda W^T \quad ; \quad Y = X W_k \quad [\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p]",
        "ejemplo": "Problema 1: Dadas 3 variables eléctricas centradas con matriz de covarianza $\\Sigma = \\begin{pmatrix} 4 & 2 \\\\ 2 & 1 \\end{pmatrix}$. Hallar las direcciones principales y la varianza explicada. Polinomio característico: $\\det(\\lambda I - \\Sigma) = \\lambda^2 - 5\\lambda = 0 \\implies \\lambda_1 = 5, \\lambda_2 = 0$. Autovector para $\\lambda_1 = 5$: $\\begin{pmatrix} -1 & 2 \\\\ 2 & -4 \\end{pmatrix}\\mathbf{w}_1 = 0 \\implies \\mathbf{w}_1 = \\frac{1}{\\sqrt{5}}\\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix}$. La primera componente principal explica el $\\frac{5}{5+0} = 100\\%$ de la varianza total. Problema 2: En perfiles de consumo horario anual (8760 horas $\\times$ 100 nodos), el PCA reduce los 100 canales a solo 3 componentes principales dominantes que retienen el $92\\%$ de la varianza.",
        "bloque_sugerido": "Ciencia de Datos Energéticos 45 min • Compresión de telemetría de medidores inteligentes",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSFORMACIÓN LINEAL ORTOGONAL",
                "titulo": "Maximización de la Varianza Proyectada",
                "puntos": [
                    "PCA rota los ejes coordenados hacia las direcciones de máxima dispersión de los datos multivariados.",
                    "Los autovectores de la matriz de covarianza son ortogonales entre sí, eliminando la colinealidad y redundancia.",
                    "Los autovalores asociados representan la cantidad de varianza capturada por cada nuevo eje principal."
                ]
            },
            {
                "numero": 2,
                "seccion": "DETECCIÓN DE ANOMALÍAS",
                "titulo": "Detección de Fallas en Subestaciones",
                "puntos": [
                    "Mediciones que violan la correlación histórica normal proyectan un elevado error de reconstrucción residual (SPE).",
                    "Permite detectar en milisegundos desconexiones no autorizadas, fallas incipientes de transformadores o ciberataques a medidores.",
                    "Optimiza el ancho de banda transmitido desde sensores de campo al centro de control SCADA."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Descomposición de Schur y Matrices Hermíticas en Dominio Complejo",
        "objetivo": "Extender los fundamentos espectrales al campo complejo $\\mathbb{C}^n$, demostrando que toda matriz cuadrada es unitariamente equivalente a una matriz triangular superior (Teorema de Schur).",
        "concepto_clave_latex": r"A = U T U^* \quad [U U^* = I, \ T \text{ triangular superior}] \quad ; \quad A = A^* \implies T = \Lambda \in \mathbb{R}^{n \times n}",
        "ejemplo": "Problema 1: Sea la matriz Hermítica $A = \\begin{pmatrix} 2 & 1-j \\\\ 1+j & 3 \\end{pmatrix}$. Comprobar que sus autovalores son reales. $p(\\lambda) = \\det(\\lambda I - A) = (\\lambda - 2)(\\lambda - 3) - (1-j)(1+j) = \\lambda^2 - 5\\lambda + 6 - (1 - (-1)) = \\lambda^2 - 5\\lambda + 4 = 0$. Factores: $(\\lambda - 4)(\\lambda - 1) = 0 \\implies \\lambda_1 = 4, \\lambda_2 = 1 \\in \\mathbb{R}$. Problema 2: Hallar autovector unitario para $\\lambda_1 = 4$: $\\begin{pmatrix} 2 & -(1-j) \\\\ -(1+j) & 1 \\end{pmatrix} \\mathbf{u}_1 = \\mathbf{0} \\implies 2x_1 = (1-j)x_2 \\implies \\mathbf{u}_1 = \\frac{1}{\\sqrt{6}}\\begin{pmatrix} 1-j \\\\ 2 \\end{pmatrix}$. Comprobación: $\|\mathbf{u}_1\|^2 = \\frac{1}{6}(|1-j|^2 + 2^2) = \\frac{1}{6}(2 + 4) = 1$.",
        "bloque_sugerido": "Álgebra Compleja 40 min • Fasores y matrices Hermíticas de impedancia y admitancia",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESPACIOS DE HILBERT",
                "titulo": "Operadores Unitarios y Hermíticos",
                "puntos": [
                    "El conjugado transpuesto (adjunto) satisface $\\langle A\\mathbf{x}, \\mathbf{y} \\rangle = \\langle \\mathbf{x}, A^*\\mathbf{y} \\rangle$ en $\\mathbb{C}^n$.",
                    "Matrices Hermíticas ($A = A^*$) poseen autovalores puramente reales y autovectores ortogonales bajo el producto interno hermitiano.",
                    "El Teorema de Schur garantiza la existencia de una base ortonormal donde cualquier transformación se vuelve cuasi-diagonal."
                ]
            },
            {
                "numero": 2,
                "seccion": "POTENCIA ELÉCTRICA",
                "titulo": "Matriz de Potencia Compleja",
                "puntos": [
                    "La matriz nodal de admitancia $Y = G + jB$ se descompone en su parte real conductora $G$ (simétrica positiva) y susceptiva $B$.",
                    "El análisis espectral de $Y$ desacopla los flujos de potencia activa $P$ y reactiva $Q$ en sistemas interconectados de alta tensión.",
                    "Fundamental para estudios de estabilidad de pequeñas señales en presencia de generadores eólicos e inversores solares."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Subespacios de Krylov y Métodos Iterativos (Gradiente Conjugado y GMRES)",
        "objetivo": "Resolver sistemas algebraicos lineales masivos $A\\mathbf{x} = \\mathbf{b}$ generados en redes eléctricas proyectando los residuos sobre subespacios de Krylov de dimensión creciente.",
        "concepto_clave_latex": r"\mathcal{K}_k(A, \mathbf{r}_0) = \text{span}\{\mathbf{r}_0, A\mathbf{r}_0, A^2\mathbf{r}_0, \dots, A^{k-1}\mathbf{r}_0\} \quad ; \quad \|\mathbf{x}_k - \mathbf{x}^*\|_A \le 2 \left(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\right)^k \|\mathbf{x}_0 - \mathbf{x}^*\|_A",
        "ejemplo": "Problema 1: Aplicar el Método del Gradiente Conjugado a $A = \\begin{pmatrix} 2 & 0 \\\\ 0 & 3 \\end{pmatrix}$, $\\mathbf{b} = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$ iniciando en $\\mathbf{x}_0 = \\mathbf{0}$. Residuo inicial $\\mathbf{r}_0 = \\mathbf{b} - A\\mathbf{x}_0 = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$, dirección $\\mathbf{p}_0 = \\mathbf{r}_0$. Paso $\\alpha_0 = \\frac{\\mathbf{r}_0^T \\mathbf{r}_0}{\\mathbf{p}_0^T A \\mathbf{p}_0} = \\frac{4+9}{\\begin{pmatrix} 2 & 3 \\end{pmatrix} \\begin{pmatrix} 4 \\\\ 9 \\end{pmatrix}} = \\frac{13}{8+27} = \\frac{13}{35}$. Actualización: $\\mathbf{x}_1 = \\mathbf{0} + \\frac{13}{35}\\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$. En a lo sumo $n = 2$ pasos el método converge exactamente a la solución analítica $\\mathbf{x}^* = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$. Problema 2: En redes con 50,000 barras, GMRES resuelve las tensiones en menos de 40 iteraciones aprovechando subespacios de Krylov.",
        "bloque_sugerido": "Computación Científica 45 min • Implementación iterativa de CG y GMRES",
        "slides": [
            {
                "numero": 1,
                "seccion": "ALGORITMOS DE KRYLOV",
                "titulo": "Optimización en Subespacios Proyectados",
                "puntos": [
                    "Evitan calcular la matriz inversa o manipular densamente matrices gigantes con millones de incógnitas.",
                    "Gradiente Conjugado (CG) aplica a matrices simétricas definidas positivas mediante direcciones $A$-ortogonales.",
                    "GMRES (Generalized Minimal Residual) minimiza la norma euclidiana del residuo $\|\mathbf{b} - A\\mathbf{x}_k)\|_2$ para matrices asimétricas arbitrarias."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONVERGENCIA Y PRECONDICIONAMIENTO",
                "titulo": "Impacto del Espectro de Autovalores",
                "puntos": [
                    "La tasa de convergencia depende de la dispersión de autovalores; grupos compactos de autovalores aceleran drásticamente la solución.",
                    "El precondicionamiento incompleto de Cholesky (IC) o LU (ILU) colapsa los autovalores cerca de $1.0$.",
                    "Pilar de los programas comerciales de simulación electromagnética transitoria (PSCAD, ATP-EMTP)."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Matrices Dispersas (Sparse Matrices) y Algoritmos de Reordenamiento Nodal",
        "objetivo": "Optimizar el almacenamiento y la factorización de matrices dispersas en redes de potencia mediante formatos CSR/CSC y el algoritmo de Cuthill-McKee inverso (RCM).",
        "concepto_clave_latex": r"\text{Sparsity} = 1 - \frac{\text{nnz}}{n^2} \quad [> 98\% \text{ en redes eléctricas}] \quad ; \quad B(P A P^T) = \max_{|i-j|} \{|i-j| : a_{ij} \ne 0\} \ll B(A)",
        "ejemplo": "Problema 1: Una red de 1000 barras tiene en promedio 3 líneas por barra, es decir, $\\approx 4000$ elementos no nulos en $Y_{bus}$. Calcular el porcentaje de dispersión: $\\text{Sparsity} = 1 - \\frac{4000}{1000^2} = 1 - 0.004 = 99.6\\%$. Almacenar solo los valores no nulos en vectores de 3 índices reduce la memoria de 8 MB a menos de 50 KB. Problema 2: El algoritmo RCM reordena las filas y columnas para concentrar todos los elementos distintos de cero a lo largo de una banda estrecha alrededor de la diagonal principal, evitando el 'fill-in' o generación de nuevos elementos no nulos durante la eliminación gaussiana.",
        "bloque_sugerido": "Estructuras de Datos 40 min • Formato CSR y minimización de ancho de banda matricial",
        "slides": [
            {
                "numero": 1,
                "seccion": "FORMATOS DE ALMACENAMIENTO",
                "titulo": "CSR, CSC y Matrices de Coordenadas (COO)",
                "puntos": [
                    "COO (Coordinate list): Almacena tuplas `(fila, columna, valor)`; eficiente para armar matrices paso a paso.",
                    "CSR (Compressed Sparse Row): Tres arreglos unidimensionales (`values`, `col_indices`, `row_ptr`); óptimo para multiplicaciones matriz-vector $A\\mathbf{x}$.",
                    "Permite realizar simulaciones dinámicas en tiempo real a escala de red nacional."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTROL DE RELLENO (FILL-IN)",
                "titulo": "Estrategias de Reordenamiento de Tinney",
                "puntos": [
                    "Tinney-1: Ordena nodos por grado ascendente fijo.",
                    "Tinney-2: Selecciona iterativamente el nodo con menor número de conexiones adyacentes dinámicas.",
                    "Tinney-3: Minimiza el número exacto de nuevos términos no nulos creados en cada paso de factorización."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Producto de Kronecker y Ecuaciones Matriciales de Lyapunov y Sylvester",
        "objetivo": "Resolver ecuaciones algebraicas continuas de Lyapunov $A X + X A^T + Q = 0$ y de Sylvester empleando la vectorización de matrices y el producto tensorial de Kronecker.",
        "concepto_clave_latex": r"A \otimes B = \begin{pmatrix} a_{11}B & \dots & a_{1n}B \\ \vdots & \ddots & \vdots \\ a_{m1}B & \dots & a_{mn}B \end{pmatrix} \quad ; \quad \text{vec}(A X B) = (B^T \otimes A) \text{vec}(X)",
        "ejemplo": "Problema 1: Sean $A = \\begin{pmatrix} 1 & 2 \\\\ 0 & 3 \\end{pmatrix}, B = \\begin{pmatrix} 4 & 5 \\\\ 6 & 7 \\end{pmatrix}$. Calcular $A \\otimes B$: $\\begin{pmatrix} 1 B & 2 B \\\\ 0 B & 3 B \\end{pmatrix} = \\begin{pmatrix} 4 & 5 & 8 & 10 \\\\ 6 & 7 & 12 & 14 \\\\ 0 & 0 & 12 & 15 \\\\ 0 & 0 & 18 & 21 \\end{pmatrix}$. Problema 2: Transformar la ecuación de Lyapunov $A X + X A^T = -Q$ en un sistema lineal clásico. Aplicando $\\text{vec}$: $(I \\otimes A + A \\otimes I) \\text{vec}(X) = -\\text{vec}(Q)$. Si los autovalores de $A$ son $\\lambda_i$, los del operador de Kronecker son $\\lambda_i + \\lambda_j$. Existe solución única si y solo si $\\lambda_i + \\lambda_j \\ne 0$ para todo par $(i,j)$.",
        "bloque_sugerido": "Control Avanzado 45 min • Ecuaciones de Lyapunov en estabilidad de generadores",
        "slides": [
            {
                "numero": 1,
                "seccion": "ÁLGEBRA TENSORIAL",
                "titulo": "Propiedades del Producto de Kronecker",
                "puntos": [
                    "Bilineal y asociativo: $(A \\otimes B)(C \\otimes D) = (AC) \\otimes (BD)$.",
                    "Inversión de Kronecker: $(A \\otimes B)^{-1} = A^{-1} \\otimes B^{-1}$.",
                    "Autovalores: Si $\\sigma(A) = \\{\\lambda_i\\}$ y $\\sigma(B) = \\{\\mu_j\\}$, entonces $\\sigma(A \\otimes B) = \\{\\lambda_i \\mu_j\\}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTABILIDAD ROBUSTA",
                "titulo": "Funciones Cuadráticas de Lyapunov",
                "puntos": [
                    "La existencia de una matriz simétrica $X > 0$ que resuelva $A^T X + X A = -Q$ con $Q > 0$ demuestra estabilidad asintótica global.",
                    "La matriz $X$ define la función de energía almacenada $V(\\mathbf{x}) = \\mathbf{x}^T X \\mathbf{x}$ con derivada estrictamente negativa $\\dot{V} = -\\mathbf{x}^T Q \\mathbf{x} < 0$.",
                    "Se utiliza para sintonizar estabilizadores de sistemas de potencia (PSS) y lazos PLL de convertidores electrónicos."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Descomposición Espectral y Operadores de Proyección Ortogonal",
        "objetivo": "Descomponer operadores lineales simétricos en sumas ponderadas de proyectores ortogonales unidimensionales $P_i = \\mathbf{u}_i \\mathbf{u}_i^T$ mutuamente aniquiladores.",
        "concepto_clave_latex": r"A = \sum_{i=1}^n \lambda_i \mathbf{u}_i \mathbf{u}_i^T = \sum_{i=1}^n \lambda_i P_i \quad [P_i^2 = P_i = P_i^T, \ P_i P_j = \mathbf{0} \ (i \ne j), \ \sum P_i = I]",
        "ejemplo": "Problema 1: Sea $A = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}$. Autovalores: $\\lambda_1 = 3, \\lambda_2 = 1$. Autovectores ortonormales: $\\mathbf{u}_1 = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}, \\mathbf{u}_2 = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix}$. Proyectores asociados: $P_1 = \\mathbf{u}_1 \\mathbf{u}_1^T = \\frac{1}{2}\\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix}$; $P_2 = \\mathbf{u}_2 \\mathbf{u}_2^T = \\frac{1}{2}\\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix}$. Verificación: $P_1 + P_2 = I$; $P_1 P_2 = 0$. Reconstrucción espectral: $3 P_1 + 1 P_2 = \\begin{pmatrix} 1.5 & 1.5 \\\\ 1.5 & 1.5 \\end{pmatrix} + \\begin{pmatrix} 0.5 & -0.5 \\\\ -0.5 & 0.5 \\end{pmatrix} = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} = A$. Problema 2: Evaluar $f(A) = A^{10}$: $f(A) = 3^{10} P_1 + 1^{10} P_2 = 59049 P_1 + P_2$.",
        "bloque_sugerido": "Resolución Proyectiva 40 min • Filtrado de modos espaciales y proyecciones ortogonales",
        "slides": [
            {
                "numero": 1,
                "seccion": "TEOREMA ESPECTRAL",
                "titulo": "Geometría de la Proyección Pura",
                "puntos": [
                    "Cualquier matriz simétrica real admite una base ortonormal completa de autovectores.",
                    "Los operadores de proyección $P_i$ son idempotentes ($P_i^2 = P_i$) y proyectan cualquier vector arbitrario sobre la línea generada por $\\mathbf{u}_i$.",
                    "Facilita la evaluación de cualquier función analítica $f(A) = \\sum f(\\lambda_i) P_i$ de manera instantánea."
                ]
            },
            {
                "numero": 2,
                "seccion": "FILTRADO ESPACIAL",
                "titulo": "Aislamiento de Perturbaciones",
                "puntos": [
                    "Permite filtrar perturbaciones armónicas proyectando el vector de estado sobre el subespacio ortogonal al modo de falla.",
                    "Utilizado en el análisis modal de oscilaciones interárea entre zonas geográficas de generación eléctrica.",
                    "Sustenta la teoría matemática del modelado cinemático y dinámico de turbinas de eje horizontal."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Transformaciones Afines, Coordenadas Homogéneas y Proyecciones 3D",
        "objetivo": "Modelar rotaciones espaciales, traslaciones y escalamientos en 3D utilizando matrices de transformación homogénea $4 \\times 4$ aplicadas al diseño mecatrónico y posicionamiento de paneles solares.",
        "concepto_clave_latex": r"\begin{pmatrix} \mathbf{x}' \\ 1 \end{pmatrix} = \begin{pmatrix} R_{3\times3} & \mathbf{t}_{3\times1} \\ \mathbf{0}_{1\times3} & 1 \end{pmatrix} \begin{pmatrix} \mathbf{x} \\ 1 \end{pmatrix} \quad ; \quad R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}",
        "ejemplo": "Problema 1: Un sensor solar en $\\mathbf{p} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix}$ se rota $90^\\circ$ sobre el eje $Z$ y luego se traslada según $\\mathbf{t} = \\begin{pmatrix} 2 \\\\ 3 \\\\ 5 \\end{pmatrix}$. Matriz homogénea: $T = \\begin{pmatrix} 0 & -1 & 0 & 2 \\\\ 1 & 0 & 0 & 3 \\\\ 0 & 0 & 1 & 5 \\\\ 0 & 0 & 0 & 1 \\end{pmatrix}$. Vector homogéneo: $\\mathbf{p}_h = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 1 \\end{pmatrix}$. Posición final: $\\mathbf{p}'_h = T \\mathbf{p}_h = \\begin{pmatrix} 0(1) + 2 \\\\ 1(1) + 3 \\\\ 0 + 5 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 4 \\\\ 5 \\\\ 1 \\end{pmatrix}$. Nueva coordenada espacial: $(2, 4, 5)$. Problema 2: El algoritmo de seguimiento solar biaxial calcula la matriz de rotación en acimut $\\theta_{az}$ y elevación $\\theta_{el}$ para alinear el vector normal de los módulos con el vector solar incidente.",
        "bloque_sugerido": "Cinemática y CAD 45 min • Matrices homogéneas en seguidores solares y turbinas",
        "slides": [
            {
                "numero": 1,
                "seccion": "GEOMETRÍA COMPUTACIONAL",
                "titulo": "Coordenadas Homogéneas",
                "puntos": [
                    "Permiten unificar traslaciones vectoriales y rotaciones lineales bajo una sola multiplicación matricial.",
                    "La composición de transformaciones secuenciales se reduce a multiplicaciones encadenadas $T_{total} = T_1 T_2 \\dots T_k$.",
                    "Estándar internacional en robótica de mantenimiento y diseño asistido por computadora (CAD/BIM)."
                ]
            },
            {
                "numero": 2,
                "seccion": "SEGUIMIENTO SOLAR",
                "titulo": "Orientación de Colectores Solares",
                "puntos": [
                    "Transforma las coordenadas astronómicas celestes (ascensión recta y declinación) al marco local de la planta.",
                    "Compensa desalineaciones mecánicas y pendientes del terreno mediante calibración matricial.",
                    "Maximiza la captación de irradiancia directa $G_{dir} = G_0 \\cos(\\theta_{inc})$ a lo largo del año."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Matrices Circulantes, Matrices de Toeplitz y DFT Matricial",
        "objetivo": "Vincular el álgebra lineal con el procesamiento de señales eléctricas discretas, demostrando que toda matriz circulante es diagonalizada por la matriz de la Transformada Discreta de Fourier (DFT).",
        "concepto_clave_latex": r"C = F_n^* \Lambda F_n \quad ; \quad F_n = \frac{1}{\sqrt{n}} \left( \omega^{jk} \right)_{j,k=0}^{n-1} \quad [\omega = e^{-j 2\pi / n}] \quad ; \quad C \mathbf{x} = \mathbf{c} * \mathbf{x}",
        "ejemplo": "Problema 1: Construir la matriz DFT $F_4$ con $\\omega = e^{-j 2\\pi / 4} = -j$. $F_4 = \\frac{1}{2} \\begin{pmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{pmatrix}$. Comprobar unitariedad: $F_4 F_4^* = I_4$. Problema 2: Una matriz circulante $C$ representa un filtro lineal invariante en el tiempo (convolución circular). Como los autovectores de cualquier matriz circulante son exactamente las columnas de $F_4^*$, los autovalores corresponden a la DFT de la primera fila del filtro. La multiplicación $C\\mathbf{x}$ se efectúa en complejidad $O(n \\log n)$ mediante la FFT en lugar de $O(n^2)$.",
        "bloque_sugerido": "Procesamiento Digital 40 min • Análisis armónico con la matriz DFT en redes",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRUCTURA DE TOEPLITZ Y CIRCULANTE",
                "titulo": "Matrices Invariantes por Desplazamiento",
                "puntos": [
                    "Matriz de Toeplitz: Elementos constantes a lo largo de cada diagonal ($A_{i,j} = a_{i-j}$).",
                    "Matriz Circulante: Cada fila es un desplazamiento circular de la fila precedente.",
                    "El producto matriz-vector circulante equivale formalmente a la convolución discreta periódica."
                ]
            },
            {
                "numero": 2,
                "seccion": "CALIDAD DE ENERGÍA",
                "titulo": "Descomposición Espectral de Armónicos",
                "puntos": [
                    "La matriz $F_n$ proyecta formas de onda distorsionadas de corriente hacia sus armónicos fundamentales y superiores.",
                    "Permite calcular la distorsión armónica total (THD) y detectar frecuencias resonantes producidas por convertidores estáticos.",
                    "Base algorítmica para filtros activos de potencia en tiempo real."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Subespacios Invariantes, Estabilidad de Lyapunov y Criterios Matriciales",
        "objetivo": "Identificar subespacios invariantes bajo transformaciones lineales continuas y discretas para evaluar la estabilidad asintótica de generadores interconectados.",
        "concepto_clave_latex": r"A \mathcal{V} \subseteq \mathcal{V} \quad ; \quad A^T P + P A = -Q \quad [P = P^T > 0, \ Q = Q^T > 0] \quad ; \quad \rho(A_{disc}) < 1",
        "ejemplo": "Problema 1: Sea el subespacio $\\mathcal{V} = \\text{span}\\left\\{\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}\\right\\}$ y $A = \\begin{pmatrix} 3 & 1 \\\\ 2 & 2 \\end{pmatrix}$. Comprobar si es invariante: $A\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 4 \\end{pmatrix} = 4\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} \\in \\mathcal{V}$. Es invariante y corresponde al subespacio propio del autovalor $\\lambda = 4$. Problema 2: En un sistema de control discreto de frecuencia de red $\\mathbf{x}_{k+1} = A\\mathbf{x}_k$, el sistema es estable si todos los autovalores de $A$ yacen estrictamente dentro del círculo unitario complejo ($|\\lambda_i| < 1$). La ecuación discreta de Lyapunov correspondiente es $A^T P A - P = -Q$.",
        "bloque_sugerido": "Control de Redes 40 min • Subespacios estables e inestables en regulación de frecuencia",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA DE SUBESPACIOS",
                "titulo": "Subespacios Estable, Inestable y Central",
                "puntos": [
                    "Subespacio Estable $E^s$: Generado por los autovectores con $\\text{Re}(\\lambda) < 0$.",
                    "Subespacio Inestable $E^u$: Generado por los autovectores con $\\text{Re}(\\lambda) > 0$.",
                    "Subespacio Central $E^c$: Generado por los autovectores con $\\text{Re}(\\lambda) = 0$ (modos neutros/oscilatorios)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTROL DE GENERACIÓN",
                "titulo": "Regulación Automática de Generación (AGC)",
                "puntos": [
                    "Asegura que las trayectorias de desviación de frecuencia converjan exponencialmente al subespacio nulo.",
                    "Las ecuaciones matriciales de Lyapunov verifican márgenes de ganancia y fase sin requerir integración numérica paso a paso.",
                    "Permite desacoplar subsistemas de control independientes mediante proyecciones de Kalman."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Optimización Cuadrática con Restricciones Lineales y Multiplicadores de Lagrange",
        "objetivo": "Resolver analítica y matricialmente problemas de programación cuadrática (QP) con restricciones lineales de igualdad a través del sistema de condiciones KKT matricial.",
        "concepto_clave_latex": r"\min_{\mathbf{x}} \frac{1}{2}\mathbf{x}^T H \mathbf{x} + \mathbf{c}^T \mathbf{x} \quad \text{s.t.} \quad A\mathbf{x} = \mathbf{b} \implies \begin{pmatrix} H & A^T \\ A & \mathbf{0} \end{pmatrix} \begin{pmatrix} \mathbf{x}^* \\ \boldsymbol{\lambda}^* \end{pmatrix} = \begin{pmatrix} -\mathbf{c} \\ \mathbf{b} \end{pmatrix}",
        "ejemplo": "Problema 1: Minimizar el costo de generación $f(x_1, x_2) = x_1^2 + 2x_2^2$ sujeto a la demanda total $x_1 + x_2 = 300\\text{ MW}$. Matriz Hessiana $H = \\begin{pmatrix} 2 & 0 \\\\ 0 & 4 \\end{pmatrix}$, $\\mathbf{c} = \\mathbf{0}$, $A = \\begin{pmatrix} 1 & 1 \\end{pmatrix}, b = 300$. Matriz KKT: $\\begin{pmatrix} 2 & 0 & 1 \\\\ 0 & 4 & 1 \\\\ 1 & 1 & 0 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\lambda \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 300 \\end{pmatrix}$. Ecuaciones: $2x_1 + \\lambda = 0 \\implies x_1 = -\\lambda/2$; $4x_2 + \\lambda = 0 \\implies x_2 = -\\lambda/4$. Sustituyendo en la restricción: $-\\frac{\\lambda}{2} - \\frac{\\lambda}{4} = 300 \\implies -\\frac{3\\lambda}{4} = 300 \\implies \\lambda = -400$. Despacho óptimo: $x_1 = 200\\text{ MW}$, $x_2 = 100\\text{ MW}$. Problema 2: El multiplicador de Lagrange $\\lambda = -400$ representa el costo marginal de la electricidad (precio sombra por MW adicional).",
        "bloque_sugerido": "Economía de la Energía 45 min • Despacho económico clásico mediante matriz KKT",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROGRAMACIÓN CUADRÁTICA",
                "titulo": "El Sistema Aumentado de Karush-Kuhn-Tucker",
                "puntos": [
                    "Si $H$ es definida positiva, el punto crítico estacionario es un mínimo global estricto.",
                    "La matriz KKT es una matriz simétrica pero indefinida (posee autovalores tanto positivos como negativos, estructura saddle-point).",
                    "Métodos directos de factorización $LDL^T$ resuelven simultáneamente las variables primales $\\mathbf{x}^*$ y duales $\\boldsymbol{\\lambda}^*$."
                ]
            },
            {
                "numero": 2,
                "seccion": "MERCADOS DE ELECTRICIDAD",
                "titulo": "Precios Marginales Locacionales (LMP)",
                "puntos": [
                    "Los multiplicadores $\\boldsymbol{\\lambda}^*$ determinan el precio nodal de la energía en cada subestación eléctrica del sistema interconectado.",
                    "Diferencias en los multiplicadores nodales reflejan costos de congestión en las líneas de transmisión y pérdidas óhmicas de transporte.",
                    "Base matemática de la operación económica de operadores de mercado independiente (XM en Colombia, CAISO en EE.UU.)."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Matriz de Admitancia Nodal ($Y_{bus}$), Incidencia Topológica y Flujo DC",
        "objetivo": "Integrar toda la teoría del álgebra lineal matricial en la construcción sistemática de la matriz $Y_{bus}$ a partir de la matriz de incidencia de red y formular el modelo linealizado de Flujo DC.",
        "concepto_clave_latex": r"Y_{bus} = A^T Y_{primitiva} A \quad ; \quad P_{bus} = B' \boldsymbol{\theta} \quad ; \quad Y_{ii} = y_{i0} + \sum_{k \in \Omega_i} y_{ik} \quad ; \quad Y_{ik} = -y_{ik}",
        "ejemplo": "Problema 1: Construir la matriz $Y_{bus}$ para una red de 3 barras con reactancias serie $x_{12} = 0.1$, $x_{13} = 0.2$, $x_{23} = 0.2$ p.u. (admitancias primitivas $b_{12} = -j10$, $b_{13} = -j5$, $b_{23} = -j5$). Elementos diagonales: $Y_{11} = -j(10+5) = -j15$; $Y_{22} = -j(10+5) = -j15$; $Y_{33} = -j(5+5) = -j10$. Elementos fuera de la diagonal: $Y_{12} = Y_{21} = j10$; $Y_{13} = Y_{31} = j5$; $Y_{23} = Y_{32} = j5$. Matriz resultante: $Y_{bus} = -j \\begin{pmatrix} 15 & -10 & -5 \\\\ -10 & 15 & -5 \\\\ -5 & -5 & 10 \\end{pmatrix}$. Problema 2: En el modelo de Flujo DC con barra slack en el nodo 3 ($\\theta_3 = 0$), se elimina la fila y columna 3 resultando en $B' = \\begin{pmatrix} 15 & -10 \\\\ -10 & 15 \\end{pmatrix}$. Para inyecciones $P_1 = 1.0\\text{ p.u.}, P_2 = -1.0\\text{ p.u.}$, resolver $B'\\boldsymbol{\\theta} = \\mathbf{P}$: $\\theta_1 = 0.04\\text{ rad}, \\theta_2 = -0.04\\text{ rad}$.",
        "bloque_sugerido": "Proyecto Integrador C4 50 min • Construcción de Ybus y solución de Flujo DC en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "TOPOLOGÍA Y MATRICES DE INCIDENCIA",
                "titulo": "Generación Sistemática de Redes",
                "puntos": [
                    "La matriz de incidencia orientada rama-nodo $A \\in \\mathbb{R}^{m \\times n}$ codifica la conectividad física de todas las líneas del sistema.",
                    "La relación de congruencia matricial $Y_{bus} = A^T Y_{lineas} A$ garantiza simetría y estructura definida no negativa.",
                    "Cada fila de $Y_{bus}$ suma cero si se desprecian los elementos en derivación (shunts a tierra)."
                ]
            },
            {
                "numero": 2,
                "seccion": "MODELADO LINEALIZADO",
                "titulo": "Aproximación de Flujo DC en Potencia",
                "puntos": [
                    "Supone diferencias angulares de fase pequeñas: $\\sin(\\theta_i - \\theta_k) \\approx \\theta_i - \\theta_k$.",
                    "Asume perfiles de tensión constantes y cercanos a la unidad nominal ($V_i \\approx 1.0$ p.u.) y desprecia resistencias de línea frente a reactancias ($R \\ll X$).",
                    "Convierte las complejas ecuaciones no lineales trigonométricas de flujo de potencia en un problema algebraico lineal clásico $B'\\boldsymbol{\\theta} = \\mathbf{P}$ de solución instantánea."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_02011809)
    # Inject right before the next subject marker: 06011837
    inject_topics_after('      - codigo: "06011837"', yaml_text)
    print("02011809 Álgebra Lineal successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
