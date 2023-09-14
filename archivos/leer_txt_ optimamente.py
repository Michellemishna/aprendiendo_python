#abre el archivo
with open("archivos\\Texto_archivo.txt", encoding="UTF-8") as archivo:
    
    #lee  el archivo
    contenido =archivo.read()
    
    #mostrar el archivo
    print(contenido)
    
    #no es necesario cerrarlo cuando se usa with open para abrirlo