from .stone import *
from .dsu import *
from .board import *

import colorama
from colorama import Fore, Back, Style

import os

import pygame


class View(object):
    _board = Board()

    def __init__(self, board=Board()):
        self._board = board
    
    @property
    def board(self):
        return self._board
    
    @board.setter
    def board(self, value):
        self._board = value

    def draw_console(self):
        def border():
            prefix = Fore.WHITE + Back.WHITE
            postfix = Style.RESET_ALL #u20DD U+25CF 25EF
            return prefix + "\u2B1B" + postfix
        
        def board(): # board
            prefix = Fore.BLACK + Back.BLACK
            postfix = Style.RESET_ALL #u20DD U+25CF 25EF
            return prefix + "\u2B1B" + postfix

        def red(): # white
            prefix = Fore.RED 
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix
        
        def blue(): # black
            prefix = Fore.BLUE
            postfix = Style.RESET_ALL
            return prefix + "\u2B1B" + postfix

        n = self._board._dimension

        beautiful_string = ""
        beautiful_string += border() * (n + 2)
        beautiful_string += "\n"

        for i in range(n):
            beautiful_string += border()
            for j in range(n):
                stone = self._board[i, j]
                if stone.color == "B": 
                    beautiful_string += blue()
                elif stone.color == "E":
                    beautiful_string += board()
                elif stone.color == "W":
                    beautiful_string += red()
            beautiful_string += border()
            beautiful_string += "\n"
        beautiful_string += border() * (n + 2)
        beautiful_string += "\n"
        print(beautiful_string)

    def draw_graphics(self):
        pass

    
    def draw(self, type_="console"):
        self.draw_console()