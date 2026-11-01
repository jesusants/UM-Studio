# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06021845 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Golpe de Ariete y Transitorios Hidráulicos en Tuberías Forzadas",
        "objetivo": "Modelar la sobrepresión transitoria generada por el cierre rápido o lento de válvulas en conducciones a presión mediante las fórmulas de Joukowsky y el método de las características.",
        "concepto_clave_latex": r"c = \sqrt{\frac{K/\rho}{1 + (K/E)(D/e)}} \quad ; \quad \Delta P_{max} = \rho c \Delta v \quad ; \quad T_c = \frac{2L}{c}",
        "ejemplo": "Problema 1: Una tubería forzada de acero ($E = 210\\text{ GPa}$, diámetro interior $D = 1.2\\text{ m}$, espesor de pared $e = 15\\text{ mm}$) transporta agua ($K = 2.2\\text{ GPa}$, $\\rho = 1000\\text{ kg/m}^3$) a una velocidad de $v_0 = 3.5\\text{ m/s}$ a lo largo de $L = 900\\text{ m}$. Calcular la celeridad de la onda de presión $c$, el tiempo crítico de cierre $T_c$ y la sobrepresión máxima de Joukowsky para un cierre rápido: Término de elasticidad: $\\frac{K}{E}\\frac{D}{e} = \\frac{2.2 \\times 10^9}{210 \\times 10^9} \\frac{1.2}{0.015} = 0.010476 \\times 80 = 0.8381$. Celeridad de onda: $c = \\sqrt{\\frac{2.2 \\times 10^9 / 1000}{1 + 0.8381}} = \\sqrt{\\frac{2.2 \\times 10^6}{1.8381}} = \\sqrt{1196888} \\approx 1094\\text{ m/s}$. Tiempo crítico de reflexión: $T_c = \\frac{2 \\times 900}{1094} = 1.645\\text{ s}$. Sobrepresión máxima: $\\Delta P = 1000 \\times 1094 \\times 3.5 = 3.829 \\times 10^6\\text{ Pa} = 3.829\\text{ MPa}$ ($~390.4\\text{ m.c.a.}$). Si el salto estático es 200 m, la tubería debe resistir casi 600 m.c.a. Problema 2: Si el tiempo de cierre de la válvula gobernadora se extiende a $T_{cierre} = 10.0\\text{ s} > T_c$ (cierre lento), la sobrepresión se mitiga según la fórmula de Michaud a $\\Delta h = \\frac{2 L v_0}{g T_{cierre}} = \\frac{2(900)(3.5)}{9.81 \\times 10} = 64.22\\text{ m.c.a.}$, evitando la rotura catastrófica de la tubería.",
        "bloque_sugerido": "Dinámica Transitoria 45 min • Ecuaciones de Joukowsky y método de diferencias finitas en tuberías",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DEL GOLPE DE ARIETE",
                "titulo": "Transformación de Energía Cinética en Elástica",
                "puntos": [
                    "Al frenar bruscamente la columna de agua, la energía cinética $\\frac{1}{2}m v^2$ se comprime en energía de deformación elástica del fluido y dilatación de la pared de acero.",
                    "La onda de sobrepresión viaja hacia el embalse a la velocidad del sonido en el conducto elástico ($c \\approx 900 - 1200\\text{ m/s}$).",
                    "Cierre Rápido ($T_v \\le 2L/c$): La onda reflejada de descompresión no llega a tiempo para aliviar la válvula; se alcanza la máxima sobrepresión de Joukowsky."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISPOSITIVOS DE PROTECCIÓN",
                "titulo": "Mitigación del Golpe de Ariete",
                "puntos": [
                    "Chimeneas de equilibrio (almenaras): Proporcionan una superficie libre que refleja la onda de presión cerca de la casa de máquinas.",
                    "Válvulas de alivio sincrónico: Derivan caudal automáticamente al canal de desagüe durante el rechazo repentino de carga eléctrica.",
                    "Calderines hidroneumáticos de aire comprimido (recipientes antiariete) en estaciones de bombeo."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Chimeneas de Equilibrio (Surge Tanks) y Criterio de Estabilidad de Thoma",
        "objetivo": "Dimensionar chimeneas de equilibrio cilíndricas y con estrangulamiento, determinando la sección mínima transversal de Thoma $A_{Th}$ para prevenir oscilaciones inestables acopladas con el regulador.",
        "concepto_clave_latex": r"A_{Th} = \frac{L A_t}{2 g c_v H_0} \quad ; \quad A_{real} = n_{seg} A_{Th} \ [n_{seg} \ge 1.5 - 1.8] \quad ; \quad Z_{max} = v_0 \sqrt{\frac{L A_t}{g A_{ch}}}",
        "ejemplo": "Problema 1: Un túnel de aducción a presión tiene longitud $L = 3000\\text{ m}$, diámetro interior $D_t = 3.0\\text{ m}$ (área $A_t = 7.069\\text{ m}^2$), coeficiente de pérdidas de fricción $c_v = 0.05\\text{ s}^2/\\text{m}$, salto neto nominal $H_0 = 180\\text{ m}$ y velocidad de flujo $v_0 = 2.5\\text{ m/s}$. Calcular el área transversal mínima de Thoma para la chimenea de equilibrio cilíndrica: $A_{Th} = \\frac{L A_t}{2 g c_v H_0} = \\frac{3000 \\times 7.069}{2 \\times 9.81 \\times 0.05 \\times 180} = \\frac{21207}{176.58} = 120.1\\text{ m}^2$. Diámetro mínimo de Thoma: $D_{Th} = \\sqrt{\\frac{4 \\times 120.1}{\\pi}} = 12.36\\text{ m}$. Aplicando un factor de seguridad de Thoma de $n = 1.6$, el área de diseño es $A_{ch} = 1.6 \\times 120.1 = 192.16\\text{ m}^2$ ($D_{ch} = 15.64\\text{ m}$). Problema 2: En un cierre total instantáneo, la máxima sobrelevación de masa de agua en la chimenea es $Z_{max} = v_0 \\sqrt{\\frac{L A_t}{g A_{ch}}} = 2.5 \\sqrt{\\frac{3000 \\times 7.069}{9.81 \\times 192.16}} = 2.5 \\sqrt{\\frac{21207}{1885.1}} = 2.5 \\sqrt{11.25} = 2.5 \\times 3.354 = 8.39\\text{ m}$, determinando la cota de coronación superior para evitar desbordamientos.",
        "bloque_sugerido": "Obras Hidráulicas 45 min • Ecuaciones diferenciales de oscilación de masa y amortiguamiento",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA DE OSCILACIÓN DE MASA",
                "titulo": "Desacoplamiento Túnel-Tubería",
                "puntos": [
                    "La chimenea divide el sistema en dos tramos: el largo túnel de aducción de baja presión y la corta tubería forzada de alta presión.",
                    "Sustituye el rápido fenómeno elástico del golpe de ariete por una oscilación hidrostática lenta de masa de agua entre el embalse y la chimenea.",
                    "El periodo de oscilación libre es de varios minutos: $T = 2\\pi\\sqrt{\\frac{L A_{ch}}{g A_t}}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTABILIDAD DE THOMA",
                "titulo": "Interacción con Turbinas a Potencia Constante",
                "puntos": [
                    "Cuando el nivel en la chimenea desciende, la altura neta cae; para mantener la potencia eléctrica constante ($P = \\eta \\rho g Q H$), el regulador abre más álabes, aumentando el caudal y reduciendo aún más el nivel.",
                    "Si el área de la chimenea es menor que el límite de Thoma ($A < A_{Th}$), este lazo de retroalimentación se vuelve inestable, generando oscilaciones divergentes que vacían la chimenea.",
                    "Chimeneas con orificio restringido introducen pérdidas de carga localizadas que amortiguan la oscilación en un tercio del tiempo."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Válvulas Hidráulicas de Guardia y Regulación: Esféricas, Mariposa y Aguja",
        "objetivo": "Seleccionar y dimensionar válvulas de cierre de emergencia y órganos de estrangulamiento según el salto neto y caudal, calculando coeficientes de flujo $K_v$ y cavitación.",
        "concepto_clave_latex": r"Q = K_v \sqrt{\frac{\Delta P}{\rho / \rho_0}} \quad ; \quad \sigma_v = \frac{P_{down} - P_v}{\Delta P} > \sigma_{crit} \quad ; \quad F_{act} = \Delta P \cdot A_{disco}",
        "ejemplo": "Problema 1: Una central hidroeléctrica con salto neto de 450 m ($P \\approx 4.41\\text{ MPa}$) y caudal nominal de $12\\text{ m}^3/\\text{s}$ requiere una válvula de guardia a la entrada de una turbina Pelton. A presiones tan elevadas, una válvula de mariposa induciría deformaciones inaceptables en el disco y pérdidas de carga continuas en el flujo. Se selecciona una Válvula Esférica de paso total (Ball Valve) de 1.4 m de diámetro con sello metálico móvil accionado por presión de agua de la propia tubería. En posición totalmente abierta, la válvula esférica deja un conducto cilíndrico liso y libre de obstrucciones, con un coeficiente de pérdida de carga prácticamente nulo ($K_L \\approx 0.02$, $\\Delta h_f < 0.1\\text{ m}$). Problema 2: En descargas de fondo de presas donde se debe disipar energía destruyendo hasta 100 metros de carga hacia el río, se utilizan Válvulas de Chorro Hueco (Howell-Bunger) o Válvulas de Aguja, que pulverizan el chorro en un cono divergente aireado para evitar la erosión destructiva del cauce.",
        "bloque_sugerido": "Equipos Hidráulicos 40 min • Curvas características de válvulas esféricas y servomotores de contrapeso",
        "slides": [
            {
                "numero": 1,
                "seccion": "TIPOLOGÍAS DE VÁLVULAS",
                "titulo": "Mariposa, Esférica y Aguja",
                "puntos": [
                    "Válvulas de Mariposa: Económicas y compactas; ideales para saltos bajos y medios ($H < 200\\text{ m}$) en turbinas Francis y Kaplan.",
                    "Válvulas Esféricas: Paso recto total al 100%, estanqueidad absoluta con doble sello de mantenimiento; estándar para saltos altos ($H > 200\\text{ m}$).",
                    "Válvulas de Aguja: Diseñadas específicamente para estrangulamiento y regulación continua de caudal sin riesgo de cavitación destructiva."
                ]
            },
            {
                "numero": 2,
                "seccion": "SISTEMAS DE ACCIONAMIENTO SEGURO",
                "titulo": "Cierre por Gravedad Fail-Safe",
                "puntos": [
                    "Las válvulas de guardia deben ser capaces de cerrar contra caudal máximo incluso durante un apagón eléctrico total de la planta.",
                    "Se abren mediante servomotores oleohidráulicos de alta presión ($100 - 160\\text{ bar}$) levantando un contrapeso de acero masivo.",
                    "En emergencia, se despresuriza el aceite y la gravedad deja caer el contrapeso, forzando el cierre mecánico seguro de la válvula."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Regulación de Velocidad y Frecuencia: Reguladores Hidroeléctricos PID y Estatismo",
        "objetivo": "Modelar la respuesta dinámica del regulador de turbina acoplado a la columna de agua (tiempo de arranque de agua $T_w$) y el grupo generador, calculando el estatismo permanente $R$ y parámetros PID.",
        "concepto_clave_latex": r"R = -\frac{\Delta f / f_0}{\Delta P / P_0} \times 100\% \quad ; \quad T_w = \frac{L v_0}{g H_0} \quad ; \quad G_{agua}(s) = \frac{1 - T_w s}{1 + 0.5 T_w s}",
        "ejemplo": "Problema 1: Un generador hidroeléctrico de 100 MW a 60 Hz opera con un estatismo permanente del $R = 4\\%$. Si la frecuencia del sistema interconectado cae en 0.15 Hz debido al disparo de otra central, calcular el incremento automático de potencia generado por regulación primaria: Variación relativa de frecuencia: $\\frac{\\Delta f}{f_0} = \\frac{-0.15}{60.0} = -0.0025$ ($-0.25\\%$). Despejando la potencia: $\\frac{\\Delta P}{P_0} = -\\frac{\\Delta f / f_0}{R} = -\\frac{-0.0025}{0.04} = +0.0625$ ($+6.25\\%$). Aumento de generación: $\\Delta P = 0.0625 \\times 100\\text{ MW} = +6.25\\text{ MW}$. Problema 2: Explicar por qué la función de transferencia hidráulica $G_{agua}(s)$ tiene un cero en el semiplano derecho ($s = +1/T_w$). Al abrir rápidamente los álabes directrices para aumentar potencia, la inercia del agua en la tubería forzada no acelera de inmediato; la presión cae transitoriamente antes de que el caudal aumente, produciendo una reducción inicial transitoria de potencia mecánica (efecto de fase no mínima).",
        "bloque_sugerido": "Control de Potencia 45 min • Sintonización de reguladores PID en turbinas hidráulicas",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA DE LA COLUMNA DE AGUA",
                "titulo": "Tiempo de Inercia Hídrica (Tw)",
                "puntos": [
                    "El tiempo de arranque de agua $T_w = \\frac{\\sum L_i v_i}{g H_0}$ representa el tiempo necesario para acelerar la columna de reposo a velocidad nominal bajo el salto $H_0$.",
                    "Comportamiento de Fase No Mínima: Una orden de apertura de compuertas reduce la potencia mecánica durante los primeros instantes.",
                    "Impone límites estrictos a la ganancia proporcional del regulador PID para evitar inestabilidad en bucle cerrado."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGULACIÓN PRIMARIA Y ESTATISMO",
                "titulo": "Compartición de Carga entre Generadores",
                "puntos": [
                    "El estatismo permanente $R$ (típicamente $3\\% - 6\\%$) asegura que múltiples generadores en paralelo compartan automáticamente las variaciones de demanda en proporción a su capacidad nominal.",
                    "Estatismo transitorio ($R_t$ y $T_r$): Incrementa temporalmente el estatismo durante maniobras rápidas para amortiguar las oscilaciones de potencia.",
                    "La regulación secundaria (AGC) actúa en minutos restableciendo la frecuencia nominal exacta a 60.00 Hz."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Hidráulica Fluvial y Sedimentación en Embalses: Criterio de Shields y Flushing",
        "objetivo": "Evaluar la colmatación de embalses por transporte de fondo y suspensión, calculando el esfuerzo cortante crítico de Shields y diseñando maniobras de purga hidráulica (flushing).",
        "concepto_clave_latex": r"\theta = \frac{\tau_0}{(\rho_s - \rho) g d_{50}} \ge \theta_c \approx 0.045 \quad ; \quad \text{TE} = 1 - \frac{1}{1 + 0.005 C/I} \quad ; \quad \tau_0 = \rho g R_h S_f",
        "ejemplo": "Problema 1: Un río andino transporta arena con $d_{50} = 1.5\\text{ mm}$ y densidad de sedimentos $\\rho_s = 2650\\text{ kg/m}^3$. En el canal de aproximación, la pendiente es $S_f = 0.002$ y el radio hidráulico es $R_h = 1.8\\text{ m}$. Calcular el esfuerzo cortante de fondo $\\tau_0$ y el parámetro adimensional de Shields $\\theta$: Esfuerzo en fondo: $\\tau_0 = 1000 \\times 9.81 \\times 1.8 \\times 0.002 = 35.316\\text{ N/m}^2$. Parámetro de Shields: $\\theta = \\frac{35.316}{(2650 - 1000) \\times 9.81 \\times 0.0015} = \\frac{35.316}{1650 \\times 9.81 \\times 0.0015} = \\frac{35.316}{24.28} = 1.455$. Como $\\theta = 1.455 \\gg \\theta_c (0.045)$, hay transporte masivo de sedimentos de fondo hacia el desarenador de la central. Problema 2: En la curva de Brune, la eficiencia de atrapamiento de sedimentos de un embalse con relación capacidad/volumen de aporte anual de $C/I = 0.25$ es $\\text{TE} \\approx 92\\%$, perdiendo volumen útil de almacenamiento año a año si no se abren compuertas de fondo en crecientes (maniobra de sediment flushing).",
        "bloque_sugerido": "Hidráulica Fluvial 45 min • Curvas de sedimentación de Brune y diseño de desarenadores Dufour",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSPORTE DE SEDIMENTOS",
                "titulo": "Carga de Fondo vs Carga en Suspensión",
                "puntos": [
                    "Carga de Fondo (Bedload): Granos de arena y grava que ruedan o saltan por el fondo arrastrados por el esfuerzo cortante $\\tau_0$.",
                    "Carga en Suspensión: Limos finos y arcillas sustentados por los remolinos turbulentos del río (perfil de Rouse).",
                    "El desarenador desvía y asienta partículas con diámetro $> 0.2\\text{ mm}$ antes de que entren a la turbina, evitando el desgaste abrasivo por erosión de álabes."
                ]
            },
            {
                "numero": 2,
                "seccion": "VIDA ÚTIL DE EMBALSES",
                "titulo": "Técnicas de Manejo de Sedimentos",
                "puntos": [
                    "Flushing Hidráulico: Vaciado del embalse durante crecientes para que el río erosione y expulse los sedimentos acumulados por las compuertas de fondo.",
                    "Sluicing: Dejar pasar el agua turbia de crecientes a alta velocidad antes de que los sedimentos decanten en el vaso.",
                    "Revestimiento de álabes con carburo de tungsteno proyectado por plasma (HVOF) para multiplicar por 5 la vida útil de las turbinas."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Pequeñas Centrales Hidroeléctricas (PCH) a Filo de Agua (Run-of-River)",
        "objetivo": "Diseñar esquemas hidroeléctricos a filo de agua sin embalse de regulación estacional, optimizando el caudal de diseño $Q_d$ a partir de la curva de duración de caudales.",
        "concepto_clave_latex": r"P_{d} = \eta \rho g Q_d H_n \quad ; \quad Q_d \in [Q_{70\%}, Q_{85\%}] \quad ; \quad E_{anual} = \int_0^{365} P(t) dt",
        "ejemplo": "Problema 1: Se diseña una PCH a filo de agua en el río Frío (Sierra Nevada de Santa Marta) con salto neto $H_n = 85\\text{ m}$ y eficiencia global de $\\eta = 84\\%$. De la curva de duración de caudales, el caudal excedido el $75\\%$ del tiempo es $Q_{75\\%} = 3.2\\text{ m}^3/\\text{s}$, y el caudal ecológico mínimo fijado por la autoridad ambiental (Corpamag) es $Q_{eco} = 0.6\\text{ m}^3/\\text{s}$. El caudal de diseño turbinable es $Q_d = 3.2 - 0.6 = 2.6\\text{ m}^3/\\text{s}$. Potencia nominal instalada: $P = 0.84 \\times 1000 \\times 9.81 \\times 2.6 \\times 85 = 1.821 \\times 10^6\\text{ W} = 1.821\\text{ MW}$. Problema 2: En épocas de estiaje cuando el caudal cae a $1.8\\text{ m}^3/\\text{s}$, el caudal turbinado se reduce a $1.8 - 0.6 = 1.2\\text{ m}^3/\\text{s}$, generando $840\\text{ kW}$. Se instalan dos turbinas Francis iguales de 910 kW cada una para operar a alta eficiencia tanto en invierno como en verano.",
        "bloque_sugerido": "Ingeniería de PCH 40 min • Análisis tecno-económico y curva de duración de potencia",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESQUEMA A FILO DE AGUA",
                "titulo": "Mínimo Impacto Ambiental",
                "puntos": [
                    "No requiere inundar valles con grandes presas de almacenamiento ni desplazar comunidades.",
                    "Bocatoma lateral o de fondo tipo tirolesa con rejilla autolimpiante para captar el caudal de diseño.",
                    "La generación eléctrica sigue estrictamente el régimen hidrológico natural del río (energía no gestionable estacionalmente)."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPTIMIZACIÓN ECONÓMICA",
                "titulo": "Selección del Caudal de Diseño",
                "puntos": [
                    "Si $Q_d$ es muy grande: La planta genera mucha potencia en crecientes pero opera a baja carga durante el resto del año, encareciendo la inversión civil.",
                    "Si $Q_d$ es muy pequeño: El factor de planta es alto ($>80\\%$), pero se vierte gran cantidad de energía hidroeléctrica por el aliviadero.",
                    "Punto óptimo tecno-económico se ubica habitualmente entre el percentil $Q_{65}$ y $Q_{85}$ de la curva de persistencia."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Hidroelectricidad de Muy Baja Caída (VLH) y Tornillo Hidrodinámico de Arquímedes",
        "objetivo": "Modelar turbinas de muy baja caída ($H < 5\\text{ m}$) y tornillos de Arquímedes operando en reversa como turbogeneradores 'fish-friendly' en presas existentes y canales de riego.",
        "concepto_clave_latex": r"P_{tornillo} = \eta \rho g Q H \quad [\eta \approx 80 - 86\%] \quad ; \quad Q = \frac{2\pi \omega}{60} \cdot V_{cangilon} \cdot N_{asp}",
        "ejemplo": "Problema 1: Se aprovecha una caída de $H = 2.8\\text{ m}$ en un vertedero de riego con caudal de $Q = 4.5\\text{ m}^3/\\text{s}$ instalando un tornillo de Arquímedes hidrodinámico con eficiencia global $\\eta = 82\\%$. Calcular la potencia eléctrica generada: $P = 0.82 \\times 1000 \\times 9.81 \\times 4.5 \\times 2.8 = 101345\\text{ W} = 101.35\\text{ kW}$. El tornillo gira a baja velocidad ($\sim 25\\text{ rpm}$) con un diámetro de $2.6\\text{ m}$ y una inclinación de $30^\\circ$ respecto a la horizontal. Problema 2: Debido a las bajas presiones hidrodinámicas y el movimiento suave sin cambios bruscos de dirección, los peces descienden vivos a través de los cangilones del tornillo con una tasa de supervivencia comprobada del $99\\%$, eliminando la necesidad de costosos filtros de peces.",
        "bloque_sugerido": "Microgeneración 40 min • Geometría del tornillo de Arquímedes y turbinas VLH integradas",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL RETO DE LAS BAJAS CAÍDAS",
                "titulo": "Aprovechamiento de Caídas Menores a 5 Metros",
                "puntos": [
                    "Turbinas convencionales (Francis o Kaplan) resultan inviables económicamente por los enormes diámetros de tubería y casa de máquinas.",
                    "Turbina VLH (Very Low Head): Turbina Kaplan compacta de velocidad variable instalada directamente en el vano de la compuerta.",
                    "Tornillo de Arquímedes Hidrodinámico: Opera a presión atmosférica llenando cámaras volumétricas continuas de agua que descienden por gravedad."
                ]
            },
            {
                "numero": 2,
                "seccion": "ECOLOGÍA Y MANTENIMIENTO",
                "titulo": "Sostenibilidad de Canal Abierto",
                "puntos": [
                    "No requiere desarenador fino; admite el paso de sólidos en suspensión y hojarasca sin atascarse.",
                    "Generador asíncrono o de imanes permanentes acoplado mediante multiplicador planetario.",
                    "Excelente opción para electrificación rural y autoabastecimiento en distritos de adecuación de tierras."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Curvas Colina (Hill Charts) y Mapas de Rendimiento de Turbinas Hidráulicas",
        "objetivo": "Interpretar curvas colina de rendimiento adimensional ($n_{11}, Q_{11}, \eta$) obtenidas en modelos a escala reducida en banco de ensayos según norma IEC 60193 para predecir la operación del prototipo.",
        "concepto_clave_latex": r"n_{11} = \frac{n D}{\sqrt{H}} \quad ; \quad Q_{11} = \frac{Q}{D^2 \sqrt{H}} \quad ; \quad \eta_{prototipo} = 1 - (1 - \eta_{modelo})\left(\frac{Re_{mod}}{Re_{prot}}\right)^{0.16}",
        "ejemplo": "Problema 1: Un modelo a escala de turbina Francis ($D_m = 0.35\\text{ m}$) ensayado bajo un salto de $H_m = 10\\text{ m}$ alcanza su punto óptimo a $n_m = 950\\text{ rpm}$ con caudal $Q_m = 0.28\\text{ m}^3/\\text{s}$ y eficiencia $\\eta_m = 91.5\\%$. Calcular las variables unitarias de la colina: $n_{11} = \\frac{950 \\times 0.35}{\\sqrt{10}} = \\frac{332.5}{3.1623} = 105.15\\text{ rpm}$. $Q_{11} = \\frac{0.28}{(0.35)^2 \\sqrt{10}} = \\frac{0.28}{0.1225 \\times 3.1623} = \\frac{0.28}{0.3874} = 0.7228\\text{ m}^3/\\text{s}$. Si el prototipo industrial tiene diámetro $D_p = 2.1\\text{ m}$ y operará bajo $H_p = 120\\text{ m}$, su velocidad de giro síncrona óptima es $n_p = \\frac{n_{11} \\sqrt{H_p}}{D_p} = \\frac{105.15 \\times \\sqrt{120}}{2.1} = \\frac{105.15 \\times 10.954}{2.1} = 548.5\\text{ rpm}$ (se selecciona generador de 14 polos a 514.3 rpm o 12 polos a 600 rpm). Problema 2: Por efecto de escala de Reynolds (fórmula de Hutton / IEC 60193), las pérdidas viscosas relativas disminuyen en la turbina grande, elevando la eficiencia del prototipo a $\\eta_p \\approx 94.2\\%$.",
        "bloque_sugerido": "Ensayos de Modelos 45 min • Digitalización de curvas colina y transposición IEC 60193",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES DE SEMEJANZA HIDRÁULICA",
                "titulo": "Variables Unitarias (n11, Q11, P11)",
                "puntos": [
                    "Permiten representar el comportamiento de toda una familia de turbinas geométricamente semejantes en una sola gráfica universal.",
                    "Las curvas de igual rendimiento forman elipses concéntricas semejantes a curvas de nivel topográficas ('colina' o 'Hill Chart').",
                    "El 'ojo de la colina' identifica el punto de diseño con máxima eficiencia de conversión hidrodinámica."
                ]
            },
            {
                "numero": 2,
                "seccion": "LÍMITES OPERATIVOS",
                "titulo": "Zonas de Inestabilidad y Cavitación",
                "puntos": [
                    "A cargas parciales ($< 40\\% Q_{nom}$), el flujo a la salida del rodete desarrolla una antorcha de vórtice cavitante helicoidal pulsante en el tubo de aspiración.",
                    "Induce fluctuaciones de presión y vibraciones severas a frecuencias submúltiplos de la rotación ($0.2 - 0.4 f_n$).",
                    "El mapa colina define la envolvente de operación permitida y las zonas prohibidas de carga continua."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Velocidad Específica ($n_s, N_q$) y Criterios Universales de Selección de Turbinas",
        "objetivo": "Calcular la velocidad específica de forma y caudal ($n_s, N_q$) a partir de las condiciones de diseño $(H_n, Q, P)$, aplicando la carta universal de selección tecnológica de turbomáquinas.",
        "concepto_clave_latex": r"n_s = \frac{n \sqrt{P [\\text{kW}]}}{H^{5/4}} \quad ; \quad N_q = \frac{n \sqrt{Q [\\text{m}^3/\\text{s}]}}{H^{3/4}} \quad ; \quad n = \frac{120 f}{p_{polos}}",
        "ejemplo": "Problema 1: Un aprovechamiento hidroeléctrico dispone de un salto neto $H_n = 220\\text{ m}$ y un caudal de $Q = 15\\text{ m}^3/\\text{s}$. Con $\\eta = 90\\%$, la potencia generada es $P = 0.90 \\times 1000 \\times 9.81 \\times 15 \\times 220 = 29.135 \\times 10^3\\text{ kW} = 29.135\\text{ MW}$. Para $f = 60\\text{ Hz}$ y un generador de 12 polos, la velocidad síncrona es $n = \\frac{120 \\times 60}{12} = 600\\text{ rpm}$. Calcular la velocidad específica $n_s$: $H^{5/4} = (220)^{1.25} = 868.5$. Raíz de potencia: $\\sqrt{29135} = 170.69$. Luego: $n_s = \\frac{600 \\times 170.69}{868.5} = \\frac{102414}{868.5} = 117.9\\text{ rpm (m, kW)}$. Clasificación: $n_s$ entre 80 y 250 corresponde indiscutiblemente a una turbina Francis de media caída. Problema 2: Si el salto fuera $H_n = 700\\text{ m}$ con $Q = 3\\text{ m}^3/\\text{s}$, $n_s \\approx 28$, exigiendo una turbina Pelton de múltiples inyectores; si fuera $H_n = 25\\text{ m}$ con $Q = 80\\text{ m}^3/\\text{s}$, $n_s \\approx 450$, exigiendo una turbina Kaplan de álabes orientables.",
        "bloque_sugerido": "Selección de Turbomáquinas 40 min • Diagramas de campo de aplicación H-Q y número específico de forma",
        "slides": [
            {
                "numero": 1,
                "seccion": "PARÁMETRO CINEMÁTICO DE FORMA",
                "titulo": "El Significado Físico de ns",
                "puntos": [
                    "Velocidad en rpm a la que giraría una turbina geométrica equivalente que produjera 1 kW bajo 1 metro de salto.",
                    "Pelton: $n_s \\approx 10 - 70$ (flujo tangencial, gran salto, bajo caudal).",
                    "Francis: $n_s \\approx 70 - 450$ (flujo centrípeto mixto, saltos medios de 40 a 500 m).",
                    "Kaplan y Axiales: $n_s \\approx 400 - 1100$ (flujo axial, saltos bajos de 2 a 50 m, grandes caudales)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIOS DE SELECCIÓN",
                "titulo": "Áreas de Solapamiento Tecnológico",
                "puntos": [
                    "En zonas limítrofes ($H \\sim 150 - 250\\text{ m}$): Pelton multinyector vs Francis lenta. Pelton mantiene alta eficiencia a cargas parciales ($<30\\%$); Francis es más compacta pero sufre cavitación a baja carga.",
                    "En zonas bajas ($H \\sim 30 - 60\\text{ m}$): Francis rápida vs Kaplan. La doble regulación de Kaplan (rodete y distribuidor) ofrece curvas de rendimiento planas en un amplio rango de caudales.",
                    "Impacta directamente el costo del generador: mayor $n_s$ implica generadores más pequeños y económicos de menos polos."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Generadores Síncronos Hidroeléctricos: Momento de Inercia $GD^2$ y Constante $H$",
        "objetivo": "Determinar los parámetros electromecánicos del grupo hidrogenerador de polos salientes, calculando el momento de inercia polar $J$, el efecto volante $GD^2$ y la constante de inercia $H$ requerida para la estabilidad de red.",
        "concepto_clave_latex": r"H = \frac{E_{cin}}{S_{nom}} = \frac{\frac{1}{2} J \omega_m^2}{S_{nom}} = \frac{1.37 \\times 10^{-6} GD^2 n^2}{S_{nom} [\\text{kVA}]} \quad [\text{s}] \quad ; \quad J = \frac{GD^2}{4}",
        "ejemplo": "Problema 1: Un hidrogenerador síncrono de polos salientes tiene una potencia nominal de $S_{nom} = 50\\text{ MVA}$ a $n = 360\\text{ rpm}$ (20 polos, $60\\text{ Hz}$). El pliego de condiciones de XM (operador del sistema colombiano) exige una constante de inercia de $H = 3.5\\text{ segundos}$ para contribuir a la estabilidad inercial del Sistema Interconectado Nacional. Calcular la energía cinética rotacional almacenada a velocidad síncrona y el efecto de volante $GD^2$ requerido: Energía cinética: $E_{cin} = H \\cdot S_{nom} = 3.5\\text{ s} \\times 50000\\text{ kVA} = 175000\\text{ kJ} = 175\\text{ MJ}$. Despejando $GD^2$: $GD^2 = \\frac{E_{cin} [\\text{kJ}]}{1.37 \\times 10^{-6} n^2} = \\frac{175000}{1.37 \\times 10^{-6} \\times (360)^2} = \\frac{175000}{1.37 \\times 10^{-6} \\times 129600} = \\frac{175000}{0.17755} \\approx 985630\\text{ kg}\\cdot\\text{m}^2$. Problema 2: Si el rotor natural aporta solo $GD^2 = 700000\\text{ kg m}^2$, se debe sobredimensionar la llanta del rotor o instalar un volante de inercia de acero forjado adicional para no violar la estabilidad de frecuencia.",
        "bloque_sugerido": "Sistemas de Generación 45 min • Cálculo de inercia sintética y dinámica del rotor hidroeléctrico",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONSTRUCCIÓN DE POLOS SALIENTES",
                "titulo": "Rotores Lentos de Gran Diámetro",
                "puntos": [
                    "A diferencia de los turbogeneradores térmicos que giran a 3600 rpm (rotor cilíndrico liso de 2 polos), los hidrogeneradores operan a velocidades lentas ($100 - 600\\text{ rpm}$) con decenas de polos salientes.",
                    "Configuración de eje vertical predominante en unidades medianas y grandes, sostenidas por un cojinete de empuje axial (chumaceras Michell o Kingsbury).",
                    "Gran diámetro de rotor ($D > 4 - 8\\text{ m}$) que proporciona un elevado momento de inercia natural intrínseco."
                ]
            },
            {
                "numero": 2,
                "seccion": "INERCIA Y ESTABILIDAD DE FRECUENCIA",
                "titulo": "La Constante de Inercia H",
                "puntos": [
                    "Representa el tiempo en segundos durante el cual el generador podría entregar su potencia nominal completa consumiendo únicamente su energía cinética de rotación.",
                    "Crucial durante los primeros 500 ms tras la pérdida de una gran línea de interconexión (frena la tasa de caída de frecuencia RoCoF).",
                    "Permite integrar mayores cuotas de energías renovables intermitentes sin inercia física (solar PV y eólica convertida)."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Transitorios Electromecánicos y Rechazo de Carga (Load Rejection) en Centrales",
        "objetivo": "Calcular la sobrevelocidad transitoria del rotor $\\Delta n_{max}$ y la sobrepresión simultánea $\\Delta H_{max}$ durante el disparo imprevisto del interruptor de potencia a plena carga.",
        "concepto_clave_latex": r"\Delta n_{max} = n_0 \sqrt{1 + \frac{2 P_0 \Delta t_{cierre}}{J \omega_0^2}} - n_0 \approx \frac{n_0 T_{cierre}}{2 T_a} \quad ; \quad T_a = \frac{J \omega_0^2}{P_0}",
        "ejemplo": "Problema 1: Una unidad hidroeléctrica de 40 MW a 450 rpm sufre un rechazo total de carga ($P_0 = 40\\text{ MW}$, interruptor de línea abierto). El tiempo de aceleración mecánica del grupo es $T_a = 7.0\\text{ s}$. El servomotor de los álabes directrices tiene un tiempo de cierre programado de $T_c = 4.5\\text{ s}$. Calcular la sobrevelocidad máxima teórica que alcanzará la máquina: Relación: $\\frac{\\Delta n}{n_0} \\approx \\frac{T_c}{2 T_a} = \\frac{4.5}{2 \\times 7.0} = \\frac{4.5}{14.0} \\approx 0.3214$ ($32.14\\%$ de sobrevelocidad). Velocidad máxima transitoria: $n_{max} = 450(1 + 0.3214) = 594.6\\text{ rpm}$. Problema 2: Si los álabes se cierran demasiado rápido para mitigar la sobrevelocidad ($T_c < 2\\text{ s}$), el golpe de ariete sobre la tubería forzada se disparará a niveles peligrosos; el diseño de la ley de cierre del gobernador optimiza un compromiso ('trade-off') entre sobrevelocidad admisible (típicamente $< 35\\%$) y sobrepresión admisible ($< 25\\%$ del salto estático).",
        "bloque_sugerido": "Seguridad de Planta 45 min • Simulación de rechazo de carga y velocidad de embalamiento (runaway)",
        "slides": [
            {
                "numero": 1,
                "seccion": "DISPARO POR FALLA ELÉCTRICA",
                "titulo": "El Escenario de Load Rejection",
                "puntos": [
                    "Al dispararse el interruptor, el par electromagnético resistente colapsa a cero instantáneamente ($T_e = 0$).",
                    "El par hidráulico motor $T_m$ continúa acelerando la masa rotativa con una aceleración angular máxima: $J \\frac{d\\omega}{dt} = T_m$.",
                    "La máquina se embala hacia su velocidad de embalamiento (runaway speed, hasta $180\\% - 220\\% n_0$ en Kaplan y Francis) si las compuertas no cierran."
                ]
            },
            {
                "numero": 2,
                "seccion": "LEYES DE CIERRE AMORTIGUADAS",
                "titulo": "Cierre en Dos Pendientes",
                "puntos": [
                    "Cierre rápido inicial hasta aproximadamente el 30% de apertura para cortar rápidamente el aporte de par motor.",
                    "Cierre lento secundario en el tramo final para amortiguar el golpe de ariete cuando el agua se aproxima a velocidad cero.",
                    "Todas las piezas mecánicas del generador (polos, devanados, cruceta) deben diseñarse para soportar los esfuerzos centrífugos extremos a velocidad de embalamiento sin deformación plástica."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Centrales Hidroeléctricas Reversibles de Bombeo (PHS): Turbomaquinaria y Rendimiento Round-Trip",
        "objetivo": "Modelar el ciclo de acumulación por bombeo (Pumped Hydro Storage - PHS), analizando turbinas reversibles Francis bomba-turbina, eficiencias acopladas de ida y vuelta y despacho como batería hidroeléctrica a gran escala.",
        "concepto_clave_latex": r"\eta_{RTE} = \eta_{bombeo} \times \eta_{turbinado} = (\eta_{m} \eta_{b} \eta_{c,b}) \times (\eta_{c,t} \eta_{t} \eta_{g}) \approx 72 - 82\%",
        "ejemplo": "Problema 1: Una central PHS dispone de un embalse superior con volumen útil de 6 millones de $\\text{m}^3$ a un salto neto medio de $H = 380\\text{ m}$. Eficiencia del modo bombeo (consumo de excedente solar): $\\eta_B = 88\\%$. Eficiencia del modo turbinado (generación nocturna): $\\eta_T = 90\\%$. Eficiencia de transformadores y líneas: $98\\%$ en cada sentido. Rendimiento Round-Trip (RTE): $\\eta_{RTE} = (0.88 \\times 0.98) \\times (0.90 \\times 0.98) = 0.8624 \\times 0.882 = 76.06\\%$. Energía eléctrica consumida para bombear el embalse completo: $E_{in} = \\frac{1000 \\times 9.81 \\times 6 \\times 10^6 \\times 380}{3600 \\times 10^6 \\times 0.8624} = \\frac{22366.8}{3104.6} = 7.205\\text{ GWh}$. Energía eléctrica devuelta a la red durante el pico de demanda: $E_{out} = 7.205 \\times 0.7606 = 5.48\\text{ GWh}$ (almacenamiento masivo equivalente a más de 500,000 baterías residenciales de litio). Problema 2: En modo bombeo, el rodete gira en sentido horario y la máquina opera contra la curva $H-Q$ del sistema; el motor síncrono arranca mediante convertidor estático de frecuencia (SFC) para evitar caídas de tensión en la red de transmisión.",
        "bloque_sugerido": "Almacenamiento Hidráulico 45 min • Curvas de cuatro cuadrantes de turbinas reversibles Francis",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA BATERÍA DEL SISTEMA ELÉCTRICO",
                "titulo": "El Papel Estratégico de PHS",
                "puntos": [
                    "Representa más del 90% de toda la capacidad de almacenamiento de energía eléctrica a escala global instalada en el planeta.",
                    "Bombea agua al embalse superior durante horas de baja demanda o alta radiación solar excedente (precios de energía baratos o negativos).",
                    "Turbina el agua hacia el embalse inferior durante las horas pico de máxima demanda nocturna (arbitraje de energía y soporte de reserva rodante)."
                ]
            },
            {
                "numero": 2,
                "seccion": "RODETE REVERSIBLE FRANCIS",
                "titulo": "Compromiso Hidrodinámico de Diseño",
                "puntos": [
                    "Un rodete diseñado óptimamente como bomba difiere de uno optimizado como turbina; el rodete reversible Francis es un compromiso hidrodinámico con menor rendimiento pico que dos máquinas separadas.",
                    "Unidades de velocidad variable con convertidores back-to-back de plena potencia permiten regular la potencia consumida en modo bombeo.",
                    "Tiempo de transición de bomba a turbina de menos de 90 segundos en centrales modernas estabiliza instantáneamente caídas de frecuencia de red."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Almacenamiento Hidroeléctrico por Bombeo Marino y Cavernas Subterráneas (UPHS)",
        "objetivo": "Evaluar esquemas no convencionales de almacenamiento por bombeo que utilizan el mar como embalse inferior o cavernas mineras subterráneas desmanteladas como reservorio inferior de alta caída.",
        "concepto_clave_latex": r"E_{almacenada} = \rho_{mar} g V_{util} H \quad [\rho_{mar} = 1025\text{ kg/m}^3] \quad ; \quad P = \frac{E}{t_{descarga}}",
        "ejemplo": "Problema 1: En las costas acantiladas del Caribe (Santa Marta/Taganga), se plantea un sistema de bombeo marino con un embalse superior artificial excavado en la meseta costera a $H = 400\\text{ m}$ sobre el nivel del mar con un volumen de $1.5\\text{ millones de m}^3$. El mar Caribe actúa como reservorio inferior infinito sin costo de adquisición de predios. Densidad del agua salada: $\\rho = 1025\\text{ kg/m}^3$. Energía potencial teórica almacenada: $E = 1025 \\times 9.81 \\times (1.5 \\times 10^6) \\times 400 = 6.033 \\times 10^{12}\\text{ J} = 1.676\\text{ GWh}$. Si se turbina en 6 horas con eficiencia del $85\\%$, la potencia media inyectada a la red es: $P_e = \\frac{1.676 \\times 10^6\\text{ kWh} \\times 0.85}{6\\text{ h}} = 237.4\\text{ MW}$. Problema 2: El uso de agua de mar impone el empleo de aceros inoxidables superdúplex ($25\\% Cr$), ánodos de sacrificio galvánicos de zinc y recubrimientos epóxicos cerámicos para resistir la corrosión marina por cloruros y la bioincrustación por percebes y algas.",
        "bloque_sugerido": "Sistemas Innovadores 40 min • Factibilidad de bombeo marino en el Caribe y cavernas UPHS",
        "slides": [
            {
                "numero": 1,
                "seccion": "BOMBEO MARINO (SEAWATER PHS)",
                "titulo": "El Océano como Depósito Inferior",
                "puntos": [
                    "Elimina la necesidad y el costo de construir un embalse inferior artificial.",
                    "Excelente opción para regiones costeras con topografía montañosa escarpada cercana al litoral.",
                    "Planta pionera de Yanbaru en Okinawa (Japón) demostró la viabilidad técnica operando con rodete de acero inoxidable austenítico."
                ]
            },
            {
                "numero": 2,
                "seccion": "CAVERNAS SUBTERRÁNEAS (UPHS)",
                "titulo": "Reutilización de Minas Agotadas",
                "puntos": [
                    "Aprovecha galerías de minas de carbón o sal abandonadas a profundidades de $600 - 1200\\text{ m}$ como reservorio inferior.",
                    "El embalse superior se ubica a nivel de superficie, minimizando el impacto visual en el paisaje.",
                    "Salto hidrostático gigantesco que reduce el volumen de agua necesario para almacenar gigavatios-hora de energía."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Hidráulica de Aliviaderos de Presa: Perfiles Creager, Compuertas Radiales y Resalto",
        "objetivo": "Calcular la capacidad de evacuación de crecidas en aliviaderos de cresta libre tipo Creager y dimensionar cuencos amortiguadores de resalto hidráulico para disipar la energía cinética destructiva del flujo.",
        "concepto_clave_latex": r"Q = C_d L_e H_e^{3/2} \quad [C_d \approx 2.0 - 2.22] \quad ; \quad \frac{y_2}{y_1} = \frac{1}{2}\left( \sqrt{1 + 8 Fr_1^2} - 1 \right) \quad ; \quad Fr_1 = \frac{v_1}{\sqrt{g y_1}}",
        "ejemplo": "Problema 1: Un aliviadero tipo Creager tiene una longitud efectiva de cresta de $L_e = 45\\text{ m}$ y un coeficiente de descarga de $C_d = 2.18$. Durante la crecida máxima probable (CMP), la carga sobre la cresta es $H_e = 3.8\\text{ m}$. Calcular el caudal de alivio evacuado: $Q = 2.18 \\times 45 \\times (3.8)^{1.5} = 98.1 \\times 7.408 = 726.7\\text{ m}^3/\\text{s}$. Problema 2: Al pie del aliviadero, el agua desciende por la rápida alcanzando el cuenco disipador con un tirante supercrítico de $y_1 = 0.8\\text{ m}$ a una velocidad de $v_1 = 20.2\\text{ m/s}$. Calcular el número de Froude entrante y el tirante conjugado subcrítico $y_2$ tras el resalto hidráulico: $Fr_1 = \\frac{20.2}{\\sqrt{9.81 \\times 0.8}} = \\frac{20.2}{\\sqrt{7.848}} = \\frac{20.2}{2.801} = 7.21$ (resalto fuerte y estable). Relación de tirantes: $\\frac{y_2}{0.8} = \\frac{1}{2}(\\sqrt{1 + 8(7.21)^2} - 1) = \\frac{1}{2}(\\sqrt{1 + 8(51.98)} - 1) = \\frac{1}{2}(\\sqrt{416.88} - 1) = \\frac{1}{2}(20.418 - 1) = 9.709$. Tirante conjugado: $y_2 = 0.8 \\times 9.709 = 7.77\\text{ m}$. Pérdida de energía disipada en el resalto: $\\Delta E = \\frac{(y_2 - y_1)^3}{4 y_1 y_2} = \\frac{(7.77 - 0.8)^3}{4(0.8)(7.77)} = \\frac{338.25}{24.86} = 13.61\\text{ metros}$ de energía convertida en turbulencia y calor, protegiendo el lecho del río contra socavación.",
        "bloque_sugerido": "Obras Hidráulicas de Presas 45 min • Perfiles Creager de depresión vs sobrepresión y resalto",
        "slides": [
            {
                "numero": 1,
                "seccion": "EVACUACIÓN SEGURA DE CRECIDAS",
                "titulo": "La Estructura Más Crítica de la Presa",
                "puntos": [
                    "El aliviadero garantiza que el nivel del agua jamás sobrepase la coronación de la presa (sobrevertido o overtopping), causa principal del colapso de presas de tierra.",
                    "El perfil Creager reproduce fielmente la geometría de la cara inferior de una lámina vertiente ventilada natural, evitando presiones negativas y cavitación en el concreto.",
                    "Compuertas Radiales (Tainter): Operadas por cables o pistones hidráulicos; transfieren las cargas hidrostáticas hacia un pivote trunnion central."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISIPACIÓN DE ENERGÍA",
                "titulo": "Cuencos Amortiguadores y Trampolines de Lanzamiento",
                "puntos": [
                    "Cuenco Amortiguador (Stilling Basin): Provoca un resalto hidráulico hidráulico forzado que confina la disipación dentro de una losa armada con dados amortiguadores.",
                    "Trampolín de Lanzamiento (Ski Jump): Proyecta el chorro a gran distancia en el aire hacia una fosa de socavación natural en el centro del río.",
                    "Disipa potencias cinéticas colosales de miles de megavatios de energía hidráulica bruta en minutos."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Estabilidad Geotécnica y Estructural de Presas de Concreto y Enrocado (CFRD)",
        "objetivo": "Evaluar la seguridad estructural frente al volcamiento, deslizamiento basal y subpresión en presas de gravedad de concreto y presas de enrocado con cara de concreto (CFRD).",
        "concepto_clave_latex": r"FS_{deslizamiento} = \frac{\mu (\sum V - U)}{\sum H} \ge 1.5 \quad ; \quad FS_{volcamiento} = \frac{\sum M_{estabilizantes}}{\sum M_{desestabilizantes}} \ge 2.0 \quad ; \quad U = \frac{1}{2}\gamma_w h A_{base}",
        "ejemplo": "Problema 1: Una presa de gravedad de concreto de sección triangular tiene una altura de $H = 60\\text{ m}$, ancho de base $B = 40\\text{ m}$ y longitud de 1 m. Densidad del concreto $\\rho_c = 2400\\text{ kg/m}^3$ ($23.54\\text{ kN/m}^3$). Peso propio de la presa: $W = \\frac{1}{2}(40)(60)(23.54) = 28248\\text{ kN/m}$. Empuje hidrostático horizontal: $F_H = \\frac{1}{2}\\rho_w g H^2 = \\frac{1}{2}(9.81)(60)^2 = 17658\\text{ kN/m}$. Subpresión en la base triangular lineal: $U = \\frac{1}{2}(9.81 \\times 60)(40) = 11772\\text{ kN/m}$. Fuerza vertical neta: $\\sum V = W - U = 28248 - 11772 = 16476\\text{ kN/m}$. Si el coeficiente de fricción concreto-roca es $\\mu = 0.70$ y se desprecia la cohesión: Factor de seguridad al deslizamiento: $FS_{desl} = \\frac{0.70 \\times 16476}{17658} = \\frac{11533.2}{17658} = 0.653 < 1.5$ (inaceptable, la presa deslizaría). Solución geotécnica: Se instala una cortina de inyecciones de lechada de cemento y una galería de drenaje a $B/3$, reduciendo la subpresión $U$ en un $60\\%$, elevando el factor de seguridad a $FS_{desl} = 1.62 > 1.5$. Problema 2: En presas de enrocado con losa de concreto (CFRD como la presa de Chivor o Miel I), el talud de aguas abajo se diseña a $1.3H:1V$ garantizando estabilidad sísmica mediante el método de Bishop modificado.",
        "bloque_sugerido": "Geotecnia de Presas 45 min • Redes de flujo de filtración y cálculo de subpresión en galerías",
        "slides": [
            {
                "numero": 1,
                "seccion": "MECÁNICA DE LA SUBPRESIÓN",
                "titulo": "La Fuerza Desestabilizante Oculta",
                "puntos": [
                    "El agua a presión del embalse se infiltra a través de las microfisuras de la roca de cimentación ejerciendo un empuje hidrostático vertical hacia arriba (subpresión $U$).",
                    "Reduce drásticamente el peso efectivo que mantiene a la presa anclada al suelo.",
                    "Los orificios de drenaje alivian la presión intersticial evacuando el agua hacia galerías de inspección internas."
                ]
            },
            {
                "numero": 2,
                "seccion": "TIPOLOGÍAS MODERNAS (CFRD)",
                "titulo": "Presas de Enrocado con Pantalla de Concreto",
                "puntos": [
                    "El cuerpo de la presa se construye con piedra y roca de cantera compactada por rodillos vibratorios.",
                    "La estanqueidad la proporciona exclusivamente una losa delgada de concreto armado de 30 a 50 cm de espesor en el talud de aguas arriba.",
                    "Excelente flexibilidad y resiliencia ante sismos de alta intensidad sin riesgo de falla frágil."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Monitoreo Piezométrico e Instrumentación Geotécnica de Seguridad de Presas",
        "objetivo": "Diseñar el sistema de instrumentación y auscultación para la vigilancia continua de presas, integrando piezómetros de cuerda vibrante, péndulos directos/invertidos y acelerógrafos.",
        "concepto_clave_latex": r"u = \rho_w g h_w \quad [\text{Piezómetro}] \quad ; \quad \Delta x = \int_0^L \theta(z) dz \quad [\text{Inclinómetro}] \quad ; \quad Q_{fugas} = C h^{5/2} \ [\text{Vertedero Thompson}]",
        "ejemplo": "Problema 1: En una presa de concreto de 80 m, se instala un péndulo invertido anclado a 25 m de profundidad en la roca firme inalterada para medir el desplazamiento horizontal relativo de la coronación. Durante el primer llenado del embalse, el sensor óptico de coordenadas bidimensional registra un desplazamiento elástico aguas abajo de $\\Delta x = 14.2\\text{ mm}$ y un asentamiento vertical de $3.1\\text{ mm}$, valores que coinciden dentro del $5\\%$ con las predicciones del modelo tridimensional de elementos finitos (FEM). Problema 2: En el vertedero triangular de 90 grados de la galería de drenaje, el caudal de filtración total medido es $Q_{fugas} = 1.36 h^{5/2} = 4.2\\text{ L/s}$ de agua completamente cristalina. Si el agua se enturbia o el caudal se duplica súbitamente sin cambios en el nivel del embalse, se activa una alarma de emergencia por tubificación interna ('piping').",
        "bloque_sugerido": "Seguridad de Presas 40 min • Redes de monitoreo SCADA en tiempo real y umbrales de alerta",
        "slides": [
            {
                "numero": 1,
                "seccion": "AUSCULTACIÓN INSTRUMENTAL",
                "titulo": "Vigilancia Estructural Permanente",
                "puntos": [
                    "Piezómetros de Cuerda Vibrante: Miden la presión de poro en el suelo y la roca sin retardo hidrodinámico.",
                    "Péndulos Directos e Invertidos: Miden inclinaciones y deflexiones de la estructura con precisión de centésimas de milímetro.",
                    "Extensómetros de varilla multipunto: Detectan deformaciones en los estribos rocosos de la presa."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTROL DE FILTRACIONES",
                "titulo": "Indicadores Premonitorios de Falla",
                "puntos": [
                    "Toda presa filtra agua; lo vital es que la filtración sea controlada, drenada y libre de partículas sólidas arrastradas.",
                    "Aforadores Thompson y celdas de turbidez detectan el inicio de erosión interna.",
                    "Integración con modelos de regresión hidrostática-estacional-tiempo (HST) para aislar efectos climáticos transitorios del envejecimiento estructural."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Caudal Ecológico Ambiental y Pasajes Biológicos para Peces (Fishways)",
        "objetivo": "Calcular regímenes de caudales ambientales aplicando metodologías hidrológicas (Tennant, Q95) e hidrobiológicas (IFIM/PHABSIM), diseñando escalas de peces de artesas sucesivas y ascensores hidráulicos.",
        "concepto_clave_latex": r"Q_{eco, Tennant} \ge 10\% - 30\% \text{ MAF} \quad ; \quad \Delta h_{peldaño} \le 0.15 - 0.30\text{ m} \quad ; \quad v_{ranura} = \sqrt{2 g \Delta h} \le 1.2 - 2.0\text{ m/s}",
        "ejemplo": "Problema 1: Un río en la vertiente norte de la Sierra Nevada tiene un caudal medio anual de $\\text{MAF} = 14.5\\text{ m}^3/\\text{s}$. La autoridad ambiental exige un caudal ecológico estacional según el método de Tennant: $10\\%$ de MAF en estiaje para supervivencia básica ($Q_{eco,estiaje} = 1.45\\text{ m}^3/\\text{s}$) y $30\\%$ de MAF en época reproductiva migratoria ($Q_{eco,reprod} = 4.35\\text{ m}^3/\\text{s}$). Si la bocatoma de una PCH capta agua a 800 msnm, este caudal debe descargarse continuamente por una compuerta ecológica calibrada al pie de la presa sin pasar por las turbinas. Problema 2: Para permitir la migración aguas arriba de peces nativos (bocachico y sábalo) cuya velocidad máxima de nado sostenido es de $1.8\\text{ m/s}$, se diseña una escala de peces de ranura vertical (Vertical Slot Fishway) salvando un desnivel total de $H = 6\\text{ m}$. El salto entre artesas sucesivas se fija en $\\Delta h = 0.15\\text{ m}$. Velocidad del chorro en la ranura: $v = \\sqrt{2(9.81)(0.15)} = \\sqrt{2.943} = 1.715\\text{ m/s} < 1.8\\text{ m/s}$. Número de artesas requeridas: $N = \\frac{6.0}{0.15} = 40\\text{ pozos}$ con volumen suficiente para disipar la energía cinética.",
        "bloque_sugerido": "Hidroecología 45 min • Modelado PHABSIM y diseño hidráulico de escalas de peces",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONECTIVIDAD FLUVIAL",
                "titulo": "El Reto de la Fragmentación del Río",
                "puntos": [
                    "Las presas y azudes constituyen barreras físicas infranqueables para especies de peces reófilas y catádromas que migran para desovar.",
                    "El caudal ecológico no es un caudal mínimo fijo constante; debe replicar la variabilidad estacional natural del régimen hidrológico.",
                    "Preserva macroinvertebrados bentónicos, vegetación de ribera y la dinámica geomorfológica del cauce aguas abajo."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTRUCTURAS DE PASAJE",
                "titulo": "Escalas de Ranura Vertical vs Ascensores",
                "puntos": [
                    "Escala de Ranura Vertical (Vertical Slot): Tolera grandes variaciones del nivel del agua en el embalse sin alterar las velocidades del flujo interno.",
                    "Ascensores de Peces (Fish Lifts): Para presas de más de 30 metros de altura donde una rampa física requeriría kilómetros de longitud.",
                    "Rejillas de toma inclinadas con espaciamiento estrecho ($< 15\\text{ mm}$) y turbinas hidroeléctricas 'fish-friendly' de bordes redondeados."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Despacho Hidrotérmico Coordinado y Programación Dinámica Estocástica (SDDP)",
        "objetivo": "Formular el problema de optimización del despacho económico coordinado de embalses a mediano y largo plazo mediante Programación Dinámica Dual Estocástica (SDDP), calculando el valor del agua.",
        "concepto_clave_latex": r"\min \mathbb{E}\left[ \sum_{t=1}^T \alpha^t \left( C_{term}(G_t) + C_{falla}(D_t - G_t - H_t) \right) \right] \quad \text{s.t.} \quad V_{t+1} = V_t + A_t - u_t - s_t - E_t \quad ; \quad \pi_t = \frac{\partial \text{CostoFuturo}}{\partial V_t}",
        "ejemplo": "Problema 1: Un sistema hidrotérmico simplificado dispone de un embalse hidroeléctrico con factor de conversión $\\rho = 0.5\\text{ MWh/m}^3$ y una planta termoeléctrica de gas con costo variable de generación $C_{term} = 65\\text{ USD/MWh}$. Si se turbina $1\\text{ m}^3$ de agua hoy, se genera $0.5\\text{ MWh}$, ahorrando $0.5 \\times 65 = 32.5\\text{ USD}$ en costos de combustible térmico inmediato. Sin embargo, si el modelo SDDP estima que la probabilidad de sequía en los próximos meses es alta, el 'costo de oportunidad futuro' de ese metro cúbico almacenado (valor marginal del agua $\\pi_t$) asciende a $48\\text{ USD/m}^3$. Decisión óptima de despacho: Conviene retener el agua en el embalse y encender la planta térmica hoy, minimizando el costo esperado a largo plazo. Problema 2: En Colombia (matriz con $>70\\%$ de generación hidroeléctrica), el software SDDP desarrollado por Mario Pereira es el motor analítico oficial que calcula semanalmente los precios de oferta y costo marginal de la energía en la bolsa de XM.",
        "bloque_sugerido": "Optimización Estocástica 45 min • Cortes de Benders y función de costo futuro del agua",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL VALOR DEL AGUA",
                "titulo": "Agua Hoy vs Agua Mañana",
                "puntos": [
                    "El combustible del agua es gratis en el momento, pero tiene un costo de oportunidad económico decisivo respecto a la energía térmica fósil futura que sustituirá.",
                    "Turbinar demasiado hoy vacía los embalses provocando racionamientos eléctricos de costo exorbitante si se desata el fenómeno de El Niño.",
                    "Retener demasiada agua provoca vertimientos inútiles por el aliviadero si llueve más de lo esperado en invierno."
                ]
            },
            {
                "numero": 2,
                "seccion": "ALGORITMO SDDP",
                "titulo": "Programación Dinámica Dual Estocástica",
                "puntos": [
                    "Rompe la 'maldición de la dimensionalidad' en sistemas multiembalse complejos mediante aproximaciones convexas sucesivas (cortes de Benders).",
                    "Simulación hacia adelante (Forward pass) y optimización dual hacia atrás (Backward pass).",
                    "Estándar internacional empleado en más de 30 países para el despacho hidroeléctrico nacional."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Hidrología Estocástica y Series Sintéticas de Caudales: Modelos PARMA",
        "objetivo": "Generar escenarios sintéticos hidrológicos multianuales preservando las propiedades estadísticas históricas (media mensual, varianza y coeficientes de correlación cruzada) mediante modelos autorregresivos periódicos (PAR / PARMA).",
        "concepto_clave_latex": r"z_{t,m} = \frac{Q_{t,m} - \mu_m}{\sigma_m} \quad ; \quad z_{t,m} = \sum_{k=1}^p \phi_{k,m} z_{t,m-k} + \varepsilon_{t,m} \quad [\varepsilon \sim \mathcal{N}(0, \sigma_{\varepsilon,m}^2)]",
        "ejemplo": "Problema 1: En la cuenca del río Magdalena, el caudal medio de abril es $\\mu_4 = 4200\\text{ m}^3/\\text{s}$ con desviación $\\sigma_4 = 850\\text{ m}^3/\\text{s}$, y el de marzo es $\\mu_3 = 2800\\text{ m}^3/\\text{s}$ con $\\sigma_3 = 600\\text{ m}^3/\\text{s}$. El coeficiente autorregresivo estacional es $\\phi_{1,4} = 0.72$ con varianza residual $\\sigma_{\\varepsilon,4} = 0.55$. Si en marzo de un año de simulación el caudal registrado fue $Q_{marzo} = 3400\\text{ m}^3/\\text{s}$, calcular el caudal sintético de abril generado por Monte Carlo con una perturbación normal estándar $w = -0.45$: Estandarización de marzo: $z_{marzo} = \\frac{3400 - 2800}{600} = \\frac{600}{600} = +1.0$. Variable estandarizada de abril: $z_{abril} = \\phi_{1,4} z_{marzo} + \\sigma_{\\varepsilon,4} w = 0.72(1.0) + 0.55(-0.45) = 0.72 - 0.2475 = +0.4725$. Destandarizando el caudal de abril: $Q_{abril} = \\mu_4 + z_{abril} \\sigma_4 = 4200 + (0.4725 \\times 850) = 4200 + 401.6 = 4601.6\\text{ m}^3/\\text{s}$. Problema 2: Simular 10,000 series sintéticas multianuales permite cuantificar con rigor probabilístico la resiliencia de la matriz hidroeléctrica frente a megasequías plurianuales severas.",
        "bloque_sugerido": "Modelado Estocástico 40 min • Calibración de modelos PAR(p) estacionales en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "CICLOS ESTACIONALES Y MEMORIA HIDROLÓGICA",
                "titulo": "Modelos PARMA",
                "puntos": [
                    "Los caudales de ríos presentan una fuerte periodicidad anual condicionada por temporadas de lluvias y estiajes.",
                    "Los parámetros de los modelos ARMA tradicionales son constantes; los modelos PARMA varían sus coeficientes $\\phi_{k,m}$ mes a mes ($m=1..12$).",
                    "Capturan la 'memoria de almacenamiento' natural del suelo y acuíferos de la cuenca hidrográfica."
                ]
            },
            {
                "numero": 2,
                "seccion": "EVALUACIÓN DE RIESGOS CLIMÁTICOS",
                "titulo": "Simulación de Monte Carlo en Sistemas Eléctricos",
                "puntos": [
                    "El registro histórico (50 a 80 años de aforos) es una sola realización muestral de un proceso estocástico infinito.",
                    "Series sintéticas revelan combinaciones críticas de estiajes más severas que las registradas históricamente.",
                    "Base metodológica para fijar la Energía Firme para el Cargo por Confiabilidad (ENFICC) por parte de la CREG."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Gemelos Digitales (Digital Twins) y Monitorización de Vibraciones en Turbinas",
        "objetivo": "Implementar modelos ciberfísicos en tiempo real acoplados con sensores IoT de desplazamiento axial, presión dinámica y temperatura para mantenimiento predictivo y detección temprana de fallas en turbinas.",
        "concepto_clave_latex": r"\text{FFT}(x(t)) \rightarrow X(f) \quad ; \quad f_{BPFI} = \frac{N_b}{2}f_r\left(1 + \frac{d}{D}\cos\alpha\right) \quad ; \quad v_{RMS} = \sqrt{\frac{1}{T}\int_0^T v^2(t)dt} \le 2.8\text{ mm/s}",
        "ejemplo": "Problema 1: En una turbina Francis de 60 MW que gira a $n = 300\\text{ rpm}$ ($f_r = 5.0\\text{ Hz}$) con 15 álabes en el rodete y 20 álabes directrices de distribuidor, el análisis espectral FFT de los acelerómetros del cojinete guía detecta un pico de vibración anómalo a $f = 15 \\times 5.0 = 75\\text{ Hz}$ (frecuencia de paso de álabes, BPF) con velocidad RMS de $v_{RMS} = 6.4\\text{ mm/s}$, superando el límite de advertencia de la norma ISO 10816-5 ($4.5\\text{ mm/s}$). El gemelo digital hidrodinámico diagnostica que la interacción rotor-estátor (RSI) se ha amplificado debido a una desalineación angular de $1.8^\\circ$ en dos paletas directrices adyacentes, programando una calibración correctiva antes de que se propague una fisura por fatiga en la corona. Problema 2: Sensores de emisión acústica de alta frecuencia ($100\\text{ kHz} - 1\\text{ MHz}$) detectan el colapso microscópico de burbujas de cavitación meses antes de que la pérdida de metal sea visible a simple vista.",
        "bloque_sugerido": "Mantenimiento Predictivo 40 min • Análisis de órbitas de cojinetes y gemelos digitales con Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURA DEL GEMELO DIGITAL",
                "titulo": "Sincronización Física y Digital",
                "puntos": [
                    "El Gemelo Digital combina simulaciones numéricas CFD/FEM de alta fidelidad con datos de telemetría de cientos de sensores en tiempo real.",
                    "Monitorea en continuo: Desplazamiento de eje en cojinetes (sensores de proximidad de corrientes de Foucault en $X-Y$), presiones pulsantes en el cono y temperaturas de metal babbit.",
                    "Estima el consumo de vida útil remanente acumulado por fatiga de ciclo bajo y alto en cada maniobra de arranque y parada."
                ]
            },
            {
                "numero": 2,
                "seccion": "DIAGNÓSTICO AUTOMATIZADO CON IA",
                "titulo": "Clasificación de Modos de Falla",
                "puntos": [
                    "Desbalance de masa: Pico dominante a $1\\times$ frecuencia de giro ($1X$).",
                    "Desalineación angular o paralela: Picos prominentes a $2X$ y armónicos superiores.",
                    "Antorcha de vórtice en tubo de aspiración: Pulsación hidrodinámica a baja frecuencia ($0.25X - 0.35X$).",
                    "Reduce paradas no programadas en un 40% e incrementa el factor de disponibilidad técnica de la central."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Cambio Climático, Resiliencia Hídrica y Energía Firme (ENFICC) en Colombia",
        "objetivo": "Calcular la Energía Firme para el Cargo por Confiabilidad (ENFICC) bajo condiciones críticas del fenómeno de El Niño (ENOS) y modelar proyecciones de escorrentía bajo escenarios del IPCC.",
        "concepto_clave_latex": r"\text{ENFICC} = \min_{t \in \text{Niño crítico}} \left( \sum_{i} \text{GenHidro}_i(t) \right) \quad ; \quad \text{CargoPorConfiabilidad} \ [\text{USD/MWh}]",
        "ejemplo": "Problema 1: Una central hidroeléctrica con embalse en Antioquia tiene una capacidad instalada de 400 MW. En un año hidrológico normal medio genera $2200\\text{ GWh/año}$ (factor de planta del $62.8\\%$). Sin embargo, durante la hidrología crítica del fenómeno de El Niño 1991-1992 (la peor sequía registrada en la historia eléctrica colombiana), los caudales colapsaron al $42\\%$ de la media. El modelo de optimización hidroeléctrica dictamina que la central solo puede garantizar con un $95\\%$ de certeza estadística una generación continua de $110\\text{ MW}$ durante el periodo de estiaje crítico. Su ENFICC base asignada por la CREG es por tanto $110\\text{ MW} \\times 24\\text{ h} = 2.64\\text{ GWh/día}$. La diferencia entre su capacidad nominal de 400 MW y su energía firme de 110 MW debe ser respaldada por plantas térmicas a gas o carbón en el mercado de confiabilidad. Problema 2: Modelos del IPCC (escenario SSP2-4.5) proyectan para finales de siglo una reducción del $12\\%$ en la escorrentía media de la cuenca del Magdalena-Cauca y una mayor frecuencia de eventos hidrológicos extremos (sequías e inundaciones intensificadas).",
        "bloque_sugerido": "Regulación Eléctrica 45 min • Metodología CREG de cálculo de ENFICC y subastas de confiabilidad",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL CARGO POR CONFIABILIDAD",
                "titulo": "Asegurando la Energía en Sequías Extremas",
                "puntos": [
                    "Remuneración fija a los generadores para asegurar que mantengan plantas disponibles y operativas para responder en periodos críticos de sequía extrema (El Niño).",
                    "ENFICC: La máxima energía eléctrica que una planta hidroeléctrica es capaz de entregar de manera continua en la condición hidrológica más desfavorable registrada.",
                    "Evita que el país sufra apagones masivos como el racionamiento de 1992 ('la hora Gaviria')."
                ]
            },
            {
                "numero": 2,
                "seccion": "ADAPTACIÓN AL CAMBIO CLIMÁTICO",
                "titulo": "Hibridación Hidro-Solar Flotante (FPV)",
                "puntos": [
                    "Instalación de paneles solares fotovoltaicos flotantes en el espejo de agua de embalses hidroeléctricos.",
                    "Sinergia perfecta: Los paneles generan en horas de sol reduciendo la evaporación de agua del embalse; el agua enfría los paneles elevando su eficiencia un 10%.",
                    "Aprovecha las subestaciones y líneas de transmisión ya construidas de la central hidroeléctrica."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Rehabilitación, Repotenciación (Uprating) y Modernización de Centrales Hidroeléctricas",
        "objetivo": "Evaluar la extensión de vida útil y el incremento de potencia y eficiencia en plantas hidroeléctricas envejecidas mediante el rediseño aerodinámico de rodetes CFD, aislamiento de estátor clase F y automatización digital.",
        "concepto_clave_latex": r"\Delta P = \rho g (Q_{nuevo} H_{nuevo} \eta_{nuevo} - Q_{viejo} H_{viejo} \eta_{viejo}) \quad ; \quad \text{LCOE}_{repotenciacíon} \ll \text{LCOE}_{greenfield}",
        "ejemplo": "Problema 1: Una central hidroeléctrica construida en 1975 cuenta con dos turbinas Francis de 25 MW cada una ($P_{total} = 50\\text{ MW}$, $\\eta = 86.5\\%$). Tras 50 años de operación, se aprueba un proyecto de repotenciación integral (uprating): 1) Se sustituyen los rodetes originales de acero fundido por rodetes modernos fresados en CNC de acero inoxidable martensítico 13Cr-4Ni optimizados con CFD 3D, elevando la eficiencia de turbina al $93.8\\%$ (+7.3 puntos porcentuales). 2) Se rebobina el estátor con aislamiento de resina epóxica al vacío clase F, permitiendo soportar un $15\\%$ más de densidad de corriente sin elevar la temperatura. 3) Se ensanchan los distribuidores para admitir un $8\\%$ más de caudal en horas pico. Nueva potencia por unidad: $P_{nueva} = 25 \\times \\left(\\frac{1.08 \\times 0.938}{0.865}\\right) = 29.28\\text{ MW}$. La central incrementa su potencia total de 50 MW a 58.56 MW (+8.56 MW adicionales de energía limpia) sin alterar las obras civiles de la presa ni construir nuevas tuberías. Problema 2: El costo nivelado de esta energía adicional repotenciada es de apenas $18\\text{ USD/MWh}$, tres veces más económico que construir una nueva central desde cero ('greenfield').",
        "bloque_sugerido": "Gestión de Activos 45 min • Análisis técnico-económico de repotenciación vs reemplazo",
        "slides": [
            {
                "numero": 1,
                "seccion": "EXTENSIÓN DE VIDA ÚTIL DE ACTIVOS",
                "titulo": "Modernizar sin Reconstruir",
                "puntos": [
                    "Las obras civiles de una presa (presa, túneles, casa de máquinas) tienen vidas útiles superiores a 100 años.",
                    "Los equipos electromecánicos (rodetes, devanados, reguladores analógicos) se vuelven obsoletos tras 30 a 50 años de fatiga y desgaste.",
                    "La repotenciación extrae hasta un 15% - 25% más de energía limpia de la misma infraestructura física existente."
                ]
            },
            {
                "numero": 2,
                "seccion": "TECNOLOGÍAS DE MODERNIZACIÓN",
                "titulo": "Del Control Hidromecánico a la Inteligencia Artificial",
                "puntos": [
                    "Sustitución de reguladores centrífugos de bolas mecánicos por gobernadores digitales programables basados en microprocesadores duales redundantes.",
                    "Sistemas de excitación estática rápida de tiristores con estabilizadores de potencia (PSS) de última generación.",
                    "Habilita el control y telemando remoto desatendido de la central desde el centro de control nacional."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06021845)
    # Inject before the next subject marker: 06021846
    inject_topics_after('      - codigo: "06021846"', yaml_text)
    print("06021845 Energía Hidráulica successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
