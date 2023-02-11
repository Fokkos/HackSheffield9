import pygame
import constants

screenX = constants.SCREEN_X
screenY = constants.SCREEN_Y
item_size = 75

pygame.init()

font_name = pygame.font.Font('freesansbold.ttf', 25)
font_description = pygame.font.Font('freesansbold.ttf', 15)

inventory_bar = pygame.image.load("img/inventory/inventory.png")
item_height = screenY - (inventory_bar.get_height() / 2)


class InventorySprite(pygame.sprite.Sprite):
    def __init__(self, name, description, img_link, x) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_link), (item_size, item_size))
        self.name = name
        self.description = description
        self.rect = self.image.get_rect()
        self.rect.center = (x, item_height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# used to create the sprite objects according to the name provided
def createSprite(name, x):
    match name:
        case "book":    # do all sprites in this format! :)
            sprite = InventorySprite("book",
                                     "mysterious book found on shelf",
                                     "img/inventory/book.png",
                                     x)
            return sprite


# checks if mouse is hovering over sprite, if so, show description and name
def checkCollision(sprite, screen):
    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
        text_name = font_name.render(sprite.name, True, (0, 0, 0))
        text_description = font_description.render(sprite.description, True, (0, 0, 0))
        screen.blit(text_name,
                    ((screenX / 2) - (text_name.get_width() / 2),
                     screenY - inventory_bar.get_height() - 50))
        screen.blit(text_description,
                    ((screenX / 2) - (text_description.get_width() / 2),
                     screenY - inventory_bar.get_height() - 25))


# used to render each item in the players inventory
def render_inventory_bar(screen, inventory):
    x = 60
    dx = 88  # rough spacing to fit all items, can do maths later ig
    for item in inventory:
        sprite = createSprite(item, x)
        sprite.draw(screen)
        checkCollision(sprite, screen)
        x += dx
