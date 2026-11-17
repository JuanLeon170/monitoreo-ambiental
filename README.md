# Monitoreo Ambiental

## Monitoreo Ambiental: Evaluación Normativa y Modelación de la Calidad Hídrica en Cundinamarca

Este proyecto busca analizar la calidad del agua en diferentes cuerpos hídricos del departamento de Cundinamarca.

A través del análisis de parámetros fisicoquímicos y microbiológicos, se pretende evaluar las condiciones del recurso hídrico, identificar posibles problemas de contaminación y comparar los resultados con la normativa ambiental vigente.

El proyecto utiliza herramientas de programación en JupyterLab para organizar y procesar los datos mediante condicionales, ciclos y funciones. Además, trabaja con información de fuentes oficiales como Datos Abiertos Colombia y la codificación territorial DIVIPOLA del DANE, con el fin de facilitar el análisis y la organización de la información ambiental.

Distribución de tareas
1. Gestión de Datos Territoriales y Lógica Condicional Normativa
Integrante 1: Juan Carlos León Ramos
Módulos asignados: data/calidad_agua_cundinamarca_gov.csv y notebooks/01_condicionales_juan.ipynb
Restricción : Uso exclusivo de estructuras condicionales (if, elif, else)
Responsabilidades y formulación:
Estructuración del Dataset Oficial: Normalización de registros fisicoquímicos y microbiológicos para 8 municipios de Cundinamarca (25269 Facatativá, 25019 Albán, 25286 Funza, 25430 Madrid, 25754 Soacha, 25473 Mosquera, 25899 Zipaquirá y 25307 Girardot) bajo codificación DANE DIVIPOLA.
Clasificación Sanitaria Puntual (Art. 15, Resolución 2115 de 2007): Categorización del Índice de Riesgo de la Calidad del Agua ($\text{IRCA}$):
$$\text{Nivel de Riesgo} = \begin{cases} \text{Sin Riesgo (Apta)} & 0.0\% \le \text{IRCA} \le 5.0\% \\ \text{Riesgo Bajo} & 5.0\% < \text{IRCA} \le 14.0\% \\ \text{Riesgo Medio} & 14.0\% < \text{IRCA} \le 35.0\% \\ \text{Riesgo Alto} & 35.0\% < \text{IRCA} \le 80.0\% \\ \text{Inviable Sanitariamente} & 80.0\% < \text{IRCA} \le 100.0\% \end{cases}$$
Validación Fisicoquímica: Control lógico de rango óptimo para potencial de hidrógeno ($6.5 \le \text{pH} \le 9.0$) y cloro residual libre ($0.3\text{ mg/L} \le \text{Cl}_2 \le 2.0\text{ mg/L}$).

2. Procesamiento Iterativo Departamental y Simulación Cinética PTAP
Integrante 2: Leydy Andrea Salinas Diaz
Módulo asignado: notebooks/02_bucles_leydy.ipynb
Restricción : Uso exclusivo de estructuras repetitivas (for, while)
Responsabilidades y formulación:
Barrido Iterativo de Estaciones (Bucle for): Recorrido secuencial de los N=8 registros municipales del dataset oficial para calcular promedios consolidados de la red departamental:
$$\overline{\text{IRCA}} = \frac{1}{N} \sum_{i=1}^{N} \text{IRCA}_i \qquad \qquad \overline{T} = \frac{1}{N} \sum_{i=1}^{N} T_i$$
Simulación de Remoción de Turbiedad en Floculación/Sedimentación (Bucle while): Modelación iterativa de las etapas de clarificación requeridas en una Planta de Tratamiento de Agua Potable (PTAP) para reducir la turbiedad inicial de un afluente crítico ($T_0 = 48.5\text{ UNT}$) hasta cumplir el límite normativo ($T_n \le 2.0\text{ UNT}$):
Tn=Tn-1(1-)
Donde Tn representa la turbiedad remanente tras n ciclos de retención hidráulica y =0.35 corresponde a la eficiencia de remoción por etapa.

3. Modularización Matemática, Balance de Cargas y Documentación
Integrante 3: Laura Sofia Bolivar Jimenez
Módulos asignados: notebooks/03_funciones_laura.ipynb y README.md
Restricción: Modularización mediante funciones reutilizables (def / return).
Responsabilidades y formulación:
Cálculo Ponderado del IRCA (calcular_irca_res2115): Implementación de los puntajes oficiales de riesgo de la Resolución 2115 de 2007 ($\text{pH} = 1.5$, $\text{Turbiedad} = 15.0$, $\text{Cloro Residual} = 15.0$, $\text{Coliformes Totales} = 15.0$):
$$\text{IRCA}(\%) = \frac{\sum_{j \in \text{No Aceptables}} P_j}{\sum_{i=1}^{m} P_i} \times 100$$
Balance de Carga Contaminante Vertida (calcular_carga_contaminante_dia): Estimación del flujo másico diario de contaminantes descargados a cuerpos receptores superficiales a partir del caudal Q ($\text{L/s}$) y la concentración C ($\text{mg/L}$):
$$C_c \left[\frac{\text{kg}}{\text{día}}\right] = Q \left[\frac{\text{L}}{\text{s}}\right] \times C \left[\frac{\text{mg}}{\text{L}}\right] \times 0.0864$$
Dosificación Química de Desinfección (estimar_demanda_cloro): Cálculo de masa de hipoclorito requerida ($\text{g}$) según el volumen del tanque (V en $\text{m}^3$) y la dosis demandada (D en $\text{mg/L}$).
