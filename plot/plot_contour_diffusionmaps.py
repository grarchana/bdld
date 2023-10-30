import numpy as np
import matplotlib.pyplot as plt

# Define the potential function U(x, y)
def potential_energy(x, y, hx, hy, x0, delta):
    a_x = (1/5) * (1 + 5 * np.exp(-((x - x0) ** 2) / delta))**2
    term1 = hx * (x**2 - 1)**2
    term2 = (hy + a_x) * (y**2 - 1)**2
    return term1 + term2

# Define the parameter values
hx = 0.5
hy = 1.0
x0 = 0.0
delta = 0.05

# Create a grid of x and y values
x = np.linspace(-2.0, 2.0, 100)
y = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(x, y)

# Calculate the potential energy for each point in the grid
Z = potential_energy(X, Y, hx, hy, x0, delta)

# Set values greater than 15 to a specific color
Z[Z > 15] = 15  # You can set any value you like for U(x, y) > 15

# Create a contour plot
contour = plt.contourf(X, Y, Z, levels=15, cmap='viridis')
plt.colorbar(contour, label='U(X,Y)', ticks=[0,5,10, 15])  # Add a colorbar with ticks

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Contour Plot of Potential Energy')

# Save the figure as "contour_diffusionmaps.png"
plt.savefig('contour_diffusionmaps.png')

# Show the plot
plt.show()
