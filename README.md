# 🧠 Segundo Desafío - Telecom X

La empresa **Telecom X** quiere anticiparse al problema del abandono de clientes.  
El objetivo es desarrollar **modelos predictivos** capaces de prever qué clientes tienen mayor probabilidad de cancelar sus servicios.

---

## 📊 Extracción y Visualización de los Datos

- Se carga el DataFrame `df`, con **7267 filas y 21 columnas**.
- Se realiza una inspección inicial para entender la estructura y calidad de los datos.

---

## 📉 Cálculo de Clases

- Se determina que un **25.7% de los clientes ha abandonado el servicio**.
- Esto refleja un **desbalance de clases**, lo cual debe ser abordado en el modelado.

---

## 🧹 Preparación de los Datos para el Modelado

### 🛠️ Feature Engineering

#### ➕ Creación de nuevas variables
- Se crea la variable `Gasto_mensual_antiguedad` como combinación de:
  - `Cuentas_diarias`
  - `Antiguedad_meses`
- Esta variable refleja el gasto mensual relativo a la antigüedad del cliente.

#### ➖ Eliminación de columnas irrelevantes
- Se usa `mutual_info_classif` para calcular la **Información Mutua (MI)** de cada variable respecto al objetivo.
- Se eliminan las variables con menor MI por su bajo aporte al análisis del **churn**.

---

## 📌 Variables Seleccionadas para el Modelado

- `Abandono_cliente`  
- `Antiguedad_meses`  
- `Seguridad_en_línea_Internet`  
- `Tipo_de_contrato`  
- `Metodo_de_pago`  
- `Gasto_diario_antiguedad`

---

## 🔄 Verificación de Correlación entre Variables

- Se aplicó el **índice VIF (Variance Inflation Factor)** para detectar multicolinealidad:
  - Todos los valores < 5 → No hay multicolinealidad.
- Se utilizó la **correlación de Pearson** para identificar posibles **fugas de datos**.

> 📌 El DataFrame final utilizado se llama `datos_reducido`.

---

## 🎯 Baseline: Modelo Predictivo Base

- Se construyó un **modelo Dummy** como línea base.
- **Score del modelo Dummy:** `0.7560` (accuracy de clase mayoritaria)

---

## 🤖 Creación de Modelos Predictivos

Se implementaron **tres modelos**:

- `KNN`  
- `Decision Tree`  
- `Random Forest`

Cada modelo fue:

- Implementado mediante `Pipeline` usando `sklearn.pipeline.Pipeline` o `imblearn.pipeline.make_pipeline`.
- Ajustado mediante mejora de **hiperparámetros**, **umbral de decisión** y **optimización de Recall**.

---

## 📊 Comparación de los Mejores Modelos

| Modelo | Umbral | Accuracy | Precision (Clase 1) | Recall (Clase 1) | F1-score | AUC      |
|--------|--------|----------|----------------------|------------------|----------|----------|
| KNN    | 0.22   | 0.6391   | 0.4065               | 0.8764           | 0.5553   | 0.7960   |
| DT     | 0.22   | 0.5577   | 0.3620               | 0.9438           | 0.5233   | 0.8158   |
| RF     | 0.22   | 0.5814   | 0.3757               | 0.9486           | 0.5383   | 0.8313   |

> 🏆 **Mejor modelo:** `Random Forest (RF3)` → `pipe_rfopt`

---

## 🧪 Evaluación de Nuevos Clientes

- Se desarrolló código para evaluar **nuevos clientes individuales** ingresando sus variables relevantes.
- También se implementó un sistema para evaluar **múltiples clientes en lote**.

---

## 📈 Visualización de Tendencias del Abandono

Se presentan tres visualizaciones clave:

1. 📦 **Boxplot**: Antigüedad vs Tipo de Contrato vs Abandono  
2. 💸 **Gráfico de Gasto Diario por Antigüedad** según Abandono_cliente  
3. 🔵 **Scatterplot**: Antigüedad vs Gasto Diario, diferenciando por Cancelación y Contrato

---

## 🧬 Importancia de las Variables

- Se utilizó un modelo de **Random Forest** para calcular la importancia relativa de cada variable.
- **`Gasto_diario_antiguedad`** resultó ser **la más importante**, con un peso aproximado de **0.65** en la predicción.

---

## ⚖️ Cálculo del Odds Ratio

- El **odds ratio** se utilizó para cuantificar la fuerza de asociación entre variables y el abandono.
- Compara la probabilidad de abandono entre grupos con y sin exposición a ciertos factores (contrato, gasto, etc.).

---

## ✅ Conclusión

- La variable **`Gasto_diario_antiguedad`** es el **mejor predictor de abandono** con un OR ≈ **8.2**.
- Le siguen:
  - El **tipo de contrato**
  - La **antigüedad del cliente**
- El modelo **Random Forest optimizado (pipe_rfopt)** logra el mejor balance entre precisión y recall.

---

## Herramientas Utilizadas
La base de este trabajo es el lenguaje Python
Se usaron las bibliotecas de python:
pandas as pd
numpy as np
matplotlib.pyplot as plt
seaborn as sns
sklearn.feature_selection import mutual_info_classif
statsmodels.stats.outliers_influence import variance_inflation_factor
statsmodels.tools.tools import add_constant
sklearn.dummy import DummyRegressor
fsklearn.model_selection import train_test_split
sklearn.dummy import DummyClassifier
sklearn.pipeline import Pipeline
sklearn.compose import ColumnTransformer
fsklearn.preprocessing import StandardScaler, OneHotEncoder
imblearn.pipeline import Pipeline as ImbPipeline
imblearn.over_sampling import SMOTE
sklearn.neighbors import KNeighborsClassifier
sklearn.model_selection import train_test_split
sklearn.metrics import (confusion_matrix, classification_report,accuracy_score, f1_score, roc_auc_score, roc_curve)
sklearn.model_selection import GridSearchCV
imblearn.pipeline import make_pipeline
sklearn.model_selection import train_test_split
sklearn.preprocessing import StandardScaler, OneHotEncoder
sklearn.tree import DecisionTreeClassifier
imblearn.over_sampling import SMOTE
imblearn.pipeline import make_pipeline
scipy.stats import randint
sklearn.model_selection import RandomizedSearchCV
sklearn.ensemble import RandomForestClassifier
sklearn.model_selection import StratifiedKFold, cross_val_predict

## AUTOR
Gabriel Mendez Oteiza



