#Función simple
def saludar(nombre,sexo):
    sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    elif (sexo != "hombre"and sexo!= "mujer"):
        adjetivo = "cra"
    print(f'Hola {adjetivo}, cómo estas? {nombre}')
    
saludar("luis","cra")

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = int(num[0])
    c1 = num_entero -2
    c2 = num_entero
    c3 = num_entero -4
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}'
    print(contraseña)
    
crear_contraseña_random(98)

