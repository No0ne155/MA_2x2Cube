import numpy as np

def rot(vec, ax):
    v_x = vec[0]
    v_y = vec[1]
    v_z = vec[2] 
    c = cos(90)
    s = sin(90)
    r = 1-c
    axe = ax/np.linalg.norm(ax)
    u_x = axe[0]
    u_y = axe[1]
    u_z = axe[2]
    v_rotated_x = v_x * (c + u_x**2 * r) + v_y * (u_x * u_y * r - u_z * s) + v_z * (u_x * u_z * r + u_y * s)
    v_rotated_y = v_x * (u_y * u_x * r + u_z * s) + v_y * (c + u_y ** 2 * r) + v_z * (u_y * u_z * r - u_x * s)
    v_rotated_z = v_x * (u_z * u_x * r - u_y * s) + v_y * (u_z * u_y * r + u_x * s) + v_z * (c + u_z**2 * r)
    newvec = np.array(v_rotated_x, v_rotated_y, v_rotated_z)
    return newvec
