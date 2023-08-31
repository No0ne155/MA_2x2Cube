import pygame
from random import*
import numpy as np

pygame.init()

#farben
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GELB    = (255,255,0)
BLAU    = (0,0,255)
CLR = (0, 255,255)

#pygame fenster
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("2x2 Cube Sim")
screen.fill(SCHWARZ)

class grid:
    def __init__(self, coord) -> None:
        self.coord = coord
    
    def draw_grid(self, coord):
        pygame.draw.circle(screen, CLR, ((300+coord[0]),(300+coord[1])), 5)


grid0 = grid([0,0])

#pygame loop vorbereiten
spielaktiv = True
clock = pygame.time.Clock()

while spielaktiv:
    # Key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("pressed 'QUIT'")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("pressed 'arrowright'")
            elif event.key == pygame.K_LEFT:
                print("pressed 'arrowleft'")
            elif event.key == pygame.K_UP:
                print("pressed 'arrowup'")
            elif event.key == pygame.K_DOWN:
                print("pressed 'arrowdown'")
            elif event.key == pygame.K_SPACE:
                print("pressed 'SPACE'")
            elif event.key == pygame.K_u:
                print("pressed 'u'")
            elif event.key == pygame.K_f:
                print("pressed 'f'")
            elif event.key == pygame.K_a:
                print("pressed 'a'")
            elif event.key == pygame.K_s:
                print("pressed 's'")
            elif event.key == pygame.K_d:
                print("pressed 'd'")
            elif event.key == pygame.K_w:
                print("pressed 'w'")
                screen.fill(SCHWARZ)
            elif event.key == pygame.K_ESCAPE:
                print("pressed 'esc'")
                spielaktiv = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked mouse")


    grid0.draw_grid([0,0])
    #logik
    
    #Fenster aktualisieren
    pygame.display.flip()

    #Framerate festlegen
    clock.tick(60)

pygame.quit()

