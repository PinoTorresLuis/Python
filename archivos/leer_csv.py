import csv

with open('archivos\\prueba_csv.txt',encoding='UTF-8') as archivo:
    reader = csv.reader(archivo)
    #me devuelve listas con las filas
    #nos deja un espacio "" es como un 4to valor, es por si le dejamos la coma, que es por como separa el programa
    for row in reader:
        print(row)
    