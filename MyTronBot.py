import tron
import sys
import random

lastDir = None

def debug(msg):
    sys.stderr.write(str(msg)+"\n")

def debug_move(direction, prefix='Moving '):
    if direction == tron.NORTH:
        debug("%sNorth" % prefix)
    elif direction == tron.SOUTH:
        debug("%sSouth" % prefix)
    elif direction == tron.EAST:
        debug("%sEast" % prefix)
    elif direction == tron.WEST:
        debug("%sWest" % prefix)

def diff_coords_relative(coord_f, coord_s):
    """ Diff two sets of coordinates relative to to the first object"""
    newCoords = [coord_f[0]-coord_s[0],
                 coord_f[1]-coord_s[1]]
    debug("Relative location: %s" % str(newCoords))
    return newCoords

def find_major_direction(diff_coords):
    horiz = None
    vertic = None

    if diff_coords[0] < 0:
        horiz = (tron.SOUTH, abs(diff_coords[0]))
    else:
        horiz = (tron.NORTH, diff_coords[0])

    if diff_coords[1] < 0:
        vertic = (tron.WEST, abs(diff_coords[1]))
    else:
        vertic = (tron.EAST, abs(diff_coords[1]))

    if abs(diff_coords[0]) > abs(diff_coords[1]):
        return horiz
    return vertic

class TronPlayer(object):
    def __init__(self):
        self.lastDirection = None

    def pickStrategy(self, board):
        pass

    def findThem(self, board):
        return find_major_direction(diff_coords_relative(board.me(),
                                                         board.them()))

    def genMove(self, board):
        themDirection, themDistance = self.findThem(board)
        debug("Distance to me: %s" % themDistance)
        debug_move(themDirection, "Direction from me: ")

#        if self.lastDirection is not None \
#                and board.passable(board.rel(self.lastDirection)):
#            debug_move(self.lastDirection)
#            return self.lastDirection

        if self.lastDirection is None:
            self.lastDirection = themDirection

        if not board.passable(board.rel(themDirection)) and \
                not board.passable(board.rel(self.lastDirection)):
            debug("Not them, Not Last, picking random")
            debug_move(self.lastDirection, "Last was: ")
            newDirection = random.choice(board.moves())
        elif not board.passable(board.rel(themDirection)) and \
                board.passable(board.rel(self.lastDirection)):
            debug("Not them, moving last")
            newDirection = self.lastDirection
        else:
            debug("Moving to them")
            newDirection = themDirection

        debug_move(newDirection)
        self.lastDirection = newDirection
        return newDirection

tronguy = TronPlayer()
# you do not need to modify this part
for board in tron.Board.generate():
    tron.move(tronguy.genMove(board))
