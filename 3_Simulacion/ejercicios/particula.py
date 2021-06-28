'''
 Movimiento de una particula

Una particula se mueve en un circulo dividido marcado con los numeros
0,1,2,...,7. Su posicion inicial es 0. En todo punto dara un paso adyacente
con igual probabilidad.

¿Cual es el numero medio de pasos para volver al inicio?
¿Cual es la probabilidad de volver al inicio en dos pasos?

Hallar datos estadisticos basicos: media, desviacion, valor minimo, valor maximo 
'''

import random, math

salir = False
salir_general = 0
inicio = 0
paso_1 = 0
salir_en_dos_pasos = 0
pasos = 0

while (salir_general != 15):
  inicio = math.floor(random.random() * 8)
  if (inicio != 0):
    while not(salir):
      paso_1 = math.floor(random.random() * 8)
      if paso_1 == 0:
        if pasos == 0:
          salir_en_dos_pasos += 1
          salir = True
          print("Salio en dos pasos")
        else:
          print(pasos)
          salir = True
      pasos += 1
  else:
    salir_general -= 1
  salir = False
  salir_general += 1
  pasos = 0

print(f"Se realizaron {pasos} - {salir_general} intentos")
