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
    def __init__(self,vec, vec1, vec2, vec3, p4,p5,p6, coX, coY, coZ) -> None:
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
        pygame.draw.polygon(window, self.coX, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300),(self.p6[0]*100+300, self.p6[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300)])
        pygame.draw.polygon(window, self.coY, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecy[0]*100+300, self.vecy[1]*100+300),(self.p4[0]*100+300, self.p4[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300)])
        pygame.draw.polygon(window, self.coZ, [(self.vec[0]*100+300, self.vec[1]*100+300), (self.vecz[0]*100+300, self.vecz[1]*100+300),(self.p5[0]*100+300, self.p5[1]*100+300), (self.vecx[0]*100+300, self.vecx[1]*100+300)])

    def turn(self, turn):
        if turn == 'r':
            if self.vec[0] >0:
                print('turn r')
                u = np.array([2.0, 0.0, 0.0])
                theta = np.radians(90)
                u_norm = u/np.linalg.norm(u)
                # Rotationsmatrix
                rotation_matrix = np.array([[np.cos(theta) + u_norm[0]**2 * (1 - np.cos(theta)),
                             u_norm[0] * u_norm[1] * (1 - np.cos(theta)) - u_norm[2] * np.sin(theta),
                             u_norm[0] * u_norm[2] * (1 - np.cos(theta)) + u_norm[1] * np.sin(theta)],
                            [u_norm[1] * u_norm[0] * (1 - np.cos(theta)) + u_norm[2] * np.sin(theta),
                             np.cos(theta) + u_norm[1]**2 * (1 - np.cos(theta)),
                             u_norm[1] * u_norm[2] * (1 - np.cos(theta)) - u_norm[0] * np.sin(theta)],
                            [u_norm[2] * u_norm[0] * (1 - np.cos(theta)) - u_norm[1] * np.sin(theta),
                             u_norm[2] * u_norm[1] * (1 - np.cos(theta)) + u_norm[0] * np.sin(theta),
                             np.cos(theta) + u_norm[2]**2 * (1 - np.cos(theta))]])
                self.vec = np.dot(rotation_matrix, self.vec)
                self.vecx = np.dot(rotation_matrix, self.vecx)
                self.vecy = np.dot(rotation_matrix, self.vecy)
                self.vecz = np.dot(rotation_matrix, self.vecz)
                self.p4 = np.dot(rotation_matrix, self.p4)
                self.p5 = np.dot(rotation_matrix, self.p5)
                self.p6 = np.dot(rotation_matrix, self.p6)

# Setup the 8 Cubes
cube1 = Cube(np.array([-1.0,-1.0, 1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yn), np.copy(zp),BLAU, ORANGE, WEISS)
cube2 = Cube(np.array([ 1.0,-1.0, 1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yn), np.copy(zp),BLAU, ROT, WEISS)
cube3 = Cube(np.array([ 1.0, 1.0, 1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yp), np.copy(zp),BLAU, ROT, GELB)
cube4 = Cube(np.array([-1.0, 1.0, 1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yp), np.copy(zp),BLAU, ORANGE, GELB)
cube5 = Cube(np.array([-1.0,-1.0,-1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yn), np.copy(zn),GRUEN, ORANGE, WEISS)
cube6 = Cube(np.array([ 1.0,-1.0,-1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yn), np.copy(zn),GRUEN, ROT, WEISS)
cube7 = Cube(np.array([ 1.0, 1.0,-1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yp), np.copy(zn),GRUEN, ROT, GELB)
cube8 = Cube(np.array([-1.0, 1.0,-1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yp), np.copy(zn),GRUEN, ORANGE, GELB)


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
    for i in range(1, 9):
        cubelet = globals()['cube{}'.format(i)]
        cubelet.fill()
    '''
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
    cube7.connectpt(cube8.vec[0], cube8.vec[1])'''
    
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
    pygame.display.update()