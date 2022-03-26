import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# color
RED = (255, 255, 255)   #RED   --> white
WHITE = (0, 255, 0)     #WHITE --> green
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)      
GREY = (128,128,128)    

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
