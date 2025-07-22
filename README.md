# Segundo_Desafio_TelecomX
Proyecto para predecir el abandono de clientes desde la empresa de telecomunicaciones Telecom X.
Extraccion y Visualizacion de los datos

Calculo de Clases

PREPARACION DE LOS DATOS PARA EL MODELADO

APLICANDO FEATURE ENGINEERING

Creando variables
 Se crea nueva variable Gasto_mensual_antiguedad, que es la union de las variables Cuentas_diarias y Antiguedad_meses
Gasto_mensual_antiguedad que refleja el gsto del cliente segun la antiguedad que tiene.

Removiendo columnas
Usando mutual_info_classif (Información Mutua) para determinar las columnas a eliminar
Se eliminaran las variables que tengan menor indice MI, ya son las que menos aportan en el analisis del churn.

Verificando Correlacion entre variables

Aplicando indice VIF para ver si hay colinealidad entre variables
Si el valor es menor a 5 no hay problemas de multicolinealidad. En consecuncia, las variables elegidas no tienen multicolinealidad.

Verificando fuga de datos con Correlacion Pearson

Dataframe datos_reducido para el modelado

CREANDO BASELINE CON MODELO DUMMY





