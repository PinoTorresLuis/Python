#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv('archivos\\prueba_csv.csv')
#convirtiendo a str los datos de una columna
df['edad']=df['edad'].astype(str)

#print(type(df['edad'][0])) muestra que es un string

#reemplazando valores. Es necesario que esté la propiedad inplace = true
df['nombre'].replace('luis','maestro',inplace=True)
#print(df['nombre'])

#eliminando filas con datos faltantes
#print("lista incompleta",df)
df = df.dropna()
#print("lista con datos faltante eliminado",df)

#eliminando las filas repetidas
df = df.drop_duplicates()
print(df)

#para guardar el dataframe limpio podemos crear uno nuevo limpio
df.to_csv('archivos\\prueba_datos_limpios_csv.csv')