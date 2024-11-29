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
                '''
                if clicked in bottom selction, see if any buttons where clicked.
                for reset, redraw board
                for display welcome screen again
                for exit, close program
                '''
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
    '''
    if my_board.is_full():
        for i in range(9):
            for j in range(9):
                if my_board[i][j] != correctBoard[i][j]:
                    win = False
        end_game = True
        break
    '''

    # end screen
    my_font = pygame.font.SysFont('Times New Roman', 30)
    if win:
        screen.fill((209, 138, 84))
        text_surface = my_font.render('You win!!', False, (0, 0, 0))
        screen.blit(text_surface, (50, 200))

    else:
        print("bummer")







