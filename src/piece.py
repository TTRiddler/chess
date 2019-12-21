# -*- coding: utf-8 -*-
color = {0: 'BLACK', 1: 'WHITE', None: 'None'}


class Piece(object):
    IMG = None

    def __init__(self, side, board):
        self.side = side
        self.board = board
        self.position = None
        self.first_move = True

    def __str__(self):
        return self.IMG[self.side]

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, color[self.side])
