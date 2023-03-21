# Importieren der Pygame-Bibliothek
import pygame
from random import*


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
pygame.display.set_caption("Unser erstes Pygame-Spiel")

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
    
    def move(self):
        if move == 'u':
            if self.pos[0] == [150, 90]:
                self.pos[0] = [200, 90]
                self.pos[1] = [300,190]
                self.pos[2] = [350,190]
            elif self.pos[0] == [200, 90]:
                self.pos[0] = [200,140]
                self.pos[1] = [200,190]
                self.pos[2] = [250,190]
            elif self.pos[0] == [200,140]:
                self.pos[0] = [150,140]
                self.pos[1] = [100,190]
                self.pos[2] = [150,190]
            elif self.pos[0] == [150,140]:
                self.pos[0] = [150, 90]
                self.pos[1] = [400,190]
                self.pos[2] = [50, 190]
            self.display()

cubicle0 = Cube([[150, 90],[400,190],[50, 190]],[0,4,1])
cubicle1 = Cube([[200, 90],[300,190],[350,190]],[0,3,4])
cubicle2 = Cube([[200,140],[200,190],[250,190]],[0,2,3])
cubicle3 = Cube([[150,140],[100,190],[150,190]],[0,1,2])
cubicle4 = Cube([[100,240],[150,240],[150,290]],[1,2,5])
cubicle5 = Cube([[200,290],[200,240],[250,240]],[5,2,3])
cubicle6 = Cube([[200,340],[300,240],[350,240]],[5,3,4])
cubicle7 = Cube([[50, 240],[400,240],[150,340]],[1,4,5])


# Schleife Hauptprogramm
move = 'none'
while spielaktiv:
    randomnr = randint(0,5)
    color = colors[randomnr]
    def outline():
        pygame.draw.rect(screen, SCHWARZ, [150, 90, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [200, 90, 50, 50],1)  
        pygame.draw.rect(screen, SCHWARZ, [200, 140, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [150, 140, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [50, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [50, 240, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [100, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [100, 240, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [150, 190, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [150, 240, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [200, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [200, 240, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [250, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [250, 240, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [300, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [300, 240, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [350, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [350, 240, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [400, 190, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [400, 240, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [150, 290, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [150, 340, 50, 50],1)
        pygame.draw.rect(screen, SCHWARZ, [200, 290, 50, 50],1)            
        pygame.draw.rect(screen, SCHWARZ, [200, 340, 50, 50],1)              
    

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("pressed 'QUIT'")
        elif event.type == pygame.KEYDOWN:
            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("pressed 'arrowright'")
                origin_X = origin_X + 10
            elif event.key == pygame.K_LEFT:
                print("pressed 'arrowleft'")
                origin_X = origin_X - 10
            elif event.key == pygame.K_UP:
                print("pressed 'arrowup'")
                origin_Y = origin_Y -10
            elif event.key == pygame.K_DOWN:
                print("pressed 'arrowdown'")
                origin_Y = origin_Y +10
            elif event.key == pygame.K_SPACE:
                print("pressed ' '")
                playerColor = color
            elif event.key == pygame.K_u:
                print('Spieler bewegt U')
                move = 'u'
            elif event.key == pygame.K_w:
                print("pressed 'w'")
                move = 'w'
                origin_Y = origin_Y -10
            elif event.key == pygame.K_a:
                print("pressed 'a'")
                move = 'a'
                origin_X = origin_X - 10
            elif event.key == pygame.K_s:
                print("pressed 's'")
                move = 's'
                origin_Y = origin_Y +10
            elif event.key == pygame.K_d:
                print("pressed 'd'")
                move = 'd'
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
    
    pieces = [[0,4,1],[0,3,4],[0,2,3],[0,1,2],[5,1,2],[5,2,3],[5,3,4],[5,4,1]]

    cubicle0.move()
    cubicle1.move()
    cubicle2.move()
    cubicle3.move()
    cubicle4.move()
    cubicle5.move()
    cubicle6.move()
    cubicle7.move()
    move = 'none'

    cubicle0.display()
    cubicle1.display()
    cubicle2.display()
    cubicle3.display()
    cubicle4.display()
    cubicle5.display()
    cubicle6.display()
    cubicle7.display()

    outline()
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()