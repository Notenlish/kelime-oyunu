import pygame
from letter import Letter

from const import POINT_DEC_FOR_LETTER


class Word:
    def __init__(
        self, font: pygame.Font, word: str, description: str, point: int
    ) -> None:
        self.font = font

        self.word = word
        self.description = description
        self.score = point

        self._gen_letters()

    def check_letter(self, letter: str):
        if self.score < POINT_DEC_FOR_LETTER:
            print(f"The point is lower than {POINT_DEC_FOR_LETTER}")
            return
        for l in self.letters:
            if l.char == letter:
                l.found = True
        self.score -= POINT_DEC_FOR_LETTER

    def _gen_letters(self):
        self.letters = [Letter(self.font, c) for c in self.word]
