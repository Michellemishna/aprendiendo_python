#DIR  es una funcion de python que devuelve la lista de atributos validos del objeto pasado. 
#metodos que se pueden hacer con un texto ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

cadena1 = "hola soy Mich 1"
cadena2= "Bienvenido"

print(dir(cadena1))

##DATO.nombre_del_metodo(parentesis)

#UPPER convierte en mayuscula
mayusc = cadena1.upper()
print(mayusc)

#LOWER convierte en minuscula
minusc = cadena1.lower()
print(minusc)

#CAPITALIZE todo lo convierte a minuzcula y deja la primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()
print(primera_letra_mayusc)

#FIND metodo encuentra la primera aparición del valor especificado, sino devuelve -1
busqueda_find = cadena1.find("a")
print(busqueda_find)

#INDEX metod enciuentra la primera aparición del valor especificado, sino devuelve una excepción
busqueda_index = cadena1.index("1")
print(busqueda_index)

#ISNUMERIC si es numerico devuelve true
si_es_numerico = cadena1.isnumeric()
print(si_es_numerico)

#ISALPHA si es alfanumerico devuelve true, sin espacio solo de a-z
cadena_alpha ="hola"
si_es_alfanumerico = cadena_alpha.isalpha()
print(si_es_alfanumerico)

#COUNT devuelve el numero de ocurrencias de una subcadena en la cadena dada
contar_coincidencias = cadena1.count("h")
print(contar_coincidencias)

#LEN es una funcion que cuenta los caracteres de una cadena
contar_caracteres=len(cadena1)
print(contar_caracteres)

#ENDSWITH verifica si una cadena comienza con 
comienza_con= cadena1.startswith("h")
print(comienza_con)

#STARTSWITH verifica si una cadena termina con
termina_con= cadena1.startswith("h")
print(termina_con)

#REPLACE remplaza un valor por otro
cadena_nueva =cadena1.replace("ola","ello")
print(cadena_nueva)

#SPLIt separa por el parametro dado
cadena_separada = cadena1.split(" ")
print(cadena_separada)
 