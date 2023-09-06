#promedio de duración
otros_cursos_min= 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso= 1.5

#duracion de crudos
crudo_promedio= 5
crudo_dalto= 3.5

#Diferecnias de duracion
print("----------------------------------------------------------------")
diferencia_con_min =100 - (dalto_curso / otros_cursos_min) * 100
print(f'el curso de Dalto dura un {diferencia_con_min}% menos que el más rapido' )
diferencia_con_max = 100 - (dalto_curso *1000 //otros_cursos_max) /10
print(f'el curso de Dalto dura un {diferencia_con_max}% menos que el más lento')
diferencia_con_promedio =100 - (dalto_curso / otros_cursos_promedio) * 100
print(f'el curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio' )
print("----------------------------------------------------------------")

#calculando el tiempo vacio
tiempo_vacio_promedio =100 - (otros_cursos_promedio *1000 // crudo_promedio) / 10
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio' )
tiempo_vacio_Dalto =100 - (dalto_curso *1000 // crudo_dalto) / 10
print(f'Este curso promedio elimina un {tiempo_vacio_Dalto}% de tiempo vacio' )
print("----------------------------------------------------------------")

#Mostrando duferencia si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100//dalto_curso /10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100//otros_cursos_promedio /10} horas de este curso')
print("----------------------------------------------------------------")

