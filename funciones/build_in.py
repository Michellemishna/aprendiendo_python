#Funciones integradas, los valores deben ser numeros para que funcionen
numeros = [4,7,1]

#encontrando el numero mayor de la lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de la lista
numero_mas_pequeño = min(numeros)
print(numero_mas_pequeño)

#redondeando a 3 decimales, primero recibe el numero a cambiar, el segundo es la cantidad de decimales que quiero que muestre
numero = round(12.345678,3)
print(numero)

#retorna False -> 0, vacio, False, None \ True -> distinto a 0, True, Cadena, datos no vacio 
resultado_bool= bool(0)
print(resultado_bool)

#retorna True si todos los parametros son verdaderos
resultado_all = all([234,"hola", "True", [344,23]])
print(resultado_all)

resultado_all = all([234,"", "True", [344,23]]) #ejemplo si es falso alguno
print(resultado_all)

#suma todos los valores de un iterable
suma_total= sum(numeros)
print(suma_total)
