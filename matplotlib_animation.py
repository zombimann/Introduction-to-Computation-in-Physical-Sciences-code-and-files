
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as am

def updatefig(frame): 
    t = 0.1 * frame
    u = np.sin(x) * np.sin(w * t)
    plot.set_data(x, u)
    return plot,  # Return tuple for blitting 

w = 1.0
x = np.linspace(0, 2*np.pi, 101)
fig = plt.figure()
plot = plt.plot(x, 0*x)[0]

# Set up the plot limits
plt.ylim(-1.2, 1.2)
plt.xlim(0, 2*np.pi)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Animated Wave')

# Create animation with finite frames
ani = am.FuncAnimation(fig, updatefig, frames=200, interval=50, 
                       cache_frame_data=False, blit=False)

plt.show()  
