# Checkers Game
import pygame
from checkers import board
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
FPS  = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# the game play
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # to end the game from close in top bar
            if event.type == pygame.QUIT:
                run = False
            # event from mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(WIN)
        pygame.display.update()

    # exit from game
    pygame.quit()

main()