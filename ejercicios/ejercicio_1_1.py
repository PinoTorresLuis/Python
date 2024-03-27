#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de Crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Ejercicio A
#Diferencia de duracion 1
#La división doble(//) me devuelve un valor entero.
diferencia_con_min = 100 -(dalto_curso * 1000 //  otros_cursos_min / 10)
#Diferencia de duracion 2
diferencia_con_max = 100 -  (dalto_curso *1000 // otros_cursos_max / 10)
#Diferencia de duracion 3
diferencia_con_cursos_promedio = 100 -  (dalto_curso *1000 //  otros_cursos_promedio / 10)
#Respuesta 1
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el curso más rápido")
#Respuesta 2
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el curso más lento")
#Respuesta 3
print(f"El curso de Dalto dura un {diferencia_con_cursos_promedio}% menos que los cursos promedio")

#Calculando el porcentaje del tiempo vacío promedio
#Ejercicio 1
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
#Ejercicio 2
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#Respuesta 1 de Diferencia vacio promedio
print(f'Un curso promedio elimina un {tiempo_vacio_promedio} de tiempo promedio')
#Respuesta 2 de Diferencia vacio promedio
print(f'Un curso promedio  de Dalto elimina un {tiempo_vacio_dalto} de tiempo promedio')

#Ejercicio 3
#Mostrando dferencia si los cursos duraran 10 horas
otros_cursos_10horas = otros_cursos_promedio * 100 // dalto_curso / 10
#Lo mismo pero al reves
otros_cursos_10hs_alreves = dalto_curso * 100 // otros_cursos_promedio /10
#Respuesta 1
print(f'Ver otros cursos promedio de 10hs equivale a {otros_cursos_10horas} del Curso de Dalto')
#Respuesta 2
print(f'Ver 10hs de otros cursos promedio equivale a {otros_cursos_10hs_alreves} del Curso de Dalto')
