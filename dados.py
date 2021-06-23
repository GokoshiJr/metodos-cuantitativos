import random, math

""" 
Desarrolle un programa en el que simule el lanzamiento de al menos 2 Dados
y calcule cual es el numero que tiene mayor probabilidad de salir
"""

result = 0
indice = 0 # indice el num con mayor probabilidad
num_p = 0 # numero con mayor probabilidad
p = 0 # probabilidad
cantidad_dados = 2 # 3 dados
rango_numeros = 11 # 17 combinaciones para 3 dados
repeticiones = 100 # numero de lanzamientos
numeros = [0 for i in range(rango_numeros)]

class Lanzamiento:
  def __init__(self, cantidad):
    self.cantidad = cantidad
  def __lanzamiento(self):
    # Numero aleatorio del 1 al 6
    return (math.floor(random.random() * 6) + 1)
  def resultado(self):
    acum = 0
    for i in range(0, self.cantidad):
      acum += self.__lanzamiento() 
    return acum

for i in range (1, repeticiones):
  result = Lanzamiento(cantidad_dados).resultado()
  for j in range(0, repeticiones):
    if result == j + 2:
      numeros[j] += 1

print(f"\nResultados de {repeticiones} lanzamientos de {cantidad_dados} dados\n")

mayor_p = max(numeros)
for i in range(0, len(numeros)):
  p = numeros[i] / repeticiones
  if numeros[i] == mayor_p:
    print(f"{i+2} = {numeros[i]} - {p}% Mayor Probabilidad")
    num_p = numeros[i]
    indice = i+2  
  else:
    print(f"{i+2} = {numeros[i]} - {p}%")
print(f"\nResultado\n El Numero {indice} salio {num_p} veces - {numeros[indice-2]/repeticiones}% de probabilidad")  
  