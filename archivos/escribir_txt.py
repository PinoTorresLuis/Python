#.w (significa que le da permiso de escritura, va como 2do parametro y si no encuentra el archivo, lo crea y te sobreescribe la información que había)
#Tambien tenemos append, que se utiliza para agregar una nueva cadena de texto y se pone , 'a'
with open('archivos\\prueba_test.txt','w', encoding='UTF-8') as archivo:
    #sobreescribiendo el archivo
    archivo.write('escribiendo desde python con write parte II')
    #arc