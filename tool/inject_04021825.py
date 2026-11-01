# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_04021825 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Ecuaciones en Derivadas Parciales Parabólicas: Difusión Térmica y Separación de Variables",
        "objetivo": "Resolver analíticamente la ecuación de difusión del calor transitoria 1D en barras y medios semi-infinitos aplicando el método de separación de variables de Fourier y condiciones de frontera de Dirichlet y Neumann.",
        "concepto_clave_latex": r"\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2} \quad ; \quad T(x,t) = \sum_{n=1}^\infty C_n \sin\left(\frac{n\pi x}{L}\right) \exp\left(-\alpha \left(\frac{n\pi}{L}\right)^2 t\right)",
        "ejemplo": "Problema 1: Una barra cilíndrica de cobre de longitud $L = 0.5\\text{ m}$ ($\alpha = 1.11 \\times 10^{-4}\\text{ m}^2/\\text{s}$) tiene una distribución inicial uniforme de $T(x,0) = 100^\\circ\\text{C}$. En $t = 0$, ambos extremos se sumergen bruscamente en agua helada fijando $T(0,t) = T(L,t) = 0^\\circ\\text{C}$. Coeficientes de Fourier: $C_n = \\frac{2}{L}\\int_0^L 100 \\sin(n\\pi x / L) dx = \\frac{200}{n\\pi}[1 - (-1)^n]$. Para $n$ par, $C_n = 0$; para $n$ impar, $C_n = \\frac{400}{n\\pi}$. Para el modo fundamental ($n=1$): exponente temporal $\\lambda_1 = \\alpha (\\pi / L)^2 = 1.11 \\times 10^{-4} \\times (\\pi / 0.5)^2 = 1.11 \\times 10^{-4} \\times 39.478 = 4.382 \\times 10^{-3}\\text{ s}^{-1}$. Tiempo característico de enfriamiento: $\\tau = 1/\\lambda_1 = 228.2\\text{ segundos}$ ($~3.8\\text{ minutos}$). En el centro de la barra ($x = 0.25\\text{ m}$), tras 5 minutos ($t = 300\\text{ s}$): $T(0.25, 300) \\approx \\frac{400}{\\pi} \\sin(\\pi/2) e^{-4.382 \\times 10^{-3} \\times 300} = 127.32(1)(0.2686) = 34.2^\\circ\\text{C}$. Problema 2: En un estrato de suelo geotérmico semi-infinito sometido a oscilaciones térmicas estacionales de superficie $T_s(t) = T_0 + \\Delta T \\cos(\\omega t)$, la solución genera una onda de penetración amortiguada con desfase de profundidad $\\delta = \\sqrt{2\\alpha / \\omega}$.",
        "bloque_sugerido": "Ecuaciones Diferenciales 45 min • Separación de variables y convergencia de series de Fourier",
        "slides": [
            {
                "numero": 1,
                "seccion": "DIFUSIÓN PURA EN MEDIOS CONTINUOS",
                "titulo": "La Ecuación del Calor Parabólica",
                "puntos": [
                    "Modela procesos irreversibles gobernados por leyes de difusión macroscópica (conducción de Fourier, difusión molecular de Fick).",
                    "Propiedad de Suavizado: Cualquier discontinuidad inicial o perfil angular agudo se difumina exponencialmente en el tiempo.",
                    "Velocidad de propagación teórica infinita: Una perturbación en un extremo se siente matemáticamente de inmediato en todo el dominio."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONDICIONES DE BORDE",
                "titulo": "Dirichlet, Neumann y Robin",
                "puntos": [
                    "Dirichlet (Primer tipo): Temperatura superficial fijada por termostato ($T = T_0$).",
                    "Neumann (Segundo tipo): Flujo térmico fijado o superficie adiabática perfectamente aislada ($\\frac{\\partial T}{\\partial x} = 0$).",
                    "Robin (Tercer tipo): Convección natural o forzada con el fluido circundante ($-k \\frac{\\partial T}{\\partial x} = h(T - T_\\infty)$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "EDPs Hiperbólicas: Ecuación de Onda 1D y Solución de d'Alembert",
        "objetivo": "Resolver la ecuación de onda unidimensional para vibraciones en líneas de transmisión aéreas y oscilaciones acústicas mediante la solución analítica de d'Alembert de ondas viajeras.",
        "concepto_clave_latex": r"\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \quad ; \quad u(x,t) = f(x - c t) + g(x + c t) \quad ; \quad c = \sqrt{\frac{T_0}{\mu}}",
        "ejemplo": "Problema 1: Un conductor de fase aéreo de alta tensión (ACSR Drake, masa lineal $\\mu = 1.628\\text{ kg/m}$, tensión mecánica de tendido $T_0 = 35000\\text{ N}$) tiene una longitud de vano de $L = 400\\text{ m}$. Calcular la velocidad de propagación de ondas transversales $c$: $c = \\sqrt{\\frac{T_0}{\\mu}} = \\sqrt{\\frac{35000}{1.628}} = \\sqrt{21498.8} = 146.62\\text{ m/s}$. Si en $t = 0$ una descarga atmosférica de rayo impacta en el centro del vano ($x = 200\\text{ m}$) induciendo una deformación local inicial triangular $u(x,0)$, la solución de d'Alembert predice que el pulso se divide en dos ondas idénticas de semiamplitud que viajan en direcciones opuestas a $146.62\\text{ m/s}$. El tiempo que tarda la onda en alcanzar los aisladores de la torre de soporte en el extremo del vano es $t = \\frac{200\\text{ m}}{146.62\\text{ m/s}} = 1.364\\text{ segundos}$. Al llegar a la torre fija ($u(0,t)=0$), la onda se refleja invertida con cambio de signo ($-f$), retornando como onda de compresión. Problema 2: En vibraciones eólicas de conductores (aeolian vibrations a 10-50 Hz provocadas por desprendimiento de vórtices de von Kármán), se forman ondas estacionarias resonantes que rompen los hilos de aluminio por fatiga si no se instalan amortiguadores Stockbridge.",
        "bloque_sugerido": "Ondas y Mecánica 45 min • Método de d'Alembert y características espaciotemporales x-ct",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA ONDULATORIA HIPERBÓLICA",
                "titulo": "Conservación de la Forma de Onda",
                "puntos": [
                    "A diferencia de las ecuaciones parabólicas que disipan la energía, las ecuaciones hiperbólicas puras conservan la energía y la forma de la perturbación.",
                    "La información viaja estrictamente a velocidad finita $c$, definiendo conos de influencia y dominios de dependencia causales.",
                    "La solución general es la superposición de una onda progresiva hacia adelante $f(x-ct)$ y una onda regresiva hacia atrás $g(x+ct)$."
                ]
            },
            {
                "numero": 2,
                "seccion": "RESONANCIA EN SISTEMAS FINITOS",
                "titulo": "Modos Propios y Frecuencias Naturales",
                "puntos": [
                    "Con extremos fijos ($u=0$), la superposición de ondas viajeras incidentes y reflejadas genera ondas estacionarias.",
                    "Frecuencias de resonancia armónicas: $f_n = \\frac{n c}{2 L} = \\frac{n}{2 L}\\sqrt{\\frac{T_0}{\\mu}}$.",
                    "Fundamental para calcular resonancias mecánicas en álabes de turbinas eólicas y pulsaciones acústicas en tuberías de gas."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "EDPs Elípticas: Ecuaciones de Laplace y Poisson en Distribución de Potenciales",
        "objetivo": "Resolver la ecuación elíptica de Poisson $\\nabla^2 V = -\\rho_v / \\varepsilon$ en geometrías bidimensionales cartesianas y cilíndricas para el mapeo de líneas equipotenciales y gradientes de campo eléctrico en aisladores.",
        "concepto_clave_latex": r"\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = 0 \quad [\text{Laplace}] \quad ; \quad V(x,y) = \frac{1}{2\pi R}\oint V ds \quad [\text{Teorema del Valor Medio}]",
        "ejemplo": "Problema 1: Un canal rectangular bidimensional de ancho $a = 1.0\\text{ m}$ y altura infinita en $y$ tiene tres paredes conectadas a potencial de tierra: $V(0,y) = 0$, $V(a,y) = 0$, y $V(x,\\infty) = 0$. La placa inferior en $y = 0$ se mantiene a un potencial constante de $V(x,0) = V_0 = 1000\\text{ V}$. Separación de variables $V(x,y) = X(x)Y(y)$: $X''(x) + k^2 X(x) = 0 \\implies X_n(x) = \\sin(n\\pi x / a)$. $Y''(y) - k^2 Y(y) = 0 \\implies Y_n(y) = e^{-n\\pi y / a}$ (descartando $e^{+ky}$ para evitar divergencia en el infinito). Coeficientes de Fourier: $C_n = \\frac{4 V_0}{n\\pi}$ para $n$ impar. En el punto medio de la base ($x = 0.5\\text{ m}, y = 0.2\\text{ m}$): para $n=1$, $V_1 = \\frac{4000}{\\pi} \\sin(\\pi/2) e^{-\\pi(0.2)/1.0} = 1273.2(1) e^{-0.6283} = 1273.2(0.5335) = 679.3\\text{ V}$. Para $n=3$, $V_3 = \\frac{4000}{3\\pi} \\sin(3\\pi/2) e^{-3\\pi(0.2)} = -424.4(-1) e^{-1.885} = -424.4(-0.1518) = +64.4\\text{ V}$. Potencial aproximado: $V \\approx 679.3 + 64.4 = 743.7\\text{ V}$. Problema 2: El teorema del valor medio demuestra que el potencial en cualquier punto interior es exactamente el promedio de los potenciales circundantes; por ende, las funciones armónicas jamás poseen máximos ni mínimos locales en el interior del dominio (principio del extremo estricto).",
        "bloque_sugerido": "Campos Potenciales 45 min • Mapeo de líneas de flujo y relajación iterativa de Laplace",
        "slides": [
            {
                "numero": 1,
                "seccion": "EQUILIBRIO ESTACIONARIO ELÍPTICO",
                "titulo": "Funciones Armónicas y Suavidad Infinita",
                "puntos": [
                    "Modela estados estacionarios en equilibrio donde las derivadas temporales son cero (distribución de potencial electrostático, conducción térmica permanente).",
                    "Cualquier solución de la ecuación de Laplace es infinitamente diferenciable ($C^\\infty$) en el interior del dominio.",
                    "El potencial en todo el interior está unívocamente determinado por las condiciones en la frontera cerrada (Teorema de Unicidad)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONCENTRACIÓN DE GRADIENTES",
                "titulo": "Efecto de Puntas y Vértices Reentrantes",
                "puntos": [
                    "En esquinas exteriores afiladas con ángulo $\\theta$, el campo eléctrico $\\mathbf{E} = -\\nabla V$ tiende teóricamente a infinito ($E \\propto r^{\\frac{\\pi}{\\beta} - 1}$).",
                    "Explica la concentración crítica de gradientes dieléctricos en electrodos con bordes afilados.",
                    "Uso de perfiles de Rogowski y electrodos esféricos en alta tensión para mantener gradientes superficiales homogéneos."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Funciones Especiales en Ingeniería: Polinomios de Legendre y Funciones de Bessel",
        "objetivo": "Resolver ecuaciones diferenciales clásicas en coordenadas polares, cilíndricas y esféricas utilizando funciones de Bessel de primera y segunda especie ($J_m, Y_m$) y polinomios de Legendre ($P_n$).",
        "concepto_clave_latex": r"x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + (x^2 - m^2)y = 0 \implies y = C_1 J_m(x) + C_2 Y_m(x) \quad ; \quad (1-x^2)y'' - 2xy' + n(n+1)y = 0",
        "ejemplo": "Problema 1: Resolver la distribución radial de densidad de corriente $J(r)$ en un conductor cilíndrico de cobre sometido a corriente alterna a alta frecuencia (efecto pelicular). La ecuación diferencial en coordenadas cilíndricas se transforma en la ecuación de Bessel modificada con argumento complejo: $\\frac{d^2 J}{dr^2} + \\frac{1}{r}\\frac{dJ}{dr} - k^2 J = 0$, donde $k = \\sqrt{j\\omega\\mu\\sigma} = \\frac{1+j}{\\delta_s}$. Dado que la solución debe ser acotada y finita en el centro del cable ($r = 0$), se descarta la función de Bessel de segunda especie $Y_0$ (que diverge logarítmicamente hacia $-\\infty$ en el origen). La solución analítica exacta es la función de Kelvin-Bessel: $J(r) = J_{superficie} \\frac{J_0(k r)}{J_0(k R_0)} = J_{sup} \\frac{\\text{ber}(r/\\delta_s) + j\\text{bei}(r/\\delta_s)}{\\text{ber}(R_0/\\delta_s) + j\\text{bei}(R_0/\\delta_s)}$. Problema 2: En la distribución de temperatura en colectores solares esféricos, los polinomios de Legendre $P_n(\\cos\\theta)$ resuelven la ecuación angular, donde $P_0(x) = 1$, $P_1(x) = x$, $P_2(x) = \\frac{1}{2}(3x^2 - 1)$.",
        "bloque_sugerido": "Matemáticas Avanzadas 45 min • Ceros de funciones de Bessel y ortogonalidad en discos vibrantes",
        "slides": [
            {
                "numero": 1,
                "seccion": "COORDENADAS CURVILÍNEAS",
                "titulo": "De D'Alembert a Bessel y Legendre",
                "puntos": [
                    "Al aplicar separación de variables en coordenadas cilíndricas $(\\rho, \\phi, z)$, el factor radial produce la ecuación diferencial de Bessel.",
                    "En coordenadas esféricas $(r, \\theta, \\phi)$, el factor colatitudinal angular produce la ecuación diferencial de Legendre.",
                    "Constituyen bases ortogonales completas de funciones continuas para el análisis espectral en geometrías curvas."
                ]
            },
            {
                "numero": 2,
                "seccion": "PROPIEDADES DE ORTOGONALIDAD",
                "titulo": "Relaciones de Recurrencia y Raíces",
                "puntos": [
                    "Los ceros positivos $\\alpha_{m,n}$ de las funciones de Bessel ($J_m(\\alpha_{m,n}) = 0$) fijan las frecuencias nodales de resonancia de membranas circulares y guías de onda cilíndricas.",
                    "Ortogonalidad de Bessel: $\\int_0^R r J_m(\\alpha_i r/R) J_m(\\alpha_j r/R) dr = \\frac{R^2}{2}[J_{m+1}(\\alpha_i)]^2 \\delta_{ij}$.",
                    "Esencial para el modelado electromagnético de cables de potencia submarinos armados."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Transformada Rápida de Fourier (FFT) y Análisis en el Dominio de la Frecuencia",
        "objetivo": "Transformar señales temporales continuas y discretas hacia el dominio de la frecuencia, aplicando el algoritmo FFT de Cooley-Tukey con complejidad $O(N \\log N)$, ventanas de ponderación y filtrado espectral.",
        "concepto_clave_latex": r"X[k] = \sum_{n=0}^{N-1} x[n] W_N^{kn} \quad [W_N = e^{-j 2\pi / N}] \quad ; \quad f_k = \frac{k \cdot f_s}{N} \quad ; \quad \text{Resolución: } \Delta f = \frac{f_s}{N} = \frac{1}{T_{total}}",
        "ejemplo": "Problema 1: Un analizador DAQ muestrea la corriente de fase de un inversor solar fotovoltaico a una frecuencia de muestreo de $f_s = 10000\\text{ Hz}$ ($10\\text{ kHz}$) durante un tiempo de registro de $T = 0.20\\text{ segundos}$ ($N = f_s \\cdot T = 2000$ muestras). La resolución en frecuencia del espectro es: $\\Delta f = \\frac{1}{T} = \\frac{1}{0.20} = 5.0\\text{ Hz}$. La frecuencia de red fundamental a 60 Hz aparece exactamente en el bin discreto $k = \\frac{60}{5.0} = 12$. El quinto armónico ($300\\text{ Hz}$) aparece en el bin $k = \\frac{300}{5} = 60$, y el séptimo ($420\\text{ Hz}$) en $k = 84$. Si la señal temporal no se corta exactamente en un número entero de ciclos fundamentales, se produce fuga espectral ('spectral leakage'), donde la energía del pico de 60 Hz se desparrama hacia las frecuencias vecinas. Para mitigar la fuga, se multiplica la señal temporal por una ventana de Hanning: $w[n] = 0.5 - 0.5 \\cos(2\\pi n / N)$, reduciendo los lóbulos secundarios a $-31\\text{ dB}$. Problema 2: El algoritmo FFT reduce el número de multiplicaciones complejas para $N = 1024$ puntos de $N^2 = 1,048,576$ operaciones a solo $\\frac{N}{2}\\log_2 N = 512 \\times 10 = 5120$ operaciones (aceleración de 200 veces en tiempo de cómputo en DSPs).",
        "bloque_sugerido": "Procesamiento Digital 45 min • Implementación del algoritmo FFT radix-2 en Python y ventanas de Chebyshev",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE TIEMPO A FRECUENCIA",
                "titulo": "La Transformada Discreta de Fourier (DFT)",
                "puntos": [
                    "Proyecta una secuencia temporal finita de $N$ números sobre una base ortonormal de funciones sinusoidales complejas.",
                    "Teorema de Nyquist-Shannon: Para evitar solapamiento espectral (aliasing), la frecuencia de muestreo debe duplicar la máxima frecuencia física de la señal ($f_s > 2 f_{max}$).",
                    "Filtros analógicos antialiasing pasabajos antes del conversor ADC son mandatorios."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL ALGORITMO DE COOLEY-TUKEY",
                "titulo": "Divide y Vencerás (Radix-2)",
                "puntos": [
                    "Descompone una DFT de orden $N$ en dos DFTs independientes de orden $N/2$: una para las muestras pares y otra para las impares.",
                    "Aprovecha la periodicidad y simetría del factor de giro ('twiddle factor') $W_N^{k + N/2} = -W_N^k$.",
                    "Diagramas de flujo en mariposa (Butterfly operations) ejecutables en microsegundos en controladores de turbinas."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Transformada Z y Sistemas Dinámicos en Tiempo Discreto",
        "objetivo": "Modelar algoritmos de control digital y filtros digitales en tiempo discreto mediante la Transformada Z, evaluando la estabilidad asintótica a través de la ubicación de polos dentro del círculo unitario complejo $|z| < 1$.",
        "concepto_clave_latex": r"X(z) = \mathcal{Z}\{x[n]\} = \sum_{n=-\infty}^\infty x[n] z^{-n} \quad ; \quad z = e^{s T_s} \quad ; \quad |z| < 1 \iff \text{Re}(s) < 0 \ [\text{Estabilidad}]",
        "ejemplo": "Problema 1: Un lazo de control digital de velocidad para una turbina hidroeléctrica se implementa con un periodo de muestreo de $T_s = 50\\text{ ms}$ ($0.05\\text{ s}$). La función de transferencia en lazo cerrado discreto es: $H(z) = \\frac{0.15 z + 0.10}{z^2 - 1.4 z + 0.65}$. Determinar si el sistema es asintóticamente estable encontrando los polos de la ecuación característica: $z^2 - 1.4 z + 0.65 = 0$. Discriminante: $\\Delta = (-1.4)^2 - 4(1)(0.65) = 1.96 - 2.60 = -0.64$. Raíces complejas conjugadas: $z_{1,2} = \\frac{1.4 \\pm j\\sqrt{0.64}}{2} = 0.70 \\pm j 0.40$. Módulo de los polos: $|z| = \\sqrt{(0.70)^2 + (0.40)^2} = \\sqrt{0.49 + 0.16} = \\sqrt{0.65} \\approx 0.8062$. Como $|z| = 0.8062 < 1.0$, ambos polos se ubican estrictamente dentro del círculo unitario en el plano Z; por tanto, el sistema digital es Asintóticamente Estable. La respuesta temporal a un escalón es una oscilación amortiguada que converge a cero. Problema 2: Si el módulo fuera $|z| = 1.05 > 1$, la respuesta diverge exponencialmente al infinito, provocando el descontrol de la turbina.",
        "bloque_sugerido": "Control Digital 45 min • Criterio de estabilidad de Jury y mapeo bilineal con prewarping",
        "slides": [
            {
                "numero": 1,
                "seccion": "DISCRETIZACIÓN TEMPORAL",
                "titulo": "Mapeo del Plano S al Plano Z",
                "puntos": [
                    "El semiplano izquierdo de Laplace ($\text{Re}(s) < 0$, región estable continua) se mapea exactamente dentro del interior del círculo unitario ($|z| < 1$).",
                    "El eje imaginario $j\\omega$ (límite de oscilación sostenida) se convierte en la circunferencia unitaria $|z| = 1$.",
                    "El semiplano derecho inestable ($\text{Re}(s) > 0$) se proyecta en el exterior del círculo ($|z| > 1$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIO DE ESTABILIDAD DE JURY",
                "titulo": "Análogo Discreto de Routh-Hurwitz",
                "puntos": [
                    "Permite comprobar si todas las raíces de un polinomio característico $P(z)$ yacen dentro del círculo unitario sin calcular explícitamente las raíces complejas.",
                    "Evalúa condiciones necesarias: $P(1) > 0$ y $(-1)^n P(-1) > 0$.",
                    "Construye una tabla de coeficientes alternados determinando márgenes de estabilidad para reguladores PID digitales."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Cálculo Variacional y Ecuaciones de Euler-Lagrange en Sistemas Energéticos",
        "objetivo": "Formular problemas de optimización funcional dinámica mediante el principio de mínima acción de Hamilton y las ecuaciones de Euler-Lagrange, deduciendo leyes de conservación asociadas a simetrías (Teorema de Noether).",
        "concepto_clave_latex": r"J[y] = \int_{x_1}^{x_2} L(x, y, y') dx \implies \frac{\partial L}{\partial y} - \frac{d}{dx}\left(\frac{\partial L}{\partial y'}\right) = 0 \quad ; \quad H = y' \frac{\partial L}{\partial y'} - L = \text{const}",
        "ejemplo": "Problema 1: Encontrar la curva geométrica $y(x)$ que conecta dos puntos en un plano vertical a lo largo de la cual una partícula masiva desciende por gravedad sin fricción en el menor tiempo posible (Problema de la Braquistócrona). La velocidad instantánea por conservación de energía es $v = \\sqrt{2 g y}$. El tiempo total de descenso es el funcional $T[y] = \\int \\frac{ds}{v} = \\int_{x_1}^{x_2} \\frac{\\sqrt{1 + (y')^2}}{\\sqrt{2 g y}} dx$. Como el lagrangiano $L(y, y') = \\sqrt{\\frac{1 + (y')^2}{y}}$ no depende explícitamente de $x$ ($\\partial L / \\partial x = 0$), se aplica la segunda forma canónica de Euler (identidad de Beltrami): $L - y' \\frac{\\partial L}{\\partial y'} = C$. Sustituyendo y simplificando: $y [1 + (y')^2] = 2 R = \\text{const}$. La solución paramétrica analítica exacta es una cicloide generada por una rueda rodante: $x = R(\\theta - \\sin\\theta)$, $y = R(1 - \\cos\\theta)$. Problema 2: En el diseño aerodinámico de palas de aerogeneradores, el cálculo variacional determina la distribución óptima de cuerda y ángulo de torsión ('twist angle') a lo largo de la pala que maximiza el coeficiente de potencia aerodinámico $C_p$.",
        "bloque_sugerido": "Mecánica Analítica 45 min • Ecuaciones de Hamilton y teorema de Noether en sistemas electromecánicos",
        "slides": [
            {
                "numero": 1,
                "seccion": "OPTIMIZACIÓN DE FUNCIONALES",
                "titulo": "Del Cálculo Numérico a los Extremos de Curvas",
                "puntos": [
                    "En cálculo tradicional se halla el punto $x^*$ que minimiza una función $f(x)$; en cálculo variacional se halla la función entera $y^*(x)$ que minimiza una integral de camino $J[y]$.",
                    "Principio de Hamilton: La trayectoria real que sigue cualquier sistema físico es aquella que estacionariza la acción $S = \\int (T - V) dt$.",
                    "Permite formular ecuaciones dinámicas de mecanismos complejos con restricciones sin necesidad de calcular fuerzas de reacción de enlace."
                ]
            },
            {
                "numero": 2,
                "seccion": "TEOREMA DE EMMY NOETHER",
                "titulo": "Simetría Implica Conservación",
                "puntos": [
                    "Invarianza bajo traslaciones temporales ($\\partial L / \\partial t = 0$) $\\implies$ Conservación estricta de la Energía total.",
                    "Invarianza bajo traslaciones espaciales $\\implies$ Conservación de la Cantidad de Movimiento lineal.",
                    "Invarianza bajo rotaciones angulares $\\implies$ Conservación del Momento Angular.",
                    "Fundamento teórico unificador de la física y la ingeniería moderna."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Método de Elementos Finitos (FEM): Formulación Débil de Galerkin en 1D y 2D",
        "objetivo": "Discretizar ecuaciones diferenciales de segundo orden con condiciones de contorno complejas mediante la formulación variacional débil de Galerkin sobre mallas de elementos lineales y triangulares.",
        "concepto_clave_latex": r"\int_\Omega \left( k \nabla T \cdot \nabla v \right) d\Omega = \int_\Omega Q v d\Omega + \oint_{\partial \Omega} q_n v d\Gamma \quad \implies \quad \mathbf{K}\mathbf{T} = \mathbf{F}",
        "ejemplo": "Problema 1: Resolver la distribución de temperatura unidimensional en una aleta de enfriamiento de sección uniforme ($L = 0.1\\text{ m}$, $k A = 2.0\\text{ W m/K}$, $h P = 8.0\\text{ W/(m K)}$) cuya ecuación de gobierno es: $k A \\frac{d^2 T}{dx^2} - h P (T - T_\\infty) = 0$, con base fija a $T(0) = 100^\\circ\\text{C}$ y extremo adiabático ($T'(L) = 0$). Se discretiza la aleta en dos elementos lineales finitos de longitud $l = 0.05\\text{ m}$ (3 nodos: $x_1 = 0, x_2 = 0.05, x_3 = 0.1$). Matriz de rigidez de conducción para cada elemento: $K_c^e = \\frac{k A}{l} \\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\frac{2.0}{0.05}\\begin{pmatrix} 1 & -1 \\\\ -1 & 1 \\end{pmatrix} = \\begin{pmatrix} 40 & -40 \\\\ -40 & 40 \\end{pmatrix}$. Matriz de convección: $K_h^e = \\frac{h P l}{6} \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} = \\frac{8.0 \\times 0.05}{6} \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} = \\begin{pmatrix} 0.133 & 0.067 \\\\ 0.067 & 0.133 \\end{pmatrix}$. Ensamblando la matriz global $3 \\times 3$ e imponiendo la condición de Dirichlet en el nodo 1 ($T_1 = 100^\\circ\\text{C}$): se resuelve el sistema lineal de 2 ecuaciones para los nodos interiores $T_2$ y $T_3$, obteniendo $T_2 = 72.4^\\circ\\text{C}$ y $T_3 = 64.8^\\circ\\text{C}$ (error menor al $0.8\\%$ respecto a la solución analítica hiperbólica exacta). Problema 2: En 2D, los elementos triangulares planos con funciones de forma lineales $N_i(x,y) = a_i + b_i x + c_i y$ resuelven la transferencia de calor en colectores solares térmicos con contornos irregulares.",
        "bloque_sugerido": "Simulación Numérica 45 min • Ensamble de matrices de rigidez y cálculo variacional en Python con NumPy",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE LA FORMA FUERTE A LA DÉBIL",
                "titulo": "Integración por Partes y Reducción de Orden",
                "puntos": [
                    "Forma Fuerte: Requiere que la función sea dos veces diferenciable en cada punto del dominio ($C^2$).",
                    "Forma Débil: Multiplica por una función de prueba arbitraria $v(x)$ e integra por partes; rebaja la exigencia de continuidad a solo primer orden ($C^0$ / espacio de Sobolev $H^1$).",
                    "Incorpora de manera natural las condiciones de contorno de flujo (Neumann y Robin) directamente en el vector de carga $\\mathbf{F}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "FUNCIONES DE FORMA NODALES",
                "titulo": "Interpolación Polinomial Local",
                "puntos": [
                    "El dominio se subdivide en submallas de elementos geométricos simples (triángulos, cuadriláteros, tetraedros).",
                    "Las funciones de base nodales valen $1.0$ en su propio nodo y $0.0$ en todos los demás nodos ($N_i(x_j) = \\delta_{ij}$).",
                    "La matriz global de rigidez resultante $\\mathbf{K}$ es rala (sparse), simétrica y definida positiva, solucionable por Cholesky."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Método de Volúmenes Finitos (FVM) y Algoritmo SIMPLE en CFD",
        "objetivo": "Discretizar las ecuaciones integrales de Navier-Stokes y transporte convectivo-difusivo mediante Volúmenes Finitos (FVM), resolviendo el acoplamiento presión-velocidad mediante el algoritmo SIMPLE.",
        "concepto_clave_latex": r"\oint_{\partial V} \rho \phi \mathbf{v} \cdot d\mathbf{A} = \oint_{\partial V} \Gamma_\phi \nabla \phi \cdot d\mathbf{A} + \int_V S_\phi dV \quad ; \quad a_P \phi_P = \sum a_{nb} \phi_{nb} + b",
        "ejemplo": "Problema 1: Formular la discretización 1D del transporte convectivo-difusivo estacionario en una celda de control centrada en el nodo $P$ con vecinos $W$ (Oeste) y $E$ (Este): $\\frac{d}{dx}(\\rho u \\phi) = \\frac{d}{dx}\\left(\\Gamma \\frac{d\\phi}{dx}\\right)$. Flujos convectivos en las caras: $F_e = (\\rho u)_e$, $F_w = (\\rho u)_w$. Conductancias difusivas: $D_e = \\Gamma_e / \\Delta x$, $D_w = \\Gamma_w / \\Delta x$. Número de Péclet de celda: $Pe = F/D = \\frac{\\rho u \\Delta x}{\\Gamma}$. Si $Pe > 2$, el esquema de diferencias centrales tradicional produce oscilaciones espaciales no físicas y divergencia numérica violenta. El esquema Upwind (viento arriba) asigna el valor de la cara según el sentido del flujo ($u > 0 \\implies \\phi_e = \\phi_P$), garantizando positividad estricta de los coeficientes de la matriz y estabilidad incondicional. Problema 2: En flujo incompresible, la presión no tiene una ecuación de estado propia; el algoritmo SIMPLE (Semi-Implicit Method for Pressure-Linked Equations de Patankar) deduce una ecuación de corrección de presión $P'$ que impone el cumplimiento estricto de la ecuación de continuidad $\\nabla \\cdot \\mathbf{v} = 0$.",
        "bloque_sugerido": "Dinámica de Fluidos Computacional 45 min • Implementación del algoritmo SIMPLE en un canal escalonado 2D",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONSERVACIÓN LOCAL ESTRICTA",
                "titulo": "La Filosofía del Volumen de Control",
                "puntos": [
                    "A diferencia de FEM, el FVM se basa directamente en la formulación integral de las leyes de conservación física sobre cada celda de volumen.",
                    "El flujo numérico que abandona una celda por su cara Este entra idénticamente en la celda vecina por su cara Oeste.",
                    "Garantiza conservación exacta de masa, momento y energía incluso sobre mallas gruesas o deformadas."
                ]
            },
            {
                "numero": 2,
                "seccion": "ACOPLAMIENTO PRESIÓN-VELOCIDAD",
                "titulo": "El Ciclo Iterativo SIMPLE",
                "puntos": [
                    "1. Estimar un campo de presiones inicial $P^*$.",
                    "2. Resolver las ecuaciones de momento para obtener velocidades intermedias $u^*, v^*$.",
                    "3. Resolver la ecuación de corrección de presión $P'$ para forzar la conservación de masa.",
                    "4. Corregir velocidades y presiones y avanzar al siguiente paso de iteración hasta convergencia de residuos."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Sistemas Dinámicos No Lineales, Bifurcaciones y Caos en Redes Eléctricas",
        "objetivo": "Modelar la dinámica no lineal en sistemas de potencia mediante mapas de bifurcación (nodo-silla, Hopf y duplicación de periodo), calculando exponentes de Lyapunov para detectar inestabilidad de voltaje.",
        "concepto_clave_latex": r"\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mu) \quad ; \quad \det(J(x^*, \mu)) = 0 \ [\text{Saddle-Node}] \quad ; \quad \lambda_L = \lim_{t\to\infty} \frac{1}{t}\ln\left(\frac{\|\delta \mathbf{x}(t)\|}{\|\delta \mathbf{x}_0\|}\right) > 0 \ [\text{Caos}]",
        "ejemplo": "Problema 1: Un sistema eléctrico simple de dos barras alimenta una carga con demanda reactiva creciente $Q_L$. Las ecuaciones de flujo de potencia no lineales determinan las trayectorias de equilibrio de tensión. A medida que se incrementa el parámetro de bifurcación $\\mu = Q_L$, la solución de tensión alta operativa y la solución inestable de baja tensión se aproximan progresivamente en la curva P-V (curva en 'nariz'). En el punto crítico de máxima transferencia de potencia (la nariz de la curva), la matriz Jacobiana del flujo de potencia se vuelve singular: $\\det(J) = 0$, ocurriendo una Bifurcación Nodo-Silla (Saddle-Node Bifurcation, SNB). Cualquier incremento infinitesimal en la demanda más allá de este punto hace desaparecer todos los puntos de equilibrio reales; el voltaje colapsa dinámicamente en una caída catastrófica (Voltage Collapse). Problema 2: En convertidores conmutados de potencia DC/DC operando a alta frecuencia en modo de conducción discontinua, una variación en el ciclo de trabajo desencadena bifurcaciones de Hopf seguidas de cascada de duplicación de periodo de Feigenbaum hacia comportamiento caótico determinista con exponente de Lyapunov positivo $\\lambda_L > 0$.",
        "bloque_sugerido": "Dinámica No Lineal 45 min • Trazado de diagramas de bifurcación y órbitas en el atractor de Lorenz",
        "slides": [
            {
                "numero": 1,
                "seccion": "TIPOLOGÍAS DE BIFURCACIÓN",
                "titulo": "Cambios Cualitativos de Estabilidad",
                "puntos": [
                    "Una bifurcación ocurre cuando una variación suave de un parámetro físico $(\\mu)$ altera bruscamente el número o la estabilidad de los puntos de equilibrio.",
                    "Bifurcación Nodo-Silla (SNB): Fusión y aniquilación mutua de un equilibrio estable y uno inestable; causa primaria de colapsos de tensión en redes eléctricas.",
                    "Bifurcación de Hopf: Un par de autovalores complejos cruza el eje imaginario al semiplano derecho; un punto fijo estable se transforma en una oscilación de ciclo límite autoexcitada continua."
                ]
            },
            {
                "numero": 2,
                "seccion": "SENSIBILIDAD A CONDICIONES INICIALES",
                "titulo": "Caos Determinista",
                "puntos": [
                    "Comportamiento aperiódico irregular generado por ecuaciones completamente deterministas sin ruido estocástico externo.",
                    "Exponente de Lyapunov $\\lambda_L > 0$: Dos trayectorias con condiciones iniciales separadas una distancia infinitesimal $\\delta x_0$ divergen exponencialmente en el tiempo.",
                    "Pérdida de predictibilidad a largo plazo en modelos meteorológicos de predicción de viento y radiación solar."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Planos de Fase, Retratos Modales y Teorema de Hartman-Grobman",
        "objetivo": "Clasificar la estabilidad local y topología de puntos de equilibrio en sistemas dinámicos autónomos no lineales 2D mediante linealización jacobiana, trazando retratos de fase y separatrices.",
        "concepto_clave_latex": r"J = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{pmatrix} \quad ; \quad \tau = \text{tr}(J), \ \Delta = \det(J) \quad ; \quad \lambda^2 - \tau\lambda + \Delta = 0",
        "ejemplo": "Problema 1: Analizar la dinámica angular de un generador síncrono conectado a una barra infinita (ecuación de oscilación no lineal de swing): $\\frac{d\delta}{dt} = \\omega$, $\\frac{d\omega}{dt} = \\frac{1}{M}[P_m - P_{max}\\sin\\delta]$. Sean $P_m = 0.5\\text{ p.u.}$, $P_{max} = 1.0\\text{ p.u.}$, $M = 0.1\\text{ s}^2$. Puntos de equilibrio ($\\omega = 0, \\sin\\delta = 0.5$): 1) $\\delta_1^* = 30^\\circ = \\pi/6\\text{ rad}$. Jacobiano en $\\delta_1^*$: $J = \\begin{pmatrix} 0 & 1 \\\\ -\\frac{P_{max}\\cos(\\pi/6)}{M} & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 1 \\\\ -8.66 & 0 \\end{pmatrix}$. Trazas y determinante: $\\tau = 0, \\Delta = 8.66 > 0$. Autovalores: $\\lambda_{1,2} = \\pm j 2.943\\text{ rad/s}$ (imaginarios puros). Con amortiguamiento físico real ($D > 0$), los autovalores adquieren parte real negativa, clasificando el punto como un Foco Estable (atractor espiral donde el generador converge a régimen permanente). 2) $\\delta_2^* = 150^\\circ = 5\\pi/6\\text{ rad}$. Jacobiano: $\\cos(150^\\circ) = -0.866 \\implies J = \\begin{pmatrix} 0 & 1 \\\\ +8.66 & 0 \\end{pmatrix}$. Determinante: $\\Delta = -8.66 < 0$. Autovalores: $\\lambda_{1,2} = \\pm 2.943\\text{ s}^{-1}$ (uno real positivo y uno real negativo). Clasificación: Punto de Silla (Saddle Point inestable). La trayectoria que entra hacia el punto de silla define la separatriz de estabilidad transitoria; si una falla mantiene el ángulo más allá del ángulo crítico de despeje $\\delta_{crit}$, el generador cruza la separatriz y pierde sincronismo irremediablemente (polo deslizado). Problema 2: Por el Teorema de Hartman-Grobman, el comportamiento topológico en una vecindad abierta del equilibrio hiperbólico no lineal es homeomorfo a su linealización.",
        "bloque_sugerido": "Sistemas Dinámicos 45 min • Trazado de campos vectoriales en plano de fase con Matplotlib y scipy.integrate",
        "slides": [
            {
                "numero": 1,
                "seccion": "TOPOLOGÍA EN EL PLANO DE FASE",
                "titulo": "Clasificación Espectral de Poincaré",
                "puntos": [
                    "Nodo Estable: $\\Delta > 0, \\tau < 0, \\tau^2 - 4\\Delta \\ge 0$ (autovalores reales negativos; atracción monótona directa).",
                    "Foco Estable: $\\Delta > 0, \\tau < 0, \\tau^2 - 4\\Delta < 0$ (autovalores complejos con parte real negativa; oscilaciones amortiguadas espirales).",
                    "Punto de Silla (Saddle): $\\Delta < 0$ (un autovalor positivo y uno negativo; inestable; atrae en una dirección y repele en todas las demás).",
                    "Centro: $\\tau = 0, \\Delta > 0$ (órbitas cerradas periódicas no amortiguadas; sistemas conservativos)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIO DE IGUALDAD DE ÁREAS",
                "titulo": "Estabilidad Transitoria en Máquinas",
                "puntos": [
                    "El plano de fase $\\delta - \\omega$ visualiza directamente el Criterio de Áreas de sistemas de potencia.",
                    "Área de aceleración durante el cortocircuito: Energía cinética transitoria absorbida por el rotor.",
                    "Área de desaceleración tras el despeje: Máxima energía potencial magnética que la red puede absorber antes de que el ángulo supere el punto de silla inestable."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Teoría de Perturbaciones Asintóticas y Métodos de Capa Límite",
        "objetivo": "Resolver ecuaciones diferenciales no lineales con parámetros perturbativos pequeños $\\varepsilon \\ll 1$, implementando expansiones asintóticas regulares y métodos de capa límite singular (soluciones interna y externa acopladas).",
        "concepto_clave_latex": r"\varepsilon y''(x) + y'(x) + y(x) = 0 \quad [\varepsilon \to 0^+] \quad ; \quad y(x) \approx y_{ext}(x) + y_{int}(x/\varepsilon) - y_{comun}",
        "ejemplo": "Problema 1: Resolver el problema de contorno con perturbación singular: $\\varepsilon y''(x) + y'(x) = 2x$ en $x \\in [0, 1]$ con condiciones de frontera $y(0) = 1$ y $y(1) = 4$, donde $\\varepsilon = 0.01 \\ll 1$. Solución Externa (fuera de la capa límite, despreciando $\\varepsilon y''$): $y_{ext}'(x) = 2x \\implies y_{ext}(x) = x^2 + C$. Imponiendo la frontera derecha $y_{ext}(1) = 4 \\implies 1^2 + C = 4 \\implies C = 3$. Así: $y_{ext}(x) = x^2 + 3$. Esta solución viola la condición izquierda ($y_{ext}(0) = 3 \\ne 1$), revelando la existencia de una capa límite estrecha de espesor $O(\\varepsilon)$ en $x = 0$. Solución Interna: Introduciendo la variable estirada $\\tilde{x} = x/\\varepsilon$: $\\frac{d^2 Y}{d\\tilde{x}^2} + \\frac{dY}{d\\tilde{x}} = 0 \\implies Y(\\tilde{x}) = A + B e^{-\\tilde{x}}$. Con $Y(0) = 1 \\implies A + B = 1$. Acoplamiento asintótico de Prandtl: $\\lim_{\\tilde{x} \\to \\infty} Y(\\tilde{x}) = \\lim_{x \\to 0} y_{ext}(x) \\implies A = 3 \\implies B = -2$. Solución compuesta uniforme para todo $x \\in [0, 1]$: $y(x) = (x^2 + 3) - 2 e^{-x/\\varepsilon}$. Para $\\varepsilon = 0.01$, a una distancia de apenas $x = 0.05$ (5 veces el espesor de capa), la exponencial cae a $e^{-5} \\approx 0.0067$, convergiendo idénticamente con la solución externa. Problema 2: En la mecánica de fluidos de Prandtl para álabes de turbinas eólicas, este método separa el flujo potencial no viscoso exterior de la delgada capa límite viscosa adyacente a la superficie de la pala.",
        "bloque_sugerido": "Matemática Asintótica 45 min • Expansiones asintóticas de Poincaré y acoplamiento de capas límite",
        "slides": [
            {
                "numero": 1,
                "seccion": "PERTURBACIONES REGULARES VS SINGULARES",
                "titulo": "La Pérdida del Orden de la Ecuación",
                "puntos": [
                    "Perturbación Regular: El parámetro pequeño $\\varepsilon$ multiplica términos de orden inferior; la solución es una serie de potencias suave: $y(x) = y_0(x) + \\varepsilon y_1(x) + \\dots$.",
                    "Perturbación Singular: El parámetro $\\varepsilon$ multiplica la derivada de mayor orden; al hacer $\\varepsilon \\to 0$, el orden de la EDO colapsa, imposibilitando satisfacer todas las condiciones de frontera.",
                    "Provoca gradientes espaciales extremos confinados en regiones micrométricas (capas límite térmicas, electrodos electroquímicos)."
                ]
            },
            {
                "numero": 2,
                "seccion": "MÉTODO DE ESCALAS MÚLTIPLES (WKB)",
                "titulo": "Oscilaciones Lentas y Rápidas",
                "puntos": [
                    "En sistemas oscilatorios no lineales (como el oscilador de Van der Pol), las perturbaciones inducen variaciones lentas en la amplitud y fase sobre miles de periodos rápidos.",
                    "El método de escalas múltiples desacopla el tiempo rápido $t_0 = t$ del tiempo lento $t_1 = \\varepsilon t$.",
                    "Elimina los términos seculares divergentes ($t \\cos t$) que arruinan las series de Taylor ordinarias."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Optimización Lineal (Método Simplex) y Dualidad en Sistemas Energéticos",
        "objetivo": "Formular y resolver problemas de asignación óptima de recursos energéticos mediante Programación Lineal (LP), aplicando el método Simplex en forma matricial, análisis de sensibilidad y precios sombra duales.",
        "concepto_clave_latex": r"\min_{\mathbf{x}} \mathbf{c}^T \mathbf{x} \quad \text{s.t.} \quad \mathbf{A}\mathbf{x} \le \mathbf{b}, \ \mathbf{x} \ge \mathbf{0} \quad \iff \quad \max_{\mathbf{y}} \mathbf{b}^T \mathbf{y} \quad \text{s.t.} \quad \mathbf{A}^T \mathbf{y} \le \mathbf{c}, \ \mathbf{y} \ge \mathbf{0}",
        "ejemplo": "Problema 1: Un sistema híbrido aislado debe cubrir una demanda continua de $100\\text{ MW}$ combinando energía solar ($x_1$) y una central térmica diésel ($x_2$). Costo de generación solar: $c_1 = 30\\text{ USD/MWh}$; costo diésel: $c_2 = 120\\text{ USD/MWh}$. Restricciones físicas: Disponibilidad solar máxima al mediodía: $x_1 \\le 60\\text{ MW}$. Capacidad diésel máxima: $x_2 \\le 80\\text{ MW}$. Balance de demanda: $x_1 + x_2 = 100\\text{ MW}$. Función objetivo: Minimizar $Z = 30 x_1 + 120 x_2$. El algoritmo Simplex selecciona la base óptima saturando la fuente más económica: $x_1^* = 60\\text{ MW}$, $x_2^* = 40\\text{ MW}$. Costo total horario óptimo: $Z^* = 30(60) + 120(40) = 1800 + 4800 = 6600\\text{ USD/h}$. Analizando el problema dual: La variable dual asociada a la restricción de demanda es $y_{demanda}^* = 120\\text{ USD/MWh}$ (el costo marginal de la última unidad despachada). La variable dual asociada al límite solar es $y_{solar}^* = 30 - 120 = -90\\text{ USD/MWh}$ (precio sombra que indica que cada megavatio adicional de capacidad solar que se instale reducirá el costo del sistema en 90 USD por hora). Problema 2: Por el Teorema de Dualidad Fuerte, el valor óptimo del primal coincide exactamente con el valor óptimo del dual: $\\mathbf{c}^T \\mathbf{x}^* = \\mathbf{b}^T \\mathbf{y}^*$.",
        "bloque_sugerido": "Investigación de Operaciones 45 min • Algoritmo Simplex matricial en Python con SciPy Optimize",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROGRAMACIÓN LINEAL MATRICIAL",
                "titulo": "Geometría del Politopo Convexo",
                "puntos": [
                    "El conjunto factible delimitado por restricciones lineales de desigualdad forma un politopo convexo cerrado en $\\mathbb{R}^n$.",
                    "Teorema Fundamental de la Programación Lineal: La solución óptima se encuentra siempre en uno de los vértices (soluciones básicas factibles) del politopo.",
                    "El algoritmo Simplex de George Dantzig navega eficientemente de un vértice adyacente a otro a lo largo de las aristas en dirección de máximo gradiente de mejora."
                ]
            },
            {
                "numero": 2,
                "seccion": "TEORÍA DE DUALIDAD Y PRECIOS SOMBRA",
                "titulo": "La Economía Oculta del Dual",
                "puntos": [
                    "A cada restricción física del problema primal (capacidad de líneas de transmisión, cuotas de agua de embalses) le corresponde una variable dual.",
                    "Las variables duales representan los Precios Sombra (Shadow Prices) o valor marginal del recurso restringido.",
                    "Base matemática de la fijación de Precios Marginales Locacionales (LMP) en mercados eléctricos liberalizados."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Optimización No Lineal Restringida: Condiciones KKT y Métodos de Punto Interior",
        "objetivo": "Resolver problemas de despacho económico no lineal y flujo óptimo de potencia (OPF) formulando las condiciones de Karush-Kuhn-Tucker (KKT) e implementando métodos de Punto Interior Primal-Dual.",
        "concepto_clave_latex": r"\nabla f(\mathbf{x}) + \sum \lambda_i \nabla g_i(\mathbf{x}) + \sum \mu_j \nabla h_j(\mathbf{x}) = \mathbf{0} \quad ; \quad \mu_j h_j(\mathbf{x}) = 0 \quad [\text{Holgura Complementaria}]",
        "ejemplo": "Problema 1: Minimizar el costo térmico total de dos generadores con funciones de costo cuadráticas: $C_1(P_1) = 0.05 P_1^2 + 20 P_1$ y $C_2(P_2) = 0.08 P_2^2 + 15 P_2$, para abastecer una demanda total de $P_1 + P_2 = 400\\text{ MW}$ con un límite de capacidad en el generador 1 de $P_1 \\le 220\\text{ MW}$. Lagrangiano: $\\mathcal{L}(P_1, P_2, \\lambda, \\mu) = (0.05 P_1^2 + 20 P_1) + (0.08 P_2^2 + 15 P_2) + \\lambda(400 - P_1 - P_2) + \\mu(P_1 - 220)$. Condiciones KKT de estación: $\\frac{\\partial \\mathcal{L}}{\\partial P_1} = 0.10 P_1 + 20 - \\lambda + \\mu = 0$; $\\frac{\\partial \\mathcal{L}}{\\partial P_2} = 0.16 P_2 + 15 - \\lambda = 0$. Condición de complementariedad: $\\mu(P_1 - 220) = 0$ con $\\mu \\ge 0$. Supongamos que la restricción no está activa ($\\mu = 0$): $0.10 P_1 + 20 = 0.16 P_2 + 15 = \\lambda$. Despejando: $P_1 = 1.6 P_2 - 50$. Con $P_1 + P_2 = 400 \\implies 2.6 P_2 - 50 = 400 \\implies 2.6 P_2 = 450 \\implies P_2 = 173.08\\text{ MW}$, lo que arroja $P_1 = 400 - 173.08 = 226.92\\text{ MW} > 220\\text{ MW}$ (violación de límite). Por tanto, la restricción está activa ($P_1^* = 220\\text{ MW}$). Generación 2: $P_2^* = 400 - 220 = 180\\text{ MW}$. Costo marginal del sistema: $\\lambda^* = 0.16(180) + 15 = 43.80\\text{ USD/MWh}$. Multiplicador KKT de la restricción: $\\mu^* = \\lambda^* - 0.10(220) - 20 = 43.80 - 22.0 - 20 = 1.80\\text{ USD/MWh} > 0$ (condición dual verificada). Problema 2: En redes con 10,000 barras, los métodos de Punto Interior Primal-Dual atraviesan el interior del dominio factible siguiendo la trayectoria central ('central path') con barreras logarítmicas en complejidad polinomial.",
        "bloque_sugerido": "Optimización No Lineal 45 min • Flujo Óptimo de Potencia (OPF) con método de Punto Interior en MATPOWER",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONDICIONES DE KARUSH-KUHN-TUCKER (KKT)",
                "titulo": "Generalización de los Multiplicadores de Lagrange",
                "puntos": [
                    "Condición necesaria y suficiente para óptimos globales en problemas convexos con restricciones de desigualdad.",
                    "1. Estacionariedad del gradiente del Lagrangiano.",
                    "2. Factibilidad primal ($g_i(x) = 0$, $h_j(x) \\le 0$).",
                    "3. Factibilidad dual ($\\mu_j \\ge 0$).",
                    "4. Holgura complementaria ($\\mu_j h_j(x) = 0$): O la restricción no está activa ($h_j < 0$) y su multiplicador es nulo ($\\mu_j = 0$), o la restricción está saturada ($h_j = 0$) y su multiplicador es estrictamente positivo."
                ]
            },
            {
                "numero": 2,
                "seccion": "MÉTODOS DE PUNTO INTERIOR PRIMAL-DUAL",
                "titulo": "Sustitución de Restricciones por Barreras",
                "puntos": [
                    "A diferencia de Simplex que viaja por los vértices externos del poliedro, el método de punto interior se mueve por el centro del espacio de búsqueda.",
                    "Aplica funciones de barrera logarítmica $-\\mu_k \\ln(-h_j(x))$ que tienden a infinito al aproximarse a las fronteras prohibidas.",
                    "Resuelve simultáneamente las ecuaciones de perturbación KKT mediante el método de Newton-Raphson modificado."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Programación Dinámica y Ecuación de Bellman en Gestión de Almacenamiento",
        "objetivo": "Resolver la gestión secuencial multi-etapa de sistemas de almacenamiento de energía y embalses hidroeléctricos mediante el Principio de Optimalidad de Bellman.",
        "concepto_clave_latex": r"V_t(x_t) = \min_{u_t} \left\{ C_t(x_t, u_t) + V_{t+1}(x_{t+1}) \right\} \quad \text{s.t.} \quad x_{t+1} = f(x_t, u_t, w_t)",
        "ejemplo": "Problema 1: Un sistema de baterías BESS de 1 MWh y potencia de 0.5 MW opera en un horizonte de 3 periodos horarios ($t=1, 2, 3$) bajo precios de electricidad dinámicos de mercado: $p_1 = 30\\text{ USD/MWh}$ (valle), $p_2 = 140\\text{ USD/MWh}$ (pico), $p_3 = 50\\text{ USD/MWh}$ (medio). El estado $x_t$ es el nivel de carga discreto (0, 0.5, o 1.0 MWh). Eficiencia round-trip del $100\\%$. El objetivo es maximizar la ganancia económica total desde un estado inicial vacío ($x_1 = 0$). Aplicando la programación dinámica hacia atrás (Backward Induction): Para $t=3$, la función de valor final es nula. Para $t=2$ (pico): si la batería está llena ($x_2 = 1.0$), la decisión óptima es descargar 0.5 MWh vendiendo a 140 USD/MWh, obteniendo un valor futuro óptimo de $V_2(1.0) = +70\\text{ USD}$. Para $t=1$ (valle): la decisión óptima es cargar 0.5 MWh comprando a 30 USD/MWh (costo $-15\\text{ USD}$) para transitar al estado $x_2 = 0.5$. La ecuación de Bellman evalúa la política óptima global sin realizar combinatorias exhaustivas de millones de caminos: Ganancia neta $= -15 + 70 = +55\\text{ USD}$. Problema 2: En la gestión de un embalse hidroeléctrico anual con 52 semanas y afluencias estocásticas $w_t$, el algoritmo discretiza el volumen en 100 estados y utiliza la esperanza matemática de la ecuación de Bellman.",
        "bloque_sugerido": "Control Óptimo 45 min • Ecuación de Bellman discreta e inducción hacia atrás en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL PRINCIPIO DE OPTIMALIDAD DE RICHARD BELLMAN",
                "titulo": "Subestructuras Óptimas",
                "puntos": [
                    "Cualquiera que sea el estado inicial y la decisión inicial, las decisiones restantes deben constituir una política óptima con respecto al estado resultante de la primera decisión.",
                    "Transforma un problema inabordable de optimización simultánea de $T$ variables acopladas en $T$ subproblemas de una sola etapa secuenciales.",
                    "Resuelve de forma natural incertidumbres estocásticas futuras mediante esperanzas condicionadas."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA MALDICIÓN DE LA DIMENSIONALIDAD",
                "titulo": "Crecimiento Exponencial del Espacio de Estados",
                "puntos": [
                    "Si un sistema tiene $n$ embalses interconectados y cada uno se discretiza en $K$ niveles, el número de estados posibles es $K^n$.",
                    "Para 1 embalse ($100^1 = 100$ estados): computación instantánea.",
                    "Para 5 embalses ($100^5 = 10^{10}$ estados): colapso computacional por memoria.",
                    "Motivó el desarrollo de la Programación Dinámica Dual Estocástica (SDDP) que aproxima la función de Bellman sin discretizar el espacio."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Algoritmos Metaheurísticos y Optimización Bio-inspirada (GA y PSO)",
        "objetivo": "Optimizar el dimensionamiento y emplazamiento óptimo de generadores distribuidos y microrredes mediante Algoritmos Genéticos (GA) y Optimización por Enjambre de Partículas (PSO).",
        "concepto_clave_latex": r"\mathbf{v}_i^{k+1} = w \mathbf{v}_i^k + c_1 r_1 (\mathbf{p}_{best,i} - \mathbf{x}_i^k) + c_2 r_2 (\mathbf{g}_{best} - \mathbf{x}_i^k) \quad ; \quad \mathbf{x}_i^{k+1} = \mathbf{x}_i^k + \mathbf{v}_i^{k+1}",
        "ejemplo": "Problema 1: En una red de distribución rural de 33 nodos se busca ubicar 3 parques solares fotovoltaicos de 2 MW para minimizar las pérdidas óhmicas de transporte $\\sum I_k^2 R_k$. El problema es fuertemente no lineal, no convexo y combinatorio entero-discreto ($33 \\times 32 \\times 31 / 6 = 5456$ combinaciones posibles de barras, con potencias continuas asociadas). Se implementa un algoritmo de Optimización por Enjambre de Partículas (PSO) con un enjambre de 30 partículas en $\\mathbb{R}^6$ (3 posiciones de barra y 3 potencias). Parámetros: Inercia decreciente $w = 0.9 \\to 0.4$, factores de aceleración cognitivo $c_1 = 2.0$ y social $c_2 = 2.0$. En cada iteración, las partículas evalúan el flujo de potencia en OpenDSS; cada partícula recuerda su mejor posición individual histórica ($\mathbf{p}_{best}$) y es atraída hacia la mejor solución encontrada por todo el enjambre ($\mathbf{g}_{best}$). En solo 45 iteraciones, el enjambre converge al óptimo global identificando los nodos 14, 28 y 32, reduciendo las pérdidas técnicas de la red en un $41.8\\%$. Problema 2: En Algoritmos Genéticos (GA), los operadores de selección por ruleta, cruzamiento de dos puntos (crossover) y mutación aleatoria con probabilidad $p_m = 0.02$ evitan quedar atrapados en óptimos locales engañosos.",
        "bloque_sugerido": "Computación Inteligente 45 min • Implementación de PSO para flujo de carga óptimo en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "METAHEURÍSTICAS BIO-INSPIRADAS",
                "titulo": "Superando las Limitaciones de los Métodos de Gradiente",
                "puntos": [
                    "Los métodos clásicos basados en derivadas (Newton, Gradiente) exigen que las funciones sean continuas y convexas, atrapándose en mínimos locales en paisajes multimodales complejos.",
                    "Las metaheurísticas estocásticas no requieren derivadas matemáticas; exploran el espacio de búsqueda utilizando analogías de la naturaleza.",
                    "Equilibrio estricto entre Exploración global (diversidad poblacional) y Explotación local (intensificación cerca del mejor candidato)."
                ]
            },
            {
                "numero": 2,
                "seccion": "ENJAMBRE DE PARTÍCULAS (PSO)",
                "titulo": "La Inteligencia de Bandada",
                "puntos": [
                    "Inspirado en el vuelo sincronizado de bandadas de aves buscando alimento en un territorio desconocido.",
                    "El vector de velocidad combina inercia propia, memoria personal cognitiva y atracción hacia el líder de la manada.",
                    "Muy superior a los algoritmos genéticos en problemas de optimización con variables continuas debido a su convergencia más rápida."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ecuaciones Diferenciales Estocásticas (SDE), Movimiento Browniano y Lema de Itô",
        "objetivo": "Modelar la dinámica estocástica continua de precios de energía en bolsa y perfiles de viento intermitente mediante procesos de difusión de Itô y el proceso de reversión a la media de Ornstein-Uhlenbeck.",
        "concepto_clave_latex": r"dX_t = \theta(\mu - X_t) dt + \sigma dW_t \quad ; \quad df(X_t) = \left( \frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma \frac{\partial f}{\partial x} dW_t",
        "ejemplo": "Problema 1: El precio horario de la electricidad en la bolsa de energía de Colombia exhibe estacionalidad y reversión a la media gobernada por el costo marginal de las plantas térmicas de gas. Se modela mediante un proceso de Ornstein-Uhlenbeck: $dP_t = \theta(\\mu - P_t) dt + \\sigma dW_t$, donde la media histórica es $\\mu = 60\\text{ USD/MWh}$, la velocidad de reversión a la media es $\\theta = 0.15\\text{ días}^{-1}$ y la volatilidad estocástica es $\\sigma = 12\\text{ USD}/(\\text{MWh}\\sqrt{\\text{día}})$. Si tras una falla inesperada el precio se dispara a $P_0 = 140\\text{ USD/MWh}$, calcular el valor esperado del precio dentro de 10 días: Esperanza matemática analítica del proceso de Itô: $\\mathbb{E}[P_t] = \\mu + (P_0 - \\mu) e^{-\\theta t} = 60 + (140 - 60) e^{-0.15 \\times 10} = 60 + 80 e^{-1.5} = 60 + 80(0.2231) = 60 + 17.85 = 77.85\\text{ USD/MWh}$. El precio decae exponencialmente de vuelta hacia su valor estructural de 60 USD. Problema 2: Por el Lema de Itô, al calcular la diferencial estocástica de una función no lineal como el logaritmo de los precios ($Y = \\ln P$), aparece un término correctivo de deriva no nulo $\\frac{1}{2}\\sigma^2 \\frac{\\partial^2 f}{\\partial P^2} = -\\frac{\\sigma^2}{2 P^2}$ derivado de la propiedad fundamental del movimiento browniano $(dW_t)^2 = dt$.",
        "bloque_sugerido": "Finanzas Energéticas 45 min • Simulación de Monte Carlo de procesos de difusión de Itô y saltos de Poisson",
        "slides": [
            {
                "numero": 1,
                "seccion": "CÁLCULO ESTOCÁSTICO DE ITÔ",
                "titulo": "Más Allá del Cálculo Diferencial Ordinario",
                "puntos": [
                    "El movimiento browniano estándar $W_t$ es continuo en todo punto pero no es diferenciable en ningún punto en el sentido clásico de Newton.",
                    "El término diferencial estocástico $dW_t$ escala con $\\sqrt{dt}$, no con $dt$.",
                    "El Lema de Itô es la regla de la cadena del cálculo estocástico, incorporando el término cuadrático de segundo orden en la serie de Taylor."
                ]
            },
            {
                "numero": 2,
                "seccion": "MODELADO DE PRECIOS Y RECURSOS",
                "titulo": "Procesos de Reversión a la Media y Saltos",
                "puntos": [
                    "A diferencia de las acciones de bolsa que siguen un paseo aleatorio geométrico (Black-Scholes), los precios de la energía no crecen indefinidamente; revierten a la media hacia el costo marginal de producción.",
                    "Fenómenos climáticos extremos inducen 'spikes' de precios transitorios modelados por procesos de difusión con saltos de Poisson.",
                    "Indispensable para la valoración financiera de contratos PPA y opciones reales en centrales de bombeo PHS."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Simulación de Monte Carlo y Evaluación de Confiabilidad de Sistemas de Potencia",
        "objetivo": "Evaluar la seguridad de suministro y confiabilidad de sistemas eléctricos mediante métodos de simulación de Monte Carlo secuencial y no secuencial, calculando índices de adecuación LOLP y EENS.",
        "concepto_clave_latex": r"\text{LOLP} = \frac{1}{N}\sum_{k=1}^N \mathbb{I}(C_k < D_k) \quad ; \quad \text{EENS} = \frac{8760}{N}\sum_{k=1}^N \max(0, D_k - C_k) \ [\text{MWh/año}]",
        "ejemplo": "Problema 1: Un sistema de potencia tiene una demanda pico anual de $D = 800\\text{ MW}$ abastecida por 5 generadores térmicos idénticos de 200 MW cada uno ($C_{total} = 1000\\text{ MW}$, reserva rodante nominal de 200 MW). Cada generador tiene una Tasa de Salidas Forzadas (Forced Outage Rate, FOR) independiente de $q = 0.08$ ($8\\%$ de probabilidad de avería aleatoria). Se ejecuta una simulación de Monte Carlo no secuencial con $N = 100000$ estados muestreados generando números aleatorios uniformes $U(0,1)$. Ocurre déficit de suministro (Loss of Load) cuando 2 o más generadores fallan simultáneamente ($C_k \\le 600\\text{ MW} < 800\\text{ MW}$). Probabilidad teórica binomial: $P(fallan \\ge 2) = 1 - [P(0) + P(1)] = 1 - [(0.92)^5 + 5(0.08)(0.92)^4] = 1 - [0.6591 + 0.2866] = 1 - 0.9457 = 0.0543$ ($5.43\\%$). En la simulación de Monte Carlo, se registran 5420 estados deficitarios sobre las 100,000 iteraciones: $\\text{LOLP} = \\frac{5420}{100000} = 0.0542$ ($5.42\\%$). Energía Esperada No Suministrada: Con un déficit medio de 150 MW en los estados de falla, $\\text{EENS} = 8760 \\times 0.0542 \\times 150 = 71219\\text{ MWh/año}$. Problema 2: En Monte Carlo secuencial cronológico, se generan trayectorias temporales continuas muestreando el Tiempo Medio Entre Fallas (MTBF) y el Tiempo Medio de Reparación (MTTR) de cada activo.",
        "bloque_sugerido": "Confiabilidad de Redes 45 min • Algoritmos de muestreo de Monte Carlo e índices SAIDI/SAIFI",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROBABILIDAD EN SISTEMAS COMPLEJOS",
                "titulo": "Monte Carlo No Secuencial vs Cronológico",
                "puntos": [
                    "Método No Secuencial: Muestreo de estados estáticos aleatorios independientes; computacionalmente muy rápido; ideal para balances de potencia en grandes redes.",
                    "Método Cronológico Secuencial: Simula hora a hora el paso del tiempo; indispensable cuando hay almacenamiento con baterías o hidroeléctricas con embalse donde el estado en $t+1$ depende estrictamente del nivel en $t$.",
                    "Permite incorporar la aleatoriedad climática conjunta de viento, radiación solar y fallas fortuitas de líneas de transmisión."
                ]
            },
            {
                "numero": 2,
                "seccion": "ÍNDICES DE CONFIABILIDAD (IEEE STD 1366)",
                "titulo": "LOLP, EENS y Riesgo de Racionamiento",
                "puntos": [
                    "LOLP (Loss of Load Probability): Probabilidad acumulada de que la demanda supere la capacidad de generación disponible.",
                    "EENS (Expected Energy Not Served): Energía total no suministrada a los usuarios en un año expresada en MWh.",
                    "Criterio estándar internacional: Un LOLP no superior a 1 día en 10 años ($0.0274\\%$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Identificación de Sistemas y Modelos Caja Negra en Energía (ARX / ARMAX)",
        "objetivo": "Estimar modelos paramétricos dinámicos de plantas térmicas y aerogeneradores a partir de datos experimentales de entrada-salida utilizando modelos ARX, ARMAX y estimación por mínimos cuadrados recursivos (RLS).",
        "concepto_clave_latex": r"A(q) y[t] = B(q) u[t - n_k] + C(q) e[t] \quad ; \quad \hat{\boldsymbol{\theta}} = (\boldsymbol{\Phi}^T \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^T \mathbf{Y} \quad ; \quad \text{AIC} = 2k - 2\ln(\hat{L})",
        "ejemplo": "Problema 1: Se identifica la dinámica de temperatura de un intercambiador de calor de una planta termosolar. La entrada $u[t]$ es la apertura de la válvula de vapor ($0-100\\%$) y la salida $y[t]$ es la temperatura del fluido secundario. Se recolectan 1000 datos a $T_s = 1.0\\text{ s}$ excitando el sistema con una señal binaria pseudoaleatoria (PRBS). Se ajusta un modelo ARX(2,2,1): $y[t] + a_1 y[t-1] + a_2 y[t-2] = b_1 u[t-1] + b_2 u[t-2] + e[t]$. El estimador por mínimos cuadrados calcula el vector de parámetros: $\\hat{\\boldsymbol{\theta}} = [-1.55, 0.58, 0.12, 0.08]^T$. Polinomio autorregresivo: $A(z) = 1 - 1.55 z^{-1} + 0.58 z^{-2}$. Polos en $z$: $z_{1,2} = 0.95, 0.60$ (ambos dentro del círculo unitario, sistema estable). Ganancia estática DC: $K_{DC} = \\frac{B(1)}{A(1)} = \\frac{0.12 + 0.08}{1 - 1.55 + 0.58} = \\frac{0.20}{0.03} = 6.67^\\circ\\text{C}$ por cada $1\\%$ de apertura de válvula. El ajuste de validación cruzada con datos no vistos alcanza un $FIT = 94.2\\%$. Problema 2: El criterio de información de Akaike (AIC) selecciona automáticamente el orden óptimo del modelo penalizando el sobreajuste ('overfitting').",
        "bloque_sugerido": "Identificación de Sistemas 45 min • Señales de excitación PRBS y ajuste de modelos ARMAX en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "MODELADO DE CAJA BLANCA VS CAJA NEGRA",
                "titulo": "Modelos Basados en Datos",
                "puntos": [
                    "Caja Blanca: Ecuaciones físicas deducidas de primeros principios (conservación de masa, energía); complejas y difíciles de calibrar en procesos industriales con turbulencia.",
                    "Caja Negra: Ecuaciones diferenciales algebraicas cuyos coeficientes se ajustan automáticamente a partir de datos experimentales de telemetría sin conocer la física interna.",
                    "Caja Gris: Estructura física fijada pero con parámetros desconocidos estimados por regresión."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTRUCTURAS PARAMÉTRICAS POLINOMIALES",
                "titulo": "ARX, ARMAX, Box-Jenkins y Output-Error",
                "puntos": [
                    "ARX (Auto-Regressive with eXogenous input): Modelo lineal en parámetros; solución analítica directa no iterativa por mínimos cuadrados ordinarios.",
                    "ARMAX: Incorpora un promedio móvil $C(q)e[t]$ para modelar ruido coloreado correlacionado en los sensores.",
                    "Mínimos Cuadrados Recursivos (RLS) con factor de olvido: Permite actualizar los parámetros del modelo en tiempo real mientras la planta envejece."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Redes Neuronales Físicamente Informadas (PINNs) para Ecuaciones Diferenciales",
        "objetivo": "Entrenar redes neuronales artificiales profundas que resuelven ecuaciones en derivadas parciales energéticas (EDPs de Navier-Stokes y conducción térmica) integrando los residuos físicos directamente en la función de pérdida mediante diferenciación automática.",
        "concepto_clave_latex": r"\mathcal{L}_{total} = \mathcal{L}_{datos} + \lambda_{fisica} \mathcal{L}_{EDP} \quad ; \quad \mathcal{L}_{EDP} = \frac{1}{N_f}\sum_{i=1}^{N_f} \left| \frac{\partial \hat{u}}{\partial t} - \alpha \frac{\partial^2 \hat{u}}{\partial x^2} \right|^2",
        "ejemplo": "Problema 1: Se desea reconstruir el campo de temperatura 2D en el disipador térmico de un inversor fotovoltaico de carburo de silicio (SiC) donde solo se dispone de 12 sensores termocupla puntuales en la superficie ($N_{datos} = 12$). Una red neuronal profunda convencional 'data-driven' comete errores severos de extrapolación fuera de los puntos medidos. Se implementa una red PINN (Physics-Informed Neural Network) con 4 capas ocultas de 50 neuronas y activación tanh. La red toma como entrada $(x, y)$ y predice la temperatura $\\hat{T}(x,y)$. La función de pérdida combina el error cuadrático medio en los 12 sensores medidos y el residuo de la ecuación de conducción estacionaria de Laplace $\\mathcal{L}_{fisica} = \\frac{1}{N_{colocacion}}\\sum |\\nabla^2 \\hat{T}|^2$ evaluado en 2000 puntos de colocación aleatorios en el interior del disipador mediante diferenciación automática (AD en PyTorch). La física actúa como un regularizador implícito perfecto: la red aprende la distribución de calor exacta respetando la ley de Fourier, reduciendo el error global de estimación del $24\\%$ a menos del $1.1\\%$ con solo 12 sensores. Problema 2: En aerodinámica de perfiles eólicos, las PINNs resuelven las ecuaciones de Navier-Stokes sin requerir la generación de mallas computacionales estructuradas complejas.",
        "bloque_sugerido": "Inteligencia Artificial Científica 45 min • Entrenamiento de una PINN en PyTorch para la ecuación del calor",
        "slides": [
            {
                "numero": 1,
                "seccion": "IA CIENTÍFICA (SCIENTIFIC MACHINE LEARNING)",
                "titulo": "La Fusión de Redes Profundas y Leyes Físicas",
                "puntos": [
                    "El Deep Learning estándar requiere millones de datos de entrenamiento y no garantiza que sus predicciones respeten principios elementales de conservación de masa o energía.",
                    "Las PINNs (Maziar Raissi, 2019) 'castigan' a la red neuronal durante el entrenamiento si las derivadas de sus salidas violan la ecuación diferencial gobernante.",
                    "No requiere mallas numéricas (mesh-free method): Evalúa las ecuaciones en cualquier punto del espacio continuo."
                ]
            },
            {
                "numero": 2,
                "seccion": "DIFERENCIACIÓN AUTOMÁTICA",
                "titulo": "Derivadas Exactas con Grafo Computacional",
                "puntos": [
                    "No utiliza diferencias finitas aproximadas ni cálculo simbólico lento.",
                    "La diferenciación automática aplica la regla de la cadena a nivel de las operaciones aritméticas elementales del grafo de la red con precisión a nivel de máquina.",
                    "Resuelve problemas inversos: Puede estimar simultáneamente la conductividad térmica desconocida de un material mientras resuelve el campo de temperatura."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelos de Orden Reducido (ROM): Descomposición Modal Adecuada (POD) y Galerkin",
        "objetivo": "Reducir la complejidad computacional de modelos multifísicos tridimensionales de millones de grados de libertad a sistemas dinámicos compactos de orden bajo ($n < 10$) mediante Descomposición en Modos Propios (POD / PCA funcional).",
        "concepto_clave_latex": r"\mathbf{u}(x,t) \approx \sum_{i=1}^r a_i(t) \boldsymbol{\phi}_i(x) \quad [r \ll N] \quad ; \quad \mathbf{X} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^T \quad ; \quad \dot{\mathbf{a}} = \mathbf{L}\mathbf{a} + \mathbf{a}^T \mathbf{Q}\mathbf{a}",
        "ejemplo": "Problema 1: Un modelo CFD de una turbina eólica de eje horizontal de 5 MW cuenta con una malla de 12 millones de celdas; cada simulación temporal de 10 segundos requiere 48 horas en un clúster HPC, impidiendo su uso en control en tiempo real. Se aplica la técnica de Descomposición en Modos Propios (Proper Orthogonal Decomposition, POD): Se recopilan 500 'instantáneas' (snapshots) del campo de velocidades tridimensional en una matriz $\\mathbf{X} \\in \\mathbb{R}^{12 \\times 10^6 \\times 500}$. Se calcula la SVD de la matriz de snapshots. El análisis de energía espectral de los valores singulares revela que los primeros $r = 6$ modos espaciales $\\boldsymbol{\\phi}_i(x)$ capturan más del $98.5\\%$ de toda la energía cinética turbulenta del flujo. Proyectando las ecuaciones de Navier-Stokes sobre estos 6 modos mediante el método de Galerkin, el modelo original de 12 millones de variables se reduce a un sistema algebraico no lineal de solo 6 ecuaciones diferenciales ordinarias en los coeficientes $a_i(t)$. Tiempo de simulación del modelo reducido ROM: $t = 15\\text{ milisegundos}$ en un microprocesador ordinario (una aceleración de 10 millones de veces en velocidad de cómputo) manteniendo un error inferior al $2.5\\%$. Problema 2: Este modelo ROM ultra-rápido se embarca directamente en el controlador PLC del aerogenerador para el ajuste dinámico continuo del ángulo de pitch en tiempo real.",
        "bloque_sugerido": "Reducción de Modelos 45 min • Método de Snapshots de Sirovich y proyección Galerkin en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA BARRERA COMPUTACIONAL DE LA SIMULACIÓN 3D",
                "titulo": "De Días de Cómputo a Milisegundos",
                "puntos": [
                    "Los modelos de alta fidelidad (CFD, FEM estructural, electromagnetismo 3D) son inviables para optimización iterativa, gemelos digitales o control en lazo cerrado.",
                    "Los fenómenos físicos reales concentran la mayor parte de su comportamiento dinámico en unas pocas estructuras coherentes espaciales dominantes.",
                    "El método ROM extrae estas estructuras coherentes óptimas directamente de los datos de simulación."
                ]
            },
            {
                "numero": 2,
                "seccion": "MÉTODO DE SNAPSHOTS",
                "titulo": "POD y Proyección Galerkin",
                "puntos": [
                    "Los modos espaciales de POD son ortonormales y óptimos en el sentido de que minimizan el error cuadrático medio de aproximación para cualquier orden $r$.",
                    "La proyección de Galerkin del operador diferencial sobre la base reducida conserva rigurosamente las propiedades de estabilidad del sistema continuo original.",
                    "Pilar tecnológico para gemelos digitales en plantas de energía de última generación."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelado Multifísico Acoplado (Termo-Electro-Mecánico) en Dispositivos Energéticos",
        "objetivo": "Integrar campos acoplados simultáneos donde las ecuaciones térmicas, electromagnéticas y de deformación elástica interactúan bidireccionalmente en convertidores electrónicos y transformadores de potencia.",
        "concepto_clave_latex": r"\begin{cases} \nabla \cdot (\sigma(T) \nabla V) = 0 & [\text{Campo Eléctrico}] \\ \rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k(T)\nabla T) + \sigma |\nabla V|^2 & [\text{Calor Joule}] \\ \nabla \cdot \boldsymbol{\sigma}_m + \mathbf{f}_L = \mathbf{0} \quad ; \quad \boldsymbol{\varepsilon} = \mathbf{C}^{-1}\boldsymbol{\sigma}_m + \boldsymbol{\alpha}\Delta T & [\text{Deformación Térmica}] \end{cases}",
        "ejemplo": "Problema 1: En un módulo semiconductor de potencia SiC MOSFET de 1200 V y 300 A para inversores solares, la corriente eléctrica que circula por los terminales disipa calor por efecto Joule volumétrico ($q''' = \\sigma(T) |\\mathbf{E}|^2$). El calor generado eleva la temperatura local de la unión de silicio a $T_j = 145^\\circ\\text{C}$. Debido a que la conductividad térmica del cobre ($k_{Cu}$) y del sustrato cerámico de nitruro de aluminio ($AlN$) difieren ampliamente, y sus coeficientes de expansión térmica son disímiles ($\\alpha_{Cu} = 16.5 \\times 10^{-6}\\text{ K}^{-1}$ vs $\\alpha_{AlN} = 4.5 \\times 10^{-6}\\text{ K}^{-1}$), el gradiente térmico de $\\Delta T = 120^\\circ\\text{C}$ genera esfuerzos mecánicos de corte masivos en la capa de soldadura de estaño-plata ($\\tau_{soldadura} > 45\\text{ MPa}$). La deformación elasto-plástica cíclica inducida por los ciclos térmicos de día/noche propaga microfisuras por fatiga de bajo ciclo en la soldadura (fatiga termo-mecánica de Coffin-Manson), aumentando la resistencia térmica de contacto y acelerando el fallo térmico destructivo. Problema 2: En transformadores de potencia, el modelado acoplado calcula simultáneamente las pérdidas de Foucault en el cobre, el flujo termo-hidráulico de convección natural del aceite aislante en los radiadores y las fuerzas dinámicas de Lorentz durante cortocircuitos.",
        "bloque_sugerido": "Simulación Multifísica 45 min • Acoplamiento de campos bidireccionales en COMSOL Multiphysics",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA NATURALEZA MULTIFÍSICA REAL",
                "titulo": "Sistemas Fuertemente Acoplados",
                "puntos": [
                    "En ingeniería real, ningún fenómeno físico ocurre de forma aislada.",
                    "La temperatura altera las propiedades eléctricas (resistencia aumenta con $T$) y mecánicas (módulo de Young cae a alta temperatura).",
                    "El campo electromagnético genera calor y fuerzas mecánicas; la deformación mecánica altera la geometría del campo electromagnético.",
                    "Exige resolver matrices acopladas monolíticas o esquemas particionados iterativos secuenciales."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISEÑO ROBUSTO EN INGENIERÍA ENERGÉTICA",
                "titulo": "Predicción de Vida Útil y Puntos Críticos",
                "puntos": [
                    "Evita el sobredimensionamiento conservador ciego y previene fallas catastróficas imprevistas.",
                    "Indispensable para el empaquetado térmico de baterías de tracción de vehículos eléctricos (gestión térmica de módulos BESS).",
                    "Culminación del proceso de formación matemática del Ingeniero Energético de la Universidad del Magdalena."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_04021825)
    # Inject before the next subject marker: 06011839
    inject_topics_after('      - codigo: "06011839"', yaml_text)
    print("04021825 Modelación Matemática para Ingeniería successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
