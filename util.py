import pygame


def draw_text(
    screen: pygame.Surface,
    pos: tuple[int, int],
    font: pygame.Font,
    text: str,
    antialias: bool,
    color: str | pygame.Color = "black",
    wraplength: int = 0,
):
    surf = font.render(text, antialias, color, wraplength=wraplength)
    screen.blit(surf, pos)


def size_of_text(font: pygame.Font, text: str):
    return font.render(text, True, "black").size


def scale_and_add_outline(rect: pygame.Rect, width: int):
    width *= 2
    orig = rect.center
    rect.width += width
    rect.height += width
    rect.center = orig
    return rect


def f_time_as_min(time: float):
    """Formats time as min."""
    mins = round(time) // 60
    seconds = round(time - (60 * mins))
    return f"{mins}:{seconds}"


def draw_text_in_rect(
    font: pygame.Font,
    text: str,
    rect: pygame.Rect,
    canvas: pygame.Surface,
    safe_width: int = 10,
):
    draw_text(
        canvas,
        rect.topleft,
        font,
        text,
        True,
        wraplength=max(rect.w - safe_width, 0),
    )
