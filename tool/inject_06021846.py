# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06021846 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Tecnología Bifacial: Albedo del Terreno, Factor de Bifacialidad y Ganancia Trasera",
        "objetivo": "Modelar la captación de irradiancia trasera en módulos solares bifaciales en función del albedo del suelo, altura de instalación sobre el suelo y factor de bifacialidad $\\varphi_{bif}$.",
        "concepto_clave_latex": r"G_{total} = G_{frontal} + \varphi_{bif} \cdot G_{trasero} \quad ; \quad G_{trasero} \approx \alpha_{albedo} G_{GHI} \cdot VF_{suelo-modulo} \quad ; \quad BGG = \frac{Y_{bif} - Y_{mono}}{Y_{mono}} \times 100\%",
        "ejemplo": "Problema 1: Un módulo fotovoltaico bifacial monocristalino TOPCon de $580\\text{ Wp}$ (potencia frontal STC) tiene un factor de bifacialidad de $\\varphi_{bif} = 80\\%$ ($0.80$). Se instala en una planta en Santa Marta sobre suelo de arena blanca costera con albedo de $\\alpha = 0.35$. Si al mediodía la irradiancia frontal incidente en el plano del módulo es $G_{front} = 950\\text{ W/m}^2$ y los sensores traseros miden una irradiancia reflejada difusa de $G_{rear} = 180\\text{ W/m}^2$, calcular la irradiancia equivalente efectiva y la potencia real instantánea generada: Irradiancia equivalente: $G_{eff} = 950 + 0.80(180) = 950 + 144 = 1094\\text{ W/m}^2$. Potencia instantánea: $P = 580\\text{ W} \\times \\frac{1094}{1000} = 634.52\\text{ W}$. La ganancia bifacial instantánea es $BGG = \\frac{634.52 - 551}{551} \\times 100\\% \\approx 15.16\\%$. Problema 2: En seguidores solares de 1 eje, elevar la altura del eje de torque a 1.5 m del suelo y pintar de blanco el suelo incrementa la ganancia bifacial anual promedio a más del $11\\%$, reduciendo el LCOE en un $7\\%$.",
        "bloque_sugerido": "Ingeniería Solar 45 min • Modelado de factores de vista 2D (View Factors) para radiación trasera",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DEL MÓDULO BIFACIAL",
                "titulo": "Captación Frontal y Posterior",
                "puntos": [
                    "Sustituye la lámina posterior opaca de polímero blanco (backsheet) por vidrio templado antirreflectante trasero (estructura vidrio-vidrio).",
                    "Factor de Bifacialidad $\\varphi_{bif} = P_{STC,trasera} / P_{STC,frontal}$: $65-75\\%$ en PERC, $80-85\\%$ en TOPCon, $>90\\%$ en Heterounión (HJT).",
                    "Vidrio-vidrio incrementa la robustez mecánica contra cargas de viento y elimina la penetración de humedad ambiental."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL FACTOR ALBEDO",
                "titulo": "Reflectancia del Entorno",
                "puntos": [
                    "Hierba verde natural: Albedo $\\alpha \\approx 0.18 - 0.22$.",
                    "Suelo árido o arena clara: Albedo $\\alpha \\approx 0.30 - 0.40$.",
                    "Pintura blanca reflectante o membranas geosintéticas: Albedo $\\alpha > 0.65 - 0.80$.",
                    "Evitar sombras directas del tubo de torque de la estructura sobre la cara posterior de las celdas."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Degradación Fotovoltaica: Mecanismos LID, LeTID, PID y Envejecimiento UV",
        "objetivo": "Cuantificar los mecanismos de degradación acelerada en celdas de silicio cristalino (LID por complejos boro-oxígeno, LeTID inducida por temperatura y PID inducida por potencial electrostático), modelando la curva de vida útil a 30 años.",
        "concepto_clave_latex": r"P(t) = P_0 (1 - d_{inicial}) (1 - d_{anual})^t \quad ; \quad \Delta V_{PID} = \sum V_{string} - V_{tierra} \approx 600 - 1500\text{ V}",
        "ejemplo": "Problema 1: Un parque solar de 1500 V DC presenta strings de 28 módulos en serie. El polo negativo del inversor central flota a $-750\\text{ V}$ respecto a tierra, mientras el marco de aluminio de los módulos está sólidamente aterrizado a $0\\text{ V}$. Esta diferencia de potencial electrostático de 750 V arrastra iones de sodio ($Na^+$) desde el vidrio frontal hacia la superficie de la celda de silicio, provocando Degradación Inducida por Potencial (PID). En 18 meses, los módulos cercanos al polo negativo pierden el $35\\%$ de su potencia nominal por reducción drástica de la resistencia en paralelo (shunting). Problema 2: Para mitigar el PID, se instalan cajas de polarización nocturna ('anti-PID boxes') que inyectan una tensión positiva inversa de $+1000\\text{ V}$ durante la noche, expulsando los iones de sodio de vuelta al vidrio y regenerando la celda.",
        "bloque_sugerido": "Confiabilidad Fotovoltaica 40 min • Pruebas IEC 62804 de resistencia a PID en cámara climática",
        "slides": [
            {
                "numero": 1,
                "seccion": "MECANISMOS DE DEGRADACIÓN",
                "titulo": "LID, LeTID y PID",
                "puntos": [
                    "LID (Light-Induced Degradation): Formación de pares Boro-Oxígeno en silicio p-type en las primeras 48 horas de sol ($~1.5 - 2.5\\%$ de pérdida); celdas n-type (TOPCon/HJT) son inmunes a LID por dopaje con fósforo.",
                    "LeTID: Degradación activada por luz y temperatura elevada ($> 60^\\circ\\text{C}$); recuperable parcialmente con recocido térmico.",
                    "PID (Potential-Induced Degradation): Migración de iones por altos voltajes de string ($1500\\text{ V}$); destruye la pasivación de superficie."
                ]
            },
            {
                "numero": 2,
                "seccion": "GARANTÍAS DE POTENCIA",
                "titulo": "Tasa de Degradación Lineal",
                "puntos": [
                    "Año 1: Degradación inicial $\\le 1.0\\%$ en módulos n-type modernos.",
                    "Años 2 al 30: Degradación lineal anual garantizada $\\le 0.40\\%$/año.",
                    "Potencia remanente garantizada al año 30: $\\ge 87.4\\%$ de la potencia nominal de placa inicial."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Topologías de Inversores Solares: Microinversores, Inversores de String y Centralizados",
        "objetivo": "Comparar técnica y económicamente las arquitecturas de conversión DC/AC en plantas fotovoltaicas a escala comercial e industrial (C&I) y utility-scale, evaluando rendimiento ponderado europeo y CEC.",
        "concepto_clave_latex": r"\eta_{Euro} = 0.03\eta_{5\%} + 0.06\eta_{10\%} + 0.13\eta_{20\%} + 0.10\eta_{30\%} + 0.48\eta_{50\%} + 0.20\eta_{100\%} \ge 98.5\%",
        "ejemplo": "Problema 1: Una planta solar de 5 MWp en el Magdalena evalúa dos arquitecturas: 1) Inversor Centralizado de 4.0 MVA único con transformador integrado de media tensión a 1500 V DC. 2) Inversores de String descentralizados (20 unidades de 200 kW cada una, cada una con 12 seguidores MPPT independientes). En presencia de suciedad heterogénea y sombras matutinas parciales, los inversores de string capturan un $2.3\\%$ más de energía anual gracias a sus 240 canales MPPT distribuidos frente a un único MPPT central. Sin embargo, el costo de capital CAPEX del inversor centralizado es un $15\\%$ inferior. El análisis LCOE a 25 años demuestra que los inversores de string minimizan el O&M al no requerir personal de fábrica especializado para reparaciones (se reemplaza un string inverter en 2 horas). Problema 2: En instalaciones residenciales complejas con múltiples orientaciones de tejado, los microinversores a nivel de módulo eliminan totalmente las pérdidas de desajuste.",
        "bloque_sugerido": "Electrónica de Potencia 45 min • Dimensionamiento de inversores con PVsyst y cálculo de CAPEX/OPEX",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURAS DE CONVERSIÓN",
                "titulo": "Centralizado vs String vs Microinversor",
                "puntos": [
                    "Microinversores ($300 - 1500\\text{ W}$): Conversión AC directa en cada módulo; máxima seguridad (sin alto voltaje DC en el techo); costo elevado por vatio.",
                    "Inversores de String ($50 - 350\\text{ kW}$): Estándar moderno C&I y utility-scale; múltiples MPPTs (hasta 12-16) con desconexión inteligente por string.",
                    "Inversores Centrales ($1.5 - 4.5\\text{ MVA}$): Bloques gigantes de potencia con centros de transformación skid; menor número de componentes pero mayor vulnerabilidad por falla única."
                ]
            },
            {
                "numero": 2,
                "seccion": "EFICIENCIA DE CONVERSIÓN",
                "titulo": "Tecnología de Carburo de Silicio (SiC)",
                "puntos": [
                    "Sustitución de IGBTs de silicio tradicionales por MOSFETs de carburo de silicio (SiC) y nitruro de galio (GaN).",
                    "Frecuencias de conmutación de más de 50 kHz con reducción drástica de pérdidas térmicas de conmutación.",
                    "Eficiencias máximas superiores al 99.0% y reducción del peso y volumen de los filtros inductivos a la mitad."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Seguidores Solares (Trackers) de 1 Eje (1T) y Algoritmos de Backtracking",
        "objetivo": "Modelar cinemática y geométricamente el seguimiento solar en eje horizontal norte-sur (HSAT 1T), calculando el ángulo óptimo de rotación y el ángulo de backtracking para evitar el sombreado mutuo inter-filas.",
        "concepto_clave_latex": r"\tan\omega_t = \frac{\cos\alpha_s \sin(\gamma_s - \gamma_t)}{\sin\alpha_s} \quad ; \quad \theta_{backtrack} = \arcsin\left( \frac{W_m}{L_{pitch}} \frac{\cos\theta_{geom}}{\dots} \right) \quad ; \quad GCR = \frac{W_m}{L_{pitch}}",
        "ejemplo": "Problema 1: Un parque solar instala seguidores monofila de un eje horizontal orientado norte-sur (eje azimutal $\\gamma_t = 0^\\circ$). El ancho del módulo en la estructura es $W_m = 2.4\\text{ m}$ (configuración 2 en vertical, 2P) y la separación entre ejes de filas consecutivas es de $L_{pitch} = 6.0\\text{ m}$. Calcular el ratio de cobertura de terreno (Ground Coverage Ratio, GCR): $GCR = \\frac{W_m}{L_{pitch}} = \\frac{2.4}{6.0} = 0.40$ ($40\\%$). En las primeras horas de la mañana, cuando la altura solar es baja ($\\alpha_s = 15^\\circ$), el seguimiento astronómico puro orientaría el seguidor a un ángulo de $\\theta = -60^\\circ$. A este ángulo, la sombra de la fila del este caería sobre la fila vecina, activando diodos bypass y colapsando la producción. El algoritmo de 'Backtracking' retrocede el seguidor a $\\theta_{bt} = -38.5^\\circ$, alineando el borde superior de la fila con el rayo de sombra rasante para garantizar cero sombreado sobre las celdas activas. Problema 2: En la región Caribe (latitud $10^\\circ - 11^\\circ\\text{ N}$), los seguidores de 1 eje aumentan la captación de energía anual en un $22\\% - 28\\%$ comparados con estructuras fijas.",
        "bloque_sugerido": "Geometría Solar Avanzada 45 min • Ecuaciones cinemáticas de rotación 1T y cálculo de sombras",
        "slides": [
            {
                "numero": 1,
                "seccion": "SEGUIMIENTO EN UN EJE HORIZONTAL",
                "titulo": "Arquitectura Norte-Sur (HSAT)",
                "puntos": [
                    "El eje rota de Este a Oeste siguiendo la trayectoria solar diurna.",
                    "Configuraciones: 1P (un módulo en vertical sobre el tubo) o 2P (dos módulos en vertical).",
                    "Estructuras accionadas por motores de corriente continua sin escobillas y reductores de corona sinfín (slewing drives)."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL ALGORITMO DE BACKTRACKING",
                "titulo": "Protección contra Sombra Propia",
                "puntos": [
                    "A primeras horas de la mañana y últimas de la tarde, el seguidor 'des-sigue' el sol hacia una posición más horizontal.",
                    "Elimina sombras inter-filas a expensas de un ángulo de incidencia ligeramente subóptimo (coseno de pérdida menor que la pérdida de bypass).",
                    "Seguidores inteligentes basados en IA ('Smart Trackers') ajustan el ángulo en días nublados para capturar la máxima radiación difusa zenital."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Modelado de Pérdidas Fotovoltaicas: Ensuciamiento (Soiling), Mismatch y Clipping",
        "objetivo": "Cuantificar el balance secuencial de pérdidas de energía desde la irradiancia global horizontal (GHI) hasta la inyección neta a la red mediante el diagrama de cascada de Sankey de PVsyst.",
        "concepto_clave_latex": r"E_{AC} = GHI \cdot PR \cdot \frac{P_{nom,STC}}{G_{STC}} \quad ; \quad PR = (1 - L_{soiling})(1 - L_{IAM})(1 - L_{temp})(1 - L_{ohmic})(1 - L_{inv}) \dots",
        "ejemplo": "Problema 1: En una planta fotovoltaica en La Guajira, el polvo desértico y partículas de sal marina se depositan sobre los módulos sin lluvia durante 4 meses, generando una tasa de ensuciamiento acumulada del $0.25\\%$/día. Al cabo de 60 días sin limpieza, la pérdida por soiling es $L_{soiling} = 15\\%$. Si la planta genera nominalmente $100\\text{ MWh/día}$, la energía perdida por suciedad es de $15\\text{ MWh/día}$ ($~1200\\text{ USD/día}$ de lucro cesante a 80 USD/MWh). El costo de una pasada de limpieza robotizada en seco es de 4000 USD. El modelo de optimización económica dicta realizar la limpieza cada 22 días para maximizar la rentabilidad neta. Problema 2: En horas pico de máxima radiación (GHI $> 1100\\text{ W/m}^2$), un ratio DC/AC de 1.35 satura la potencia máxima del inversor provocando 'inverter clipping', disipando un $1.2\\%$ de la energía anual pero abaratando la infraestructura de conexión.",
        "bloque_sugerido": "Simulación PVsyst 45 min • Árbol de pérdidas detallado y tasa de ensuciamiento estacional",
        "slides": [
            {
                "numero": 1,
                "seccion": "CASCADA DE PÉRDIDAS",
                "titulo": "Del Fotón al Megavatio AC",
                "puntos": [
                    "Pérdidas Ópticas: Ensuciamiento (soiling, $2 - 10\\%$), reflexión por ángulo de incidencia (IAM, $1.5 - 3\\%$), sombreado de horizonte y cercano ($1 - 4\\%$).",
                    "Pérdidas de Conversión en Celda: Efecto térmico de temperatura ($8 - 14\\%$ en climas cálidos), baja irradiancia ($0.5 - 1.5\\%$).",
                    "Pérdidas de Circuito Eléctrico: Desajuste de módulos (mismatch, $1 - 2\\%$), cableado DC ($1 - 1.5\\%$), degradación LID/PID ($0.5 - 1\\%$).",
                    "Pérdidas de Conversión AC: Rendimiento del inversor ($1.5 - 2\\%$), clipping ($0.5 - 3\\%$), cableado AC y transformador de MT ($1 - 1.5\\%$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "PERFORMANCE RATIO (PR)",
                "titulo": "Indicador Maestro de Calidad",
                "puntos": [
                    "$PR = \\frac{Y_f}{Y_r} = \\frac{E_{AC} / P_{DC,STC}}{H_{POA} / G_{STC}}$.",
                    "Plantas utility-scale bien diseñadas en Colombia alcanzan un PR anual del $78\\%$ al $83\\%$.",
                    "El PR es independiente de la cantidad de sol que haga; mide exclusivamente la eficiencia de la planta para transformar el recurso disponible."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Sistemas de Almacenamiento con Baterías BESS Acopladas en DC y AC",
        "objetivo": "Diseñar la hibridación de parques solares con sistemas de almacenamiento electroquímico de energía (BESS) de iones de litio (LFP / NMC), evaluando acoplamientos DC-coupled vs AC-coupled y funciones de 'energy time-shifting' y 'peak shaving'.",
        "concepto_clave_latex": r"E_{BESS} = P_{descarga} \cdot t_{duracion} \quad [\text{MWh}] \quad ; \quad \text{C-rate} = \frac{I_{carga}}{C_{nom}} \quad ; \quad \eta_{BESS, RTE} \approx 85 - 92\%",
        "ejemplo": "Problema 1: Un parque solar de 10 MWp experimenta restricciones de evacuación de red que limitan su inyección a $P_{max,grid} = 7.0\\text{ MW}$ entre las 11:00 y las 14:00 (recorte de 3 MW pico). Se instala un sistema BESS de 12 MWh con baterías LFP para almacenar el excedente solar recortado y descargarlo entre las 18:00 y las 22:00 durante el pico de precio nocturno. Si la eficiencia round-trip del sistema BESS es $\\eta_{RTE} = 88\\%$, por cada 10 MWh cargados durante el mediodía, el sistema inyecta $8.8\\text{ MWh}$ en la noche. Problema 2: En la arquitectura DC-coupled, las baterías se conectan directamente al bus DC del inversor mediante convertidores DC/DC bidireccionales, evitando la doble conversión DC-AC-DC y capturando la energía de clipping que de otro modo se perdería por saturación del inversor.",
        "bloque_sugerido": "Almacenamiento BESS 45 min • Dimensionamiento de baterías LFP y curvas de ciclado DoD",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURAS DE INTEGRACIÓN BESS",
                "titulo": "DC-Coupled vs AC-Coupled",
                "puntos": [
                    "DC-Coupled: Las baterías comparten el inversor central con el campo solar fotovoltaico; captura energía de recorte ('clipping recapture') con alta eficiencia; menor costo de transformadores.",
                    "AC-Coupled: El sistema BESS tiene sus propios inversores bidireccionales independientes conectados en el lado de media tensión; máxima flexibilidad operativa y modularidad para modernizaciones (retrofit).",
                    "Química dominante: Fosfato de Hierro y Litio ($LiFePO_4$ o LFP) por su estabilidad térmica intrínseca (sin riesgo de embalamiento térmico por oxígeno)."
                ]
            },
            {
                "numero": 2,
                "seccion": "SERVICIOS AUXILIARES AL SISTEMA",
                "titulo": "Aplicaciones de Red del BESS",
                "puntos": [
                    "Firming / Ramp-Rate Control: Suaviza las caídas repentinas de generación solar provocadas por el paso de nubes espesas.",
                    "Frecuencia Rápida (FFR): Respuesta subsegundo para estabilizar frecuencia ante contingencias de red.",
                    "Black-Start: Capacidad de energizar tramos de la red tras un colapso eléctrico total."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Celdas Tándem Perovskita-Silicio: Rompiendo el Límite de Shockley-Queisser",
        "objetivo": "Modelar la división espectral fotónica en celdas solares multiunión tándem de 2 terminales (2T) y 4 terminales (4T), evaluando cómo superan el límite teórico de Shockley-Queisser del silicio cristalino ($29.4\\%$).",
        "concepto_clave_latex": r"\eta_{tandem} = \eta_{top} + \eta_{bottom} > 33\% \quad ; \quad E_{g,top} \approx 1.68 - 1.75\text{ eV} \quad ; \quad E_{g,bottom} = 1.12\text{ eV} \ [\text{Silicio}]",
        "ejemplo": "Problema 1: En una celda tándem monolítica 2T perovskita/silicio, los fotones azules y verdes de alta energía ($h\\nu > 1.7\\text{ eV}$) se absorben en la capa superior de perovskita haluro de plomo ($E_{g1} = 1.70\\text{ eV}$), generando electrones a alta tensión con mínimas pérdidas por termalización. Los fotones rojos e infrarrojos de menor energía ($1.12\\text{ eV} < h\\nu < 1.70\\text{ eV}$) atraviesan la perovskita transparente y son absorbidos por la base inferior de silicio ($E_{g2} = 1.12\\text{ eV}$). En configuración 2T, las dos subceldas están conectadas en serie, por lo que el diseño exige adaptación perfecta de corriente ($J_{top} = J_{bottom} \\approx 20.5\\text{ mA/cm}^2$). Si el voltaje de circuito abierto suma $V_{oc} = 1.25\\text{ V} + 0.72\\text{ V} = 1.97\\text{ V}$ con factor de llenado $FF = 81\\%$, la eficiencia de conversión es: $\\eta = \\frac{1.97 \\times 20.5 \\times 0.81}{100} \\times 100\\% = 32.71\\%$ (récord mundial superando ampliamente el silicio puro). Problema 2: En celdas de 4 terminales (4T), ambas celdas son eléctricamente independientes, eliminando la restricción de adaptación de corriente a expensas de requerir el doble de cableado e inversores.",
        "bloque_sugerido": "Física de Semiconductores 45 min • Celdas tándem perovskita y adaptación espectral AM1.5G",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITE DE SHOCKLEY-QUEISSER",
                "titulo": "La Barrera Termodinámica de una Sola Unión",
                "puntos": [
                    "Una celda de unión simple no puede absorber fotones con energía menor a su banda prohibida ($h\\nu < E_g$).",
                    "Para fotones con $h\\nu > E_g$, el exceso de energía $(h\\nu - E_g)$ se disipa instantáneamente en calor por relajación de fonones (pérdida por termalización).",
                    "El límite teórico absoluto para una celda de silicio es del 29.4%; las mejores celdas comerciales de laboratorio rozan ya el 26.8%."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA REVOLUCIÓN DE LA PEROVSKITA",
                "titulo": "Hibridación Tándem",
                "puntos": [
                    "Las perovskitas de haluro metálico poseen una banda prohibida sintonizable químicamente modificando la proporción de iones halógeno ($I, Br$).",
                    "Fabricación económica por deposición química en solución o evaporación en vacío sobre obleas de silicio convencionales.",
                    "Reto principal: Estabilidad a largo plazo frente a humedad, radiación ultravioleta y temperaturas operativas sostenidas ($> 65^\\circ\\text{C}$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Sistemas Fotovoltaicos Flotantes (Floating PV - FPV) en Embalses",
        "objetivo": "Diseñar plantas solares flotantes sobre cuerpos de agua (represas hidroeléctricas, lagunas de tratamiento y ciénagas), evaluando el efecto refrigerante hídrico, anclajes de fondeo y reducción de evaporación.",
        "concepto_clave_latex": r"T_{celda,FPV} = T_{amb} + \left(\frac{G_{POA}}{800}\right)(NOCT_{FPV} - 20) \quad [NOCT_{FPV} < NOCT_{tierra}] \quad ; \quad \Delta E_{refrig} \approx +8 - 12\%",
        "ejemplo": "Problema 1: Una planta solar de 1 MWp en tierra en clima cálido alcanza temperaturas de celda de $T_c = 65^\\circ\\text{C}$ con $G = 1000\\text{ W/m}^2$ a $T_{amb} = 35^\\circ\\text{C}$. Los módulos tienen un coeficiente de temperatura de potencia de $\\gamma = -0.35\\% /^\\circ\\text{C}$. Pérdida por temperatura en tierra: $\\Delta P = -0.35\\% \\times (65 - 25) = -14.0\\%$. La misma planta instalada en una plataforma flotante en el embalse se beneficia del efecto convectivo del agua y brisa constante, reduciendo su temperatura de operación a $T_{c,FPV} = 48^\\circ\\text{C}$ (17 grados más fría). Pérdida térmica en flotante: $\\Delta P_{FPV} = -0.35\\% \\times (48 - 25) = -8.05\\%$. La planta flotante entrega una ganancia neta por refrigeración pasiva de $+5.95\\%$ de potencia adicional continua. Problema 2: En embalses colombianos como Guatapé o Betania, cubrir el $10\\%$ del espejo de agua con FPV evita la evaporación de hasta $12000\\text{ m}^3$ de agua por hectárea al año, reteniendo agua para turbinar en hidroelectricidad.",
        "bloque_sugerido": "Sistemas Flotantes 45 min • Diseño de flotadores HDPE y líneas de anclaje con batimetría variable",
        "slides": [
            {
                "numero": 1,
                "seccion": "SINERGIA HIDRO-SOLAR",
                "titulo": "Ventajas del Emplazamiento Flotante",
                "puntos": [
                    "Cero conflicto por uso del suelo (no compite con agricultura ni áreas urbanas).",
                    "Reducción de evaporación de agua dulce en embalses y mitigación de floraciones de algas invasoras por bloqueo solar parcial.",
                    "Aprovechamiento inmediato de la infraestructura eléctrica existente (subestación y líneas de alta tensión de la central hidroeléctrica)."
                ]
            },
            {
                "numero": 2,
                "seccion": "INGENIERÍA MECÁNICA Y FONDEO",
                "titulo": "Flotadores y Cargas de Viento y Oleaje",
                "puntos": [
                    "Flotadores modulares de polietileno de alta densidad (HDPE) con protección UV para más de 25 años de inmersión continua.",
                    "Sistemas de anclaje elásticos de tensión constante capaces de absorber oscilaciones de nivel de embalse de hasta 20 a 40 metros entre verano e invierno.",
                    "Corrosión ambiental: Uso de acero galvanizado en caliente clase C5-M y tornillería de acero inoxidable marino AISI 316."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Agrovoltaica (Agri-PV): Co-diseño de Cultivos y Estructuras Elevadas",
        "objetivo": "Diseñar proyectos fotovoltaicos que combinan la producción agrícola de alimentos y la generación de energía eléctrica sobre la misma superficie, optimizando la radiación PAR (Photosynthetically Active Radiation).",
        "concepto_clave_latex": r"\text{LER} = \frac{Y_{agri,AgriPV}}{Y_{agri,mono}} + \frac{Y_{pv,AgriPV}}{Y_{pv,mono}} > 1.4 \quad ; \quad \text{PAR} = \int_{400\text{ nm}}^{700\text{ nm}} I(\lambda) d\lambda \ [\mu\text{mol}/(\text{m}^2\text{s})]",
        "ejemplo": "Problema 1: En una hectárea agrícola en el valle del río Magdalena, un monocultivo de café o cacao produce un rendimiento de $100\\%$ ($Y_{agri,mono}$), mientras que una hectárea dedicada exclusivamente a energía solar produce $100\\%$ de electricidad ($Y_{pv,mono}$). Se implementa un sistema Agrovoltaico elevado a 4.5 metros con módulos semitransparentes espaciados: la cosecha de café alcanza el $85\\%$ de la producción agrícola tradicional (al verse protegida del estrés térmico extremo y quemaduras solares), mientras que los paneles solares generan el $75\\%$ de la energía de un parque estándar. Calcular el Coeficiente de Equivalencia de Tierra (Land Equivalent Ratio, LER): $\\text{LER} = 0.85 + 0.75 = 1.60$. Esto significa que se requerirían 1.6 hectáreas de tierra separada para obtener la misma cantidad combinada de alimentos y energía, logrando un $60\\%$ de incremento en la productividad global del suelo. Problema 2: En cultivos como bayas y hortalizas, la sombra parcial reduce la demanda de agua de riego por evapotranspiración en un $20\\% - 30\\%$.",
        "bloque_sugerido": "Agroenergía 40 min • Espectro PAR, fotoselección y estructuras agrícolas para paso de tractores",
        "slides": [
            {
                "numero": 1,
                "seccion": "COMPARTICIÓN DE LA LUZ",
                "titulo": "Sinergia Alimentos-Energía",
                "puntos": [
                    "La fotosíntesis vegetal satura a niveles de irradiancia moderados; el exceso de radiación solar tropical estresa las plantas y aumenta la transpiración.",
                    "Los paneles fotovoltaicos absorben el excedente de radiación generando ingresos limpios continuos para los agricultores.",
                    "Estructuras elevadas a $4.0 - 5.5\\text{ m}$ permiten el paso cómodo de maquinaria agrícola pesada (tractores y cosechadoras)."
                ]
            },
            {
                "numero": 2,
                "seccion": "TIPOLOGÍAS AGROVOLTAICAS",
                "titulo": "Módulos Elevados vs Verticales Bifaciales",
                "puntos": [
                    "Paneles elevados con seguimiento dinámico inteligente que prioriza sombra durante el mediodía y luz matutina para el cultivo.",
                    "Vallas solares verticales bifaciales orientadas Este-Oeste: Ocupan menos del 2% del área del suelo, sirviendo como barreras cortavientos y generando picos de potencia en la mañana y tarde.",
                    "Marco de licenciamiento socialmente responsable para proyectos de transición energética justa."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Fotovoltaica Integrada en Edificaciones (BIPV): Fachadas y Vidrios Solares",
        "objetivo": "Modelar la integración arquitectónica de elementos fotovoltaicos como materiales constructivos estructurales (Building-Integrated Photovoltaics), calculando el balance energético nexo nZEB.",
        "concepto_clave_latex": r"U_{vidrio,BIPV} \le 1.1\ \frac{\text{W}}{\text{m}^2\text{K}} \quad ; \quad \text{SHGC} \le 0.25 \quad ; \quad \text{VLT} \approx 20 - 40\%",
        "ejemplo": "Problema 1: Un edificio corporativo en Barranquilla instala $800\\text{ m}^2$ de fachada ventilada BIPV de doble acristalamiento con celdas solares de silicio embebidas (eficiencia del $16\\%$, potencia total $128\\text{ kWp}$). La fachada recibe una radiación vertical de $3.8\\text{ kWh/(m}^2\\text{día)}$. La generación eléctrica diaria es: $E = 800 \\times 3.8 \\times 0.16 \\times 0.78 = 379.4\\text{ kWh/día}$ (138.5 MWh anuales). Simultáneamente, el vidrio solar tiene un coeficiente de ganancia de calor solar bajo ($\text{SHGC} = 0.22$), bloqueando el $78\\%$ del calor solar radiativo hacia el interior del edificio. Esta reducción de carga térmica ahorra $190\\text{ kWh/día}$ adicionales en el consumo eléctrico de los chillers de climatización. Beneficio neto combinado: $379.4 + 190 = 569.4\\text{ kWh/día}$. Problema 2: A diferencia de los paneles adosados BAPV (Building-Applied), los componentes BIPV deben cumplir estrictas normas de seguridad estructural de construcción (resistencia al fuego clase A, impacto de granizo y aislamiento acústico según norma EN 50583).",
        "bloque_sugerido": "Arquitectura Bioclimática 45 min • Diseño de edificios nZEB con fachadas solares BIPV",
        "slides": [
            {
                "numero": 1,
                "seccion": "MATERIAL CONSTRUCTIVO MULTIFUNCIONAL",
                "titulo": "Más que un Panel Solar",
                "puntos": [
                    "BIPV cumple simultáneamente funciones constructivas básicas: Estanqueidad al agua, aislamiento térmico/acústico, soporte de cargas de viento y estética arquitectónica.",
                    "Sustituye materiales convencionales costosos (vidrio muro cortina, paneles de aluminio compuesto, tejas cerámicas).",
                    "Convierte las envolventes verticales y techos de las ciudades en centrales generadoras distribuidas 'in situ'."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTROL SOLAR Y CONFORT",
                "titulo": "Propiedades Ópticas y Térmicas",
                "puntos": [
                    "Transmitancia Visual (VLT): Permite el paso de luz natural diurna reduciendo el consumo de iluminación artificial interior.",
                    "Coeficiente de Ganancia Solar (SHGC): Minimiza el efecto invernadero en rascacielos acristalados.",
                    "El espacio de ventilación trasero en fachadas de doble piel evacúa el calor por convección natural de chimenea, enfriando las celdas."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Termografía Infrarroja (IR) y Detección de Puntos Calientes (Hot Spots)",
        "objetivo": "Inspeccionar fallas térmicas en módulos fotovoltaicos según la norma IEC 62446-3 mediante cámaras termográficas montadas en drones autónomos, diagnosticando diodos en corto y roturas de celdas.",
        "concepto_clave_latex": r"\Delta T_{hotspot} = T_{celda,fallo} - T_{modulo,sano} \quad ; \quad \Delta T \ge 10^\circ\text{C} \ [\text{Clase 2}] \quad ; \quad \Delta T \ge 30^\circ\text{C} \ [\text{Clase 3: Crítico}]",
        "ejemplo": "Problema 1: Durante una inspección termográfica aérea con dron con cámara radiométrica calibrada a irradiancia $> 700\\text{ W/m}^2$, se detecta una celda individual en un módulo con una temperatura focalizada de $T_{hotspot} = 88.5^\\circ\\text{C}$, mientras que las celdas circundantes operan uniformemente a $T_{sano} = 46.2^\\circ\\text{C}$. El gradiente térmico es: $\\Delta T = 88.5 - 46.2 = 42.3^\\circ\\text{C} > 30^\\circ\\text{C}$. Se clasifica como un Punto Caliente Severo de Clase 3 (Riesgo Crítico de Incendio y Delaminación de EVA). Causa raíz: Una microfisura interna profunda bloquea la corriente de la celda; al estar en un string en serie, la celda defectuosa pasa de generar energía a disipar la potencia forzada de las otras celdas polarizándose en inversa ($P_{disip} = I_{string}^2 R_{shunt}$). El diodo de bypass correspondiente no actuó por estar averiado en circuito abierto. Se programa el reemplazo inmediato del módulo. Problema 2: Si todo un tercio del módulo aparece uniformemente caliente a $+12^\\circ\\text{C}$, el diagnóstico inequívoco es un diodo de bypass en cortocircuito permanente.",
        "bloque_sugerido": "Inspección O&M 40 min • Vuelos autónomos de drones con termografía IR y visión por computador",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMOGRAFÍA INDUSTRIAL IEC 62446-3",
                "titulo": "Inspección Termográfica No Invasiva",
                "puntos": [
                    "Condiciones ambientales normalizadas de ensayo: Irradiancia solar $> 700\\text{ W/m}^2$, velocidad de viento $< 4\\text{ m/s}$, cielo despejado libre de nubes.",
                    "Emisividad del vidrio solar fijada en $\\varepsilon \\approx 0.85 - 0.90$.",
                    "Ángulo de observación de la cámara entre $50^\\circ$ y $60^\\circ$ para evitar el reflejo directo de la radiación solar y la silueta del operador."
                ]
            },
            {
                "numero": 2,
                "seccion": "PATRONES TÉRMICOS TÍPICOS",
                "titulo": "Catálogo de Anomalías Térmicas",
                "puntos": [
                    "Punto caliente puntual: Microfisura, excremento de pájaro adherido o impacto de proyectil.",
                    "Patrón de tablero de ajedrez ('patchwork'): Desajuste severo por PID o degradación desigual.",
                    "String completo caliente: String desconectado o fusible fundido en la combiner box (sin circulación de corriente).",
                    "Cajas de conexión sobrecalentadas: Mal apriete de terminales o corrosión por penetración de agua."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Electroluminiscencia (EL) y Fotoluminiscencia (PL) en Módulos Fotovoltaicos",
        "objetivo": "Diagnosticar microfisuras invisibles, fallas de soldadura y roturas de dedos colectores mediante la emisión óptica infrarroja inducida por inyección de corriente eléctrica en oscuridad (EL).",
        "concepto_clave_latex": r"I_{EL} \propto \exp\left(\frac{q V_j}{k_B T}\right) \quad [\lambda \approx 1150\text{ nm} \text{ en Silicio}] \quad ; \quad \Delta R_s \implies \text{Zonas Oscuras}",
        "ejemplo": "Problema 1: Un lote de módulos solares llega a puerto tras un transporte marítimo con fuertes aceleraciones dinámicas. En la inspección visual exterior, los vidrios frontales no presentan ningún daño aparente. Se somete el módulo a un ensayo de Electroluminiscencia en cámara oscura inyectando su corriente nominal de cortocircuito en polarización directa ($I_{nom} = 13.5\\text{ A}$). Una cámara CCD/CMOS enfriada de silicio modificada para el infrarrojo cercano capta la emisión espontánea a $1150\\text{ nm}$. La imagen de EL revela que 8 celdas presentan fracturas dendríticas completas en cruz ('cross cracks') y dedos metálicos desoldados visibles como zonas negras inactivas sin emisión radiativa. Las fracturas aisladas desconectan el $25\\%$ del área activa de esas celdas, prediciendo una caída de potencia del $12\\%$ y futuros puntos calientes severos en operación. El lote es rechazado formalmente con el informe pericial de EL. Problema 2: En la Fotoluminiscencia (PL), la excitación se induce ópticamente mediante láser sin requerir contacto eléctrico físico, permitiendo inspeccionar obleas en movimiento en la línea de fabricación.",
        "bloque_sugerido": "Control de Calidad 40 min • Análisis de imágenes de electroluminiscencia con redes neuronales",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DE LA ELECTROLUMINISCENCIA",
                "titulo": "El Proceso Fotovoltaico Inverso",
                "puntos": [
                    "La celda solar opera temporalmente como un diodo emisor de luz (LED) infrarrojo muy tenue.",
                    "La inyección de corriente externa fuerza la recombinación radiativa banda a banda de electrones y huecos, emitiendo fotones con longitud de onda correspondiente a la banda prohibida del silicio ($~1150\\text{ nm}$).",
                    "Zonas sanas y bien conectadas emiten un brillo infrarrojo homogéneo brillante; zonas aisladas o fisuradas permanecen completamente negras."
                ]
            },
            {
                "numero": 2,
                "seccion": "AUDITORÍA EN FÁBRICA Y CAMPO",
                "titulo": "Detección Previa a la Instalación",
                "puntos": [
                    "Invaluable para auditorías de aceptación en fábrica (FAT) y peritajes de seguros tras granizadas severas o vendavales.",
                    "Detecta 'marcas de caracol' ('snail trails'), causadas por la penetración de humedad a través de microfisuras que reacciona con la pasta de plata.",
                    "Sistemas móviles de EL para inspección nocturna directa en strings montados en el campo."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelos de Trasposición de Radiación: Isótropo vs Perez y Hay-Davies",
        "objetivo": "Calcular la radiación total incidente sobre una superficie inclinada ($G_{POA}$) a partir de componentes horizontales globales ($GHI$) y difusas ($DHI$), aplicando modelos anisótropos avanzados.",
        "concepto_clave_latex": r"G_{POA} = G_b R_b + G_d \left[ (1 - F_1)\left(\frac{1 + \cos\beta}{2}\right) + F_1 \frac{a}{b} + F_2 \sin\beta \right] + GHI \cdot \alpha \left(\frac{1 - \cos\beta}{2}\right)",
        "ejemplo": "Problema 1: En un plano inclinado a $\\beta = 15^\\circ$ orientado al sur, se mide en plano horizontal: radiación directa normal $DNI = 850\\text{ W/m}^2$, radiación difusa $DHI = 180\\text{ W/m}^2$, altura solar $\\alpha_s = 60^\\circ$ (ángulo cenital $\\theta_z = 30^\\circ$) y ángulo de incidencia sobre el panel $\\theta = 15^\\circ$. El modelo isótropo simple de Liu-Jordan asume que la radiación difusa del cielo es idéntica en todas direcciones: $G_{d,POA} = DHI \\left( \\frac{1 + \\cos 15^\\circ}{2} \\right) = 180 \\left( \\frac{1 + 0.9659}{2} \\right) = 180(0.983) = 176.9\\text{ W/m}^2$. El modelo anisótropo de Perez descompone la bóveda celeste en tres componentes: difusa isotrópica de fondo, brillo circunsolar alrededor del disco solar ($F_1$) y brillo del horizonte ($F_2$). Con coeficientes de brillo de Perez $F_1 = 0.42$ y $F_2 = 0.08$, el modelo de Perez calcula $G_{d,POA} = 212.4\\text{ W/m}^2$ ($+20\\%$ más de difusa). Problema 2: En climas tropicales con alta nubosidad variable como el Caribe colombiano, el modelo de Perez reduce el error de estimación de energía anual en PVsyst a menos del $1.5\\%$.",
        "bloque_sugerido": "Modelos de Radiación 45 min • Implementación de algoritmos de trasposición Perez y Reindl en Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "ANISOTROPÍA DE LA BÓVEDA CELESTE",
                "titulo": "La Realidad del Cielo Difuso",
                "puntos": [
                    "El modelo isótropo de Liu-Jordan (1960) subestima sistemáticamente la radiación difusa incidente en planos inclinados.",
                    "El cielo real presenta brillo circunsolar concentrado alrededor del disco del sol debido a la dispersión hacia adelante de aerosoles (dispersión de Mie).",
                    "Aparece además una franja de abrillantamiento en el horizonte, especialmente pronunciada en cielos despejados."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL MODELO DE RICHARD PEREZ",
                "titulo": "El Estándar de la Industria",
                "puntos": [
                    "Parámetros de entrada: Claridad del cielo ($\\varepsilon$) y brillo del cielo ($\\Delta$) calculados a partir de mediciones empíricas.",
                    "Matriz empírica de coeficientes $F_{ij}$ ajustada a partir de millones de mediciones radiométricas mundiales.",
                    "Obligatorio para la certificación bancable de proyectos fotovoltaicos multi-megavatio."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Integración a Red y Códigos de Red (CREG 060): Control Q(V), P(f) y LVRT",
        "objetivo": "Implementar las funciones de soporte dinámico de red requeridas para plantas solares conectadas al Sistema Interconectado Nacional según la Resolución CREG 060 / CREG 148, modelando curvas $Q(V)$, $P(f)$ y capacidad de soporte ante huecos de tensión (LVRT).",
        "concepto_clave_latex": r"Q(V) = \pm Q_{max} \cdot f(V - V_0) \quad ; \quad \Delta P = -\frac{1}{R_p}\left(\frac{\Delta f}{f_0}\right)P_n \quad ; \quad \text{LVRT: Soportar } V \to 0\% \text{ durante } 150\text{ ms}",
        "ejemplo": "Problema 1: Una planta solar fotovoltaica de 50 MW está conectada a una subestación de 110 kV. Se desata un cortocircuito trifásico en una línea vecina, provocando un hueco de tensión donde el voltaje en el punto de conexión común (PCC) colapsa al $15\\%$ de su valor nominal durante 250 milisegundos. Según el código de red colombiano (CREG 060), los inversores de la planta tienen estrictamente prohibido desconectarse; deben mantenerse conectados (Low-Voltage Ride-Through, LVRT) e inyectar inmediatamente corriente reactiva rápida capacitiva de soporte ($I_Q \\ge 2.0\\ \\Delta V \\cdot I_n$) dentro de los primeros 20 milisegundos para ayudar a sostener la tensión de la red. Superada la falla en 300 ms, la planta debe recuperar su potencia activa previa a una rampa mínima de $20\\% P_n$ por segundo. Problema 2: En condiciones de sobrevoltaje diurno en barras rurales ($V > 1.05\\text{ p.u.}$), la función $Q(V)$ fuerza a los inversores a absorber potencia reactiva inductiva ($Q < 0$), bajando la tensión local dentro de los límites operativos admisibles sin recortar potencia activa.",
        "bloque_sugerido": "Códigos de Red 45 min • Ensayos de cumplimiento CREG 060 y modelos RMS en DigSILENT PowerFactory",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE FUENTE PASIVA A NODO ACTIVO",
                "titulo": "La Evolución de los Códigos de Red",
                "puntos": [
                    "Históricamente, los inversores solares se desconectaban inmediatamente ante cualquier perturbación de red (anti-isla pasivo).",
                    "Con penetraciones solares $> 20\\%$, la desconexión masiva simultánea provocaría el colapso en cascada de todo el país.",
                    "Las plantas modernas deben actuar como centrales síncronas virtuales proporcionando servicios auxiliares de soporte dinámico."
                ]
            },
            {
                "numero": 2,
                "seccion": "CURVAS DE CONTROL AUTÓNOMO",
                "titulo": "Q(V) y Respuesta Inercial Rápida",
                "puntos": [
                    "Control Volt/Var $Q(V)$: Absorbe o inyecta reactivos automáticamente según el perfil de voltaje del punto de conexión.",
                    "Control Frecuencia/Potencia $P(f)$: Reduce generación en sobre-frecuencia ($f > 60.2\\text{ Hz}$) y aporta reserva en sub-frecuencia (si opera en modo de reserva con 'curtailment').",
                    "Verificación y modelado obligatorio en software DigSILENT para conexión al SIN."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Inversores Formadores de Red (Grid-Forming) vs Seguidores (Grid-Following)",
        "objetivo": "Modelar la transición de inversores de fuente de corriente 'Grid-Following' con lazos PLL a inversores formadores de red 'Grid-Forming' basados en oscilador virtual y control droop para redes débiles con baja relación de cortocircuito (SCR).",
        "concepto_clave_latex": r"\text{SCR} = \frac{S_{sc}}{P_{nom,PV}} < 2.0 \ [\text{Red Débil}] \quad ; \quad \omega = \omega_0 - D_p (P - P_0) \quad ; \quad E = E_0 - D_q (Q - Q_0)",
        "ejemplo": "Problema 1: En una subestación aislada de La Guajira con una capacidad de cortocircuito de $S_{sc} = 60\\text{ MVA}$, se conecta un parque solar de $40\\text{ MW}$. Calcular la relación de cortocircuito (Short Circuit Ratio, SCR): $\\text{SCR} = \\frac{60}{40} = 1.5 < 2.0$. Se trata de una red extremadamente débil. Un inversor convencional Grid-Following basado en lazo de enganche de fase (PLL) pierde el sincronismo debido a las oscilaciones angulares inducidas por variaciones de carga, entrando en resonancia subsíncrona y disparando protecciones. Solución: Se programan inversores Grid-Forming (GFM) que operan como fuentes ideales de tensión detrás de una reactancia, fijando su propio voltaje y frecuencia interna mediante emulación de máquina síncrona virtual (VISMA / Droop Control), garantizando operación estable sin depender de la rigidez de la red externa. Problema 2: Los inversores Grid-Forming aportan inercia sintética verdadera instantánea durante los primeros milisegundos de una perturbación.",
        "bloque_sugerido": "Control Avanzado de Inversores 45 min • Lazos PLL vs Control Droop de Inversores Formadores de Red",
        "slides": [
            {
                "numero": 1,
                "seccion": "GRID-FOLLOWING vs GRID-FORMING",
                "titulo": "Fuente de Corriente vs Fuente de Tensión",
                "puntos": [
                    "Grid-Following (GFL): Mide el voltaje de la red con un PLL e inyecta corrientes sincronizadas con el ángulo medido; requiere una red preexistente rígida y estable.",
                    "Grid-Forming (GFM): Fija autónomamente la amplitud y frecuencia de tensión interna; puede energizar una red completamente muerta (capacidad de Black-Start).",
                    "Imprescindible para alcanzar penetraciones del 100% de energías renovables sin generadores térmicos encendidos."
                ]
            },
            {
                "numero": 2,
                "seccion": "EMULACIÓN DE MÁQUINA SÍNCRONA",
                "titulo": "Sincronización Inercial Virtual",
                "puntos": [
                    "Implementa digitalmente la ecuación de oscilación de rotor: $J_{virt} \\frac{d\\omega}{dt} = T_m - T_e - D\\Delta\\omega$.",
                    "Responde físicamente ante caídas de frecuencia entregando energía cinética virtual almacenada en los condensadores DC y baterías BESS.",
                    "Mitiga armónicos de tensión y previene desconexiones en redes con bajo SCR."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Trazado de Curvas I-V en Campo y Normalización STC según IEC 60891",
        "objetivo": "Medir y normalizar curvas características Corriente-Voltaje ($I-V$) y Potencia-Voltaje ($P-V$) de strings en operación real hacia condiciones estándar de medida (STC) aplicando los procedimientos de trasposición de la norma IEC 60891.",
        "concepto_clave_latex": r"I_2 = I_1 + I_{sc} \left(\frac{G_2}{G_1} - 1\right) + \alpha_{Isc}(T_2 - T_1) \quad ; \quad V_2 = V_1 - R_s(I_2 - I_1) - k I_2(T_2 - T_1) + \beta_{Voc}(T_2 - T_1)",
        "ejemplo": "Problema 1: En una auditoría de comisionamiento de una planta fotovoltaica en Valledupar, un trazador de curvas I-V mide un string de 24 módulos bajo condiciones de campo: $G_1 = 820\\text{ W/m}^2$, $T_1 = 52^\\circ\\text{C}$. Mediciones registradas: $I_{sc1} = 11.2\\text{ A}$, $V_{oc1} = 1045\\text{ V}$, $P_{max1} = 8.65\\text{ kW}$. Parámetros de placa STC ($G_2 = 1000\\text{ W/m}^2$, $T_2 = 25^\\circ\\text{C}$): $\\alpha_{Isc} = +0.045\\% /^\\circ\\text{C} = +0.00504\\text{ A/}^\\circ\\text{C}$, $\\beta_{Voc} = -0.27\\% /^\\circ\\text{C} = -2.82\\text{ V/}^\\circ\\text{C}$. Aplicando el Procedimiento 1 de la norma IEC 60891: Corriente corregida a STC: $I_{sc2} = 11.2 + 11.2\\left(\\frac{1000}{820} - 1\\right) + 0.00504(25 - 52) = 11.2 + 11.2(0.2195) - 0.136 = 11.2 + 2.458 - 0.136 = 13.52\\text{ A}$. Voltaje corregido a STC: $V_{oc2} = 1045 - 2.82(25 - 52) = 1045 - (-76.14) = 1121.14\\text{ V}$. Potencia normalizada a STC: $P_{STC} = 11.62\\text{ kW}$. Si la potencia nominal contratada era de $12.0\\text{ kWp}$, el string presenta una degradación del $3.17\\%$, dentro de las tolerancias de garantía. Problema 2: Una muesca ('step') en la curva I-V normalizada indica con certeza inequívoca la activación de diodos de bypass por sombreado parcial o desajuste de celdas.",
        "bloque_sugerido": "Metrología Solar 45 min • Trazadores de curvas I-V capacitivos y transposición IEC 60891",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRAZADO DE CURVAS I-V",
                "titulo": "La Huella Digital Eléctrica del Módulo",
                "puntos": [
                    "Carga Electrónica Capacitiva: Carga un condensador interno en milisegundos desde cortocircuito ($I_{sc}, V=0$) hasta circuito abierto ($V_{oc}, I=0$).",
                    "Mide simultáneamente irradiancia coplanar con piranómetro o celda de referencia calibrada y temperatura con sensor PT100/termocupla pegada al dorso.",
                    "Revela la resistencia en serie ($R_s$, pendiente en $V_{oc}$) y la resistencia en paralelo ($R_{sh}$, pendiente en $I_{sc}$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "NORMALIZACIÓN IEC 60891",
                "titulo": "Comparabilidad Rigurosa",
                "puntos": [
                    "Las condiciones reales de sol nunca son exactamente $1000\\text{ W/m}^2$ a $25^\\circ\\text{C}$.",
                    "La transposición matemática según IEC 60891 elimina las distorsiones ambientales para comparar directamente contra la ficha técnica del fabricante.",
                    "Herramienta definitiva para reclamaciones de garantía y recepción formal de obras fotovoltaicas."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Calidad de Energía en Parques Solares: Armónicos, Interarmónicos, Flicker y Filtros LCL",
        "objetivo": "Diseñar filtros de salida LCL para inversores solares y evaluar la distorsión armónica total de corriente ($THD_i$) y voltaje ($THD_v$) según normas IEEE 519 e IEC 61000-4-30.",
        "concepto_clave_latex": r"THD_i = \frac{\sqrt{\sum_{h=2}^\infty I_h^2}}{I_1} \times 100\% \le 5.0\% \quad ; \quad f_{res,LCL} = \frac{1}{2\pi}\sqrt{\frac{L_1 + L_2}{L_1 L_2 C_f}} \quad ; \quad P_{st} \le 1.0",
        "ejemplo": "Problema 1: Un inversor solar trifásico de 250 kW a 480 V conmuta por modulación de ancho de pulso (PWM) a $f_{sw} = 8.0\\text{ kHz}$. Para atenuar los armónicos de alta frecuencia de conmutación se diseña un filtro pasivo LCL con inductor de inversor $L_1 = 120\\ \\mu\\text{H}$, condensador de filtro $C_f = 60\\ \\mu\\text{F}$ e inductor de red $L_2 = 40\\ \\mu\\text{H}$. Calcular la frecuencia de resonancia natural del filtro: Inductancia equivalente: $\\frac{L_1 + L_2}{L_1 L_2} = \\frac{(120 + 40) \\times 10^{-6}}{(120 \\times 10^{-6})(40 \\times 10^{-6})} = \\frac{160 \\times 10^{-6}}{4800 \\times 10^{-12}} = \\frac{160}{4.8 \\times 10^{-6}} = 3.333 \\times 10^7\\text{ H}^{-1}$. Producto con capacitancia: $3.333 \\times 10^7 \\times 60 \\times 10^{-6} = 2000$. Frecuencia de resonancia: $f_{res} = \\frac{\\sqrt{2000}}{2\\pi} = \\frac{44.721}{6.283} = 7.118\\text{ kHz}$. Dado que $10 f_{red} (600\\text{ Hz}) < f_{res} < 0.5 f_{sw} (4000\\text{ Hz})$ no se cumple la regla de diseño recomendada ($f_{res} < 4.0\\text{ kHz}$), existiendo riesgo de amplificación armónica resonante. Se rediseña aumentando $C_f$ a $180\\ \\mu\\text{F}$, reduciendo $f_{res}$ a $4.1\\text{ kHz}$ e incorporando una resistencia de amortiguamiento pasivo $R_d$ en serie con el condensador. Problema 2: En el punto de conexión común, la norma IEEE 519 limita la Distorsión de Demanda Total ($TDD$) a un máximo del $5.0\\%$ para sistemas con relaciones de cortocircuito moderadas ($20 < I_{sc}/I_L < 50$).",
        "bloque_sugerido": "Calidad de Potencia 45 min • Diseño y amortiguamiento de resonancia de filtros LCL en MATLAB/Simulink",
        "slides": [
            {
                "numero": 1,
                "seccion": "PERTURBACIONES ARMÓNICAS",
                "titulo": "Fuentes de Distorsión en Inversores",
                "puntos": [
                    "La conmutación PWM genera bandas laterales de armónicos centradas en múltiplos de la frecuencia portadora ($f_{sw}, 2f_{sw}$).",
                    "Interarmónicos: Frecuencias no enteras generadas por la interacción entre el lazo de seguimiento MPPT y la dinámica de la red.",
                    "Flicker (parpadeo de voltaje): Fluctuaciones de tensión de baja frecuencia ($0.5 - 25\\text{ Hz}$) inducidas por el paso intermitente de nubes."
                ]
            },
            {
                "numero": 2,
                "seccion": "TOPOLOGÍA DEL FILTRO LCL",
                "titulo": "Atenuación de Tercer Orden",
                "puntos": [
                    "Atenúa a una tasa de $-60\\text{ dB/década}$ por encima de la frecuencia de resonancia (frente a los $-20\\text{ dB}$ de un filtro inductivo simple L).",
                    "Permite inductores sustancialmente más pequeños y económicos con menor caída de tensión reactiva a frecuencia fundamental.",
                    "Amortiguamiento pasivo (resistencia de dumping) o activo (retroalimentación de corriente de condensador en el algoritmo de control digital)."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sobredimensionamiento DC/AC (Inverter Loading Ratio - ILR) y Optimización de LCOE",
        "objetivo": "Optimizar la relación entre la potencia pico de paneles solares en continua y la potencia nominal del inversor en alterna ($ILR = P_{DC} / P_{AC}$), minimizando el costo nivelado de la energía (LCOE).",
        "concepto_clave_latex": r"ILR = \frac{P_{DC,STC}}{P_{AC,nom}} \approx 1.25 - 1.45 \quad ; \quad \text{LCOE} = \frac{\text{CAPEX} + \sum_{t=1}^N \frac{\text{OPEX}_t}{(1+r)^t}}{\sum_{t=1}^N \frac{E_{t,AC}}{(1+r)^t}} \ [\text{USD/MWh}]",
        "ejemplo": "Problema 1: Se diseña una planta solar donde la conexión a red está limitada por contrato de transporte a $P_{AC} = 10\\text{ MVA}$. Se simulan dos configuraciones: Caso A con $ILR = 1.05$ ($P_{DC} = 10.5\\text{ MWp}$) y Caso B con $ILR = 1.35$ ($P_{DC} = 13.5\\text{ MWp}$). En el Caso B, durante las horas del mediodía en días soleados el inversor satura a 10 MW y recorta potencia ('clipping loss' anual del $2.8\\%$, equivalente a $680\\text{ MWh}$ perdidos). Sin embargo, durante las primeras 3 horas de la mañana, las 3 horas de la tarde y en todos los días nublados del año, el inversor opera mucho más cerca de su capacidad nominal del 100%, generando $5200\\text{ MWh}$ netos adicionales al año. Como el costo del vatio de panel solar ha caído por debajo de $0.10\\text{ USD/Wp}$ mientras que el transformador de media tensión y la línea de interconexión son costos fijos, el Caso B reduce el LCOE de $38.5\\text{ USD/MWh}$ a $32.8\\text{ USD/MWh}$ (una reducción del $14.8\\%$ en el costo de la energía). Problema 2: En plantas con baterías DC-coupled, el ILR puede elevarse económicamente a $1.60 - 1.80$ derivando toda la energía excedente de clipping hacia las celdas de almacenamiento sin perder un solo kilovatio-hora.",
        "bloque_sugerido": "Economía Solar 45 min • Curvas de sensibilidad de LCOE vs ILR y análisis de clipping",
        "slides": [
            {
                "numero": 1,
                "seccion": "FACTOR DE CARGA DEL INVERSOR",
                "titulo": "Maximizando el Activo de Interconexión",
                "puntos": [
                    "Los paneles solares rara vez operan a su potencia nominal de placa STC debido a temperaturas elevadas de celda ($50 - 65^\\circ\\text{C}$), suciedad y pérdidas angulares.",
                    "Un ratio de $ILR = 1.0$ mantiene al inversor subutilizado al $60-70\\%$ de su capacidad la mayor parte de las horas del día.",
                    "Sobredimensionar la potencia DC 'aplana' y ensancha la curva de generación diurna, entregando un perfil cuadrado continuo de potencia garantizada."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL COMPROMISO DE CLIPPING",
                "titulo": "El Punto Dulce Económico",
                "puntos": [
                    "A medida que el ILR supera 1.40, las pérdidas por recorte de pico ('clipping') aumentan exponencialmente.",
                    "El óptimo tecno-económico ocurre en el punto donde el costo marginal del panel solar adicional es igual al ingreso marginal de la energía adicional vendida en horas matutinas/vespertinas.",
                    "En regiones tropicales con alta componente de radiación difusa, el ILR óptimo se ubica consistentemente entre 1.30 y 1.45."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sistemas de Bombeo Solar Fotovoltaico Autónomo (PV Pumping) sin Baterías",
        "objetivo": "Diseñar sistemas de bombeo de agua con energía solar directa utilizando variadores de frecuencia (VFD) con algoritmo MPPT integrado, calculando la altura manométrica total (TDH) y el volumen diario de agua bombeada.",
        "concepto_clave_latex": r"E_{hidro,diaria} = \rho g V_{agua} \cdot TDH \quad ; \quad P_{bomba} = \frac{\rho g Q \cdot TDH}{\eta_{bomba}} \quad ; \quad V_{tanque} \ge 3 \times V_{diario} \ [\text{Autonomía}]",
        "ejemplo": "Problema 1: Una comunidad rural en las estribaciones de la Sierra Nevada requiere extraer $45\\text{ m}^3/\\text{día}$ de agua subterránea de un pozo profundo para consumo doméstico y riego caprino. El nivel dinámico del pozo está a 55 m y el tanque de almacenamiento elevado se ubica a 15 m sobre el terreno, con pérdidas por fricción en tubería de 4 m (Altura Manométrica Total: $TDH = 55 + 15 + 4 = 74\\text{ m.c.a.}$). La bomba sumergible helicoidal tiene una eficiencia de $\\eta_b = 60\\%$. La radiación solar disponible en las horas sol pico (HSP) es de $5.2\\text{ kWh/(m}^2\\text{día)}$. Energía hidráulica neta diaria: $E_h = \\frac{1000 \\times 9.81 \\times 45 \\times 74}{3600 \\times 1000} = 9.07\\text{ kWh/día}$. Energía eléctrica requerida por la bomba: $E_e = \\frac{9.07}{0.60} = 15.12\\text{ kWh/día}$. Potencia del generador fotovoltaico considerando un factor de seguridad por polvo y temperatura de $F_s = 1.25$: $P_{pv} = \\frac{15.12\\text{ kWh}}{5.2\\text{ h}} \\times 1.25 = 2.908 \\times 1.25 = 3.635\\text{ kWp}$ (se instalan 8 paneles solares de 460 Wp = 3.68 kWp). Problema 2: En lugar de almacenar energía en costosas baterías de ciclo profundo con vida útil de 4 años, se almacena energía en forma de agua en un tanque australiano de $150\\text{ m}^3$ que provee 3.3 días de autonomía durante días lluviosos con cero costo de mantenimiento.",
        "bloque_sugerido": "Sistemas Autónomos 40 min • Curvas características caudal-frecuencia en bombas solares sumergibles",
        "slides": [
            {
                "numero": 1,
                "seccion": "ALMACENAMIENTO DE AGUA VS BATERÍAS",
                "titulo": "La Filosofía del Bombeo Directo",
                "puntos": [
                    "Almacenar agua en tanques elevados de polietileno o concreto es 10 veces más económico y duradero que almacenar electricidad en baterías electroquímicas.",
                    "El variador de frecuencia (VFD) solar adapta la velocidad de giro de la bomba ($n \\propto f$) en función de la irradiancia solar en tiempo real.",
                    "La bomba arranca suavemente a primeras horas de la mañana ($f \\approx 30\\text{ Hz}$) y bombea a máxima capacidad al mediodía ($50 - 60\\text{ Hz}$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "LEYES DE AFINIDAD EN BOMBAS",
                "titulo": "Caudal y Presión Dinámica",
                "puntos": [
                    "Caudal proporcional a la velocidad: $Q \\propto n$.",
                    "Presión proporcional al cuadrado de la velocidad: $H \\propto n^2$.",
                    "Existe una frecuencia mínima de corte ($f_{min} \\approx 30 - 35\\text{ Hz}$) por debajo de la cual la bomba gira pero no es capaz de vencer la columna estática de elevación."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Microrredes Solares Aisladas en Zonas No Interconectadas (ZNI) con Control Droop",
        "objetivo": "Diseñar microrredes fotovoltaicas híbridas diésel-batería para comunidades rurales aisladas en Zonas No Interconectadas (ZNI) sin red eléctrica nacional, aplicando control droop descentralizado $P-f$ y $Q-V$.",
        "concepto_clave_latex": r"f - f_0 = -m_p (P - P_0) \quad ; \quad V - V_0 = -n_q (Q - Q_0) \quad ; \quad \text{RE-Share} = \frac{E_{solar} + E_{BESS}}{E_{total}} \ge 70\%",
        "ejemplo": "Problema 1: En una comunidad pesquera de la Ciénaga Grande de Santa Marta (ZNI) con demanda pico nocturna de 45 kW y consumo diario de $320\\text{ kWh/día}$, se diseña una microrred híbrida compuesta por: Campo solar de 80 kWp, banco de baterías BESS de 180 kWh y un motogenerador diésel de respaldo de 50 kVA. Durante el día, el campo solar abastece el 100% de la carga comunitaria y recarga completamente el banco de baterías. El generador diésel permanece completamente apagado durante el $85\\%$ de las horas del año, operando únicamente como última reserva durante periodos de nubosidad prolongada de más de 2 días. El consumo de combustible diésel subsidiado se reduce de 38,000 galones a menos de 4,500 galones anuales, mitigando derrames de combustible en el ecosistema lagunar y garantizando energía 24/7. Problema 2: El control droop permite que tres inversores de batería de 25 kW compartan la carga en paralelo de forma inalámbrica sin requerir líneas de comunicación física entre ellos basándose únicamente en la frecuencia y tensión del microgrid.",
        "bloque_sugerido": "Microrredes 45 min • Control droop primario y gestión de energía en software HOMER Pro",
        "slides": [
            {
                "numero": 1,
                "seccion": "ELECTRIFICACIÓN EN ZONAS NO INTERCONECTADAS",
                "titulo": "El Reto de la Autosuficiencia Rural",
                "puntos": [
                    "En Colombia, más del 50% del territorio nacional son Zonas No Interconectadas (Amazonía, Orinoquía, costas pacífica y caribe insular).",
                    "Históricamente dependientes de plantas diésel ruidosas y contaminantes con suministro de combustible intermitente de alto costo logístico.",
                    "Las microrredes solares híbridas reducen el costo unitario de generación (LCOE) de más de $0.50\\text{ USD/kWh}$ a menos de $0.18\\text{ USD/kWh}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTROL DROOP DESCENTRALIZADO",
                "titulo": "Compartición de Potencia sin Comunicación",
                "puntos": [
                    "Imita la respuesta inercial de generadores síncronos: Cada inversor reduce ligeramente su frecuencia ante incrementos de potencia activa.",
                    "Elimina el riesgo de falla catastrófica por caída de redes de comunicación de datos entre inversores.",
                    "Control secundario centralizado basado en microcontroladores industriales reajusta el bus de voltaje cada 5 minutos."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Economía Circular y Reciclaje de Módulos Fotovoltaicos al Final de su Vida Útil",
        "objetivo": "Evaluar las rutas de desmantelamiento, delaminación térmica/química y recuperación de materiales estratégicos de alta pureza (plata, silicio de grado solar, cobre, aluminio y vidrio plano) según la directiva WEEE.",
        "concepto_clave_latex": r"\text{Tasa de Recuperación} = \frac{m_{recuperada}}{m_{total,panel}} \ge 85 - 95\% \quad ; \quad \text{Composición Másica: Vidrio } 76\%, \text{ Al } 10\%, \text{ Polímero } 10\%, \text{ Si } 3\%, \text{ Metales } 1\%",
        "ejemplo": "Problema 1: Un parque solar de 100 MWp desmantelado tras 30 años de operación contiene aproximadamente 250,000 módulos solares con una masa de 22 kg cada uno (Masa total de residuos electrónicos: $5500\\text{ toneladas}$). El marco de aluminio representa el $10\\%$ ($550\\text{ toneladas}$) y se desmonta mecánicamente con un $100\\%$ de reciclabilidad. El vidrio representa el $76\\%$ ($4180\\text{ toneladas}$). Mediante un proceso de pirolisis térmica del polímero EVA a $480^\\circ\\text{C}$ seguido de disolución química ácida de contactos, se recuperan $440\\text{ kg}$ de plata pura ($Ag$) y $165\\text{ toneladas}$ de silicio de alta pureza. Sabiendo que la plata representa menos del $0.05\\%$ de la masa del módulo pero aporta más del $45\\%$ de su valor económico residual de reciclaje ($~850\\text{ USD/kg}$), calcular el valor de la plata recuperada: $V_{Ag} = 440 \\times 850 = 374000\\text{ USD}$. Problema 2: Evitar que 5500 toneladas de residuos fotovoltaicos terminen en vertederos previene la lixiviación de trazas de plomo ($Pb$) presente en soldaduras antiguas hacia los acuíferos.",
        "bloque_sugerido": "Sostenibilidad de Materiales 40 min • Procesos de delaminación térmica vs disolución con solventes verdes",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL TSUNAMI DE RESIDUOS SOLARES",
                "titulo": "El Desafío al Año 2050",
                "puntos": [
                    "IRENA estima que para el año 2050 habrá más de 78 millones de toneladas métricas de paneles solares retirados en el mundo.",
                    "Los módulos contienen materiales valiosos de alta intensidad energética cuya extracción primaria es intensiva en emisiones de carbono.",
                    "Directiva europea WEEE impone una tasa mínima obligatoria de valorización y reciclaje del 85% en masa."
                ]
            },
            {
                "numero": 2,
                "seccion": "RUTAS DE RECICLAJE DE ALTO VALOR",
                "titulo": "Downcycling vs Upcycling",
                "puntos": [
                    "Downcycling tradicional: Trituración mecánica bruta para usar como material de relleno de carreteras o aislamiento de construcción de bajo valor.",
                    "Upcycling térmico y químico: Separación del vidrio solar ultra-claro bajo en hierro y recuperación hidrometalúrgica de plata y silicio para nuevas celdas tándem.",
                    "Diseño circular 'Design-for-Recycling': Uso de encapsulantes termoplásticos fácilmente solubles que permiten el desensamble limpio sin químicos tóxicos."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Marco Regulatorio CREG 174 / CREG 030: Autogeneración (AGPE) y Venta de Excedentes",
        "objetivo": "Aplicar el marco normativo colombiano de la Comisión de Regulación de Energía y Gas (CREG) para la autogeneración a pequeña escala (AGPE $\\le 1\\text{ MW}$) y autogeneración a gran escala (AGGE), calculando la liquidación horaria de créditos de energía y excedentes.",
        "concepto_clave_latex": r"\text{ExcedenteTipo1: } Exp \le Imp \implies \text{Crédito a tarifa plena } (CU_v - C_v) \quad ; \quad \text{ExcedenteTipo2: } Exp > Imp \implies \text{Liquidación a Precio de Bolsa}",
        "ejemplo": "Problema 1: Un usuario comercial en Santa Marta (Estrato comercial, operador Air-e) instala un sistema solar fotovoltaico de 100 kWp bajo el esquema AGPE (Resolución CREG 174 de 2021). En un mes típico, el medidor bidireccional registra una importación de red de $12000\\text{ kWh}$ y una exportación de excedentes solares a la red de $8000\\text{ kWh}$. Como los excedentes exportados son menores o iguales a la importación ($8000 \\le 12000$), el 100% de los excedentes se liquidan como Excedentes Tipo 1 (crédito de energía 1 a 1 descontado de la factura). Si la tarifa de energía es $CU = 900\\text{ COP/kWh}$ con un costo de comercialización minorista de $C_v = 80\\text{ COP/kWh}$, el usuario recibe una compensación de: $8000 \\times (900 - 80) = 8000 \\times 820 = 6560000\\text{ COP}$. El usuario solo paga por los $4000\\text{ kWh}$ netos importados más el componente de comercialización de los excedentes intercambiados, reduciendo su factura mensual en más de un $60\\%$. Problema 2: Si el usuario exportara $15000\\text{ kWh}$ (superando su consumo en $3000\\text{ kWh}$), esos 3000 kWh adicionales se clasifican como Excedentes Tipo 2 y el comercializador los paga en dinero en efectivo liquidándolos al precio horario de bolsa de energía de XM.",
        "bloque_sugerido": "Regulación Colombiana 45 min • Liquidación matemática de facturas AGPE y trámite de conexión simplificada",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEY 1715 Y REGULACIÓN CREG 174",
                "titulo": "Democratización de la Energía en Colombia",
                "puntos": [
                    "AGPE (Autogenerador a Pequeña Escala): Capacidad instalada $\\le 1000\\text{ kW}$ (1 MW). Trámite de conexión simplificado en línea ante el Operador de Red (OR).",
                    "Medición bidireccional horaria obligatoria (registro independiente de energía importada y exportada).",
                    "Exención de pago de cargos por respaldo para autogeneradores solares con capacidad menor o igual a su carga contratada."
                ]
            },
            {
                "numero": 2,
                "seccion": "MECANISMO DE LIQUIDACIÓN DE EXCEDENTES",
                "titulo": "Excedentes Tipo 1 vs Tipo 2",
                "puntos": [
                    "Excedentes Tipo 1: Hasta el monto de la energía importada en el mes; se descuentan de la factura al Costo Unitario menos comercialización ($CU - C_v$).",
                    "Excedentes Tipo 2: Los excedentes que superen el consumo total mensual del usuario; se pagan al precio marginal horario de bolsa del mercado mayorista.",
                    "Incentivos tributarios de la Ley 2099: Deducción del 50% de la inversión en el impuesto de renta, depreciación acelerada a 3 años y exclusión de IVA y aranceles."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06021846)
    # Inject before the next subject marker: 06011838
    inject_topics_after('      - codigo: "06011838"', yaml_text)
    print("06021846 Energía Solar Fotovoltaica successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
