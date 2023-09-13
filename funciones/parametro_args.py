#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados= numeros_sumados + numero
    return numeros_sumados
  
resultado = suma([5,3,9,10,20])
print (resultado)

#forma optima de realizar una suma usando el parametro args, si usamos * debe ser en el ultimo parametro no antes, sino no funcionaría
def suma_optima(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma_optima("Mimi",5,3,9,10,20)
print (resultado)
