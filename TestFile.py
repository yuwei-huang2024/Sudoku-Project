from tabnanny import check

my_list = [[4, 7, 9, 1, 3, 2, 8, 5, 6], [2, 8, 6, 9, 5, 7, 1, 3, 4], [5, 3, 1, 8, 4, 6, 2, 7, 9], [3, 2, 5, 4, 6, 9, 7, 1, 8], [6, 9, 7, 5, 1, 8, 3, 4, 2], [8, 1, 4, 7, 2, 3, 9, 6, 5], [1, 6, 2, 3, 8, 5, 4, 9, 7], [7, 4, 8, 6, 9, 1, 5, 2, 3], [9, 5, 3, 2, 7, 4, 6, 8, 1]]

def check_if_win(my_list):
    cell_coordinates = [[[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]],
                        [[1,4], [1,5], [1,6], [2,4], [2,5], [2,6], [3,4], [3,5], [3,6]],
                        [[1,7], [1,8], [1,9], [2,7], [2,8], [2,9], [3,7], [3,8], [3,9]],
                        [[4,1], [4,2], [4,3], [5,1], [5,2], [5,3], [6,1], [6,2], [6,3]],
                        [[4,4], [4,5], [4,6], [5,4], [5,5], [5,6], [6,4], [6,5], [6,6]],
                        [[4,7], [4,8], [4,9], [5,7], [5,8], [5,9], [6,7], [6,8], [6,9]],
                        [[7,1], [7,2], [7,3], [8,1], [8,2], [8,3], [9,1], [9,2], [9,3]],
                        [[7,4], [7,5], [7,6], [8,4], [8,5], [8,6], [9,4], [9,5], [9,6]],
                        [[7,7], [7,8], [7,9], [8,7], [8,8], [8,9], [9,7], [9,8], [9,9]]]

    # check rows
    for i in range(9):
        row = my_list[i]
        row_set = set(row)
        if len(row_set) != 9:
            print("row false")
            return False

    # column
    for i in range(9):
        col = []
        for j in range(9):
            col.append(my_list[j][i])
        col_set = set(col)
        if len(col_set) != 9:
            return False

    # check 3 by 3 boxes
    for i in range(9): # loop through each 3x3 box
        box = []
        for j in range(9): # loop through each cell in 3x3
            row_num = cell_coordinates[i][j][0] - 1 # minus 1 is to make coordinates match up with computer talk
            col_num = cell_coordinates[i][j][1] - 1 # (start at 0 and not 1)
            box.append(my_list[row_num][col_num])
        box_set = set(box)
        if len(box_set) != 9:
            print("box fail")
            return False

    return True

print(check_if_win(my_list))

'''
from sudoku_generator import *
import pygame, sys

pygame.init()
pygame.font.init()

# main logic
while True:
    draw_start_screen()
    selection = 0  # which difficulty box is clicked
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
    pygame.display.update()

    game_reset = False
    game_restart = False
    game_exit = False
    end_game = False
    win = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clicked in bottom selction, see if any buttons where clicked.
                for reset, redraw board
                for display welcome screen again
                for exit, close program
                # some math here, likely, integer divide mouse
                # coordinates by square size to get which row and
                # column is selected
                board = []
                i, j = 0
                if board[i][j] == 0:  # that cell is blank
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
                        # set_cell_calue():
                    pygame.display.update()

            player_board = generate_sudoku(9, removed_cells)
        if end_game:
            break
    if my_board.is_full():
        for i in range(9):
            for j in range(9):
                if my_board[i][j] != correctBoard[i][j]:
                    win = False
        end_game = True
        break

    # end screen
    my_font = pygame.font.SysFont('Times New Roman', 30)
    if win:
        screen.fill((209, 138, 84))
        text_surface = my_font.render('You win!!', False, (0, 0, 0))
        screen.blit(text_surface, (50, 200))

    else:
        print("bummer")









'''