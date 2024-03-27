#Podemos crearlo con set. Necesita como dato, algo iterable. Estos no son modificables
conjunto = set(["Dato1", "Dato2"])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset (["Dato 1", "Dato 2"])#Con la fn frozen creo un conjunto inmutable y que puede estar congelado para que sea hasheable. De esta forma puedo meter un conjunto dentro de otro conjunto.
conjunto2 = {conjunto1, "dato 3"} #Sin frozenset no podría hacer esto
print(conjunto2)

#Teoría de Conjuntos
conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}
#Cómo sabemos si un conjunto es un subconjunto de otro conjunto?
resultado = conjunto3.issubset(conjunto4)
#print(resultado)#La respuesta es False. Si lo hacemos al reves, nos devuelve true
resultadoSimilar = conjunto3 <= conjunto4 #Es lo mismo que escribir .issuperset()

resultadoSuperConjunto = conjunto3 > conjunto4
print(resultadoSuperConjunto)

#Verificar si hay algún número en común
resultado = conjunto3.isdisjoint(conjunto3) #Esto SÓLAMENTE me va a devolver TRUE si en la comparación de conjuntos no se repite ningún número