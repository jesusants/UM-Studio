# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06011839 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Flujo de Energía en Sistemas Complejos: Diagramas de Sankey y Balances de Masa y Energía",
        "objetivo": "Construir balances macroscópicos de masa y primer principio de la termodinámica en macro-sistemas energéticos industriales representando flujos y degradación mediante diagramas de Sankey rigurosos.",
        "concepto_clave_latex": r"\sum \dot{m}_{in} \left(h_{in} + \frac{V_{in}^2}{2} + g z_{in}\right) + \dot{Q} = \sum \dot{m}_{out} \left(h_{out} + \frac{V_{out}^2}{2} + g z_{out}\right) + \dot{W}_{net}",
        "ejemplo": "Problema 1: Un complejo petroquímico y de refinería recibe una corriente de gas natural de 15 kg/s con un poder calorífico inferior (LHV) de 48 MJ/kg (entrada energética total de 720 MW_th). La planta destina 400 MW_th a hornos de craqueo de etileno con una eficiencia térmica del 82% (pérdidas por chimenea de 72 MW_th), 200 MW_th a una caldera de vapor de alta presión que genera 250 t/h de vapor a 100 bar y 520 °C con eficiencia del 88% (pérdidas de 24 MW_th), y 120 MW_th a una turbina de gas que genera 42 MW de potencia eléctrica (eficiencia eléctrica del 35%, pérdidas en gases de escape de 78 MW_th recuperables). Construir el balance global del complejo: Entradas totales = 720 MW. Energía útil directa = (400 * 0.82) + (200 * 0.88) + 42 = 328 MW_th + 176 MW_th + 42 MW_e = 546 MW útiles. Pérdidas directas al ambiente = 72 + 24 + 78 = 174 MW. Eficiencia de primer principio de la planta: eta_I = 546 / 720 = 75.83%. Al recuperar el calor de escape de la turbina para precalentar agua de alimentación de caldera en un economizador a razón de 55 MW_th recuperados, las pérdidas netas se reducen a 119 MW, incrementando la eficiencia energética global del complejo a (546 + 55) / 720 = 83.47%. Problema 2: En una acería con horno de arco eléctrico de 100 MVA, el balance energético demuestra que el 18% de la energía eléctrica consumida se disipa en los humos de aspiración a 1200 °C, justificando la instalación de un ciclo Rankine orgánico (ORC) de recuperación.",
        "bloque_sugerido": "Sistemas Complejos 45 min • Balances multivariable y diagramas de Sankey industriales",
        "slides": [
            {
                "numero": 1,
                "seccion": "BALANCES INTEGRALES DE ENERGÍA",
                "titulo": "Visualización y Conservación de Flujos",
                "puntos": [
                    "El diagrama de Sankey representa gráficamente los vectores energéticos donde el ancho de cada banda es estrictamente proporcional a la magnitud del flujo en MW.",
                    "Permite identificar de manera inmediata los cuellos de botella térmicos y las mayores fuentes de disipación irreversible hacia la atmósfera.",
                    "Sustenta la auditoría de primer principio requerida por la norma ISO 50001 de gestión energética."
                ]
            },
            {
                "numero": 2,
                "seccion": "REUTILIZACIÓN TÉRMICA",
                "titulo": "Recuperación de Calor Residual (WHR)",
                "puntos": [
                    "Flujos a alta temperatura (> 400 °C) deben priorizarse para generación de energía mecánica o vapor motriz.",
                    "Flujos a temperatura intermedia (150 - 400 °C) son aptos para ciclos Rankine orgánicos o calentamiento de proceso.",
                    "Flujos a baja temperatura (< 150 °C) se destinan a precalentamiento de reactivos o bombas de calor industriales."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Integración Térmica de Procesos: Curvas Compuestas y Temperatura Pinch",
        "objetivo": "Calcular la temperatura de pellizco (Pinch Point) y los objetivos mínimos de servicios auxiliares calientes (QH,min) y fríos (QC,min) en redes térmicas multi-corriente utilizando la metodología de Linnhoff.",
        "concepto_clave_latex": r"\Delta T_{min} = T_h - T_c \quad ; \quad \dot{Q}_{H,min} = \sum \dot{m} c_p (T_{out} - T_{in})_c - \dot{Q}_{rec,max}",
        "ejemplo": "Problema 1: Una planta química dispone de dos corrientes calientes que deben enfriarse y dos frías que deben calentarse, con un salto térmico mínimo admisible Delta_T_min = 10 °C. Corriente C1: 150 °C a 60 °C con capacidad calorífica horaria CP = 20 kW/°C (Delta_H = 1800 kW). Corriente C2: 200 °C a 100 °C con CP = 30 kW/°C (Delta_H = 3000 kW). Corriente F1: 40 °C a 160 °C con CP = 25 kW/°C (Delta_H = 3000 kW). Corriente F2: 80 °C a 180 °C con CP = 35 kW/°C (Delta_H = 3500 kW). Construir el algoritmo de la tabla de intervalos térmicos con temperaturas desplazadas (T*_h = T_h - 5 °C, T*_c = T_c + 5 °C). Ordenando los puntos de corte: {195, 185, 145, 95, 85, 55, 45} °C. Se obtiene la cascada de calor acumulada; el mayor déficit acumulado define el requerimiento de servicio caliente: Q_H,min = 2300 kW. La temperatura de pellizco (Pinch Point) resulta en T_pinch,caliente = 100 °C y T_pinch,frio = 90 °C. El requerimiento de enfriamiento auxiliar resulta en Q_C,min = 1500 kW. Si el proceso no estuviera integrado, requeriría calentar las frías con vapor por 6500 kW y enfriar con agua por 4800 kW; la integración por Análisis Pinch ahorra: Ahorro_calor = (6500 - 2300) / 6500 = 64.6%. Problema 2: Demuestre que transferir calor cruzando el Pinch desde una corriente por encima del Pinch hacia una por debajo aumenta el consumo de servicios auxiliares exactamente en el doble del calor transferido.",
        "bloque_sugerido": "Tecnología Pinch 45 min • Construcción de curvas compuestas y tabla de cascada térmica",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA DE PELLIZCO",
                "titulo": "La Regla de Oro del Análisis Pinch",
                "puntos": [
                    "Por encima del Pinch: El sistema se comporta como un sumidero neto de calor; NO debe enfriarse con servicios fríos auxiliares.",
                    "Por debajo del Pinch: El sistema se comporta como una fuente neta de calor; NO debe calentarse con vapor ni combustible auxiliar.",
                    "NUNCA transferir calor a través del Pinch: Violar esta regla impone penalización doble de consumo de energía primaria."
                ]
            },
            {
                "numero": 2,
                "seccion": "SELECCIÓN DE DELTA T MÍNIMO",
                "titulo": "Compromiso Técnico-Económico (Trade-off)",
                "puntos": [
                    "Un Delta_T_min pequeño maximiza la recuperación energética pero dispara exponencialmente el área de intercambio y el costo de capital CAPEX.",
                    "Un Delta_T_min grande abarata los intercambiadores pero eleva el OPEX por compra de vapor y electricidad de bombeo.",
                    "El óptimo económico para refinerías e industria térmica suele ubicarse entre 10 °C y 20 °C."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Síntesis de Redes de Intercambiadores de Calor (HEN): Reglas de Factibilidad y Bucles",
        "objetivo": "Diseñar redes óptimas de intercambiadores de calor (Heat Exchanger Networks) dividiendo el problema en el Pinch y aplicando reglas de compatibilidad de capacidades caloríficas CP.",
        "concepto_clave_latex": r"CP_{out} \ge CP_{in} \quad [\text{Arriba del Pinch}] \quad ; \quad CP_{in} \ge CP_{out} \quad [\text{Abajo del Pinch}]",
        "ejemplo": "Problema 1: En una red HEN con Pinch en 100 °C / 90 °C, diseñar la red en la zona por encima del Pinch para una corriente caliente C1 (CP = 10 kW/°C, de 150 °C a 100 °C, Delta_H = 500 kW) y dos corrientes frías: F1 (CP = 8 kW/°C, de 90 °C a 140 °C, Delta_H = 400 kW) y F2 (CP = 12 kW/°C, de 90 °C a 130 °C, Delta_H = 480 kW). Regla de factibilidad arriba del Pinch: CP_caliente <= CP_fria para cada emparejamiento individual. Si emparejamos C1 (CP=10) con F1 (CP=8), se viola la condición (10 > 8), lo que generaría un cruce de temperaturas inadmisible (Delta_T < 10 °C). Solución: Emparejar C1 (CP=10) con F2 (CP=12), lo cual es termodinámicamente factible (10 <= 12). C1 se enfría desde 150 °C hasta 100 °C transfiriendo 500 kW a F2. La corriente F2 sube desde 90 °C hasta: T_F2,out = 90 + 500 / 12 = 131.67 °C, satisfaciendo completamente su demanda térmica de 130 °C. La corriente F1 no recibe calor del proceso y se calienta íntegramente con vapor de servicio auxiliar (Q_H = 400 kW). La red resultante respeta estrictamente Delta_T >= 10 °C en todos los puntos de transferencia. Problema 2: En redes con bucles térmicos cerrados (loops), la rotura de bucles y la relajación de Delta_T_min permite eliminar intercambiadores pequeños, reduciendo el número de unidades a N_min = S - 1.",
        "bloque_sugerido": "Diseño HEN 45 min • Algoritmo de emparejamiento por pendientes CP y síntesis de redes",
        "slides": [
            {
                "numero": 1,
                "seccion": "CRITERIOS DE CONEXIÓN",
                "titulo": "División de Corrientes y Compatibilidad",
                "puntos": [
                    "Si el número de corrientes calientes supera al de frías arriba del Pinch, es obligatorio dividir (split) corrientes para satisfacer las reglas de CP.",
                    "Cada emparejamiento en el punto de pellizco debe iniciar con un salto de temperatura exactamente igual a Delta_T_min.",
                    "El número mínimo de unidades de intercambio viene dado por el teorema de Euler de la teoría de grafos: U_min = N_corrientes + N_servicios - 1."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPTIMIZACIÓN DE ÁREA",
                "titulo": "Área Total y Distribución de Presión",
                "puntos": [
                    "La caída de presión permisible (Delta_P) restringe la velocidad del fluido y el coeficiente global de transferencia U.",
                    "Redes bien integradas alcanzan ahorros de combustible del 30% al 60% con periodos de amortización de capital inferiores a 2 años.",
                    "El software Aspen Energy Analyzer automatiza el cálculo de redes complejas con cientos de corrientes."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Sistemas de Cogeneración (CHP): Turbinas de Gas y Calderas de Recuperación (HRSG)",
        "objetivo": "Evaluar el rendimiento termodinámico de plantas de cogeneración de calor y electricidad (Combined Heat and Power) modelando calderas HRSG de un nivel de presión y ciclos topping.",
        "concepto_clave_latex": r"\text{EUF} = \frac{\dot{W}_e + \dot{Q}_u}{\dot{m}_f \cdot \text{LHV}} \quad ; \quad \text{PURPA Efficiency} = \frac{\dot{W}_e + 0.5 \dot{Q}_u}{\dot{m}_f \cdot \text{LHV}} \ge 45\%",
        "ejemplo": "Problema 1: Una industria papelera instala una turbina de gas aeroderivada de 25 MW de potencia eléctrica consumiendo 3800 kg/h de gas natural (LHV = 47.5 MJ/kg, potencia térmica introducida Q_in = 50.14 MW). Los gases de combustión salen de la turbina a un flujo de 68 kg/s y una temperatura de 510 °C (c_p = 1.12 kJ/(kg*K)). Los gases ingresan a una caldera de recuperación de calor (HRSG) para generar vapor saturado a 15 bar (h_g = 2792.2 kJ/kg, h_liq_retorno = 334.9 kJ/kg a 80 °C). Los gases se descargan por la chimenea a 140 °C para evitar condensaciones ácidas de azufre. Calor recuperado en la HRSG: Q_u = dot{m}_gas * c_p * (T_in - T_out) = 68 * 1.12 * (510 - 140) = 68 * 1.12 * 370 = 28179 kW = 28.18 MW_th. Producción de vapor de proceso: dot{m}_v = Q_u / (h_g - h_f) = 28179 / (2792.2 - 334.9) = 28179 / 2457.3 = 11.47 kg/s = 41.28 toneladas/hora. Factor de Utilización Energética (EUF): EUF = (W_e + Q_u) / Q_in = (25.0 + 28.18) / 50.14 = 53.18 / 50.14 = 106.0% (base LHV aparente con calor sensible recuperado; en base estricta = 53.18 / 50.14 -> 94.2% del calor de combustión útil). Eficiencia eléctrica simple: eta_e = 25 / 50.14 = 49.86%. Razón calor/electricidad (C/P ratio): C/P = 28.18 / 25.0 = 1.127. Eficiencia PURPA estándar: PURPA = (25.0 + 0.5 * 28.18) / 50.14 = 39.09 / 50.14 = 77.96% (supera con holgura el límite regulatorio del 45%). Problema 2: En calderas HRSG con post-combustión suplementaria (duct firing), el oxígeno residual en los gases de escape (13-15% O2) permite inyectar gas adicional para duplicar la producción de vapor en picos de demanda.",
        "bloque_sugerido": "Cogeneración Industrial 45 min • Balance termo-mecánico de turbina de gas + HRSG",
        "slides": [
            {
                "numero": 1,
                "seccion": "FUNDAMENTOS DE COGENERACIÓN",
                "titulo": "Ciclos Topping vs Bottoming",
                "puntos": [
                    "Ciclo Topping: El combustible primario produce primero trabajo de alta temperatura (electricidad) y el calor residual abastece los procesos térmicos.",
                    "Ciclo Bottoming: El combustible genera calor de muy alta temperatura para hornos (cemento, metalurgia) y los gases de escape mueven turbinas de vapor.",
                    "La cogeneración reduce las emisiones de CO2 entre un 30% y un 50% frente a la producción separada de calor y electricidad en red."
                ]
            },
            {
                "numero": 2,
                "seccion": "PARÁMETROS CRÍTICOS EN HRSG",
                "titulo": "Pinch Point y Approach Temperature",
                "puntos": [
                    "Pinch Point en HRSG: Diferencia entre la temperatura del gas a la salida del evaporador y la temperatura de saturación del agua (típicamente 8 - 15 °C).",
                    "Approach Temperature: Diferencia entre la temperatura de saturación y la del agua a la salida del economizador (evita vaporización prematura en tubos).",
                    "Pinch points reducidos maximizan el vapor generado a costa de incrementar el número de filas de tubos y la caída de presión en gases."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ciclos Combinados Gas-Vapor (CCGT): Presiones Múltiples y Rendimiento Exergético",
        "objetivo": "Modelar ciclos combinados de turbina de gas y turbina de vapor de triple presión con recalentamiento, evaluando el incremento de rendimiento hasta el 60-64% y la minimización de destrucciones exergéticas.",
        "concepto_clave_latex": r"\eta_{CC} = \eta_{GT} + \eta_{ST} - \eta_{GT} \cdot \eta_{ST} = \eta_{GT} + (1 - \eta_{GT}) \cdot \eta_{HR} \cdot \eta_{ST}",
        "ejemplo": "Problema 1: Una central de ciclo combinado moderna de 600 MW clase H opera con una turbina de gas que genera 400 MW con una eficiencia térmica eta_GT = 41.5% consumiendo combustible a razón de Q_in = 400 / 0.415 = 963.85 MW_th. Los gases de escape transfieren calor a una HRSG de triple presión (Alta Presión: 130 bar / 565 °C, Media Presión con Recalentamiento: 30 bar / 565 °C, Baja Presión: 5 bar / 240 °C). La eficiencia de recuperación de la HRSG es eta_HR = 84% del calor disponible en gases. El ciclo de vapor bottoming produce 200 MW netos. Eficiencia del ciclo de vapor respecto al calor absorbido: eta_ST = 200 / (963.85 * (1 - 0.415) * 0.84) = 200 / (963.85 * 0.585 * 0.84) = 200 / 473.64 = 42.23%. Eficiencia global neta de la central: eta_CC = (W_GT + W_ST) / Q_in = (400 + 200) / 963.85 = 600 / 963.85 = 62.25%. Ahorro de combustible comparado con generación térmica simple de vapor (eta = 38%): Ahorro = (1/0.38 - 1/0.6225) / (1/0.38) = (2.631 - 1.606) / 2.631 = 38.96%. Problema 2: En la HRSG de triple presión, el escalonamiento de niveles de vapor reduce drásticamente la diferencia de temperatura promedio entre los gases y el agua, disminuyendo la tasa de generación de entropía S_gen por transferencia térmica con gradiente finito.",
        "bloque_sugerido": "Ciclos Térmicos Avanzados 45 min • Termodinámica de ciclos combinados 1P, 2P y 3P",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURA DE CICLO COMBINADO",
                "titulo": "Sinergia de Altas y Bajas Temperaturas",
                "puntos": [
                    "El ciclo Brayton aporta calor a muy alta temperatura (> 1400 °C en cámara de combustión), logrando una alta eficiencia de Carnot.",
                    "El ciclo Rankine rechaza calor a temperatura cercana a la ambiente (30 - 40 °C en condensador de agua/aire).",
                    "La combinación aprovecha un salto térmico total de más de 1350 °C, imposible de gestionar con un único fluido de trabajo."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPTIMIZACIÓN DE NIVELES DE PRESIÓN",
                "titulo": "HRSG de Triple Presión con Recalentamiento",
                "puntos": [
                    "HRSG 1P: Deja escapar calor residual valioso a la chimenea debido a la alta temperatura de saturación del agua a alta presión.",
                    "HRSG 3P: El circuito de baja presión recupera las últimas calorías del gas antes de chimenea, enfriándolo hasta 90-100 °C.",
                    "Las centrales modernas alcanzan eficiencias superiores al 63% en configuración 1x1 o 2x1 con turbinas de gas clase J/H refrigeradas con vapor."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Trigeneración y Sistemas CCHP: Enfriadores por Absorción (LiBr-H2O y NH3-H2O)",
        "objetivo": "Diseñar plantas de trigeneración (Combined Cooling, Heating, and Power) integrando enfriadores por absorción de simple y doble efecto activados térmicamente por calores residuales.",
        "concepto_clave_latex": r"\text{COP}_{abs} = \frac{\dot{Q}_{evap}}{\dot{Q}_{gen} + \dot{W}_{bomba}} \approx \frac{\dot{Q}_{evap}}{\dot{Q}_{gen}} \quad ; \quad \text{COP}_{1E} \sim 0.7 \quad ; \quad \text{COP}_{2E} \sim 1.2",
        "ejemplo": "Problema 1: Un centro de datos (Data Center) con demanda eléctrica crítica constante de 4 MW y una demanda de climatización ininterrumpida de 2800 kW de frío (800 toneladas de refrigeración, TR) a 7 °C instala un motogenerador a gas natural de 4 MW_e (eficiencia eléctrica del 42%, potencia combustible de 9.52 MW_th). El calor recuperado del agua de camisas del motor y de los gases de escape totaliza 3800 kW_th disponibles a 120 °C. Este calor se canaliza a un chiller de absorción de agua-bromuro de litio (H2O-LiBr) de simple efecto con un coeficiente de operación térmico COP_th = 0.74. Capacidad de refrigeración generada por absorción: Q_frio = Q_gen * COP_th = 3800 * 0.74 = 2812 kW de frío (804 TR), cubriendo el 100% de la carga térmica del centro de datos sin consumir electricidad en compresores mecánicos. Si el frío se produjera mediante chillers eléctricos tradicionales con COP_electrico = 4.2, la potencia eléctrica consumida sería: W_chiller_elec = 2800 / 4.2 = 666.7 kW. La trigeneración ahorra 666.7 kW de potencia eléctrica continua, equivalente a 5840 MWh al año. Eficiencia primaria de la trigeneración: PES = (4000 + 2812) / 9520 = 71.55%. Problema 2: En sistemas de refrigeración industrial bajo cero (-20 °C), se emplea el par amoníaco-agua (NH3-H2O), donde el agua actúa como absorbente y el amoníaco como refrigerante volátil requiriendo una columna de rectificación para evitar arrastre de agua al evaporador.",
        "bloque_sugerido": "Trigeneración CCHP 45 min • Modelado termodinámico de ciclos de refrigeración por absorción",
        "slides": [
            {
                "numero": 1,
                "seccion": "CICLOS ACTIVADOS TÉRMICAMENTE",
                "titulo": "Reemplazo del Compresor Mecánico",
                "puntos": [
                    "El compresor eléctrico se sustituye por un absorbedor, una bomba de solución de baja potencia y un generador (desolvedor).",
                    "El consumo de trabajo mecánico se reduce en más del 95% debido al ínfimo volumen específico de los líquidos frente a los vapores.",
                    "Par LiBr-H2O: El agua es el refrigerante; apto exclusivamente para aire acondicionado (> 0 °C) por riesgo de congelamiento.",
                    "Par NH3-H2O: El amoníaco es el refrigerante; permite temperaturas de congelación de hasta -40 °C en la industria alimentaria."
                ]
            },
            {
                "numero": 2,
                "seccion": "EFICIENCIA EN TRIGENERACIÓN",
                "titulo": "Aplanamiento de la Curva de Demanda",
                "puntos": [
                    "En verano la demanda de calefacción cae drásticamente; la trigeneración aprovecha el calor residual para generar frío de climatización.",
                    "Mantiene alta la carga de los motores o turbinas de gas durante todo el año, maximizando el factor de planta del activo de generación.",
                    "Clasifica para incentivos tributarios de eficiencia energética y deducción de renta bajo la Ley 1715 de Colombia."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Bombas de Calor Industriales y Ciclos de Compresión de Vapor de Alta Temperatura (HTHP)",
        "objetivo": "Diseñar bombas de calor industriales de alta temperatura (High Temperature Heat Pumps - HTHP) con refrigerantes de bajo GWP para valorizar calor residual de 40-70 °C elevándolo a vapor de proceso a 120-150 °C.",
        "concepto_clave_latex": r"\text{COP}_{HP} = \frac{\dot{Q}_{cond}}{\dot{W}_{comp}} = \frac{\dot{Q}_{evap} + \dot{W}_{comp}}{\dot{W}_{comp}} \quad ; \quad \text{COP}_{Carnot} = \frac{T_{cond}}{T_{cond} - T_{evap}}",
        "ejemplo": "Problema 1: Una planta de procesamiento de alimentos descarga 30 kg/s de agua tibia de condensadores a 55 °C (328.15 K). Se requiere suministrar agua caliente presurizada a 115 °C (388.15 K) para esterilización, demandando 2500 kW térmicos. Se instala una bomba de calor HTHP operando con refrigerante HFO-1336mzz(Z) (temperatura crítica 171.3 °C, GWP < 2). Suponiendo evaporación a 45 °C y condensación a 125 °C (salto de temperatura Delta_T_lift = 80 K). COP de Carnot teórico: COP_Carnot = (125 + 273.15) / (125 - 45) = 398.15 / 80 = 4.977. Si la bomba de calor alcanza una eficiencia de segunda ley de Carnot de eta_II = 0.52: COP_real = 0.52 * 4.977 = 2.588. Potencia eléctrica consumida por el compresor: W_comp = Q_cond / COP_real = 2500 kW / 2.588 = 966 kW. Calor residual absorbido del efluente: Q_evap = Q_cond - W_comp = 2500 - 966 = 1534 kW. Enfriamiento del agua residual: Delta_T_efluente = Q_evap / (dot{m} * c_p) = 1534 / (30 * 4.18) = 12.2 °C (el agua residual se vierte enfriada a 42.8 °C, cumpliendo normas de vertimiento térmico). Si los 2500 kW térmicos se generaran en caldera de gas natural (eficiencia 85%, costo gas = 0.045 USD/kWh_th): Costo_caldera = 2500 * (0.045 / 0.85) = 132.35 USD/h. Costo_bomba_calor (electricidad = 0.09 USD/kWh_e): Costo_HP = 966 * 0.09 = 86.94 USD/h. Ahorro económico neto: (132.35 - 86.94) * 8000 h/año = 363,280 USD anuales. Problema 2: El uso de ciclos de compresión mecánica de vapor directo (MVR) en evaporadores concentra efluentes comprimiendo el vapor generado para reutilizar su propia entalpía de condensación.",
        "bloque_sugerido": "Electrificación del Calor 45 min • Bombas de calor de alta temperatura y fluidos HFO/CO2",
        "slides": [
            {
                "numero": 1,
                "seccion": "ELECTRIFICACIÓN DEL CALOR INDUSTRIAL",
                "titulo": "Termodinámica del Salto Térmico (Lift)",
                "puntos": [
                    "A diferencia de las resistencias eléctricas (COP = 1.0), las bombas de calor transfieren 2 a 5 veces más energía térmica que la electricidad consumida.",
                    "El COP depende inversamente de la diferencia de temperatura entre fuente y sumidero (Delta_T_lift = T_cond - T_evap).",
                    "Reducir el lift en 5 °C incrementa el COP en aproximadamente un 12% a 15%."
                ]
            },
            {
                "numero": 2,
                "seccion": "REFRIGERANTES DE NUEVA GENERACIÓN",
                "titulo": "Fluidos Naturales y HFOs de Bajo GWP",
                "puntos": [
                    "Ciclos transcríticos de CO2 (R-744): Excelente para calentar agua desde 15 °C hasta 90 °C con gran deslizamiento térmico.",
                    "HFO-1234ze(E) y HFO-1336mzz(Z): Estables a temperaturas superiores a 140 °C con potencial nulo de agotamiento de ozono (ODP=0) y GWP < 2.",
                    "Pilar fundamental para la descarbonización del calor de proceso por debajo de 200 °C en la transición energética."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Redes de Climatización y Calefacción de Distrito (District Heating and Cooling - DHC)",
        "objetivo": "Modelar la hidráulica y termodinámica de redes térmicas distritales de 4ta y 5ta generación (4GDH/5GDH), calculando caídas de presión en ramales mallados y pérdidas térmicas por aislamiento.",
        "concepto_clave_latex": r"\Delta P_f = f \frac{L}{D} \frac{\rho V^2}{2} \quad ; \quad \dot{Q}_{perdida} = \frac{2\pi k_{ins} L}{\ln(D_{ext}/D_{int})} (T_{agua} - T_{suelo})",
        "ejemplo": "Problema 1: Una red de enfriamiento de distrito (District Cooling) en una zona urbana costera distribuye agua helada a 5 °C con retorno a 13 °C (Delta_T = 8 °C) a través de una tubería troncal enterrada de acero preaislado de 400 mm de diámetro interior y L = 1800 m. Flujo másico total = 250 kg/s (potencia de refrigeración transportada Q = dot{m} * c_p * Delta_T = 250 * 4.18 * 8 = 8360 kW = 2377 TR). Densidad rho = 1000 kg/m^3, viscosidad cinemática nu = 1.52 * 10^-6 m^2/s a 5 °C. Velocidad de flujo: V = 250 / (1000 * pi * 0.2^2) = 250 / 125.66 = 1.989 m/s. Número de Reynolds: Re = V * D / nu = 1.989 * 0.4 / (1.52 * 10^-6) = 523,421 (turbulento severo). Rugosidad relativa epsilon/D = 0.045 / 400 = 0.0001125. Factor de fricción de Colebrook: f = 0.0152. Caída de presión en la tubería troncal: Delta_P = 0.0152 * (1800 / 0.4) * (1000 * 1.989^2 / 2) = 0.0152 * 4500 * 1978 = 135,295 Pa = 1.353 bar. Potencia de bombeo con rendimiento de bomba eta_bomba = 0.78: W_bomba = (dot{V} * Delta_P) / eta_bomba = (0.25 m^3/s * 135,295 Pa) / 0.78 = 33,824 / 0.78 = 43.36 kW. Si el aislamiento de poliuretano (k = 0.026 W/(m*K), D_ext = 0.52 m) está enterrado en suelo a 24 °C: Resistencia térmica R = ln(0.52 / 0.40) / (2 * pi * 0.026) = 0.2624 / 0.1634 = 1.606 (m*K)/W. Pérdida térmica por metro: q' = (24 - 5) / 1.606 = 11.83 W/m. Ganancia térmica total en los 1800 m: Q_perdida = 11.83 * 1800 = 21.29 kW (solo el 0.25% de la capacidad de refrigeración transportada, demostrando la alta eficiencia de las redes modernas). Problema 2: En redes de 5ta generación (5GDH/bidireccionales), el agua circula a temperatura ambiente (15-25 °C) sin aislamiento térmico, permitiendo que edificios que requieren frío descarguen calor directamente a la red mientras edificios que requieren calor lo absorben.",
        "bloque_sugerido": "Redes Urbanas 45 min • Hidráulica de redes de distrito y dimensionamiento térmico",
        "slides": [
            {
                "numero": 1,
                "seccion": "EVOLUCIÓN GENERACIONAL DE REDES DHC",
                "titulo": "De Vapor a Redes Neutras de 5ta Generación",
                "puntos": [
                    "1G y 2G: Vapor de alta presión (> 150 °C) o agua a alta temperatura (> 100 °C) con enormes pérdidas de calor y fugas.",
                    "3G y 4G: Agua presurizada a 50-70 °C con tuberías de plástico flexibles preaisladas e integración masiva de biomasa y solar térmica.",
                    "5GDHC: Redes a temperatura no regulada o neutra; cada suscriptor tiene una pequeña bomba de calor que extrae o inyecta calor según necesidad."
                ]
            },
            {
                "numero": 2,
                "seccion": "ECONOMÍA DE ESCALA URBANA",
                "titulo": "Centralización vs Sistemas Distribuidos",
                "puntos": [
                    "Permite emplear fuentes geológicas o marinas inaccesibles a nivel doméstico (Deep Sea Water Air Conditioning - SWAC).",
                    "Aumenta la resiliencia energética de las ciudades y reduce el efecto de isla de calor urbana eliminando condensadores en azoteas.",
                    "La inversión inicial intensiva exige alta densidad lineal de demanda térmica (> 1.5 MWh por metro de zanja al año)."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Almacenamiento Térmico de Energía (TES): Calor Sensible, Latente (PCM) y Termoquímico",
        "objetivo": "Diseñar sistemas de almacenamiento de energía térmica (Thermal Energy Storage) mediante calor sensible en tanques termoclina y calor latente con Materiales de Cambio de Fase (PCM) para desacoplar generación y demanda.",
        "concepto_clave_latex": r"Q_{TES} = \int_{T_1}^{T_m} m c_p dT + m \Delta h_{fus} + \int_{T_m}^{T_2} m c_{p,liq} dT \quad ; \quad \text{Bi} = \frac{h L_c}{k} < 0.1",
        "ejemplo": "Problema 1: Una central termosolar CSP de torre de 110 MW de potencia eléctrica con turbina de vapor (eta = 42%, potencia térmica requerida = 261.9 MW_th) requiere 8 horas de almacenamiento térmico en sales fundidas para generar electricidad continua en horario nocturno (energía térmica requerida E_th = 261.9 * 8 = 2095.2 MWh_th = 7.543 * 10^12 J). Se utiliza una mezcla binaria eutéctica 'Solar Salt' (60% NaNO3, 40% KNO3, calor específico c_p = 1.50 kJ/(kg*K) = 1500 J/(kg*K)). Temperatura del tanque caliente T_caliente = 565 °C; temperatura del tanque frío T_frio = 290 °C (salto de temperatura de almacenamiento Delta_T = 275 °C). Masa total de sales fundidas requerida: M = E_th / (c_p * Delta_T) = (7.543 * 10^12 J) / (1500 J/(kg*K) * 275 K) = (7.543 * 10^12) / (412,500) = 18,286,060 kg = 18,286 toneladas de sal. A una densidad media de 1870 kg/m^3, el volumen de sal es: V_sal = 18,286,060 / 1870 = 9778 m^3. Se dimensionan dos tanques cilíndricos aislados de acero inoxidable de 30 metros de diámetro: Área de base A = pi * 15^2 = 706.85 m^2. Altura de líquido en el tanque: H = 9778 / 706.85 = 13.83 metros (dimensiones estándar comerciales tipo Cerro Dominador). Problema 2: En tanques de agua fría estratificada para acondicionamiento de aire, el número de Froude de entrada (Fr < 1.0) garantiza la estabilidad de la termoclina impidiendo la mezcla turbulenta entre el agua fría a 4 °C y el agua de retorno a 12 °C.",
        "bloque_sugerido": "Almacenamiento Térmico 45 min • Dimensionamiento de tanques de sales fundidas y PCMs",
        "slides": [
            {
                "numero": 1,
                "seccion": "TECNOLOGÍAS DE ALMACENAMIENTO TÉRMICO",
                "titulo": "Sensible, Latente y Termoquímico",
                "puntos": [
                    "Calor Sensible: Almacena energía elevando la temperatura de un medio (agua líquida, rocas, sales fundidas, hormigón térmico).",
                    "Calor Latente (PCM): Aprovecha la entalpía de cambio de fase sólido-líquido a temperatura prácticamente constante (parafinas, sales hidratadas).",
                    "Termoquímico (TCS): Reacciones reversibles (ej. disociación de óxidos metálicos, hidratación de sales) con densidades energéticas 5 a 10 veces mayores."
                ]
            },
            {
                "numero": 2,
                "seccion": "ROL EN LA DESCARBONIZACIÓN",
                "titulo": "Arbitraje y Gestión de Despacho",
                "puntos": [
                    "El almacenamiento térmico es entre un 70% y un 85% más económico en costo nivelado de capacidad (USD/kWh) que las baterías de litio.",
                    "Permite a las plantas solares térmicas operar en base 24/7 y ofrecer inercia síncrona mecánica pura a la red eléctrica.",
                    "Facilita la integración de excedentes solares y eólicos mediante calderas eléctricas de sales (Power-to-Heat)."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Termoeconomía y Análisis Exergoeconómico: Metodología SPECO y Costeo de Exergía",
        "objetivo": "Aplicar la teoría de costeo exergoeconómico SPECO (Specific Exergy Costing) para imputar costos monetarios a corrientes de materia y energía basándose en su contenido exergético real.",
        "concepto_clave_latex": r"\sum \dot{C}_{in} + \dot{Z}_k = \sum \dot{C}_{out} \quad ; \quad \dot{C}_i = c_i \dot{E}x_i \quad ; \quad r_k = \frac{c_{P,k} - c_{F,k}}{c_{F,k}}",
        "ejemplo": "Problema 1: Un compresor de aire industrial accionado por un motor eléctrico opera en estado estacionario. El motor consume 120 kW de electricidad comprada a la red a un costo específico c_e = 0.10 USD/kWh (flujo de costo del combustible exergoeconómico C_F = 120 kW * 0.10 USD/kWh = 12.00 USD/hora). La inversión de capital anualizada, mantenimiento y operación del compresor totaliza Z_k = 2.40 USD/hora. El aire entra con exergía nula Ex_in = 0 kW y sale comprimido a 8 bar con un flujo de exergía útil Ex_out = 72 kW (eficiencia exergética epsilon = 72 / 120 = 60%, destrucción de exergía Ex_D = 48 kW). Ecuación de balance de costos SPECO: C_out = C_in + C_W + Z_k ==> c_out * Ex_out = 0 + 12.00 + 2.40 = 14.40 USD/hora. Costo unitario específico de la exergía de aire comprimido: c_out = 14.40 USD/h / 72 kWh/h = 0.20 USD/kWh_ex. Factor exergoeconómico f_k (peso relativo del costo de capital frente al costo por ineficiencia): Costo de destrucción de exergía C_D = c_F * Ex_D = 0.10 * 48 = 4.80 USD/hora. f_k = Z_k / (Z_k + C_D) = 2.40 / (2.40 + 4.80) = 2.40 / 7.20 = 33.33%. Interpretación ingenieril: Dado que C_D (4.80 USD/h) duplica el costo de amortización Z_k (2.40 USD/h), está plenamente justificado invertir en un compresor más eficiente y de mayor costo inicial para reducir la destrucción exergética. Problema 2: En una turbina de extracción de vapor de una central de cogeneración, la regla SPECO asigna el mismo costo unitario a las corrientes de vapor que abandonan la misma etapa de expansión.",
        "bloque_sugerido": "Termoeconomía 45 min • Metodología SPECO y cálculo del factor exergoeconómico",
        "slides": [
            {
                "numero": 1,
                "seccion": "FUSIÓN DE TERMODINÁMICA Y ECONOMÍA",
                "titulo": "La Moneda de la Calidad Energética",
                "puntos": [
                    "La contabilidad tradicional basada en energía comete el error de valorar igual un joule de calor a 40 °C que un joule de electricidad.",
                    "La termoeconomía asigna costos monetarios a la exergía: la capacidad real de producir trabajo mecánico útil.",
                    "Permite descubrir exactamente qué componente de una planta industrial destruye capital a través de sus ineficiencias térmicas."
                ]
            },
            {
                "numero": 2,
                "seccion": "DIAGNÓSTICO EXERGOECONÓMICO",
                "titulo": "El Factor Exergoeconómico f_k",
                "puntos": [
                    "f_k alto (> 60%): Predomina el costo de capital Z_k; el equipo está sobrediseñado y se deberían buscar alternativas más económicas.",
                    "f_k bajo (< 30%): Predominan las pérdidas por irreversibilidad C_D; el equipo es ineficiente y debe mejorarse tecnológicamente.",
                    "Herramienta decisiva para la optimización y auditoría avanzada de centrales termoeléctricas complejas."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Detección y Asignación de Costos de Ineficiencia en Sistemas Térmicos Complejos",
        "objetivo": "Cuantificar las interacciones entre componentes en plantas de potencia descomponiendo la destrucción de exergía en partes endógenas/exógenas y evitables/inevitables.",
        "concepto_clave_latex": r"\dot{E}x_{D,k} = \dot{E}x_{D,k}^{EN} + \dot{E}x_{D,k}^{EX} = \dot{E}x_{D,k}^{AV} + \dot{E}x_{D,k}^{UN} \quad ; \quad \dot{E}x_{D,k}^{AV,EN}",
        "ejemplo": "Problema 1: En una caldera de central térmica, la destrucción total de exergía es Ex_D,total = 60 MW. Mediante simulaciones del ciclo operando con componentes ideales se determina que la destrucción endógena (causada exclusivamente por las irreversibilidades internas de la combustión y transferencia en la propia caldera) es Ex_D^EN = 48 MW (80%), mientras que la destrucción exógena (inducida por la baja temperatura del agua precalentada proveniente de calentadores regenerativos ineficientes) es Ex_D^EX = 12 MW (20%). Considerando las limitaciones tecnológicas actuales impuestas por los materiales y la cinética química, la destrucción de exergía inevitable en la combustión adiabática con exceso de aire es Ex_D^UN = 38 MW. Por consiguiente, la destrucción de exergía evitable que los ingenieros pueden corregir mediante optimización es: Ex_D^AV = Ex_D,total - Ex_D^UN = 60 - 38 = 22 MW. La porción evitable endógena resulta Ex_D^AV,EN = 16 MW. Si el costo del carbón/gas es c_F = 8.5 USD/GJ_ex (0.0306 USD/kWh_ex), el ahorro monetario máximo teóricamente alcanzable optimizando la caldera es: Ahorro_anual = 16000 kW * 0.0306 USD/kWh * 7500 h/año = 3,672,000 USD anuales. Problema 2: El análisis exergoambiental (Exergoenvironmental Analysis) correlaciona la exergía destruida con los impactos ambientales del análisis de ciclo de vida (LCA) medidos en puntos Eco-indicator 99.",
        "bloque_sugerido": "Análisis Exergético Avanzado 45 min • Descomposición endógena/exógena de irreversibilidades",
        "slides": [
            {
                "numero": 1,
                "seccion": "EXERGÍA AVANZADA",
                "titulo": "Irreversibilidades Propias vs Inducidas",
                "puntos": [
                    "Destrucción Endógena: Ocurre dentro del componente incluso si todos los demás componentes de la planta fuesen 100% perfectos.",
                    "Destrucción Exógena: Es forzada por las ineficiencias y mal diseño de los equipos circundantes conectados a él.",
                    "Evita culpar erróneamente a un componente por fallas estructurales originadas en otra parte del ciclo."
                ]
            },
            {
                "numero": 2,
                "seccion": "POTENCIAL REAL DE MEJORA",
                "titulo": "Parte Evitable vs Inevitable",
                "puntos": [
                    "Destrucción Inevitable: No puede eliminarse debido a limitaciones físicas, cinéticas o de resistencia de materiales existentes.",
                    "Destrucción Evitable: Margen de maniobra tecnológico real sobre el cual deben focalizarse las inversiones de modernización (retrofit).",
                    "Permite fijar metas de descarbonización e inversión de capital con total realismo económico."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Centrales Térmicas Solares de Concentración (CSP): Torre Central y Cilindro-Parabólicos",
        "objetivo": "Calcular la eficiencia óptica, factores de intercepción, pérdidas térmicas por radiación y rendimiento global de conversión en plantas CSP de torre central con helióstatos y colectores cilindro-parabólicos (PTC).",
        "concepto_clave_latex": r"\eta_{opt} = \rho_{refl} \gamma_{int} \tau_{env} \alpha_{rec} \cos\theta \quad ; \quad q_{loss} = \epsilon \sigma (T_{rec}^4 - T_{amb}^4) + h_c (T_{rec} - T_{amb})",
        "ejemplo": "Problema 1: Un campo solar cilindro-parabólico (PTC) cuenta con 100 lazos de colectores con un ancho de apertura de 5.77 m y una longitud total por lazo de 600 m (área total de apertura A = 100 * 5.77 * 600 = 346,200 m^2). La radiación solar directa normal es DNI = 900 W/m^2 (potencia solar incidente directa = 311.58 MW_th). Propiedades ópticas: reflectividad de espejos rho = 0.94, factor de intercepción gamma = 0.96, transmisividad del tubo envolvente de vidrio tau = 0.965, absortividad del recubrimiento selectivo cermet alpha = 0.955, factor de ángulo de incidencia cos(theta) = 0.92. Eficiencia óptica neta: eta_opt = 0.94 * 0.96 * 0.965 * 0.955 * 0.92 = 0.7648 (76.48%). Potencia solar absorbida por el receptor: Q_abs = 311.58 * 0.7648 = 238.30 MW_th. Los tubos absorbedores operan a una temperatura media de T_rec = 390 °C (663.15 K) con pérdidas térmicas totales medidas de 320 W por metro lineal de colector. Pérdidas térmicas totales del campo: Q_loss = 320 W/m * 60,000 m = 19,200,000 W = 19.20 MW_th. Potencia térmica neta transferida al fluido térmico (aceite sintético Therminol VP-1): Q_net = 238.30 - 19.20 = 219.10 MW_th. Eficiencia térmica global del campo solar: eta_campo = 219.10 / 311.58 = 70.32%. Con una turbina de vapor de ciclo Rankine con eta = 37.5%, la potencia eléctrica neta generada es: W_e = 219.10 * 0.375 = 82.16 MW_e. Problema 2: En torres solares centrales con sales fundidas a 565 °C, la concentración geométrica C > 1000 soles reduce drásticamente el área relativa del receptor, minimizando el impacto de las pérdidas por radiación a altas temperaturas.",
        "bloque_sugerido": "Energía Solar Térmica 45 min • Modelado óptico-térmico de colectores PTC y torres centrales",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONCENTRACIÓN DE LA RADIACIÓN SOLAR",
                "titulo": "Sistemas de Foco Lineal vs Puntual",
                "puntos": [
                    "Cilindro-parabólicos (PTC) y Fresnel lineal: Foco lineal con concentración media (30 - 80 soles); temperaturas limitadas a 400 - 450 °C.",
                    "Torres solares centrales y Discos Stirling: Foco puntual con alta concentración (500 - 1500 soles); superan los 565 °C hasta 1000 °C.",
                    "A mayor temperatura de trabajo, mayor es la eficiencia de Carnot de la turbina de generación eléctrica."
                ]
            },
            {
                "numero": 2,
                "seccion": "VENTAJA ESTRATÉGICA EN LA RED",
                "titulo": "Despachabilidad y Estabilidad Inercial",
                "puntos": [
                    "A diferencia de la solar fotovoltaica, la tecnología CSP integra almacenamiento térmico en sales fundidas de costo competitivo.",
                    "Suministra potencia firme durante los picos de consumo nocturnos sin quemar hidrocarburos.",
                    "La turbina de vapor y el alternador síncrono brindan inercia rotacional y soporte de tensión a la red de alta tensión."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelado de Redes de Transporte de Gas Natural y Mezclas con Hidrógeno (Blending)",
        "objetivo": "Resolver las ecuaciones compresibles de flujo en gasoductos en estado estacionario y evaluar el impacto del blending de hidrógeno en la capacidad energética y compresión.",
        "concepto_clave_latex": r"Q_g = C \cdot \frac{T_b}{P_b} \left[ \frac{P_1^2 - P_2^2 - \Delta H_{elev}}{G \cdot T_f \cdot L \cdot Z \cdot f} \right]^{0.5} D^{2.5} \quad ; \quad \text{WI} = \frac{\text{HHV}}{\sqrt{G}}",
        "ejemplo": "Problema 1: Un gasoducto de acero API 5L X70 de longitud L = 80 km y diámetro interior D = 20 pulgadas (0.4953 m) transporta gas natural puro (gravedad específica G = 0.60, peso molecular M = 17.4 kg/kmol, HHV = 39.8 MJ/m^3). Presión de entrada P_1 = 75 bar y de salida P_2 = 45 bar. Con factor de compresibilidad medio Z = 0.85 y f = 0.0125, la capacidad de flujo volumétrico estándar es Q_GN = 450,000 m^3(st)/hora (potencia energética transportada P_E = 450000 * 39.8 MJ/m^3 / 3600 = 4975 MW). Se analiza inyectar una mezcla de hidrógeno verde al 20% en volumen (20% H2, 80% CH4). La nueva gravedad específica de la mezcla cae a: G_mix = 0.80 * 0.60 + 0.20 * (2.016 / 28.96) = 0.48 + 0.0139 = 0.4939. Como el caudal volumétrico es inversamente proporcional a sqrt(G): Q_mix = Q_GN * sqrt(0.60 / 0.4939) = 450,000 * 1.102 = 495,900 m^3/h (aumento del 10.2% en volumen transportado bajo el mismo diferencial de presión). No obstante, el poder calorífico de la mezcla cae porque el H2 tiene menor energía por volumen (HHV_H2 = 12.7 MJ/m^3 vs HHV_CH4 = 39.8 MJ/m^3): HHV_mix = 0.80 * 39.8 + 0.20 * 12.7 = 31.84 + 2.54 = 34.38 MJ/m^3. Nueva potencia energética transportada: P_E,mix = 495,900 * 34.38 / 3600 = 4735.8 MW. Reducción de la capacidad energética transportada: (4975 - 4735.8) / 4975 = 4.81%. El índice de Wobbe cae de WI_GN = 39.8 / sqrt(0.60) = 51.38 a WI_mix = 34.38 / sqrt(0.4939) = 48.92 MJ/m^3 (dentro de los límites de tolerancia de los quemadores comerciales sin requerir modificación). Problema 2: En mezclas con concentraciones de H2 > 30%, el fenómeno de fragilización por hidrógeno (hydrogen embrittlement) acelera la propagación de grietas por fatiga en soldaduras de aceros de alta resistencia.",
        "bloque_sugerido": "Redes de Gas e Hidrógeno 45 min • Ecuación de Weymouth y análisis del índice de Wobbe",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSPORTE COMPRESIBLE",
                "titulo": "Flujo en Gasoductos de Alta Presión",
                "puntos": [
                    "Gobernado por la caída de presión al cuadrado ($P_1^2 - P_2^2$), debido a la variación de densidad con la presión.",
                    "Estaciones de compresión cada 80 - 150 km restituyen la presión motriz consumiendo entre el 3% y 5% del gas transportado.",
                    "El empaque de línea (Linepack) actúa como un sistema de almacenamiento masivo capaz de amortiguar oscilaciones horarias."
                ]
            },
            {
                "numero": 2,
                "seccion": "DESCARBONIZACIÓN POR INYECCIÓN DE H2",
                "titulo": "Límites Técnicos del Blending",
                "puntos": [
                    "Hasta 10-15% en volumen de H2: No exige reemplazo de tuberías ni compresores centrífugos en la mayoría de gasoductos.",
                    "El hidrógeno requiere mayor relación de compresión volumétrica y puede degradar elastómeros y sellos mecánicos.",
                    "La certificación de integridad estructural y monitoreo con 'smart pigs' es obligatoria antes de iniciar inyecciones comerciales."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Despacho Económico y Compromiso de Unidades (Unit Commitment) con Restricciones",
        "objetivo": "Formular y resolver el problema del Despacho Económico con pérdidas de red y el Compromiso de Unidades (UC) mediante optimización lineal entera mixta (MILP).",
        "concepto_clave_latex": r"\min \sum_{t=1}^T \sum_{i=1}^N \left[ F_i(P_{i,t}) u_{i,t} + S_{i,t} + C_{i,t}^{SD} \right] \quad \text{s.t.} \quad \sum P_{i,t} = D_t \quad ; \quad P_i^{min} u_{i,t} \le P_{i,t} \le P_i^{max} u_{i,t}",
        "ejemplo": "Problema 1: Un sistema eléctrico despacha dos generadores térmicos para abastecer una demanda continua de P_D = 700 MW. Las funciones de costo de combustible en USD/hora son: F_1(P_1) = 0.004 P_1^2 + 8.5 P_1 + 450 con límites 100 <= P_1 <= 500 MW; F_2(P_2) = 0.006 P_2^2 + 7.2 P_2 + 600 con límites 100 <= P_2 <= 400 MW. Despreciando pérdidas, la condición de costo marginal idéntico exige: dF_1/dP_1 = dF_2/dP_2 = lambda. Igualando costos marginales: 0.008 P_1 + 8.5 = 0.012 P_2 + 7.2 ==> 0.008 P_1 - 0.012 P_2 = -1.3. Ecuación de balance de potencia: P_1 + P_2 = 700 ==> P_2 = 700 - P_1. Sustituyendo: 0.008 P_1 - 0.012(700 - P_1) = -1.3 ==> 0.008 P_1 - 8.4 + 0.012 P_1 = -1.3 ==> 0.020 P_1 = 7.1 ==> P_1 = 355 MW. Potencia de la segunda unidad: P_2 = 700 - 355 = 345 MW. Ambos despachos respetan sus límites técnicos de potencia mínima y máxima. Costo marginal del sistema: lambda = 0.008 * 355 + 8.5 = 2.84 + 8.5 = 11.34 USD/MWh. Costo total de operación horario: F_total = F_1(355) + F_2(345) = (0.004 * 126025 + 3017.5 + 450) + (0.006 * 119025 + 2484 + 600) = (504.1 + 3467.5) + (714.15 + 3084) = 3971.6 + 3798.15 = 7769.75 USD/hora. Problema 2: En el problema dinámico de Unit Commitment, las restricciones intertemporales de tiempo mínimo de encendido (minimum up time) y tiempo mínimo de apagado (minimum down time) impiden apagar centrales nucleares o de carbón por pocas horas.",
        "bloque_sugerido": "Operación de Sistemas de Potencia 45 min • Algoritmos de despacho económico y formulación MILP",
        "slides": [
            {
                "numero": 1,
                "seccion": "GESTIÓN TÉCNICO-ECONÓMICA DEL SISTEMA",
                "titulo": "Despacho Económico vs Unit Commitment",
                "puntos": [
                    "Despacho Económico (ED): Distribuye la potencia entre los generadores que YA están encendidos para minimizar el costo marginal instantáneo.",
                    "Unit Commitment (UC): Determina el programa óptimo de qué plantas deben encenderse, apagarse o mantenerse en espera a lo largo de 24 a 168 horas.",
                    "El UC es un problema NP-hard formulado como Optimización Lineal Entera Mixta (MILP) resuelto con motores CPLEX o Gurobi."
                ]
            },
            {
                "numero": 2,
                "seccion": "RESTRICCIONES TÉCNICAS REALES",
                "titulo": "Rampas y Reserva Rodante",
                "puntos": [
                    "Límites de rampa (MW/min): Restringen la rapidez con la que una central puede cambiar su potencia de salida.",
                    "Reserva Rodante (Spinning Reserve): Capacidad no utilizada de plantas sincronizadas disponible en segundos ante la salida imprevista de un generador.",
                    "Costos de arranque en frío vs caliente: Encender una caldera desde frío demanda ingentes cantidades de combustible y desgaste térmico."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Flexibilidad Operativa y Acoplamiento Sectorial en Redes Multi-Energéticas (Sector Coupling)",
        "objetivo": "Modelar el acoplamiento bidireccional entre la red eléctrica, la red de gas natural y la red de calor urbano (Energy Hubs) optimizando la flexibilidad del sistema integrado.",
        "concepto_clave_latex": r"\begin{bmatrix} L_e \\ L_h \\ L_g \end{bmatrix} = \begin{bmatrix} c_{ee} & c_{he} & c_{ge} \\ c_{eh} & c_{hh} & c_{gh} \\ c_{eg} & c_{hg} & c_{gg} \end{bmatrix} \begin{bmatrix} P_e \\ P_h \\ P_g \end{bmatrix} \quad ; \quad \mathbf{L} = \mathbf{C} \cdot \mathbf{P}",
        "ejemplo": "Problema 1: Una ciudad costera industrial cuenta con una matriz Energy Hub que consume electricidad de la red (P_e) y gas natural (P_g) para abastecer una demanda simultánea de electricidad L_e = 50 MW y calor distrital L_h = 40 MW_th. La infraestructura de conversión interna consta de una turbina de gas cogeneradora (eta_e = 0.35, eta_h = 0.45) que puede consumir hasta P_g,CHP = 60 MW_th de gas, una caldera de gas auxiliar (eta_caldera = 0.90) y una bomba de calor eléctrica (COP = 3.8). En horas valle nocturnas, la electricidad en el mercado spot cae a c_e = 0.02 USD/kWh debido a excedentes de viento, mientras que el gas natural cuesta c_g = 0.04 USD/kWh. Formular la matriz de acoplamiento C y resolver el despacho óptimo: Dado que el calor producido por bomba de calor cuesta c_calor,HP = 0.02 / 3.8 = 0.00526 USD/kWh_th, mientras que el calor de la caldera de gas cuesta c_calor,caldera = 0.04 / 0.90 = 0.0444 USD/kWh_th, el optimizador decide apagar la caldera y la turbina de gas (P_g = 0), y encender la bomba de calor a máxima potencia: Potencia eléctrica de la bomba de calor: W_HP = 40 MW_th / 3.8 = 10.53 MW_e. Importación eléctrica total de la red: P_e = L_e + W_HP = 50 + 10.53 = 60.53 MW. Costo total horario nocturno: 60.53 * 1000 kW * 0.02 USD/kWh = 1,210.60 USD/h. En horas pico diurnas, cuando la electricidad sube a 0.18 USD/kWh, el hub invierte su operación: la turbina de gas opera a plena carga generando 21 MW_e y 27 MW_th de calor, exportando flexibilidad a la red eléctrica y reduciendo el costo total en un 58%. Problema 2: En sistemas de respuesta a la demanda (Demand Response), el precalentamiento o pre-enfriamiento de la inercia térmica de edificios comerciales absorbe variaciones de frecuencia de red sin perturbar el confort térmico.",
        "bloque_sugerido": "Acoplamiento Sectorial 45 min • Modelado matricial de Energy Hubs multivectoriales",
        "slides": [
            {
                "numero": 1,
                "seccion": "REDES MULTI-ENERGÉTICAS",
                "titulo": "Sinergia entre Vectores (Sector Coupling)",
                "puntos": [
                    "Supera la visión fragmentada donde la electricidad, el gas y el transporte operan como silos independientes.",
                    "El vector térmico y el vector gas ofrecen una capacidad de almacenamiento órdenes de magnitud superior a la red eléctrica.",
                    "Power-to-Heat y Power-to-Gas transforman la sobreproducción eólica o solar en calor o combustibles sintéticos."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA MATRIZ ENERGY HUB",
                "titulo": "Optimización Global de Despacho Multi-Vector",
                "puntos": [
                    "La matriz de conversión relaciona directamente los vectores de entrada con las cargas multi-energéticas finales.",
                    "Los coeficientes de acoplamiento representan las eficiencias y factores de reparto entre los equipos de conversión.",
                    "Permite el arbitraje de precios en tiempo real seleccionando el combustible o vector más económico en cada hora."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Generación Distribuida y Micro-Redes Híbridas (HRES): Despacho con BESS y Renovables",
        "objetivo": "Diseñar y simular micro-redes eléctricas aisladas e interconectadas integrando energía solar fotovoltaica, eólica, generadores diésel y almacenamiento en baterías (BESS) con HOMER Pro.",
        "concepto_clave_latex": r"\text{LCOE} = \frac{\sum_{t=0}^N \frac{I_t + M_t + F_t}{(1+r)^t}}{\sum_{t=0}^N \frac{E_t}{(1+r)^t}} \quad ; \quad \text{RE}_{fraction} = 1 - \frac{\sum E_{fossil}}{\sum E_{demand}}",
        "ejemplo": "Problema 1: Una comunidad rural aislada no interconectada (ZNI) en la región Caribe colombiana demanda una carga pico diurna de 300 kW y una demanda de energía diaria de E_diaria = 3600 kWh/día (promedio horario 150 kW). Se dimensiona un sistema híbrido renovable (HRES) consistente en: 1) Campo solar FV de 400 kW_p (producción anual = 640,000 kWh/año). 2) Aerogenerador de 100 kW (producción anual = 220,000 kWh/año). 3) Banco de baterías de fosfato de hierro y litio (LiFePO4) de 800 kWh útiles con profundidad de descarga DoD = 80% y eficiencia de ciclo round-trip del 92%. 4) Generador diésel de respaldo de 200 kVA (consumo específico 0.28 litros/kWh). Producción renovable anual combinada: E_renov = 640,000 + 220,000 = 860,000 kWh/año. Demanda total anual de la comunidad: E_demanda = 3600 * 365 = 1,314,000 kWh/año. De la energía renovable generada, el 72% se consume directamente o vía baterías (619,200 kWh/año). El déficit restante de energía es cubierto por el generador diésel: E_diesel = 1,314,000 - 619,200 = 694,800 kWh/año. Consumo de combustible diésel: Litros = 694,800 * 0.28 = 194,544 litros/año. Fracción Renovable neta (RE fraction): RE = 619,200 / 1,314,000 = 47.12%. Con el precio del diésel subsidiado transportado a 1.25 USD/litro, el ahorro de combustible diésel atribuible al parque solar y batería es: Ahorro = (1,314,000 * 0.28 - 194,544) * 1.25 = (367,920 - 194,544) * 1.25 = 173,376 * 1.25 = 216,720 USD anuales, amortizando el CAPEX de la instalación en 4.3 años. Problema 2: En micro-redes conectadas a red, el algoritmo de 'Peak Shaving' descarga las baterías BESS durante las horas punta para evitar cobros de demanda máxima por peaje de transmisión.",
        "bloque_sugerido": "Micro-Redes Aisladas 45 min • Dimensionamiento híbrido solar-eólico-baterías con HOMER",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURA DE MICRO-REDES",
                "titulo": "Sistemas Aislados y Resiliencia Local",
                "puntos": [
                    "Una micro-red es un sistema energético confinado capaz de operar conectado a la red principal o en 'modo isla' (islanding).",
                    "El controlador central de micro-red (Microgrid Controller) gestiona la frecuencia y tensión mediante convertidores 'Grid-Forming'.",
                    "Clave para la electrificación rural de las Zonas No Interconectadas (ZNI) en Colombia y América Latina."
                ]
            },
            {
                "numero": 2,
                "seccion": "OPTIMIZACIÓN MULTIOBJETIVO",
                "titulo": "Costo Nivelado (LCOE) vs Confiabilidad",
                "puntos": [
                    "Un sistema 100% renovable puro con baterías puede disparar el LCOE debido a la sobrecapacidad requerida en días nublados consecutivos.",
                    "La inclusión de un generador diésel o de biodiésel de bajo CAPEX que opere solo el 5-10% del año reduce el costo de la energía a la mitad.",
                    "El software HOMER evalúa miles de combinaciones estocásticas identificando la configuración de mínimo costo presente neto (NPC)."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sistemas de Almacenamiento Hidráulico por Bombeo (PHES) a Escala de Red",
        "objetivo": "Calcular la capacidad energética, potencia instalada, eficiencia de ciclo cerrado y tiempos de respuesta de centrales hidroeléctricas reversibles (Pumped Hydro Energy Storage).",
        "concepto_clave_latex": r"E_{PHES} = \rho V g H_{net} \eta_{gen} \quad ; \quad \eta_{round-trip} = \eta_{gen} \cdot \eta_{bomba} \approx 72\% - 82\%",
        "ejemplo": "Problema 1: Un proyecto de central hidroeléctrica reversible (PHES) en circuito cerrado conecta un embalse superior con uno inferior mediante una tubería de carga con caída bruta H_bruta = 450 m y longitud L = 2200 m. El volumen útil almacenable del embalse superior es V = 6,000,000 m^3 (6 hm^3). En modo generación, el caudal turbinado a través de dos turbinas Francis reversibles es Q = 140 m^3/s. Las pérdidas por fricción y accesorios en la conducción hidráulica representan h_f = 18 m (salto neto H_net = 450 - 18 = 432 m). Densidad del agua rho = 1000 kg/m^3. Eficiencia combinada turbina-generador en generación eta_gen = 0.91. Potencia eléctrica entregada a la red en modo turbinado: P_e = rho * g * Q * H_net * eta_gen = 1000 * 9.81 * 140 * 432 * 0.91 = 539,949,000 W = 540 MW. Tiempo de descarga continuo a plena potencia: t_descarga = V / Q = 6,000,000 / 140 = 42,857 segundos = 11.90 horas. Energía total entregada a la red por ciclo completo: E_descarga = 540 MW * 11.90 h = 6426 MWh. En modo bombeo, la central bombea el agua desde el embalse inferior hacia el superior en horas nocturnas con salto de bombeo H_bomba = 450 + 18 = 468 m y eficiencia combinada bomba-motor eta_bomba = 0.88. Energía eléctrica consumida durante el bombeo: E_bombeo = (rho * g * V * H_bomba) / (eta_bomba * 3.6 * 10^9) = (1000 * 9.81 * 6000000 * 468) / (0.88 * 3.6 * 10^9) = (2.754 * 10^13) / (3.168 * 10^9) = 8693 MWh. Eficiencia de ciclo round-trip de la planta: eta_RT = E_descarga / E_bombeo = 6426 / 8693 = 73.92%. Con un diferencial de precio de arbitraje de energía de 90 USD/MWh (compra a 30 USD/MWh en valle solar/eólico y venta a 120 USD/MWh en pico nocturno): Margen económico por ciclo diario: (6426 * 120) - (8693 * 30) = 771,120 - 260,790 = 510,330 USD/día (más de 180 millones de USD anuales). Problema 2: En centrales reversibles modernas, el uso de máquinas síncronas de velocidad variable con convertidores DFIM (Doubly-Fed Induction Machine) permite regular activamente la potencia de bombeo en la red.",
        "bloque_sugerido": "Almacenamiento Hidráulico 45 min • Dimensionamiento de centrales reversibles y arbitraje",
        "slides": [
            {
                "numero": 1,
                "seccion": "ALMACENAMIENTO MASIVO GIGAVATIO-HORA",
                "titulo": "La Batería de Agua del Planeta",
                "puntos": [
                    "El bombeo hidroeléctrico (PHES) representa más del 90% de toda la capacidad de almacenamiento de energía eléctrica mundial instalada.",
                    "Ofrece almacenamiento de larga duración (LDES) de 8 a 24 horas continuas con vida útil superior a los 60 años.",
                    "Circuito Cerrado (Off-river): Embalses artificiales sin conexión a cauces fluviales vivos, minimizando el impacto en ecosistemas acuáticos."
                ]
            },
            {
                "numero": 2,
                "seccion": "SERVICIOS AUXILIARES DE SISTEMA",
                "titulo": "Inercia Síncrona y Arranque en Negro",
                "puntos": [
                    "Aporte de inercia física real y capacidad masiva de arranque autógeno (Black Start) para levantar la red nacional tras un apagón.",
                    "Capacidad de transición de modo bombeo a modo turbinado en menos de 90 a 120 segundos.",
                    "Herramienta crítica para absorber el vertimiento masivo (curtailable power) de parques solares durante el mediodía."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Conversión de Energía a Gas (Power-to-Gas / P2X): Electrólisis, Metanación y Almacenamiento Químico",
        "objetivo": "Modelar plantas P2G (Power-to-Gas) integrando electrolizadores de baja y alta temperatura (PEM, Alcalinos y SOEC) con reactores catalíticos de metanación de Sabatier.",
        "concepto_clave_latex": r"\text{CO}_2 + 4\text{H}_2 \rightleftharpoons \text{CH}_4 + 2\text{H}_2\text{O} \quad ; \quad \Delta H_{298}^\circ = -165.0 \text{ kJ/mol} \quad ; \quad \eta_{P2G} = \frac{\dot{m}_{CH_4} \cdot \text{LHV}_{CH_4}}{\dot{W}_{electrica}}",
        "ejemplo": "Problema 1: Una planta de Power-to-Gas (P2G) instalada junto a un parque eólico marino aprovecha 100 MW de excedentes de electricidad para alimentar un electrolizador PEM (eficiencia de celda del 68% en base HHV, consumo específico de 50 kWh por cada kg de H2 producido). Producción de hidrógeno verde: dot{m}_H2 = 100,000 kW / 50 kWh/kg = 2000 kg/hora (1000 kmol/h de H2). El hidrógeno producido se introduce en un reactor catalítico de metanación termoquímica de Sabatier con lecho fijo de níquel a 350 °C y 15 bar, junto con una corriente purificada de dióxido de carbono capturado de una planta de biogás. La estequiometría de Sabatier exige 1 mol de CO2 por cada 4 moles de H2. Flujo de CO2 requerido: dot{n}_CO2 = 1000 / 4 = 250 kmol/h = 250 * 44 = 11,000 kg/h = 11.0 toneladas/hora de CO2 capturado y neutralizado. Suponiendo una selectividad y conversión del 98%: Producción de metano sintético (SNG): dot{n}_CH4 = 250 * 0.98 = 245 kmol/h = 245 * 16.04 = 3930 kg/h de metano renovable. Con LHV_CH4 = 50.0 MJ/kg (13.89 kWh/kg), la potencia química del gas sintético inyectable a la red es: P_SNG = 3930 * 13.89 kWh = 54,588 kW = 54.59 MW. Eficiencia global Power-to-Methane de la planta: eta_P2M = 54.59 MW / 100 MW = 54.59%. Calor exotérmico de la reacción de Sabatier recuperado a 300 °C: Q_exo = 245,000 mol/h * 165,000 J/mol / 3.6 * 10^9 = 11.23 MW_th. Al utilizar este calor en una red distrital, la eficiencia global de aprovechamiento de la planta se eleva al 65.82%. Problema 2: Los electrolizadores de óxido sólido de alta temperatura (SOEC a 800 °C) reducen el consumo eléctrico a 38-40 kWh/kg de H2 utilizando calor de desecho industrial para vaporizar el agua.",
        "bloque_sugerido": "Power-to-Gas 45 min • Cinética de Sabatier y balances de electrolizadores PEM/SOEC",
        "slides": [
            {
                "numero": 1,
                "seccion": "ALMACENAMIENTO QUÍMICO MOLECULAR",
                "titulo": "Electrólisis y Metanación Catalítica",
                "puntos": [
                    "Permite desacoplar estacionalmente la energía: almacenar excedentes renovables de primavera/verano para consumirlos en invierno.",
                    "El metano sintético (e-metano) es químicamente idéntico al gas natural convencional (drop-in fuel).",
                    "Se transporta y almacena directamente utilizando la red de gasoductos e instalaciones subterráneas de gas existentes."
                ]
            },
            {
                "numero": 2,
                "seccion": "ECONOMÍA CIRCULAR DEL CARBONO",
                "titulo": "Captura y Utilización de Carbono (CCU)",
                "puntos": [
                    "Recicla emisiones biogénicas de plantas de biogás, fermentación o chimeneas industriales evitando fósiles adicionales.",
                    "Sustenta la producción de e-combustibles para la aviación (e-kerosene) y el transporte marítimo (e-metanol).",
                    "El factor crítico de viabilidad económica es acceder a electricidad renovable de bajo costo (< 25 USD/MWh) y alto factor de carga."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Confiabilidad y Seguridad de Redes de Energía: Análisis N-1, LOLP y Confiabilidad Compuesta",
        "objetivo": "Calcular la probabilidad de pérdida de carga (LOLP), la energía esperada no suministrada (EENS) y la seguridad de red N-1 bajo fallas fortuitas en generadores y líneas de transmisión.",
        "concepto_clave_latex": r"\text{LOLP} = \sum_{j} P(C_j) \cdot t_j \quad [\text{días/año}] \quad ; \quad \text{FOR}_i = \frac{\text{FOH}_i}{\text{SH}_i + \text{FOH}_i} \quad ; \quad \text{EENS} = \sum (D_j - C_j) P_j",
        "ejemplo": "Problema 1: Un sistema de potencia aislado tiene una demanda diaria constante de 80 MW durante un año y cuenta con cuatro unidades generadoras térmicas idénticas de 30 MW cada una (capacidad instalada total = 120 MW). La tasa de salidas forzadas fortuitas (Forced Outage Rate - FOR) de cada unidad es p = 0.08, con disponibilidad q = 1 - p = 0.92. Se construye la Tabla de Probabilidad de Capacidad de Salida (COPT) mediante la distribución binomial: 1) Estado 0 unidades fuera (Capacidad disponible = 120 MW > 80 MW, déficit = 0): P_0 = (0.92)^4 = 0.71639. 2) Estado 1 unidad fuera (Capacidad disponible = 90 MW > 80 MW, déficit = 0): P_1 = 4 * (0.08)^1 * (0.92)^3 = 0.24918. 3) Estado 2 unidades fuera (Capacidad disponible = 60 MW < 80 MW, déficit = 20 MW): P_2 = 6 * (0.08)^2 * (0.92)^2 = 0.03250. 4) Estado 3 unidades fuera (Capacidad disponible = 30 MW < 80 MW, déficit = 50 MW): P_3 = 4 * (0.08)^3 * (0.92)^1 = 0.00188. 5) Estado 4 unidades fuera (Capacidad disponible = 0 MW, déficit = 80 MW): P_4 = (0.08)^4 = 0.00004. Pérdida de carga ocurre si fallan 2 o más unidades (capacidad < 80 MW): Probabilidad de déficit: P_falla = P_2 + P_3 + P_4 = 0.03250 + 0.00188 + 0.00004 = 0.03442. Índice LOLP en horas por año: LOLP = 0.03442 * 8760 horas/año = 301.52 horas/año. Energía Esperada No Suministrada (EENS): EENS = [20 MW * 0.03250 + 50 MW * 0.00188 + 80 MW * 0.00004] * 8760 = [0.6500 + 0.0940 + 0.0032] * 8760 = 0.7472 MW * 8760 h = 6545.47 MWh/año. Con un costo de energía no servida (Value of Lost Load - VOLL) de 2500 USD/MWh, el costo social de la no confiabilidad del sistema es de 16,363,675 USD anuales, justificando sobradamente la adición de una quinta unidad de reserva N-1. Problema 2: El criterio de seguridad estática N-1 en redes malladas exige que el disparo imprevisto de cualquier línea de transmisión no sobrecargue los transformadores restantes más allá de su capacidad de emergencia.",
        "bloque_sugerido": "Confiabilidad de Sistemas de Potencia 45 min • Construcción de COPT y cálculo de LOLP/EENS",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROBABILIDAD APLICADA A REDES ELÉCTRICAS",
                "titulo": "Índices Cuantitativos de Adecuación",
                "puntos": [
                    "LOLP (Loss of Load Probability): Mide el número esperado de días u horas al año en que la demanda excede la capacidad de generación disponible.",
                    "El estándar internacional clásico exige un LOLP inferior a '1 día en 10 años' (0.1 días/año = 2.4 horas/año).",
                    "EENS (Expected Energy Not Served): Cuantifica los megavatios-hora reales que no podrán abastecerse, clave para el análisis costo-beneficio."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIO DETERMINÍSTICO N-1",
                "titulo": "Seguridad Operativa y Redundancia",
                "puntos": [
                    "Exige que la red continúe operando de forma segura y sin cortes tras la pérdida intempestiva del elemento más crítico.",
                    "Análisis de Contingencias AC rápido: Evalúa en milisegundos las sobretensiones y sobrecargas ante disparos de interruptores.",
                    "Regulado estrictamente por el CNO (Consejo Nacional de Operación) y XM en el Sistema Interconectado Nacional de Colombia."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Evaluación de Impacto Ambiental y Factores de Emisión Marginales en Redes Eléctricas",
        "objetivo": "Calcular los factores de emisión marginales horarios (MEF) y el balance de ciclo de vida (LCA) de GEI en redes eléctricas con alta penetración renovable.",
        "concepto_clave_latex": r"\text{MEF}_t = \frac{\Delta \text{Emisiones}_t}{\Delta \text{Demanda}_t} \quad \left[\frac{\text{kg CO}_2\text{e}}{\text{MWh}}\right] \quad ; \quad \text{GHG}_{LCA} = \sum_i E_i \cdot \text{EF}_{LCA,i}",
        "ejemplo": "Problema 1: En una red eléctrica regional interconectada, la demanda promedio en horas de la madrugada (02:00 h) es de 4200 MW, cubierta por 2500 MW de hidroeléctricas de pasada (EF = 0 kg/MWh), 1000 MW de eólica (EF = 0 kg/MWh) y 700 MW de una planta termoeléctrica de carbón que actúa como unidad marginal de rampa (consumo específico = 10,200 kJ/kWh, factor de emisión de carbón = 94.6 kg CO2/GJ ==> EF_carbon = 0.965 kg CO2/kWh = 965 kg CO2/MWh). El Factor de Emisión Promedio en la red a esa hora es: AEF = (700 * 965 + 3500 * 0) / 4200 = 675,500 / 4200 = 160.83 kg CO2/MWh. Sin embargo, si una flota de 10,000 vehículos eléctricos decide cargar sus baterías a las 02:00 h incrementando la demanda en Delta_D = 50 MW, la única unidad técnica con capacidad de subir su potencia es la central térmica de carbón. El Factor de Emisión Marginal es: MEF = Delta_Emisiones / Delta_Demanda = (50 MW * 965 kg/MWh) / 50 MW = 965 kg CO2/MWh. Por tanto, calcular el beneficio ambiental de los vehículos usando el factor promedio (160.8 kg/MWh) subestimaría las emisiones reales inducidas en casi 6 veces. A las 12:00 h del mediodía, con saturación y vertimiento de energía solar fotovoltaica, la unidad marginal es el vertimiento renovable (MEF = 0 kg CO2/MWh), demostrando que la carga diurna es infinitamente más limpia. Problema 2: El análisis de ciclo de vida (LCA) 'cuna a tumba' de paneles solares fotovoltaicos revela que sus emisiones integradas oscilan entre 25 y 45 g CO2e/kWh, generadas principalmente durante la purificación del silicio cuarzo a 1800 °C en hornos de arco.",
        "bloque_sugerido": "Sostenibilidad y Emisiones 45 min • Cálculo de factores de emisión marginales horarios MEF",
        "slides": [
            {
                "numero": 1,
                "seccion": "HUELLA DE CARBONO EN SISTEMAS ENERGÉTICOS",
                "titulo": "Factor Promedio vs Factor Marginal",
                "puntos": [
                    "Factor Promedio (AEF): Divide las emisiones totales de la red entre la generación total; útil únicamente para contabilidad de huella corporativa retroactiva.",
                    "Factor Marginal (MEF): Identifica la planta específica que arranca o frena cuando la demanda varía en 1 MWh adicional.",
                    "Cualquier política de eficiencia energética o electrificación de transporte debe evaluarse obligatoriamente con el MEF."
                ]
            },
            {
                "numero": 2,
                "seccion": "ANÁLISIS DE CICLO DE VIDA (LCA)",
                "titulo": "Metodología Cuna-a-Tumba (ISO 14040/44)",
                "puntos": [
                    "Evalúa las emisiones indirectas de fabricación, minería de materiales críticos (litio, cobre, neodimio), transporte y desmantelamiento.",
                    "Tiempo de Retorno de Carbono (Carbon Payback Time): Tiempo que tarda una tecnología limpia en evitar las emisiones emitidas en su propia construcción.",
                    "Los parques eólicos y solares modernos devuelven toda su energía de fabricación en menos de 10 a 14 meses de operación."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelación y Optimización de Redes Multi-Vectoriales usando Grafos Energéticos",
        "objetivo": "Formular el flujo óptimo de energía multi-red (Multi-Energy Optimal Power Flow - ME-OPF) acoplando ecuaciones de flujo DC/AC con las ecuaciones hidráulicas no lineales de gas y calefacción mediante teoría de grafos.",
        "concepto_clave_latex": r"\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad \mathbf{A}_e \mathbf{f}_e = \mathbf{P}_e \quad ; \quad \mathbf{A}_g \mathbf{f}_g = \mathbf{P}_g \quad ; \quad \mathbf{A}_h \mathbf{f}_h = \mathbf{P}_h \quad ; \quad g_k(\mathbf{x}) \le 0",
        "ejemplo": "Problema 1: Un sistema multi-vectorial modelado como un grafo conexo G = (V, E) cuenta con 3 nodos donde coexisten infraestructura eléctrica y de gas natural. Nodo 1: Generador eólico de 80 MW y punto de inyección de gas a 60 bar. Nodo 2: Central de ciclo combinado CCGT (consume gas para generar electricidad) y compresor de gas accionado por motor eléctrico. Nodo 3: Centro de carga con demanda eléctrica L_e = 60 MW y demanda de gas L_g = 40,000 m^3/h. Las matrices de incidencia nodo-arista A_e y A_g describen la topología de las líneas de transmisión y tuberías. Cuando la línea eléctrica directa 1-3 alcanza su límite térmico de transmisión de 45 MW, se produce una congestión de red eléctrica. El despachador multi-vectorial ejecuta el algoritmo ME-OPF: en lugar de encender un generador diésel caro y contaminante en el Nodo 3, inyecta gas adicional en la tubería 1-2, utiliza la central CCGT del Nodo 2 para convertir gas en electricidad local y transporta el resto a través de la línea 2-3 (descongestión indirecta de la red eléctrica mediante la infraestructura de gasoductos). El algoritmo reduce las pérdidas combinadas del sistema en un 18.4% comparado con la operación desacoplada tradicional. Problema 2: En redes de calefacción distrital, el método de las matrices de lazo de grafo permite calcular simultáneamente la distribución no lineal de presiones de agua y la temperatura de llegada a cada subestación considerando el retardo de transporte por velocidad finita.",
        "bloque_sugerido": "Optimización Multi-Red 45 min • Formulación de flujos de carga multi-vector con grafos",
        "slides": [
            {
                "numero": 1,
                "seccion": "TEORÍA DE GRAFOS APLICADA A LA ENERGÍA",
                "titulo": "Topología Unificada de Flujos",
                "puntos": [
                    "Representa cualquier red física (líneas eléctricas, tuberías de vapor, gasoductos, acueductos) mediante matrices de incidencia nodo-arista.",
                    "Aplica las leyes de Kirchhoff generalizadas: conservación de flujo en los vértices y caída de potencial en las aristas.",
                    "Facilita la formulación matemática de problemas complejos de optimización no lineal para solvers computacionales modernos."
                ]
            },
            {
                "numero": 2,
                "seccion": "BENEFICIOS DE LA OPERACIÓN ACOPLADA",
                "titulo": "Descongestión y Redundancia Cruzada",
                "puntos": [
                    "Permite 'eludir' cuellos de botella en la red eléctrica transportando energía a través de la red de gasoductos o redes térmicas.",
                    "Aumenta la resiliencia del suministro urbano ante eventos climáticos extremos o fallas en subestaciones eléctricas.",
                    "Base científica indispensable para el despliegue de las Ciudades Inteligentes (Smart Cities) y Distritos de Energía Neta Cero."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Planificación Energética a Largo Plazo hacia Emisiones Netas Cero: Modelos TIMES y OSeMOSYS",
        "objetivo": "Diseñar planes de transición y expansión de sistemas energéticos a escala país con horizontes a 2050 evaluando trayectorias de costo mínimo hacia la neutralidad de carbono mediante modelos TIMES/OSeMOSYS.",
        "concepto_clave_latex": r"\min \sum_{r,y} \text{DiscountFactor}_{r,y} \cdot \left[ \text{CapitalCost} + \text{FixedCost} + \text{VariableCost} + \text{ImportCost} - \text{SalvageValue} \right]",
        "ejemplo": "Problema 1: Un modelo de optimización energética de horizonte temporal de 30 años (2020 a 2050 en tramos quinquenales) evalúa la trayectoria de expansión de generación eléctrica de Colombia para alcanzar Net-Zero CO2 en 2050 bajo una tasa de descuento social r = 8%. La demanda eléctrica proyectada crece de 75 TWh/año en 2020 a 160 TWh/año en 2050 impulsada por la electrificación del transporte y la industria. En el año 2025, el modelo debe decidir entre instalar 5 GW de parques solares fotovoltaicos (CAPEX = 750 USD/kW, OPEX fijo = 12 USD/kW-año, factor de planta = 22%) o 3 GW de ciclos combinados de gas natural (CAPEX = 900 USD/kW, eficiencia = 60%, costo gas = 5.5 USD/GJ) con una penalización por impuesto al carbono que sube de 5 USD/tCO2 en 2025 a 80 USD/tCO2 en 2040. Función de minimización del Valor Presente Neto (VPN) de costos totales del sistema: A partir de 2030, la trayectoria de costo mínimo descarta toda nueva construcción fósil y fuerza la penetración de 22 GW de energía solar fotovoltaica, 14 GW de eólica marina y terrestre en La Guajira, 4 GW de hidroeléctricas reversibles y 3 GW de almacenamiento térmico CSP. El modelo demuestra que el costo nivelado de transición (LCOE del sistema) se reduce en un 24.6% comparado con el escenario inercial 'Business As Usual', neutralizando 45 millones de toneladas de CO2 anuales para el año 2050. Problema 2: En la metodología OSeMOSYS (Open Source Energy Modelling System), la ecuación de balance de actividad relaciona dinámicamente la extracción de recursos primarios, la transformación en refinerías y centrales, y el consumo final de servicios energéticos por sectores.",
        "bloque_sugerido": "Planificación Energética 45 min • Modelos de optimización de largo plazo TIMES y Net-Zero 2050",
        "slides": [
            {
                "numero": 1,
                "seccion": "MODELACIÓN ENERGÉTICA MACROECONÓMICA",
                "titulo": "Modelos Bottom-up vs Top-down",
                "puntos": [
                    "Modelos Bottom-up (TIMES, MARKAL, OSeMOSYS): Describen explícitamente cientos de tecnologías energéticas con sus costos y eficiencias reales.",
                    "Modelos Top-down (CGE): Modelos macroeconómicos de equilibrio general que evalúan el impacto de las políticas en el PIB, empleo e inflación.",
                    "Permiten a los ministerios y entidades de planeación (UPME en Colombia) formular los Planes de Expansión de Referencia Generación-Transmisión."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA RUTA HACIA EL NET-ZERO 2050",
                "titulo": "Culminación del Ingeniero Energético",
                "puntos": [
                    "Integración holística de termodinámica, electrotecnia, economía, regulación y sostenibilidad ambiental.",
                    "Planifica la sustitución ordenada de combustibles fósiles garantizando la seguridad de abastecimiento y la soberanía energética.",
                    "El egresado de Ingeniería Energética de la Universidad del Magdalena lidera la transformación hacia una matriz limpia y equitativa."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06011839)
    marker = '  - cuatrimestre: 6'
    inject_topics_after(marker, yaml_text)
    print("06011839 Sistemas Energéticos successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
