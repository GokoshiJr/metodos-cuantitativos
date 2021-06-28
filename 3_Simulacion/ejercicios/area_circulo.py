""" 
Simulacion Monte Carlo - Integracion con simulacion

Calcule el area de un circulo que esta dentro de un cuadrado de area 1

En la que hacemos lanzamientos de dardos al area del circulo

Ejemplo
Area del cuadrado = 1
Area teorica del circulo = 0.7853982 
"""

import random, math

ensayos = 1000000
area_cuadrado = 2
distancia = 0
aciertos = 0
area_circulo = 0
linea = "-"*35

for i in range(1, ensayos):
  # generacion de coord aleatorias donde impactan los dardos
  x = random.random() 
  y = random.random()
  # Calculamos la distancia donde cayo el dardo con el origen del circulo
  distancia = math.sqrt(math.pow(x - 0.5, 2) + math.pow(y - 0.5, 2))
  # Si el dardo cayo dentro del area del circulo sumamos +1
  if distancia < 0.5:
    aciertos += 1

area_circulo = (aciertos / ensayos) * area_cuadrado
print(linea)
print("  Simulacion Monte Carlo")
print(linea)
print(f"  Lanzando {ensayos} dardos \n  en un cuadro de area {area_cuadrado} cm^2")
print(f"  Dardos acertados {aciertos}")
print(linea)
print(f"  El area estimada del circulo es: \n  {area_circulo} cm^2")
print(linea)