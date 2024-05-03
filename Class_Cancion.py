#ejercisio 4

class Cancion():
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

  def get_titulo(self):
    self.titulo

  def get_autor(self):
    self.autor

  def set_titulo(self, nuevo_titulo):
    self.titulo = nuevo_titulo

  def set_autor(self, nuevo_autor):
    self.autor = nuevo_autor

cancion = Cancion("Blue skies", "Jamiroquai")
print("Titulo:", cancion.get_titulo())
print("Autor:", cancion.get_autor())

cancion.set_titulo("Dont Stop")
cancion.set_autor("The Rolling Stones")
print("Nuevo Titulo:", cancion.get_titulo())
print("Nuevo Autor:", cancion.get_autor())
