#ejecisio 2
class Punto():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def eje_x(self):
        return self.x

  def eje_y(self):
        return self.y

  def impresion(self):
    print('('+str(self.x) + '(+ str(self.y)')

  def opuesto(self):
    return Punto(-self.x, -self.y)

class Punto_Diagonal(Punto):
  def __init__(self, x):
    self.super().__init__(x, x)
    self = Punto(x, x)

punto1 = Punto(3, 4)
print("Coordenada x:", punto1.eje_x())
print("Coordenada y:", punto1.eje_y())
print("Representación del punto:", punto1.impresion())
punto_opuesto = punto1.opuesto()
print("Punto opuesto:", punto_opuesto.impresion())

#ejercisio 3
class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def __str__(self):
        return f"Línea de {self._punto_a} a {self._punto_b}"



punto1 = Punto(1, 1)
punto2 = Punto(4, 5)
linea = Linea(punto1, punto2)
print("Línea original:", linea)
linea.mueve_derecha(2)
linea.mueve_arriba(3)
print("Línea movida:", linea)