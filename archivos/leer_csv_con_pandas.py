import pandas as pd #se importa con pd
#los dataframe son esctructura de datos bidimensionales similares a una hoja de calculo. Al no comportarse como un archivo comun, por ejemplo siempre va a tener filas y columnas

#usando la fn read csv para leer el archivo csv
archivo = pd.read_csv("archivos\\prueba_csv.csv",names = ["name","lastname","age"])
print(archivo)
#obteniendo los datos de la columna nombre
nombres = archivo["age"]

