import pandas as pd
import joblib

# Cargar el modelo previamente guardado
pipe_rfopt = joblib.load('modelo_abandono.pkl')

# Variables requeridas por el modelo
columnas_modelo = [
    'Antiguedad_meses',
    'Seguridad_en_línea_Internet',
    'Tipo_de_contrato',
    'Metodo_de_pago',
    'Gasto_diario_antiguedad'
]

def ingresar_cliente():
    print("\n--- Ingresar datos del cliente ---")
    antiguedad = int(input("Antigüedad en meses: "))
    seguridad = int(input("¿Tiene seguridad en línea? (1=Sí, 0=No): "))
    contrato = int(input("Tipo de contrato (0=Mes a mes, 1=Un año, 2=Dos años): "))
    metodo_pago = int(input("Método de pago (0=Electronic check, 1=Mailed check, 2=Bank, 3=Card): "))
    gasto_diario = float(input("Gasto diario por antigüedad: "))

    return [antiguedad, seguridad, contrato, metodo_pago, gasto_diario]

# Lista para almacenar datos de clientes nuevos
clientes_nuevos = []

while True:
    cliente = ingresar_cliente()
    clientes_nuevos.append(cliente)

    otro = input("¿Deseas ingresar otro cliente? (s/n): ").lower()
    if otro != 's':
        break

# Crear DataFrame con los datos ingresados
clientes_df = pd.DataFrame(clientes_nuevos, columns=columnas_modelo)

# Realizar predicciones
probabilidades = pipe_rfopt.predict_proba(clientes_df)[:, 1]
umbral_optimo = 0.22
predicciones = (probabilidades >= umbral_optimo).astype(int)

# Mostrar resultados
print("\n--- Resultados de predicción ---")
for i, (prob, pred) in enumerate(zip(probabilidades, predicciones), start=1):
    print(f"Cliente {i}: Prob. de abandono = {prob:.2f} → {'Sí' if pred else 'No'}")
