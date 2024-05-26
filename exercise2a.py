from graphics.interpreter import draw
from graphics.chessPictures import *

table = knight.join(knight.negative())
table = table.up(table.negative())

draw(table)
