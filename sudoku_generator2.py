#sorry i was confused with where to put the class
#i saw oliver's code but I wasn't sure where to include mine so I thought of making a separate file and then we can just merge it later
#pls let me know what edits i need to make and thank you guys for your patience

import random


class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=30):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        # :param row_length: always 9
        # :param removed_cells: cells to be cleared

    def get_board(self):
        return self.board #returning current board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row)) #for debugging??

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (
            self.valid_in_row(row, num)
            and self.valid_in_col(col, num)
            and self.valid_in_box(row - row % 3, col - col % 3, num)
        )

    def fill_box(self, row_start, col_start):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self):
        def backtrack(row, col):
            if row == self.row_length - 1 and col == self.row_length:
                return True
            if col == self.row_length:
                row += 1
                col = 0
            if self.board[row][col] != 0:
                return backtrack(row, col + 1)
            for num in range(1, 10):
                if self.is_valid(row, col, num):
                    self.board[row][col] = num
                    if backtrack(row, col + 1):
                        return True
                    self.board[row][col] = 0
            return False

        backtrack(0, 0)

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining()

    def remove_cells(self):
        removed_count = 0
        while removed_count < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed_count += 1


def generate_sudoku(size=9, removed=30):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    return sudoku.get_board()
 # function generates a Sudoku board with a given size and number of removed cells
    # :param size: aize of the board (always 9 for this project)
    # :param removed: number of cells to be removed
    # :return: a 2D list representing the Sudoku board



