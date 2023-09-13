archivo_sin_leer = open("archivos\\Texto_archivo.txt", encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()
#print(archivo)

#leer linea 1
#linea_1 = archivo_sin_leer.readline()
#print(linea_1)


#leer linea por linea
lineas = archivo_sin_leer.readlines()
print(lineas)

#cerrrar el archivo
archivo_sin_leer.close()
