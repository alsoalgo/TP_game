from .stone import *
from .dsu import *
from .board import *
from .view import *

import os


class Game:
    def __init__(self, graphics=False):
        self._graphics = graphics
    
    def run(self, n):
        board = Board(n)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            View(board).draw("console")
            print("Current turn ", board.turn)
            print("Scores:")
            print("Black(Blue) :", board.score[0], ", White(Red) :", board.score[1])
            move_i, move_j = map(int, input().split())
            board.move(move_i, move_j)
        

        