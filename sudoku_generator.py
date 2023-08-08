import math,random

class SudokuGenerator:
    # First array in array is the row, then in the row are the column numbers. This is how i am making the board for reference
    def __init__(self, row_length=9, removed_cells=30):
        self.row_length = row_length
        self.removed_cells = removed_cells
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
        for row in range(3):
            for col in range(3):
                if num == self.board[row + row_start][col + col_start]:
                    return False
        return True
    # Goes from the start of a row to two below the row and from start of col to two right of col to see if num is in it. Returns False if not in box.
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) == False:
            return False
        elif self.valid_in_col(col, num) == False:
            return False
        else:
            row_checker = (row // 3) * 3
            col_checker = (col // 3) * 3
            if self.valid_in_box(row_checker, col_checker, num) == False:
                return False
            else:
                return True
    # Goes through to check if given num is valid in that row, valid in the col, and valid in the box. If not valid, returns False; else, returns True. Used Chat GPT to simplify the box checker portion of code.
    def fill_box(self, row_start, col_start):
        self.counter = 0
        self.random_array = random.sample(range(1, 10), 9)
        for row in range(3):
            for col in range(3):
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
        random_set = set()
        counter = 0
        while counter < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if (row, col) not in random_set:
                self.board[row][col] = 0
                counter += 1
                random_set.add((row, col))
        # Call this function after all the values are filled for the sudoku puzzle. Used similar randomness in fill box to generate ordered pairs. I used ChatGPT to find out how to generate a random integer 0 - 8

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

if __name__ == "__main__":
    pass
