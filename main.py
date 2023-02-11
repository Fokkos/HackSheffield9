import pygame
import random
from pygame import mixer

import sprites

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
showInventory = False
scene = "title"  # look into setting as a dictionary?

font = pygame.font.Font('freesansbold.ttf', 32)

# caption and icon
pygame.display.set_caption("kitty simulator >:3")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

# inventory
inventory = pygame.image.load("img/inventory.png")

# paw initial values
pawImg = pygame.image.load('img/paw.png')
pawX = 0
pawY = 0

catSound = mixer.Sound("sounds/miau.wav")
loreMusic = mixer.Sound("sounds/space-odyssey.wav")

# lore page assets
lore = pygame.image.load("img/lorem ipsum.png")
loreY = 75


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


def draw_inventory():
    screen.blit(inventory, (0, screenY - inventory.get_height()))

# title screen assets
startBtn = sprites.StartButton()

# bookshelf and bookpage objects
bookShelf = sprites.Bookshelf()
bookpage = sprites.BookPage()

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
        showInventory = True

        # displays book page
        if isBookOpened:
            bookShelf.pop_book(screen, bookpage)

    if showInventory:
        draw_inventory()

    paw(pawX, pawY)



    pygame.display.update()
