import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the potential function U(x, y)
def potential_energy(x, y, hx, hy, x0, delta):
    a_x = (1/5) * (1 + 5 * np.exp(-((x - x0) ** 2) / delta))**2
    term1 = hx * x * (x**2 - 1)**2
    term2 = (hy + a_x) * (y**2 - 1)**2
    return term1 + term2

# Define the parameter values
hx = 0.5
hy = 1.0
x0 = 0.0
delta = 1/20

# Create a grid of x and y values
x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(x, y)

# Calculate the potential energy for each point in the grid
Z = potential_energy(X, Y, hx, hy, x0, delta)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('U(x, y)')
ax.set_title('Potential Energy Surface')

# Show the plot
plt.show()

