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
                "btn-click": "btn-click.ogg",
                "transition": "transition.mp3",
                "press-btn": "btn-click.mp3",
                "loop": "loop.ogg",
                "get-letter": "num-go-up.ogg",
                "correct-guess": "num-go-up.ogg",
            }.items()
        }

        self.current = None

    @property  # could this be a normal getter? yep. I like using this though.
    def cur_btn_music(self):
        if not self.game.button_active:
            raise Exception("Cannot be called while button is not active!")
        t = self.game.button_time
        if t < 15:
            return "assets/sounds/fast.ogg"
        else:
            return "assets/sounds/empty.ogg"

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

        print("playing sound")
        channel = self.sounds[name].play()
        self.channels_events[channel] = listener

    def play_looping(self, name: str, listener: SoundEventListener | None = None):
        def _(): ...

        if not listener:
            listener = _

        s = self.sounds[name]
        channel = s.play(loops=-1)
        self.channels_events[channel] = listener

    def stop_looping(self, name: str):
        self.sounds[name].stop()

    def check_listeners(self):
        remove: list[pygame.Channel] = []
        for chn, listener in self.channels_events.items():
            if chn:
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
