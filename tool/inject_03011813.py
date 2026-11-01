# -*- coding: utf-8 -*-
import sys
from injector_base import format_topics_yaml, inject_topics_after

topics = [
    {
        "numero_tema": 10,
        "corte": 1,
        "modalidad": "tecnica",
        "titulo": "Algoritmos de Búsqueda, Ordenamiento y Complejidad Asintótica (Big-O)",
        "objetivo": "Analizar y optimizar la complejidad temporal O(n log n) y espacial de algoritmos de procesamiento de datos.",
        "concepto_clave_latex": r"T(n) = 2 T(n/2) + \mathcal{O}(n) \implies T(n) \in \mathcal{O}(n \log n) \quad ; \quad T_{\text{bin}}(n) \in \mathcal{O}(\log_2 n)",
        "ejemplo": """CLASE MAGISTRAL: COMPLEJIDAD COMPUTACIONAL Y ALGORITMOS DE BÚSQUEDA
1. Notación Asintótica Big-O y Teorema Maestro:
En ingeniería computacional aplicada a telemetría masiva de redes eléctricas (SCADA), el tiempo de cómputo no se mide en segundos de reloj, sino en cómo escala el número de operaciones elementales f(n) con respecto al tamaño de entrada n cuando n tiende a infinito. Formalmente, f(n) en O(g(n)) sii existen constantes c > 0 y n_0 tales que 0 <= f(n) <= c * g(n) para todo n >= n_0.
2. Algoritmos de Búsqueda Binaria y Quicksort:
La búsqueda lineal sobre n registros desordenados requiere O(n) comparaciones. Si el arreglo de mediciones horarias está ordenado, la búsqueda binaria divide el espacio de búsqueda a la mitad en cada paso: T(n) = T(n/2) + O(1), resolviéndose en O(log_2 n). Quicksort particiona respecto a un pivote; su relación de recurrencia en caso promedio T(n) = 2T(n/2) + O(n) produce O(n log n) por el Teorema Maestro.
3. Problema Resuelto 1 (Aplicación Directa):
Un sistema SCADA almacena N = 1,048,576 mediciones de tensión ordenadas temporalmente. Determine cuántas comparaciones como máximo requiere la búsqueda binaria para encontrar un evento anómalo específico en comparación con una búsqueda lineal.
Solución: En el peor caso de búsqueda lineal: C_lineal = N = 1,048,576 comparaciones.
Para búsqueda binaria: C_binaria = ceil(log_2(N)) = ceil(log_2(2^20)) = 20 comparaciones.
El factor de aceleración es A = 1,048,576 / 20 = 52,428.8 veces más rápido.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Dado un algoritmo recursivo de ordenamiento por división donde T(n) = 4T(n/2) + c*n, determine su complejidad asintótica usando el Teorema Maestro y compare con Quicksort.
Solución: Identificamos a = 4, b = 2, f(n) = c*n = O(n^1).
Calculamos el exponente crítico: log_b(a) = log_2(4) = 2.
Comparamos f(n) = O(n^1) con n^(log_b(a)) = n^2. Dado que 1 < 2, f(n) = O(n^(2 - epsilon)) con epsilon = 1.
Aplica el Caso 1 del Teorema Maestro: T(n) = Theta(n^(log_b(a))) = Theta(n^2).
Conclusión: Este algoritmo es cuadrático Theta(n^2), subóptimo frente al caso promedio de Quicksort que es Theta(n log n).""",
        "bloque_sugerido": "Laboratorio 50 min • Algoritmos de búsqueda y complejidad Big-O",
        "slides": [
            {"numero": 1, "seccion": "TEORÍA", "titulo": "Complejidad Asintótica Big-O", "puntos": ["Escalabilidad temporal y espacial frente a grandes volúmenes de datos.", "Clases típicas: O(1) constante, O(log n) logarítmico, O(n) lineal, O(n log n), O(n^2)."]},
            {"numero": 2, "seccion": "ALGORITMOS", "titulo": "Búsqueda Binaria y Quicksort", "puntos": ["Búsqueda binaria reduce 1 millón de registros a 20 iteraciones.", "Quicksort opera bajo el paradigma Divide y Vencerás en O(n log n)."]}
        ]
    },
    {
        "numero_tema": 11,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Programación Orientada a Objetos I: Clases, Instancias y Métodos en Redes",
        "objetivo": "Modelar componentes de sistemas de potencia mediante clases, atributos tipados y métodos de estado.",
        "concepto_clave_latex": r"\text{Clase}(P_{\text{nom}}, \eta, V) \implies \text{Instancia}: p_{\text{out}} = P_{\text{nom}} \cdot \eta \cdot \cos(\theta)",
        "ejemplo": """CLASE MAGISTRAL: POO PARA SISTEMAS ELÉCTRICOS DE POTENCIA
1. Paradigma Orientado a Objetos:
La programación estructurada falla en proyectos de ingeniería a gran escala por acoplamiento de datos y funciones. La POO encapsula el estado interno (atributos) y el comportamiento (métodos) en una entidad conceptual llamada Clase, de la cual se instancian objetos independientes.
2. Anatomía de una Clase en Python:
El método constructor __init__(self, ...) inicializa los atributos del objeto en memoria Heap. La referencia explícita 'self' vincula la instancia al espacio de nombres de la clase. Los métodos operan sobre el estado sin alterar variables globales.
3. Problema Resuelto 1 (Aplicación Directa):
Defina una clase 'InversorFotovoltaico' con potencia nominal P_nom = 5000 W y eficiencia nominal eta = 0.96. Cree un método 'potencia_ac(P_dc)' que retorne la potencia AC inyectada limitándola a P_nom.
Solución en Python:
class InversorFotovoltaico:
    def __init__(self, p_nom: float, eta: float):
        self.p_nom = p_nom
        self.eta = eta
    def potencia_ac(self, p_dc: float) -> float:
        p_conv = p_dc * self.eta
        return min(p_conv, self.p_nom)
inv = InversorFotovoltaico(5000.0, 0.96)
print(inv.potencia_ac(6000.0)) # Retorna 5000.0 W (clipping del inversor).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Modele un banco de baterías con capacidad C_kWh = 100 y SoC inicial = 0.5. Implemente un método de despacho que reciba delta_P (positivo = carga, negativo = descarga) en un intervalo delta_t = 1 hora con rendimiento de ida y vuelta eta_rt = 0.90, verificando límites de seguridad (SoC entre 0.20 y 0.90).
Solución:
class Bateria:
    def __init__(self, cap_kwh: float, soc_ini: float):
        self.cap = cap_kwh
        self.soc = soc_ini
    def operar(self, p_kw: float, dt_h: float = 1.0) -> float:
        if p_kw >= 0:
            energia = p_kw * dt_h * (0.90 ** 0.5)
            nuevo_soc = self.soc + energia / self.cap
            self.soc = min(nuevo_soc, 0.90)
        else:
            energia = abs(p_kw) * dt_h / (0.90 ** 0.5)
            nuevo_soc = self.soc - energia / self.cap
            self.soc = max(nuevo_soc, 0.20)
        return self.soc
Si p_kw = 50 kW durante 1 h en batería de 100 kWh al 50%: energia = 50 * 0.9487 = 47.43 kWh. SoC final = min(0.5 + 0.4743, 0.90) = 0.90 (alcanzó cota máxima segura).""",
        "bloque_sugerido": "Laboratorio 50 min • Modelado POO de inversores y acumuladores",
        "slides": [
            {"numero": 1, "seccion": "PARADIGMA", "titulo": "Fundamentos de Clases y Objetos", "puntos": ["Encapsulamiento de estado (atributos) y lógica (métodos).", "Constructor __init__ y puntero self de instancia."]},
            {"numero": 2, "seccion": "APLICACIÓN", "titulo": "Modelado de Activos de Energía", "puntos": ["Representación discreta de inversores, baterías y generadores síncronos.", "Validación de cotas operativas dentro del método de despacho."]}
        ]
    },
    {
        "numero_tema": 12,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Programación Orientada a Objetos II: Herencia, Polimorfismo y Dunder Methods",
        "objetivo": "Construir jerarquías de componentes energéticos mediante herencia, despacho polimórfico y sobrecarga de operadores.",
        "concepto_clave_latex": r"\text{Generador} \subset \text{ActivoRed} \quad ; \quad \sum_{i} G_i = \sum_{i} G_i.\text{despachar}(t)",
        "ejemplo": """CLASE MAGISTRAL: HERENCIA Y POLIMORFISMO EN REDES INTELIGENTES
1. Principio de Sustitución de Liskov (LSP) y Herencia:
Una subclase hereda propiedades de una clase base (superclase), permitiendo reutilización y extensibilidad modular. Si S es subtipo de T, los objetos de tipo T pueden reemplazarse por objetos de tipo S sin alterar la corrección del programa.
2. Polimorfismo y Sobrecarga de Operadores (Dunder Methods):
El polimorfismo permite que distintas clases compartan una misma firma de método (__call__, operar, despachar), ejecutando comportamientos específicos en tiempo de ejecución. Los métodos mágicos (__add__, __repr__, __eq__) dotan a los objetos de aritmética natural.
3. Problema Resuelto 1 (Aplicación Directa):
Implemente una clase base 'FuenteRenovable' y dos subclases 'ParqueSolar' y 'ParqueEolico' que sobrescriban el método polimórfico 'generar(recurso)'.
Solución:
class FuenteRenovable:
    def generar(self, recurso: float) -> float:
        raise NotImplementedError("Debe implementarse en subclase")
class ParqueSolar(FuenteRenovable):
    def generar(self, radiacion: float) -> float:
        return radiacion * 0.20 * 1000 # 20% eficiencia, 1000 m^2
class ParqueEolico(FuenteRenovable):
    def generar(self, velocidad_viento: float) -> float:
        return 0.5 * 1.225 * 500 * (velocidad_viento ** 3) * 0.40 / 1000
Ambas clases responden a .generar() adaptando el recurso físico específico.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Sobrecargue el operador '+' (__add__) para que al sumar dos objetos 'VectorPotencia(P, Q)', el resultado sea un nuevo objeto 'VectorPotencia' con potencia compleja suma S = (P1+P2) + j(Q1+Q2) y calcule automáticamente la potencia aparente |S| = sqrt(P^2 + Q^2).
Solución:
import math
class VectorPotencia:
    def __init__(self, p: float, q: float):
        self.p = p
        self.q = q
    def __add__(self, other: 'VectorPotencia') -> 'VectorPotencia':
        return VectorPotencia(self.p + other.p, self.q + other.q)
    @property
    def potencia_aparente(self) -> float:
        return math.hypot(self.p, self.q)
    def __repr__(self) -> str:
        return f"S = {self.p:.1f} kW + j{self.q:.1f} kVAR (|S| = {self.potencia_aparente:.1f} kVA)"
v1 = VectorPotencia(100.0, 40.0)
v2 = VectorPotencia(150.0, -20.0)
v3 = v1 + v2
# v3.p = 250.0 kW, v3.q = 20.0 kVAR, |S| = sqrt(250^2 + 20^2) = 250.8 kVA.""",
        "bloque_sugerido": "Pomodoro 50/10 • Herencia y polimorfismo en Python",
        "slides": [
            {"numero": 1, "seccion": "HERENCIA", "titulo": "Estructuras Jerárquicas", "puntos": ["Clases base abstractas para estandarizar interfaces.", "Extensibilidad sin modificación de código cliente (Open/Closed Principle)."]},
            {"numero": 2, "seccion": "DUNDER", "titulo": "Polimorfismo y Sobrecarga", "puntos": ["Despacho dinámico de métodos de generación.", "Sobrecarga de operadores aritméticos para potencia compleja."]}
        ]
    },
    {
        "numero_tema": 13,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Manejo Robusto de Excepciones, Logging y Aserciones en Sistemas Críticos",
        "objetivo": "Implementar arquitecturas resilientes ante fallos de hardware, desconexión de sensores y datos corruptos.",
        "concepto_clave_latex": r"\Pr(\text{Fallo SCADA}) > 0 \implies \text{try} \; \{x = \text{leer}\} \; \text{except} \; \{x = \text{safe}\} \; \text{finally} \; \{\text{close}\}",
        "ejemplo": """CLASE MAGISTRAL: RESILIENCIA COMPUTACIONAL Y MANEJO DEFENSIVO
1. Taxonomía de Errores en Software Energético:
En sistemas de control de subestaciones y telemetría de microrredes, fallos imprevistos (ZeroDivisionError, TimeoutError, ValueError, KeyError) no deben provocar la caída (crash) del proceso de control principal.
2. Flujo Try-Except-Else-Finally y Excepciones Personalizadas:
El bloque try aísla código susceptible de fallar; except captura errores por jerarquía de tipos; else ejecuta código solo si no hubo excepción; finally garantiza la liberación de recursos físicos (cerrar sockets Modbus, desconectar bases de datos, activar relés de emergencia).
3. Problema Resuelto 1 (Aplicación Directa):
Escriba una función 'calcular_factor_potencia(p_kw, s_kva)' que maneje ZeroDivisionError cuando la potencia aparente sea cero y lance una excepción personalizada 'SobrecargaError' si p_kw > s_kva.
Solución:
class SobrecargaError(Exception):
    pass
def calcular_factor_potencia(p_kw: float, s_kva: float) -> float:
    if p_kw > s_kva:
        raise SobrecargaError(f"Potencia activa {p_kw} kW supera la aparente {s_kva} kVA")
    try:
        fp = p_kw / s_kva
        return round(fp, 4)
    except ZeroDivisionError:
        return 1.0
4. Problema Resuelto 2 (Nivel Examen Parcial):
Diseñe un despachador que intente leer telemetría de 3 medidores con reintentos exponenciales (backoff) y registre en un log con nivel WARNING cada fallo antes de activar una fuente de respaldo en el bloque finally.
Solución:
import logging
import time
logging.basicConfig(level=logging.INFO)
def leer_telemetria_con_backoff(sensor_id: str, max_reintentos: int = 3) -> float:
    reintento = 0
    espera = 1.0
    while reintento < max_reintentos:
        try:
            val = lectura_hardware(sensor_id)
            return val
        except IOError as e:
            reintento += 1
            logging.warning(f"Fallo sensor {sensor_id}, reintento {reintento}/{max_reintentos} en {espera}s. Error: {e}")
            time.sleep(espera)
            espera *= 2.0
    logging.critical(f"Sensor {sensor_id} inalcanzable. Conmutando a modo seguro.")
    return 0.0""",
        "bloque_sugerido": "Laboratorio 50 min • Manejo de excepciones y logging en SCADA",
        "slides": [
            {"numero": 1, "seccion": "DEFENSIVA", "titulo": "Arquitectura Antifallos", "puntos": ["Bloques try-except-else-finally para salvaguardar el bucle de control.", "Excepciones de dominio personalizadas (Sobrecarga, TensiónInestable)."]},
            {"numero": 2, "seccion": "LOGGING", "titulo": "Trazabilidad y Backoff", "puntos": ["Niveles jerárquicos: DEBUG, INFO, WARNING, ERROR, CRITICAL.", "Reintentos con espera exponencial ante fluctuaciones de red."]}
        ]
    },
    {
        "numero_tema": 14,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Estructuras de Datos Avanzadas: Colas de Prioridad, Heaps y Tablas Hash",
        "objetivo": "Optimizar el despacho económico y la atención de alarmas mediante montículos binarios y diccionarios hash.",
        "concepto_clave_latex": r"\text{Costo Marginal} \; \lambda_i \implies \text{HeapMin}(\lambda_1, \dots, \lambda_m) \; \text{en} \; \mathcal{O}(\log m)",
        "ejemplo": """CLASE MAGISTRAL: ESTRUCTURAS DE DATOS PARA DESPACHO ENERGÉTICO
1. Tablas Hash y Resolución de Colisiones:
Las tablas hash (implementación interna de los dict y set en Python) mapean claves arbitrarias a posiciones de memoria en tiempo O(1) promedio mediante una función de hash criptográfica o distributiva, esencial para indexar millones de contadores inteligentes.
2. Montículos Binarios (Heaps) y Colas de Prioridad:
En un mercado eléctrico spot, las centrales generadoras deben despacharse en orden ascendente de costo marginal de generación (Merit Order). Un Heap Mínimo mantiene el elemento de menor costo en la raíz en O(1), permitiendo inserciones y extracciones ordenadas en O(log m).
3. Problema Resuelto 1 (Aplicación Directa):
Dado un conjunto de 5 ofertas horarias con costos marginales [85, 42, 120, 25, 60] USD/MWh, construya un min-heap usando el módulo 'heapq' y extraiga las 3 plantas más baratas.
Solución:
import heapq
ofertas = [(85, "Gas Ciclo Combinado"), (42, "Hidroeléctrica"), (120, "Diésel Peaker"), (25, "Solar FV"), (60, "Eólica")]
heapq.heapify(ofertas)
despacho = [heapq.heappop(ofertas) for _ in range(3)]
# 1. (25, 'Solar FV')
# 2. (42, 'Hidroeléctrica')
# 3. (60, 'Eólica')
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre que mantener un ordenamiento continuo mediante inserción sobre lista tiene costo O(n^2), mientras que usar un Heap para despachar K generadores entre N disponibles toma O(N + K log N).
Solución:
Para una lista: insertar un elemento en orden requiere O(n) desplazamientos en memoria contigua. Insertar N elementos: sum_{i=1}^N i = N(N+1)/2 = O(N^2).
Para un Heap: 'heapify' organiza los N elementos iniciales en O(N) operaciones utilizando el algoritmo de Floyd (sift-down). Cada una de las K extracciones toma O(log N).
Complejidad total: O(N) + K * O(log N) = O(N + K log N).
Para N = 10,000 generadores y K = 100:
Lista: ~10^8 operaciones.
Heap: 10,000 + 100 * 13.29 = 11,329 operaciones (aceleración de 8,826x).""",
        "bloque_sugerido": "Práctica 50 min • Colas de prioridad en despacho de carga",
        "slides": [
            {"numero": 1, "seccion": "ESTRUCTURAS", "titulo": "Tablas Hash vs Heaps", "puntos": ["Hash maps: Búsqueda y actualización O(1) para telemetría SCADA.", "Min-Heap: Raíz siempre contiene el generador de menor costo marginal."]},
            {"numero": 2, "seccion": "DESPACHO", "titulo": "Merit-Order Eficiente", "puntos": ["Heapify en tiempo lineal O(N) frente a ordenamientos O(N^2).", "Extracción de K plantas óptimas en O(K log N)."]}
        ]
    },
    {
        "numero_tema": 15,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Cómputo Numérico de Alto Rendimiento con NumPy: Vectorización y Matrices",
        "objetivo": "Acelerar simulaciones energéticas masivas mediante operaciones vectorizadas y broadcasting en memoria contigua C.",
        "concepto_clave_latex": r"\mathbf{V}_{\text{bus}} = \mathbf{Y}_{\text{bus}}^{-1} \mathbf{I}_{\text{inj}} \quad ; \quad \mathbf{P}_{\text{loss}} = \mathbf{I}^T \mathbf{R} \mathbf{I}",
        "ejemplo": """CLASE MAGISTRAL: VECTORIZACIÓN Y CÓMPUTO CIENTÍFICO CON NUMPY
1. Limitaciones del GIL de Python y Ventajas de NumPy:
Los bucles for en Python puro son lentos debido al tipado dinámico y al Global Interpreter Lock (GIL). NumPy soluciona esto asignando búferes contiguos de memoria en C/Fortran (ndarrays tipados de forma homogénea) y ejecutando instrucciones SIMD (Single Instruction, Multiple Data).
2. Reglas de Difusión (Broadcasting) y Álgebra Lineal:
El broadcasting permite operar arreglos de distintas dimensiones sin copiar datos en RAM si las dimensiones son compatibles (iguales o una de ellas es 1).
3. Problema Resuelto 1 (Aplicación Directa):
Calcule la potencia disipada en una red trifásica de 3 conductores de resistencia R = 0.05 Ohm con corrientes instantáneas i = [120.5, 118.2, 122.1] A utilizando vectorización de NumPy.
Solución:
import numpy as np
i_vec = np.array([120.5, 118.2, 122.1], dtype=np.float64)
r_val = 0.05
p_disipada = r_val * np.square(i_vec)
p_total = np.sum(p_disipada)
# p_disipada = [726.01, 698.56, 745.42] W ==> p_total = 2170.0 W = 2.17 kW.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Dada una matriz de irradiancia de 365 días por 24 horas (G de forma 365x24 en W/m^2) y un vector de eficiencia horaria por temperatura eta_t de longitud 24, use broadcasting para calcular la energía anual total generada por un arreglo de área A = 500 m^2 en MWh.
Solución:
G = np.random.uniform(0, 1000, size=(365, 24))
eta = np.linspace(0.18, 0.15, 24)
P_horaria = G * eta * 500.0
Energia_MWh = np.sum(P_horaria) * 1.0 / 1e6
print(f"Energía total calculada vectorialmente: {Energia_MWh:.2f} MWh")""",
        "bloque_sugerido": "Laboratorio 50 min • Vectorización y broadcasting con NumPy",
        "slides": [
            {"numero": 1, "seccion": "NUMPY", "titulo": "Arquitectura de Arreglos ND", "puntos": ["Memoria contigua C y tipado homogéneo para operaciones vectorizadas SIMD.", "Aceleración de 50x a 200x frente a bucles for estándar."]},
            {"numero": 2, "seccion": "BROADCASTING", "titulo": "Álgebra Vectorial y Redes", "puntos": ["Cálculo instantáneo de pérdidas Joule P = I^2 R.", "Matrices de admitancia nodal y producto matricial np.dot / @"]}
        ]
    },
    {
        "numero_tema": 16,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Análisis y Limpieza de Series Temporales con Pandas",
        "objetivo": "Procesar curvas de carga horarias, imputar telemetría faltante y agregar métricas con resample y groupby.",
        "concepto_clave_latex": r"\bar{E}_{\text{mes}} = \int_{t_0}^{t_f} P(t)\,dt \approx \sum_{k \in \text{Mes}} P_k \Delta t \quad ; \quad \text{Resample}(\text{'1D'})",
        "ejemplo": """CLASE MAGISTRAL: PROCESAMIENTO DE SERIES TEMPORALES EN ENERGÍA
1. Objetos Series y DataFrame de Pandas:
Pandas indexa registros temporales con DatetimeIndex de precisión de nanosegundos, permitiendo operaciones de alineación automática, slice temporal y tratamiento de datos faltantes (NaN).
2. Técnicas de Imputación y Remuestreo (Resampling):
La telemetría eléctrica sufre caídas de enlace. La interpolación temporal (linear, time, cubic) y el método 'ffill' (forward fill) preservan la física del sistema. Las funciones resample('1H', '1D', '1M') permiten cambiar la frecuencia muestral integrando o promediando.
3. Problema Resuelto 1 (Aplicación Directa):
Dado un DataFrame de potencia 'df' con mediciones cada 15 minutos en kW, obtenga el consumo diario en kWh y la demanda máxima horaria del mes.
Solución:
import pandas as pd
import numpy as np
fechas = pd.date_range(start='2026-01-01', periods=96*31, freq='15min')
df = pd.DataFrame({'potencia_kw': np.random.uniform(20, 100, size=len(fechas))}, index=fechas)
energia_diaria_kwh = df['potencia_kw'].resample('1D').apply(lambda x: x.sum() * 0.25)
demanda_horaria_max = df['potencia_kw'].resample('1h').mean().max()
print(f"Pico horario mensual: {demanda_horaria_max:.2f} kW")
4. Problema Resuelto 2 (Nivel Examen Parcial):
Un medidor inteligente perdió telemetría durante 3 horas seguidas (12 muestras consecutivas NaN de 15 min). Compare el error cuadrático medio al imputar por 'bfill' frente a 'linear interpolation' conociendo que antes del fallo la carga era 40 kW y después 100 kW en una rampa constante.
Solución:
En rampa lineal verdadera: los valores son 45, 50, ..., 95 kW.
Imputación bfill rellena los 12 puntos con 100 kW.
Error en cada punto k: (100 - (40 + 5*k))^2 = (60 - 5k)^2.
MSE(bfill) = sum_{k=1}^{11} (60 - 5k)^2 / 11 = 962.5 kW^2.
Imputación linear interpola exactamente los puntos de la rampa recta: y_k = 40 + 5k.
Error en cada punto: 0. MSE(linear) = 0.0 kW^2.
Conclusión: En rampas de carga eléctrica la interpolación temporal lineal es analíticamente superior a rellenos constantes.""",
        "bloque_sugerido": "Pomodoro 50/10 • Curvas de carga horaria y resampling en Pandas",
        "slides": [
            {"numero": 1, "seccion": "PANDAS", "titulo": "Series de Tiempo Energéticas", "puntos": ["DatetimeIndex para indexación horaria de 8760 horas del año.", "Detección y tratamiento de valores nulos con fillna e interpolate."]},
            {"numero": 2, "seccion": "AGREGACIÓN", "titulo": "Resampling y GroupBy", "puntos": ["Conversión de potencia 15-min a energía diaria y mensual.", "Agrupamiento por perfiles estacionales y tipos de día (hábil/festivo)."]}
        ]
    },
    {
        "numero_tema": 17,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Visualización Científica con Matplotlib y Seaborn",
        "objetivo": "Construir diagramas de ingeniería rigurosos: curvas de duración de carga, mapas de calor y distribución de Weibull.",
        "concepto_clave_latex": r"f(v; k, c) = \frac{k}{c}\left(\frac{v}{c}\right)^{k-1} e^{-(v/c)^k} \quad ; \quad \text{LDC}(t) = \text{sort}_{\downarrow}(P(t))",
        "ejemplo": """CLASE MAGISTRAL: VISUALIZACIÓN DE INGENIERÍA Y COMUNICACIÓN TÉCNICA
1. Gramática de Gráficos y Arquitectura de Matplotlib:
Una figura científica consta de objetos explícitos Figure y Axes (método orientado a objetos 'fig, ax = plt.subplots()'). No se deben usar llamadas de estado implícitas de MATLAB en entornos profesionales.
2. Curvas de Duración de Carga (Load Duration Curve - LDC):
La LDC ordena la demanda horaria anual de mayor a menor (de 0 a 8760 horas), mostrando gráficamente la base de generación firme, la media y las puntas críticas que justifican baterías o peakers.
3. Problema Resuelto 1 (Aplicación Directa):
Genere el código en Python para graficar una Curva de Duración de Carga a partir de un arreglo anual de 8760 horas y calcule el área bajo la curva (energía total anual).
Solución:
import numpy as np
import matplotlib.pyplot as plt
demanda_anual = np.random.normal(500, 80, 8760)
ldc = np.sort(demanda_anual)[::-1]
horas = np.arange(1, 8761)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(horas, ldc, color='blue', linewidth=1.5, label='Demanda Ordenada')
ax.set_title("Curva de Duración de Carga (LDC) Anual")
ax.set_xlabel("Horas del Año (h)")
ax.set_ylabel("Demanda (kW)")
ax.grid(True, linestyle='--', alpha=0.6)
energia_anual_mwh = np.trapz(ldc, horas) / 1000.0
print(f"Energía anual bajo LDC: {energia_anual_mwh:.2f} MWh")
4. Problema Resuelto 2 (Nivel Examen Parcial):
Grafique la función de densidad de probabilidad de Weibull para un recurso eólico con parámetro de forma k = 2.1 y escala c = 8.5 m/s, superponiendo la velocidad de viento nominal v_n = 12 m/s y de corte v_out = 25 m/s.
Solución:
v = np.linspace(0, 30, 500)
k, c = 2.1, 8.5
pdf = (k / c) * (v / c)**(k - 1) * np.exp(-(v / c)**k)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(v, pdf, color='crimson', label=f'Weibull (k={k}, c={c})')
ax.axvline(12, color='green', linestyle=':', label='v_nominal (12 m/s)')
ax.axvline(25, color='black', linestyle='--', label='v_corte (25 m/s)')
ax.fill_between(v[(v>=3) & (v<=25)], pdf[(v>=3) & (v<=25)], color='skyblue', alpha=0.4, label='Zona de Operación')
ax.set_xlabel("Velocidad de Viento (m/s)")
ax.set_ylabel("Densidad de Probabilidad")
ax.legend()""",
        "bloque_sugerido": "Laboratorio 50 min • Visualización científica con Matplotlib",
        "slides": [
            {"numero": 1, "seccion": "VISUALIZACIÓN", "titulo": "Arquitectura Figure y Axes", "puntos": ["Control explícito de lienzos, escalas logarítmicas y formato vectorial.", "Mapas de calor para radiación solar mensual vs horaria."]},
            {"numero": 2, "seccion": "CURVAS TÉCNICAS", "titulo": "Curvas de Duración y Weibull", "puntos": ["LDC para dimensionamiento de potencia base, intermedia y pico.", "Ajuste de distribución de viento para producción de aerogeneradores."]}
        ]
    },
    {
        "numero_tema": 18,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Análisis Exploratorio de Datos (EDA) y Detección de Anomalías SCADA",
        "objetivo": "Filtrar espurias y detectar fraudes o fallas de transformadores mediante Z-Score e Interquartile Range (IQR).",
        "concepto_clave_latex": r"z_i = \frac{x_i - \mu}{\sigma} \quad ; \quad \text{Outlier} \iff x_i < Q_1 - 1.5\,\text{IQR} \;\lor\; x_i > Q_3 + 1.5\,\text{IQR}",
        "ejemplo": """CLASE MAGISTRAL: DETECCIÓN DE ANOMALÍAS EN REDES ELÉCTRICAS
1. Naturaleza de los Outliers en Sensores de Potencia:
Los transitorios electromagnéticos de maniobra, caídas de rayos y fallas de comunicación introducen picos espurios irreales. Por otro lado, derivas persistentes hacia abajo indican posible robo de energía o fallos de TC/TP (transformadores de medida).
2. Métodos Estadísticos de Detección:
- Z-Score: Mide cuántas desviaciones estándar dista un punto de la media. Válido para distribuciones gaussianas (|z| > 3 se considera anomalía con p < 0.0027).
- Rango Intercuartílico (IQR = Q3 - Q1): No paramétrico, robusto ante asimetrías severas. Puntos fuera de [Q1 - 1.5*IQR, Q3 + 1.5*IQR] son catalogados como atípicos.
3. Problema Resuelto 1 (Aplicación Directa):
Un alimentador reporta las siguientes potencias diarias (kW): [102, 98, 105, 101, 100, 350, 99, 103]. Detecte analíticamente si el valor 350 kW es un outlier usando Z-score e IQR.
Solución:
Valores: n = 8.
media mu = 132.25 kW, sigma = 82.30 kW.
z(350) = (350 - 132.25) / 82.30 = 2.645.
Por IQR: Q1 = 99.5, Q3 = 103.5 ==> IQR = 4 kW. Cota superior: 103.5 + 1.5*(4) = 109.5 kW.
Como 350 > 109.5, por IQR es indiscutiblemente un outlier extremo.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Implemente una función en Python 'limpiar_scada(df, columna)' que reemplace los valores atípicos detectados por IQR por el valor mediano móvil de una ventana de 5 periodos.
Solución:
def limpiar_scada(df, columna):
    serie = df[columna]
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    cota_inf = q1 - 1.5 * iqr
    cota_sup = q3 + 1.5 * iqr
    es_outlier = (serie < cota_inf) | (serie > cota_sup)
    mediana_movil = serie.rolling(window=5, center=True, min_periods=1).median()
    df[columna + '_limpio'] = np.where(es_outlier, mediana_movil, serie)
    return df""",
        "bloque_sugerido": "Práctica 50 min • Limpieza y detección de anomalías SCADA",
        "slides": [
            {"numero": 1, "seccion": "ESTADÍSTICA", "titulo": "Detección de Valores Atípicos", "puntos": ["Z-Score paramétrico para ruido gaussiano.", "IQR de Tukey robusto frente a distribuciones asimétricas de carga."]},
            {"numero": 2, "seccion": "FILTRADO", "titulo": "Limpieza en Tiempo Real", "puntos": ["Reemplazo de espurias mediante ventanas de mediana móvil.", "Preservación de transitorios físicos legítimos de conmutación."]}
        ]
    },
    {
        "numero_tema": 19,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Métodos de Integración Numérica: Reglas del Trapecio y Simpson en Energía",
        "objetivo": "Calcular integrales de energía acumulada y calor a partir de datos discretos mediante fórmulas de Newton-Cotes.",
        "concepto_clave_latex": r"E = \int_a^b P(t)\,dt \approx \frac{h}{2}\sum_{k=1}^n (P_{k-1} + P_k) \quad ; \quad E_{\text{simp}} = \frac{h}{3}\left[P_0 + 4\sum P_{\text{impar}} + 2\sum P_{\text{par}} + P_n\right]",
        "ejemplo": """CLASE MAGISTRAL: INTEGRACIÓN NUMÉRICA PARA BALANCES ENERGÉTICOS
1. Fórmulas de Cuadratura de Newton-Cotes:
En sistemas físicos reales la función de potencia P(t) no se conoce analíticamente, sino a través de un vector discreto de muestras en instantes equiespaciados h = delta_t. La integral definida representa la energía neta transferida.
2. Regla del Trapecio y Regla de Simpson 1/3:
- Trapecio: Aproxima P(t) por segmentos lineales. Error global O(h^2).
- Simpson 1/3: Aproxima P(t) por parábolas de segundo orden. Error global O(h^4).
3. Problema Resuelto 1 (Aplicación Directa):
La potencia generada por una turbina hidráulica medida cada h = 2 horas es: P = [10, 18, 25, 22, 12] MW. Calcule la energía total producida durante las 8 horas mediante la Regla de Simpson 1/3.
Solución: n = 4 intervalos pares (5 puntos), h = 2 h.
Fórmula: E = (h / 3) * [P_0 + 4*(P_1 + P_3) + 2*P_2 + P_4]
E = (2 / 3) * [10 + 4*(18 + 22) + 2*(25) + 12]
E = (2 / 3) * [10 + 160 + 50 + 12] = (2 / 3) * [232] = 154.67 MWh.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre analíticamente que la Regla de Simpson 1/3 integra de forma exacta cualquier polinomio cúbico f(x) = a*x^3 + b*x^2 + c*x + d a pesar de estar basada en interpolación cuadrática.
Solución:
El término de error de la Regla de Simpson compuesta es:
Error = - (b - a) / 180 * h^4 * f^{(4)}(xi) para algún xi in [a, b].
Calculamos la cuarta derivada de un polinomio de tercer grado:
f'(x) = 3ax^2 + 2bx + c
f''(x) = 6ax + 2b
f'''(x) = 6a
f^{(4)}(x) = 0.
Al sustituir f^{(4)}(xi) = 0: Error = 0.
Por lo tanto, la Regla de Simpson integra con error exactamente nulo polinomios de grado <= 3. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Cuadratura de Newton-Cotes y balances de energía",
        "slides": [
            {"numero": 1, "seccion": "INTEGRACIÓN", "titulo": "Fórmulas de Newton-Cotes", "puntos": ["Regla del Trapecio O(h^2) para integración rápida de sensores.", "Regla de Simpson 1/3 O(h^4) con convergencia de orden superior."]},
            {"numero": 2, "seccion": "PRECISIÓN", "titulo": "Exactitud Polinomial", "puntos": ["Simpson es exacta para polinomios hasta grado 3 por simetría impar del error.", "Cálculo riguroso de MWh a partir de telemetría discontinua."]}
        ]
    },
    {
        "numero_tema": 20,
        "corte": 2,
        "modalidad": "tecnica",
        "titulo": "Solución Numérica de Ecuaciones Diferenciales Ordinarias: Euler y Runge-Kutta",
        "objetivo": "Simular la dinámica transitoria de carga de condensadores y baterías mediante integración numérica temporal de EDOs.",
        "concepto_clave_latex": r"\frac{dy}{dt} = f(t, y) \quad ; \quad y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)",
        "ejemplo": """CLASE MAGISTRAL: DINÁMICA TRANSITORIA Y MÉTODOS DE INTEGRACIÓN TEMPORAL
1. Planteamiento de Problemas de Valor Inicial (PVI):
Los sistemas físicos en ingeniería energética se rigen por ecuaciones diferenciales ordinarias dy/dt = f(t, y) con condición inicial y(t_0) = y_0.
2. Comparación entre Método de Euler y Runge-Kutta de 4to Orden (RK4):
- Euler hacia adelante: y_{n+1} = y_n + h * f(t_n, y_n). Primer orden O(h).
- RK4: Evalúa 4 pendientes intermedias k1, k2, k3, k4 ponderándolas con la regla de Simpson. Error global O(h^4).
3. Problema Resuelto 1 (Aplicación Directa):
La tensión en un condensador de C = 100 uF cargado a través de R = 10 kOhm con fuente V_s = 100 V cumple dv/dt = (100 - v) / (R*C). Con v(0) = 0 V y h = 0.2 s (tau = R*C = 1.0 s), calcule v(0.2) usando un paso de Euler hacia adelante.
Solución:
tau = R * C = 10,000 * 100e-6 = 1.0 s.
f(t, v) = (100 - v) / 1.0 = 100 - v.
En t = 0: f(0, 0) = 100 V/s.
Euler: v(0.2) = v(0) + h * f(0, 0) = 0 + 0.2 * 100 = 20.0 V.
(Analítico exacto: 18.13 V. Error = 1.87 V).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Calcule el mismo punto v(0.2) del circuito RC usando el método Runge-Kutta de 4to Orden (RK4) y demuestre la drástica reducción del error.
Solución: f(v) = 100 - v, h = 0.2, v_0 = 0.
k1 = f(0) = 100.0.
k2 = f(0 + 0.1 * 100) = f(10) = 90.0.
k3 = f(0 + 0.1 * 90) = f(9) = 91.0.
k4 = f(0 + 0.2 * 91) = f(18.2) = 81.8.
v_1 = 0 + (0.2 / 6) * [100.0 + 2*(90.0) + 2*(91.0) + 81.8] = 18.1267 V.
Error absoluto RK4 = |18.1267 - 18.1269| = 0.0002 V. Redujo el error de Euler en ~10,000 veces.""",
        "bloque_sugerido": "Laboratorio 50 min • Simulación de transitorios con Runge-Kutta",
        "slides": [
            {"numero": 1, "seccion": "EDOS", "titulo": "Integración Numérica Temporal", "puntos": ["Discretización temporal de leyes de conservación y transitorios RC/RL.", "Criterio de estabilidad numérica de Euler frente a sistemas rígidos."]},
            {"numero": 2, "seccion": "RUNGE-KUTTA", "titulo": "Algoritmo RK4", "puntos": ["Evaluación en cuatro pendientes intermedias con precisión O(h^4).", "Estándar de la industria para simulación electromagnética."]}
        ]
    },
    {
        "numero_tema": 21,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Preprocesamiento y Escalado de Características en Machine Learning",
        "objetivo": "Acondicionar variables heterogéneas (tensión, temperatura, irradiancia) mediante normalización y codificación categórica.",
        "concepto_clave_latex": r"x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \quad ; \quad z = \frac{x - \mu}{\sigma}",
        "ejemplo": """CLASE MAGISTRAL: FEATURE ENGINEERING Y PREPROCESAMIENTO DE DATOS
1. Sensibilidad de Algoritmos al Rango de Escalas:
Algoritmos basados en distancias (KNN, K-Means, SVM) o en optimización por gradiente (Regresión Lineal, Redes Neuronales) son fuertemente sesgados si una variable tiene orden de magnitud 10^5 (potencia en Watts) y otra orden 10^-1 (factor de potencia).
2. Técnicas de Estandarización y Normalización:
- Min-Max Scaling: Transforma el rango a [0, 1]. Preserva ceros pero es sensible a outliers.
- Standard Scaler (Z-score): Centra los datos en media 0 y varianza unitaria.
- One-Hot Encoding: Convierte variables categóricas en vectores binarios ortogonales.
3. Problema Resuelto 1 (Aplicación Directa):
Un sensor mide irradiancia solar G con valores observados G_min = 50 W/m^2 y G_max = 1050 W/m^2. Calcule el valor normalizado Min-Max para una medición de 650 W/m^2.
Solución:
x_norm = (650 - 50) / (1050 - 50) = 600 / 1000 = 0.6000.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Dado un conjunto de entrenamiento con media mu_train = 400 V y sigma_train = 15 V, y una muestra de prueba con V = 445 V, demuestre por qué es un error metodológico grave (Data Leakage) recalcular mu y sigma con el conjunto de prueba y calcule el z-score correcto.
Solución:
En ML riguroso, los parámetros de preprocesamiento (mu, sigma, min, max) deben derivarse exclusivamente del set de entrenamiento para simular condiciones reales donde los datos futuros son desconocidos. Recalcularlos en test introduce fuga de información (data leakage).
El escalado correcto usa los parámetros de entrenamiento:
z_test = (V - mu_train) / sigma_train = (445 - 400) / 15 = 45 / 15 = 3.00.
Este z-score de 3.0 indica inmediatamente al modelo que la muestra está en el percentil extremo de sobretensión.""",
        "bloque_sugerido": "Laboratorio 50 min • Preprocesamiento con Scikit-Learn",
        "slides": [
            {"numero": 1, "seccion": "ESCALADO", "titulo": "Min-Max vs StandardScaler", "puntos": ["Homogeneización de unidades físicas dispares para algoritmos basados en gradiente.", "Prevención estricta de Data Leakage entre entrenamiento y test."]},
            {"numero": 2, "seccion": "CATEGORIZACIÓN", "titulo": "Codificación One-Hot", "puntos": ["Transformación de variables nominales a vectores booleanos independientes.", "Evita relaciones de orden espurias inducidas por Label Encoding."]}
        ]
    },
    {
        "numero_tema": 22,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Regresión Lineal Múltiple, Descenso de Gradiente y Regularización",
        "objetivo": "Predecir la demanda eléctrica mediante optimización de la función de coste MSE con regularización Ridge (L2).",
        "concepto_clave_latex": r"J(\mathbf{w}) = \frac{1}{2N}\|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2 \quad ; \quad \mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla J(\mathbf{w})",
        "ejemplo": """CLASE MAGISTRAL: OPTIMIZACIÓN CONVEXA Y REGRESIÓN REGULARIZADA
1. Ecuación Normal frente a Descenso de Gradiente:
La solución exacta de mínimos cuadrados w = (X^T X)^{-1} X^T y requiere invertir una matriz de d x d, inviable para grandes dimensiones O(d^3). El Descenso de Gradiente (GD) actualiza iterativamente los pesos en la dirección opuesta al gradiente con tasa de aprendizaje alpha.
2. Regularización L2 (Ridge) y Sobreajuste (Overfitting):
Cuando las características son colineales, la matriz X^T X se vuelve casi singular. La regularización Ridge añade una penalización proporcional a la norma L2 de los pesos, restringiendo su magnitud.
3. Problema Resuelto 1 (Aplicación Directa):
Para un modelo simple y_hat = w * x con función de pérdida J(w) = (w*x - y)^2 / 2, donde x = 2, y = 10 y valor inicial w_0 = 1, calcule w_1 tras una iteración de descenso de gradiente con alpha = 0.05.
Solución:
Error residual: e = (1 * 2 - 10) = -8.
Gradiente: dJ/dw = (-8) * 2 = -16.
Actualización: w_1 = 1 - 0.05 * (-16) = 1 + 0.8 = 1.8.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre que la solución analítica para el vector de pesos de la regresión Ridge con penalización lambda > 0 siempre tiene inversa única y está dada por w = (X^T X + lambda*I)^{-1} X^T y.
Solución:
J(w) = (1/2) * (Xw - y)^T (Xw - y) + (lambda / 2) * w^T w.
Gradiente respecto a w: nabla_w J(w) = X^T X w - X^T y + lambda * w = 0.
Factorizando: (X^T X + lambda * I) w = X^T y.
Como lambda > 0 y X^T X es semidefinida positiva, (X^T X + lambda * I) es estrictamente definida positiva, garantizando autovalores > 0 e invertibilidad única:
w = (X^T X + lambda * I)^{-1} X^T y. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Gradiente descendente y regularización L2",
        "slides": [
            {"numero": 1, "seccion": "OPTIMIZACIÓN", "titulo": "Descenso de Gradiente", "puntos": ["Convergencia iterativa minimizando la función cuadrática de pérdida MSE.", "Selección de hiperparámetro de tasa de aprendizaje alpha."]},
            {"numero": 2, "seccion": "REGULARIZACIÓN", "titulo": "Regresión Ridge (L2)", "puntos": ["Garantía de invertibilidad matricial sumando lambda*I.", "Control estricto de varianza y mitigación de multicolinealidad."]}
        ]
    },
    {
        "numero_tema": 23,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Clasificación Binaria con Regresión Logística y Función Sigmoide",
        "objetivo": "Predecir la probabilidad de disparo de protecciones mediante clasificación probabilística y entropía cruzada.",
        "concepto_clave_latex": r"\sigma(z) = \frac{1}{1 + e^{-z}} \quad ; \quad \mathcal{L}(\mathbf{w}) = -\frac{1}{N}\sum_{i=1}^N \left[y_i \ln(\hat{y}_i) + (1 - y_i)\ln(1 - \hat{y}_i)\right]",
        "ejemplo": """CLASE MAGISTRAL: CLASIFICACIÓN PROBABILÍSTICA Y MÁXIMA VEROSIMILITUD
1. Función Sigmoide y Mapeo de Odds:
En problemas de clasificación binaria (1 = disparo de relé, 0 = operación normal), la función logística sigmoide mapea cualquier combinación lineal z = w^T x a una probabilidad estricta en el intervalo (0, 1).
2. Pérdida de Entropía Cruzada Binaria:
Derivada aplicando el principio de máxima verosimilitud a una variable Bernoulli. Penaliza con severidad logarítmica predicciones que confían plenamente en la clase errónea.
3. Problema Resuelto 1 (Aplicación Directa):
Para un relé de sobrecorriente, la combinación lineal es z = 2.5 * I_pu - 3.0. Si la corriente per-unit es I_pu = 1.6 pu, determine la probabilidad estimada de disparo P(y=1).
Solución:
z = 2.5 * 1.6 - 3.0 = 4.0 - 3.0 = 1.0.
sigma(z) = 1 / (1 + exp(-1.0)) = 1 / (1 + 0.3679) = 1 / 1.3679 = 0.7311 (73.11%). Con umbral 0.5, el relé dispara.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre que la derivada de la función sigmoide sigma(z) respecto a z es exactamente sigma(z) * (1 - sigma(z)).
Solución:
sigma(z) = (1 + e^{-z})^{-1}.
d/dz [sigma(z)] = - (1 + e^{-z})^{-2} * (-e^{-z}) = e^{-z} / (1 + e^{-z})^2.
Factorizando: [1 / (1 + e^{-z})] * [e^{-z} / (1 + e^{-z})].
Como 1 - sigma(z) = e^{-z} / (1 + e^{-z}):
d/dz [sigma(z)] = sigma(z) * (1 - sigma(z)). Q.E.D.""",
        "bloque_sugerido": "Laboratorio 50 min • Clasificación binaria y función sigmoide",
        "slides": [
            {"numero": 1, "seccion": "LOGÍSTICA", "titulo": "Función Sigmoide", "puntos": ["Mapeo suave y diferenciable de la recta real a probabilidades [0, 1].", "Derivada compacta sigma(z) * (1 - sigma(z))."]},
            {"numero": 2, "seccion": "VEROSIMILITUD", "titulo": "Pérdida de Entropía Cruzada", "puntos": ["Optimización convexa que penaliza el error de confianza.", "Decisión mediante umbral de probabilidad sintonizable."]}
        ]
    },
    {
        "numero_tema": 24,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Métricas de Evaluación: Matriz de Confusión, ROC-AUC y K-Fold",
        "objetivo": "Evaluar clasificadores con clases desbalanceadas mediante Precision, Recall, F1-Score y validación cruzada.",
        "concepto_clave_latex": r"\text{Recall} = \frac{TP}{TP + FN} \quad ; \quad \text{Precision} = \frac{TP}{TP + FP} \quad ; \quad F_1 = 2\frac{P \cdot R}{P + R}",
        "ejemplo": """CLASE MAGISTRAL: EVALUACIÓN RIGUROSA DE MODELOS CON DATOS DESBALANCEADOS
1. La Paradoja de la Exactitud (Accuracy Paradox):
En detección de fallas eléctricas de red, el 99.9% de los registros corresponden a operación normal y sólo el 0.1% a eventos de falla. Un clasificador trivial que siempre prediga 'normal' tiene 99.9% de exactitud, pero es totalmente inútil.
2. Matriz de Confusión, Recall y F1-Score:
- Recall: Capacidad de detectar fallas reales (minimiza Falsos Negativos).
- Precision: Certeza cuando emite una alarma (minimiza Falsas Alarmas).
- F1-Score: Media armónica entre Precision y Recall.
3. Problema Resuelto 1 (Aplicación Directa):
Un clasificador de fallas en cables subterráneos arroja: TP = 45, FN = 5, FP = 15, TN = 935. Calcule Accuracy, Precision, Recall y F1-Score.
Solución:
Accuracy = (45 + 935) / 1000 = 98.0%.
Precision = 45 / (45 + 15) = 0.7500 (75.0%).
Recall = 45 / (45 + 5) = 0.9000 (90.0%).
F1-Score = 2 * (0.75 * 0.90) / (0.75 + 0.90) = 1.35 / 1.65 = 0.8182 (81.82%).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Explique el procedimiento de Validación Cruzada Estratificada de K-Folds (Stratified K-Fold con K=5) y demuestre por qué previene el sobreajuste frente a un simple split 80/20.
Solución:
En K-Fold estratificado, el dataset total D se particiona en K subconjuntos disjuntos preservando exactamente la proporción de clases de falla en cada partición. Cada muestra se usa exactamente una vez para validación y K-1 veces para entrenamiento. Esto reduce la varianza de la estimación del error por un factor proporcional a 1/K y elimina el sesgo de particiones afortunadas presentes en un único split 80/20.""",
        "bloque_sugerido": "Pomodoro 50/10 • Matriz de confusión y curvas ROC-AUC",
        "slides": [
            {"numero": 1, "seccion": "MÉTRICAS", "titulo": "Matriz de Confusión y F1", "puntos": ["Insuficiencia de Accuracy ante eventos raros de falla eléctrica.", "Foco en Recall para minimizar Falsos Negativos catastróficos."]},
            {"numero": 2, "seccion": "VALIDACIÓN", "titulo": "Stratified K-Fold", "puntos": ["Partición balanceada preservando porcentajes de desbalance.", "Estimación insesgada de generalización del modelo en campo."]}
        ]
    },
    {
        "numero_tema": 25,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Árboles de Decisión y Random Forests para Diagnóstico de Fallas",
        "objetivo": "Construir modelos interpretables de ensamble basados en impureza de Gini y bagging para clasificar transitorios de potencia.",
        "concepto_clave_latex": r"I_G(p) = 1 - \sum_{k=1}^C p_k^2 \quad ; \quad \hat{y}_{\text{RF}} = \text{mode}\{\hat{y}_1, \dots, \hat{y}_B\}",
        "ejemplo": """CLASE MAGISTRAL: ALGORITMOS DE ENSAMBLE Y DIAGNÓSTICO EN TIEMPO REAL
1. Criterios de División en Árboles (CART):
Un árbol de decisión particiona recursivamente el espacio de características seleccionando la división que maximiza la reducción de la impureza de Gini I_G.
2. Bosques Aleatorios (Random Forests) y Bagging:
Los árboles individuales sufren de alta varianza. Random Forest entrena B árboles independientes sobre muestras bootstrap considerando un subconjunto aleatorio de sqrt(d) características en cada nodo, descorrelacionando los árboles y reduciendo la varianza del ensamble.
3. Problema Resuelto 1 (Aplicación Directa):
En un nodo con 40 muestras de cortocircuito (clase 1) y 10 muestras de sobretensión (clase 2), calcule la impureza de Gini del nodo.
Solución: N = 50. p_1 = 40/50 = 0.80, p_2 = 10/50 = 0.20.
I_G = 1 - (0.80^2 + 0.20^2) = 1 - (0.64 + 0.04) = 0.3200.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Demuestre que al promediar B estimadores con varianza sigma^2 y correlación rho > 0, la varianza del ensamble es rho * sigma^2 + (1 - rho) * sigma^2 / B.
Solución:
Sea Y = (1/B) sum X_i.
Var(Y) = (1/B^2) [ sum Var(X_i) + sum_{i != j} Cov(X_i, X_j) ]
Var(Y) = (1/B^2) [ B * sigma^2 + B*(B - 1) * rho * sigma^2 ] = rho * sigma^2 + (1 - rho) * sigma^2 / B.
Cuando B tiende a infinito, la varianza se reduce a rho * sigma^2. Esto demuestra analíticamente que descorrelacionar los árboles (minimizando rho) es indispensable para reducir la varianza.""",
        "bloque_sugerido": "Laboratorio 50 min • Random Forests para diagnóstico en subestaciones",
        "slides": [
            {"numero": 1, "seccion": "CART", "titulo": "Árboles de Decisión", "puntos": ["Partición greedy maximizando reducción de impureza de Gini.", "Alta interpretabilidad en reglas de operación de protecciones."]},
            {"numero": 2, "seccion": "BAGGING", "titulo": "Random Forests", "puntos": ["Ensamble sobre muestras bootstrap y subespacios aleatorios.", "Reducción analítica de la varianza del modelo."]}
        ]
    },
    {
        "numero_tema": 26,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Agrupamiento No Supervisado con K-Means y Segmentación de Consumo",
        "objetivo": "Clasificar perfiles típicos de carga eléctrica diaria sin etiquetas previas mediante optimización de inercia intra-cluster.",
        "concepto_clave_latex": r"J = \sum_{j=1}^K \sum_{x_i \in S_j} \|x_i - \mu_j\|^2 \quad ; \quad \text{Inercia} \; W(K)",
        "ejemplo": """CLASE MAGISTRAL: APRENDIZAJE NO SUPERVISADO EN PERFILES DE DEMANDA
1. Taxonomía del Aprendizaje No Supervisado:
En redes de distribución, las distribuidoras no conocen a priori los patrones de comportamiento de miles de usuarios. K-Means agrupa clientes según similitud euclídea en sus vectores de demanda horaria de 24 horas.
2. Algoritmo de Lloyd (K-Means):
Asigna cada punto al centroide más cercano y recalcula los centroides como el promedio aritmético de los puntos asignados hasta converger la inercia.
3. Problema Resuelto 1 (Aplicación Directa):
Tres usuarios con perfiles de carga pico [Mañana, Tarde]: U1=[2, 3], U2=[3, 4], U3=[10, 12] y dos centroides iniciales C1=[2, 2] y C2=[9, 11]. Asigne cada usuario al cluster más cercano.
Solución:
Distancias euclídeas al cuadrado:
U1 a C1: 1. U1 a C2: 113. ==> Cluster 1.
U2 a C1: 5. U2 a C2: 85. ==> Cluster 1.
U3 a C1: 164. U3 a C2: 2. ==> Cluster 2.
Cluster 1: {U1, U2}. Cluster 2: {U3}.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Calcule la actualización de los centroides C1 y C2 tras el paso anterior y demuestre analíticamente que la inercia total disminuye estrictamente.
Solución:
Nuevo C1 = promedio(U1, U2) = [(2+3)/2, (3+4)/2] = [2.5, 3.5].
Nuevo C2 = [10, 12].
Inercia inicial: J_ini = 1 + 5 + 2 = 8.
Inercia actualizada:
d^2(U1, C1_new) = (2-2.5)^2 + (3-3.5)^2 = 0.5.
d^2(U2, C1_new) = (3-2.5)^2 + (4-3.5)^2 = 0.5.
d^2(U3, C2_new) = 0.
J_final = 0.5 + 0.5 + 0 = 1.0 < J_ini = 8.0.
La inercia disminuyó estrictamente, demostrando convergencia monótona hacia un mínimo local.""",
        "bloque_sugerido": "Pomodoro 50/10 • Clustering K-Means de perfiles de carga",
        "slides": [
            {"numero": 1, "seccion": "CLUSTERING", "titulo": "Algoritmo K-Means", "puntos": ["Segmentación de perfiles de carga de 24 horas sin supervisión previa.", "Optimización iterativa de Lloyd minimizando la inercia intra-cluster."]},
            {"numero": 2, "seccion": "DIAGNÓSTICO", "titulo": "Método del Codo y Silueta", "puntos": ["Determinación objetiva de la cantidad de arquetipos tarifarios K.", "Evaluación de cohesión y separación de conglomerados."]}
        ]
    },
    {
        "numero_tema": 27,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Redes Neuronales Artificiales I: Perceptrón Multicapa y Propagación Adelante",
        "objetivo": "Implementar la arquitectura matricial de un MLP feedforward con funciones de activación no lineales (ReLU).",
        "concepto_clave_latex": r"\mathbf{a}^{[l]} = g^{[l]}(\mathbf{W}^{[l]}\mathbf{a}^{[l-1]} + \mathbf{b}^{[l]}) \quad ; \quad \text{ReLU}(z) = \max(0, z)",
        "ejemplo": """CLASE MAGISTRAL: FUNDAMENTOS DEL APRENDIZAJE PROFUNDO
1. Del Perceptrón Simple al Perceptrón Multicapa (MLP):
El perceptrón simple no puede resolver problemas no lineales como XOR. El Teorema de Cybenko (1989) demuestra que un MLP con una capa oculta y activación no lineal es un aproximador universal de funciones continuas.
2. Funciones de Activación:
ReLU (Rectified Linear Unit): f(z) = max(0, z). Tiene derivada unitaria para z > 0, evitando el desvanecimiento del gradiente y acelerando el cómputo matricial.
3. Problema Resuelto 1 (Aplicación Directa):
Para una capa oculta con W = [[0.5, -0.2], [0.8, 0.4]], sesgo b = [0.1, -0.5] y entrada x = [1.0, 2.0], calcule la activación a usando ReLU.
Solución:
z_1 = 0.5*(1.0) + (-0.2)*(2.0) + 0.1 = 0.2.
z_2 = 0.8*(1.0) + (0.4)*(2.0) + (-0.5) = 1.1.
Aplicando ReLU: a = [max(0, 0.2), max(0, 1.1)] = [0.2, 1.1].
4. Problema Resuelto 2 (Nivel Examen Parcial):
Formule la propagación hacia adelante puramente vectorial en NumPy para un lote de m muestras con matriz X de forma (m, d_in), W de (d_in, d_out) y b de (1, d_out).
Solución:
import numpy as np
def forward_layer(X, W, b):
    Z = np.dot(X, W) + b
    A = np.maximum(0, Z)
    return Z, A
Para m = 1000 horas, d_in = 10 variables meteorológicas y d_out = 64 neuronas, np.dot opera en memoria contigua en C con librerías BLAS sin bucles for.""",
        "bloque_sugerido": "Laboratorio 50 min • Propagación hacia adelante en NumPy",
        "slides": [
            {"numero": 1, "seccion": "ARQUITECTURA", "titulo": "Perceptrón Multicapa (MLP)", "puntos": ["Teorema de Cybenko: aproximador universal de funciones continuas.", "Composición de capas afines z = W a + b y activaciones no lineales."]},
            {"numero": 2, "seccion": "ACTIVACIONES", "titulo": "ReLU y Mitigación de Saturación", "puntos": ["ReLU f(z) = max(0, z) preserva el flujo del gradiente en capas profundas.", "Formulación matricial por lotes para inferencia ultra rápida."]}
        ]
    },
    {
        "numero_tema": 28,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Redes Neuronales Artificiales II: Backpropagation y Optimizador Adam",
        "objetivo": "Calcular gradientes analíticos por regla de la cadena computacional y actualizar pesos con momentos adaptativos.",
        "concepto_clave_latex": r"\frac{\partial \mathcal{L}}{\partial \mathbf{W}} = \boldsymbol{\delta}^{[l]} (\mathbf{a}^{[l-1]})^T \quad ; \quad \mathbf{w}_{t} = \mathbf{w}_{t-1} - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon}\hat{m}_t",
        "ejemplo": """CLASE MAGISTRAL: RETROPROPAGACIÓN DEL ERROR Y OPTIMIZADORES MODERNOS
1. Algoritmo de Retropropagación (Backpropagation):
Evalúa el vector de derivadas parciales nabla_W L mediante la regla de la cadena aplicada al grafo computacional, propagando la señal de error delta hacia atrás.
2. Optimizador Adam (Adaptive Moment Estimation):
Combina el momento de Poljak (media móvil m_t) y RMSprop (media móvil del cuadrado v_t), adaptando la tasa de aprendizaje individual de cada peso.
3. Problema Resuelto 1 (Aplicación Directa):
En una neurona lineal con L = 0.5*(a - y)^2 donde a = W*x, con x = 3, y = 7 y W = 2, calcule dL/dW y el nuevo peso con alpha = 0.1.
Solución:
a = 2 * 3 = 6. dL/da = (6 - 7) = -1. da/dW = 3.
dL/dW = (-1) * 3 = -3.
W_new = 2 - 0.1 * (-3) = 2.3.
4. Problema Resuelto 2 (Nivel Examen Parcial):
Escriba la ecuación de corrección de sesgo en Adam y demuestre por qué m_t / (1 - beta_1^t) es un estimador insesgado de E[g_t] cuando m_0 = 0.
Solución:
m_t = (1 - beta_1) sum_{i=1}^t beta_1^{t - i} g_i.
Tomando esperanza E[g_i] = E[g_t]:
E[m_t] = (1 - beta_1) * E[g_t] * sum_{k=0}^{t-1} beta_1^k = (1 - beta_1) * E[g_t] * [(1 - beta_1^t) / (1 - beta_1)] = (1 - beta_1^t) * E[g_t].
Dividiendo entre (1 - beta_1^t) se obtiene E[m_hat_t] = E[g_t], eliminando el sesgo inicial hacia cero. Q.E.D.""",
        "bloque_sugerido": "Pomodoro 50/10 • Backpropagation y optimizador Adam",
        "slides": [
            {"numero": 1, "seccion": "BACKPROP", "titulo": "Regla de la Cadena Computacional", "puntos": ["Propagación reversa del tensor de errores delta desde la función de coste.", "Cálculo simultáneo de gradientes con complejidad temporal O(W)."]},
            {"numero": 2, "seccion": "ADAM", "titulo": "Momentos Adaptativos", "puntos": ["Combinación de momentum y RMSprop para amortiguar oscilaciones.", "Corrección analítica del sesgo de inicialización en cero."]}
        ]
    },
    {
        "numero_tema": 29,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Redes Neuronales Recurrentes (LSTM) para Pronóstico de Series Temporales",
        "objetivo": "Modelar dependencias temporales de largo plazo en generación fotovoltaica y demanda mediante celdas LSTM con compuertas.",
        "concepto_clave_latex": r"\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) \quad ; \quad \mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t",
        "ejemplo": """CLASE MAGISTRAL: PRONÓSTICO DE GENERACIÓN RENOVABLE CON LSTM
1. Limitación de RNN Estándar y el Problema del Gradiente Desvaneciente:
Al retropropagar en el tiempo a través de T pasos, el gradiente decae exponencialmente a cero si los autovalores son < 1.
2. Arquitectura de Celdas LSTM:
Introduce el estado de celda C_t como autopista lineal regulada por 3 compuertas: Olvido (f_t), Entrada (i_t) y Salida (o_t).
3. Problema Resuelto 1 (Aplicación Directa):
Para una compuerta de olvido con W_f = [0.4, 0.6], b_f = -1.2, h_{t-1} = 0.5 y entrada x_t = 1.5, determine el factor de retención f_t.
Solución:
z_f = 0.4*(0.5) + 0.6*(1.5) - 1.2 = 0.2 + 0.9 - 1.2 = -0.1.
f_t = 1 / (1 + exp(0.1)) = 1 / (1 + 1.1052) = 0.4750 (47.5% de memoria retenida).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Diseñe la estructura de tensores para pronosticar la generación solar de 24 horas a partir de una ventana histórica de 7 días (168 horas) con 4 variables meteorológicas para N = 5000 secuencias.
Solución:
Tensor de entrada X: (N, Timesteps, Features) = (5000, 168, 4).
Tensor de salida Y: (N, Forecast_Horizon) = (5000, 24).
Arquitectura: Capa LSTM(units=64, return_sequences=False) que colapsa los 168 pasos al estado oculto h_168 de tamaño (5000, 64), seguida de una capa Dense(24) lineal para el vector de 24 horas.""",
        "bloque_sugerido": "Laboratorio 50 min • Pronóstico de irradiancia solar con LSTM",
        "slides": [
            {"numero": 1, "seccion": "RECURRENTES", "titulo": "Dinámica Temporal y Memoria", "puntos": ["Superación del gradiente desvaneciente mediante la celda LSTM.", "Autopista lineal del estado de celda C_t para retención de largo plazo."]},
            {"numero": 2, "seccion": "COMPUERTAS", "titulo": "Compuertas de Olvido y Entrada", "puntos": ["Control matemático de flujo de información con compuertas sigmoideas.", "Pronóstico multivariable de generación renovable a 24 horas vista."]}
        ]
    },
    {
        "numero_tema": 30,
        "corte": 3,
        "modalidad": "tecnica",
        "titulo": "Despliegue de Modelos de IA en el Borde, Monitoreo de Data Drift y Ética",
        "objetivo": "Desplegar modelos en microcontroladores (Edge AI), cuantizar pesos a INT8 y monitorear deriva de datos en campo.",
        "concepto_clave_latex": r"D_{\text{KL}}(P \parallel Q) = \sum_{x} P(x) \ln\left(\frac{P(x)}{Q(x)}\right) \quad ; \quad q = \text{round}\left(\frac{r}{S}\right) + Z",
        "ejemplo": """CLASE MAGISTRAL: MLOPS, INFERENCIA EN EL BORDE Y DERIVA DE MODELOS
1. Edge Computing y Cuantización:
En subestaciones remotas, la falta de internet exige inferencia en el borde (ARM Cortex, ESP32). La cuantización convierte tensores de FP32 (4 bytes) a INT8 (1 byte), reduciendo la memoria en 75% y acelerando el cómputo.
2. Monitoreo de Data Drift con Divergencia KL:
La instalación de paneles solares modifica la distribución de demanda P(X). La Divergencia de Kullback-Leibler D_KL(P || Q) mide cuantitativamente la deriva para disparar reentrenamientos automáticos.
3. Problema Resuelto 1 (Aplicación Directa):
Un modelo de red neuronal ocupa 120 MB en float32. Calcule el peso en disco tras cuantizar a int8 y determine la reducción porcentual.
Solución:
Tamaño_int8 = 120 MB * (1 byte / 4 bytes) = 30 MB.
Reducción: (120 - 30) / 120 = 75% (factor 4x de compresión).
4. Problema Resuelto 2 (Nivel Examen Parcial):
Explique cómo usar la Divergencia de Kullback-Leibler D_KL(P || Q) para disparar una alerta automática de reentrenamiento de un modelo de demanda eléctrica cuando la distribución real Q difiere de la base P.
Solución:
D_KL(P || Q) = sum_{x} P(x) * log(P(x) / Q(x)).
Propiedades: D_KL >= 0 (Gibbs), D_KL = 0 sii P = Q.
Procedimiento MLOps:
Se discretiza la variable en B bins de histograma. Con umbral epsilon = 0.05, si D_KL(P || Q) > epsilon, se dispara una alerta de Data Drift Crítico que inicia un job de reentrenamiento en la nube con los datos del último trimestre antes de redistribuir los pesos cuantizados al hardware de campo.""",
        "bloque_sugerido": "Laboratorio 50 min • MLOps, cuantización INT8 y monitoreo de drift",
        "slides": [
            {"numero": 1, "seccion": "EDGE AI", "titulo": "Inferencia en el Borde y Cuantización", "puntos": ["Conversión de tensores FP32 a INT8 para dispositivos de campo de baja potencia.", "Inferencia autónoma en subestaciones sin dependencia de la nube."]},
            {"numero": 2, "seccion": "MLOPS", "titulo": "Detección de Data Drift", "puntos": ["Monitoreo de deriva con Divergencia de Kullback-Leibler.", "Gobernanza ética y reentrenamiento automatizado ante cambios estructurales de red."]}
        ]
    }
]

if __name__ == '__main__':
    target = '      - codigo: "01021802"'
    yaml_text = format_topics_yaml(topics)
    inject_topics_after(target, yaml_text)
    print("03011813 Fundamentos de Programación e IA now has 30 topics!")
