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
ROTATE_SPEED = 0.05

# Variables
scale = 100
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()
center = [(WINDOW_SIZE/2),(WINDOW_SIZE/2)]

# Centerpoints
xp = np.array([ 1,0,0])
xn = np.array([-1,0,0])
yp = np.array([0, 1,0])
yn = np.array([0,-1,0])
zp = np.array([0,0, 1])
zn = np.array([0,0,-1])

# Class Cube
class Cube:
    def __init__(self,vec, vec1, vec2, vec3, coX, coY, coZ) -> None:
        # Vector from Center to Corner
        self.vec = vec 
        # Vectors from Corners to Edges
        self.vecx = vec1 + vec
        self.vecy = vec2 + vec
        self.vecz = vec3 + vec
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
            if axis == 'x':
                self.vec[1] = y * c - z * s
                self.vec[2] = y * s + z * c
                self.vecx[1] = xy * c - xz * s
                self.vecx[2] = xy * s + xz * c
                self.vecy[1] = yy * c - yz * s
                self.vecy[2] = yy * s + yz * c
                self.vecz[1] = zy * c - zz * s
                self.vecz[2] = zy * s + zz * c
            elif axis == 'y':
                self.vec[0] = x * c + z * s
                self.vec[2] = -x * s + z * c
                self.vecx[0] = xx * c + xz * s
                self.vecx[2] = -xx * s + xz * c
                self.vecy[0] = yx * c + yz * s
                self.vecy[2] = -yx * s + yz * c
                self.vecz[0] = zx * c + zz * s
                self.vecz[2] = -zx * s + zz * c

    # Drawing points
    def drawpoint(self):
        pygame.draw.circle(window, (255, 0, 0), (self.vec[0] *100+300, self.vec[1] *100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecx[0]*100+300, self.vecx[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecy[0]*100+300, self.vecy[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecz[0]*100+300, self.vecz[1]*100+300),5)
        
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
        pass


# Setup the 8 Cubes
cube1 = Cube(np.array([-1.0,-1.0, 1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), ORANGE, GELB, GRUEN)
cube2 = Cube(np.array([ 1.0,-1.0, 1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), ROT, GELB, GRUEN)
cube3 = Cube(np.array([ 1.0, 1.0, 1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), ROT, WEISS, GRUEN)
cube4 = Cube(np.array([-1.0, 1.0, 1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), ORANGE, WEISS, GRUEN)
cube5 = Cube(np.array([-1.0,-1.0,-1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), ORANGE, GELB, BLAU)
cube6 = Cube(np.array([ 1.0,-1.0,-1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), ROT, GELB, BLAU)
cube7 = Cube(np.array([ 1.0, 1.0,-1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), ROT, WEISS, BLAU)
cube8 = Cube(np.array([-1.0, 1.0,-1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), ORANGE, WEISS, BLAU)



# Main Loop
angle_x = angle_y = angle_z = 0
running = True
agl = 1
while running == True:
    # Set Timer
    clock.tick(60)
    window.fill((0,0,0))

    # Draw Center point
    pygame.draw.circle(window, (255, 0, 0), (WINDOW_SIZE/2, WINDOW_SIZE/2), 5)

    # Draw all the points and lines
    cube1.drawpoint()
    cube2.drawpoint()
    cube3.drawpoint()
    cube4.drawpoint()
    cube5.drawpoint()
    cube6.drawpoint()
    cube7.drawpoint()
    cube8.drawpoint()
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
                angle_y -= ROTATE_SPEED
                cube1.rotate(-agl, 'y')
                cube2.rotate(-agl, 'y')
                cube3.rotate(-agl, 'y')
                cube4.rotate(-agl, 'y')
                cube5.rotate(-agl, 'y')
                cube6.rotate(-agl, 'y')
                cube7.rotate(-agl, 'y')
                cube8.rotate(-agl, 'y')
            elif event.key == pygame.K_LEFT:
                angle_y += ROTATE_SPEED
                cube1.rotate(agl, 'y')
                cube2.rotate(agl, 'y')
                cube3.rotate(agl, 'y')
                cube4.rotate(agl, 'y')
                cube5.rotate(agl, 'y')
                cube6.rotate(agl, 'y')
                cube7.rotate(agl, 'y')
                cube8.rotate(agl, 'y')
            elif event.key ==pygame.K_UP:
                angle_x += ROTATE_SPEED
                cube1.rotate(-agl, 'x')
                cube2.rotate(-agl, 'x')
                cube3.rotate(-agl, 'x')
                cube4.rotate(-agl, 'x')
                cube5.rotate(-agl, 'x')
                cube6.rotate(-agl, 'x')
                cube7.rotate(-agl, 'x')
                cube8.rotate(-agl, 'x')
            elif event.key == pygame.K_DOWN:
                angle_x -= ROTATE_SPEED
                cube1.rotate(agl, 'x')
                cube2.rotate(agl, 'x')
                cube3.rotate(agl, 'x')
                cube4.rotate(agl, 'x')
                cube5.rotate(agl, 'x')
                cube6.rotate(agl, 'x')
                cube7.rotate(agl, 'x')
                cube8.rotate(agl, 'x')
            elif event.key == pygame.K_0:
                angle_y = angle_x = angle_z = 0
                cube1.setzero(np.array([-1,-1, 1]))
                cube2.setzero(np.array([ 1,-1, 1]))
                cube3.setzero(np.array([ 1, 1, 1]))
                cube4.setzero(np.array([-1, 1, 1]))
                cube5.setzero(np.array([-1,-1,-1]))
                cube6.setzero(np.array([ 1,-1,-1]))
                cube7.setzero(np.array([ 1, 1,-1]))
                cube8.setzero(np.array([-1, 1,-1]))
            elif event.key == pygame.K_ESCAPE:
                running = False   
    pygame.display.update()