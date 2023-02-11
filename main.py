import pygame
import random
from pygame import mixer

from scripts import render_inventory, sprites
import constants

# TODO:
# name. the. cat.
# come up with final title of game
# create better looking title screen
# write the lore at the start of the game
# draw sprites and environments
# work out interactions
# inventory system (decide whether always visible or toolbar (i.e. minecraft))
# come up with "win conditions"
# make endings depending on what player does

# initialise pygame
pygame.init()

# create the screen
screenX = constants.SCREEN_X
screenY = constants.SCREEN_Y
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
inventory_bar = pygame.image.load("img/inventory.png")
inventory = []

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
    screen.blit(inventory_bar, (0, screenY - inventory_bar.get_height()))


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
                    startBtn.setImage("img/start_button-hover.png", (200, 120))
            else:
                startBtn.setImage("img/start_button.png", (200, 120))



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
            if "book" not in inventory:
                inventory.append("book")

    if showInventory:
        draw_inventory()
        if len(inventory) > 0:
            render_inventory.render_inventory_bar(screen, inventory)

    paw(pawX, pawY)

    pygame.display.update()
