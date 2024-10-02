import pygame
import mili  # type: ignore

from const import SC_RECT
from typing import TYPE_CHECKING
from math import sin

from game import Game
from util import draw_text, draw_text_in_rect


if TYPE_CHECKING:
    from main import App


class GameUI:
    def __init__(self, app: "App") -> None:
        self.app = app
        self.game: Game = app.game  # type:ignore
        self.canvas = self.app.sc
        self.mili = mili.MILI(self.canvas)

        self.ali_varol = pygame.image.load("assets/ali-ihsan-varol.png").convert_alpha()

    def _ui_top(self): ...

    def _ui_bottom(self):
        m = self.mili
        with m.begin(
            None,
            {
                "axis": "x",
                "padx": 0,
                "pady": 0,
                "fillx": "100",
                "filly": "100",
                "clip_draw": False,
            },
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
                        "pady": "10",
                        "padx": 10,  # normally we wouldnt need to do this, but mili ui is buggy.
                        "axis": "y",
                    },
                ):  # left inner
                    with m.begin(None, {"filly": "30"}):
                        ...
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
                            for l in self.game.active_word.letters:  # noqa E741
                                sep = 10
                                l.render(r, self.canvas)
                                r.x += l.bg_rect_size.x + sep
                    with m.begin(None, {"filly": "10"}):
                        ...
                    with m.begin(
                        None, {"filly": "50", "fillx": "100"}, get_data=True
                    ) as desc_cont:
                        self.game.active_word.draw_desc(
                            desc_cont.absolute_rect.move(5, 3),
                            self.canvas,  # type:ignore
                        )
                        m.rect(
                            {
                                "color": "#E7ECEE",
                                "border_radius": 2,
                                "padx": 2,
                                "pady": 2,
                            }
                        )
                        m.rect(
                            {
                                "color": "#C5D2D4",
                                "outline": 1,
                                "border_radius": 2,
                                "padx": 2,
                                "pady": 2,
                            }
                        )
            with m.begin(
                None, {"filly": "100", "padx": 5, "pady": 5, "fillx": "30"}
            ):  # right
                with m.begin(None, {"fillx": "100", "filly": "100"}):  # right in
                    m.image(self.ali_varol)

    def _ui(self):
        m = self.mili
        m.start({"padx": 0, "pady": 0})
        with m.begin(SC_RECT, {"padx": 0, "pady": 0, "axis": "y", "clip_draw": False}):
            m.rect({"color": "#D3DAE2", "border_radius": 0})
            with m.begin(
                None,
                {"fillx": "100", "filly": "20", "pady": 0, "padx": 0},
            ):  # skorlar cart curt
                self._ui_top()
            with m.begin(
                None, {"fillx": "100", "filly": "80", "pady": 0, "padx": 0}
            ):  # alt kısım
                self._ui_bottom()

    def render(self):
        self.mili.update_draw()
        self._ui()


class StartUI:
    def __init__(self, app: "App") -> None:
        self.app = app
        self.canvas = self.app.sc
        self.mili = mili.MILI(self.canvas)

        self.bg = pygame.image.load("assets/bg.png").convert()
        self.title = pygame.image.load("assets/title.png").convert_alpha()
        self.aiv1 = pygame.image.load("assets/aiv1.png").convert_alpha()
        self.aiv2 = pygame.image.load("assets/aiv2.png").convert_alpha()
        self.aiv2 = pygame.transform.rotate(self.aiv2, 60)

        self.font = pygame.Font("assets/AfacadFlux.ttf", 22)

    def _ui(self):
        m = self.mili
        m.start({"padx": 0, "pady": 0})
        with m.begin(
            SC_RECT,
            {"padx": 0, "pady": 0, "axis": "y"} | mili.CENTER,
        ):
            m.image(self.bg)
            with m.begin(
                None,
                {
                    "padx": 0,
                    "pady": 0,
                    "fillx": "100",
                    "filly": "100",
                    "axis": "y",
                    "align": "last",
                }
                | mili.CENTER,
            ):
                with m.begin(
                    None,
                    {
                        "padx": 0,
                        "pady": 0,
                        "fillx": self.title.width,
                        "filly": self.title.height,
                        "axis": "y",
                        "align": "center",
                    },
                ):
                    m.image(self.title)
            with m.begin(
                None,
                {"padx": 0, "pady": 0, "fillx": "100", "filly": "100"} | mili.CENTER,
            ):
                # m.rect({"outline": 2, "color": "white"})
                with m.begin(
                    None,
                    {"padx": 5, "pady": 5, "fillx": "45", "filly": "50"} | mili.CENTER,
                    get_data=True,
                ) as cont:
                    r = cont.absolute_rect

                    m.rect({"color": "white"})
                    draw_text_in_rect(
                        self.font, "Welcome To WordGame IBDP Edition!", r, self.canvas
                    )

    def _weirds(self):
        """Draws the objects that are positioned weirdly"""
        offset = sin(self.app.elapsed * 2) * 10
        self.canvas.blit(self.aiv1, (0, 150 + offset))
        self.canvas.blit(self.aiv2, (440, 15 - offset))

    def render(self):
        self.mili.update_draw()
        self._ui()
        self._weirds()
