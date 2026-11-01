# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_03041821 = [
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ecuación de Onda Electromagnética en Medios con Pérdidas y Medios Conductores",
        "objetivo": "Deducir las ecuaciones de onda vectorial de Helmholtz a partir de las ecuaciones de Maxwell para medios arbitrarios caracterizados por $(\\varepsilon, \\mu, \\sigma)$, determinando la constante de propagación compleja $\\gamma = \\alpha + j\\beta$.",
        "concepto_clave_latex": r"\nabla^2 \mathbf{E} - \gamma^2 \mathbf{E} = 0 \quad ; \quad \gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)} \quad ; \quad \tan\delta = \frac{\sigma}{\omega\varepsilon}",
        "ejemplo": "Problema 1: Una onda electromagnética de $f = 100\\text{ MHz}$ se propaga en agua de mar con $\\sigma = 4.0\\text{ S/m}$, $\\varepsilon_r = 81$, $\\mu_r = 1$. Calcular la tangente de pérdidas para clasificar el medio: $\\omega = 2\\pi \\times 10^8\\text{ rad/s} = 6.283 \\times 10^8\\text{ rad/s}$. $\\varepsilon = 81 \\times 8.854 \\times 10^{-12} = 7.172 \\times 10^{-10}\\text{ F/m}$. Tangente: $\\tan\\delta = \\frac{4.0}{6.283 \\times 10^8 \\times 7.172 \\times 10^{-10}} = \\frac{4.0}{0.4506} \\approx 8.88$. Al ser $\\tan\\delta > 1$, el medio se comporta como un buen conductor. Constante de atenuación: $\\alpha \\approx \\sqrt{\\frac{\\omega\\mu\\sigma}{2}} = \\sqrt{\\frac{6.283 \\times 10^8 \\times 4\\pi \\times 10^{-7} \\times 4.0}{2}} = \\sqrt{1579.1} \\approx 39.74\\text{ Np/m}$. La onda se extingue a una fracción de metro. Problema 2: En un dieléctrico perfecto ($\\sigma = 0$), $\\alpha = 0$ y $\\beta = \\omega\\sqrt{\\mu\\varepsilon}$, propagándose sin disipación térmica.",
        "bloque_sugerido": "Taller Electromagnético 40 min • Constante de propagación y clasificación de medios",
        "slides": [
            {
                "numero": 1,
                "seccion": "DEDUCCIÓN VECTORIAL",
                "titulo": "De Maxwell a Helmholtz",
                "puntos": [
                    "Aplicando el rotacional al rotacional: $\\nabla \\times (\\nabla \\times \\mathbf{E}) = \\nabla(\\nabla \\cdot \\mathbf{E}) - \\nabla^2 \\mathbf{E}$.",
                    "En medios libres de carga volumétrica libre ($\\rho_v = 0$), la divergencia se anula, resultando en la ecuación vectorial de onda homogénea.",
                    "La presencia de conductividad finita $\\sigma$ acopla la corriente de conducción $\\mathbf{J} = \\sigma\\mathbf{E}$ con la corriente de desplazamiento $\\frac{\\partial \\mathbf{D}}{\\partial t}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "PARÁMETROS COMPLEJOS",
                "titulo": "Permitividad Compleja y Pérdidas",
                "puntos": [
                    "Permitividad equivalente compleja: $\\varepsilon_c = \\varepsilon - j\\frac{\\sigma}{\\omega} = \\varepsilon'(1 - j\\tan\\delta)$.",
                    "El ángulo de pérdidas $\\delta$ cuantifica la potencia electromagnética disipada en calor por unidad de volumen ($P_d = \\frac{1}{2}\\sigma |\\mathbf{E}|^2$).",
                    "Base para el cálculo de pérdidas dieléctricas en cables aislados de potencia subterránea (XLPE)."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ondas Planas Uniformes, Impedancia Intrínseca y Profundidad de Penetración (Skin Depth)",
        "objetivo": "Analizar la estructura espacial de ondas transversales electromagnéticas (TEM), calculando la impedancia intrínseca de onda $\\eta$ y la profundidad pelicular $\\delta_s$ en conductores de potencia.",
        "concepto_clave_latex": r"\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}} \quad [\Omega] \quad ; \quad \delta_s = \frac{1}{\alpha} \approx \sqrt{\frac{2}{\omega\mu\sigma}} = \frac{1}{\sqrt{\pi f \mu \sigma}} \quad [\text{m}]",
        "ejemplo": "Problema 1: Calcular la profundidad de penetración (efecto piel) en un conductor cilíndrico de cobre ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$, $\\mu = \\mu_0 = 4\\pi \\times 10^{-7}\\text{ H/m}$) a la frecuencia de red eléctrica colombiana de $f = 60\\text{ Hz}$. Aplicando la fórmula: $\\delta_s = \\frac{1}{\\sqrt{\\pi \\times 60 \\times 4\\pi \\times 10^{-7} \\times 5.8 \\times 10^7}} = \\frac{1}{\\sqrt{1.3739 \\times 10^4}} = \\frac{1}{117.21} = 8.53 \\times 10^{-3}\\text{ m} = 8.53\\text{ mm}$. Conductores con radio mayor a 8.5 mm presentan un núcleo central sin densidad de corriente efectiva, incrementando la resistencia en corriente alterna ($R_{AC} > R_{DC}$). Problema 2: A alta frecuencia ($f = 1\\text{ MHz}$), $\\delta_s \\approx 0.066\\text{ mm}$, confinando la corriente casi exclusivamente a la superficie exterior del conductor.",
        "bloque_sugerido": "Cálculo Numérico 40 min • Efecto pelicular y resistencia AC en conductores de fase",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRUCTURA DE ONDA TEM",
                "titulo": "Ortogonalidad Espacial de E y H",
                "puntos": [
                    "En una onda plana uniforme, los vectores $\\mathbf{E}$, $\\mathbf{H}$ y la dirección de propagación $\\hat{\\mathbf{k}}$ son mutuamente ortogonales.",
                    "La relación de amplitudes está fijada por la impedancia intrínseca del medio: $\\frac{|E_x|}{|H_y|} = |\\eta|$.",
                    "En el vacío: $\\eta_0 = \\sqrt{\\frac{\\mu_0}{\\varepsilon_0}} \\approx 120\\pi \\approx 376.73\\ \\Omega$."
                ]
            },
            {
                "numero": 2,
                "seccion": "EFECTO PELICULAR (SKIN EFFECT)",
                "titulo": "Atenuación Exponencial en Conductores",
                "puntos": [
                    "La densidad de corriente decae como $J(z) = J_0 e^{-z/\\delta_s} e^{-j z/\\delta_s}$.",
                    "En una profundidad de $z = \\delta_s$, la amplitud de la corriente cae al $36.8\\%$ ($1/e$) de su valor superficial.",
                    "Explica por qué en líneas de alta tensión se emplean conductores trenzados ACSR y haces de subconductores por fase."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Polarización Electromagnética y Parámetros de Stokes",
        "objetivo": "Caracterizar el lugar geométrico descrito por la punta del vector de campo eléctrico en el plano transversal (polarización lineal, circular y elíptica), utilizando los cuatro parámetros de Stokes.",
        "concepto_clave_latex": r"\mathbf{E}(z,t) = E_{0x}\cos(\omega t - \beta z)\hat{\mathbf{a}}_x + E_{0y}\cos(\omega t - \beta z + \delta)\hat{\mathbf{a}}_y \quad ; \quad S_0^2 = S_1^2 + S_2^2 + S_3^2",
        "ejemplo": "Problema 1: Sea una onda con fasor $\\mathbf{E} = E_0(\\hat{\\mathbf{a}}_x + j\\hat{\\mathbf{a}}_y)e^{-j\\beta z}$. Determinar su estado de polarización. Las amplitudes de las componentes son iguales: $E_{0x} = E_{0y} = E_0$. La diferencia de fase es $\\delta = +\\pi/2$. En el plano $z = 0$, para $t = 0$: $\\mathbf{E} = E_0 \\hat{\\mathbf{a}}_x$; para $\\omega t = \\pi/2$: $\\mathbf{E} = -E_0 \\hat{\\mathbf{a}}_y$. El vector rota en sentido horario (visto en dirección de propagación), configurando una onda con Polarización Circular a Izquierdas (LCP). Problema 2: En antenas de satélite para monitoreo de subestaciones, la polarización circular mitiga la atenuación por rotación de Faraday en la ionosfera terrestre.",
        "bloque_sugerido": "Visualización Geométrica 35 min • Estados de polarización y esfera de Poincaré",
        "slides": [
            {
                "numero": 1,
                "seccion": "CINEMÁTICA DEL CAMPO ELÉCTRICO",
                "titulo": "Lineal, Circular y Elíptica",
                "puntos": [
                    "Polarización Lineal: Ocurre si $\\delta = 0$ o $\\delta = \\pm \\pi$, o si una de las componentes es nula.",
                    "Polarización Circular: Ocurre cuando $E_{0x} = E_{0y}$ y $\\delta = \\pm \\pi/2$.",
                    "Polarización Elíptica: Caso general para amplitudes arbitrarias y desfases distintos de múltiplos de $\\pi$."
                ]
            },
            {
                "numero": 2,
                "seccion": "PARÁMETROS DE STOKES",
                "titulo": "Representación de Potencia de Stokes",
                "puntos": [
                    "$S_0$: Intensidad total de la onda ($E_{0x}^2 + E_{0y}^2$).",
                    "$S_1$: Predominio de polarización horizontal sobre vertical ($E_{0x}^2 - E_{0y}^2$).",
                    "$S_2$: Predominio de polarización lineal a $+45^\\circ$ sobre $-45^\\circ$ ($2 E_{0x} E_{0y} \\cos\\delta$).",
                    "$S_3$: Grado de polarización circular derecha vs izquierda ($2 E_{0x} E_{0y} \\sin\\delta$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Reflexión y Refracción de Ondas EM: Ecuaciones de Fresnel y Ángulo de Brewster",
        "objetivo": "Calcular los coeficientes de reflexión y transmisión en interfaces planas entre medios dieléctricos con incidencia oblicua, determinando el ángulo de Brewster $\\theta_B$ para polarizaciones paralela y perpendicular.",
        "concepto_clave_latex": r"\Gamma_\parallel = \frac{\eta_2\cos\theta_t - \eta_1\cos\theta_i}{\eta_2\cos\theta_t + \eta_1\cos\theta_i} \quad ; \quad \tan\theta_{B} = \sqrt{\frac{\varepsilon_2}{\varepsilon_1}} \quad [\Gamma_\parallel(\theta_B) = 0]",
        "ejemplo": "Problema 1: Una onda electromagnética incide desde el aire ($\\varepsilon_1 = 1$) hacia un panel solar cubierto de vidrio templado ($\\varepsilon_2 = 2.25$, índice de refracción $n_2 = 1.5$). Calcular el ángulo de Brewster para polarización paralela: $\\tan\\theta_B = \\sqrt{\\frac{2.25}{1.0}} = 1.5 \\implies \\theta_B = \\arctan(1.5) \\approx 56.31^\\circ$. A este ángulo de incidencia, el coeficiente de reflexión para luz polarizada paralela es idénticamente cero ($\\Gamma_\\parallel = 0$), maximizando la penetración de radiación hacia las celdas solares. Problema 2: El ángulo crítico de reflexión interna total ocurre cuando la onda viaja de un medio más denso a uno menos denso y $\\sin\\theta_c = \\sqrt{\\varepsilon_2/\\varepsilon_1}$, principio de confinamiento en fibras ópticas de telecomunicaciones en redes de potencia.",
        "bloque_sugerido": "Óptica Ondulatoria 45 min • Coeficientes de Fresnel y diseño de capas antirreflectantes",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES DE SNELL Y CONDICIONES DE FRONTERA",
                "titulo": "Continuidad Tangencial en la Interfaz",
                "puntos": [
                    "Condición cinemática: El ángulo de reflexión es igual al ángulo de incidencia ($\\theta_r = \\theta_i$).",
                    "Ley de Snell de refracción: $k_1 \\sin\\theta_i = k_2 \\sin\\theta_t \\implies n_1 \\sin\\theta_i = n_2 \\sin\\theta_t$.",
                    "Condiciones dinámicas de frontera: Continuidad de las componentes tangenciales $\\mathbf{E}_t$ y $\\mathbf{H}_t$ a través de la discontinuidad."
                ]
            },
            {
                "numero": 2,
                "seccion": "POLARIZACIÓN TE Y TM",
                "titulo": "Ángulo de Brewster y Transmisión Total",
                "puntos": [
                    "Para polarización transversal magnética (TM o paralela), existe un ángulo de incidencia donde no hay onda reflejada.",
                    "Para medios no magnéticos ($\\mu_1 = \\mu_2 = \\mu_0$), no existe ángulo de Brewster para polarización perpendicular (TE).",
                    "Fundamental para optimizar la eficiencia óptica de colectores solares y ventanas de plasma."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Densidad de Energía Electromagnética, Teorema de Poynting y Flujo de Potencia",
        "objetivo": "Formular el principio de conservación de energía electromagnética de Poynting, calculando el flujo medio temporal del vector $\\mathbf{S}$ en guías, cables coaxiales y radiación.",
        "concepto_clave_latex": r"\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad [\text{W/m}^2] \quad ; \quad \langle \mathbf{S} \rangle = \frac{1}{2} \text{Re}\left( \mathbf{E} \times \mathbf{H}^* \right) \quad ; \quad \nabla \cdot \mathbf{S} + \frac{\partial u_{em}}{\partial t} + \mathbf{J} \cdot \mathbf{E} = 0",
        "ejemplo": "Problema 1: Un cable coaxial transmite una potencia DC $P = V I$. El conductor interno de radio $a$ está a potencial $V$ y el blindaje externo de radio $b$ a potencial cero. El campo eléctrico radial en el dieléctrico es $E_r = \\frac{V}{r \\ln(b/a)}$ y el campo magnético azimutal por ley de Ampère es $H_\\phi = \\frac{I}{2\\pi r}$. El vector de Poynting es puramente axial: $S_z = E_r H_\\phi = \\frac{V I}{2\\pi \\ln(b/a) r^2}$. Integrando sobre la sección transversal del dieléctrico: $P = \\int_a^b \\int_0^{2\\pi} S_z (r d\\phi dr) = \\frac{V I}{2\\pi \\ln(b/a)} 2\\pi \\int_a^b \\frac{dr}{r} = V I$. La energía eléctrica no viaja dentro de los hilos de cobre, sino a través del campo electromagnético en el espacio aislante entre ellos. Problema 2: En la superficie del sol, el vector de Poynting integrado da la luminosidad solar total de $3.828 \\times 10^{26}\\text{ W}$.",
        "bloque_sugerido": "Balances Energéticos 45 min • Flujo de Poynting en líneas de transmisión y circuitos",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONSERVACIÓN DE ENERGÍA EM",
                "titulo": "El Teorema de Poynting",
                "puntos": [
                    "La divergencia del vector de Poynting $\\nabla \\cdot \\mathbf{S}$ representa la tasa neta de potencia electromagnética que sale de un volumen cerrado.",
                    "El término $\\frac{\\partial u_{em}}{\\partial t}$ cuantifica la variación temporal de la energía almacenada en campos eléctricos y magnéticos.",
                    "El término $\\mathbf{J} \cdot \\mathbf{E}$ modela las pérdidas Joule disipadas o el trabajo realizado sobre cargas móviles."
                ]
            },
            {
                "numero": 2,
                "seccion": "RÉGIMEN ARMÓNICO",
                "titulo": "Vector Complejo de Poynting",
                "puntos": [
                    "Vector complejo: $\\mathbf{S}_c = \\frac{1}{2}\\mathbf{E} \\times \\mathbf{H}^*$.",
                    "Parte real: $\\text{Re}(\\mathbf{S}_c)$ modela el flujo neto de potencia activa transmitida.",
                    "Parte imaginaria: $\\text{Im}(\\mathbf{S}_c) = \\omega(u_m - u_e)$ modela el intercambio reactivo oscilante entre campos magnéticos y eléctricos."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Potenciales Retardados y Calibraciones Electrodinámicas (Lorentz y Coulomb)",
        "objetivo": "Resolver las ecuaciones electrodinámicas inhomogéneas desacopladas empleando el potencial escalar $V$ y el potencial vector magnético $\\mathbf{A}$ bajo la condición de norma de Lorentz.",
        "concepto_clave_latex": r"\nabla \cdot \mathbf{A} + \mu\varepsilon \frac{\partial V}{\partial t} = 0 \quad [\text{Gauge de Lorentz}] \quad ; \quad \mathbf{A}(\mathbf{r},t) = \frac{\mu}{4\pi}\iiint \frac{\mathbf{J}(\mathbf{r}', t - R/c)}{R} dV'",
        "ejemplo": "Problema 1: Explicar físicamente el tiempo retardado $t_r = t - R/c$ en el potencial vector. Una perturbación de corriente en un conductor en el punto $\\mathbf{r}'$ no se siente instantáneamente en un punto de observación distante $\\mathbf{r}$. La información viaja a la velocidad finita de la luz $c = 1/\\sqrt{\\mu\\varepsilon}$. Por tanto, los campos en el instante $t$ dependen del estado dinámico de las fuentes en el instante previo $t_r$. Problema 2: En el régimen magnetostático estacionario ($\\partial / \\partial t = 0$), la norma de Lorentz colapsa exactamente en la norma de Coulomb $\\nabla \\cdot \\mathbf{A} = 0$, recuperando la ley clásica de Biot-Savart.",
        "bloque_sugerido": "Electrodinámica Teórica 40 min • Transformaciones de calibre y potenciales de Liénard-Wiechert",
        "slides": [
            {
                "numero": 1,
                "seccion": "FORMULACIÓN POR POTENCIALES",
                "titulo": "Desacoplamiento de Ecuaciones de Campo",
                "puntos": [
                    "Definición: $\\mathbf{B} = \\nabla \\times \\mathbf{A}$, lo que garantiza idénticamente $\\nabla \\cdot \\mathbf{B} = 0$.",
                    "Por ley de Faraday: $\\nabla \\times \\left( \\mathbf{E} + \\frac{\\partial \\mathbf{A}}{\\partial t} \\right) = 0 \\implies \\mathbf{E} = -\\nabla V - \\frac{\\partial \\mathbf{A}}{\\partial t}$.",
                    "La libertad de calibración (gauge freedom) permite imponer $\\nabla \\cdot \\mathbf{A} + \\mu\\varepsilon \\frac{\\partial V}{\\partial t} = 0$ transformando Maxwell en dos ecuaciones de onda de d'Alembert desacopladas."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIONES RADIATIVAS",
                "titulo": "Cálculo de Campos de Radiación",
                "puntos": [
                    "Determinar directamente los campos $\\mathbf{E}$ y $\\mathbf{B}$ de geometrías de antenas complejas es matemáticamente intratable.",
                    "El método estándar calcula primero el potencial vector retardado $\\mathbf{A}$ por integración volumétrica sobre las corrientes de la antena.",
                    "Luego los campos se obtienen por simple derivación espacial: $\\mathbf{B} = \\nabla \\times \\mathbf{A}$ y $\\mathbf{E} = \\frac{1}{j\\omega\\mu\\varepsilon}\\nabla \\times (\\nabla \\times \\mathbf{A})$."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Radiación Electromagnética: Dipolo Eléctrico Hertziano y Resistencia de Radiación",
        "objetivo": "Modelar la emisión de ondas esféricas en zona lejana por un dipolo oscilante elemental $I_0 dl$, deduciendo el patrón de radiación y la resistencia equivalente de radiación $R_{rad}$.",
        "concepto_clave_latex": r"E_\theta = j \frac{\eta I_0 \beta dl}{4\pi r} \sin\theta e^{-j\beta r} \quad ; \quad P_{rad} = \frac{\pi \eta}{3} \left( \frac{I_0 dl}{\lambda} \right)^2 = \frac{1}{2} I_0^2 R_{rad} \quad ; \quad R_{rad} = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2",
        "ejemplo": "Problema 1: Un dipolo hertziano de longitud $dl = 5\\text{ cm}$ opera a una frecuencia de comunicación de $f = 30\\text{ MHz}$ en el aire libre. La longitud de onda es $\\lambda = \\frac{3 \\times 10^8}{30 \\times 10^6} = 10\\text{ m}$. Calcular la resistencia de radiación del dipolo: $R_{rad} = 80\\pi^2 \\left( \\frac{0.05}{10.0} \\right)^2 = 789.57 \\times (0.005)^2 = 789.57 \\times 2.5 \\times 10^{-5} \\approx 0.0197\\ \\Omega$. Si la corriente de alimentación pico es $I_0 = 10\\text{ A}$, la potencia electromagnética radiada es $P_{rad} = \\frac{1}{2}(10)^2 \\times 0.0197 = 0.985\\text{ W}$. Problema 2: En antenas prácticas de media onda (dipolo de $\\lambda/2$), la resistencia de radiación se eleva drásticamente a $R_{rad} \\approx 73.13\\ \\Omega$, permitiendo una adaptación de impedancias eficiente con cables coaxiales comerciales de $75\\ \\Omega$.",
        "bloque_sugerido": "Teoría de Antenas 45 min • Zona de campo cercano (reactiva) vs campo lejano de Fraunhofer",
        "slides": [
            {
                "numero": 1,
                "seccion": "ZONAS ELECTROMAGNÉTICAS",
                "titulo": "Campo Cercano vs Campo Lejano",
                "puntos": [
                    "Zona Reactiva Cercana ($r < 0.62\\sqrt{D^3/\\lambda}$): Predominan campos electrostáticos e inductivos ($1/r^3$ y $1/r^2$); energía reactiva no radiada.",
                    "Zona de Radiación de Fraunhofer ($r > 2D^2/\\lambda$): Los campos decaen como $1/r$, con fase esférica transversal uniforme.",
                    "El patrón de radiación del dipolo tiene forma toroidal ('doughnut') con radiación máxima en el plano ecuatorial ($\\theta = 90^\\circ$) y nulos en el eje del dipolo."
                ]
            },
            {
                "numero": 2,
                "seccion": "CIRCUITO EQUIVALENTE",
                "titulo": "Resistencia de Radiación y Eficiencia",
                "puntos": [
                    "Resistencia de radiación $R_{rad}$: Modela la conversión irreversible de energía eléctrica del circuito en ondas electromagnéticas libres.",
                    "Resistencia óhmica de pérdidas $R_{loss}$: Disipación Joule por efecto piel en el metal de la antena.",
                    "Eficiencia de radiación: $\\eta_{rad} = \\frac{R_{rad}}{R_{rad} + R_{loss}}$. Se busca siempre $R_{rad} \\gg R_{loss}$."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Teoría de Líneas de Transmisión: Ecuaciones del Telegrafista e Impedancia $Z_0$",
        "objetivo": "Formular el modelo de parámetros distribuidos $(R', L', G', C')$ por unidad de longitud para líneas de transmisión eléctricas, deduciendo la impedancia característica $Z_0$ y la velocidad de fase.",
        "concepto_clave_latex": r"\frac{d^2 V}{dz^2} - \gamma^2 V = 0 \quad ; \quad Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}} \quad ; \quad \gamma = \alpha + j\beta = \sqrt{(R' + j\omega L')(G' + j\omega C')}",
        "ejemplo": "Problema 1: Una línea de transmisión aérea trifásica de alta tensión de 230 kV opera a $60\\text{ Hz}$ y puede considerarse sin pérdidas ($R' \\approx 0, G' \\approx 0$). Si los parámetros distribuidos son $L' = 1.25\\ \\mu\\text{H/m}$ y $C' = 8.85\\text{ pF/m}$, calcular su impedancia característica (impedancia de onda) y la velocidad de propagación: $Z_0 = \\sqrt{\\frac{L'}{C'}} = \\sqrt{\\frac{1.25 \\times 10^{-6}}{8.85 \\times 10^{-12}}} = \\sqrt{141242.9} \\approx 375.8\\ \\Omega$. Velocidad de fase: $v_p = \\frac{1}{\\sqrt{L' C'}} = \\frac{1}{\\sqrt{1.25 \\times 10^{-6} \\times 8.85 \\times 10^{-12}}} = \\frac{1}{\\sqrt{1.10625 \\times 10^{-17}}} \\approx 3.003 \\times 10^8\\text{ m/s} \\approx c$. Problema 2: La potencia natural de la línea o SIL (Surge Impedance Loading) es $P_{SIL} = \\frac{V_{LL}^2}{Z_0} = \\frac{(230 \\times 10^3)^2}{375.8} = \\frac{5.29 \\times 10^{10}}{375.8} = 140.77\\text{ MW}$, donde la línea transporta potencia con factor de potencia unitario sin requerir compensación reactiva.",
        "bloque_sugerido": "Líneas de Potencia 45 min • Ecuaciones del telegrafista y potencia natural SIL",
        "slides": [
            {
                "numero": 1,
                "seccion": "PARÁMETROS DISTRIBUIDOS",
                "titulo": "Validez del Modelo Distribuido",
                "puntos": [
                    "La teoría de circuitos concentrados de Kirchhoff es válida solo si la longitud de la línea es mucho menor que la longitud de onda física ($l \\ll \\lambda$).",
                    "A 60 Hz, $\\lambda = c/f = 5000\\text{ km}$; líneas mayores a 250 km ($l > \\lambda/20$) requieren rigurosamente el modelo de onda distribuido.",
                    "Cada tramo infinitesimal $\\Delta z$ contiene resistencia serie $R'\\Delta z$, inductancia $L'\\Delta z$, conductancia de fuga $G'\\Delta z$ y capacitancia $C'\\Delta z$."
                ]
            },
            {
                "numero": 2,
                "seccion": "LÍNEA LIBRE DE DISTORSIÓN",
                "titulo": "Condición de Heaviside",
                "puntos": [
                    "Oliver Heaviside demostró que si $\\frac{R'}{L'} = \\frac{G'}{C'}$, la atenuación $\\alpha = \\sqrt{R' G'}$ es independiente de la frecuencia.",
                    "La velocidad de fase se vuelve constante, eliminando la dispersión de pulsos electromagnéticos en telecomunicaciones.",
                    "Inspira el uso de inductancias de carga en cables telefónicos y de datos antiguos."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Líneas con Pérdidas, Coeficiente de Reflexión y Razón de Onda Estacionaria (VSWR)",
        "objetivo": "Calcular la onda reflejada debida al desacoplo de impedancia entre la línea y la carga, determinando el coeficiente de reflexión $\\Gamma_L$ y el patrón de voltaje estacionario VSWR.",
        "concepto_clave_latex": r"\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_L| e^{j\theta_L} \quad ; \quad \text{VSWR} = \frac{V_{\max}}{V_{\min}} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|} \ge 1",
        "ejemplo": "Problema 1: Una línea de transmisión coaxial de $Z_0 = 50\\ \\Omega$ alimenta una antena con impedancia compleja de carga $Z_L = 100 + j50\\ \\Omega$. Calcular el coeficiente de reflexión en la carga: $\\Gamma_L = \\frac{(100 + j50) - 50}{(100 + j50) + 50} = \\frac{50 + j50}{150 + j50} = \\frac{1 + j}{3 + j} = \\frac{(1+j)(3-j)}{3^2+1^2} = \\frac{3 - j + 3j - j^2}{10} = \\frac{4 + j2}{10} = 0.4 + j0.2$. Módulo: $|\\Gamma_L| = \\sqrt{0.4^2 + 0.2^2} = \\sqrt{0.16 + 0.04} = \\sqrt{0.20} \\approx 0.447$. Calcular la razón de onda estacionaria: $\\text{VSWR} = \\frac{1 + 0.447}{1 - 0.447} = \\frac{1.447}{0.553} \\approx 2.62$. Problema 2: La fracción de potencia incidente reflejada que no se entrega a la carga es $|\\Gamma_L|^2 = (0.447)^2 = 0.20$ ($20\\%$ de potencia reflejada), provocando calentamiento del transmisor si no se adapta la línea.",
        "bloque_sugerido": "Laboratorio RF 40 min • Medición de ondas estacionarias y reflectometría en el dominio del tiempo (TDR)",
        "slides": [
            {
                "numero": 1,
                "seccion": "DESACOPLO DE IMPEDANCIA",
                "titulo": "Interferencia Constructiva y Destructiva",
                "puntos": [
                    "La superposición de la onda incidente $V_0^+ e^{-\\gamma z}$ y la reflejada $V_0^- e^{+\\gamma z}$ genera un patrón estacionario espacial de nodos y antinodos.",
                    "Línea acoplada ($Z_L = Z_0$): $\\Gamma_L = 0$ y $\\text{VSWR} = 1.0$ (transferencia óptima total de potencia).",
                    "Cortocircuito ($Z_L = 0$): $\\Gamma_L = -1$, $\\text{VSWR} = \\infty$, con nodos de voltaje nulo en la carga.",
                    "Circuito abierto ($Z_L = \\infty$): $\\Gamma_L = +1$, $\\text{VSWR} = \\infty$, con antinodos de voltaje máximo en la carga."
                ]
            },
            {
                "numero": 2,
                "seccion": "SEGURIDAD EN SISTEMAS DE POTENCIA",
                "titulo": "Sobretensiones por Reflexión",
                "puntos": [
                    "En maniobras de conmutación de interruptores, las ondas viajeras de frente escarpado se duplican al llegar a extremos abiertos de líneas.",
                    "Las ondas reflejadas someten el aislamiento de devanados de transformadores a sobretensiones destructivas.",
                    "Uso de descargadores de sobretensión de óxido metálico (varistores MOV) para absorber ondas viajeras reflejadas."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "La Carta de Smith y Adaptación de Impedancias mediante Stubs",
        "objetivo": "Utilizar la Carta de Smith para calcular impedancias de entrada $Z_{in}(l)$, localizar puntos de máximo voltaje y diseñar redes de acoplamiento de reactancia mediante stubs simples en paralelo.",
        "concepto_clave_latex": r"z = r + j x = \frac{Z}{Z_0} = \frac{1 + \Gamma}{1 - \Gamma} \quad ; \quad Y_{stub} = -j Y_0 \cot(\beta l_{oc}) \text{ o } +j Y_0 \tan(\beta l_{sc})",
        "ejemplo": "Problema 1: Una carga normalizada $z_L = 2.0 - j1.0$ en una línea de $50\\ \\Omega$ se conecta a una distancia $d$ de un stub en paralelo cortocircuitado. En la Carta de Smith, se rota en sentido horario hacia el generador sobre el círculo de $|\\Gamma| = \\text{constante}$ hasta cortar el círculo de conductancia unitaria ($y = 1 + j b$). Para este punto, $b = +1.2$. Para cancelar la susceptancia reactiva se coloca el stub con susceptancia $b_{stub} = -1.2$. La longitud del stub en cortocircuito satisface: $-j \\cot(\\beta l_{sc}) = -j 1.2 \\implies \\cot(\\beta l_{sc}) = 1.2 \\implies \\tan(\\beta l_{sc}) = 0.833 \\implies \\beta l_{sc} = 0.695\\text{ rad} = 39.8^\\circ \\implies l_{sc} = \\frac{39.8}{360}\\lambda \\approx 0.111\\lambda$. Problema 2: La adaptación de impedancia elimina toda reflexión hacia la fuente, haciendo que $\\text{VSWR} = 1.0$ aguas arriba del stub.",
        "bloque_sugerido": "Taller Carta de Smith 45 min • Adaptación con stubs simples y dobles en software interactivo",
        "slides": [
            {
                "numero": 1,
                "seccion": "MAPEO CONFORME BILINEAL",
                "titulo": "Geometría de la Carta de Smith",
                "puntos": [
                    "Transformación conforme entre el semiplano derecho de impedancia compleja normalizada $z$ y el círculo unitario complejo $|\\Gamma| \\le 1$.",
                    "Círculos de resistencia constante: Círculos concéntricos tangentes al punto $(1, 0)$ en el extremo derecho.",
                    "Arcos de reactancia constante: Curvas ortogonales a los círculos de resistencia.",
                    "Una vuelta completa alrededor de la carta equivale exactamente a media longitud de onda ($\\lambda/2$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "ACONDICIONAMIENTO DE ALTA FRECUENCIA",
                "titulo": "Sintonizadores Stubs",
                "puntos": [
                    "Los stubs son segmentos de línea en cortocircuito o circuito abierto que aportan reactancia o susceptancia pura ajustable.",
                    "Evitan el uso de condensadores o inductores concentrados que a frecuencias de GHz se comportan de manera impredecible.",
                    "Indispensables en transmisores de microondas, radares y convertidores conmutados de alta velocidad GaN/SiC."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Guías de Onda Metálicas Rectangulares: Modos TE y TM y Frecuencia de Corte",
        "objetivo": "Resolver la propagación electromagnética en tuberías metálicas huecas conductoras, determinando las frecuencias de corte $f_c$, modos dominantes $TE_{10}$ y velocidades de grupo y fase.",
        "concepto_clave_latex": r"f_{c,mn} = \frac{1}{2\pi\sqrt{\mu\varepsilon}}\sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2} \quad ; \quad v_p = \frac{c}{\sqrt{1 - (f_c/f)^2}} > c \quad ; \quad v_g = c \sqrt{1 - (f_c/f)^2} < c",
        "ejemplo": "Problema 1: Una guía de onda rectangular de aire libre ($c = 3 \\times 10^8\\text{ m/s}$) tiene dimensiones interiores $a = 2.286\\text{ cm}$ y $b = 1.016\\text{ cm}$ (banda X estándar WR-90). Calcular la frecuencia de corte para el modo dominante $TE_{10}$ ($m=1, n=0$): $f_{c,10} = \frac{c}{2a} = \frac{3 \times 10^{10}\text{ cm/s}}{2 \times 2.286\text{ cm}} = \frac{3 \times 10^{10}}{4.572} = 6.562 \times 10^9\text{ Hz} = 6.562\text{ GHz}$. A una frecuencia operativa de $f = 10.0\text{ GHz}$, calcular la velocidad de grupo y de fase: Factor radical: $\\sqrt{1 - (6.562/10.0)^2} = \\sqrt{1 - 0.4306} = \\sqrt{0.5694} \\approx 0.7546$. Velocidad de grupo (transporte de energía e información): $v_g = 0.7546 \\times c \\approx 2.264 \\times 10^8\\text{ m/s} < c$. Velocidad de fase aparente de cresta: $v_p = c / 0.7546 \\approx 3.976 \\times 10^8\\text{ m/s} > c$. Producto: $v_p v_g = c^2$. Problema 2: Señales con frecuencia $f < f_c$ son evanescentes; no propagan potencia y decaen exponencialmente.",
        "bloque_sugerido": "Guías de Microondas 45 min • Distribución de campos en modo TE10 y atenuación en paredes",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONFINAMIENTO ELECTROMAGNÉTICO",
                "titulo": "Física de las Guías Huecas",
                "puntos": [
                    "Un conductor hueco cerrado no puede soportar ondas TEM (no existe modo TEM en guías monoconductoras ya que requeriría campos estáticos sin carga interna).",
                    "Modos TE (Transversal Eléctrico): $E_z = 0, H_z \\ne 0$.",
                    "Modos TM (Transversal Magnético): $H_z = 0, E_z \\ne 0$.",
                    "El modo de menor frecuencia de corte es el modo fundamental $TE_{10}$ fijado exclusivamente por la dimensión más ancha $a$."
                ]
            },
            {
                "numero": 2,
                "seccion": "TRANSPORTE DE ALTA POTENCIA",
                "titulo": "Ventajas sobre Cables Coaxiales",
                "puntos": [
                    "Al no tener conductor central ni aislante dieléctrico sólido, eliminan pérdidas de ruptura por alta tensión y calentamiento dieléctrico.",
                    "Soportan potencias continuas de megavatios en bandas de microondas y radares de alerta temprana.",
                    "Utilizadas para inyección de potencia de radiofrecuencia para calentamiento de plasma en reactores de confinamiento magnético (Tokamaks)."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Cavidades Resonantes Electromagnéticas y Factor de Calidad $Q$",
        "objetivo": "Modelar el almacenamiento de energía en cavidades metálicas cerradas tridimensionales, evaluando frecuencias de resonancia propias y el factor de calidad selectivo $Q$.",
        "concepto_clave_latex": r"f_{0,mnp} = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2 + \left(\frac{p}{d}\right)^2} \quad ; \quad Q = \omega_0 \frac{U_{almacenada}}{P_{disipada}} = \frac{\omega_0 (U_e + U_m)}{P_{paredes}}",
        "ejemplo": "Problema 1: Una cavidad resonante cúbica de aire ($a = b = d = 5\\text{ cm}$) tiene paredes de cobre ($\sigma = 5.8 \\times 10^7\\text{ S/m}$). Calcular la frecuencia de resonancia del modo fundamental $TE_{101}$ ($m=1, n=0, p=1$): $f_0 = \\frac{3 \\times 10^8}{2} \\sqrt{\\frac{1^2}{0.05^2} + 0 + \\frac{1^2}{0.05^2}} = 1.5 \\times 10^8 \\times \\frac{\\sqrt{2}}{0.05} = 1.5 \\times 10^8 \\times 28.284 = 4.243 \\times 10^9\\text{ Hz} = 4.243\\text{ GHz}$. Problema 2: En cavidades de cobre bien pulidas, el factor de calidad alcanza $Q \\approx 10000 - 30000$, proporcionando un ancho de banda extremadamente estrecho $\\Delta f = f_0 / Q \\approx 140\\text{ kHz}$, ideal como filtro pasabanda o cámara de magnetrón de microondas.",
        "bloque_sugerido": "Resonancia EM 40 min • Modos de cavidad y factor de calidad Q cargado vs descargado",
        "slides": [
            {
                "numero": 1,
                "seccion": "CIRCUITO RESONANTE 3D",
                "titulo": "Almacenamiento Confinado",
                "puntos": [
                    "Equivalente electromagnético tridimensional distribuido de un circuito tanque LC.",
                    "En la frecuencia de resonancia exacta $\\omega_0$, la energía eléctrica media almacenada en el volumen es idéntica a la magnética: $\\langle U_e \\rangle = \\langle U_m \\rangle$.",
                    "Las corrientes inducidas de radiofrecuencia circulan por una capa superficial de espesor $\\delta_s$ en las paredes metálicas internas."
                ]
            },
            {
                "numero": 2,
                "seccion": "SUPERCONDUCTIVIDAD RF",
                "titulo": "Cavidades de Niobio Superconductor",
                "puntos": [
                    "Enfriadas a 2 K con helio líquido, la resistencia superficial cae a nano-ohmios, logrando factores de calidad $Q > 10^9 - 10^{10}$.",
                    "Permiten generar gradientes de aceleración de más de 35 MV/m en aceleradores de partículas de radiación sincrotrón.",
                    "Sustentan fuentes de radiación utilizadas en la caracterización cuántica de nuevos materiales energéticos."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Circuitos Magnéticos, Histéresis y Pérdidas de Foucault en Núcleos",
        "objetivo": "Modelar circuitos magnéticos aplicando analogías de Ohm con reluctancia $\\mathcal{R}$, calculando pérdidas por histéresis de Steinmetz y pérdidas por corrientes de Foucault.",
        "concepto_clave_latex": r"\mathcal{F} = N I = \Phi \mathcal{R} \quad ; \quad \mathcal{R} = \frac{l}{\mu A} \quad ; \quad P_{fe} = P_h + P_e = k_h f B_{\max}^n + k_e f^2 t_{lam}^2 B_{\max}^2",
        "ejemplo": "Problema 1: Un núcleo de acero al silicio laminado tiene una longitud media de $l_c = 0.5\\text{ m}$, sección $A = 20\\text{ cm}^2 = 2 \\times 10^{-3}\\text{ m}^2$, permeabilidad relativa $\\mu_r = 2500$ y un entrehierro de aire de $l_g = 1.0\\text{ mm}$. Devanado de $N = 400$ espiras. Reluctancia del núcleo de acero: $\\mathcal{R}_c = \\frac{0.5}{2500 \\times 4\\pi \\times 10^{-7} \\times 2 \\times 10^{-3}} = \\frac{0.5}{6.283 \\times 10^{-6}} = 79577\\text{ A-v/Wb}$. Reluctancia del entrehierro de aire: $\\mathcal{R}_g = \\frac{1.0 \\times 10^{-3}}{4\\pi \\times 10^{-7} \\times 2 \\times 10^{-3}} = \\frac{1.0 \\times 10^{-3}}{2.513 \\times 10^{-9}} = 397887\\text{ A-v/Wb}$. Reluctancia total: $\\mathcal{R}_T = 79577 + 397887 = 477464\\text{ A-v/Wb}$. El entrehierro de 1 mm aporta el $83.3\\%$ de la resistencia al flujo. Para un flujo de $\\Phi = 2.4\\text{ mWb}$, la corriente requerida es $I = \\frac{\\Phi \\mathcal{R}_T}{N} = \\frac{0.0024 \\times 477464}{400} = 2.86\\text{ A}$. Problema 2: Laminar el núcleo en láminas de espesor $t_{lam} = 0.35\\text{ mm}$ aisladas con barniz carlite reduce las corrientes de Foucault proporcionalmente a $t_{lam}^2$, disminuyendo las pérdidas en más del $90\\%$.",
        "bloque_sugerido": "Máquinas Eléctricas 45 min • Ciclos B-H de histéresis y separación de pérdidas en el hierro",
        "slides": [
            {
                "numero": 1,
                "seccion": "ANALOGÍA MAGNÉTICA DE HOPKINSON",
                "titulo": "Fuerza Magnetomotriz y Reluctancia",
                "puntos": [
                    "Fuerza Magnetomotriz $\\mathcal{F} = N I$ análoga al voltaje $V$.",
                    "Flujo magnético $\\Phi = \\iint \\mathbf{B} \\cdot d\\mathbf{A}$ análogo a la corriente eléctrica $I$.",
                    "Reluctancia $\\mathcal{R} = \\frac{l}{\\mu A}$ análoga a la resistencia eléctrica $R$.",
                    "Permeancia $\\mathcal{P} = 1/\\mathcal{R}$ análoga a la conductancia $G$."
                ]
            },
            {
                "numero": 2,
                "seccion": "PÉRDIDAS EN EL HIERRO",
                "titulo": "Histéresis y Corrientes Parásitas",
                "puntos": [
                    "Pérdidas por Histéresis: Área encerrada por el lazo $B-H$ en cada ciclo de magnetización alternada ($W_h = \\oint H dB$).",
                    "Pérdidas de Foucault (Eddy Currents): Corrientes microscópicas en bucle inducidas por $\\frac{\\partial B}{\\partial t}$ dentro del material conductor del núcleo.",
                    "Uso de aceros eléctricos de grano orientado (GOES) para optimizar transformadores de distribución."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Efecto Proximidad y Distribución de Corriente en Conductores Multifilares",
        "objetivo": "Analizar la distorsión asimétrica de la densidad de corriente en conductores adyacentes debida a los campos magnéticos mutuos, evaluando la resistencia AC en cables y devanados.",
        "concepto_clave_latex": r"R_{AC} = R_{DC} \cdot k_{skin} \cdot k_{prox} \quad ; \quad k_{prox} \propto \left(\frac{d_{cond}}{s_{separacion}}\right)^2 f^2",
        "ejemplo": "Problema 1: Dos conductores cilíndricos paralelos transportan corrientes alternas en la misma dirección a $10\\text{ kHz}$. El campo magnético generado por el conductor 1 ejerce una fuerza de Lorentz sobre las cargas móviles del conductor 2, empujando la densidad de corriente hacia los bordes externos opuestos (efecto proximidad repulsivo). Si las corrientes circulan en direcciones opuestas, la densidad de corriente se concentra en las superficies interiores enfrentadas. En ambos casos, el área efectiva de conducción se contrae drásticamente, incrementando la resistencia AC hasta 4 veces la resistencia DC. Problema 2: El hilo de Litz (Litz wire), compuesto por decenas de hilos finamente aislados entre sí y trenzados en patrones transpuestos geométricos, asegura que cada hilo ocupe uniformemente todas las posiciones espaciales, cancelando el efecto proximidad en inversores solares.",
        "bloque_sugerido": "Electrónica de Potencia 40 min • Modelado de Dowell para resistencia AC en transformadores HF",
        "slides": [
            {
                "numero": 1,
                "seccion": "CAMPOS MAGNÉTICOS CRUZADOS",
                "titulo": "Mecanismo del Efecto Proximidad",
                "puntos": [
                    "A diferencia del efecto pelicular que es simétrico y puramente autoinducido, el efecto proximidad surge de la interacción con conductores vecinos.",
                    "Provoca puntos calientes ('hot spots') localizados en las capas internas de devanados de transformadores e inductores.",
                    "Aumenta exponencialmente con el número de capas enrolladas superpuestas."
                ]
            },
            {
                "numero": 2,
                "seccion": "MITIGACIÓN TÉCNICA",
                "titulo": "Hilo de Litz y Láminas de Cobre",
                "puntos": [
                    "Elegir el diámetro de cada hilo individual menor que la profundidad de piel ($d_{hilo} < 2\\delta_s$).",
                    "Uso de conductores en lámina plana (foil windings) para inductores de alta corriente en cargadores de vehículos eléctricos.",
                    "Intercalado de capas de primario y secundario (interleaving) para cancelar fuerzas magnetomotrices locales."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Inductancia Mutua, Coeficiente de Acoplamiento y Polaridad en Transformadores",
        "objetivo": "Calcular la inductancia mutua $M$ entre circuitos magnéticamente acoplados a partir del flujo concatenado, deduciendo la convención de puntos de polaridad y el coeficiente de acoplamiento $k$.",
        "concepto_clave_latex": r"M = k \sqrt{L_1 L_2} \quad [0 \le k \le 1] \quad ; \quad v_1 = L_1 \frac{di_1}{dt} \pm M \frac{di_2}{dt} \quad ; \quad v_2 = \pm M \frac{di_1}{dt} + L_2 \frac{di_2}{dt}",
        "ejemplo": "Problema 1: Dos bobinas acopladas sobre un núcleo toroidal tienen inductancias propias $L_1 = 400\\text{ mH}$, $L_2 = 100\\text{ mH}$ y un coeficiente de acoplamiento de $k = 0.95$. Calcular la inductancia mutua $M$: $M = 0.95 \\sqrt{0.400 \\times 0.100} = 0.95 \\times \\sqrt{0.040} = 0.95 \\times 0.200 = 0.190\\text{ H} = 190\\text{ mH}$. Si se conectan en serie con polaridad aditiva: $L_{eq,aditiva} = L_1 + L_2 + 2M = 400 + 100 + 2(190) = 880\\text{ mH}$. Con polaridad sustractiva: $L_{eq,sustractiva} = L_1 + L_2 - 2M = 500 - 380 = 120\\text{ mH}$. Problema 2: En sistemas de transferencia inalámbrica de potencia inductiva (WPT) para vehículos eléctricos, el núcleo de aire reduce el acoplamiento a $k \\approx 0.15 - 0.30$, requiriendo redes de compensación resonante serie-paralelo para maximizar la potencia transmitida.",
        "bloque_sugerido": "Laboratorio de Circuitos 40 min • Ensayo de acoplamiento mutuo y regla de los puntos",
        "slides": [
            {
                "numero": 1,
                "seccion": "ACOPLAMIENTO MAGNÉTICO",
                "titulo": "La Regla de los Puntos de Polaridad",
                "puntos": [
                    "Si una corriente entra por el terminal con punto de una bobina, la tensión inducida en la otra bobina es positiva en su correspondiente terminal con punto.",
                    "Físicamente representa el sentido relativo del devanado de las espiras en torno al núcleo magnético.",
                    "En transformadores de potencia de núcleo ferromagnético cerrado, $k > 0.998$, acercándose al transformador ideal."
                ]
            },
            {
                "numero": 2,
                "seccion": "TRANSFERENCIA INALÁMBRICA",
                "titulo": "Carga Inductiva Resonante",
                "puntos": [
                    "Permite cargar vehículos eléctricos sin contacto físico eliminando riesgos de choque eléctrico en lluvia.",
                    "Bobinas emisora y receptora sintonizadas a idéntica frecuencia resonante (típicamente $85\\text{ kHz}$ según norma SAE J2954).",
                    "Flujo magnético de dispersión controlado mediante blindajes de ferrita y aluminio para cumplir normas ICNIRP de exposición humana."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Tensor de Esfuerzos de Maxwell y Fuerzas Electromecánicas en Máquinas",
        "objetivo": "Calcular fuerzas y torques mecánicos a partir de la distribución espacial de campos electromagnéticos integrando el Tensor de Esfuerzos de Maxwell sobre superficies de control cerradas.",
        "concepto_clave_latex": r"T_{ij} = \varepsilon_0 \left( E_i E_j - \frac{1}{2}\delta_{ij} |\mathbf{E}|^2 \right) + \frac{1}{\mu_0} \left( B_i B_j - \frac{1}{2}\delta_{ij} |\mathbf{B}|^2 \right) \quad ; \quad \mathbf{F} = \oint_S \mathbf{T} \cdot d\mathbf{A}",
        "ejemplo": "Problema 1: En el entrehierro cilíndrico de un generador síncrono eólico de imanes permanentes de radio medio $r = 1.2\\text{ m}$, longitud axial $L = 0.8\\text{ m}$ y espesor de entrehierro $g = 3\\text{ mm}$, el campo radial es $B_r = 0.9\\text{ T}$ y el campo azimutal de reacción de armadura es $B_\\theta = 0.25\\text{ T}$. El esfuerzo de corte tangencial de Maxwell es: $\\sigma_{r\\theta} = \\frac{1}{\\mu_0} B_r B_\\theta = \\frac{0.9 \\times 0.25}{4\\pi \\times 10^{-7}} = \\frac{0.225}{1.2566 \\times 10^{-6}} = 1.79 \\times 10^5\\text{ N/m}^2 = 179\\text{ kPa}$. Superficie del entrehierro: $A = 2\\pi r L = 2\\pi(1.2)(0.8) = 6.032\\text{ m}^2$. Fuerza tangencial total: $F_\\theta = 1.79 \\times 10^5 \\times 6.032 = 1.08 \\times 10^6\\text{ N}$. Torque electromagnético generado: $\\tau = F_\\theta \\cdot r = 1.08 \\times 10^6 \\times 1.2 = 1.296\\text{ MN}\\cdot\\text{m}$. Problema 2: La atracción magnética radial normal $\\sigma_{rr} = \\frac{B_r^2 - B_\\theta^2}{2\\mu_0} \\approx \\frac{0.9^2}{2\\mu_0} \\approx 322\\text{ kPa}$ ejerce un esfuerzo de compresión masivo sobre los rodamientos mecánicos si existe excentricidad en el rotor.",
        "bloque_sugerido": "Electromecánica 45 min • Cálculo de par por tensor de Maxwell vs método de coenergía",
        "slides": [
            {
                "numero": 1,
                "seccion": "DENSIDAD DE FUERZA DE LORENTZ",
                "titulo": "Esfuerzos Mecánicos del Campo",
                "puntos": [
                    "Transforma la fuerza volumétrica de Lorentz $\\mathbf{f} = \\rho \\mathbf{E} + \\mathbf{J} \\times \\mathbf{B}$ en la divergencia de un tensor de tensiones mecánicas superficiales: $\\mathbf{f} = \\nabla \\cdot \\mathbf{T}$.",
                    "Tensión a lo largo de las líneas de campo magnético: Las líneas de campo actúan como cuerdas elásticas tensas ($B^2/(2\\mu)$).",
                    "Presión hidrostática perpendicular a las líneas de campo: Tienden a separarse y repelerse lateralmente."
                ]
            },
            {
                "numero": 2,
                "seccion": "SIMULACIÓN POR ELEMENTOS FINITOS",
                "titulo": "Cálculo de Torque en Motores Eléctricos",
                "puntos": [
                    "En software FEM (ANSYS Maxwell, FEMM), el torque se obtiene integrando numéricamente el tensor a lo largo de una banda de elementos en el aire del entrehierro.",
                    "No requiere conocer las fuerzas de Lorentz individuales espira por espira en los conductores ranurados.",
                    "Permite diseñar rotores con mínimo par de rizado ('cogging torque') para generadores eólicos direct-drive."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ruptura Dieléctrica, Descargas Parciales y Efecto Corona en Alta Tensión",
        "objetivo": "Modelar el campo eléctrico crítico de ionización del aire según la ley de Peek, calculando pérdidas de potencia por efecto corona y criterios de diseño de conductores en líneas de transmisión.",
        "concepto_clave_latex": r"E_0 = 30 m \delta \left( 1 + \frac{0.3}{\sqrt{\delta r}} \right) \quad [\text{kV/cm}] \quad ; \quad P_{corona} \propto \frac{242.2}{\delta}(f + 25)\sqrt{\frac{r}{D}}(V - V_d)^2",
        "ejemplo": "Problema 1: Calcular el gradiente crítico disruptivo de ruptura $E_0$ en aire seco a nivel del mar ($\delta = 1.0$) para un conductor de fase cilíndrico de radio $r = 1.5\\text{ cm}$ con factor de rugosidad superficial $m = 0.85$ (conductor trenzado envejecido). Aplicando la fórmula de Peek: $E_0 = 30(0.85)(1.0) \\left( 1 + \\frac{0.3}{\sqrt{1.0 \\times 1.5}} \\right) = 25.5 \\left( 1 + \\frac{0.3}{1.2247} \\right) = 25.5(1 + 0.245) = 25.5(1.245) = 31.75\\text{ kV/cm}$. Si el campo eléctrico superficial nominal en la línea supera los $31.75\\text{ kV/cm}$, el aire circundante se ioniza, desatando una descarga luminiscente continua (efecto corona). Problema 2: En días lluviosos en la Sierra Nevada de Santa Marta, la humedad reduce el factor $m$ a $0.6$, disparando las pérdidas por corona hasta $15\\text{ kW/km}$ por circuito trifásico y generando interferencia de radiofrecuencia (RIV) y zumbido acústico audible.",
        "bloque_sugerido": "Alta Tensión 45 min • Ley de Peek, diseño de haces de conductores y anillos anticorona",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DE LA DESCARGA EN GASES",
                "titulo": "Mecanismo de Avalancha de Townsend",
                "puntos": [
                    "Campos eléctricos elevados aceleran electrones libres iniciales provocando ionización por impacto en moléculas de $N_2$ y $O_2$.",
                    "Se forma una vaina de plasma luminosa azulada alrededor del conductor acompañada de síntesis de ozono ($O_3$) y ácido nítrico corrosivo.",
                    "Las pérdidas aumentan con el cuadrado del voltaje por encima del umbral de extinción ($V - V_d$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "INGENIERÍA DE LÍNEAS",
                "titulo": "Mitigación con Haces de Subconductores",
                "puntos": [
                    "Subdividir cada fase en un haz ('bundle') de 2, 3 o 4 conductores separados por espaciadores incrementa el radio geométrico equivalente ($r_{eq} = \\sqrt[n]{n r R^{n-1}}$).",
                    "Reduce drásticamente el gradiente de potencial superficial por debajo del límite crítico de Peek.",
                    "Uso de anillos anticorona toroidales en cadenas de aisladores para uniformizar la distribución de campo eléctrico en terminales."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Blindaje Electromagnético, Efecto Jaula de Faraday y Compatibilidad (EMC)",
        "objetivo": "Calcular la efectividad de apantallamiento $SE$ de recintos metálicos frente a ondas electromagnéticas radiadas e interferencias conducidas según normas IEC/IEEE.",
        "concepto_clave_latex": r"SE = R + A + B \quad [\text{dB}] \quad ; \quad A = 20 \log_{10}(e^{t/\delta_s}) \approx 8.686 \frac{t}{\delta_s} \quad ; \quad R = 20 \log_{10}\left( \frac{|\eta_0|}{4|\eta_s|} \right)",
        "ejemplo": "Problema 1: Una lámina de cobre de espesor $t = 0.5\\text{ mm}$ ($\\sigma = 5.8 \\times 10^7\\text{ S/m}$) se utiliza para blindar un centro de control de subestación frente a pulsos electromagnéticos de alta frecuencia de $f = 10\\text{ MHz}$. Profundidad de penetración a 10 MHz: $\\delta_s = \\frac{1}{\\sqrt{\\pi \\times 10^7 \\times 4\\pi \\times 10^{-7} \\times 5.8 \\times 10^7}} \\approx 0.0209\\text{ mm}$. Calcular la atenuación por absorción pura $A$: $A = 8.686 \\times \\frac{0.5\\text{ mm}}{0.0209\\text{ mm}} = 8.686 \\times 23.92 = 207.8\\text{ dB}$. Una atenuación de más de 200 dB reduce la potencia residual de la onda a una fracción menor a $10^{-20}$, garantizando un blindaje prácticamente hermético. Problema 2: A bajas frecuencias ($60\\text{ Hz}$), la impedancia intrínseca de campos magnéticos de alta corriente es muy baja, requiriendo materiales de alta permeabilidad magnética ($\mu$-metal o permalloy) para desviar las líneas de inducción magnética.",
        "bloque_sugerido": "Compatibilidad Electromagnética 40 min • Normas CISPR/IEC 61000 y efectividad de blindaje",
        "slides": [
            {
                "numero": 1,
                "seccion": "MECANISMOS DE APANTALLAMIENTO",
                "titulo": "Reflexión, Absorción y Múltiples Reflexiones",
                "puntos": [
                    "Pérdida por Reflexión ($R$): Desajuste entre la impedancia de la onda incidente y la impedancia característica del metal de blindaje.",
                    "Pérdida por Absorción ($A$): Disipación térmica Joule de corrientes parásitas al atravesar el espesor del material.",
                    "Factor de corrección de reflexiones internas múltiples ($B$): Relevante solo en láminas extremadamente delgadas ($t < \\delta_s$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "INTEGRIDAD DE SUBESTACIONES",
                "titulo": "Jaulas de Faraday y Puesta a Tierra",
                "puntos": [
                    "Cualquier ranura o apertura de ventilación en el gabinete actúa como una antena de ranura si su dimensión mayor se acerca a $\\lambda/2$.",
                    "Mallas de puesta a tierra equipotenciales de baja impedancia en subestaciones encapsuladas en $SF_6$ (GIS).",
                    "Protección contra pulsos electromagnéticos de origen nuclear (HEMP) y descargas atmosféricas directas."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Superconductividad, Fenómeno de Meissner y Cables HTS de Potencia",
        "objetivo": "Comprender la transición a resistencia eléctrica nula y expulsión de flujo magnético en superconductores de alta temperatura crítica (HTS), evaluando su aplicación en cables de transmisión de gran densidad energética.",
        "concepto_clave_latex": r"\mathbf{B} = 0 \quad [T < T_c, \ H < H_c \implies \text{Diamagnetismo Perfecto}] \quad ; \quad \mathbf{J}_c = J_c(T, B) \quad ; \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}",
        "ejemplo": "Problema 1: Un cable superconductor HTS de segunda generación basado en cintas de $YBCO$ ($YBa_2Cu_3O_{7-\\delta}$, $T_c = 93\\text{ K}$) opera refrigerado con nitrógeno líquido a $77\\text{ K}$. Una sola cinta de 4 mm de ancho y $1\\ \\mu\\text{m}$ de espesor superconductor transporta una corriente crítica de $I_c = 150\\text{ A}$ sin disipación Joule ($R = 0$). Calcular la densidad de corriente crítica en la capa activa: $A = 4 \\times 10^{-3}\\text{ m} \\times 10^{-6}\\text{ m} = 4 \\times 10^{-9}\\text{ m}^2$. Densidad de corriente: $J_c = \\frac{150\\text{ A}}{4 \\times 10^{-9}\\text{ m}^2} = 3.75 \\times 10^{10}\\text{ A/m}^2 = 37500\\text{ A/mm}^2$. Esto es más de 7000 veces superior a la densidad admisible en cables convencionales de cobre ($~5\\text{ A/mm}^2$). Problema 2: Un cable subterráneo HTS trifásico concéntrico de 15 cm de diámetro puede transportar 3.2 GW de potencia eléctrica a media tensión (50 kV), eliminando la necesidad de subestaciones transformadoras gigantes en centros urbanos densos.",
        "bloque_sugerido": "Superconductividad Aplicada 45 min • Ecuaciones de London y limitadores de corriente de falla (SFCL)",
        "slides": [
            {
                "numero": 1,
                "seccion": "ELECTRODINÁMICA DE LONDON",
                "titulo": "Resistencia Cero y Efecto Meissner",
                "puntos": [
                    "Primera Ecuación de London: $\\frac{\\partial \\mathbf{J}_s}{\\partial t} = \\frac{n_s e^2}{m} \\mathbf{E}$ (aceleración continua de pares de Cooper sin fricción).",
                    "Segunda Ecuación de London: $\\nabla \\times \\mathbf{J}_s = -\\frac{n_s e^2}{m} \\mathbf{B}$, que combinada con Ampère implica $\\nabla^2 \\mathbf{B} = \\frac{1}{\\lambda_L^2} \\mathbf{B}$.",
                    "El campo magnético se extingue exponencialmente en la superficie con una longitud de penetración de London $\\lambda_L \\approx 50 - 200\\text{ nm}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "REDES DE TRANSMISIÓN DEL FUTURO",
                "titulo": "Limitadores de Falla (SFCL) y Almacenamiento SMES",
                "puntos": [
                    "Limitadores de Corriente de Falla Superconductores (SFCL): Durante un cortocircuito, la corriente supera $I_c$, el material transita instantáneamente a estado resistivo normal (quench) frenando la falla en menos de 2 milisegundos sin piezas móviles.",
                    "Sistemas SMES: Almacenamiento magnético toroidal sin pérdidas de ciclado con tiempos de inyección de potencia de microsegundos.",
                    "Sistemas de refrigeración criogénica con circuito cerrado Stirling o Gifford-McMahon."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Métodos Numéricos Electromagnéticos: Diferencias Finitas (FDTD) y Elementos Finitos (FEM)",
        "objetivo": "Formular la discretización espaciotemporal de las ecuaciones rotacionales de Maxwell mediante el algoritmo de Yee (FDTD) y la formulación variacional de elementos finitos (FEM).",
        "concepto_clave_latex": r"E_x^{n+1/2}(i+1/2,j,k) = E_x^{n-1/2} + \frac{\Delta t}{\varepsilon \Delta y}(H_z - H_z) - \frac{\Delta t}{\varepsilon \Delta z}(H_y - H_y) \quad ; \quad \Delta t \le \frac{1}{c\sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2}}}",
        "ejemplo": "Problema 1: En una simulación FDTD tridimensional con celdas espaciales cúbicas de resolución $\\Delta x = \\Delta y = \\Delta z = 1.0\\text{ mm}$, calcular el paso de tiempo máximo permitido por la condición de estabilidad de Courant-Friedrichs-Lewy (CFL): $\\Delta t_{max} = \\frac{1.0 \\times 10^{-3}\\text{ m}}{3.0 \\times 10^8\\text{ m/s} \\times \\sqrt{3}} = \\frac{10^{-3}}{5.196 \\times 10^8} \\approx 1.924 \\times 10^{-12}\\text{ s} = 1.924\\text{ ps}$. Un paso temporal mayor genera inestabilidad numérica no física y divergencia exponencial instantánea del campo. Problema 2: En formulaciones FEM 2D para diseño de aisladores de subestación, se minimiza el funcional de energía electrostática $W[V] = \\frac{1}{2}\\iint \\varepsilon |\\nabla V|^2 dx dy$ sobre una malla de triángulos adaptativos.",
        "bloque_sugerido": "Computación Electromagnética 45 min • Algoritmo de celda intercalada de Kane Yee en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "DISCRETIZACIÓN TEMPORAL FDTD",
                "titulo": "La Malla Intercalada de Kane Yee",
                "puntos": [
                    "Las componentes de $\\mathbf{E}$ y $\\mathbf{H}$ se posicionan desplazadas espacialmente en medio paso de rejilla ($\\Delta x/2$) y temporalmente en medio paso de tiempo ($\\Delta t/2$).",
                    "Evalúa directamente los rotacionales de Maxwell sin inversión de matrices mediante actualización explícita ('leapfrog').",
                    "Condiciones de frontera absorbentes de capas perfectamente adaptadas (PML) para simular espacio abierto infinito sin reflexiones numéricas."
                ]
            },
            {
                "numero": 2,
                "seccion": "MÉTODO DE ELEMENTOS FINITOS (FEM)",
                "titulo": "Geometrías Complejas y Materiales No Lineales",
                "puntos": [
                    "Ideal para geometrías curvas de rotores ranurados y materiales con permeabilidad no lineal $\\mu(B)$ saturable.",
                    "Resuelve la formulación débil mediante funciones de base nodales o de borde (elementos de Whitney).",
                    "Núcleo de software de diseño industrial de alta fidelidad (COMSOL Multiphysics, ANSYS Maxwell)."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Campos Electromagnéticos Ambientales y Normatividad de Exposición en Subestaciones",
        "objetivo": "Evaluar los niveles de exposición ocupacional y poblacional a campos electromagnéticos de frecuencia industrial (60 Hz) generados por líneas de transmisión y subestaciones eléctricas, aplicando las directrices internacionales ICNIRP y el RETIE colombiano.",
        "concepto_clave_latex": r"B_{max, poblacional} \le 200\ \mu\text{T} \quad ; \quad B_{max, ocupacional} \le 1000\ \mu\text{T} \quad ; \quad E_{max, poblacional} \le 4.16\text{ kV/m} \quad [60\text{ Hz}]",
        "ejemplo": "Problema 1: A una distancia horizontal de $x = 15\\text{ m}$ del eje de una línea aérea trifásica de 500 kV suspendida a una altura mínima de $h = 12\\text{ m}$ sobre el suelo, las mediciones arrojan un campo magnético de $B = 14.5\\ \\mu\\text{T}$ y un campo eléctrico de $E = 2.1\\text{ kV/m}$ a 1 metro sobre el nivel del terreno. Comparar con los límites del Reglamento Técnico de Instalaciones Eléctricas de Colombia (RETIE / Resolución 90708): El límite poblacional continuo es $200\\ \\mu\\text{T}$ y $4.16\\text{ kV/m}$. Como $14.5\\ \\mu\\text{T} \\ll 200\\ \\mu\\text{T}$ y $2.1\\text{ kV/m} < 4.16\\text{ kV/m}$, la servidumbre cumple satisfactoriamente la normatividad de seguridad de salud pública. Problema 2: En el patio de una subestación de 230 kV, el campo eléctrico bajo pórticos puede alcanzar $8.5\\text{ kV/m}$, requiriendo trajes de protección conductivos (traje de Faraday) y protocolos de permanencia de tiempo restringido para los ingenieros de mantenimiento.",
        "bloque_sugerido": "Seguridad Electromagnética 40 min • Simulación de perfiles de campo bajo líneas de alta tensión",
        "slides": [
            {
                "numero": 1,
                "seccion": "BIOELECTROMAGNETISMO",
                "titulo": "Efectos Biológicos a Frecuencia Industrial (60 Hz)",
                "puntos": [
                    "A bajas frecuencias (60 Hz), los campos eléctricos y magnéticos no ionizantes no rompen enlaces moleculares ni causan calentamiento térmico.",
                    "El mecanismo primario es la inducción de densidades de corriente microscópicas ($J_{ind} = \\sigma_{tejido} E_{int}$) en tejidos nerviosos y musculares.",
                    "Las directrices ICNIRP imponen factores de seguridad de hasta 50 veces por debajo de los umbrales de estimulación sináptica detectable."
                ]
            },
            {
                "numero": 2,
                "seccion": "ZONAS DE SERVIDUMBRE Y RETIE",
                "titulo": "Franjas de Seguridad de Líneas de Transmisión",
                "puntos": [
                    "El ancho de la franja de servidumbre (retiradas mínimas de 15 a 60 metros según el nivel de tensión) garantiza que en el borde del corredor los campos no superen los límites poblacionales.",
                    "Cálculo de tensiones inducidas por acoplamiento capacitivo en vallas metálicas y tuberías paralelas.",
                    "Uso de medidores de campo triaxiales calibrados según norma IEEE Std 644 para certificación y licenciamiento ambiental."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_03041821)
    # Inject before the next subject marker: 01021805
    inject_topics_after('      - codigo: "01021805"', yaml_text)
    print("03041821 Electricidad y Magnetismo successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
