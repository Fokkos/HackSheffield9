import pygame
import random
import time
from pygame import mixer

from scripts import render_inventory, sprites
import constants

# TODO:
# name. the. cat.
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
# pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))  # make cursor invisible
start = False
show_inventory = False
scene = "title"  # look into setting as a dictionary?

font = pygame.font.Font('freesansbold.ttf', 32)

# caption and icon
pygame.display.set_caption("kitty simulator >:3")
icon = pygame.image.load('img/icon.jpg')
pygame.display.set_icon(icon)

# inventory
inventory_bar = pygame.image.load("img/inventory/inventory.png")
inventory = []

# paw initial values
paw_img = pygame.image.load('img/player/Paw.png')
pawX = 0
pawY = 0

cat_sound = mixer.Sound("sounds/miau.wav")
tear_sound = mixer.Sound("sounds/tear.wav")
chomp_sound = mixer.Sound("sounds/chomp.wav")

# title screen assets
title_screen = pygame.image.load("img/title-screen/title_screen.png")
start_button = sprites.StartButton()

# lore page assets
lore_music = mixer.Sound("sounds/space-odyssey.wav")
lore = pygame.image.load("img/lore-screen/lorem ipsum.png")
loreY = 75

# living room assets
state_bookshelf = "default"
state_bookshelf_bottom = "default"
state_armchair = "default"
state_blue_book = "invisible"
state_sage_book = "invisible"

bookshelf = sprites.Bookshelf()
blue_book = sprites.BlueBook()
sage_book = sprites.SageBook()


# sets the background size and position taking inventory bar into account
def set_background(img_link):
    screen.blit(pygame.transform.scale(pygame.image.load(img_link), (800, 500)), (0, 0))


# plays the meow sound with a probability of 1/n+1
def meow_rng(n):
    roll = random.randint(0, n)
    if roll == 0:
        cat_sound.play()


def paw(x, y):
    screen.blit(paw_img, (x, y))


def show_lore(y):
    screen.blit(lore, (0, y))


def draw_inventory():
    screen.blit(inventory_bar, (0, screenY - inventory_bar.get_height()))


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
            pawX = mousePosX - (paw_img.get_width() / 2)
            pawY = mousePosY - 50
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            paw_img = pygame.image.load('img/player/paw_claw.png')
            meow_rng(5)
        elif event.type == pygame.MOUSEBUTTONUP:
            paw_img = pygame.image.load('img/player/Paw.png')
            cat_sound.stop()

        if scene == "title":
            if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("start button pressed")
                    lore_music.play()
                    scene = "exposition"
                else:
                    start_button.setImage("img/title-screen/start_button-hover.png", (150, 90))
            else:
                start_button.setImage("img/title-screen/start_button.png", (150, 90))

        elif scene == "exposition":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space button pressed")
                    scene = "living-room"
                    lore_music.stop()

        elif scene == "living-room":
            # book state logic
            if state_blue_book == "visible":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(100, 50, 600, 400).collidepoint(pygame.mouse.get_pos()):
                        state_blue_book = "eaten"
                        chomp_sound.play()
            elif state_blue_book == "eaten":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not pygame.Rect(100, 50, 600, 400).collidepoint(pygame.mouse.get_pos()):
                        state_blue_book = "invisible-eaten"

            if state_sage_book == "visible":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(100, 50, 600, 400).collidepoint(pygame.mouse.get_pos()):
                        state_sage_book = "torn"
                        tear_sound.play()
            elif state_sage_book == "torn":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not pygame.Rect(100, 50, 600, 400).collidepoint(pygame.mouse.get_pos()):
                        state_sage_book = "invisible-torn"

            # bookshelf logic
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(138, 193, 35, 60).collidepoint(pygame.mouse.get_pos()):
                    if state_blue_book == "invisible":
                        state_blue_book = "visible"
                    else:
                        state_blue_book = "eaten"
                elif pygame.Rect(187, 265, 40, 75).collidepoint(pygame.mouse.get_pos()):
                    if state_sage_book == "invisible":
                        state_sage_book = "visible"
                    else:
                        state_sage_book = "torn"

            if state_bookshelf_bottom == "default":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(77, 334, 279, 421).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf_bottom = "knocked"
                    else:
                        state_bookshelf = "default"
                else:   #hover
                    if pygame.Rect(73, 341, 200, 65).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "init_light_bottom_shelf"
                    elif pygame.Rect(138, 193, 35, 60).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "init_light_dark_blue"
                    elif pygame.Rect(187, 265, 40, 75).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "init_light_sage"
                    else:
                        state_bookshelf = "default"
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(208, 344, 50, 50).collidepoint(pygame.mouse.get_pos()):
                        print("implement keypad")
                else:   #hover
                    if pygame.Rect(208, 344, 50, 50).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "final_light_keypad"
                    elif pygame.Rect(138, 193, 35, 60).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "final_light_dark_blue"
                    elif pygame.Rect(187, 265, 40, 75).collidepoint(pygame.mouse.get_pos()):
                        state_bookshelf = "final_light_sage"
                    else:
                        state_bookshelf = "final_nolight"

            bookshelf.changeState(state_bookshelf)





    if scene == "title":
        screen.blit(title_screen, (0, 0))
        start_button.draw(screen)
    elif scene == "exposition":
        show_lore(loreY)
        loreY -= .3
    elif scene == "living-room":

        set_background('img/living-room/living-room.png')
        bookshelf.draw(screen)
        show_inventory = True

        if state_blue_book == "visible" or state_blue_book == "eaten":
            blue_book.draw(screen)
        if state_blue_book == "eaten":
            blue_book.changeState("eaten")

        if state_sage_book == "visible" or state_sage_book == "torn":
            sage_book.draw(screen)
        if state_sage_book == "torn":
            sage_book.changeState("torn")

    if show_inventory:
        draw_inventory()
        if len(inventory) > 0:
            render_inventory.render_inventory_bar(screen, inventory)

    paw(pawX, pawY)

    pygame.display.update()
