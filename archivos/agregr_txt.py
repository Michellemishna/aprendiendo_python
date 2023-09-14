#abre el archivo
with open("archivos\\Texto_archivo.txt","a", encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("agregando un texto a un archivo")
    # usando un bucle para agregar varias lineas 
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada.\n")
   
#print(archivo)