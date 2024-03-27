#Creando diccionarios con dict() o como un .json de JS-> {'nombre':'Luis', 'apellido':'Pino'}
#Si queremos armar dicts vacios hay que hacerlos así - diccionario = dict()
#Si queremos crear tuplas vacías, no podemos al menos que hagamos tuplas = tuple() y lo mismo con List

diccionario = dict(nombre="Luis",apellido="Pino")
print(diccionario)
#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jaja"}#Esto me lo muestra porque las tuplas pueden ser claves
#print(diccionario)
#Pero si lo hacemos con lista, en vez de (), va [], no se puede porque no es hasheable. 

#Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)#esto así, muestra nombre como key porque itera el primer elemento, si ponemos entre corchetes, te lo separa 

diccionario_con_dosparametros = dict.fromkeys("ABDC","Prueba")
print(diccionario_con_dosparametros)