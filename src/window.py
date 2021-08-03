import pygame
from pygame import display, font
pygame.init()
font.init() # you have to call this at the start, 


(width, height) = (1280, 720)
screen = display.set_mode((width, height))

myfont = pygame.font.SysFont('Monospace', 30)


def showText(text):
    textsurface = myfont.render(text, False, (255,255,0))
    screen.blit(textsurface,(0,0))

def showWindow(running):
    display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False