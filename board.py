import pygame
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:

    def __init__(self, width, height, screen, difficulty):
        self.selected = None
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        for i in range(0, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * 150), (WIDTH, i * 50), 2)
        for i in range(0, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * 150), (WIDTH, i *150), LINE_WIDTH)
        for i in range(0, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (i * (WIDTH//9), 0), (i * (WIDTH//9), HEIGHT - 150), 2)

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass