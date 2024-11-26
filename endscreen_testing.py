from sudoku_generator import *
import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
running = True


win = True
my_font = pygame.font.SysFont('Times New Roman', 30)
if win:
    screen.fill((209, 138, 84))
    text_surface = my_font.render('You win!!', False, (0, 0, 0))
    screen.blit(text_surface, (230, 200))
    exit_rect = pygame.Rect(220, 290, 100, 50)
    pygame.draw.rect(screen, (0, 0, 0), exit_rect)
    pygame.draw.rect(screen, (209, 138, 84), (225, 295, 90, 40))
    pygame.display.update()
    text_surface_2 = my_font.render('EXIT', False, (0, 0, 0))
    screen.blit(text_surface_2, (230, 300))

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
                running = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not running:
        pygame.quit()
        sys.exit()

    pygame.display.update()