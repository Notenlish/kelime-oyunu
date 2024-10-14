import pygame
from letter import Letter

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App
    from game import Game

from const import POINT_DEC_FOR_LETTER, POINTS_PER_LETTER
from util import draw_text_in_rect

from random import randint


class Word:
    def __init__(
        self,
        app: "App",
        game: "Game",
        font: pygame.Font,
        hexagon: pygame.Surface,
        word: str,
        description: str,
    ) -> None:
        self.app = app
        self.game = game

        self.font = font
        self.bg = hexagon

        self.word = word
        self.description = description
        self.score = len(word) * POINTS_PER_LETTER
        self.orig_score = self.score

        self._gen_letters()

    def show_all(self):
        for letter in self.letters:
            if not letter.found:
                letter.find(self.app.elapsed)

    def draw_desc(
        self,
        rect: pygame.Rect,
        canvas: pygame.Surface,
        color: str | pygame.Color = "black",
    ):
        draw_text_in_rect(self.font, self.description, rect, canvas, color=color)

    def open_letter(self):
        if self.score < POINT_DEC_FOR_LETTER:
            print(f"The point is lower than {POINT_DEC_FOR_LETTER}")
            return

        while True:
            i = randint(0, len(self.letters) - 1)
            if not self.letters[i].found:
                self.letters[i].find(self.app.elapsed)
                break
        self.score -= POINT_DEC_FOR_LETTER

    def _gen_letters(self):
        self.letters = [Letter(self.app, self.font, self.bg, c) for c in self.word]
