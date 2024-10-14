import pygame

from typing import TYPE_CHECKING
from util import size_of_text, draw_text, scale_and_add_outline  # type:ignore  # noqa F401

if TYPE_CHECKING:
    from main import App


class Letter:
    def __init__(
        self,
        app: "App",
        font: pygame.Font,
        bg: pygame.Surface,
        char: str,
        found: bool = False,
    ) -> None:
        self.app = app
        self.char = char
        self.char_displayed = char.upper()
        self.found = found
        self.found_at = 0.0

        self.font = font
        self.bg = bg

        self.bg_rect_size = pygame.Vector2(
            bg.size
        )  # pygame.Vector2(size_of_text(font, ".#"))

    def find(self, time: float):
        self.found = True
        self.found_at = time

    def render(self, topleft: tuple[int, int], canvas: pygame.Surface):
        bg_rect = pygame.Rect(*topleft, *self.bg_rect_size)

        canvas.blit(self.bg, bg_rect.topleft)

        # pygame.draw.rect(canvas,"#B4BEC9",scale_and_add_outline(bg_rect.copy(), 2))
        # pygame.draw.rect(canvas, "white", bg_rect)
        if self.found:
            text_size = pygame.Vector2(size_of_text(self.font, self.char_displayed))
            # get dif between bg size and text size, divide by 2 and move the rect by that amount -> centers text
            text_rect = bg_rect.copy()

            text_rect.move_ip((self.bg_rect_size - text_size) / 2)

            text_rect.move_ip(0, -20)
            dif = self.found_at - self.app.elapsed
            if dif < -2:
                dif = 0.55
            movement = dif * -120 % 42
            text_rect.move_ip(0, movement)

            draw_text(canvas, text_rect.topleft, self.font, self.char_displayed, True)
            canvas.blit(self.bg, bg_rect.topleft)
