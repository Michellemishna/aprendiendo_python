#creando datos, el desempaquetamiento funciona en listas y tuplas
datos_tupla = ("Mich", "Maj", 100000)
datos_lista = ["Mich", "Maj", 100000]

#desempaquetando
nombre,apellido,cantidad = datos_tupla
nombre,apellido,cantidad = datos_lista

#mostrando resultado
print(nombre)
print(apellido)
print(cantidad)
