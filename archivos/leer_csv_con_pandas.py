import pandas as pd #se importa con pd
#los dataframe son esctructura de datos bidimensionales similares a una hoja de calculo. Al no comportarse como un archivo comun, por ejemplo siempre va a tener filas y columnas

#usando la fn read csv para leer el archivo csv
archivo = pd.read_csv("archivos\\prueba_csv.csv")
archivo2 = pd.read_csv("archivos\\prueba_datos_2.csv")


#obteniendo los datos de la columna nombre
#nombres = archivo["name"]

#datos_edad_ordenados = archivo.sort_values("edad")
#print(datos_edad_ordenados)

#ordenando de forma descensdente
#datos_edad_desc = archivo.sort_values('edad', ascending=False)
#print(datos_edad_desc)

#concatenando los dataframe
df_concatenado = pd.concat([archivo,archivo2])
#print(df_concatenado)

#Prueba para utilizar método sliceing
#cadena = '0123456789'
#print(cadena[:])#Al poner : recorre toda la cadena. Sino, a la izquierda significa desde y a la derecha va el hasta. Por ejemplo 1:7, o :7. La posición 0 sí está incluida, el valor de la derecha no está incluido 

#Accediendo a la primera fila con head()
primera_fila = archivo.head(1)#Si le paso 1 y accedemos a la 1ra fila. Si ponemos 0 nos muestra nombre,apellido,edad
#print(primera_fila)

#Con tail() accedemos a las últimas filas
ultimas_filas = archivo.tail(3)
#print(ultimas_filas)

#Accediendo a la cantidad de filas y columnas con shape. Shape, es un atributo, o sea, una propiedad del objeto

filas_y_columnas_totales = archivo.shape
#print(filas_y_columnas_totales)#El resultado te muestra una TUPLA. Y esto, al ser una TUPLA la podemos desempaquetar como hacemos más abajo y de esa forma manipular los datos de una forma más eficiente

#Podemos desempaquetar esto y poner:
filas_totales,columnas_totales = archivo.shape
#print(columnas_totales)

#Obteniendo data estadistica del dataframe : 
archivo_info = archivo.describe()
#print(archivo_info)Los datos que retorna son datos estadisticos

#Accediendo a un dato especifico del archivo con loc
elemento_especifico_loc = archivo.loc[2,"edad"]
#print(elemento_especifico_loc)

#Accediendo a un dato especifico del archivo con iloc. Con iloc solamente accedemos por los indices (2 es edad y 2 es el index 2 tenemos lo mismo que cn loc)
elemento_especifico_iloc = archivo.iloc[2,2]
#print(elemento_especifico_iloc)

#Accediendo a todas las filas de una columna con iloc y sliceing

apellidos = archivo.iloc[0:,0]#acá al sliceing le estamos diciendo que empiece en posición 0 y como no ponemos 2 do parametro,va a traer todos los valores que haya. Y como 2do parametro ponemos la posición del dato que queremos que traiga
#print(apellidos)

#accediendo a la fila 3 con loc 
fila_3 = archivo.loc[2,:] # de esta forma le decimos que ingrese al indice 2, osae ruki y al poner : , que traiga todos los datos de esa fila. Si quisiera hacerlo con iloc en est caso es lo mismo porque es por indice
#print(fila_3)

#accediendo a las filas con edad mayor que 30
mayor_que_30 = archivo.loc[archivo["edad"]>30,:]
#print(mayor_que_30)