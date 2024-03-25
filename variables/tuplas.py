#Las tuplas las podemos crear cuand son datos de sólo lectura. Manejan mejor el espacio en memoria. Son mucho más óptimas para datos fijos

#Las listas manejan dos espacios en memoria,key= value cuando modificas un espacio en la lista. Son mucho más óptimas para datos flexibles.

tupla = tuple(["Dato1","Dato2"])#Forma de crear tupla con tuple
tupla2 = "Hola","Adios"#Esto también es tupla
tupla3 = "Dato3", #Con una coma al final, también es una tupla
print(tupla)