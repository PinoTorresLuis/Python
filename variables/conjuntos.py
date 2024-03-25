#Podemos crearlo con set. Necesita como dato, algo iterable. Estos no son modificables
conjunto = set(["Dato1", "Dato2"])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset (["Dato 1", "Dato 2"])#Con la fn frozen creo un conjunto inmutable y que puede estar congelado para que sea hasheable. De esta forma puedo meter un conjunto dentro de otro conjunto.
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)