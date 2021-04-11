from .board import Board
from .view import View
from .utils import *
import sys
import time

class Game(object):
    def __init__(self, dimension):
        self._board = Board(dimension)
        self._view = View(self._board)

    def move(self):
        self._board.move(*view.cursor)
        self._view.draw(board)

    def exit(self):
        sys.exit(0)

    def run(self):
        KEYS = {
            'w': self._view.cursor_up,
            's': self._view.cursor_down,
            'a': self._view.cursor_left,
            'd': self._view.cursor_right,
            ' ': self.move,
            '\x1b': self.exit,
        }
        while True:
            clear()
            sys.stdout.write('{0}\n'.format(self._view))
            c = getch()
            print(c)
            time.sleep(1)
            try:
                KEYS[c]()
            except Exception:
                pass
