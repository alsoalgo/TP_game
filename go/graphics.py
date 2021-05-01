from .stone import *
from .board import *
from .cursor import Cursor

import os

import pygame


class Graphics(object):
    def __init__(self, gtype="console"):
        self._type = gtype
        self._screen = None
        self._is_screen_created = False
        self._n = 0
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (64, 128, 255)
        self.GREEN = (0, 200, 64)
        self.PINK = (230, 50, 230)
        self.x = 20
    
    def create_screen(self, n):
        self._n = n
        if self._is_screen_created:
            return
        self._is_screen_created = True
        pygame.init()
        pygame.mixer.init()
        print("Inited")
        self._screen = pygame.display.set_mode(((n + 1) * self.x, (n + 1) * self.x))
        pygame.display.set_caption("Go")
        self._clock = pygame.time.Clock()

    def draw_graphics(self, board, cursor):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        BLUE = (64, 128, 255)
        GREEN = (0, 200, 64)
        PINK = (230, 50, 230)

        n = board._dimension
        self.create_screen(board._dimension)
        pygame.draw.rect(self._screen, WHITE, (0, 0, (n + 1) * self.x, (n + 1) * self.x)) #background
        for i in range(n):
            pygame.draw.aaline(self._screen, BLACK, [(i + 1) * self.x, 0], [(i + 1) * self.x, (n + 1) * self.x]) #vertical line
            pygame.draw.aaline(self._screen, BLACK, [0, (i + 1) * self.x], [(n + 1) * self.x, (i + 1) * self.x]) #horizontal line
        for i in range(n):
            for j in range(n):
                if [i, j] == cursor.position:
                    pygame.draw.circle(self._screen, self.GREEN, [(j + 1) * self.x, (i + 1) * self.x], int(0.4 * self.x))
                    continue
                stone = board[i, j]
                if stone.color == "B": 
                    pygame.draw.circle(self._screen, self.BLUE, [(j + 1) * self.x, (i + 1) * self.x], int(0.4 * self.x))
                elif stone.color == "W":
                    pygame.draw.circle(self._screen, self.PINK, [(j + 1) * self.x, (i + 1) * self.x], int(0.4 * self.x))
        pygame.display.update()

    def draw_console(self, _board, _cursor):
        n = _board._dimension

        beautiful_string = ""
        beautiful_string += "#" * (n + 2)
        beautiful_string += "\n"

        for i in range(n):
            beautiful_string += "#"
            for j in range(n):
                if [i, j] == _cursor.position:
                    beautiful_string += "C"
                    continue
                stone = _board[i, j]
                if stone.color == "B": 
                    beautiful_string += "x"
                elif stone.color == "E":
                    beautiful_string += " "
                elif stone.color == "W":
                    beautiful_string += "o"
            beautiful_string += "#"
            beautiful_string += "\n"
        beautiful_string += "#" * (n + 2)
        beautiful_string += "\n"
        print(beautiful_string)
    
    def exit(self):
        if self._type == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            pygame.quit()
    
    def clear(self):
        if self._type == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            pygame.draw.rect(self._screen, self.WHITE, (0, 0, (self._n + 1) * self.x, (self._n + 1) * self.x))

    def draw(self, board, cursor):
        if self._type == "console":
            self.draw_console(board, cursor)
        else:
            self.draw_graphics(board, cursor)