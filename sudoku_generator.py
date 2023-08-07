import math,random

class SudokuGenerator:
    # First array in array is the row, then in the row are the column numbers. This is how i am making the board for reference
    def __init__(self, row_length=9, removed_cells):
        self.row_length = row_length
        if board.difficulty == 'easy':
            self.removed_cells = 30
        elif board.difficulty == 'medium':
            self.removed_cells = 40
        else:
            self.removed_cells = 50
        self.board = [['0' for i in range(9)] for j in range(9)]
        self.box_length = 3
        # Person doing board difficulty can change board.difficulty == based on what they want ot select


    def get_board(self):
        return self.board
        # Simple, just returns the board array
    def print_board(self):
        print(self.board)
        # Just prints the board array as a 2D array
    def valid_in_row(self, row, num):
        for i in range(9):
            if num == self.board[row][i]:
                return False
        return True
        # Checks to see if num is in that row and goes through every column, returns False if it is; else returns True.
    def valid_in_col(self, col, num):
        for i in range(9):
            if num == self.board[i][col]:
                return False
        return True
    # Checks in range 9 so goes through each row in that col to check if num is in it. If yes, returns False; else returns True.
    def valid_in_box(self, row_start, col_start, num):
        for row in range(2):
            for col in range(2):
                if num == self.board[row + row_start][col + col_start]:
                    return True
        return False
    # Goes from the start of a row to two below the row and from start of col to two right of col to see if num is in it. Returns False if not in box.
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) == False:
            return False
        elif self.valid_in_col(col, num) == False:
            return False
        elif row <= 2:
            if col <= 2:
                if self.valid_in_box(0, 0, num) == False:
                    return False
            elif 3 <= col <= 5:
                if self.valid_in_box(0, 3, num) == False:
                    return False
            else:
                if self.valid_in_box(0, 6, num) == False:
                    return False
        elif 3 <= row <= 5:
            if col <= 2:
                if self.valid_in_box(3, 0, num) == False:
                    return False
            elif 3 <= col <= 5:
                if self.valid_in_box(3, 3, num) == False:
                    return False
            else:
                if self.valid_in_box(3, 6, num) == False:
                    return False
        elif 6 <= row:
            if col <= 2:
                if self.valid_in_box(6, 0, num) == False:
                    return False
            elif 3 <= col <= 5:
                if self.valid_in_box(6, 3, num) == False:
                    return False
            else:
                if self.valid_in_box(6, 6, num) == False:
                    return False
        else:
            return True
    # Goes through to check if given num is valid in that row, valid in the col, and valid in the box. If not valid, returns False; else, returns True
    def fill_box(self, row_start, col_start):
        self.counter = 0
        self.random_array = random.sample(range(1, 10), 9)
        for row in range(2):
            for col in range(2):
                self.board[row + row_start][col + col_start] = self.random_array[self.counter]
                self.counter += 1
        return None
        # I used chat gpt to find out how to generate a list of random numbers 1-9

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
        return None
        # Just fills in the diagonal boxes as upper left cell starts at (0, 0), (3, 3), and (6, 6)
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
        # I got this from the sudoku_generator.py given
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        self.random_array = []
        self.counter = 0
        while self.counter <= self.removed_cells:
            self.row = random.randint(0, 8)
            self.col = random.randint(0, 8)
            if [[self.row, self.col]] in self.random_array:
                pass
            else:
                self.board[self.row][self.col] = 0
                self.counter += 1
        # Call this function after all the values are filled for the sudoku puzzle. Used similar randomness in fill box to generate ordered pairs. I used ChatGPT to find out how to generate a random integer 0 - 8

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
    # Got this from given sudoku_generator.py file.