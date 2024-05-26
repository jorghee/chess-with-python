from graphics.interpreter import draw
from graphics.chessPictures import *

squares = square.join(square.negative()).horizontalRepeat(4)
piecesPart = rock.join(knight).join(bishop)

# Part black
pieces = squares.under(piecesPart.join(queen).join(king).join(piecesPart).negative())
pawns = squares.under(pawn.horizontalRepeat(8)).negative()
partBlack = pieces.up(pawns)

# Part empty
tableEmpty = squares.up(squares.negative()).verticalRepeat(2)

# Part white
partWhite = pawns.up(pieces).negative()

# table
table = partBlack.up(tableEmpty).up(partWhite)

draw(table)

