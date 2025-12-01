##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665


"""
Projectile Motion Kinematics Notes

Kinematic Equations:
x(t) = v0x * t + x0
y(t) = -0.5 * g * t^2 + v0y * t + y0
v0x = v0 * cos(theta)
v0y = v0 * sin(theta)

Time to reach ground (t*):
t* = (v0y + sqrt(v0y^2 + 2*g*y0)) / g

Range R(theta):
R(theta) = (v0x / g) * (v0y + sqrt(v0y^2 + 2*g*y0))

Range-maximizing angle (theta*):
theta* = arccos( sqrt((2*g*y0 + v0^2) / (2*g*y0 + 2*v0^2)) )

Notes on theta*:
- y0 = 0 → theta* = 45 deg
- y0 > 0 → theta* < 45 deg
- y0 < 0 → theta* > 45 deg
- Example: y0 = 1 m, v0 = 3 m/s → theta* ≈ 29 deg

Air resistance model (numerical):
y(t+dt) ≈ y(t) + f(y, v, t)*dt
v(t+dt) ≈ v(t) + g(y, v, t)*dt

"""


#%% Import modules
import math
import numpy as np
import matplotlib.pyplot as plt

#%% Define functions
def projectile_range(x0, y0, v0, theta, dt=0.01):
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
angles, ranges01, ranges001, R = [], [], [], [] # Lists to store angles and associated ranges.
trajectories = [] # List to store trajectory data.
for i in range(int(90/dtheta)):
    angles.append(i*dtheta) # Append 0, dtheta, 2*dtheta, ..., up to 90 deg

#%% Run Simulations
for angle in angles:
    theta = deg_to_rad(angle)
    x_range01, y_range01 = projectile_range(x0, y0, v0, theta) # Numerical Range
    x_range001, y_range001 = projectile_range(x0, y0, v0, theta, 0.001) # Numerical Range
    R.append((v0*math.cos(theta) / g) * (v0*math.sin(theta) + math.sqrt((v0*math.cos(theta))**2 + 2*g*y0))) # Analytical range
    # trajectories.append((x_range, y_range))
    ranges01.append(x_range01)
    ranges001.append(x_range001)

#%% Simulation analysis.
max_index01 = ranges01.index(max(ranges01))
max_angle01 = angles[max_index01]
max_index001 = ranges001.index(max(ranges001))
max_angle001 = angles[max_index001]
print(f"Numerical Optimum Angle (dt = 0.01): {max_angle01:.1f}") # 29.0
print(f"Numerical Optimum Angle (dt = 0.001): {max_angle001:.1f}") # 29.4
# print(trajectories)

#%% Analytical Solution
optimum_angle = math.acos(math.sqrt((2*g*y0 + v0**2)/(2*g*y0 + 2*v0**2))) * 360 / (2 *math.pi)
print(f"Analytical Optimum Angle : {optimum_angle:.1f}") # 29.3

# R = x - x(0) = (v*math.cos(angle) / g) * (v*sin(angle) + sqrt((v*math.cos(angle))**2 + ((v*sin(angle)))**2)


#%% Visualization
# Plot of Angles Vs Ranges
#--------------------------
plt.plot(angles, R, label="Analytical")
plt.plot(angles, ranges01, 'go-', label='Numerical dt = 0.01')
plt.plot(angles, ranges001, 'r-', label='Numerical dt = 0.001')
plt.xlabel("Various Launch Angles (Degrees)")
#plt.xlim([min(angles), max(angles)])
plt.ylabel("Final Range (m)")
#plt.xlim([min(ranges), max(ranges)])
plt.title("Various Launch Angles and the Final Ranges- Analytical Vs Numerical")
plt.legend()
plt.show()

## Plot of Trajectories

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
