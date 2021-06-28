""" 
Estimacion del valor del numero pi 

Consiste en un experimento para estimar el valor del número π. 

Si se lanza una aguja de longitud l sobre una mesa pintada con líneas paralelas, 
con un espaciado entre ellas d (donde d ≥ l), entonces la
probabilidad de que la aguja corte una línea es:

p = 2.l / pi.d
"""

import random, math

linea = "-"*35
Ncorta = 0 # numero de veces que la aguja corta o toca la linea 
n = 0 # numero de lanzamientos que no tocan la linea
# se debe cumplir d >= l
l = 10 # longitud de la aguja
d = 20 # espaciado entre las lineas paralelas de la mesa
Ntotal = 3000 # numero total de intentos

for i in range (0, Ntotal):
  num_1 = random.random() 
  num_2 = random.random()  
  a = (d/2) * num_1 # distancia del punto medio de la aguja a la linea mas cercana
  theta = math.pi * num_2 # angulo que forma respecto a las lineas paralelas
  if a > ((l/2) * math.sin(theta)):
    n +=1
  else:
    Ncorta += 1

num_pi = (2*l) / ((Ncorta/Ntotal) * d)

print(linea)
print(f"  Estimacion del numero pi")
print(linea)
print(f"  Probabilidad de que la aguja toque la linea: \n  {Ncorta/Ntotal}%")
print(linea)
print(f"  pi ~ {num_pi}")
print(linea)
print(f"  Numero de aciertos: {Ncorta} \n  Numero de desaciertos: {n}")
print(linea)