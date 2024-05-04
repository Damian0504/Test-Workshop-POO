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






