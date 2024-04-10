#A la clase que estamos armando, le estamos heredando todas las propiedades de la clase Exception
class MiExcepcion(Exception):
    #constructor def __init__
    def __init__(self, err): #self va SIEMPRE y ponemos ERR, de error
            print(f'cometiste el siguiente erorr : {err}')

#Acá estamos probando la clase MiExcepcion            
try:
    #Con raise lanzas una excepción de forma forzada
    raise MiExcepcion("persona poca culta")
except:
    print("Cómo vas a cometer este error")       
           
    