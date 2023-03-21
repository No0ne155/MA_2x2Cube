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

# Schleife Hauptprogramm
while spielaktiv:
    randomnr = randint(0,5)
    color = colors[randomnr]

    def rCube():
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
        
        def piece0():
            pygame.draw.rect(screen, colors[0], [pos[0][0][0], pos[0][0][1], 50, 50])
            pygame.draw.rect(screen, colors[4], [pos[0][1][0], pos[0][1][1], 50, 50])
            pygame.draw.rect(screen, colors[1], [pos[0][2][0], pos[0][2][1], 50, 50])

        def piece1():
            pygame.draw.rect(screen, colors[0], [pos[1][0][0], pos[1][0][1], 50, 50])
            pygame.draw.rect(screen, colors[3], [pos[1][1][0], pos[1][1][1], 50, 50])
            pygame.draw.rect(screen, colors[4], [pos[1][2][0], pos[1][2][1], 50, 50])

        def piece2():
            pygame.draw.rect(screen, colors[0], [pos[2][0][0], pos[2][0][1], 50, 50])
            pygame.draw.rect(screen, colors[2], [pos[2][1][0], pos[2][1][1], 50, 50])
            pygame.draw.rect(screen, colors[3], [pos[2][2][0], pos[2][2][1], 50, 50])

        def piece3():
            pygame.draw.rect(screen, colors[0], [pos[3][0][0], pos[3][0][1], 50, 50])
            pygame.draw.rect(screen, colors[1], [pos[3][1][0], pos[3][1][1], 50, 50])
            pygame.draw.rect(screen, colors[2], [pos[3][2][0], pos[3][2][1], 50, 50])

        def piece4():
            pygame.draw.rect(screen, colors[1], [pos[4][0][0], pos[4][0][1], 50, 50])
            pygame.draw.rect(screen, colors[2], [pos[4][1][0], pos[4][1][1], 50, 50])
            pygame.draw.rect(screen, colors[5], [pos[4][2][0], pos[4][2][1], 50, 50])

        def piece5():
            pygame.draw.rect(screen, colors[5], [pos[5][0][0], pos[5][0][1], 50, 50])
            pygame.draw.rect(screen, colors[2], [pos[5][1][0], pos[5][1][1], 50, 50])
            pygame.draw.rect(screen, colors[3], [pos[5][2][0], pos[5][2][1], 50, 50])
            
        def piece6():
            pygame.draw.rect(screen, colors[5], [pos[6][0][0], pos[6][0][1], 50, 50])
            pygame.draw.rect(screen, colors[3], [pos[6][1][0], pos[6][1][1], 50, 50])
            pygame.draw.rect(screen, colors[4], [pos[6][2][0], pos[6][2][1], 50, 50])
           
        def piece7():
            pygame.draw.rect(screen, colors[1], [pos[7][0][0], pos[7][0][1], 50, 50])
            pygame.draw.rect(screen, colors[4], [pos[7][1][0], pos[7][1][1], 50, 50])
            pygame.draw.rect(screen, colors[5], [pos[7][2][0], pos[7][2][1], 50, 50])

        
        
        #piece0()
        #piece1()
        #piece2()
        #piece3()
        #piece4()
        #piece5()
        #piece6()
        #piece7()
        outline()

    class Cube:
        def __init__(self, pos, colors):
            self.pos = pos
            self.colors = colors

        def startup(self):
            pygame.draw.rect(screen, colors[self.colors[0]], [self.pos[0][0], self.pos[0][1], 50, 50])
            pygame.draw.rect(screen, colors[self.colors[1]], [self.pos[1][0], self.pos[1][1], 50, 50])
            pygame.draw.rect(screen, colors[self.colors[2]], [self.pos[2][0], self.pos[2][1], 50, 50])
        
    def move(posX, posY,  rota):
        if posX == 50:
            if posY == 190:
                if rota == 'U':
                    print('success')


    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
                origin_X = origin_X + 10
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
                origin_X = origin_X - 10
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
                origin_Y = origin_Y -10
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
                origin_Y = origin_Y +10
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")
                playerColor = color
            elif event.key == pygame.K_u:
                print('Spieler bewegt U')
                move(50, 190, 'U')


            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
                origin_Y = origin_Y -10
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
                origin_X = origin_X - 10
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
                origin_Y = origin_Y +10
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")
                origin_X = origin_X + 10

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
            playerColor = color

    # Spiellogik hier integrieren

    # Spielfeld/figuren zeichnen
    screen.fill(SCHWARZ)
    def player():
        pygame.draw.rect(screen, playerColor, [origin_X, origin_Y, 50, 50])
        pygame.draw.rect(screen, SCHWARZ, [origin_X, origin_Y, 50, 50],1)
    player()
    
    Cube
    pieces = [[0,4,1],[0,3,4],[0,2,3],[0,1,2],[5,1,2],[5,2,3],[5,3,4],[5,4,1]]
    cubicle0 = Cube([[150, 90],[400,190],[50, 190]],[0,4,1])
    cubicle1 = Cube([[200, 90],[300,190],[350,190]],[0,3,4])
    cubicle2 = Cube([[200,140],[200,190],[250,190]],[0,2,3])
    cubicle3 = Cube([[150,140],[100,190],[150,190]],[0,1,2])
    cubicle4 = Cube([[100,240],[150,240],[150,290]],[1,2,5])
    cubicle5 = Cube([[200,290],[200,240],[250,240]],[5,2,3])
    cubicle6 = Cube([[200,340],[300,240],[350,240]],[5,3,4])
    cubicle7 = Cube([[50, 240],[400,240],[150,340]],[1,4,5])

    cubicle0.startup()
    cubicle1.startup()
    cubicle2.startup()
    cubicle3.startup()
    cubicle4.startup()
    cubicle5.startup()
    cubicle6.startup()
    cubicle7.startup()
    rCube()
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()