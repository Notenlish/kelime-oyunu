import pygame

from const import SC_SIZE, FLAGS
from ui import UI
from game import Game

pygame.font.init()


class App:
    def __init__(self) -> None:
        self.sc = pygame.display.set_mode(SC_SIZE, flags=FLAGS)
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.ui = UI(self)

        pygame.key.start_text_input()

    def input(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit
            if e.type == pygame.TEXTINPUT:
                print(e.text)
                self.game.enter_letter(e.text)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    self.game.answer()

    def update(self): ...

    def render(self):
        self.sc.fill("black")
        self.ui.render()

    def run(self):
        while True:
            self.input()
            self.update()
            self.render()

            dt = self.clock.tick(60)  # type:ignore
            pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.run()
