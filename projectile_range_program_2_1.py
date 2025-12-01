##### CODE BY MUGAMBI NDWIGA, mugambindwiga@gmail.com, +254714103665



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
