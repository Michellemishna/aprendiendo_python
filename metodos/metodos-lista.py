#DIR  es una funcion de python que devuelve la lista de atributos validos del objeto pasado.
#metodos que sirven con una lista: ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#LIST crea una lista
lista = list(["hola", "Mich", 30])
print (dir(lista))

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


#en tupla solo se puede usar el index y buscar elementos
#en conjuntos solo se puede agregar remover elementos