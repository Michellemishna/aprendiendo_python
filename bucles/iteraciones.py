frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena ="Hola"
numeros = [2,5,8,10]

#evitando la condicion de manzana usando el continue ( si usas else en el for no se va a ejecutar si se encuentra despues de un break)
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f'Me voy a comer una {fruta}')
    
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == "pera":
        break
    
print("fin del bucle")

for letra in cadena: 
    print(letra)

#for en una sola linea de codigo el primer codigo es igual al segundo apartir de esta linea, solo que mas corto
numeros_duplicados = list()
for numero in numeros: 
    numeros_duplicados.append(numero*2)
    
print(numeros_duplicados)

numeros_duplicados2 = [numero*2 for numero in numeros]
print(numeros_duplicados2)
