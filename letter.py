import pygame

from util import size_of_text, draw_text, scale_and_add_outline  # type:ignore  # noqa F401


class Letter:
    def __init__(
        self, font: pygame.Font, bg: pygame.Surface, char: str, found: bool = False
    ) -> None:
        self.char = char
        self.char_displayed = char.upper()
        self.found = found

        self.font = font
        self.bg = bg

        self.bg_rect_size = pygame.Vector2(
            bg.size
        )  # pygame.Vector2(size_of_text(font, ".#"))

    def render(self, topleft: tuple[int, int], canvas: pygame.Surface):
        bg_rect = pygame.Rect(*topleft, *self.bg_rect_size)

        canvas.blit(self.bg, bg_rect.topleft)

        # pygame.draw.rect(canvas,"#B4BEC9",scale_and_add_outline(bg_rect.copy(), 2))
        # pygame.draw.rect(canvas, "white", bg_rect)
        if self.found:
            text_size = pygame.Vector2(size_of_text(self.font, self.char_displayed))
            # get dif between bg size and text size, divide by 2 and move the rect by that amount -> centers text
            bg_rect.move_ip((self.bg_rect_size - text_size) / 2)
            draw_text(canvas, bg_rect.topleft, self.font, self.char_displayed, True)
