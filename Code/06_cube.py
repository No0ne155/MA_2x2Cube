# Imports
import pygame
from math import*
import numpy as np

# Colors
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
GELB    = (255,255,0)
BLAU    = (0,0,255)
CLR = (0, 255,255)
WINDOW_SIZE =  600

# Variables
scale = 100
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()
center = [(WINDOW_SIZE/2),(WINDOW_SIZE/2)]

# Centerpoints
xp = np.array([ 1.0,0.0,0.0])
xn = np.array([-1.0,0.0,0.0])
yp = np.array([0.0, 1.0,0.0])
yn = np.array([0.0,-1.0,0.0])
zp = np.array([0.0,0.0, 1.0])
zn = np.array([0.0,0.0,-1.0])

# Class Cube
class Cube:
    def __init__(self,vec, vec1, vec2, vec3, p4,p5,p6, coX, coY, coZ, nr) -> None:
        # Vector from Center to Corner
        self.vec = vec 
        # Vectors from Corners to Edges
        self.vecx = vec1 + vec
        self.vecy = vec2 + vec
        self.vecz = vec3 + vec
        # Vectors from Center to Middle
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        # Colors for X, Y and Z
        self.coX = coX
        self.coY = coY
        self.coZ = coZ
        
        self.nr = nr

    # Rotationalgorithm for all points
    def rotate(self, angle, axis):
            rad = angle * pi / 180.0
            c = cos(rad)
            s = sin(rad)
            x = self.vec[0]
            y = self.vec[1]
            z = self.vec[2]
            xx = self.vecx[0]
            xy = self.vecx[1]
            xz = self.vecx[2]
            yx = self.vecy[0]
            yy = self.vecy[1]
            yz = self.vecy[2]
            zx = self.vecz[0]
            zy = self.vecz[1]
            zz = self.vecz[2]
            p4x = self.p4[0]
            p4y = self.p4[1]
            p4z = self.p4[2]
            p5x = self.p5[0]
            p5y = self.p5[1]
            p5z = self.p5[2]
            p6x = self.p6[0]
            p6y = self.p6[1]
            p6z = self.p6[2]
            if axis == 'x':
                self.vec[1] = y * c - z * s
                self.vec[2] = y * s + z * c
                self.vecx[1] = xy * c - xz * s
                self.vecx[2] = xy * s + xz * c
                self.vecy[1] = yy * c - yz * s
                self.vecy[2] = yy * s + yz * c
                self.vecz[1] = zy * c - zz * s
                self.vecz[2] = zy * s + zz * c
                self.p4[1] = p4y * c - p4z * s
                self.p4[2] = p4y * s + p4z * c
                self.p5[1] = p5y * c - p5z * s
                self.p5[2] = p5y * s + p5z * c
                self.p6[1] = p6y * c - p6z * s
                self.p6[2] = p6y * s + p6z * c
            elif axis == 'y':
                self.vec[0] = x * c + z * s
                self.vec[2] = -x * s + z * c
                self.vecx[0] = xx * c + xz * s
                self.vecx[2] = -xx * s + xz * c
                self.vecy[0] = yx * c + yz * s
                self.vecy[2] = -yx * s + yz * c
                self.vecz[0] = zx * c + zz * s
                self.vecz[2] = -zx * s + zz * c
                self.p4[0] = p4x * c + p4z * s
                self.p4[2] = -p4x * s + p4z * c
                self.p5[0] = p5x * c + p5z * s
                self.p5[2] = -p5x * s + p5z * c
                self.p6[0] = p6x * c + p6z * s
                self.p6[2] = -p6x * s + p6z * c

    # Drawing points
    def drawpoint(self):
        pygame.draw.circle(window, (255, 0, 0), (self.vec[0] *100+300, self.vec[1] *100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecx[0]*100+300, self.vecx[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecy[0]*100+300, self.vecy[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecz[0]*100+300, self.vecz[1]*100+300),5)
        pygame.draw.circle(window, (255,0,255), (self.p4[0]*100+300, self.p4[1]*100+300),5)
        pygame.draw.circle(window, (255,0,255), (self.p5[0]*100+300, self.p5[1]*100+300),5)
        pygame.draw.circle(window, (255,0,255), (self.p6[0]*100+300, self.p6[1]*100+300),5)
        
    # Drawing lines
    def connectpt(self, x2,y2):
        x1 = (self.vec[0] * 100) + WINDOW_SIZE/2
        y1 = (self.vec[1] * 100) + WINDOW_SIZE/2
        x2 = (x2 * scale) + WINDOW_SIZE/2
        y2 = (y2 * scale) + WINDOW_SIZE/2
        pygame.draw.line(window, (255, 255, 255), (x1, y1),(x2,y2))
    
    # Resetting the Cube
    def setzero(self,vec):
        self.vec = vec

    #Color fill algorithm
    def fill(self):
        sor = []
        sor.append([self.p4[2],4])
        sor.append([self.p5[2],5])
        sor.append([self.p6[2],6])
        solt = sorted(sor, key=lambda x: x[0], reverse=True)
        if solt[0][1]==4:
            pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
            if solt[1][1]==5:
                pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])
                pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
            elif solt[1][1]==6:
                pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
                pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])
        elif solt[0][1]==5:
            pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])
            if solt[1][1]==4:
                pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
                pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
            elif solt[1][1]==6:
                pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
                pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
            
        elif solt[0][1]==6:
            pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
            if solt[1][1]==4:
                pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
                pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])
            elif solt[1][1]==5:
                pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])
                pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
        
    def turn(self, turn):
        if turn == 'r':
            if self.vec[0] >0:
                ax = self.p4*10
                self.vec = rot(self.vec,ax)
                self.vecx = rot(self.vecx,ax)
                self.vecy = rot(self.vecy,ax)
                self.vecz = rot(self.vecz,ax)
                self.p4 = rot(self.p4,ax)
                self.p5 = rot(self.p5,ax)
                self.p6 = rot(self.p6,ax)
                print('r', self.nr)

        elif turn == 'l':
            if self.vec[0] < 0:
                ax = self.p4*10
                self.vec = rot(self.vec,ax)
                self.vecx = rot(self.vecx,ax)
                self.vecy = rot(self.vecy,ax)
                self.vecz = rot(self.vecz,ax)
                self.p4 = rot(self.p4,ax)
                self.p5 = rot(self.p5,ax)
                self.p6 = rot(self.p6,ax)
                print('l', self.nr)
        
        elif turn == 'u':
            if self.vec[1] < 0:
                ax = self.p5*10
                self.vec = rot(self.vec,ax)
                self.vecx = rot(self.vecx,ax)
                self.vecy = rot(self.vecy,ax)
                self.vecz = rot(self.vecz,ax)
                self.p4 = rot(self.p4,ax)
                self.p5 = rot(self.p5,ax)
                self.p6 = rot(self.p6,ax)
                print('u', self.nr)
                
#Setup the 8 Cubes
cube1 = Cube(np.array([-1.0,-1.0, 1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yn), np.copy(zp),BLAU, ORANGE, WEISS,1)
cube2 = Cube(np.array([ 1.0,-1.0, 1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yn), np.copy(zp),BLAU, ROT, WEISS,2)
cube3 = Cube(np.array([ 1.0, 1.0, 1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yp), np.copy(zp),BLAU, ROT, GELB,3)
cube4 = Cube(np.array([-1.0, 1.0, 1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yp), np.copy(zp),BLAU, ORANGE, GELB,4)
cube5 = Cube(np.array([-1.0,-1.0,-1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yn), np.copy(zn),GRUEN, ORANGE, WEISS,5)
cube6 = Cube(np.array([ 1.0,-1.0,-1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yn), np.copy(zn),GRUEN, ROT, WEISS,6)
cube7 = Cube(np.array([ 1.0, 1.0,-1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yp), np.copy(zn),GRUEN, ROT, GELB,7)
cube8 = Cube(np.array([-1.0, 1.0,-1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yp), np.copy(zn),GRUEN, ORANGE, GELB,8)

def buffer():
    sort = []
    sort.append([cube1.vec[2],1])
    sort.append([cube2.vec[2],2])
    sort.append([cube3.vec[2],3])
    sort.append([cube4.vec[2],4])
    sort.append([cube5.vec[2],5])
    sort.append([cube6.vec[2],6])
    sort.append([cube7.vec[2],7])
    sort.append([cube8.vec[2],8])
    
    sorted_list = sorted(sort, key=lambda x: x[0], reverse=True)

    for i in range(1, 8):
        cubelet = globals()['cube{}'.format(sorted_list[i][1])]
        cubelet.fill()

def rot(vec, ax):
    v_x = vec[0]
    v_y = vec[1]
    v_z = vec[2] 
    c = cos(np.radians(90))
    s = sin(np.radians(90))
    r = 1-c
    axe = ax/np.linalg.norm(ax)
    u_x = axe[0]
    u_y = axe[1]
    u_z = axe[2]
    v_rotated_x = v_x * (c + u_x**2 * r) + v_y * (u_x * u_y * r - u_z * s) + v_z * (u_x * u_z * r + u_y * s)
    v_rotated_y = v_x * (u_y * u_x * r + u_z * s) + v_y * (c + u_y ** 2 * r) + v_z * (u_y * u_z * r - u_x * s)
    v_rotated_z = v_x * (u_z * u_x * r - u_y * s) + v_y * (u_z * u_y * r + u_x * s) + v_z * (c + u_z**2 * r)
    newvec = np.array([v_rotated_x, v_rotated_y, v_rotated_z])
    return newvec

# Main Loop
running = True
agl = 5
while running == True:
    # Set Timer
    clock.tick(60)
    window.fill((0,0,0))

    # Draw Center point
    pygame.draw.circle(window, (255, 0, 0), (WINDOW_SIZE/2, WINDOW_SIZE/2), 5)

    # Draw all the points and lines
    for i in range(1, 9):
        cubelet = globals()['cube{}'.format(i)]
        cubelet.drawpoint()
    
    buffer()

    cube1.connectpt(cube2.vec[0], cube2.vec[1])    
    cube1.connectpt(cube4.vec[0], cube4.vec[1])
    cube1.connectpt(cube5.vec[0], cube5.vec[1])
    cube2.connectpt(cube3.vec[0], cube3.vec[1])
    cube2.connectpt(cube6.vec[0], cube6.vec[1])
    cube3.connectpt(cube7.vec[0], cube7.vec[1])
    cube3.connectpt(cube4.vec[0], cube4.vec[1])
    cube4.connectpt(cube8.vec[0], cube8.vec[1])
    cube5.connectpt(cube6.vec[0], cube6.vec[1])
    cube5.connectpt(cube8.vec[0], cube8.vec[1])
    cube7.connectpt(cube6.vec[0], cube6.vec[1])
    cube7.connectpt(cube8.vec[0], cube8.vec[1])


    # Key Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.rotate(-agl, 'y')
            elif event.key == pygame.K_LEFT:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.rotate(agl, 'y')
            elif event.key ==pygame.K_UP:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.rotate(-agl, 'x')
            elif event.key == pygame.K_DOWN:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.rotate(agl, 'x')
            elif event.key == pygame.K_0:
                cube1.setzero(np.array([-1.0,-1.0, 1.0]))
                cube2.setzero(np.array([ 1.0,-1.0, 1.0]))
                cube3.setzero(np.array([ 1.0, 1.0, 1.0]))
                cube4.setzero(np.array([-1.0, 1.0, 1.0]))
                cube5.setzero(np.array([-1.0,-1.0,-1.0]))
                cube6.setzero(np.array([ 1.0,-1.0,-1.0]))
                cube7.setzero(np.array([ 1.0, 1.0,-1.0]))
                cube8.setzero(np.array([-1.0, 1.0,-1.0]))
            elif event.key == pygame.K_ESCAPE:
                running = False   
            elif event.key == pygame.K_r:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.turn('r')
            elif event.key == pygame.K_l:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.turn('l')
            elif event.key == pygame.K_u:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.turn('u')
    pygame.display.update()