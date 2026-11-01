# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06011838 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Transformadores de Medida para Alta Tensión: TCs de Rogowski, TPs Capacitivos y Sensores Ópticos",
        "objetivo": "Modelar transductores de corriente y tensión para sistemas de potencia, analizando transformadores inductivos de protección clase 5P20, bobinas de Rogowski no saturables y sensores electroópticos de efecto Faraday/Pockels.",
        "concepto_clave_latex": r"v_{out}(t) = -M \frac{di(t)}{dt} \quad [\text{Bobina de Rogowski}] \quad ; \quad \theta_F = V_B \int_L \mathbf{B} \cdot d\mathbf{l} \quad [\text{Efecto Faraday Óptico}]",
        "ejemplo": "Problema 1: Una bobina de Rogowski toroidal con inductancia mutua $M = 0.25\\ \\mu\\text{H}$ rodea una barra colectora de 115 kV. Durante un cortocircuito simétrico a 60 Hz, la corriente de falla es $i(t) = 15000\\sqrt{2} \\sin(120\\pi t)\\text{ A}$. La tensión instantánea inducida en bornes de la bobina es: $v_{out}(t) = -M \\frac{di}{dt} = -(0.25 \\times 10^{-6})(15000\\sqrt{2})(120\\pi) \\cos(120\\pi t) = -1.999 \\cos(120\\pi t)\\text{ V}$. Un integrador analógico activo con constante de tiempo $\\tau = R C = 1/(120\\pi) = 2.653\\text{ ms}$ reconstruye la señal proporcional a la corriente primaria: $v_{int}(t) = -\\frac{1}{\\tau}\\int v_{out} dt = 7.535\\sqrt{2}\\sin(120\\pi t)\\text{ V}$. Al carecer de núcleo ferromagnético, la bobina jamás se satura incluso con corrientes de falla de $100\\text{ kA}$, garantizando linealidad absoluta para relés de protección diferencial. Problema 2: En un Transformador de Corriente Óptico (OCT), un haz láser linealmente polarizado atraviesa una fibra óptica dopada que rodea el conductor de alta tensión; el campo magnético rota el plano de polarización por efecto Faraday ($\\Delta \\theta = V_B I$), entregando una medición puramente digital inmune a interferencias electromagnéticas.",
        "bloque_sugerido": "Instrumentación de Potencia 45 min • Error de relación y ángulo en TCs según IEC 61869",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITES DE LOS TRANSFORMADORES CONVENCIONALES",
                "titulo": "Saturación Ferromagnética",
                "puntos": [
                    "Los TCs convencionales de hierro se saturan durante cortocircuitos severos con componente aperiódica DC, recortando la forma de onda secundaria.",
                    "La saturación ciega a los relés de protección diferencial, provocando disparos indebidos de subestaciones completas.",
                    "Peligro de muerte por sobretensión extrema si el circuito secundario de un TC tradicional se abre accidentalmente ($V_{sec} > 5\\text{ kV}$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "TRANSDUCTORES ELECTRÓNICOS (NCIT)",
                "titulo": "Bobinas de Rogowski y Sensores Ópticos",
                "puntos": [
                    "Bobina de Rogowski: Núcleo de aire flexible; ancho de banda de varios megahercios; peso liviano para montaje en celdas compactas GIS.",
                    "Transformador de Potencial Capacitivo (CCVT): Divisor capacitivo acoplado que permite inyectar simultáneamente señales de comunicación por onda portadora (PLC).",
                    "Sensores electro-ópticos no convencionales (NCIT): Cumplimiento de la norma IEC 61869-9 con salida directa en tramas digitales Sampled Values (SV)."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Medición de Calidad de Energía: Flicker, Sags, Swells y Armónicos según IEC 61000-4-30",
        "objetivo": "Analizar perturbaciones en la onda de tensión aplicando los algoritmos de clase A de la norma IEC 61000-4-30 para el cálculo de severidad de flicker ($P_{st}, P_{lt}$), huecos de tensión (sags) y sobretensiones temporales (swells).",
        "concepto_clave_latex": r"P_{st} = \sqrt{0.0314 P_{0.1} + 0.0525 P_{1} + 0.0657 P_{3} + 0.28 P_{10} + 0.08 P_{50}} \le 1.0 \quad ; \quad P_{lt} = \sqrt[3]{\frac{1}{12}\sum_{i=1}^{12} P_{st,i}^3} \le 0.8",
        "ejemplo": "Problema 1: Un analizador de calidad de energía clase A registra la tensión en el secundario de un transformador de 13.8 kV que alimenta un parque eólico en el Magdalena. Se detecta un hueco de tensión ('voltage sag') donde la tensión eficaz de media onda ($U_{rms(1/2)}$) desciende al $68\\%$ del valor nominal ($0.68\\text{ p.u.}$) con una duración de $\\Delta t = 180\\text{ ms}$. Según la curva de tolerancia ITIC/CBEMA, la perturbación se ubica en la zona de disparo de variadores de frecuencia industriales no protegidos. En el cálculo de flicker generado por el paso de las palas frente a la torre del aerogenerador ('tower shadow effect'), el medidor computa un índice de severidad de parpadeo a corto plazo (10 minutos) de $P_{st} = 1.35 > 1.0$, violando el código de red de XM y exigiendo la sintonización del compensador síncrono estático STATCOM. Problema 2: El análisis de subarmónicos e interarmónicos mediante ventanas FFT de 10 ciclos (200 ms a 50 Hz, 12 ciclos / 200 ms a 60 Hz) desagrega grupos armónicos según IEC 61000-4-7.",
        "bloque_sugerido": "Calidad de Red 45 min • Clasificación de eventos según estándar IEEE 1159 y curvas ITIC",
        "slides": [
            {
                "numero": 1,
                "seccion": "PERTURBACIONES TRANSITORIAS",
                "titulo": "Sags, Swells e Interrupciones",
                "puntos": [
                    "Hueco de Tensión (Sag/Dip): Disminución del voltaje RMS entre el 10% y el 90% con duración de 10 ms a 1 minuto; causado por cortocircuitos remotos y arranque de motores masivos.",
                    "Sobretensión Temporal (Swell): Aumento del voltaje RMS entre el 110% y el 180%; provocado por desconexión repentina de grandes cargas o fallas a tierra monobásicas.",
                    "Interrupción: Caída del voltaje eficaz por debajo del 10% nominal."
                ]
            },
            {
                "numero": 2,
                "seccion": "MEDICIÓN DE FLICKER (PARPADEO)",
                "titulo": "El Medidor de Flicker IEC 61000-4-15",
                "puntos": [
                    "Modela la respuesta fisiológica psicofísica del sistema ojo-cerebro humano ante la fluctuación luminosa de lámparas incandescentes.",
                    "Frecuencia más crítica: Fluctuaciones a $8.8\\text{ Hz}$, donde el ojo humano es extremadamente sensible a variaciones de tensión de apenas el $0.28\\%$.",
                    "$P_{st}$ evalúa 10 minutos; $P_{lt}$ evalúa 2 horas continuas con media cúbica ponderada."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Unidades de Medición Fasorial (PMU) y Sincrofasores GPS según IEEE C37.118",
        "objetivo": "Modelar la estimación de fasores sincronizados temporalmente por satélite GPS con precisión de microsegundos en redes de transporte, evaluando el Error de Vector Total (TVE) y la dinámica de área amplia (WAMS).",
        "concepto_clave_latex": r"\text{TVE} = \sqrt{\frac{(\hat{X}_r - X_r)^2 + (\hat{X}_i - X_i)^2}{X_r^2 + X_i^2}} \le 1.0\% \quad ; \quad X(t) = \frac{X_m}{\sqrt{2}} e^{j(2\pi f_0 t + \phi(t))}",
        "ejemplo": "Problema 1: Una PMU instalada en la subestación Sabanalarga 500 kV mide el sincrofasor de tensión de fase a 60 Hz sincronizada con la señal de pulso por segundo (1-PPS) de su reloj atómico GPS. El fasor real del sistema es $X = 288.68 \\angle 15.00^\\circ\\text{ kV}$. La PMU calcula un fasor estimado de $\\hat{X} = 287.50 \\angle 15.45^\\circ\\text{ kV}$ (error de amplitud de $-1.18\\text{ kV}$ y error angular de $+0.45^\\circ = +0.00785\\text{ rad}$). Calcular el Error de Vector Total (TVE): Error fasorial: $(\\hat{X} - X) = 287.50[\\cos(15.45^\\circ) + j\\sin(15.45^\\circ)] - 288.68[\\cos(15^\\circ) + j\\sin(15^\\circ)] = (277.10 + j76.88) - (278.84 + j74.72) = -1.74 + j2.16\\text{ kV}$. Magnitud del error vectorial: $|\\hat{X} - X| = \\sqrt{(-1.74)^2 + (2.16)^2} = \\sqrt{3.028 + 4.666} = \\sqrt{7.694} = 2.774\\text{ kV}$. TVE porcentual: $\\text{TVE} = \\frac{2.774}{288.68} \\times 100\\% = 0.961\\%$. Como $\\text{TVE} < 1.0\\%$, la PMU cumple estrictamente el criterio de precisión de clase M de la norma IEEE C37.118. Problema 2: Un error de sincronización de reloj de apenas $26.5\\ \\mu\\text{s}$ induce por sí solo un error de fase de $0.573^\\circ$, violando el límite del $1\\%$ de TVE.",
        "bloque_sugerido": "Sistemas WAMS 45 min • Arquitectura de concentradores PDC y detección de oscilaciones interárea",
        "slides": [
            {
                "numero": 1,
                "seccion": "FASORES SINCRONIZADOS EN EL TIEMPO",
                "titulo": "Sincrofasores vs SCADA Tradicional",
                "puntos": [
                    "SCADA tradicional: Muestreo asíncrono lento cada 2 a 4 segundos; mide solo magnitudes RMS sin información de ángulo de fase relativo.",
                    "PMU (Phasor Measurement Unit): Muestreo ultra-rápido sincronizado por GPS a 30, 60 o 120 fasores completos por segundo.",
                    "Permite observar en tiempo real la diferencia angular exacta $\\delta_A - \\delta_B$ entre subestaciones separadas cientos de kilómetros, midiendo la estabilidad angular del rotor."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONCENTRADORES DE DATOS (PDC)",
                "titulo": "Sistemas WAMS y Detección de Colapso",
                "puntos": [
                    "Los concentradores PDC (Phasor Data Concentrators) alinean temporalmente las tramas de datos recibidas de decenas de PMUs distribuidas.",
                    "Detecta en milisegundos modos oscilatorios interárea mal amortiguados ($0.1 - 0.8\\text{ Hz}$).",
                    "Habilita esquemas de desconexión automática de carga en área amplia (SIPS) para evitar 'blackouts' nacionales."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Radiometría Solar: Piranómetros Clase A (ISO 9060) y Pirheliómetros",
        "objetivo": "Evaluar la incertidumbre metrológica en la medición del recurso solar mediante piranómetros termoeléctricos de cúpula doble clase A (ISO 9060), pirheliómetros montados en seguidores solares y calibración en exteriores.",
        "concepto_clave_latex": r"G = \frac{V_{termo}}{\mathcal{S}} \quad [\mu\text{V} / (\text{W/m}^2)] \quad ; \quad GHI = DNI \cos\theta_z + DHI \quad ; \quad u_c(G) \le 1.5\%",
        "ejemplo": "Problema 1: Un piranómetro termoeléctrico Clase A (antiguamente llamado Estándar Secundario) tiene una constante de sensibilidad calibrada de $\\mathcal{S} = 8.52\\ \\mu\\text{V}/(\\text{W/m}^2)$ con una incertidumbre expandida ($k=2$) del $1.2\\%$. El sensor se conecta a un registrador de datos de alta precisión con error de lectura en microvoltios de $\\pm 2\\ \\mu\\text{V}$. Al mediodía solar, el registrador mide una tensión de $V = 8.136\\text{ mV} = 8136\\ \\mu\\text{V}$. Calcular la irradiancia global horizontal (GHI) medida: $GHI = \\frac{8136\\ \\mu\\text{V}}{8.52\\ \\mu\\text{V}/(\\text{W/m}^2)} = 954.93\\text{ W/m}^2$. Incertidumbre combinada de la medición: Incertidumbre por sensibilidad: $u(S) = \\frac{1.2\\%}{2} = 0.6\\% \\implies 5.73\\text{ W/m}^2$. Incertidumbre por resolución del voltímetro: $u(V) = \\frac{2}{\\sqrt{3}} \\times \\frac{1}{8.52} = 0.135\\text{ W/m}^2$. Incertidumbre combinada: $u_c = \\sqrt{(5.73)^2 + (0.135)^2} \\approx 5.73\\text{ W/m}^2$. Incertidumbre expandida ($95\\%$ de confianza): $U = 2 u_c = 11.46\\text{ W/m}^2$ ($GHI = 954.9 \\pm 11.5\\text{ W/m}^2$). Problema 2: En estaciones de prospección bancable de energía solar, un pirheliómetro colimado en un seguidor biaxial mide la radiación directa $DNI$, mientras un piranómetro con bola de sombra mide la difusa $DHI$, verificando la consistencia física estricta con la radiación global horizontal.",
        "bloque_sugerido": "Metrología Solar 45 min • Clasificación ISO 9060:2018 y corrección de compensación térmica (zero offset)",
        "slides": [
            {
                "numero": 1,
                "seccion": "PRINCIPIO TERMOELÉCTRICO",
                "titulo": "Termopila Negra vs Fotodiodo de Silicio",
                "puntos": [
                    "Piranómetros de Termopila: Absorbente negro con respuesta espectral perfectamente plana desde 285 hasta 3000 nm (todo el espectro solar); referencia oficial de medición.",
                    "Sensores de Fotodiodo de Silicio: Económicos pero limitados a 400-1100 nm; sensibles a variaciones de temperatura y espectro de masa de aire.",
                    "Doble cúpula de vidrio de cuarzo óptico: Aíslan la termopila de las corrientes convectivas de viento y la radiación infrarroja lejana ambiental."
                ]
            },
            {
                "numero": 2,
                "seccion": "NORMAS Y CLASIFICACIÓN",
                "titulo": "ISO 9060:2018 y WMO",
                "puntos": [
                    "Clase A (Spectrally Flat Class A): Tiempo de respuesta $< 0.5\\text{ s}$, 'zero offset' térmico $< 7\\text{ W/m}^2$, error direccional (coseno) $< 10\\text{ W/m}^2$.",
                    "Calibración periódica cada 2 años trazable al Grupo Mundial de Radiómetros (WRR) en Davos, Suiza.",
                    "Ventilación forzada y calefacción integrada para evitar formación de rocío matutino y escarcha en la cúpula."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Anemometría Eólica: Sensores Sónicos 3D, Copas MEASNET y Perfiladores LiDAR",
        "objetivo": "Medir el campo vectorial de velocidades de viento, cizalladura vertical de viento (Wind Shear) y perfil de turbulencia (TI) mediante anemómetros de copas calibrados MEASNET y perfiladores ópticos LiDAR de efecto Doppler.",
        "concepto_clave_latex": r"v(z) = v_{ref} \left(\frac{z}{z_{ref}}\right)^\alpha \quad ; \quad TI = \frac{\sigma_v}{\bar{v}} \times 100\% \quad ; \quad \Delta f_D = 2 \frac{v_{radial}}{c} f_0 \quad [\text{LiDAR}]",
        "ejemplo": "Problema 1: Una torre meteorológica de prospección eólica en La Guajira tiene anemómetros de copas Clase 1A calibrados según estándar MEASNET instalados a 40 m y a 80 m de altura. Los registros horarios promedios arrojan $v(40\\text{ m}) = 7.2\\text{ m/s}$ y $v(80\\text{ m}) = 8.5\\text{ m/s}$. Calcular el exponente de cizalladura vertical de la ley de Hellmann $\\alpha$: $\\frac{8.5}{7.2} = \\left( \\frac{80}{40} \\right)^\\alpha \\implies 1.1805 = 2^\\alpha \\implies \\alpha = \\frac{\\ln(1.1805)}{\\ln(2)} = \\frac{0.1659}{0.6931} = 0.239$. Si el buje (hub) de un aerogenerador de 4.5 MW se instalará a $120\\text{ m}$ de altura, extrapolar la velocidad esperada de viento: $v(120\\text{ m}) = 8.5 \\times \\left( \\frac{120}{80} \\right)^{0.239} = 8.5 \\times (1.5)^{0.239} = 8.5 \\times 1.1017 = 9.36\\text{ m/s}$. Dado que la potencia del viento depende del cubo de la velocidad, la potencia disponible a 120 m es $(9.36/7.2)^3 = 2.19$ veces mayor que a 40 m. Problema 2: Un LiDAR Doppler continuo montado en el suelo dispara rayos láser infrarrojos hacia la atmósfera, midiendo la velocidad del viento por retrodispersión de aerosoles a múltiples alturas simultáneas ($40\\text{ m}$ a $250\\text{ m}$) sin erigir costosas torres de acero.",
        "bloque_sugerido": "Evaluación del Recurso Eólico 45 min • Calibración MEASNET y anemómetros ultrasónicos 3D de tiempo de tránsito",
        "slides": [
            {
                "numero": 1,
                "seccion": "TECNOLOGÍAS DE ANEMOMETRÍA",
                "titulo": "Copas Mecánicas vs Ultrasónicos vs LiDAR",
                "puntos": [
                    "Anemómetros de Copas: Estándar histórico IEC 61400-12-1; precisos en flujo horizontal estacionario; sufren de sobrevelocidad ('overspeeding') en ráfagas turbulentas.",
                    "Anemómetros Ultrasónicos 3D: Miden el tiempo de tránsito de pulsos acústicos entre transductores enfrentados; miden componentes $u, v, w$ sin inercia mecánica a frecuencias $> 20\\text{ Hz}$.",
                    "Sistemas LiDAR / SoDAR: Perfilado vertical no invasivo por efecto Doppler óptico/acústico hasta 300 m de altura."
                ]
            },
            {
                "numero": 2,
                "seccion": "INTENSIDAD DE TURBULENCIA (TI)",
                "titulo": "Fatiga en Palas de Turbinas Eólicas",
                "puntos": [
                    "Intensidad de Turbulencia $TI = \\sigma_v / \\bar{v}$ calculada a partir de la desviación estándar en ventanas de 10 minutos.",
                    "Clases de viento según IEC 61400-1: Clase A ($TI_{ref} = 16\\%$, alta turbulencia), Clase B ($14\\%$), Clase C ($12\\%$).",
                    "Turbulencias excesivas provocan cargas cíclicas de fatiga mecánica en la raíz de las palas y la caja multiplicadora."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Sensores de Par Torsional, Potencia Mecánica y Velocidad en Ejes Rotativos",
        "objetivo": "Medir torque torsional dinámico y velocidad angular en trenes de potencia de turbinas y motores mediante galgas extensiométricas en puente de Wheatstone con telemetría inalámbrica y codificadores ópticos.",
        "concepto_clave_latex": r"\tau = \frac{J_p G \theta}{L} \quad ; \quad \varepsilon_{45^\circ} = \frac{\tau D}{4 G J_p} = \frac{8 T}{\pi G D^3} \quad ; \quad P_{mec} = T \omega = T \left(\frac{2\pi n}{60}\right)",
        "ejemplo": "Problema 1: Un eje macizo de acero forjado de transmisión mecánica ($G = 80\\text{ GPa}$, diámetro exterior $D = 120\\text{ mm}$) conecta una turbina hidráulica con un generador a $n = 720\\text{ rpm}$. Se instala una roseta de cuatro galgas extensiométricas orientadas a $\\pm 45^\\circ$ en configuración de puente completo de Wheatstone ($GF = 2.1$, voltaje de excitación $V_{in} = 5.0\\text{ V}$). Durante la prueba a plena carga, el sistema de telemetría digital de radiofrecuencia acoplado al eje rotativo transmite una lectura de salida del puente de $V_{out} = 2.52\\text{ mV}$. Deformación unitaria por torsión: $\\varepsilon = \\frac{V_{out}}{V_{in} \\cdot GF} = \\frac{2.52 \\times 10^{-3}}{5.0 \\times 2.1} = 2.40 \\times 10^{-4}\\text{ strain} = 240\\ \\mu\\varepsilon$. Despejando el par torsional: $T = \\frac{\\pi G D^3 \\varepsilon}{8} = \\frac{\\pi (80 \\times 10^9)(0.12)^3 (2.40 \\times 10^{-4})}{8} = \\frac{\\pi \\times 80 \\times 10^9 \\times 0.001728 \\times 2.40 \\times 10^{-4}}{8} = 13028.8\\text{ N}\\cdot\\text{m} = 13.03\\text{ kN}\\cdot\\text{m}$. Potencia mecánica entregada al generador: $P_{mec} = T \\omega = 13028.8 \\times \\left( \\frac{2\\pi \\times 720}{60} \\right) = 13028.8 \\times 75.398 = 982345\\text{ W} = 982.35\\text{ kW}$. Problema 2: El uso de puentes completos de 4 galgas activas a $\\pm 45^\\circ$ cancela por simetría cualquier señal parásita inducida por flexión del eje o dilatación térmica axial.",
        "bloque_sugerido": "Ensayos Dinámicos 40 min • Calibración de torquímetros rotativos y codificadores ópticos en cuadratura",
        "slides": [
            {
                "numero": 1,
                "seccion": "DEFORMACIÓN POR CORTE TORSIONAL",
                "titulo": "Esfuerzos Principales a 45 Grados",
                "puntos": [
                    "La torsión pura genera un estado de esfuerzo cortante puro $\\tau = T r / J_p$.",
                    "En los ejes inclinados a $\\pm 45^\\circ$ respecto a la generatriz del cilindro, el esfuerzo cortante puro se transforma en esfuerzos principales normales de tracción pura (+45°) y compresión pura (-45°).",
                    "Disponer las galgas a $\\pm 45^\\circ$ maximiza la sensibilidad eléctrica del puente de Wheatstone ($V_{out} = V_{in} GF \\varepsilon$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "TELEMETRÍA Y ACOPLAMIENTO SIN CONTACTO",
                "titulo": "Eliminación de Anillos Rozantes",
                "puntos": [
                    "Los anillos rozantes mecánicos convencionales con escobillas sufren desgaste prematuro, generan ruido eléctrico por chispas y requieren mantenimiento continuo.",
                    "Torquímetros de telemetría moderna: Transmisión digital de datos por radiofrecuencia (2.4 GHz) o acoplamiento inductivo rotativo sin rozamiento.",
                    "Permite medir el rendimiento mecánico exacto de bombas, turbinas y reductores eólicos en operación comercial continua."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Medición Ultrasónica y Electromagnética de Caudal en Tuberías Forzadas",
        "objetivo": "Modelar caudalímetros ultrasónicos de tiempo de tránsito multi-trayectoria según norma IEC 60041 para ensayos oficiales de rendimiento de turbinas y caudalímetros electromagnéticos por ley de Faraday.",
        "concepto_clave_latex": r"v = \frac{L^2}{2 D \cos\theta}\left(\frac{t_{down} - t_{up}}{t_{down} \cdot t_{up}}\right) \quad ; \quad Q = \frac{\pi D^2}{4}\sum_{i=1}^M w_i v_i \quad ; \quad E_{mag} = B \cdot D \cdot v",
        "ejemplo": "Problema 1: En una tubería forzada de $D = 2.0\\text{ m}$ de una central hidroeléctrica, se instala un caudalímetro ultrasónico de tiempo de tránsito clamp-on con dos transductores piezoeléctricos separados una trayectoria acústica inclinada a $\\theta = 45^\\circ$ con longitud $L = 2.828\\text{ m}$. Velocidad del sonido en agua: $c \\approx 1480\\text{ m/s}$. El tiempo de tránsito aguas abajo es $t_{down} = 1.9080\\text{ ms}$ y aguas arriba es $t_{up} = 1.9140\\text{ ms}$ (diferencia de tiempo de vuelo de $\\Delta t = 6.0\\ \\mu\\text{s}$). Calcular la velocidad media del agua en la línea acústica: $t_{down} \\cdot t_{up} = (1.908 \\times 10^{-3})(1.914 \\times 10^{-3}) = 3.6519 \\times 10^{-6}\\text{ s}^2$. Velocidad: $v = \\frac{(2.828)^2}{2(2.0)\\cos 45^\\circ} \\left( \\frac{6.0 \\times 10^{-6}}{3.6519 \\times 10^{-6}} \\right) = \\frac{7.9976}{2.8284} \\times 1.643 = 2.8276 \\times 1.643 = 4.646\\text{ m/s}$. Caudal aproximado: $Q = \\frac{\\pi(2.0)^2}{4} \\times 4.646 = 3.1416 \\times 4.646 = 14.595\\text{ m}^3/\\text{s}$. Problema 2: Para mediciones de aceptación garantizada de turbinas hidráulicas (IEC 60041), se exigen configuraciones de al menos 4 u 8 trayectorias acústicas cruzadas (método de Gauss-Jacobi) para integrar asimetrías y perfiles de velocidad perturbados con incertidumbre global inferior al $\\pm 0.5\\%$.",
        "bloque_sugerido": "Metrología de Fluidos 45 min • Caudalímetros ultrasónicos de tiempo de tránsito vs efecto Doppler",
        "slides": [
            {
                "numero": 1,
                "seccion": "TIEMPO DE TRÁNSITO ULTRASÓNICO",
                "titulo": "Velocidad del Sonido a Favor y en Contra del Flujo",
                "puntos": [
                    "El pulso ultrasónico que viaja a favor de la corriente viaja más rápido ($c + v\\cos\\theta$); el que viaja en contra viaja más lento ($c - v\\cos\\theta$).",
                    "La diferencia de tiempos $\\Delta t$ es directamente proporcional a la velocidad media del fluido e independiente de la velocidad absoluta del sonido en el medio.",
                    "No introduce ninguna pérdida de carga hidrodinámica ni piezas móviles en la tubería."
                ]
            },
            {
                "numero": 2,
                "seccion": "CAUDALÍMETROS ELECTROMAGNÉTICOS",
                "titulo": "Ley de Inducción de Faraday",
                "puntos": [
                    "Bobinas externas generan un campo magnético $\\mathbf{B}$ perpendicular al flujo de agua conductora ($\\sigma > 5\\ \\mu\\text{S/cm}$).",
                    "Dos electrodos en contacto con el fluido miden la tensión inducida $E = B D v$.",
                    "Excelente para aguas turbias con sedimentos, fangos de digestores de biogás y salmueras geotérmicas."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Cromatografía de Gases en Línea para Biogás, Gas Natural e Hidrógeno",
        "objetivo": "Modelar el principio de separación cromatográfica en fase gaseosa (GC) con detector de conductividad térmica (TCD) y ionización de llama (FID) para la determinación en tiempo real de la composición molar y poder calorífico (Wobbe Index).",
        "concepto_clave_latex": r"I_W = \frac{\text{HHV}}{\sqrt{SG}} \quad ; \quad SG = \frac{M_{gas}}{M_{aire}} \quad ; \quad t_R = t_M (1 + k') \quad [\text{Tiempo de Retención}]",
        "ejemplo": "Problema 1: Un cromatógrafo de gases en línea industrial analiza una muestra de gas natural antes de alimentar una turbina de gas. El análisis reporta la siguiente composición molar fraccional: $90.0\\% CH_4$ ($M=16.04$, $\\text{HHV} = 37.7\\text{ MJ/Nm}^3$), $6.0\\% C_2H_6$ ($M=30.07$, $\\text{HHV} = 66.1\\text{ MJ/Nm}^3$), $2.0\\% C_3H_8$ ($M=44.10$, $\\text{HHV} = 94.0\\text{ MJ/Nm}^3$), $1.5\\% N_2$ ($M=28.01$, $\\text{HHV} = 0$), $0.5\\% CO_2$ ($M=44.01$, $\\text{HHV} = 0$). Calcular la masa molar aparente, la densidad relativa ($SG$) y el Índice de Wobbe del gas: Masa molar: $M = 0.90(16.04) + 0.06(30.07) + 0.02(44.10) + 0.015(28.01) + 0.005(44.01) = 14.436 + 1.804 + 0.882 + 0.420 + 0.220 = 17.762\\text{ kg/kmol}$. Densidad relativa: $SG = \\frac{17.762}{28.97} = 0.613$. Poder calorífico de la mezcla: $\\text{HHV}_m = 0.90(37.7) + 0.06(66.1) + 0.02(94.0) = 33.93 + 3.966 + 1.88 = 39.776\\text{ MJ/Nm}^3$. Índice de Wobbe: $I_W = \\frac{39.776}{\\sqrt{0.613}} = \\frac{39.776}{0.783} = 50.80\\text{ MJ/Nm}^3$. El gas cumple las especificaciones de intercambiabilidad del quemador ($48.5 < I_W < 52.5\\text{ MJ/Nm}^3$). Problema 2: En mezclas de hidrógeno-gas natural ('H2-blending' en gasoductos), el cromatógrafo detecta enriquecimientos de $H_2$ en menos de 90 segundos mediante detectores micro-TCD.",
        "bloque_sugerido": "Análisis Instrumental 45 min • Columnas capilares de tamiz molecular y cálculo de Índice de Wobbe",
        "slides": [
            {
                "numero": 1,
                "seccion": "SEPARACIÓN CROMATOGRÁFICA",
                "titulo": "Fase Móvil y Fase Estacionaria",
                "puntos": [
                    "El gas portador inerte (helio o argón) arrastra la muestra a través de una columna capilar recubierta con polímero o zeolitas porosas.",
                    "Cada molécula interactúa con diferente afinidad química, emergiendo a tiempos de retención ($t_R$) característicos y únicos.",
                    "El área bajo el pico del cromatograma es directamente proporcional a la concentración molar de esa especie."
                ]
            },
            {
                "numero": 2,
                "seccion": "DETECTORES INDUSTRIALES (TCD vs FID)",
                "titulo": "Transducción de Composición",
                "puntos": [
                    "Detector de Conductividad Térmica (TCD): Mide el cambio de enfriamiento de un filamento caliente de tungsteno; detecta especies universales ($H_2, N_2, O_2, CO_2, CH_4$).",
                    "Detector de Ionización de Llama (FID): Quema hidrocarburos en llama de hidrógeno generando iones; sensibilidad extrema para hidrocarburos pesados (C6+).",
                    "Determinación en continuo del poder calorífico para facturación en custodia y control de combustión."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis de Emisiones en Chimenea: Sensores de Circonia ($O_2$), NDIR y CEMS",
        "objetivo": "Diseñar Sistemas de Monitoreo Continuo de Emisiones (CEMS) para centrales térmicas y calderas de biomasa, evaluando celdas electroquímicas de óxido de zirconio para $O_2$ y fotometría infrarroja no dispersiva (NDIR) para $CO, CO_2$ y $SO_2$.",
        "concepto_clave_latex": r"E_{Nernst} = \frac{RT}{4F}\ln\left(\frac{P_{O_2,ref}}{P_{O_2,humos}}\right) \quad [\text{Sonda Lambda/Circonia}] \quad ; \quad I = I_0 e^{-\alpha(\lambda) \cdot c \cdot L} \quad [\text{NDIR}]",
        "ejemplo": "Problema 1: Una sonda de oxígeno de óxido de zirconio ($ZrO_2$ dopado con itria) opera a $750^\\circ\\text{C}$ (1023.15 K) en el conducto de gases de escape de una caldera de biomasa. La cara de referencia se expone a aire atmosférico limpio ($20.9\\% O_2$, $P_{ref} = 0.209\\text{ atm}$). La celda galvánica genera un potencial de equilibrio de Nernst de $E = 35.8\\text{ mV} = 0.0358\\text{ V}$. Calcular el porcentaje de oxígeno residual en los humos de combustión: Parámetros: $R = 8.314\\text{ J/(mol K)}$, $F = 96485\\text{ C/mol}$. Factor: $\\frac{RT}{4F} = \\frac{8.314 \\times 1023.15}{4 \\times 96485} = \\frac{8506.5}{385940} = 0.02204\\text{ V}$. Despejando: $\\ln\\left(\\frac{0.209}{P_{humos}}\\right) = \\frac{0.0358}{0.02204} = 1.6243 \\implies \\frac{0.209}{P_{humos}} = e^{1.6243} = 5.075 \\implies P_{humos} = \\frac{0.209}{5.075} = 0.04118\\text{ atm} = 4.12\\% O_2$. Una concentración de $4.1\\% O_2$ residual confirma una combustión controlada con un exceso de aire óptimo del $24\\%$. Problema 2: En el analizador NDIR para monóxido de carbono ($CO$), la atenuación espectral a $4.67\\ \\mu\\text{m}$ mide trazas de $CO$ con resolución de 1 ppm según la ley de Beer-Lambert.",
        "bloque_sugerido": "Monitoreo Ambiental 45 min • Arquitectura CEMS extractiva vs in-situ y normatividad EPA/Resolución 909",
        "slides": [
            {
                "numero": 1,
                "seccion": "SONDAS DE CIRCONIA (O2 EN TIEMPO REAL)",
                "titulo": "Conducción de Iones Óxido",
                "puntos": [
                    "A temperaturas superiores a $600^\\circ\\text{C}$, el óxido de zirconio ($ZrO_2$) se vuelve un conductor sólido puro de iones oxígeno ($O^{2-}$).",
                    "El gradiente de presiones parciales de oxígeno entre el aire ambiente y los humos genera una fuerza electromotriz de Nernst de respuesta instantánea ($< 1\\text{ s}$).",
                    "Sensor directo in-situ instalado en el corazón de la chimenea sin requerir acondicionamiento de muestra."
                ]
            },
            {
                "numero": 2,
                "seccion": "FOTOMETRÍA NDIR",
                "titulo": "Huella Infrarroja de Gases de Efecto Invernadero",
                "puntos": [
                    "Moléculas heteroatómicas ($CO, CO_2, SO_2, CH_4$) absorben radiación infrarroja en bandas de longitud de onda resonantes específicas.",
                    "Filtros ópticos de interferencia aíslan la banda objetivo mientras una cubeta de gas de referencia compensa el envejecimiento de la fuente óptica.",
                    "Requisito ambiental legal obligatorio para el reporte continuo de emisiones contaminantes a las corporaciones autónomas regionales (CARs)."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Termometría de Radiación Infrarroja y Pirómetros Ópticos de Alta Temperatura",
        "objetivo": "Medir sin contacto temperaturas extremas en cámaras de combustión, receptores solares de torre y metales fundidos mediante pirómetros ópticos monocromáticos y de relación de dos colores (bicolor).",
        "concepto_clave_latex": r"\frac{1}{T_{real}} = \frac{1}{T_{aparente}} + \frac{\lambda}{c_2}\ln(\varepsilon_\lambda) \quad ; \quad \frac{E(\lambda_1)}{E(\lambda_2)} = \frac{\varepsilon_{\lambda_1}}{\varepsilon_{\lambda_2}}\left(\frac{\lambda_2}{\lambda_1}\right)^5 \exp\left[-\frac{c_2}{T}\left(\frac{1}{\lambda_1} - \frac{1}{\lambda_2}\right)\right]",
        "ejemplo": "Problema 1: Un pirómetro infrarrojo monocromático sintonizado a $\\lambda = 0.90\\ \\mu\\text{m}$ ($c_2 = 14388\\ \\mu\\text{m}\\cdot\\text{K}$) apunta hacia un tubo receptor de sales fundidas de una torre solar térmica. La temperatura de brillo aparente registrada asumiendo cuerpo negro es $T_{ap} = 850\\text{ K}$ ($576.85^\\circ\\text{C}$). Si la emisividad espectral real del recubrimiento cerámico a esa longitud de onda es $\\varepsilon_\\lambda = 0.88$, calcular la temperatura real verdadera de la superficie metálica: $\\frac{1}{T_{real}} = \\frac{1}{850} + \\frac{0.90}{14388}\\ln(0.88) = 0.0011765 + (6.255 \\times 10^{-5})(-0.1278) = 0.0011765 - 7.994 \\times 10^{-6} = 0.0011685\\text{ K}^{-1}$. Invirtiendo: $T_{real} = \\frac{1}{0.0011685} = 855.8\\text{ K} = 582.65^\\circ\\text{C}$ (un error de casi $6^\\circ\\text{C}$ si no se compensa la emisividad). Problema 2: En presencia de polvo atmosférico o ventanas ópticas parcialmente sucias, un pirómetro bicolor que mide en dos longitudes de onda cercanas ($\\lambda_1 = 0.95\\ \\mu\\text{m}, \\lambda_2 = 1.05\\ \\mu\\text{m}$) elimina por completo el error de emisividad y atenuación óptica, ya que las pérdidas cancelan en el cociente de señales.",
        "bloque_sugerido": "Metrología Térmica 40 min • Pirómetros de relación bicolor y calibración con cavidad de cuerpo negro",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES DE RADIACIÓN TÉRMICA",
                "titulo": "Aproximación de Wien para Altas Temperaturas",
                "puntos": [
                    "A temperaturas elevadas y longitudes de onda ópticas cortas ($c_2 / (\\lambda T) \\gg 1$), la ley de Planck se simplifica a la ley de Wien: $E_b(\\lambda, T) = \\frac{c_1}{\\lambda^5} e^{-c_2 / (\\lambda T)}$.",
                    "El pirómetro mide la radiancia espectral emitida por la superficie y resuelve para la temperatura.",
                    "La emisividad superficial $\\varepsilon_\\lambda < 1.0$ de cuerpos reales (cuerpos grises) hace que la temperatura de brillo aparente sea siempre inferior a la real."
                ]
            },
            {
                "numero": 2,
                "seccion": "PIRÓMETROS DE RELACIÓN (BICOLOR)",
                "titulo": "Inmunidad ante Atenuación de Señal",
                "puntos": [
                    "Mide simultáneamente la radiancia en dos bandas espectrales estrechas y adyacentes.",
                    "Si el medio entre el sensor y el blanco presenta humo, polvo, vapor o vidrio sucio, ambas longitudes de onda se atenúan en la misma proporción.",
                    "El cociente de intensidades es independiente de la atenuación del trayecto óptico y de la emisividad absoluta, garantizando mediciones estables en ambientes industriales agresivos."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Detección de Descargas Parciales (PD) en Aislamientos Eléctricos de Alta Tensión",
        "objetivo": "Modelar la actividad de descargas parciales internas y superficiales en cables XLPE, transformadores y celdas GIS mediante sensores de alta frecuencia (HFCT, TEV y UHF) según la norma IEC 60270.",
        "concepto_clave_latex": r"q_{aparente} = C_b \Delta V \quad [\text{pC}] \quad ; \quad \text{PRPD: Diagrama } \phi - q - n \quad ; \quad f_{UHF} \approx 300\text{ MHz} - 1.5\text{ GHz}",
        "ejemplo": "Problema 1: En una subestación blindada encapsulada en $SF_6$ (GIS) de 230 kV, un sensor de UHF interno detecta pulsos de microdescargas con carga aparente de $q = 85\\text{ pC}$ a la frecuencia de red de 60 Hz. El software de adquisición sincronizada con la fase de voltaje construye el diagrama PRPD (Phase-Resolved Partial Discharge, $\\phi-q-n$). Los pulsos se concentran exclusivamente en las crestas positivas ($90^\\circ$) y negativas ($270^\\circ$) del ciclo con amplitudes simétricas, patrón dactilar característico de una cavidad gaseosa oclusa ('void') dentro del aislador cónico de resina epóxica. Si la descarga superara los 100 pC de forma continua, el bombardeo de electrones y ozono degradaría el polímero hasta provocar una perforación por arborescencia eléctrica ('electrical treeing') y falla catastrófica de la barra. Se programa el cambio de la fase durante el mantenimiento de fin de semana. Problema 2: En transformadores de potencia inmersos en aceite, sensores de corriente de alta frecuencia (HFCT) colocados en el cable de aterrizamiento del neutro capturan transitorios de corriente de nanosegundos.",
        "bloque_sugerido": "Aislamiento Eléctrico 45 min • Clasificación de patrones PRPD y sensores TEV en celdas de media tensión",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DE LAS DESCARGAS PARCIALES",
                "titulo": "Ruptura Dieléctrica Localizada",
                "puntos": [
                    "Descarga eléctrica microscópica que puentea parcialmente el aislamiento entre dos conductores sin causar un cortocircuito franco inmediato.",
                    "Ocurre en vacuolas de gas, fisuras mecánicas, burbujas en aceite o partículas metálicas flotantes donde el campo eléctrico local supera la rigidez dieléctrica.",
                    "El síntoma premonitorio más fidedigno del colapso inminente de cables subterráneos y transformadores."
                ]
            },
            {
                "numero": 2,
                "seccion": "PATRONES PRPD Y SENSORES",
                "titulo": "Detección No Invasiva Online",
                "puntos": [
                    "Sensores TEV (Transient Earth Voltage): Capturan pulsos electromagnéticos inducidos en la superficie exterior metálica de los gabinetes.",
                    "Sensores UHF ($300\\text{ MHz} - 1.5\\text{ GHz}$): Excelente relación señal-ruido, inmunes al ruido electromagnético de radio AM ambiental.",
                    "Diagramas de Fase Resuelta (PRPD): Mapean el ángulo de fase de ocurrencia, magnitud de carga y conteo de pulsos para identificar el tipo exacto de defecto."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis de Respuesta en Frecuencia (FRA) e Impedancia Electroquímica (EIS)",
        "objetivo": "Evaluar la integridad mecánica de devanados de transformadores mediante barrido de frecuencia (SFRA según IEC 60076-18) y modelar el estado de salud (SOH) de baterías mediante Espectroscopía de Impedancia Electroquímica (EIS).",
        "concepto_clave_latex": r"Z_{FRA}(f) = 20 \log_{10}\left( \frac{V_{resp}(f)}{V_{in}(f)} \right) \quad [\text{dB}] \quad ; \quad Z_{EIS}(\omega) = R_s + \frac{R_{ct}}{1 + (j\omega R_{ct} C_{dl})^\alpha} + Z_W(\omega)",
        "ejemplo": "Problema 1: Un transformador de potencia de 60 MVA en una subestación soporta un cortocircuito cercano con corriente de falla de 22 kA. Tras el despeje de la falla, se realiza un ensayo de Barrido de Respuesta en Frecuencia (SFRA) inyectando una señal senoidal calibrada de 10 V desde 20 Hz hasta 2 MHz en el devanado de alta tensión. En el rango de medias frecuencias ($20\\text{ kHz} - 100\\text{ kHz}$, gobernado por las inductancias mutuas e inductancias de dispersión entre espiras), la curva de respuesta en decibelios presenta un desplazamiento de resonancia hacia la izquierda de $\\Delta f = 14\\text{ kHz}$ con una variación de amplitud de $8.5\\text{ dB}$ respecto a la huella original de fábrica (Fingerprint). Diagnóstico SFRA: Deformación plástica severa y desplazamiento axial de los discos centrales del devanado inducido por las colosales fuerzas electromagnéticas de Lorentz durante el cortocircuito. El transformador se retira de servicio antes de re-energizarlo, previniendo un cortocircuito interno devastador. Problema 2: En baterías BESS de litio, la EIS barriendo desde 10 mHz hasta 10 kHz grafica el diagrama de Nyquist ($-Z_{im}$ vs $Z_{re}$); el diámetro del semicírculo de media frecuencia cuantifica directamente la resistencia de transferencia de carga ($R_{ct}$), midiendo el envejecimiento y degradación de la batería con precisión microscópica.",
        "bloque_sugerido": "Diagnóstico de Activos 45 min • Diagramas de Bode SFRA y diagramas de Nyquist en baterías electroquímicas",
        "slides": [
            {
                "numero": 1,
                "seccion": "HUELLA ELECTROMECÁNICA (SFRA)",
                "titulo": "Radiografía en Frecuencia de Devanados",
                "puntos": [
                    "Un devanado de transformador es una red compleja distribuida de inductancias propias y mutuas, capacitancias entre espiras y resistencias parásitas.",
                    "Cada geometría física de devanado posee una respuesta en frecuencia ($20\\text{ Hz} - 2\\text{ MHz}$) única e irrepetible.",
                    "Cualquier movimiento mecánico milimétrico de conductores, inclinación de espiras o pérdida de sujeción altera drásticamente la curva SFRA."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESPECTROSCOPÍA DE IMPEDANCIA (EIS)",
                "titulo": "Modelado de Celdas Electroquímicas",
                "puntos": [
                    "Aplica una perturbación senoidal AC de pequeña amplitud ($~10\\text{ mV}$) a diferentes frecuencias superpuesta al voltaje DC.",
                    "Altas frecuencias ($> 1\\text{ kHz}$): Resistencia óhmica pura del electrolito y bornes ($R_s$).",
                    "Medias frecuencias ($1\\text{ Hz} - 1\\text{ kHz}$): Cinética de transferencia de carga y capacitancia de doble capa en los electrodos ($R_{ct}, C_{dl}$).",
                    "Bajas frecuencias ($< 1\\text{ Hz}$): Resistencia difusional de Warburg ($Z_W$) por transporte de iones litio en el estado sólido."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sensores de Fibra Óptica (FBG y DTS) para Monitoreo Térmico y Mecánico",
        "objetivo": "Diseñar sistemas de sensado distribuido por fibra óptica utilizando Redes de Bragg en Fibra (FBG) para deformación y dispersión Raman/Brillouin (DTS/BOTDA) para perfiles continuos de temperatura en líneas de transmisión y devanados.",
        "concepto_clave_latex": r"\lambda_B = 2 n_{eff} \Lambda \quad ; \quad \frac{\Delta \lambda_B}{\lambda_B} = (1 - p_e)\varepsilon + (\alpha_\Lambda + \xi)\Delta T \quad ; \quad \frac{I_{anti-Stokes}}{I_{Stokes}} \propto \exp\left(-\frac{h\nu}{k_B T}\right)",
        "ejemplo": "Problema 1: Un sensor de fibra óptica con Red de Bragg (FBG) tiene una longitud de onda de reflexión central de $\\lambda_B = 1550.00\\text{ nm}$ a $25^\\circ\\text{C}$ con sensibilidad mecánica de $S_\\varepsilon = 1.2\\text{ pm}/\\mu\\varepsilon$ y térmica de $S_T = 10.5\\text{ pm}/^\\circ\\text{C}$. Se instala sobre la raíz de una pala de aerogenerador eólico de 5 MW. Un interrogador óptico espectral con fotodiodo de avalancha detecta un corrimiento de la cresta reflejada a $\\lambda_{B}' = 1551.85\\text{ nm}$ ($\\Delta \\lambda_B = +1850\\text{ pm}$). Un FBG de referencia aislado de carga mecánica montado al lado mide un desplazamiento térmico puro de $+210\\text{ pm}$ (indicando un calentamiento de $\\Delta T = 210/10.5 = 20^\\circ\\text{C}$, temperatura ambiente $45^\\circ\\text{C}$). Desplazamiento por deformación pura: $\\Delta \\lambda_\\varepsilon = 1850 - 210 = 1640\\text{ pm}$. Deformación mecánica sufrida por la pala compuesta de fibra de carbono: $\\varepsilon = \\frac{1640\\text{ pm}}{1.2\\text{ pm}/\\mu\\varepsilon} = 1366.7\\ \\mu\\varepsilon$ ($~0.137\\%$ de alargamiento elástico bajo ráfaga de viento). Problema 2: En un cable subterráneo de 230 kV de 15 km de longitud, un sistema DTS (Distributed Temperature Sensing) analiza la dispersión inelástica Raman a lo largo de un hilo óptico integrado, entregando un perfil térmico cada metro ($15,000$ puntos de medición de temperatura) para operar la línea bajo Capacidad Térmica Dinámica (DLR).",
        "bloque_sugerido": "Fotónica Aplicada 45 min • Redes de Bragg y reflectometría óptica en el dominio del tiempo (OTDR)",
        "slides": [
            {
                "numero": 1,
                "seccion": "FIBRA ÓPTICA COMO SENSOR",
                "titulo": "Inmunidad Total al Ruido Electromagnético",
                "puntos": [
                    "Construidos en sílice dieléctrico puro; inmunes a campos electromagnéticos de alta tensión, rayos y radiofrecuencia.",
                    "Seguridad intrínseca ATEX: No transportan corriente eléctrica, eliminando riesgos de ignición en tanques de combustible o hidrógeno.",
                    "Transmisión de señales de medición a distancias de más de 40 kilómetros sin repetidores intermedios."
                ]
            },
            {
                "numero": 2,
                "seccion": "SENSADO PUNTUAL VS DISTRIBUIDO",
                "titulo": "FBG Multiplexado vs DTS Raman",
                "puntos": [
                    "FBG (Fiber Bragg Grating): Grabado láser de modulación de índice de refracción; decenas de sensores multiplexados en longitud de onda en una sola hebra fina.",
                    "DTS Raman: Utiliza toda la fibra continua como un sensor ininterrumpido midiendo el cociente anti-Stokes/Stokes sensible a la temperatura absoluta.",
                    "BOTDA Brillouin: Mide simultáneamente temperatura y deformación distribuida en tuberías forzadas de hidroeléctricas."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Redes Inalámbricas Industriales de Sensores (WSN): WirelessHART e ISA100.11a",
        "objetivo": "Diseñar redes malladas de sensores inalámbricos de ultra-bajo consumo energético según los estándares IEEE 802.15.4, WirelessHART e ISA100.11a con saltos de canal temporizados (TSCH).",
        "concepto_clave_latex": r"\text{Canales: } 16 \text{ en } 2.4\text{ GHz} \quad ; \quad \text{TimeSlot} = 10\text{ ms} \quad ; \quad \text{Fiabilidad de Entrega} \ge 99.9\%",
        "ejemplo": "Problema 1: En una planta de cogeneración de ciclo combinado se requiere instrumentar 80 transmisores de presión y temperatura en válvulas y tuberías distantes donde el tendido de cables blindados en bandejas costaría $120\\text{ USD por metro}$ ($>90000\\text{ USD}$ en cableado). Se instala una red mallada inalámbrica WirelessHART (estándar IEC 62591) que opera en la banda libre ISM de 2.4 GHz. La arquitectura TSCH divide el tiempo en ranuras (time-slots) de 10 ms; en cada ranura, los nodos transmiten en un canal de frecuencia pseudoaleatorio diferente (Channel Hopping entre 15 canales RF), evitando colisiones e interferencias con redes Wi-Fi de oficina. Si un obstáculo mecánico (como una grúa de mantenimiento) bloquea la línea de visión directa entre un sensor y la pasarela (gateway), el paquete de datos se enruta automáticamente a través de dos transmisores vecinos intermedios ('mesh routing'), logrando una fiabilidad de entrega confirmada del $99.95\\%$. Problema 2: Mediante algoritmos de gestión de energía y modo de reposo profundo ('deep sleep') durante el $99\\%$ del tiempo, las baterías internas de litio-cloruro de tionilo ($Li-SOCl_2$) garantizan una autonomía operativa de más de 8 años sin recambio.",
        "bloque_sugerido": "Redes Industriales 40 min • Protocolo TSCH y seguridad criptográfica AES-128 en WirelessHART",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL RETO DEL CABLEADO INDUSTRIAL",
                "titulo": "Redes Inalámbricas Malladas (Mesh)",
                "puntos": [
                    "El costo de instalar conduit de acero galvanizado a prueba de explosión, cables blindados y barreras intrínsecas supera frecuentemente el costo del propio sensor.",
                    "Las redes malladas se autoorganizan y autorreparan: Si un nodo se apaga o pierde señal, el grafo de la red reconfigura la ruta de transmisión en segundos.",
                    "Cada nodo actúa como sensor y como enrutador repetidor para los nodos vecinos."
                ]
            },
            {
                "numero": 2,
                "seccion": "DETERMINISMO Y COEXISTENCIA",
                "titulo": "Time-Slotted Channel Hopping (TSCH)",
                "puntos": [
                    "Sincronización temporal estricta con microsegundos de precisión en todas las ranuras de 10 ms.",
                    "El salto de canal continuo supera el desvanecimiento multicamino (fading) causado por reflexiones en estructuras de acero.",
                    "Cifrado de seguridad multicapa con claves AES-128 garantiza inmunidad contra accesos no autorizados e inyección de datos falsos."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Protocolo DNP3 y Ciberseguridad en Sistemas SCADA de Subestaciones",
        "objetivo": "Modelar las comunicaciones SCADA mediante el protocolo de red distribuido DNP3 (IEEE Std 1815) sobre enlaces serie RS-485 y TCP/IP, evaluando la seguridad mediante DNP3-SA (Secure Authentication v5).",
        "concepto_clave_latex": r"\text{Trama DNP3: } [0x05, 0x64, \text{Len}, \text{Ctrl}, \text{Dest}, \text{Src}, \text{CRC}] \quad ; \quad \text{HMAC-SHA256} \ [\text{Autenticación Segura}]",
        "ejemplo": "Problema 1: Un centro de control SCADA maestro de XM envía un comando de apertura de interruptor de potencia a una RTU remota en una subestación de 230 kV utilizando DNP3 sobre TCP/IP (puerto 20000). Sin mecanismos de seguridad, un ciberatacante en la red corporativa podría interceptar el tráfico e inyectar una trama maliciosa sin autenticación forzando el disparo indebido del interruptor (ataque Man-in-the-Middle). Con la implementación de DNP3 Secure Authentication (DNP3-SA v5 / IEC 62351-5), la RTU remota no ejecuta la orden inmediatamente; emite un mensaje de 'Challenge' conteniendo un número aleatorio no repetible (nonce). El maestro debe calcular un código de autenticación de mensajes basado en hash (HMAC-SHA256) combinando el nonce con una clave simétrica de actualización precompartida (Session Key) y devolverlo en un mensaje de 'Reply'. La RTU verifica criptográficamente el HMAC en menos de 10 milisegundos; solo si la firma es válida y el nonce coincide, el relé de salida cierra el contacto y acciona la bobina de disparo del interruptor. Problema 2: DNP3 admite reporte por excepción no solicitado (Unsolicited Responses) que reduce el tráfico de red en un $90\\%$ frente al sondeo cíclico continuo.",
        "bloque_sugerido": "Ciberseguridad OT 45 min • Análisis de tramas DNP3 con Wireshark y mitigación de ataques SCADA",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL PROTOCOLO DE SUBESTACIÓN DNP3",
                "titulo": "Diseño para Redes Eléctricas Críticas",
                "puntos": [
                    "Desarrollado específicamente para sistemas eléctricos; soporta marcas de tiempo precisas con resolución de 1 ms asignadas directamente por la RTU.",
                    "Almacenamiento de eventos en búfer local en caso de caída temporal del canal de comunicación WAN sin pérdida de datos históricos.",
                    "Reporte por Excepción: La RTU transmite únicamente cuando una variable analógica cambia más allá de su banda muerta o un estado digital conmuta."
                ]
            },
            {
                "numero": 2,
                "seccion": "CIBERSEGURIDAD EN ENTORNOS OT",
                "titulo": "DNP3-SA y Estándar NERC CIP",
                "puntos": [
                    "A diferencia de TLS que cifra todo el canal añadiendo sobrecarga de latencia, DNP3-SA autentica críticamente los mensajes de control sin ralentizar el tráfico de telemetría normal.",
                    "Protección estricta contra ataques de repetición (Replay Attacks) mediante rotación continua de números de desafío (challenges).",
                    "Cumplimiento obligatorio para infraestructuras críticas del sector eléctrico colombiano (Resolución CREG 500-001 de Ciberseguridad)."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Arquitectura IEC 61850: Mensajería GOOSE, Sampled Values (SV) y Subestación Digital",
        "objetivo": "Diseñar la arquitectura de comunicaciones de una subestación eléctrica digitalizada según la norma IEC 61850, reemplazando el cableado de cobre punto a punto por bus de estación y bus de proceso con tramas GOOSE y SV.",
        "concepto_clave_latex": r"t_{GOOSE} \le 3 - 4\text{ ms} \quad [\text{Capa 2 Ethernet / Prioridad 802.1Q}] \quad ; \quad \text{SV: } 4800\text{ samples/s} \ [80\text{ muestras/ciclo a } 60\text{ Hz}]",
        "ejemplo": "Problema 1: En una subestación digital de 500 kV, un relé de protección de distancia (IED) detecta una falla interna en una barra y debe ordenar el disparo coordinado de 4 interruptores asociados. En lugar de enviar una señal de 125 V DC por cables de cobre físicos a través del patio (tiempo de propagación y rebote de relés auxiliares $> 25\\text{ ms}$), el IED inyecta una trama digital GOOSE (Generic Object Oriented Substation Event) directamente a la red de fibra óptica Ethernet del bus de estación. El mensaje GOOSE se transmite directamente sobre la capa de enlace de datos OSI (Capa 2 / MAC multipunto sin sobrecarga de enrutamiento TCP/IP) con etiqueta de prioridad IEEE 802.1Q (VLAN ID con prioridad máxima de tráfico). La trama GOOSE llega a los IEDs receptores de los 4 interruptores en $t = 1.8\\text{ ms} < 3\\text{ ms}$, disparando los interruptores con una velocidad cuatro veces superior a la tecnología convencional y eliminando cientos de kilómetros de cables de cobre de control propensos a sobretensiones inducidas. Problema 2: En el bus de proceso, las Unidades de Mezcla (Merging Units) digitalizan las corrientes y tensiones de los transformadores ópticos transmitiendo tramas Sampled Values (SV según IEC 61869-9) sincronizadas por el protocolo PTP (IEEE 1588v2).",
        "bloque_sugerido": "Subestaciones Digitales 45 min • Configuración de archivos SCL (ICD/CID/SCD) y captura de tramas GOOSE",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE LA SUBESTACIÓN CABLEADA A LA FIBRA",
                "titulo": "La Revolución de la Subestación Digital",
                "puntos": [
                    "Sustituye mazos masivos de cables de cobre por fibra óptica óptica inmune a interferencias electromagnéticas.",
                    "Bus de Estación: Comunica IEDs de protección entre sí y con el SCADA local.",
                    "Bus de Proceso: Conecta las Unidades de Mezcla (Merging Units) ubicadas en el patio junto a los interruptores con los relés de la sala de control.",
                    "Reducción de hasta un 80% en los costos de zanjas civiles y cableado de control."
                ]
            },
            {
                "numero": 2,
                "seccion": "MECANISMOS DE MENSAJERÍA IEC 61850",
                "titulo": "GOOSE, SV y MMS",
                "puntos": [
                    "GOOSE: Transmisión ultra-rápida en Capa 2 para disparos de protección y bloqueos de seguridad ($< 3\\text{ ms}$); repetición periódica automática (Heartbeat) para supervisión de enlace.",
                    "Sampled Values (SV): Corrientes y tensiones instantáneas digitalizadas a alta frecuencia para protección diferencial de barras.",
                    "MMS (Manufacturing Message Specification): Comunicaciones Cliente-Servidor en Capa 7 para telemando y ajustes de configuración desde el SCADA."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Filtrado Digital de Señales: Filtros FIR, IIR y Filtro de Kalman en Instrumentación",
        "objetivo": "Diseñar algoritmos de filtrado digital de señales ruidosas de sensores energéticos, implementando filtros FIR de fase lineal, filtros recursivos IIR y el estimador estocástico óptimo de Kalman.",
        "concepto_clave_latex": r"y[n] = \sum_{k=0}^M b_k x[n-k] - \sum_{k=1}^N a_k y[n-k] \quad ; \quad \hat{\mathbf{x}}_{k} = \hat{\mathbf{x}}_k^- + \mathbf{K}_k(\mathbf{z}_k - \mathbf{H}\hat{\mathbf{x}}_k^-) \quad ; \quad \mathbf{K}_k = \mathbf{P}_k^- \mathbf{H}^T(\mathbf{H}\mathbf{P}_k^-\mathbf{H}^T + \mathbf{R})^{-1}",
        "ejemplo": "Problema 1: Un sensor piezoeléctrico mide las vibraciones del cojinete de una turbina hidráulica, pero la señal de salida está contaminada por ruido electromagnético de alta frecuencia generado por los inversores de potencia vecinos. Se diseña un filtro digital paso bajo FIR con ventana de Hamming con $M = 32$ coeficientes y frecuencia de corte de $f_c = 120\\text{ Hz}$ a una tasa de muestreo de $f_s = 2000\\text{ Hz}$. La respuesta al impulso simétrica $b_k = b_{M-k}$ garantiza fase estrictamente lineal, lo que significa que todas las componentes armónicas de la vibración se retrasan exactamente por el mismo retardo temporal $(\\tau = M / (2 f_s) = 8\\text{ ms}$), preservando sin ninguna distorsión la forma de onda de los picos de vibración transitorios. Problema 2: En la estimación del Estado de Carga (SOC) de una batería de litio BESS donde las mediciones de corriente tienen ruido gaussiano y el voltaje terminal varía con la histéresis, el Filtro de Kalman Extendido (EKF) fusiona en tiempo real el modelo dinámico electroquímico con las mediciones, reduciendo la incertidumbre de estimación de SOC del $\\pm 8\\%$ a menos del $\\pm 1.2\\%$.",
        "bloque_sugerido": "Procesamiento Digital de Señales 45 min • Implementación de filtro de Kalman para estimación de SOC en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "FILTROS FIR vs IIR",
                "titulo": "Fase Lineal vs Eficiencia Computacional",
                "puntos": [
                    "Filtros FIR (Respuesta al Impulso Finita): Incondicionalmente estables sin retroalimentación; fase perfectamente lineal (cero distorsión de fase); requieren mayor número de coeficientes.",
                    "Filtros IIR (Respuesta al Impulso Infinita): Arquitectura recursiva que requiere pocos coeficientes; emulan filtros analógicos clásicos (Butterworth, Chebyshev); fase no lineal.",
                    "Transformada Bilineal con prewarping de frecuencia para mapeo analógico-digital en el plano Z."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL FILTRO ÓPTIMO DE KALMAN",
                "titulo": "Fusión Sensorial Estocástica",
                "puntos": [
                    "Algoritmo recursivo en dos etapas: Predicción (a partir del modelo matemático físico) y Corrección (ponderando la nueva medición del sensor).",
                    "Ganancia de Kalman $\\mathbf{K}_k$: Pondera dinámicamente si confiar más en el modelo o en el sensor en función de las matrices de covarianza de ruido $\\mathbf{Q}$ y $\\mathbf{R}$.",
                    "Indispensable para filtrado de telemetría ruidosa en tiempo real en centros de despacho de energía."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Metrología Legal, Trazabilidad y Calibración según ISO/IEC 17025",
        "objetivo": "Formular los requisitos técnicos de competencia metrológica según la norma ISO/IEC 17025 para laboratorios de ensayo y calibración de instrumentos energéticos, construyendo la cadena ininterrumpida de trazabilidad hacia los patrones primarios del SI.",
        "concepto_clave_latex": r"U = k \cdot u_c \quad [k=2 \implies 95.45\% \text{ Confianza}] \quad ; \quad u_c = \sqrt{\sum \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)} \quad ; \quad E_n = \frac{x_{lab} - X_{ref}}{\sqrt{U_{lab}^2 + U_{ref}^2}} \le 1.0",
        "ejemplo": "Problema 1: El laboratorio de calibración de medidores de energía eléctrica de la Universidad del Magdalena calibra un medidor estático trifásico de energía activa de precisión clase 0.2S contra un patrón patrón de trabajo de alta precisión ($X_{ref} = 1000.00\\text{ kWh}$, $U_{ref} = 0.20\\text{ kWh}$). El medidor bajo calibración registra $x_{lab} = 1000.35\\text{ kWh}$ con incertidumbre expandida calculada de $U_{lab} = 0.45\\text{ kWh}$. Calcular el error normalizado de intercalibración $E_n$: $E_n = \\frac{1000.35 - 1000.00}{\\sqrt{(0.45)^2 + (0.20)^2}} = \\frac{0.35}{\\sqrt{0.2025 + 0.0400}} = \\frac{0.35}{\\sqrt{0.2425}} = \\frac{0.35}{0.4924} = 0.711$. Como $|E_n| = 0.711 \\le 1.0$, el resultado de calibración es formalmente satisfactorio y metrológicamente conforme según ISO/IEC 17025. Problema 2: En el presupuesto de incertidumbre tipo B del sensor de presión, se incluyen las incertidumbres de resolución del display digital (distribución rectangular $u = a/\\sqrt{3}$) y la deriva térmica por temperatura ambiente.",
        "bloque_sugerido": "Acreditación Metrológica 40 min • Presupuesto de incertidumbre GUM y ensayos de aptitud interlaboratorios",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA CADENA DE TRAZABILIDAD",
                "titulo": "Conexión Ininterrumpida con el SI",
                "puntos": [
                    "Patrones Internacionales (BIPM en Sèvres, Francia): Realización cuántica de las unidades base del SI (segundo atómico de cesio, voltio Josephson, ohmio Hall cuántico).",
                    "Institutos Nacionales de Metrología (INM en Colombia): Custodia de los patrones nacionales primarios.",
                    "Laboratorios Acreditados ONAC: Calibran los instrumentos de trabajo de las empresas eléctricas asegurando trazabilidad jurídica y técnica."
                ]
            },
            {
                "numero": 2,
                "seccion": "EVALUACIÓN DE LA INCERTIDUMBRE (GUM)",
                "titulo": "Tipo A vs Tipo B",
                "puntos": [
                    "Incertidumbre Tipo A: Evaluada por métodos estadísticos a partir de series de mediciones repetidas (desviación estándar de la media $s/\\sqrt{n}$).",
                    "Incertidumbre Tipo B: Evaluada por juicios científicos basados en certificados de calibración previos, especificaciones de fabricante y tolerancias.",
                    "Incertidumbre combinada $u_c$ expandida con factor de cobertura $k=2$ para el 95% de nivel de confianza."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Seguridad Funcional y Niveles de Integridad SIL según IEC 61508 / IEC 61511",
        "objetivo": "Diseñar Sistemas Instrumentados de Seguridad (SIS) para protección de plantas térmicas y refinerías de biometano, calculando la Probabilidad Media de Falla en Demanda (PFDavg) y asignando niveles SIL (1 al 4).",
        "concepto_clave_latex": r"\text{PFD}_{avg} \approx \lambda_{DU} \left( \frac{TI}{2} \right) \quad ; \quad \text{SIL 1: } 10^{-2} \le \text{PFD} < 10^{-1} \quad ; \quad \text{SIL 2: } 10^{-3} \le \text{PFD} < 10^{-2} \quad ; \quad \text{SIL 3: } 10^{-4} \le \text{PFD} < 10^{-3}",
        "ejemplo": "Problema 1: En una caldera de gasificación de biomasa, la explosión por sobrepresión catastrófica del domo de vapor se protege mediante una Función Instrumentada de Seguridad (SIF) que corta el combustible si la presión supera 45 bar. La tasa de fallas peligrosas no detectadas del transmisor de presión es $\\lambda_{DU} = 1.8 \\times 10^{-6}\\text{ fallas/hora}$ y el intervalo de prueba periódica de parada completa ('Proof Test Interval') es de 1 año ($TI = 8760\\text{ horas}$). Para una arquitectura simple 1oo1 (1 de 1): $\\text{PFD}_{avg} = \\lambda_{DU} \\frac{TI}{2} = (1.8 \\times 10^{-6}) \\frac{8760}{2} = 7.884 \\times 10^{-3}$. Como $10^{-3} \\le 7.884 \\times 10^{-3} < 10^{-2}$, el sensor solo alcanza nivel SIL 1. Sin embargo, el análisis de riesgos HazOp exige nivel SIL 3 para salvar vidas humanas. Solución: Se implementa una arquitectura redundante con votación 2oo3 (2 de 3) con tres transmisores de presión independientes de fabricantes disímiles. Con arquitectura 2oo3: $\\text{PFD}_{avg} \\approx (\\lambda_{DU} TI)^2 = (1.8 \\times 10^{-6} \\times 8760)^2 = (0.015768)^2 = 2.486 \\times 10^{-4}$, alcanzando exitosamente el nivel de seguridad requerido SIL 3 sin disparos en falso de la planta. Problema 2: En la matriz de capas de protección independiente (LOPA), el SIS representa la última barrera activa antes del alivio pasivo por disco de ruptura mecánico.",
        "bloque_sugerido": "Seguridad de Procesos 45 min • Metodología LOPA y cálculo de PFDavg en software exSILentia",
        "slides": [
            {
                "numero": 1,
                "seccion": "CAPAS DE PROTECCIÓN INDEPENDIENTE (LOPA)",
                "titulo": "La Cebolla de Seguridad",
                "puntos": [
                    "Capa 1: Diseño mecánico inherente del proceso y contención física.",
                    "Capa 2: Sistema Básico de Control de Procesos (BPCS / DCS industrial).",
                    "Capa 3: Alarmas críticas con intervención del operador humano.",
                    "Capa 4: Sistema Instrumentado de Seguridad (SIS / ESD con certificación SIL).",
                    "Capa 5: Alivio mecánico pasivo (válvulas de seguridad de resorte y discos de ruptura)."
                ]
            },
            {
                "numero": 2,
                "seccion": "ARQUITECTURAS DE VOTACIÓN REDUNDANTE",
                "titulo": "1oo1 vs 1oo2 vs 2oo3",
                "puntos": [
                    "1oo1 (One out of One): Barato pero vulnerable a fallas únicas no detectadas.",
                    "1oo2 (One out of Two): Máxima seguridad; si cualquiera de los dos sensores detecta peligro, dispara la planta; desventaja: incrementa los disparos en falso que paralizan la producción.",
                    "2oo3 (Two out of Three): Combina máxima seguridad y máxima disponibilidad industrial; se requiere que al menos 2 de los 3 sensores confirmen la anomalía para ordenar el disparo."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Transmisores Inteligentes: Protocolos HART, Fieldbus Foundation y Profibus-PA",
        "objetivo": "Modelar la superposición de señales digitales de instrumentación sobre bucles analógicos de corriente de 4-20 mA mediante modulación FSK (HART) y arquitecturas puramente digitales de bus de campo.",
        "concepto_clave_latex": r"I_{bucle} = 4 - 20\text{ mA DC} \quad ; \quad \text{HART FSK: } 1200\text{ Hz (Bit 1)} \quad / \quad 2200\text{ Hz (Bit 0)} \quad [\pm 0.5\text{ mA AC}]",
        "ejemplo": "Problema 1: Un transmisor de presión diferencial inteligente instalado en una placa de orificio para medición de vapor industrial mide un rango calibrado (span) de $0$ a $250\\text{ kPa}$ entregando la variable primaria en corriente analógica continua de $4\\text{ a } 20\\text{ mA}$. A una presión medida de $175\\text{ kPa}$, calcular la corriente analógica en el bucle: Fracción de escala: $\\frac{175}{250} = 0.70$ ($70\\%$). Corriente: $I = 4.0 + 0.70(20.0 - 4.0) = 4.0 + 0.70(16.0) = 4.0 + 11.2 = 15.20\\text{ mA DC}$. Simultáneamente, sobre este valor continuo de 15.20 mA se modulan señales senoidales de corriente alterna de $\\pm 0.5\\text{ mA}$ según la norma Bell 202: ondas de $1200\\text{ Hz}$ para '1' lógico y $2200\\text{ Hz}$ para '0' lógico. Dado que el valor medio de la onda sinusoidal simétrica es exactamente cero, el receptor analógico del PLC ni siquiera nota la presencia de la señal digital, mientras que un comunicador de mano o sistema de gestión de activos (AMS) lee digitalmente la temperatura interna del sensor, diagnóstico de membrana de aislamiento dañada y horas de operación acumuladas. Problema 2: En Fieldbus Foundation y Profibus-PA, el cable bifilar alimenta los sensores en media tensión y transmite datos bidireccionales digitales continuos a $31.25\\text{ kbit/s}$ (estándar Manchester bus powered).",
        "bloque_sugerido": "Comunicaciones de Campo 45 min • Simulación de modulación FSK Bell 202 y configuración de descriptores DDL",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL BUCLE DE CORRIENTE 4-20 mA",
                "titulo": "La Ventaja del 'Live Zero'",
                "puntos": [
                    "Corriente de 4 mA para el cero de escala ('live zero'): Permite detectar instantáneamente si un cable está roto o cortado (corriente colapsa a 0 mA exactos).",
                    "Inmune a caídas de tensión ohmicas por longitud de cable (la fuente de corriente constante ajusta el voltaje para mantener los miliamperios exactos).",
                    "Los 4 mA basales alimentan energéticamente los circuitos del propio transmisor sin requerir cables de alimentación adicionales (transmisores a dos hilos)."
                ]
            },
            {
                "numero": 2,
                "seccion": "HART DIGITAL SOBRE ANALÓGICO",
                "titulo": "Diagnóstico y Mantenimiento Remoto",
                "puntos": [
                    "Permite reconfigurar el rango de calibración (re-ranging) de un sensor de campo desde la sala de control sin desmontar el instrumento.",
                    "Transmite múltiples variables secundarias en el mismo par de cobre (presión estática, temperatura de cápsula y voltaje de excitación).",
                    "Habilita el mantenimiento predictivo alertando sobre bloqueos de líneas de impulsión antes de que el proceso se desestabilice."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Medición Inteligente de Energía (AMI) y Protocolo DLMS/COSEM",
        "objetivo": "Modelar la infraestructura avanzada de medición de energía eléctrica (AMI), analizando la comunicación entre medidores inteligentes (Smart Meters), concentradores de datos por PLC/celular y el sistema central MDMS mediante el protocolo internacional DLMS/COSEM (IEC 62056).",
        "concepto_clave_latex": r"\text{OBIS Code: } A-B:C.D.E*F \quad [\text{ej: } 1-0:1.8.0*255 \implies \text{Energía Activa Importada Total}] \quad ; \quad \text{PLC G3 / PRIME}",
        "ejemplo": "Problema 1: Una empresa distribuidora de energía en Santa Marta implementa una red de 50,000 medidores inteligentes AMI según el reglamento CREG 131 de modernización de redes de distribución. Cada medidor estático ejecuta el modelo de objetos COSEM (Companion Specification for Energy Metering) bajo la norma IEC 62056. El sistema de gestión de datos de medida (MDMS) interroga el medidor leyendo el código de identificación de objeto OBIS `1-0:1.8.0*255` para obtener la energía activa importada acumulada, `1-0:2.8.0*255` para la energía solar exportada por autogeneradores, y `1-0:32.7.0*255` para la tensión instantánea de fase RMS. Los datos se transmiten por comunicación por línea de potencia (PLC PRIME en baja tensión) hacia un concentrador en el transformador de distribución, y de allí por enlace celular 4G LTE/NB-IoT al centro de facturación. Si un usuario intenta puentear el medidor abriendo la tapa de bornes, un microrruptor 'tamper' registra el evento con marca temporal certificada en el objeto de registro de eventos y desconecta internamente el contactor de potencia en menos de 50 ms. Problema 2: El sistema AMI permite implementar tarifas horarias multi-bloque en tiempo real (Time-of-Use, TOU) dinamizando la respuesta a la demanda de los consumidores.",
        "bloque_sugerido": "Smart Grids 45 min • Decodificación de tramas DLMS/COSEM y arquitectura MDMS/HES",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE LA LECTURA MANUAL AL SMART METERING",
                "titulo": "Infraestructura Avanzada de Medición (AMI)",
                "puntos": [
                    "Elimina la lectura visual manual mensual puerta a puerta y los cortes físicos de energía con cuadrilla de técnicos.",
                    "Lectura remota bidireccional continua cada 15 o 60 minutos con curvas de carga horarias detalladas.",
                    "Contactor interno biestable que permite reconectar o suspender el servicio telemáticamente desde la central."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTRUCTURA DE DATOS DLMS/COSEM",
                "titulo": "Interoperabilidad Universal Multimarca",
                "puntos": [
                    "COSEM: Modela todos los atributos del medidor mediante clases de objetos orientados a objetos normalizados.",
                    "OBIS (Object Identification System): Identificador único universal de 6 dígitos alfanuméricos para cada magnitud eléctrica.",
                    "Cifrado de extremo a extremo con suite criptográfica AES-128-GCM para proteger los datos de consumo y privacidad de los usuarios contra ciberataques."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Instrumentación Virtual, Automatización de Ensayos y Protocolos SCPI en Python/LabVIEW",
        "objetivo": "Diseñar bancos automatizados de caracterización energética conectando multímetros de precisión, fuentes DC regenerativas y osciloscopios a través de buses GPIB/Ethernet empleando comandos estándar SCPI y librerías PyVISA.",
        "concepto_clave_latex": r"\text{SCPI: } \text{':MEAS:VOLT:DC? 10,0.001'} \quad ; \quad \text{PyVISA: } \text{rm.open\_resource('TCPIP0::192.168.1.100::inst0::INSTR')}",
        "ejemplo": "Problema 1: En el laboratorio de energías renovables de la Universidad del Magdalena se automatiza la caracterización de una celda de combustible PEM de 1 kW mediante un script de control en Python utilizando la librería PyVISA. El computador maestro se conecta por red Gigabit Ethernet a una carga electrónica regenerativa y a un registrador de temperaturas termocupla multicanal. El script ejecuta un lazo automatizado de barrido de polarización: 1) Envía el comando SCPI `:SOUR:CURR:LEV 5.0` fijando la corriente de carga en 5.0 A. 2) Espera 10 segundos a que la temperatura y el flujo de hidrógeno se estabilicen en estado estacionario. 3) Consulta el voltaje terminal enviando la cadena `:MEAS:VOLT:DC?`, leyendo la respuesta con precisión de 6 dígitos y medio ($V = 0.742351\\text{ V}$). 4) Lee simultáneamente los 8 canales de temperatura con `:MEAS:TEMP:TC? TYPE_K`. 5) Incrementa la corriente en pasos de 1.0 A hasta alcanzar la corriente límite de 35 A, graficando en vivo la curva de polarización y potencia con Matplotlib y exportando el dataset certificado a un archivo HDF5 en 8 minutos. Problema 2: Automatizar el banco de pruebas elimina el error humano en la toma manual de datos, reduce los tiempos de ensayo en un $95\\%$ y garantiza la repetibilidad experimental según normas internacionales.",
        "bloque_sugerido": "Automatización de Laboratorios 45 min • Scripting en Python con PyVISA y desarrollo de VIs en LabVIEW",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL CONCEPTO DE INSTRUMENTACIÓN VIRTUAL",
                "titulo": "El Software es el Instrumento",
                "puntos": [
                    "Sustituye costosos paneles de control físicos con perillas y agujas por interfaces gráficas de usuario interactivas en computadora.",
                    "Combina hardware de adquisición modular industrial (PXI, cRIO, USB-DAQ) con software avanzado de procesamiento digital y visualización.",
                    "Permite modificar la funcionalidad completa del banco de pruebas cambiando únicamente unas líneas de código sin alterar el hardware físico."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTÁNDARES VISA Y COMANDOS SCPI",
                "titulo": "Comandos Estándar para Instrumentos Programables",
                "puntos": [
                    "SCPI (Standard Commands for Programmable Instruments): Sintaxis jerárquica ASCII en árbol estandarizada universal para todos los fabricantes de instrumentos (Keysight, Tektronix, Rohde & Schwarz).",
                    "VISA (Virtual Instrument Software Architecture): Capa middleware que unifica las comunicaciones independientemente del bus físico (USB, Ethernet, GPIB o RS-232).",
                    "Acelerador indispensable para bancos de prueba de prototipos en proyectos de ingeniería energética CDIO."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06011838)
    # Inject before the next subject marker: 04021825
    inject_topics_after('      - codigo: "04021825"', yaml_text)
    print("06011838 Mediciones e Instrumentación successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
