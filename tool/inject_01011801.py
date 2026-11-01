# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_9_to_20 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Lógica Proposicional, Silogismos y Falacias en Debates Técnicos",
        "objetivo": "Identificar falacias lógicas (ad hominem, causa falsa, hombre de paja) y validar argumentos mediante tablas de verdad.",
        "concepto_clave_latex": r"(p \to q) \land p \implies q \quad ; \quad \text{Modus Tollens: } (p \to q) \land \neg q \implies \neg p",
        "ejemplo": """CLASE MAGISTRAL: RIGOR LÓGICO Y REFUTACIÓN DE FALACIAS
1. Lógica Formal y Validez Deductiva:
Un argumento técnico es deductivamente válido si es imposible que sus premisas sean verdaderas y su conclusión falsa. Las dos reglas de inferencia fundamentales son Modus Ponens [(p -> q) ^ p => q] y Modus Tollens [(p -> q) ^ ~q => ~p].
2. Taxonomía de Falacias en Políticas Energéticas:
- Falacia de Causa Falsa (Post hoc ergo propter hoc): Confundir correlación temporal con causalidad física.
- Falacia del Hombre de Paja: Distorsionar la postura del oponente técnico para refutar una versión caricaturizada.
- Ad Hominem: Atacar la credibilidad personal del investigador en lugar de evaluar los datos empíricos.
3. Problema Resuelto 1 (Aplicación Directa):
Analice la validez lógica del siguiente argumento presentado en un panel regulatorio:
Premisa 1: Si una microrred cuenta con generación solar y banco de baterías BESS suficiente, mantiene el suministro eléctrico durante apagones del SIN (p -> q).
Premisa 2: La comunidad sufrió un apagón total en sus hogares durante la tormenta (~q).
Conclusión: Por lo tanto, la microrred no contaba con almacenamiento BESS suficiente en ese momento (~p).
Solución:
Estructura formal:
Premisa 1: p -> q
Premisa 2: ~q
Conclusión: ~p
Esta estructura corresponde exactamente a la regla de inferencia Modus Tollens.
Construcción de tabla de verdad:
En la única fila donde (p -> q) es V y (~q) es V (cuando p=F y q=F), la conclusión ~p es necesariamente Verdadera.
Por lo tanto, la inferencia es lógicamente válida.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique y desmonte formalmente la falacia en la afirmación: 'Desde que se instaló el parque eólico en el municipio costero en marzo, la precipitación en abril y mayo cayó un 40%; por ende, los aerogeneradores ahuyentan las nubes de lluvia'.
Solución:
1. Identificación: Falacia de Falsa Causa (Post hoc ergo propter hoc). Se asume causalidad física basándose únicamente en la precedencia temporal de dos eventos.
2. Desmontaje Técnico y Evidencia Científica:
La precipitación atmosférica se rige por la dinámica termodinámica de mesoescala (frentes tropicales, Zona de Convergencia Intertropical ZCIT, ciclos de El Niño/La Niña). Los rotores eólicos operan en la capa límite superficial (0 a 150 m) y carecen de la energía cinética o el gradiente térmico necesario para disipar nubes cumulonimbus situadas a 2,000 - 10,000 m de altitud. Se refuta demostrando que el déficit de lluvias fue regional y se explica por la oscilación estacional del Niño registrada por el IDEAM.""",
        "bloque_sugerido": "Taller 45 min • Detección de falacias y validación formal de argumentos",
        "slides": [
            {"numero": 1, "seccion": "LÓGICA", "titulo": "Reglas de Inferencia Válidas", "puntos": ["Modus Ponens y Modus Tollens como pilares del razonamiento deductivo.", "Distinción entre verdad fáctica de las premisas y validez lógica formal."]},
            {"numero": 2, "seccion": "FALACIAS", "titulo": "Falacias Informales en Energía", "puntos": ["Post hoc ergo propter hoc: correlación no implica causalidad física.", "Hombre de paja y ataque ad hominem en debates socioambientales."]}
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Análisis de Artículos Científicos de Alto Impacto (Estructura IMRyD)",
        "objetivo": "Descomponer y evaluar críticamente artículos científicos indexados según la estructura IMRyD.",
        "concepto_clave_latex": r"\text{IMRyD: } \text{Introducción} \to \text{Metodología} \to \text{Resultados} \to \text{Discusión}",
        "ejemplo": """CLASE MAGISTRAL: ESTRUCTURA Y LECTURA CRÍTICA DE PAPERS (IMRyD)
1. El Estándar IMRyD en Revistas Q1/Q2 (IEEE, Elsevier, Springer):
- Introducción: ¿Qué problema se aborda y cuál es la brecha de conocimiento en el estado del arte?
- Metodología: ¿Cómo se investigó el problema? Detalle suficiente para permitir la replicabilidad experimental exacta.
- Resultados: ¿Qué hallazgos empíricos y cuantitativos se obtuvieron? (Datos objetivos sin interpretación subjetiva).
- Discusión: ¿Qué significan los resultados a la luz de teorías previas? Limitaciones y trabajos futuros.
2. El Embudo Retórico de Swales (CARS Model):
La introducción transita de lo general a lo particular: Establecer el territorio -> Identificar el nicho o vacante -> Ocupar el nicho con la propuesta actual.
3. Problema Resuelto 1 (Aplicación Directa):
Al auditar la sección de Metodología de un artículo sobre degradación de paneles solares fotovoltaicos, identifique los 4 elementos metodológicos indispensables que garantizan su reproducibilidad científica.
Solución:
1. Caracterización del espécimen: Tecnología de celdas (monocristalino PERC), fabricante, potencia nominal, dimensiones y lote.
2. Condiciones de contorno y entorno: Temperatura controlada, simulador solar clase AAA (IEC 60904-9), espectro AM 1.5G e irradiancia calibrada con celda patrón certificada.
3. Protocolo de medición e instrumentación: Trazador de curvas I-V con precisión nominal, número de repeticiones y tiempo de exposición.
4. Análisis estadístico de incertidumbre: Intervalos de confianza al 95%, propagación de errores sistemáticos y prueba de repetibilidad.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Diferencie epistemológicamente entre la sección de Resultados y la sección de Discusión en un paper que reporta una eficiencia experimental del 22.4% para una celda de perovskita-silicio en tándem.
Solución:
- En Resultados: Se reporta el dato crudo y sintetizado: 'La curva I-V arrojó V_oc = 1.78 V, J_sc = 16.2 mA/cm^2, FF = 0.778, resultando en una eficiencia de conversión PCE = 22.4% +- 0.3% bajo STC'. No se especula sobre las causas ni se compara con la literatura.
- En Discusión: Se contextualiza el significado: 'El 22.4% obtenido supera en 1.8 puntos porcentuales el récord previo de Smith et al. (2024), atribuible a la pasivación interfacial con fluoruro. Sin embargo, la celda retuvo sólo el 85% de su eficiencia tras 200 horas de humedad relativa del 60%, lo que evidencia que la estabilidad hidrofóbica sigue siendo una barrera crítica antes del escalado comercial'.""",
        "bloque_sugerido": "Lectura Activa 50 min • Deconstrucción de un paper Q1 de IEEE Transactions",
        "slides": [
            {"numero": 1, "seccion": "IMRYD", "titulo": "Arquitectura del Artículo Científico", "puntos": ["Estructura canónica internacional: Introducción, Metodología, Resultados y Discusión.", "Flujo lógico desde la pregunta de investigación hasta la respuesta empírica."]},
            {"numero": 2, "seccion": "REPLICABILIDAD", "titulo": "Metodología vs Discusión", "puntos": ["Metodología transparente para permitir la repetición del experimento en cualquier laboratorio.", "Discusión crítica reconociendo limitaciones y comparando con el estado del arte."]}
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "La Definición Operacional y el Léxico Especializado en Ingeniería",
        "objetivo": "Formular definiciones operacionales rigurosas erradicando la ambigüedad, la vaguedad y la polisemia en documentos técnicos.",
        "concepto_clave_latex": r"\text{Definición}(X) = \text{Género Próximo} + \text{Diferencia Específica} \quad ; \quad \text{Ambigüedad} = 0",
        "ejemplo": """CLASE MAGISTRAL: PRECISIÓN LÉXICA Y DEFINICIONES OPERACIONALES
1. La Regla Clásica de Aristóteles:
Una definición técnica precisa se construye mediante el Género Próximo (clase general superior a la que pertenece el concepto) y la Diferencia Específica (propiedad distintiva que lo separa de todos los demás miembros de la misma clase).
2. Definición Operacional:
Define una variable no de forma abstracta, sino mediante el procedimiento experimental exacto utilizado para medirla o cuantificarla (ej. no decir 'alta temperatura', sino 'temperatura de bulbo seco superior a 35 °C medida con termocupla tipo K').
3. Problema Resuelto 1 (Aplicación Directa):
Construya la definición técnica formal de 'Inversor Solar Centralizado' utilizando la regla de Género Próximo y Diferencia Específica.
Solución:
- Concepto a definir: Inversor solar centralizado.
- Género Próximo: Convertidor estático de potencia electrónica.
- Diferencia Específica: Que transforma la corriente continua (DC) generada por múltiples ramales fotovoltaicos conectados en paralelo en corriente alterna (AC) trifásica a media tensión para inyección directa a la red eléctrica.
Definición completa: 'Un inversor solar centralizado es un convertidor estático de potencia electrónica que transforma la corriente continua (DC) generada por múltiples ramales fotovoltaicos en corriente alterna (AC) trifásica sincronizada para inyección directa a la red eléctrica'.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique los defectos de ambigüedad y vaguedad en la siguiente cláusula contractual de una licitación: 'El contratista instalará cables de buena calidad y suficientes protecciones eléctricas para garantizar que el sistema no falle a menudo', y reescríbala bajo un estándar operacional riguroso.
Solución:
Defectos identificados:
1. 'Buena calidad': Término valorativo vago; carece de norma técnica de referencia.
2. 'Suficientes protecciones': Ambigüedad cuantitativa; no especifica tipo, curva de disparo ni coordinación.
3. 'No falle a menudo': Imprecisión inaceptable; no fija una tasa de indisponibilidad medible.
Reescritura operacional rigurosa:
'El contratista instalará conductores de cobre electrolítico libre de oxígeno con aislamiento XLPE de 90 °C bajo norma técnica NTC 2050 / UL 44. El sistema incorporará interruptores termomagnéticos en caja moldeada y descargadores de sobretensión transitoria DPS Tipo 1+2 coordinados bajo IEC 61643-11, garantizando una disponibilidad operativa auditada superior al 99.5% anual (SAIDI < 43 horas/año)'.""",
        "bloque_sugerido": "Taller 45 min • Redacción de especificaciones técnicas sin ambigüedad",
        "slides": [
            {"numero": 1, "seccion": "DEFINICIÓN", "titulo": "Género Próximo y Diferencia", "puntos": ["Construcción aristotélica para eliminar polisemia en manuales técnicos.", "Eliminación de definiciones circulares y tautológicas en ingeniería."]},
            {"numero": 2, "seccion": "OPERACIONAL", "titulo": "Especificaciones Cuantificables", "puntos": ["Transformación de adjetivos vagos en tolerancias numéricas y normas ISO/IEC.", "Blindaje contractual de pliegos de condiciones y términos de referencia."]}
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Cohesión Textual Avanzada: Anáfora, Catáfora y Marcadores Discursivos",
        "objetivo": "Garantizar la fluidez y conectividad lógica de párrafos técnicos mediante recursos gramaticales de referencia y progresión temática.",
        "concepto_clave_latex": r"\text{Cohesión} = \text{Anáfora} + \text{Catáfora} + \text{Conectores Lógicos} \quad ; \quad \text{Flujo Continuo}",
        "ejemplo": """CLASE MAGISTRAL: MECANISMOS DE COHESIÓN Y CONECTIVIDAD
1. Cohesión vs Coherencia:
La coherencia es el plano semántico global (unidad de sentido e inteligibilidad del tema central). La cohesión es el plano gramatical y léxico explícito (los puentes y conectores superficiales que unen oraciones y párrafos entre sí).
2. Mecanismos Referenciales:
- Anáfora: Remite a un elemento mencionado previamente en el texto (ej. 'La turbina Francis fue inspeccionada; esta presentó cavitación en el rodete').
- Catáfora: Anticipa un elemento que se enunciará a continuación (ej. 'Se evaluaron los siguientes componentes: transformadores, disyuntores y seccionadores').
- Deixis y Elipsis: Evitan la repetición cacofónica de sustantivos técnicos idénticos.
3. Problema Resuelto 1 (Aplicación Directa):
Mejore la cohesión del siguiente fragmento inconexo utilizando anáforas y conectores de causa y contraste:
'Los paneles solares generan corriente continua. La corriente continua no puede entrar a la red nacional. El inversor transforma la corriente en corriente alterna. La temperatura sube mucho a mediodía. La eficiencia del panel solar cae.'
Solución:
Texto reescrito con cohesión técnica:
'Los módulos solares generan corriente continua; sin embargo, esta no puede inyectarse directamente a la red nacional. Por esta razón, se requiere un inversor de potencia que la transforme en corriente alterna trifásica sincronizada. Por otro lado, cuando la temperatura de operación se eleva durante el mediodía, la eficiencia de conversión de dichos dispositivos se reduce debido al coeficiente térmico negativo del semiconductor'.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Clasifique los siguientes marcadores discursivos según su función retórica en un informe técnico: 'por consiguiente', 'no obstante', 'en primer lugar', 'es decir', 'en efecto', y redacte un párrafo que integre al menos tres de ellos demostrando progresión temática lineal.
Solución:
Clasificación:
1. 'Por consiguiente': Conector consecutivo / causal.
2. 'No obstante': Conector adversativo / contraargumentativo.
3. 'En primer lugar': Ordenador / estructurador de la información.
4. 'Es decir': Marcador reformulador / explicativo.
5. 'En efecto': Conector confirmativo / probatorio.
Párrafo integrado:
'En primer lugar, los generadores síncronos aportan inercia física a la red mediante la masa rotatoria de sus rotores. No obstante, las centrales solares fotovoltaicas carecen de piezas móviles y entregan potencia a través de inversores estáticos; es decir, no suministran inercia intrínseca al sistema interconectado. Por consiguiente, ante una contingencia de pérdida súbita de generación, la tasa de cambio de frecuencia (RoCoF) se incrementa de forma peligrosa si no se implementan controles de inercia sintética'.""",
        "bloque_sugerido": "Escritura 45 min • Rediseño de párrafos técnicos y conectores lógicos",
        "slides": [
            {"numero": 1, "seccion": "COHESIÓN", "titulo": "Mecanismos de Referencia", "puntos": ["Anáfora, catáfora y sustitución léxica para erradicar repeticiones.", "Progresión temática: de tema conocido a rema informativo nuevo."]},
            {"numero": 2, "seccion": "CONECTORES", "titulo": "Marcadores del Discurso", "puntos": ["Relaciones lógicas: causalidad, contraste, reformulación y jerarquía.", "Estructuración de párrafos fluidos y densamente informativos."]}
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "La Paráfrasis Rigurosa y la Síntesis Bibliográfica",
        "objetivo": "Sintetizar y parafrasear fuentes científicas complejas manteniendo fidelidad técnica absoluta y atribución autoral.",
        "concepto_clave_latex": r"\text{Paráfrasis} = \text{Idea Original} + \text{Voz Propia} + \text{Cita [Ref]} \quad ; \quad \text{Turnitin} \le 10\%",
        "ejemplo": """CLASE MAGISTRAL: EL ARTE DE LA PARÁFRASIS CIENTÍFICA
1. Citas Textuales vs Paráfrasis en Ingeniería:
En ingeniería y ciencias exactas, las citas textuales directas entre comillas representan menos del 1% del texto y se reservan exclusivamente para definiciones canónicas o leyes. Más del 99% de las revisiones de literatura se construyen mediante paráfrasis: asimilar la idea ajena, reexpresarla con palabras y sintaxis propias, y citar formalmente la fuente.
2. Protocolo de Paráfrasis en Tres Pasos:
- Paso 1 (Comprensión): Leer hasta capturar el núcleo del hallazgo sin mirar el texto original.
- Paso 2 (Reescritura): Redactar la idea combinando conceptos con la propia línea discursiva.
- Paso 3 (Verificación): Comparar con el original para asegurar que no se copiaron frases consecutivas y añadir la cita (ej. [14]).
3. Problema Resuelto 1 (Aplicación Directa):
Dado el texto original: 'El silicio monocristalino presenta una degradación inducida por potencial (PID) que puede mermar hasta el 30% de la potencia del módulo en ambientes cálidos y húmedos si no se polariza adecuadamente el marco metálico a tierra (González, 2023)', elabore una paráfrasis técnica adecuada en estilo IEEE.
Solución:
Paráfrasis rigurosa en estilo IEEE:
De acuerdo con González [1], la omisión de una puesta a tierra apropiada en el bastidor de los módulos monocristalinos expuestos a condiciones tropicales de alta temperatura y humedad favorece el fenómeno PID, provocando mermas de generación de hasta un tercio de su capacidad nominal.
(Se reestructuró la sintaxis, se cambió el orden lógico y se integró la cita numérica [1] sin alterar la veracidad física).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Explique qué es el plagio en mosaico (patchwriting) y demuestre por qué limitarse a cambiar 2 o 3 palabras por sinónimos sigue siendo considerado deshonestidad académica por comités de ética.
Solución:
El plagio en mosaico ocurre cuando el redactor conserva la estructura oracional, el orden de las cláusulas y la secuencia de ideas del autor original, limitándose a reemplazar sustantivos o adjetivos aislados mediante un diccionario de sinónimos.
Esto constituye falta ética porque:
1. No existe un esfuerzo intelectual de digestión, análisis y síntesis por parte del autor.
2. Se apropia de la voz y el estilo argumentativo ajeno haciéndolo pasar por propio.
3. Frecuentemente introduce errores conceptuales graves al sustituir términos técnicos especializados por sinónimos coloquiales inexactos (ej. cambiar 'reactancia' por 'resistencia').
La verdadera paráfrasis exige reformular la arquitectura del pensamiento desde sus fundamentos lógicos.""",
        "bloque_sugerido": "Taller 45 min • Paráfrasis avanzada y prevención de patchwriting",
        "slides": [
            {"numero": 1, "seccion": "PARÁFRASIS", "titulo": "Digestión de Literatura Científica", "puntos": ["Predominio de la síntesis sobre las citas entrecomilladas en ingeniería.", "Asimilación conceptual y reformulación con estilo propio y cita formal."]},
            {"numero": 2, "seccion": "INTEGRIDAD", "titulo": "Riesgos del Patchwriting", "puntos": ["El plagio en mosaico como simulación de escritura original.", "Uso ético de gestores bibliográficos (Zotero, Mendeley) y verificación de similitud."]}
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Normas de Estilo Editorial Técnico: Estándares IEEE",
        "objetivo": "Aplicar rigurosamente el manual de estilo IEEE para formatear tablas, figuras, ecuaciones y referencias.",
        "concepto_clave_latex": r"\text{IEEE: } [1]\; \text{A. Author, ``Title,'' } \textit{Title of Periodical}\text{, vol. x, no. x, pp. xxx, Year.}",
        "ejemplo": """CLASE MAGISTRAL: FORMATO EDITORIAL IEEE PARA ARTÍCULOS TÉCNICOS
1. Estándar Global del Institute of Electrical and Electronics Engineers (IEEE):
Es el formato de publicación por excelencia en ingeniería eléctrica, electrónica y energética. Regula la tipografía a doble columna, el espaciado, la posición de leyendas y el sistema de citación numérica secuencial entre corchetes rectos [1].
2. Reglas Estrictas de Elementos Gráficos y Ecuaciones:
- Figuras: La leyenda se ubica abajo: 'Fig. 1. Curva de potencia horaria...'.
- Tablas: La leyenda se ubica arriba en versalitas / mayúsculas: 'TABLE I / RESUMEN DE PARÁMETROS ELÉCTRICOS'.
- Ecuaciones: Se numeran consecutivamente con números entre paréntesis alineados a la derecha: '(1)'. Las variables deben ir en cursiva ($V$, $I$, $P$) y las unidades en fuente romana estándar (V, A, W).
3. Problema Resuelto 1 (Aplicación Directa):
Formatee correctamente la siguiente referencia bibliográfica en estilo IEEE:
Autores: Juan Carlos Martínez y Diana Marcela Castro. Título: Análisis de estabilidad transitoria en microrredes aisladas. Revista: IEEE Transactions on Power Systems. Volumen: 39. Número: 2. Páginas: 1420-1431. Año: 2024. DOI: 10.1109/TPWRS.2024.1234567.
Solución:
Referencia en formato IEEE estricto:
[1] J. C. Martínez and D. M. Castro, "Análisis de estabilidad transitoria en microrredes aisladas," IEEE Trans. Power Syst., vol. 39, no. 2, pp. 1420-1431, Mar. 2024, doi: 10.1109/TPWRS.2024.1234567.
(Nótese: iniciales del nombre antes del apellido, título entrecomillado, nombre de revista abreviado según norma ISO 4, volumen y número en minúsculas).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique y corrija los 3 errores de formato en el siguiente fragmento de un reporte técnico: 'Como se puede observar en la tabla de abajo (ver Fig. 2), el voltaje V=120v y la potencia P=500w cumplen la ecuación: P = V * I [1]'
Solución:
Errores identificados y correcciones:
1. Llamado cruzado incorrecto: Llamar a una tabla 'Fig. 2' genera contradicción. Debe llamarse 'TABLE II' con leyenda superior.
2. Unidades mal formateadas: '120v' y '500w' están en minúscula y pegadas al número. Debe ser '120 V' y '500 W' con espacio inseparable y mayúscula oficial SI.
3. Formato de ecuación: La ecuación debe estar en su propia línea, con variables en cursiva y con etiqueta numérica entre paréntesis a la derecha:
P = V I (1)
Texto corregido:
'Como se evidencia en la Tabla II, la tensión nominal V = 120 V y la potencia activa P = 500 W satisfacen la relación:
P = V I (1)'.""",
        "bloque_sugerido": "Laboratorio 45 min • Maquetación IEEE en LaTeX / Overleaf",
        "slides": [
            {"numero": 1, "seccion": "IEEE", "titulo": "Manual de Estilo Editorial", "puntos": ["Citación numérica secuencial [1], [2], [3] por orden de aparición.", "Convenciones tipográficas para variables en cursiva y unidades en romana."]},
            {"numero": 2, "seccion": "ELEMENTOS", "titulo": "Tablas, Figuras y Fórmulas", "puntos": ["Leyendas de figuras inferiores (Fig. 1) y de tablas superiores (TABLE I).", "Ecuaciones centradas con numeración consecutiva a la derecha (1)."]}
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Redacción de Procedimientos de Laboratorio y Manuales SOP",
        "objetivo": "Redactar Procedimientos Operativos Estándar (SOP) con imperatividad, precisión secuencial y advertencias de seguridad.",
        "concepto_clave_latex": r"\text{SOP: } \text{Propósito} \to \text{EPP} \to \text{Paso a Paso Secuencial} \to \text{Protocolo de Emergencia}",
        "ejemplo": """CLASE MAGISTRAL: REDACCIÓN DE PROCEDIMIENTOS Y MANUALES OPERATIVOS
1. Estructura de un Procedimiento Operativo Estándar (Standard Operating Procedure - SOP):
Documento técnico normativo obligatorio que describe paso a paso cómo ejecutar una tarea de ingeniería de forma segura, repetible y eficiente sin margen de error humano.
2. Estilo Lingüístico de los Manuales Técnicos:
- Modo imperativo directo o infinitivo impersonal ('Conecte el cable...', 'Verificar el nivel de aislamiento...').
- Estructura estrictamente cronológica y numerada.
- Bloques de seguridad visualmente destacados según severidad: NOTA (información aclaratoria), PRECAUCIÓN (riesgo de daño material al equipo), PELIGRO (riesgo inminente de descarga eléctrica, arco eléctrico o muerte).
3. Problema Resuelto 1 (Aplicación Directa):
Redacte el bloque de advertencia de seguridad para el procedimiento de desenergización y bloqueo (LOTO) de un inversor trifásico de 50 kW antes de intervenir su barra DC.
Solución:
PELIGRO: RIESGO DE DESCARGA ELÉCTRICA Y ARCO POR TENSIÓN RESIDUAL
Antes de abrir el gabinete del inversor:
1. Abra el seccionador AC en el tablero de distribución.
2. Abra el seccionador DC proveniente de las cadenas fotovoltaicas.
3. Aplique candado y tarjeta de seguridad (LOTO) en ambos mandos.
4. ESPERE AL MENOS 10 MINUTOS para permitir la descarga completa de los condensadores electrolíticos internos del bus DC.
5. Verifique la ausencia de tensión con un multímetro categoría CAT IV 1000V antes de tocar cualquier borne de conexión. El incumplimiento de este paso puede causar lesiones graves o electrocución mortal.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique las fallas de redacción procedimental en el siguiente texto: 'Uno agarra la celda solar y la pone debajo de la lámpara prendida, fijándose que no se caliente mucho para que no se dañe, y después mira en la pantalla del computador si marca corriente y anota lo que le parezca más representativo'.
Solución:
Fallas identificadas:
1. Uso coloquial e impreciso de verbos ('uno agarra', 'la pone').
2. Ambigüedad de parámetros ('lámpara prendida', 'no se caliente mucho'): no fija irradiancia ni temperatura máxima.
3. Subjetividad no científica ('anota lo que le parezca más representativo'): destruye la repetibilidad del ensayo.
Reescritura bajo estándar SOP:
'Procedimiento de Ensayo Fotovoltaico:
1. Posicione la celda de prueba en el soporte horizontal del simulador solar a una distancia focal d = 40 cm del colimador óptico.
2. Ajuste la irradiancia a 1000 W/m^2 verificando la lectura con la celda de referencia calibrada.
3. Supervise el sensor térmico superficial PT100; asegure que la temperatura de la celda permanezca en 25 °C +- 1 °C activando el ventilador de refrigeración si T > 26 °C.
4. Inicie el barrido de tensión en el software de control desde V = 0 hasta V = V_oc con un paso de 10 mV.
5. Exporte el archivo de datos tabulado en formato .CSV conteniendo las columnas de Voltaje (V) y Corriente (A)'.""",
        "bloque_sugerido": "Taller 45 min • Elaboración de un manual SOP para laboratorio de potencia",
        "slides": [
            {"numero": 1, "seccion": "SOP", "titulo": "Arquitectura de Procedimientos", "puntos": ["Estructura cronológica numerada orientada a la repetibilidad operativa.", "Lenguaje imperativo e impersonal para eliminar interpretaciones subjetivas."]},
            {"numero": 2, "seccion": "SEGURIDAD", "titulo": "Niveles de Alerta y LOTO", "puntos": ["Diferenciación estandarizada: NOTA, PRECAUCIÓN y PELIGRO.", "Protocolos de bloqueo y etiquetado (Lockout/Tagout) en alta tensión."]}
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "El Artículo de Revisión Bibliográfica (Review Paper) y PRISMA",
        "objetivo": "Diseñar la metodología de búsqueda sistemática y síntesis crítica de un artículo de revisión bajo el protocolo PRISMA.",
        "concepto_clave_latex": r"\text{PRISMA: } \text{Identificación} \to \text{Cribado} \to \text{Elegibilidad} \to \text{Inclusión Final}",
        "ejemplo": """CLASE MAGISTRAL: REVISIONES SISTEMÁTICAS DE LITERATURA
1. Naturaleza del Review Paper:
A diferencia del artículo de investigación original que aporta un dato experimental nuevo, el artículo de revisión mapea, clasifica, compara críticamente y sintetiza el estado del arte sobre una temática emergente (ej. almacenamiento térmico en sales fundidas), identificando vacíos y directrices futuras para la comunidad científica.
2. Declaración PRISMA (Preferred Reporting Items for Systematic Reviews):
Protocolo metodológico transparente que documenta el flujo de selección de fuentes:
- Identificación: Registros encontrados en bases de datos (Scopus, Web of Science, IEEE Xplore) con ecuaciones de búsqueda booleanas.
- Cribado (Screening): Eliminación de duplicados y filtro por título y resumen.
- Elegibilidad: Lectura a texto completo aplicando criterios de inclusión y exclusión explícitos.
- Inclusión: Conjunto final de estudios analizados cualitativa y cuantitativamente.
3. Problema Resuelto 1 (Aplicación Directa):
Diseñe una ecuación de búsqueda booleana avanzada para rastrear en Scopus investigaciones sobre inversores formadores de red (Grid-Forming Inverters) aplicados a microrredes fotovoltaicas entre 2020 y 2025.
Solución:
Ecuación booleana optimizada:
TITLE-ABS-KEY ( ( "grid-forming" OR "GFM" OR "virtual synchronous" ) AND ( "inverter" OR "converter" ) AND ( "photovoltaic" OR "solar" OR "PV" ) AND ( "microgrid" OR "islanded network" ) ) AND PUBYEAR > 2019 AND PUBYEAR < 2026.
(Combina sinónimos con OR dentro de cada categoría conceptual y une los ejes temáticos mediante operadores AND).
4. Problema Resuelto 2 (Nivel Examen Parcial):
En una revisión sistemática, la ecuación inicial arrojó 850 artículos en IEEE Xplore y 620 en Scopus. Tras combinar las bases, se detectaron 310 duplicados. En el cribado por título/resumen se descartaron 890 por no tratar sistemas eléctricos de potencia. En la lectura a texto completo de los restantes, 85 se excluyeron por no incluir validación experimental ni datos de simulación completos. Calcule cuántos artículos superaron cada fase y cuántos conformaron la muestra final de inclusión.
Solución:
1. Total identificado: 850 + 620 = 1470 registros brutos.
2. Registros únicos (post-duplicados): 1470 - 310 = 1160 artículos a cribar.
3. Artículos cribados por título y resumen: Se descartan 890 ==> Quedan para elegibilidad: 1160 - 890 = 270 artículos a texto completo.
4. Elegibilidad: De los 270 evaluados a texto completo, se excluyen 85.
5. Inclusión final: N_final = 270 - 85 = 185 artículos incluidos en la revisión sistemática.
Se construye el diagrama de flujo PRISMA reportando rigurosamente cada cifra.""",
        "bloque_sugerido": "Laboratorio 50 min • Construcción de un diagrama de flujo PRISMA",
        "slides": [
            {"numero": 1, "seccion": "REVIEW", "titulo": "Artículos de Revisión Crítica", "puntos": ["Mapeo sistemático del estado del arte sin sesgo de selección subjetiva.", "Identificación de brechas de investigación y tendencias tecnológicas globales."]},
            {"numero": 2, "seccion": "PRISMA", "titulo": "Protocolo Metodológico PRISMA", "puntos": ["Ecuaciones booleanas de búsqueda avanzada (AND, OR, NOT).", "Flujograma: Identificación, Cribado, Elegibilidad e Inclusión."]}
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Redacción de Propuestas Técnicas y Términos de Referencia (TdR)",
        "objetivo": "Estructurar propuestas de ingeniería con objetivos SMART, entregables claros, presupuesto y cronograma.",
        "concepto_clave_latex": r"\text{SMART: } \text{Específico} + \text{Medible} + \text{Alcanzable} + \text{Relevante} + \text{Temporal}",
        "ejemplo": """CLASE MAGISTRAL: PROPUESTAS TÉCNICAS Y LICITACIONES EN ENERGÍA
1. Estructura de Términos de Referencia (TdR) y Ofertas Técnicas:
Documento que define las necesidades de un cliente o entidad pública para contratar consultorías o proyectos EPC (Engineering, Procurement, Construction). Contiene: Contexto, Objetivos, Alcance, Especificaciones Técnicas, Entregables, Cronograma y Presupuesto.
2. Formulación de Objetivos según Criterio SMART:
Un objetivo técnico deficiente es vago ('Mejorar la calidad de la energía'); un objetivo SMART fija métricas y plazos verificables:
- S (Specific): Reducir la distorsión armónica total de corriente (THD_i).
- M (Measurable): Llevar el THD_i por debajo del 5%.
- A (Achievable): Mediante la instalación de un filtro activo de armónicos de 100 A.
- R (Relevant): Para dar cumplimiento a la resolución CREG 015 y evitar penalizaciones.
- T (Time-bound): En un plazo de ejecución de 60 días calendario.
3. Problema Resuelto 1 (Aplicación Directa):
Redacte el Objetivo General de una propuesta técnica para el diseño de un sistema fotovoltaico en el campus principal de Unimagdalena cumpliendo estrictamente con el estándar SMART.
Solución:
Objetivo General formulado bajo SMART:
'Diseñar e ingenierar un sistema solar fotovoltaico de autogeneración a pequeña escala (AGPE) de 250 kWp sobre las cubiertas del edificio de aulas de la Universidad del Magdalena, que genere al menos 360 MWh anuales para cubrir el 28% de la demanda diurna de la edificación bajo cumplimiento de la norma RETIE y la resolución CREG 174, en un periodo de desarrollo de 4 meses con un presupuesto máximo de inversión de 850 millones de COP'.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique las 3 inconsistencias operativas críticas en el alcance de una propuesta técnica que promete: 'El contratista suministrará 500 paneles solares de 550 Wp, instalará la estructura y el inversor de 100 kW, garantizando que el sistema entregará 275 kW de potencia inyectada constante las 24 horas del día a la red'.
Solución:
Inconsistencias técnicas críticas:
1. Imposibilidad física diurna/nocturna: Prometer potencia solar constante las 24 horas del día sin incluir un banco de baterías BESS masivo es un absurdo físico elemental; la energía solar nocturna es nula.
2. Incompatibilidad de potencias (Clipping severo): La potencia pico en paneles es 500 * 550 Wp = 275 kWp, pero el inversor especificado es de sólo 100 kW. La máxima potencia inyectable está limitada físicamente por la capacidad del inversor a 100 kW; jamás podrá entregar 275 kW a la red (relación DC/AC sobredimensionada en 2.75x sin justificación).
3. Incumplimiento contractual inminente: El contratista enfrentaría demandas por incumplimiento y cobro de pólizas de garantía de cumplimiento al no poder certificar la entrega prometida.""",
        "bloque_sugerido": "Taller 45 min • Elaboración de propuesta técnica y objetivos SMART",
        "slides": [
            {"numero": 1, "seccion": "PROPUESTAS", "titulo": "Estructura de Licitación y TdR", "puntos": ["Estructura: Justificación, Alcance, Entregables, Cronograma y Presupuesto.", "Matriz de responsabilidades y división del trabajo (WBS/EDT)."]},
            {"numero": 2, "seccion": "SMART", "titulo": "Objetivos Técnicos Rigurosos", "puntos": ["Criterio SMART: metas cuantitativas, plazos fijos y normas de referencia.", "Eliminación de promesas técnicamente inviables que violan leyes físicas."]}
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "La Crítica por Pares (Peer Review) y Rúbricas de Evaluación",
        "objetivo": "Ejecutar revisiones académicas rigurosas mediante rúbricas analíticas, retroalimentación constructiva y juicio ético.",
        "concepto_clave_latex": r"\text{Dictamen: } \text{Aceptar} \;|\; \text{Cambios Menores} \;|\; \text{Cambios Mayores} \;|\; \text{Rechazar}",
        "ejemplo": """CLASE MAGISTRAL: EL SISTEMA DE REVISIÓN POR PARES (PEER REVIEW)
1. El Filtro de Calidad de la Ciencia:
La revisión por pares ciega (single-blind o double-blind) es el mecanismo de control que previene la publicación de fraudes, metodologías viciadas o conclusiones sin sustento empírico.
2. Tipología de Dictámenes Editoriales:
- Accept as is: Aprobación sin cambios (extremadamente raro en primera ronda).
- Minor Revision: Ajustes puntuales de redacción, citación o aclaración de figuras.
- Major Revision: Requiere nuevos experimentos, reanálisis estadístico o reformulación del modelo matemático.
- Reject: Errores conceptuales insalvables, falta de novedad técnica o plagio.
3. Problema Resuelto 1 (Aplicación Directa):
Redacte un comentario formal de revisión por pares señalando constructivamente que un artículo carece de análisis de incertidumbre experimental en sus mediciones de temperatura de una turbina de vapor.
Solución:
Comentario del Revisor (Peer Review Comment):
'Revisión Metodológica - Sección 3.2: El manuscrito reporta mediciones de temperatura en los alabes de la turbina con una precisión de tres cifras decimales (ej. T = 542.185 °C). Sin embargo, los autores no especifican el tipo de sensor empleado ni reportan la incertidumbre expandida del sistema de adquisición. Se solicita a los autores:
a) Indicar la clase de tolerancia del sensor según norma IEC 60584.
b) Incorporar las barras de error correspondientes en la Fig. 4 con un nivel de confianza del 95% (k = 2).
c) Discutir cómo esta incertidumbre afecta el cálculo de la eficiencia isentrópica'.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Diseñe una rúbrica analítica de 4 criterios con ponderación porcentual para evaluar un informe final de laboratorio de circuitos eléctricos en primer semestre.
Solución:
Rúbrica Analítica de Evaluación:
1. Rigor Teórico y Modelación Matemática (25%): Planteamiento correcto de leyes de Kirchhoff y ecuaciones nodales con unidades del SI.
2. Metodología Experimental y Replicabilidad (25%): Diagrama esquemático claro, listado de equipos con código de inventario y protocolo de medición detallado.
3. Análisis de Resultados y Discusión de Discrepancias (30%): Comparación cuantitativa entre valores teóricos y experimentales mediante cálculo del error porcentual relativo y justificación física de pérdidas.
4. Cohesión, Formato IEEE y Redacción Técnica (20%): Aplicación de plantilla IEEE, leyendas de figuras y tablas correctas, ortografía impecable y ausencia de lenguaje informal.""",
        "bloque_sugerido": "Simulacro 45 min • Arbitraje ciego de un informe técnico entre pares",
        "slides": [
            {"numero": 1, "seccion": "PEER REVIEW", "titulo": "El Sistema de Arbitraje Científico", "puntos": ["Modalidades: revisión ciega simple, doble ciego y revisión abierta.", "Elaboración de dictámenes editoriales objetivos y constructivos."]},
            {"numero": 2, "seccion": "RÚBRICAS", "titulo": "Evaluación Analítica por Criterios", "puntos": ["Desglose por dimensiones: teoría, método, resultados y comunicación.", "Eliminación de la subjetividad en la calificación docente y profesional."]}
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Corrección de Estilo en Ingeniería: Supresión de Vicios del Lenguaje",
        "objetivo": "Depurar textos técnicos eliminando queísmos, dequeísmos, redundancias, pleonasmos y abuso de la voz pasiva.",
        "concepto_clave_latex": r"\text{Índice de Niebla (Gunning Fog)} = 0.4 \left[ \left(\frac{\text{palabras}}{\text{frases}}\right) + 100 \left(\frac{\text{palabras complejas}}{\text{palabras}}\right) \right]",
        "ejemplo": """CLASE MAGISTRAL: HIGIENE DISCURSIVA Y CORRECCIÓN DE ESTILO
1. Vicios Gramaticales Frecuentes en Ingeniería:
- Pleonasmos técnicos: 'subir hacia arriba', 'experimento empírico', 'período de tiempo', 'resultado final'.
- Queísmo / Dequeísmo: Omitir o agregar la preposición 'de' antes de 'que' erróneamente ('estoy seguro que' en lugar de 'estoy seguro de que'; o 'pienso de que' en lugar de 'pienso que').
- Gerundio de posterioridad: Usar gerundio para acciones posteriores al verbo principal ('La turbina colapsó, fracturándose después el eje' -> incorrecto; debe ser 'La turbina colapsó y posteriormente el eje se fracturó').
2. Concisión y Densidad Informativa:
El estilo técnico prefiere la voz activa y oraciones con longitud media de 15 a 22 palabras para mantener la legibilidad y evitar sobrecargar la memoria de trabajo del lector.
3. Problema Resuelto 1 (Aplicación Directa):
Depure la siguiente oración repleta de pleonasmos y gerundio incorrecto: 'En el presente trabajo actual se procedió a realizar un análisis previo de antemano de la red, obteniendo como consecuencia un fallo'.
Solución:
Identificación de vicios:
1. 'presente trabajo actual': Pleonasmo (presente = actual).
2. 'se procedió a realizar un análisis': Circunloquio hinchado (basta con 'se analizó').
3. 'previo de antemano': Pleonasmo redundante.
4. 'obteniendo como consecuencia': Gerundio de consecuencia defectuoso.
Reescritura depurada y elegante:
'En este trabajo se analizó previamente la red eléctrica y se identificó la causa de la falla'.
(De 23 palabras redundantes se redujo a 14 palabras exactas y contundentes).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Aplique la prueba de sustitución ('de eso' / 'eso') para corregir rigurosamente las siguientes dos expresiones: a) 'El operador técnico se percató que el transformador estaba sobrecalentado'; b) 'El informe sostiene de que la transición energética es viable'.
Solución:
Prueba de sustitución:
Caso a: Se formula la pregunta: ¿De qué se percató el operador? -> Respuesta: El operador se percató DE ESO. La presencia de la preposición 'de' es obligatoria tras el verbo pronominal 'percatarse de'.
Forma correcta: 'El operador técnico se percató DE QUE el transformador estaba sobrecalentado' (la original sufría de queísmo).
Caso b: Se formula la pregunta: ¿Qué sostiene el informe? -> Respuesta: El informe sostiene ESO (no 'sostiene de eso'). El verbo 'sostener' es transitivo directo y no admite 'de'.
Forma correcta: 'El informe sostiene QUE la transición energética es viable' (la original sufría de dequeísmo).""",
        "bloque_sugerido": "Taller 45 min • Corrección de estilo y pruebas de sustitución gramatical",
        "slides": [
            {"numero": 1, "seccion": "ESTILO", "titulo": "Vicios Comunes del Lenguaje", "puntos": ["Supresión radical de pleonasmos, queísmos y dequeísmos.", "Prohibición del gerundio de posterioridad en informes técnicos."]},
            {"numero": 2, "seccion": "CONCISIÓN", "titulo": "Densidad Informativa y Fog Index", "puntos": ["Eliminación de circunloquios vacíos ('se procedió a realizar').", "Estructuración de oraciones directas con sujeto, verbo y predicado."]}
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Visualización de Datos como Discurso Retórico en Ingeniería",
        "objetivo": "Diseñar gráficos técnicos informativos eliminando el 'chartjunk' y maximizando la relación Data-Ink de Tufte.",
        "concepto_clave_latex": r"\text{Data-Ink Ratio} = \frac{\text{Tinta dedicada a los datos}}{\text{Tinta total utilizada en el gráfico}} \to 1.0",
        "ejemplo": """CLASE MAGISTRAL: DISEÑO DE GRÁFICOS Y RETÓRICA VISUAL (EDWARD TUFTE)
1. Principios de Visualización Científica de Edward Tufte:
- Data-Ink Ratio: Toda línea, sombreado o color que no represente directamente datos numéricos es ruido visual residual ('chartjunk') que debe eliminarse.
- Factor de Distorsión (Lie Factor): Mide la honestidad de la visualización. Si el tamaño del efecto gráfico exagera la variación real de los números, el gráfico miente al lector:
Lie Factor = (Variación porcentual en el gráfico) / (Variación porcentual en los datos).
Un Lie Factor entre 0.95 y 1.05 es éticamente aceptable.
2. Buenas Prácticas en Figuras de Ingeniería:
- Ejes acotados con unidades del SI explícitas entre corchetes (ej. 'Potencia [kW]').
- No cortar el eje Y arbitrariamente para magnificar pequeñas variaciones sin advertirlo.
- Prohibición estricta de gráficos 3D decorativos en gráficos de torta o barras.
3. Problema Resuelto 1 (Aplicación Directa):
Un gráfico de barras en un informe de prensa muestra que la producción solar aumentó de 100 GWh a 120 GWh (+20%). Sin embargo, para exagerar el logro, el diseñador inició el eje Y en 90 GWh, haciendo que la barra de 120 GWh parezca el triple de alta que la de 100 GWh (+200% de tamaño gráfico). Calcule el Lie Factor y dictamine si el gráfico es ético.
Solución:
Variación real en los datos: delta_datos% = (120 - 100) / 100 = +20%.
Variación gráfica aparente:
Altura barra 1: 100 - 90 = 10 unidades.
Altura barra 2: 120 - 90 = 30 unidades.
delta_grafico% = (30 - 10) / 10 = +200%.
Lie Factor = delta_grafico% / delta_datos% = 200% / 20% = 10.0.
Dictamen ético: Un Lie Factor de 10.0 representa una distorsión visual del 1000%, constituyendo manipulación gráfica inaceptable según los estándares de integridad científica.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Indique cómo optimizar un gráfico de radiación solar de 24 horas aplicando el principio de Data-Ink Ratio para publicación en revista IEEE.
Solución:
1. Eliminar rejillas de fondo gruesas y oscuras: reemplazarlas por líneas grises muy tenues (alpha = 0.3) o eliminarlas por completo.
2. Suprimir fondos grises o coloreados en el marco del gráfico: dejar lienzo en blanco puro.
3. Eliminar bordes pesados de la caja: conservar únicamente los ejes X e Y con marcas de graduación externas.
4. Etiquetado directo de curvas: en lugar de forzar al lector a desviar la mirada a una caja de leyendas separada, rotular la línea directamente ('Radiación Directa', 'Radiación Difusa') cerca de la serie.
5. El Data-Ink Ratio se maximiza aproximándose a 1.0, concentrando la atención del lector en la física del fenómeno.""",
        "bloque_sugerido": "Laboratorio 45 min • Rediseño de gráficos y cálculo del Lie Factor",
        "slides": [
            {"numero": 1, "seccion": "TUFTE", "titulo": "Data-Ink Ratio y Chartjunk", "puntos": ["Eliminación de adornos 3D y elementos decorativos sin valor informativo.", "Toda tinta del gráfico debe representar variación cuantitativa de datos."]},
            {"numero": 2, "seccion": "ÉTICA VISUAL", "titulo": "Lie Factor y Distorsión", "puntos": ["Fórmula de Edward Tufte para medir honestidad en visualización de datos.", "Rango admisible 0.95 <= Lie Factor <= 1.05 para informes profesionales."]}
        ]
    }
]

topics_21_to_30 = [
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "El Discurso de Elevador (Elevator Pitch) para Proyectos Energéticos",
        "objetivo": "Sintetizar propuestas técnicas y de innovación en discursos persuasivos de 90 segundos con estructura Hook-Problem-Solution-Call.",
        "concepto_clave_latex": r"\text{Pitch: } \text{Gancho (15s)} \to \text{Dolor (25s)} \to \text{Solución Tecnológica (35s)} \to \text{CTA (15s)}",
        "ejemplo": """CLASE MAGISTRAL: COMUNICACIÓN DE IMPACTO RÁPIDO (ELEVATOR PITCH)
1. Estructura Retórica de 90 Segundos:
En rondas de inversión, concursos de innovación o encuentros con tomadores de decisiones, el ingeniero dispone de escasos segundos para captar la atención:
- Gancho (Hook - 0 a 15 s): Dato impactante o pregunta provocadora que rompe la apatía.
- Problema / Dolor (Pain - 15 a 40 s): Magnitud del costo económico o ambiental actual no resuelto.
- Solución Propuesta (Value Prop - 40 a 75 s): Cómo la tecnología desarrollada soluciona el dolor de forma medible y superior a alternativas.
- Llamado a la Acción (Call to Action - 75 a 90 s): Petición concreta (reunión técnica, financiamiento piloto, acceso a datos).
2. Problema Resuelto 1 (Aplicación Directa):
Redacte un Elevator Pitch de 90 segundos para presentar un software de predicción de radiación solar basado en IA desarrollado en Unimagdalena ante inversionistas de parques solares.
Solución:
Discurso estructurado (180 palabras, ~85 segundos):
[Gancho - 15s] ¿Sabía usted que las penalizaciones por desvíos de generación en el mercado eléctrico colombiano le costaron a los parques solares más de 40 mil millones de pesos el último año?
[Problema - 25s] La variabilidad de las nubes en el Caribe hace que los modelos meteorológicos tradicionales fallen hasta en un 35% en sus pronósticos intradiarios, obligando a los operadores a pagar costosas desviaciones en la bolsa de energía de XM.
[Solución - 35s] En la Universidad del Magdalena desarrollamos Heliodata-AI: un algoritmo que combina imágenes satelitales en tiempo real y redes neuronales LSTM, reduciendo el error de predicción horario a menos del 8%. Esto significa un ahorro directo comprobado de 180 millones de pesos al año para una planta solar de 10 megavatios.
[Llamado a la Acción - 15s] Tenemos el prototipo validado con datos reales. Los invito a reunirnos este jueves por 20 minutos para coordinar un piloto gratuito de 30 días en uno de sus alimentadores. Muchas gracias.
3. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique las 3 fallas que arruinan la efectividad de un pitch cuando un ingeniero comete el error de hablar exclusivamente de ecuaciones internas y jerga de programación frente a gerentes de inversión.
Solución:
Fallas analizadas:
1. Desconexión con la propuesta de valor: Los inversionistas buscan entender el retorno sobre la inversión (ROI), la reducción de costos y la escalabilidad del negocio, no las líneas de código de PyTorch.
2. Fatiga cognitiva inmediata: Saturar con detalles de bajo nivel en 90 segundos aturde a la audiencia e impide retener el mensaje central.
3. Ausencia de llamado a la acción (CTA): Cerrar con un vago 'y eso es todo lo que hace mi modelo' desperdicia la oportunidad; un pitch debe concluir obligatoriamente con una solicitud formal de interacción futura.""",
        "bloque_sugerido": "Práctica Oral 45 min • Grabación y feedback de Elevator Pitch de 90s",
        "slides": [
            {"numero": 1, "seccion": "PITCH", "titulo": "Estructura en Cuatro Actos", "puntos": ["Gancho inicial, dolor del mercado, solución tecnológica y llamado a la acción.", "Control estricto del tiempo: 90 segundos (aprox. 180 a 200 palabras)."]},
            {"numero": 2, "seccion": "PERSUASIÓN", "titulo": "Enfoque en Valor vs Jerga", "puntos": ["Traducción de especificaciones técnicas a beneficios económicos y ambientales.", "Cierre contundente con solicitud de reunión de negocios o piloto técnico."]}
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Negociación Técnica y Debate Académico: Modelo de Toulmin",
        "objetivo": "Defender proyectos y posturas regulatorias estructurando argumentos mediante el Modelo de Toulmin.",
        "concepto_clave_latex": r"\text{Toulmin: } \text{Aserción} \leftarrow \text{Evidencia} \leftarrow \text{Garantía} \leftarrow \text{Respaldo} \leftarrow \text{Reserva}",
        "ejemplo": """CLASE MAGISTRAL: ARGUMENTACIÓN AVANZADA Y MODELO DE TOULMIN
1. Los 6 Elementos del Modelo de Stephen Toulmin:
- Aserción (Claim): La tesis o conclusión que se defiende.
- Evidencia (Data/Grounds): Hechos empíricos, datos estadísticos y mediciones objetivas.
- Garantía (Warrant): Principio lógico, ley física o teorema que conecta la evidencia con la aserción.
- Respaldo (Backing): Normas técnicas, papers indexados o códigos que avalan la garantía.
- Calificador Modal (Qualifier): Grado de certeza o probabilidad de la conclusión ('probablemente', 'con un 95% de confianza').
- Reserva (Rebuttal): Excepciones o condiciones de contorno bajo las cuales la aserción no se cumple.
2. Problema Resuelto 1 (Aplicación Directa):
Estructure un argumento completo bajo el modelo de Toulmin para defender la instalación de un banco de baterías BESS en una subestación de distribución con alta penetración solar.
Solución:
1. Aserción: La subestación Libertador debe instalar un sistema BESS de 5 MW / 10 MWh.
2. Evidencia: Las mediciones horarias de XM muestran que el voltaje en la barra de 13.2 kV supera en un 8.5% el límite máximo de la CREG entre las 11:00 y las 13:00 debido al flujo inverso de potencia de 15 MWp de techos solares.
3. Garantía: El almacenamiento electroquímico absorbe la sobreproducción en horas pico diurnas y reduce el flujo inverso, estabilizando la tensión según las ecuaciones de flujo de potencia.
4. Respaldo: Resolución CREG 015 de 2018 sobre calidad de potencia y norma IEEE 1547-2018 para interconexión de recursos distribuidos.
5. Calificador Modal: Con certeza técnica absoluta, logrando una reducción del 100% de los eventos de sobretensión.
6. Reserva: A menos que los operadores de red acuerden curtailment (corte) voluntario remunerado con los autogeneradores.
3. Problema Resuelto 2 (Nivel Examen Parcial):
En un debate técnico sobre energía nuclear vs eólica en Colombia, identifique cómo refutar una reserva del oponente que afirma que 'las baterías son inviables para respaldar la intermitencia eólica debido a su degradación química cíclica'.
Solución:
Estrategia de refutación fundamentada:
1. Concesión parcial: Reconocer la premisa fáctica válida: las baterías de litio sufren degradación cíclica (típicamente 4000 a 6000 ciclos al 80% DoD).
2. Introducción de contragarantía y evidencia complementaria: Demostrar que el respaldo del sistema interconectado no depende exclusivamente de baterías electroquímicas de corta duración, sino de la complementariedad estacional con el parque hidroeléctrico con embalses de regulación plurianual existente en Colombia (firmeza de >12,000 MW), complementado con almacenamiento por bombeo hidráulico y baterías de flujo redox de vanadio (VRFB) con vida útil superior a 20,000 ciclos sin degradación química.
La aserción del oponente colapsa por falso dilema al restringir artificialmente las opciones de almacenamiento.""",
        "bloque_sugerido": "Debate Dirigido 50 min • Controversias regulatorias y Modelo de Toulmin",
        "slides": [
            {"numero": 1, "seccion": "TOULMIN", "titulo": "Componentes del Modelo Argumentativo", "puntos": ["Estructura: Aserción, Evidencia, Garantía, Respaldo, Calificador y Reserva.", "Blindaje contra refutaciones simplistas en comités de expertos."]},
            {"numero": 2, "seccion": "DEBATE", "titulo": "Negociación y Refutación Técnica", "puntos": ["Manejo solvente de contraargumentos y excepciones de reserva.", "Sustento en leyes físicas y regulaciones oficiales del sector."]}
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Comunicación Intercultural y Trabajo Multidisciplinar",
        "objetivo": "Gestionar la comunicación en consorcios internacionales y concertaciones previas con comunidades étnicas locales.",
        "concepto_clave_latex": r"\text{Consenso} = \text{Diálogo Intercultural} \cap \text{Rigor Técnico} \cap \text{Licencia Social}",
        "ejemplo": """CLASE MAGISTRAL: COMUNICACIÓN TERRITORIAL Y MULTIDISCIPLINAR
1. Desafíos de Comunicación en Proyectos Renovables:
Un proyecto de generación eólica o solar en La Guajira o el Magdalena involucra tres actores con lenguajes y cosmovisiones dispares:
- El consorcio financiero y tecnológico internacional (inversionistas, EPCs alemanes o chinos).
- La institucionalidad regulatoria nacional (Ministerio de Minas, UPME, CREG, ANLA).
- Las comunidades étnicas y campesinas locales (pueblos Wayuu, Kogui, Arhuaco).
2. Consulta Previa y Licencia Social para Operar:
El fracaso de múltiples parques eólicos en el Caribe no ha sido técnico ni financiero, sino comunicativo: incapacidad de construir confianza, respetar autoridades tradicionales y acordar compensaciones justas en el marco de la consulta previa (Convenio 169 de la OIT).
3. Problema Resuelto 1 (Aplicación Directa):
Diseñe una estrategia de comunicación para explicar el funcionamiento y trazado de una línea de evacuación de 110 kV a una comunidad de pescadores sin usar jerga eléctrica incomprensible.
Solución:
Estrategia comunicativa intercultural:
1. Analogía contextualizada: En lugar de hablar de 'amperios, kilovoltios y campos electromagnéticos ionizantes', comparar la línea con una autopista de transporte de agua: la alta tensión es como aumentar la presión para llevar agua a larga distancia en tubos delgados sin que se caliente ni se pierda.
2. Evidencia física y disipación de temores: Demostrar con mediciones en vivo mediante medidores de campo electromagnético calibrados que el campo a nivel de suelo debajo de los conductores está muy por debajo de los límites internacionales ICNIRP y es incapaz de dañar la fauna marina ni las redes de pesca.
3. Traducción y voceros comunitarios: Trabajar con líderes locales bilingües y maquetas físicas tridimensionales a escala.
4. Problema Resuelto 2 (Nivel Examen Parcial):
En un equipo multidisciplinar integrado por ingenieros electricistas, economistas, biólogos ambientales y sociólogos, analice cómo resolver un desacuerdo sobre la ubicación de una subestación solar adyacente a un humedal.
Solución:
Procedimiento de mediación técnica multidisciplinar:
1. Matriz de Criterios Ponderados (AHP - Analytic Hierarchy Process): Asignar pesos objetivos a cada dimensión (Técnica: pérdidas eléctricas; Ambiental: impacto en avifauna y ronda hídrica; Económica: costo de cableado; Social: afectación a pastoreo).
2. Búsqueda de soluciones de compromiso ganar-ganar: Evaluar el desplazamiento de la subestación 300 metros hacia terreno degradado y compensar la caída de tensión aumentando el calibre de los conductores de aluminio de 240 mm^2 a 300 mm^2. El incremento marginal de CAPEX (+4%) se compensa plenamente con la eliminación del riesgo de litigio ambiental y la obtención pacífica de la licencia ANLA.""",
        "bloque_sugerido": "Mesa de Concertación 45 min • Simulación de consulta previa comunitaria",
        "slides": [
            {"numero": 1, "seccion": "TERRITORIO", "titulo": "Consulta Previa y Licencia Social", "puntos": ["Convenio 169 OIT y diálogo genuino con autoridades tradicionales.", "Superación de la soberbia tecnocrática en proyectos de infraestructura energética."]},
            {"numero": 2, "seccion": "EQUIPOS", "titulo": "Coordinación Multidisciplinar", "puntos": ["Articulación entre ingeniería eléctrica, ecología, economía y derecho.", "Matrices multicriterio para resolución negociada de conflictos de trazado."]}
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "La Presentación en Congresos Científicos y Ponencias Magistrales",
        "objetivo": "Exponer investigaciones ante auditorios de especialistas dominando el tiempo, transiciones retóricas y sesiones de preguntas.",
        "concepto_clave_latex": r"T_{\text{charla}} = 15\text{ min} \pm 30\text{ s} \quad ; \quad N_{\text{slides}} \le 12 \quad ; \quad \text{Q\&A} = 5\text{ min}",
        "ejemplo": """CLASE MAGISTRAL: PRESENTACIONES ORALES EN CONGRESOS (IEEE STYLE)
1. El Estándar de Conferencia Internacional:
En congresos de ingeniería (ej. IEEE PES General Meeting), el tiempo es riguroso e inflexible: típicamente 12 a 15 minutos de ponencia seguidos de 3 a 5 minutos de preguntas. El moderador corta el micrófono al ponente si excede el tiempo asignado.
2. Regla de Oro de Diapositivas:
Máximo 1 diapositiva por cada 1.5 minutos de exposición (10 a 12 diapositivas para 15 minutos). Nunca leer el texto de la pantalla: el orador debe mirar al público el 90% del tiempo.
3. Problema Resuelto 1 (Aplicación Directa):
Diseñe la distribución temporal segundo a segundo para una ponencia de 12 minutos sobre un modelo de control de microrredes.
Solución:
Cronograma de la ponencia:
1. Minuto 0:00 - 1:30 (1.5 min): Portada, contexto del problema y motivación.
2. Minuto 1:30 - 3:00 (1.5 min): Limitaciones del estado del arte actual y contribución original del trabajo.
3. Minuto 3:00 - 6:30 (3.5 min): Metodología, formulación matemática y topología del sistema simulado/experimental.
4. Minuto 6:30 - 10:00 (3.5 min): Resultados clave, curvas de respuesta dinámica y comparación cuantitativa de métricas.
5. Minuto 10:00 - 11:30 (1.5 min): Conclusiones principales y líneas de trabajo futuro.
6. Minuto 11:30 - 12:00 (0.5 min): Agradecimientos, fuentes de financiación y apertura de preguntas.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un experto en la audiencia formula una pregunta agresiva: 'Su modelo de control asume inversores ideales con fuentes de tensión perfectas, lo cual es totalmente irreal en redes reales con armónicos. ¿No invalida esto todas sus conclusiones?' Redacte una respuesta diplomática, solvente y rigurosa.
Solución:
Respuesta modelo (Técnica de Agradecimiento + Delimitación de Alcance + Validación Futura):
'Agradezco profundamente la observación del colega, pues apunta a un desafío crítico en la integración práctica.
En efecto, en esta primera fase de la investigación se implementó un modelo promediado de inversor para aislar la dinámica de estabilidad de frecuencia a nivel de despacho primario, validando el algoritmo de optimización central sin el costo computacional de la conmutación PWM de alta frecuencia.
Sin embargo, concuerdo plenamente en que la distorsión armónica no lineal es fundamental; por ello, en la Sección 5.3 del paper reportamos que ya estamos corriendo simulaciones electromagnéticas detalladas en PSCAD incluyendo conmutación a 10 kHz y filtros LCL, y los resultados preliminares confirman que el tiempo de estabilización se preserva dentro de una ventana de 250 milisegundos con un THD menor al 4.2%. Con gusto podemos profundizar en los datos al finalizar la sesión'.""",
        "bloque_sugerido": "Simulacro 45 min • Exposición con cronómetro estricto de 12 min y ronda Q&A",
        "slides": [
            {"numero": 1, "seccion": "CONGRESOS", "titulo": "Protocolo de Ponencias IEEE", "puntos": ["Gestión inflexible del tiempo: 12 a 15 minutos cronometrados.", "Ritmo de diapositivas: 1 slide por cada 1.5 minutos de exposición."]},
            {"numero": 2, "seccion": "Q&A", "titulo": "Gestión de Preguntas Hostiles", "puntos": ["Protocolo diplomático: agradecimiento, delimitación de alcance y rigor técnico.", "Manejo escénico sin perder la serenidad ni la autoridad científica."]}
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "El Póster Científico: Jerarquía Visual y Sustentación Relámpago",
        "objetivo": "Diseñar un póster académico de alta densidad informativa y sustentarlo interactivamente en 3 minutos.",
        "concepto_clave_latex": r"\text{Póster: } 20\%\text{ Texto} + 50\%\text{ Gráficos/Figuras} + 30\%\text{ Espacio Blanco} \quad ; \quad \text{Pitch: } 3\text{ min}",
        "ejemplo": """CLASE MAGISTRAL: COMUNICACIÓN VISUAL MEDIANTE PÓSTER CIENTÍFICO
1. Arquitectura de un Póster Científico (Formato A0: 841 x 1189 mm):
Un póster no es un artículo pegado en una cartulina. Es una herramienta de comunicación gráfica que debe ser legible y comprensible a 2 metros de distancia en menos de 60 segundos.
2. Jerarquía Tipográfica y Composición:
- Título principal: Letra de al menos 72 a 85 pt (visible a 5 metros).
- Encabezados de sección: 36 a 44 pt.
- Texto de cuerpo: 24 a 28 pt (máximo 300 a 400 palabras en todo el póster).
- Distribución en 3 o 4 columnas verticales con flujo de lectura natural de izquierda a derecha.
3. Problema Resuelto 1 (Aplicación Directa):
Calcule la proporción de áreas para un póster A0 (superficie total aprox. 1.0 m^2) que maximice el impacto visual según las pautas de Colin Purrington.
Solución:
Superficie total A0 = 0.841 m * 1.189 m = 0.9999 m^2 (aprox. 10,000 cm^2).
1. Gráficos, esquemas y diagramas (50%): 5,000 cm^2 dedicados a figuras de alta resolución (mínimo 300 dpi) con curvas legibles.
2. Espacio blanco / márgenes de respiro (30%): 3,000 cm^2 para evitar saturación visual y guiar el ojo del visitante.
3. Texto escrito esencial (20%): 2,000 cm^2 en viñetas concisas (máximo 350 palabras tipografiadas a 26 pt).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Estructure la presentación oral interactiva de 3 minutos para un visitante que se detiene frente a su póster titulado: 'Diseño de un colector solar híbrido fotovoltaico-térmico (PVT) con refrigeración por nanofluidos'.
Solución:
Estructura interactiva de 3 minutos:
- Minuto 1 (El Gancho y el Problema): 'Buenas tardes. Sabía usted que los paneles solares tradicionales sólo convierten el 20% de la radiación en electricidad y el 80% restante se pierde como calor que recalienta la celda y degrada su rendimiento? Nuestro objetivo fue capturar ese calor residual'.
- Minuto 2 (La Solución Visual): Señalando el esquema central del póster: 'Diseñamos este colector híbrido PVT: adherimos un serpentín de cobre en la parte posterior por donde circula un nanofluido de alúmina (Al2O3 en agua). Como muestran estas curvas experimentales (Fig. 2), el nanofluido redujo la temperatura de la celda en 18 °C e incrementó la eficiencia eléctrica en un 12%, entregando simultáneamente agua caliente a 55 °C'.
- Minuto 3 (Conclusión e Interacción): 'La eficiencia combinada total alcanzó el 71%. ¿Tiene alguna duda sobre la estabilidad del nanofluido o le gustaría revisar los costos de fabricación?'.""",
        "bloque_sugerido": "Taller 45 min • Diseño de póster en Canva/Illustrator y pitch interactivo",
        "slides": [
            {"numero": 1, "seccion": "PÓSTER", "titulo": "Diseño Visual de Alto Impacto", "puntos": ["Formato estándar A0 con jerarquía tipográfica legible a 2 metros.", "Regla 20/50/30: 20% texto, 50% gráficos de alta resolución, 30% espacio en blanco."]},
            {"numero": 2, "seccion": "INTERACCIÓN", "titulo": "Sustentación Relámpago de 3 Minutos", "puntos": ["Flujo conversacional interactivo guiando la mirada hacia los gráficos clave.", "Cierre con preguntas abiertas para generar redes de contacto y networking."]}
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Divulgación Científica y Comunicación a Públicos No Especializados",
        "objetivo": "Traducir conceptos tecnológicos complejos a lenguaje accesible mediante metáforas rigurosas para la sociedad civil.",
        "concepto_clave_latex": r"\text{Claridad} = \frac{\text{Rigor Conceptual}}{\text{Complejidad Terminológica}} \quad ; \quad \text{Metáfora Isomórfica}",
        "ejemplo": """CLASE MAGISTRAL: APROPIACIÓN SOCIAL DEL CONOCIMIENTO CIENTÍFICO
1. El Deber Social del Ingeniero de Divulgar:
Los proyectos de ingeniería energética se financian con recursos públicos o afectan directamente a comunidades ciudadanas. La divulgación científica no consiste en 'infantilizar' la ciencia, sino en traducir conceptos abstractos a referencias perceptibles de la vida cotidiana sin distorsionar la verdad física.
2. El Uso de Metáforas Isomórficas:
Una metáfora es isomórfica si conserva exactamente la misma estructura relacional que la ley física subyacente (ej. explicar el voltaje como presión de agua, la corriente como caudal y la resistencia como estrangulamiento de la manguera).
3. Problema Resuelto 1 (Aplicación Directa):
Explique el concepto de 'Factor de Planta de un parque solar (típicamente 20%)' en un artículo de prensa local sin usar fórmulas matemáticas para que cualquier ciudadano entienda por qué un parque de 10 MW no genera 10 MW todo el tiempo.
Solución:
Explicación divulgativa rigurosa:
'Imagine que usted compra un automóvil diseñado para viajar a una velocidad máxima de 100 kilómetros por hora. Sin embargo, en el día a día usted pasa por trancones, semáforos en rojo y conduce despacio en zonas residenciales, de modo que al final del día su velocidad promedio fue de 20 kilómetros por hora.
Lo mismo le ocurre a un parque solar de 10 megavatios: 10 megavatios es la velocidad máxima que puede alcanzar únicamente al mediodía con sol radiante. Como durante la noche no hay sol y por las mañanas y tardes la luz es suave, si promediamos toda la energía que produjo en el año, equivale a haber funcionado de manera continua al 20% de su capacidad. Por eso, para tener energía constante las 24 horas, necesitamos combinar la energía solar con baterías o centrales hidroeléctricas'.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique el error conceptual que cometen los medios de comunicación al titular: 'La ciudad consumió 500 Megavatios de energía este mes', y explique cómo redactarlo con precisión divulgativa.
Solución:
Error conceptual identificado:
El megavatio (MW) es una unidad de potencia instantánea (rapidez con la que se usa la energía por segundo), no de energía acumulada en el tiempo. La energía total acumulada durante un mes se mide en Megavatios-hora (MWh) o Gigavatios-hora (GWh).
Decir 'consumió 500 MW este mes' es el equivalente físico a decir 'el carro recorrió una distancia de 100 kilómetros por hora'.
Redacción divulgativa correcta:
'La ciudad registró una demanda pico de potencia de 500 Megavatios a las 7:00 de la noche y consumió un volumen total de 216,000 Megavatios-hora de energía a lo largo de todo el mes'.""",
        "bloque_sugerido": "Redacción 45 min • Artículo de divulgación científica para prensa",
        "slides": [
            {"numero": 1, "seccion": "DIVULGACIÓN", "titulo": "Apropiación Social del Conocimiento", "puntos": ["Traducción de leyes físicas a metáforas cotidianas sin pérdida de veracidad.", "Diferenciación conceptual clara entre potencia (MW) y energía (MWh)."]},
            {"numero": 2, "seccion": "MEDIOS", "titulo": "Comunicación en Prensa y Redes", "puntos": ["Redacción de comunicados de prensa libres de sensacionalismo espurio.", "Rol del ingeniero como educador ciudadano en la transición energética."]}
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Redacción de Cartas de Motivación y Perfil Profesional (LinkedIn / CV)",
        "objetivo": "Redactar currículums vitae de alto impacto, cartas de motivación y perfiles de LinkedIn orientados al sector de la energía.",
        "concepto_clave_latex": r"\text{Fórmula de Impacto Google: } \text{Logré } [X] \text{ medido por } [Y] \text{ haciendo } [Z]",
        "ejemplo": """CLASE MAGISTRAL: MARCA PROFESIONAL Y EMPLEABILIDAD EN INGENIERÍA
1. La Fórmula de Impacto de Google para Hojas de Vida (CV):
Los reclutadores de empresas globales del sector energético (Enel, Celsia, ISA, Ecopetrol, Vestas) descartan hojas de vida que sólo listan tareas pasivas ('Responsable de mantenimiento'). Cada viñeta debe seguir la fórmula:
'Logré [X], medido cuantitativamente por [Y], implementando [Z]'.
2. Anatomía de la Carta de Motivación (Statement of Purpose - SOP):
- Párrafo 1: Propósito específico y alineación con la misión de la empresa o posgrado.
- Párrafo 2: Evidencia empírica de competencia técnica demostrada con proyectos reales.
- Párrafo 3: Por qué esa institución específica y qué valor diferencial aportará el postulante.
- Párrafo 4: Cierre asertivo solicitando entrevista.
3. Problema Resuelto 1 (Aplicación Directa):
Transforme la siguiente viñeta pasiva de un estudiante en una declaración de impacto bajo la fórmula de Google: 'Ayudé en el laboratorio con mediciones de paneles solares'.
Solución:
Viñeta reescrita bajo la fórmula de Google:
'Optimicé el protocolo de ensayo de caracterización I-V de 48 módulos solares monocristalinos en el Laboratorio de Energías Renovables, reduciendo el tiempo de adquisición de datos en un 35% y manteniendo la incertidumbre experimental por debajo del +-1.2% mediante el diseño de scripts automatizados en Python'.
(Contiene: Logro X = optimización de caracterización; Métrica Y = -35% de tiempo y +-1.2% de error; Acción Z = scripts en Python).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique los 3 errores críticos que invalidan un perfil de LinkedIn de un ingeniero junior y cómo optimizar la sección 'Acerca de' (About).
Solución:
Errores críticos identificados:
1. Titular genérico y pasivo: Colocar 'Estudiante en búsqueda de oportunidades' en lugar de un titular estratégico con palabras clave indexables por ATS (ej. 'Estudiante de Ingeniería Energética | Modelación de Microrredes & Sistemas Fotovoltaicos | Python & Homer Pro').
2. Ausencia de proyectos y métricas en la sección de experiencia: No adjuntar enlaces a repositorios de GitHub con código limpio ni reportes técnicos demostrables.
3. Fotografía informal o sin fondo profesional neutro.
Optimización de la sección 'Acerca de':
Redactar en primera persona estructurando en tres bloques: 1) Pasión técnica y especialización (energías limpias y potencia); 2) Proyectos destacados y herramientas de dominio (PVSyst, MATLAB, Python, RETIE); 3) Disponibilidad para aportar en consultoría, diseño EPC y transición energética territorial.""",
        "bloque_sugerido": "Taller 45 min • Optimización de perfil LinkedIn y CV bajo ATS",
        "slides": [
            {"numero": 1, "seccion": "CV ATS", "titulo": "Fórmula de Impacto de Google", "puntos": ["Redacción orientada a logros: Logré [X], medido por [Y], haciendo [Z].", "Optimización de palabras clave para sistemas de filtrado algorítmico ATS."]},
            {"numero": 2, "seccion": "LINKEDIN", "titulo": "Posicionamiento Profesional", "puntos": ["Titular estratégico, biografía con métricas y enlaces a repositorios GitHub.", "Redacción de cartas de motivación persuasivas y personalizadas."]}
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "La Entrevista Técnica y Laboral: Método STAR",
        "objetivo": "Responder preguntas de comportamiento y solvencia técnica en entrevistas de selección mediante la metodología STAR.",
        "concepto_clave_latex": r"\text{STAR: } \text{Situación (20\%)} \to \text{Tarea (15\%)} \to \text{Acción (50\%)} \to \text{Resultado (15\%)}",
        "ejemplo": """CLASE MAGISTRAL: DOMINIO DE ENTREVISTAS TÉCNICAS (MÉTODO STAR)
1. El Método STAR para Preguntas de Competencia y Comportamiento:
Los paneles de selección evalúan el desempeño futuro basándose en conductas pasadas demostradas ante problemas reales:
- S (Situation): Contexto y entorno donde ocurrió el desafío (dónde, cuándo, quiénes).
- T (Task): El reto específico o problema que debía resolverse (la meta exigida).
- A (Action): Las acciones individuales específicas ejecutadas por el candidato (el núcleo de la respuesta, debe representar el 50% del tiempo; usar 'yo implementé', no refugiarse en 'nosotros').
- R (Result): El resultado cuantitativo, lecciones aprendidas y beneficios alcanzados con datos numéricos.
2. Problema Resuelto 1 (Aplicación Directa):
Responda a la pregunta típica de entrevista: 'Cuénteme sobre una ocasión en la que un proyecto de ingeniería no salió como esperaba y cómo manejó la situación', aplicando el método STAR.
Solución:
Respuesta modelo estructurada bajo STAR (tiempo total: 2 minutos):
- Situación: 'En el tercer cuatrimestre, durante la construcción de un prototipo de seguidor solar de dos ejes para la feria universitaria...'
- Tarea: 'A 48 horas de la presentación final, los servomotores se sobrecalentaron y el microcontrolador se reiniciaba constantemente al conectarlo a la batería'.
- Acción: 'En lugar de entrar en pánico, tomé el multímetro y tracé las corrientes del circuito. Identifiqué que los motores demandaban picos de corriente que inducían caídas de tensión en el carril de 5V del microcontrolador. Como no teníamos tiempo de comprar otra fuente, aislé eléctricamente la alimentación de los motores usando un regulador step-down independiente y añadí condensadores de desacoplo de 470 uF para absorber los transitorios inductivos, reescribiendo además el código para escalonar el encendido de los motores'.
- Resultado: 'El prototipo operó continuamente durante las 6 horas de la feria sin un solo reinicio, y obtuvimos el segundo lugar en innovación técnica. Aprendí la importancia crítica del desacoplo de fuentes de potencia y control en sistemas electromecánicos'.
3. Problema Resuelto 2 (Nivel Examen Parcial):
Identifique las 3 trampas comunes que cometen los postulantes en entrevistas técnicas y cómo superarlas:
Solución:
1. Hablar en plural pasivo ('Nosotros hicimos el informe'): El entrevistador no está contratando al grupo de compañeros, sino al candidato. Debe enfatizar: 'El equipo tenía cuatro miembros; mi rol específico fue formular las ecuaciones de flujo en MATLAB y validar los datos experimentales'.
2. Olvidar cuantificar el Resultado (la R de STAR): Terminar con 'y al final funcionó bien' no aporta valor. Debe cerrarse con datos: 'logrando una reducción de temperatura de 15 °C y una eficiencia 8% superior'.
3. Inventar respuestas ante preguntas técnicas desconocidas: Intentar engañar al panel técnico cuando no se sabe una respuesta destruye la confianza ética de inmediato. La respuesta profesional correcta es: 'No conozco ese parámetro específico de memoria, pero basándome en los principios de la norma IEEE 519, estimo que el procedimiento correcto para determinarlo sería medir la impedancia de cortocircuito en el punto de acoplamiento común'.""",
        "bloque_sugerido": "Simulacro 45 min • Role-playing de entrevistas técnicas con método STAR",
        "slides": [
            {"numero": 1, "seccion": "STAR", "titulo": "Metodología de Respuesta STAR", "puntos": ["Situación, Tarea, Acción y Resultado cuantificable.", "Foco en el 50% del tiempo en las acciones técnicas individuales tomadas."]},
            {"numero": 2, "seccion": "ENTREVISTA", "titulo": "Solvencia Técnica y Honestidad", "puntos": ["Demostración de resiliencia y resolución metódica ante fallos de hardware.", "Honestidad intelectual al enfrentar preguntas técnicas complejas sin divagaciones."]}
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Ética en la Comunicación Científica e Inteligencia Artificial Generativa",
        "objetivo": "Aplicar estándares de integridad científica sobre autoría, conflicto de intereses y uso responsable de LLMs en ingeniería.",
        "concepto_clave_latex": r"\text{Integridad Científica: } \text{Cero Plagio} \land \text{Cero Falsificación} \land \text{Uso Ético de IA}",
        "ejemplo": """CLASE MAGISTRAL: ÉTICA DE LA PUBLICACIÓN E INTELIGENCIA ARTIFICIAL
1. Faltas Gravísimas a la Integridad Científica:
- Falsificación: Manipular datos experimentales, alterar puntos en gráficos o calibraciones para forzar que los resultados concuerden con una hipótesis preconcebida.
- Fabricación: Inventar mediciones que nunca se realizaron en laboratorio.
- Plagio: Apropiación de ideas, algoritmos o textos sin reconocimiento autoral formal.
2. Uso Responsable de Modelos de Lenguaje (LLMs / ChatGPT) en Textos de Ingeniería:
Las políticas editoriales de IEEE, Elsevier y Nature establecen taxativamente:
- Un modelo de IA NO puede ser listado como autor (carece de responsabilidad legal y ética sobre lo escrito).
- El uso de IA generativa para asistencia en redacción, traducción o depuración de código debe declararse explícitamente en una sección de Agradecimientos o Metodología.
- El autor humano asume el 100% de la responsabilidad civil y académica por cualquier alucinación, error conceptual, dato falso o cita inexistente generada por la IA.
3. Problema Resuelto 1 (Aplicación Directa):
Un tesista utilizó un modelo de IA para generar la revisión de literatura de su trabajo de grado. El modelo redactó un párrafo impecable citando a 'Rodríguez et al. (2022) en Solar Energy'. Al verificar la cita, el jurado constata que dicho artículo nunca existió (alucinación del modelo). Analice las implicaciones académicas y éticas del hecho.
Solución:
Implicaciones analizadas:
1. Deshonestidad y negligencia académica: El estudiante violó el principio de verificación directa de fuentes primarias al incluir referencias inventadas sin haber leído los textos.
2. Falta de rigor científico: En un trabajo de ingeniería avalado por la Universidad del Magdalena, una cita falsa desacredita la validez de todo el marco teórico y compromete la reputación institucional.
3. Sanción disciplinaria: Conforme al reglamento estudiantil y el código de ética COPNIA, la inclusión de datos bibliográficos fabricados puede acarrear la reprobación inmediata del trabajo de grado y apertura de proceso disciplinario por fraude académico.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Redacte una declaración transparente y ética de uso de herramientas de IA generativa para ser incluida en la sección metodológica de un artículo de investigación según las directrices de IEEE.
Solución:
Declaración formal de uso de IA (AI Usage Declaration):
'Declaración de Asistencia de Inteligencia Artificial: Durante la preparación de este manuscrito, los autores utilizaron Claude 3.5 Sonnet / ChatGPT exclusivamente para la corrección estilística del idioma inglés y la optimización sintáctica de fragmentos de código en Python. Tras el uso de dicha herramienta, los autores revisaron, editaron críticamente y validaron todo el contenido resultante, asumiendo la plena responsabilidad por la exactitud teórica, la integridad de los datos experimentales y la veracidad de las referencias bibliográficas citadas en el presente artículo'.""",
        "bloque_sugerido": "Debate 45 min • Dilemas éticos sobre IA generativa e integridad científica",
        "slides": [
            {"numero": 1, "seccion": "ÉTICA", "titulo": "Integridad Científica Fundamental", "puntos": ["Prohibición absoluta de fabricación, falsificación y plagio de datos.", "Conflictos de interés y autoría responsable (criterios de autoría ICMJE)."]},
            {"numero": 2, "seccion": "IA RESPONSABLE", "titulo": "Directrices IEEE sobre LLMs", "puntos": ["La IA como herramienta de apoyo, nunca como coautora del documento.", "Declaración obligatoria de uso y responsabilidad humana indelegable."]}
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "El Manifiesto del Ingeniero: Discurso Integrador y Compromiso Territorial",
        "objetivo": "Sintetizar las competencias lectoras, escriturales y orales en un discurso magistral de compromiso ético, ambiental y profesional.",
        "concepto_clave_latex": r"\text{Retórica Magistral: } \text{Ethos (Credibilidad)} + \text{Pathos (Emoción)} + \text{Logos (Razón Lógica)}",
        "ejemplo": """CLASE MAGISTRAL: LA CÚSPIDE DE LA COMUNICACIÓN EN INGENIERÍA
1. La Tríada Aristotélica de la Retórica Magistral:
Todo gran discurso técnico que transforma la sociedad equilibra tres fuerzas:
- Logos: El rigor de los datos, las leyes de la termodinámica y el análisis numérico irrefutable.
- Ethos: La autoridad moral, la integridad ética y la solvencia técnica del orador.
- Pathos: La conexión emocional con las necesidades humanas reales (justicia climática, erradicación de la pobreza energética en el Caribe, dignidad para comunidades rurales).
2. El Manifiesto del Ingeniero Energético de Unimagdalena:
Culminación del primer cuatrimestre: los estudiantes sintetizan su voz académica no como meros calculadores de circuitos, sino como comunicadores solventes capaces de liderar la transformación energética justa de Colombia y el planeta.
3. Problema Resuelto 1 (Aplicación Directa):
Descomponga cómo se integran el Logos, el Ethos y el Pathos en el siguiente extracto de discurso pronunciado por un estudiante de ingeniería energética:
'Como futuros ingenieros formados en las aulas de la Universidad del Magdalena [Ethos], no podemos aceptar que mientras nuestra región irradia más de 5.5 kilovatios-hora de sol por metro cuadrado cada día [Logos], miles de niños en nuestros corregimientos sigan estudiando a oscuras o respirando el humo nocivo de plantas diésel obsoletas [Pathos]. Nuestra ciencia tiene una misión humana inaplazable: llevar luz soberana y limpia a cada rincón de nuestro territorio'.
Solución:
Descomposición analítica:
1. Ethos: Establece pertenencia e identidad institucional ('Como futuros ingenieros formados en las aulas de la Universidad del Magdalena'), cimentando autoridad moral y compromiso formativo.
2. Logos: Aporta el dato físico riguroso y objetivo ('más de 5.5 kilovatios-hora de sol por metro cuadrado cada día'), demostrando conocimiento del recurso energético territorial.
3. Pathos: Evoca la realidad social dolorosa ('miles de niños... a oscuras o respirando el humo nocivo de plantas diésel') para despertar sentido de urgencia ética y empatía en la audiencia.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Redacte el cierre concluyente de un discurso de graduación de ingeniería energética que sintetice la transición ecológica, la soberanía territorial y el código deontológico COPNIA.
Solución:
Discurso de cierre magistral (150 palabras):
'Colegas: la ingeniería no es un ejercicio estéril de fórmulas sobre papel; es la herramienta más poderosa que la humanidad ha creado para moldear la realidad material en armonía con la vida.
Al recibir este título bajo la ley colombiana y el código ético del COPNIA, asumimos un pacto solemne: jamás antepondremos el beneficio económico a la seguridad de las personas ni a la preservación de nuestros ecosistemas.
Desde las estribaciones de la Sierra Nevada hasta las costas del Caribe, seremos los artífices de una transición energética soberana, democrática y justa. Que cuando el futuro nos juzgue, no se recuerde sólo cuántos megavatios instalamos, sino a cuántas comunidades liberamos de la exclusión y cuántas toneladas de carbono dejamos de arrojar al cielo de nuestra patria.
Muchas gracias'.""",
        "bloque_sugerido": "Discurso Magistral 50 min • Declamación del Manifiesto Ético de Primer Semestre",
        "slides": [
            {"numero": 1, "seccion": "RETÓRICA", "titulo": "Tríada de Aristóteles: Ethos, Pathos, Logos", "puntos": ["Logos: Verdad empírica y leyes termodinámicas irrefutables.", "Ethos: Integridad ética profesional; Pathos: Compromiso humano territorial."]},
            {"numero": 2, "seccion": "MANIFIESTO", "titulo": "Compromiso del Ingeniero de Unimagdalena", "puntos": ["Liderazgo técnico ético al servicio de la transición energética del Caribe.", "Síntesis de excelencia en lectura crítica, escritura precisa y oratoria convincente."]}
        ]
    }
]

if __name__ == '__main__':
    target = '  - cuatrimestre: 2'
    yaml_text = format_topics_yaml(topics_9_to_20 + topics_21_to_30)
    inject_topics_after(target, yaml_text)
    print("01011801 Procesos Lectores, Escriturales y Orales now has 30 topics!")
