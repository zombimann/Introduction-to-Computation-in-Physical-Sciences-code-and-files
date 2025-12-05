##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, RadioButtons, CheckButtons

g = 9.8
f = lambda x: x**2

# Initial Parameters
v0_init = 0
val_init = "pos"

# Create the figure and axis
fig, ax = plt.subplots(figsize=(7, 3))
plt.subplots_adjust(left=0.15, bottom=0.35)

t = np.linspace(0, 1, 100)

# Initial plot
sol = -(g/2)*f(t) + v0_init*t
line, = ax.plot(t, sol, linewidth=2)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Position (meters)")
ax.set_title("Position over time")
ax.grid(True)

# Create slider for v0
ax_v0 = plt.axes([0.15, 0.20, 0.65, 0.03])
slider_v0 = Slider(ax_v0, 'Initial Velocity (v0)', -5, 5, valinit=v0_init, valstep=0.1)

# Create radio buttons for pos/vel selection
ax_radio = plt.axes([0.15, 0.05, 0.15, 0.10])
radio = RadioButtons(ax_radio, ('pos', 'vel'))

# Create checkbox for refresh
ax_check = plt.axes([0.4, 0.05, 0.15, 0.10])
check = CheckButtons(ax_check, ['Refresh'], [True])


def plot_freefall_ypos(val=None):
    """Implements Euler's algorithm for a 1D projectile freefal model. Solves for a projectile
    with a initial velocity for a peovided time range"""
    
    v0 = slider_v0.val
    val = radio.value_selected
    refresh = check.get_status()[0]

    if not refresh:
        return
    
    if val == 'pos':
        sol = -(g/2)*f(t) + v0*t        #  f(t) = t**2.
        ax.set_title = "Position over time"
        ax.set_ylabel = "Position (meters)"
    elif val == 'vel':
        sol = v0 + (-g) * t
        ax.set_title = "Velocity over time "
        ax.set_ylabel = "Velocity (m/s)"

    line.set_ydata(sol)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

slider_v0.on_changed(plot_freefall_ypos)
radio.on_clicked(plot_freefall_ypos)
check.on_clicked(plot_freefall_ypos)

plt.show()

