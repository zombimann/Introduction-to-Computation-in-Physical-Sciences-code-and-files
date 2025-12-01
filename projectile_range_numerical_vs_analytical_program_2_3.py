##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665


"""
##  Projectile Motion Kinematics Notes

This section outlines the **kinematic equations** used to model projectile motion, focusing on the relationships between position, initial velocity, and launch angle, as well as the calculation for the range-maximizing angle.

---

### Kinematic Equations (Equations 2.1)

The position of a projectile at time $t$ is described by the following equations, assuming motion in a constant gravitational field and ignoring air resistance:

* **Horizontal Position:**
    $$x(t) = v_{0x}t + x_0$$
* **Vertical Position:**
    $$y(t) = -\frac{1}{2}gt^2 + v_{0y}t + y_0$$

Where $v_{0x}$ and $v_{0y}$ are the components of the initial velocity $v_0$ at the launch angle $\theta$:
$$v_{0x} = v_0 \cos \theta$$
$$v_{0y} = v_0 \sin \theta$$

---

### Time to Reach Ground ($t_*$) and Traversed Range ($R(\theta)$) (Equations 2.2 & 2.3)

The time $t_*$ at which the projectile reaches the ground (i.e., $y(t_*) = 0$) is given by:

$$t_* = \frac{1}{g}\left(v_{0y} + \sqrt{v_{0y}^2 + 2gy_0}\right)$$

The corresponding **traversed range** $R(\theta)$ is the horizontal distance covered:

$$R(\theta) = x(t_*) - x(0) = \frac{v_{0x}}{g}\left(v_{0y} + \sqrt{v_{0y}^2 + 2gy_0}\right)$$

---

### Range-Maximizing Angle ($\theta_*$)

The **optimal launch angle** $\theta_*$ that maximizes the range $R(\theta)$ is found by setting $dR/d\theta = 0$:

$$\theta_* = \cos^{-1}\left(\sqrt{\frac{2gy_0 + v_0^2}{2gy_0 + 2v_0^2}}\right)$$

**Notes on $\theta_*$:**
* If the launch and landing heights are the same ($y_0 = 0$), the optimal angle is $\mathbf{\theta_* = 45^{\circ}}$.
* If $y_0 > 0$ (launch from above the ground), then $\theta_* < 45^{\circ}$.
* If $y_0 < 0$ (launch into a pit), then $\theta_* > 45^{\circ}$.
* *Example:* With $y_0 = 1 \text{ m}$ and $v_0 = 3 \text{ m/s}$, $\theta_* \approx 29^{\circ}$.

---

### Modeling with Air Resistance (Equations 2.4)

When air resistance is included, the analytic solutions become highly complex. The logic behind Eqs. (2.2) and (2.3) generally remains, but the update rules are typically solved numerically using discrete steps:

$$\begin{aligned} y(t) &\approx y(t) + f(y, v, t)\Delta t \\ v(t) &\approx v(t) + g(y, v, t)\Delta t \end{aligned}$$

Here, $f(\cdot)$ and $g(\cdot)$ are more complicated functions incorporating drag forces.

I'll modify Ex 2.1 for this exercise
"""


#%% Import modules
import math
import numpy as np
import matplotlib.pyplot as plt

#%% Define functions
def projectile_range(x0, y0, v0, theta, dt=0.01, ):
    """Compute range of project launched from (x0, y0) at velocity v0 and angle theta
    relative to horizontal ground (in radians)"""
    t, x, y = 0, x0, y0
    vx, vy = v0 * math.cos(theta), v0 * math.sin(theta)
    g = 9.8
    # Using Euler's method
    while y >= 0:
        t = t + dt
        x = x + vx * dt
        y = y + vy * dt
        vx = vx; # Constant - No horizontal acceleration
        vy = vy + (-g) * dt # Freefall
    return x - x0, y- y0

def deg_to_rad(angle):
    """Convert and angle from degrees to radians"""
    return angle * (math.pi / 180)

#%% Define and initialize parameters
g = 9.8 # Freefall acceleration
x0, y0, v0 = 0, 1, 3 # Initial positions (m) and speed (m/s).
dtheta = .1 # Angle resolution (deg).
angles, ranges = [], [] # Lists to store angles and associated ranges.
trajectories = [] # List to store trajectory data.
for i in range(int(90/dtheta)):
    angles.append(i*dtheta) # Append 0, dtheta, 2*dtheta, ..., up to 90 deg

#%% Run Simulations
for angle in angles:
    theta = deg_to_rad(angle)
    x_range, y_range = projectile_range(x0, y0, v0, theta)
    # trajectories.append((x_range, y_range))
    ranges.append(x_range)

#%% Simulation analysis.
max_index = ranges.index(max(ranges))
max_angle = angles[max_index]
print(max_angle) # 29.0
# print(trajectories)

#%% Visualization
# Plot of Angles Vs Ranges
#--------------------------
plt.plot(angles, ranges)
plt.xlabel("Various Launch Angles (Degrees)")
#plt.xlim([min(angles), max(angles)])
plt.ylabel("Final Range (m)")
#plt.xlim([min(ranges), max(ranges)])
plt.title("Various Launch Angles and the Final Ranges")
plt.show()

# # Plot of Trajectories

# plt.figure()
# for i in range(len(trajectories)):
#     angle = angles[i]
#     if angle % 5 != 0:
#         x_range, y_range = trajectories[i]
#         # Generate trajectory points for plotting
#         x_points = np.linspace(0, x_range, 100)
#         y_points = np.linspace(0, y_range, 100)
#         plt.plot(x_points, y_points, label=f"{angle}°")
# plt.show()
