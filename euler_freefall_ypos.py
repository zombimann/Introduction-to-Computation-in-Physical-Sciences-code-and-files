##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665



def euler_freefall_ypos(tf, dt=0.1, y0=0, v0=0):
    """Implements Euler's algorithm for a 1D projectile freefal model. Solves for a projectile
    with a user-defined initial position above ground as well as initial velocity up to its
    position at a user-specified final time"""
    t, y, v = 0, y0, v0
    g = 9.8
    while t < tf:
        t = t + dt
        y = y + v * dt
        v = v + (-g) * dt 
    return y 

## Example test(s)
print(euler_freefall_ypos(2, dt=.01))
print(euler_freefall_ypos(2, dt=.001))