# Segundo Desafío - Telecom X

Proyecto para predecir el abandono de clientes en la empresa de telecomunicaciones **Telecom X**.


## 📊 Extracción y Visualización de los Datos

- Se carga el DataFrame `df`, con 7267 filas y 21 columnas.
- Se visualizan los datos para una primera inspección.

---

## 📉 Cálculo de Clases

- Se determina que hay un **25.7% de abandono de clientes**.
- Esto indica un **desbalance de clases**, que se debe considerar al modelar.

---

## 🧹 Preparación de los Datos para el Modelado

### 🛠️ Feature Engineering

#### ➕ Creación de nuevas variables
- Se crea la variable `Gasto_mensual_antiguedad`, que es la combinación de:
  - `Cuentas_diarias`
  - `Antiguedad_meses`
- Esta variable refleja el gasto del cliente en función de su antigüedad.

#### ➖ Remoción de columnas
- Antes de eliminar columnas, se utilizó `mutual_info_classif` para medir la importancia de cada variable.
- Se eliminaron las variables con menor índice de **Información Mutua (MI)**, ya que aportan poco al análisis del **churn**.

---

## 📌 Variables seleccionadas para el modelado

- `Abandono_cliente`  
- `Antiguedad_meses`  
- `Seguridad_en_línea_Internet`  
- `Tipo_de_contrato`  
- `Metodo_de_pago`  
- `Gasto_diario_antiguedad`  

---

## 🔄 Verificación de correlación entre variables

- Se aplicó el **índice VIF** (Variance Inflation Factor) para detectar multicolinealidad.
  - Como los valores fueron menores a 5, no hay problemas de multicolinealidad.
- Se utilizó la **correlación de Pearson** para verificar posibles fugas de datos.

- El DataFrame final para el modelado se llama: `datos_reducido`.

---

## 🎯 Baseline: Modelo Predictivo Base

- Se construyó un modelo Dummy como línea base para comparar los modelos futuros.
- Este modelo tiene un score de 0.7560
---
##  CREANDO MODELOS PREDICTIVOS
Se crearon tres modelos , que son : KNN, DecisionTree y RandomForest.
Todos los modelos se crearon con Pipeline, usando sklearn.pipeline import Pipeline o imblearn.pipeline import make_pipeline
Cada modelo se creo un modelo base y luego se mejoraron los hiperparametros, el umbral y se mejoró el Recall, para llegar al mejor modelo

---

## 📊Comparacion de los tres mejores en cada modelo.
En el caso de KNN, el mejor modelo fue : pipe_knn_opt
En el caso de DecisionTree, el mejor modelo fue: pipe_arbol_opt
En el caso de RandomForest, el mejor modelo fue: pipe_rfopt

---

## 📊Comparacion de los tres mejores e modelo.
Los tres mejores modelos, se compararon y las metricas de los modelos son:

Modelo  Umbral  Accuracy  Precision (Clase 1)  Recall (Clase 1)  \
0  KNN 3    0.22  0.639053             0.406452          0.876404   
1   DT 2    0.22  0.557727             0.361995          0.943820   
2   RF 3    0.22  0.581395             0.375715          0.948636   

   F1-score (Clase 1)       AUC  
0            0.555348  0.795976  
1            0.523287  0.815838  
2            0.538251  0.831315  

Finalmente el mejor modelo fue: **pipe_rfopt**

---

## EVALUANDO NUEVOS CLIENTES CON EL MODELO










