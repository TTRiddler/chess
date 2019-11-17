class Piece(object):
    IMG = None

    def __init__(self, side, position):
        self.side = side
        self.position = position

    def __str__(self):
        return self.IMG[self.side]
