#Problema
frase = input ("Decime una frase y te calculo cuánto tardarías si tuvieras que decirlo :")
#Respuesta
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} de palabras y tardarías {cantidad_de_palabras /2} segundos en decirlas')

if cantidad_de_palabras >= 120 :
    print(f'para flaco, no te pedi un testamento')
elif cantidad_de_palabras <= 60 :
    print(f'Flaco, podrías esforzarte un poco más')
else :
    print("Lo estás haciendo muy bien")
    
         

