from .stone import *
from .board import *
from .graphics import *
from .handler import get_key as handle

import os

def clear():
    pass


class Game:
    def __init__(self):
        pass
        
    def run(self, n):
        board = Board(n)
        view = Graphics("graphics")
        cursor = Cursor(n)
        view.draw(board, cursor)
        while True:
            key_code = ord(handle())
            if key_code in [119, 97, 115, 100]:
                cursor.update(key_code)
                view.clear()
                view.draw(board, cursor)
            elif key_code == 27:
                view.exit()
                break
            elif key_code == 13:
                board.move(*cursor.position)
                view.clear()
                view.draw(board, cursor)
        