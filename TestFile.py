from sudoku_generator import *
import pygame, sys

pygame.init()
pygame.font.init()
WIDTH = 600
HEIGHT = 600
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
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, 66),
        (WIDTH, 66),
        3
    )
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0, 66 + 202 * i),
            (WIDTH, 66 + 202 * i),
            3
        )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, 133),
        (WIDTH, 133),
        3
    )
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (0, 133 + 202 * i),
            (WIDTH, 133 + 202 * i),
            3
        )
    # drawing vertical cell lines
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (66, 0),
        (66, HEIGHT),
        3
    )
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (66 + 202 * i, 0),
            (66 + 202 * i, WIDTH),
            3
        )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (133, 0),
        (133, HEIGHT),
        3
    )
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (202 * i + 133, 0),
            (202 * i + 133, HEIGHT),
            3
        )
    # drawing vertical border lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (69 * i + 133 * i, 0),
            (69 * i + 133 * i, HEIGHT),
            7
        )
    # drawing horizontal border lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, 69 * i + 133 * i),
            (WIDTH, 69 * i + 133 * i),
            7

        )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, HEIGHT + 8),
        (WIDTH, HEIGHT + 8),
        15
    )

screen.fill((209, 138, 84))
draw_grid()


'''
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    '''

# main logic
def draw_start_screen():
    pass
def draw_numbers():
    pass
def draw_end_screen():
    pass


draw_start_screen()
selection = 0 # which difficulty box is clicked
removed_cells = 0
if selection == 1:
    removed_cells = 30
elif selection == 2:
    removed_cells = 40
else:
    removed_cells = 50

my_board = generate_sudoku(9, removed_cells)
draw_sudoku_screen()
draw_numbers()

game_reset = False
game_restart = False
game_exit = False
end_game = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTOONDOWN:
            '''
            if clicked in bottom selction, see if any buttons where clicked.
            for reset, redraw board
            for display welcome screen again
            for exit, close program
            '''
            #some math here, likely, integer divide mouse
            #coordinates by square size to get which row and
            #column is selected
            board = []
            i, j = 0
            if board[i][j] == 0: #that cell is blank
                if event.key == pygame.K_KP1:
                    sketched = 1
                elif event.key == pygame.K_KP2:
                    sketched = 2
                elif event.key == pygame.K_KP3:
                    sketched = 3
                elif event.key == pygame.K_KP4:
                    sketched = 4
                elif event.key == pygame.K_KP5:
                    sketched = 5
                elif event.key == pygame.K_KP6:
                    sketched = 6
                elif event.key == pygame.K_KP7:
                    sketched = 7
                elif event.key == pygame.K_KP8:
                    sketched = 8
                elif event.key == pygame.K_KP9:
                    sketched = 9
                elif event.key == pygame.K_RETURN:
                    pass
                    #set_cell_calue():
                pygame.display.update()

        my_board = Board()
        correctBoard  = []
        if my_board.is_full():
            for i in range(9):
                for j in range(9):
                    if my_board[i][j] != correctBoard[i][j]:
                        win = False
            end_game = True
            break
    if end_game:
        break

#end screen
my_font = pygame.font.SysFont('Times New Roman', 30)
if win:
    screen.fill((209, 138, 84))
    text_surface = my_font.render('You win!!', False, (0, 0, 0))
    screen.blit(text_surface, (50,200))

else:
    print("bummer")







