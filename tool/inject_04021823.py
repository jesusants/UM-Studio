# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_04021823 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Modelado Paramétrico Basado en Restricciones Geométricas y Tablas de Diseño",
        "objetivo": "Construir modelos sólidos 3D completamente acotados y definidos mediante relaciones geométricas y variables paramétricas globales vinculadas a tablas de diseño (Design Tables).",
        "concepto_clave_latex": r"\mathbf{f}(\mathbf{x}) = \mathbf{0} \quad ; \quad \text{DOF} = 3N - C_{geom} - C_{dim} = 0 \quad [\text{Croquis Completamente Definido}]",
        "ejemplo": "Problema 1: En el modelado paramétrico de un cubo de buje (hub) de turbina eólica de 2 MW, la geometría depende de 3 variables maestras: diámetro del eje del rotor D_eje = 600 mm, diámetro de pernos de fijación de pala D_pala = 2100 mm y espesor de pared de fundición nodular t = 65 mm. Se define una ecuación paramétrica de diseño donde el radio de empalme estructural r_fillet se calcula automáticamente para evitar concentración de tensiones como r_fillet = 0.35 * t = 22.75 mm. Si la potencia de la turbina escala a 3.5 MW, el diámetro del eje aumenta a D_eje = 750 mm y el espesor a t = 85 mm. Al actualizar la tabla de diseño vinculada en Excel, el software CAD recalcula todas las operaciones de revolución, vaciado y matriz circular de 64 taladros M36 en un único paso regenerativo sin errores de reconstrucción topológica ni pérdida de referencias de ensamble. Problema 2: En un croquis 2D con 8 entidades lineales y 6 arcos tangentes, un grado de libertad no restringido (under-defined) provoca distorsiones imprevistas de geometría durante la actualización de la base de datos.",
        "bloque_sugerido": "Modelado Paramétrico 45 min • Ecuaciones globales y tablas de configuración de diseño",
        "slides": [
            {
                "numero": 1,
                "seccion": "FILOSOFÍA PARAMÉTRICA",
                "titulo": "Intención de Diseño (Design Intent)",
                "puntos": [
                    "La intención de diseño define cómo debe comportarse y mutar el modelo 3D cuando sus dimensiones cambian.",
                    "Un croquis debe estar 100% completamente definido (negro en SolidWorks/Inventor), eliminando cualquier grado de libertad errático.",
                    "Relaciones geométricas (tangencia, concentricidad, simetría) deben prevalecer sobre las cotas numéricas rígidas."
                ]
            },
            {
                "numero": 2,
                "seccion": "TABLAS Y CONFIGURACIONES",
                "titulo": "Familias de Piezas y Estandarización",
                "puntos": [
                    "Permite crear bibliotecas completas de bridas, válvulas y pernos a partir de un único archivo maestro de pieza.",
                    "Actualización asociativa: los cambios en la pieza maestra se propagan instantáneamente a los planos 2D y ensamblajes.",
                    "Reduce los tiempos de desarrollo en oficinas de ingeniería en más de un 70%."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Modelado de Superficies Complejas y Curvaturas NURBS para Perfiles Aerodinámicos",
        "objetivo": "Generar superficies de clase A con continuidad de curvatura G2/G3 mediante curvas B-splines y NURBS para el diseño aerodinámico de álabes eólicos y rodetes hidráulicos.",
        "concepto_clave_latex": r"\mathbf{C}(u) = \frac{\sum_{i=0}^n N_{i,p}(u) w_i \mathbf{P}_i}{\sum_{i=0}^n N_{i,p}(u) w_i} \quad ; \quad G^0: \text{Posición} \;, G^1: \text{Tangencia} \;, G^2: \text{Curvatura}",
        "ejemplo": "Problema 1: El álabe de un aerogenerador de 65 metros de longitud se define mediante 18 estaciones transversales de perfiles aerodinámicos normalizados (NACA 63-418 en la punta, DU 91-W2-250 en la sección media y sección cilíndrica en la raíz). La transición geométrica exige un solevado (loft) con curvas guía tridimensionales que mantengan continuidad de curvatura G2 (igualdad de radio de curvatura y vector normal) para evitar desprendimiento turbulento del flujo laminar. Si la transición se realizara con continuidad simple G1 (solo tangencia), el salto brusco en la segunda derivada d^2C/du^2 generaría una inflexión superficial visible que incrementa el arrastre parásito C_d en un 4.5% y genera ruidos aeroacústicos perceptibles. Mediante un peine de curvatura (curvature comb) se verifica que el radio de curvatura rho varía monótonamente a lo largo del extradós e intradós sin singularidades ni inversión de pendiente. Problema 2: Las superficies NURBS de grado p = 3 con pesos ponderados w_i permiten modelar secciones circulares exactas y transiciones elípticas en el borde de ataque del álabe.",
        "bloque_sugerido": "Superficies Avanzadas 45 min • Continuidad G0/G1/G2 y generación de perfiles con curvas guía",
        "slides": [
            {
                "numero": 1,
                "seccion": "GEOMETRÍA COMPUTACIONAL",
                "titulo": "Fundamentos de NURBS y Continuidad",
                "puntos": [
                    "NURBS (Non-Uniform Rational B-Splines): Estándar matemático universal para modelar formas libres tridimensionales suaves.",
                    "G0 (Contacto): Coincidencia posicional en la arista común; genera bordes afilados o pliegues.",
                    "G1 (Tangencia): Los vectores tangentes son colineales; la transición visual es suave pero la aceleración geométrica es discontinua.",
                    "G2 (Curvatura): Coincidencia en el centro y radio de curvatura instantáneo; indispensable en aerodinámica y óptica reflectante."
                ]
            },
            {
                "numero": 2,
                "seccion": "DIAGNÓSTICO SUPERFICIAL",
                "titulo": "Rayas de Cebra y Peines de Curvatura",
                "puntos": [
                    "El análisis de franjas de cebra (Zebra Stripes) simula la reflexión de luz para detectar visualmente imperfecciones y discontinuidades.",
                    "Bordes desalineados inducen micro-vórtices en turbomaquinaria que reducen el rendimiento isentrópico de la máquina.",
                    "Las herramientas Surface Loft y Boundary Surface son los pilares del modelado de álabes en SolidWorks y Siemens NX."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Ensamblajes Mecánicos Complejos: Cinemática, Grados de Libertad y Colisiones",
        "objetivo": "Construir ensamblajes mecánicos jerárquicos de sistemas de potencia con restricciones cinemáticas y evaluar interferencias dinámicas y grados de libertad remanentes.",
        "concepto_clave_latex": r"M = 6(n - 1) - \sum_{i=1}^j (6 - f_i) \quad [\text{Criterio de Kutzbach-Grübler en 3D}]",
        "ejemplo": "Problema 1: En un mecanismo de seguimiento solar biaxial para concentración fotovoltaica, la estructura móvil consta de n = 5 eslabones rígidos (pedestal fijo, horquilla de azimut, marco de elevación y 2 actuadores lineales electro-hidráulicos). Se cuenta con una junta de revolución para el eje de azimut (f_1 = 1 GDL), una junta de revolución para elevación (f_2 = 1 GDL) y cuatro uniones de rótula esférica (f = 3 GDL cada una) en los extremos de los actuadores cilíndricos (j = 2 cilíndricas con f = 2 GDL). Aplicando el criterio de Kutzbach-Grübler en 3D: M = 6(5 - 1) - [(6 - 1) + (6 - 1) + 2*(6 - 2) + 4*(6 - 3)] = 24 - [5 + 5 + 8 + 12] = 24 - 30 = -6 (sistema aparentemente hiperestático sobre-restringido). Para permitir el movimiento real de los dos ejes ortogonales sin atasco mecánico ni deformaciones de torsión, se reemplazan dos rótulas por uniones cardán de 2 GDL y se calcula el rango cinemático de movimiento: azimut de 0° a 340° y elevación de 10° a 85°. La detección dinámica de colisiones en SolidWorks verifica que durante la posición de tormenta (defensa horizontal a 0° de elevación con vientos de 140 km/h) existe una holgura libre mínima de 45 mm entre la biela del actuador y el pedestal central. Problema 2: El análisis de interferencia estática en un tren de potencia eólico identifica una colisión de 1.8 mm entre los tornillos de fijación del disco de freno y la carcasa del multiplicador de engranajes planetarios.",
        "bloque_sugerido": "Ensamblajes Cinemáticos 45 min • Detección de interferencias y movilidad de Kutzbach",
        "slides": [
            {
                "numero": 1,
                "seccion": "ARQUITECTURA DE ENSAMBLAJES",
                "titulo": "Gestión de Grandes Ensamblajes (Large Assemblies)",
                "puntos": [
                    "Uso de subensamblajes jerárquicos modulares para optimizar la memoria RAM y la GPU de la estación de trabajo.",
                    "Componentes aligerados (Lightweight / SpeedPak): Cargan únicamente la información gráfica sin el árbol de operaciones completo.",
                    "Relaciones de posición cinemáticas: Coincidencia, concentricidad, distancia límite, engranaje y tornillo sinfín."
                ]
            },
            {
                "numero": 2,
                "seccion": "VERIFICACIÓN DIGITAL",
                "titulo": "Detección de Colisiones y Holguras",
                "puntos": [
                    "Interferencia Estática: Detecta solapamientos de volumen entre sólidos rígidos debido a errores de cota.",
                    "Interferencia Dinámica en Movimiento: Identifica choques entre eslabones en cualquier ángulo de la trayectoria operativa.",
                    "Previene costosos errores de montaje en campo y rotura de componentes en la fase de prototipado físico."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Tolerancias Geométricas y Dimensionales (GD&T - ASME Y14.5M): Datums y Zonas",
        "objetivo": "Aplicar la norma internacional ASME Y14.5M para definir marcos de control de características (Feature Control Frames), datums de referencia y zonas de tolerancia cilíndricas.",
        "concepto_clave_latex": r"\text{Posición}: \;\; \begin{array}{|c|c|c|c|} \hline \bigoplus & \varnothing 0.05 \text{ \textcircled{M}} & \text{A} & \text{B} & \text{C} \\ \hline \end{array} \quad ; \quad \text{Bonus} = \text{MMC} - \text{Real}",
        "ejemplo": "Problema 1: En la brida de acoplamiento de un eje de transmisión de generador síncrono de 10 MW (eje de 250 mm de diámetro), se especifican 12 taladros pasantes de diámetro nominal 30 mm para pernos de alta resistencia de clase 10.9. El plano define la tolerancia de posición con respecto al datum primario A (cara plana de apoyo perpendicular), datum secundario B (diámetro exterior de centrado) y datum terciario C (chavetero de orientación): [Posición | Diámetro 0.08 (M) | A | B | C]. Dimensión del agujero en Condición de Máximo Material (MMC): 30.00 mm. Dimensión en Condición de Mínimo Material (LMC): 30.15 mm. Si un taladro maquinado en CNC mide 30.10 mm de diámetro real, calcular la tolerancia de posición permitida aprovechando la tolerancia de bonificación (Bonus Tolerance): Bonus = Diámetro_real - MMC = 30.10 - 30.00 = 0.10 mm. Tolerancia de posición total admisible = Tolerancia_base + Bonus = 0.08 + 0.10 = 0.18 mm de zona cilíndrica. Si el centro real del taladro se desvía Delta_x = 0.05 mm y Delta_y = 0.06 mm respecto a su posición teórica exacta básica: Desviación radial r = sqrt(0.05^2 + 0.06^2) = sqrt(0.0025 + 0.0036) = 0.0781 mm. Diámetro de la zona de posición real ocupada: D_zona = 2 * r = 2 * 0.0781 = 0.1562 mm. Como 0.1562 mm <= 0.18 mm, la pieza es ACEPTADA por control de calidad dimensional, salvando un componente de 15,000 USD de ser desechado erróneamente. Problema 2: La tolerancia de coaxialidad y cabeceo circular (circular runout < 0.02 mm) en ejes de alta velocidad evita vibraciones destructivas por desbalance dinámico.",
        "bloque_sugerido": "Metrología y GD&T 45 min • Marcos de control, datums ASME Y14.5M y tolerancia de bonificación",
        "slides": [
            {
                "numero": 1,
                "seccion": "LENGUAJE GD&T INDUSTRIAL",
                "titulo": "Superando la Tolerancia Tradicional +-",
                "puntos": [
                    "La tolerancia cartesiana tradicional (+- Delta_x, +- Delta_y) genera zonas de tolerancia cuadradas irreales y acumulación de tolerancias (stack-up).",
                    "GD&T utiliza zonas de tolerancia circulares y cilíndricas que aumentan el área de aceptación en un 57% sin afectar la función mecánica.",
                    "El marco de control vincula la tolerancia a datums funcionales de ensamblaje (A, B, C) que replican el montaje real."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONDICIONES DE MATERIAL",
                "titulo": "MMC (Máximo Material) y LMC",
                "puntos": [
                    "MMC (Condición de Máximo Material): El agujero más pequeño o el eje más grande (máximo peso de la pieza).",
                    "Símbolo (M): Otorga tolerancia de bonificación cuando la dimensión real se aparta de la condición más desfavorable.",
                    "Permite el diseño de calibres funcionales 'Pasa / No Pasa' rígidos para control de calidad masivo en planta."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Diseño para Manufactura y Ensamble (DFMA) en Componentes de Conversión de Energía",
        "objetivo": "Optimizar geometrías 3D para procesos de fundición, forja, mecanizado CNC por arranque de viruta y conformado de chapa metálica minimizando costos y tiempos de fabricación.",
        "concepto_clave_latex": r"\text{Eficiencia DFMA} = \frac{N_{min} \times t_a}{t_{total}} \quad ; \quad \text{Ángulo de Salida}: \theta_{draft} \ge 1.5^\circ - 3.0^\circ",
        "ejemplo": "Problema 1: El cárter de la caja multiplicadora de una turbina eólica se proyecta fabricar en fundición de hierro nodular EN-GJS-400. Se somete la pieza a un análisis DFM (Design for Manufacturing) en CAD detectando 3 errores críticos: 1) Paredes verticales con ángulo de desmolde nulo (0° draft), lo que provocaría desgarro de las arenas de moldeo y rechazo de la pieza fundida. Se aplica una operación de ángulo de salida de 2.0° hacia la línea de partición. 2) Variaciones bruscas de espesor de pared de 40 mm a 12 mm sin transiciones graduales, lo que generaría cavidades de contracción interna (rechupes) y porosidad durante la solidificación no uniforme. Se unifica el espesor a 25 mm con nervios rigidizadores de refuerzo de espesor t_rib = 0.6 * t_pared = 15 mm. 3) Presencia de esquinas vivas internas que concentran esfuerzos y provocan agrietamiento térmico. Se aplican redondeos de R = 8 mm. El rediseño reduce la masa total del cárter de 3800 kg a 2950 kg (ahorro de material del 22.4%), elimina la necesidad de machos de arena complejos y abarata el maquinado CNC posterior al reducir el volumen de viruta arrancada en un 35%. Problema 2: La consolidación de piezas en el conjunto de soporte de rodamientos reduce el número de componentes de 14 a 3 piezas integradas, reduciendo el tiempo de montaje en un 68%.",
        "bloque_sugerido": "DFMA Avanzado 45 min • Reglas de diseño para fundición, mecanizado CNC y chapa metálica",
        "slides": [
            {
                "numero": 1,
                "seccion": "INGENIERÍA CONCURRENTE",
                "titulo": "Principios DFMA de Boothroyd & Dewhurst",
                "puntos": [
                    "Diseño para Ensamble (DFA): Minimizar el número de piezas, estandarizar fijaciones y garantizar inserción unidireccional vertical descendente.",
                    "Diseño para Manufactura (DFM): Adaptar las geometrías a las limitaciones intrínsecas de cada proceso de conformado.",
                    "El 70% del costo total de un producto se define durante la fase conceptual de modelado CAD 3D."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGLAS GEOMÉTRICAS CLAVE",
                "titulo": "Fundición y Mecanizado CNC",
                "puntos": [
                    "Fundición: Espesor de pared uniforme, radios de empalme generosos y ángulos de salida en todas las caras perpendiculares a la partición.",
                    "Mecanizado CNC: Evitar cavidades profundas con relación profundidad/diámetro > 4 para impedir deflexión y vibración de la fresa.",
                    "Chapa metálica: Respetar radios mínimos de plegado (R >= espesor) y factores K para evitar fisuras por tracción en la fibra neutra."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Modelado CAD de Turbomaquinaria: Rotores Pelton, Francis y Álabes Axiales 3D",
        "objetivo": "Modelar rodetes hidráulicos Pelton y Francis mediante perfiles hidrodinámicos curvados en 3D, cucharas de doble cazoleta y alabes directores distribuidores.",
        "concepto_clave_latex": r"\text{Pelton}: \;\; \beta_2 \approx 165^\circ \quad ; \quad \text{Francis}: \;\; \frac{W_2^2 - W_1^2}{2} + \frac{U_1^2 - U_2^2}{2} + \frac{V_1^2 - V_2^2}{2} = g H_u",
        "ejemplo": "Problema 1: En el modelado 3D de un rodete Pelton monobloque de 22 cucharas para una caída neta H = 420 m y caudal Q = 1.2 m^3/s (diámetro primitivo D_p = 1.40 m): Cada cuchara consta de dos cazoletas semiesféricas divididas por una arista afilada central (splitter) que divide simétricamente el chorro de agua a velocidad V_1 = 89 m/s. El ángulo de salida del álabe se parametriza a beta_2 = 165° (deflexión de 165° con un ángulo de escape lateral de 15° para que el agua que abandona la cazoleta no golpee el dorso de la siguiente cuchara que entra en el chorro). El labio de entrada de la cuchara se corta con una escotadura periférica (cut-out) modelada mediante corte por revolución oblicua para permitir que el chorro alcance la arista central sin ser recortado prematuramente. La transición entre la base de la cuchara y el disco central de acero inoxidable forjado 13Cr-4Ni se modela con filetes de curvatura continua G2 de radio variable R_var = 18 mm a 32 mm, eliminando puntos de concentración de esfuerzos que inducirían fallas catastróficas por fatiga de alto ciclo (HCF). El modelo sólido final se reproduce mediante una matriz circular angular de 22 instancias a 360/22 = 16.364°. Problema 2: En turbinas Francis, el modelado del canal entre la corona (crown) y la banda (band) exige superficies complejas de revolución recortadas por álabes torcidos tridimensionalmente de espesor hidrodinámico variable.",
        "bloque_sugerido": "Turbomaquinaria CAD 45 min • Modelado 3D de cazoletas Pelton y coronas Francis",
        "slides": [
            {
                "numero": 1,
                "seccion": "GEOMETRÍA HIDRÁULICA AVANZADA",
                "titulo": "Cazoletas Pelton y Álabes Francis",
                "puntos": [
                    "La geometría debe minimizar el choque del chorro y guiar la inversión de cantidad de movimiento sin turbulencia.",
                    "La arista divisoria (splitter) debe mantenerse perfectamente afilada con radio de curvatura inferior a 0.5 mm.",
                    "El modelado por vaciado y operaciones de corte de barrido (swept cut) define los perfiles de entrada y salida hidrodinámicos."
                ]
            },
            {
                "numero": 2,
                "seccion": "FABRICACIÓN POR MECANIZADO CNC 5 EJES",
                "titulo": "Del Sólido CAD al Código G de Mecanizado",
                "puntos": [
                    "El espacio confinado entre cucharas contiguas exige fresado simultáneo en centros de mecanizado multieje de 5 ejes.",
                    "El modelo CAD se exporta en formato STEP AP242 o Parasolid (.x_t) para la programación de trayectorias en software CAM.",
                    "La precisión superficial geométrica es crítica para prevenir cavitación destructiva por caída de presión local."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Simulación Cinemática y Dinámica de Seguidores Solares (Trackers 1P y 2P)",
        "objetivo": "Simular el comportamiento dinámico y cinemático de seguidores solares monoaxiales (1P/2P) y biaxiales calculando momentos de torsión aerodinámica y cargas de accionamiento motor.",
        "concepto_clave_latex": r"T_{actuador} = J_{eq} \alpha + T_{aero}(\theta) + T_{gravedad}(\theta) \quad ; \quad T_{aero} = \frac{1}{2} C_T(\theta) \rho V_{viento}^2 A L",
        "ejemplo": "Problema 1: Un seguidor solar horizontal monoaxial monofila (1P) de 90 metros de longitud soporta 90 módulos fotovoltaicos bifaciales de 650 W (área total de vela A = 90 * 3.1 m^2 = 279 m^2, ancho de cuerda c = 2.4 m). La masa total de módulos y correas estructurales es M = 7500 kg, con centro de gravedad excéntrico a e = 0.08 m del eje de rotación del tubo de torsión. Momento de inercia rotacional respecto al eje: J = 28,500 kg*m^2. En ángulo de inclinación theta = 45°, bajo una ráfaga de viento de diseño V = 35 m/s (126 km/h, densidad del aire rho = 1.2 kg/m^3), el coeficiente de momento torsional aerodinámico obtenido en túnel de viento es C_T = 0.18. Momento aerodinámico estático: T_aero = 0.5 * C_T * rho * V^2 * A * c = 0.5 * 0.18 * 1.2 * (35)^2 * 279 * 2.4 = 0.108 * 1225 * 669.6 = 88,588 N*m = 88.59 kN*m. Momento gravitatorio por desbalance: T_grav = M * g * e * sin(45°) = 7500 * 9.81 * 0.08 * 0.7071 = 4162 N*m = 4.16 kN*m. Momento total requerido en el reductor de corona y tornillo sinfín (slewing drive): T_total = T_aero + T_grav = 88.59 + 4.16 = 92.75 kN*m. Se selecciona un reductor giratorio con capacidad de torque de retención de 110 kN*m y relación de transmisión i = 74:1, garantizando que el seguidor resista la ráfaga de viento sin girar involuntariamente. Problema 2: En seguidores solares largos, la inestabilidad aeroelástica por flameo torsional (torsional gallop / flutter) provoca oscilaciones divergentes que destruyen el tubo de torsión si no se instalan amortiguadores viscosos dampers en los extremos.",
        "bloque_sugerido": "Seguidores Solares 45 min • Cinemática de actuadores y torsión aerodinámica en trackers",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA DE TRACKERS HORIZONTALES",
                "titulo": "Arquitectura 1P vs 2P",
                "puntos": [
                    "Configuración 1P (Un módulo en vertical): Menor brazo de palanca aerodinámico y menor momento de torsión en el tubo.",
                    "Configuración 2P (Dos módulos en vertical): Reduce el número de hileras y motores pero duplica las fuerzas de torsión aerodinámica.",
                    "El tubo de torsión central (perfil redondo o cuadrado de 120-150 mm) soporta torsión pura combinada con flexión por peso propio."
                ]
            },
            {
                "numero": 2,
                "seccion": "DEFENSA ANTE EL VIENTO",
                "titulo": "Estrategias de Posición de Tormenta (Stow)",
                "puntos": [
                    "Posición horizontal (0°): Minimiza la fuerza de sustentación pero maximiza el riesgo de flameo aeroelástico por vórtices.",
                    "Posición inclinada de bloqueo (45° - 60°): Reduce las oscilaciones torsionales a costa de aumentar la fuerza de arrastre global en los pilotes.",
                    "Algoritmo de 'Backtracking': Evita sombras mutuas inter-filas durante las primeras horas de la mañana y últimas de la tarde."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Modelado de Estructuras Metálicas Fotovoltaicas y Análisis de Cargas (NSR-10)",
        "objetivo": "Modelar estructuras metálicas en perfiles de acero conformado en frío (Cold-Formed Steel) para parques solares y calcular cargas de viento y sismo según NSR-10 / ASCE 7.",
        "concepto_clave_latex": r"q_z = 0.613 K_z K_{zt} K_d K_e V^2 \quad [\text{N/m}^2] \quad ; \quad p = q_z G C_p - q_i (G C_{pi})",
        "ejemplo": "Problema 1: Se modela una mesa fija fotovoltaica para 40 módulos (2 filas de 20 módulos en orientación vertical) en Santa Marta, Colombia. Altura media del techo z = 2.8 m. Parámetros de viento según la norma colombiana NSR-10 (Capítulo B.6): Velocidad básica del viento V = 38 m/s (136.8 km/h). Factor de direccionalidad del viento K_d = 0.85. Coeficiente topográfico K_zt = 1.0 (terreno plano costero). Factor de exposición K_z = 0.85 (Exposición C a baja altura). Factor de elevación K_e = 1.0 (nivel del mar). Presión dinámica básica de viento: q_z = 0.613 * K_z * K_zt * K_d * K_e * V^2 = 0.613 * 0.85 * 1.0 * 0.85 * 1.0 * (38)^2 = 0.4428 * 1444 = 639.4 N/m^2. Para un ángulo de inclinación de la mesa de 12°, el factor de ráfaga es G = 0.85 y el coeficiente de presión neta para marquesinas abiertas es C_p,net = -1.35 (fuerza de succión hacia arriba). Presión de diseño neta: p_net = 639.4 * 0.85 * (-1.35) = -733.7 N/m^2 (succión ascendente de 73.4 kgf/m^2). Área tributaria de cada correa (perfil C 100x50x2 mm en acero galvanizado estructural S350GD, L = 4.2 m): A_trib = 4.2 * 1.2 = 5.04 m^2. Fuerza total de levantamiento por correa: F_up = 733.7 * 5.04 = 3698 N. Peso propio del módulo y correa: W_propio = 280 N. Carga neta de tracción sobre el pilote de hincado: T_hincado = 3698 - 280 = 3418 N (348.4 kgf de extracción). Se especifica una profundidad de hincado en terreno arenoso de 1.80 metros garantizando un factor de seguridad FS >= 2.0 frente al arrancamiento por viento. Problema 2: En estructuras de aluminio extruido 6005-T5, la verificación de corrosión galvánica exige el uso de almohadillas de aislamiento de EPDM en el contacto con tornillería de acero inoxidable A2/A4.",
        "bloque_sugerido": "Estructuras Solares 45 min • Cargas de viento NSR-10 y diseño de perfiles conformados en frío",
        "slides": [
            {
                "numero": 1,
                "seccion": "NORMATIVA DE CARGAS ESTRUCTURALES",
                "titulo": "Viento y Succión en Marquesinas Abiertas",
                "puntos": [
                    "A diferencia de edificios cerrados, las estructuras solares sufren presiones simultáneas por el intradós y extradós.",
                    "La fuerza crítica gobernante casi siempre es el levantamiento por succión (uplift) en lugar de la gravedad.",
                    "La norma NSR-10 en Colombia y la ASCE 7-16 en EE.UU. dictan las combinaciones de carga factorizadas LRFD."
                ]
            },
            {
                "numero": 2,
                "seccion": "PERFILERÍA Y CIMENTACIÓN",
                "titulo": "Hincado Directo vs Zapatas de Concreto",
                "puntos": [
                    "Pilotes de acero galvanizado hincados por impacto: Solución rápida y de bajo costo para terrenos cohesivos.",
                    "Perfiles C y Z con labios rigidizadores: Maximizan el momento de inercia y resistencia a flexión con mínimo espesor.",
                    "Micropilotes con bulbo de hormigón: Obligatorios en terrenos rocosos o con nivel freático elevado."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis por Elementos Finitos (FEA): Esfuerzos de von Mises y Deformación en Soportes",
        "objetivo": "Realizar análisis elastostáticos lineales por elementos finitos (FEA) de componentes estructurales de turbinas y soportes solares evaluando tensiones de von Mises y factores de seguridad.",
        "concepto_clave_latex": r"\sigma_{vM} = \sqrt{\frac{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}{2}} \le \frac{S_y}{\text{FS}} \quad ; \quad \mathbf{K} \mathbf{u} = \mathbf{F}",
        "ejemplo": "Problema 1: Se realiza un análisis FEA del soporte de fundición de acero (ASTM A36, límite elástico S_y = 250 MPa) que sujeta el cojinete principal de un aerogenerador pequeño de 10 kW. El componente se somete a una fuerza axial de empuje del rotor de F_thrust = 8500 N y un momento de vuelco vertical M = 3200 N*m. Se discretiza el sólido mediante una malla tetraédrica parabólica sólida de 10 nodos (SOLID186) con un tamaño de elemento global de 10 mm y un refinamiento de malla local de 2 mm en los radios de entalla de la base. Número total de nodos: 84,200 (grados de libertad u_x, u_y, u_z por nodo). Se fija la base cilíndrica con restricción fija (fixed support u = 0). La resolución del sistema de rigidez K * u = F arroja un desplazamiento elástico máximo en la punta de delta_max = 0.42 mm. El tensor de esfuerzos principal en la zona de concentración arroja: sigma_1 = 142 MPa, sigma_2 = 28 MPa, sigma_3 = -18 MPa. Tensión equivalente de von Mises: sigma_vM = sqrt([(142 - 28)^2 + (28 - (-18))^2 + (-18 - 142)^2] / 2) = sqrt([114^2 + 46^2 + (-160)^2] / 2) = sqrt([12996 + 2116 + 25600] / 2) = sqrt(40712 / 2) = sqrt(20356) = 142.67 MPa. Factor de seguridad respecto a la fluencia plástica: FS = S_y / sigma_vM = 250 / 142.67 = 1.75. Como el factor de seguridad exigido por la norma IEC 61400-2 es FS >= 1.50, el diseño se aprueba sin requerir refuerzos de masa adicionales. Problema 2: En análisis de convergencia de malla (Mesh Convergence), si el esfuerzo máximo varía menos del 2% al duplicar el número de elementos, se descartan singularidades matemáticas causadas por restricciones puntuales.",
        "bloque_sugerido": "Simulación FEA 45 min • Mallado tetraédrico, tensiones de von Mises y convergencia",
        "slides": [
            {
                "numero": 1,
                "seccion": "MÉTODO DE ELEMENTOS FINITOS (FEM)",
                "titulo": "Discretización y Matriz de Rigidez",
                "puntos": [
                    "Divide un continuo geométrico complejo en un número finito de elementos interconectados por nodos.",
                    "Elementos de 1er orden (lineales): Rígidos y propensos a bloqueo por cortante (shear locking).",
                    "Elementos de 2do orden (cuadráticos/parabólicos): Incorporan nodos medios; capturan gradientes de tensión con alta precisión."
                ]
            },
            {
                "numero": 2,
                "seccion": "CRITERIOS DE FALLA",
                "titulo": "Teoría de la Energía de Distorsión (von Mises)",
                "puntos": [
                    "Criterio estándar para materiales dúctiles (aceros estructurales, aluminio, cobre).",
                    "Postula que la fluencia inicia cuando la energía de distorsión elástica alcanza el valor correspondiente al ensayo de tracción uniaxial.",
                    "Esfuerzo de Tresca (máximo esfuerzo cortante): Más conservador; utilizado en recipientes a presión y calderas ASME."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Análisis Modal y Frecuencias Propias: Resonancia en Torres Eólicas y Ejes Rotativos",
        "objetivo": "Calcular las frecuencias naturales y modos de vibración estructurales mediante análisis modal numérico evitando la resonancia armónica con las frecuencias de paso de pala 1P y 3P.",
        "concepto_clave_latex": r"\det(\mathbf{K} - \omega^2 \mathbf{M}) = 0 \quad ; \quad f_n = \frac{\omega_n}{2\pi} \quad ; \quad \text{Régimen Soft-Stiff}: f_{1P} < f_{n,1} < f_{3P}",
        "ejemplo": "Problema 1: Una torre eólica tubular cónica de acero de 80 metros de altura soporta una nacelle y rotor de 3 palas con una masa en cabeza (top mass) de M_top = 85,000 kg. El rotor gira en un rango de operación variable de 8 a 18 rpm. Frecuencias de excitación rotacional del rotor (frecuencia 1P): f_1P,min = 8 / 60 = 0.133 Hz; f_1P,max = 18 / 60 = 0.300 Hz. Frecuencias de paso de pala (frecuencia 3P debida a sombra de torre y cizalladura del viento): f_3P,min = 3 * 0.133 = 0.400 Hz; f_3P,max = 3 * 0.300 = 0.900 Hz. El análisis modal por elementos finitos calcula el primer modo natural de flexión de la torre cantilever: f_n,1 = 0.345 Hz. Diagrama de Campbell de resonancia: La frecuencia natural f_n,1 (0.345 Hz) se sitúa con un margen de seguridad del 15% por encima de la banda 1P máxima (0.300 * 1.15 = 0.345 Hz) y un 14% por debajo de la banda 3P mínima (0.400 * 0.86 = 0.344 Hz). Clasificación estructural: La torre opera en el régimen óptimo de diseño 'Soft-Stiff', evitando resonancia destructiva inducida por vibraciones armónicas forzadas sin exigir el peso masivo de una torre 'Stiff-Stiff' (f_n > 0.90 Hz). Problema 2: En ejes de turbogeneradores de vapor a 3600 rpm (60 Hz), la primera velocidad crítica lateral de flexión de Jeffcott debe superarse rápidamente durante el arranque con rampas de aceleración altas para no destruir los cojinetes de película de aceite.",
        "bloque_sugerido": "Dinámica y Vibraciones 45 min • Análisis modal numérico y diagrama de Campbell en aerogeneradores",
        "slides": [
            {
                "numero": 1,
                "seccion": "DINÁMICA ESTRUCTURAL LINEAL",
                "titulo": "Modos Propios y Autovalores",
                "puntos": [
                    "Las frecuencias naturales dependen únicamente de la distribución de masa [M] y rigidez [K] de la estructura libre de amortiguamiento.",
                    "Modo 1: Flexión fundamental (cantilever sway); Modo 2: Segunda flexión con nodo intermedio; Modo 3: Torsión pura.",
                    "La resonancia ocurre cuando una fuerza periódica coincide con una frecuencia natural, amplificando las oscilaciones hasta el fallo catastrófico."
                ]
            },
            {
                "numero": 2,
                "seccion": "DISEÑO AEROELÁSTICO",
                "titulo": "El Diagrama de Campbell",
                "puntos": [
                    "Grafica las frecuencias de excitación armónica (1P, 2P, 3P) en función de las revoluciones por minuto del rotor.",
                    "Torre Soft-Soft: f_n < 1P (ultra-flexible, difícil control en arranque); Soft-Stiff: 1P < f_n < 3P (estándar de la industria moderna).",
                    "Exigido por la norma DNV-GL y la certificación IEC 61400-1 para parques eólicos marinos y terrestres."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Simulación Térmica y Termo-Mecánica en CAD/CAE: Disipadores y Módulos de Potencia",
        "objetivo": "Modelar campos de temperatura estacionarios y transitorios por conducción y convección en disipadores de calor de inversores solares y evaluar deformaciones térmicas acopladas.",
        "concepto_clave_latex": r"R_{th,tot} = R_{th,j-c} + R_{th,c-s} + R_{th,s-a} \quad ; \quad \Delta T = \dot{Q}_{loss} \cdot R_{th} \quad ; \quad \varepsilon_{th} = \alpha \Delta T",
        "ejemplo": "Problema 1: Un inversor solar fotovoltaico trifásico de 100 kW utiliza 6 módulos IGBT de potencia que disipan en conjunto Q_loss = 2400 W de pérdidas por conmutación y conducción. Cada módulo mide 106 x 62 mm y tiene una resistencia térmica unión-carcasa R_th,j-c = 0.08 K/W. El material de interfaz térmica (TIM de pasta térmica con k = 3.5 W/(m*K) y espesor t = 50 micras) presenta R_th,c-s = 0.02 K/W. Se modela en 3D un disipador de aluminio extruido 6063-T6 (k = 200 W/(m*K)) de 600 mm de largo con 48 aletas longitudinales de 80 mm de altura y 2.5 mm de espesor. Se aplica un flujo de aire forzado generado por 2 ventiladores axiales con caudal total de 350 m^3/h (velocidad entre aletas V = 4.2 m/s, coeficiente de convección forzada h = 42 W/(m^2*K)). La simulación térmica en estado estacionario calcula una resistencia térmica disipador-ambiente de R_th,s-a = 0.018 K/W. A una temperatura ambiente de diseño de T_amb = 45 °C en La Guajira: Temperatura del disipador de calor: T_s = T_amb + Q_loss * R_th,s-a = 45 + 2400 * 0.018 = 45 + 43.2 = 88.2 °C. Temperatura de la unión de silicio del semiconductor: T_j = T_s + (Q_loss/6) * (R_th,j-c + R_th,c-s) = 88.2 + (400) * (0.08 + 0.02) = 88.2 + 40.0 = 128.2 °C. Como T_j = 128.2 °C está por debajo de la temperatura máxima admisible del fabricante de T_j,max = 150 °C con un margen de seguridad de 21.8 °C, el diseño térmico se valida. En el análisis termo-mecánico acoplado, la dilatación diferencial entre el aluminio (alpha = 23 * 10^-6 K^-1) y el cobre del módulo (alpha = 16.5 * 10^-6 K^-1) genera un esfuerzo de flexión térmico de 28 MPa en la tornillería M5. Problema 2: En disipadores de convección natural para micro-inversores sellados IP67, la separación óptima entre aletas calculada por la correlación de Bar-Cohen evita la interferencia de capas límite térmicas.",
        "bloque_sugerido": "Simulación Térmica 45 min • Redes de resistencia térmica j-c-s-a y convección forzada en FEA",
        "slides": [
            {
                "numero": 1,
                "seccion": "GESTIÓN TÉRMICA DE ELECTRÓNICA DE POTENCIA",
                "titulo": "La Cadena de Resistencia Térmica",
                "puntos": [
                    "El calor debe evacuar desde la minúscula pastilla de silicio (unión) hasta el aire ambiente sin superar 125-150 °C.",
                    "TIM (Thermal Interface Material): Elimina las micro-bolsas de aire aislante entre las superficies metálicas mecanizadas.",
                    "El 54% de las fallas catastróficas en inversores solares y convertidores eólicos son originadas por sobrecalentamiento térmico."
                ]
            },
            {
                "numero": 2,
                "seccion": "ACOPLAMIENTO MULTIFÍSICO CAE",
                "titulo": "Esfuerzos Termomecánicos y Fatiga",
                "puntos": [
                    "El gradiente espacial de temperatura induce dilatación térmica desigual (alpha * Delta_T).",
                    "Genera esfuerzos cortantes cíclicos masivos en las capas de soldadura de los transistores (fatiga termo-mecánica).",
                    "La simulación acoplada transfiere automáticamente el mapa de temperaturas del solver térmico como carga al solver estructural."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Análisis de Pandeo Lineal y No Lineal (Buckling) en Torres Eólicas y Cilindros",
        "objetivo": "Calcular la carga crítica de pandeo elástico de Euler y factores de reducción por imperfección en torres eólicas esbeltas y carcasas cilíndricas según Eurocódigo 3.",
        "concepto_clave_latex": r"P_{cr} = \frac{\pi^2 E I}{(K L)^2} \quad ; \quad \sigma_{cr,shell} = 0.605 E \frac{t}{r} \alpha_{imp} \quad ; \quad \text{BLF} = \frac{\lambda_{cr}}{\text{Carga Aplicada}}",
        "ejemplo": "Problema 1: Una torre eólica tubular de acero estructural S355 (módulo de elasticidad E = 210 GPa, Poisson nu = 0.3) tiene una sección cilíndrica intermedia de radio exterior r = 1800 mm y espesor de pared t = 20 mm (relación radio/espesor r/t = 90). La sección soporta una carga axial combinada de peso propio y empuje de P = 4,200 kN. Tensión axial nominal de compresión: sigma_comp = P / (2 * pi * r * t) = 4,200,000 / (2 * pi * 1.8 * 0.02) = 4,200,000 / 0.2262 = 18,567,639 Pa = 18.57 MPa. Tensión clásica teórica de pandeo elástico local de membrana cilíndrica de Koiter: sigma_cl = 0.605 * E * (t / r) = 0.605 * (210,000 MPa) * (20 / 1800) = 127,050 * 0.01111 = 1411.6 MPa. De acuerdo con el Eurocódigo 3 (EN 1993-1-6) para estructuras cilíndricas delgadas, debido a la extrema sensibilidad a las imperfecciones geométricas iniciales de redondez (out-of-roundness) y soldaduras circunferenciales, se aplica un factor de reducción por imperfección elástica alpha_imp = 0.28. Tensión elástica de pandeo característica de diseño: sigma_cr = alpha_imp * sigma_cl = 0.28 * 1411.6 = 395.25 MPa. Esbeltez relativa de la lámina: lambda_s = sqrt(S_y / sigma_cr) = sqrt(355 / 395.25) = 0.9477. El factor de reducción por interacción elastoplástica resulta chi = 0.68. Resistencia de cálculo al pandeo local: sigma_Rd = chi * S_y / gamma_M1 = 0.68 * 355 / 1.1 = 219.45 MPa. Factor de Carga de Pandeo (Buckling Load Factor - BLF): BLF = sigma_Rd / sigma_comp = 219.45 / 18.57 = 11.82. Como BLF > 3.0, la torre posee una holgura segura frente al colapso catastrófico por arrugamiento local de la chapa. Problema 2: En recipientes a presión cilíndricos horizontales sometidos a vacío interno o presión hidrostática externa, la adición de anillos atiesadores circunferenciales (stiffener rings) incrementa el número de ondas circunferenciales de pandeo n = 4 a n = 8, multiplicando la rigidez por cuatro sin aumentar el espesor global de la chapa.",
        "bloque_sugerido": "Estabilidad Estructural 45 min • Pandeo lineal eigenvalue y colapso de cascarones Eurocódigo 3",
        "slides": [
            {
                "numero": 1,
                "seccion": "INESTABILIDAD POR PANDEO",
                "titulo": "Bifurcación de Equilibrio",
                "puntos": [
                    "El pandeo es un modo de fallo catastrófico repentino donde la estructura pierde rigidez transversal antes de alcanzar la fluencia plástica.",
                    "Pandeo Global de Euler: Afecta a la torre completa como una columna esbelta en voladizo (K = 2.0).",
                    "Pandeo Local de Cascarón (Shell Buckling): Abolladura elástica localizada de la chapa metálica cilíndrica bajo compresión axial o flexión."
                ]
            },
            {
                "numero": 2,
                "seccion": "SENSIBILIDAD A IMPERFECCIONES",
                "titulo": "Teoría No Lineal de Koiter",
                "puntos": [
                    "Los cascarones cilíndricos delgados son las estructuras más sensibles del mundo a desalineaciones milimétricas de soldadura.",
                    "Una imperfección geométrica de solo la mitad del espesor de la chapa (t/2) puede reducir la capacidad portante real a menos del 35% del valor teórico.",
                    "El Eurocódigo 3 clasifica la calidad de fabricación en Clases A, B y C mediante estrictas tolerancias de control dimensional."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelado de Tuberías Industriales y Trazado Isométrico 3D (ASME B31.3 / B31.4)",
        "objetivo": "Diseñar trazados tridimensionales de tuberías industriales para plantas energéticas y geotérmicas generando planos isométricos y listas de materiales (BOM) conformes a ASME B31.3.",
        "concepto_clave_latex": r"t = \frac{P D}{2(S E W + P Y)} + c \quad ; \quad \text{Expansión Térmica}: \Delta L = \alpha L \Delta T",
        "ejemplo": "Problema 1: En una planta geotérmica de vapor saturado a 180 °C (453.15 K) y presión de diseño P = 1.0 MPa (145 psi), se traza una línea de tubería troncal de vapor de acero al carbono ASTM A106 Grado B (tensión admisible de código S = 118 MPa, factor de junta soldada E = 1.0, coeficiente Y = 0.4, sobreespesor de corrosión admisible c = 3.0 mm). Diámetro exterior nominal de la tubería NPS 12 (D = 323.8 mm). Cálculo del espesor mínimo de pared por código ASME B31.3: t_min = (P * D) / [2 * (S * E + P * Y)] + c = (1.0 * 323.8) / [2 * (118 * 1.0 + 1.0 * 0.4)] + 3.0 = 323.8 / (2 * 118.4) + 3.0 = 323.8 / 236.8 + 3.0 = 1.367 + 3.0 = 4.367 mm. Considerando una tolerancia de fabricación de laminación del 12.5%: t_requerido = 4.367 / 0.875 = 4.99 mm. Se selecciona tubería estándar Schedule 20 (espesor nominal 6.35 mm > 4.99 mm). La longitud recta total de la tubería entre anclajes fijos es L = 80 metros. Con coeficiente de dilatación térmica alpha = 12.5 * 10^-6 K^-1 y temperatura de montaje de 25 °C (Delta_T = 180 - 25 = 155 K): Dilatación térmica longitudinal total: Delta_L = alpha * L * Delta_T = (12.5 * 10^-6) * 80 * 155 = 0.155 metros = 155 mm. Para absorber esta expansión de 15.5 cm sin sobrecargar las bridas de las turbinas con momentos torsores inadmisibles, el software de enrutamiento 3D diseña una lira o bucle de expansión (expansion loop) en forma de U de 4 x 4 metros, ubicando soportes deslizantes con patines de teflón PTFE y guías laterales. Problema 2: En la modelación del plano isométrico de tuberías con Plant 3D, el software inserta automáticamente empalmes biselados a 37.5°, codos de radio largo (R = 1.5 D) y genera el archivo PCF para análisis de flexibilidad de esfuerzos en CAESAR II.",
        "bloque_sugerido": "Piping 3D 45 min • Ecuación de espesor ASME B31.3 y diseño de lazos de dilatación térmica",
        "slides": [
            {
                "numero": 1,
                "seccion": "SISTEMAS DE TUBERÍAS INDUSTRIALES",
                "titulo": "Normativas ASME B31 para Piping",
                "puntos": [
                    "ASME B31.1: Tuberías de centrales eléctricas de generación de vapor y agua de alimentación de calderas.",
                    "ASME B31.3: Tuberías de plantas químicas, refinerías y complejos petroquímicos.",
                    "ASME B31.4 / B31.8: Oleoductos y gasoductos de transporte a larga distancia.",
                    "El espesor de pared debe resistir presión interna, presión externa de vacío y sobreespesor de corrosión por vida útil."
                ]
            },
            {
                "numero": 2,
                "seccion": "FLEXIBILIDAD TÉRMICA",
                "titulo": "Liras de Expansión y Soportaría",
                "puntos": [
                    "Tuberías calientes que no pueden expandirse generan esfuerzos compresivos masivos que doblan los tubos o arrancan bombas.",
                    "Liras en U, juntas de fuelle metálicas corrugadas y codos en Z disipan la deformación mediante flexión elástica.",
                    "Soportes de resorte constante y resorte variable compensan desplazamientos verticales manteniendo constante la carga."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Enrutamiento Eléctrico en 3D (Wiring & Harness): Bandejas, Cables y Radio de Curvatura",
        "objetivo": "Modelar el enrutamiento tridimensional de arneses de cables eléctricos de potencia y control en nacelles eólicas y cuartos de inversores respetando radios mínimos de curvatura y factores de llenado.",
        "concepto_clave_latex": r"R_{bend} \ge k \cdot D_{cable} \quad (k \approx 8 - 12) \quad ; \quad \text{Factor de Llenado}: \frac{\sum A_{cables}}{W_{tray} \cdot H_{tray}} \le 40\% - 50\%",
        "ejemplo": "Problema 1: En el interior de la torre tubular de un aerogenerador de 3.5 MW, se enrutan tres cables tripolares unipolares apantallados de media tensión (34.5 kV, cobre XLPE de sección 240 mm^2 con armadura de alambres de aluminio, diámetro exterior por cable D_cable = 48 mm). La norma IEC 60502-2 y el fabricante exigen un radio de curvatura dinámico mínimo durante la instalación de R_bend >= 12 * D_cable = 12 * 48 mm = 576 mm. En el paso por la plataforma intermedia de transición hacia la celda de media tensión, el software 3D Electrical Routing detecta una curva en el spline de enrutamiento con un radio de curvatura local de R_actual = 380 mm (violación crítica que estrangularía el aislamiento dieléctrico XLPE y provocaría descargas parciales destructivas a 34.5 kV). Se rediseña el soporte acodado para forzar un radio suave de R = 650 mm. Para la bandeja portacables perforada tipo escalera de W = 400 mm de ancho y H = 100 mm de peralte (área transversal bruta A_bandeja = 40,000 mm^2): Se enrutan 18 cables secundarios de potencia y control de diámetro medio d = 16 mm (área transversal total sumada = 18 * pi * 8^2 = 3619 mm^2). Factor de llenado de la bandeja: Llenado = 3619 / 40,000 = 9.05% (ampliamente inferior al límite reglamentario del RETIE / NEC del 40%, garantizando una disipación térmica por convección adecuada para no aplicar factores severos de desclasificación por agrupamiento). Problema 2: En la nacelle eólica, el bucle de caída libre de cables (cable droop loop) se modela cinemáticamente para permitir que la máquina gire libremente 720° en azimut durante las maniobras de orientación hacia el viento sin cizallar los conductores.",
        "bloque_sugerido": "Enrutamiento 3D 45 min • Arneses eléctricos, radio de curvatura y factor de llenado RETIE",
        "slides": [
            {
                "numero": 1,
                "seccion": "ELECTRICAL ROUTING 3D",
                "titulo": "Digitalización del Cableado Industrial",
                "puntos": [
                    "Sustituye el trazado empírico manual en obra por modelos 3D precisos con longitudes de corte de cable exactas al milímetro.",
                    "Permite segregar físicamente las bandejas de potencia de alta tensión respecto a los cables de instrumentación sensible y fibra óptica.",
                    "Evita el acoplamiento capacitivo e inductivo (interferencia electromagnética - EMI) en señales de control SCADA."
                ]
            },
            {
                "numero": 2,
                "seccion": "SEGURIDAD Y NORMA RETIE",
                "titulo": "Límites Térmicos y Radios de Doblez",
                "puntos": [
                    "Doblar un cable por debajo de su radio de curvatura garantizado fractura las pantallas semiconductoras y la armadura metálica.",
                    "Bandejas sobrellenadas (> 40-50%) acumulan calor por efecto Joule provocando envejecimiento prematuro del polietileno reticulado (XLPE).",
                    "Aporte vital para la generación automática de planos de ensamble de arneses (nailboard / formboard drawings)."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelado de Recipientes a Presión según ASME Sección VIII Div. 1: Envolventes y Cabezales",
        "objetivo": "Diseñar y modelar recipientes a presión cilíndricos horizontales y verticales para acumuladores de vapor y separadores geotérmicos bajo el código ASME Sección VIII División 1.",
        "concepto_clave_latex": r"t_{cil} = \frac{P R}{S E - 0.6 P} + c \quad ; \quad t_{torisf} = \frac{0.885 P L_r}{S E - 0.1 P} + c \quad ; \quad t_{hemisf} = \frac{P R}{2 S E - 0.2 P} + c",
        "ejemplo": "Problema 1: Se diseña un separador ciclónico de vapor y salmuera geotérmica (cuerpo cilíndrico vertical) con presión de diseño interna P = 1.60 MPa (232 psi) a 205 °C. Radio interior de la envolvente cilíndrica R = 900 mm. Material: placa de acero al carbono de calidad para calderas SA-516 Grado 70 (tensión máxima admisible a 205 °C de S = 125 MPa, inspección radiográfica completa de soldadura E = 1.0, sobreespesor de corrosión exigido por presencia de fluidos corrosivos c = 4.0 mm). Cálculo del espesor de la envolvente cilíndrica según fórmula UG-27(c)(1): t_cil = (P * R) / (S * E - 0.6 * P) + c = (1.60 * 900) / (125 * 1.0 - 0.6 * 1.60) + 4.0 = 1440 / (125 - 0.96) + 4.0 = 1440 / 124.04 + 4.0 = 11.61 + 4.0 = 15.61 mm. Para los cabezales de cierre superior e inferior torisféricos estándar ASME (con radio de abombado de corona L_r = D = 1800 mm y radio de nudillo r_knuckle = 0.06 * D = 108 mm) según fórmula UG-32(e): t_torisf = (0.885 * P * L_r) / (S * E - 0.1 * P) + c = (0.885 * 1.60 * 1800) / (125 * 1.0 - 0.1 * 1.60) + 4.0 = 2548.8 / (125 - 0.16) + 4.0 = 2548.8 / 124.84 + 4.0 = 20.42 + 4.0 = 24.42 mm. Para un cabezal semielíptico 2:1: t_elip = (P * D) / (2 * S * E - 0.2 * P) + c = (1.60 * 1800) / (250 - 0.32) + 4.0 = 2880 / 249.68 + 4.0 = 11.53 + 4.0 = 15.53 mm. El cabezal semielíptico 2:1 ahorra 8.89 mm de espesor de placa frente al torisférico (reducción del 36.4% de masa y costo de acero forjado), seleccionándose para la fabricación del recipiente. Problema 2: En la abertura de conexiones de toberas de entrada de fluido (nozzles), el cálculo del área de compensación de refuerzo (Area Replacement Method según UG-37) determina el espesor del anillo de refuerzo (pad) soldado alrededor del cuello de la boquilla.",
        "bloque_sugerido": "Recipientes ASME VIII 45 min • Ecuaciones UG-27/UG-32 de envolventes y cabezales 2:1",
        "slides": [
            {
                "numero": 1,
                "seccion": "CÓDIGO ASME DE CALDERAS Y RECIPIENTES",
                "titulo": "Filosofía ASME BPVC Sección VIII Div 1",
                "puntos": [
                    "Estándar internacional obligatorio de seguridad para recipientes que operan a presión manométrica superior a 15 psi (1 bar).",
                    "Enfoque de diseño por fórmulas (Design by Rule): Aplica factores de seguridad conservadores (FS = 3.5 sobre resistencia a la tracción).",
                    "Exige certificación de materiales con Reporte de Ensayo de Laminación (MTR) y trazabilidad metalúrgica de soldaduras."
                ]
            },
            {
                "numero": 2,
                "seccion": "GEOMETRÍA DE CABEZALES DE CIERRE",
                "titulo": "Hemisféricos, Elípticos y Torisféricos",
                "puntos": [
                    "Cabezal Hemisférico: La forma más eficiente del universo; requiere exactamente la mitad del espesor del cilindro pero es costoso de embutir.",
                    "Cabezal Semielíptico 2:1: Excelente compromiso técnico-económico; espesor casi idéntico al del cuerpo cilíndrico.",
                    "Cabezal Torisférico (FDT): Más plano y fácil de conformar pero acumula esfuerzos cortantes elevados en el radio de nudillo."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelado BIM (Building Information Modeling) para Plantas Energéticas (LOD 300/400)",
        "objetivo": "Integrar modelos paramétricos 3D mecánicos, eléctricos y civiles en un entorno BIM multidisciplinar (LOD 300/400) utilizando formatos abiertos IFC y detección de colisiones Navisworks.",
        "concepto_clave_latex": r"\text{LOD 100: Conceptual} \to \text{LOD 300: Específico} \to \text{LOD 400: Fabricación} \to \text{LOD 500: As-Built}",
        "ejemplo": "Problema 1: En el proyecto de construcción de una subestación eléctrica elevadora 34.5/220 kV y sala de control para un parque fotovoltaico de 100 MW, se coordina el modelo federado BIM combinando los modelos de arquitectura (revit civil), ingeniería estructural (cimentaciones y pórticos metálicos) y el modelo mecánico MEP (bandejas, ductos de climatización HVAC y tuberías contraincendios). Durante la auditoría de interferencias en Navisworks (Clash Detection), se ejecutan matrices de comprobación espacial con una tolerancia de holgura cero: 1) Se detectan 14 colisiones duras (hard clashes) donde canalizaciones subterráneas de cables de potencia de 34.5 kV intersectan directamente vigas de cimentación de concreto armado de los transformadores de potencia. 2) Se detectan 6 colisiones suaves (soft clashes) donde un conducto de climatización pasa a solo 150 mm del aislador de paso de un transformador, violando la distancia dieléctrica de seguridad al aire de 600 mm exigida por norma técnica. Resolver estas interferencias en la etapa de diseño virtual 3D BIM evita demoliciones en campo, órdenes de cambio imprevistas y retrasos en el cronograma valorados en más de 85,000 USD. Se exporta el modelo coordinado en estándar abierto IFC 4.3 (Industry Foundation Classes) con nivel de desarrollo LOD 400 conteniendo parámetros de número de serie, fabricante, peso neto y fecha programada de montaje 4D. Problema 2: En la dimensión 4D y 5D del BIM, la vinculación del modelo 3D con la carta Gantt de Primavera P6 y el presupuesto desglosado en Navisworks simula virtualmente el avance financiero de la obra semana a semana.",
        "bloque_sugerido": "BIM para Energía 45 min • Niveles de desarrollo LOD 100-500, IFC y Clash Detection",
        "slides": [
            {
                "numero": 1,
                "seccion": "METODOLOGÍA BIM MULTIDISCIPLINAR",
                "titulo": "Del CAD 2D al Modelo Inteligente Paramétrico",
                "puntos": [
                    "BIM no es un software; es una metodología de trabajo colaborativa basada en bases de datos tridimensionales unificadas.",
                    "LOD (Level of Development): LOD 300 define forma y dimensiones precisas; LOD 400 añade ensamblaje y detalles de fabricación en taller.",
                    "Cada elemento BIM porta metadatos paramétricos: costo unitario, potencia eléctrica, vida útil y manuales de mantenimiento."
                ]
            },
            {
                "numero": 2,
                "seccion": "COORDINACIÓN Y GESTIÓN DE INTERFERENCIAS",
                "titulo": "Modelos Federados y Formato IFC",
                "puntos": [
                    "Modelo Federado: Superposición coordinada de los archivos independientes de las disciplinas civil, eléctrica y mecánica.",
                    "Detección de interferencias automatizada: Resuelve incompatibilidades en oficina antes de verter el primer metro cúbico de concreto.",
                    "IFC (ISO 16739): Garantiza interoperabilidad neutral sin atarse a licencias propietarias entre Revit, Tekla, SolidWorks y Archicad."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Optimización Topológica y Diseño Generativo de Componentes Mecánicos",
        "objetivo": "Aplicar algoritmos de optimización topológica SIMP (Solid Isotropic Material with Penalization) para aligerar componentes estructurales manteniendo la rigidez mecánica.",
        "concepto_clave_latex": r"\min_{\boldsymbol{\rho}} \mathbf{U}^T \mathbf{K}(\boldsymbol{\rho}) \mathbf{U} \quad \text{s.t.} \quad \frac{V(\boldsymbol{\rho})}{V_0} \le f_v \quad ; \quad E_e(\rho_e) = E_{min} + \rho_e^p (E_0 - E_{min})",
        "ejemplo": "Problema 1: El soporte de basculación (pitch bracket) de una pala de aerogenerador marino se fabrica originalmente en un bloque macizo de aleación de aluminio 7075-T6 de masa inicial M_0 = 42.0 kg. Se somete a optimización topológica basada en densidad SIMP con penalización de rigidez p = 3 y una restricción de fracción volumétrica meta f_v = 0.40 (reducción del 60% del volumen inicial). Condiciones de contorno: Dos casos de carga combinados (momento de paso de pala M_pitch = 6500 N*m y empuje centrífugo F_c = 18,000 N). El optimizador calcula iterativamente la densidad pseudomaterial de cada elemento finito rho_e in [0, 1]. Tras 48 iteraciones de convergencia de energía de deformación, el algoritmo redistribuye el material eliminando núcleos pasivos y generando nervaduras biomiméticas de celosía que siguen exactamente las trayectorias de las líneas de esfuerzo isostáticas de tracción y compresión. La masa final del soporte optimizado se reduce a M_final = 16.8 kg (ahorro de 25.2 kg por pala, totalizando 75.6 kg menos de masa en cabeza de rotor). La tensión máxima de von Mises en el componente optimizado es de 168 MPa, manteniendo un factor de seguridad de FS = 2.98 respecto al límite de fluencia del material (503 MPa) con una pérdida de rigidez torsional inferior al 6%. El sólido optimizado se reconvierte en una superficie NURBS cerrada mediante herramientas de diseño generativo listas para manufactura aditiva metálica o fundición de precisión. Problema 2: En componentes aeroelásticos, la optimización topológica multiobjetivo maximiza simultáneamente la rigidez estática y la primera frecuencia natural de vibración para alejar el componente de la resonancia.",
        "bloque_sugerido": "Optimización Topológica 45 min • Algoritmo SIMP, fracción de volumen y diseño generativo",
        "slides": [
            {
                "numero": 1,
                "seccion": "DISEÑO ORIENTADO AL MATERIAL EFICIENTE",
                "titulo": "La Matemática de la Optimización Topológica",
                "puntos": [
                    "A diferencia de la optimización dimensional, la optimización topológica crea cavidades y altera el número de agujeros de la geometría.",
                    "Minimiza la compliancia (Compliance): Maximiza la rigidez estructural global bajo un volumen de material preestablecido.",
                    "Algoritmo SIMP: Penaliza densidades intermedias (p = 3) forzando a que cada elemento sea sólido puro (rho = 1) o vacío puro (rho = 0)."
                ]
            },
            {
                "numero": 2,
                "seccion": "SINERGIA CON MANUFACTURA ADITIVA",
                "titulo": "Geometrías Orgánicas y Biomiméticas",
                "puntos": [
                    "Las geometrías resultantes imitan las estructuras óseas trabeculares de la naturaleza.",
                    "Históricamente imposibles de fabricar mediante fresado tradicional; hoy 100% viables mediante impresión 3D metálica (DMLS / SLM).",
                    "Aporte crucial para reducir la masa de torres eólicas flotantes marinas donde cada kilogramo ahorrado reduce el costo del flotador."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Simulación de Fatiga y Ciclos de Carga en Componentes Mecánicos (Regla de Miner)",
        "objetivo": "Evaluar la vida a fatiga por alto y bajo ciclo en ejes rotativos y soldaduras sometidos a esfuerzos fluctuantes combinando diagramas de Wöhler (S-N), Goodman y daño acumulado de Palmgren-Miner.",
        "concepto_clave_latex": r"\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = 1 \quad [\text{Criterio de Goodman Modificado}] \quad ; \quad D = \sum_{i=1}^k \frac{n_i}{N_i} \le 1.0",
        "ejemplo": "Problema 1: El eje principal forjado (acero aleado AISI 4340 templado y revenido, resistencia última a la tracción S_ut = 1050 MPa, límite elástico S_y = 880 MPa) de una pequeña central hidroeléctrica gira a 720 rpm sometido a un momento flector cíclico completamente reversible originado por el peso del rodete en voladizo (sigma_alt = 180 MPa) y un momento torsional medio cuasi-estático que induce una tensión media normal de sigma_m = 120 MPa. Límite de fatiga teórico de probeta pulida: S'_e = 0.5 * S_ut = 525 MPa. Factores de corrección de Marin para el componente real: factor de acabado superficial mecanizado k_a = 0.76; factor de tamaño para diámetro de 120 mm k_b = 0.75; factor de confiabilidad del 99% k_c = 0.814; factor de concentración de tensiones por entalla k_e = 0.85. Límite de fatiga corregido del eje: S_e = k_a * k_b * k_c * k_e * S'_e = 0.76 * 0.75 * 0.814 * 0.85 * 525 = 0.3944 * 525 = 207.06 MPa. Aplicando el criterio de Goodman modificado para la amplitud de esfuerzo equivalente: S_a = sigma_alt / (1 - sigma_m / S_ut) = 180 / (1 - 120 / 1050) = 180 / (1 - 0.1143) = 180 / 0.8857 = 203.23 MPa. Factor de seguridad a vida infinita: FS_fatiga = S_e / S_a = 207.06 / 203.23 = 1.019 (supera marginalmente el umbral de vida infinita de 10^6 ciclos). Si durante 100 horas al año la máquina opera en régimen de cavitación severa que eleva la amplitud a sigma_alt = 240 MPa (donde la curva S-N predice una vida finita de N = 4.2 * 10^6 ciclos): A 720 rpm, en 100 h se acumulan n = 720 * 60 * 100 = 4.32 * 10^6 ciclos. Daño anual acumulado según Palmgren-Miner: D_anual = n / N = 4.32 * 10^6 / 4.2 * 10^6 = 1.028 > 1.0, lo que predice que el eje fallará por fractura frágil por fatiga en menos de 1 año si no se corrigen las vibraciones hidrodinámicas. Problema 2: El algoritmo Rainflow Counting descompone historiales estocásticos de viento en espectros equivalentes de amplitud constante para evaluar el daño por fatiga acumulada en álabes eólicos a 20 años.",
        "bloque_sugerido": "Análisis de Fatiga 45 min • Factores de Marin, criterio de Goodman y regla de Palmgren-Miner",
        "slides": [
            {
                "numero": 1,
                "seccion": "MECÁNICA DE LA FRACTURA POR FATIGA",
                "titulo": "La Falla Silenciosa de los Metales",
                "puntos": [
                    "Más del 85% de las fallas mecánicas en maquinaria rotativa ocurren por fatiga bajo esfuerzos inferiores al límite elástico.",
                    "Fases de la fatiga: 1) Iniciación de microfisuras en concentradores de esfuerzo; 2) Propagación lenta con marcas de playa; 3) Rotura frágil súbita.",
                    "Límite de Fatiga (Endurance Limit S_e): Esfuerzo por debajo del cual el material resiste teóricamente un número infinito de ciclos (> 10^6)."
                ]
            },
            {
                "numero": 2,
                "seccion": "DAÑO ACUMULADO VARIABLE",
                "titulo": "Algoritmo Rainflow y Regla de Miner",
                "puntos": [
                    "En servicio real, los esfuerzos no son senoidales perfectos; varían estocásticamente con el viento y las olas.",
                    "Conteo Rainflow (ASTM E1049): Método estandarizado para extraer ciclos de histéresis cerrados a partir de historiales temporales desordenados.",
                    "Regla de Miner: El daño total acumulado es la suma lineal del daño parcial de cada bloque; el colapso ocurre cuando D = 1.0."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Gemelos Digitales (Digital Twins) 3D: Conexión de Modelos CAD con Sensores IoT y SCADA",
        "objetivo": "Diseñar arquitecturas de Gemelos Digitales (Digital Twins) vinculando modelos CAD/BIM 3D con flujos telemétricos en tiempo real de protocolos industriales OPC UA y MQTT.",
        "concepto_clave_latex": r"\text{Digital Twin} = \{ \text{Modelo 3D CAD/BIM} \} \otimes \{ \text{Física CAE} \} \otimes \{ \text{Sensores IoT/SCADA} \}",
        "ejemplo": "Problema 1: Se desarrolla un Gemelo Digital 3D para un transformador de potencia elevador de 50 MVA en una subestación solar. El modelo CAD 3D de alta definición se aloja en una plataforma en la nube (AWS IoT TwinMaker / Azure Digital Twins) conectada mediante protocolo seguro OPC UA al sistema SCADA de la planta. Se ingieren cada 2 segundos flujos de datos en tiempo real provenientes de 16 sensores físicos: 6 sondas de fibra óptica insertas en los devanados de alta tensión (temperatura del punto más caliente hot-spot T_hs), 4 sensores de vibración piezoeléctricos triaxiales en la cuba, un monitor continuo de gases disueltos en aceite DGA (concentraciones de H2, C2H2, CH4, CO) y sensor de nivel de aceite. El gemelo digital corre en segundo plano un modelo térmico numérico en tiempo real basado en la norma IEEE C57.91. Cuando la temperatura del punto más caliente sube de 95 °C a 118 °C bajo una sobrecarga de mediodía, el gemelo digital proyecta un mapa térmico tridimensional dinámico de colores sobre el modelo CAD del transformador, calcula la tasa instantánea de pérdida de vida útil del papel aislante celulósico (Aging Acceleration Factor F_AA = exp[15000/383 - 15000/(T_hs + 273)] = exp[39.16 - 38.36] = exp[0.80] = 2.225) y dispara automáticamente en el SCADA la activación de la segunda etapa de motoventiladores de refrigeración forzada ONAF, retornando T_hs a 98 °C y previniendo la degradación irreversible del activo. Problema 2: La integración de modelos de realidad aumentada (AR) en tablets permite a los técnicos de mantenimiento enfocar un aerogenerador e inspeccionar en 3D la temperatura interna de los rodamientos superpuesta directamente sobre la carcasa física.",
        "bloque_sugerido": "Digital Twins 45 min • Arquitectura IoT TwinMaker, integración OPC UA y cálculo de vida en tiempo real",
        "slides": [
            {
                "numero": 1,
                "seccion": "INDUSTRIA 4.0 EN EL SECTOR ENERGÉTICO",
                "titulo": "La Convergencia de lo Físico y lo Virtual",
                "puntos": [
                    "Un Gemelo Digital es una réplica virtual viva de un activo físico sincronizada bidireccionalmente en tiempo real.",
                    "Supera los dashboards SCADA 2D tradicionales ofreciendo navegación espacial tridimensional inmersiva.",
                    "Permite el Mantenimiento Predictivo Prescriptivo: pronostica averías semanas antes de que ocurra la falla física."
                ]
            },
            {
                "numero": 2,
                "seccion": "ARQUITECTURA DE DATOS",
                "titulo": "Protocolos Industriales e Inteligencia Artificial",
                "puntos": [
                    "OPC UA (Open Platform Communications Unified Architecture): Estándar seguro multiplataforma para interconexión máquina a máquina (M2M).",
                    "MQTT (Message Queuing Telemetry Transport): Protocolo ligero de publicación/suscripción ideal para sensores remotos de bajo ancho de banda.",
                    "Algoritmos de Machine Learning ejecutan simulaciones 'What-If' para evaluar escenarios de sobrecarga sin arriesgar la planta real."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Manufactura Aditiva (Impresión 3D): Modelado para FDM, SLA, SLS y DMLS en Energía",
        "objetivo": "Diseñar componentes mecánicos adaptados a procesos de manufactura aditiva polimérica y metálica (FDM, SLA, SLS, DMLS) respetando reglas de orientación de capa, soportes y contracción.",
        "concepto_clave_latex": r"\text{Regla de Autoportabilidad}: \theta_{overhang} \ge 45^\circ \quad ; \quad t_{min} \ge 1.2 \text{ mm} \quad ; \quad \text{Anisotropía}: \sigma_{z} \approx 0.55 - 0.75 \sigma_{xy}",
        "ejemplo": "Problema 1: Se diseña para manufactura aditiva por sinterizado directo de metal por láser (DMLS en aleación de titanio Ti-6Al-4V) un intercambiador de calor microcanal de contraflujo de ultra-alta eficiencia para un ciclo Brayton supercrítico de CO2 (sCO2). Reglas de diseño DfAM (Design for Additive Manufacturing): 1) Los microcanales interiores tienen sección transversal romboidal o en gota invertida con ángulo de inclinación respecto al plano horizontal de construcción de theta = 52° (mayor que el ángulo crítico de autoportabilidad de 45°), eliminando completamente la necesidad de estructuras de soporte internas que serían imposibles de remover mecánicamente tras la impresión. 2) El espesor de pared entre canales de alta y baja presión se fija en t = 0.80 mm (superior al diámetro del haz de láser focalizado de 100 micras y al espesor de capa de polvo de 40 micras). 3) Se incorporan orificios de escape de polvo no sinterizado de 3.5 mm en los colectores terminales. El intercambiador impreso en una sola pieza monolítica sin soldaduras alcanza un área superficial volumétrica de 2400 m^2/m^3 con una masa de 3.4 kg, soportando presiones de prueba hidrostática de 250 bar a 550 °C sin fugas. Si se hubiera fabricado por mecanizado convencional y soldadura fuerte (brazing), habría requerido 120 piezas individuales ensambladas con un riesgo masivo de fugas por microfisuras térmicas. Problema 2: En componentes poliméricos impresos por modelado por deposición fundida (FDM en polímero técnico ULTEM 9085 ignífugo), la orientación de impresión en el eje Z debe orientarse en la dirección de compresión para evitar que la tracción delplace las capas impresas por delaminación interlaminar.",
        "bloque_sugerido": "Impresión 3D DfAM 45 min • Reglas de diseño para manufactura aditiva y metal DMLS/SLM",
        "slides": [
            {
                "numero": 1,
                "seccion": "REVOLUCIÓN EN MANUFACTURA ADITIVA",
                "titulo": "Diseño para Manufactura Aditiva (DfAM)",
                "puntos": [
                    "La complejidad geométrica es 'gratis': canales conformados, celosías internas y vaciados orgánicos no incrementan el costo de fabricación.",
                    "FDM (Filamento fundido): Prototipado rápido; SLA (Estereolitografía de resina): Alta precisión visual; SLS (Láser en polvos): Sin soportes.",
                    "DMLS / SLM (Fusión láser en lecho de polvo metálico): Fabricación de piezas funcionales de titanio, Inconel y aceros inoxidables."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGLAS GEOMÉTRICAS DFAM",
                "titulo": "Soportes, Orientación y Anisotropía",
                "puntos": [
                    "Ángulo de voladizo (Overhang): Caras con ángulos inferiores a 45° exigen material de soporte sacrificial para no colapsar durante la deposición.",
                    "Anisotropía estructural: La adherencia interlaminar en el eje vertical Z es entre un 25% y 45% más débil que la resistencia en el plano horizontal XY.",
                    "Tratamientos térmicos posteriores (Hot Isostatic Pressing - HIP): Eliminan la porosidad residual y alivian tensiones térmicas residuales."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Representación Gráfica Avanzada y Renderizado Fotorrealista para Proyectos de Ingeniería",
        "objetivo": "Generar imágenes y animaciones fotorrealistas de alta fidelidad mediante motores de renderizado con trazado de rayos (Raytracing) e iluminación global basada en física (PBR) para defensa ante inversores.",
        "concepto_clave_latex": r"L_o(\mathbf{x}, \omega_o) = L_e(\mathbf{x}, \omega_o) + \int_\Omega f_r(\mathbf{x}, \omega_i, \omega_o) L_i(\mathbf{x}, \omega_i) (\omega_i \cdot \mathbf{n}) d\omega_i \quad [\text{Ecuación de Renderizado}]",
        "ejemplo": "Problema 1: Se prepara el paquete de presentación ejecutiva para inversionistas de un parque eólico marino flotante de 500 MW en el mar Caribe colombiano. Para superar el rechazo visual y evaluar el impacto paisajístico en licencias ambientales ante la ANLA, se genera una simulación fotorrealista con renderizado basado en física PBR (KeyShot / Unreal Engine 5 / Blender Cycles). Se configuran mapas de materiales ópticos rigurosos: pintura de poliuretano marina semi-brillante en la torre (rugosidad roughness = 0.22, índice de refracción IOR = 1.54, componente especular specular = 0.04), agua de mar con shaders dieléctricos transparentes acoplados a un mapa de oleaje dinámico de ondas de Airy dependiente del espectro JONSWAP, y cielo físico mediante imágenes de alto rango dinámico (HDRI de 16K calibradas a 100,000 lux solares directos con balance de blancos a 5600 K). El motor de trazado de rayos por trayectoria de luz (Path Tracing) calcula con precisión las sombras arrojadas por las palas en rotación y la reflexión especular del sol sobre la superficie marina sin artefactos visuales de pixelado ni alias. El render final a resolución 4K (3840 x 2160 píxeles a 60 fps) demuestra con exactitud fotográfica que a una distancia de 14 km de la línea de costa los aerogeneradores son prácticamente imperceptibles bajo condiciones de bruma marina habituales, facilitando la obtención de la viabilidad social y ambiental del megaproyecto. Problema 2: En la animación técnica de ensamblaje (exploded view animation), la sincronización de trayectorias de cámara y despiece de componentes en SolidWorks Composer genera manuales de montaje interactivos sin texto para operarios de campo.",
        "bloque_sugerido": "Visualización 3D 45 min • Renderizado PBR con trazado de rayos y animación de despiece",
        "slides": [
            {
                "numero": 1,
                "seccion": "COMUNICACIÓN VISUAL DE ALTO NIVEL",
                "titulo": "Materiales Basados en Física (PBR)",
                "puntos": [
                    "PBR (Physically Based Rendering): Modela la interacción real de los fotones con la microestructura superficial de los materiales.",
                    "Mapas de textura estándar: Albedo/Base Color (color puro sin sombras), Roughness (rugosidad microscópica), Normal Map (detalles sin elevar polígonos).",
                    "Transforma un frío modelo CAD en una experiencia visual convincente para bancos, juntas directivas y comunidades locales."
                ]
            },
            {
                "numero": 2,
                "seccion": "ILUMINACIÓN GLOBAL Y RAYTRACING",
                "titulo": "Trazado de Rayos en Tiempo Real (RTX)",
                "puntos": [
                    "Calcula rebotes indirectos de luz (color bleeding), refracciones cáusticas en agua y oclusión ambiental de contacto.",
                    "Aceleración por hardware mediante núcleos RT en tarjetas gráficas modernas: renders fotográficos en segundos en lugar de horas.",
                    "Herramienta decisiva para la aprobación de estudios de impacto ambiental y licitaciones internacionales de energía renovable."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Gestión del Ciclo de Vida del Producto (PLM) y Control de Versiones CAD en Ingeniería",
        "objetivo": "Implementar flujos de trabajo de gestión del ciclo de vida del producto (Product Lifecycle Management - PLM / PDM) mediante control de versiones, firmas electrónicas y órdenes de cambio de ingeniería (ECO).",
        "concepto_clave_latex": r"\text{ECO} \to \text{Check-out} \to \text{Revisión (Rev A} \to \text{Rev B)} \to \text{Firma Electrónica} \to \text{Check-in Release}",
        "ejemplo": "Problema 1: En una oficina técnica de diseño de plantas de energía, un equipo multidisciplinar de 12 ingenieros colabora simultáneamente en el diseño del sistema auxiliar de bombeo e intercambio de calor de una central geotérmica. Para evitar la sobrescritura destructiva accidental de archivos de piezas maestras y garantizar trazabilidad ISO 9001, se implementa un sistema PDM/PLM (SolidWorks PDM Professional / Siemens Teamcenter). El flujo de trabajo define un ciclo de vida con 4 estados de seguridad: [1. En Edición / Work in Progress] -> [2. En Revisión Técnica / Pending Approval] -> [3. Liberado para Producción / Released] -> [4. Obsoleto / Obsolete]. Un ingeniero mecánico solicita modificar el diámetro de una brida de acero en el modelo maestro mediante una Orden de Cambio de Ingeniería (Engineering Change Order - ECO #2026-084). El sistema aplica un bloqueo de edición (Check-out) asignando el archivo exclusivamente al ingeniero solicitante, mientras los demás miembros del equipo visualizan una copia de solo lectura con marca de agua 'En Modificación'. Al finalizar los cálculos FEA y actualizar los planos 2D asociados, el ingeniero ejecuta el Check-in; el sistema incrementa automáticamente la versión de revisión de 'Rev B.2' a 'Rev C.0', archiva la versión anterior en el almacén de seguridad (vault) impidiendo su pérdida, y notifica por correo electrónico al Ingeniero Jefe para su aprobación con firma electrónica criptográfica digital. El sistema genera de forma automatizada la Lista de Materiales (BOM) multi-nivel exportable al ERP SAP de la empresa, evitando discrepancias de inventario y errores de compra en fábrica. Problema 2: El análisis de impacto de cambio (Where-Used Analysis) en el PDM rastrea en 2 segundos todos los ensamblajes, planos y proyectos de la compañía donde se utiliza un perno específico M24 antes de autorizar su descatalogación técnica.",
        "bloque_sugerido": "Gestión PLM 45 min • Flujo de trabajo PDM, órdenes de cambio ECO y control de versiones",
        "slides": [
            {
                "numero": 1,
                "seccion": "CONTROL DOCUMENTAL EN GRANDES PROYECTOS",
                "titulo": "Sistemas PDM/PLM Empresariales",
                "puntos": [
                    "PDM (Product Data Management): Gestiona archivos CAD, relaciones de ensamble, planos 2D y versiones sin duplicación en carpetas de red.",
                    "PLM (Product Lifecycle Management): Extiende el control a toda la vida del producto: desde el concepto inicial hasta el desmantelamiento y reciclaje.",
                    "Elimina la pesadilla de archivos desincronizados con nombres caóticos como 'plano_final_v2_este_si.dwg'."
                ]
            },
            {
                "numero": 2,
                "seccion": "GOBERNANZA DE INGENIERÍA",
                "titulo": "Trazabilidad Total y Auditoría ISO 9001",
                "puntos": [
                    "Órdenes de Cambio de Ingeniería (ECO / ECN): Ninguna cota puede alterarse en producción sin justificación técnica y firma autorizada.",
                    "Integración directa con el sistema ERP corporativo (SAP, Oracle) para compras automáticas de perfiles, pernos y motores.",
                    "Culminación de las competencias de diseño y modelado tridimensional del Ingeniero Energético de la Universidad del Magdalena."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_04021823)
    marker = '      - codigo: "04031827"'
    inject_topics_after(marker, yaml_text)
    print("04021823 Ingeniería del Diseño y Modelado en 3D successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
