#LIST crea una lista
lista = list(["hola", "Mich", 30])
print (lista)

#LEN  cuenta la cantidad de elementos de una lista
resultado = len(lista)
print (resultado)

#APPEND agrega un elemento a una lista 
lista.append("jijiji")
print (lista)

#INSERT agrega un elemento a la lista en el indice especificado
lista.insert(2,"jijiji")
print(lista)

#EXPEND agrega varios elementos a la lista
lista.extend(["a", "b", "c",27])
print(lista)

#POP elimina un elemento de una lista, pide indice y devuelve valor (para eliminar el ultimo es pasando como parametro el -1, -2 es el penultimo y asi susesivamente)
lista.pop(2)
print(lista)

#REMOVE remueve un elemento de una lista, pide valor
lista.remove("a")
print(lista)

#SORT ordena una lista de form ascendente a descendente
lista2 = [1,2,3,4,5,6,7,4,5,3, False, False, False, True, True, True, True]
lista2.sort()
print(lista2)

#REVERSE invierte los elementos de una lista
lista2.reverse()
print(lista2)

#CLEAR elimina todos los elementos de una lista
lista.clear()
print(lista)
