numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x: x*2

print(multiplicar_por_dos(5))

#creando una funcion comun que diga si es par o no
def es_par(num):
    if(num%2 == 0):
        return True
    
#usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))

#creando lo mismo pero ahora usando la función lambda
numeros_pares1 = filter(lambda numero: numero%2 == 0, numeros)
print(list(numeros_pares1))