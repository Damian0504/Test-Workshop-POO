class Cuenta_bancaria:
  def __init__ (self, nombre, saldo):
    self.nombre = nombre
    self.saldo = saldo

  def extraer(self, cantidad):
    if cantidad <= self.saldo:
      self.saldo = cantidad
      return cantidad
    else:
      return "Saldo insuficiente"

  def reset_saldo(self):
    self.saldo = 0

  def datos_saldo(self):
        return f"Nombre: {self.nombre}, Saldo: {self.saldo}"

felipe_morales = Cuenta_bancaria("Felipe morales", 100000)
felipe_morales = Cuenta_bancaria("Felipe morales", 900000)

cantidad_extraida = felipe_morales.extraer(100000)
cantidad_extraida = felipe_morales.extraer(900000)

print(f"Se extrajo {cantidad_extraida}")






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