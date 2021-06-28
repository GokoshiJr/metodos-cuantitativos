""" 
Problemario - Ejercicio 5.2

Utilice el método congruencial mixto para generar las siguientes sucesiones de nº aleatorios.
a) Una sucesión de 10 n.a. enteros de un dígito tal que ( )(3 )10 X 1 X módulo n + = n + y X0=2.
b) Una sucesión de 8 n.a. enteros entre 0 y 7 de un dígito tal que 5( )(1 )8 X 1 X módulo n + = n +
y X0=1.
c) Una sucesión de 5 n.a. enteros de un dígito tal que 61( )(27 100) X 1 X módulo n + = n + y
X0=100.
"""

from algoritmo_congruencial import ACM

linea = "-"*25

# a)
print(linea)
print("  a)")
print(linea)
a = ACM(semilla=2, c_multiplicativa=1, c_aditiva=3, modulo=10, cantidad_num=10)
a.generar()
a.imprimir()

# b)
print(linea)
print("  b)")
print(linea)
b = ACM(semilla=1, c_multiplicativa=5, c_aditiva=1, modulo=8, cantidad_num=8)
b.generar()
b.imprimir()

# c)
print(linea)
print("  c)")
print(linea)
c = ACM(semilla=100, c_multiplicativa=61, c_aditiva=27, modulo=100, cantidad_num=5)
c.generar()
c.imprimir()