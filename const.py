import pygame

DEV = True


FLAGS = pygame.SCALED | pygame.RESIZABLE | pygame.FULLSCREEN if not DEV else 0
SC_SIZE = SC_W, SC_H = 640, 360
SC_RECT = pygame.Rect(0, 0, *SC_SIZE)


POINT_DEC_FOR_LETTER = 100
POINTS_PER_LETTER = 100

BUTTON_TIME = 30
