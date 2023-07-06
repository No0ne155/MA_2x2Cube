import numpy as np
from math import*

xp = np.array([0,1,0])

v1 = np.copy(xp)
v2 = np.copy(xp)
xp[0]=2
v2[0]=7
print(v1[0])