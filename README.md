# Segundo_Desafio_TelecomX
Proyecto para predecir el abandono de clientes desde la empresa de telecomunicaciones Telecom X.

**Extraccion y Visualizacion de los datos**
Se carga el dataframe df , con7267 columnas  con 21 columnas
Se visualizan los datos.

**Calculo de Clases**
Se determina que hay un 25.7% de abandono de clientes. Ese dato indica que hay un desbalance de clases.

**PREPARACION DE LOS DATOS PARA EL MODELADO**

**APLICANDO FEATURE ENGINEERING**
**Creando variables**
 Se crea una nueva variable Gasto_mensual_antiguedad, que es la union de las variables Cuentas_diarias y Antiguedad_meses
Gasto_mensual_antiguedad que refleja el gsto del cliente segun la antiguedad que tiene.

**Removiendo columnas**
Antes e remover las columnas que no son necesarias para el estudio en cuestión, se usó mutual_info_classif  para determinar las columnas a eliminar
Se eliminaran las variables que tengan menor indice MI, ya son las que menos aportan en el analisis del churn.

Las columnas que se dejaron en el dataframe son:
	Abandono_cliente	
 Antiguedad_meses	
 Seguridad_en_línea_Internet	
 Tipo_de_contrato
 Metodo_de_pago	
 Gasto_diario_antiguedad

**Verificando Correlacion entre variables**

Aplicando indice VIF para ver si hay colinealidad entre variables
Si el valor es menor a 5 no hay problemas de multicolinealidad. En consecuncia, las variables elegidas no tienen multicolinealidad.

Verificando fuga de datos con Correlacion Pearson

Dataframe datos_reducido para el modelado

CREANDO BASELINE CON MODELO DUMMY





