import pygame
from math import*
import numpy as np
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
scale = 100
#z_buffering
window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pygame.time.Clock()

center = [(WINDOW_SIZE/2),(WINDOW_SIZE/2)]

xp = np.array([ 1,0,0])
xn = np.array([-1,0,0])
yp = np.array([0, 1,0])
yn = np.array([0,-1,0])
zp = np.array([0,0, 1])
zn = np.array([0,0,-1])

class Cube:
    def __init__(self,vec, vec1, vec2, vec3) -> None:
        self.vec = vec
        self.vecx = vec1 + vec
        self.vecy = vec2 + vec
        self.vecz = vec3 + vec

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

        
    def drawpoint(self):
        pygame.draw.circle(window, (255, 0, 0), (self.vec[0] *100+300, self.vec[1] *100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecx[0]*100+300, self.vecx[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecy[0]*100+300, self.vecy[1]*100+300),5)
        pygame.draw.circle(window, (255,255,0), (self.vecz[0]*100+300, self.vecz[1]*100+300),5)
        #print(x,y)
        

    def connectpt(self, x2,y2):
        x1 = (self.vec[0] * 100) + WINDOW_SIZE/2
        y1 = (self.vec[1] * 100) + WINDOW_SIZE/2
        x2 = (x2 * scale) + WINDOW_SIZE/2
        y2 = (y2 * scale) + WINDOW_SIZE/2
        pygame.draw.line(window, (255, 255, 255), (x1, y1),(x2,y2))
    
    def setzero(self,vec):
        self.vec = vec

    def addvec(self, vec1):
        self.vecx = vec1 + self.vec
        print(self.vecx)
        pygame.draw.circle(window, (255, 0, 0), (self.vecx[0]*100+300, self.vecx[1]*100+30), 5)
        #self.vecy = vec2 + self.vec
        #self.vecz = vec3 + self.vec

    
cube1 = Cube(np.array([-1.0,-1.0, 1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]))
cube2 = Cube(np.array([ 1.0,-1.0, 1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]))
cube3 = Cube(np.array([ 1.0, 1.0, 1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]))
cube4 = Cube(np.array([-1.0, 1.0, 1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]))
cube5 = Cube(np.array([-1.0,-1.0,-1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]))
cube6 = Cube(np.array([ 1.0,-1.0,-1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]))
cube7 = Cube(np.array([ 1.0, 1.0,-1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]))
cube8 = Cube(np.array([-1.0, 1.0,-1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]))



# Main Loop
angle_x = angle_y = angle_z = 0
running = True
while running == True:
    clock.tick(60)
    window.fill((0,0,0))

    pygame.draw.circle(window, (255, 0, 0), (WINDOW_SIZE/2, WINDOW_SIZE/2), 5)

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


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                angle_y -= ROTATE_SPEED
                cube1.rotate(-9, 'y')
                cube2.rotate(-9, 'y')
                cube3.rotate(-9, 'y')
                cube4.rotate(-9, 'y')
                cube5.rotate(-9, 'y')
                cube6.rotate(-9, 'y')
                cube7.rotate(-9, 'y')
                cube8.rotate(-9, 'y')
            elif event.key == pygame.K_LEFT:
                angle_y += ROTATE_SPEED
                cube1.rotate(9, 'y')
                cube2.rotate(9, 'y')
                cube3.rotate(9, 'y')
                cube4.rotate(9, 'y')
                cube5.rotate(9, 'y')
                cube6.rotate(9, 'y')
                cube7.rotate(9, 'y')
                cube8.rotate(9, 'y')
            elif event.key ==pygame.K_UP:
                angle_x += ROTATE_SPEED
                cube1.rotate(-9, 'x')
                cube2.rotate(-9, 'x')
                cube3.rotate(-9, 'x')
                cube4.rotate(-9, 'x')
                cube5.rotate(-9, 'x')
                cube6.rotate(-9, 'x')
                cube7.rotate(-9, 'x')
                cube8.rotate(-9, 'x')
            elif event.key == pygame.K_DOWN:
                angle_x -= ROTATE_SPEED
                cube1.rotate(9, 'x')
                cube2.rotate(9, 'x')
                cube3.rotate(9, 'x')
                cube4.rotate(9, 'x')
                cube5.rotate(9, 'x')
                cube6.rotate(9, 'x')
                cube7.rotate(9, 'x')
                cube8.rotate(9, 'x')
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