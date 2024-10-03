import pygame

from const import SC_SIZE, FLAGS

from states import StateManager
from game import Game

pygame.font.init()


class App:
    def __init__(self) -> None:
        self.sc = pygame.display.set_mode(SC_SIZE, flags=FLAGS)
        self.clock = pygame.time.Clock()
        self.elapsed = 0.0
        self.dt = 0.0

        self.states = StateManager(self)

        self.game: None | Game

        pygame.key.start_text_input()

    def input(self):
        self.states.input()

    def update(self):
        self.states.update()

    def render(self):
        self.sc.fill("black")
        self.states.render()

    def run(self):
        while True:
            self.input()
            self.update()
            self.render()

            self.dt = self.clock.tick(60) / 1000  # type:ignore
            self.elapsed += self.dt
            pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.run()
