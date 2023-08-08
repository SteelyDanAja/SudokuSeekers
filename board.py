import pygame
from constants import *
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
        self.selected_cell = None

    def draw(self):
        # Draw Sudoku grid outline and cells
        # Implement drawing logic here
        pass

    def select(self, row, col):
        self.selected_cell = (row, col)

    def click(self, x, y):
        # Determine clicked cell and return (row, col)
        row = y // (self.screen.get_height() // self.height)
        col = x // (self.screen.get_width() // self.width)
        return row, col

    def clear(self):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].value = 0

    def sketch(self, value):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].sketch = value

    def place_number(self, value):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].value = value

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                # Reset cell to its original value
                cell.value = 0

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        # Update underlying 2D board with cell values
        pass

    def find_empty(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.cells[row][col].value == 0:
                    return row, col
        return None

    def check_board(self):
        # Check if the Sudoku board is solved correctly
        for row in self.cells:
            values = set()
            for cell in row:
                if cell.value != 0:
                    if cell.value in values:
                        return False
                    values.add(cell.value)
        
        for col in range(self.width):
            values = set()
            for row in range(self.height):
                if self.cells[row][col].value != 0:
                    if self.cells[row][col].value in values:
                        return False
                    values.add(self.cells[row][col].value)

        for row in range(0, self.height, 3):
            for col in range(0, self.width, 3):
                values = set()
                for i in range(3):
                    for j in range(3):
                        value = self.cells[row + i][col + j].value
                        if value != 0:
                            if value in values:
                                return False
                            values.add(value)
        return True