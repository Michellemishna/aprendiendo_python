diccionario= {
    'nombre': "Mich",
    'canal': "Canal",
    'emocionado': True,
    'altura': 100000,
}

#KEYS  devuelven las claves, tambien para iterar
claves = diccionario.keys()
print(claves)

#GET devuelve el valor de una clave
obtener = diccionario.get('canal')
print(obtener)

#POP elimina un elemento
diccionario.pop("emocionado","altura")
print(diccionario)

#ITEMS para iterar el dict (diccionario)
diccionario_iterable = diccionario.items()
print(diccionario_iterable) 

#CLEAR elimina todos los elementos
#diccionario.clear()
#print(diccionario)

