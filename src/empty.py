# -*- coding: utf-8 -*-
from piece import Piece


class Empty(Piece):
    IMG = '🙿'

    def __str__(self):
        return self.IMG

    def make_move(self, pos_to):
        raise Exception('No piece selected')
