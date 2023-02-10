import pygame
import random

#Initialise pygame
pygame.init()

# create the screen
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))


font = pygame.font.Font('freesansbold.ttf', 32)

# Caption and Icon
pygame.display.set_caption("HackSheffield9 game (WIP)")
# icon = pygame.image.load('ufo.png') SET LATER
# pygame.display.set_icon(icon)

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
    temp_text(300, 200)
    pygame.display.update()