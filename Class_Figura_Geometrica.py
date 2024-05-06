import math
class Figuras_Geometricas:
  def __init__(self):
    pass

class Cuadrado(Figuras_Geometricas):
  
  def cuadrado(self, lado):
    area = lado ** 2
    perimetro = lado ** 4

    return area, perimetro

class Rectangulo(Figuras_Geometricas):

  def rectangulo(largo, ancho):
    area = largo * ancho
    perimetro = 2 * (largo + ancho)

    return area, perimetro

class Circulo(Figuras_Geometricas):

  def circulo(radio):
    area = math.pi * (radio ** 2)
    circunferencia = 2 * math.pi * radio

    return area, circunferencia

area_cuadrado, perimetro_cuadrado = Cuadrado(5)
print(f"Area del cuadrado: {area_cuadrado}, Perimetro del cuadrado: {perimetro_cuadrado}")

area_rectangulo, perimetro_rectangulo = Rectangulo(4, 7)
print(f"Area del rectangulo: {area_rectangulo}, Perimetro del rectaqngulo, {perimetro_rectangulo}")

area_circulo, circunferencia_circulo = Circulo(3)
print(f"Area del circulo: {area_circulo}, Circunferencia del circulo, {circunferencia_circulo}")