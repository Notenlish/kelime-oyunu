import pygame
import mili  # type: ignore

from const import SC_RECT
from typing import TYPE_CHECKING

from util import draw_text


if TYPE_CHECKING:
    from main import App


class UI:
    def __init__(self, app: "App") -> None:
        self.app = app
        self.game = app.game
        self.canvas = self.app.sc
        self.mili = mili.MILI(self.canvas)

        self.ali_varol = pygame.image.load("assets/ali-ihsan-varol.png").convert_alpha()

    def _ui(self):
        m = self.mili
        m.start({"padx": 0, "pady": 0})
        with m.begin(
            SC_RECT, {"padx": 0, "pady": 0, "axis": "x", "clip_draw": False}
        ):  # main
            m.rect({"padx": 0, "pady": 0, "color": "#D3DAE2", "border_radius": 0})
            with m.begin(
                None, {"filly": "100", "padx": 5, "pady": 5, "fillx": "70"}
            ):  # left
                with m.begin(
                    None,
                    {
                        "fillx": "100",
                        "filly": "100",
                        "pady": "25",
                        "padx": 10,  # normally we wouldnt need to do this, but mili ui is buggy.
                        "axis": "y",
                    },
                ):  # left inner
                    with m.begin(
                        None,
                        {
                            "fillx": "100",
                            "filly": "30",
                            "pady": "0",
                            "padx": 0,
                            "axis": "y",
                        },
                    ):  # topleft
                        # m.rect({"color": (180,) * 3,"padx": 0,"pady": 0,"border_radius": 2,})
                        with m.begin(
                            None, {"fillx": "100", "filly": "50"}, get_data=True
                        ) as score_cont:  # s
                            r = score_cont.absolute_rect

                            draw_text(
                                self.canvas,
                                r.topleft,
                                self.game.font,
                                f"Total: {self.game.total_score}   Score: {self.game.active_word.score}",
                                True,
                            )
                        with m.begin(
                            None, {"fillx": "100", "filly": "50"}, get_data=True
                        ) as letters_cont:  # s
                            r = pygame.Vector2(letters_cont.absolute_rect.topleft)
                            for l in self.game.active_word.letters:
                                sep = 10
                                l.render(r, self.canvas)
                                r.x += l.bg_rect_size.x + sep
            with m.begin(
                None, {"filly": "100", "padx": 5, "pady": 5, "fillx": "30"}
            ):  # right
                with m.begin(None, {"fillx": "100", "filly": "100"}):  # right in
                    m.image(self.ali_varol)

    def render(self):
        self.mili.update_draw()
        self._ui()
