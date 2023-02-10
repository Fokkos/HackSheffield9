import pygame
import random

#Initialise pygame
pygame.init()

# create the screen
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))    #make cursor invisible
start = False


font = pygame.font.Font('freesansbold.ttf', 32)

# Caption and Icon
pygame.display.set_caption("HackSheffield9 game (WIP)")
# icon = pygame.image.load('ufo.png') SET LATER
# pygame.display.set_icon(icon)

#Paw
pawImg = pygame.image.load('img\paw.png')
pawX = 0
pawY = 0

def paw(x, y):
    screen.blit(pawImg, (x, y))

def temp_text():
    text = font.render("kitty simulator >:3", True, (255, 255, 255))
    screen.blit(text, (200, 200))
    text = font.render("press space to start", True, (255, 255, 255))
    screen.blit(text, (200, 250))

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
            pawY = mousePosY - 100
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pawImg = pygame.image.load('img\paw_claw.png')
        elif event.type == pygame.MOUSEBUTTONUP:
            pawImg = pygame.image.load('img\paw.png')





    if start == False:
        temp_text()
    else:
        paw(pawX, pawY)
    pygame.display.update()