import pygame
import random
from pygame import mixer

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

# paw
pawImg = pygame.image.load('img/paw.png')
pawX = 0
pawY = 0

catSound = mixer.Sound("sounds/miau.wav")

# title screen assets
startBtn = pygame.image.load('img/start_button.png')
startBtnRect = pygame.Rect((screenX / 2) - (startBtn.get_width() / 2), 300, (screenX / 2) - (startBtn.get_width() / 2) + 200, 420)

def meowRNG():
    roll = random.randint(0, 5)
    if roll > 3:
        catSound.play()


def paw(x, y):
    screen.blit(pawImg, (x, y))


def title_text():
    text = font.render("kitty simulator >:3", True, (255, 255, 255))
    screen.blit(text, (200, 200))


def start_button():
    screen.blit(startBtn, ((screenX / 2) - (startBtn.get_width() / 2), 300))

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
            meowRNG()
        elif event.type == pygame.MOUSEBUTTONUP:
            pawImg = pygame.image.load('img/paw.png')
            catSound.stop()

        if scene == "title":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startBtnRect.collidepoint(pygame.mouse.get_pos()):
                    print("start button pressed")
                    scene = "living-room"

    if scene == "title":
        title_text()
        start_button()
    elif scene == "living-room":
        background = pygame.image.load('img/living-room.png')
        screen.blit(background, (0, 0))


    paw(pawX, pawY)
    pygame.display.update()
