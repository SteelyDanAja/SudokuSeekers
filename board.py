import pygame
from constants import *
from cell import Cell
from sudoku_generator import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        if difficulty == 'easy':
            self.generated_sudoku = generate_sudoku(9, 30)
        elif difficulty == 'medium':
            self.generated_sudoku = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            self.generated_sudoku = generate_sudoku(9, 50)
        self.cells = [[Cell(self.generated_sudoku[j][i], j, i, screen) for i in range(width)] for j in range(height)]


    def draw(self):
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 3), (WIDTH, SQUARE_SIZE * 3), LINE_WIDTH + 5)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 4), (WIDTH, SQUARE_SIZE * 4), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 5), (WIDTH, SQUARE_SIZE * 5), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 6), (WIDTH, SQUARE_SIZE * 6), LINE_WIDTH + 5)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 7), (WIDTH, SQUARE_SIZE * 7), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 8), (WIDTH, SQUARE_SIZE * 8), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 9), (WIDTH, SQUARE_SIZE * 9), LINE_WIDTH + 5)
        # Sets up the Horizontal Lines
        for i in range(1, 10):
            if i == 3 or i == 6 or i == 9:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT-300), LINE_WIDTH + 5)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT - 300), LINE_WIDTH)
        # Sets up the Vertical Lines
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

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