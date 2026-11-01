# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_04031827 = [
    {
        "numero_tema": 9,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Marco Institucional y Desagregación Vertical: Leyes 142 y 143 de 1994",
        "objetivo": "Analizar la arquitectura institucional del sector eléctrico colombiano fundamentada en las Leyes 142 y 143 de 1994, evaluando la separación de actividades y el rol de CREG, UPME, SSPD y XM.",
        "concepto_clave_latex": r"\text{Cadena de Valor}: \text{Generación (G)} \to \text{Transmisión (T)} \to \text{Distribución (D)} \to \text{Comercialización (C)}",
        "ejemplo": "Problema 1: Una empresa integrada de servicios públicos domiciliarios constituida antes de 1994 opera simultáneamente plantas de generación hidroeléctrica, redes de distribución regional y comercialización de energía. La compañía proyecta adquirir el 40% de las acciones de un consorcio de transmisión nacional (STN) y aumentar su cuota de mercado en comercialización al 32% de la demanda nacional regulada. Evaluación jurídica bajo las Leyes 142 y 143 de 1994 y resoluciones antimonopolio de la CREG: 1) Principio de Desagregación Vertical Estricta: El artículo 74 de la Ley 143 de 1994 y la Resolución CREG 057 de 1996 prohíben taxativamente que una empresa que realice actividades de generación, distribución o comercialización participe en el capital accionario de transportadores del Sistema de Transmisión Nacional (STN), por lo que la compra del 40% es ilegal y debe ser vetada. 2) Límite de Concentración Horizontal en Comercialización: La Resolución CREG 180 de 2009 fija un límite máximo de concentración de mercado (market share) en comercialización del 25% de la demanda total del Sistema Interconectado Nacional (SIN). Como el 32% propuesto supera en 7 puntos porcentuales el tope regulatorio, la Superintendencia de Servicios Públicos Domiciliarios (SSPD) y la Superintendencia de Industria y Comercio (SIC) deniegan la operación por riesgo de abuso de posición dominante. La empresa debe estructurar una escisión corporativa (spin-off) manteniendo cuentas contables separadas e independientes para cada negocio. Problema 2: En contratos entre empresas vinculadas del mismo grupo económico, la CREG impone la doctrina de 'trato a distancia' (Arm's Length Principle) para impedir subsidios cruzados indebidos que inflen la tarifa al usuario final.",
        "bloque_sugerido": "Derecho Energético 45 min • Leyes 142/143 de 1994 y límites de integración vertical y horizontal",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTRUCTURA INSTITUCIONAL COLOMBIANA",
                "titulo": "Separación de Funciones Estado - Mercado",
                "puntos": [
                    "Ministerio de Minas y Energía (MME): Define las políticas públicas sectoriales y la visión de transición energética.",
                    "CREG (Comisión de Regulación de Energía y Gas): Regula monopolios naturales y promueve la competencia eficiente.",
                    "UPME (Unidad de Planeación Minero Energética): Diseña los Planes de Expansión de Referencia de Generación y Transmisión.",
                    "SSPD (Superintendencia de Servicios Públicos): Ejerce el control, inspección y vigilancia sobre los operadores.",
                    "XM S.A. E.S.P.: Administrador del Mercado (ASIC) y Centro Nacional de Despacho (CND)."
                ]
            },
            {
                "numero": 2,
                "seccion": "DESAGREGACIÓN Y COMPETENCIA",
                "titulo": "Monopolios Naturales vs Mercados Competitivos",
                "puntos": [
                    "Actividades en Competencia: Generación (G) y Comercialización (C); los precios se determinan libremente por oferta y demanda.",
                    "Monopolios Naturales Regulados: Transmisión (T) y Distribución (D); las tarifas son remuneradas bajo esquemas de ingreso máximo (Revenue Cap).",
                    "Regla de Acceso Abierto No Discriminatorio (Open Access): Los dueños de las redes no pueden negar la conexión a generadores terceros."
                ]
            }
        ]
    },
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Leyes 1715 de 2014 y 2099 de 2021: Régimen de Incentivos Tributarios a FNCER",
        "objetivo": "Estructurar modelos financieros de proyectos de energía renovable e hidrógeno aprovechando los cuatro beneficios tributarios y aduaneros de la Ley 1715 modificada por la Ley 2099.",
        "concepto_clave_latex": r"\text{Deducción Renta}: 50\% \text{ CAPEX} \le 50\% \text{ Renta Líquida} \quad ; \quad \text{Depreciación Acelerada}: d \le 33.33\% \text{ anual}",
        "ejemplo": "Problema 1: Un desarrollador privado estructura un parque solar fotovoltaico de 20 MW en el Magdalena con un CAPEX total de inversión elegible de 18,000,000 USD (inversores, módulos, seguidores solares y obra civil). Se gestiona la certificación ambiental y técnica ante la UPME para acogerse a los cuatro incentivos tributarios de la Ley 1715 de 2014 / Ley 2099 de 2021: 1) Deducción Especial de Renta (Art. 11): Deducción del 50% de la inversión en el impuesto de renta durante los primeros 15 años (ahorro fiscal de deducción = 9,000,000 USD aplicable hasta el 50% de la renta líquida anual; a la tarifa corporativa del 35%, genera un ahorro monetario en efectivo de 9,000,000 * 0.35 = 3,150,000 USD en impuestos no pagados). 2) Exclusión de IVA (Art. 12): Los módulos, inversores y cables importados están exentos del 19% de IVA (ahorro directo en liquidez de 18,000,000 * 0.19 = 3,420,000 USD no financiados). 3) Exención de Gravámenes Arancelarios (Art. 13): 0% de arancel de importación sobre bienes no producidos en la industria nacional (ahorro del 5% al 10%, equivalente a 900,000 USD). 4) Depreciación Acelerada de Activos (Art. 14): Tasa anual máxima de depreciación contable y fiscal del 33.33% (depreciación del 100% de la planta en solo 3 años en lugar de los 20 años estándar, generando un escudo fiscal masivo en los primeros años de operación comercial). Impacto en la rentabilidad del proyecto: La Tasa Interna de Retorno (TIR) del capital propio se eleva del 9.2% al 15.8%, reduciendo el Costo Nivelado de Energía (LCOE) de 54 USD/MWh a 38 USD/MWh. Problema 2: Con la Ley 2099 de 2021 (Ley de Transición Energética), estos mismos 4 incentivos se extienden al hidrógeno verde/azul, captura y almacenamiento de carbono (CCUS) y sistemas de almacenamiento masivo con baterías (BESS).",
        "bloque_sugerido": "Incentivos Tributarios FNCER 45 min • Modelado financiero de los 4 beneficios Ley 1715/2099",
        "slides": [
            {
                "numero": 1,
                "seccion": "LEGISLACIÓN DE FOMENTO",
                "titulo": "Los 4 Pilares Tributarios de la Ley 1715 / 2099",
                "puntos": [
                    "Deducción especial de renta: Hasta el 50% de la inversión en un plazo máximo de 15 años.",
                    "Exclusión de IVA: Plena sobre equipos, materiales y servicios nacionales o importados certificados por la UPME.",
                    "Exención arancelaria: Arancel cero (0%) para bienes no sustituibles por producción nacional.",
                    "Depreciación acelerada: Amortización de hasta el 33.33% anual (recuperación total en 3 años)."
                ]
            },
            {
                "numero": 2,
                "seccion": "TRÁMITE DE CERTIFICACIÓN UPME",
                "titulo": "Requisitos y Ventanilla Única",
                "puntos": [
                    "El inversionista debe radicar solicitud digital ante la UPME aportando ficha técnica, planos y presupuesto detallado.",
                    "Emisión de la Certificación UPME: Requisito vinculante previo para que la DIAN apruebe la exclusión aduanera.",
                    "Catalizador fundamental que posicionó a Colombia como líder regional en atracción de inversión extranjera renovable."
                ]
            }
        ]
    },
    {
        "numero_tema": 11,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Regulación CREG de Autogeneración y Generación Distribuida (CREG 174 de 2021)",
        "objetivo": "Aplicar el marco regulatorio de la Resolución CREG 174 de 2021 para autogeneradores a pequeña escala (AGPE <= 1 MW), autogeneradores a gran escala (AGGE) y generadores distribuidos (GD).",
        "concepto_clave_latex": r"\text{AGPE}: P \le 1 \text{ MW} \quad ; \quad \text{Crédito de Energía}: E_{exp} \le E_{imp} \implies \text{Valorizado a } CU_m - C_m",
        "ejemplo": "Problema 1: Un campus universitario en Santa Marta instala un sistema solar fotovoltaico de 400 kW_p clasificado como Autogenerador a Pequeña Escala con Entrega de Excedentes (AGPE con potencia instalada <= 1000 kW bajo CREG 174 de 2021). Durante un mes de 30 días, el campus consume de la red eléctrica una energía importada de E_imp = 45,000 kWh en horas sin sol. El sistema solar genera 58,000 kWh, de los cuales 38,000 kWh son autoconsumidos instantáneamente y 20,000 kWh se exportan a la red de distribución local como excedentes (E_exp = 20,000 kWh). Tarifas del comercializador del mes: Costo Unitario CU = 850 COP/kWh, componente de comercialización C_m = 95 COP/kWh, precio de bolsa horario promedio P_bolsa = 280 COP/kWh. Liquidación oficial en factura según las reglas CREG 174: 1) Tramo 1 (Excedentes hasta el límite de la importación, E_exp <= E_imp, es decir, los 20,000 kWh completos): Se remuneran bajo el mecanismo de 'Crédito de Energía' al valor del Costo Unitario menos la comercialización: Tarifa_credito = CU - C_m = 850 - 95 = 755 COP/kWh. Valor acreditado en factura: Credito = 20,000 kWh * 755 COP/kWh = 15,100,000 COP. 2) Cobro por energía importada: Costo_importada = 45,000 kWh * 850 COP/kWh = 38,250,000 COP. 3) Valor neto final a pagar por la universidad en la factura mensual: Factura = 38,250,000 - 15,100,000 = 23,150,000 COP (ahorro total en el mes de 32,300,000 COP sumando el autoconsumo directo valorizado a 850 COP/kWh). Si en vacaciones la exportación superara la importación (E_exp > E_imp), el excedente superior se liquidaría al precio marginal de bolsa P_bolsa. Problema 2: En sistemas AGPE <= 100 kW, la CREG 174 impone un trámite simplificado de conexión ante el Operador de Red (OR) con respuesta perentoria en máximo 10 días hábiles sin exigir estudios complejos de conexión.",
        "bloque_sugerido": "Regulación AGPE 45 min • Resolución CREG 174/2021 y liquidación de créditos de energía",
        "slides": [
            {
                "numero": 1,
                "seccion": "CATEGORÍAS REGULATORIAS CREG 174",
                "titulo": "AGPE, AGGE y Generador Distribuido",
                "puntos": [
                    "AGPE (Autogeneración a Pequeña Escala): Capacidad nominal instalada P <= 1 MW; produce energía prioritariamente para atender consumo propio.",
                    "AGGE (Autogeneración a Gran Escala): Capacidad nominal P > 1 MW; debe someterse a despacho centralizado si P > 20 MW.",
                    "Generador Distribuido (GD): Empresa de servicios públicos con planta P <= 1 MW conectada al SDL sin demanda asociada (vende el 100% de la energía)."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGLAS DE LIQUIDACIÓN DE EXCEDENTES",
                "titulo": "El Mecanismo de Crédito de Energía",
                "puntos": [
                    "Para FNCER <= 100 kW: Los excedentes que igualen la importación se descuentan del componente (CU - C_m); los saldos netos a precio de bolsa.",
                    "Sistemas > 100 kW y <= 1 MW: Se liquidan al precio horario de bolsa del MEM menos costos de comercialización.",
                    "Medición Bidireccional Inteligente (AMI): Es obligatoria para registrar por separado la energía horaria importada y exportada."
                ]
            }
        ]
    },
    {
        "numero_tema": 12,
        "corte": 1,
        "modalidad": "teorico",
        "titulo": "Estructura Tarifaria de la Energía Eléctrica: La Fórmula del Costo Unitario (CU)",
        "objetivo": "Descomponer y auditar la fórmula tarifaria del Costo Unitario de Prestación del Servicio (CU) calculando los componentes de Generación (G), Transmisión (T), Distribución (D), Comercialización (C), Pérdidas (P) y Restricciones (R).",
        "concepto_clave_latex": r"CU_{n,m,t} = G_{m,t} + T_{m,t} + D_{n,m,t} + C_{v,m,t} + P_{r,n,m,t} + R_{m,t} \quad \left[\frac{\text{COP}}{\text{kWh}}\right]",
        "ejemplo": "Problema 1: Se audita la factura de energía eléctrica de un usuario industrial conectado en Nivel de Tensión 2 (13.2 kV, tarifa monomia sin factor de subsidio/contribución, estrato industrial con contribución de solidaridad del +20%) para el mes de octubre en el mercado regulado de la Costa Caribe. Valores de los componentes tarifarios oficiales publicados por el operador en COP/kWh: Generación en contratos bilaterales y bolsa G = 345.20 COP/kWh; Transmisión nacional STN T = 52.80 COP/kWh; Distribución regional STR y SDL Nivel 2 D = 198.40 COP/kWh; Comercialización minorista C_v = 74.15 COP/kWh; Compras de pérdidas técnicas y no técnicas reconocidas P = 112.60 COP/kWh; Costos por restricciones operativas y redispacho térmico por congestión R = 68.90 COP/kWh. 1) Costo Unitario base: CU = G + T + D + C + P + R = 345.20 + 52.80 + 198.40 + 74.15 + 112.60 + 68.90 = 852.05 COP/kWh. El consumo medido del mes es E = 120,000 kWh. Costo de energía facturada: Costo_base = 120,000 * 852.05 = 102,246,000 COP. 2) Contribución de solidaridad legal del 20% para el fondo FOSYGEC / subsidios a estratos 1, 2 y 3: Contribución = 102,246,000 * 0.20 = 20,449,200 COP. Total a pagar en factura = 122,695,200 COP. Análisis regulatorio: El componente de pérdidas (P = 112.60 COP/kWh, 13.2% del total) y restricciones (R = 68.90 COP/kWh, 8.1% del total) representan en conjunto el 21.3% del costo de la energía, evidenciando el sobrecosto originado por la falta de redes de transmisión y el hurto de energía en la región. Problema 2: En la opción tarifaria (Resolución CREG 012 de 2020), los comercializadores acumulan saldos por cobrar cuando la tarifa aplicada es inferior al CU real, difiriendo el cobro a los usuarios en cuotas mensuales indexadas.",
        "bloque_sugerido": "Tarifas Eléctricas 45 min • Descomposición analítica de la fórmula CU CREG 119/2007",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA FÓRMULA OFICIAL DEL CU",
                "titulo": "Los 6 Componentes de la Factura",
                "puntos": [
                    "G (Generación): Costo ponderado de compra de energía en contratos a largo plazo y compras en bolsa.",
                    "T (Transmisión): Remuneración del transporte de electricidad a través del Sistema de Transmisión Nacional (STN > 220 kV).",
                    "D (Distribución): Cargo por uso de las redes regionales (STR y SDL) remunerado según el nivel de tensión (Nivel 1 a 4).",
                    "C (Comercialización): Remunera la gestión de lectura, facturación, atención al cliente y riesgo de cartera.",
                    "P (Pérdidas): Costo de adquirir la energía que se pierde físicamente por efecto Joule y no técnicamente por fraude.",
                    "R (Restricciones): Costo de encender plantas térmicas caras fuera de mérito para garantizar la seguridad de la red."
                ]
            },
            {
                "numero": 2,
                "seccion": "SUBSIDIOS Y CONTRIBUCIONES",
                "titulo": "Régimen de Solidaridad Tarifaria (Ley 142)",
                "puntos": [
                    "Estrato 1: Subsidio de hasta el 60% sobre el Consumo de Subsistencia (173 kWh en clima cálido, 130 kWh en templado).",
                    "Estrato 2: Subsidio de hasta el 50%; Estrato 3: Subsidio del 15% del consumo básico.",
                    "Estratos 5, 6 y Usuarios Comerciales/Industriales: Pagan una sobretasa de contribución obligatoria del +20%."
                ]
            }
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "El Mercado de Energía Mayorista (MEM): Bolsa de Energía y Contratos Bilaterales",
        "objetivo": "Modelar el funcionamiento del Mercado de Energía Mayorista (MEM) en Colombia, analizando la formación del precio de bolsa por orden de mérito, ofertas horarias y contratos bilaterales.",
        "concepto_clave_latex": r"P_{\text{bolsa},t} = \max_{i \in \text{Despachados}} \{ \text{Oferta}_{i,t} \} \quad ; \quad \text{Exposición}: \%_{\text{bolsa}} = \frac{E_{\text{demanda}} - E_{\text{contratos}}}{E_{\text{demanda}}}",
        "ejemplo": "Problema 1: En una hora específica de alta demanda (19:00 h, demanda nacional de 11,200 MW), los generadores del MEM envían sus ofertas de precio de energía a XM (Centro Nacional de Despacho). El orden de mérito económico apila las plantas desde el menor costo de oferta: 1) Hidroeléctricas de pasada y parques solares/eólicos ofertan 6,500 MW a 0 COP/kWh (costo variable nulo). 2) Centrales hidroeléctricas con embalse ofertan 3,800 MW a precios entre 120 y 240 COP/kWh. 3) Ciclos combinados a gas natural ofertan 800 MW a 380 COP/kWh. 4) Plantas térmicas a carbón ofertan 400 MW a 450 COP/kWh. 5) Turbinas térmicas a diésel (fuel oil) ofertan 500 MW a 720 COP/kWh. La demanda acumulada de 11,200 MW se satisface con: 6,500 MW (renovables) + 3,800 MW (hidro embalse) + 800 MW (gas) + 100 MW (carbón) = 11,200 MW. La última planta despachada que cierra la demanda es la central a carbón ofertando a 450 COP/kWh. Por la regla de mercado marginalista unificado (pay-as-cleared), todas las plantas despachadas reciben el mismo precio marginal de bolsa: P_bolsa = 450 COP/kWh. Un comercializador atiende una demanda de 200 MW en esa hora; tiene el 80% cubierto con contratos bilaterales de largo plazo a precio fijo de 260 COP/kWh y el 20% expuesto a bolsa. Costo total de compra horario: Compras = (200 * 0.80 * 1000 kWh * 260 COP) + (200 * 0.20 * 1000 kWh * 450 COP) = (160,000 * 260) + (40,000 * 450) = 41,600,000 + 18,000,000 = 59,600,000 COP. Precio medio de compra: 59,600,000 / 200,000 = 298.0 COP/kWh. Si el comercializador hubiera estado expuesto al 100% en bolsa, habría pagado 90,000,000 COP, demostrando la función crítica de cobertura financiera de los contratos bilaterales durante sequías o fenómenos de El Niño. Problema 2: En la subasta estandarizada SICEP, los comercializadores están obligados a convocar convocatorias públicas abiertas para la compra de energía conforme a la Resolución CREG 130 de 2019.",
        "bloque_sugerido": "Mercado Mayorista MEM 45 min • Formación del precio marginal de bolsa y contratos bilaterales",
        "slides": [
            {
                "numero": 1,
                "seccion": "FUNCIONAMIENTO DEL MEM",
                "titulo": "Mercado Marginalista Horario (Bolsa de Energía)",
                "puntos": [
                    "Todos los generadores envían diariamente a XM sus 24 ofertas de precio y disponibilidad técnica para el día siguiente.",
                    "Orden de mérito: El CND despacha las plantas de menor a mayor precio de oferta hasta satisfacer la demanda pronosticada.",
                    "Precio Marginal de Bolsa (Uniform Clearing Price): Todas las plantas reciben el precio de la última unidad despachada en esa hora."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTRATOS BILATERALES Y COBERTURAS",
                "titulo": "Protección ante la Volatilidad Climática",
                "puntos": [
                    "Más del 80% de la energía del país se comercializa a través de contratos financieros y físicos bilaterales a largo plazo.",
                    "Protege a los usuarios regulados de disparos astronómicos del precio de bolsa durante el Fenómeno de El Niño.",
                    "SICEP (Sistema Centralizado de Información de Convocatorias Públicas): Garantiza transparencia y libre concurrencia en la contratación."
                ]
            }
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Cargo por Confiabilidad y Energía Firme para el Cargo por Confiabilidad (ENFICC)",
        "objetivo": "Calcular la Energía Firme para el Cargo por Confiabilidad (ENFICC) y evaluar la remuneración del Cargo por Confiabilidad mediante la opción de compra de energía en condición crítica.",
        "concepto_clave_latex": r"\text{Cargo por Confiabilidad} = \text{ENFICC} \cdot \text{P}_{\text{subasta}} \quad ; \quad \text{Obligación}: \text{OEF} \implies P_{\text{bolsa}} > P_{\text{escasez}}",
        "ejemplo": "Problema 1: Una central termoeléctrica a gas natural de 300 MW de capacidad neta efectiva con consumo térmico heat rate de 8,200 kJ/kWh participa en la subasta del Cargo por Confiabilidad (Resolución CREG 071 de 2006) y se le asigna una Obligación de Energía Firme de OEF = 6.0 GWh/día (equivalente a una potencia firme continua de 250 MW durante 24 horas) por un periodo de vigencia de 10 años, a un precio de cierre de subasta de P_subasta = 15.10 USD/MWh (remuneración fija por capacidad de potencia disponible). Ingreso anual fijo por Cargo por Confiabilidad: Ingreso_fijo = 6000 MWh/día * 365 días * 15.10 USD/MWh = 2,190,000 MWh * 15.10 USD = 33,069,000 USD anuales, independientemente de si la planta es despachada o no. A cambio de este pago fijo garantizado, la planta contrae la obligación jurídica estricta de generar cuando el precio de bolsa supere el 'Precio de Escasez' fijado por la CREG (ej. P_escasez = 210 USD/MWh). Durante un Fenómeno de El Niño severo, los embalses bajan al 28% y el precio de bolsa se dispara a P_bolsa = 480 USD/MWh durante 60 días consecutivos. La planta es despachada a plena capacidad generando los 6.0 GWh diarios. En el mercado, la planta vende su energía al precio de escasez (210 USD/MWh), devolviendo a los comercializadores la diferencia (480 - 210 = 270 USD/MWh de renta de escasez) a través del mecanismo de liquidación de XM. Esto actúa como un seguro financiero perfecto que impide que las tarifas de los usuarios se multipliquen por tres durante las sequías. Problema 2: En plantas solares fotovoltaicas y eólicas, el cálculo de la ENFICC base (Resoluciones CREG 201 de 2017 y CREG 038 de 2020) utiliza series históricas horarias con una probabilidad de excedencia del 95% (P95) o requiere respaldo con almacenamiento BESS.",
        "bloque_sugerido": "Confiabilidad del Mercado 45 min • Cálculo de ENFICC, precio de escasez y subastas CREG 071",
        "slides": [
            {
                "numero": 1,
                "seccion": "SEGURIDAD DE SUMINISTRO ENÉRGICO",
                "titulo": "El Mecanismo de Capacidad Firme",
                "puntos": [
                    "Colombia depende en un 70% de hidroeléctricas vulnerables a sequías cíclicas extremas (El Niño).",
                    "El Cargo por Confiabilidad es un esquema regulatorio que remunera a las plantas por ESTAR DISPONIBLES para generar en crisis.",
                    "Sustituye la construcción sobredimensionada e ineficiente por un incentivo económico de mercado robusto."
                ]
            },
            {
                "numero": 2,
                "seccion": "LA OPCIÓN DE COMPRA FINANCIERA",
                "titulo": "El Precio de Escasez como Techo Tarifario",
                "puntos": [
                    "Los usuarios pagan una prima mensual constante en su factura (Cargo por Confiabilidad).",
                    "A cambio, compran una opción financiera: cuando hay escasez, la energía se les entrega a un precio regulado tope (Precio de Escasez).",
                    "Si un generador con OEF asignada no entrega su energía comprometida en escasez, es intervenido y pierde las garantías bancarias."
                ]
            }
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Subastas de Contratos de Energía a Largo Plazo y Contratos PPA (Power Purchase Agreements)",
        "objetivo": "Diseñar y negociar contratos privados y públicos de compraventa de energía a largo plazo (PPA físicos y virtuales) evaluando estructuras de precio 'Take-or-Pay' y 'Pay-as-Produced'.",
        "concepto_clave_latex": r"\text{PPA Físico}: \text{Entrega directa en nodo} \quad ; \quad \text{VPPA / CFD}: \text{Liquidación Financiera} = Q_t \times (P_{\text{strike}} - P_{\text{spot},t})",
        "ejemplo": "Problema 1: Una empresa minera multinacional en el Cesar firma un contrato privado de compraventa de energía renovable a largo plazo (PPA Físico a 15 años) con un desarrollador solar para un parque de 80 MW. Modalidad contractual: 'Pay-as-Produced' (la minera compra toda la energía que el parque efectivamente inyecte al nodo de entrega a 115 kV). Precio pactado (Strike Price): P_strike = 42.0 USD/MWh indexado anualmente a la inflación estadounidense (US-CPI con un tope de 2.5% anual). La producción solar anual estimada en el modelo P50 es de E = 155,000 MWh/año. En el año 1, la planta entrega 152,000 MWh. Facturación anual del generador: Ingreso = 152,000 MWh * 42.0 USD/MWh = 6,384,000 USD. Durante las horas solares, el precio medio spot de bolsa en ese nodo fue de P_spot = 68.5 USD/MWh. Ahorro económico neto de la minera en el año: Ahorro = 152,000 * (68.5 - 42.0) = 152,000 * 26.5 USD = 4,028,000 USD ahorrados en costos de energía frente a comprar en bolsa o a su comercializador tradicional. Para bancarizar el proyecto, los bancos internacionales (Project Finance con deuda senior al 70%) exigen que el PPA cubra al menos el 75% de la producción esperada P90 para garantizar una razón de cobertura del servicio de la deuda DSCR >= 1.30. Problema 2: En un PPA Virtual (VPPA o Contrato por Diferencias - CfD), la energía fluye normalmente al pool del mercado pero el generador y el comprador corporativo liquidan mensualmente una compensación financiera por diferencias (Contracts for Difference).",
        "bloque_sugerido": "Contratación PPA 45 min • Estructuración de PPAs privados, subastas FNCER y bancabilidad",
        "slides": [
            {
                "numero": 1,
                "seccion": "FINANCIACIÓN DE PROYECTOS RENOVABLES",
                "titulo": "La Centralidad del Contrato PPA",
                "puntos": [
                    "Ningún parque eólico o solar de gran escala se construye 'merchant' (expuesto al 100% al precio spot de bolsa).",
                    "El PPA (Power Purchase Agreement) es el contrato que garantiza un flujo de caja predecible durante 10, 15 o 20 años.",
                    "Es la piedra angular de la 'bancabilidad' requerida por los bancos para prestar capital en modalidad Project Finance."
                ]
            },
            {
                "numero": 2,
                "seccion": "TIPOLOGÍAS DE CONTRATACIÓN",
                "titulo": "Take-or-Pay vs Pay-as-Produced",
                "puntos": [
                    "Take-or-Pay: El comprador paga una cantidad fija de energía se consuma o no; el riesgo de volumen lo asume el comprador.",
                    "Pay-as-Produced: El comprador solo paga los megavatios-hora generados en tiempo real; el riesgo de recurso lo asume el generador.",
                    "Subastas Estatales FNCER (MME): Mecanismo competitivo que adjudica contratos a 15 años respaldando la transición nacional."
                ]
            }
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Procedimiento de Conexión al Sistema Interconectado Nacional (UPME y CREG 075)",
        "objetivo": "Tramitar la conexión de proyectos de generación ante la UPME bajo la Resolución CREG 075 de 2021, evaluando estudios de conexión, garantías de reserva de capacidad y curvas S.",
        "concepto_clave_latex": r"\text{Garantía de Reserva de Capacidad}: G = 10 \text{ USD/kW} \quad ; \quad \text{Hitos}: \text{Curva S de Inversión y FPO}",
        "ejemplo": "Problema 1: Un consorcio tramita la conexión de un parque eólico de 200 MW en Uribia, La Guajira, para conectarse a la subestación Colectora 500 kV del STN. Bajo la Resolución CREG 075 de 2021 (que unificó y endureció los criterios de asignación de capacidad de transporte): 1) El promotor radica ante la UPME el Estudio de Conexión Simplificado y el Estudio de Flujo de Carga, Cortocircuito y Estabilidad Electromecánica en software DigSILENT PowerFactory demostrando que la inyección de 200 MW no sobrecarga las líneas ni provoca colapso de tensión. 2) La UPME aprueba y emite el concepto de conexión viable. 3) Para formalizar la reserva de capacidad y evitar la especulación de puntos de conexión, el promotor debe constituir ante el Administrador del Mercado (XM) una Garantía Bancaria de Reserva de Capacidad a primer requerimiento de 10 USD por cada kilovatio asignado: Garantía = 200,000 kW * 10 USD/kW = 2,000,000 USD. 4) Obligación de Hitos de Construcción: El proyecto debe reportar una Curva S de avance físico y financiero semestral ante la UPME. La Fecha de Puesta en Operación (FPO) oficial se fija para el 1 de diciembre de 2027. Si el proyecto se atrasa más de 12 meses sin fuerza mayor demostrada, la CREG y la UPME cancelan unilateralmente la asignación de capacidad, ejecutan la fianza de 2,000,000 USD y reasignan el punto de conexión en subasta pública al siguiente proyecto en lista de espera. Problema 2: En la ventanilla única de la UPME, los proyectos que presenten superposición geográfica con resguardos indígenas deben certificar el inicio del proceso de consulta previa antes de la aprobación del concepto de conexión definitivo.",
        "bloque_sugerido": "Conexión a Red 45 min • Procedimiento CREG 075/2021, garantías UPME y Curva S de hitos",
        "slides": [
            {
                "numero": 1,
                "seccion": "ACCESO AL SISTEMA DE TRANSMISIÓN",
                "titulo": "La Regulación Anti-Especulación CREG 075",
                "puntos": [
                    "Históricamente, empresas 'de papel' acaparaban los puntos de conexión de la UPME para revenderlos sin construir proyectos.",
                    "La CREG 075 de 2021 estableció un régimen estricto de garantías financieras obligatorias y cronogramas vinculantes.",
                    "Garantía de cumplimiento: Se ejecuta si el proyecto no entra en operación comercial en la fecha aprobada (FPO)."
                ]
            },
            {
                "numero": 2,
                "seccion": "ESTUDIOS ELÉCTRICOS DE CONEXIÓN",
                "titulo": "Validación de Impacto en la Red",
                "puntos": [
                    "Flujo de carga y contingencias N-1: Verifica que las líneas no se sobrecalienten tras el disparo de un circuito.",
                    "Análisis de cortocircuito: Evalúa si las corrientes de falla superan la capacidad de ruptura de los interruptores de subestación.",
                    "Estabilidad transitoria: Simula la respuesta dinámica ante caídas de tensión y fluctuaciones rápidas de viento/sol."
                ]
            }
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Código de Redes (Grid Code): Resoluciones CREG 060 de 2019 y CREG 148 de 2021",
        "objetivo": "Modelar el cumplimiento técnico de plantas solares y eólicas frente a las exigencias del Código de Redes colombiano: soporte ante huecos de tensión (FRT), control P-Q y respuesta rápida en frecuencia.",
        "concepto_clave_latex": r"\text{FRT}: V_{\text{red}} \to 0.0 \text{ p.u.} \text{ durante } 150 \text{ ms sin desconexión} \quad ; \quad \Delta Q = K \cdot (1.0 - V) I_n",
        "ejemplo": "Problema 1: Un parque solar fotovoltaico de 120 MW conectado al STR a 115 kV debe superar las pruebas de cumplimiento del Código de Redes (Resolución CREG 060 de 2019 para FNCER en el SIN). Durante una falla trifásica a tierra en una línea vecina, la tensión en el punto de conexión común (PCC) cae bruscamente a V = 0.15 p.u. (17.25 kV) durante 200 milisegundos antes de que los interruptores de protección despejen la falla: 1) Requisito de Soportabilidad ante Huecos de Tensión (Fault Ride Through - FRT): El parque tiene terminantemente prohibido desconectarse de la red si la tensión permanece por encima del perfil límite de la CREG 060 (tolerancia de tensión cero 0.0 p.u. durante 150 ms, recuperando al 85% en 1.5 segundos). Los inversores deben permanecer sincronizados ininterrumpidamente. 2) Inyección Rápida de Corriente Reactiva: Durante el hueco de tensión (V = 0.15 p.u. < 0.90 p.u.), el controlador de planta PPC (Power Plant Controller) conmuta en menos de 20 milisegundos a modo de soporte de tensión, inyectando corriente reactiva capacitiva proporcional a la caída de tensión: I_q = K * (1.0 - V) * I_n. Con factor de ganancia K = 2.0: I_q = 2.0 * (1.0 - 0.15) * I_n = 2.0 * 0.85 * I_n = 1.70 * I_n (limitado al 100% de la capacidad de corriente máxima del inversor, I_q = 1.0 I_n). Esta inyección masiva de reactivos eleva la tensión local ayudando a despejar la falla. 3) Regulación Primaria de Frecuencia: Cuando la frecuencia del sistema sube por encima de 60.2 Hz (sobre-frecuencia), la planta debe reducir su potencia activa con un estatismo del s = 3% en menos de 2 segundos. La superación de estas pruebas en campo auditadas por XM es condición obligatoria para obtener la certificación de entrada en operación comercial (FPO). Problema 2: En plantas sin inercia mecánica, la función de 'inercia sintética' (Fast Frequency Response - FFR) inyecta potencia activa adicional desde condensadores DC de inversores en menos de 100 ms tras una caída súbita de frecuencia.",
        "bloque_sugerido": "Código de Redes 45 min • Resoluciones CREG 060/2019 y requisitos técnicos FRT / P-Q",
        "slides": [
            {
                "numero": 1,
                "seccion": "ESTÁNDARES TÉCNICOS DE INTERCONEXIÓN",
                "titulo": "De Fuentes Pasivas a Soporte Activo de Red",
                "puntos": [
                    "Las plantas renovables modernas ya no pueden ser simples espectadores pasivos que se desconectan ante cualquier perturbación.",
                    "El Código de Redes (Grid Code) exige que los parques fotovoltaicos y eólicos se comporten igual o mejor que las centrales térmicas tradicionales.",
                    "Resolución CREG 060 de 2019: Marco regulatorio unificado de requerimientos técnicos para plantas solares y eólicas en el SIN."
                ]
            },
            {
                "numero": 2,
                "seccion": "EXIGENCIAS DINÁMICAS CRÍTICAS",
                "titulo": "Soporte FRT y Control de Frecuencia",
                "puntos": [
                    "Fault Ride Through (FRT): Capacidad de soportar caídas drásticas de tensión sin dispararse, inyectando reactivos de apoyo.",
                    "Control de Tensión P-Q: Margen obligatorio de factor de potencia entre 0.95 inductivo y 0.95 capacitivo en el punto de acoplamiento.",
                    "Respuesta rápida de frecuencia (Estatismo): Modulación automática de potencia activa ante desviaciones de los 60 Hz del sistema."
                ]
            }
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Comunidades Energéticas y Usuarios Asociados: CREG 101 028 de 2024 y Decretos Reglamentarios",
        "objetivo": "Estructurar comunidades energéticas y proyectos de generación distribuida asociativa bajo el Decreto 2236 de 2023 y la Resolución CREG 101 028 de 2024, evaluando modelos asociativos y tarifas.",
        "concepto_clave_latex": r"\text{Comunidad Energética}: \text{Asociación de usuarios} \implies \text{Autogeneración Colectiva y Reparto de Excedentes}",
        "ejemplo": "Problema 1: En un barrio de estrato 1 y 2 en Ciénaga, Magdalena, una asociación comunitaria de 120 familias constituye una Comunidad Energética (bajo el Decreto Presidencial 2236 de 2023 y la Resolución CREG 101 028 de 2024). Con cofinanciación estatal del FENOGE y la Gobernación, instalan una granja solar comunitaria de 250 kW_p en un lote comunal baldío conectado al circuito urbano del operador de red (Air-e / Afinia a 13.2 kV). Generación solar mensual promedio: 36,000 kWh/mes. Demanda residencial sumada de las 120 familias: 24,000 kWh/mes (promedio de 200 kWh/familia-mes). Mecanismo de Reparto Asociativo CREG 101 028: 1) Cada familia firma un acuerdo asociativo donde se le asigna un coeficiente de reparto de energía del alpha_i = 1/120 = 0.833% de la generación total (300 kWh asignados por familia al mes). 2) De los 300 kWh generados para cada usuario, 200 kWh compensan el 100% de su consumo mensual de subsistencia, reduciendo su cobro por energía a cero COP. 3) Los 100 kWh restantes por familia (12,000 kWh/mes en total de excedentes de la comunidad) se inyectan a la red y el comercializador los liquida al precio de bolsa horaria (P_bolsa = 260 COP/kWh), generando un ingreso en efectivo para la junta comunitaria de 12,000 * 260 = 3,120,000 COP mensuales. Este fondo comunitario se destina formalmente a la operación, limpieza y seguro de la planta fotovoltaica y a financiar microcréditos locales de conectividad a internet. Problema 2: En comunidades energéticas rurales aisladas de zonas no interconectadas (ZNI), la figura de 'Usuario Asociado' permite que pequeñas micro-redes hidroeléctricas o solares vendan energía prepago entre vecinos sin requerir constituirse como empresas prestadoras ESP de gran capital.",
        "bloque_sugerido": "Comunidades Energéticas 45 min • Marco legal Decreto 2236/2023 y CREG 101 028/2024",
        "slides": [
            {
                "numero": 1,
                "seccion": "DEMOCRATIZACIÓN DE LA ENERGÍA",
                "titulo": "Qué es una Comunidad Energética en Colombia",
                "puntos": [
                    "Personas naturales o jurídicas que se unen para generar, comercializar y consumir su propia energía limpia colectivamente.",
                    "Pueden ser comunidades indígenas, afrodescendientes, campesinas, juntas de acción comunal o barrios urbanos populares.",
                    "El objetivo central es erradicar la pobreza energética y reducir las tarifas eléctricas en los estratos más vulnerables."
                ]
            },
            {
                "numero": 2,
                "seccion": "MODELO REGULATORIO CREG",
                "titulo": "Compensación Remota y Excedentes Colectivos",
                "puntos": [
                    "Permite que la planta de generación esté físicamente ubicada en un predio comunal o techo escolar y beneficie a casas lejanas.",
                    "El operador de red descuenta en la factura de cada miembro su porcentaje de energía generado por la comunidad.",
                    "Exige estatutos asociativos claros, personería jurídica comunitaria y medidores inteligentes homologados."
                ]
            }
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "teorico",
        "titulo": "Regulación de Sistemas de Almacenamiento con Baterías (BESS): CREG 098 de 2019",
        "objetivo": "Evaluar el marco regulatorio para la incorporación de sistemas de almacenamiento de energía con baterías (BESS) a gran escala para alivio de congestión en transmisión y arbitraje.",
        "concepto_clave_latex": r"\text{BESS en STN/STR}: \text{Remuneración regulada por disponibilidad (Anualidad de Inversión + AOM)}",
        "ejemplo": "Problema 1: En la subestación Carreto 110 kV en el departamento del Atlántico, la línea de transmisión regional opera al 98% de su capacidad térmica durante los picos de demanda nocturna de 18:00 a 22:00 h, forzando cortes preventivos de carga o redespacho térmico costoso en la zona (sobrecosto por restricciones en tarifa). La UPME convoca la primera subasta de almacenamiento del país bajo la Resolución CREG 098 de 2019: Instalación de un sistema BESS de 50 MW de potencia y 45 MWh de capacidad de descarga continua (tecnología LiFePO4 de escala de red): 1) Modelo de Remuneración Regulada: El BESS no participa como generador en la bolsa ni hace arbitraje de precios especulativo; su función regulatoria exclusiva es aliviar la congestión de la red de transmisión (Storage as a Transmission Asset - SATA). 2) Se remunera al inversionista mediante un Ingreso Anual Regulado garantizado a 15 años pagado por todos los usuarios del sistema a través del componente D de la tarifa, cubriendo el CAPEX, costo de reposición de celdas a los 10 años y AOM. 3) Despacho Operativo por XM: Cuando la línea de 110 kV supera el 85% de carga, el Centro Nacional de Despacho ordena al BESS inyectar hasta 45 MW instantáneamente en la barra de carga, descongestionando la línea sin arrancar turbinas de gas obsoletas. En horas de la madrugada (01:00 a 05:00 h), el BESS se recarga absorbiendo energía eólica excedente de bajo costo. La instalación ahorra más de 22 millones de dólares anuales en costos de restricciones en la factura regional de energía. Problema 2: En la regulación de servicios auxiliares futuros (Resolución CREG 101 011 de 2023), los BESS privados podrán ofertar regulación secundaria de frecuencia rápida (AGC) y control de tensión recibiendo pagos adicionales por desempeño.",
        "bloque_sugerido": "Regulación de Baterías BESS 45 min • Resolución CREG 098/2019 y almacenamiento como activo de red",
        "slides": [
            {
                "numero": 1,
                "seccion": "BATERÍAS A ESCALA DE TRANSMISIÓN",
                "titulo": "BESS como Activo de Red (SATA)",
                "puntos": [
                    "Evita o posterga la construcción de líneas de alta tensión costosas que tardan entre 5 y 8 años en licenciarse.",
                    "Resuelve problemas de congestión nodal y atrapamiento de energía renovable en cuestión de milisegundos.",
                    "Resolución CREG 098 de 2019: Hito pionero en América Latina para remunerar almacenamiento en el sistema de transporte."
                ]
            },
            {
                "numero": 2,
                "seccion": "FUTURO REGULATORIO DE BESS PRIVADOS",
                "titulo": "Arbitraje y Servicios Complementarios",
                "puntos": [
                    "Permitirá a desarrolladores solares y eólicos coinvertir en baterías (co-located BESS) para aplanar su curva de inyección.",
                    "Capacidad de vender servicios de arranque en negro (Black Start) y soporte de inercia virtual ultra-rápida.",
                    "La reducción global del costo de las baterías de litio y sodio acelera la paridad de red del almacenamiento."
                ]
            }
        ]
    },
    {
        "numero_tema": 20,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Marco Normativo del Hidrógeno y Derivados: Ley 2099 y Hoja de Ruta Nacional",
        "objetivo": "Interpretar la Hoja de Ruta del Hidrógeno de Colombia y la reglamentación técnica de producción, transporte y certificación de origen de hidrógeno verde y azul.",
        "concepto_clave_latex": r"\text{Hidrógeno Verde}: \text{Electrólisis con FNCER} \quad ; \quad \text{Hidrógeno Azul}: \text{Gas Natural + SMR + CCUS}",
        "ejemplo": "Problema 1: Un consorcio petroquímico e industrial proyecta construir una planta de hidrógeno verde en Mamonal, Cartagena, integrada por un parque solar fotovoltaico de 150 MW dedicado y un electrolizador PEM de 80 MW (producción de 12,000 toneladas de H2 verde al año destinadas a la refinería para hidrotratamiento de diésel y exportación como amoníaco verde). Análisis de cumplimiento normativo y fiscal bajo la Ley 2099 de 2021 y el Decreto 1476 de 2022: 1) Clasificación y Definición Legal: El Artículo 21 de la Ley 2099 define expresamente al hidrógeno verde como aquel producido a partir de FNCER o biomasa, y al hidrógeno azul como aquel obtenido de combustibles fósiles con captura de al menos el 85% del CO2. El proyecto clasifica legalmente como Hidrógeno Verde. 2) Beneficios Tributarios Aplicables: Al quedar catalogado como FNCER, el proyecto accede de forma automática a los 4 incentivos de la Ley 1715 (deducción del 50% de renta, 0% IVA, 0% aranceles y depreciación acelerada en 3 años). 3) Certificación de Origen y Huella de Carbono: Para que el amoníaco sea exportable a la Unión Europea bajo la directiva RED II / CertifHy y el mecanismo CBAM (Carbon Border Adjustment Mechanism), la intensidad de emisiones de ciclo de vida del H2 producido no puede superar el umbral estricto de 3.38 kg CO2e por kg de H2. Como el electrolizador se alimenta al 100% con energía solar directa dedicada 'off-grid' (emisión neta = 0.42 kg CO2e/kg H2), el proyecto obtiene la certificación de hidrógeno verde, eximiéndose de pagar el arancel fronterizo de carbono europeo de 85 EUR por tonelada de CO2 evitada. Problema 2: En la inyección de hidrógeno a las redes existentes de gas natural, la Resolución CREG reglamenta los límites máximos de blending en volumen (inicialmente hasta el 5%) garantizando la compatibilidad con estufas domésticas y compresores.",
        "bloque_sugerido": "Normativa del Hidrógeno 45 min • Ley 2099/2021, Hoja de Ruta y certificación de origen verde",
        "slides": [
            {
                "numero": 1,
                "seccion": "LA HOJA DE RUTA DEL HIDRÓGENO",
                "titulo": "Metas de Colombia a 2030",
                "puntos": [
                    "Meta nacional: 1 a 3 GW de capacidad de electrólisis instalada y 50,000 toneladas de H2 verde producidas para 2030.",
                    "La Costa Caribe y La Guajira son identificadas como polos estratégicos de exportación global de amoníaco verde hacia Europa y Asia.",
                    "Sinergia con la industria de fertilizantes: Sustitución de amoníaco fósil importado por urea verde nacional."
                ]
            },
            {
                "numero": 2,
                "seccion": "CERTIFICACIÓN DE ORIGEN Y TRAZABILIDAD",
                "titulo": "Estándares Internacionales (CertifHy / CBAM)",
                "puntos": [
                    "Garantía de Origen (GoO): Pasaporte digital que certifica que cada molécula de H2 fue generada con electricidad 100% limpia.",
                    "El CBAM europeo penalizará fiscalmente las importaciones de acero, cemento y químicos que no demuestren descarbonización.",
                    "Regulación de seguridad técnica: Normas NFPA 2 y códigos ASME B31.12 para tuberías de hidrógeno a alta presión."
                ]
            }
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Consulta Previa (Convenio 169 de la OIT) y Gestión Social en La Guajira",
        "objetivo": "Diseñar y liderar procesos de Consulta Previa libre, previa e informada con comunidades indígenas y afrodescendientes según el Convenio 169 de la OIT y la jurisprudencia de la Corte Constitucional.",
        "concepto_clave_latex": r"\text{Consulta Previa}: \text{Apertura} \to \text{Talleres de Identificación de Impactos} \to \text{Acuerdos Vinculantes} \to \text{Protocolización}",
        "ejemplo": "Problema 1: Una multinacional energética tramita el desarrollo del parque eólico 'Wichimana' de 350 MW y su línea de transmisión asociada de 220 kV en la Alta Guajira, abarcando territorios ancestrales pertenecientes a 8 comunidades del Pueblo Wayuu (organizadas bajo clanes matrilineales Uriana, Epieyu y Pushaina). Procedimiento de Consulta Previa obligatorio bajo el Convenio 169 de la OIT, la Directiva Presidencial 08 de 2020 y sentencias T-129/11 y SU-123/18 de la Corte Constitucional: 1) Solicitud de Certificación de Presencia de Comunidades ante la Dirección de la Autoridad Nacional de Consulta Previa (DANCP) del Ministerio del Interior. 2) Etapa de Pre-consulta: Coordinación de la metodología intercultural con las autoridades tradicionales Wayuu (Alaulayuu) y palabreros (Pütchipü'üi) en su lengua nativa wayuunaiki, garantizando traductores oficiales neutrales. 3) Apertura e Identificación de Impactos Ambientales y Culturales: Análisis de afectación sobre cementerios ancestrales (amuyuwau), sitios sagrados de pastoreo y rutas migratorias de chivos. 4) Formulación de Medidas de Manejo y Acuerdos de Beneficios Compartidos: La empresa acuerda: a) Reubicar 4 aerogeneradores para mantener una distancia de respeto de 800 m con respecto a los cementerios familiares; b) Construcción de una planta desalinizadora de agua de mar de 150 m^3/día alimentada por energía solar para abastecer de agua potable a las 8 rancherías; c) Pago de servidumbre colectiva por ocupación del suelo y reparto de un canon anual del 1.5% de los ingresos brutos de generación en proyectos productivos y becas universitarias. 5) Protocolización del Acta de Cierre ante la Defensoría del Pueblo y la Procuraduría. El cumplimiento estricto y de buena fe de los acuerdos evita paros comunitarios y garantiza la viabilidad social del proyecto a 30 años. Problema 2: En caso de falta de acuerdo en consultas previas donde no exista reasentamiento forzoso de la comunidad, el Estado ejerce el principio de 'ponderación proporcional' permitiendo avanzar el proyecto bajo estrictas medidas de mitigación.",
        "bloque_sugerido": "Consulta Previa y DDHH 45 min • Convenio 169 OIT, jurisprudencia Corte Constitucional y Guajira",
        "slides": [
            {
                "numero": 2,
                "seccion": "DERECHO FUNDAMENTAL COLECTIVO",
                "titulo": "El Convenio 169 de la OIT en Colombia",
                "puntos": [
                    "Derecho fundamental de los pueblos indígenas y tribales a ser consultados de forma previa, libre e informada ante medidas legislativas o proyectos que los afecten.",
                    "No es un simple trámite administrativo de socialización informativa; es un diálogo intercultural vinculante de buena fe.",
                    "No otorga derecho de veto unilateral arbitrario a las comunidades, salvo en casos extremos de reasentamiento o uso de tóxicos (Sentencia SU-123/18)."
                ]
            },
            {
                "numero": 2,
                "seccion": "LECCIONES APRENDIDAS EN LA GUAJIRA",
                "titulo": "Sostenibilidad y Reparto de Beneficios",
                "puntos": [
                    "La fragmentación social y la proliferación de mesas de concertación descoordinadas paralizó más de 2000 MW eólicos entre 2021 y 2023.",
                    "Los proyectos exitosos van más allá de compensaciones económicas individuales, creando alianzas público-populares a largo plazo.",
                    "Acceso al agua, salud, educación y electrificación de las rancherías como compromisos éticos irrenunciables de la ingeniería."
                ]
            }
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Licenciamiento Ambiental para Proyectos de Energía: ANLA y Estudios de Impacto (EIA)",
        "objetivo": "Elaborar y tramitar Estudios de Impacto Ambiental (EIA) y Diagnósticos Ambientales de Alternativas (DAA) ante la ANLA conforme a la Metodología General para la Elaboración de Estudios Ambientales.",
        "concepto_clave_latex": r"\text{EIA} = \{ \text{Línea Base: Abiótico, Biótico, Socioeconómico} \} + \{ \text{Evaluación de Impactos (Conesa)} \} + \text{PMA}",
        "ejemplo": "Problema 1: Un parque solar fotovoltaico de 180 MW de potencia nominal en el Cesar requiere Licencia Ambiental Global de competencia exclusiva de la Autoridad Nacional de Licencias Ambientales (ANLA), dado que su capacidad excede los 100 MW (según el Decreto 1076 de 2015 / Decreto 2041 de 2014; plantas < 100 MW son licenciadas por la Corporación Autónoma Regional Corpocesar): 1) Diagnóstico Ambiental de Alternativas (DAA): No aplica para la planta de generación solar fija, pero sí es exigible para la línea de transmisión de evacuación de 115 kV de 32 km si cruza reservas forestales o ecosistemas sensibles, evaluando dos trazados alternativos mediante análisis multicriterio geográfico. 2) Estudio de Impacto Ambiental (EIA): Se levanta la línea base en temporada seca y de lluvias abarcando el medio abiótico (hidrología, suelos, geomorfología), biótico (flora, fauna, censos de avifauna y quirópteros) y socioeconómico. 3) Matriz de Evaluación de Impactos de Conesa-Fernández: Se evalúa el impacto de 'Pérdida de cobertura vegetal de bosque seco tropical (bs-T)': Importancia ambiental I = +(3*Intensidad + 2*Extensión + Momento + Persistencia + Reversibilidad + Sinergia + Acumulación + Efecto + Periodicidad + Recuperabilidad) = 68 (Impacto Crítico Negativo). 4) Plan de Manejo Ambiental (PMA): Se formulan programas de compensación por pérdida de biodiversidad (Resolución 1447 de 2018): Si se intervienen 140 hectáreas de bosque seco tropical con factor de compensación 1:4, el proyecto debe restaurar ecológicamente 560 hectáreas en áreas prioritarias del Sistema Nacional de Áreas Protegidas (SINAP), además de destinar el 1% de la inversión total (Art. 43 Ley 99/93) a la protección y recuperación de la cuenca hídrica abastecedora. Tras la Audiencia Pública Ambiental y revisión técnica, la ANLA expide la Resolución de Licencia Ambiental en un plazo de 6 meses. Problema 2: En parques eólicos marinos (offshore), los estudios acústicos submarinos durante el hincado de pilotes de monopilote exigen cortinas de burbujas (bubble curtains) para no lesionar el sistema auditivo de cetáceos y peces.",
        "bloque_sugerido": "Licenciamiento ANLA 45 min • Estructuración de EIA, matriz de Conesa y compensación 1%",
        "slides": [
            {
                "numero": 1,
                "seccion": "AUTORIDADES Y COMPETENCIAS AMBIENTALES",
                "titulo": "ANLA vs Corporaciones Autónomas Regionales (CAR)",
                "puntos": [
                    "ANLA: Competente para proyectos de generación de energía con capacidad nominal instalada >= 100 MW.",
                    "CAR (ej. Corpamag, Corpocesar): Competentes para proyectos de generación con capacidad < 100 MW y líneas de distribución local.",
                    "La Licencia Ambiental autoriza de manera integral el aprovechamiento de recursos naturales (concesión de aguas, vertimientos, emisiones, descapote)."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL ESTUDIO DE IMPACTO AMBIENTAL (EIA)",
                "titulo": "Jerarquía de la Mitigación",
                "puntos": [
                    "1. Evitar: Modificar el diseño para no tocar ecosistemas críticos o especies amenazadas (UICN / CITES).",
                    "2. Minimizar: Implementar tecnología para reducir la magnitud del impacto remanente.",
                    "3. Restaurar: Rehabilitar áreas temporalmente degradadas durante la fase de construcción.",
                    "4. Compensar: Último recurso; financiar áreas protegidas equivalentes con factores de multiplicación de 1:2 a 1:10."
                ]
            }
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Mercados de Carbono en Colombia: Impuesto al Carbono, No Causación y Registro RENARE",
        "objetivo": "Estructurar proyectos de mitigación de gases de efecto invernadero comercializando créditos de carbono (VERs/CERs) bajo el Mecanismo de No Causación del Impuesto Nacional al Carbono.",
        "concepto_clave_latex": r"\text{Impuesto Carbono}: \tau \approx 25,000 \text{ COP/tCO}_2\text{e} \quad ; \quad \text{Ahorro No Causación} = \text{Créditos Utilizados} \times \tau",
        "ejemplo": "Problema 1: Un gran distribuidor mayorista de combustibles líquidos en Colombia importa y vende anualmente 120 millones de galones de combustible diésel y gasolina. La Ley 1819 de 2016 y la reforma tributaria Ley 2277 de 2022 gravan la venta e importación de combustibles fósiles con el Impuesto Nacional al Carbono, fijado en una tarifa de 25,799 COP por tonelada de CO2 equivalente emitida (aproximadamente 191 COP por galón de diésel y 169 COP por galón de gasolina). El impuesto total liquidado para el año fiscal es de 21,500,000,000 COP (21.5 mil millones de COP). La empresa decide acogerse al Mecanismo de Carbono Neutralidad / No Causación del Impuesto (Decreto 926 de 2017): 1) La empresa compra en el mercado voluntario de carbono 833,365 créditos de carbono certificados (cada crédito equivale a 1 tCO2e evitada o capturada) provenientes de un proyecto de reforestación comercial y un parque solar fotovoltaico en Colombia, registrados en el sistema oficial RENARE (Registro Nacional de Reducción de Emisiones) del Ministerio de Ambiente y verificados bajo el estándar internacional Gold Standard / Verra VCS. 2) Precio de compra negociado en el mercado privado: 18,500 COP por crédito de carbono. Costo de adquisición de los créditos: Costo = 833,365 * 18,500 = 15,417,252,500 COP. 3) Presentación ante la DIAN del certificado de cancelación voluntaria emitido en RENARE para la no causación del 100% del impuesto al carbono. Ahorro tributario neto en efectivo para la empresa: Ahorro = 21,500,000,000 - 15,417,252,500 = 6,082,747,500 COP anuales (más de 6 mil millones de COP de beneficio económico). Este incentivo canaliza capital privado masivo hacia el financiamiento de proyectos de energía renovable y reforestación en el país. Problema 2: Con el Artículo 65 de la Ley 2277, se establece un límite legal máximo del 50% para la no causación con créditos de carbono, obligando a pagar en dinero en efectivo al menos la mitad del impuesto a la DIAN.",
        "bloque_sugerido": "Mercados de Carbono 45 min • Impuesto al carbono Ley 1819/2277, mecanismo de no causación y RENARE",
        "slides": [
            {
                "numero": 1,
                "seccion": "ECONOMÍA DEL CAMBIO CLIMÁTICO",
                "titulo": "Fijación de Precio al Carbono (Carbon Pricing)",
                "puntos": [
                    "Impuesto al Carbono: Instrumento fiscal que penaliza directamente el contenido de carbono de los combustibles fósiles.",
                    "Mercado de Cupos Transables (ETS / Cap-and-Trade): Fija un límite máximo de emisiones y permite comprar y vender derechos de emisión.",
                    "Colombia fue pionera en el mundo al permitir que las empresas neutralicen su impuesto comprando créditos de proyectos limpios nacionales."
                ]
            },
            {
                "numero": 2,
                "seccion": "EL REGISTRO NACIONAL RENARE",
                "titulo": "Integridad Ambiental y Cero Doble Contabilidad",
                "puntos": [
                    "RENARE (Ministerio de Ambiente): Plataforma digital oficial donde deben inscribirse obligatoriamente todas las iniciativas de mitigación.",
                    "Evita el 'doble conteo' (double counting) de reducciones de emisiones entre empresas y metas país (NDC) del Acuerdo de París.",
                    "Exige validación y verificación independiente por Organismos Evaluadores de la Conformidad (OEC) acreditados por el ONAC."
                ]
            }
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Eficiencia Energética y Normativa PROURE: Auditorías y Etiquetado RETIQ",
        "objetivo": "Aplicar el Programa de Uso Racional y Eficiente de la Energía (PROURE), las exigencias de auditorías energéticas obligatorias y el etiquetado de eficiencia RETIQ según la Resolución 41012 de 2015.",
        "concepto_clave_latex": r"\text{Indicador de Desempeño Energético (EnPI)} = \frac{\text{Consumo de Energía}}{\text{Unidad de Producción}} \quad ; \quad \text{Clases RETIQ}: \text{A (Máxima)} \to \text{G}",
        "ejemplo": "Problema 1: Una planta cervecera e industrial en Barranquilla consume 18,500,000 kWh de energía eléctrica y 85,000 GJ de gas natural al año, con una factura energética anual de 19,200,000,000 COP. La empresa contrata una auditoría energética de Grado 3 (Inversión / Investment-Grade Audit conforme a la norma ISO 50002) para cumplir las metas del plan PROURE del Ministerio de Minas y Energía: 1) Balances energéticos y descomposición por usos significativos de la energía (SEU): Compresores de aire comprimido (28%), salas de cocción y calderas de vapor (42%), motores de bombeo (18%) y refrigeración industrial (12%). 2) Implementación de Medidas de Eficiencia Energética (URE): a) Reemplazo de 24 motores eléctricos de eficiencia estándar IE1 por motores de ultra-alta eficiencia IE4 'Super Premium' con variadores de frecuencia VFD certificados bajo el reglamento RETIQ (Resolución 41012 de 2015): Inversión CAPEX = 320,000,000 COP, ahorro eléctrico medido = 8.5% (1,572,500 kWh/año = 1,336,625,000 COP/año, periodo simple de retorno de inversión Payback = 320 / 1336 = 0.24 años, menos de 3 meses). b) Reparación integral de fugas de aire comprimido detectadas con cámara acústica ultrasónica: 48 fugas eliminadas que ahorran 45 kW de potencia continua de compresor (394,200 kWh/año = 335,070,000 COP anuales con costo de reparación de 15,000,000 COP). 3) Certificación del Sistema de Gestión de la Energía bajo ISO 50001: La planta reduce su intensidad energética en un 14.2%, accediendo a beneficios tributarios de exclusión de IVA y descuento en renta del 50% de la inversión en equipos eficientes avalados por la UPME. Problema 2: En la comercialización de electrodomésticos y equipos de climatización, el reglamento RETIQ prohíbe taxativamente la venta en territorio nacional de acondicionadores de aire con factor de rendimiento estacional (CSPF) inferior a la Clase C.",
        "bloque_sugerido": "Eficiencia PROURE y RETIQ 45 min • Auditorías ISO 50002, etiquetado RETIQ y gestión ISO 50001",
        "slides": [
            {
                "numero": 1,
                "seccion": "USO RACIONAL DE LA ENERGÍA",
                "titulo": "El Programa PROURE en Colombia",
                "puntos": [
                    "Marco de política pública nacional que fija metas vinculantes de ahorro de energía para la industria, transporte y sector residencial.",
                    "La eficiencia energética es el 'primer combustible del mundo': la energía más limpia y barata es la que NO se necesita generar.",
                    "ISO 50001: Norma internacional para establecer Líneas Base de Energía (EnB) e Indicadores de Desempeño Energético (EnPI)."
                ]
            },
            {
                "numero": 2,
                "seccion": "REGLAMENTO TÉCNICO RETIQ",
                "titulo": "Etiquetado Obligatorio de Equipos",
                "puntos": [
                    "RETIQ (Reglamento Técnico de Etiquetado): Exige que todo motor, refrigerador o transformador comercializado exhiba su etiqueta de eficiencia.",
                    "Clasificación de eficiencia de la A a la G: Protege a los consumidores contra equipos obsoletos importados de alto consumo.",
                    "Obliga a fabricantes e importadores a certificar sus productos en laboratorios de ensayo acreditados por ONAC."
                ]
            }
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Reglamento Técnico de Instalaciones Eléctricas (RETIE) en Sistemas de Generación",
        "objetivo": "Interpretar y aplicar las disposiciones obligatorias del RETIE en el diseño, montaje y certificación plena de centrales de generación, subestaciones y puestas a tierra.",
        "concepto_clave_latex": r"V_{\text{paso}} \le \frac{1000 + 6 C_s \rho_s}{\sqrt{t}} \cdot 0.116 \quad ; \quad V_{\text{contacto}} \le \frac{1000 + 1.5 C_s \rho_s}{\sqrt{t}} \cdot 0.116",
        "ejemplo": "Problema 1: Se diseña la malla de puesta a tierra y las distancias de seguridad de la subestación elevadora de 34.5/110 kV de una central solar según los requisitos obligatorios del RETIE (Resolución 90708 de 2013 y actualizaciones MinEnergía): 1) Cálculo de Tensiones Máximas Tolerables de Paso y Contacto (Metodología IEEE Std 80 adoptada por el RETIE): Para un tiempo de despeje de falla a tierra por los relés de protección de t = 0.50 segundos, suelo con capa superficial de gravilla triturada de 10 cm (resistividad rho_s = 3000 ohm*m, factor de reducción C_s = 0.74): Tensión de contacto admisible: V_contacto = [(1000 + 1.5 * 0.74 * 3000) / sqrt(0.50)] * 0.116 = [(1000 + 3330) / 0.7071] * 0.116 = [4330 / 0.7071] * 0.116 = 6123.6 * 0.116 = 710.3 V. Tensión de paso admisible: V_paso = [(1000 + 6.0 * 0.74 * 3000) / sqrt(0.50)] * 0.116 = [(1000 + 13320) / 0.7071] * 0.116 = [14320 / 0.7071] * 0.116 = 20251.7 * 0.116 = 2349.2 V. La simulación de la cuadrícula de malla con conductor de cobre desnudo 4/0 AWG y 16 varillas copperweld calcula tensiones de contacto reales de 420 V y de paso de 890 V, ambas inferiores a los límites del RETIE, evitando electrocución por choque ventricular. 2) Distancias Mínimas de Seguridad al Aire en 110 kV: Distancia mínima fase-fase = 1100 mm; distancia fase-tierra = 950 mm; altura mínima de partes energizadas sobre el nivel del suelo = 4.0 metros. 3) Certificación Plena RETIE: Se contrata un Organismo de Inspección acreditado por el ONAC que emite el Dictamen de Conformidad RETIE para la planta solar, subestación y línea de transmisión, documento indispensable exigido por el Operador de Red para energizar la conexión. Problema 2: En instalaciones solares en techos comerciales, el RETIE exige dispositivos de desconexión rápida (Rapid Shutdown) a nivel de módulo para reducir la tensión del arreglo por debajo de 30 V en menos de 30 segundos protegiendo al cuerpo de bomberos ante incendios.",
        "bloque_sugerido": "Normativa RETIE 45 min • Cálculo de tensiones de paso/contacto IEEE 80 y dictamen ONAC",
        "slides": [
            {
                "numero": 1,
                "seccion": "SEGURIDAD ELÉCTRICA EN COLOMBIA",
                "titulo": "Objetivos y Alcance del RETIE",
                "puntos": [
                    "Reglamento Técnico de Instalaciones Eléctricas: Ley técnica obligatoria que busca preservar la vida humana, animal y el medio ambiente.",
                    "Aplica a todas las instalaciones de generación, transmisión, distribución y uso final de la electricidad en Colombia.",
                    "Ninguna instalación puede ser energizada por el operador de red sin el Dictamen de Inspección de Conformidad RETIE."
                ]
            },
            {
                "numero": 2,
                "seccion": "ASPECTOS TÉCNICOS CRÍTICOS",
                "titulo": "Puestas a Tierra y Distancias de Seguridad",
                "puntos": [
                    "Sistemas de Puesta a Tierra (SPT): Deben garantizar que las corrientes de falla se disipen sin crear tensiones de paso o contacto letales.",
                    "Distancias de seguridad: Espaciamientos físicos mínimos obligatorios entre conductores vivos y personas, edificios o vías públicas.",
                    "Productos certificados: Todo cable, interruptor, transformador y fusible debe contar con certificado de producto de tercera parte."
                ]
            }
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Regulación del Transporte y Comercialización de Gas Natural (CREG 186 y 080)",
        "objetivo": "Modelar el mercado mayorista de gas natural en Colombia, calculando tarifas de transporte reguladas por distancia y estampilla, cargos de capacidad y contratos de suministro bajo CREG 186 de 2020.",
        "concepto_clave_latex": r"\text{Tarifa de Transporte}: T = \text{Cargo Capacidad (USD/kpd-mes)} + \text{Cargo Volumétrico (USD/kpc)}",
        "ejemplo": "Problema 1: Una central termoeléctrica de ciclo combinado de 400 MW en Barranquilla consume 65,000 miles de pies cúbicos diarios de gas natural (65,000 kpd = 65 MBTU/día). La planta suscribe un contrato de transporte de gas natural con el transportador del gasoducto troncal Ballena-Barranquilla (TGI / Promigas) regulado por la Resolución CREG 186 de 2020 y CREG 080: 1) Estructura Tarifaria Binomia: La tarifa de transporte regulada se compone de un cargo por capacidad de reserva firme de tubería (C_cap = 1.15 USD por kpd reservado al mes) y un cargo volumétrico variable por gas efectivamente transportado (C_vol = 0.085 USD por kpc transportado). 2) Reserva de Capacidad Firme: La central reserva una capacidad firme contratada de 70,000 kpd durante todo el año para garantizar suministro continuo sin interrupciones. Costo mensual fijo de capacidad: Cargo_fijo = 70,000 kpd * 1.15 USD/kpd-mes = 80,500 USD/mes. 3) En un mes donde la central opera al 80% de factor de planta transportando un total volumétrico de 1,560,000 kpc de gas: Costo variable volumétrico: Cargo_variable = 1,560,000 kpc * 0.085 USD/kpc = 132,600 USD/mes. Costo total de transporte en el mes: Total_transporte = 80,500 + 132,600 = 213,100 USD. 4) Mercado Secundario de Gas: Durante un periodo de mantenimiento programado de 10 días de la turbina, la central libera 50,000 kpd de su capacidad de transporte no utilizada en el Mercado Secundario de Gas gestionado por el Gestor del Mercado (Bolsa Mercantil de Colombia), vendiendo la capacidad ociosa a una refinería a 0.95 USD/kpd-mes y recuperando 15,833 USD de costos fijos. Problema 2: En contratos de suministro de gas de producción nacional, las modalidades contractuales de la CREG (Firmeza Condicionada, Opción de Compra de Gas y Pague lo Contratado / Take-or-Pay) determinan qué agente asume el riesgo de declinación de los yacimientos maduros.",
        "bloque_sugerido": "Mercado del Gas 45 min • Resoluciones CREG 186/2020, tarifas de transporte y mercado secundario",
        "slides": [
            {
                "numero": 1,
                "seccion": "TRANSPORTE REGULADO DE GAS",
                "titulo": "Sistemas de Transporte por Red en Colombia",
                "puntos": [
                    "Dos grandes sistemas troncales: Sistema de la Costa Caribe (Promigas) y Sistema del Interior (TGI).",
                    "Regulación de Acceso Abierto: Los transportadores no pueden negar capacidad disponible a ningún remitente.",
                    "Tarifas reguladas por la CREG mediante metodología de ingreso máximo con cargos de capacidad y distancia."
                ]
            },
            {
                "numero": 2,
                "seccion": "CONTRATACIÓN Y GESTOR DEL MERCADO",
                "titulo": "El Mercado Mayorista de Gas Natural",
                "puntos": [
                    "Mercado Primario: Contratos negociados entre productores (Ecopetrol, Canacol) y grandes consumidores o distribuidores.",
                    "Mercado Secundario: Negociación de excedentes temporales de gas y capacidad de transporte a través de la Bolsa Mercantil.",
                    "Gas Natural Licuado (GNL): Terminal de Regasificación de SPEC en Cartagena como respaldo estratégico de las termoeléctricas."
                ]
            }
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Transición Energética Justa: Política Nacional, Descarbonización y Reconversión",
        "objetivo": "Analizar la Hoja de Ruta de la Transición Energética Justa (TEJ) en Colombia, formulando planes de reconversión laboral, cierre gradual de minas de carbón y diversificación económica regional.",
        "concepto_clave_latex": r"\text{TEJ} = \text{Descarbonización} \cap \text{Justicia Social} \cap \text{Soberanía Energética} \cap \text{Reconversión Laboral}",
        "ejemplo": "Problema 1: En los departamentos del Cesar y La Guajira, la minería de carbón térmico a cielo abierto genera aproximadamente 28,000 empleos directos e indirectos y aporta más del 45% del PIB departamental a través de regalías mineras e impuestos locales. Ante la caída de la demanda internacional de carbón y los compromisos de neutralidad climática a 2050 asumidos por Colombia en su NDC (reducción del 51% de GEI a 2030): Se diseña un Plan Departamental de Transición Energética Justa (TEJ) bajo las directrices del Ministerio de Minas y Energía: 1) Reconversión y Cierre Gradual de Activos Fósiles: Cronograma ordenado de desmantelamiento de tajos mineros agotados con remediación ambiental de pasivos mineros y estabilización hidrogeológica de botaderos. 2) Reconversión Laboral y Capacitación Técnica: Se articula un programa interinstitucional entre el SENA y la Universidad del Magdalena para reentrenar a 4,500 técnicos y operadores mineros de maquinaria pesada en competencias de montaje electromecánico, soldadura especializada y mantenimiento preventivo de parques solares y eólicos. 3) Sustitución de Regalías Fósiles por Canon de Energía Limpia: La Ley 2099 y la reforma al Sistema General de Regalías asignan transferencias directas del 6% de las ventas de energía de parques solares y eólicos a los municipios productores para financiar proyectos de agroindustria sostenible, acueductos comunitarios y turismo ecológico. 4) Inclusión Comunitaria: El 30% de las microempresas de transporte y alimentación para la fase constructiva se reserva obligatoriamente para cooperativas locales y ex-trabajadores mineros, garantizando que la descarbonización no devenga en desolación económica territorial. Problema 2: En la reconversión de termoeléctricas de carbón antiguas, el estudio de viabilidad evalúa la reutilización de la turbina de vapor y el alternador síncrono transformándolos en condensadores síncronos para brindar inercia a la red.",
        "bloque_sugerido": "Transición Energética Justa 45 min • Hoja de Ruta TEJ, reconversión laboral en carbón y regalías",
        "slides": [
            {
                "numero": 1,
                "seccion": "EL CONCEPTO DE JUSTICIA ENERGÉTICA",
                "titulo": "Más Allá de la Mera Sustitución Tecnológica",
                "puntos": [
                    "Una transición que destruya economías locales y aumente el desempleo NO es sostenible ni éticamente admisible.",
                    "Justicia Distributiva: Acceso universal a energía asequible y reparto equitativo de los beneficios económicos.",
                    "Justicia Procedimental: Participación vinculante de los trabajadores y comunidades en la toma de decisiones territoriales.",
                    "Justicia Restaurativa: Reparación de los pasivos ambientales históricos dejados por la explotación de hidrocarburos."
                ]
            },
            {
                "numero": 2,
                "seccion": "DIVERSIFICACIÓN ECONÓMICA TERRITORIAL",
                "titulo": "Sustitución de la Renta Minero-Energética",
                "puntos": [
                    "Aprovechamiento del potencial solar del Caribe para crear polos de reindustrialización nacional de acero verde y fertilizantes.",
                    "Formación de talento humano especializado: Ingenieros energéticos como líderes técnicos del nuevo modelo productivo.",
                    "Soberanía energética: Reducción de la dependencia macroeconómica de las exportaciones de petróleo y carbón."
                ]
            }
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Solución de Controversias en el Sector Energético: Arbitraje CIADI, CCI y Estabilidad Jurídica",
        "objetivo": "Analizar los mecanismos alternativos de solución de controversias (MASC) en contratos energéticos internacionales, evaluando cláusulas arbitrales (CCI, CIADI) y tratados bilaterales de inversión (TBI).",
        "concepto_clave_latex": r"\text{Cláusula Arbitral}: \text{Jurisdicción Arbitral Internacional (CIADI / CCI)} \implies \text{Renuncia a Vía Judicial Ordinaria}",
        "ejemplo": "Problema 1: Un consorcio de inversionistas europeos y un Estado soberano firman un contrato de concesión para el desarrollo de un parque eólico marino de 400 MW con una inversión extranjera directa de 750 millones de dólares, amparado por un Tratado Bilateral de Inversión (TBI) y el Convenio CIADI (Centro Internacional de Arreglo de Diferencias Relativas a Inversiones del Banco Mundial). Tras la construcción del 60% de la planta, el gobierno promulga un decreto de emergencia tarifaria que congela unilateralmente las tarifas de compra de energía pactadas en el PPA por 10 años, reduce los incentivos tributarios de amortización acelerada e impone un impuesto extraordinario a la generación limpia del 25%: 1) Tipificación de la Controversia Jurídica Internacional: El consorcio activa la cláusula de resolución de disputas del TBI invocando la violación del estándar de 'Trato Justo y Equitativo' (Fair and Equitable Treatment - FET) y la comisión de una 'Expropiación Indirecta o Regulatoria' (Indirect Expropriation), al destruir la rentabilidad económica esperada del proyecto sin indemnización adecuada. 2) Período de Enfriamiento y Notificación de Disputa (Cooling-off Period de 6 meses). 3) Demanda Arbitral ante el Tribunal CIADI en Washington D.C. bajo el Reglamento de Arbitraje de la CNUDMI / UNCITRAL: El tribunal arbitral independiente de tres árbitros internacionales analiza la doctrina de los derechos adquiridos y la confianza legítima del inversionista. El tribunal falla a favor de la empresa demandante, condenando al Estado al pago de una indemnización compensatoria de 340 millones de dólares por daño emergente y lucro cesante futuro, amparado bajo la Convención de Nueva York de 1958 para la ejecución forzosa de laudos arbitrales extranjeros en activos estatales en el exterior. Problema 2: En contratos PPA privados locales en Colombia, la cláusula de arbitraje ante el Centro de Arbitraje y Conciliación de la Cámara de Comercio de Bogotá (CCB) resuelve disputas técnicas y comerciales en menos de 12 meses frente a los 8 a 12 años de la justicia ordinaria.",
        "bloque_sugerido": "Arbitraje Internacional 45 min • Litigio CIADI/CCI, tratados TBI y estabilidad contractual",
        "slides": [
            {
                "numero": 1,
                "seccion": "SEGURIDAD JURÍDICA E INVERSIÓN",
                "titulo": "Mecanismos Internacionales de Protección",
                "puntos": [
                    "Los megaproyectos energéticos conllevan inversiones de capital masivas a horizontes de 20 a 30 años.",
                    "Los inversionistas exigen neutralidad jurídica frente a la interferencia política de los gobiernos de turno.",
                    "Tratados Bilaterales de Inversión (TBI): Protegen contra la expropiación sin justa compensación y la discriminación regulatoria."
                ]
            },
            {
                "numero": 2,
                "seccion": "ARBITRAJE COMERCIAL E INVERSIÓN",
                "titulo": "Tribunales CIADI y Cámara de Comercio Internacional (CCI)",
                "puntos": [
                    "Arbitraje CIADI (Banco Mundial): Exclusivo para disputas entre inversionistas extranjeros privados y Estados soberanos.",
                    "Arbitraje CCI (Cámara de Comercio Internacional): Estándar por excelencia para litigios comerciales entre empresas privadas.",
                    "Laudo Arbitral Definitivo: Tiene fuerza de cosa juzgada vinculante y es ejecutable internacionalmente (Convención de Nueva York)."
                ]
            }
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Modelos Regulatorios Internacionales Comparados: PJM, Mercado Ibérico (OMIE) y FERC",
        "objetivo": "Comparar la arquitectura de mercados eléctricos mayoristas internacionales (el mercado de precios nodales PJM en EE.UU., el mercado zonal OMIE en España/Portugal y la FERC) frente al modelo colombiano.",
        "concepto_clave_latex": r"\text{LMP}_i = \lambda_{\text{energía}} + \text{LMP}_i^{\text{congestión}} + \text{LMP}_i^{\text{pérdidas}} \quad [\text{Precios Marginales Locacionales PJM}]",
        "ejemplo": "Problema 1: Se compara el modelo de mercado eléctrico colombiano (mercado uninodal con precio marginal de bolsa único nacional y compensación separada de restricciones en tarifa) con el mercado eléctrico PJM Interconnection de Estados Unidos (mercado multinodal basado en Precios Marginales Locacionales - Locational Marginal Pricing / LMP supervisado por la FERC): En PJM, la red de más de 10,000 barras calcula cada 5 minutos un precio LMP diferenciado para cada subestación individual: LMP_i = Componente_energía + Componente_congestión_i + Componente_pérdidas_i. En una hora pico: Componente base del sistema = 45 USD/MWh. En el Nodo A (zona saturada con 8,000 MW de parques eólicos y líneas de transmisión congestionadas que impiden evacuar la potencia): La congestión local fuerza un LMP_A = 45 - 38 + 2 = 9 USD/MWh (precio muy bajo que desincentiva económicamente inyectar más energía allí). En el Nodo B (gran centro urbano de consumo industrial con déficit de generación local): La congestión fuerza a importar energía por rutas indirectas saturadas, resultando en LMP_B = 45 + 55 + 4 = 104 USD/MWh (señal económica explícita que incentiva la instalación de baterías BESS o generación distribuida local). Ventaja frente al modelo colombiano: El modelo PJM transparenta y localiza los cuellos de botella de la red directamente en el precio del nodo, eliminando el opaco cobro globalizado de restricciones R que pagan por igual todos los usuarios en Colombia sin importar su ubicación. Problema 2: En el Mercado Ibérico de la Electricidad (MIBEL / OMIE), el mecanismo de acoplamiento de mercados diarios (Euphemia) optimiza el despacho simultáneo de España, Portugal y Francia mediante la asignación implícita de capacidad de interconexión fronteriza.",
        "bloque_sugerido": "Regulación Comparada 45 min • Mercados multinodales LMP (PJM), FERC y modelo ibérico OMIE",
        "slides": [
            {
                "numero": 1,
                "seccion": "DIVERSIDAD DE DISEÑOS DE MERCADO",
                "titulo": "Mercado Uninodal vs Multinodal (LMP)",
                "puntos": [
                    "Mercado Uninodal (Colombia): Un solo precio marginal para todo el país; las congestiones se pagan aparte como 'restricciones'.",
                    "Mercado Multinodal LMP (PJM, California CAISO, Texas ERCOT): Cada nodo de la red tiene su propio precio de electricidad.",
                    "La señal locacional (LMP) guía con precisión matemática dónde es rentable construir nuevas plantas o líneas de transmisión."
                ]
            },
            {
                "numero": 2,
                "seccion": "TENDENCIAS REGULATORIAS GLOBALES",
                "titulo": "Remuneración de Flexibilidad y Capacidad",
                "puntos": [
                    "FERC (Federal Energy Regulatory Commission): Orden 841 (elimina barreras al almacenamiento) y Orden 2222 (agrega DERs y prosumidores).",
                    "Mercados Zonales Europeos: Separación de áreas de precio por congestión estructural (ej. Suecia y Noruega en 4 zonas de precio).",
                    "Colombia avanza en estudios regulatorios para transicionar gradualmente hacia un esquema de precios nodales LMP."
                ]
            }
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "teorico",
        "titulo": "Regulación de Redes Inteligentes (Smart Grids): Infraestructura AMI, Agregadores y Mercados P2P",
        "objetivo": "Diseñar marcos normativos para la digitalización de la red eléctrica regulando la Infraestructura de Medición Avanzada (AMI), agregadores de demanda, recursos energéticos distribuidos (DER) y comercio P2P mediante contratos inteligentes Blockchain.",
        "concepto_clave_latex": r"\text{Tarifas Horarias (ToU)}: \text{Punta} \to \text{Valle} \to \text{Super-Valle} \quad ; \quad \text{P2P Trading}: \text{Smart Contracts ERC-20}",
        "ejemplo": "Problema 1: La CREG y el Ministerio de Minas y Energía expiden la regulación definitiva para el despliegue obligatorio de Infraestructura de Medición Avanzada (AMI - Smart Meters) y agregadores de demanda en Colombia: 1) Plan de Despliegue AMI: Los operadores de red deben reemplazar gradualmente el 75% del parque de medidores electromecánicos por medidores inteligentes bidireccionales con comunicación inalámbrica celular (LTE-M / NB-IoT) o PLC. 2) Tarifas Multirrango Horarias (Time-of-Use - ToU): La tarifa tradicional monomia fija se reemplaza por tres periodos horarios dinámicos: Horas Valle (23:00 a 06:00 h, tarifa = 380 COP/kWh), Horas Llanas (06:00 a 18:00 h, tarifa = 650 COP/kWh) y Horas Pico (18:00 a 22:00 h, tarifa = 1180 COP/kWh). 3) Agregador de Recursos Energéticos Distribuidos (DER Aggregator): Una empresa comercializadora virtual agrega la flexibilidad de 3,500 hogares residenciales dotados de sistemas solares fotovoltaicos, baterías domésticas y cargadores inteligentes de vehículos eléctricos (capacidad agregada total = 18 MW / 36 MWh). Cuando el Centro Nacional de Despacho emite una orden de reducción de demanda por sobrecarga de la red a las 19:30 h, el agregador envía una señal digital a los inversores domésticos para que descarguen sus baterías y detengan la carga de los autos durante 45 minutos. Los usuarios reciben una compensación económica de 850 COP por cada kWh de alivio entregado. 4) Mercado Local Peer-to-Peer (P2P): Mediante contratos inteligentes en tecnología Blockchain (Ethereum / Hyperledger), un vecino que tiene excedentes solares le vende directamente energía limpia a su vecino que está cargando su auto eléctrico sin intermediación del comercializador tradicional, liquidando los cargos de red (D y T) automáticamente. Problema 2: En la gestión de datos masivos de AMI, la regulación de ciberseguridad y protección de datos personales (Habeas Data) exige cifrado de grado militar AES-256 para evitar el secuestro remoto de la infraestructura eléctrica nacional.",
        "bloque_sugerido": "Smart Grids y Futuro 45 min • Regulación AMI, tarifas ToU, agregadores de demanda y P2P",
        "slides": [
            {
                "numero": 1,
                "seccion": "DIGITALIZACIÓN DE LA DISTRIBUCIÓN",
                "titulo": "Infraestructura de Medición Avanzada (AMI)",
                "puntos": [
                    "AMI no es solo un medidor digital; es una red bidireccional de comunicaciones, gestión de datos (MDMS) y sensores de red.",
                    "Permite la lectura remota en tiempo real, desconexión/reconexión instantánea sin cuadrillas y detección automática de cortes y fallas.",
                    "Empodera al usuario consumidor transformándolo en 'Prosumidor' activo (productor y consumidor consciente de energía)."
                ]
            },
            {
                "numero": 2,
                "seccion": "NUEVOS MODELOS DE NEGOCIO ENERGÉTICO",
                "titulo": "Agregadores de Demanda y Comercio P2P",
                "puntos": [
                    "Plantas de Potencia Virtuales (VPP): Agrupan miles de pequeñas baterías caseras y techos solares para operar como una megacentral.",
                    "Respuesta a la Demanda (Demand Response): Remunera a los usuarios por modificar o posponer su consumo en horas pico.",
                    "Culminación de la formación regulatoria y jurídica del Ingeniero Energético de la Universidad del Magdalena."
                ]
            }
        ]
    }
]

def main():
    yaml_text = format_topics_yaml(topics_04031827)
    marker = '      - codigo: "06011840"'
    inject_topics_after(marker, yaml_text)
    print("04031827 Legislación y Regulación Energética successfully expanded to 30 topics!")

if __name__ == '__main__':
    main()
