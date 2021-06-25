""" 
Algortimo congruencial multiplicativo

Determinar los parametros:
a = constante multiplicativa
c = constante aditiva
m = modulo o periodo/ciclo de vida
X0 = semilla con D digitos

Sugerencia:
a = 3+8k o 5+8k k = 1,2,3,4,...
c = impar multiplo de m
m = 2^g, g = es un numero entero
X0 = debe ser impar
"""

class ACM:
  def __init__(self, semilla, c_multiplicativa, c_aditiva, modulo, cantidad_num):
    self.__semilla = semilla # X0 -> semilla con D digitos
    self.__c_multiplicativa = c_multiplicativa # a 
    self.__c_aditiva = c_aditiva # c
    self.__modulo = modulo # m -> modulo o periodo/ciclo de vida
    self.__cantidad_num = cantidad_num # cantidad de numeros a generar
    self.__num_1 = 0
    self.__num_2 = 0
    self.__array_num = []
    self.__array_num_modulo = []
  def generar(self):
    # Genera la secuencia de numeros
    for i in range (0, self.__cantidad_num):
      self.__num_1 = (self.__c_multiplicativa * self.__semilla + self.__c_aditiva) % self.__modulo
      self.__num_2 = self.__num_1 / (self.__modulo - 1)      
      self.__array_num.append(self.__num_1)
      self.__array_num_modulo.append(self.__num_2)
      self.__semilla = self.__num_1  
  def get_array_num(self):
    # Retorna el array normal de los numeros pseudo aleatorios
    return self.__array_num
  def get_array_num_modulo(self):
    # Retorna el array de los numeros en base al modulo - del 0 al 1
    return self.__array_num_modulo  
  def imprimir(self):
    # Imprime los datos generados
    for i in range (0, self.__cantidad_num):
      print(f"{i+1}. {self.__array_num[i]} ({self.__array_num_modulo[i]:.4f})")

''' 
Ejemplo:

Se desean obtener 16 números pseudo aleatorios usando el algoritmo congruencia multiplicativo:

Para obtener 16 se necesita que m = 64 
pues el período de vida máximo = m/4 o 64/4=16. 

Es decir, g=6 pues 2^6 = 64 (Modulo, periodo o ciclo de vida)
y el periodo de vida es de 2^6-2 = 2^4 = 16 (16 numeros a generar)
c = 0 (Constante Aditiva)
X0 debe ser impar, por lo que seleccionamos 15 (semilla)
a = 4 por lo que a = 3+8(4) = 35 (Constante multiplicativa)

tenemos:

test = ACM(semilla=15, c_multiplicativa=35, c_aditiva=0, modulo=64, cantidad_num=20)
'''
