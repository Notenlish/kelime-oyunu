from typing import TYPE_CHECKING

import pygame

from game import Game
from ui import GameUI, StartUI

if TYPE_CHECKING:
    from main import App


global CURRENT
global SINCE_PRESS


class StateManager:
    def __init__(self, app: "App") -> None:
        self.app = app
        self.objs = []
        self.state = None

        self.load_start()

    def init_objs(self, objs: list[object]):
        for obj in self.objs:
            del obj
        self.objs = objs

    def load_start(self):
        self.state = "start"

        self.ui = StartUI(self.app)
        self.init_objs([self.ui])

    def load_game(self):
        self.state = "game"

        self.game = Game(self.app)
        self.app.game = self.game
        self.ui = GameUI(self.app)
        self.init_objs([self.game, self.ui])

    def load_credits(self):
        self.state = "credits"

    def update(self):
        SHARED = self.app.SHARED
        match self.state:
            case "start":
                ...
            case "game":
                self.game.update(self.app.dt)

                if SHARED["current"]:
                    if SHARED["since_press"] == -1:  # first frame of pressing
                        pygame.event.post(
                            pygame.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})
                        )
                        SHARED["since_press"] = 0
                else:
                    # button is not pressed.
                    SHARED["since_press"] = -1
            case "credits":
                ...
            case _:
                raise Exception(f"Undefined State: {self.state}")

    def render(self):
        match self.state:
            case "start":
                self.ui.render()
            case "game":
                self.ui.render()
            case "credits":
                ...
            case _:
                raise Exception(f"Undefined State: {self.state}")

    def input(self):
        match self.state:
            case "start":
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        raise SystemExit
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            self.load_game()
            case "game":
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        raise SystemExit
                    if e.type == pygame.TEXTINPUT:
                        print(e.text)
                        # self.game.open_random_letter(e.text)
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            self.game.answer()
                        if e.key == pygame.K_SPACE:
                            self.game.press_button()
                        if e.key == pygame.K_e:
                            self.game.open_random_letter()
            case "credits":
                ...
            case _:
                raise Exception(f"Undefined State: {self.state}")
