##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665


import vpython as vp

scene = vp.canvas(title=('right drag to change camera,' +
'double drag to zoom'))
ball = vp.sphere()
box = vp.box(pos=vp.vector(0,0,-1.1),  length=10, height=5, width=.2,
color=vp.color.cyan)
t = 0

while t < 100:
    vp.rate(30)
    ball.pos = vp.vector(2*vp.sin(2*t),0,0)
    t += 0.1
