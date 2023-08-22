# Importieren der Pygame-Bibliothek
import pygame
from random import*
import numpy as np

#Matrizen
#Rotations Matrix
#numpy


# initialisieren von pygame
pygame.init()

#farben definieren
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GELB    = (255,255,0)
BLAU    = (0,0,255)

# Fenster öffnen
screen = pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption("2x2 Cube Sim")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Spielfeld färben
colors = [WEISS, ORANGE, GRUEN, ROT, BLAU, GELB]
screen.fill(SCHWARZ)
origin_X = 10
origin_Y = 20
playerColor = SCHWARZ

pos       = [[[150, 90],[400,190],[50, 190]],
             [[200, 90],[300,190],[350,190]],
             [[200,140],[200,190],[250,190]],
             [[150,140],[100,190],[150,190]],
             [[100,240],[150,240],[150,290]],
             [[200,290],[200,240],[250,240]],
             [[200,340],[300,240],[350,240]],
             [[50, 240],[400,240],[150,340]]]

class Cube:
    def __init__(self, pos, colors):
        self.pos = pos
        self.colors = colors
        
    def display(self):
        pygame.draw.rect(screen, colors[self.colors[0]], [self.pos[0][0], self.pos[0][1], 50, 50])
        pygame.draw.rect(screen, colors[self.colors[1]], [self.pos[1][0], self.pos[1][1], 50, 50])
        pygame.draw.rect(screen, colors[self.colors[2]], [self.pos[2][0], self.pos[2][1], 50, 50])

cubicle1 = Cube((1,1,1), [WEISS, ROT, GRUEN])


# Schleife Hauptprogramm
move = 'none'
while spielaktiv:
    randomnr = randint(0,5)
    color = colors[randomnr]
    
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("pressed 'QUIT'")
        elif event.type == pygame.KEYDOWN:
            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("pressed 'arrowright'")
            elif event.key == pygame.K_LEFT:
                print("pressed 'arrowleft'")
            elif event.key == pygame.K_UP:
                print("pressed 'arrowup'")
            elif event.key == pygame.K_DOWN:
                print("pressed 'arrowdown'")
            elif event.key == pygame.K_SPACE:
                print("pressed ' '")
                playerColor = color
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
                origin_Y = origin_Y +10
            elif event.key == pygame.K_d:
                print("pressed 'd'")
                origin_X = origin_X + 10

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked mouse")
            playerColor = color

    # Spiellogik hier integrieren

    # Spielfeld/figuren zeichnen
    screen.fill(SCHWARZ)
    def player():
        pygame.draw.rect(screen, playerColor, [origin_X, origin_Y, 50, 50])
        pygame.draw.rect(screen, SCHWARZ, [origin_X, origin_Y, 50, 50],1)
    player()
    
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()