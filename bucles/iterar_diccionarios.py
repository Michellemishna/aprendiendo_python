diccionario = {
     "nombre":"Mich", 
 "apellido":"Diaz",
 "numero": 2000
}
#recorriendo el diccionario obteniendo sola la clave
for key in diccionario:
    print(key)

#recorriendo el diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key}, y su valor es: {value}')