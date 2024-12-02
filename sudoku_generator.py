import random, pygame, sys
pygame.init()
pygame.font.init()


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = 3
        # :param row_length: always 9
        # :param removed_cells: cells to be cleared

    def get_board(self):
        return self.board  # returning current board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))  # for debugging??


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
    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
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

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        removed_count = 0
        while removed_count < self.removed_cells:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed_count += 1


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''

solution = []

def generate_sudoku(size: object, removed: object) -> object:
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    global solution # it says not to change, but added this to save solution or else solution was not saving anywhere?
    solution = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = initialize_board()
        self.selected = None
        self.cells = [
            [Cell(self.board[i][j],i, j, screen) for j in range(9)]
            for i in range(9)
        ]

    def draw(self):
        pass
    #Need to make this work with draw_sudoku_screen


    def select(self, row, col):
        if self.selected != None:
            self.selected = None
        self.selected = self.cells[row][col]
        self.selected.selected = True


    def click(self, row, col):
        #Very rough, just wanna mess with event parameter
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("test")
                x, y = event.pos
                if 0 <= x <= 600 and 0 <= y <= 600:
                    newRow = x // 68
                    newCol = y // 68

                #Need to figure out positioning fully

                    return (newRow, newCol)

        return None



    def clear(self):
        #This basically does nothing, need to see how board generates non-user values
        for row in self.cells:
            for cell in row:
                if cell.isUser == True:
                    cell.value = "-"
                    cell.sketched_value = "-"

    def sketch(self, value):
        self.sketched_value = value

    def place_number(self, value):
        pass

    def reset_to_original(self):
        for cell in self.cells:
            if cell.value != 0 and cell.isUser == True:
                cell.value = 0

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == "-":
                    return False

        return True

    def update_board(self):
        pass

    def find_empty(self):
        for row in self.cells:
            for cell in row:
                if cell.value == "-":
                    return (cell.row, cell.col)

    def check_board(self):
        pass


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.isUser = False


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        my_font = pygame.font.SysFont('Times New Roman', 30)
        color = (255, 255, 255)

        cellRow = self.row * 64 + self.row * 3
        cellCol = self.col * 64 + self.col * 3


        pygame.draw.rect(self.screen, color, (cellCol, cellRow, 67, 67))

        if self.value != 0:
            text_surf = my_font.render(str(self.value), True, (0,0,0))

            #using to test
            text_rect = text_surf.get_rect(center=((cellCol+32.5), (cellRow+32.5)))
            self.screen.blit(text_surf, text_rect)

        if self.selected == True:
            pygame.draw.rect(self.screen, (255, 0, 0), (cellRow, cellCol, 65, 65),  2)







WIDTH = 646
HEIGHT = 646
LINE_COLOR = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT+120))
pygame.display.set_caption("Sudoku")

#initializing the board
def initialize_board():
    # 1st approach
    return [["-" for i in range(9)] for j in range(9)]
board = initialize_board()

def draw_sudoku_screen(): # changed draw grid to this function
    # drawing horizontal cell lines
    screen.fill((209, 138, 84))


    #print(board[0][0])

    for row in range(9):
        for col in range(9):
            cell = Cell(1, row, col, screen)

            board.cells[row][col].value = cell.value
            #print(board.cells[row][col].value)
            cell.draw()

    pygame.display.update()
	
    #cell lines
    for i in range(0,10):
            pygame.draw.line(
                screen,
                (255,255,255),
                (0, 3 + i * 71),
                (646, 3 + i * 71),
                7

            )
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (3 + i * 71, 1),
                (3 + i * 71, 646),
                7

            )
    #border lines
    for i in range(0,10):
            if i % 3 == 0:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (3 + i * 71, 0),
                    (3 + i * 71, 646),
                    7

                )
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    (0, 3 + i * 71),
                    (646, 3 + i * 71),
                    7

                )

    my_font = pygame.font.SysFont('Times New Roman', 30)
    reset_rect = pygame.Rect(100, 630, 100, 50)
    restart_rect = pygame.Rect(240, 630, 120, 50)
    exit_rect = pygame.Rect(400, 630, 100, 50)

    pygame.draw.rect(screen, (0, 0, 0), reset_rect)
    pygame.draw.rect(screen, (0, 0, 0), restart_rect)
    pygame.draw.rect(screen, (0, 0, 0), exit_rect)

    pygame.draw.rect(screen, (209, 138, 84), (105, 635, 90, 40))
    pygame.draw.rect(screen, (209, 138, 84), (245, 635, 110, 40))
    pygame.draw.rect(screen, (209, 138, 84), (405, 635, 90, 40))

    text_surface = my_font.render('Reset', False, (0, 0, 0))
    screen.blit(text_surface, (115, 638))
    text_surface = my_font.render('Restart', False, (0, 0, 0))
    screen.blit(text_surface, (250, 638))
    text_surface = my_font.render('Exit', False, (0, 0, 0))
    screen.blit(text_surface, (410, 638))


    pygame.display.update()
    return reset_rect, restart_rect, exit_rect

def draw_start_screen():
    my_font = pygame.font.SysFont('Times New Roman', 30)
    screen.fill((209, 138, 84))

    text_surface = my_font.render('Welcome to Sudoku!', False, (0, 0, 0))
    screen.blit(text_surface, (195, 200))
    text_surface = my_font.render('Select difficulty:', False, (0, 0, 0))
    screen.blit(text_surface, (220, 300))

    easy_rect = pygame.Rect(80, 390, 120, 50)
    medium_rect = pygame.Rect(261, 390, 120, 50)
    hard_rect = pygame.Rect(442, 390, 120, 50)

    pygame.draw.rect(screen, (0, 0, 0), easy_rect)
    pygame.draw.rect(screen, (0, 0, 0), medium_rect)
    pygame.draw.rect(screen, (0, 0, 0), hard_rect)

    pygame.draw.rect(screen, (209, 138, 84), (85, 395, 110, 40))
    pygame.draw.rect(screen, (209, 138, 84), (266, 395, 110, 40))
    pygame.draw.rect(screen, (209, 138, 84), (447, 395, 110, 40))

    text_surface = my_font.render('Easy', False, (0, 0, 0))
    screen.blit(text_surface, (110, 398))
    text_surface = my_font.render('Medium', False, (0, 0, 0))
    screen.blit(text_surface, (270, 398))
    text_surface = my_font.render('Hard', False, (0, 0, 0))
    screen.blit(text_surface, (472, 398))

    pygame.display.update()
    return easy_rect, medium_rect, hard_rect

def draw_numbers():
    pass
def draw_win_end_screen():
    my_font = pygame.font.SysFont('Times New Roman', 30)

    screen.fill((209, 138, 84))
    text_surface = my_font.render('You win!!', False, (0, 0, 0))
    screen.blit(text_surface, (230, 200))
    exit_rect = pygame.Rect(220, 290, 100, 50)
    pygame.draw.rect(screen, (0, 0, 0), exit_rect)
    pygame.draw.rect(screen, (209, 138, 84), (225, 295, 90, 40))
    pygame.display.update()
    text_surface_2 = my_font.render('EXIT', False, (0, 0, 0))
    screen.blit(text_surface_2, (230, 300))

    return exit_rect
def draw_lose_end_screen():
    my_font = pygame.font.SysFont('Times New Roman', 30)

    screen.fill((209, 138, 84))
    text_surface = my_font.render('Game Over :(', False, (0, 0, 0))
    screen.blit(text_surface, (230, 200))
    restart_rect = pygame.Rect(220, 290, 160, 50)
    pygame.draw.rect(screen, (0, 0, 0), restart_rect)
    pygame.draw.rect(screen, (209, 138, 84), (225, 295, 150, 40))
    pygame.display.update()
    text_surface_2 = my_font.render('RESTART', False, (0, 0, 0))
    screen.blit(text_surface_2, (230, 300))

    return restart_rect


end_loop = False

difficulty = ""
while True:
    # event loop
    while True: # for start screen
        if end_loop:
            end_loop = False
            break
        easy_rect, medium_rect, hard_rect = draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    removed_cells = 30
                    print("1")
                    end_loop = True
                    difficulty = "Easy"
                    board = Board(WIDTH,HEIGHT, pygame.display, difficulty)
                    break
                elif medium_rect.collidepoint(event.pos):
                    removed_cells = 40
                    print('2')
                    end_loop = True
                    difficulty = "Medium"
                    board = Board(WIDTH, HEIGHT, pygame.display, difficulty)
                    break
                elif hard_rect.collidepoint(event.pos):
                    removed_cells = 50
                    print('3')
                    end_loop = True
                    difficulty = "Hard"
                    board = Board(WIDTH, HEIGHT, pygame.display, difficulty)
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    while True: # for sudoku screen


        if end_loop:
            end_loop = False
            break
        reset_rect, restart_rect, exit_rect = draw_sudoku_screen()
        #pygame.display.update()

        #print(board.click(event.pos[0], event.pos[1]))
        #Just used this for testing for now


        #Used to test selection, cell can be selected but leads to some jank with display :)

        # click = board.click(event.pos[0], event.pos[1])
        #
        # if click != None:
        #     board.selected = board.cells[click[0]][click[1]]
        #     board.selected.selected = True
        #     board.selected.screen = screen
        #     board.selected.draw()
        #     pass

        pygame.display.update()

        for event in pygame.event.get():
            #purely for testing purposes

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if reset_rect.collidepoint(event.pos):
                        win = True
                        end_loop = True
                    elif restart_rect.collidepoint(event.pos):
                        win = False
                        end_loop = True
		    elif exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    while True: #end screen win scenario
        if end_loop:
            pygame.quit()
            sys.exit()
        if win:
            exit_rect = draw_win_end_screen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rect.collidepoint(event.pos):
                        end_loop = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        else:
            restart_rect = draw_lose_end_screen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # also exits at the moment, fix later
                    if restart_rect.collidepoint(event.pos):
                        end_loop = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



