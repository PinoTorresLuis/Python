diccionario = {
    "nombre":"luis",
    "apellido":"pino",
    "edad":29
}
#Keys devuelve todas las key del diccionario. Esto después nos va a servir para poder iterar
claves = diccionario.keys()
print(claves)
#Get me devuelve el valor de la key que le indico. Si no encuentra nada el programa continua
value = diccionario.get("nombre")
print(value)

#Eliminando todo del diccionario
#diccionario.clear()
#print(diccionario)

#Eliminando un elemento del diccionario
diccionario.pop("nombre")#si quiero sacar más elementos, pongo una coma
print(diccionario)
#Obteniendo un elemento dic_ites iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)