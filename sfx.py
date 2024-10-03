import pygame
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from main import App
    from game import Game


type SoundEventListener = Callable[[], None]


class SFX:
    def __init__(self, app: "App", game: "Game") -> None:
        pygame.mixer.init(buffer=4096)

        self.app = app
        self.game = game

        self.channels_events: dict[pygame.Channel, SoundEventListener] = {}

        self.sounds = {
            k: pygame.mixer.Sound(f"assets/sounds/{v}")
            for k, v in {
                "win": "win.mp3",
                "failed": "failed.mp3",
                "wohwoh": "wuah-wuah-wuaaah.mp3",
                "btn-click": "btn-click.mp3",
                "transition": "transition.mp3",
                "press-btn": "press-btn.mp3",
            }.items()
        }

        self.current = None

    @property  # could this be a normal getter? yep. I like using this though.
    def cur_btn_music(self):
        if not self.game.button_active:
            raise Exception("Cannot be called while button is not active!")
        t = self.game.button_time
        if t < 10:
            return "assets/sounds/fast.mp3"
        elif t < 20:
            return "assets/sounds/medium.mp3"
        else:
            return "assets/sounds/slow.mp3"

    def play_tick_tock(self, name: str):
        m = pygame.mixer.music
        if self.current != name:
            m.load(name)
            m.play(-1)
            self.current = name

    def play_sfx(self, name: str, listener: SoundEventListener | None = None):
        def _(): ...

        if not listener:
            listener = _

        channel = self.sounds[name].play()
        self.channels_events[channel] = listener

    def check_listeners(self):
        remove: list[pygame.Channel] = []
        for chn, listener in self.channels_events.items():
            if not chn.get_busy():
                listener()
                remove.append(chn)

        for to_del in remove:
            del self.channels_events[to_del]

    def stop(self):
        pygame.mixer.music.stop()

    def update(self):
        if self.game.button_active:
            self.play_tick_tock(self.cur_btn_music)
        else:
            self.stop()

        self.check_listeners()
