
#Lista si se puede modificar
lista = ["hola", 1,2,3,4, True,["a","b","c"]]
print (lista[0])

#Tupla no se puede modificar
tupla1 = [1,2,3,4,5,6,"hola"]
type(tupla1)

#creando un conjunto (set) se puede redefinir  pero no modificar. No deja acceder por el indice y repetir datos

conjunto = {"hola", "chau",1}

#conjunto[1] = "Adiós" ESTO ESTÁ MAL

conjunto = {"Ahora sí, esto funciona porque lo redefini"}
print (conjunto)
        
#creando un diccionadrio

diccionario = {
    'nombre': 'Luis Pino',
    'edad': 27
}        
print (diccionario["nombre", "edad"])

tupla1 = [1,2,3,4,5,6,"hola"]
type(tupla1)
