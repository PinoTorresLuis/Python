#definiendo funciones. Es importante tener en cuenta el identado
def saludar (nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else: 
        adjetivo = "amor"
    print (f'Hola {nombre}, un gusto saludarte {adjetivo}')
        
saludar("Luis","hombre")


def saludarDos(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        respuesta = "reina"
    elif(sexo == "hombre"):
        respuesta = "titan"
    else:
        respuesta = "NN"
        print(f'Hola {nombre}, cómo estas, gracias por venir')
        
saludar("NN","hombre")
print(saludar)