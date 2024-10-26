from sklearn.preprocessing import LabelEncoder # type: ignore
from sklearn.metrics import mean_squared_error, r2_score # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sbr # type: ignore
import numpy as dts  # type: ignore
import pandas as pd
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore

car_data = pd.read_csv('car data.csv')
car_dekho = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')

print("Primeras filas de  'car data':")
print(car_data)

print("\nPrimeras filas de 'Car DETAILS FORN CAR DEKHO':")
print(car_dekho)


print("\nNombres de las columnas en 'car data':")
print(car_data.columns.tolist())
print("\nNombres de las columnas en 'CAR DETAILS FROM CAR DEKHO':")
print(car_dekho.columns.tolist())

car_data.columns = car_data.columns.str.strip()
car_dekho.columns = car_dekho.columns.str.strip()

print("\nNombres de las columnas despues de limpiar en 'car data':")
print(car_data.columns.tolist())
print("\nNombres de las columnas despues de limpiar en 'CAR DETAILS FROM CAR DEKHO':")
print(car_dekho.columns.tolist())

if 'Selling_Price' in car_data.columns:
    print("\n'Selling_Price' existe en 'car data'")
else:
    print("\n'Selling_Price' No existe en 'car data'")

if 'Selling_Price' in car_dekho.columns:
    print("\n'Selling_Price' existe en 'CAR DETAILS FROM CAR DEKHO'")
else:
    print("\n'Selling_Price' No existe en 'CAR DETAILS FROM CAR DEKHO'")

    # numpy es una libreria de datos
# saborn es un libreria de interfas de alto nivel para crear graficos estadisticos
# matplotlib.pyplot saborn es un libreria de interfas de alto nivel para crear graficos estadisticos pero en dos dimenciones

# Importar datos de cada una de las librerias

# Vamos o importamos cargar los datos
Data = pd.read_csv('Car details v3.csv')

# Mostrar los datos con lo siguiente
Data.head(5)

# Vamos a describir los datos con los describe
Data.describe()

# Manejar los datos que nos falta
# nan = no aplica los datos
# inplace remplace cierto dato
# numeric_only = validar que solo sea verdadero o falso
Data.replace(0, dts.nan, inplace=True)
Data.fillna(Data.mean(numeric_only=True), inplace=True)
Data.fillna('NA', inplace=True)

# Mostrar los datos
Data.head(5)

print(Data.columns)

# Vamos a configurar las columnas
plt.figure(figsize=(6, 3))
# Boxplot es la que distrubulle los datos para encontrar los datos como mediana, cuartiles, persentiles
sbr.boxplot(x=Data['selling_price'])
# title = Titulo
plt.title('Identificación de Datos Atípicos', fontsize=10)

# crear variable de años (year)
plt.figure(figsize=(6, 3))
sbr.boxenplot(x=Data['year'])

# Crear la variable de km_driven

plt.figure(figsize=(6, 3))
sbr.boxenplot(x=Data['km_driven'])

# Crear la variable de fuel
plt.figure(figsize=(6, 3))
sbr.boxenplot(x=Data['fuel'])


max_asientos = 10
min_asientos = 2
total_asientos = ((Data['seats'] < min_asientos) |
                  (Data['seats'] > max_asientos)).sum()

max_ano = 2020
min_ano = 1990
total_ano = ((Data['year'] < min_ano) | (Data['year'] > max_ano)).sum()

print("Total registros dataset: {}".format(len(Data)))
print("El total de datos atípicos para la cantidad de asientos es {}".format(
    total_asientos))
print("El total de datos atípicos para el año es {}".format(total_ano))
print("")
Data.info()
