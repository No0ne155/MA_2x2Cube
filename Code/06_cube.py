# Imports
import pygame
import time
import numpy as np
import py222
import solver
from math import*
from random import*
from pygame import font

# Monte carlo simulation
# Abweichung durch rotation

pygame.init()
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
state = True
shift = False
turns = ['u','d','f','b','r','l']
font_path = pygame.font.get_default_font()  # This gets the path of the default font on your system
myfont = pygame.font.Font(font_path, 26)
file_path = 'cubedata.txt'
file_path2 = 'cubedata2.txt'
loop = False
agl = 10
scramblelst = ""
cube222 = py222.initState()
add = ''
oma = False
solvedoma = False
omac = False

# Centerpoints
xp = np.array([ 1.0,0.0,0.0])
xn = np.array([-1.0,0.0,0.0])
yp = np.array([0.0, 1.0,0.0])
yn = np.array([0.0,-1.0,0.0])
zp = np.array([0.0,0.0, 1.0])
zn = np.array([0.0,0.0,-1.0])

# Class Cube
class Cube:
    # Innitialise Cube, with all relevant Variables
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

    # Color fill algorithm, with z-buffering
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
        
    # Turning the Cublet in a certain direction with a certain angle
    def turn(self, turn, agl):
        if turn == 'r':
            if self.vec[0] >0:
                lst = [[self.p4[0], 4],[self.p5[0],5],[self.p6[0],6]]
                slst = sorted(lst, key=lambda x: x[0], reverse=True)
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)

        elif turn == 'l':
            if self.vec[0] < 0:
                lst = [[self.p4[0], 4],[self.p5[0],5],[self.p6[0],6]]
                slst = sorted(lst, key=lambda x: x[0])
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)
        
        elif turn == 'u':
            if self.vec[1] < 0:
                lst = [[self.p4[1], 4],[self.p5[1],5],[self.p6[1],6]]
                slst = sorted(lst, key=lambda x: x[0])
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)
        
        elif turn == 'd':
            if self.vec[1] > 0:
                lst = [[self.p4[1], 4],[self.p5[1],5],[self.p6[1],6]]
                slst = sorted(lst, key=lambda x: x[0], reverse=True)
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)
        
        elif turn == 'b':
            if self.vec[2] > 0:
                lst = [[self.p4[2], 4],[self.p5[2],5],[self.p6[2],6]]
                slst = sorted(lst, key=lambda x: x[0], reverse=True)
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)
                
        elif turn == 'f':
            if self.vec[2] < 0:
                lst = [[self.p4[2], 4],[self.p5[2],5],[self.p6[2],6]]
                slst = sorted(lst, key=lambda x: x[0])
                lo = slst[0][1]
                if lo ==4:
                    ax = self.p4
                elif lo ==5:
                    ax = self.p5
                else:
                    ax = self.p6
                self.vec = rot(self.vec,ax,agl)
                self.vecx = rot(self.vecx,ax,agl)
                self.vecy = rot(self.vecy,ax,agl)
                self.vecz = rot(self.vecz,ax,agl)
                self.p4 = rot(self.p4,ax,agl)
                self.p5 = rot(self.p5,ax,agl)
                self.p6 = rot(self.p6,ax,agl)
                
# Setup the 8 Cubes
cube1 = Cube(np.array([-1.0,-1.0, 1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yn), np.copy(zp),BLAU, ORANGE, WEISS,1)
cube2 = Cube(np.array([ 1.0,-1.0, 1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yn), np.copy(zp),BLAU, ROT, WEISS,2)
cube3 = Cube(np.array([ 1.0, 1.0, 1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xp), np.copy(yp), np.copy(zp),BLAU, ROT, GELB,3)
cube4 = Cube(np.array([-1.0, 1.0, 1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0,-1]), np.copy(xn), np.copy(yp), np.copy(zp),BLAU, ORANGE, GELB,4)
cube5 = Cube(np.array([-1.0,-1.0,-1.0]), np.array([ 1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yn), np.copy(zn),GRUEN, ORANGE, WEISS,5)
cube6 = Cube(np.array([ 1.0,-1.0,-1.0]), np.array([-1,0,0]), np.array([0, 1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yn), np.copy(zn),GRUEN, ROT, WEISS,6)
cube7 = Cube(np.array([ 1.0, 1.0,-1.0]), np.array([-1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xp), np.copy(yp), np.copy(zn),GRUEN, ROT, GELB,7)
cube8 = Cube(np.array([-1.0, 1.0,-1.0]), np.array([ 1,0,0]), np.array([0,-1,0]), np.array([0,0, 1]), np.copy(xn), np.copy(yp), np.copy(zn),GRUEN, ORANGE, GELB,8)

# Def to Calculate the order of the piece rendering
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

# Def to Calculate the new position after rotating a certain vec around axis
def rot(vec, ax,agl):
    v_x = vec[0]
    v_y = vec[1]
    v_z = vec[2] 
    c = cos(np.radians(agl))
    s = sin(np.radians(agl))
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

# Def to show, if the cube solved
def mark(res):
    global state
    if res == 't':
        pygame.draw.line(window, GRUEN, (80,60), (130,10), 5)
        pygame.draw.line(window, GRUEN, (80,60), (50,30), 5)
        state = True
    if res == 'f':
        pygame.draw.line(window, ROT, (50,30), (110,90), 5)
        pygame.draw.line(window, ROT, (110,30), (50,90), 5)
        state = False

# Checker, if the correct pieces are Neighbours = Cube solved
def checker():
    global omac
    if np.allclose(cube1.vecx, cube2.vecx, 0.00001) == True:
        if np.allclose(cube5.vecx, cube6.vecx, 0.00001) == True:
            if np.allclose(cube2.vecz, cube6.vecz, 0.00001) == True:
                if np.allclose(cube3.vecx, cube4.vecx, 0.00001) == True:
                    if np.allclose(cube7.vecx, cube8.vecx, 0.00001) == True:
                        if np.allclose(cube4.vecz, cube8.vecz, 0.00001) == True:
                            if np.allclose(cube8.vecy, cube5.vecy, 0.00001) == True:
                                mark('t')
                                omac = True 
                            else:
                                mark('f')                        
                        else:
                            mark('f')  
                    else:
                        mark('f')                   
                else:
                    mark('f')           
            else:
                mark('f')          
        else:
            mark('f')       
    else:
        mark('f')

# Def to solve Random
def solveR():
    global loop
    count = 0
    t0=time.time()
    run = True
    while state == False and run == True:
        window.fill((0,0,0))
        k = randint(0,5)
        dir = randint(0,1)
        dire = [-90,90]
        turn = turns[k]
        for i in range(1, 9):
            cubelet = globals()['cube{}'.format(i)]
            cubelet.turn(f'{turn}', dire[dir])
        count = count+1
        display_text(f"Moves: {count}", 370, 50)
        if loop == True:
            display_text('L', 10,10)
        if loop == False:
            display_text('N', 10,10)
        display_text('R', 550,570)
        checker()
        buffer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(count)
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(count)
                    exit()
                elif event.key == pygame.K_0:
                    run = False
                elif event.key == pygame.K_w:
                    if loop == True:
                        loop = False
                    elif loop == False:
                        loop = True
        pygame.display.update()
    print(count)
    t1 = time.time()
    ts = t1-t0
    tm = ts/60
    th = tm/60
    print(f'Your Time was{ts} seconds.')
    print(f'This is {tm} minutes')
    print(f'Or {th} hours!!')
    print(f'Solved is {state}')
    if state:
        with open(file_path, 'a') as file:
            file.write(f'Finished random in: {ts} sec, {count} turns.'+'\n')

# Def to check OneMoveAway
def omaCheck():
    global oma

    oma = False
    if np.allclose(cube1.vecx, cube2.vecx, 0.00001) == True:
        if np.allclose(cube5.vecx, cube6.vecx, 0.00001) == True:
            if np.allclose(cube2.vecz, cube6.vecz, 0.00001) == True:
                if np.allclose(cube3.vecx, cube4.vecx, 0.00001) == True:
                    if np.allclose(cube7.vecx, cube8.vecx, 0.00001) == True:
                        if np.allclose(cube4.vecz, cube8.vecz, 0.00001) == True:
                            oma = True
    elif np.allclose(cube1.vecx, cube2.vecx, 0.00001) == True:
        if np.allclose(cube3.vecx, cube4.vecx, 0.00001) == True:
            if np.allclose(cube1.vecy, cube4.vecy, 0.00001) == True:
                if np.allclose(cube5.vecx, cube6.vecx, 0.00001) == True:
                    if np.allclose(cube7.vecx, cube8.vecx, 0.00001) == True:
                        if np.allclose(cube5.vecy, cube8.vecy, 0.00001) == True:
                            oma = True
    elif np.allclose(cube1.vecy, cube4.vecy, 0.00001) == True:
        if np.allclose(cube5.vecy, cube8.vecy, 0.00001) == True:
            if np.allclose(cube5.vecz, cube1.vecz, 0.00001) == True:
                if np.allclose(cube2.vecy, cube3.vecy, 0.00001) == True:
                    if np.allclose(cube6.vecy, cube7.vecy, 0.00001) == True:
                        if np.allclose(cube2.vecz, cube6.vecz, 0.00001) == True:
                            oma = True
    if oma == True:
        for i in range(1, 9):
            cubelet = globals()['cube{}'.format(i)]
            cubelet.turn('r',90)
        print('oma')
        
# Def more efficient random
def solveR2():
    global loop
    count = 0
    t0=time.time()
    run = True
    lastTurn = 'x'
    while state == False and run == True:
        window.fill((0,0,0))
        print(oma)
        omaCheck()
        print(oma)
        if oma == False:
            print(oma)
            dir = randint(0,2)
            dire = [-90, 90, 180]
            if lastTurn == 'x':
                t = ['u','d','f','b','r','l']
                k = randint(0,5)
                turn = t[k]
            elif lastTurn == 'u' or lastTurn == 'd':
                t = ['f','b','r','l']
                k = randint(0,3)
                turn = t[k]
            elif lastTurn == 'f' or lastTurn == 'b':
                t = ['d','u','r','l']
                k = randint(0,3)
                turn = t[k]
            elif lastTurn == 'r' or lastTurn == 'l':
                t = ['f','b','u','d']
                k = randint(0,3)
                turn = t[k]
            lastTurn=turn
            print(turn)
            for i in range(1, 9):
                cubelet = globals()['cube{}'.format(i)]
                cubelet.turn(f'{turn}', dire[dir])
            count = count+1
        elif oma == True:
            print(oma)
            for i in range(1, 9):
                cubelet = globals()['cube{}'.format(i)]
                cubelet.turn('u',-90)
            print('c1')
            checker()
            if omac == False:
                for i in range(1, 9):
                    cubelet = globals()['cube{}'.format(i)]
                    cubelet.turn('u',-90)
                print('c2')
                checker()
                if omac == False:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('u',-90)
                    print('c3')
                    checker()
                    if omac == False:
                        for i in range(1, 9):
                            cubelet = globals()['cube{}'.format(i)]
                            cubelet.turn('u',-90)
                        print('c4')
                        checker()
        display_text(f"Moves: {count}", 370, 50)
        if loop == True:
            display_text('L', 10,10)
        if loop == False:
            display_text('N', 10,10)
        display_text('R2', 550,570)
        checker()
        buffer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(count)
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(count)
                    exit()
                elif event.key == pygame.K_0:
                    run = False
                elif event.key == pygame.K_w:
                    if loop == True:
                        loop = False
                    elif loop == False:
                        loop = True
        pygame.display.update()
    print(count)
    t1 = time.time()
    ts = t1-t0
    tm = ts/60
    th = tm/60
    print(f'Your Time was{ts} seconds.')
    print(f'This is {tm} minutes')
    print(f'Or {th} hours!!')
    print(f'Solved is {state}')
    if state:
        with open(file_path2, 'a') as file:
            file.write(f'Finished random in: {ts} sec, {count} turns.'+'\n')

# Def to scramble the cube
def scramble():
    global scramblelst
    for j in range(25):
        k = randint(0,5)
        turn = turns[k]
        dir = randint(0,2)
        dire = [-90,90,180]
        if dire[dir] == -90:
            add = ''
        elif dire[dir] == 90:
            add = "'"
        elif dire[dir] == 180:
            add = '2'
        scramblelst =scramblelst + turn.upper()+add+' '
        for i in range(1, 9):
            cubelet = globals()['cube{}'.format(i)]
            cubelet.turn(f'{turn}',dire[dir])
    print(scramblelst)

# py222 solver
def solve222():
    global cube222
    t0 = time.time()
    cube222 = py222.doAlgStr(cube222, scramblelst)
    alg = solver.solveCube(cube222)
    print(alg)
    algs = solver.solvedalg
    head, sep, tail = algs.partition("gap")
    algs = head.split()
    for i in range(len(algs)):
        algs[i]=algs[i].lower()
    for i in range(len(algs)):
        if len(algs[i]) == 2:
            if algs[i][1] == '2':
                for l in range(1, 9):
                    cubelet = globals()['cube{}'.format(l)]
                    cubelet.turn(f'{algs[i][0]}',180)
            elif algs[i][1] == "'":
                for l in range(1, 9):
                    cubelet = globals()['cube{}'.format(l)]
                    cubelet.turn(f'{algs[i][0]}',90)
        else:
            for l in range(1, 9):
                cubelet = globals()['cube{}'.format(l)]
                cubelet.turn(f'{algs[i]}',-90)
    t1 = time.time()
    ti = t1 - t0
    with open(file_path2, 'a') as file:
        file.write(f'Finished random in: {ti} sec, {len(algs)} turns.'+'\n')
    print(ti, len(algs))
                              
# Welcome Message
def welcome():
    print('Wilkommen zu meinem 2x2 Cube simulator')
    print('Um zu beginnen, können sie den Cube mit den Pfeiltasten bewegen')
    print('Um eine Drehung vorzunehmen, drücken Sie eine der folgenden Tasten:')
    print(turns)
    print('Dies nimmt eine Rotation der entsprechenden seite in Uhrzeigerrichtung vor')
    print('Um eine Drehung gegen den Uhrzeigersinn vorzunehmen, drücken Sie zusätzlich "Shift Links"')
    print('Um den Cube verdrehen zu lassen, drücken Sie die "1"')
    print('Um den Cube von einem Zufallsgenerator lösen zu lassen, drücken sie die "2"')
    print('Während dem lösen durch zufalls, können Sie den Prozess mit "0" abbrechen, und selbst zu lösen beginnen.')
    print('Mit der Taste "W" könnens Sie in den Loop eintreten, d.h. nach dem lösen, verdreht er sich wieder, und beginnt zu lösen.')
    print('Mit der Taste "3" können Sie einen Effizienteren Zufallsalgorithmus zum lösen wählen')
    print('Mit der Taste "4" können Sie den Cube mit einem Effizienzsolver lösen.')

# Def to show text on Screen
def display_text(text, x, y):
    text_surface = myfont.render(text, True, WEISS)
    window.blit(text_surface, (x, y))

def setupR():
    for i in range(1, 9):
        cubelet = globals()['cube{}'.format(i)]
        cubelet.rotate(agl, 'y')
    for i in range(1, 9):
        cubelet = globals()['cube{}'.format(i)]
        cubelet.rotate(agl, 'x')
    
setupR()
welcome()
# Main Loop
running = True
agl = 5
while running == True:
    # Set Timer
    clock.tick(60)
    window.fill((0,0,0))

    buffer()
    checker()

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
            elif event.key == pygame.K_ESCAPE:
                running = False   
            elif event.key == pygame.K_r:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('r',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('r',90)
            elif event.key == pygame.K_l:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('l',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('l',90)
            elif event.key == pygame.K_u:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('u',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('u',90)
            elif event.key == pygame.K_d:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('d',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('d',90)
            elif event.key == pygame.K_f:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('f',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('f',90)
            elif event.key == pygame.K_b:
                if not shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('b',-90)
                if shift:
                    for i in range(1, 9):
                        cubelet = globals()['cube{}'.format(i)]
                        cubelet.turn('b',90)
            elif event.key == pygame.K_1:
                scramble()
            elif event.key == pygame.K_2:
                solveR()
            elif event.key == pygame.K_LSHIFT:
                shift = True  # Set the shift_pressed flag
            elif event.key == pygame.K_w:
                if loop:
                    loop = False
                elif not loop:
                    loop = True
            elif event.key == pygame.K_3:
                solveR2()
            elif event.key == pygame.K_4:
                solve222()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift = False  # Reset the shift_pressed flag

        
    if loop:
        scramble()
        solveR()
    
    pygame.display.update()

