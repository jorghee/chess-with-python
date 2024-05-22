from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  # Iterando desde el último elemento de la listas hacia el primer elmemento
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    size = len(self.img)
    horizontal = []
    for value in range(size):
      horizontal.append(self.img[size - 1 - value])
    return Picture(horizontal)

  # Usamos el método _invColor() para cambiar el caracter
  def negative(self):
    """ Devuelve un negativo de la imagen """
    inverter = []
    for value in self.img:
      inverter.append(self._invColor(caracter) for caracter in value)
    return Picture(inverter)

  # Usamos el operador '+' para concatenar los strings
  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = []
    for i in range(len(self.img)):
      join.append(self.img[i] + p.img[i])
    return Picture(join)

  # Usamos los operadores de destructuración  propios de la sintaxis de python
  def up(self, p):
    up = [*self.img, *p.img]
    return Picture(up)

  # Las dos imagenes deben ser del mismo tamaño, si la imagen como argumento es más grande
  # se recorta a la imagen actual y de lo contrario, ocurre un error.
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    under = []
    for i in range(len(self.img)):
      under.append(self.newString(self.img[i], p.img[i]))
    return Picture(under)
  
  # Funcion que itera por cada caracter
  def newString(self, s, p):
    string = ""
    for i in range(len(s)):
      if p[i] == " ":
        string += s[i]
      else:
        string += p[i]
    return string

  # Usando el operador multiplicador '*' para generar el elemento cuantas veces queramos
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    horizontal = []
    for value in self.img:
      horizontal.append(value * n)
      # print(value * n)
    return Picture(horizontal)

  # Usando destructuración de listas
  def verticalRepeat(self, n):
    vertical = []
    for value in range(n):
      vertical = [*vertical, *self.img]
    return Picture(vertical)

  # Extra: Sólo para realmente viciosos
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

