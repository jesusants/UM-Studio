# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_03021817 = [
    {
        "numero_tema": 10,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Relaciones Termodinámicas Fundamentales y Ecuaciones de Maxwell",
        "objetivo": "Deducir las cuatro relaciones de Maxwell a partir de los potenciales termodinámicos ($U, H, A, G$) para evaluar propiedades térmicas no medibles directamente ($s$) mediante magnitudes medibles ($P, v, T$).",
        "concepto_clave_latex": r"\left(\frac{\partial T}{\partial v}\right)_s = -\left(\frac{\partial P}{\partial s}\right)_v \quad ; \quad \left(\frac{\partial T}{\partial P}\right)_s = \left(\frac{\partial v}{\partial s}\right)_P \quad ; \quad \left(\frac{\partial P}{\partial T}\right)_v = \left(\frac{\partial s}{\partial v}\right)_T \quad ; \quad \left(\frac{\partial v}{\partial T}\right)_P = -\left(\frac{\partial s}{\partial P}\right)_T",
        "ejemplo": "Problema 1: Deducir la variación de entropía con el volumen a temperatura constante para un gas que obedece la ecuación de Van der Waals: $\\left(P + \\frac{a}{v^2}\\right)(v - b) = RT$. Despejando la presión: $P = \\frac{RT}{v - b} - \\frac{a}{v^2}$. Aplicando la tercera relación de Maxwell: $\\left(\\frac{\\partial s}{\\partial v}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_v$. Derivando $P$ respecto a $T$ a volumen constante: $\\left(\\frac{\\partial P}{\\partial T}\\right)_v = \\frac{R}{v - b}$. Integrando entre $v_1$ y $v_2$ isotérmicamente: $\\Delta s_T = R \\ln\\left(\\frac{v_2 - b}{v_1 - b}\\right)$. Problema 2: En la compresión isotérmica de agua líquida a $20^\\circ\\text{C}$ de 1 a 100 bar, la cuarta relación de Maxwell calcula el cambio de entropía utilizando el coeficiente de dilatación volumétrica: $\\Delta s = -\\beta v \\Delta P$.",
        "bloque_sugerido": "Termodinámica Matemática 45 min • Deducción de diferenciales exactas y relaciones de Helmholtz/Gibbs",
        "slides": [
            {
                "numero": 1,
                "seccion": "POTENCIALES TERMODINÁMICOS",
                "titulo": "Las Cuatro Ecuaciones de Gibbs",
                "puntos": [
                    "Energía Interna: $dU = T ds - P dv$.",
                    "Entalpía: $dH = T ds + v dP$.",
                    "Energía Libre de Helmholtz: $dA = -s dT - P dv$.",
                    "Energía Libre de Gibbs: $dG = -s dT + v dP$."
                ]
            },
            {
                "numero": 2,
                "seccion": "TEOREMA DE SCHWARZ",
                "titulo": "Simetría de Segundas Derivadas Cruzadas",
                "puntos": [
                    "Dado que los potenciales son funciones de estado con diferenciales exactas: $\\frac{\\partial^2 f}{\\partial x \\partial y} = \\frac{\\partial^2 f}{\\partial y \\partial x}$.",
                    "Transforman derivadas de entropía inalcanzables experimentalmente en coeficientes compresibles $(\\kappa_T)$ y térmicos $(\\beta)$ medibles en laboratorio.",
                    "Pilar para construir tablas termodinámicas y ecuaciones multiparamétricas de estado (IAPWS-95)."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ecuación de Clapeyron y Clapeyron-Clausius para Cambio de Fase",
        "objetivo": "Determinar la pendiente de las curvas de coexistencia de fases y estimar la entalpía de vaporización $\\Delta h_{vap}$ a partir de la relación entre presión y temperatura de saturación.",
        "concepto_clave_latex": r"\left(\frac{dP}{dT}\right)_{sat} = \frac{h_{fg}}{T(v_g - v_f)} \quad ; \quad \ln\left(\frac{P_2}{P_1}\right) \approx -\frac{h_{fg}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)",
        "ejemplo": "Problema 1: Estimar la entalpía de vaporización del refrigerante R134a a $0^\\circ\\text{C}$ (273.15 K) sabiendo que $P_{sat}(-2^\\circ\\text{C}) = 271.86\\text{ kPa}$ y $P_{sat}(+2^\\circ\\text{C}) = 314.65\\text{ kPa}$, con volúmenes específicos $v_f = 0.000771\\text{ m}^3/\\text{kg}$ y $v_g = 0.0693\\text{ m}^3/\\text{kg}$. Pendiente numérica: $\\frac{dP}{dT} \\approx \\frac{314.65 - 271.86}{4} = \\frac{42.79\\text{ kPa}}{4\\text{ K}} = 10.6975\\text{ kPa/K} = 10697.5\\text{ Pa/K}$. Diferencia de volúmenes: $v_{fg} = 0.0693 - 0.000771 \\approx 0.06853\\text{ m}^3/\\text{kg}$. Entalpía de Clapeyron: $h_{fg} = T v_{fg} \\left(\\frac{dP}{dT}\\right) = 273.15 \\times 0.06853 \\times 10697.5 = 200236\\text{ J/kg} = 200.24\\text{ kJ/kg}$ (desvía menos del $1\\%$ del valor de tabla de 197.8 kJ/kg). Problema 2: En la cumbre de la Sierra Nevada (4500 m, $P \\approx 58\\text{ kPa}$), la ecuación de Clausius-Clausius calcula que el agua hierve a apenas $85.3^\\circ\\text{C}$.",
        "bloque_sugerido": "Termodinámica de Fases 40 min • Ajuste de ecuaciones de Antoine y curvas de equilibrio líquido-vapor",
        "slides": [
            {
                "numero": 1,
                "seccion": "EQUILIBRIO DE FASES",
                "titulo": "Igualdad del Potencial Químico",
                "puntos": [
                    "Durante el cambio de fase a $T$ y $P$ constantes, las energías de Gibbs específicas de ambas fases son idénticas: $g_f(T,P) = g_g(T,P)$.",
                    "A lo largo de la curva de saturación: $dg_f = dg_g \\implies -s_f dT + v_f dP = -s_g dT + v_g dP$.",
                    "Reordenando surge la ecuación exacta de Clapeyron: $\\frac{dP}{dT} = \\frac{s_g - s_f}{v_g - v_f} = \\frac{h_{fg}}{T v_{fg}}$."
                ]
            },
            {
                "numero": 2,
                "seccion": "APROXIMACIÓN DE CLAUSIUS",
                "titulo": "Vapor como Gas Ideal",
                "puntos": [
                    "Suponiendo que $v_g \\gg v_f$ ($v_{fg} \\approx v_g$) y modelando el vapor saturado como gas ideal ($v_g = RT/P$).",
                    "La ecuación se convierte en $\\frac{d(\\ln P)}{dT} = \\frac{h_{fg}}{R T^2}$, integrándose en la famosa ecuación de Clausius-Clapeyron.",
                    "Permite extrapolar presiones de vapor de biocombustibles y fluidos orgánicos de trabajo en ciclos ORC."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Coeficiente de Joule-Thomson y Procesos de Estrangulamiento Isoentálpicos",
        "objetivo": "Modelar la caída de temperatura y presión en válvulas de expansión y tapones porosos mediante el coeficiente de Joule-Thomson $\\mu_{JT}$, determinando la curva de inversión.",
        "concepto_clave_latex": r"\mu_{JT} = \left(\frac{\partial T}{\partial P}\right)_h = \frac{1}{c_p}\left[ T \left(\frac{\partial v}{\partial T}\right)_P - v \right] \quad ; \quad T_{inv}: \mu_{JT} = 0 \iff \left(\frac{\partial v}{\partial T}\right)_P = \frac{v}{T}",
        "ejemplo": "Problema 1: Demostrar que para un gas ideal el coeficiente de Joule-Thomson es idénticamente cero. Para un gas ideal, $v = RT/P$. Derivando a presión constante: $\\left(\\frac{\\partial v}{\\partial T}\\right)_P = \\frac{R}{P} = \\frac{v}{T}$. Sustituyendo en la fórmula: $\\mu_{JT} = \\frac{1}{c_p}\\left[ T \\left(\\frac{v}{T}\\right) - v \\right] = \\frac{1}{c_p}[v - v] = 0$. Por ende, la temperatura de un gas ideal no cambia en una válvula de estrangulamiento isoentálpica ($T_2 = T_1$). Problema 2: En el gas natural (metano) a $25^\\circ\\text{C}$ y 60 bar, $\\mu_{JT} \\approx +0.45^\\circ\\text{C/bar}$. Una caída de presión de 60 a 5 bar en una estación city-gate produce un enfriamiento de $\\Delta T \\approx 0.45 \\times (-55) = -24.75^\\circ\\text{C}$, requiriendo precalentadores de gas para evitar el congelamiento y formación de hidratos de metano en las tuberías.",
        "bloque_sugerido": "Sistemas de Gas 40 min • Válvulas Joule-Thomson y curva de inversión de refrigerantes",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRANGULAMIENTO ISOENTÁLPICO",
                "titulo": "El Efecto Joule-Thomson",
                "puntos": [
                    "En una válvula de estrangulamiento adiabática rígida sin trabajo de eje: $h_1 = h_2$.",
                    "Si $\\mu_{JT} > 0$: La caída de presión provoca enfriamiento del fluido (región de refrigeración).",
                    "Si $\\mu_{JT} < 0$: La caída de presión provoca calentamiento del fluido (ocurre en hidrógeno y helio a temperatura ambiente)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CURVA DE INVERSIÓN",
                "titulo": "Temperatura Máxima de Inversión",
                "puntos": [
                    "Separa la región de enfriamiento de la de calentamiento en el diagrama T-P.",
                    "Para licuar un gas por estrangulamiento (ciclo Linde), la temperatura inicial debe estar estrictamente por debajo de su temperatura de inversión.",
                    "Para el metano: $T_{inv,max} \\approx 960\\text{ K}$; para el hidrógeno: $T_{inv,max} \\approx 205\\text{ K}$ (requiere precriogenia con nitrógeno líquido a 77 K)."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Ecuaciones de Estado para Gases Reales (Van der Waals, Redlich-Kwong y Peng-Robinson)",
        "objetivo": "Predecir el comportamiento $P-v-T$ de gases a presiones elevadas y bajas temperaturas utilizando ecuaciones cúbicas de estado con corrección de covolumen y fuerzas de atracción molecular.",
        "concepto_clave_latex": r"P = \frac{RT}{v - b} - \frac{a(T)}{v^2 + u b v + w b^2} \quad ; \quad a = 0.45724 \frac{R^2 T_c^2}{P_c} \alpha(T_r, \omega) \quad ; \quad b = 0.07780 \frac{R T_c}{P_c}",
        "ejemplo": "Problema 1: Calcular la presión ejercida por 1 kmol de vapor de agua a $T = 400^\\circ\\text{C}$ (673.15 K) ocupando un volumen de $0.5\\text{ m}^3$ usando la ecuación de Van der Waals ($a = 553.6\\text{ kPa m}^6/\\text{kmol}^2$, $b = 0.0305\\text{ m}^3/\\text{kmol}$, $R = 8.314\\text{ kPa m}^3/(\\text{kmol K})$). Término repulsivo: $\\frac{RT}{v - b} = \\frac{8.314 \\times 673.15}{0.5 - 0.0305} = \\frac{5596.57}{0.4695} = 11920.3\\text{ kPa}$. Término atractivo: $\\frac{a}{v^2} = \\frac{553.6}{(0.5)^2} = 2214.4\\text{ kPa}$. Presión Van der Waals: $P = 11920.3 - 2214.4 = 9705.9\\text{ kPa} = 9.71\\text{ MPa}$. El modelo de gas ideal predeciría $P_{ideal} = \\frac{8.314 \\times 673.15}{0.5} = 11.19\\text{ MPa}$ (un error del $+15.3\\%$ por ignorar las fuerzas de atracción dipolares). Problema 2: En la industria del petróleo y gas, la ecuación de Peng-Robinson (PR-EOS) es el estándar indiscutible para calcular equilibrios vapor-líquido (VLE) de hidrocarburos.",
        "bloque_sugerido": "Simulación Termodinámica 45 min • Raíces cúbicas de volumen en Peng-Robinson con Python",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITES DEL GAS IDEAL",
                "titulo": "Fuerzas Intermoleculares y Volumen Propio",
                "puntos": [
                    "A altas presiones, el volumen propio ocupado por las moléculas ($b$) deja de ser despreciable frente al volumen del recipiente.",
                    "A bajas temperaturas, las fuerzas atractivas de van der Waals ($a$) reducen la fuerza neta de colisión contra las paredes.",
                    "El punto crítico impone las condiciones de punto de inflexión: $\\left(\\frac{\\partial P}{\\partial v}\\right)_{T_c} = 0$ y $\\left(\\frac{\\partial^2 P}{\\partial v^2}\\right)_{T_c} = 0$."
                ]
            },
            {
                "numero": 2,
                "seccion": "ECUACIONES CÚBICAS MODERNAS",
                "titulo": "Redlich-Kwong-Soave (SRK) y Peng-Robinson",
                "puntos": [
                    "Incorporan el factor acéntrico de Pitzer $\\omega = -\\log_{10}(P^{sat}_{r} \\text{ at } T_r = 0.7) - 1.0$ para modelar la no-esfericidad de las moléculas.",
                    "Se resuelven como un polinomio de tercer grado en el factor de compresibilidad $Z^3 + A_2 Z^2 + A_1 Z + A_0 = 0$.",
                    "La raíz más grande representa la fase vapor; la raíz más pequeña positiva representa la fase líquida saturada."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Factor de Compresibilidad Generalizado $Z$ y Teorema de Estados Correspondientes",
        "objetivo": "Evaluar las propiedades termodinámicas de fluidos reales utilizando la carta generalizada de Nelson-Obert basada en la temperatura reducida $T_r$ y presión reducida $P_r$.",
        "concepto_clave_latex": r"Z = \frac{P v}{R T} \quad ; \quad T_r = \frac{T}{T_c} \quad ; \quad P_r = \frac{P}{P_c} \quad ; \quad v_R' = \frac{v}{R T_c / P_c}",
        "ejemplo": "Problema 1: Se almacena gas propano ($C_3H_8$, $T_c = 369.8\\text{ K}$, $P_c = 4.25\\text{ MPa}$, masa molar $44.1\\text{ kg/kmol}$) a $T = 406.8\\text{ K}$ y $P = 8.5\\text{ MPa}$. Determinar la masa de propano en un tanque de $0.2\\text{ m}^3$ usando la carta generalizada de compresibilidad. Coordenadas reducidas: $T_r = \\frac{406.8}{369.8} = 1.10$, $P_r = \\frac{8.5}{4.25} = 2.0$. De la carta de Nelson-Obert, para $T_r = 1.10$ y $P_r = 2.0$, se lee $Z \\approx 0.44$. Constante de gas: $R = \\frac{8.314}{44.1} = 0.1885\\text{ kJ/(kg K)}$. Volumen específico: $v = \\frac{Z R T}{P} = \\frac{0.44 \\times 0.1885 \\times 406.8}{8500} = \\frac{33.74}{8500} = 0.00397\\text{ m}^3/\\text{kg}$. Masa almacenada: $m = \\frac{V}{v} = \\frac{0.2}{0.00397} \\approx 50.38\\text{ kg}$. Si se asumiera gas ideal ($Z=1$), se calcularía $m_{ideal} = 22.17\\text{ kg}$, cometiendo un error peligroso de subestimación del $56\\%$ en la capacidad del tanque. Problema 2: El teorema de estados correspondientes establece que todos los fluidos con igual $Z_c$ se desvían de la idealidad de manera casi idéntica a las mismas coordenadas reducidas $(T_r, P_r)$.",
        "bloque_sugerido": "Diseño de Recipientes 40 min • Cartas generalizadas de Nelson-Obert y volumen pseudorreducido",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES DE ESTADOS CORRESPONDIENTES",
                "titulo": "Adimensionalización Termodinámica",
                "puntos": [
                    "Todos los fluidos que exhiben las mismas coordenadas reducidas $(P_r, T_r)$ tienen el mismo factor de compresibilidad $Z$.",
                    "Zona $P_r \\ll 1$: Comportamiento como gas ideal ($Z \\to 1.0$) independientemente de la temperatura.",
                    "Zona cerca del punto crítico ($P_r \\approx 1, T_r \\approx 1$): Máxima desviación de la idealidad, con $Z_c \\approx 0.27$ para la mayoría de hidrocarburos."
                ]
            },
            {
                "numero": 2,
                "seccion": "APLICACIONES DE TRANSPORTE",
                "titulo": "Compresión y Almacenamiento Criogénico",
                "puntos": [
                    "Esencial para dimensionar recipientes de gas natural comprimido (GNC) a 200 bar.",
                    "Determina la potencia real consumida por compresores centrífugos en gasoductos troncales.",
                    "Permite calcular la densidad de gas licuado de petróleo (GLP) en tanques estacionarios domiciliarios."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Mezclas de Gases Ideales: Leyes de Dalton y Amagat y Entropía de Mezcla",
        "objetivo": "Calcular propiedades molares y másicas equivalentes de mezclas gaseosas, determinando la generación de entropía intrínseca debida a la difusión irreversible de componentes.",
        "concepto_clave_latex": r"P = \sum_{i=1}^k P_i \quad [P_i = y_i P] \quad ; \quad M_m = \sum y_i M_i \quad ; \quad \Delta S_{mezcla} = -n_m R_u \sum_{i=1}^k y_i \ln y_i > 0",
        "ejemplo": "Problema 1: Una mezcla gaseosa está compuesta por 4 kmol de nitrógeno ($N_2$, $M=28$) y 1 kmol de oxígeno ($O_2$, $M=32$) a $25^\\circ\\text{C}$ y 1 bar. Moles totales $n_m = 5\\text{ kmol}$. Fracciones molares: $y_{N_2} = 4/5 = 0.8$, $y_{O_2} = 1/5 = 0.2$. Masa molar de la mezcla: $M_m = 0.8(28) + 0.2(32) = 22.4 + 6.4 = 28.8\\text{ kg/kmol}$. Presiones parciales: $P_{N_2} = 0.8\\text{ bar}$, $P_{O_2} = 0.2\\text{ bar}$. Calcular la entropía generada durante el proceso de mezclado isotérmico de los dos gases inicialmente puros a 1 bar: $\\Delta S_{mezcla} = -5 \\times 8.314 [0.8 \\ln(0.8) + 0.2 \\ln(0.2)] = -41.57 [-0.1785 - 0.3219] = -41.57 [-0.5004] = +20.80\\text{ kJ/K}$. Esta generación de entropía positiva confirma que el mezclado es un proceso espontáneo estrictamente irreversible según la Segunda Ley. Problema 2: En la captura de $CO_2$, separar la mezcla de gases de combustión exige como trabajo mínimo el trabajo reversible de desmezclado: $W_{min} = T_0 \\Delta S_{mezcla}$.",
        "bloque_sugerido": "Mezclas Termodinámicas 40 min • Fracciones molares, fracciones másicas y trabajo mínimo de separación",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEYES DE MEZCLA GASEOSA",
                "titulo": "Dalton vs Amagat",
                "puntos": [
                    "Ley de Dalton de las Presiones Parciales: La presión total de una mezcla es la suma de las presiones que cada gas ejercería ocupando solo el volumen total a la misma temperatura.",
                    "Ley de Amagat de los Volúmenes Parciales: El volumen total de una mezcla es la suma de los volúmenes que cada gas ocuparía a la presión total y temperatura de la mezcla.",
                    "Para gases ideales, la fracción de volumen es exactamente igual a la fracción molar: $v_i / V = y_i$."
                ]
            },
            {
                "numero": 2,
                "seccion": "PARADOJA DE GIBBS",
                "titulo": "Entropía de Mezclado de Gases Distinguibles",
                "puntos": [
                    "La entropía de mezclado aparece únicamente cuando los gases son químicamente distinguibles ($N_2$ y $O_2$).",
                    "Si se mezclan dos masas del mismo gas a idéntica $T$ y $P$, la generación de entropía es cero (resolución cuántica de la paradoja de Gibbs).",
                    "Cuantifica la pérdida irreversible de exergía en procesos de dilución de chimeneas y escapes industriales."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Psicrometría Fundamental y Acondicionamiento de Aire",
        "objetivo": "Modelar el aire húmedo como mezcla binaria de aire seco y vapor de agua, deduciendo la humedad específica $\\omega$, humedad relativa $\\phi$ y temperatura de punto de rocío $T_{dp}$.",
        "concepto_clave_latex": r"\omega = 0.622 \frac{P_v}{P - P_v} \quad \left[\frac{\text{kg}_{vapor}}{\text{kg}_{aire\_seco}}\right] \quad ; \quad \phi = \frac{P_v}{P_{sat}(T)} \quad ; \quad h = c_{pa} T + \omega (2501 + 1.82 T) \ [\text{kJ/kg}_{as}]",
        "ejemplo": "Problema 1: En Santa Marta, el aire ambiente está a $32^\\circ\\text{C}$ con una humedad relativa del $\\phi = 75\\%$ a presión barométrica estándar de $P = 101.325\\text{ kPa}$. La presión de saturación a $32^\\circ\\text{C}$ es $P_{sat} = 4.759\\text{ kPa}$. Calcular la presión parcial de vapor, la humedad específica y la entalpía del aire húmedo: Presión de vapor: $P_v = 0.75 \\times 4.759 = 3.569\\text{ kPa}$. Humedad específica: $\\omega = 0.622 \\frac{3.569}{101.325 - 3.569} = 0.622 \\frac{3.569}{97.756} = 0.02271\\text{ kg}_{v}/\\text{kg}_{as}$ (22.7 g de agua por kg de aire seco). Entalpía: $h = 1.005(32) + 0.02271(2501 + 1.82 \\times 32) = 32.16 + 0.02271(2559.24) = 32.16 + 58.12 = 90.28\\text{ kJ/kg}_{as}$. La humedad aporta el $64.4\\%$ de la carga térmica total. Problema 2: Para deshumidificar este aire hasta $22^\\circ\\text{C}$ y $50\\%$, el aire debe enfriarse por debajo de su punto de rocío ($T_{dp} \\approx 26.8^\\circ\\text{C}$), condensando agua en los serpentines del evaporador.",
        "bloque_sugerido": "Climatización 45 min • Manejo de la carta psicrométrica y cargas sensibles vs latentes",
        "slides": [
            {
                "numero": 1,
                "seccion": "PARÁMETROS DEL AIRE HÚMEDO",
                "titulo": "Definición Termodinámica de Variables",
                "puntos": [
                    "Aire Seco: Mezcla no condensable de gases con masa molar fija $M_{as} = 28.97\\text{ kg/kmol}$.",
                    "Humedad Relativa $\\phi$: Relación entre la masa de vapor de agua presente y la masa máxima que el aire podría retener a esa temperatura antes de saturarse.",
                    "Temperatura de Rocío $T_{dp}$: Temperatura a la cual el vapor comienza a condensar al enfriarse a presión constante ($P_v = P_{sat}(T_{dp})$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONFORT TÉRMICO Y HVAC",
                "titulo": "Calor Sensible vs Calor Latente",
                "puntos": [
                    "Factor de Calor Sensible (SHR): $\\text{SHR} = \\frac{\\dot{Q}_{sensible}}{\\dot{Q}_{total}}$. En climas tropicales costeros, $\\text{SHR} \\approx 0.60 - 0.70$.",
                    "El enfriamiento evaporativo directo solo es viable en climas secos; en el Caribe se requiere deshumidificación forzada por compresión o desecantes sólidos.",
                    "Optimiza el consumo energético de los sistemas de aire acondicionado en edificios universitarios."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Procesos Psicrométricos Industriales: Torres de Enfriamiento Evaporativas",
        "objetivo": "Diseñar torres de enfriamiento de agua mediante balances de masa y energía psicrométricos, calculando el rango de enfriamiento, el acercamiento (approach) y el agua de reposición (make-up).",
        "concepto_clave_latex": r"\text{Rango} = T_{w,in} - T_{w,out} \quad ; \quad \text{Approach} = T_{w,out} - T_{wb} \quad ; \quad \dot{m}_{make-up} = \dot{m}_{evap} + \dot{m}_{drift} + \dot{m}_{blowdown}",
        "ejemplo": "Problema 1: Una torre de enfriamiento de tiro forzado para el condensador de una central térmica recibe $100\\text{ kg/s}$ de agua caliente a $40^\\circ\\text{C}$ y la enfría hasta $28^\\circ\\text{C}$ (Rango = $12^\\circ\\text{C}$). El aire exterior entra a $30^\\circ\\text{C}$ con temperatura de bulbo húmedo $T_{wb} = 24^\\circ\\text{C}$ (Approach = $4^\\circ\\text{C}$, $h_1 = 72.5\\text{ kJ/kg}$, $\\omega_1 = 0.015\\text{ kg/kg}$) y sale saturado a $35^\\circ\\text{C}$ ($h_2 = 129.0\\text{ kJ/kg}$, $\\omega_2 = 0.0365\\text{ kg/kg}$). Calor disipado del agua: $\\dot{Q} = 100 \\times 4.18 \\times 12 = 5016\\text{ kW}$. Caudal másico de aire seco necesario: $\\dot{m}_{as} = \\frac{\\dot{Q}}{h_2 - h_1} = \\frac{5016}{129.0 - 72.5} = \\frac{5016}{56.5} = 88.78\\text{ kg/s}$. Tasa de agua evaporada: $\\dot{m}_{evap} = \\dot{m}_{as}(\\omega_2 - \\omega_1) = 88.78(0.0365 - 0.015) = 88.78(0.0215) = 1.909\\text{ kg/s}$. Se evaporan aproximadamente 1.91 litros de agua por segundo para enfriar los 100 kg/s de agua circulante. Problema 2: La purga periódica ('blowdown') es mandataria para evitar la precipitación de carbonato de calcio e incrustaciones en las paredes del condensador.",
        "bloque_sugerido": "Sistemas Térmicos 45 min • Ecuación de Merkel y dimensionamiento de relleno en torres de enfriamiento",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA EVAPORATIVA",
                "titulo": "Enfriamiento por Calor Latente",
                "puntos": [
                    "El enfriamiento no se logra por convección sensible con el aire, sino porque el agua se evapora consumiendo su propio calor latente de vaporización ($~2430\\text{ kJ/kg}$).",
                    "El límite termodinámico inferior absoluto alcanzable por el agua enfriada es la temperatura de bulbo húmedo del aire ambiente ($T_{wb}$).",
                    "Un 'approach' típico de diseño oscila entre $3^\\circ\\text{C}$ y $6^\\circ\\text{C}$ para equilibrar costos de inversión y consumo de ventilador."
                ]
            },
            {
                "numero": 2,
                "seccion": "COMPONENTES DE LA TORRE",
                "titulo": "Relleno, Separadores de Gotas y Tiro",
                "puntos": [
                    "Relleno de película ('film fill'): Aumenta el área superficial de contacto líquido-gas sin generar caídas excesivas de presión de aire.",
                    "Separadores de gotas ('drift eliminators'): Reducen el arrastre mecánico de gotas de agua líquida a menos del $0.005\\%$ del caudal circulante.",
                    "Torres de tiro natural hiperbólicas: Emplean el tiro inducido por boyamiento hidrostático de aire caliente sin ventiladores eléctricos en grandes centrales de 1 GW."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Termodinámica de la Combustión: Relación Aire-Combustible y Dosado Relativo",
        "objetivo": "Balancear ecuaciones estequiométricas de combustión completa e incompleta para hidrocarburos y biomasa, determinando la relación aire-combustible real $(A/F)$ y el factor de equivalencia $\\lambda$.",
        "concepto_clave_latex": r"(A/F)_{esteq} = \frac{m_{aire,esteq}}{m_{comb}} = \frac{4.76 a M_{aire}}{M_{comb}} \quad ; \quad \lambda = \frac{(A/F)_{real}}{(A/F)_{esteq}} = \frac{1}{\Phi}",
        "ejemplo": "Problema 1: Calcular la relación aire-combustible estequiométrica en base masa para la combustión de octano líquido ($C_8H_{18}$, $M = 114.22\\text{ kg/kmol}$) con aire teórico ($21\\% O_2, 79\\% N_2$, $M_{aire} = 28.97\\text{ kg/kmol}$). Ecuación estequiométrica: $C_8H_{18} + 12.5(O_2 + 3.76 N_2) \\rightarrow 8 CO_2 + 9 H_2O + 47.0 N_2$. Moles de aire por kmol de combustible: $n_{aire} = 12.5 \\times 4.76 = 59.5\\text{ kmol}$. Masa de aire: $m_{aire} = 59.5 \\times 28.97 = 1723.7\\text{ kg}$. Luego: $(A/F)_{esteq} = \\frac{1723.7}{114.22} = 15.09\\text{ kg aire / kg combustible}$. Problema 2: Si un motor diésel opera con un $40\\%$ de exceso de aire ($\\lambda = 1.40$), la relación aire-combustible real es $(A/F)_{real} = 1.40 \\times 15.09 = 21.13\\text{ kg/kg}$, garantizando combustión completa libre de inquemados de monóxido de carbono ($CO$) y hollín particulado.",
        "bloque_sugerido": "Cinética y Combustión 40 min • Análisis Orsat en base seca y dosado estequiométrico",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTEQUIOMETRÍA QUÍMICA",
                "titulo": "Balance Molar de Elementos",
                "puntos": [
                    "Conservación estricta de especies atómicas individuales: Carbono ($C$), Hidrógeno ($H$), Oxígeno ($O$) y Nitrógeno ($N$).",
                    "El nitrógeno se modela habitualmente como gas inerte térmico diatómico a temperaturas moderadas ($N_2$).",
                    "Mezclas ricas ($\\Phi > 1, \\lambda < 1$): Deficiencia de oxígeno; genera $CO$, hidrocarburos no quemados ($HC$) y hollín.",
                    "Mezclas pobres ($\\Phi < 1, \\lambda > 1$): Exceso de oxígeno; reduce la temperatura de llama y minimiza emisiones de monóxido."
                ]
            },
            {
                "numero": 2,
                "seccion": "GASES DE COMBUSTIÓN",
                "titulo": "Análisis en Base Seca vs Húmeda",
                "puntos": [
                    "Los analizadores de gases de chimenea (sensores electroquímicos y cromatógrafos) condensan previamente el agua, midiendo fracciones molares en base seca.",
                    "La presencia de oxígeno residual en los humos permite reconstruir de forma inequívoca el exceso de aire real con el que opera la caldera.",
                    "Permite optimizar la relación aire/combustible en tiempo real reduciendo pérdidas de calor por humos calientes de chimenea."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Entalpía de Formación, Entalpía de Combustión y Poderes Caloríficos (HHV / LHV)",
        "objetivo": "Aplicar la Primera Ley a reactores químicos de flujo estacionario utilizando entalpías estándar de formación $\\bar{h}_f^0$, calculando el poder calorífico superior e inferior de combustibles fósiles y renovables.",
        "concepto_clave_latex": r"\Delta H_R^0 = \sum n_p \bar{h}_{f,p}^0 - \sum n_r \bar{h}_{f,r}^0 \quad ; \quad \text{HHV} = \text{LHV} + \left(\frac{m_{H_2O}}{m_{comb}}\right) h_{fg,H_2O}",
        "ejemplo": "Problema 1: Calcular la entalpía de combustión del metano gaseoso ($CH_4$) a $25^\\circ\\text{C}$ sabiendo que: $\\bar{h}_{f,CH_4}^0 = -74850\\text{ kJ/kmol}$, $\\bar{h}_{f,CO_2}^0 = -393520\\text{ kJ/kmol}$, $\\bar{h}_{f,H_2O(l)}^0 = -285830\\text{ kJ/kmol}$, $\\bar{h}_{f,O_2}^0 = 0$. Reacción: $CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O(l)$. Entalpía de reacción (HHV molar): $\\Delta H_R^0 = [1(-393520) + 2(-285830)] - [1(-74850) + 0] = [-393520 - 571660] + 74850 = -965180 + 74850 = -890330\\text{ kJ/kmol}$. Masa molar del metano: $16.043\\text{ kg/kmol}$. Poder Calorífico Superior másico: $\\text{HHV} = \\frac{890330}{16.043} = 55497\\text{ kJ/kg} = 55.50\\text{ MJ/kg}$. Problema 2: En el Poder Calorífico Inferior (LHV), el agua en los productos permanece como vapor ($\bar{h}_{f,H_2O(v)}^0 = -241820\\text{ kJ/kmol}$): $\\text{LHV}_{molar} = -802310\\text{ kJ/kmol} \\implies \\text{LHV} = 50.01\\text{ MJ/kg}$. La condensación del vapor de agua en calderas de condensación recupera este $10.9\\%$ adicional de calor latente.",
        "bloque_sugerido": "Termoquímica 45 min • Cálculo de calores de reacción y bomba calorimétrica de Berthelot",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTADO TERMODINÁMICO DE REFERENCIA",
                "titulo": "La Convención de Formación Estándar",
                "puntos": [
                    "A los elementos químicos puros en su forma alotrópica más estable a $25^\\circ\\text{C}$ (298.15 K) y 1 atm se les asigna entalpía de formación nula: $\\bar{h}_f^0 = 0$ ($O_2, N_2, H_2, C_{grafito}$).",
                    "La entalpía de un compuesto a cualquier temperatura es: $\\bar{h}(T) = \\bar{h}_f^0 + [\\bar{h}(T) - \\bar{h}^0(298.15)]$.",
                    "Permite balancear la Primera Ley en sistemas reaccionantes sin ambigüedades de niveles de referencia."
                ]
            },
            {
                "numero": 2,
                "seccion": "HHV vs LHV EN INGENIERÍA",
                "titulo": "Diferenciación Operativa",
                "puntos": [
                    "Poder Calorífico Superior (HHV): El agua de combustión se condensa completamente al estado líquido a $25^\\circ\\text{C}$.",
                    "Poder Calorífico Inferior (LHV): El agua de combustión abandona los humos en estado gaseoso (condición estándar de turbinas de gas y calderas convencionales).",
                    "Biomasas húmedas sufren una severa penalización de LHV porque gran parte del calor liberado se consume evaporando su propia humedad interna."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Temperatura de Llama Adiabática a Presión y Volumen Constante",
        "objetivo": "Calcular la máxima temperatura teórica alcanzada por los productos de combustión en ausencia total de pérdidas de calor hacia los alrededores ($Q = 0$) y sin trabajo de eje.",
        "concepto_clave_latex": r"H_{productos}(T_{ad}) = H_{reactivos}(T_{reac}) \implies \sum_{p} n_p \left[ \bar{h}_{f,p}^0 + \Delta \bar{h}_p(T_{ad}) \right] = \sum_{r} n_r \left[ \bar{h}_{f,r}^0 + \Delta \bar{h}_r(T_{reac}) \right]",
        "ejemplo": "Problema 1: Se quema metano gaseoso con aire estequiométrico puro a $25^\\circ\\text{C}$ a presión constante de 1 atm en una cámara de combustión adiabática. Balance entálpico: $H_{prod}(T_{ad}) = H_{reac}(298\\text{ K}) = -74850\\text{ kJ}$. En los productos: $1 CO_2 + 2 H_2O + 7.52 N_2$. Mediante balance iterativo con tablas de entalpía de gases ideales: para $T = 2300\\text{ K}$, $H_{prod} = -92500\\text{ kJ}$; para $T = 2400\\text{ K}$, $H_{prod} = +5800\\text{ kJ}$. Interpolando linealmente: $T_{ad} \\approx 2328\\text{ K} \\approx 2055^\\circ\\text{C}$. Problema 2: Si se utiliza un $100\\%$ de exceso de aire ($\\lambda = 2.0$), la masa adicional de nitrógeno y oxígeno en los productos absorbe gran parte de la energía liberada como calor sensible, reduciendo la temperatura de llama adiabática a aproximadamente $1350^\\circ\\text{C}$, cota máxima permitida para proteger los álabes de la turbina de gas.",
        "bloque_sugerido": "Diseño de Quemadores 45 min • Iteración numérica de temperatura de llama adiabática",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITE TÉRMICO SUPERIOR",
                "titulo": "Condición Adiabática Pura",
                "puntos": [
                    "Representa el techo térmico físico alcanzable en una cámara de combustión bien aislada.",
                    "La temperatura real de llama en operación es siempre entre $150^\\circ\\text{C}$ y $300^\\circ\\text{C}$ menor debido a pérdidas radiativas a las paredes y disociación molecular incompleta.",
                    "La combustión a volumen constante (en motores de pistón) genera una temperatura y presión de pico sensiblemente superior a la combustión a presión constante."
                ]
            },
            {
                "numero": 2,
                "seccion": "FORMACIÓN DE CONTAMINANTES",
                "titulo": "Mecanismo Térmico de Zeldovich (NOx)",
                "puntos": [
                    "A temperaturas superiores a $1550^\\circ\\text{C}$ (1800 K), las moléculas de $N_2$ del aire reaccionan térmicamente con el oxígeno para formar óxidos de nitrógeno ($NO$ y $NO_2$).",
                    "La tasa de generación de $NO_x$ crece exponencialmente con la temperatura adiabática de llama.",
                    "Técnicas de quemadores de bajas emisiones (Dry Low NOx - DLN) utilizan mezclas muy pobres premezcladas para mantener $T_{ad} < 1500^\\circ\\text{C}$."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Segunda Ley en Reacciones Químicas y Destrucción de Exergía de Combustión",
        "objetivo": "Evaluar la irreversibilidad intrínseca en la combustión de combustibles fósiles y biomasa, determinando la destrucción de exergía debida a gradientes químicos y térmicos.",
        "concepto_clave_latex": r"\dot{I}_{comb} = \dot{E}x_{D,comb} = T_0 \dot{S}_{gen} \quad ; \quad \dot{S}_{gen} = \sum \dot{n}_p \bar{s}_p - \sum \dot{n}_r \bar{s}_r - \frac{\dot{Q}_{perdida}}{T_0} \quad ; \quad \eta_{ex,comb} \approx 65 - 75\%",
        "ejemplo": "Problema 1: En una caldera industrial se quema metano a $25^\\circ\\text{C}$ y 1 bar de forma adiabática. La exergía química del metano es $\\bar{e}x_{ch} = 831650\\text{ kJ/kmol}$. Los productos se generan a $T_{ad} \\approx 2300\\text{ K}$. La entropía de los productos a esa temperatura es mayor que la de los reactivos entrantes, generándose $\\Delta \\bar{S}_{gen} = 89.4\\text{ kJ/(kmol K)}$. A una temperatura ambiente de $T_0 = 298.15\\text{ K}$, la destrucción de exergía por irreversibilidad química pura es: $\\bar{I} = T_0 \\Delta \\bar{S}_{gen} = 298.15 \\times 89.4 = 26655\\text{ kJ/kmol}$. La eficiencia exergética de la combustión es $\\eta_{ex} = \\frac{831650 - 26655}{831650} = \\frac{804995}{831650} \\approx 96.8\\%$. Sin embargo, si esos gases calientes se enfrían en un generador de vapor transfiriendo calor a agua a $250^\\circ\\text{C}$, la transferencia a través de una diferencia de temperatura finita de más de $1500^\\circ\\text{C}$ destruye un $25\\%$ adicional de la exergía original. Problema 2: En celdas de combustible (SOFC), la oxidación electroquímica directa ocurre casi reversiblemente sin combustión en llama libre, alcanzando eficiencias exergéticas superiores al $80\\%$.",
        "bloque_sugerido": "Exergía Química 45 min • Exergía química estándar de Szargut y balances exergéticos",
        "slides": [
            {
                "numero": 1,
                "seccion": "IRREVERSIBILIDAD DE LA COMBUSTIÓN",
                "titulo": "Degradación Molecular de la Energía",
                "puntos": [
                    "La combustión en llama abierta es uno de los procesos industriales más destructores de exergía en el universo tecnológico.",
                    "Entre un 25% y un 35% de la capacidad de producir trabajo del combustible se destruye irremediablemente en la zona de reacción.",
                    "Causas principales: Reorganización molecular incontrolada, difusión violenta de especies químicas y conducción térmica interna extrema."
                ]
            },
            {
                "numero": 2,
                "seccion": "MITIGACIÓN EXERGÉTICA",
                "titulo": "Precalentamiento y Combustión Química en Bucle",
                "puntos": [
                    "Precalentar el aire de combustión con gases residuales de escape reduce la tasa neta de destrucción de exergía.",
                    "Chemical Looping Combustion (CLC): Utiliza transportadores de oxígeno metálicos ($Fe_2O_3, CuO$) en dos reactores acoplados, reduciendo las pérdidas de mezcla y facilitando captura pura de $CO_2$.",
                    "Fundamental para el diseño de plantas térmicas de alta eficiencia."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Equilibrio Químico y Constante de Equilibrio $K_p(T)$ (Ecuación de van 't Hoff)",
        "objetivo": "Calcular la composición de equilibrio de mezclas reactivas a alta temperatura minimizando la energía libre de Gibbs y aplicando la constante de equilibrio en presiones parciales $K_p(T)$.",
        "concepto_clave_latex": r"\Delta G_R^0(T) = -R_u T \ln K_p(T) \quad ; \quad \frac{d(\ln K_p)}{dT} = \frac{\Delta H_R^0}{R_u T^2} \quad ; \quad K_p = \prod \left(\frac{P_i}{P^0}\right)^{\nu_i}",
        "ejemplo": "Problema 1: Para la reacción endotérmica de reformado de metano con vapor: $CH_4 + H_2O \\leftrightarrow CO + 3H_2$ con $\\Delta H_R^0 = +206\\text{ kJ/mol}$. A $25^\\circ\\text{C}$ (298 K), $\\Delta G_R^0 = +142\\text{ kJ/mol}$, por lo que $\\ln K_p = -\\frac{142000}{8.314 \\times 298.15} = -57.3 \\implies K_p \\approx 1.3 \\times 10^{-25}$ (la reacción no procede espontáneamente a temperatura ambiente). Aplicando la ecuación de van 't Hoff, al ser $\\Delta H_R^0 > 0$, la constante $K_p$ crece exponencialmente con la temperatura. A $T = 1073\\text{ K}$ ($800^\\circ\\text{C}$), $\\Delta G_R^0 \\approx -25\\text{ kJ/mol} \\implies K_p \\approx 16.5$. A alta temperatura, el equilibrio se desplaza fuertemente hacia la formación de gas de síntesis ($CO + H_2$). Problema 2: El principio de Le Chatelier demuestra que como la reacción incrementa el número total de moles gaseosos ($2 \\to 4$), un aumento de la presión total frena la conversión, por lo que los reformadores solares operan a presiones optimizadas intermedias.",
        "bloque_sugerido": "Equilibrio Químico 45 min • Ecuación de van 't Hoff y composición de equilibrio en gases",
        "slides": [
            {
                "numero": 1,
                "seccion": "CRITERIO DE EQUILIBRIO DE GIBBS",
                "titulo": "Minimización de la Energía Libre",
                "puntos": [
                    "A presión y temperatura constantes, una mezcla reaccionante alcanza el equilibrio térmico y químico en el punto donde su energía de Gibbs total es mínima: $(dG)_{T,P} = 0$.",
                    "El grado de avance de la reacción $\\xi$ se estabiliza cuando la afinidad química se anula: $\\sum \\nu_i \\mu_i = 0$.",
                    "La constante $K_p$ depende única y exclusivamente de la temperatura absoluta $T$, no de la presión total del sistema."
                ]
            },
            {
                "numero": 2,
                "seccion": "PRINCIPIO DE LE CHATELIER",
                "titulo": "Respuesta a Perturbaciones Externas",
                "puntos": [
                    "Reacción endotérmica ($\Delta H > 0$): Un aumento de temperatura desplaza el equilibrio hacia los productos ($K_p$ aumenta).",
                    "Reacción exotérmica ($\Delta H < 0$): Un aumento de temperatura favorece a los reactivos ($K_p$ disminuye).",
                    "Un incremento de la presión total desplaza el equilibrio hacia el lado con menor número de moles gaseosos netos."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Disociación Térmica de Gases de Combustión a Alta Temperatura",
        "objetivo": "Modelar la disociación reversible del $CO_2$ y del $H_2O$ en radicales libres y monóxido a temperaturas superiores a 1800 K, evaluando su efecto amortiguador sobre la temperatura real de llama.",
        "concepto_clave_latex": r"\text{CO}_2 \xrightleftharpoons{} \text{CO} + \frac{1}{2}\text{O}_2 \quad ; \quad \text{H}_2\text{O} \xrightleftharpoons{} \text{H}_2 + \frac{1}{2}\text{O}_2 \quad ; \quad \text{H}_2\text{O} \xrightleftharpoons{} \frac{1}{2}\text{H}_2 + \text{OH}",
        "ejemplo": "Problema 1: En una cámara de combustión de cohete a $T = 2800\\text{ K}$ y 30 bar, se alimenta $1\\text{ kmol}$ de $CO_2$. Si una fracción $\\alpha$ se disocia en $CO + \\frac{1}{2}O_2$, la mezcla en equilibrio contiene $(1-\\alpha)\\text{ kmol } CO_2$, $\\alpha\\text{ kmol } CO$, y $0.5\\alpha\\text{ kmol } O_2$. Moles totales: $n_T = 1 + 0.5\\alpha$. A 2800 K, $\\ln K_p = -1.52 \\implies K_p = 0.2187$. Ecuación de equilibrio: $K_p = \\frac{y_{CO} y_{O_2}^{1/2}}{y_{CO_2}} \\left(\\frac{P}{P^0}\\right)^{1/2} = \\frac{\\alpha (0.5\\alpha)^{1/2}}{(1-\\alpha)(1 + 0.5\\alpha)^{1/2}} \\sqrt{30} = 0.2187$. Resolviendo para $\\alpha$: se obtiene $\\alpha \\approx 0.14$. El $14\\%$ del dióxido de carbono se rompe espontáneamente absorbiendo $283\\text{ kJ/mol}$ de calor endotérmico, lo que frena el aumento de temperatura de los gases. Problema 2: A medida que los gases se expanden y enfrían en la tobera de escape, el equilibrio se recombina liberando calor, un fenómeno modelado mediante cinética química congelada vs cinética en equilibrio químico local.",
        "bloque_sugerido": "Combustión Avanzada 45 min • Cálculo de disociación simultánea múltiple con NASA CEA",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA DE DISOCIACIÓN",
                "titulo": "Ruptura de Enlaces a Calor Extremo",
                "puntos": [
                    "A temperaturas ordinarias ($< 1200^\\circ\\text{C}$), la combustión completa convierte el 100% del carbono en $CO_2$ y el hidrógeno en $H_2O$.",
                    "Por encima de $1800^\\circ\\text{C}$, la energía térmica de colisión supera la energía de enlace covalente, disociando moléculas estables en fragmentos y radicales ($CO, OH, H, O, NO$).",
                    "Actúa como un 'termostato químico natural' que absorbe calor latente endotérmico y limita la temperatura máxima alcanzable."
                ]
            },
            {
                "numero": 2,
                "seccion": "RECOMBINACIÓN EN TOBERAS",
                "titulo": "Flujo en Equilibrio vs Congelado",
                "puntos": [
                    "Flujo en Equilibrio (Equilibrium Flow): Las reacciones de recombinación son instantáneas, liberando toda la energía química durante la expansión.",
                    "Flujo Congelado (Frozen Flow): La velocidad del gas es tan alta que los radicales no tienen tiempo de chocar y recombinarse, perdiendo empuje y eficiencia termodinámica.",
                    "Crucial para el diseño de turbinas de gas aeroderivadas y propulsión aeroespacial."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ciclos de Refrigeración por Compresión de Vapor Multietapa y en Cascada",
        "objetivo": "Diseñar ciclos frigoríficos de dos etapas con enfriamiento intermedio por tanque flash y sistemas en cascada con fluidos disímiles para ultracongelación industrial y licuefacción.",
        "concepto_clave_latex": r"\text{COP}_{multietapa} = \frac{\dot{Q}_L}{\dot{W}_{comp,1} + \dot{W}_{comp,2}} > \text{COP}_{simple} \quad ; \quad P_{int} \approx \sqrt{P_{evap} P_{cond}}",
        "ejemplo": "Problema 1: Un sistema de congelación de atún a $-40^\\circ\\text{C}$ ($P_{evap} = 51.2\\text{ kPa}$) rechaza calor a un ambiente de $+35^\\circ\\text{C}$ ($P_{cond} = 887.6\\text{ kPa}$) usando amoníaco ($NH_3$). Una compresión en una sola etapa requeriría una relación de compresión de $r_p = \\frac{887.6}{51.2} = 17.33$, provocando temperaturas de descarga de compresor superiores a $180^\\circ\\text{C}$ que degradan el aceite lubricante. Presión intermedia óptima: $P_{int} = \\sqrt{51.2 \\times 887.6} = \\sqrt{45445} \\approx 213.2\\text{ kPa}$ ($-10^\\circ\\text{C}$). La relación de compresión en cada etapa se reduce a solo $r_{p,1} = 213.2/51.2 = 4.16$, bajando la temperatura de descarga a menos de $85^\\circ\\text{C}$. Problema 2: En sistemas en cascada para licuefacción de gas natural (GNL a $-162^\\circ\\text{C}$), se acopla un ciclo de propano superior que condensa un ciclo intermedio de etileno, el cual a su vez condensa un ciclo inferior de metano, logrando un COP global optimizado.",
        "bloque_sugerido": "Refrigeración Industrial 45 min • Diagrama P-h de amoníaco con tanque economizador flash",
        "slides": [
            {
                "numero": 1,
                "seccion": "LÍMITES DE UNA SOLA ETAPA",
                "titulo": "Por qué Dividir la Compresión",
                "puntos": [
                    "Altas relaciones de compresión ($r_p > 8$) provocan caídas drásticas en el rendimiento volumétrico del compresor.",
                    "Calentamiento excesivo de los gases de descarga que carboniza el aceite sintético de lubricación.",
                    "El tanque flash intermedio separa el vapor generado en la primera expansión desahogando al compresor de baja presión."
                ]
            },
            {
                "numero": 2,
                "seccion": "SISTEMAS EN CASCADA",
                "titulo": "Fluidos Refrigerantes Diferenciados",
                "puntos": [
                    "Utiliza dos o más circuitos de refrigeración completamente independientes térmicamente conectados por un intercambiador condensador-evaporador intermedio.",
                    "Permite elegir el refrigerante idóneo para cada rango de temperatura (evitando presiones subatmosféricas de vacío profundo en la etapa fría).",
                    "Estándar en el procesamiento y almacenamiento de nitrógeno líquido y vacunas a ultra-baja temperatura ($-80^\\circ\\text{C}$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ciclos de Refrigeración por Absorción ($NH_3-H_2O$ y $LiBr-H_2O$)",
        "objetivo": "Modelar el ciclo de refrigeración accionado térmicamente donde una bomba de solución y un absorbedor reemplazan al compresor mecánico, calculando el COP térmico.",
        "concepto_clave_latex": r"\text{COP}_{abs} = \frac{\dot{Q}_L}{\dot{Q}_{generador} + \dot{W}_{bomba}} \approx \frac{\dot{Q}_L}{\dot{Q}_G} \quad ; \quad \text{COP}_{Carnot} = \left(\frac{T_L}{T_0 - T_L}\right)\left(\frac{T_G - T_0}{T_G}\right)",
        "ejemplo": "Problema 1: Un enfriador de absorción de agua-bromuro de litio ($H_2O - LiBr$) se alimenta con calor residual de un motor a gas a $T_G = 95^\\circ\\text{C}$ (368.15 K). Enfría agua para aire acondicionado a $T_L = 7^\\circ\\text{C}$ (280.15 K) y rechaza calor a la torre de enfriamiento a $T_0 = 32^\\circ\\text{C}$ (305.15 K). Calcular el COP de Carnot reversible máximo teórico: Factor frigorífico: $\\frac{T_L}{T_0 - T_L} = \\frac{280.15}{305.15 - 280.15} = \\frac{280.15}{25} = 11.206$. Factor motor térmico: $\\frac{T_G - T_0}{T_G} = \\frac{368.15 - 305.15}{368.15} = \\frac{63}{368.15} \\approx 0.1711$. Multiplicando ambos factores: $\\text{COP}_{Carnot} = 11.206 \\times 0.1711 \\approx 1.917$. Un enfriador comercial de simple efecto alcanza un $\\text{COP}_{real} \\approx 0.72$ (alrededor del $37\\%$ del límite de Carnot). Problema 2: Como el trabajo mecánico de bombeo de líquido $\\dot{W}_{bomba} = \\dot{V} \\Delta P$ consume menos del $1\\%$ del calor suministrado al generador, el ciclo opera impulsado prácticamente por energía térmica pura gratuita.",
        "bloque_sugerido": "Climatización Solar 45 min • Carta entalpía-concentración de soluciones LiBr-Agua",
        "slides": [
            {
                "numero": 1,
                "seccion": "COMPRESIÓN TÉRMICA",
                "titulo": "Sustitución del Compresor Mecánico",
                "puntos": [
                    "El absorbedor absorbe los vapores de refrigerante a baja presión en una solución líquida concentrada liberando calor de dilución.",
                    "La bomba eleva la presión de la fase líquida con un consumo eléctrico infinitesimal frente a la compresión de vapor.",
                    "El generador (hervidor) calienta la solución rica con vapor o agua caliente, desorbiendo el vapor refrigerante a alta presión."
                ]
            },
            {
                "numero": 2,
                "seccion": "PARES QUÍMICOS DOMINANTES",
                "titulo": "LiBr-Agua vs Amoníaco-Agua",
                "puntos": [
                    "Agua-Bromuro de Litio: El agua es el refrigerante y el LiBr es el absorbente; limitado a $T > 0^\\circ\\text{C}$ (aire acondicionado); riesgo de cristalización de la sal a altas concentraciones.",
                    "Amoníaco-Agua: El amoníaco es el refrigerante y el agua es el absorbente; opera por debajo de $0^\\circ\\text{C}$ (hielo y congelación); requiere columna rectificadora para eliminar trazas de agua del amoníaco.",
                    "Integración ideal con colectores solares térmicos de tubos al vacío."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ciclos de Licuefacción de Gases: Procesos Linde-Hampson y Claude para Hidrógeno y GNL",
        "objetivo": "Modelar la licuefacción criogénica de gases permanentes integrando compresión isotérmica, intercambiadores de calor regenerativos en contracorriente y expansión isoentálpica (Linde) o isoentrópica (Claude).",
        "concepto_clave_latex": r"y = \frac{\dot{m}_{liq}}{\dot{m}} = \frac{h_1 - h_2}{h_1 - h_f} \quad ; \quad W_{min} = T_0 (s_1 - s_f) - (h_1 - h_f) \quad [\text{kWh/kg}]",
        "ejemplo": "Problema 1: En un ciclo simple de Linde para licuar metano, el gas retorna por el intercambiador a $1\\text{ bar}$ y $290\\text{ K}$ ($h_1 = 1180\\text{ kJ/kg}$). Tras ser comprimido a $200\\text{ bar}$ y preenfriado a $290\\text{ K}$, entra a la línea de alta presión con $h_2 = 820\\text{ kJ/kg}$. En el recibidor de líquido a 1 bar ($-161.5^\\circ\\text{C}$), la entalpía del líquido saturado es $h_f = 285\\text{ kJ/kg}$. Calcular la fracción licuada por cada kg de gas comprimido: $y = \\frac{h_1 - h_2}{h_1 - h_f} = \\frac{1180 - 820}{1180 - 285} = \\frac{360}{895} \\approx 0.4022$ ($40.22\\%$ de rendimiento de licuefacción por ciclo). Problema 2: En la licuefacción de hidrógeno para transporte naval, el ciclo Claude introduce una turbina de expansión criogénica intermedia (expansor) que realiza trabajo mecánico real a costa de la energía interna del gas, reduciendo el consumo energético de $30\\text{ kWh/kg}$ a menos de $10\\text{ kWh/kg}$.",
        "bloque_sugerido": "Criogenia 45 min • Ciclos Linde-Hampson y conversión orto-para hidrógeno en catalizadores",
        "slides": [
            {
                "numero": 1,
                "seccion": "CRIOGENIA PROFUNDA",
                "titulo": "El Reto de los Gases Permanentes",
                "puntos": [
                    "Fluidos como metano ($T_b = 111.6\\text{ K}$), oxígeno ($90.2\\text{ K}$), nitrógeno ($77.3\\text{ K}$) e hidrógeno ($20.3\\text{ K}$) no pueden condensarse por simple compresión a temperatura ambiente.",
                    "El intercambiador regenerador utiliza los gases fríos que no condensaron en la válvula para preenfriar el flujo entrante de alta presión.",
                    "El proceso es continuo hasta que la temperatura previa a la válvula desciende por debajo de la curva de saturación."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONVERSIÓN ORTO-PARA HIDRÓGENO",
                "titulo": "Espín Nuclear en Hidrógeno Líquido",
                "puntos": [
                    "A temperatura ambiente, el hidrógeno normal es $75\\%$ orto-hidrógeno (espines de protones paralelos) y $25\\%$ para-hidrógeno (espines antiparalelos).",
                    "En estado líquido a 20 K, el equilibrio exige $> 99.8\\%$ para-hidrógeno.",
                    "La conversión espontánea orto a para libera $703\\text{ kJ/kg}$ de calor (superior al calor de vaporización de $446\\text{ kJ/kg}$), evaporando el líquido en los tanques si no se emplean catalizadores de óxido de hierro en el ciclo."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ciclos Stirling y Ericsson con Regeneración Térmica Ideal",
        "objetivo": "Modelar ciclos cerrados de combustión externa que operan entre dos isotermas con regeneración interna completa, demostrando teóricamente su equivalencia con la eficiencia de Carnot.",
        "concepto_clave_latex": r"\eta_{Stirling, ideal} = \eta_{Ericsson, ideal} = 1 - \frac{T_L}{T_H} = \eta_{Carnot} \quad ; \quad Q_{reg, absorbe} = Q_{reg, cede} = m c_v (T_H - T_L)",
        "ejemplo": "Problema 1: Un motor Stirling ideal opera con $0.05\\text{ kg}$ de helio ($c_v = 3.116\\text{ kJ/(kg K)}$, $R = 2.077\\text{ kJ/(kg K)}$) entre una fuente geotérmica de alta entalpía a $T_H = 300^\\circ\\text{C}$ (573.15 K) y un río de enfriamiento a $T_L = 25^\\circ\\text{C}$ (298.15 K). La relación de compresión volumétrica es $r_v = v_{max}/v_{min} = 2.5$. Calcular la eficiencia térmica teórica y el trabajo neto por ciclo: Eficiencia: $\\eta = 1 - \\frac{298.15}{573.15} = 1 - 0.5202 = 47.98\\%$. Calor absorbido en la expansión isoterma: $Q_{in} = m R T_H \\ln(r_v) = 0.05 \\times 2.077 \\times 573.15 \\times \\ln(2.5) = 59.52 \\times 0.9163 = 54.54\\text{ kJ}$. Trabajo neto producido: $W_{net} = \\eta \\cdot Q_{in} = 0.4798 \\times 54.54 = 26.17\\text{ kJ}$. Calor almacenado temporalmente en el regenerador de alambre fino de cobre en cada carrera: $Q_{reg} = 0.05 \\times 3.116 \\times (573.15 - 298.15) = 42.84\\text{ kJ}$. Problema 2: En la práctica, motores Stirling solares con discos parabólicos (Dish-Stirling) alcanzan un récord mundial de eficiencia neta de conversión solar a electricidad del $31.25\\%$.",
        "bloque_sugerido": "Motores Stirling 40 min • Cinemática de configuraciones Alpha, Beta y Gamma",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA DEL REGENERADOR",
                "titulo": "La Magia del Regenerador Térmico",
                "puntos": [
                    "Ciclo Stirling: Dos procesos isotermos (adición y rechazo de calor) y dos procesos isócoros regenerativos a volumen constante.",
                    "Ciclo Ericsson: Dos procesos isotermos y dos procesos isobáricos regenerativos a presión constante.",
                    "El regenerador almacena internamente la energía térmica cedida en el enfriamiento y la devuelve al fluido durante el calentamiento, cancelando las irreversibilidades externas."
                ]
            },
            {
                "numero": 2,
                "seccion": "COMBUSTIÓN EXTERNA",
                "titulo": "Flexibilidad Absoluta de Combustibles",
                "puntos": [
                    "El fluido de trabajo (helio o hidrógeno de alta pureza) está sellado herméticamente dentro del motor.",
                    "Puede accionarse con cualquier fuente de calor: biomasa agrícola, pellets, concentración solar, radioisótopos o calor residual industrial.",
                    "Marcha extremadamente silenciosa y libre de explosiones, ideal para submarinos militares (propulsión AIP) y cogeneración doméstica."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Ciclos Brayton Avanzados: Interenfriamiento, Recalentamiento y Regeneración",
        "objetivo": "Optimizar ciclos de turbina de gas mediante compresión escalonada con intercooling, expansión multietapa con reheat y regeneración térmica (recuperador de calor).",
        "concepto_clave_latex": r"r_{p,opt,etapa} = \sqrt{r_{p,total}} \quad ; \quad \varepsilon_{regen} = \frac{h_5 - h_2}{h_4 - h_2} \quad ; \quad w_{net} = (w_{turb,1} + w_{turb,2}) - (w_{comp,1} + w_{comp,2})",
        "ejemplo": "Problema 1: Un ciclo Brayton regenerativo con intercooling y recalentamiento opera con una relación de presión global de $r_p = 16$ entre $T_{min} = 300\\text{ K}$ y $T_{max} = 1400\\text{ K}$. Las etapas de compresión y turbina se dividen en dos con relación de presión intermedia idéntica $r_{p,1} = r_{p,2} = \\sqrt{16} = 4$. Para aire ideal ($k = 1.4$): Temperatura tras primera compresión: $T_2 = 300(4)^{(1.4-1)/1.4} = 300(4)^{0.2857} = 300(1.486) = 445.8\\text{ K}$. El interenfriador enfría el aire de nuevo a $300\\text{ K}$ antes del segundo compresor, reduciendo el trabajo total de compresión en un $18\\%$. En la turbina, el gas se expande de 1400 K hasta $942\\text{ K}$, se recalienta a 1400 K en una segunda cámara y se expande de nuevo, maximizando el trabajo neto específico. El regenerador transfiere calor de los gases de escape calientes al aire comprimido frío, elevando la eficiencia térmica por encima del $52\\%$. Problema 2: En microturbinas de gas (30 a 200 kW), el recuperador es obligatorio para hacerlas económicamente competitivas frente a motores diésel.",
        "bloque_sugerido": "Turbomaquinaria 45 min • Ciclo Ericsson aproximado en turbinas de gas multietapa",
        "slides": [
            {
                "numero": 1,
                "seccion": "MINIMIZACIÓN DEL TRABAJO DE COMPRESIÓN",
                "titulo": "Interenfriamiento (Intercooling)",
                "puntos": [
                    "El trabajo de compresión en flujo estacionario es $w = \\int v dP$. Al enfriar el gas entre etapas intermedias, su volumen específico $v$ se contrae.",
                    "Aproxima la compresión real a una isoterma reversible, consumiendo el mínimo trabajo mecánico posible.",
                    "Requiere agua de enfriamiento o intercambiadores aire-aire compactos."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGENERACIÓN TÉRMICA",
                "titulo": "El Papel del Recuperador",
                "puntos": [
                    "Solo es aplicable si la temperatura de salida de la turbina es estrictamente mayor que la temperatura de salida del compresor ($T_{escape} > T_{comp}$).",
                    "A relaciones de presión muy altas ($r_p > 25$), el aire sale del compresor más caliente que el escape, haciendo inviable la regeneración simple.",
                    "La combinación de intercooling + reheat + regeneración transforma el ciclo Brayton en un ciclo cuasi-Ericsson de altísima eficiencia."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Flujo Compresible Unidimensional en Toberas de Laval y Ondas de Choque",
        "objetivo": "Resolver la dinámica de gases compresibles en toberas convergentes-divergentes de Laval, evaluando la condición de bloqueo sónico ($Ma = 1$) en la garganta y la formación de ondas de choque normales.",
        "concepto_clave_latex": r"\frac{dA}{A} = \frac{dP}{\rho v^2}(1 - Ma^2) \quad ; \quad \frac{T_0}{T} = 1 + \frac{k-1}{2}Ma^2 \quad ; \quad \frac{P_0}{P} = \left(1 + \frac{k-1}{2}Ma^2\right)^{\frac{k}{k-1}}",
        "ejemplo": "Problema 1: Una tobera de vapor de una turbina de impulsión recibe vapor recalentado a $P_0 = 3.0\\text{ MPa}$ y $T_0 = 400^\\circ\\text{C}$ (673.15 K) con velocidad despreciable. Suponiendo $k = 1.30$, calcular la presión crítica en la garganta para lograr flujo sónico ($Ma = 1$): Relación de presión crítica: $\\frac{P^*}{P_0} = \\left( \\frac{2}{k+1} \\right)^{\\frac{k}{k-1}} = \\left( \\frac{2}{2.3} \\right)^{\\frac{1.3}{0.3}} = (0.8696)^{4.333} \\approx 0.5457$. Presión en la garganta: $P^* = 0.5457 \\times 3.0\\text{ MPa} = 1.637\\text{ MPa}$. Temperatura sónica: $T^* = T_0 \\left(\\frac{2}{k+1}\\right) = 673.15 \\times 0.8696 = 585.37\\text{ K} = 312.2^\\circ\\text{C}$. Una vez alcanzado $Ma = 1$ en la garganta, la tobera se encuentra bloqueada acústicamente ('choked flow'); reducciones adicionales en la presión de salida no incrementan el caudal másico $\\dot{m}_{max}$. En la sección divergente el flujo se acelera a velocidades supersónicas ($Ma > 1$). Problema 2: Si la contrapresión exterior es superior a la de diseño supersónico, se genera una onda de choque normal discontinua en el cono divergente que desacelera bruscamente el flujo a subsónico con una severa pérdida irreversible de presión de estancamiento $\\Delta P_0$.",
        "bloque_sugerido": "Dinámica de Gases 45 min • Relaciones de flujo isentrópico y tablas de choque normal",
        "slides": [
            {
                "numero": 1,
                "seccion": "GEOMETRÍA Y NÚMERO DE MACH",
                "titulo": "La Ecuación Fundamental de Hugoniot",
                "puntos": [
                    "Flujo Subsónico ($Ma < 1$): Para acelerar el gas ($dv > 0$), el conducto debe converger ($dA < 0$).",
                    "Flujo Sónico ($Ma = 1$): Ocurre exclusivamente en la sección de área mínima transversal (la garganta).",
                    "Flujo Supersónico ($Ma > 1$): Para continuar acelerando el gas ($dv > 0$), el conducto debe divergir ($dA > 0$)."
                ]
            },
            {
                "numero": 2,
                "seccion": "ONDAS DE CHOQUE NORMALES",
                "titulo": "Discontinuidad Irreversible en Espesor Micrométrico",
                "puntos": [
                    "Frente de onda perpendicular al flujo donde las variables de estado sufren saltos casi discontinuos en una distancia de pocas trayectorias libres medias moleculares.",
                    "El número de Mach colapsa de supersónico ($Ma_1 > 1$) a subsónico ($Ma_2 < 1$).",
                    "La presión estática, temperatura y entropía aumentan bruscamente ($s_2 > s_1$), mientras la presión de estancamiento total cae irreversiblemente ($P_{02} < P_{01}$)."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Termodinámica de Procesos Irreversibles y Relaciones de Reciprocidad de Onsager",
        "objetivo": "Modelar fenómenos acoplados simultáneos de transporte de calor, masa y electricidad fuera del equilibrio termodinámico aplicando las relaciones de simetría de Onsager.",
        "concepto_clave_latex": r"\sigma_s = \sum_{i=1}^n J_i X_i > 0 \quad ; \quad J_i = \sum_{j=1}^n L_{ij} X_j \quad ; \quad L_{ij} = L_{ji} \quad [L_{ij}(\mathbf{B}) = L_{ji}(-\mathbf{B})]",
        "ejemplo": "Problema 1: En una barra semiconductora sometida simultáneamente a un gradiente de temperatura $\\nabla T$ y a un campo eléctrico $\\mathbf{E} = -\\nabla V$, la tasa local de producción de entropía es: $\\sigma_s = \\mathbf{J}_e \\cdot \\left(-\\frac{\\nabla V}{T}\\right) + \\mathbf{J}_q \\cdot \\nabla\\left(\\frac{1}{T}\\right)$. Los flujos acoplados de corriente eléctrica $\\mathbf{J}_e$ y de calor $\\mathbf{J}_q$ se expresan como: $\\mathbf{J}_e = L_{11} X_1 + L_{12} X_2$ y $\\mathbf{J}_q = L_{21} X_1 + L_{22} X_2$. El teorema de reciprocidad de Lars Onsager (Premio Nobel de Química) estipula que los coeficientes cruzados son rigurosamente iguales: $L_{12} = L_{21}$. Esto demuestra matemáticamente la relación fundamental entre el coeficiente Seebeck $S$ (voltaje por gradiente térmico) y el coeficiente Peltier $\\Pi$ (transporte de calor por corriente): $\\Pi = S \\cdot T$. Problema 2: En membranas de desalinización por ósmosis inversa y electrodiálisis, las relaciones de Onsager vinculan simétricamente el flujo osmótico de agua y el flujo electroforético de iones salinos.",
        "bloque_sugerido": "Física Estadística 45 min • Producción de entropía en sistemas continuos y relaciones de Onsager",
        "slides": [
            {
                "numero": 1,
                "seccion": "TERMODINÁMICA FUERA DEL EQUILIBRIO",
                "titulo": "Fuerzas Afines y Flujos Conjugados",
                "puntos": [
                    "La termodinámica clásica describe estados de equilibrio estático; la termodinámica de no equilibrio modela la velocidad finita a la que ocurren los procesos.",
                    "Fuerzas generalizadas ($X_i$): Gradientes espaciales de temperatura, potencial químico, concentración o potencial eléctrico.",
                    "Flujos acoplados ($J_i$): Densidades de flujo térmico, másico o de carga eléctrica."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL TEOREMA DE ONSAGER",
                "titulo": "Reversibilidad Microscópica en el Macrocosmos",
                "puntos": [
                    "Consecuencia directa de la simetría temporal de las ecuaciones de movimiento cuánticas y clásicas a nivel molecular.",
                    "Garantiza que la matriz de coeficientes fenomenológicos $L$ sea simétrica y semidefinida positiva.",
                    "Base unificadora para la termoeléctrica, la termodifusión (efecto Soret/Dufour) y la electrocinética moderna."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_03021817)
    # Inject before the next cuatrimestre marker: cuatrimestre: 5
    inject_topics_after('  - cuatrimestre: 5', yaml_text)
    print("03021817 Termodinámica successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
