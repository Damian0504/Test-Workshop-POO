import math

def cuadrado(lado):
  area = lado ** 2
  perimetro = lado ** 4

  return area, perimetro

def rectangulo(largo, ancho):
  area = largo * ancho
  perimetro = 2 * (largo + ancho)

  return area, perimetro

def circulo(radio):
  area = math.pi * (radio ** 2)
  circunferencia = 2 * math.pi * radio

  return area, circunferencia

area_cuadrado, perimetro_cuadrado = cuadrado(5)
print(f"Area del cuadrado: {area_cuadrado}, Perimetro del cuadrado: {perimetro_cuadrado}")

area_rectangulo, perimetro_rectangulo = rectangulo(4, 7)
print(f"Area del rectangulo: {area_rectangulo}, Perimetro del rectaqngulo, {perimetro_rectangulo}")

area_circulo, circunferencia_circulo = circulo(3)
print(f"Area del circulo: {area_circulo}, Circunferencia del circulo, {circunferencia_circulo}")