#maneras de importar una funcion : 

#import modulo_saludar

#saludo = modulo_saludar.saludar("Michelle")
#print(saludo)

#la funcion saludar se importa normal y la segunda es un ejemplo para ver que se puede cambiar el nombre de la función al importarla
from modulo_saludar import saludar, saludar_raro as saludar_coscu

saludo = saludar("Michelle")
saludo2 = saludar_coscu("Michelle")

print(saludo)
print(saludo2)