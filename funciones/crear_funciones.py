#creando una funcion simple
def saludar():
    print("hola")
    
#crear funcion con parametros
def saludo(nombre, sexo):
    sexo= sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'maestra'
    elif sexo == 'hombre':
        adjetivo = 'maestro'
    else: adjetivo = "crack"
    
    print(f"Hola {nombre} Cómo estas {adjetivo}?")
    
saludo("Lucas", "Hombre")
saludo("Dana", "mujer")
saludo("Daniel", "ni binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
password =crear_contraseña_random(98)
frase = f"Tu contraseña nueva es: {password}"
print(frase)