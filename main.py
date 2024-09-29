import pygame
import mili # type: ignore

DEV = True
FLAGS = pygame.SCALED|pygame.RESIZABLE if not DEV else 0

class App:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((640, 360), flags=FLAGS)
        self.mili = mili.MILI(self.window)
    
    def run(self):
        ...
