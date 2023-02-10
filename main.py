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

def temp_text(x, y):
    text = font.render("HACKSHEFFIELD 9!!!!!" , True, (255, 255, 255))
    screen.blit(text, (x, y))

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
            start = True
            mousePosX, mousePosY = pygame.mouse.get_pos()
            pawX = mousePosX - (pawImg.get_width() / 2)
            pawY = mousePosY - 100




    if start == False:
        temp_text(300, 200)
    else:
        paw(pawX, pawY)
    pygame.display.update()