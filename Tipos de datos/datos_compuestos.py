#son datos que se componen de otros datos compuestos o simples

#creando una lista (se pueden modificar)
lista = ["Mich", "soy", True, 1.60]

#creando una tupla (no se pueden modificar, si sep uede redefinir)
#si se puede acceder por su indice y almacena valores repetidos (si agregas uno repetido lo mostrara)

tupla= ("Mich", "soy", True, 1.60)

#esto es valido
lista[3]="maquina"

#esto no se puede hacer
#tupla[3]= "maquina"

print(lista)

#creando un conjunto set
conjunto = {"Mich", "soy", True, 1.60}

#el conjunto se puede redefinir pero no modificar sus elementos, 
#tampoco se puede acceder por su indice ni almacena valores repetidos ( si agregas uno repetido no lo mostrara)
#esto no se puede
#conjunto[3]="maquina"

#esto si es valido
conjunto={"maquina"}


#creando un diccionario (dict)

diccionario= {
    'nombre': "Mich",
    'canal': "Canal",
    'emociado': True,
    'altura': 1.60,
    'dato_duplicado': "Canal"
}

print(diccionario['nombre'])