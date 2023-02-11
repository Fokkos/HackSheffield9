import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../img/icon.jpg"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def setImage(self, img_link, size):
        self.image = pygame.transform.scale(pygame.image.load(img_link), size)


def createClass(sprite, img_link, size, pos):
    sprite.image = pygame.transform.scale(pygame.image.load(img_link), size)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = pos


class StartButton(GameSprite):
    def __init__(self) -> None:
        createClass(self, "img/title-screen/start_button.png", (200, 120), (130, 340))


class Bookshelf(GameSprite):
    def __init__(self) -> None:
        size = (250, 350)
        pos = (185, 260)
        createClass(self, "img/living-room/bookshelf_default.png", size, pos)

    def pop_book(self, screen, bookpage):
        bookpage.draw(screen)

    # changes the state of the bookshelf
    def changeState(self, state):
        if state == "default":
            self.setImage("img/living-room/bookshelf_default.png", (250, 350))
        elif state == "init_light_bottom_shelf":
            self.setImage("img/living-room/bookshelf_initial_light_bottom_shelf.png", (250, 350))
        elif state == "final_light_keypad":
            self.setImage("img/living-room/bookshelf_final_light_keypad.png", (250, 350))
        elif state == "final_nolight":
            self.setImage("img/living-room/bookshelf_final_nolight.png", (250, 350))


class BookPage(GameSprite):
    def __init__(self) -> None:
        createClass(self, "img/living-room/bookpage_tutorial.png", (50, 50), (600, 220))
