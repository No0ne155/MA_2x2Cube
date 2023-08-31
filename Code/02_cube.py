import pygame
from random import*
import numpy as np

#Pygame initialisieren
pygame.init()

#farben
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GELB    = (255,255,0)
BLAU    = (0,0,255)

#pygame fenster
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2x2 Cube Sim")
screen.fill(SCHWARZ)

#pygame loop vorbereiten
spielaktiv = True
clock = pygame.time.Clock()

class Cube:
    def __init__(self, colors, posvec) -> None:
        self.posvec = posvec
        self.colors = colors
 
    def display(self):
        if self.posvec == (1,1,1):
            pygame.draw.polygon(screen, self.colors[0], [[400,300], [487, 250], [400, 200], [313, 250]], 0)
            pygame.draw.polygon(screen, self.colors[1], [[400,300], [400, 400], [487, 350], [487, 250]], 0)
            pygame.draw.polygon(screen, self.colors[2], [[400,300], [400, 400], [313, 350], [313, 250]], 0)
            
        elif self.posvec == (1,-1,1):
            pygame.draw.polygon(screen, self.colors[1], [[400,530], [487, 480], [400, 430], [313, 480]], 0)
            pygame.draw.polygon(screen, self.colors[0], [[400,500], [400, 400], [487, 350], [487, 450]], 0)
            pygame.draw.polygon(screen, self.colors[2], [[400,500], [400, 400], [313, 350], [313, 450]], 0)
            
        elif self.posvec == (-1,-1,1):
            pygame.draw.polygon(screen, self.colors[1], [[400,530], [487, 480], [400, 430], [313, 480]], 0)
            pygame.draw.polygon(screen, self.colors[2], [[313,350], [313, 450], [326, 400], [326, 300]], 0)
            pygame.draw.polygon(screen, self.colors[0], [[400,500], [400, 400], [313, 350], [313, 450]], 0)
            


cube1 = Cube([WEISS, BLAU, ROT], ( 1, 1, 1))
cube2 = Cube([BLAU, GELB, ROT],  ( 1,-1, 1))
cube3 = Cube([ROT, GELB, GRUEN], (-1,-1, 1))


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
                cube1.display()
                cube2.display()
                #cube3.display()
            elif event.key == pygame.K_u:
                print("pressed 'u'")
            elif event.key == pygame.K_f:
                print("pressed 'f'")
                origin_Y = origin_Y -10
            elif event.key == pygame.K_a:
                print("pressed 'a'")
                origin_X = origin_X - 10
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



    #logik
    
    #Fenster aktualisieren
    pygame.display.flip()

    #Framerate festlegen
    clock.tick(60)

pygame.quit()
