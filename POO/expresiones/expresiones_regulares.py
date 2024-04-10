#es el módulo que utilizamos para trabajar con expresiones regulares. 
import re

#Hay que encontrar coincidencia, para devolverla, remplazarla, usarla como separador, etc. 

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la 2 linea de texto
Y esta es la 3 final definitva, mi capitan
"""
#Con esto buscamos la coincidencia y la devolvemos
resultado = re.search("Hola",texto)
#Con esto buscamos todos los esta. Con flags re.IGNORECASE le decimos que ignore las mayusculas
resultado2 = re.findall("esta",texto, flags = re.IGNORECASE)

#\d -- Busca digitos números del 0 - 9
resultado = re.findall(r"\d",texto)
print(resultado)