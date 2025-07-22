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

## 🎯 Baseline: Modelo Dummy

- Se construyó un modelo Dummy como línea base para comparar los modelos futuros.

---
✅ Recomendaciones
Guarda este contenido como README.md en la raíz del repositorio.

Puedes seguir agregando secciones como "Modelos Probados", "Métricas", "Conclusiones", etc.

¿Quieres que te agregue una sección de resultados o visualizaciones también?









Preguntar a ChatGPT


