#creando un conjunto con set

conjunto = set(["dato1", "dato2"])

#metiendo un conjunro dentro de otro
conjunto = frozenset(["dato1","dato2"])
conjunto2 = {conjunto, "dato3"}
print(conjunto2)

#Teoria de conjuntos 
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
conjunto3 = {2,5,9}


#verificando si es un subconjunto, cualquiera de las 2 formas es valida
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1
print(resultado1, resultado2)

#verificando si es un supereconjunto, cualquiera de las 2 formas es valida
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto2 > conjunto1
print(resultado3, resultado4)

#verificando si hay un numero en común, da False si es así, si no hay numeros en comun dara True
resultado5 = conjunto3.isdisjoint(conjunto1)
print(resultado5)