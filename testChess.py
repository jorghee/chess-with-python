from interpreter import draw
from chessPictures import *

# Ocurre un error en tiempo de ejecución
# draw(king.join(queen).under(square))

# Solución no esperada, king.join.(queen) se recorta
draw(square.under(king.join(queen)))
