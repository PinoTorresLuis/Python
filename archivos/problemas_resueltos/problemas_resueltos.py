#Creando 2 listas, una con nombres y otra con apellidos
nombres = ["luis","sol","rukia","lua","roberto"]
apellidos = ["pino","autiero","luna","torres"]

#Registrar esta información en un txt de forma optima
with open("nombres_y_apellidos.txt","w") as archivo : 
    archivo.writelines("Los datos son : \n\n")
    #La forma para que esto funcione tiene que sí o si ir entre corchetes
    [archivo.writelines(f'Nombre:{n}\nApellido:{a}\n -------------\n') for n,a in zip(nombres,apellidos)]