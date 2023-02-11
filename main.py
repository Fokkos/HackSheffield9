import pygame
import random
from pygame import mixer

# TODO:
# name. the. cat.
# come up with final title of game
# create better looking title screen
# write the lore at the start of the game
# create an abstract class for Sprites
# draw sprites and environments
# work out interactions
# inventory system (decide whether always visible or toolbar (i.e. minecraft))
# come up with "win conditions"
# make endings depending on what player does

# initialise pygame
pygame.init()

# create the screen
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))  # make cursor invisible
start = False
scene = "title"  # look into setting as a dictionary?

font = pygame.font.Font('freesansbold.ttf', 32)

# caption and icon
pygame.display.set_caption("kitty simulator >:3")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

# paw initial values
pawImg = pygame.image.load('img/paw.png')
pawX = 0
pawY = 0

catSound = mixer.Sound("sounds/miau.wav")
loreMusic = mixer.Sound("sounds/space-odyssey.wav")

# lore page assets
lore = pygame.image.load("img/lorem ipsum.png")
loreY = 0


# plays the meow sound with a probability of 1/n+1
def meowRNG(n):
    roll = random.randint(0, n)
    if roll == 0:
        catSound.play()


def paw(x, y):
    screen.blit(pawImg, (x, y))


def title_text():
    text = font.render("kitty simulator >:3", True, (255, 255, 255))
    screen.blit(text, (200, 200))


def show_lore(y):
    screen.blit(lore, (0, y))


class StartButton(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/start_button.png")
        self.rect = self.image.get_rect()
        self.rect.center = (screenX / 2, 350)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# bookshelf class
class Bookshelf(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/bookshelf.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 220)

    def pop_book(self, screen, bookpage):
        bookpage.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# bookpage class
class Bookpage(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("img/bookpage_tutorial.png")
        self.rect = self.image.get_rect()
        self.rect.center = (460, 220)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# title screen assets
startBtn = StartButton()

# bookshelf and bookpage objects
bookShelf = Bookshelf()
bookpage = Bookpage()

# sets if book is clicked from the shelf
isBookOpened = False
# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mousePosX, mousePosY = pygame.mouse.get_pos()
            pawX = mousePosX - (pawImg.get_width() / 2)
            pawY = mousePosY - 50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pawImg = pygame.image.load('img/paw_claw.png')
            meowRNG(5)
        elif event.type == pygame.MOUSEBUTTONUP:
            pawImg = pygame.image.load('img/paw.png')
            catSound.stop()

        if scene == "title":
            if startBtn.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("start button pressed")
                    loreMusic.play()
                    scene = "exposition"
                else:
                    startBtn.image = pygame.image.load("img/start_button-hover.png")
            else:
                startBtn.image = pygame.image.load("img/start_button.png")



        elif scene == "exposition":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space button pressed")
                    scene = "living-room"
                    loreMusic.stop()

        elif scene == "living-room":

            # checks if bookshelf or page is clicked on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bookShelf.rect.collidepoint(pygame.mouse.get_pos()):
                    print("book pressed")
                    isBookOpened = True
                elif bookpage.rect.collidepoint(pygame.mouse.get_pos()):
                    print("book scratched")
                    isBookOpened = False

    if scene == "title":
        title_text()
        startBtn.draw(screen)
    elif scene == "exposition":
        show_lore(loreY)
        loreY -= .3
    elif scene == "living-room":
        background = pygame.image.load('img/living-room.png')
        screen.blit(background, (0, 0))
        bookShelf.draw(screen)

        # displays book page
        if isBookOpened:
            bookShelf.pop_book(screen, bookpage)

    paw(pawX, pawY)
    pygame.display.update()
