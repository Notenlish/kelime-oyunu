import string as string_stuff
from typing import TYPE_CHECKING, Literal

import pygame

from const import BUTTON_TIME
from sfx import SFX
from word import Word

if TYPE_CHECKING:
    from main import App


class Game:
    def __init__(self, app: "App") -> None:
        self.app = app

        self.db: list[Word] = []
        self.font = pygame.Font("assets/AfacadFlux.ttf", 20)
        self.bigfont = pygame.Font("assets/AfacadFlux.ttf", 22)
        self.total_score = 0
        self.left_time = 4 * 60
        self.button_time = -1

        self.sub_state: Literal["question", "answer"] = "question"
        self.active_word: Word = None  # type:ignore

        self.hexagon = pygame.image.load_sized_svg(
            "assets/hexagon3.svg", (48, 64)
        ).convert_alpha()

        self.sfx = SFX(self.app, self)

        self.read_db()

    @property
    def button_active(self):
        button_active = self.button_time > -1
        return button_active

    def fail_button_word_guess(self):
        """Called when the player cannot guess the word correctly when they have pressed the button."""
        self.total_score -= self.active_word.orig_score
        self.reset_button_time()
        self.next_word()
        self.sfx.play_sfx("failed")

    def reset_button_time(self):
        self.button_time = -1

    def press_button(self):
        def _():
            pass
            # self._get_active_word()

        self.sfx.play_sfx("press-btn", _)
        self.button_time = BUTTON_TIME

    def update(self, dt: float):
        self.sfx.update()

        def time_stuff():
            if not self.button_active:
                self.left_time -= dt
                if self.left_time <= 0:
                    # TODO: CHANGE TO CREDITS/END SCENE
                    print("Run Out Of Time!")
                    raise SystemExit
            elif self.button_active:
                self.button_time -= dt
                if self.button_time <= 0:
                    self.fail_button_word_guess()

        if self.sub_state == "question":
            time_stuff()

    def open_random_letter(self):
        self.active_word.open_letter()
        self.sfx.play_sfx("get-letter")

    def read_db(self):
        with open("questions.txt", "r", encoding="utf-8") as f:
            rows = f.readlines()

        for r in rows:
            inp = r.split(":", maxsplit=1)
            print(inp)
            word = inp[0].strip()
            description = inp[1].strip()
            self.db.append(Word(self.app, self, self.bigfont, self.hexagon, word, description))

        self.next_word()

    def answer(self):
        """Called if user answers the word."""
        if self.sub_state == "question":
            self.total_score += self.active_word.score
            self.sub_state = "answer"
            self.active_word.show_all()
            self.sfx.stop_looping("loop")
            self.sfx.play_sfx("correct-guess")
        elif self.sub_state == "answer":
            self.sub_state = "question"
            self.next_word()

    def next_word(self):
        self.sfx.play_looping("loop")
        """Called if user moves on to the next word."""
        if self.active_word:
            self.db.remove(self.active_word)
        if len(self.db) == 0:
            # TODO: move to credits screen
            print("Kazandınız!")
        self.reset_button_time()
        self._get_active_word()

    def _get_active_word(self, i: int | None = None):
        if i is None:
            self.active_word = self.db[0]
        else:
            self.active_word = self.db[i]

        print(f"Answer is: {self.active_word.word}")
