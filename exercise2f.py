from interpreter import draw
from chessPictures import *

table = square.join(square.negative()).horizontalRepeat(4)
table = table.up(table.negative()).verticalRepeat(2)

draw(table)

