'''
San Diego, 28 de junio de 2021
Universidad Jose Antonio Paez
Metodos Cuantitativos
Julio Gonzalez 28.195.303

Asignacion 1

Saludos cordiales profesor, le dejo el link del codigo en github por si acaso

https://github.com/GokoshiJr/metodos-cuantitativos/blob/master/3_Simulacion/ejercicios/proyecto.py

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

Datos:

Orientacion del Modelo: Este modelo es orientado a los procesos
Tipo de similacion: De modelo de tiempo discreto

Conclusion

A la hora de tener un sistema, nosotros usamos estrategias de simulacion, para realizar un muestreo
o estudio probabilistico de como se va a comportar nuestro sistema ante dichas entradas aleatorias,
esto con el fin de ahorrar recursos, ya que al simular estamos usando un modelo que en efecto es mucho 
más rentable en costos de operacion que los del modelo o sistema en la vida real, al evaluar las entradas
podemos observar si tenemos alguna falla en el sistema y corregirla, esto es una buena estrategia que
nos ahorra recursos, solo debemos programar el modelo y usar recursos computacionales.

'''

import math, random

class M_M_1: # eventos

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

  def get_ws(self):
    return (1 / (self.__miu - self.__lamb)) * 60

  def longitud_sistema(self): # Ls
    return self.__lamb / (self.__miu - self.__lamb)

  def longitud_cola(self): # Lq
    return self.__lamb / 60 * self.__wq

  def p_cliente_cola(self, n): # calcula la probabilidad de que haya n clientes en la cola
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

def main():

  # inicializacion

  linea = "-"*60
  lamb_total = 0
  miu_total  = 0
  ws_total   = 0
  estable    = 0

  print(linea)
  print("  Asignacion 1 - Julio Gonzalez 28.195.303")
  print(linea)
  print("  Datos Generales")
  print(linea)
  horas  = int(input("  Horas laborales que desea simular (horas): "))
  miu    = int(input("  Capacidad de atencion del sistema (clientes/hora): ")) # 150
  minimo = int(input("  Minimo de personas que llegan en promedio (clientes/hora): "))  # 100
  maximo = int(input("  Maximo de personas que llegan en promedio (clientes/hora): ")) # 150
  wq     = int(input("  Tiempo promedio de espera en la cola (minutos): ")) # 2 minutos
  print(linea)  

  for i in range (1, horas + 1): # tiempo

    servidor =  M_M_1(miu, maximo, minimo, wq, False) # eventos

    if (servidor.sistema_estable()):

      estable += 1
      lamb_total += servidor.get_lambda()
      miu_total += servidor.get_miu()
      ws_total += servidor.get_ws()

      print("\n\n\n")
      print(linea)
      print(f"  Datos Hora {i}")
      print(linea)
      print(f"  miu (velocidad de servicio, clientes/hora)= {servidor.get_miu():.2f}")
      print(f"  lambda (velocidad de llegadas, clientes/hora) = {servidor.get_lambda():.2f}")
      print(f"  Ws (tiempo en el sistema) = {servidor.get_ws():.2f} minutos")
      print(f"  Wq (tiempo en la cola) = {servidor.get_wq():.2f} minutos")
      print(f"  Ls (longitud del sistema) = {servidor.longitud_sistema():.2f} clientes")
      print(f"  Lq (longitud de la cola) = {servidor.longitud_cola():.2f} clientes")
      print(linea)
      print(f"  Resultados Hora {i}")
      print(linea)      
      print(f"  Sistema ocioso: {servidor.p_sistema_ocioso()*100:.2f} %") # a) probabilidad de que el sistema este ocioso
      print(f"  Sistema ocupado: {servidor.p_sistema_ocupado()*100:.2f} %") # b) probabilidad de que un cliente llegue y tenga que esperar      
      print(f"  Probabilidad de que un cliente llegue y espere: {servidor.p_cliente_cola(1)*100:.2f} %")
      print(f"  Probabilidad de tener 3 o menos clientes {servidor.p_cliente_cola_sumatoria(3)*100:.2f} %")
      print(f"  Probabilidad de tener mas de 10 clientes {(1 - servidor.p_cliente_cola_sumatoria(10))*100:.2f} %")      
      print(f"  Numero promedio de clientes en la cola {servidor.longitud_cola():.2f} personas") # c) cual es el numero promedio de clientes en la cola      
      print(f"  Probabilidad de tener 10 clientes en la cola: {servidor.p_cliente_cola(10)*100:.2f} %") # d) probabilidad de tener 10 clientes en la cola
      print(linea)
    else:
      print("  Error el sistema esta saturado - rho > 1")
      print(linea)
      break
  
  if (estable == horas): # informes
    print("\n\n\n")  
    print(linea)
    print(f"  Resultado del Modelo - Jornada de {horas} horas laborales")
    print(linea)
    print(f"  miu (velocidad de servicio, clientes/hora) = {miu_total / horas:.2f}")
    print(f"  lambda (velocidad de llegadas, clientes/hora) = {lamb_total / horas:.2f}")
    servidor_total = M_M_1(miu_total, 0, 0, wq, True, lamb_total)
    print(f"  Ws (tiempo en el sistema) = {ws_total / horas:.2f} minutos")
    print(f"  Wq (tiempo en la cola) = {servidor_total.get_wq():.2f} minutos")
    print(f"  Ls (longitud del sistema) = {servidor_total.longitud_sistema():.2f} clientes")
    print(f"  Lq (longitud de la cola) = {servidor_total.longitud_cola():.2f} clientes")
    print(f"  Sistema ocupado: {servidor_total.p_sistema_ocupado()*100:.2f} %")
    print(linea)

if __name__ == "__main__":
  main()