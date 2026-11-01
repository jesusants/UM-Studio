# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_05011834 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Metodología CDIO y Estándares Internacionales de Formación en Ingeniería",
        "objetivo": "Apropiar el marco pedagógico y profesional CDIO (Conceive - Design - Implement - Operate) del MIT y KTH, planificando proyectos de ingeniería energética con enfoque sistémico y ciclo de vida completo.",
        "concepto_clave_latex": r"\text{Ciclo CDIO}: \text{Concebir (C)} \to \text{Diseñar (D)} \to \text{Implementar (I)} \to \text{Operar (O)} \quad ; \quad \text{Estándares 1 a 12}",
        "ejemplo": "Problema 1: Un equipo de cuatro estudiantes de Ingeniería Energética de la Universidad del Magdalena formula el proyecto integrador CDIO I: 'Diseño e implementación de un generador termoeléctrico de recuperación de calor (TEG) acoplado al tubo de escape de un motogenerador diésel rural'. El proyecto debe estructurarse conforme a los 12 Estándares CDIO: 1) Estándar 1 (El Contexto): El proyecto concibe, diseña, implementa y opera un sistema físico real resolviendo una necesidad auténtica de electrificación rural en el Magdalena. 2) Estándar 2 (Resultados de Aprendizaje): Se definen competencias técnicas disciplinarias (termodinámica de Seebeck, transferencia de calor, electrónica de conversión DC/DC), habilidades interpersonales (liderazgo compartido, resolución de conflictos de equipo) y construcción de sistemas. 3) Plan de Fases Temporales: Semanas 1 a 4: Fase Concebir (definición del problema, estado del arte, requerimientos del cliente, estudio de patentes); Semanas 5 a 9: Fase Diseñar (balances térmicos, modelado CAD 3D, selección de módulos Peltier/Seebeck, diseño del circuito MPPT); Semanas 10 a 14: Fase Implementar (mecanizado de intercambiadores de calor en taller, soldadura de termocuplas, programación de firmware en microcontrolador ESP32); Semanas 15 a 16: Fase Operar (puesta en marcha en banco de pruebas del laboratorio de energía, medición de curva de potencia P-V, análisis de fallas y desmantelamiento seguro). La matriz de trazabilidad CDIO demuestra que el 100% de los entregables técnicos y sustentaciones orales se alinean con las rúbricas internacionales de acreditación ABET (Criterios 1 al 7). Problema 2: En la autoevaluación grupal CDIO, la aplicación de la evaluación por pares 360° (Peer Assessment) identifica desviaciones en la carga de trabajo entre miembros del equipo antes de que afecten el cronograma crítico.",
        "bloque_sugerido": "Metodología CDIO 45 min • Los 12 estándares CDIO del MIT y ciclo de vida de proyectos",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL PARADIGMA DE FORMACIÓN CDIO",
                "titulo": "Concebir - Diseñar - Implementar - Operar",
                "puntos": [
                    "Iniciativa internacional fundada por MIT, KTH, Chalmers y Linköping University en el año 2000.",
                    "Supera la educación teórica pasiva memorística; educa a los ingenieros en el contexto de la práctica real.",
                    "Enfatiza tanto las ciencias fundamentales de la ingeniería como el trabajo en equipo multidisciplinar y la ética."
                ]
            },
            {
                "numero": 2,
                "seccion": "LOS 12 ESTÁNDARES CDIO",
                "titulo": "De la Misión al Espacio de Aprendizaje",
                "puntos": [
                    "Currículo Integrado: Conecta las matemáticas, la física y los circuitos en proyectos aplicados tangibles.",
                    "Experiencias de Diseño e Implementación: Talleres donde los estudiantes construyen prototipos con sus propias manos.",
                    "Espacios de Trabajo de Ingeniería (Makerspaces): Laboratorios con impresoras 3D, osciloscopios y herramientas CNC."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Formulación del Problema y Metodología de Marco Lógico en Ingeniería Energética",
        "objetivo": "Estructurar la problemática técnica, social y ambiental de un proyecto mediante el Árbol de Causas-Efectos y la Matriz de Marco Lógico (MML) con Indicadores Objetivamente Verificables (IOV).",
        "concepto_clave_latex": r"\text{MML} = \begin{bmatrix} \text{Fin} & \text{Indicador} & \text{Medio Verificación} & \text{Supuestos} \\ \text{Propósito} & \text{IOV} & \text{Fuentes} & \text{Riesgos} \\ \text{Componentes} & \text{Metas} & \text{Informes} & \text{Factores} \\ \text{Actividades} & \text{Presupuesto} & \text{Facturas} & \text{Condiciones} \end{bmatrix}",
        "ejemplo": "Problema 1: En una comunidad pesquera de Tasajera, Magdalena, la falta de refrigeración confiable provoca la descomposición de hasta el 35% de la pesca artesanal diaria antes de su comercialización. Se formula el proyecto integrador bajo la Metodología de Marco Lógico (MML): 1) Árbol de Problemas: Problema Central: 'Elevada pérdida económica y descomposición de pescado fresco por déficit de cadena de frío en Tasajera'. Causas Raíz (Nivel 1): a) Ausencia de suministro eléctrico continuo de red (red inestable con cortes de 18 horas/semana); b) Alto costo del hielo transportado en camiones desde Barranquilla (12,000 COP por bloque de 25 kg); c) Desconocimiento de tecnologías solares térmicas y fotovoltaicas. Efectos Directos: Pérdida del 35% de ingresos de los pescadores, proliferación de enfermedades gastrointestinales por consumo de producto deteriorado y dependencia de intermediarios informales. 2) Árbol de Objetivos: Transformación de causas en medios y efectos en fines positivos (Propósito Central: 'Implementar un prototipo de máquina de hielo en escamas alimentada por energía solar fotovoltaica con almacenamiento térmico de salmuera para cooperativas de pesca'). 3) Matriz de Marco Lógico (MML): Propósito: Producir 150 kg de hielo diarios a -5 °C. Indicador Objetivamente Verificable (IOV): Capacidad de congelación verificada de 150 +- 5 kg/día con disponibilidad del 95% auditada durante 30 días continuos. Medio de Verificación: Registros automatizados de báscula digital y datalogger de temperatura en tiempo real. Supuestos Críticos: Las condiciones de radiación solar en la Ciénaga Grande no descienden por debajo de 4.5 kWh/m^2-día y la comunidad aporta un operador local capacitado para el mantenimiento de filtros de agua. Problema 2: En la definición del problema técnico, el error de formular el problema como la 'falta de una solución preconcebida' (ej. 'falta una planta solar') sesga el espacio de diseño impidiendo evaluar alternativas más eficientes como biodigestores o bombas de calor.",
        "bloque_sugerido": "Marco Lógico 45 min • Construcción de árbol de problemas, árbol de objetivos y matriz MML",
        "slides": [
            {
                "numero": 1,
                "seccion": "INGENIERÍA CENTRADA EN NECESIDADES REALES",
                "titulo": "El Diagnóstico Causa-Efecto",
                "puntos": [
                    "Los ingenieros aficionados proponen soluciones antes de entender el problema real.",
                    "El Árbol de Problemas descompone las causas raíces subyacentes diferenciándolas de los síntomas superficiales.",
                    "Asegura la pertinencia social y pertinencia técnica del proyecto en el territorio del Magdalena."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA MATRIZ DE MARCO LÓGICO (MML)",
                "titulo": "Lógica Vertical y Horizontal de Proyecto",
                "puntos": [
                    "Lógica Vertical (Fin -> Propósito -> Componentes -> Actividades): Garantiza causalidad estricta paso a paso.",
                    "Lógica Horizontal (Objetivos -> Indicadores -> Medios de Verificación -> Supuestos): Permite la auditoría objetiva de resultados.",
                    "Metodología estándar exigida por el Banco Mundial, BID, MinCiencias y las regalías del SGR en Colombia."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Vigilancia Tecnológica y Mapeo de Patentes en Energías Renovables (WIPO/Espacenet)",
        "objetivo": "Realizar búsquedas estructuradas de patentes y literatura científica indexada aplicando operadores booleanos y códigos de clasificación IPC/CPC para determinar el estado de la técnica y la libertad de operación (FTO).",
        "concepto_clave_latex": r"\text{Ecuación de Búsqueda}: (\text{Solar Tracker} \text{ OR } \text{Heliostat}) \text{ AND } (\text{CPC}: \text{Y02E10/50}) \text{ AND } (\text{Backtracking})",
        "ejemplo": "Problema 1: Un equipo de desarrollo proyecta patentar un mecanismo de acoplamiento elástico amortiguador para mitigar oscilaciones aeroelásticas por flameo (flutter) en tubos de torsión de seguidores solares monoaxiales. Antes de iniciar el diseño de detalle, se ejecuta un estudio de Vigilancia Tecnológica y Libertad de Operación (Freedom to Operate - FTO) en las bases de datos mundiales de patentes Patentscope (WIPO), Espacenet (EPO) y Google Patents: 1) Identificación de Códigos de Clasificación Cooperativa de Patentes (CPC): Clase Y02E 10/50 (Sistemas fotovoltaicos de energía solar); Subclase F24S 30/425 (Monturas de seguimiento alrededor de un único eje horizontal); F16F 15/02 (Supresión de vibraciones mecánicas mediante amortiguadores). 2) Ecuación de Búsqueda Booleana Avanzada: ((solar tracker OR single axis tracker) AND (torque tube OR drive tube) AND (torsional damper OR flutter OR aeroelastic) AND (CPC = F24S 30/425 OR CPC = F16F 15/00)). 3) Análisis de Resultados: La búsqueda arroja 142 patentes concedidas. Se analizan las reivindicaciones independientes (claims) de las patentes dominantes de competidores internacionales: Patente US 10,855,220 B2 (Nextracker) reivindica amortiguadores hidráulicos de doble efecto con válvulas de corte por velocidad fijadas rígidamente al pilote. Patente EP 3,425,302 B1 (Soltec) reivindica algoritmos de bloqueo angular preventivo a 60°. 4) Determinación de Novedad y FTO: El mecanismo propuesto por los estudiantes utiliza un amortiguador de fricción elastomérico rotativo no lineal integrado dentro del rodamiento central. Al no invadir las reivindicaciones de las patentes activas de la competencia, se dictamina Libertad de Operación positiva (FTO = VIABLE) y se confirma Novedad inventiva y Actividad Inventiva, permitiendo radicar una solicitud de Patente de Modelo de Utilidad ante la Superintendencia de Industria y Comercio (SIC) de Colombia. Problema 2: En la vigilancia científica con Scopus y Web of Science, el análisis bibliométrico con VOSviewer mapea las redes de co-citación e identifica a los investigadores y laboratorios líderes a nivel mundial.",
        "bloque_sugerido": "Vigilancia Tecnológica 45 min • Ecuaciones de patentes CPC, análisis de reivindicaciones y FTO",
        "slides": [
            {
                "numero": 1,
                "seccion": "PROPIEDAD INTELECTUAL EN INGENIERÍA",
                "titulo": "Patentes de Invención vs Modelos de Utilidad",
                "puntos": [
                    "Más del 80% de toda la información tecnológica del mundo solo se publica en documentos de patentes, nunca en revistas científicas.",
                    "Patente de Invención (20 años de exclusividad): Exige Novedad Mundial, Nivel Inventivo y Aplicación Industrial.",
                    "Modelo de Utilidad (10 años de exclusividad): Protege mejoras funcionales o adaptaciones en la forma de herramientas y dispositivos mecánicos."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTUDIOS DE LIBERTAD DE OPERACIÓN (FTO)",
                "titulo": "Evitando Demandas por Infracción",
                "puntos": [
                    "Construir y vender un producto que infrinja las reivindicaciones de una patente ajena activa conlleva millonarias demandas judiciales y decomisos.",
                    "El análisis FTO debe realizarse al inicio de la fase Concebir (CDIO), no al final del proyecto.",
                    "Identifica patentes caducadas de dominio público que pueden ser copiadas y mejoradas legalmente sin pagar regalías."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Definición de Requerimientos y Despliegue de la Función de Calidad (QFD / House of Quality)",
        "objetivo": "Traducir los requerimientos cualitativos de los usuarios ('Voz del Cliente' - VOC) en especificaciones de ingeniería cuantitativas mediante la matriz QFD (House of Quality).",
        "concepto_clave_latex": r"\text{Importancia Técnica}_j = \sum_{i=1}^m w_i \cdot R_{ij} \quad ; \quad R_{ij} \in \{ 0: \text{Nula}, 1: \text{Baja}, 3: \text{Media}, 9: \text{Fuerte} \}",
        "ejemplo": "Problema 1: Un equipo de proyecto CDIO diseña un deshidratador solar híbrido para pequeños productores de mango y banano en la Zona Bananera del Magdalena. Mediante encuestas y entrevistas de campo a 25 campesinos, se identifican las 4 demandas prioritarias de la Voz del Cliente (VOC) ponderadas por importancia en escala 1 a 5: 1) 'Bajo costo de compra y repuestos' (peso w_1 = 5); 2) 'Secado rápido en menos de 8 horas' (w_2 = 4); 3) 'Fácil de operar y limpiar por una sola persona' (w_3 = 4); 4) 'Operación continua en días nublados o noche' (w_4 = 3). El equipo formula 4 especificaciones técnicas medibles de ingeniería (HOWs): a) Potencia del calefactor eléctrico auxiliar (P_aux en Watts); b) Flujo volumétrico de aire forzado del ventilador (CFM); c) Área superficial de captación del colector solar plano (A_col en m^2); d) Masa total del equipo vacío (M_total en kg). Se construye la Matriz de Relaciones QFD (asignando puntuación de correlación: 9 = Fuerte, 3 = Moderada, 1 = Débil, 0 = Nula): - 'Secado rápido': Correlación fuerte (9) con Flujo CFM, fuerte (9) con Área A_col y fuerte (9) con Potencia P_aux. - 'Bajo costo': Correlación moderada inversa (3) con Área y Potencia (mayor área = mayor costo), y débil (1) con Masa. - 'Fácil de operar/limpiar': Correlación fuerte (9) con Masa reducida. - 'Operación nocturna': Correlación fuerte (9) con Potencia auxiliar P_aux. Cálculo del Peso Técnico Ponderado de cada parámetro de ingeniería: Para el Área del colector A_col: Peso = (5 * 3) + (4 * 9) + (4 * 0) + (3 * 0) = 15 + 36 = 51 puntos. Para el Flujo CFM: Peso = (5 * 1) + (4 * 9) + (4 * 3) + (3 * 0) = 5 + 36 + 12 = 53 puntos. Para la Potencia auxiliar P_aux: Peso = (5 * 3) + (4 * 9) + (4 * 0) + (3 * 9) = 15 + 36 + 27 = 78 puntos (Máxima prioridad de ingeniería). Para la Masa total M_total: Peso = (5 * 1) + (4 * 0) + (4 * 9) + (3 * 0) = 5 + 36 = 41 puntos. El tejado de correlaciones de la Casa de la Calidad revela una correlación fuertemente negativa entre Masa reducida y Área grande del colector. La especificación técnica final fija: P_aux = 1500 W con termostato PID, CFM = 120 CFM y A_col = 2.0 m^2, resolviendo el compromiso óptimo. Problema 2: En la matriz QFD, la inclusión del benchmarking competitivo evalúa el rendimiento del prototipo propuesto frente a 2 secadores comerciales del mercado, identificando las ventajas competitivas diferenciadoras.",
        "bloque_sugerido": "Diseño QFD 45 min • Construcción de la Casa de la Calidad y ponderación técnica VOC",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE LA VOZ DEL CLIENTE A LA INGENIERÍA",
                "titulo": "Quality Function Deployment (QFD)",
                "puntos": [
                    "Metodología creada por Yoji Akao en Mitsubishi Heavy Industries en 1966.",
                    "Impide que los ingenieros diseñen lo que ellos 'creen' que el usuario necesita en lugar de lo que realmente requiere.",
                    "Transforma deseos cualitativos ambiguos ('que sea rápido', 'que sea barato') en métricas de laboratorio cuantificables (m/s, USD, kg)."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA CASA DE LA CALIDAD (HOUSE OF QUALITY)",
                "titulo": "Anatomía de la Matriz QFD",
                "puntos": [
                    "El 'Qué' (WHATS): Requerimientos y necesidades del cliente con pesos de ponderación.",
                    "El 'Cómo' (HOWS): Características de ingeniería y especificaciones de diseño medibles.",
                    "La Matriz Central: Grado de correlación (0, 1, 3, 9) entre los Qué y los Cómo.",
                    "El Tejado: Conflictos y sinergias físicas entre las especificaciones técnicas (Trade-offs)."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Generación Sistemática de Conceptos y Morfología de Soluciones (Zwicky Box)",
        "objetivo": "Aplicar métodos estructurados de creatividad e ideación (análisis morfológico de Zwicky y lluvia de ideas inversa) para generar un espacio exhaustivo de conceptos de solución técnica.",
        "concepto_clave_latex": r"N_{\text{combinaciones}} = \prod_{i=1}^k m_i \quad ; \quad \text{Espacio Morfológico de Zwicky}",
        "ejemplo": "Problema 1: Se desarrolla un sistema de limpieza automatizada de paneles solares para mitigar las pérdidas por ensuciamiento (soiling) en el desierto de La Guajira, donde el recurso hídrico es extremadamente escaso. El equipo descompone el sistema en 5 subfunciones técnicas fundamentales y define las alternativas viables para cada una mediante una Caja Morfológica de Zwicky: 1) Subfunción 1: Medio de Limpieza [A1: Cepillos secos rotativos de microfibra; A2: Aspersión de agua presurizada; A3: Limpieza electrostática por onda viajera de alto voltaje; A4: Aire comprimido pulsado]. (m_1 = 4 alternativas). 2) Subfunción 2: Sistema de Tracción / Desplazamiento [B1: Orugas de caucho sobre marco del módulo; B2: Ruedas guiadas por cables tensores; B3: Robot aéreo tipo dron con tobera; B4: Marco pórtico móvil sobre riel fijo]. (m_2 = 4 alternativas). 3) Subfunción 3: Fuente de Energía [C1: Batería de iones de litio integrada recargable; C2: Cable umbilical retráctil desde inversor; C3: Pequeño panel solar propio con supercondensadores]. (m_3 = 3 alternativas). 4) Subfunción 4: Sistema de Navegación y Detección de Bordes [D1: Sensores de distancia ultrasónicos; D2: Finales de carrera mecánicos de contacto; D3: Visión artificial con cámara LiDAR]. (m_4 = 3 alternativas). 5) Subfunción 5: Retorno y Estación de Carga [E1: Estación base de acoplamiento automático en extremo de fila; E2: Retorno manual por operario]. (m_5 = 2 alternativas). Número total de combinaciones de conceptos posibles en el espacio morfológico: N = 4 * 4 * 3 * 3 * 2 = 288 conceptos de diseño independientes. El equipo selecciona y documenta tres conceptos contrastantes: Concepto Alfa (A1-B1-C1-D1-E1: Robot oruga autónomo de cepillo seco con batería Li-ion); Concepto Beta (A3-B4-C2-D2-E1: Sistema electrostático fijo con riel guiado); Concepto Gamma (A4-B3-C1-D3-E2: Dron de soplado con navegación visual). Problema 2: El análisis de incompatibilidad técnica descarta inmediatamente combinaciones inviables (ej. dron con cable umbilical pesado o aspersión de agua en zonas sin acueducto), reduciendo el espacio de búsqueda a 36 conceptos evaluables.",
        "bloque_sugerido": "Ideación Morfológica 45 min • Caja morfológica de Zwicky y generación sistemática de conceptos",
        "slides": [
            {
                "numero": 1,
                "seccion": "CREATIVIDAD SISTEMÁTICA EN INGENIERÍA",
                "titulo": "Superando el Bloqueo Mental y la Fijación de Diseño",
                "puntos": [
                    "Fijación de diseño: Tendencia inconsciente de los ingenieros a copiar la primera solución que vieron en internet.",
                    "Descomposición funcional: Dividir un problema complejo e inmanejable en subfunciones simples e independientes.",
                    "El análisis morfológico de Fritz Zwicky fuerza a explorar combinaciones no convencionales que dan lugar a patentes."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA CAJA MORFOLÓGICA",
                "titulo": "Exploración Combinatoria del Espacio de Soluciones",
                "puntos": [
                    "Fila superior: Las funciones esenciales que el producto debe realizar sí o sí.",
                    "Columnas: Las múltiples maneras físicas, biológicas o químicas de cumplir cada función.",
                    "Permite visualizar cientos de conceptos viables en una sola tabla matricial de síntesis."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Matriz de Pugh y Selección Multicriterio de la Arquitectura Óptima de Proyecto",
        "objetivo": "Evaluar y seleccionar objetivamente el mejor concepto de ingeniería mediante la Matriz de Selección de Conceptos de Pugh (Pugh Matrix) comparando candidatos contra una línea base de referencia (Datum).",
        "concepto_clave_latex": r"\text{Score}_k = \sum_{j=1}^n w_j \cdot S_{jk} \quad ; \quad S_{jk} \in \{ +1: \text{Mejor}, 0: \text{Igual}, -1: \text{Peor que el Datum} \}",
        "ejemplo": "Problema 1: Un equipo de estudiantes de CDIO I debe seleccionar la arquitectura óptima para un aerogenerador de eje vertical (VAWT) para bombeo de agua en comunidades de la Sierra Nevada de Santa Marta. Se comparan 3 conceptos generados en la fase morfológica frente a una solución comercial de referencia tomada como Datum (Aerogenerador multipala tradicional americano tipo molino de viento de chapa galvanizada): Concepto A (Rotor Savonius helicoidal de dos etapas en fibra de vidrio); Concepto B (Rotor Darrieus con álabes trocopoidales de perfil NACA 0018); Concepto C (Rotor híbrido Darrieus-Savonius concéntrico combinado). Se definen 6 criterios de selección ponderados de 1 a 5 según su relevancia para la comunidad: 1) Par de arranque a baja velocidad de viento (w_1 = 5); 2) Eficiencia aerodinámica máxima C_p (w_2 = 4); 3) Simplicidad de fabricación local y mantenimiento (w_3 = 5); 4) Resistencia estructural a vientos huracanados (w_4 = 4); 5) Costo total de materiales (w_5 = 4); 6) Nivel de ruido e impacto visual (w_6 = 2). Matriz de Pugh Ponderada (asignando puntuación relativa frente al Datum: +1 Mejor, 0 Igual, -1 Peor): - Criterio 1 (Par de arranque, w=5): A(+1), B(-1), C(+1), Datum(0). - Criterio 2 (Eficiencia C_p, w=4): A(-1), B(+1), C(+1), Datum(0). - Criterio 3 (Fabricación local, w=5): A(+1), B(-1), C(0), Datum(0). - Criterio 4 (Resistencia estructural, w=4): A(+1), B(-1), C(0), Datum(0). - Criterio 5 (Costo de materiales, w=4): A(+1), B(-1), C(0), Datum(0). - Criterio 6 (Bajo ruido, w=2): A(+1), B(0), C(+1), Datum(0). Cálculo de Puntuaciones Ponderadas: Para Concepto A: (5*1) + (4*-1) + (5*1) + (4*1) + (4*1) + (2*1) = 5 - 4 + 5 + 4 + 4 + 2 = +16 puntos. Para Concepto B: (5*-1) + (4*1) + (5*-1) + (4*-1) + (4*-1) + (2*0) = -5 + 4 - 5 - 4 - 4 + 0 = -14 puntos (Descartado por nulo par de arranque y fragilidad estructural). Para Concepto C: (5*1) + (4*1) + (5*0) + (4*0) + (4*0) + (2*1) = 5 + 4 + 0 + 0 + 0 + 2 = +11 puntos. Para el Datum: 0 puntos. Decisión de Ingeniería: El Concepto A (Savonius helicoidal) resulta ganador indiscutible (+16 puntos) gracias a su extraordinario par de arranque, bajo costo y facilidad de reparación con recursos locales de la Sierra Nevada. Problema 2: En la etapa de mejora de conceptos (Combine & Improve), los atributos sobresalientes del Concepto C se integran en el Concepto A añadiendo deflectores estatóricos aerodinámicos exteriores.",
        "bloque_sugerido": "Selección de Conceptos 45 min • Matriz de decisión de Pugh ponderada y análisis de trade-offs",
        "slides": [
            {
                "numero": 1,
                "seccion": "DECISIONES BASADAS EN EVIDENCIA",
                "titulo": "La Matriz de Selección de Stuart Pugh",
                "puntos": [
                    "Evita que el concepto ganador se elija por la elocuencia o jerarquía del estudiante más dominante del equipo.",
                    "Compara rigurosamente los pros y contras de cada candidato frente a un estándar conocido de la industria (Datum).",
                    "Método iterativo: estimula la hibridación combinando las fortalezas de dos conceptos para crear una solución superior."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIOS DE SELECCIÓN",
                "titulo": "Ponderación y Sensibilidad",
                "puntos": [
                    "Los criterios deben reflejar los requerimientos técnicos y las restricciones de costo y manufactura del QFD.",
                    "Análisis de Sensibilidad: Evalúa si el concepto ganador cambia al modificar ligeramente los pesos ponderados.",
                    "Cierra formalmente la fase Concebir (C) del CDIO, habilitando el inicio del Diseño de Detalle (D)."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Dimensionamiento Preliminar y Balances de Masa y Energía de la Solución",
        "objetivo": "Formular los balances termodinámicos analíticos de primer principio y dimensionar las especificaciones preliminares de capacidad, potencia y flujo del concepto seleccionado.",
        "concepto_clave_latex": r"\dot{Q} - \dot{W} = \sum \dot{m}_{out} h_{out} - \sum \dot{m}_{in} h_{in} \quad ; \quad \eta_{\text{sistema}} = \prod_{i=1}^k \eta_i",
        "ejemplo": "Problema 1: Tras seleccionar el concepto de deshidratador solar de frutas con colector de aire y almacenamiento térmico en piedras para secar una carga de m_fruta = 100 kg de rodajas de mango verde por lote en 8 horas continuas (t = 28,800 s): Parámetros termodinámicos: Humedad inicial de la fruta w_i = 85% en base húmeda; humedad final de conservación segura exigida por norma sanitaria w_f = 12%. 1) Balance de Masa de Agua a Evaporar: Masa de sólidos secos: m_ss = m_fruta * (1 - w_i) = 100 * (1 - 0.85) = 15.0 kg. Masa final del producto seco: m_final = m_ss / (1 - w_f) = 15.0 / (1 - 0.12) = 15.0 / 0.88 = 17.05 kg. Masa total de agua que debe removerse: m_w = m_fruta - m_final = 100 - 17.05 = 82.95 kg de agua. Flujo másico de evaporación medio: dot{m}_w = 82.95 kg / 28,800 s = 2.88 * 10^-3 kg/s. 2) Balance de Energía Térmica Requerida: Entalpía de vaporización del agua a 55 °C: h_fg = 2370 kJ/kg. Energía latente neta: E_latente = m_w * h_fg = 82.95 kg * 2370 kJ/kg = 196,591 kJ = 54.61 kWh. Considerando una eficiencia térmica de la cámara de secado del 45% (pérdidas en el aire de escape y paredes): Demanda térmica total requerida: E_termica = 54.61 / 0.45 = 121.35 kWh térmicos. Potencia térmica media: Q_th = 121.35 kWh / 8 h = 15.17 kW_th. 3) Dimensionamiento del Colector Solar de Aire: Radiación solar útil diaria en la zona: H = 5.2 kWh/m^2-día. Eficiencia térmica media del colector solar plano con placa absorbedora corrugada y cubierta de policarbonato: eta_col = 42%. Área de colectores solares requerida: A_col = E_termica / (H * eta_col) = 121.35 / (5.2 * 0.42) = 121.35 / 2.184 = 55.56 m^2. Dado que 55.6 m^2 es inviable para un prototipo compacto de laboratorio, se redimensiona el prototipo a escala piloto para 10 kg de mango (área A_col = 5.56 m^2, 3 colectores comerciales de 2 x 1 m) acoplado a un lecho de piedras de grava basáltica de 350 kg como acumulador térmico sensible. Problema 2: El cálculo del caudal volumétrico del ventilador de aire caliente verifica que una velocidad de aire de 1.2 m/s sobre las bandejas optimiza el coeficiente de transferencia de masa por convección forzada h_m sin arrastrar físicamente las rodajas.",
        "bloque_sugerido": "Balances de Ingeniería 45 min • Balances de masa/energía de secado y dimensionamiento de colectores",
        "slides": [
            {
                "numero": 1,
                "seccion": "DE LA IDEA A LOS NÚMEROS",
                "titulo": "Balances de Conservación Rigurosos",
                "puntos": [
                    "Un proyecto de ingeniería no puede basarse en dimensiones arbitrarias o empíricas sin sustento analítico.",
                    "Balance de Materia: Toda masa que entra debe salir o acumularse dentro de las fronteras de control del sistema.",
                    "Balance de Energía: Cuantifica los requerimientos de calor, potencia de compresión y flujo de aire necesarios."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESCALADO TÉCNICO DE PROTOTIPOS",
                "titulo": "Semejanza Geométrica y Operativa",
                "puntos": [
                    "Si el proyecto industrial a escala completa es inabarcable con el presupuesto del curso, se diseña un prototipo a escala representativo.",
                    "El prototipo a escala debe preservar números adimensionales críticos (Reynolds, Biot, Nusselt).",
                    "Garantiza que las conclusiones y curvas de eficiencia del prototipo sean extrapolables a escala comercial."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Gestión del Proyecto: Estructura de Desglose del Trabajo (WBS/EDT) y Ruta Crítica (CPM/PERT)",
        "objetivo": "Planificar la ejecución del proyecto integrador mediante la Estructura de Desglose del Trabajo (EDT/WBS), calculando la Ruta Crítica (CPM) y holguras temporales para mitigar riesgos de retraso.",
        "concepto_clave_latex": r"\text{Duración Esperada PERT}: t_e = \frac{a + 4m + b}{6} \quad ; \quad \text{Holgura Total}: H_i = LS_i - ES_i = 0 \implies \text{Ruta Crítica}",
        "ejemplo": "Problema 1: Un equipo CDIO planifica las 16 semanas del semestre para construir un prototipo de biodigestor anaeróbico automatizado con agitación magnética y monitoreo de pH/CH4. Se estructura la WBS jerárquica descompuesta en 6 paquetes de trabajo principales con sus actividades, dependencias y tiempos estimados por método PERT (en días hábiles): A: Diseño de detalle y cálculos térmicos (a=4, m=6, b=8 ==> t_e = [4 + 4*6 + 8]/6 = 36/6 = 6 días; sin predecesores). B: Compra y recepción de materiales COTS (t_e = 10 días; predecesor A). C: Mecanizado y soldadura del reactor en taller (t_e = 12 días; predecesor B). D: Diseño y fabricación de tarjeta PCB de control (t_e = 8 días; predecesor A). E: Programación de firmware y calibración de sensores en banco (t_e = 7 días; predecesor D). F: Integración mecánica y electrónica final (t_e = 5 días; predecesores C y E). G: Puesta en marcha, inoculación y pruebas experimentales de producción de biogás (t_e = 14 días; predecesor F). H: Redacción de artículo IEEE y póster final (t_e = 6 días; predecesor G). Red de Flechas y Cálculo de Ruta Crítica (CPM): 1) Rama 1 (Mecánica): Inicio -> A(6) -> B(10) -> C(12) -> F(5) -> G(14) -> H(6) -> Fin. Duración total = 6 + 10 + 12 + 5 + 14 + 6 = 53 días. 2) Rama 2 (Electrónica): Inicio -> A(6) -> D(8) -> E(7) -> F(5) -> G(14) -> H(6) -> Fin. Duración total = 6 + 8 + 7 + 5 + 14 + 6 = 46 días. Análisis de Holguras: La Rama 1 es la RUTA CRÍTICA gobernante (duración máxima de 53 días hábiles = 10.6 semanas de trabajo). Las actividades A, B, C, F, G y H tienen Holgura Total cero (H = 0); cualquier retraso de un solo día en la compra o mecanizado de taller atrasa directamente la entrega del proyecto final. Las actividades electrónicas D y E tienen una holgura libre de 7 días (53 - 46 = 7 días), lo que permite absorber demoras en la llegada de componentes electrónicos sin impactar la fecha de entrega. Problema 2: En la gestión ágil con tableros Kanban (Trello / Jira), el límite de trabajo en curso (WIP limit = 3 tareas activas por estudiante) previene el bloqueo de actividades y cuellos de botella en la fase constructiva.",
        "bloque_sugerido": "Gestión de Proyectos 45 min • WBS, cálculo de ruta crítica CPM y diagramas de Gantt",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRUCTURACIÓN DEL TRABAJO",
                "titulo": "Work Breakdown Structure (WBS / EDT)",
                "puntos": [
                    "La WBS descompone el proyecto en paquetes de trabajo manejables orientados a entregables tangibles.",
                    "Regla del 100%: La suma de los paquetes de trabajo de nivel inferior debe abarcar el 100% del alcance del proyecto, ni más ni menos.",
                    "Cada paquete de trabajo debe tener un único líder responsable asignado con entregables fechados."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL MÉTODO DE LA RUTA CRÍTICA (CPM)",
                "titulo": "Identificación de Cuellos de Botella",
                "puntos": [
                    "Ruta Crítica: La secuencia de actividades dependientes que determina la duración total mínima del proyecto.",
                    "Actividades críticas tienen Holgura Cero; si se atrasan un día, todo el proyecto se atrasa un día.",
                    "Permite a los estudiantes enfocar sus recursos y horas de taller en las tareas verdaderamente prioritarias."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Presupuestación, Estructura de Costos CAPEX/OPEX y Viabilidad Financiera (VAN/TIR)",
        "objetivo": "Elaborar el presupuesto de ingeniería detallado desagregando costos directos e indirectos (CAPEX/OPEX) y evaluar la viabilidad financiera mediante Valor Actual Neto (VAN), Tasa Interna de Retorno (TIR) y Período de Recuperación (Payback).",
        "concepto_clave_latex": r"\text{VAN} = \sum_{t=1}^n \frac{\text{FC}_t}{(1 + r)^t} - \text{CAPEX} = 0 \implies r = \text{TIR} \quad ; \quad \text{B/C} = \frac{\text{VP}(\text{Beneficios})}{\text{VP}(\text{Costos})} > 1.0",
        "ejemplo": "Problema 1: Un equipo de proyecto CDIO I estructura la viabilidad tecnoeconómica de una planta piloto de generación de biogás y biofertilizante para una granja porcícola de 200 cerdos en Ciénaga. Presupuesto detallado de inversión de capital inicial (CAPEX): Materiales mecánicos (reactor de polietileno de 10 m^3, tuberías PVC, válvulas de alivio, manómetros) = 3,850,000 COP; Instrumentación y electrónica (sensores de metano NDIR, transmisor de pH, electroválvula proporcional, microcontrolador industrial) = 2,450,000 COP; Obra civil menor (fosa de cimentación y caseta de control) = 1,800,000 COP; Mano de obra especializada de montaje e ingeniería = 1,900,000 COP; Imprevistos de ingeniería (10%) = 1,000,000 COP. CAPEX total inicial de inversión: I_0 = 11,000,000 COP. Costos de operación y mantenimiento anual (OPEX): Mantenimiento de sellos, insumos químicos de calibración y recambio de filtros de sulfhídrico H2S = 1,200,000 COP/año. Flujos de ingresos y ahorros anuales generados por la planta (Flujo de Caja): 1) Sustitución de 32 cilindros de gas GLP de 33 lb al año para cocción y calefacción de lechones = 32 * 95,000 COP = 3,040,000 COP/año; 2) Producción y venta de 4,000 litros de biol líquido concentrado (biofertilizante orgánico rico en N-P-K) a 1,500 COP/litro = 6,000,000 COP/año. Ahorro e ingreso total bruto = 9,040,000 COP/año. Flujo de caja neto anual constante: FC = Ingresos - OPEX = 9,040,000 - 1,200,000 = 7,840,000 COP/año durante una vida útil evaluada de n = 5 años. Tasa de descuento de oportunidad del agricultor r = 12% anual. 1) Valor Actual Neto (VAN): Factor de actualización de anualidad: FVA = [1 - (1 + 0.12)^-5] / 0.12 = [1 - 0.5674] / 0.12 = 0.4326 / 0.12 = 3.6048. Valor presente de los flujos: VP = 7,840,000 * 3.6048 = 28,261,450 COP. VAN = VP - I_0 = 28,261,450 - 11,000,000 = +17,261,450 COP. 2) Tasa Interna de Retorno (TIR): Se resuelve VAN(r) = 0: FC * [(1 - (1+TIR)^-5)/TIR] = 11,000,000 ==> [(1 - (1+TIR)^-5)/TIR] = 11,000,000 / 7,840,000 = 1.403. Interpolando iterativamente se obtiene una TIR = 64.8% anual (excepcionalmente atractiva frente a la tasa de corte del 12%). 3) Período simple de recuperación de la inversión (Payback): Payback = I_0 / FC = 11,000,000 / 7,840,000 = 1.40 años (recuperación total de la inversión en solo 1 año y 5 meses). El proyecto se aprueba como altamente rentable y bancable. Problema 2: El análisis de sensibilidad financiero evalúa el impacto de una caída del 20% en el precio de venta del biofertilizante y un sobrecosto del 15% en el CAPEX, demostrando que el proyecto mantiene un VAN positivo superior a 8 millones de COP.",
        "bloque_sugerido": "Evaluación Financiera 45 min • Presupuesto CAPEX/OPEX, cálculo de VAN, TIR y Payback",
        "slides": [
            {
                "numero": 1,
                "seccion": "ECONOMÍA DE LA INGENIERÍA",
                "titulo": "Presupuestación y Clasificación de Costos",
                "puntos": [
                    "CAPEX (Capital Expenditures): Gastos iniciales en compra de activos fijos, equipos, herramientas e infraestructura.",
                    "OPEX (Operational Expenditures): Costos recurrentes para mantener el sistema operando (energía, reactivos, salarios, seguros).",
                    "Lista de Materiales (BOM) costea cada tornillo, relé y metro de cable con cotizaciones reales de proveedores locales."
                ]
            },
            {
                "numero": 2,
                "seccion": "INDICADORES DE RENTABILIDAD",
                "titulo": "VAN, TIR y Relación Beneficio/Costo",
                "puntos": [
                    "VAN > 0: El proyecto genera más riqueza que invertir el dinero a la tasa de interés de oportunidad; inversión viable.",
                    "TIR: La tasa máxima de financiamiento bancario que el proyecto puede soportar sin entrar en pérdidas.",
                    "Criterio decisivo para convencer a inversores privados y obtener fondos de incubadoras de base tecnológica."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis de Modos y Efectos de Falla (FMEA / AMFE) y Seguridad del Prototipo",
        "objetivo": "Identificar riesgos técnicos, operacionales y ambientales mediante la matriz FMEA (Failure Mode and Effects Analysis), calculando el Número de Prioridad de Riesgo (NPR / RPN) e implementando acciones correctivas.",
        "concepto_clave_latex": r"\text{NPR / RPN} = S \times O \times D \quad (1 \le \text{NPR} \le 1000) \quad ; \quad \text{Umbral de Acción}: \text{NPR} \ge 100",
        "ejemplo": "Problema 1: Se elabora el FMEA de diseño y proceso para un prototipo de gasificador de biomasa de flujo descendente (downdraft) de 15 kW_th que utiliza cascarilla de café para producir gas de síntesis (syngas rico en CO y H2). Se evalúan los modos potenciales de falla en escala de 1 a 10 para Severidad (S), Ocurrencia (O) y Detección (D): 1) Modo de Falla 1: 'Acumulación de alquitranes (tar) y condensados en la tobera del quemador'. Efecto potencial: Bloqueo de flujo y apagado del motor. Severidad S = 7. Causa: Temperatura de la zona de combustión inferior a 800 °C. Ocurrencia O = 6. Detección D = 5 (detectable por termocupla). Número de Prioridad de Riesgo inicial: NPR_1 = S * O * D = 7 * 6 * 5 = 210 (Riesgo Crítico, supera el umbral de 100). Acción preventiva de ingeniería: Rediseño del aislamiento térmico con manta de fibra cerámica de 50 mm y adición de un craqueador catalítico de carbón vegetal al rojo; la ocurrencia se reduce a O = 2 y la detección mejora a D = 2 (nuevo NPR_1 = 7 * 2 * 2 = 28, riesgo mitigado). 2) Modo de Falla 2: 'Fuga de monóxido de carbono (CO) a la atmósfera del laboratorio por fallo de junta de estanqueidad'. Efecto potencial: Asfixia e intoxicación letal para los estudiantes y docentes. Severidad máxima S = 10 (catastrófica para la vida). Ocurrencia O = 4. Detección D = 8 (el CO es incoloro e inodoro, indetectable por sentidos humanos). NPR_2 inicial = 10 * 4 * 8 = 320 (Riesgo Inadmisible Extremo). Acción obligatoria de seguridad: a) Operación de la cámara del gasificador bajo presión negativa continua mediante ventilador de tiro inducido (si hay una fuga, entra aire en lugar de escapar CO hacia afuera); b) Instalación de sensor digital de CO con alarma sonora de 95 dB a 50 ppm y corte automático de emergencia por electroválvula; c) Ensayos obligatorios en campana de extracción de gases al aire libre. La ocurrencia cae a O = 1 y la detección mejora a D = 1 (nuevo NPR_2 = 10 * 1 * 1 = 10, nivel de seguridad aceptado). Problema 2: En la matriz de riesgos de proyecto, el análisis evalúa riesgos de retraso en la importación de sensores por trámites aduaneros, definiendo proveedores alternativos locales de respaldo.",
        "bloque_sugerido": "Gestión de Riesgos 45 min • Metodología FMEA, cálculo de NPR (S x O x D) y seguridad de laboratorio",
        "slides": [
            {
                "numero": 1,
                "seccion": "INGENIERÍA PREVENTIVA Y SEGURIDAD",
                "titulo": "Failure Mode and Effects Analysis (FMEA)",
                "puntos": [
                    "Desarrollado por la industria aeroespacial (NASA) y automotriz (Ford) para prevenir fallas antes de que ocurran.",
                    "Obliga a preguntarse sistemáticamente en cada pieza: ¿Cómo puede fallar? ¿Qué pasaría si falla? ¿Cómo lo detectamos?",
                    "Indispensable para garantizar la seguridad física de los estudiantes en los laboratorios de ensayo."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL NÚMERO DE PRIORIDAD DE RIESGO (NPR)",
                "titulo": "Severidad, Ocurrencia y Detección",
                "puntos": [
                    "Severidad (S): Gravedad del impacto sobre el usuario o el equipo (1: imperceptible a 10: riesgo mortal).",
                    "Ocurrencia (O): Probabilidad de que la causa raíz se manifieste durante la vida útil.",
                    "Detección (D): Dificultad para descubrir la falla antes de que cause daño (1: detección segura a 10: indetectable).",
                    "Todo NPR > 100 exige obligatoriamente un rediseño de ingeniería documentado."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Diagramas de Tuberías e Instrumentación (P&ID) bajo Norma ISA 5.1",
        "objetivo": "Diseñar e interpretar diagramas de tuberías e instrumentación (P&ID) y diagramas de flujo de proceso (PFD) aplicando la simbología normalizada ISA 5.1 para lazos de control de temperatura, presión, nivel y flujo.",
        "concepto_clave_latex": r"\text{Identificación ISA}: \text{TT (Transmisor Temperatura)} \to \text{TIC (Controlador Indicador)} \to \text{TCV (Válvula de Control)}",
        "ejemplo": "Problema 1: Un equipo CDIO I diseña el diagrama P&ID conforme a la norma internacional ANSI/ISA 5.1 para un banco de pruebas de colectores solares térmicos parabólicos con lazo cerrado de aceite térmico: Componentes e instrumentación del lazo de control de temperatura del fluido a la salida del receptor: 1) Elemento primario de medición: Sensor de temperatura RTD Pt100 inserto en termopozo en la tubería de salida etiquetado como TE-101 (Temperature Element). 2) Transmisor de temperatura montado en campo con protocolo digital 4-20 mA Hart etiquetado en círculo simple como TT-101 (Temperature Transmitter). 3) Señal de transmisión eléctrica (representada en el plano por línea discontinua con tres trazos oblicuos). 4) Controlador e Indicador de Temperatura basado en microcontrolador accesible al operador en panel principal (representado por un círculo con una línea horizontal continua divisoria en el centro) etiquetado como TIC-101. 5) Salida de control de modulación (línea de señal digital) conectada a la Válvula de Control de Temperatura TCV-101 instalada en la línea de derivación (bypass). 6) Lazo de Seguridad y Alivio: Transmisor de presión PT-102 conectado a interruptor de alta presión PSH-102 que desenergiza la bomba enclavada interlock I-101 si la presión supera 6.0 bar; y Válvula de Seguridad de Alivio mecánico por resorte PSV-103 ajustada a 7.5 bar descargando a tanque atmosférico. La codificación ISA 5.1 asegura que cualquier ingeniero químico, eléctrico o mecánico de cualquier parte del mundo interprete el funcionamiento exacto de la planta piloto sin ambigüedades. Problema 2: En el Diagrama de Flujo de Procesos (PFD), la tabla de balance de materia y energía anexa lista la temperatura, presión, entalpía y caudal de cada una de las 12 corrientes numeradas del proceso.",
        "bloque_sugerido": "Instrumentación P&ID 45 min • Normativa ISA 5.1, simbología de lazos de control y diseño de PFDs",
        "slides": [
            {
                "numero": 1,
                "seccion": "LENGUAJE UNIVERSAL DE PROCESOS",
                "titulo": "El Estándar ISA 5.1",
                "puntos": [
                    "P&ID (Piping and Instrumentation Diagram): El plano maestro que muestra la interconexión entre tuberías, equipos e instrumentos de control.",
                    "Primera letra (Variable): T (Temperatura), P (Presión), F (Flujo / Caudal), L (Nivel), A (Análisis / pH).",
                    "Letras sucesivas (Función): E (Elemento primario), T (Transmisor), I (Indicador), C (Controlador), V (Válvula), S (Interruptor switch)."
                ]
            },
            {
                "numero": 2,
                "seccion": "SIMBOLOGÍA DE CONTROL E INSTRUMENTACIÓN",
                "titulo": "Círculos, Líneas y Válvulas",
                "puntos": [
                    "Círculo solo: Instrumento discreto montado en campo (in situ).",
                    "Círculo con línea central: Instrumento montado en panel de control principal accesible al operador.",
                    "Cuadrado con círculo interno: Sistema de Control Distribuido (DCS / PLC / SCADA).",
                    "Líneas de conexión: Línea continua (tubería de proceso), línea segmentada (señal eléctrica 4-20 mA), doble trazo (neumática)."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Modelado CAD 3D del Prototipo y Selección de Componentes Comerciales (COTS)",
        "objetivo": "Desarrollar el ensamble mecánico tridimensional completo del prototipo en software CAD paramétrico, integrando componentes comerciales de catálogo (COTS) con componentes a fabricar a medida.",
        "concepto_clave_latex": r"\text{Ensamble CAD} = \{ \text{Piezas Mecanizadas a Medida} \} \cup \{ \text{Componentes Comerciales COTS (STEP)} \}",
        "ejemplo": "Problema 1: En el modelado 3D del prototipo de seguidor solar monoaxial de 1 kW para el laboratorio de energías renovables, el equipo modela en SolidWorks la arquitectura electromecánica completa: 1) Componentes COTS (Commercial Off-The-Shelf) descargados en formato neutro STEP AP214 desde bibliotecas digitales de fabricantes (Misumi, McMaster-Carr, SKF): Actuador lineal eléctrico telescópico de 24 V DC carrera 300 mm (fuerza 4000 N con encoder Hall integrado); dos chumaceras de pie con rodamiento oscilante de bolas de 30 mm de diámetro interior; tornillería de acero inoxidable clase A2-70 (pernos M10x40 con arandelas de presión Grower y tuercas autoblocantes de nylon Nyloc). 2) Componentes Diseñados a Medida (Custom Made): Tubo de torsión de sección cuadrada estructural ASTM A500 de 75 x 75 x 3 mm y 3.2 metros de longitud; brazos de soporte de módulos en chapa de aluminio 6061-T6 plegada de 3.0 mm de espesor modelados con módulo de Chapa Metálica (Sheet Metal) para generar el archivo DXF de corte por láser; pedestal central de acero soldado con cartelas triangulares de rigidización de 6.0 mm. 3) Planos de Fabricación 2D: Se generan planos acotados bajo norma ISO/ASME con tolerancias dimensionales ISO 2768-m, indicación de soldadura filete de 4 mm con electrodo E7018 y lista de despiece desglosada (BOM). 4) Renderizado y Verificación de Centro de Gravedad: El software calcula la masa total ensamblada del prototipo en M = 64.8 kg y verifica que el centro de masa se ubica a menos de 15 mm del eje neutro de giro, minimizando el torque de desbalance sobre el motor actuador a menos de 9.5 N*m. Problema 2: El uso de componentes COTS estandarizados en lugar de diseñar piezas mecánicas desde cero reduce el costo del prototipo en un 45% y acorta el plazo de fabricación en 3 semanas.",
        "bloque_sugerido": "Modelado CAD de Prototipos 45 min • Ensamble 3D, integración COTS de catálogo y planos de taller",
        "slides": [
            {
                "numero": 1,
                "seccion": "DISEÑO DETALLADO DE PROTOTIPOS",
                "titulo": "Estrategia COTS (Commercial Off-The-Shelf)",
                "puntos": [
                    "Nunca 'reinventar la rueda': todo perno, rodamiento, motor o válvula existente en catálogo debe comprarse, no fabricarse.",
                    "McMaster-Carr, Misumi, GrabCAD: Descarga directa de modelos 3D nativos que se insertan directamente en el ensamble.",
                    "Permite enfocar los esfuerzos de manufactura en las piezas verdaderamente innovadoras y propietarias del proyecto."
                ]
            },
            {
                "numero": 2,
                "seccion": "DOCUMENTACIÓN DE INGENIERÍA 2D",
                "titulo": "Planos Técnicos para el Tornero y Soldador",
                "puntos": [
                    "El modelo 3D en pantalla no fabrica piezas; el operario del taller exige planos en papel claros y normalizados.",
                    "Vistas ortogonales normalizadas, vistas en corte de sección, detalles ampliados y cotas funcionales.",
                    "Especificación de acabados superficiales (rugosidad Ra), tratamientos térmicos y tipos de pintura anticorrosiva."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Simulación Numérica CAE y Gemelo Virtual para Validación Temprana del Diseño",
        "objetivo": "Validar virtualmente el prototipo mediante simulaciones numéricas de mecánica de fluidos (CFD) y elementos finitos (FEA) antes de invertir presupuesto en compras físicas de materiales.",
        "concepto_clave_latex": r"\text{Validación Virtual}: \text{Simulación CAE} \iff \text{Cálculo Analítico de Primer Principio} \quad (\text{Error} \le 5\% - 10\%)",
        "ejemplo": "Problema 1: Antes de cortar las láminas de acero y mandar a tornear el rotor de una micro-turbina hidroeléctrica tipo Michell-Banki de 500 W (flujo transversal) para una caída de agua de H = 8.0 m y caudal Q = 9.0 L/s, el equipo de proyecto realiza la validación numérica computacional CAE: 1) Simulación CFD Multidominio en ANSYS Fluent / OpenFOAM: Se discretiza el canal de entrada, la tobera inyectora rectangular con álabe regulador y el rotor de 24 álabes curvados con una malla poliédrica no estructurada de 1.8 millones de celdas con refinamiento en las capas límite (y+ < 1.0 para el modelo de turbulencia k-omega SST). Se aplica la técnica de interfaz móvil deslizante (Sliding Mesh) para rotar el rotor a n = 600 rpm en interacción transitoria con el flujo libre bifásico de agua y aire (modelo Volume of Fluid - VOF). Resultados hidrodinámicos: El chorro de agua atraviesa la primera etapa del rotor transfiriendo el 74% de su energía, cruza el espacio interior hueco y golpea la segunda etapa de adentro hacia afuera transfiriendo el 14% restante. Potencia mecánica neta calculada en el eje: P_eje = 524.8 W. Eficiencia hidrodinámica simulada: eta = 524.8 / (rho * g * Q * H) = 524.8 / (1000 * 9.81 * 0.009 * 8) = 524.8 / 706.32 = 74.30% (perfectamente consistente con el rango experimental clásico de Banki de 72-78%). 2) Simulación Estructural FEA: El mapa de presiones hidrodinámicas transitorias calculado por el CFD se exporta automáticamente como carga de presión sobre los álabes en ANSYS Mechanical. Tensión máxima de von Mises en la unión álabe-disco: sigma_max = 48.5 MPa (ampliamente inferior al límite elástico del acero inoxidable 304, S_y = 215 MPa, FS = 4.43). La simulación virtual valida el perfil del inyector y confirma que no habrá rotura mecánica ni fenómenos de recirculación parásita, autorizando el desembolso financiero para el mecanizado CNC. Problema 2: Si la simulación virtual hubiera revelado una eficiencia pobre del 55% debido a choque de entrada desalineado, el ángulo del inyector se optimiza paramétricamente en el software en 2 horas sin perder un solo peso en material físico desechado.",
        "bloque_sugerido": "Simulación Numérica Virtual 45 min • Validación cruzada CFD/FEA acoplada de turbinas hidroeléctricas",
        "slides": [
            {
                "numero": 1,
                "seccion": "INGENIERÍA ASISTIDA POR COMPUTADOR (CAE)",
                "titulo": "Construir Digitalmente Antes de Cortar Metal",
                "puntos": [
                    "El paradigma moderno de ingeniería sustituye el costoso ensayo y error físico por experimentación digital.",
                    "CFD (Computational Fluid Dynamics): Visualiza líneas de corriente, vectores de velocidad, vórtices y caída de presión.",
                    "FEA (Finite Element Analysis): Verifica deformaciones elásticas y descarta concentradores de esfuerzo peligrosos."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERIFICACIÓN Y VALIDACIÓN (V&V)",
                "titulo": "La Regla de Oro del Modelado Numérico",
                "puntos": [
                    "Verificación: ¿El modelo matemático se está resolviendo correctamente? (Convergencia de residuos, independencia de malla).",
                    "Validación: ¿El modelo numérico representa la física del mundo real? (Comparación con fórmulas analíticas y literatura).",
                    "'Garbage in, Garbage out': Una simulación con condiciones de contorno erróneas es más peligrosa que no simular."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Estrategia de Prototipado Rápido y Niveles de Madurez Tecnológica (TRL 1 a 4)",
        "objetivo": "Evaluar la madurez del proyecto según la escala TRL (Technology Readiness Level) de la NASA/Horizonte Europa, planificando la progresión desde el principio científico (TRL 1) hasta la validación del prototipo en laboratorio (TRL 4).",
        "concepto_clave_latex": r"\text{TRL 1: Principios} \to \text{TRL 2: Concepto} \to \text{TRL 3: Prueba de Concepto} \to \text{TRL 4: Validación Lab}",
        "ejemplo": "Problema 1: Un equipo de estudiantes de CDIO I desarrolla un sistema de cogeneración solar fotovoltaica y térmica híbrida (PVT) refrigerado por líquido con nanofluidos de grafeno para elevar la eficiencia eléctrica del panel solar en un 12% y capturar agua caliente simultáneamente. Se audita la trayectoria de madurez del proyecto conforme a la escala TRL estandarizada por MinCiencias y la NASA: 1) TRL 1 (Principios Básicos Observados y Reportados): Revisión bibliográfica en Scopus del efecto de la temperatura sobre el coeficiente de temperatura de potencia de las células de silicio (gamma = -0.38%/°C) y las propiedades térmicas mejoradas de suspensiones coloidales de grafeno (k_nf > 1.2 W/(m*K)). 2) TRL 2 (Concepto Tecnológico Formulado): Formulación matemática preliminar del intercambiador de calor de serpentín pegado a la cara posterior del panel solar con adhesivo térmico de alta conductividad. 3) TRL 3 (Prueba de Concepto Analítica y Experimental de Subsistema Crítico): Ensayo de laboratorio a pequeña escala probando la estabilidad coloidal del nanofluido con surfactante SDS en un tubo de ensayo sometido a 100 ciclos térmicos sin sedimentación de nanopartículas. 4) TRL 4 (Validación de Componentes en Entorno de Laboratorio): Construcción del prototipo físico integrado a escala reducida (módulo solar comercial de 50 W modificado con el intercambiador de calor posterior, bomba circuladora de 12 V, medidores de caudal y termocuplas) conectado a un simulador solar con lámparas halógenas calibradas a 800 W/m^2 en el laboratorio de la Universidad del Magdalena. La prueba en laboratorio demuestra experimentalmente que la circulación del fluido reduce la temperatura de la célula solar de 62 °C a 38 °C, incrementando la potencia eléctrica de 38.2 W a 43.1 W (+12.8% de ganancia) y generando 140 W térmicos de agua caliente a 45 °C. El proyecto se certifica exitosamente en nivel TRL 4, cumpliendo el alcance final exigido para el Proyecto Integrador CDIO I y dejando las bases sentadas para escalar a TRL 6 (entorno relevante real) en CDIO II. Problema 2: El 'Valle de la Muerte' de la innovación tecnológica ocurre en la transición entre TRL 4 (laboratorio académico) y TRL 7 (prototipo operativo pre-comercial en campo), donde la falta de financiamiento de capital semilla detiene la transferencia de patentes hacia la industria.",
        "bloque_sugerido": "Madurez Tecnológica TRL 45 min • Escala TRL 1-9 de la NASA, prueba de concepto y TRL 4 en CDIO I",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA ESCALA DE MADUREZ TECNOLÓGICA",
                "titulo": "Technology Readiness Levels (TRL de la NASA)",
                "puntos": [
                    "Creada en los años 70 para evaluar el riesgo de integrar nuevas tecnologías en misiones espaciales complejas.",
                    "Hoy es el estándar métrico universal adoptado por la Unión Europea, MinCiencias y las grandes corporaciones energéticas.",
                    "TRL 1 a 3: Investigación básica y prueba de concepto; TRL 4 a 6: Desarrollo y prototipado; TRL 7 a 9: Despliegue comercial."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL OBJETIVO DE CDIO I",
                "titulo": "Alcanzar con Éxito el Hito TRL 4",
                "puntos": [
                    "TRL 4 exige que los componentes individuales estén completamente integrados y funcionen juntos en laboratorio.",
                    "No se exige aún operación en campo abierto bajo lluvia o polvo (eso corresponde a CDIO II / TRL 6).",
                    "La validación debe basarse en mediciones experimentales objetivas, no en opiniones subjetivas."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Selección de Sensores, Actuadores y Microcontroladores para Adquisición de Datos (IoT)",
        "objetivo": "Diseñar la arquitectura de instrumentación electrónica del prototipo, seleccionando transductores de corriente (Efecto Hall), tensión, temperatura (RTD/termocuplas) y plataformas de cómputo embebido (ESP32/STM32).",
        "concepto_clave_latex": r"V_{ADC} = V_{in} \cdot \frac{R_2}{R_1 + R_2} \quad ; \quad \text{Resolución ADC}: \Delta V = \frac{V_{ref}}{2^n - 1} \quad (n = 12 \text{ bits} \implies 0.806 \text{ mV})",
        "ejemplo": "Problema 1: Se diseña el sistema de monitoreo y adquisición de datos en tiempo real (DAQ) para un prototipo de micro-red híbrida con batería de 24 V y panel solar fotovoltaico de 300 W. Variables a medir continuamente: Tensión del banco de baterías (V_bat = 20 a 30 V DC); corriente de carga/descarga (I_bat = -15 A a +15 A DC); temperatura del inversor (T = 20 a 100 °C); irradiancia solar incidente (G = 0 a 1200 W/m^2). Selección y acondicionamiento electrónico de transductores: 1) Medición de Corriente: Sensor de corriente de Efecto Hall bidireccional aislado galvánicamente ACS712-20A (sensibilidad de 100 mV/A con salida analógica centrada en V_cc/2 = 2.50 V a corriente cero). A +15 A, la tensión de salida es V_out = 2.50 + (15 * 0.100) = 4.00 V. 2) Medición de Tensión: Divisor de tensión resistivo de precisión con resistencias al 1% de película metálica (R_1 = 100 k-ohms, R_2 = 10 k-ohms, factor de atenuación = 10 / 110 = 1/11). Para V_bat,max = 33.0 V, la tensión de salida hacia el microcontrolador es V_adc = 33.0 / 11 = 3.00 V. 3) Microcontrolador y Plataforma de Adquisición: Se selecciona el microcontrolador SoC ESP32-WROOM-32 (procesador dual-core de 32 bits a 240 MHz con conectividad Wi-Fi 802.11 b/g/n y Bluetooth BLE integrada, tensión operativa de 3.3 V). Como el conversor analógico-digital (ADC) interno de 12 bits del ESP32 presenta no-linealidades marcadas por debajo de 0.15 V y por encima de 3.1 V, se añade un ADC externo I2C de 16 bits de alta precisión ADS1115 (4 canales diferenciales, ganancia programable PGA y tasa de muestreo de hasta 860 muestras/s). Tensión de referencia V_ref = 4.096 V: Resolución del convertidor: Delta_V = 4.096 V / 32,768 cuentas = 0.125 mV por bit. El error de cuantificación en la tensión de batería es de solo Delta_V_bat = 11 * 0.125 mV = 1.375 mV (error relativo del 0.005%, precisión metrológica cuasi-profesional). 4) Sensor de Temperatura: Sonda digital blindada sumergible DS18B20 con protocolo 1-Wire (resolución de 12 bits, precisión de +-0.5 °C sin requerir calibración analógica externa). Problema 2: En la transmisión telemétrica hacia la nube (Cloud IoT Dashboard en Grafana / ThingsBoard), el protocolo MQTT con formato JSON liviano permite enviar paquetes de telemetría de 120 bytes cada 1 segundo consumiendo menos de 50 mW de potencia de telecomunicaciones.",
        "bloque_sugerido": "Electrónica y Sensores IoT 45 min • Sensores Hall, ADC externo ADS1115 y microcontrolador ESP32",
        "slides": [
            {
                "numero": 1,
                "seccion": "DIGITALIZACIÓN DE PROTOTIPOS CDIO",
                "titulo": "Arquitectura de un Sistema DAQ Embebido",
                "puntos": [
                    "Un prototipo de energía moderno debe ser inteligente y capaz de autodiagnosticarse y transmitir datos a internet.",
                    "Sensores: Efecto Hall (corriente no invasiva), divisores resistivos atenuados (voltaje), Pt100 / DS18B20 (temperatura).",
                    "Aislamiento galvánico con optoacopladores para proteger el procesador de transitorios de alta potencia."
                ]
            },
            {
                "numero": 2,
                "seccion": "MICROCONTROLADORES PARA ENERGÍA",
                "titulo": "ESP32 vs STM32 vs Arduino",
                "puntos": [
                    "Arduino Uno (ATmega328P de 8 bits a 16 MHz): Obsoleto para control de potencia avanzado; memoria RAM insuficiente.",
                    "ESP32 (32 bits, dual-core, 240 MHz con Wi-Fi/Bluetooth): Estándar por excelencia para prototipos IoT de bajo costo (< 6 USD).",
                    "STM32 (Cortex-M4/M7 con unidad de punto flotante FPU): Ideal para control de conmutación de inversores PWM de alta frecuencia."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Acondicionamiento de Señal y Circuitos de Potencia para el Prototipo Físico",
        "objetivo": "Diseñar etapas de amplificación, filtrado analógico activo Butterworth paso-bajo, optoaislamiento y drivers de conmutación de compuerta (gate drivers) para transistores MOSFET/IGBT.",
        "concepto_clave_latex": r"f_c = \frac{1}{2\pi R C} \quad ; \quad I_g = \frac{V_{driver} - V_{th}}{R_g} \quad ; \quad \text{Filtro Anti-Aliasing}: f_c \le \frac{f_s}{2}",
        "ejemplo": "Problema 1: En el convertidor reductor DC/DC síncrono (Buck Converter de 100 W, conmutando a f_sw = 50 kHz) de un cargador solar MPPT, se diseña el circuito de acondicionamiento de señal y la etapa de potencia de disparo de compuerta: 1) Filtro Analógico Paso-Bajo Anti-Aliasing: La corriente de salida del panel solar presenta ruido de alta frecuencia por la conmutación PWM del convertidor a 50 kHz. Para muestrear la señal con el ADC a una frecuencia de muestreo de f_s = 2000 muestras/s (2 kHz), el Teorema de Nyquist exige filtrar drásticamente cualquier frecuencia superior a f_Nyquist = f_s / 2 = 1000 Hz. Se diseña un filtro activo Butterworth paso-bajo de 2do orden con amplificador operacional rail-to-rail (OPA340) con frecuencia de corte a f_c = 200 Hz: Seleccionando condensadores normalizados C_1 = 100 nF y C_2 = 50 nF, la resistencia calculada es R = 1 / (2 * pi * f_c * sqrt(C_1 * C_2 * 2)) = 11.25 k-ohms (se usan resistencias de 11.3 k-ohms al 1%). A 50 kHz, el filtro atenúa el ruido de conmutación en más de -80 dB, entregando al ADC una señal continua pura y sin fluctuaciones espurias. 2) Driver de Disparo de Compuerta (Gate Driver): El MOSFET de potencia de canal N del lado alto (High-Side N-MOSFET de 60 V y R_ds(on) = 8.5 m-ohms, capacitancia de entrada C_iss = 1800 pF con carga total de compuerta Q_g = 35 nC) requiere una tensión compuerta-fuente V_gs = 12 V para saturar completamente, mientras que el microcontrolador solo entrega 3.3 V lógicos a baja corriente (máximo 12 mA). Se implementa un circuito integrado gate driver flotante por bootstrap IR2104: Tiempo de conmutación deseado t_on = 40 ns. Corriente de pico de compuerta requerida: I_g = Q_g / t_on = 35 nC / 40 ns = 0.875 A. Resistencia de compuerta externa seleccionada: R_g = (V_driver - V_th) / I_g = (12 - 3) / 0.875 = 10.28 ohms (se instala una resistencia anti-oscilaciones de 10 ohms en serie con la compuerta y un diodo Schottky en antiparalelo para apagado rápido). 3) Condensador de Bootstrap: C_boot = 10 * Q_g / Delta_V_boot = 10 * 35 nC / 0.2 V = 1.75 microfaradios (se instala condensador cerámico X7R de 2.2 microfaradios de bajo ESR en paralelo con diodo ultrarrápido UF4007), garantizando conmutación limpia sin calentamiento del transistor. Problema 2: En la placa de circuito impreso (PCB), la separación de pistas de masa analógica (AGND) y masa de potencia ruidosa (PGND) unidas en un único punto estrella elimina los lazos de tierra (ground loops) que distorsionan las mediciones de los sensores.",
        "bloque_sugerido": "Electrónica de Potencia 45 min • Filtros analógicos activos, gate drivers flotantes y diseño de PCBs",
        "slides": [
            {
                "numero": 1,
                "seccion": "INTERFAZ ENTRE CONTROL Y POTENCIA",
                "titulo": "La Necesidad del Acondicionamiento",
                "puntos": [
                    "Los microcontroladores (3.3 V / 12 mA) son chips frágiles que se destruyen instantáneamente si tocan tensiones de potencia.",
                    "Los transistores MOSFET de potencia necesitan corrientes de compuerta de 1 a 2 Amperios para conmutar en nanosegundos.",
                    "El Gate Driver actúa como el músculo amplificador intermedio indispensable entre el cerebro digital y el interruptor de potencia."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISEÑO DE CIRCUITOS IMPRESOS (PCB)",
                "titulo": "Ruido Electromagnético y Planos de Masa",
                "puntos": [
                    "Pistas de potencia anchas (> 2.5 mm) calculadas según IPC-2152 para evacuar calor y minimizar inductancia parásita L*di/dt.",
                    "Filtros paso-bajo de hardware: Esenciales para que el software no tome decisiones erróneas basadas en picos de ruido de conmutación.",
                    "Optoacopladores (aisladores ópticos): Transmiten señales lógicas a través de luz infrarroja garantizando aislamiento de 2500 V."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Programación de Firmware en Tiempo Real y Algoritmos de Control Embebido",
        "objetivo": "Programar el firmware embebido del prototipo estructurando lazos de control PID discretizados en tiempo real y máquinas de estados finitos (FSM) sobre RTOS o temporizadores por interrupción.",
        "concepto_clave_latex": r"u[k] = u[k-1] + K_p (e[k] - e[k-1]) + K_i T_s e[k] + \frac{K_d}{T_s} (e[k] - 2e[k-1] + e[k-2])",
        "ejemplo": "Problema 1: En el controlador de carga solar MPPT de un prototipo CDIO I, se programa el algoritmo de control embebido en lenguaje C/C++ sobre el microcontrolador ESP32: 1) Estructura de Tiempo Real por Interrupción de Temporizador (Timer Interrupt ISR a 100 Hz exactos, periodo de muestreo T_s = 10 ms = 0.010 s): La rutina de interrupción de hardware garantiza un tiempo de muestreo determinístico e inalterable, libre de los retrasos impredecibles de la función bloqueante delay(). 2) Implementación Discreta del Algoritmo de Seguimiento de Máxima Potencia Perturb & Observe (P&O): En cada ciclo k, el microcontrolador lee la tensión V[k] y corriente I[k] del panel, calcula la potencia instantánea P[k] = V[k] * I[k] y evalúa la derivada discreta: Delta_P = P[k] - P[k-1]; Delta_V = V[k] - V[k-1]. Si Delta_P > 0: El punto de operación se mueve hacia el MPP; si Delta_V > 0 se incrementa el ciclo de trabajo PWM (D = D + Delta_D), si Delta_V < 0 se decrementa (D = D - Delta_D con paso fijo Delta_D = 0.005). Si Delta_P < 0: El punto de operación se alejó del MPP; se invierte la dirección de perturbación. 3) Algoritmo de Regulación de Tensión PID Discreto con Anti-Windup: Cuando la batería alcanza su tensión de absorción (V_ref = 28.8 V), el sistema conmuta automáticamente mediante una Máquina de Estados Finitos (FSM) desde modo MPPT a modo de regulación de tensión constante (Float Charging). Ecuación del algoritmo PID en forma incremental de velocidad para evitar el desbordamiento integral: Error actual e[k] = V_ref - V_bat[k]. Término proporcional: Delta_u_p = K_p * (e[k] - e[k-1]). Término integral: Delta_u_i = K_i * T_s * e[k]. Término derivativo filtrado: Delta_u_d = (K_d / T_s) * (e[k] - 2*e[k-1] + e[k-2]). Salida de control de ciclo de trabajo PWM: u[k] = u[k-1] + Delta_u_p + Delta_u_i + Delta_u_d. Clamp de Anti-Windup: Si u[k] > 0.95 se satura en 0.95; si u[k] < 0.05 se satura en 0.05, congelando la acumulación integral. Con ganancias sintonizadas por Ziegler-Nichols (K_p = 0.45, K_i = 12.0 s^-1, K_d = 0.002 s), el lazo de tensión estabiliza la salida en 28.80 +- 0.05 V en menos de 80 milisegundos sin sobretensiones que degraden la batería. Problema 2: En la Máquina de Estados Finitos (FSM), se programan transiciones seguras entre estados: [ESTADO_INICIO] -> [ESTADO_MPPT] -> [ESTADO_ABSORCION] -> [ESTADO_FLOTACION] -> [ESTADO_FALLA_OVERVOLTAGE], garantizando que si se detecta sobrecalentamiento térmico el sistema desconecte el PWM en menos de 1 milisegundo.",
        "bloque_sugerido": "Firmware Embebido 45 min • Algoritmo MPPT P&O, controlador PID discreto y máquinas de estados FSM",
        "slides": [
            {
                "numero": 1,
                "seccion": "SOFTWARE DE CONTROL DE TIEMPO REAL",
                "titulo": "Sistemas Embebidos Determinísticos",
                "puntos": [
                    "Prohibición de funciones bloqueantes (delay() o bucles infinitos): Congelan el microcontrolador e impiden responder ante fallas.",
                    "Interrupciones por temporizador (Hardware Timers): Ejecutan el lazo de control matemático a intervalos de tiempo exactos (ej. cada 10 ms).",
                    "Máquinas de Estados Finitos (FSM): Estructuran la lógica de operación de manera predecible y a prueba de errores."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISCRETIZACIÓN DE CONTROLADORES PID",
                "titulo": "De la Transformada de Laplace al Código C",
                "puntos": [
                    "Aproximación de Euler / Tustin (Bilineal): Transforma funciones de transferencia continuas C(s) en ecuaciones de diferencias u[k].",
                    "Anti-Windup Integral: Impide que el integrador acumule valores gigantescos cuando los actuadores alcanzan su límite físico de saturación.",
                    "Filtro en el término derivativo: Elimina la amplificación de ruido de alta frecuencia que quemaría los transistores."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ensamblaje Electromecánico del Prototipo y Pruebas Unitarias de Subsistemas",
        "objetivo": "Ejecutar el ensamblaje físico del prototipo en el taller de ingeniería aplicando buenas prácticas de conexionado electromecánico, torque de apriete y pruebas unitarias independientes de subsistemas.",
        "concepto_clave_latex": r"\text{Prueba Unitaria}: \text{Sub-Mecánico} \cap \text{Sub-Potencia} \cap \text{Sub-Control} \implies \text{Validación Independiente}",
        "ejemplo": "Problema 1: Un equipo CDIO I finaliza la fabricación de piezas y procede al ensamblaje físico e integración de un prototipo de aerogenerador eólico urbano de eje horizontal de 300 W en el taller de máquinas y herramientas: 1) Protocolo de Montaje Mecánico: Montaje de los dos rodamientos rígidos de bolas 6206 en el eje principal de acero rectificado mediante prensa hidráulica con casquillo de empuje apoyado exclusivamente en el anillo interior (evitando transmitir la fuerza de prensado a través de las bolas, lo que provocaría indentaciones Brinell y ruido prematuro). Apriete de los 12 pernos de fijación de las tres palas de fibra de vidrio con llave dinamométrica calibrada aplicando el torque especificado por diseño de T_apriete = 24.5 N*m con fijador de roscas anaeróbico de resistencia media (Loctite 243). 2) Pruebas Unitarias Aisladas (Unit Testing): Antes de conectar todos los sistemas juntos, se prueba cada subsistema de forma 100% aislada: a) Prueba Unitaria Mecánica: Giro manual libre del rotor con tacómetro óptico; se verifica que el par de fricción en vacío de los sellos y rodamientos es inferior a 0.08 N*m y el descentramiento radial en la punta del cono es menor a 0.35 mm. b) Prueba Unitaria de Potencia: Conexión del generador síncrono PMSG desacoplado a un motor motriz en banco de pruebas; se mide la tensión de circuito abierto entre fases (FCEM) comprobando que entrega exactamente 24.2 V a 450 rpm con una simetría entre fases del 99.4%. c) Prueba Unitaria del Rectificador y Filtro: Se alimenta el puente de diodos trifásico con fuente AC de laboratorio; se comprueba que el rizado de tensión en el condensador electrolítico es inferior al 4.2%. d) Prueba Unitaria de Control y Firmware: Se alimenta el microcontrolador ESP32 con fuente de 5 V aislada; se simula la entrada de tensión analógica con potenciómetro de precisión verificando que la pantalla OLED muestra los valores con error inferior al 1% y el relé de frenado magnético conmuta al superar el umbral de sobretensión. Este procedimiento riguroso de pruebas unitarias permite descubrir y corregir un diodo rectificador soldado con polaridad invertida ANTES de la integración final, evitando un cortocircuito destructivo que habría quemado el generador y el microcontrolador. Problema 2: En el conexionado de cuadros de potencia, la aplicación de terminales tubulares preaislados (ferrules) prensados con crimpadora hexagonal en todos los cables flexibles previene que hilos de cobre sueltos provoquen cortocircuitos entre bornas contiguas.",
        "bloque_sugerido": "Ensamblaje y Pruebas Unitarias 45 min • Buenas prácticas de taller, torque dinamométrico y pruebas aisladas",
        "slides": [
            {
                "numero": 1,
                "seccion": "INTEGRACIÓN FÍSICA EN TALLER",
                "titulo": "Metodología de Ensamblaje Seguro",
                "puntos": [
                    "El montaje no consiste en 'juntar todo rápido y ver si echa humo'.",
                    "Uso de torquímetros: Apretar pernos al tacto genera tensiones desiguales y rotura por cizallamiento.",
                    "Orden y limpieza (5S): Un taller desordenado provoca pérdida de componentes y accidentes mecánicos con virutas."
                ]
            },
            {
                "numero": 2,
                "seccion": "PRUEBAS UNITARIAS DE SUBSISTEMAS",
                "titulo": "Aislar Errores Antes de la Conexión Total",
                "puntos": [
                    "Regla de oro: NUNCA energizar un prototipo completo por primera vez con potencia plena.",
                    "Probar el subsistema mecánico en vacío -> Probar la tarjeta de control con fuente regulada -> Probar la etapa de potencia.",
                    "Localiza fallas y componentes defectuosos en minutos en lugar de buscar a ciegas en un sistema complejo."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Protocolos de Pruebas de Integración y Calibración Metrológica Experimental",
        "objetivo": "Diseñar protocolos formales de prueba de integración de prototipos completos, calibrando sensores frente a patrones certificados y calculando la incertidumbre combinada según la Guía GUM.",
        "concepto_clave_latex": r"y = f(x_1, x_2, \dots, x_n) \quad ; \quad u_c(y) = \sqrt{\sum_{i=1}^n \left( \frac{\partial f}{\partial x_i} \right)^2 u^2(x_i)} \quad ; \quad U = k \cdot u_c(y) \;\; (k=2)",
        "ejemplo": "Problema 1: En el banco de pruebas de un prototipo de bomba de calor para calentamiento de agua asistida por energía solar, se ejecuta la calibración metrológica y el cálculo de incertidumbre del coeficiente de desempeño térmico experimental (COP_exp = Q_calor / W_electrico): 1) Calibración de Sensores de Temperatura: Se calibran dos sondas RTD Pt100 de inmersión en baño termostático de recirculación frente a un termómetro patrón de mercurio con trazabilidad metrológica al INM (Instituto Nacional de Metrología). Curva de calibración por regresión lineal: T_corregida = 0.9982 * T_leida + 0.085 °C (coeficiente de determinación R^2 = 0.9998). Incertidumbre estándar combinada de temperatura: u(T) = 0.12 °C. Salto térmico medido en el condensador: Delta_T = T_out - T_in = 48.50 - 36.20 = 12.30 °C. Incertidumbre del salto térmico: u(Delta_T) = sqrt(u(T_out)^2 + u(T_in)^2) = sqrt(0.12^2 + 0.12^2) = 0.170 °C. 2) Medición de Flujo Másico de Agua: Medido con caudalímetro de turbina calibrado en banco volumétrico por pesaje gravimétrico: dot{m} = 0.150 kg/s con incertidumbre relativa u(dot{m})/dot{m} = 1.2% (u(dot{m}) = 0.0018 kg/s). Calor específico del agua: c_p = 4.182 kJ/(kg*K). Potencia térmica entregada: Q_th = dot{m} * c_p * Delta_T = 0.150 * 4.182 * 12.30 = 7.716 kW. 3) Medición de Potencia Eléctrica: Medida con analizador de redes de potencia de precisión Fluke 435 Clase A: W_elec = 2.150 kW con incertidumbre u(W) = 0.015 kW (0.7%). 4) Coeficiente de Desempeño Experimental: COP_exp = Q_th / W_elec = 7.716 kW / 2.150 kW = 3.589. 5) Propagación de Incertidumbre según la Guía GUM (ISO/IEC Guide 98-3): Incertidumbre relativa combinada: u_c(COP)/COP = sqrt([u(dot{m})/dot{m}]^2 + [u(Delta_T)/Delta_T]^2 + [u(W)/W]^2) = sqrt([0.012]^2 + [0.170 / 12.30]^2 + [0.015 / 2.150]^2) = sqrt([0.012]^2 + [0.01382]^2 + [0.00698]^2) = sqrt(0.000144 + 0.000191 + 0.000049) = sqrt(0.000384) = 0.0196 (1.96%). Incertidumbre estándar combinada absoluta: u_c(COP) = 3.589 * 0.0196 = 0.0703. Incertidumbre expandida con factor de cobertura k = 2 (nivel de confianza del 95.45%): U = 2 * 0.0703 = 0.141. Resultado metrológico formal de ingeniería: COP = 3.59 +- 0.14 (k = 2, 95%). El reporte riguroso con barras de incertidumbre valida científicamente la superioridad del prototipo frente a bombas comerciales estándar (COP = 2.8). Problema 2: En la calibración de piranómetros solares, la verificación frente a un radiómetro de cavidad absoluta en días despejados determina la constante de calibración en microvoltios por W/m^2.",
        "bloque_sugerido": "Metrología Experimental 45 min • Calibración de transductores, propagación de incertidumbre GUM y k=2",
        "slides": [
            {
                "numero": 1,
                "seccion": "RIGOR CIENTÍFICO EN LAS MEDICIONES",
                "titulo": "Metrología e Incertidumbre Experimental",
                "puntos": [
                    "Una medición sin declaración explícita de incertidumbre no tiene ningún valor científico ni técnico.",
                    "Calibración: Comparar las lecturas de los sensores del prototipo contra un patrón de mayor jerarquía con trazabilidad.",
                    "Guía GUM (JCGM 100): Estándar internacional unificado para calcular y reportar incertidumbres experimentales."
                ]
            },
            {
                "numero": 2,
                "seccion": "PROPAGACIÓN DE ERRORES",
                "titulo": "Incertidumbre Combinada y Expandida (k = 2)",
                "puntos": [
                    "Incertidumbre Tipo A: Evaluada mediante métodos estadísticos (desviación estándar de n lecturas repetidas).",
                    "Incertidumbre Tipo B: Evaluada mediante especificaciones de fabricante, certificados de calibración y manuales.",
                    "Incertidumbre expandida U = k * u_c (con k = 2 representa un intervalo de confianza del 95.45%)."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Evaluación del Desempeño Energético y Cálculo de Eficiencia Real del Prototipo",
        "objetivo": "Evaluar experimentalmente la eficiencia global de conversión y pérdidas parásitas del prototipo físico integrado operando bajo condiciones reales de carga en el laboratorio.",
        "concepto_clave_latex": r"\eta_{\text{global}} = \frac{E_{\text{salida,útil}}}{E_{\text{entrada,primaria}}} \times 100\% \quad ; \quad \text{Balance}: E_{\text{in}} = E_{\text{out}} + \sum E_{\text{pérdidas}}",
        "ejemplo": "Problema 1: Se somete a prueba de rendimiento continuo de 4 horas el prototipo integrado CDIO I: 'Planta de desalinización solar por destilación por membrana de contacto directo (DCMD) asistida por calentador de inducción magnética': Mediciones experimentales promediadas durante el régimen permanente de 4 horas (14,400 s): Entrada de energía: 1) Energía solar térmica capturada por colector cilindro-parabólico de apertura A = 2.4 m^2 bajo radiación directa media DNI = 820 W/m^2 con eficiencia óptica-térmica eta_col = 58%: Potencia solar absorbida Q_sol = 2.4 * 820 * 0.58 = 1141.4 W (energía solar acumulada E_sol = 1141.4 * 14,400 / 3.6*10^6 = 4.566 kWh); 2) Consumo de energía eléctrica de la bomba de recirculación de salmuera y la bomba de agua destilada fría: Potencia eléctrica total medida en analizador W_elec = 65 W (energía eléctrica acumulada E_elec = 65 * 4 = 0.260 kWh). Entrada energética total al prototipo: E_in = 4.566 + 0.260 = 4.826 kWh = 17.374 MJ. Salida útil producida: Volumen total de agua destilada pura producida medido en probeta graduada V = 18.2 litros (masa de agua potable m = 18.2 kg, conductividad eléctrica final de 8.5 microSiemens/cm apta para consumo humano, removiendo el 99.98% de las sales marinas). Entalpía de vaporización del agua a la temperatura de la membrana (65 °C): h_fg = 2345 kJ/kg. Energía térmica latente útil equivalente incorporada en el agua desalinizada: E_util = m * h_fg = 18.2 kg * 2345 kJ/kg = 42,679 kJ = 42.68 MJ. 1) Relación de Ganancia de Salida (GOR - Gained Output Ratio, indicador internacional de eficiencia en desalinización térmica): GOR = (m * h_fg) / E_termica_in = 42.68 MJ / 16.44 MJ = 2.60 (indica que gracias a la recuperación de calor latente en el módulo multietapa de membranas, el sistema produce 2.6 veces más agua que un destilador solar simple de evaporación directa). 2) Eficiencia global de primer principio: eta_global = E_util / E_in = 42.68 MJ / 17.37 MJ = 245.7% (en base aparente por efecto multiplicador de recuperación latente; eficiencia de recuperación térmica pura = 68.4%). 3) Tasa de Producción Específica: Producción = 18.2 L / (2.4 m^2 * 4 h) = 1.895 L/(m^2*hora). El prototipo supera en un 38% la meta inicial fijada en el marco lógico (1.3 L/(m^2*h)), validando la eficacia del aislamiento térmico de poliuretano y la aerodinámica de flujos en la membrana. Problema 2: El balance exergético experimental revela que la mayor destrucción de exergía (62% del total) ocurre en la diferencia de temperatura irreversible entre el agua de salmuera caliente a 75 °C y la película de condensación a 25 °C.",
        "bloque_sugerido": "Evaluación Experimental 45 min • Cálculo de eficiencia de primer principio, balance de pérdidas y GOR",
        "slides": [
            {
                "numero": 1,
                "seccion": "VERIFICACIÓN EXPERIMENTAL DE METAS",
                "titulo": "La Prueba de Fuego del Prototipo",
                "puntos": [
                    "Llegó el momento de contrastar los cálculos teóricos de la fase Diseñar con la cruda realidad del laboratorio.",
                    "¿El prototipo cumplió las especificaciones técnicas prometidas en la matriz QFD? ¿Qué porcentaje de error existe?",
                    "Las desviaciones entre teoría y práctica son la fuente más rica de aprendizaje formativo del ingeniero."
                ]
            },
            {
                "numero": 2,
                "seccion": "MÉTRICAS CLAVE DE RENDIMIENTO (KPI)",
                "titulo": "Rendimiento, Pérdidas y Factores de Planta",
                "puntos": [
                    "Eficiencia de Conversión: Relación entre la energía útil aprovechable y la energía primaria total consumida.",
                    "Identificación de pérdidas parásitas no previstas: Fricción mecánica en retenes, caídas de tensión en cables, fugas térmicas.",
                    "Genera las curvas características reales que se publicarán en el artículo de investigación final."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Documentación Técnica IEEE y Elaboración de Póster Científico",
        "objetivo": "Redactar el artículo técnico final del proyecto integrador en formato estándar IEEE de dos columnas y diseñar un póster visual científico para ferias y congresos de ingeniería.",
        "concepto_clave_latex": r"\text{Estructura IMRyD}: \text{Introducción} \to \text{Metodología} \to \text{Resultados} \to \text{Discusión y Conclusiones}",
        "ejemplo": "Problema 1: El equipo estructura el artículo de investigación técnica final del proyecto CDIO I conforme a la plantilla oficial de conferencias IEEE (IEEE Conference Template en LaTeX / Overleaf, formato a doble columna, tamaño carta, tipografía Times New Roman): 1) Estructura Canónica IMRyD: - Título conciso y descriptivo en inglés y español (< 15 palabras sin abreviaturas oscuras); - Resumen estructurado (Abstract de exactamente 200 palabras conteniendo: contexto, brecha técnica, objetivo, metodología de diseño/implementación, resultado cuantitativo clave con incertidumbre y conclusión principal); - Palabras clave (5 términos controlados del tesauro IEEE); - Sección I. Introducción: Marco conceptual, estado del arte citando al menos 12 artículos recientes indexados en Scopus/IEEE Xplore y justificación; - Sección II. Metodología CDIO y Diseño: Balances termodinámicos, esquemas P&ID y modelo 3D; - Sección III. Implementación y Pruebas Experimentales: Descripción del banco de ensayos, sensores y metrología; - Sección IV. Resultados y Discusión: Gráficas de alta resolución en formato vectorial EPS/PDF (curvas P-V, mapas de temperatura, eficiencia en función de la carga con barras de error +-U); - Sección V. Conclusiones y Trabajo Futuro: Hallazgos objetivos sin repetir el resumen; - Referencias: Formato IEEE estricto con DOIs activos y citas cruzadas [1]-[15]. 2) Diseño del Póster Científico (Dimensiones normalizadas pliego A0 vertical: 841 x 1189 mm): Regla visual 40-30-30 (40% figuras e infografías de alta resolución, 30% espacio blanco libre para descanso visual, 30% texto en fuentes legibles a 2 metros de distancia: títulos a 72 pt, subtítulos a 48 pt, texto a 28 pt). Código QR dinámico en la esquina inferior derecha que enlaza al repositorio público de GitHub del proyecto con los archivos CAD (STEP), código fuente del firmware (C++) y video demostrativo en YouTube de 2 minutos. Problema 2: En la revisión por pares ciegos (Peer Review simulado entre grupos del curso), la aplicación de la rúbrica de redacción científica penaliza el uso de lenguaje informal, la falta de numeración de ecuaciones o la inclusión de tablas sin unidades de medida explícitas del Sistema Internacional (SI).",
        "bloque_sugerido": "Redacción Científica IEEE 45 min • Plantilla IEEE LaTeX en Overleaf y diseño de póster A0",
        "slides": [
            {
                "numero": 1,
                "seccion": "COMUNICACIÓN CIENTÍFICA ESTANDARIZADA",
                "titulo": "El Formato de Publicación IEEE",
                "puntos": [
                    "IEEE (Institute of Electrical and Electronics Engineers): La mayor asociación profesional técnica del planeta.",
                    "Plantilla a dos columnas: Estándar riguroso de redacción concisa, figuras vectoriales y citación bibliográfica.",
                    "Permite a los estudiantes postular sus proyectos de pregrado a congresos internacionales de energía."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL PÓSTER VISUAL DE INGENIERÍA",
                "titulo": "Impacto Visual en Ferias de Innovación",
                "puntos": [
                    "En una feria científica, un evaluador decide en menos de 10 segundos si se detiene o pasa de largo ante tu póster.",
                    "El póster no es un documento pegado en la pared; es un apoyo gráfico visual dominado por diagramas 3D y gráficas de resultados.",
                    "Código QR interactivo: Puerta de acceso a repositorios abiertos de código y demostraciones en video."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Sustentación Oral, Demostración en Vivo y Evaluación del Ciclo CDIO I",
        "objetivo": "Defender públicamente el proyecto integrador ante un jurado de profesores de la Facultad de Ingeniería mediante una presentación ejecutiva (Elevator Pitch) y una demostración funcional en vivo del prototipo.",
        "concepto_clave_latex": r"\text{Calificación CDIO} = 30\% \text{ Prototipo Operativo} + 25\% \text{ Artículo IEEE} + 25\% \text{ Defensa Oral} + 20\% \text{ Metodología}",
        "ejemplo": "Problema 1: El equipo defiende su proyecto integrador de fin de semestre CDIO I en el auditorio de la Facultad de Ingeniería de la Universidad del Magdalena ante un jurado compuesto por 3 profesores especialistas (un termofluídico, un eléctrico y un metodólogo): 1) Estructura de la Presentación Oral (Tiempo total cronometrado estrictamente de 15 minutos: 10 min de exposición oral + 5 min de demostración en vivo del prototipo + 10 min de preguntas de defensa): - Minutos 0 a 2 (El Gancho y el Problema): El presentador inicia con el problema real del campesinado en Tasajera, mostrando el impacto social y económico de la falta de energía. - Minutos 2 a 5 (Solución de Ingeniería): Presentación rápida de la matriz de selección morfológica, balances de masa y ensamble CAD 3D explotado en animación fluida. - Minutos 5 a 8 (Resultados Técnicos Experimentales): Análisis de las curvas de eficiencia real medidas en laboratorio con declaración formal de incertidumbre metrológica y balance económico de Payback (1.4 años). - Minutos 8 a 10 (Conclusiones y Trabajo Futuro): Lecciones aprendidas y ruta de escalado a TRL 6. 2) Demostración Funcional en Vivo (Live Demo de 5 minutos): Con el prototipo montado sobre la mesa del jurado, los estudiantes activan el interruptor general; el sensor lee la temperatura en tiempo real, el display OLED muestra la potencia generada, el ventilador modula suavemente por PWM y se extrae agua destilada pura en un vaso de precipitados ante los ojos del jurado. 3) Defensa en la Sesión de Preguntas y Respuestas: Un jurado cuestiona: '¿Por qué seleccionaron un sensor de corriente ACS712 si presenta una deriva térmica de 0.2%/°C?'. El estudiante responde con seguridad y aplomo: 'Excelente observación, profesor. Evaluamos esa deriva en la matriz de diseño y la compensamos en el firmware del ESP32 implementando una curva polinómica de calibración térmica cruzada con el sensor DS18B20 adyacente, reduciendo el error global al 0.4%'. El jurado califica la sustentación con 5.0/5.0, felicitando al equipo por su rigurosidad conceptual y destreza práctica. 4) Cierre Formal del Ciclo CDIO I: El prototipo se desmantela con orden, se limpian los bancos de trabajo y se archiva toda la documentación en la plataforma institucional. Culminación de la primera mitad de la carrera del Ingeniero Energético de la Universidad del Magdalena.",
        "bloque_sugerido": "Defensa CDIO I 45 min • Estructura de presentación ejecutiva, demostración en vivo y rúbrica ABET",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA DEFENSA PROFESIONAL DE INGENIERÍA",
                "titulo": "El Arte de la Presentación Ejecutiva",
                "puntos": [
                    "Puedes haber construido el mejor prototipo del mundo, pero si no sabes comunicarlo, tu proyecto está muerto.",
                    "Regla de oro: Ensayar con cronómetro en mano; exceder el tiempo asignado demuestra falta de preparación y desconsideración.",
                    "Reparto equitativo del uso de la palabra: Todos los miembros del equipo deben demostrar dominio técnico pleno de todas las áreas."
                ]
            },
            {
                "numero": 2,
                "seccion": "DEMOSTRACIÓN FUNCIONAL EN VIVO",
                "titulo": "La Prueba Irrefutable: '¡Funciona!'",
                "puntos": [
                    "La demostración en vivo del prototipo separa la verdadera ingeniería de la simple oratoria vacía.",
                    "Plan de contingencia para la demo: Tener baterías de repuesto, fusibles extra y cables duplicados ante cualquier imprevisto.",
                    "Culminación victoriosa del Cuatrimestre 6 y consolidación del perfil profesional del Ingeniero Energético de Unimagdalena."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_05011834)
    marker = '  - cuatrimestre: 7'
    inject_topics_after(marker, yaml_text)
    print("05011834 Proyecto Integrador CDIO I successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
