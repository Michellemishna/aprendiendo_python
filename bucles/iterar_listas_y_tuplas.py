#el bucle for funciona con listas [] y tuplas ()
animales = [ "gato", "perro", "loro", "cocodrilo", "pez" ]
numeros = [52,32,16,72, 12]

for animal in animales: 
    print(f'Ahora la variable animal es: {animal}')
    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#se pueden iterar dos o mas listas a la vez, solo es necesario que ambas tengan el mismo numero de elementos
for numero,animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')
    
#aca itera un rango de numeros iniciando con el primer numero dado y terminando antes de llegar al segundo parametro 
#si le paso solo un parametro va a comenzar desde 0 y termina antes de llegar al numero dado
for num in range(5,10):
    print(num)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice= num[0]
    valor =num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')