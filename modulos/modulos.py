#Solamente se importa el nombre del archivo, sin la extensión .py
#import modulo_saludar as m_saludar Esto es un objeto name space ->nombre del módulo

#Para llamarlos vamos a hacerlo como si fuesen métodos. Un método es una función aplicada a un objeto

#La mayoría de las cosas en python no la vamos a crear nosotros, tenemos que usar varios módulos de librerias externas
#saludo = m_saludar.saludar('Luis')
#print(saludo)

#Tenemos un operador AS que funciona para asignar u nuevo nombre, de esa forma podemos abreviarla a nuestro gusto

#Ejemplo: import modulo_saludar as m_saludar

#Con from extraemos directamente la función que queremos utilizar de otro módulo. Si quiero traer más de una FN de un módulo, utilizo la ","
#Ejemplo: from modulo_saludar import saludar,otro_saludo

#También podemos importar las funciones y cambiarle los nombres
#Ejemplo: from modulo_saludar import saludar as saludo_normal , otro_saludo as otro_nuevo_saludo

#si quiero ver las propiedades y métodos de el namespace:
#print(dir(modulo_saludar))

#Si el  módulo está en una misma carpeta, se importa así
import modulos.paquetes.saludar as m_saludo
print(m_saludo.saludar("Luisito"))

#Si el módulo está en una carpeta afuera, se importa así
#import sys 

