import tron
import sys
import random

lastDir = None

def debug(msg):
    sys.stderr.write(str(msg)+"\n")

def debug_move(direction):
    if direction == tron.NORTH:
        debug("Moving North")
    elif direction == tron.SOUTH:
        debug("Moving South")
    elif direction == tron.EAST:
        debug("Moving East")
    elif direction == tron.WEST:
            debug("Moving West")

class TronPlayer(object):
    def __init__(self):
        self.lastDirection = None

    def pickStrategy(self, board):
        pass

    def genMove(self, board):
        if self.lastDirection is not None \
                and board.passable(board.rel(self.lastDirection)):
            debug_move(self.lastDirection)
            return self.lastDirection

        newDirection = random.choice(board.moves())
        self.lastDirection = newDirection
        debug_move(newDirection)
        return newDirection

tronguy = TronPlayer()
# you do not need to modify this part
for board in tron.Board.generate():
    tron.move(tronguy.genMove(board))
