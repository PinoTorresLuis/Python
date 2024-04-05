#usando open para abrir un archivo con una codificación universal(UTF-8)
archivo_sin_leer = open('archivos\\prueba_test.txt', encoding='UTF-8')
# leer archivo completo
# archivo = archivo_sin_leer.read()

#Leer una sóla linea
#linea = archivo_sin_leer.readline()

#leer línea por línea
#lineas = archivo_sin_leer.readlines()
#print(lineas)
#ésta es la forma optima de abrir y cerrar un archivo
with open('archivos\\prueba_test.txt',encoding='UTF-8') as archivo:
    print(archivo.read())