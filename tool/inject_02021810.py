# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics_10_to_20 = [
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Dinámica del Movimiento Circular y Fuerzas Centrales",
        "objetivo": "Modelar fuerzas centrípetas y efectos de inercia rotacional en componentes giratorios de turbinas.",
        "concepto_clave_latex": r"\sum F_r = m a_c = m \frac{v^2}{R} = m \omega^2 R \quad ; \quad v_{\text{peralte}} = \sqrt{R g \tan(\theta)}",
        "ejemplo": """CLASE MAGISTRAL: DINÁMICA DE FUERZAS CENTRALES Y ROTACIÓN
1. Fuerza Centrípeta vs Fuerza Centrífuga:
En un sistema de referencia inercial, la fuerza centrípeta no es una nueva fuerza de la naturaleza, sino la resultante neta de las fuerzas reales (tensión, fricción, gravedad, normal) dirigida hacia el centro de curvatura para producir aceleración normal a_c = v^2/R.
2. Curvas con Peralte y Fatiga por Tracción Centrífuga:
El ángulo de peralte theta permite que la componente horizontal de la fuerza normal suministre la fuerza centrípeta sin depender de la fricción neumático-asfalto. En las palas de una turbina eólica, la rotación induce esfuerzos de tracción centrífuga masivos en la raíz del álabe.
3. Problema Resuelto 1 (Aplicación Directa):
Una curva en una carretera de acceso a una subestación tiene un radio de curvatura R = 80 m. Calcule el ángulo de peralte theta requerido para que un camión pesado que transporta un transformador a v = 72 km/h (20 m/s) tome la curva de manera segura sin requerir fricción lateral.
Solución:
Velocidad v = 20 m/s, g = 9.81 m/s^2, R = 80 m.
Condición de no fricción:
N * sin(theta) = m * v^2 / R
N * cos(theta) = m * g
Dividiendo ambas ecuaciones:
tan(theta) = v^2 / (R * g)
tan(theta) = (20)^2 / (80 * 9.81) = 400 / 784.8 = 0.5097.
theta = arctan(0.5097) = 27.01° de inclinación transversal de la calzada.
4. Problema Resuelto 2 (Nivel Examen Parcial):
La pala de un aerogenerador tiene una masa m = 8,000 kg distribuida a lo largo de su longitud L = 50 m con centro de gravedad ubicado a r_cg = 20 m del eje del rotor. Si el rotor gira a una velocidad nominal omega = 15 rpm, determine la fuerza de tracción centrípeta neta ejercida en los pernos de unión de la raíz de la pala al buje (hub).
Solución:
Velocidad angular en rad/s:
omega = 15 * (2 * pi / 60) = 1.5708 rad/s.
Aceleración centrípeta del centro de masa:
a_c = omega^2 * r_cg = (1.5708)^2 * 20 = 2.4674 * 20 = 49.35 m/s^2.
Fuerza centrípeta en la raíz:
F_c = m * a_c = (8,000 kg) * (49.35 m/s^2) = 394,784 N = 394.78 kN.
Esta carga cíclica de casi 40 toneladas de tracción debe soportarse de forma permanente junto a la flexión aerodinámica.""",
        "bloque_sugerido": "Pomodoro 50/10 • Cargas centrífugas en álabes y peralte",
        "slides": [
            {"numero": 1, "seccion": "DINÁMICA", "titulo": "Fuerza Centrípeta", "puntos": ["Resultante neta F_r = m omega^2 R dirigida hacia el centro.", "Diferenciación entre marco inercial y marco no inercial rotatorio."]},
            {"numero": 2, "seccion": "APLICACIÓN", "titulo": "Peralte y Rotores Eólicos", "puntos": ["Condición analítica de diseño tan(theta) = v^2 / (R g).", "Tracción en la raíz de álabes de aerogeneradores de gran escala."]}
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Sistemas de Partículas, Centro de Masa y Sistemas de Masa Variable",
        "objetivo": "Calcular centros de masa de sólidos continuos y aplicar la ecuación de Tsiolkovsky para propulsión.",
        "concepto_clave_latex": r"\vec{r}_{\text{cm}} = \frac{1}{M}\int \vec{r}\,dm \quad ; \quad m \frac{d\vec{v}}{dt} = \vec{F}_{\text{ext}} + \vec{v}_{\text{rel}}\frac{dm}{dt}",
        "ejemplo": """CLASE MAGISTRAL: CENTRO DE MASA Y DINÁMICA DE MASA VARIABLE
1. Definición y Propiedades del Centro de Masa (CM):
El centro de masa es el punto geométrico ponderado por masa donde actúa la fuerza gravitacional neta externa. Para una distribución continua con densidad volumétrica rho, r_cm = (1/M) int r dm.
2. Teorema del Movimiento del Centro de Masa:
El CM se mueve como si toda la masa del sistema estuviera concentrada en él y todas las fuerzas externas estuvieran aplicadas allí: sum F_ext = M * a_cm.
3. Ecuación de Movimiento de Masa Variable (Ecuación de Tsiolkovsky):
Aplica la conservación del momentum a sistemas abiertos donde la masa entra o sale con velocidad relativa v_rel (combustibles en cohetes, bandas transportadoras de carbón o tolvas de biomasa).
4. Problema Resuelto 1 (Aplicación Directa):
Determine la posición del centro de masa de una varilla delgada no homogénea de longitud L = 2.0 m cuya densidad lineal de masa varía linealmente desde el extremo x = 0 según lambda(x) = k * x, donde k = 1.5 kg/m^2.
Solución:
Masa total M:
M = int_0^L lambda(x) dx = int_0^2 (1.5 x) dx = [ 1.5 * x^2 / 2 ]_0^2 = 0.75 * 4 = 3.0 kg.
Momento de masa respecto al origen:
int_0^L x * dm = int_0^2 x * (1.5 x dx) = 1.5 int_0^2 x^2 dx = 1.5 * [ x^3 / 3 ]_0^2 = 1.5 * (8 / 3) = 4.0 kg*m.
Posición del CM:
x_cm = (int x dm) / M = 4.0 / 3.0 = 1.333 m desde el extremo más liviano (x = 0).
5. Problema Resuelto 2 (Nivel Examen Parcial):
Una tolva alimenta carbón triturado sobre una banda transportadora horizontal a una tasa constante dm/dt = 120 kg/s desde el reposo. La banda se desplaza a una velocidad constante v = 2.5 m/s. Calcule la fuerza horizontal F que debe ejercer el motor exclusivamente para acelerar el carbón y la potencia mecánica disipada en el impacto.
Solución:
Ecuación de masa variable:
F = dp/dt = d(m * v) / dt = m * (dv/dt) + v * (dm/dt).
Como v = constante (dv/dt = 0):
F = v * (dm/dt) = 2.5 m/s * 120 kg/s = 300 N.
Potencia mecánica suministrada por el motor:
P_motor = F * v = 300 N * 2.5 m/s = 750 W.
Tasa de aumento de energía cinética del carbón:
dK/dt = 0.5 * (dm/dt) * v^2 = 0.5 * 120 * (2.5)^2 = 60 * 6.25 = 375 W.
Potencia disipada como calor por fricción en el impacto inicial:
P_disipada = P_motor - dK/dt = 750 - 375 = 375 W (exactamente el 50% de la potencia).""",
        "bloque_sugerido": "Laboratorio 50 min • Centro de masa e integración continua",
        "slides": [
            {"numero": 1, "seccion": "CENTRO MASA", "titulo": "Distribuciones Continuas de Masa", "puntos": ["Integral de momento espacial r_cm = (1/M) int r dm.", "Cálculo de centroide en geometrías compuestas de palas y torres."]},
            {"numero": 2, "seccion": "MASA VARIABLE", "titulo": "Ecuación de Cohetes y Tolvas", "puntos": ["Término de empuje por expulsión o captura de masa v_rel dm/dt.", "Pérdida por fricción en bandas transportadoras de material a granel."]}
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Momento de Inercia y Teorema de los Ejes Paralelos (Steiner)",
        "objetivo": "Calcular momentos de inercia de cuerpos rígidos complejos aplicando el Teorema de Steiner.",
        "concepto_clave_latex": r"I = I_{\text{cm}} + M d^2 \quad ; \quad I_z = \int (x^2 + y^2)\,dm = I_x + I_y",
        "ejemplo": """CLASE MAGISTRAL: INERCIA ROTACIONAL Y TEOREMA DE STEINER
1. Momento de Inercia como Medida de Oposición Rotacional:
En dinámica rotacional, el momento de inercia I = int r^2 dm cumple el mismo rol que la masa inercial m en traslación. Depende no sólo de la cantidad de masa, sino de cómo está distribuida cuadráticamente respecto al eje de rotación.
2. Teorema de los Ejes Paralelos (Teorema de Steiner):
El momento de inercia I respecto a cualquier eje paralelo que diste una distancia d del eje que pasa por el centro de masa cumple estrictamente: I = I_cm + M * d^2.
3. Teorema de los Ejes Perpendiculares (para láminas planas z = 0):
I_z = I_x + I_y.
4. Problema Resuelto 1 (Aplicación Directa):
Una barra homogénea de masa M = 12 kg y longitud L = 3.0 m tiene un momento de inercia respecto a su centro de masa I_cm = (1/12) M L^2. Calcule su momento de inercia respecto a un eje transversal que pasa por uno de sus extremos.
Solución:
La distancia desde el centro de masa (L/2) hasta el extremo es d = L / 2 = 1.5 m.
Por el Teorema de Steiner:
I_extremo = I_cm + M * d^2 = (1/12) M L^2 + M * (L/2)^2
I_extremo = (1/12) M L^2 + (1/4) M L^2 = (1/12 + 3/12) M L^2 = (4/12) M L^2 = (1/3) M L^2.
Evaluando con datos:
I_extremo = (1/3) * (12 kg) * (3.0 m)^2 = 4 * 9 = 36.0 kg*m^2.
(Nótese que I_cm era sólo (1/12)*12*9 = 9 kg*m^2; rotar por el extremo cuadruplica la inercia).
5. Problema Resuelto 2 (Nivel Examen Parcial):
Un volante de inercia de una prensa industrial está formado por un disco central macizo de radio R_1 = 0.4 m y masa M_1 = 80 kg, y un aro periférico exterior de masa M_2 = 120 kg con radio interior R_1 = 0.4 m y radio exterior R_2 = 0.6 m. Calcule el momento de inercia total del volante respecto al eje de giro del motor.
Solución:
1. Disco central macizo:
I_1 = (1/2) * M_1 * R_1^2 = 0.5 * 80 * (0.4)^2 = 40 * 0.16 = 6.40 kg*m^2.
2. Aro periférico hueco (anillo cilíndrico):
I_2 = (1/2) * M_2 * (R_1^2 + R_2^2) = 0.5 * 120 * [ (0.4)^2 + (0.6)^2 ]
I_2 = 60 * [ 0.16 + 0.36 ] = 60 * 0.52 = 31.20 kg*m^2.
Momento de inercia total por superposición:
I_total = I_1 + I_2 = 6.40 + 31.20 = 37.60 kg*m^2.
(El aro exterior aporta el 83% de la inercia a pesar de representar solo el 60% de la masa).""",
        "bloque_sugerido": "Pomodoro 50/10 • Teorema de Steiner y volantes de inercia",
        "slides": [
            {"numero": 1, "seccion": "INERCIA", "titulo": "Teorema de Steiner", "puntos": ["Ecuación I = I_cm + M d^2: el eje centroidal siempre tiene la mínima inercia.", "Concentración periférica de masa para maximizar almacenamiento cinético."]},
            {"numero": 2, "seccion": "SUPERPOSICIÓN", "titulo": "Cuerpos Compuestos", "puntos": ["Suma directa de tensores de inercia referidos al mismo eje de rotación.", "Diseño de volantes (Flywheels) para estabilización de microrredes."]}
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Rodadura sin Deslizamiento (Rolling Motion) y Conservación Energética",
        "objetivo": "Modelar la cinemática y dinámica combinada de traslación y rotación en cuerpos redondos.",
        "concepto_clave_latex": r"v_{\text{cm}} = \omega R \quad ; \quad a_{\text{cm}} = \alpha R \quad ; \quad K_{\text{total}} = \frac{1}{2}M v_{\text{cm}}^2 + \frac{1}{2}I_{\text{cm}}\omega^2",
        "ejemplo": """CLASE MAGISTRAL: RODADURA SIN DESLIZAMIENTO
1. Condición Cinemática de Rodadura Pura:
El punto de contacto del cuerpo con el suelo tiene velocidad instantánea exactamente nula (v_contacto = 0). Esto impone la ligadura geométrica: v_cm = omega * R y a_cm = alpha * R.
2. Energía Cinética Total de un Cuerpo Rodante:
Por el Teorema de König, la energía cinética total es la suma desacoplada de la energía de traslación del centro de masa más la energía de rotación alrededor del centro de masa:
K = (1/2) M v_cm^2 + (1/2) I_cm omega^2 = (1/2) M v_cm^2 * [ 1 + I_cm / (M R^2) ].
3. Rol de la Fricción Estática:
La fuerza responsable de acelerar angularmente el cuerpo es la fricción estática f_s. Como el punto de contacto no desliza, la fricción estática no disipa energía mecánica en forma de calor (W_f = 0).
4. Problema Resuelto 1 (Aplicación Directa):
Una esfera sólida uniforme (I_cm = 2/5 M R^2) de masa M = 5 kg y radio R = 0.2 m rueda sin deslizar sobre una superficie horizontal a v_cm = 6.0 m/s. Calcule su energía cinética total y la fracción correspondiente a la rotación.
Solución:
K_tras = (1/2) M v_cm^2 = 0.5 * 5 * (6)^2 = 0.5 * 5 * 36 = 90.0 J.
K_rot = (1/2) I_cm omega^2 = (1/2) * (2/5 M R^2) * (v_cm / R)^2 = (1/5) M v_cm^2.
K_rot = (1/5) * 5 * (6)^2 = 36.0 J.
K_total = 90.0 + 36.0 = 126.0 J.
Fracción rotacional: K_rot / K_total = 36 / 126 = 2 / 7 approx 28.57%.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Se liberan desde el reposo en la cima de un plano inclinado de altura h y ángulo beta tres cuerpos idénticos en masa M y radio R: un cilindro hueco de pared delgada (I = M R^2), un cilindro sólido (I = 1/2 M R^2) y una esfera sólida (I = 2/5 M R^2). Deduzca analíticamente la velocidad con la que cada cuerpo llega a la base y ordénelos por orden de llegada.
Solución:
Por conservación de la energía mecánica:
M * g * h = (1/2) M v^2 + (1/2) (c M R^2) (v / R)^2 = (1/2) M v^2 (1 + c), donde I_cm = c M R^2.
Despejando la velocidad final:
v = sqrt( [ 2 g h ] / [ 1 + c ] ).
Evaluando el factor c para cada geometría:
1. Esfera sólida: c = 2/5 = 0.40 ==> 1 + c = 1.40 ==> v_esfera = sqrt(2 g h / 1.40) = 1.195 * sqrt(g h).
2. Cilindro sólido: c = 1/2 = 0.50 ==> 1 + c = 1.50 ==> v_cil_sol = sqrt(2 g h / 1.50) = 1.155 * sqrt(g h).
3. Cilindro hueco: c = 1.00 ==> 1 + c = 2.00 ==> v_cil_hueco = sqrt(2 g h / 2.00) = 1.000 * sqrt(g h).
Orden de llegada: Primero la esfera sólida (mayor velocidad), segundo el cilindro sólido y último el cilindro hueco. La aceleración es independiente de la masa M y del radio R, dependiendo exclusivamente de la distribución adimensional de masa c.""",
        "bloque_sugerido": "Laboratorio 50 min • Carreras en plano inclinado y rodadura",
        "slides": [
            {"numero": 1, "seccion": "RODADURA", "titulo": "Cinemática y Teorema de König", "puntos": ["Ligadura v_cm = omega R por punto de contacto estacionario instantáneo.", "Energía total K = 1/2 M v^2 (1 + c) con c = I/(M R^2)."]},
            {"numero": 2, "seccion": "DINÁMICA", "titulo": "Velocidad en Planos Inclinados", "puntos": ["La fricción estática acelera el giro sin disipar calor.", "Independencia de M y R: la geometría adimensional c rige la aceleración."]}
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Momento Angular, Conservación y Precesión Giroscópica",
        "objetivo": "Modelar el momento angular vectorial y calcular pares giroscópicos en turbinas de eje horizontal.",
        "concepto_clave_latex": r"\vec{L} = \vec{r} \times \vec{p} = \mathbf{I}\vec{\omega} \quad ; \quad \vec{\tau}_{\text{ext}} = \frac{d\vec{L}}{dt} \quad ; \quad \Omega_{\text{prec}} = \frac{\tau}{L}",
        "ejemplo": """CLASE MAGISTRAL: MOMENTO ANGULAR Y EFECTOS GIROSCÓPICOS
1. Conservación del Momento Angular:
Si el torque externo neto sobre un sistema es nulo (sum tau_ext = 0), el momento angular total es una constante del movimiento: dL/dt = 0 => L_inicial = L_final.
2. Precesión Giroscópica:
Cuando se aplica un torque perpendicular al vector momento angular L = I * omega, el eje de rotación no cae en la dirección del torque, sino que rota perpendicularmente con velocidad de precesión Omega_prec = tau / L.
3. Par Giroscópico en Turbomaquinaria y Aerogeneradores:
Cuando un aerogenerador de eje horizontal realiza un movimiento de guiñada (yawing) a velocidad Omega para orientarse al viento, la interacción entre el giro del rotor omega y la guiñada genera un par giroscópico tau_gir = I_rotor * omega * Omega que somete al eje principal y a la góndola a severos esfuerzos de flexión.
4. Problema Resuelto 1 (Aplicación Directa):
Una patinadora gira a omega_1 = 3.0 rad/s con los brazos extendidos (I_1 = 4.5 kg*m^2). Al cerrar los brazos sobre el pecho, su momento de inercia se reduce a I_2 = 1.5 kg*m^2. Calcule su nueva velocidad angular omega_2 y la relación entre la energía cinética final e inicial.
Solución:
Por conservación de L (torque externo nulo):
I_1 * omega_1 = I_2 * omega_2
omega_2 = (I_1 / I_2) * omega_1 = (4.5 / 1.5) * 3.0 = 3.0 * 3.0 = 9.0 rad/s.
Energía cinética inicial: K_1 = 0.5 * I_1 * omega_1^2 = 0.5 * 4.5 * (3)^2 = 20.25 J.
Energía cinética final: K_2 = 0.5 * I_2 * omega_2^2 = 0.5 * 1.5 * (9)^2 = 60.75 J.
Relación: K_2 / K_1 = 60.75 / 20.25 = 3.0.
(La energía cinética se triplicó; el trabajo mecánico proviene de la fuerza muscular de la patinadora al cerrar los brazos contra la fuerza centrífuga).
5. Problema Resuelto 2 (Nivel Examen Parcial):
El rotor de un aerogenerador tiene un momento de inercia I = 2.5 * 10^6 kg*m^2 y gira a velocidad nominal de 12 rpm (omega = 1.257 rad/s). Si el sistema de control acciona el mecanismo de guiñada para rotar la góndola horizontalmente a una tasa Omega = 0.5 °/s (0.00873 rad/s), determine la magnitud del torque giroscópico inducido sobre los cojinetes de la góndola.
Solución:
Momento angular del rotor:
L = I * omega = (2.5e6 kg*m^2) * (1.257 rad/s) = 3,142,500 kg*m^2/s = 3.1425e6 N*m*s.
Torque giroscópico perpendicular:
tau_gir = L * Omega = (3.1425e6 N*m*s) * (0.00873 rad/s) = 27,434 N*m = 27.43 kN*m.
Este torque transversal constante de 27.4 kN*m debe ser absorbido por los pernos de la corona de orientación de la torre para evitar fatiga estructural catastrófica.""",
        "bloque_sugerido": "Pomodoro 50/10 • Conservación de momento angular y giroscopios",
        "slides": [
            {"numero": 1, "seccion": "MOMENTO ANGULAR", "titulo": "Conservación Vectorial", "puntos": ["Ecuación dL/dt = tau_ext y constancia de L ante torque externo nulo.", "Variación de velocidad angular por redistribución interna de masa."]},
            {"numero": 2, "seccion": "GIROSCÓPICO", "titulo": "Precesión y Par en Turbinas", "puntos": ["Vector dL/dt perpendicular al eje generando precesión Omega = tau/L.", "Par giroscópico en maniobras de guiñada de aerogeneradores."]}
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Elasticidad, Ley de Hooke y Deformaciones en Materiales",
        "objetivo": "Calcular esfuerzos normales y cortantes, deformaciones unitarias y módulos de elasticidad en estructuras de ingeniería.",
        "concepto_clave_latex": r"\sigma = \frac{F_{\perp}}{A} = E \epsilon = E \frac{\Delta L}{L_0} \quad ; \quad \tau = \frac{F_{\parallel}}{A} = G \gamma \quad ; \quad \nu = -\frac{\epsilon_{\text{trans}}}{\epsilon_{\text{long}}}",
        "ejemplo": """CLASE MAGISTRAL: TEORÍA DE LA ELASTICIDAD Y RESISTENCIA DE MATERIALES
1. Esfuerzo (Stress) y Deformación Unitaria (Strain):
- Esfuerzo Normal (sigma): Fuerza perpendicular por unidad de área transversal (Pa = N/m^2).
- Deformación Unitaria (epsilon): Cambio relativo de longitud adimensional delta_L / L_0.
- Ley de Hooke Unidimensional: sigma = E * epsilon, donde E es el Módulo de Young (medida de rigidez elástica intrínseca del material).
2. Módulo de Corte (G) y Relación de Poisson (nu):
El esfuerzo cortante tau = G * gamma distorsiona angularmente el material. La Relación de Poisson nu cuantifica la contracción lateral cuando el cuerpo se somete a tracción longitudinal (nu aprox 0.28 a 0.33 en aceros estructurales).
3. Problema Resuelto 1 (Aplicación Directa):
Un cable de acero estructural de alta resistencia (Módulo de Young E = 200 GPa = 200 * 10^9 Pa) de longitud L_0 = 40 m y diámetro d = 20 mm se utiliza para arriostrar la torre de medición anemométrica en un parque eólico. Si soporta una tensión de tracción F = 50 kN, determine el alargamiento elástico delta_L.
Solución:
Área de la sección transversal del cable:
A = pi * (d/2)^2 = pi * (0.010 m)^2 = 3.1416 * 10^-4 m^2.
Esfuerzo normal:
sigma = F / A = 50,000 N / (3.1416e-4 m^2) = 159,154,943 Pa = 159.15 MPa.
(Muy por debajo del límite de fluencia del acero S355 de 355 MPa, opera en zona elástica segura).
Alargamiento por Ley de Hooke:
delta_L = (F * L_0) / (A * E) = (sigma * L_0) / E
delta_L = (159.155e6 Pa * 40 m) / (200e9 Pa) = 6,366.2 / 200,000 = 0.03183 m = 31.83 mm.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente que la densidad de energía elástica de deformación almacenada por unidad de volumen u_e en una barra sometida a tracción uniaxial dentro del rango elástico lineal es u_e = (1/2) sigma * epsilon = sigma^2 / (2E).
Solución:
El trabajo infinitesimal realizado por la fuerza para estirar la barra una distancia dx es:
dW = F(x) dx = (A * sigma(x)) * (L_0 * d_epsilon) = (A * L_0) * sigma d_epsilon.
Como el volumen inicial es V_0 = A * L_0:
Densidad de energía: du_e = dW / V_0 = sigma d_epsilon.
Aplicando la Ley de Hooke: sigma = E * epsilon:
u_e = int_0^epsilon (E * epsilon) d_epsilon = (1/2) E * epsilon^2.
Como epsilon = sigma / E:
u_e = (1/2) E * (sigma / E)^2 = (1/2) sigma^2 / E = (1/2) sigma * epsilon.
Para el cable anterior con sigma = 159.15 MPa y E = 200 GPa:
u_e = (159.155e6)^2 / (2 * 200e9) = 2.533e16 / 4e11 = 63,325 J/m^3.
Energía total almacenada en el cable de volumen V = 0.01257 m^3:
U_total = u_e * V = 63,325 * 0.01257 = 796.0 J. Q.E.D.""",
        "bloque_sugerido": "Laboratorio 50 min • Módulo de Young y ensayos de tracción",
        "slides": [
            {"numero": 1, "seccion": "ELASTICIDAD", "titulo": "Esfuerzo y Ley de Hooke", "puntos": ["Esfuerzo normal sigma = F/A y deformación unitaria epsilon = delta_L / L_0.", "Módulo de Young E como constante elástica fundamental del material."]},
            {"numero": 2, "seccion": "ENERGÍA", "titulo": "Densidad de Energía Elástica", "puntos": ["Energía de deformación por unidad de volumen u_e = sigma^2 / (2E).", "Cálculo de alargamientos elásticos en tirantes y cables tensores."]}
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Estática de Fluidos I: Principio de Pascal y Fuerzas Hidrostáticas",
        "objetivo": "Calcular la distribución de presiones hidrostáticas y la fuerza resultante sobre compuertas de presas.",
        "concepto_clave_latex": r"P(z) = P_0 + \rho g z \quad ; \quad F_R = P_{\text{cg}} A = \rho g h_{\text{cg}} A \quad ; \quad y_{\text{cp}} = y_{\text{cg}} + \frac{I_{xx,\text{cg}}}{y_{\text{cg}} A}",
        "ejemplo": """CLASE MAGISTRAL: PRESIÓN HIDROSTÁTICA Y COMPUERTAS SUMERGIDAS
1. Presión en un Fluido Estático e Incompresible:
La presión es isotrópica (actúa igual en todas las direcciones) y perpendicular a cualquier superficie frontera. La ecuación fundamental de la hidrostática dP/dz = rho * g indica que la presión aumenta linealmente con la profundidad z.
2. Principio de Pascal y Prensas Hidráulicas:
La presión aplicada a un fluido incompresible encerrado se transmite íntegramente a todos los puntos del fluido: P_1 = P_2 => F_1 / A_1 = F_2 / A_2.
3. Centro de Presión (CP) en Compuertas Hidráulicas:
Dado que la presión crece con la profundidad, la fuerza resultante neta F_R no actúa en el centro de gravedad (CG) geométrico de la compuerta, sino en un punto más profundo llamado Centro de Presión (y_cp > y_cg).
4. Problema Resuelto 1 (Aplicación Directa):
Una prensa hidráulica de taller para ensamblar cojinetes de turbina tiene un émbolo menor de radio r_1 = 2.0 cm y un émbolo mayor de radio r_2 = 20.0 cm. Si se aplica una fuerza manual F_1 = 250 N en el émbolo menor, calcule la fuerza resultante F_2 en el émbolo mayor.
Solución:
Áreas: A_1 = pi * r_1^2, A_2 = pi * r_2^2.
Relación de áreas: A_2 / A_1 = (r_2 / r_1)^2 = (20 / 2)^2 = 10^2 = 100.
Por Pascal: F_2 = F_1 * (A_2 / A_1) = 250 N * 100 = 25,000 N = 25.0 kN.
(Multiplicador de fuerza de 100x gracias a la incompresibilidad del aceite hidráulico).
5. Problema Resuelto 2 (Nivel Examen Parcial):
La compuerta rectangular de descarga de fondo de una presa hidroeléctrica tiene un ancho b = 4.0 m y una altura h = 3.0 m, articulada en su borde superior horizontal. El nivel del agua en el embalse alcanza la parte superior de la compuerta. Determine la fuerza hidrostática total F_R y la ubicación exacta del centro de presión y_cp medido desde la superficie libre del agua (rho = 1000 kg/m^3, g = 9.81 m/s^2).
Solución:
1. Área de la compuerta: A = b * h = 4.0 * 3.0 = 12.0 m^2.
2. Centro de gravedad: y_cg = h / 2 = 3.0 / 2 = 1.5 m de profundidad.
3. Presión en el centro de gravedad:
P_cg = rho * g * y_cg = 1000 * 9.81 * 1.5 = 14,715 Pa.
4. Fuerza resultante hidrostática:
F_R = P_cg * A = 14,715 Pa * 12.0 m^2 = 176,580 N = 176.58 kN.
5. Momento de inercia centroidal de un rectángulo:
I_xx,cg = (b * h^3) / 12 = (4.0 * 3^3) / 12 = (4 * 27) / 12 = 9.0 m^4.
6. Centro de presión y_cp:
y_cp = y_cg + [ I_xx,cg / (y_cg * A) ]
y_cp = 1.5 + [ 9.0 / (1.5 * 12.0) ] = 1.5 + [ 9.0 / 18.0 ] = 1.5 + 0.5 = 2.0 m.
La fuerza actúa a 2.0 m de profundidad (exactamente a dos tercios de la altura de la compuerta).""",
        "bloque_sugerido": "Laboratorio 50 min • Presión hidrostática y centro de presión",
        "slides": [
            {"numero": 1, "seccion": "HIDROSTÁTICA", "titulo": "Distribución Lineal de Presión", "puntos": ["Ecuación fundamental dP/dz = rho g y principio de Pascal.", "Multiplicación de fuerza en sistemas hidráulicos de potencia."]},
            {"numero": 2, "seccion": "COMPUERTAS", "titulo": "Fuerza y Centro de Presión", "puntos": ["Fuerza resultante F_R = P_cg A actuando en el centro de presión.", "El centro de presión siempre se ubica por debajo del centroide geométrico."]}
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Estática de Fluidos II: Principio de Arquímedes y Flotabilidad",
        "objetivo": "Calcular fuerzas de empuje boyante y determinar la estabilidad rotacional de plataformas eólicas flotantes.",
        "concepto_clave_latex": r"E = \rho_f g V_{\text{sumergido}} \quad ; \quad \text{Metacentro } GM = BM + KB - KG > 0",
        "ejemplo": """CLASE MAGISTRAL: PRINCIPIO DE ARQUÍMEDES Y ESTABILIDAD FLOTANTE
1. Fuerza de Empuje Boyante (Principio de Arquímedes):
Todo cuerpo sumergido total o parcialmente en un fluido estático experimenta una fuerza de empuje vertical hacia arriba igual al peso del volumen de fluido desalojado: E = rho_fluido * g * V_desalojado. El empuje actúa en el Centro de Flotación (B), que es el centroide del volumen sumergido.
2. Criterio de Estabilidad y Altura Metacéntrica (GM):
Para que un cuerpo flotante (un barco o una plataforma semisumergible de aerogenerador marino) sea rotacionalmente estable y retorne a la vertical tras una inclinación (escoramiento), el Metacentro (M) debe ubicarse estrictamente por encima del Centro de Gravedad (G) del sistema: GM > 0.
3. Problema Resuelto 1 (Aplicación Directa):
Un flotador cilíndrico de baliza marina de masa M = 1,200 kg y diámetro D = 1.6 m flota en agua salada (rho_mar = 1025 kg/m^3). Calcule el calado (profundidad sumergida h_sub) del flotador en equilibrio estático.
Solución:
Área de la base cilíndrica:
A = pi * (D/2)^2 = pi * (0.8)^2 = 2.0106 m^2.
En equilibrio de flotación: Peso = Empuje
M * g = rho_mar * g * V_sumergido
M = rho_mar * (A * h_sub)
h_sub = M / (rho_mar * A) = 1,200 kg / (1025 kg/m^3 * 2.0106 m^2) = 1,200 / 2060.86 = 0.5823 m = 58.23 cm.
El cilindro se sumerge 58.2 cm en el agua de mar.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un bloque rectangular de madera balsa homogénea (densidad rho_m = 600 kg/m^3) de dimensiones L x W x H = 2.0 m x 1.0 m x 0.8 m flota en agua dulce (rho_w = 1000 kg/m^3) con su eje vertical H. Determine si la posición vertical es estable ante una perturbación rotacional respecto al eje longitudinal L.
Solución:
1. Calado sumergido h_s:
h_s = (rho_m / rho_w) * H = (600 / 1000) * 0.8 = 0.48 m.
2. Centro de gravedad de la madera:
KG = H / 2 = 0.8 / 2 = 0.40 m desde el fondo.
3. Centro de flotación del agua desalojada:
KB = h_s / 2 = 0.48 / 2 = 0.24 m desde el fondo.
4. Radio metacéntrico BM = I_flotacion / V_sub:
El momento de inercia del plano de flotación (rectángulo L x W) respecto a la rotación es:
I_flotacion = (L * W^3) / 12 = (2.0 * 1.0^3) / 12 = 2.0 / 12 = 0.1667 m^4.
Volumen sumergido: V_sub = L * W * h_s = 2.0 * 1.0 * 0.48 = 0.96 m^3.
BM = 0.1667 / 0.96 = 0.1736 m.
5. Altura metacéntrica GM:
GM = KB + BM - KG = 0.24 + 0.1736 - 0.40 = 0.4136 - 0.40 = +0.0136 m = +1.36 cm.
Como GM = +0.0136 m > 0, el par restaurador es positivo y el bloque es estable en posición vertical.""",
        "bloque_sugerido": "Laboratorio 50 min • Estabilidad de cuerpos flotantes y metacentro",
        "slides": [
            {"numero": 1, "seccion": "ARQUÍMEDES", "titulo": "Fuerza de Empuje Boyante", "puntos": ["E = rho g V_desalojado actuando en el centro de flotación B.", "Equilibrio estático: peso total igual al empuje en cuerpos flotantes."]},
            {"numero": 2, "seccion": "ESTABILIDAD", "titulo": "Altura Metacéntrica GM", "puntos": ["Criterio de estabilidad rotacional GM = KB + BM - KG > 0.", "Diseño de cimentaciones flotantes (spar-buoy, TLP) en eólica marina."]}
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Movimiento Armónico Simple (MAS) y Conservación Energética",
        "objetivo": "Formular y resolver la ecuación diferencial del MAS para osciladores mecánicos masa-resorte y péndulos.",
        "concepto_clave_latex": r"\frac{d^2 x}{dt^2} + \omega_0^2 x = 0 \quad ; \quad x(t) = A \cos(\omega_0 t + \phi) \quad ; \quad E = \frac{1}{2}k A^2",
        "ejemplo": """CLASE MAGISTRAL: OSCILACIONES MECÁNICAS Y MOVIMIENTO ARMÓNICO
1. Cinemática y Ecuación Diferencial del MAS:
El MAS surge cuando una masa m experimenta una fuerza restauradora lineal proporcional al desplazamiento respecto a la posición de equilibrio: F = -k * x (Ley de Hooke).
Aplicando Newton: m * d^2x/dt^2 = -k * x => d^2x/dt^2 + (k/m) * x = 0.
Definiendo la frecuencia angular propia: omega_0 = sqrt(k / m) [rad/s].
2. Solución Analítica General:
x(t) = A * cos(omega_0 * t + phi), donde A es la amplitud y phi la fase inicial.
Velocidad: v(t) = -omega_0 * A * sin(omega_0 * t + phi), con v_max = omega_0 * A.
Aceleración: a(t) = -omega_0^2 * x(t), con a_max = omega_0^2 * A.
3. Conservación de Energía Mecánica en el MAS:
E = K + U = (1/2) m v^2 + (1/2) k x^2 = (1/2) k A^2 = constante. La energía oscila continuamente entre energía cinética (máxima en x = 0) y potencial elástica (máxima en x = +-A).
4. Problema Resuelto 1 (Aplicación Directa):
Un amortiguador de vibraciones en la bancada de un generador diésel se modela como una masa m = 20 kg sujeta a un resorte de rigidez k = 8000 N/m. Se desplaza x_0 = 0.05 m desde el equilibrio y se suelta desde el reposo (v_0 = 0). Determine la frecuencia angular omega_0, el periodo T, la velocidad máxima v_max y la aceleración máxima a_max.
Solución:
omega_0 = sqrt(k / m) = sqrt(8000 / 20) = sqrt(400) = 20.0 rad/s.
Frecuencia: f = omega_0 / (2 * pi) = 20 / (2 * 3.1416) = 3.183 Hz.
Periodo: T = 1 / f = 1 / 3.183 = 0.314 s.
Amplitud A = x_0 = 0.05 m.
Velocidad máxima: v_max = omega_0 * A = 20 * 0.05 = 1.0 m/s (en x = 0).
Aceleración máxima: a_max = omega_0^2 * A = (20)^2 * 0.05 = 400 * 0.05 = 20.0 m/s^2 (en x = +-A).
5. Problema Resuelto 2 (Nivel Examen Parcial):
En un oscilador armónico simple de masa m y constante k, determine analíticamente las posiciones x donde la energía cinética K es exactamente igual a la energía potencial U, y exprese la velocidad v en ese punto en función de v_max.
Solución:
Energía total: E = (1/2) k A^2.
Condición K = U:
Dado que E = K + U = 2 U:
(1/2) k A^2 = 2 * [ (1/2) k x^2 ] = k x^2.
Despejando x:
x^2 = A^2 / 2 ==> x = +- A / sqrt(2) approx +- 0.7071 A.
Para la velocidad:
Como K = E / 2:
(1/2) m v^2 = (1/2) * [ (1/2) m v_max^2 ]
v^2 = v_max^2 / 2 ==> v = +- v_max / sqrt(2) approx +- 0.7071 v_max.
La energía se distribuye equitativamente cuando el cuerpo está al 70.7% de su desplazamiento máximo.""",
        "bloque_sugerido": "Laboratorio 50 min • Simulación de oscilador masa-resorte y energía",
        "slides": [
            {"numero": 1, "seccion": "MAS", "titulo": "Ecuación Diferencial del MAS", "puntos": ["Ecuación d^2x/dt^2 + omega_0^2 x = 0 y solución sinusoidal.", "Frecuencia angular intrínseca omega_0 = sqrt(k/m) y periodo T = 2pi/omega_0."]},
            {"numero": 2, "seccion": "ENERGÍA", "titulo": "Conservación K + U", "puntos": ["Energía total constante E = 1/2 k A^2.", "Intercambio continuo de energía cinética y potencial elástica."]}
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Péndulo Simple, Péndulo Físico y Péndulo de Torsión",
        "objetivo": "Determinar periodos de oscilación para cuerpos rígidos articulados mediante dinámica rotacional.",
        "concepto_clave_latex": r"T_{\text{simple}} = 2\pi\sqrt{\frac{L}{g}} \quad ; \quad T_{\text{físico}} = 2\pi\sqrt{\frac{I}{M g d}} \quad ; \quad T_{\text{torsión}} = 2\pi\sqrt{\frac{I}{\kappa}}",
        "ejemplo": """CLASE MAGISTRAL: PÉNDULOS Y MEDICIÓN DE INERCIA
1. Péndulo Simple y Aproximación de Ángulo Pequeño:
Para oscilaciones pequeñas (theta < 10° o 0.17 rad), sin(theta) approx theta con error < 0.5%. La ecuación diferencial d^2theta/dt^2 + (g/L) theta = 0 arroja un periodo independiente de la masa: T = 2 pi sqrt(L / g).
2. Péndulo Físico (Cuerpo Rígido Compuesto):
Para un cuerpo rígido suspendido de un pivote que dista d del centro de masa: tau = -M g d sin(theta) = I * d^2theta/dt^2.
Para ángulos pequeños: d^2theta/dt^2 + (M g d / I) theta = 0, con T = 2 pi sqrt(I / (M g d)).
3. Aplicación Metrológica:
Permite medir experimentalmente el momento de inercia I de componentes con geometrías complejas (bielas, álabes) midiendo su periodo de oscilación libre.
4. Problema Resuelto 1 (Aplicación Directa):
Se suspende una varilla uniforme de masa M = 2.0 kg y longitud L = 1.2 m desde un extremo pivotado sin fricción (I = (1/3) M L^2). Calcule su periodo de oscilación para pequeñas amplitudes (g = 9.81 m/s^2).
Solución:
Distancia del pivote al centro de masa: d = L / 2 = 1.2 / 2 = 0.60 m.
Momento de inercia: I = (1/3) * M * L^2.
Frecuencia angular del péndulo físico:
omega_0 = sqrt( [ M g d ] / I ) = sqrt( [ M g (L/2) ] / [ (1/3) M L^2 ] ) = sqrt( [ (1/2) g ] / [ (1/3) L ] ) = sqrt( [ 3 g ] / [ 2 L ] ).
Evaluando:
omega_0 = sqrt( (3 * 9.81) / (2 * 1.2) ) = sqrt( 29.43 / 2.4 ) = sqrt(12.2625) = 3.5018 rad/s.
Periodo:
T = 2 * pi / omega_0 = (2 * 3.1416) / 3.5018 = 1.794 segundos.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Un álabe de turbina de masa M = 15 kg se suspende de una cuchilla horizontal para medir su momento de inercia I_cm respecto al centro de masa. El centro de masa se determinó previamente balanceando el álabe, ubicándose a d = 0.35 m del eje de pivote. Al soltarlo con pequeña amplitud, se cronometran 20 oscilaciones completas en un tiempo t = 28.4 segundos. Calcule el momento de inercia centroidal I_cm del álabe.
Solución:
Periodo experimental: T = 28.4 s / 20 = 1.420 s.
Frecuencia angular: omega = 2 pi / T = (2 * 3.1416) / 1.420 = 4.4248 rad/s.
De la ecuación del péndulo físico: omega^2 = (M g d) / I_pivote.
I_pivote = (M * g * d) / omega^2
I_pivote = (15 kg * 9.81 m/s^2 * 0.35 m) / (4.4248)^2 = (51.5025) / (19.5786) = 2.6305 kg*m^2.
Por el Teorema de Steiner: I_pivote = I_cm + M * d^2.
I_cm = I_pivote - M * d^2
I_cm = 2.6305 - [ 15 * (0.35)^2 ] = 2.6305 - [ 15 * 0.1225 ] = 2.6305 - 1.8375 = 0.7930 kg*m^2.
El momento de inercia centroidal del álabe es 0.793 kg*m^2.""",
        "bloque_sugerido": "Laboratorio 50 min • Determinación experimental de momentos de inercia",
        "slides": [
            {"numero": 1, "seccion": "PÉNDULOS", "titulo": "Péndulo Simple vs Péndulo Físico", "puntos": ["Aproximación de ángulos pequeños sin(theta) approx theta.", "Periodo del péndulo físico T = 2pi sqrt(I / (M g d))."]},
            {"numero": 2, "seccion": "METROLOGÍA", "titulo": "Medición de Inercia de Cuerpos Reales", "puntos": ["Determinación de I_pivote mediante cronometraje de oscilaciones.", "Despeje analítico de I_cm aplicando el Teorema de Steiner."]}
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Oscilaciones Amortiguadas: Amortiguamiento Subcrítico y Factor Q",
        "objetivo": "Resolver la ecuación diferencial con amortiguamiento viscoso y clasificar regímenes de disipación energética.",
        "concepto_clave_latex": r"m\ddot{x} + b\dot{x} + kx = 0 \quad ; \quad \omega_d = \sqrt{\omega_0^2 - \gamma^2} \quad ; \quad Q = \frac{\omega_0}{2\gamma} = \frac{\sqrt{k m}}{b}",
        "ejemplo": """CLASE MAGISTRAL: OSCILACIONES AMORTIGUADAS
1. Disipación de Energía por Resistencia Viscosa:
En cualquier sistema físico real existe fricción con el fluido o histéresis material, representada como una fuerza disipativa viscosa opuesta a la velocidad: F_d = -b * v = -b * (dx/dt).
Ecuación diferencial: m * d^2x/dt^2 + b * (dx/dt) + k * x = 0.
Dividiendo entre m: d^2x/dt^2 + 2 gamma * dx/dt + omega_0^2 * x = 0, donde gamma = b / (2m) es el coeficiente de amortiguamiento y omega_0 = sqrt(k/m).
2. Clasificación de Regímenes según el Discriminante Delta = gamma^2 - omega_0^2:
- Subcrítico (gamma < omega_0): El sistema oscila con amplitud exponencialmente decreciente A(t) = A_0 * exp(-gamma t) y frecuencia amortiguada omega_d = sqrt(omega_0^2 - gamma^2).
- Crítico (gamma = omega_0): Retorna al equilibrio en el menor tiempo posible sin oscilar.
- Sobreamortiguado (gamma > omega_0): Retorno lento y perezoso al equilibrio gobernado por dos exponenciales decrecientes.
3. Factor de Calidad (Q):
Cuantifica la pérdida relativa de energía por ciclo: Q = 2 pi * (Energía almacenada / Energía disipada por ciclo). Un Q alto indica muy bajo amortiguamiento.
4. Problema Resuelto 1 (Aplicación Directa):
Un soporte elástico de turbina con m = 100 kg y k = 250,000 N/m presenta un amortiguamiento viscoso b = 400 N*s/m. Calcule la frecuencia natural no amortiguada omega_0, el coeficiente gamma, la frecuencia amortiguada omega_d y el factor de calidad Q.
Solución:
omega_0 = sqrt(k / m) = sqrt(250,000 / 100) = sqrt(2500) = 50.0 rad/s.
gamma = b / (2 * m) = 400 / (2 * 100) = 2.0 s^-1.
Como gamma = 2.0 < omega_0 = 50.0, el régimen es claramente subcrítico.
Frecuencia amortiguada:
omega_d = sqrt(omega_0^2 - gamma^2) = sqrt(50^2 - 2^2) = sqrt(2500 - 4) = sqrt(2496) = 49.96 rad/s.
(La frecuencia apenas varió un 0.08% respecto a omega_0).
Factor de calidad Q:
Q = omega_0 / (2 * gamma) = 50.0 / (2 * 2.0) = 50 / 4 = 12.5.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre la relación del Decremento Logarítmico delta = ln(x_n / x_{n+1}) = gamma * T_d = 2 pi / sqrt(4 Q^2 - 1), y calcule el decremento logarítmico y la reducción porcentual de amplitud entre dos picos sucesivos para el soporte anterior.
Solución:
La envolvente de picos en instantes t y t + T_d cumple:
x_n = A_0 * exp(-gamma * t).
x_{n+1} = A_0 * exp(-gamma * (t + T_d)).
Cociente de amplitudes:
x_n / x_{n+1} = exp(gamma * T_d).
Decremento logarítmico:
delta = ln(x_n / x_{n+1}) = gamma * T_d.
Como T_d = 2 pi / omega_d:
delta = gamma * (2 pi / omega_d) = (2 pi * gamma) / sqrt(omega_0^2 - gamma^2).
Dividiendo numerador y denominador entre omega_0:
delta = (2 pi * (gamma / omega_0)) / sqrt( 1 - (gamma / omega_0)^2 ) = (2 pi / (2Q)) / sqrt( 1 - 1/(4Q^2) ) = 2 pi / sqrt(4 Q^2 - 1).
Evaluando para el soporte con gamma = 2.0 y omega_d = 49.96 rad/s:
T_d = 2 * pi / 49.96 = 0.1257 s.
delta = gamma * T_d = 2.0 * 0.1257 = 0.2514.
Razón de amplitudes: x_{n+1} / x_n = exp(-delta) = exp(-0.2514) = 0.7777 (77.77%).
Reducción de amplitud por ciclo: (1 - 0.7777) * 100% = 22.23% de pérdida en cada oscilación.""",
        "bloque_sugerido": "Laboratorio 50 min • Decremento logarítmico y factor Q en osciladores",
        "slides": [
            {"numero": 1, "seccion": "AMORTIGUAMIENTO", "titulo": "Regímenes de Oscilación", "puntos": ["Subcrítico (gamma < omega_0), Crítico (gamma = omega_0) y Sobrecrítico.", "Envolvente exponencial decreciente exp(-gamma t)."]},
            {"numero": 2, "seccion": "DISIPACIÓN", "titulo": "Factor de Calidad y Decremento", "puntos": ["Métrica de disipación energética Q = omega_0 / (2 gamma).", "Decremento logarítmico delta = ln(x_n / x_{n+1}) para medición experimental."]}
        ]
    }
]

topics_21_to_30 = [
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Oscilaciones Forzadas, Resonancia Mecánica y Aislamiento",
        "objetivo": "Calcular la respuesta en frecuencia de sistemas forzados y dimensionar aisladores de vibración para maquinaria.",
        "concepto_clave_latex": r"A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (2\gamma\omega)^2}} \quad ; \quad \omega_{\text{res}} = \sqrt{\omega_0^2 - 2\gamma^2}",
        "ejemplo": """CLASE MAGISTRAL: VIBRACIONES FORZADAS Y EL FENÓMENO DE RESONANCIA
1. Excitación Armónica Externa:
Cuando una máquina rotativa (motor, turbina desbalanceada) opera a velocidad omega, induce una fuerza periódica externa F(t) = F_0 * cos(omega t).
Ecuación diferencial: m * d^2x/dt^2 + b * dx/dt + k * x = F_0 * cos(omega t).
2. Curva de Resonancia y Pico de Amplitud:
La respuesta de estado estacionario oscila a la frecuencia de excitación omega con amplitud A(omega). Cuando la frecuencia impulsora coincide con la frecuencia de resonancia omega_res = sqrt(omega_0^2 - 2 gamma^2), la amplitud se amplifica drásticamente pudiendo ocasionar colapso estructural (falla por fatiga).
3. Transmisibilidad y Aislamiento de Vibraciones:
Para aislar una máquina de su cimentación, la frecuencia de operación omega debe ser superior a sqrt(2) * omega_0 (zona de aislamiento donde la fuerza transmitida es menor que la perturbadora).
4. Problema Resuelto 1 (Aplicación Directa):
Un compresor de gas de masa m = 200 kg opera a 1800 rpm (f = 30 Hz => omega = 188.5 rad/s) y presenta una fuerza de desbalance residual F_0 = 500 N. Se monta sobre aisladores elastoméricos con rigidez k = 800,000 N/m y amortiguamiento b = 1200 N*s/m. Calcule la amplitud de vibración de estado estacionario A(omega).
Solución:
omega_0 = sqrt(k / m) = sqrt(800,000 / 200) = sqrt(4000) = 63.245 rad/s.
gamma = b / (2m) = 1200 / (2 * 200) = 3.0 s^-1.
F_0 / m = 500 / 200 = 2.5 m/s^2.
Diferencia cuadrática de frecuencias:
(omega_0^2 - omega^2) = (4000 - (188.5)^2) = 4000 - 35532 = -31,532 (rad/s)^2.
(omega_0^2 - omega^2)^2 = (-31532)^2 = 9.943 * 10^8.
Término disipativo:
(2 * gamma * omega)^2 = (2 * 3.0 * 188.5)^2 = (1131)^2 = 1.279 * 10^6.
Denominador:
sqrt( 9.943e8 + 1.279e6 ) approx sqrt( 9.956e8 ) = 31,553.
Amplitud:
A = 2.5 / 31,553 = 7.923 * 10^-5 m = 0.0792 mm.
Como omega = 188.5 > sqrt(2) * 63.25 = 89.4 rad/s, el sistema opera con éxito en la zona de aislamiento.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente que la amplitud en resonancia para amortiguamiento ligero (gamma << omega_0) se simplifica a A_max = Q * (F_0 / k), donde Q es el factor de calidad del oscilador.
Solución:
En resonancia omega approx omega_0:
El término (omega_0^2 - omega^2)^2 = 0.
La amplitud máxima queda:
A_max = (F_0 / m) / sqrt( (2 * gamma * omega_0)^2 ) = (F_0 / m) / (2 * gamma * omega_0).
Multiplicando y dividiendo por k (recordando que k = m * omega_0^2):
A_max = [ F_0 / (m * omega_0^2) ] * [ omega_0 / (2 * gamma) ].
Reconociendo que F_0 / k es la deflexión estática x_estatica, y que Q = omega_0 / (2 gamma):
A_max = x_estatica * Q = Q * (F_0 / k).
Esto demuestra que el Factor de Calidad Q actúa como el factor de amplificación dinámica directa en resonancia. Para Q = 20, la amplitud vibratoria es 20 veces superior a la fuerza aplicada estáticamente. Q.E.D.""",
        "bloque_sugerido": "Laboratorio 50 min • Curvas de resonancia y transmisibilidad",
        "slides": [
            {"numero": 1, "seccion": "RESONANCIA", "titulo": "Amplificación Dinámica", "puntos": ["Ecuación de estado estacionario con desfase angular delta.", "Pico de resonancia gobernado por el factor de calidad A_max = Q x_est."]},
            {"numero": 2, "seccion": "AISLAMIENTO", "titulo": "Criterio de Aislamiento", "puntos": ["Zona de aislamiento vibratorio para omega > sqrt(2) omega_0.", "Protección de cimentaciones frente a desbalance de generadores."]}
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Ondas Mecánicas Unidimensionales: Ecuación de Onda y Transporte",
        "objetivo": "Formular la ecuación diferencial de onda en cuerdas y calcular la tasa de transporte de energía y potencia.",
        "concepto_clave_latex": r"\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2} \quad ; \quad v = \sqrt{\frac{T}{\mu}} \quad ; \quad \bar{P} = \frac{1}{2}\mu v \omega^2 A^2",
        "ejemplo": """CLASE MAGISTRAL: PROPAGACIÓN DE ONDAS MECÁNICAS
1. Perturbación y Transporte de Energía sin Transporte de Masa:
Una onda mecánica es una perturbación que viaja a través de un medio deformable elástico transportando energía cinética y potencial elástica sin desplazar la masa del medio en dirección de propagación.
2. Ecuación Clásica de Onda de D'Alembert:
Derivada aplicando la Segunda Ley de Newton a un segmento infinitesimal de cuerda con tensión T y densidad lineal mu = dm/dx:
d^2y/dx^2 = (1 / v^2) * d^2y/dt^2, donde la velocidad de fase es v = sqrt(T / mu).
3. Función de Onda Sinusoidal:
y(x, t) = A * cos(k * x - omega * t), donde k = 2 pi / lambda es el número de onda y omega = 2 pi f.
4. Problema Resuelto 1 (Aplicación Directa):
Una línea de transmisión aérea de aleación de aluminio tiene una densidad lineal de masa mu = 0.85 kg/m y está tensada entre dos torres a T = 34,000 N. Calcule la velocidad de propagación de una onda transversal inducida por una ráfaga de viento y determine el tiempo que tarda la perturbación en recorrer el vano de L = 400 m.
Solución:
Velocidad de propagación transversal:
v = sqrt(T / mu) = sqrt(34,000 N / 0.85 kg/m) = sqrt(40,000) = 200.0 m/s.
Tiempo de tránsito del pulso:
t = L / v = 400 m / (200.0 m/s) = 2.0 segundos.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Una cuerda elástica con densidad mu = 0.05 kg/m y tensión T = 80 N transporta una onda armónica de amplitud A = 0.04 m y frecuencia f = 60 Hz. Calcule la potencia promedio transmitida por la onda en Watts y demuestre analíticamente que la potencia es proporcional al cuadrado de la amplitud y de la frecuencia.
Solución:
1. Velocidad de onda: v = sqrt(80 / 0.05) = sqrt(1600) = 40.0 m/s.
2. Frecuencia angular: omega = 2 * pi * f = 2 * pi * 60 = 376.99 rad/s.
3. Potencia promedio:
P_prom = 0.5 * mu * v * omega^2 * A^2
P_prom = 0.5 * (0.05 kg/m) * (40 m/s) * (376.99 rad/s)^2 * (0.04 m)^2
P_prom = 1.0 * (142,122) * (0.0016) = 227.40 Watts.
Demostración analítica: La energía total en una longitud de onda es E_lambda = (1/2) mu lambda omega^2 A^2. Como la potencia es la energía transferida por periodo P = E_lambda / T = E_lambda * (v / lambda): P = (1/2) mu v omega^2 A^2. Por ende, la potencia escala estrictamente con A^2 y con omega^2 = (2 pi f)^2. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Ecuación de onda y transporte de potencia",
        "slides": [
            {"numero": 1, "seccion": "ONDAS", "titulo": "Ecuación de Onda y Velocidad", "puntos": ["Ecuación de D'Alembert y velocidad en medios tensos v = sqrt(T/mu).", "Solución armónica y(x, t) = A cos(kx - omega t)."]},
            {"numero": 2, "seccion": "POTENCIA", "titulo": "Transporte de Energía", "puntos": ["Potencia promedio P = 1/2 mu v omega^2 A^2.", "Dependencia cuadrática con la amplitud y con la frecuencia angular."]}
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Superposición, Ondas Estacionarias y Resonancia Acústica",
        "objetivo": "Modelar la formación de ondas estacionarias, modos normales de vibración y frecuencias armónicas.",
        "concepto_clave_latex": r"y(x, t) = 2A\sin(kx)\cos(\omega t) \quad ; \quad f_n = n \frac{v}{2L} = \frac{n}{2L}\sqrt{\frac{T}{\mu}} \quad (n = 1, 2, 3, \dots)",
        "ejemplo": """CLASE MAGISTRAL: ONDAS ESTACIONARIAS Y MODOS NORMALES
1. Principio de Superposición Lineal:
Cuando dos o más ondas se propagan simultáneamente en el mismo medio elástico, la función de onda resultante es la suma algebraica directa de las perturbaciones individuales: y(x, t) = y_1(x, t) + y_2(x, t).
2. Formación de Ondas Estacionarias:
Surgen de la interferencia de dos ondas idénticas viajando en direcciones opuestas:
y_total = A sin(kx - omega t) + A sin(kx + omega t) = [ 2A sin(kx) ] * cos(omega t).
A diferencia de las ondas viajeras, no transportan energía neta a lo largo del eje x.
- Nodos: Puntos donde la amplitud es permanentemente cero (sin(kx) = 0 => x = n lambda / 2).
- Antinodos (Vientres): Puntos de máxima oscilación (x = (2n + 1) lambda / 4).
3. Problema Resuelto 1 (Aplicación Directa):
Una cuerda de guitarra de acero de longitud L = 0.65 m y densidad lineal mu = 4.0 * 10^-3 kg/m está afinada para que su modo fundamental (n = 1) vibre a f_1 = 440 Hz (Nota La). Determine la tensión mecánica T a la que debe ajustarse la cuerda.
Solución:
Para extremos fijos: f_n = n * v / (2L).
Para n = 1: f_1 = v / (2L) ==> v = 2 * L * f_1.
v = 2 * (0.65 m) * (440 Hz) = 1.30 * 440 = 572.0 m/s.
Como v = sqrt(T / mu):
T = mu * v^2 = (4.0e-3 kg/m) * (572.0 m/s)^2 = 4.0e-3 * 327,184 = 1,308.74 N.
La cuerda requiere una tensión de 1.31 kN.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un cable de puente atirantado de longitud L = 80 m y densidad mu = 12 kg/m está sometido a una tensión T = 4.8 * 10^5 N. Vórtices de viento periódicos (desprendimiento de vórtices de Von Kármán) inducen una oscilación estacionaria correspondiente al tercer armónico (n = 3). Calcule la frecuencia de excitación f_3, la longitud de onda lambda_3 y las posiciones exactas de todos los nodos medidos desde un extremo fijo.
Solución:
1. Velocidad de onda transversal:
v = sqrt(T / mu) = sqrt(4.8e5 / 12) = sqrt(40,000) = 200.0 m/s.
2. Longitud de onda para n = 3:
lambda_n = 2L / n ==> lambda_3 = (2 * 80) / 3 = 160 / 3 = 53.333 m.
3. Frecuencia del tercer armónico:
f_3 = 3 * v / (2L) = (3 * 200) / (2 * 80) = 600 / 160 = 3.75 Hz.
4. Posiciones de los nodos (donde la amplitud es nula):
x_m = m * (lambda_3 / 2) = m * (53.333 / 2) = m * 26.667 m, para m = 0, 1, 2, 3.
- Nodo 1 (extremo inicial): x_0 = 0.0 m.
- Nodo 2: x_1 = 26.67 m.
- Nodo 3: x_2 = 53.33 m.
- Nodo 4 (extremo final): x_3 = 80.0 m.
Se forman 3 vientres de oscilación intercalados a 13.33 m, 40.0 m y 66.67 m.""",
        "bloque_sugerido": "Laboratorio 50 min • Modos normales en cuerdas y columnas de aire",
        "slides": [
            {"numero": 1, "seccion": "SUPERPOSICIÓN", "titulo": "Ondas Estacionarias", "puntos": ["Interferencia de ondas opuestas sin transporte neto de energía.", "Nodos estacionarios de amplitud nula y antinodos de máxima vibración."]},
            {"numero": 2, "seccion": "ARMÓNICOS", "titulo": "Frecuencias Resonantes", "puntos": ["Serie armónica f_n = n v / (2L) en condiciones de contorno fijas.", "Riesgo de resonancia inducida por viento en cables de transporte."]}
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Ondas Sonoras, Presión Acústica y Escala de Decibeles",
        "objetivo": "Calcular la velocidad del sonido en medios continuos y evaluar niveles de presión sonora (dB) en parques eólicos.",
        "concepto_clave_latex": r"v_s = \sqrt{\frac{B}{\rho}} = \sqrt{\gamma \frac{R_{\text{esp}} T}{M}} \quad ; \quad \beta = 10 \log_{10}\left(\frac{I}{I_0}\right) \quad (I_0 = 10^{-12}\,\text{W/m}^2)",
        "ejemplo": """CLASE MAGISTRAL: ACÚSTICA TÉCNICA Y PRESIÓN SONORA
1. Naturaleza Longitudinal del Sonido:
Las ondas sonoras son ondas elásticas longitudinales de presión y densidad que se propagan mediante compresiones y rarefacciones adiabáticas en un fluido compressible: v = sqrt(B_adiab / rho) = sqrt(gamma R T).
2. Intensidad Acústica y Escala Logarítmica de Decibeles (dB):
El oído humano responde logarítmicamente a la presión acústica en un rango que abarca 12 órdenes de magnitud (desde el umbral auditivo I_0 = 10^-12 W/m^2 hasta el umbral del dolor 1 W/m^2 = 120 dB).
Nivel sonoro: beta = 10 * log_10(I / I_0) [dB].
3. Problema Resuelto 1 (Aplicación Directa):
Calcule la velocidad del sonido en aire seco a nivel del mar para una tarde cálida en Santa Marta a T = 35 °C (308.15 K), considerando gamma = 1.40 y constante de gas del aire R_esp = 287 J/(kg*K).
Solución:
v_s = sqrt( gamma * R_esp * T )
v_s = sqrt( 1.40 * 287 * 308.15 ) = sqrt( 123,814.67 ) = 351.87 m/s.
(A 0 °C la velocidad es ~331 m/s; la temperatura incrementa significativamente la velocidad del sonido).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un aerogenerador produce un nivel de potencia acústica que genera una intensidad sonora I_1 = 1.0 * 10^-6 W/m^2 a una distancia r_1 = 100 m. Determine: a) El nivel en decibeles beta_1 a 100 m; b) El nivel en decibeles beta_2 a una distancia r_2 = 400 m asumiendo propagación esférica sin absorción atmosférica; c) El efecto de operar dos aerogeneradores idénticos simultáneamente en el mismo sitio.
Solución:
a) Nivel a 100 m:
beta_1 = 10 * log_10( 1.0e-6 / 1.0e-12 ) = 10 * log_10( 10^6 ) = 10 * 6 = 60.0 dB.
b) Nivel a 400 m:
Por la ley del inverso del cuadrado para ondas esféricas: I prop 1 / r^2.
I_2 = I_1 * (r_1 / r_2)^2 = 1.0e-6 * (100 / 400)^2 = 1.0e-6 * (1/16) = 6.25 * 10^-8 W/m^2.
beta_2 = 10 * log_10( 6.25e-8 / 1.0e-12 ) = 10 * log_10( 62,500 ) = 10 * 4.7959 = 47.96 dB.
(Cada duplicación de distancia reduce el nivel en exactamente 6 dB: de 100m a 200m cae a 54 dB, y a 400m cae a 48 dB).
c) Dos aerogeneradores simultáneos:
La intensidad se duplica: I_total = 2 * I_1.
beta_total = 10 * log_10( 2 * I_1 / I_0 ) = beta_1 + 10 * log_10(2) = 60.0 + 3.01 = 63.01 dB.
(Duplicar la fuente sonora incrementa el nivel sonoro en sólo 3 dB).""",
        "bloque_sugerido": "Laboratorio 50 min • Atenuación geométrica del ruido y decibeles",
        "slides": [
            {"numero": 1, "seccion": "SONIDO", "titulo": "Ondas Longitudinales de Presión", "puntos": ["Velocidad adiabática en gases v = sqrt(gamma R T).", "Compresiones y rarefacciones como perturbación de densidad."]},
            {"numero": 2, "seccion": "DECIBELES", "titulo": "Escala Acústica Logarítmica", "puntos": ["Definición beta = 10 log_10(I / I_0) y umbrales auditivos.", "Atenuación geométrica de 6 dB por duplicación de distancia."]}
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Efecto Doppler y Ondas de Choque en Fluidos",
        "objetivo": "Calcular corrimientos de frecuencia por movimiento relativo y comprender el número de Mach.",
        "concepto_clave_latex": r"f' = f \left(\frac{v \pm v_o}{v \mp v_s}\right) \quad ; \quad \sin(\theta_{\text{Mach}}) = \frac{v}{v_s} = \frac{1}{M}",
        "ejemplo": """CLASE MAGISTRAL: CINEMÁTICA ONDULATORIA Y EFECTO DOPPLER
1. Corrimiento de Frecuencia por Movimiento Relativo:
Cuando una fuente emisora de ondas o un observador se mueven con respecto al medio elástico, la frecuencia percibida f' difiere de la frecuencia emitida propia f:
- Acercamiento mutuo: Frecuencia aparente más alta (tono más agudo).
- Alejamiento mutuo: Frecuencia aparente más baja (tono más grave).
2. Régimen Supersónico y Cono de Mach:
Si la fuente se desplaza a una velocidad v_fuente superior a la velocidad del sonido v en el fluido (Número de Mach M = v_fuente / v > 1), las crestas de onda se superponen constructivamente formando una superficie cónica de discontinuidad de presión (onda de choque o estampido sónico).
3. Problema Resuelto 1 (Aplicación Directa):
Un vehículo de inspección de redes eléctricas se desplaza a v_o = 25 m/s aproximándose hacia una subestación fija que tiene una sirena de alarma emitiendo a f = 1000 Hz. La velocidad del sonido en el aire es v = 340 m/s. Calcule la frecuencia percibida por los técnicos a bordo del vehículo: a) Mientras se aproximan; b) Tras sobrepasar la subestación y alejarse.
Solución:
Fuente estacionaria: v_s = 0. Observador en movimiento: v_o = 25 m/s.
a) En aproximación (signo + en numerador):
f'_aprox = f * [ (v + v_o) / v ]
f'_aprox = 1000 * [ (340 + 25) / 340 ] = 1000 * (365 / 340) = 1073.53 Hz.
b) En alejamiento (signo - en numerador):
f'_alej = f * [ (v - v_o) / v ]
f'_alej = 1000 * [ (340 - 25) / 340 ] = 1000 * (315 / 340) = 926.47 Hz.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un anemómetro acústico ultrasónico (Sonic Anemometer) en una torre eólica mide la velocidad horizontal del viento v_viento midiendo la diferencia de tiempo de tránsito delta_t entre dos pulsos ultrasónicos de frecuencia f = 40 kHz emitidos en sentidos opuestos a través de una distancia fija d = 0.20 m. Deduzca la expresión analítica para v_viento en función de delta_t y calcule el valor para delta_t = 8.5 microsegundos (v_sonido = 345 m/s).
Solución:
Tiempo en sentido a favor del viento: t_1 = d / (c + v_viento).
Tiempo en sentido en contra del viento: t_2 = d / (c - v_viento).
Diferencia de tiempos:
delta_t = t_2 - t_1 = d * [ 1/(c - v_viento) - 1/(c + v_viento) ] = d * [ (c + v - c + v) / (c^2 - v^2) ] = (2 d v_viento) / (c^2 - v_viento^2).
Dado que v_viento << c (v_viento^2 << c^2):
delta_t approx (2 d / c^2) * v_viento.
Despejando la velocidad del viento:
v_viento = (c^2 * delta_t) / (2 d).
Evaluando numéricamente:
v_viento = [ (345)^2 * (8.5 * 10^-6 s) ] / [ 2 * 0.20 m ]
v_viento = [ 119,025 * 8.5e-6 ] / 0.40 = 1.0117 / 0.40 = 2.529 m/s.
El anemómetro ultrasónico mide la velocidad del viento con precisión milimétrica sin piezas móviles mediante el principio Doppler de tiempos de vuelo.""",
        "bloque_sugerido": "Laboratorio 50 min • Anemometría sónica y efecto Doppler",
        "slides": [
            {"numero": 1, "seccion": "DOPPLER", "titulo": "Efecto Doppler Clásico", "puntos": ["Fórmula general f' = f (v +- v_o) / (v -+ v_s).", "Compresión espacial de frentes de onda en la dirección del movimiento."]},
            {"numero": 2, "seccion": "ULTRASONIDO", "titulo": "Anemometría Acústica", "puntos": ["Medición de velocidad del viento por diferencia de tiempo de vuelo delta_t.", "Cono de Mach y régimen supersónico para M > 1."]}
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Gravitación Universal, Campo Gravitatorio y Velocidad de Escape",
        "objetivo": "Modelar campos gravitacionales, energía potencial gravitatoria en el espacio y velocidades orbitales.",
        "concepto_clave_latex": r"\vec{F}_g = -G \frac{M m}{r^2}\hat{r} \quad ; \quad U(r) = -G \frac{M m}{r} \quad ; \quad v_{\text{esc}} = \sqrt{\frac{2 G M}{R}}",
        "ejemplo": """CLASE MAGISTRAL: LEY DE GRAVITACIÓN UNIVERSAL Y ENERGÍA ORBITAL
1. Ley del Inverso del Cuadrado de Newton:
Toda partícula de masa M atrae a otra de masa m con una fuerza central radial dirigida hacia ella, directamente proporcional al producto de sus masas e inversamente proporcional al cuadrado de la distancia r entre sus centros: F_g = G M m / r^2, con G = 6.674 * 10^-11 N*m^2/kg^2.
2. Energía Potencial Gravitacional Universal:
Tomando el nivel de referencia cero en el infinito (U(infinito) = 0): U(r) = - int_infinito^r F_g dr = - G M m / r. El potencial es estrictamente negativo, reflejando que el sistema masa-tierra es un estado ligado.
3. Velocidad de Escape:
Velocidad inicial mínima requerida para que un proyectil lanzado desde la superficie de un astro escape de su atracción gravitatoria y llegue al infinito con velocidad residual cero:
(1/2) m v_esc^2 - G M m / R = 0 => v_esc = sqrt(2 G M / R).
4. Problema Resuelto 1 (Aplicación Directa):
Calcule la velocidad de escape desde la superficie de la Tierra (M_T = 5.972 * 10^24 kg, radio medio R_T = 6,371 km = 6.371 * 10^6 m).
Solución:
v_esc = sqrt( (2 * G * M_T) / R_T )
v_esc = sqrt( [ 2 * (6.674e-11) * (5.972e24) ] / (6.371e6) )
v_esc = sqrt( [ 7.971e14 ] / (6.371e6) ) = sqrt( 1.2511 * 10^8 ) = 11,185 m/s = 11.19 km/s.
(Cualquier sonda espacial requiere al menos 11.2 km/s para salir del pozo gravitatorio terrestre).
5. Problema Resuelto 2 (Nivel Examen Parcial):
Un satélite meteorológico de monitoreo de radiación solar de masa m = 1,500 kg se encuentra en una órbita circular a una altitud h = 800 km sobre la superficie terrestre. Determine: a) La velocidad orbital v_orb; b) La energía mecánica total del satélite; c) La energía adicional necesaria para transferirlo a una órbita más alta a h_2 = 1,600 km.
Solución:
Radio orbital 1: r_1 = R_T + h = 6,371 + 800 = 7,171 km = 7.171 * 10^6 m.
Constante mu_T = G * M_T = 3.986 * 10^14 m^3/s^2.
a) Velocidad orbital (F_g = F_c):
G M m / r_1^2 = m v_orb^2 / r_1 ==> v_orb = sqrt(G M / r_1)
v_orb = sqrt( 3.986e14 / 7.171e6 ) = sqrt( 5.5585e7 ) = 7,455.5 m/s = 7.456 km/s.
b) Energía mecánica total (Teorema del Virial E = -K = U/2):
E_total_1 = - (G M m) / (2 r_1) = - (3.986e14 * 1500) / (2 * 7.171e6) = - 5.979e17 / 1.4342e7 = - 4.1689 * 10^10 J = - 41.69 GJ.
c) En r_2 = 6,371 + 1600 = 7,971 km = 7.971 * 10^6 m:
E_total_2 = - (3.986e14 * 1500) / (2 * 7.971e6) = - 5.979e17 / 1.5942e7 = - 3.7505 * 10^10 J = - 37.51 GJ.
Energía adicional requerida suministrada por los propulsores:
Delta_E = E_total_2 - E_total_1 = (-37.51 GJ) - (-41.69 GJ) = + 4.18 GJ de energía positiva.""",
        "bloque_sugerido": "Pomodoro 50/10 • Leyes gravitacionales y energía orbital",
        "slides": [
            {"numero": 1, "seccion": "GRAVITACIÓN", "titulo": "Fuerza y Potencial Universal", "puntos": ["Ley de Newton F = G M m / r^2 y potencial U(r) = -G M m / r.", "Velocidad de escape v_esc = sqrt(2 G M / R) para superación del pozo gravitatorio."]},
            {"numero": 2, "seccion": "ÓRBITAS", "titulo": "Energía de Satélites", "puntos": ["Teorema del Virial E_total = -K = U/2 para trayectorias circulares.", "Cálculo de delta_E para maniobras de elevación orbital."]}
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Leyes de Kepler y Satélites Geoestacionarios",
        "objetivo": "Aplicar las tres Leyes de Kepler y calcular el radio y altitud de una órbita geoestacionaria (GEO).",
        "concepto_clave_latex": r"T^2 = \left(\frac{4\pi^2}{G M}\right) a^3 \quad ; \quad r_{\text{geo}} = \sqrt[3]{\frac{G M T_{\text{sidéreo}}^2}{4\pi^2}} \approx 42,164\text{ km}",
        "ejemplo": """CLASE MAGISTRAL: MECÁNICA CELESTE Y SATÉLITES GEOESTACIONARIOS
1. Las Tres Leyes de Johannes Kepler:
- 1ra Ley (Ley de las Órbitas): Los planetas se mueven en elipses con el Sol en uno de sus focos.
- 2da Ley (Ley de las Áreas): El vector de posición barre áreas iguales en tiempos iguales (dA/dt = L / (2m) = constante, consecuencia de la conservación del momento angular en fuerzas centrales).
- 3ra Ley (Ley de los Periodos): El cuadrado del periodo orbital es proporcional al cubo del semieje mayor: T^2 = (4 pi^2 / (G M)) * a^3.
2. Órbita Geoestacionaria (Geostationary Earth Orbit - GEO):
Órbita circular ecuatorial directa cuyo periodo orbital coincide exactamente con el periodo de rotación sidéreo de la Tierra (T_sidéreo = 23 h 56 min 4 s = 86,164.1 s). Un satélite en GEO parece suspendido inmóvil sobre el mismo punto de la superficie terrestre, fundamental para satélites meteorológicos (GOES) que alimentan modelos solares y de viento.
3. Problema Resuelto 1 (Aplicación Directa):
Demuestre analíticamente el radio orbital exacto de la órbita geoestacionaria r_geo y determine su altitud sobre la superficie terrestre (M_T = 5.972 * 10^24 kg, R_T = 6,371 km).
Solución:
De la Tercera Ley de Kepler:
T^2 = (4 pi^2 / (G M_T)) * r_geo^3.
Despejando r_geo:
r_geo = [ (G * M_T * T_sidéreo^2) / (4 pi^2) ]^(1/3).
Evaluando:
G * M_T = 3.9860 * 10^14 m^3/s^2.
T_sidéreo = 86,164 s ==> T^2 = (86,164)^2 = 7.4242 * 10^9 s^2.
Numerador: (3.9860e14) * (7.4242e9) = 2.9593 * 10^24.
Dividiendo entre 4 pi^2 (39.4784):
r_geo^3 = 2.9593e24 / 39.4784 = 7.4960 * 10^22 m^3.
Extrayendo raíz cúbica:
r_geo = (7.4960e22)^(1/3) = 42,164,140 m = 42,164 km desde el centro de la Tierra.
Altitud sobre la superficie:
h_geo = r_geo - R_T = 42,164 km - 6,371 km = 35,793 km (aproximadamente 35,800 km).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un asteroide orbita el Sol con un perihelio r_p = 1.0 UA y un afelio r_a = 5.0 UA (donde 1 UA es la distancia media Tierra-Sol = 1.496 * 10^11 m). Calcule el semieje mayor a, la excentricidad de la órbita e y el periodo orbital T en años terrestres aplicando la Tercera Ley de Kepler.
Solución:
1. Semieje mayor a:
El eje mayor completo es 2a = r_p + r_a = 1.0 + 5.0 = 6.0 UA.
a = 6.0 / 2 = 3.0 UA.
2. Excentricidad e:
r_p = a * (1 - e) ==> 1.0 = 3.0 * (1 - e) ==> 1 - e = 1/3 ==> e = 1 - 1/3 = 2/3 approx 0.6667.
3. Periodo orbital en años:
Para el sistema solar con unidades T en años y a en UA, la Tercera Ley de Kepler se simplifica a:
T^2 = a^3.
T^2 = (3.0)^3 = 27.0.
T = sqrt(27.0) = 5.196 años terrestres.""",
        "bloque_sugerido": "Laboratorio 50 min • Órbita geoestacionaria y leyes de Kepler",
        "slides": [
            {"numero": 1, "seccion": "KEPLER", "titulo": "Leyes de la Mecánica Celeste", "puntos": ["1ra Ley: elipses; 2da Ley: velocidad areolar constante por momento angular.", "3ra Ley: relación armónica T^2 proporcional al semieje mayor a^3."]},
            {"numero": 2, "seccion": "GEO", "titulo": "Órbita Geoestacionaria", "puntos": ["Sincronización con el día sidéreo a 35,786 km de altitud.", "Monitoreo satelital continuo de radiación solar y cobertura nubosa."]}
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Dinámica de Fluidos Ideales: Continuidad y Ecuación de Bernoulli",
        "objetivo": "Aplicar la conservación de masa y energía en líneas de corriente para fluidos incompresibles no viscosos.",
        "concepto_clave_latex": r"A_1 v_1 = A_2 v_2 = Q \quad ; \quad P_1 + \frac{1}{2}\rho v_1^2 + \rho g z_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g z_2 = \text{constante}",
        "ejemplo": """CLASE MAGISTRAL: DINÁMICA DE FLUIDOS IDEALES Y BERNOULLI
1. Hipótesis del Fluido Ideal:
Un fluido es ideal si es incompresible (densidad rho = constante), no viscoso (fricción interna nula), flujo estacionario (propiedades independientes del tiempo en cada punto) e irrotacional.
2. Ecuación de Continuidad (Conservación de la Masa):
El caudal volumétrico Q se conserva a lo largo de un tubo de flujo: Q = A_1 * v_1 = A_2 * v_2. Si el área disminuye, la velocidad se incrementa proporcionalmente.
3. Ecuación de Bernoulli (Conservación de la Energía Mecánica):
Integración de las ecuaciones de Euler a lo largo de una línea de corriente:
P / (rho g) + v^2 / (2g) + z = H = constante.
- Altura piezométrica: P / (rho g).
- Altura cinética o dinámica: v^2 / (2g).
- Altura geométrica o de posición: z.
4. Problema Resuelto 1 (Aplicación Directa):
Una tubería forzada que alimenta una pequeña central hidroeléctrica reduce su diámetro desde D_1 = 0.60 m en la parte superior hasta D_2 = 0.30 m en el inyector. Si el caudal turbinado es Q = 0.50 m^3/s, calcule las velocidades medias v_1 y v_2.
Solución:
Área 1: A_1 = pi * (D_1/2)^2 = pi * (0.30)^2 = 0.2827 m^2.
Velocidad 1: v_1 = Q / A_1 = 0.50 / 0.2827 = 1.768 m/s.
Área 2: A_2 = pi * (D_2/2)^2 = pi * (0.15)^2 = 0.07069 m^2.
Velocidad 2: v_2 = Q / A_2 = 0.50 / 0.07069 = 7.073 m/s.
(Al reducir el diámetro a la mitad, el área se divide por 4 y la velocidad se cuadruplica).
5. Problema Resuelto 2 (Nivel Examen Parcial):
En la tubería anterior, el punto 1 se encuentra a una cota z_1 = 50 m con una presión manométrica P_1 = 200 kPa. El punto 2 se encuentra en la casa de máquinas a nivel del suelo z_2 = 0 m con D_2 = 0.30 m. Calcule la presión manométrica P_2 disponible a la entrada de la turbina (rho_agua = 1000 kg/m^3, g = 9.81 m/s^2).
Solución:
Ecuación de Bernoulli entre 1 y 2:
P_1 + 0.5 * rho * v_1^2 + rho * g * z_1 = P_2 + 0.5 * rho * v_2^2 + rho * g * z_2.
Despejando P_2:
P_2 = P_1 + rho * g * (z_1 - z_2) + 0.5 * rho * (v_1^2 - v_2^2).
Evaluando términos:
1. P_1 = 200,000 Pa.
2. Cabeza estática: rho * g * (50 - 0) = 1000 * 9.81 * 50 = 490,500 Pa.
3. Diferencia cinética: 0.5 * 1000 * [ (1.768)^2 - (7.073)^2 ] = 500 * [ 3.126 - 50.027 ] = 500 * (-46.901) = -23,450 Pa.
Presión en el punto 2:
P_2 = 200,000 + 490,500 - 23,450 = 667,050 Pa = 667.05 kPa.
La presión creció de 200 kPa a 667 kPa debido a la conversión de energía potencial gravitacional en presión hidrostática.""",
        "bloque_sugerido": "Laboratorio 50 min • Teorema de Bernoulli en tuberías convergentes",
        "slides": [
            {"numero": 1, "seccion": "CONTINUIDAD", "titulo": "Conservación de la Masa", "puntos": ["Ecuación Q = A_1 v_1 = A_2 v_2 para fluidos incompresibles.", "Aumento cuadrático de la velocidad al estrecharse la sección de flujo."]},
            {"numero": 2, "seccion": "BERNOULLI", "titulo": "Líneas de Corriente y Energía", "puntos": ["Conservación de energía P + 1/2 rho v^2 + rho g z = constante.", "Intercambio continuo entre presión estática, dinámica y potencial."]}
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Aplicaciones de Bernoulli: Venturi, Pitot y Teorema de Torricelli",
        "objetivo": "Calcular caudales y velocidades de flujo en instrumentación hidráulica y orificios de descarga.",
        "concepto_clave_latex": r"Q_{\text{venturi}} = A_2 \sqrt{\frac{2(P_1 - P_2)}{\rho(1 - (A_2/A_1)^2)}} \quad ; \quad v_{\text{pitot}} = \sqrt{\frac{2(P_{\text{estanc}} - P_{\text{est}})}{\rho}} \quad ; \quad v_{\text{torricelli}} = \sqrt{2 g h}",
        "ejemplo": """CLASE MAGISTRAL: INSTRUMENTACIÓN DE FLUJO BASADA EN BERNOULLI
1. Tubo Venturi:
Estrechamiento calibrado donde la caída de presión estática Delta P = P_1 - P_2 es directamente proporcional al cuadrado del caudal volumétrico Q^2.
2. Tubo de Pitot:
Mide la presión de estancamiento en un punto donde el fluido se frena a velocidad cero (v = 0). La diferencia entre la presión total de estancamiento y la presión estática lateral arroja la velocidad local instantánea: v = sqrt(2 Delta P / rho). Estándar en aeronaves y túneles de viento eólicos.
3. Teorema de Torricelli:
Velocidad de salida de un fluido a través de un pequeño orificio situado a una profundidad h bajo la superficie libre de un gran tanque abierto: v = sqrt(2 g h).
4. Problema Resuelto 1 (Aplicación Directa):
Un tanque de almacenamiento de agua de refrigeración de una central termoeléctrica tiene una altura de nivel h = 4.5 m respecto a un orificio de drenaje de diámetro d = 50 mm abierto a la atmósfera. Calcule la velocidad teórica de salida por Torricelli y el caudal volumétrico de drenaje.
Solución:
Velocidad de salida:
v = sqrt(2 * g * h) = sqrt(2 * 9.81 * 4.5) = sqrt(88.29) = 9.396 m/s.
Área del orificio:
A = pi * (d/2)^2 = pi * (0.025 m)^2 = 1.9635 * 10^-3 m^2.
Caudal de descarga teórico:
Q = A * v = (1.9635e-3 m^2) * (9.396 m/s) = 0.01845 m^3/s = 18.45 litros/segundo.
5. Problema Resuelto 2 (Nivel Examen Parcial):
Un tubo Venturi horizontal instalado en una tubería de agua (rho = 1000 kg/m^3) tiene un diámetro de entrada D_1 = 200 mm y una garganta D_2 = 100 mm. Un manómetro diferencial de mercurio (rho_Hg = 13,600 kg/m^3) conectado entre la entrada y la garganta marca un desnivel Delta h = 150 mm = 0.15 m. Determine la caída de presión Delta P en Pascales y el caudal volumétrico Q que fluye por la tubería.
Solución:
1. Caída de presión manométrica:
Delta P = P_1 - P_2 = (rho_Hg - rho_agua) * g * Delta h
Delta P = (13,600 - 1000) * 9.81 * 0.15 = 12,600 * 9.81 * 0.15 = 18,540.9 Pa = 18.54 kPa.
2. Relación de áreas:
A_1 / A_2 = (D_1 / D_2)^2 = (200 / 100)^2 = 4.0 ==> A_2 / A_1 = 0.25.
(A_2 / A_1)^2 = 0.0625.
3. Área de la garganta A_2:
A_2 = pi * (0.05)^2 = 7.854 * 10^-3 m^2.
4. Caudal por fórmula de Venturi:
Q = A_2 * sqrt( [ 2 * Delta P ] / [ rho * (1 - (A_2/A_1)^2) ] )
Q = 7.854e-3 * sqrt( [ 2 * 18540.9 ] / [ 1000 * (1 - 0.0625) ] )
Q = 7.854e-3 * sqrt( [ 37081.8 ] / [ 937.5 ] ) = 7.854e-3 * sqrt( 39.554 )
Q = 7.854e-3 * 6.2892 = 0.0494 m^3/s = 49.4 litros/segundo.""",
        "bloque_sugerido": "Laboratorio 50 min • Medición de caudal con tubo Venturi y Pitot",
        "slides": [
            {"numero": 1, "seccion": "VENTURI", "titulo": "Tubo Venturi y Presión Diferencial", "puntos": ["Estrechamiento de sección y caída de presión estática proporcional a Q^2.", "Medición industrial de caudal con mínima pérdida de carga permanente."]},
            {"numero": 2, "seccion": "PITOT", "titulo": "Tubo de Pitot y Torricelli", "puntos": ["Presión de estancamiento total para determinar velocidad local v.", "Teorema de Torricelli v = sqrt(2gh) para descarga libre por orificios."]}
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Viscosidad, Fluidos Reales, Número de Reynolds y Darcy-Weisbach",
        "objetivo": "Calcular esfuerzos cortantes viscosos, clasificar régimen de flujo laminar/turbulento y evaluar pérdidas por fricción.",
        "concepto_clave_latex": r"\tau = \mu \frac{dv}{dy} \quad ; \quad Re = \frac{\rho v D}{\mu} \quad ; \quad h_f = f \frac{L}{D} \frac{v^2}{2g}",
        "ejemplo": """CLASE MAGISTRAL: MECÁNICA DE FLUIDOS REALES Y PÉRDIDAS POR FRICCIÓN
1. Ley de Viscosidad de Newton:
En fluidos reales, el movimiento relativo entre capas adyacentes genera fricción interna cuantificada por la viscosidad dinámica mu [Pa*s]: tau = mu * (dv/dy).
2. Número de Reynolds (Re):
Parámetro adimensional que relaciona las fuerzas inerciales con las fuerzas viscosas:
Re = (rho * v * D) / mu = (v * D) / nu.
- Re < 2300: Flujo Laminar (capas suaves y ordenadas; f = 64 / Re).
- 2300 <= Re <= 4000: Zona de Transición crítica.
- Re > 4000: Flujo Turbulento (vórtices caóticos, mezcla intensa y mayor resistencia al avance).
3. Ecuación de Darcy-Weisbach para Pérdidas de Carga Distribuidas:
h_f = f * (L / D) * (v^2 / (2g)), donde el factor de fricción f se obtiene analíticamente (laminar) o del Diagrama de Moody / Ecuación de Colebrook-White (turbulento).
4. Problema Resuelto 1 (Aplicación Directa):
Aceite lubricante de turbina (rho = 880 kg/m^3, viscosidad dinámica mu = 0.080 Pa*s) fluye por una tubería de diámetro interior D = 50 mm a una velocidad media v = 1.2 m/s. Determine el Número de Reynolds, clasifique el régimen de flujo y calcule el factor de fricción de Darcy f.
Solución:
Re = (rho * v * D) / mu
Re = (880 kg/m^3 * 1.2 m/s * 0.050 m) / (0.080 Pa*s) = (52.8) / (0.080) = 660.
Como Re = 660 < 2300, el flujo es estrictamente LAMINAR.
Factor de fricción de Darcy en régimen laminar:
f = 64 / Re = 64 / 660 = 0.09697.
5. Problema Resuelto 2 (Nivel Examen Parcial):
En una central hidroeléctrica, fluye agua (rho = 1000 kg/m^3, nu = 1.0 * 10^-6 m^2/s) a través de una tubería forzada de acero soldado de diámetro D = 0.80 m y longitud L = 250 m con velocidad media v = 3.5 m/s. Si el factor de fricción obtenido del diagrama de Moody es f = 0.018:
a) Verifique que el flujo es altamente turbulento calculando Re.
b) Calcule la pérdida de carga por fricción h_f en metros de columna de agua.
c) Determine la potencia hidráulica disipada en forma de calor por fricción en kW.
Solución:
a) Número de Reynolds:
Re = (v * D) / nu = (3.5 * 0.80) / (1.0e-6) = 2.80 / 1.0e-6 = 2,800,000 (2.8 * 10^6).
Como Re = 2.8 * 10^6 >> 4000, el flujo es plenamente TURBULENTO.
b) Pérdida de carga de Darcy-Weisbach:
h_f = f * (L / D) * [ v^2 / (2g) ]
h_f = 0.018 * (250 / 0.80) * [ (3.5)^2 / (2 * 9.81) ]
h_f = 0.018 * (312.5) * [ 12.25 / 19.62 ] = 5.625 * 0.62436 = 3.512 metros de agua.
c) Caudal volumétrico:
Q = A * v = pi * (0.40)^2 * 3.5 = 0.50265 * 3.5 = 1.7593 m^3/s.
Potencia disipada por fricción:
P_perdida = rho * g * Q * h_f
P_perdida = (1000 kg/m^3) * (9.81 m/s^2) * (1.7593 m^3/s) * (3.512 m) = 60,612 Watts = 60.61 kW.
Se pierden 60.6 kW de potencia mecánica disipados como calor en las paredes de la tubería.""",
        "bloque_sugerido": "Laboratorio 50 min • Número de Reynolds y pérdidas de Darcy-Weisbach",
        "slides": [
            {"numero": 1, "seccion": "VISCOSIDAD", "titulo": "Leyes de Newton y Reynolds", "puntos": ["Tensión de corte viscosa tau = mu dv/dy.", "Número de Reynolds Re = rho v D / mu: criterio de transición laminar-turbulento."]},
            {"numero": 2, "seccion": "PÉRDIDAS", "titulo": "Ecuación de Darcy-Weisbach", "puntos": ["Pérdidas de carga distribuidas h_f = f (L/D) (v^2/2g).", "Factor f de Moody y cuantificación de potencia disipada en tuberías forzadas."]}
        ]
    }
]

if __name__ == '__main__':
    target = '      - codigo: "03041819"'
    yaml_text = format_topics_yaml(topics_10_to_20 + topics_21_to_30)
    inject_topics_after(target, yaml_text)
    print("02021810 Física Mecánica now has 30 topics!")
