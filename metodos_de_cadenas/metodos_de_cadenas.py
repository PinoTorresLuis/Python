#Ejemplo
cadena = "Hola,como,estas,todo,bien,guacho,piola"

#Count busca una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena.count("a")#acá le preguntamos cuántas veces está la letra A. Si no encuentra nada, responde 0 porque no apareció ni una vez
print("respuesta de count",busqueda_index)

#Len contamos cuantos caracteres tiene una cadena. LEN es una función, por eso se escribe primero y dentro del paramétro que queremos analizar
contar_caracteres = len(cadena)
print("respuesta de len",contar_caracteres)

#StarstWith verificamos si una cadena empieza con otra cadena dada. Si es así, devuelve TRUE
empieza_con = cadena.startswith("H")
print('respuesta de empieza con :', empieza_con)

#Endswith verificamos si una cadena TERMINA con otra cadena dada. Si es así, devuelve TRUE
termina_con = cadena.endswith("a")
print('respuesta de termina con :', termina_con)

#Replace reemplaza un pedazo de la cadena dada, por otra dada 
cadena_nueva = cadena.replace("H", "oooaaaaaaa")
print(cadena_nueva)

#Split separa cadenas con la cadena que le pasemos
cadena_separada = cadena.split(",")
print("respuesta de cadena_separada", cadena_separada)
print(type(cadena_separada))

print(dir(set(['asdadas','asdasdasd']))) #Nos muestra lo que se puede hacer en el conjunto: Sacar elementos de los conjuntos, removerlos pero no podemos agregar elementos. Por ejemplo, no podemos usar append o extend.
