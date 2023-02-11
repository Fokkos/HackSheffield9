import pygame


def getSprite(name):
    match name:
        case "book":
            return "img/book.png"


def render_inventory_bar(screen, inventory):
    x = 20
    y = 520
    dx = 88  # rough spacing to fit all items, can do maths later ig
    for item in inventory:
        sprite = pygame.transform.scale(pygame.image.load(getSprite(item)), (50, 50))
        screen.blit(sprite, (x, y))
        x += dx
