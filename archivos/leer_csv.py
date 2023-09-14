import csv

with open("archivos\\datos.csv", encoding="UTF_8") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    
    for row in reader:
        print(row)
    