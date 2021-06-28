'''
San Diego, 28 de junio de 2021
Universidad Jose Antonio Paez
Metodos Cuantitativos
Julio Gonzalez 28.195.303

Asignacion 1

Simulando el ejercicio 2 del problemario de teoria de colas (unidad 1)

Suponga un restaurante de comidas rápidas al cual llegan en promedio 100 clientes
por hora. Se !ene capacidad para atender en promedio a 150 clientes por hora Se sabe
que los clientes esperan en promedio 2 minutos en la cola Calcule las medidas de
desempeño del sistema

a) ¿Cuál es la probabilidad que el sistema este ocioso?
b) ¿Cuál es la probabilidad que un cliente llegue y tenga que esperar, porque el
sistema está ocupado?
c) ¿Cuál es el número promedio de clientes en la cola?
d) ¿Cuál es la probabilidad que hayan 10 clientes en la cola?

'''

import math, random

# Modelo orientado a los procesos
# De modelo de tiempo discreto

class M_M_1:

  def __init__(self, miu, maximo, minimo, wq, total, lamb=0):
    if total == True:
      self.__lamb = lamb
    else:
      self.__lamb = math.floor(random.random() * (maximo - minimo + 1) + minimo)
    self.__miu  = miu
    self.__wq   = wq 

  def get_lambda(self):
    return self.__lamb

  def get_miu(self):
    return self.__miu

  def get_wq(self):
    return self.__wq

  def get_ws(self): # ws
    return (1 / (self.__miu - self.__lamb)) * 60

  def longitud_sistema(self): # Ls
    return self.__lamb / (self.__miu - self.__lamb)

  def longitud_cola(self): # Lq
    return self.__lamb / 60 * self.__wq

  def p_cliente_cola(self, n): # Calcula la probabilidad de que haya n clientes en la cola
    return (1 - (self.__lamb / self.__miu)) * math.pow((self.__lamb / self.__miu), n)

  def p_cliente_cola_sumatoria(self, n): # probabilidad de que haya al menos n clientes en la cola
    acum = 0
    for i in range(0, n + 1):      
      acum += (1 - (self.__lamb / self.__miu)) * math.pow((self.__lamb / self.__miu), i)
    return acum

  def p_sistema_ocupado(self): # probabilidad de que el sistema esta ocupado
    return self.__lamb / self.__miu

  def p_sistema_ocioso(self): # probabilidad de que el sistema esta ocioso
    return (1 - self.p_sistema_ocupado())

  def sistema_estable(self): # calcula que el sistema sea estable para operar con el
    if (self.p_sistema_ocupado() < 1): # condicion de no saturacion
      return True
    else:
      return False


if __name__ == '__main__':

  linea = "-"*50
  print(linea)
  print("  Asignacion 1 - Julio Gonzalez 28.195.303")
  print(linea)
  print("  Datos Generales")
  print(linea)
  miu    = int(input("  Capacidad de atencion del sistema: ")) # 150
  minimo = int(input("  Minimo de personas que llegan en promedio: "))  # 100
  maximo = int(input("  Maximo de personas que llegan en promedio: ")) # 150
  wq     = int(input("  Tiempo promedio de espera en la cola (minutos): ")) # 2 minutos
  print("  Se realizara la simulacion 8 veces, \n  para simular el resultado de 8 horas laborales de nuestro restaurante")

  lamb_total = 0
  miu_total = 0

  for i in range (1, 9):

    servidor =  M_M_1(miu, maximo, minimo, wq, False)

    if (servidor.sistema_estable()):

      lamb_total += servidor.get_lambda()
      miu_total += servidor.get_miu()

      print(linea)
      print(f"  Datos Hora {i}")
      print(linea)
      print(f"  lambda = {servidor.get_lambda():.2f}")
      print(f"  miu = {servidor.get_miu():.2f}")
      print(f"  Ws = {servidor.get_ws():.2f} minutos")
      print(f"  Wq = {servidor.get_wq():.2f} minutos")
      print(f"  Ls = {servidor.longitud_sistema():.2f} clientes")
      print(f"  Lq = {servidor.longitud_cola():.2f} clientes")
      print(linea)
      print(f"  Resultados Hora {i}")
      print(linea)
      # a) probabilidad de que el sistema este ocioso
      print(f"  Sistema ocioso: {servidor.p_sistema_ocioso()*100:.2f} %")
      print(f"  Sistema ocupado: {servidor.p_sistema_ocupado()*100:.2f} %")
      # b) probabilidad de que un cliente llegue y tenga que esperar
      print(f"  Probabilidad de que un cliente llegue y espere: {servidor.p_cliente_cola(1)*100:.2f} %")
      print(f"  Probabilidad de tener 3 o menos clientes {servidor.p_cliente_cola_sumatoria(3)*100:.2f} %")
      print(f"  Probabilidad de tener mas de 10 clientes {(1 - servidor.p_cliente_cola_sumatoria(10))*100:.2f} %")
      # c) cual es el numero promedio de clientes en la cola
      print(f"  Numero promedio de clientes en la cola {servidor.longitud_cola():.2f} personas")
      # d) probabilidad de tener 10 clientes en la cola
      print(f"  Probabilidad de tener 10 clientes en la cola: {servidor.p_cliente_cola(10)*100:.2f} %")
    else:
      print("  error el sistema esta saturado")
      
  print(linea)
  print("  Resultados Finales y  Probabilidades - 8 horas laborales")
  print(linea)
  print(f"  miu promedio de 8 horas = {miu_total / 8}")
  print(f"  lambda promedio de 8 horas = {lamb_total / 8}")
  servidor_total = M_M_1(miu_total, 0, 0, wq, True, lamb_total)
  print(f"  Ws = {servidor_total.get_ws():.2f} minutos")
  print(f"  Wq = {servidor_total.get_wq():.2f} minutos")
  print(f"  Ls = {servidor_total.longitud_sistema():.2f} clientes")
  print(f"  Lq = {servidor_total.longitud_cola():.2f} clientes")
  print(linea)
  print(f"  Resultados")
  print(linea)
  # a) probabilidad de que el sistema este ocioso
  print(f"  Sistema ocioso: {servidor_total.p_sistema_ocioso()*100:.2f} %")
  print(f"  Sistema ocupado: {servidor_total.p_sistema_ocupado()*100:.2f} %")
  # b) probabilidad de que un cliente llegue y tenga que esperar
  print(f"  Probabilidad de que un cliente llegue y espere: {servidor_total.p_cliente_cola(1)*100:.2f} %")
  print(f"  Probabilidad de tener 3 o menos clientes {servidor_total.p_cliente_cola_sumatoria(3)*100:.2f} %")
  print(f"  Probabilidad de tener mas de 10 clientes {(1 - servidor_total.p_cliente_cola_sumatoria(10))*100:.2f} %")
  # c) cual es el numero promedio de clientes en la cola
  print(f"  Numero promedio de clientes en la cola {servidor_total.longitud_cola():.2f} personas")
  # d) probabilidad de tener 10 clientes en la cola
  print(f"  Probabilidad de tener 10 clientes en la cola: {servidor_total.p_cliente_cola(10)*100:.2f} %")
  

''' Elaborar un programa Python modular parametrizado que permita simular procesos y evaluar los resultados obtenidos. Debe cumplir con los siguientes requisitos:

Identificar la Orientación del Modelo:
A los eventos
A los procesos.
Identificar el tipo de Simulación:
De modelos de tiempo discreto
Orientada a los intervalos
Incluir las Rutinas Básicas de Simulación:
Inicialización.
Tiempo.
Eventos.
Informes.
Simular y evaluar los resultados obtenidos para alguna de las situaciones planteadas en los problemas del Problemario de Teoría de Líneas de Espera (Unidad I).
Código del modelo, enunciado del problema a simular, resultados y conclusiones obtenidas.
Todo guardado en un archivo Word debidamente identificado.
NOTA:
Dos o más respuestas iguales o parecidas les será dividida la nota entre la cantidad de asignaciones en esa situación.
Tamaño máximo permitido: 5 Mb.
Debe tenerla lista para el día del Tercer Parcial cuando le será requerida '''