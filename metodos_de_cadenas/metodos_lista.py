#Creando una lista con list()
lista = list([12,10,"hola",True,"adios"]) #Las listas se suelen usar para crear listas vacías 
print(type(lista))
#Len devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)
print(cantidad_elementos)
#Append agrega un elemento a la lista
agregar_elemento = lista.append("HOLsdsdL")
print(agregar_elemento)#Esto devuelve "None",es un valor especial que representa la ausencia de contenido o valor en una variable. Sin embargo,almacena el nuevo caracterer.

lista.append("HOLKAETUL")
print("append:", lista)

#Insert agrega un elemento a la lista en un indice especifico
lista.insert(2,"SOYNUEVAPOSICIÓN2")
print("Insert:", lista)

#Extends agrega varios elementos a la lista 
lista.extend(["nueva lista","con nuevos elementos"])
print("Extiendo la lista:", lista)

#Pop eliminando un elemento de la lista (por su indice)
lista.pop(0) #Indicamos el número del indice que queremos eliminar. A su vez, si ponemos el signo -, le indicamos cuál es el elemento que queremos contando de atrás para adelante. -1 (último), -2(ante último)
print('Eliminamos con POP', lista)

#Remove remueve un elemento de la lista por su valor
lista.remove("adios")
print("prueba de remove",lista)

#Clear remueve todos los elementos de la lista
#lista.clear()

#Sort sirve para ordenar la lista, que contengan números o true, los cuales van a quedar primeros.
lista_sort = [5,1,2,3,9,10,6,7,8,4]
lista_sort.sort()
print("lista ordenada",lista_sort)
#Reverse , hace lo mismo pero lo ordena de forma descendente.
lista_sort.reverse()
print("lista al reves",lista_sort)

#Con index verificamos si el elemento existe en la lista
elemento_encontrado = lista_sort.index(5)
print("Busqueda con index",elemento_encontrado)