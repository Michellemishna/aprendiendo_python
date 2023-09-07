#creando diccionarios con dict() no se pueden crear diccionarios vacios asi {}, debe usar dict
diccionario = dict(nombre="Mich", apellido="Diaz")

{ 
 "nombre":"Mich", 
 "apellido":"Diaz"}

print(diccionario)

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1= {frozenset(["Mina", "Altea"]): "Hola"}
print(diccionario1)

#creando diccionarios con fromkeys, crea todas las claves que le agregamos a la lista pero con en valor asignado sera: "None"
diccionario2 = dict.fromkeys(["Nombre", "Apellido"])
print(diccionario2)

#creando diccionarios con fromkeys, itera el primer parametro por cada letra y le asigna como valor el segundo parametro es decir "N": "Apellido"
diccionario3 = dict.fromkeys("Nombre", "Apellido")
print(diccionario3)

#creando diccionarios con fromkeys, itera la lista le asigna como valor el segundo parametro es decir "N": "Apellido"
diccionario4 = dict.fromkeys(["Nombre", "Apellido"], "por asignar")
print(diccionario4)