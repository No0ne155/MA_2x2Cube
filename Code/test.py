import numpy as np
from math import*

class Cube:
    def __init__(self,vec) -> None:
        self.vec = vec

    def rotate(self, angle, axis):
        rad = radians(angle)
        c = cos(rad)
        s = sin(rad)
        
        if axis == 'x':
            y, z = self.y, self.z
            self.y = y * c - z * s
            self.z = y * s + z * c
        elif axis == 'y':
            x, z = self.x, self.z
            self.x = x * c + z * s
            self.z = -x * s + z * c
        elif axis == 'z':
            x, y = self.x, self.y
            self.x = x * c - y * s
            self.y = x * s + y * c

cube1 = Cube(np.array([-1,-1, 1]))

#cube1.rotate(3, 'x')
x = cube1.vec[0]
print(x)
x = cube1.vec[0]+1
print(cube1.vec[0])