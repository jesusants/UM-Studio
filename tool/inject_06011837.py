# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_06011837 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Ciclos Combinados Gas-Vapor (CCGT) y Recuperadores de Calor (HRSG)",
        "objetivo": "Modelar termodinámicamente la integración del ciclo Brayton de gas con el ciclo Rankine de vapor mediante generadores de vapor por recuperación de calor (HRSG) de múltiples niveles de presión.",
        "concepto_clave_latex": r"\eta_{CC} = \eta_{GT} + \eta_{ST}(1 - \eta_{GT}) \quad ; \quad \dot{Q}_{HRSG} = \dot{m}_g c_{p,g} (T_{g,in} - T_{g,out}) = \dot{m}_w (h_{sup} - h_{eco,in})",
        "ejemplo": "Problema 1: Una turbina de gas opera con eficiencia térmica del 38% y genera 120 MW eléctricos. Si los gases de escape alimentan un ciclo Rankine con eficiencia del 34%, calcular la eficiencia global del ciclo combinado y la potencia total generada. Eficiencia combinada: $\\eta_{CC} = 0.38 + 0.34(1 - 0.38) = 0.38 + 0.34(0.62) = 0.38 + 0.2108 = 59.08\\%$. Calor suministrado por combustible: $\\dot{Q}_{in} = 120\\text{ MW} / 0.38 = 315.79\\text{ MW}$. Potencia de la turbina de vapor: $\\dot{W}_{ST} = 0.2108 \\times 315.79\\text{ MW} = 66.57\\text{ MW}$. Potencia total: $\\dot{W}_{total} = 120 + 66.57 = 186.57\\text{ MW}$. Problema 2: En el diseño del HRSG, el 'pinch point' representa la mínima diferencia de temperatura entre los gases de combustión y el agua saturada en el evaporador (típicamente $8 - 15^\\circ\\text{C}$), fijando el caudal máximo de vapor generado.",
        "bloque_sugerido": "Simulación Termodinámica 45 min • Modelado de diagrama T-Q en HRSG triple presión",
        "slides": [
            {
                "numero": 1,
                "seccion": "ACOPLAMIENTO TERMODINÁMICO",
                "titulo": "Sinergia Brayton-Rankine",
                "puntos": [
                    "El ciclo Brayton rechaza calor a altas temperaturas ($500 - 620^\\circ\\text{C}$), ideal como fuente caliente del ciclo Rankine.",
                    "La combinación eleva la eficiencia térmica de generación térmica fósil desde un 35% hasta superar el 62% LHV en plantas modernas clase H/J.",
                    "El generador de vapor por recuperación de calor (HRSG) opera con recirculación natural o forzada sin requerir quemadores adicionales (salvo 'duct firing')."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISEÑO DEL HRSG",
                "titulo": "Pinch Point y Approach Point",
                "puntos": [
                    "Pinch Point: $\\Delta T_{pp} = T_{gas,evap} - T_{sat}(P_{drum})$. Valores menores aumentan el área del intercambiador y los costos de capital.",
                    "Approach Point: $\\Delta T_{ap} = T_{sat}(P_{drum}) - T_{water,eco,out}$. Evita la vaporización prematura en el economizador.",
                    "Las configuraciones de triple presión con recalentamiento minimizan la destrucción de exergía en la transferencia térmica gas-agua."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Cogeneración (CHP) y Trigeneración (CCHP) Industrial",
        "objetivo": "Evaluar el aprovechamiento secuencial de la energía para producir simultáneamente electricidad, calor de proceso y refrigeración por absorción, cuantificando factores de uso de combustible.",
        "concepto_clave_latex": r"\text{FUE} = \frac{\dot{W}_e + \dot{Q}_{util}}{\dot{Q}_{in}} \quad ; \quad \text{PER} = \frac{\dot{W}_e}{\dot{Q}_{util}} \quad ; \quad \text{COP}_{abs} = \frac{\dot{Q}_{frio}}{\dot{Q}_{termico}}",
        "ejemplo": "Problema 1: Una planta industrial consume 10 MW de gas natural en un motor reciprocante para producir 4 MW de electricidad y recupera 4.5 MW de calor útil en forma de vapor saturado a 6 bar. Calcular el Factor de Utilización de Combustible (FUE): $\\text{FUE} = \\frac{4.0 + 4.5}{10.0} = 85\\%$, comparado con el $40\\%$ de generación eléctrica aislada. Problema 2: Si 2.0 MW del calor recuperado se derivan a un enfriador de absorción de bromuro de litio-agua ($LiBr-H_2O$) con $\\text{COP}_{abs} = 0.75$, la capacidad frigorífica producida para aire acondicionado es $\\dot{Q}_{frio} = 2.0 \\times 0.75 = 1.5\\text{ MW}_{term}$ (426 toneladas de refrigeración), configurando un sistema de trigeneración CCHP.",
        "bloque_sugerido": "Auditoría Térmica 45 min • Balance de masa y energía en sistemas CHP y CCHP",
        "slides": [
            {
                "numero": 1,
                "seccion": "EFICIENCIA INTEGRADA",
                "titulo": "Cogeneración (Topping vs Bottoming)",
                "puntos": [
                    "Ciclo Topping: El combustible se quema a alta temperatura para generar electricidad primero, y el calor residual alimenta procesos industriales.",
                    "Ciclo Bottoming: El combustible aporta calor a procesos de alta temperatura (vidrio, siderurgia) y los gases de escape mueven una turbina de vapor.",
                    "Reduce drásticamente las emisiones de CO2 y la demanda máxima sobre las redes de transporte eléctrico."
                ]
            },
            {
                "numero": 2,
                "seccion": "TRIGENERACIÓN Y DISTRITOS TÉRMICOS",
                "titulo": "Enfriadores por Absorción",
                "puntos": [
                    "Sustituyen el compresor mecánico accionado eléctricamente por un generador térmico y absorbedor químico.",
                    "Pares de trabajo dominantes: $LiBr-H_2O$ para aire acondicionado comercial ($> 5^\\circ\\text{C}$) y $NH_3-H_2O$ para congelación industrial ($< 0^\\circ\\text{C}$).",
                    "Aplanan la curva de demanda eléctrica en climas cálidos durante los picos de radiación solar diurna."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Conversión Termosolar de Concentración (CSP): Cilindro-Parabólicos y Torres",
        "objetivo": "Analizar la concentración óptica y la conversión termo-mecánica en plantas solares térmicas, evaluando el factor de concentración geométrica y el receptor central.",
        "concepto_clave_latex": r"C_g = \frac{A_{ap}}{A_{rec}} \quad ; \quad \eta_{opt} = \rho_{refl} \gamma_{int} \tau_{env} \alpha_{rec} \quad ; \quad \eta_{rec} = \eta_{opt} - \frac{\varepsilon \sigma (T_{rec}^4 - T_{amb}^4)}{C_g DNI}",
        "ejemplo": "Problema 1: Un colector cilindro-parabólico con apertura de 5.77 m de ancho y tubo receptor de 70 mm de diámetro exterior recibe una radiación directa normal ($DNI$) de $900\\text{ W/m}^2$. Calcular el factor de concentración geométrica: $A_{ap} = 5.77 \\times L$, $A_{rec} = \\pi D_{ext} L = \\pi(0.070)L = 0.2199 L$. Luego $C_g = \\frac{5.77}{0.2199} \\approx 26.24$. Si la eficiencia óptica es $\\eta_{opt} = 0.82$, la potencia térmica absorbida por metro lineal es $\\dot{q}_{abs}' = 5.77 \\times 900 \\times 0.82 = 4258\\text{ W/m}$. Problema 2: En plantas de torre central con helióstatos, $C_g > 600$, lo que permite temperaturas en sales fundidas superiores a $565^\\circ\\text{C}$ con eficiencias Rankine superiores al $42\\%$.",
        "bloque_sugerido": "Taller Solar Térmico 40 min • Balances radiativos y térmicos en receptores CSP",
        "slides": [
            {
                "numero": 1,
                "seccion": "TECNOLOGÍAS DE CONCENTRACIÓN",
                "titulo": "Enfoque Lineal vs Puntual",
                "puntos": [
                    "Cilindro-Parabólicos y Fresnel Lineal: Concentración 1D ($C_g \\sim 20 - 80$), operan con aceites térmicos sintéticos hasta $390^\\circ\\text{C}$.",
                    "Torre Central y Discos Stirling: Concentración 2D puntual ($C_g \\sim 500 - 1500$), operan con sales fundidas ($KNO_3/NaNO_3$) o aire presurizado hasta $700^\\circ\\text{C}$.",
                    "Permiten almacenamiento térmico a gran escala (TES en tanques de sales de dos zonas) garantizando despacho nocturno continuo."
                ]
            },
            {
                "numero": 2,
                "seccion": "BALANCES TÉRMICOS",
                "titulo": "Pérdidas Térmicas a Alta Temperatura",
                "puntos": [
                    "Las pérdidas por radiación crecen proporcionalmente a $T_{rec}^4$, exigiendo tubos al vacío con recubrimientos selectivos cerámico-metálicos (Cermet).",
                    "Baja emisividad en el infrarrojo lejano ($\\varepsilon < 0.08$) y alta absortancia solar ($\\alpha > 0.95$).",
                    "Factor de capacidad anual del 60% al 75% alcanzable en regiones con alto DNI (como La Guajira en Colombia)."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Generación Magnetohidrodinámica (MHD) y Metales Líquidos",
        "objetivo": "Comprender la extracción directa de energía eléctrica a partir de plasmas ionizados o metales líquidos en movimiento a través de un campo magnético perpendicular sin piezas mecánicas móviles.",
        "concepto_clave_latex": r"\mathbf{J} = \sigma (\mathbf{E} + \mathbf{v} \times \mathbf{B}) \quad ; \quad P_{elec} = \mathbf{J} \cdot \mathbf{E} = \sigma v^2 B^2 K(1 - K) \quad [K = E / (v B)]",
        "ejemplo": "Problema 1: Un canal generador MHD transporta un plasma gaseoso sembrado con sales de potasio a velocidad $v = 1200\\text{ m/s}$ a través de un campo magnético $B = 4.0\\text{ T}$. La conductividad eléctrica del gas es $\\sigma = 25\\text{ S/m}$ y el factor de carga eléctrica se fija en $K = 0.5$ (máxima potencia). Calcular la densidad de potencia eléctrica generada por metro cúbico: $P_{elec} = 25 \\times (1200)^2 \\times (4.0)^2 \\times 0.5(1 - 0.5) = 25 \\times 1.44 \\times 10^6 \\times 16 \\times 0.25 = 144 \\times 10^6\\text{ W/m}^3 = 144\\text{ MW/m}^3$. Problema 2: La fuerza de frenado magnético de Lorentz $\\mathbf{F}_L = \\mathbf{J} \\times \\mathbf{B}$ induce una caída de presión $\\frac{dP}{dx} = -J_y B_z$ que convierte directamente entalpía de flujo en trabajo eléctrico.",
        "bloque_sugerido": "Física de Plasmas 40 min • Ecuaciones magnetohidrodinámicas y canal de Faraday",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONVERSIÓN DIRECTA DE FLUIDOS",
                "titulo": "Principio Magnetohidrodinámico",
                "puntos": [
                    "Aplica la ley de inducción de Faraday a fluidos conductores de la electricidad (metales líquidos como sodio-potasio NaK, o gases ionizados térmicamente).",
                    "Elimina turbinas mecánicas, álabes y ejes rotativos, permitiendo temperaturas de entrada extremas ($> 2000^\\circ\\text{C}$).",
                    "El dopaje o sembrado con cesio o potasio ioniza el gas a temperaturas termodinámicamente viables."
                ]
            },
            {
                "numero": 2,
                "seccion": "ARQUITECTURA DE CANALES",
                "titulo": "Canales de Faraday, Hall y Disco",
                "puntos": [
                    "Canal de Faraday: Electrodos segmentados continuous para evitar corrientes axiales parásitas causadas por el efecto Hall.",
                    "Generador de Disco: Flujo de plasma radial divergente con campo magnético axial, con electrodos circulares concéntricos.",
                    "Excelente opción para ciclo topping acoplado a reactores de fusión nuclear o ciclos térmicos fósiles avanzados."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Celdas de Combustible de Alta Temperatura (SOFC / MCFC) e Hibridación",
        "objetivo": "Modelar la electroquímica y la termodinámica de celdas de óxido sólido (SOFC) y carbonato fundido (MCFC), evaluando su integración en ciclo híbrido con microturbinas de gas.",
        "concepto_clave_latex": r"E_{Nernst} = E^0 + \frac{RT}{nF} \ln\left( \frac{P_{H_2} P_{O_2}^{1/2}}{P_{H_2O}} \right) \quad ; \quad \eta_{hibrido} = \frac{W_{SOFC} + W_{MGT}}{\dot{m}_{CH_4} LHV} > 70\%",
        "ejemplo": "Problema 1: Una celda SOFC opera a $800^\\circ\\text{C}$ (1073 K). Calcular el potencial ideal de Nernst con presiones parciales $P_{H_2} = 0.85\\text{ atm}$, $P_{O_2} = 0.21\\text{ atm}$, $P_{H_2O} = 0.15\\text{ atm}$, sabiendo que $E^0(1073\\text{ K}) = 0.985\\text{ V}$. Parámetros: $R = 8.314\\text{ J/(mol K)}$, $F = 96485\\text{ C/mol}$, $n = 2$. Término: $\\frac{RT}{2F} = \\frac{8.314 \\times 1073}{2 \\times 96485} = 0.0462\\text{ V}$. Argumento logaritmo: $\\frac{0.85 \\times \\sqrt{0.21}}{0.15} = \\frac{0.85 \\times 0.4583}{0.15} = 2.597$. Luego $E = 0.985 + 0.0462 \\ln(2.597) = 0.985 + 0.0462(0.954) = 0.985 + 0.0441 = 1.029\\text{ V}$. Problema 2: En un ciclo híbrido SOFC-MGT, el combustible no reaccionado del ánodo se quema en una cámara de combustión para impulsar una microturbina de gas, alcanzando eficiencias combinadas superiores al $70\\%$.",
        "bloque_sugerido": "Electroquímica 45 min • Curvas de polarización V-I e impedancia electroquímica",
        "slides": [
            {
                "numero": 1,
                "seccion": "ELECTROQUÍMICA A ALTA TEMPERATURA",
                "titulo": "Electrolito Cerámico de YSZ",
                "puntos": [
                    "Las SOFC emplean un electrolito sólido de Circonia Estabilizada con Itria (YSZ) que conduce iones óxido ($O^{2-}$) a $650 - 900^\\circ\\text{C}$.",
                    "Cátodo: $\\frac{1}{2}O_2 + 2e^- \\rightarrow O^{2-}$; Ánodo: $H_2 + O^{2-} \\rightarrow H_2O + 2e^-$.",
                    "Permiten reformado interno directo de metano ($CH_4 + H_2O \\rightarrow CO + 3H_2$) sin reformadores externos caros."
                ]
            },
            {
                "numero": 2,
                "seccion": "SOFC INTEGRADA CON MICROTURBINAS",
                "titulo": "Sistemas Híbridos SOFC-GT",
                "puntos": [
                    "El aire presurizado por el compresor alimenta el cátodo de la celda de combustible.",
                    "Los gases de escape calientes a más de $850^\\circ\\text{C}$ entran directamente a la turbina de expansión generando trabajo mecánico adicional.",
                    "Cero emisiones de óxidos de nitrógeno ($NO_x$) y emisiones de CO2 altamente concentradas listas para captura directa."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Efecto Termoeléctrico Avanzado: Módulos Seebeck, Peltier y Factor de Mérito $ZT$",
        "objetivo": "Diseñar generadores termoeléctricos (TEG) de estado sólido para la cosecha de calor residual en tuberías y escapes industriales optimizando el factor de mérito adimensional $ZT$.",
        "concepto_clave_latex": r"ZT = \frac{S^2 \sigma}{\kappa} T \quad ; \quad \eta_{TEG} = \frac{T_H - T_C}{T_H} \frac{\sqrt{1+ZT_{avg}} - 1}{\sqrt{1+ZT_{avg}} + T_C/T_H} \quad ; \quad V_{oc} = N S \Delta T",
        "ejemplo": "Problema 1: Un material semiconductor termoeléctrico de telururo de bismuto ($Bi_2Te_3$) tiene un coeficiente Seebeck $S = 220\\ \\mu\\text{V/K}$, conductividad eléctrica $\\sigma = 1.1 \\times 10^5\\text{ S/m}$ y conductividad térmica $\\kappa = 1.5\\text{ W/(m K)}$ a una temperatura promedio $T = 350\\text{ K}$. Calcular $ZT$: Factor de potencia $S^2 \\sigma = (220 \\times 10^{-6})^2 \\times 1.1 \\times 10^5 = 4.84 \\times 10^{-8} \\times 1.1 \\times 10^5 = 5.324 \\times 10^{-3}\\text{ W/(m K}^2)$. Luego $ZT = \\frac{5.324 \\times 10^{-3}}{1.5} \\times 350 = 3.549 \\times 10^{-3} \\times 350 = 1.242$. Problema 2: Un módulo TEG comercial con 127 pares termopares opera entre $T_H = 200^\\circ\\text{C}$ (473 K) y $T_C = 40^\\circ\\text{C}$ (313 K). La tensión de circuito abierto es $V_{oc} = 127 \\times 220\\ \\mu\\text{V/K} \\times (200 - 40) = 0.02794 \\times 160 = 4.47\\text{ V}$.",
        "bloque_sugerido": "Laboratorio TEG 40 min • Curvas de potencia de generadores termoeléctricos",
        "slides": [
            {
                "numero": 1,
                "seccion": "FÍSICA DEL ESTADO SÓLIDO",
                "titulo": "Coeficientes Seebeck, Peltier y Thomson",
                "puntos": [
                    "Efecto Seebeck: Un gradiente de temperatura genera difusión de portadores de carga (electrones en tipo n, huecos en tipo p) produciendo un voltaje neto.",
                    "Efecto Peltier: Una corriente eléctrica externa absorbe o libera calor en la unión de dos conductores disímiles (enfriamiento de estado sólido).",
                    "El factor de mérito $ZT$ exige maximizar el factor de potencia termoeléctrico $S^2\\sigma$ mientras se minimiza la conducción térmica por fonones $\\kappa_{ph}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "COSECHA DE CALOR RESIDUAL",
                "titulo": "Generadores Termoeléctricos (TEG)",
                "puntos": [
                    "Dispositivos completamente estáticos, silenciosos, sin lubricantes ni mantenimiento mecánico.",
                    "Instalados en tubos de escape de motores de combustión interna reducen el consumo específico de combustible en un 3% a 5%.",
                    "Materiales nanomatriciales y skutteruditas empujan hoy $ZT > 2.0$, elevando la viabilidad tecno-económica."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Conversión Termofotovoltaica (TPV) y Emisores Espectrales Selectivos",
        "objetivo": "Analizar la conversión directa de fotones infrarrojos emitidos por fuentes térmicas de alta temperatura hacia celdas fotovoltaicas de baja banda prohibida ($E_g$).",
        "concepto_clave_latex": r"E_{ph} = \frac{h c}{\lambda} \ge E_g \quad ; \quad P_{rad} = \int_0^\infty \varepsilon(\lambda) \frac{2\pi h c^2}{\lambda^5 (e^{hc/(\lambda k_B T)} - 1)} d\lambda \quad ; \quad \eta_{TPV} > 40\%",
        "ejemplo": "Problema 1: Un emisor cerámico selectivo a $T = 1400^\\circ\\text{C}$ (1673 K) emite fotones hacia una celda fotovoltaica de Antimoniuro de Galio ($GaSb$) con banda prohibida $E_g = 0.72\\text{ eV}$. Calcular la longitud de onda de corte $\\lambda_{corte}$ para absorción fotovoltaica: $\\lambda_{corte} = \\frac{hc}{E_g} = \\frac{6.626 \\times 10^{-34} \\times 3.0 \\times 10^8}{0.72 \\times 1.602 \\times 10^{-19}} = \\frac{1.9878 \\times 10^{-25}}{1.1534 \\times 10^{-19}} = 1.723\\ \\mu\\text{m}$. Fotones con $\\lambda > 1.723\\ \\mu\\text{m}$ no excitan pares electrón-hueco y deben ser reflejados de vuelta al emisor para no disiparse en calor. Problema 2: Sistemas TPV con espejos de Bragg traseros logran eficiencias de conversión superiores al $41\\%$, superando a las turbinas de vapor en almacenamiento de energía térmica en silicio líquido.",
        "bloque_sugerido": "Óptica y Radiación 40 min • Celdas GaSb e integración en baterías térmicas",
        "slides": [
            {
                "numero": 1,
                "seccion": "PRINCIPIOS TERMOFOTOVOLTAICOS",
                "titulo": "Aislamiento de la Radiación Infrarroja",
                "puntos": [
                    "A diferencia de la solar PV donde la fuente está a 5800 K a 150 millones de km, en TPV el emisor térmico está a pocos centímetros a $1200 - 2000^\\circ\\text{C}$.",
                    "Permite densidades de potencia fotovoltaica enormes ($> 100\\text{ kW/m}^2$, cientos de veces superior al sol).",
                    "Celdas de banda estrecha ($InGaAs$, $GaSb$, $Ge$) sintonizadas con el pico de emisión infrarroja."
                ]
            },
            {
                "numero": 2,
                "seccion": "BATERÍAS TÉRMICAS",
                "titulo": "Almacenamiento Térmico de Muy Larga Duración",
                "puntos": [
                    "La electricidad renovable excedente calienta bloques de grafito o silicio hasta $2400^\\circ\\text{C}$.",
                    "Al descargarse, las celdas TPV convierten el brillo radiativo de nuevo en electricidad bajo demanda.",
                    "Costos de capital de almacenamiento hasta 10 veces inferiores a las baterías electroquímicas de iones de litio."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Conversión Piezotérmica y Piezoeléctrica de Vibraciones Mecánicas",
        "objetivo": "Modelar la captación de energía a partir de deformaciones mecánicas cíclicas y gradientes de temperatura pulsantes mediante cristales piezoeléctricos y materiales piroeléctricos.",
        "concepto_clave_latex": r"D = d \cdot T_m + \varepsilon^T E \quad ; \quad S_m = s^E T_m + d \cdot E \quad ; \quad P_{piezo} = \frac{1}{2} C_p V_{pk}^2 f \quad [d_{33} \text{ en C/N}]",
        "ejemplo": "Problema 1: Una viga en voladizo piezoeléctrica de PZT ($d_{33} = 400\\text{ pC/N}$, capacitancia $C_p = 25\\text{ nF}$) se somete a una vibración mecánica resonante de $f = 60\\text{ Hz}$ en una turbina hidráulica, alcanzando un voltaje pico de $V_{pk} = 18\\text{ V}$. Calcular la potencia media cosechada: $P = \\frac{1}{2} C_p V_{pk}^2 f = 0.5 \\times 25 \\times 10^{-9} \\times (18)^2 \\times 60 = 0.5 \\times 25 \\times 10^{-9} \\times 324 \\times 60 = 243 \\times 10^{-6}\\text{ W} = 243\\ \\mu\\text{W}$. Problema 2: Esta potencia es suficiente para alimentar de manera autónoma un nodo sensor inalámbrico IoT de vibración y temperatura sin requerir reemplazo de baterías.",
        "bloque_sugerido": "Microgeneración 35 min • Circuitos de acondicionamiento SSHI para transductores piezoeléctricos",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSDUCCIÓN ELECTROMECÁNICA",
                "titulo": "Efecto Piezoeléctrico Directo e Inverso",
                "puntos": [
                    "El efecto directo polariza eléctricamente el material bajo esfuerzo mecánico; el inverso induce deformación ante campos eléctricos.",
                    "Cerámicas dominantes: Titanato Zirconato de Plomo (PZT) y polímeros flexibles como PVDF.",
                    "Se sintoniza la frecuencia natural de la viga con los armónicos mecánicos del equipo rotativo."
                ]
            },
            {
                "numero": 2,
                "seccion": "AUTONOMÍA ENERGÉTICA",
                "titulo": "Cosecha de Energía en Smart Grids",
                "puntos": [
                    "Los sensores en torres de alta tensión cosechan vibraciones eólicas en conductores (vibración eólica de aeolian flutter).",
                    "Circuitos rectificadores sincronizados con interruptor (SSHI) cuadruplican la potencia extraíble frente a puentes de diodos pasivos.",
                    "Habilita el despliegue masivo del Internet de las Cosas Energético (IoT-E) en zonas remotas."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ciclos Supercríticos de Dióxido de Carbono ($sCO_2$) y Ciclo Allam",
        "objetivo": "Evaluar la termodinámica de ciclos de potencia cerrados y semicerrados operando por encima del punto crítico del $CO_2$ ($31.0^\\circ\\text{C}$, 7.39 MPa), con captura intrínseca de carbono.",
        "concepto_clave_latex": r"P_{cr} = 7.39\text{ MPa} \quad ; \quad T_{cr} = 31.0^\circ\text{C} \quad ; \quad \eta_{sCO_2, recompress} > 50\% \quad ; \quad W_{comp} \ll W_{comp, gas}",
        "ejemplo": "Problema 1: Explicar por qué el trabajo de compresión en un ciclo $sCO_2$ es significativamente menor que en un ciclo de gas convencional. Cerca del punto crítico, el dióxido de carbono exhibe una densidad similar a la de un líquido ($~600 - 800\\text{ kg/m}^3$) pero retiene la baja viscosidad de un gas. Dado que el trabajo de flujo continuo es $w = \\int v dP$, el volumen específico extremadamente bajo $v = 1/\\rho$ reduce el consumo del compresor a solo un $20\\%$ del trabajo de turbina (frente al $40-50\\%$ en ciclos Brayton de aire). Problema 2: En el ciclo Allam oxi-combustión a 300 bar, el $CO_2$ es el propio fluido de trabajo y los productos netos son solo agua líquida y $CO_2$ puro a alta presión listo para secuestro geológico sin penalización de captura energética.",
        "bloque_sugerido": "Ciclos Avanzados 45 min • Arquitectura de recompresión y propiedades cerca del punto pseudocrítico",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA SUPERCRÍTICA",
                "titulo": "El Comportamiento Anómalo del sCO2",
                "puntos": [
                    "El fluido no sufre cambio de fase líquido-vapor discontinuo; transita continuamente por encima de la línea pseudocrítica.",
                    "Turbinas extremadamente compactas: una turbomáquina de $sCO_2$ de 10 MW tiene el tamaño de un motor de automóvil gracias a la alta densidad del flujo.",
                    "Eficiencias térmicas de hasta 50% con temperaturas de fuente moderadas ($550 - 650^\\circ\\text{C}$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CERO EMISIONES",
                "titulo": "Ciclo Allam y Captura de Carbono",
                "puntos": [
                    "Quema gas natural con oxígeno puro ($O_2$) en presencia de un flujo de reciclado masivo de $sCO_2$ a 30 MPa.",
                    "No genera óxidos de nitrógeno ($NO_x$) y condensa el agua de combustión de manera instantánea al enfriarse.",
                    "Revolución para la descarbonización de la generación termoeléctrica de respaldo."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ciclos Orgánicos de Rankine (ORC) y Ciclos Kalina",
        "objetivo": "Diseñar ciclos termodinámicos con fluidos orgánicos e hidrocarburos de bajo punto de ebullición para la valorización de calor residual y energía geotérmica de baja/media entalpía.",
        "concepto_clave_latex": r"\frac{dT}{ds} \ge 0 \quad [\text{Fluidos Secos/Isentrópicos}] \quad ; \quad \dot{W}_{net} = \dot{m}_{org}(h_1 - h_2) - \dot{W}_{bomba} \quad ; \quad \eta_{ORC} = \frac{\dot{W}_{net}}{\dot{Q}_{in}}",
        "ejemplo": "Problema 1: Un ciclo ORC utiliza R245fa para recuperar calor de una corriente de agua caliente a $120^\\circ\\text{C}$ con caudal de $15\\text{ kg/s}$ que se enfría hasta $80^\\circ\\text{C}$ ($c_p = 4.18\\text{ kJ/(kg K)}$). Calor suministrado: $\\dot{Q}_{in} = 15 \\times 4.18 \\times (120 - 80) = 2508\\text{ kW}$. Si el ciclo ORC alcanza una eficiencia térmica del $12\\%$, calcular la potencia neta generada: $\\dot{W}_{net} = 2508 \\times 0.12 = 300.96\\text{ kW}$. Problema 2: En el ciclo Kalina, la mezcla binaria amoníaco-agua ($NH_3-H_2O$) no hierve a temperatura constante sino en un rango deslizante ('glide' térmico), acoplándose perfectamente a la curva de enfriamiento de la fuente caliente y reduciendo a la mitad la destrucción de exergía en el evaporador.",
        "bloque_sugerido": "Diseño Térmico 40 min • Selección de fluidos orgánicos en diagramas T-s (Secos vs Húmedos)",
        "slides": [
            {
                "numero": 1,
                "seccion": "FLUIDOS DE TRABAJO ORGÁNICOS",
                "titulo": "Fluidos Secos y Expansión sin Gotas",
                "puntos": [
                    "Fluidos como R134a, R245fa, n-pentano y tolueno poseen pendientes positivas ($dT/ds > 0$) en su curva de vapor saturado.",
                    "La expansión en la turbina no genera condensación ni gotas de líquido erosivas, eliminando el riesgo de sobrecalentamiento excesivo.",
                    "Aprovechan fuentes térmicas entre $80^\\circ\\text{C}$ y $250^\\circ\\text{C}$ donde el vapor de agua resulta inviable por bajas presiones y grandes volúmenes específicos."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIONES INDUSTRIALES",
                "titulo": "Geotermia y Residuos Térmicos",
                "puntos": [
                    "Clave para plantas geotérmicas de ciclo binario en yacimientos volcánicos de entalpía media.",
                    "Recupera calor de camisas y gases de escape en compresores de gasoductos y estaciones diésel insulares.",
                    "Fluidos ecológicos de cuarta generación (HFO como R1233zd(E)) con potencial de agotamiento ozono nulo ($ODP = 0$) y $GWP < 1$."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Gasificación Termoquímica y Producción de Gas de Síntesis (Syngas)",
        "objetivo": "Modelar las reacciones termoquímicas de oxidación parcial y reformado de biomasa sólida para producir gas de síntesis ($CO + H_2$), evaluando la eficiencia de gas frío (CGE).",
        "concepto_clave_latex": r"\text{CGE} = \frac{\dot{V}_{syngas} \cdot \text{LHV}_{syngas}}{\dot{m}_{bio} \cdot \text{LHV}_{bio}} \times 100\% \quad ; \quad \text{C} + \text{H}_2\text{O} \leftrightarrow \text{CO} + \text{H}_2 \ [\Delta H = +131\text{ kJ/mol}]",
        "ejemplo": "Problema 1: Un gasificador downdraft procesa $100\\text{ kg/h}$ de cuesco de palma africana ($\text{LHV} = 18\\text{ MJ/kg}$) inyectando aire subestequiométrico (relación de equivalencia $\\Phi = 0.3$). Produce $220\\text{ Nm}^3/\\text{h}$ de syngas con un poder calorífico inferior de $\\text{LHV}_{syngas} = 5.2\\text{ MJ/Nm}^3$. Calcular la Eficiencia de Gas Frío (CGE): Energía en biomasa: $\\dot{E}_{bio} = 100 \\times 18 = 1800\\text{ MJ/h}$. Energía en syngas: $\\dot{E}_{syn} = 220 \\times 5.2 = 1144\\text{ MJ/h}$. Luego $\\text{CGE} = \\frac{1144}{1800} \\times 100\\% = 63.56\\%$. Problema 2: La reacción de Boudouard ($C + CO_2 \\leftrightarrow 2CO$) y la reacción gas-agua absorben calor a temperaturas $> 850^\\circ\\text{C}$ para enriquecer el syngas en monóxido de carbono e hidrógeno.",
        "bloque_sugerido": "Bioenergía 45 min • Equilibrio químico y cinética en reactores downdraft y lecho fluidizado",
        "slides": [
            {
                "numero": 1,
                "seccion": "ZONAS TERMOQUÍMICAS",
                "titulo": "Secado, Pirólisis, Oxidación y Reducción",
                "puntos": [
                    "Secado ($100 - 150^\\circ\\text{C}$): Evaporación del contenido de humedad de la biomasa.",
                    "Pirólisis ($200 - 500^\\circ\\text{C}$): Desvolatilización térmica en carbón vegetal, gases condensables (alquitranes) y gases ligeros.",
                    "Oxidación ($800 - 1200^\\circ\\text{C}$): Combustión parcial exotérmica con agente gasificante (aire, oxígeno puro o vapor).",
                    "Reducción ($700 - 900^\\circ\\text{C}$): Reacciones endotérmicas heterogéneas que fijan el contenido energético del syngas."
                ]
            },
            {
                "numero": 2,
                "seccion": "LIMPIEZA DE ALQUITRANES",
                "titulo": "Acondicionamiento para Motores",
                "puntos": [
                    "Los alquitranes condensan a temperaturas $< 300^\\circ\\text{C}$ obstruyendo válvulas e inyectores de motores.",
                    "Craqueo térmico y catalítico (con dolomita o catalizadores de níquel) para transformar alquitranes pesados en $H_2$ y $CO$.",
                    "Gasificadores de lecho fluidizado circulante permiten escalar a potencias superiores a 50 MW térmicos."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Pirólisis de Biomasa: Bio-oil, Biochar y Fracciones Volátiles",
        "objetivo": "Diferenciar la pirólisis lenta, rápida y flash en función de las tasas de calentamiento y tiempos de residencia para optimizar la producción de biolíquidos y biocombustibles sólidos.",
        "concepto_clave_latex": r"\text{Biomasa} \xrightarrow{\Delta, \text{ anóxica}} \text{Bio-oil (líq)} + \text{Biochar (sól)} + \text{Gases no condensables}",
        "ejemplo": "Problema 1: En un reactor de pirólisis rápida de lecho fluidizado con tasa de calentamiento de $1000^\\circ\\text{C/s}$ y tiempo de residencia de vapores de 1.2 segundos a $500^\\circ\\text{C}$, el rendimiento másico es: $68\\%$ bio-oil, $18\\%$ biochar y $14\\%$ gas. Si se alimentan $500\\text{ kg/h}$ de bagazo de caña seco, calcular la tasa de producción de bio-oil: $\\dot{m}_{oil} = 500 \\times 0.68 = 340\\text{ kg/h}$. Con una densidad de $1.2\\text{ kg/L}$, esto equivale a $283.3\\text{ L/h}$. Problema 2: El biochar producido tiene un contenido de carbono fijado superior al $80\\%$, funcionando como sumidero permanente de carbono recalcitrante y mejorador de suelos agrícolas.",
        "bloque_sugerido": "Biorrefinerías 40 min • Caracterización fisicoquímica y acidez del bio-oil",
        "slides": [
            {
                "numero": 1,
                "seccion": "CINÉTICA DE PIRÓLISIS",
                "titulo": "Pirólisis Lenta vs Rápida vs Flash",
                "puntos": [
                    "Pirólisis Lenta (carbonización): Bajas tasas de calentamiento ($0.1 - 1^\\circ\\text{C/s}$), largos tiempos de residencia; maximiza el rendimiento de biochar ($~35\\%$).",
                    "Pirólisis Rápida: Altas tasas ($> 100^\\circ\\text{C/s}$), enfriamiento rápido (quench) de vapores; maximiza bio-oil líquido ($60 - 75\\%$).",
                    "El bio-oil crudo es ácido ($pH \\approx 2.5$) y oxigenado ($~40\\%$ O2), requiriendo hidrodesoxigenación (HDO) para usarse como combustible vehicular."
                ]
            },
            {
                "numero": 2,
                "seccion": "ECONOMÍA CIRCULAR",
                "titulo": "Secuestro de Carbono con Biochar",
                "puntos": [
                    "El biochar resiste la degradación microbiana en el suelo durante siglos, logrando emisiones netas negativas de carbono.",
                    "Aumenta la capacidad de retención hídrica y de intercambio catiónico en terrenos degradados.",
                    "Co-beneficio directo para zonas agrícolas del Magdalena y el Caribe colombiano."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Digestión Anaerobia y Conversión de Biogás a Biometano y Electricidad",
        "objetivo": "Modelar las fases bioquímicas de la digestión anaerobia de residuos orgánicos, calculando el rendimiento específico de metano ($CH_4$) y el enriquecimiento (upgrading) a biometano.",
        "concepto_clave_latex": r"\text{C}_n\text{H}_a\text{O}_b\text{N}_c + \dots \rightarrow \frac{n}{2} \text{CH}_4 + \dots \quad ; \quad Y_{CH_4} = 350 \frac{\text{L } CH_4}{\text{kg } DQO_{removida}} \quad ; \quad \text{LHV}_{biogas} \approx 21.5\text{ MJ/m}^3",
        "ejemplo": "Problema 1: Una planta de beneficio ganadero genera aguas residuales con una carga de demanda química de oxígeno removida de $1200\\text{ kg DQO/día}$. Calcular el volumen diario de metano generado en condiciones estándar y la potencia eléctrica media si el biogás alimenta un motogenerador con eficiencia del $35\\%$. Volumen de metano: $V_{CH_4} = 1200 \\times 0.350 = 420\\text{ Nm}^3/\\text{día}$. Contenido energético ($\text{LHV}_{CH_4} = 35.8\\text{ MJ/Nm}^3$): $E = 420 \\times 35.8 = 15036\\text{ MJ/día} = 4176.67\\text{ kWh/día}$. Potencia eléctrica media: $P_e = \\frac{4176.67 \\times 0.35}{24\\text{ h}} = \\frac{1461.83}{24} = 60.91\\text{ kW}$. Problema 2: En el upgrading a biometano ($>97\\% CH_4$), tecnologías de lavado con agua a presión (PWS) o membranas poliméricas eliminan el $CO_2$ y el ácido sulfhídrico ($H_2S$) corrosivo para inyección en redes de gas.",
        "bloque_sugerido": "Ingeniería de Biogás 40 min • Diseño de biodigestores CSTR y UASB",
        "slides": [
            {
                "numero": 1,
                "seccion": "FASES MICROBIOLÓGICAS",
                "titulo": "Ruta Metabólica Anaerobia",
                "puntos": [
                    "Hidrólisis: Polímeros complejos (carbohidratos, lípidos, proteínas) descompuestos en monómeros solubles.",
                    "Acidogénesis: Bacterias fermentativas generan ácidos grasos volátiles (AGV), alcoholes y $CO_2$.",
                    "Acetogénesis: Conversión de AGV en acetato, $H_2$ y $CO_2$.",
                    "Metanogénesis: Arqueas metanogénicas acetoclásticas e hidrogenotróficas sintetizan metano a $37^\\circ\\text{C}$ (mesofílico) o $55^\\circ\\text{C}$ (termofílico)."
                ]
            },
            {
                "numero": 2,
                "seccion": "UPGRADING Y VALORIZACIÓN",
                "titulo": "Biometano para Red y Transporte",
                "puntos": [
                    "El biogás bruto contiene $55-65\\% CH_4$, $35-45\\% CO_2$, y trazas de $H_2S$ ($100 - 5000$ ppm).",
                    "Filtros de carbón activado o biofiltros de lecho fijo desulfuran el gas antes de entrar a motogeneradores.",
                    "El digestato líquido y sólido remanente es un biofertilizante rico en nitrógeno, fósforo y potasio (NPK)."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Electrólisis del Agua para Producción de Hidrógeno Verde (PEM, Alcalina y SOEC)",
        "objetivo": "Cuantificar el consumo específico de energía, el sobrepotencial electroquímico y la eficiencia de conversión faradaica en electrolizadores alcalinos, PEM y de óxido sólido (SOEC).",
        "concepto_clave_latex": r"E_{rev} = 1.229\text{ V} \quad ; \quad E_{tn} = 1.481\text{ V} \quad ; \quad \eta_{electrolisis} = \frac{\text{HHV}_{H_2}}{\text{Consumo Específico } [\\text{kWh/kg}]} \approx 65 - 82\%",
        "ejemplo": "Problema 1: Un electrolizador PEM opera con un consumo específico de $52\\text{ kWh por cada kg de } H_2$ producido. Sabiendo que el poder calorífico superior del hidrógeno es $\\text{HHV}_{H_2} = 141.8\\text{ MJ/kg} = 39.39\\text{ kWh/kg}$, calcular la eficiencia eléctrica del sistema en base HHV: $\\eta_{PEM} = \\frac{39.39}{52.0} \\times 100\\% = 75.75\\%$. Problema 2: Un parque solar fotovoltaico de 10 MW en el Magdalena genera $45\\text{ MWh}$ diarios de excedente renovable. Calcular la masa de hidrógeno verde producible diariamente: $m_{H_2} = \\frac{45000\\text{ kWh}}{52\\text{ kWh/kg}} = 865.38\\text{ kg } H_2/\\text{día}$. A presión estándar, esto equivale a $\\approx 9692\\text{ Nm}^3/\\text{día}$.",
        "bloque_sugerido": "Economía del Hidrógeno 45 min • Curvas de polarización y sobrepotenciales de Tafel",
        "slides": [
            {
                "numero": 1,
                "seccion": "TECNOLOGÍAS DE ELECTRÓLISIS",
                "titulo": "Alcalina vs PEM vs SOEC",
                "puntos": [
                    "Alcalina (AEL): Electrolito acuoso KOH ($20-30\\%$), electrodos de níquel; bajo costo de capital pero lenta respuesta dinámica.",
                    "Membrana de Intercambio Protónico (PEM): Membrana sólida Nafion, catalizadores de platino e iridio; respuesta en milisegundos ideal para acople solar y eólico.",
                    "Óxido Sólido (SOEC): Opera con vapor de agua a alta temperatura ($700-850^\\circ\\text{C}$); consume calor residual reduciendo la demanda eléctrica a $< 40\\text{ kWh/kg}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "DINÁMICA DE ACOPLE RENOVABLE",
                "titulo": "Operación con Fuentes Variables",
                "puntos": [
                    "La naturaleza intermitente de la energía solar y eólica requiere electrolizadores capaces de operar desde un 5% hasta un 120% de su carga nominal.",
                    "Degradación acelerada por ciclos térmicos y transitorios de voltaje de apagado.",
                    "El hidrógeno comprimido a 350 o 700 bar actúa como almacenamiento estacional y vector químico para síntesis de amoníaco verde."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Almacenamiento Termoquímico de Energía (TCES) y Reacciones Redox Reversibles",
        "objetivo": "Modelar la acumulación de energía a alta densidad mediante reacciones químicas endotérmicas y exotérmicas reversibles sin pérdidas térmicas durante el almacenamiento prolongado.",
        "concepto_clave_latex": r"\text{AB} + \Delta H_r \xrightleftharpoons[\text{Descarga (exotérmica)}]{\text{Carga (endotérmica)}} \text{A} + \text{B} \quad ; \quad \text{CaCO}_3 + 178\text{ kJ/mol} \leftrightarrow \text{CaO} + \text{CO}_2",
        "ejemplo": "Problema 1: En el ciclo de carbonatación-calcinación de calcio ($CaL$), el carbonato de calcio se calcina a $900^\\circ\\text{C}$ absorbiendo $178\\text{ kJ/mol}$. La masa molar del $CaCO_3$ es $100.09\\text{ g/mol}$. Calcular la densidad teórica de almacenamiento de energía por kilogramo de reactivo sólido: $\\rho_E = \\frac{178\\text{ kJ}}{0.10009\\text{ kg}} = 1778.4\\text{ kJ/kg} = 0.494\\text{ kWh/kg}$. Esto es casi 3 veces superior a la densidad de almacenamiento térmico de sales fundidas líquidas. Problema 2: Una vez separados y enfriados a temperatura ambiente, el $CaO$ y el $CO_2$ pueden almacenarse indefinidamente sin pérdidas de calor (pérdidas térmicas cero), reaccionando exotérmicamente solo cuando se recombina a demanda para generar vapor.",
        "bloque_sugerido": "Termoquímica 40 min • Termogrametría y cinética de ciclos redox en TCES",
        "slides": [
            {
                "numero": 1,
                "seccion": "DENSIDADES DE ENERGÍA",
                "titulo": "Sensible vs Latente vs Termoquímico",
                "puntos": [
                    "Calor Sensible ($c_p \\Delta T$): Densidad de $0.1 - 0.3\\text{ GJ/m}^3$; sufre pérdidas térmicas continuas por aislamiento imperfecto.",
                    "Calor Latente ($\Delta H_{fus}$): Densidad de $0.3 - 0.5\\text{ GJ/m}^3$; opera a temperatura fija de cambio de fase.",
                    "Termoquímico (TCES): Densidad de $1.0 - 3.0\\text{ GJ/m}^3$; almacenamiento químico a temperatura ambiente durante meses sin pérdidas."
                ]
            },
            {
                "numero": 2,
                "seccion": "SISTEMAS QUÍMICOS PROMETEDORES",
                "titulo": "Óxidos Metálicos y Sales Hidratadas",
                "puntos": [
                    "Pares óxido-reducción de óxidos de manganeso y cobalto ($Co_3O_4 / CoO$) a $> 800^\\circ\\text{C}$ para plantas solares de torre.",
                    "Deshidratación de sales a baja temperatura ($MgSO_4 \\cdot 7H_2O$) para calefacción de distritos urbanos en invierno.",
                    "Retos: Sinterización y aglomeración de partículas sólidas tras cientos de ciclos térmicos continuos."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Conversión de Energía Térmica Oceánica (OTEC): Ciclos Abiertos y Cerrados",
        "objetivo": "Evaluar la extracción de potencia a partir del gradiente térmico entre aguas superficiales cálidas tropicales y aguas abisales frías mediante ciclos Rankine de baja presión.",
        "concepto_clave_latex": r"\Delta T_{ocean} = T_{sup} - T_{prof} \ge 20^\circ\text{C} \quad ; \quad \eta_{Carnot} = 1 - \frac{T_{prof}}{T_{sup}} \approx 6.7\% \quad ; \quad P_{net} = P_{turb} - P_{bomba,cw} - P_{bomba,ww}",
        "ejemplo": "Problema 1: En las costas del Caribe frente a Santa Marta, la temperatura superficial es $T_{sup} = 28^\\circ\\text{C}$ (301.15 K) y a 1000 m de profundidad es $T_{prof} = 5^\\circ\\text{C}$ (278.15 K). Calcular la eficiencia máxima de Carnot teórica: $\\eta_{Carnot} = 1 - \\frac{278.15}{301.15} = 1 - 0.9236 = 7.64\\%$. Si la eficiencia real del ciclo cerrado de amoníaco es el $3.2\\%$, para producir 10 MW brutos se requiere extraer $\\dot{Q}_{in} = \\frac{10\\text{ MW}}{0.032} = 312.5\\text{ MW}$ de calor del mar superficial. Problema 2: El bombeo de agua fría profunda consume entre el $25\\%$ y el $35\\%$ de la potencia bruta generada, exigiendo conductos verticales aislados de polietileno de alta densidad (HDPE) de gran diámetro ($> 4\\text{ m}$).",
        "bloque_sugerido": "Energía Marina 40 min • Ciclo abierto Claude con desalinización simultánea de agua",
        "slides": [
            {
                "numero": 1,
                "seccion": "POTENCIAL TÉRMICO MARINO",
                "titulo": "Energía de Carga Base Constante",
                "puntos": [
                    "A diferencia de la solar o eólica, el gradiente térmico oceánico opera las 24 horas del día, 365 días al año sin variabilidad meteorológica.",
                    "El Caribe colombiano posee uno de los mejores recursos OTEC del mundo con $\\Delta T > 22^\\circ\\text{C}$ todo el año.",
                    "Ciclo Cerrado (Anderson): Utiliza amoníaco puro ($NH_3$) evaporado por el agua superficial cálida y condensado por el agua fría del fondo."
                ]
            },
            {
                "numero": 2,
                "seccion": "CO-PRODUCTOS DE ALTO VALOR",
                "titulo": "Ciclo Abierto y Acuicultura",
                "puntos": [
                    "Ciclo Abierto (Claude): El agua de mar superficial se evapora a vacío instantáneamente (flash evaporation); el vapor mueve la turbina y al condensarse produce agua potable pura.",
                    "El agua profunda bombeada es prístina, rica en nutrientes inorgánicos (nitratos y fosfatos) ideal para maricultura y enfriamiento de distritos.",
                    "Elevados costos de capital inicial amortizables por la generación combinada de energía y agua dulce."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Energía de Gradiente Salino (Osmótica): PRO y Electrodiálisis Inversa (RED)",
        "objetivo": "Calcular la energía libre de mezcla liberada cuando se encuentran masas de agua dulce de río y agua salada de mar, modelando tecnologías PRO y RED.",
        "concepto_clave_latex": r"\Delta \Pi = \nu R T (c_{sal} - c_{dulce}) \quad ; \quad W_{mix} = 2 R T \left[ c_s \ln\left(\frac{c_s}{c_m}\right) \right] \approx 0.8\text{ kWh/m}^3 \text{ de agua de río}",
        "ejemplo": "Problema 1: En la desembocadura del río Magdalena en Bocas de Ceniza, agua de río ($c_d \\approx 0$) se mezcla con agua de mar Caribe ($c_s = 0.55\\text{ mol/L}$ NaCl) a $T = 27^\\circ\\text{C}$ (300.15 K). Calcular la presión osmótica teórica $\\Delta \\Pi$ con factor de van 't Hoff $\\nu = 2$: $\\Delta \\Pi = 2 \\times 8.314\\text{ J/(mol K)} \\times 300.15\\text{ K} \\times 550\\text{ mol/m}^3 = 2.745 \\times 10^6\\text{ Pa} = 2.745\\text{ MPa}$ ($~27.4\\text{ bar}$, equivalente a una columna hidrostática de 280 metros de caída). Problema 2: En Ósmosis por Retardo de Presión (PRO), el agua de río atraviesa una membrana semipermeable hacia una cámara salina presurizada a $\\Delta P = \\Delta \\Pi / 2 = 13.7\\text{ bar}$, expulsando agua presurizada hacia una turbina hidroeléctrica Pelton para generar electricidad.",
        "bloque_sugerido": "Sistemas Osmóticos 45 min • Densidad de potencia en membranas PRO y apilamientos RED",
        "slides": [
            {
                "numero": 1,
                "seccion": "POTENCIAL AZUL",
                "titulo": "Energía Osmótica en Desembocaduras",
                "puntos": [
                    "Potencial de energía renovable no intermitente de carga base sin emisiones de gases de efecto invernadero.",
                    "Cada metro cúbico de agua de río descargado en el mar libera teóricamente cerca de $0.8\\text{ kWh}$ de energía por disipación entrópica.",
                    "El río Magdalena aporta un caudal medio de $7200\\text{ m}^3/\\text{s}$, representando gigavatios potenciales teóricos de potencia azul."
                ]
            },
            {
                "numero": 2,
                "seccion": "PRO vs ELECTRODIÁLISIS INVERSA",
                "titulo": "Presión Hidráulica vs Voltaje Nodal",
                "puntos": [
                    "PRO (Pressure Retarded Osmosis): Transporte osmótico de agua a través de membrana que incrementa caudal y presión mecánica hidrostática.",
                    "RED (Reverse Electrodialysis): Membranas alternadas de intercambio catiónico (CEM) y aniónico (AEM) generan directamente corriente eléctrica por migración de iones $Na^+$ y $Cl^-$.",
                    "El ensuciamiento biológico (biofouling) y el costo por metro cuadrado de membrana son los principales retos de maduración tecnológica."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Conversión Termoacústica: Motores y Refrigeradores sin Partes Móviles",
        "objetivo": "Analizar la interacción entre gradientes térmicos y ondas acústicas estacionarias o viajeras en canales porosos para la conversión calor-sonido-electricidad mediante transductores piezoeléctricos o lineales.",
        "concepto_clave_latex": r"\dot{W}_{acustico} = \frac{1}{2} \text{Re} \left[ \iint p_1 \cdot u_1^* dA \right] \quad ; \quad \frac{dT}{dx} > \left(\frac{dT}{dx}\right)_{crit} = \frac{\omega T_m \beta}{\rho c_p} \frac{p_1}{u_1}",
        "ejemplo": "Problema 1: Un motor termoacústico de onda estacionaria opera con helio presurizado a 3.0 MPa. Si el gradiente de temperatura a lo largo del regenerador poroso supera el valor crítico $(dT/dx)_{crit} = 45^\\circ\\text{C/cm}$, las oscilaciones de presión acústica crecen espontáneamente alcanzando un nivel de presión sonora de 170 dB ($p_1 = 35\\text{ kPa}$ pico). La potencia acústica generada de 1.8 kW incide sobre un alternador lineal de imanes permanentes con rendimiento del 85%, produciendo $P_e = 1.8 \\times 0.85 = 1.53\\text{ kW}$ eléctricos. Problema 2: Al no requerir cigüeñal, pistones lubricados ni sellos mecánicos, los sistemas termoacústicos exhiben vidas útiles superiores a 20 años sin mantenimiento en misiones espaciales e industrias criogénicas.",
        "bloque_sugerido": "Física Acústica 40 min • Termodinámica del regenerador poroso y canales de Rott",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL EFECTO TERMOACÚSTICO",
                "titulo": "Calor en Sincronía con Ondas Sonoras",
                "puntos": [
                    "Criterio de Rayleigh: Si se transfiere calor al gas en el momento de máxima compresión y se extrae en la máxima rarefacción, la onda sonora se amplifica.",
                    "El regenerador ('stack') de malla fina o panal cerámico impone un gradiente de temperatura longitudinal estricto.",
                    "Ondas viajeras (ciclo Stirling acústico) logran eficiencias térmicas de más del 30% del límite de Carnot."
                ]
            },
            {
                "numero": 2,
                "seccion": "FIABILIDAD EXTREMA",
                "titulo": "Cosecha Térmica en Ambientes Hostiles",
                "puntos": [
                    "Refrigeración criogénica para licuefacción de gas natural y enfriamiento de sensores infrarrojos.",
                    "Alimentado por concentradores solares parabólicos o radioisótopos térmicos (RTG termoacústico).",
                    "Cero desgaste por fricción y total ausencia de gases refrigerantes contaminantes (usa helio inerte o nitrógeno)."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Almacenamiento Térmico por Calor Latente con Materiales de Cambio de Fase (PCM)",
        "objetivo": "Modelar la fusión y solidificación de parafinas, sales inorgánicas e hidratos salinos para la acumulación isotérmica de calor y frío en sistemas de climatización e industria.",
        "concepto_clave_latex": r"Q_{almacenado} = m \left[ c_{p,sol}(T_f - T_1) + \Delta H_{fus} + c_{p,liq}(T_2 - T_f) \right] \quad ; \quad \frac{\partial H}{\partial t} = \nabla \cdot (k \nabla T)",
        "ejemplo": "Problema 1: Un tanque cilíndrico de almacenamiento de frío para acondicionamiento de aire en la Universidad del Magdalena contiene $2000\\text{ kg}$ de un PCM orgánico a base de ácidos grasos con punto de fusión $T_f = 12^\\circ\\text{C}$, calor latente $\\Delta H_{fus} = 180\\text{ kJ/kg}$, $c_{p,sol} = 2.1\\text{ kJ/(kg K)}$ y $c_{p,liq} = 2.4\\text{ kJ/(kg K)}$. Si se enfría desde $20^\\circ\\text{C}$ hasta congelarse a $8^\\circ\\text{C}$, calcular el calor total absorbido: Enfriamiento líquido ($20 \\rightarrow 12$): $Q_1 = 2000 \\times 2.4 \\times 8 = 38400\\text{ kJ}$. Cambio de fase a $12^\\circ\\text{C}$: $Q_2 = 2000 \\times 180 = 360000\\text{ kJ}$. Enfriamiento sólido ($12 \\rightarrow 8$): $Q_3 = 2000 \\times 2.1 \\times 4 = 16800\\text{ kJ}$. Total: $Q_T = 38400 + 360000 + 16800 = 415200\\text{ kJ} = 115.33\\text{ kWh}$. El calor latente aporta el $86.7\\%$ del almacenamiento total en un rango de apenas $12^\\circ\\text{C}$. Problema 2: La baja conductividad térmica de los PCM orgánicos ($k \\approx 0.2\\text{ W/(m K)}$) se mitiga incorporando aletas de aluminio, espumas de cobre o nanopartículas de grafeno.",
        "bloque_sugerido": "Simulación Numérica 45 min • Método de la entalpía para problemas de frontera móvil de Stefan",
        "slides": [
            {
                "numero": 1,
                "seccion": "CLASIFICACIÓN DE PCMs",
                "titulo": "Orgánicos, Inorgánicos y Eutécticos",
                "puntos": [
                    "Orgánicos (parafinas y ácidos grasos): Químicamente estables, no corrosivos, fusión congruente sin segregación de fases; inflamables y baja conductividad térmica.",
                    "Inorgánicos (sales hidratadas): Alto calor latente y alta conductividad; sufren de sobreenfriamiento ('supercooling') y corrosión metálica.",
                    "Materiales de cambio de fase de alta temperatura ($300 - 800^\\circ\\text{C}$) basados en sales de nitratos y carbonatos para CSP."
                ]
            },
            {
                "numero": 2,
                "seccion": "EFICIENCIA EN EDIFICACIONES",
                "titulo": "Gestión de la Inercia Térmica",
                "puntos": [
                    "Integrados en paneles de yeso, techos y fachadas reducen las oscilaciones de temperatura interior entre el día y la noche.",
                    "Permiten cargar almacenamiento de frío durante la noche con tarifas eléctricas valle y descargar durante el pico diurno.",
                    "Disminuyen el tamaño de los compresores de aire acondicionado en un 30% a 40%."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Captura, Almacenamiento y Utilización de Carbono (CCUS) en Centrales Térmicas",
        "objetivo": "Evaluar los métodos de captura de $CO_2$ postcombustión con aminas químicas, precombustión e integración de oxi-combustión, determinando la penalización de eficiencia de planta.",
        "concepto_clave_latex": r"\text{Penalización } \Delta \eta = \eta_{sin\_captura} - \eta_{con\_captura} \approx 6 - 11\% \quad ; \quad \dot{Q}_{rehervidor} \approx 3.0 - 4.2 \frac{\text{MJ}}{\text{kg } CO_2}",
        "ejemplo": "Problema 1: Una central termoeléctrica de carbón de 500 MWe con eficiencia del 38% emite $0.85\\text{ kg CO}_2/\\text{kWh}$. Se instala una planta de captura postcombustión con monoetanolamina (MEA) al 90% de captura. Emisiones horarias capturadas: $\\dot{m}_{CO_2} = 500000\\text{ kW} \\times 0.85\\text{ kg/kWh} \\times 0.90 = 382500\\text{ kg CO}_2/\\text{h} = 106.25\\text{ kg/s}$. Si el rehervidor de desorción requiere $3.6\\text{ MJ/kg CO}_2$, el calor extraído de la turbina de vapor es: $\\dot{Q}_{desorb} = 106.25 \\times 3.6 = 382.5\\text{ MW}_{term}$. Esta derivación reduce la potencia eléctrica neta de 500 MW a aproximadamente 415 MW, reflejando una penalización energética de 8.5 puntos porcentuales de eficiencia. Problema 2: En la utilización de carbono (CCU), el $CO_2$ capturado se hidrogena con $H_2$ verde para sintetizar metanol ($CH_3OH$) y combustibles de aviación sintéticos sostenibles (e-fuels).",
        "bloque_sugerido": "Ingeniería Química 45 min • Columnas de absorción de relleno y desorción térmica de MEA",
        "slides": [
            {
                "numero": 1,
                "seccion": "RUTAS DE CAPTURA TECNOLÓGICA",
                "titulo": "Post-combustión, Pre-combustión y Oxi-combustión",
                "puntos": [
                    "Post-combustión: Absorción química reversible con aminas (MEA, piperazina); adaptable a plantas térmicas existentes (retrofitting).",
                    "Pre-combustión: Gasificación de combustible seguida de reacción de desplazamiento gas-agua (WGS) para separar $CO_2$ a alta presión antes de la combustión.",
                    "Oxi-combustión: Combustión en oxígeno puro diluido con $CO_2$ reciclado; produce humo compuesto solo de $CO_2$ y vapor de agua fácilmente condensable."
                ]
            },
            {
                "numero": 2,
                "seccion": "SECUESTRO Y DESTINO FINAL",
                "titulo": "Almacenamiento Geológico Seguro",
                "puntos": [
                    "Inyección en formaciones salinas profundas ($> 1000\\text{ m}$) en estado supercrítico donde permanece atrapado por mecanismos estructurales, capilares y de mineralización.",
                    "Monitoreo sísmico y gravimétrico para verificar la integridad de la roca sello.",
                    "Pilar indispensable para alcanzar la neutralidad climática en industrias de difícil descarbonización (cemento, acero, petroquímica)."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Análisis Termoeconómico y Exergoeconómico de Sistemas Energéticos",
        "objetivo": "Integrar el segundo principio de la termodinámica con la economía de costos mediante la metodología SPECO (Specific Exergy Costing) para imputar costos monetarios a flujos de exergía y destrucción irreversibilidad.",
        "concepto_clave_latex": r"\sum \dot{C}_{out} + \dot{C}_{w} = \sum \dot{C}_{in} + \dot{C}_{q} + \dot{Z}_k \quad ; \quad \dot{C}_i = c_i \dot{E}x_i \quad ; \quad f_k = \frac{\dot{Z}_k}{\dot{Z}_k + c_{F,k} \dot{E}x_{D,k}}",
        "ejemplo": "Problema 1: Una turbina de gas consume un flujo de exergía de combustible $\\dot{E}x_F = 80\\text{ MW}$ con un costo unitario $c_F = 6.0\\text{ USD/GJ}$ ($0.0216\\text{ USD/kWh}$). La potencia producida es $\\dot{W} = 30\\text{ MW}$, destruyendo $\\dot{E}x_D = 20\\text{ MW}$ de exergía en combustión y fricción, con una tasa de costo de inversión amortizada $\\dot{Z} = 450\\text{ USD/h}$. Costo de combustible por hora: $\\dot{C}_F = 80000\\text{ kW} \\times 3600\\text{ s/h} \\times 10^{-6}\\text{ GJ} \\times 6 = 1728\\text{ USD/h}$. Costo de la destrucción de exergía: $\\dot{C}_D = c_F \\dot{E}x_D = 20000 \\times 3.6 \\times 10^{-3} \\times 6 = 432\\text{ USD/h}$. Factor exergoeconómico $f_k$: $f_k = \\frac{450}{450 + 432} = \\frac{450}{882} = 51.02\\%$. Al estar cercano al 50%, el componente de inversión y la penalización por ineficiencia termodinámica están equilibrados. Problema 2: Si $f_k < 20\\%$, se debe invertir más capital en turbomaquinaria de mayor rendimiento aerodinámico para mitigar las pérdidas termodinámicas excesivas.",
        "bloque_sugerido": "Ingeniería Económica 45 min • Asignación matricial de costos exergoeconómicos con SPECO",
        "slides": [
            {
                "numero": 1,
                "seccion": "COSTEO BASADO EN EXERGÍA",
                "titulo": "La Moneda de la Calidad Energética",
                "puntos": [
                    "La primera ley de la termodinámica no distingue entre calor a baja temperatura y electricidad pura; la exergía sí cuantifica su verdadero potencial de trabajo.",
                    "El costeo exergoeconómico asigna tarifas en USD a los julios exergéticos ($c_i$ en USD/GJ).",
                    "Permite descubrir exactamente qué componente de una planta termoeléctrica o de biomasa es el culpable económico de la elevación de costos de generación."
                ]
            },
            {
                "numero": 2,
                "seccion": "FACTOR EXERGOECONÓMICO",
                "titulo": "Optimización Tecno-Económica",
                "puntos": [
                    "Si $f_k \\gg 50\\%$: Los costos fijos de capital ($Z_k$) dominan; se deben buscar equipos más económicos aunque sean ligeramente menos eficientes.",
                    "Si $f_k \\ll 50\\%$: Los costos de combustible por irreversibilidad dominan; se justifica una mayor inversión inicial en materiales y eficiencia térmica.",
                    "Guía de diseño decisiva para inversores y diseñadores en proyectos energéticos a escala de megavatios."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Evaluación de Ciclo de Vida (LCA) y Factor EROI en Tecnologías de Conversión",
        "objetivo": "Evaluar la sostenibilidad integral de sistemas de conversión energética calculando la Tasa de Retorno Energético (EROI), el Tiempo de Amortización Energética (EPBT) y la huella de carbono 'cradle-to-grave' según normas ISO 14040/44.",
        "concepto_clave_latex": r"\text{EROI} = \frac{E_{generada, vida\_util}}{E_{invertida, ciclo\_completo}} \quad ; \quad \text{EPBT} = \frac{E_{fabricacion, instalacion}}{\dot{E}_{neta\_anual}} \quad [\text{años}]",
        "ejemplo": "Problema 1: Un panel solar fotovoltaico de 400 W monocristalino requiere una energía incorporada de fabricación e instalación de $E_{inv} = 1800\\text{ kWh}_{eq}$. En Santa Marta genera anualmente $650\\text{ kWh}$ con una vida útil garantizada de 30 años (degradación $0.5\\%$/año, energía total producida en 30 años $\\approx 18000\\text{ kWh}$). Calcular: 1) Tiempo de amortización energética: $\\text{EPBT} = \\frac{1800}{650} = 2.77\\text{ años}$. A partir del año 2.8, el panel entrega energía neta positiva a la sociedad. 2) Retorno energético: $\\text{EROI} = \\frac{18000}{1800} = 10.0$. Problema 2: Tecnologías con $\\text{EROI} < 3.0$ no pueden sostener una sociedad industrial avanzada debido a que consumen una fracción excesiva de su propia energía producida para su reconstrucción y operación.",
        "bloque_sugerido": "Sostenibilidad Energética 45 min • Inventario de Ciclo de Vida (LCI) en software SimaPro/OpenLCA",
        "slides": [
            {
                "numero": 1,
                "seccion": "RETORNO ENERGÉTICO",
                "titulo": "El Concepto de EROI (Energy Return on Investment)",
                "puntos": [
                    "Mide cuántas unidades de energía útil entrega una tecnología por cada unidad de energía primaria gastada en extraer materiales, fabricarla, instalarla y desmantelarla.",
                    "Hidroeléctrica tradicional: EROI $> 40:1$; Solar Fotovoltaica moderna: EROI $\\approx 10 - 15:1$; Biocombustibles de primera generación: EROI $\\approx 1.3 - 2.5:1$.",
                    "El 'acantilado energético' (Energy Cliff): Por debajo de un EROI de 5:1, la viabilidad económica decae exponencialmente."
                ]
            },
            {
                "numero": 2,
                "seccion": "HUELLA DE CARBONO INTEGRAL",
                "titulo": "Análisis de la Cuna a la Tumba (LCA)",
                "puntos": [
                    "Cuantifica emisiones en extracción minera (silicio, litio, tierras raras), transporte, ensamblaje, 25-30 años de operación y reciclaje final.",
                    "Intensidad de carbono típica: Carbón ($~820\\text{ g CO}_2/\\text{kWh}$), Gas Natural ($~450\\text{ g}$), Solar PV ($~20 - 40\\text{ g}$), Eólica ($~11\\text{ g}$), Nuclear ($~12\\text{ g}$).",
                    "Requisito regulatorio indispensable para acceder a bonos verdes y financiación climática multilateral."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_06011837)
    # Inject before the next subject marker: 03041821
    inject_topics_after('      - codigo: "03041821"', yaml_text)
    print("06011837 Conversión de Energía successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
