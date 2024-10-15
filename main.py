import pygame

from const import SC_SIZE, FLAGS

from states import StateManager
from game import Game

import threading
from local_pc import run_socket

from player import PlayerManager

pygame.font.init()

SHARED = {"current": 0, "thread_will_run": True, "since_press": -1}


class App:
    def __init__(self) -> None:
        self.sc = pygame.display.set_mode(SC_SIZE, flags=FLAGS)
        self.clock = pygame.time.Clock()
        self.elapsed = 0.0
        self.dt = 0.0

        self.SHARED = SHARED

        self.cur_user_id = 0
        self.player_manager = PlayerManager()
        self.states = StateManager(self, self.player_manager)

        self.sock_thread = threading.Thread(target=run_socket, args=(self.SHARED,), daemon=True)
        self.sock_thread.start()

        self.game: None | Game

        pygame.key.start_text_input()

    def quit(self):
        print("please quit")
        self.SHARED["thread_will_run"] = False
        pygame.key.stop_text_input()
        raise SystemExit

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
