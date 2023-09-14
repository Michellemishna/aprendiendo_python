#abre el archivo
with open("archivos\\Texto_archivo.txt","w", encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("agregando un texto a un archivo")
    #sobreescribiendo el archivo agregando en forma de lista, agregando 2 lineas 
    archivo.writelines(["Hola Maestro\n", "¿Cómo andas?\n"])
    
    #sobreescribiendo el archivo agregando en forma de lista, agregando 2 lineas mas
    archivo.writelines(["Hola de nuevo\n", "¿Que pasa?"])
#print(archivo)
