#Creando bucle con While True / Except
def sumar_dos():
    #Pidiendo números
    while True:
        a = input("numero 1:")
        b = input("numero 2:")
        #Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b) 
        #Si lanzó una excepción, pedirle que reingrese los datos
        except:
            print("Por favor, ingresa números, no letras")
        #Si todo salió bien, terminamos el bucle
        else:
            break
        #También podemos agregar finally para que se ejecute siempre. Aunque no es común usarlo
        finally:
            print("Esto se ejecutaría siempre")
    #Retornamos el valor       
    return f'El resultado de tu suma es:{resultado}'
print(sumar_dos())

