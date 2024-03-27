#Bucle for
animales = ["perro","gato","loro","zorro"]
for animal in animales:
    print(f'Ahora la variables es igual a : {animal}')

numeros = [20,5,10,40,50]
for numero in numeros:
    resultado = numero *2
    print(f'El valor del resultado es :{resultado}')
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    #num es = a una tupla
    indice = num[0]
    valor = num[1]
    print(f'El indice es:{indice} y su valor es: {valor}')     
     