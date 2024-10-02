import pygame
from word import Word


class Game:
    def __init__(self) -> None:
        self.db: list[Word] = []
        self.font = pygame.Font("assets/AfacadFlux.ttf", 20)
        self.total_score = 0

        self.hexagon = pygame.image.load_sized_svg(
            "assets/hexagon.svg", (48, 48)
        ).convert_alpha()

        self.read_db()

    def enter_letter(self, char: str):
        self.active_word.check_letter(char)

    def read_db(self):
        with open("questions.txt", "r") as f:
            rows = f.readlines()

        for r in rows:
            inp = r.split(":", maxsplit=1)
            word = inp[0].strip()
            description = inp[1].strip()
            self.db.append(Word(self.font, self.hexagon, word, description))

        self.get_active_word()

    def answer(self):
        self.total_score += self.active_word.score
        self.db.remove(self.active_word)
        if len(self.db) == 0:
            print("Kazandınız!")
        self.get_active_word()

    def get_active_word(self, i: int | None = None):
        if i is None:
            self.active_word = self.db[0]
        else:
            self.active_word = self.db[i]

        print(f"Answer is: {self.active_word.word}")
