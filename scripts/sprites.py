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
        createClass(self, "img/start_button.png", (200, 120), (400, 350))


class Bookshelf(GameSprite):
    def __init__(self) -> None:
        createClass(self, "img/bookshelf.png", (270, 240), (300, 270))

    def pop_book(self, screen, bookpage):
        bookpage.draw(screen)


class BookPage(GameSprite):
    def __init__(self) -> None:
        createClass(self, "img/bookpage_tutorial.png", (300, 300), (460, 220))
