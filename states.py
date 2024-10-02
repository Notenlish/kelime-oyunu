import pygame
from ui import GameUI, StartUI
from game import Game
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import App


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

        self.game = Game()
        self.app.game = self.game
        self.ui = GameUI(self.app)
        self.init_objs([self.game, self.ui])

    def load_credits(self):
        self.state = "credits"

    def update(self):
        match self.state:
            case "start":
                ...
            case "game":
                ...
            case "credits":
                ...
            case _:
                print(self.state)
                raise Exception()

    def render(self):
        match self.state:
            case "start":
                self.ui.render()
            case "game":
                self.ui.render()
            case "credits":
                ...
            case _:
                print(self.state)
                raise Exception()

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
                        self.game.enter_letter(e.text)
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_RETURN:
                            self.game.answer()
            case "credits":
                ...
            case _:
                print(self.state)
                raise Exception()
