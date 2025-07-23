🧠 Segundo Desafío - Telecom X
La empresa Telecom X busca anticiparse al problema del abandono de clientes.
El objetivo es desarrollar modelos predictivos capaces de prever qué clientes tienen mayor probabilidad de cancelar sus servicios.

📊 Extracción y Visualización de los Datos
Se carga el DataFrame df, con 7267 filas y 21 columnas.

Se realiza una inspección inicial para entender la estructura y calidad de los datos.

📉 Cálculo de Clases
Se determina que un 25.7% de los clientes ha abandonado el servicio.

Esto refleja un desbalance de clases, lo cual debe ser considerado al modelar.

🧹 Preparación de los Datos para el Modelado
🛠️ Feature Engineering
➕ Creación de nuevas variables
Se crea la variable Gasto_mensual_antiguedad como combinación de:

Cuentas_diarias

Antiguedad_meses

Esta variable refleja el gasto mensual relativo a la antigüedad del cliente.

➖ Eliminación de columnas irrelevantes
Se utiliza mutual_info_classif para calcular la Información Mutua (MI).

Se eliminan las variables con menor MI por su bajo aporte al análisis del churn.

📌 Variables Seleccionadas para el Modelado
Abandono_cliente

Antiguedad_meses

Seguridad_en_línea_Internet

Tipo_de_contrato

Metodo_de_pago

Gasto_diario_antiguedad

🔄 Verificación de Correlación entre Variables
Se aplicó el índice VIF (Variance Inflation Factor):

Todos los valores < 5 → no hay multicolinealidad.

Se utilizó correlación de Pearson para detectar posibles fugas de datos.

📌 El DataFrame final utilizado se llama: datos_reducido.

🎯 Baseline: Modelo Predictivo Base
Se construyó un modelo DummyClassifier como línea base.

Score del modelo Dummy: 0.7560 (accuracy al predecir siempre la clase mayoritaria).

🤖 Creación de Modelos Predictivos
Se desarrollaron tres modelos supervisados:

KNN

Decision Tree

Random Forest

Cada modelo fue:

Implementado con Pipeline usando sklearn o imblearn.

Mejorado mediante:

Ajuste de hiperparámetros.

Optimización del umbral.

Optimización del Recall (minimizar falsos negativos).

📊 Comparación de los Mejores Modelos
Modelo	Umbral	Accuracy	Precision (Clase 1)	Recall (Clase 1)	F1-score	AUC
KNN	0.22	0.6391	0.4065	0.8764	0.5553	0.7960
DT	0.22	0.5577	0.3620	0.9438	0.5233	0.8158
RF	0.22	0.5814	0.3757	0.9486	0.5383	0.8313

🏆 Mejor modelo: Random Forest (RF3) → pipe_rfopt

🧪 Evaluación de Nuevos Clientes
Se implementó un sistema para evaluar nuevos clientes individuales.

También se desarrolló código para predecir el abandono de múltiples clientes en lote.

📈 Visualización de Tendencias del Abandono
Se generaron tres visualizaciones clave:

📦 Boxplot: Antigüedad vs Tipo de Contrato vs Abandono

💸 Gráfico de Gasto Diario por Antigüedad según Abandono_cliente

🔵 Scatterplot: Antigüedad vs Gasto Diario, por Cancelación y Tipo de Contrato

🧬 Importancia de las Variables
Usando Random Forest, se calculó la importancia relativa de cada variable.

Gasto_diario_antiguedad fue la variable más relevante, con un peso de aproximadamente 0.65.

⚖️ Cálculo del Odds Ratio
Se utilizó el odds ratio para cuantificar la probabilidad de abandono en distintos grupos.

Se comparan odds de abandono entre grupos expuestos y no expuestos a variables como tipo de contrato, gasto, etc.

✅ Conclusión
Gasto_diario_antiguedad es el predictor más potente del abandono (OR ≈ 8.2).

Le siguen:

Tipo de contrato

Antigüedad del cliente

El modelo Random Forest optimizado (pipe_rfopt) ofrece el mejor balance entre precisión y recall.

🧰 Herramientas Utilizadas
Proyecto desarrollado en Python con las siguientes bibliotecas:

pandas, numpy

matplotlib, seaborn

sklearn: selección de variables, modelado, pipelines, métricas, validación

imblearn: balanceo con SMOTE y pipelines

statsmodels: VIF

scipy.stats: búsqueda aleatoria de hiperparámetros

👤 Autor
Gabriel Méndez Oteiza
Proyecto desarrollado como parte del desafío de análisis y predicción del abandono de clientes en Telecom X.

