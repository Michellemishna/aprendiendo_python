#creando una funcion que nos devuelva los numeros primos entre 0 y el argumento que pasamos

def numeros_es_primo(num):
    for i in range(2,num-1):
        if num%i == 0: return False
    return True

resultado = numeros_es_primo(7)
print(resultado)

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado= numeros_es_primo(i)
        if resultado == True : primos.append(i)
    return primos

resultado = primos_hasta(13)
print(resultado)
