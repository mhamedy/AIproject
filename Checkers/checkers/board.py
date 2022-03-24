# checker board
import pygame
from .constants import BLACK, ROWS, RED,SQUARE_SIZE

from checkers.constants import BLACK
class Board:
    def __init__(self):
        # board piece
        self.board = [] 
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row %2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # to add pieces in board
    def create_board(self):
        pass