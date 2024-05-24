from interpreter import draw
from chessPictures import *

table = knight.join(knight.negative())
table = table.up(table.negative())

draw(table)
