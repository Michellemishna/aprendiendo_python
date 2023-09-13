#en este ejemplo respetamos el orden en que aparecen los parametros y asi se van a mostrar al pasarlo a print
def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante= frase("Michelle", "Díaz", "lista")
print (frase_resultante)

#en este ejemplo cambio el orden de los parametros especificando que parametro corresponde a qué Keyword
def frase2(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante= frase2(adjetivo="lista", apellido="Díaz", nombre="Michelle" )
print (frase_resultante)

#creando la misma funcion con un parametro opcional y un balor por defecto
def frase3(nombre, apellido, adjetivo = "ale"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante= frase3("Michelle", "Díaz","inteligente" )
print (frase_resultante)