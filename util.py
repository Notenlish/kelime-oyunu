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
