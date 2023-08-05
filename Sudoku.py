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
        self.board = [['-' for i in range(9)] for j in range(9)]
        # Person doing board difficulty can change board.difficulty == based on what they want ot select


    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)

    def valid_in_row(self, row, num):
        for i in range(9):
            if num == self.board[row][i]:
                return True
        return False

    def valid_in_col(self, col, num):
        for i in range(9):
            if num == self.board[i][col]:
                return True
        return False
    # Checks in range 10 so goes through each row in that col to check if num is in it. If yes, returns True.
    def valid_in_box(self, row_start, col_start, num):
        for row in range(2):
            for col in range(2):
                if num == self.board[row + row_start][col + col_start]:
                    return True
        return False
    # Goes from the start of a row to two below the row and from start of col to two right of col to see if num is in it.
    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass
    def fill_values(self):
        pass

    def remove_cells(self):
        pass
