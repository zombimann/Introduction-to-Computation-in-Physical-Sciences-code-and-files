##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665


import vpython as vp


scene = vp.canvas(title=('right drag to change camera,' +
'double drag to zoom'))
ball = vp.sphere()
box = vp.box(pos=vp.vector(0, 0, -1.1), length=10, height=5, width=.2,
             color=vp.color.cyan)

velvec = vp.arrow(axis=vp.vector(2, 0, 0), length=ball.radius) # axis = arrow direction

t = 0
while t < 10:
    vp.rate(10)
    ball.pos = vp.vector(2*vp.sin(2*t), 0, 0)
    velvec.pos = ball.pos 
    # velvec.length = ball.radius
    # velvec.pos = ball.pos + vp.vector(ball.radius*vp.cos(t), 0, 0) # Update arrow position
    velvec.axis = vp.vector(2*vp.cos(2*t), 0, 0)
    t = t + 0.1


