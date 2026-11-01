# -*- coding: utf-8 -*-
import sys
from injector_base import inject_topics_after

topics_03031818 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "titulo": "Análisis Exploratorio Multivariado, Matriz de Covarianza y Correlación de Pearson",
        "objetivo": "Calcular e interpretar matrices de varianza-covarianza y coeficientes de correlación lineal en series multivariadas de variables meteorológicas y consumo de potencia.",
        "concepto_clave_latex": r"\boldsymbol{\Sigma} = \frac{1}{n-1}\sum_{k=1}^n (\mathbf{x}_k - \bar{\mathbf{x}})(\mathbf{x}_k - \bar{\mathbf{x}})^T \quad ; \quad r_{xy} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} \quad [-1 \le r \le 1]",
        "ejemplo": """Problema 1: Se registran 5 pares de datos simultáneos de irradiancia solar G [W/m²] y generación eléctrica P [kW]: (200, 18), (400, 38), (600, 59), (800, 78), (1000, 99). Calcule el coeficiente de correlación muestral de Pearson r_xy.
Paso 1: Medias aritméticas: x̄ = (200+400+600+800+1000)/5 = 600 W/m²; ȳ = (18+38+59+78+99)/5 = 58.4 kW.
Paso 2: Desviaciones: (x_i - x̄) = [-400, -200, 0, 200, 400]; (y_i - ȳ) = [-40.4, -20.4, 0.6, 19.6, 40.6].
Paso 3: Covarianza cruzada numeradora: (-400)(-40.4) + (-200)(-20.4) + 0 + (200)(19.6) + (400)(40.6) = 16160 + 4080 + 0 + 3920 + 16240 = 40400.
Paso 4: Suma de cuadrados: SS_xx = (-400)² + (-200)² + 0 + 200² + 400² = 400,000; SS_yy = (-40.4)² + (-20.4)² + (0.6)² + (19.6)² + (40.6)² = 1632.16 + 416.16 + 0.36 + 384.16 + 1648.36 = 4081.2.
Paso 5: Denominador: √(400,000 × 4081.2) = √(1,632,480,000) = 40403.96.
Paso 6: r_xy = 40400 / 40403.96 = 0.9999 (correlación lineal positiva prácticamente perfecta).

Problema 2: En una subestación se analiza la covarianza entre voltaje de barra V [kV] y potencia reactiva Q [MVAr] con Cov(V, Q) = -1.8 kV·MVAr, s_V = 0.5 kV y s_Q = 4.0 MVAr. Determine r_{VQ} y concluya físicamente.
Paso 1: r_{VQ} = Cov(V, Q) / (s_V · s_Q) = -1.8 / (0.5 × 4.0) = -1.8 / 2.0 = -0.90.
Paso 2: Existe una fuerte correlación lineal negativa: incrementos en la demanda reactiva descienden severamente la tensión de barra.""",
        "bloque_sugerido": "Resolución Analítica 40 min • Cálculo de matrices de covarianza y elipses de confianza en Python"
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "titulo": "Distribuciones de Probabilidad Conjuntas, Marginales y Condicionales",
        "objetivo": "Modelar probabilísticamente dos o más variables aleatorias simultáneas calculando densidades marginales y condicionales en redes de distribución.",
        "concepto_clave_latex": r"f_X(x) = \int_{-\infty}^\infty f_{XY}(x,y)\, dy \quad ; \quad f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)} \quad ; \quad P((X,Y) \in A) = \iint_A f_{XY}(x,y)\, dx\, dy",
        "ejemplo": """Problema 1: Sean X (generación eólica normalizada [0,1]) e Y (generación solar normalizada [0,1]) con densidad conjunta f(x,y) = c(x + 2y) para 0 <= x <= 1, 0 <= y <= 1. Halle la constante c, la marginal f_X(x) y la probabilidad condicional P(Y > 0.5 | X = 0.8).
Paso 1: Normalización: ∫_0^1 ∫_0^1 c(x + 2y) dy dx = 1.
∫_0^1 [xy + y²]_0^1 dx = ∫_0^1 (x + 1) dx = [x²/2 + x]_0^1 = 1/2 + 1 = 1.5. Luego c(1.5) = 1 => c = 2/3.
Paso 2: Densidad marginal de X: f_X(x) = ∫_0^1 (2/3)(x + 2y) dy = (2/3)[xy + y²]_0^1 = (2/3)(x + 1).
Paso 3: Densidad condicional: f_{Y|X}(y|x) = f(x,y) / f_X(x) = (2/3)(x + 2y) / [(2/3)(x + 1)] = (x + 2y)/(x + 1).
Paso 4: Para x = 0.8: f_{Y|X}(y|0.8) = (0.8 + 2y) / 1.8.
Paso 5: P(Y > 0.5 | X = 0.8) = ∫_0.5^1 (0.8 + 2y)/1.8 dy = (1/1.8)[0.8y + y²]_0.5^1 = (1/1.8)[(0.8 + 1) - (0.4 + 0.25)] = (1/1.8)(1.8 - 0.65) = 1.15 / 1.8 = 0.6389 (63.89%).

Problema 2: Verifique si X e Y son independientes.
Paso 1: Marginal f_Y(y) = ∫_0^1 (2/3)(x + 2y) dx = (2/3)[x²/2 + 2yx]_0^1 = (2/3)(1/2 + 2y) = (1/3) + (4/3)y.
Paso 2: Producto f_X(x) f_Y(y) = (2/3)(x + 1) × (1/3)(1 + 4y) = (2/9)(x + 1)(1 + 4y) != (2/3)(x + 2y).
Paso 3: Dado que f_{XY}(x,y) != f_X(x) f_Y(y), las variables X e Y no son estadísticamente independientes.""",
        "bloque_sugerido": "Taller Teórico 35 min • Integración doble de densidades conjuntas y cálculo condicional"
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "titulo": "Esperanza Condicional, Varianza Total y Teorema de la Varianza Iterada",
        "objetivo": "Descomponer la varianza de la demanda energética mediante la ley de varianza total y esperanza condicional iterada.",
        "concepto_clave_latex": r"\mathbb{E}[Y] = \mathbb{E}[\mathbb{E}[Y|X]] \quad ; \quad \text{Var}(Y) = \mathbb{E}[\text{Var}(Y|X)] + \text{Var}(\mathbb{E}[Y|X])",
        "ejemplo": """Problema 1: El consumo diario de energía Y [MWh] en un distrito industrial depende del estado operativo X (1 = jornada normal con P(X=1) = 0.7; 2 = turno de mantenimiento con P(X=2) = 0.3). Se conoce: E[Y|X=1] = 120 MWh, Var(Y|X=1) = 100 MWh²; E[Y|X=2] = 50 MWh, Var(Y|X=2) = 64 MWh². Calcule la esperanza total E[Y] y la varianza total Var(Y).
Paso 1: E[Y] = E[E[Y|X]] = (120)(0.7) + (50)(0.3) = 84 + 15 = 99 MWh.
Paso 2: Promedio de varianzas condicionales (varianza intra-grupos): E[Var(Y|X)] = (100)(0.7) + (64)(0.3) = 70 + 19.2 = 89.2 MWh².
Paso 3: Varianza de esperanzas condicionales (varianza inter-grupos): Var(E[Y|X]) = E[(E[Y|X])²] - (E[Y])² = [120²(0.7) + 50²(0.3)] - 99² = [14400(0.7) + 2500(0.3)] - 9801 = (10080 + 750) - 9801 = 10830 - 9801 = 1029 MWh².
Paso 4: Varianza total Var(Y) = 89.2 + 1029 = 1118.2 MWh².
Paso 5: Desviación estándar sigma_Y = √(1118.2) = 33.44 MWh.

Problema 2: ¿Qué porcentaje de la incertidumbre total del consumo es atribuible al tipo de jornada X?
Paso 1: Proporción explicada = Var(E[Y|X]) / Var(Y) = 1029 / 1118.2 = 0.9202 (92.02%).
Paso 2: El 92% de la dispersión de la demanda se debe al cambio entre jornada normal y mantenimiento.""",
        "bloque_sugerido": "Estudio Práctico 30 min • Descomposición de varianza de pronóstico en parques solares"
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "titulo": "Funciones Generadoras de Momentos y Teorema del Límite Central (CLT)",
        "objetivo": "Deducir momentos estadísticos mediante la FGM y fundamentar la convergencia asintótica de la suma de variables aleatorias independientes hacia la distribución normal.",
        "concepto_clave_latex": r"M_X(t) = \mathbb{E}[e^{tX}] \quad ; \quad \mathbb{E}[X^k] = \left.\frac{d^k M_X(t)}{dt^k}\right|_{t=0} \quad ; \quad Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)",
        "ejemplo": """Problema 1: Sea X una variable aleatoria con distribución exponencial f(x) = lambda e^(-lambda x) para x >= 0. Halle su función generadora de momentos M_X(t) y demuestre a partir de ella que E[X] = 1/lambda y Var(X) = 1/lambda².
Paso 1: M_X(t) = ∫_0^inf e^(tx) lambda e^(-lambda x) dx = lambda ∫_0^inf e^(-(lambda - t)x) dx = lambda / (lambda - t) para t < lambda.
Paso 2: Primera derivada: M'_X(t) = lambda / (lambda - t)². Evaluando en t = 0: E[X] = M'_X(0) = lambda / lambda² = 1/lambda.
Paso 3: Segunda derivada: M''_X(t) = 2 lambda / (lambda - t)³. Evaluando en t = 0: E[X²] = M''_X(0) = 2 lambda / lambda³ = 2/lambda².
Paso 4: Varianza: Var(X) = E[X²] - (E[X])² = (2/lambda²) - (1/lambda)² = 1/lambda². Q.E.D.

Problema 2: Una micro-red alimenta 64 residencias cuyos consumos individuales diarios X_i son independientes e idénticamente distribuidos con media mu = 12.5 kWh y desviación estándar sigma = 4.0 kWh. Calcule la probabilidad de que la demanda promedio de la muestra exceda 13.2 kWh.
Paso 1: Por el Teorema del Límite Central, la media muestral X̄_64 sigue aproximadamente N(mu, sigma / √n) = N(12.5, 4.0 / √64) = N(12.5, 0.50 kWh).
Paso 2: Estandarización: Z = (13.2 - 12.5) / 0.50 = 0.70 / 0.50 = 1.40.
Paso 3: P(X̄ > 13.2) = P(Z > 1.40) = 1 - Phi(1.40) = 1 - 0.9192 = 0.0808 (8.08%).""",
        "bloque_sugerido": "Demostración y Simulación 40 min • Simulación de CLT con 10,000 réplicas en Python/Dart"
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "titulo": "Distribuciones Gamma, Beta y Chi-Cuadrado en Confiabilidad y Radiación Solar",
        "objetivo": "Aplicar las distribuciones Gamma, Beta y Chi-Cuadrado para modelar el tiempo hasta la k-ésima falla en generadores y el índice de claridad atmosférica.",
        "concepto_clave_latex": r"f_\Gamma(x;\alpha,\beta) = \frac{\beta^\alpha x^{\alpha-1} e^{-\beta x}}{\Gamma(\alpha)} \quad ; \quad f_\mathrm{B}(k_t; p, q) = \frac{k_t^{p-1} (1-k_t)^{q-1}}{\mathrm{B}(p,q)} \quad ; \quad \chi^2(k) \equiv \Gamma\left(\frac{k}{2}, \frac{1}{2}\right)",
        "ejemplo": """Problema 1: El tiempo t [miles de horas] hasta la tercera falla (alpha = 3) en un sistema de rodamientos eólicos sigue una distribución Gamma con tasa beta = 0.5 (falla cada 2,000 horas en promedio). Calcule la media E[T], la varianza Var(T) y la probabilidad de que el rodamiento opere más de 4,000 horas antes de la tercera falla.
Paso 1: Media: E[T] = alpha / beta = 3 / 0.5 = 6 (6,000 horas).
Paso 2: Varianza: Var(T) = alpha / beta² = 3 / (0.5)² = 3 / 0.25 = 12 (12 millones de horas²); sigma = √12 = 3.464 miles de horas.
Paso 3: La probabilidad P(T > 4) con alpha entero equivale a la probabilidad de Poisson de observar a lo sumo 2 fallas en t = 4 con media lambda = beta × t = 0.5 × 4 = 2.0:
P(T > 4) = sum_{k=0}^2 e^(-2) (2^k / k!) = e^(-2) [1 + 2 + 2²/2] = e^(-2) [1 + 2 + 2] = 5 e^(-2) = 5 × 0.135335 = 0.6767 (67.67%).

Problema 2: El índice de claridad solar k_t en Santa Marta sigue una distribución Beta con parámetros p = 4 y q = 2 en el intervalo [0, 1]. Calcule el valor esperado E[k_t] y la moda de k_t.
Paso 1: E[k_t] = p / (p + q) = 4 / (4 + 2) = 4/6 = 0.667.
Paso 2: Moda = (p - 1) / (p + q - 2) = (4 - 1) / (4 + 2 - 2) = 3 / 4 = 0.75. La condición atmosférica más frecuente es de cielo predominantemente despejado.""",
        "bloque_sugerido": "Modelación Avanzada 35 min • Ajuste de índice de claridad solar k_t mediante distribución Beta"
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "titulo": "Distribuciones t de Student y F de Snedecor en Control Metrológico",
        "objetivo": "Utilizar las distribuciones t de Student y F de Fisher-Snedecor para pruebas de varianza y comparaciones con muestras pequeñas en calibración de medidores.",
        "concepto_clave_latex": r"T = \frac{Z}{\sqrt{U / \nu}} \sim t(\nu) \quad ; \quad F = \frac{U_1 / d_1}{U_2 / d_2} = \frac{s_1^2 / \sigma_1^2}{s_2^2 / \sigma_2^2} \sim F(d_1, d_2)",
        "ejemplo": """Problema 1: Se ensayan n = 10 medidores inteligentes de energía para verificar el error porcentual medio. La media muestral es x̄ = 0.24% y la desviación estándar muestral s = 0.30%. Determine el intervalo de confianza del 95% para el error verdadero mu.
Paso 1: Grados de libertad nu = n - 1 = 9.
Paso 2: Valor crítico t_{0.025, 9} = 2.262.
Paso 3: Error estándar: SE = s / √n = 0.30 / √10 = 0.30 / 3.1623 = 0.0949%.
Paso 4: Margen de error: ME = 2.262 × 0.0949% = 0.2147%.
Paso 5: IC 95%: [0.24 - 0.2147, 0.24 + 0.2147] = [0.0253%, 0.4547%]. Como el cero no está contenido, los medidores tienen un sesgo positivo estadísticamente significativo al 5%.

Problema 2: Se comparan las varianzas de error de dos bancos de condensadores (muestra 1: n_1 = 16, s_1 = 1.2 kV; muestra 2: n_2 = 21, s_2 = 0.8 kV). Calcule el estadístico F y el intervalo de confianza al 90% para sigma_1² / sigma_2².
Paso 1: F_{calc} = s_1² / s_2² = (1.2)² / (0.8)² = 1.44 / 0.64 = 2.25.
Paso 2: Grados de libertad: d_1 = 15, d_2 = 20.
Paso 3: Valores críticos: F_{0.05, 15, 20} = 2.20; F_{0.95, 15, 20} = 1 / F_{0.05, 20, 15} = 1 / 2.33 = 0.429.
Paso 4: Intervalo: [(s_1²/s_2²) × (1 / F_{0.05, 15, 20}), (s_1²/s_2²) × F_{0.05, 20, 15}] = [2.25 × (1/2.20), 2.25 × 2.33] = [1.023, 5.24]. Con 90% de confianza, la varianza del primer banco es significativamente mayor.""",
        "bloque_sugerido": "Resolución Metrológica 30 min • Contraste de precisión en medidores de energía eléctrica"
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "titulo": "Estimación Puntual: Método de Máxima Verosimilitud (MLE) en Modelos Energéticos",
        "objetivo": "Formular la función de verosimilitud y obtener estimadores MLE para parámetros de distribuciones continuas y discretas.",
        "concepto_clave_latex": r"L(\theta; \mathbf{x}) = \prod_{i=1}^n f(x_i; \theta) \quad ; \quad \ell(\theta) = \sum_{i=1}^n \ln f(x_i; \theta) \quad ; \quad \left.\frac{\partial \ell(\theta)}{\partial \theta}\right|_{\hat{\theta}_{\text{MLE}}} = 0",
        "ejemplo": """Problema 1: Sea una muestra de tiempos entre fallas t_1, t_2, ..., t_n [horas] proveniente de una distribución exponencial f(t; lambda) = lambda e^(-lambda t). Deduzca analíticamente el estimador de máxima verosimilitud lambda_hat.
Paso 1: Función de verosimilitud: L(lambda) = prod_{i=1}^n lambda e^(-lambda t_i) = lambda^n exp(-lambda sum_{i=1}^n t_i).
Paso 2: Log-verosimilitud: ell(lambda) = ln L(lambda) = n ln(lambda) - lambda sum_{i=1}^n t_i.
Paso 3: Derivada con respecto a lambda: d ell / d lambda = (n / lambda) - sum_{i=1}^n t_i.
Paso 4: Igualando a cero: (n / lambda_hat) = sum_{i=1}^n t_i => lambda_hat = n / (sum t_i) = 1 / t̄.
Paso 5: Segunda derivada: d² ell / d lambda² = -n / lambda² < 0 para todo lambda > 0 (confirma máximo global). El estimador MLE es el recíproco de la media muestral.

Problema 2: En 8 paradas imprevistas de un turbogenerador, los tiempos de reparación en horas fueron: 4, 7, 2, 9, 3, 6, 5, 8. Calcule el valor numérico de lambda_hat [h⁻¹].
Paso 1: Suma sum t_i = 4 + 7 + 2 + 9 + 3 + 6 + 5 + 8 = 44 horas.
Paso 2: Media t̄ = 44 / 8 = 5.5 horas.
Paso 3: lambda_hat = 1 / 5.5 = 0.1818 h⁻¹ (tasa media de reparación: 0.18 reparaciones por hora).""",
        "bloque_sugerido": "Demostración Analítica 35 min • Deducción formal de MLE para parámetros de Weibull y Normal"
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "titulo": "Método de los Momentos (MoM) y Propiedades de los Estimadores",
        "objetivo": "Estimar parámetros mediante igualación de momentos poblacionales y muestrales evaluando insesgadez, consistencia y eficiencia asintótica.",
        "concepto_clave_latex": r"\mu_k(\boldsymbol{\theta}) = m_k \equiv \frac{1}{n}\sum_{i=1}^n X_i^k \quad ; \quad \text{Bias}(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta \quad ; \quad \text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \text{Bias}^2(\hat{\theta})",
        "ejemplo": """Problema 1: Sea una muestra x_1, ..., x_n de una distribución uniforme continua U(0, theta). Halle el estimador del método de los momentos theta_tilde, evalúe si es insesgado y calcule su error cuadrático medio MSE.
Paso 1: Momento poblacional: mu_1 = E[X] = theta / 2.
Paso 2: Momento muestral: m_1 = X̄.
Paso 3: Igualando mu_1 = m_1: theta / 2 = X̄ => theta_tilde = 2 X̄.
Paso 4: Insesgadez: E[theta_tilde] = E[2 X̄] = 2 E[X̄] = 2 (theta / 2) = theta. El sesgo es Bias = 0 (estimador insesgado).
Paso 5: Varianza: Var(X) = theta² / 12 => Var(X̄) = theta² / (12n).
Luego Var(theta_tilde) = Var(2 X̄) = 4 Var(X̄) = 4 theta² / (12n) = theta² / (3n).
Paso 6: Como Bias = 0, MSE(theta_tilde) = Var(theta_tilde) = theta² / (3n).

Problema 2: Compare theta_tilde con el estimador MLE theta_hat = X_{(n)} = max(X_i), cuya esperanza es E[X_{(n)}] = (n / (n+1)) theta y varianza Var(X_{(n)}) = n theta² / [(n+1)² (n+2)]. ¿Cuál es más eficiente asintóticamente?
Paso 1: Bias(theta_hat) = [n / (n+1) - 1] theta = -theta / (n+1).
Paso 2: MSE(theta_hat) = Var(theta_hat) + Bias² = n theta² / [(n+1)² (n+2)] + theta² / (n+1)² = 2 theta² / [(n+1)(n+2)] ≈ 2 theta² / n².
Paso 3: Como el MSE de theta_hat decae a orden O(1/n²) mientras que el de theta_tilde decae a O(1/n), el estimador MLE es infinitamente más eficiente que el método de los momentos para muestras grandes.""",
        "bloque_sugerido": "Comparativa de Estimadores 35 min • Evaluación de MSE y sesgo en distribuciones energéticas"
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "titulo": "Información de Fisher, Cota de Cramér-Rao y Estimadores UMVUE",
        "objetivo": "Calcular la información de Fisher de una muestra y verificar si un estimador alcanza la varianza mínima insesgada (UMVUE).",
        "concepto_clave_latex": r"\mathcal{I}_n(\theta) = n \mathbb{E}\left[\left(\frac{\partial \ln f(X;\theta)}{\partial \theta}\right)^2\right] = -n \mathbb{E}\left[\frac{\partial^2 \ln f(X;\theta)}{\partial \theta^2}\right] \quad ; \quad \text{Var}(\hat{\theta}) \ge \frac{1}{\mathcal{I}_n(\theta)}",
        "ejemplo": """Problema 1: Sea X ~ N(mu, sigma_0²) con varianza conocida sigma_0². Calcule la información de Fisher I_n(mu) y demuestre que la media muestral X̄ es un estimador de varianza mínima insesgado (UMVUE).
Paso 1: Densidad: f(x; mu) = (1 / (sigma_0 √(2pi))) exp(-(x - mu)² / (2 sigma_0²)).
Paso 2: ln f(x; mu) = -ln(sigma_0 √(2pi)) - (x - mu)² / (2 sigma_0²).
Paso 3: Primera derivada: d ln f / d mu = (x - mu) / sigma_0².
Paso 4: Segunda derivada: d² ln f / d mu² = -1 / sigma_0² (constante independiente de x).
Paso 5: Información de Fisher: I_n(mu) = -n E[-1 / sigma_0²] = n / sigma_0².
Paso 6: Cota inferior de Cramér-Rao (CRLB): Var(mu_hat) >= 1 / I_n(mu) = sigma_0² / n.
Paso 7: La varianza de X̄ es Var(X̄) = sigma_0² / n, la cual coincide exactamente con la CRLB. Por lo tanto, X̄ es UMVUE. Q.E.D.

Problema 2: Para una muestra de n = 25 sensores de temperatura con desviación instrumental sigma_0 = 0.4 °C, calcule la cota inferior de Cramér-Rao para estimar la temperatura media de la caldera.
Paso 1: CRLB = sigma_0² / n = (0.4)² / 25 = 0.16 / 25 = 0.0064 (°C)².
Paso 2: La menor desviación estándar alcanzable por cualquier estimador insesgado es √0.0064 = 0.080 °C.""",
        "bloque_sugerido": "Cálculo Teórico 35 min • Derivación de información de Fisher para distribuciones de Weibull y Rayleigh"
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "titulo": "Intervalos de Confianza para Dos Poblaciones: Diferencia de Medias y Cociente de Varianzas",
        "objetivo": "Construir intervalos de confianza para comparar el rendimiento energético promedio y la estabilidad de dos tecnologías renovables.",
        "concepto_clave_latex": r"(\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2, \nu} s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} \quad ; \quad s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2} \quad ; \quad \frac{s_1^2 / s_2^2}{F_{\alpha/2, \nu_1, \nu_2}} \le \frac{\sigma_1^2}{\sigma_2^2} \le \frac{s_1^2 / s_2^2}{F_{1-\alpha/2, \nu_1, \nu_2}}",
        "ejemplo": """Problema 1: Se comparan dos inversores fotovoltaicos (A y B) midiendo la eficiencia diaria durante n_1 = 12 días (A) y n_2 = 10 días (B). Se obtiene: x̄_A = 97.4%, s_A = 0.5%; x̄_B = 96.8%, s_B = 0.6%. Asumiendo varianzas poblacionales iguales, calcule el intervalo de confianza del 95% para la diferencia mu_A - mu_B.
Paso 1: Grados de libertad nu = 12 + 10 - 2 = 20.
Paso 2: Varianza mancomunada s_p² = [11(0.5)² + 9(0.6)²] / 20 = [11(0.25) + 9(0.36)] / 20 = [2.75 + 3.24] / 20 = 5.99 / 20 = 0.2995 (%²); s_p = 0.5473%.
Paso 3: Error estándar combinado: SE = s_p √(1/12 + 1/10) = 0.5473 × √(0.0833 + 0.1000) = 0.5473 × 0.4282 = 0.2343%.
Paso 4: t crítico: t_{0.025, 20} = 2.086.
Paso 5: Diferencia de medias: x̄_A - x̄_B = 97.4 - 96.8 = 0.60%.
Paso 6: Margen de error: ME = 2.086 × 0.2343% = 0.4888%.
Paso 7: IC 95%: [0.60 - 0.4888, 0.60 + 0.4888] = [0.111%, 1.089%].
Conclusión: Con 95% de confianza, el inversor A supera al inversor B entre 0.11% y 1.09% de eficiencia diaria.

Problema 2: Si el intervalo hubiese incluido el cero, ¿qué decisión de ingeniería se tomaría?
Paso 1: Si [L_1, L_2] contiene a 0, no existe evidencia estadística suficiente para preferir una tecnología sobre otra en términos de eficiencia media.""",
        "bloque_sugerido": "Laboratorio Estadístico 30 min • Comparación A/B de rendimiento térmico en paneles monocristalinos vs policristalinos"
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "titulo": "Pruebas de Hipótesis para Dos Muestras: Independientes y Pareadas",
        "objetivo": "Diseñar y ejecutar pruebas de hipótesis z y t para contrastar medias energéticas en muestras independientes y experimentos pareados antes/después.",
        "concepto_clave_latex": r"t_{\text{calc}} = \frac{(\bar{x}_1 - \bar{x}_2) - \Delta_0}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \quad ; \quad t_{\text{pareada}} = \frac{\bar{d} - \mu_d}{s_d / \sqrt{n}} \quad ; \quad d_i = x_{1i} - x_{2i}",
        "ejemplo": """Problema 1: Se evalúa un recubrimiento antirreflectante en n = 8 paneles solares midiendo la potencia máxima [W] antes y después de la aplicación:
Antes: [290, 295, 300, 288, 305, 292, 298, 302]
Después: [298, 303, 307, 295, 311, 300, 306, 309]
Pruebe con nivel de significancia alpha = 0.01 si el recubrimiento incrementa significativamente la potencia (H_0: mu_d <= 0 vs H_1: mu_d > 0).
Paso 1: Diferencias individuales d_i = Después - Antes:
d = [8, 8, 7, 7, 6, 8, 8, 7] W.
Paso 2: Media de diferencias: d̄ = (8+8+7+7+6+8+8+7) / 8 = 59 / 8 = 7.375 W.
Paso 3: Desviaciones (d_i - d̄): [0.625, 0.625, -0.375, -0.375, -1.375, 0.625, 0.625, -0.375].
Suma de cuadrados sum (d_i - d̄)² = 4(0.3906) + 3(0.1406) + 1.8906 = 1.5624 + 0.4218 + 1.8906 = 3.8748.
Paso 4: Varianza s_d² = 3.8748 / 7 = 0.5535; s_d = √0.5535 = 0.7440 W.
Paso 5: Error estándar: SE_d = 0.7440 / √8 = 0.7440 / 2.8284 = 0.2630 W.
Paso 6: Estadístico t: t_{calc} = 7.375 / 0.2630 = 28.04.
Paso 7: Valor crítico con nu = 7 y alpha = 0.01 (cola derecha): t_{0.01, 7} = 2.998.
Paso 8: Como t_{calc} = 28.04 >>> 2.998 (p-valor < 10⁻⁸), se rechaza rotundamente H_0. El recubrimiento produce una ganancia media confirmada de 7.38 W por panel.

Problema 2: ¿Por qué la prueba pareada es superior a una prueba para dos muestras independientes en este caso?
Paso 1: Porque elimina la variabilidad intrínseca de fábrica entre paneles, controlando el efecto del panel como su propio bloque experimental.""",
        "bloque_sugerido": "Resolución Aplicada 30 min • Contrastes pareados de pre-calentamiento en colectores solares térmicos"
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "titulo": "Análisis de Varianza (ANOVA) Unifactorial y Pruebas Post-Hoc de Tukey",
        "objetivo": "Descomponer la variabilidad total en tratamientos y error para comparar tres o más niveles de factor tecnológico mediante ANOVA y Tukey HSD.",
        "concepto_clave_latex": r"F = \frac{\text{MST}}{\text{MSE}} = \frac{\text{SST} / (k-1)}{\text{SSE} / (N-k)} \quad ; \quad \text{HSD} = q_{\alpha, k, N-k} \sqrt{\frac{\text{MSE}}{n}}",
        "ejemplo": """Problema 1: Se ensayan k = 3 fluidos de transferencia térmica en colectores cilindro-parabólicos (Aceite sintético, Sales fundidas, Agua presurizada), midiendo el calor útil absorbido [kW] en n = 5 réplicas por fluido:
Tratamiento 1 (Aceite): x̄_1 = 45 kW, s_1² = 4.0
Tratamiento 2 (Sales): x̄_2 = 52 kW, s_2² = 5.0
Tratamiento 3 (Agua): x̄_3 = 41 kW, s_3² = 3.0
Nivel de significancia alpha = 0.05. Ejecute la prueba ANOVA F.
Paso 1: Número total de observaciones N = 3 × 5 = 15; k = 3.
Paso 2: Media global x̄_G = (45 + 52 + 41) / 3 = 138 / 3 = 46.0 kW.
Paso 3: Suma de cuadrados entre tratamientos (SST):
SST = n sum_{i=1}^k (x̄_i - x̄_G)² = 5 [(45 - 46)² + (52 - 46)² + (41 - 46)²] = 5 [(-1)² + 6² + (-5)²] = 5 [1 + 36 + 25] = 5 × 62 = 310.0.
Paso 4: Cuadrado medio del tratamiento (MST): MST = SST / (k - 1) = 310.0 / (3 - 1) = 155.0.
Paso 5: Suma de cuadrados del error (SSE):
SSE = sum_{i=1}^k (n_i - 1) s_i² = 4(4.0) + 4(5.0) + 4(3.0) = 16 + 20 + 12 = 48.0.
Paso 6: Cuadrado medio del error (MSE): MSE = SSE / (N - k) = 48.0 / (15 - 3) = 48.0 / 12 = 4.0.
Paso 7: Estadístico F: F_{calc} = MST / MSE = 155.0 / 4.0 = 38.75.
Paso 8: Valor crítico F_{0.05, 2, 12} = 3.89.
Como F_{calc} = 38.75 > 3.89, se rechaza H_0: existen diferencias térmicas altamente significativas entre los fluidos.

Problema 2: Calcule la diferencia mínima significativa de Tukey HSD con q_{0.05, 3, 12} = 3.77.
Paso 1: HSD = q × √(MSE / n) = 3.77 × √(4.0 / 5) = 3.77 × √0.8 = 3.77 × 0.8944 = 3.37 kW.
Paso 2: Comparación |x̄_2 - x̄_1| = |52 - 45| = 7 > 3.37 (Sales vs Aceite: significativo).
Paso 3: Comparación |x̄_2 - x̄_3| = |52 - 41| = 11 > 3.37 (Sales vs Agua: significativo).
Paso 4: Comparación |x̄_1 - x̄_3| = |45 - 41| = 4 > 3.37 (Aceite vs Agua: significativo). Las tres medias difieren entre sí.""",
        "bloque_sugerido": "Taller Experimental 40 min • Construcción de tablas ANOVA completas en R/Python"
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "titulo": "Análisis de Varianza Bifactorial con Interacción en Procesos Industriales",
        "objetivo": "Evaluar efectos principales y términos de interacción entre dos factores de proceso (p. ej., temperatura y presión) sobre el rendimiento energético.",
        "concepto_clave_latex": r"y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk} \quad ; \quad \text{SS}_{\text{Total}} = \text{SS}_A + \text{SS}_B + \text{SS}_{AB} + \text{SS}_E",
        "ejemplo": """Problema 1: En un reactor de biomasa para síntesis de biocombustibles se analiza el rendimiento de gas [%] bajo a = 2 niveles de Temperatura (T_1 = 600°C, T_2 = 800°C) y b = 2 niveles de Catalizador (C_1 = Zeolita, C_2 = Níquel), con n = 4 réplicas por combinación. Los cuadrados medios calculados son: MS_A = 120.0, MS_B = 80.0, MS_{AB} = 32.0 y MSE = 4.0. Pruebe los efectos principales y la interacción al nivel alpha = 0.05.
Paso 1: Grados de libertad:
nu_A = a - 1 = 1; nu_B = b - 1 = 1; nu_{AB} = (a-1)(b-1) = 1; nu_E = ab(n - 1) = 2 × 2 × 3 = 12.
Paso 2: Valor crítico F_{0.05, 1, 12} = 4.75.
Paso 3: Prueba de interacción: F_{AB} = MS_{AB} / MSE = 32.0 / 4.0 = 8.0 > 4.75. Se rechaza H_{0,AB}: la interacción temperatura-catalizador es estadísticamente significativa.
Paso 4: Prueba de Temperatura (Factor A): F_A = MS_A / MSE = 120.0 / 4.0 = 30.0 > 4.75 (significativo).
Paso 5: Prueba de Catalizador (Factor B): F_B = MS_B / MSE = 80.0 / 4.0 = 20.0 > 4.75 (significativo).

Problema 2: ¿Cómo altera la presencia de interacción significativa la interpretación de los factores individuales?
Paso 1: Al existir interacción significativa, el efecto del tipo de catalizador depende críticamente del nivel térmico del reactor: no se deben recomendar catalizadores de forma aislada sin fijar la temperatura de operación.""",
        "bloque_sugerido": "Diseño de Experimentos 35 min • Gráficos de interacción en síntesis termoquímica de hidrógeno"
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "titulo": "Pruebas de Bondad de Ajuste: Chi-Cuadrado y Kolmogorov-Smirnov",
        "objetivo": "Evaluar formalmente si un conjunto de observaciones de velocidad de viento o radiación se ajusta a distribuciones teóricas de Weibull o Rayleigh.",
        "concepto_clave_latex": r"\chi^2_{\text{calc}} = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} \sim \chi^2(k - p - 1) \quad ; \quad D_n = \sup_{x} |F_n(x) - F_0(x)|",
        "ejemplo": """Problema 1: Se registran n = 200 observaciones horarias de radiación solar clasificadas en k = 5 intervalos de clase. Las frecuencias observadas son O = [30, 55, 60, 35, 20]. Bajo la hipótesis de ajuste a una distribución teórica con p = 1 parámetro estimado por MLE, las frecuencias esperadas son E = [25, 50, 65, 40, 20]. Contraste el ajuste con alpha = 0.05.
Paso 1: Grados de libertad: nu = k - p - 1 = 5 - 1 - 1 = 3.
Paso 2: Cálculo término a término (O_i - E_i)² / E_i:
Clase 1: (30 - 25)² / 25 = 25 / 25 = 1.000.
Clase 2: (55 - 50)² / 50 = 25 / 50 = 0.500.
Clase 3: (60 - 65)² / 65 = 25 / 65 = 0.385.
Clase 4: (35 - 40)² / 40 = 25 / 40 = 0.625.
Clase 5: (20 - 20)² / 20 = 0 / 20 = 0.000.
Paso 3: Estadístico chi²: chi²_{calc} = 1.000 + 0.500 + 0.385 + 0.625 + 0.000 = 2.510.
Paso 4: Valor crítico chi²_{0.05, 3} = 7.815.
Paso 5: Como chi²_{calc} = 2.510 < 7.815 (p-valor = 0.473), no se rechaza H_0: el modelo teórico describe adecuadamente la radiación solar observada.

Problema 2: En una prueba de Kolmogorov-Smirnov con n = 50 datos de velocidad de viento, la máxima discrepancia observada entre la función empírica F_n y la acumulada teórica F_0 es D_50 = 0.115. El valor crítico al 5% es D_{crit} = 1.36 / √50 = 1.36 / 7.071 = 0.192. Concluya.
Paso 1: D_50 = 0.115 < 0.192. Se acepta la hipótesis nula: no hay evidencia de divergencia frente al modelo eólico propuesto.""",
        "bloque_sugerido": "Ajuste de Distribuciones 35 min • Validación K-S de velocidades de viento con Scipy"
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "titulo": "Tablas de Contingencia y Prueba de Independencia Chi-Cuadrado",
        "objetivo": "Evaluar la independencia estadística entre variables categóricas de fallas en equipos y condiciones ambientales operativas.",
        "concepto_clave_latex": r"E_{ij} = \frac{R_i C_j}{N} \quad ; \quad \chi^2_{\text{calc}} = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2((r-1)(c-1))",
        "ejemplo": """Problema 1: Se auditan N = 300 fallas en transformadores según el tipo de clima (Costero vs Interior) y la causa principal (Sobrecarga, Aislamiento, Descarga atmosférica):
            Sobrecarga   Aislamiento   Descarga   Total
Costero         30           60           10       100
Interior        80           90           30       200
Total          110          150           40       300
Pruebe con alpha = 0.01 si la causa de falla es independiente de la ubicación geográfica.
Paso 1: Grados de libertad: nu = (2 - 1)(3 - 1) = 1 × 2 = 2.
Paso 2: Frecuencias esperadas E_{ij} = (Fila × Columna) / 300:
E_{11} = (100 × 110) / 300 = 36.67 ; E_{12} = (100 × 150) / 300 = 50.00 ; E_{13} = (100 × 40) / 300 = 13.33
E_{21} = (200 × 110) / 300 = 73.33 ; E_{22} = (200 × 150) / 300 = 100.00; E_{23} = (200 × 40) / 300 = 26.67
Paso 3: Cálculo de chi²:
(30 - 36.67)² / 36.67 = 44.49 / 36.67 = 1.213
(60 - 50.00)² / 50.00 = 100.0 / 50.00 = 2.000
(10 - 13.33)² / 13.33 = 11.09 / 13.33 = 0.832
(80 - 73.33)² / 73.33 = 44.49 / 73.33 = 0.607
(90 - 100.0)² / 100.0 = 100.0 / 100.0 = 1.000
(30 - 26.67)² / 26.67 = 11.09 / 26.67 = 0.416
Paso 4: chi²_{calc} = 1.213 + 2.000 + 0.832 + 0.607 + 1.000 + 0.416 = 6.068.
Paso 5: Valor crítico chi²_{0.01, 2} = 9.210.
Paso 6: Como chi²_{calc} = 6.068 < 9.210 (p-valor = 0.048 > 0.01), no se rechaza la independencia al nivel del 1% (aunque sí se rechazaría al 5%).

Problema 2: ¿Qué celda aportó mayor discrepancia relativa?
Paso 1: La celda de fallas de aislamiento en zona costera (E = 50, O = 60), atribuible a salinidad marina.""",
        "bloque_sugerido": "Análisis de Datos 30 min • Tabulación cruzada de incidentes en subestaciones de transmisión"
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "titulo": "Regresión Lineal Múltiple, Estimación Matricial y Coeficiente R² Ajustado",
        "objetivo": "Ajustar modelos de regresión lineal múltiple por álgebra matricial calculando coeficientes beta y coeficiente de determinación ajustado.",
        "concepto_clave_latex": r"\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \quad ; \quad R^2_{\text{adj}} = 1 - \left[\frac{(1 - R^2)(n - 1)}{n - p - 1}\right] \quad ; \quad \text{Cov}(\hat{\boldsymbol{\beta}}) = \sigma^2 (\mathbf{X}^T \mathbf{X})^{-1}",
        "ejemplo": """Problema 1: Se modela la potencia eléctrica P [MW] en función de la velocidad del viento v [m/s] y densidad del aire rho [kg/m³]. Tras estandarizar datos de n = 50 horas, se obtiene R² = 0.88 con p = 2 variables predictoras. Calcule R²_{adj} y el estadístico F global del modelo.
Paso 1: R²_{adj} = 1 - [(1 - 0.88)(50 - 1) / (50 - 2 - 1)] = 1 - [(0.12)(49) / 47] = 1 - [5.88 / 47] = 1 - 0.1251 = 0.8749 (87.49%).
Paso 2: Sumas relativas: SS_{reg} / SS_{tot} = 0.88; SS_{res} / SS_{tot} = 0.12.
Paso 3: F global = (R² / p) / [(1 - R²) / (n - p - 1)] = (0.88 / 2) / (0.12 / 47) = 0.44 / 0.002553 = 172.3.
Paso 4: Con F_{calc} = 172.3 >>> F_{0.01, 2, 47} ≈ 5.10, el modelo conjunto es altamente significativo.

Problema 2: En un modelo matricial y = X beta + epsilon con n = 4 y p = 1:
X^T X = [[4, 10], [10, 30]]; X^T y = [20, 65]^T. Halle el vector beta_hat.
Paso 1: Det(X^T X) = (4)(30) - (10)(10) = 120 - 100 = 20.
Paso 2: (X^T X)⁻¹ = (1/20) [[30, -10], [-10, 4]].
Paso 3: beta_hat = (1/20) [[30, -10], [-10, 4]] [20, 65]^T = (1/20) [30(20) - 10(65), -10(20) + 4(65)]^T = (1/20) [600 - 650, -200 + 260]^T = (1/20) [-50, 60]^T = [-2.5, 3.0]^T.
Paso 4: El modelo ajustado es y_hat = -2.5 + 3.0 x.""",
        "bloque_sugerido": "Modelado Matricial 40 min • Ajuste e inversión matricial en predicción de despacho térmico"
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "titulo": "Diagnóstico de Regresión: Multicolinealidad (VIF), Residuos y Homocedasticidad",
        "objetivo": "Validar supuestos de regresión evaluando factores de inflación de la varianza (VIF), homocedasticidad y normalidad de residuos.",
        "concepto_clave_latex": r"\text{VIF}_j = \frac{1}{1 - R_j^2} \quad ; \quad e_i = y_i - \hat{y}_i \quad ; \quad d = \frac{\sum_{i=2}^n (e_i - e_{i-1})^2}{\sum_{i=1}^n e_i^2} \quad [0 \le d \le 4]",
        "ejemplo": """Problema 1: En un modelo de predicción de carga eléctrica con 3 predictores (Temperatura T, Radiación G y Humedad Relativa H), se calcula la regresión auxiliar de T sobre G y H obteniendo R_T² = 0.85. Calcule el factor de inflación de varianza VIF_T y determine si existe multicolinealidad severa.
Paso 1: VIF_T = 1 / (1 - R_T²) = 1 / (1 - 0.85) = 1 / 0.15 = 6.67.
Paso 2: Criterio técnico: VIF > 5 indica multicolinealidad moderada-alta; VIF > 10 indica multicolinealidad severa.
Paso 3: La varianza del estimador beta_T está inflada 6.67 veces respecto al caso ortogonal; conviene evaluar regularización Ridge o componentes principales (PCA).

Problema 2: Los residuos sucesivos de un pronóstico horario de demanda e = [1.2, 1.0, 0.8, -0.2, -0.6] presentan sum e_i² = 3.28 y sum (e_i - e_{i-1})² = 0.04 + 0.04 + 1.00 + 0.16 = 1.24. Calcule el estadístico de Durbin-Watson d e interprete.
Paso 1: d = 1.24 / 3.28 = 0.378.
Paso 2: Como d está marcadamente por debajo de 2.0 (cercano a 0), existe una fuerte autocorrelación positiva en los residuos, violando el supuesto de independencia gaussiana.""",
        "bloque_sugerido": "Diagnóstico Estadístico 35 min • Gráficos residuales Q-Q y prueba Breusch-Pagan en Python"
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "titulo": "Regresión Logística y Clasificación Binaria de Eventos Críticos de Red",
        "objetivo": "Modelar la probabilidad de disparo de protecciones o contingencias mediante la función sigmoide y el modelo logit.",
        "concepto_clave_latex": r"p(\mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \boldsymbol{\beta}^T \mathbf{x})}} \quad ; \quad \text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \beta_0 + \sum_{j=1}^k \beta_j x_j \quad ; \quad \text{OR} = e^{\beta_j}",
        "ejemplo": """Problema 1: La probabilidad de disparo imprevisto de un transformador de potencia en función de la temperatura de aceite T [°C] se modela como: logit(p) = -8.0 + 0.10 T. Calcule la probabilidad de disparo cuando T = 70°C y cuando T = 90°C.
Paso 1: Para T = 70°C: z = -8.0 + 0.10(70) = -8.0 + 7.0 = -1.0.
p(70) = 1 / (1 + e^(-(-1.0))) = 1 / (1 + e^1) = 1 / (1 + 2.7183) = 1 / 3.7183 = 0.2689 (26.89%).
Paso 2: Para T = 90°C: z = -8.0 + 0.10(90) = -8.0 + 9.0 = +1.0.
p(90) = 1 / (1 + e^(-1.0)) = 1 / (1 + 0.3679) = 1 / 1.3679 = 0.7311 (73.11%).
Paso 3: Un aumento de 20°C en el aceite eleva la probabilidad de disparo del 26.9% al 73.1%.

Problema 2: Interprete el Odds Ratio (razón de momios) por cada incremento de 1°C en la temperatura.
Paso 1: OR = e^(beta_1) = e^(0.10) = 1.1052.
Paso 2: Por cada grado Celsius adicional, el momio de disparo se incrementa en un 10.52%.""",
        "bloque_sugerido": "Modelado de Clasificación 35 min • Matriz de confusión, curvas ROC y métrica AUC en fallas eléctricas"
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "titulo": "Series de Tiempo Energéticas: Estacionariedad, Autocorrelación y Modelos ARMA/ARIMA",
        "objetivo": "Evaluar la estacionariedad de perfiles de generación y demanda mediante funciones de autocorrelación (ACF) y formular modelos autorregresivos.",
        "concepto_clave_latex": r"\rho_k = \frac{\gamma_k}{\gamma_0} = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Var}(X_t)} \quad ; \quad X_t = c + \sum_{i=1}^p \phi_i X_{t-i} + \varepsilon_t + \sum_{j=1}^q \theta_j \varepsilon_{t-j} \quad ; \quad \varepsilon_t \sim \mathcal{WN}(0, \sigma^2)",
        "ejemplo": """Problema 1: Sea un proceso autorregresivo de primer orden AR(1) para la potencia eólica residual: X_t = 0.7 X_{t-1} + epsilon_t, donde epsilon_t es ruido blanco con varianza sigma_epsilon² = 4.0 MW². Halle la media E[X_t], la varianza gamma_0 = Var(X_t) y las primeras dos autocorrelaciones rho_1 y rho_2.
Paso 1: Media: E[X_t] = 0.7 E[X_{t-1}] => (1 - 0.7) E[X] = 0 => E[X_t] = 0.
Paso 2: Varianza: Var(X_t) = 0.7² Var(X_{t-1}) + Var(epsilon_t) = 0.49 gamma_0 + 4.0.
gamma_0 (1 - 0.49) = 4.0 => 0.51 gamma_0 = 4.0 => gamma_0 = 4.0 / 0.51 = 7.843 MW².
Paso 3: Autocorrelación lag 1: rho_1 = phi_1 = 0.70.
Paso 4: Autocorrelación lag 2: rho_2 = phi_1² = 0.7² = 0.49.

Problema 2: Verifique la condición de estacionariedad en sentido amplio para el modelo AR(1).
Paso 1: El polinomio característico es 1 - 0.7 z = 0 => raíz z = 1 / 0.7 = 1.4286.
Paso 2: Como |z| = 1.4286 > 1 (raíz fuera del círculo unitario complejo), el proceso es estrictamente estacionario.""",
        "bloque_sugerido": "Series Temporales 40 min • Pronóstico de demanda de 24 horas con modelos ARIMA en Python"
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "titulo": "Métodos de Remuestreo y Simulación Monte Carlo en Riesgo Energético",
        "objetivo": "Implementar simulaciones estocásticas de Monte Carlo para cuantificar pérdidas por interrupción y probabilidad de pérdida de carga (LOLP).",
        "concepto_clave_latex": r"\text{LOLP} = \frac{1}{M}\sum_{m=1}^M \mathbb{I}(L_m > G_m) \quad ; \quad \text{EENS} = \frac{8760}{M}\sum_{m=1}^M \max(0, L_m - G_m) \quad [\text{MWh/año}]",
        "ejemplo": """Problema 1: En una micro-red aislada se simulan M = 10,000 estados aleatorios del sistema para evaluar la suficiencia de generación. La demanda L sigue una distribución normal N(100 kW, 15² kW²) y la generación disponible G sigue una distribución con media 115 kW y varianza 400 kW². En 420 réplicas se detectó déficit de potencia (L > G). Calcule el índice de probabilidad de pérdida de carga LOLP y su intervalo de confianza al 95%.
Paso 1: Estimación puntual: LOLP_hat = 420 / 10,000 = 0.0420 (4.20%).
Paso 2: Error estándar de la simulación: SE = √[LOLP(1 - LOLP) / M] = √[(0.042)(0.958) / 10000] = √[0.040236 / 10000] = √[4.0236 × 10⁻⁶] = 0.002006 (0.201%).
Paso 3: Margen de error al 95% (z = 1.96): ME = 1.96 × 0.002006 = 0.00393.
Paso 4: IC 95%: [0.0420 - 0.00393, 0.0420 + 0.00393] = [0.0381, 0.0459] (entre 3.81% y 4.59%).

Problema 2: Si el déficit medio observado durante los estados de falla fue de 18 kW, estime la energía esperada no suministrada EENS anual.
Paso 1: Horas de déficit anuales: 8760 × LOLP = 8760 × 0.042 = 367.92 horas/año.
Paso 2: EENS = 367.92 h × 18 kW = 6,622.6 kWh/año = 6.62 MWh/año.""",
        "bloque_sugerido": "Simulación Numérica 40 min • Algoritmo Monte Carlo de despacho de reserva rodante"
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "titulo": "Confiabilidad de Sistemas Energéticos: Curva de la Bañera, MTTF y Disponibilidad",
        "objetivo": "Calcular tasas de falla, tiempo medio hasta la falla (MTTF), tiempo medio entre fallas (MTBF) y disponibilidad asintótica en plantas de generación.",
        "concepto_clave_latex": r"R(t) = e^{-\int_0^t \lambda(\tau)d\tau} \quad ; \quad \text{MTBF} = \text{MTTF} + \text{MTTR} \quad ; \quad A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} = \frac{\mu}{\lambda + \mu}",
        "ejemplo": """Problema 1: Un generador diésel de emergencia opera en su periodo de vida útil con tasa de falla constante lambda = 0.0004 fallas/hora (MTTF = 2,500 h) y tasa media de reparación mu = 0.05 reparaciones/hora (MTTR = 20 h). Calcule la disponibilidad intrínseca A, la indisponibilidad no forzada U y la confiabilidad a las 1,000 horas de operación continua R(1000).
Paso 1: MTTF = 1 / lambda = 1 / 0.0004 = 2,500 horas.
Paso 2: MTTR = 1 / mu = 1 / 0.05 = 20 horas.
Paso 3: Disponibilidad asintótica: A = MTTF / (MTTF + MTTR) = 2500 / (2500 + 20) = 2500 / 2520 = 0.99206 (99.21%).
Paso 4: Indisponibilidad: U = 1 - A = 20 / 2520 = 0.00794 (0.794%, equivalente a 69.5 horas de paro anual).
Paso 5: Confiabilidad a t = 1,000 h: R(1000) = e^(-lambda t) = e^(-0.0004 × 1000) = e^(-0.4) = 0.6703 (67.03%).

Problema 2: Para una configuración redundante en paralelo de dos generadores idénticos e independientes (cada uno con R = 0.6703), calcule la confiabilidad del sistema global R_sys(1000).
Paso 1: R_sys = 1 - (1 - R)² = 1 - (1 - 0.6703)² = 1 - (0.3297)² = 1 - 0.1087 = 0.8913 (89.13%).
Paso 2: La redundancia activa en paralelo reduce la probabilidad de colapso de la planta del 32.97% al 10.87%.""",
        "bloque_sugerido": "Ingeniería de Confiabilidad 35 min • Modelación RAMS (Reliability, Availability, Maintainability) en plantas solares"
    }
]

if __name__ == '__main__':
    from injector_base import format_topics_yaml
    yaml_text = format_topics_yaml(topics_03031818)
    inject_topics_after('      - codigo: "02031812"', yaml_text)
    print("03031818 Probabilidad y Estadística now has 30 topics!")

