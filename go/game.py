from .stone import *
from .dsu import *
from .board import *
from .view import *

import os


class Game:
    def __init__(self):
        pass
        
    def run(self, n):
        pygame.init()
        pygame.mixer.init()
        #screen = pygame.display.set_mode((600, 600))
        #pygame.display.set_caption("My Game")
        clock = pygame.time.Clock()
        board = Board(n)
        view = View(board)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            view.draw("console")
            print("Current turn ", board.turn)
            print("Scores:")
            print("Black(Blue) :", board.score[0], ", White(Red) :", board.score[1])
            move_i, move_j = map(int, input().split())
            board.move(move_i, move_j)
        
    
        