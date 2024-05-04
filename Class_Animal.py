class Animal:
  def __init__ (self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def hablar(self):
     print('Soy ' + self.nombre + ' y digo ' + self.texto_hablar)
  def edad(self):
     print('soy' + self.nombre + 'y tengo' + self.edad)
class Perro(Animal):
    texto_hablar = '¡Guau!'

class Gato(Animal):
    texto_hablar = 'Miauu'

class Raton(Animal):
    texto_hablar = 'fuck'

animales = [Perro('Spike', 10), Gato('Tom',6), Raton('Jerry', 3)]
for animal in animales:
    animal.hablar()