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

# Flatten potential energy values into a 1D array for histogram plotting
Z_flattened = Z.flatten()

# Create a histogram to represent the distribution of potential energy values
plt.figure(figsize=(8, 6))
plt.hist(Z_flattened, bins=100, density=True, alpha=0.7, color='green')  # Adjust bins and other parameters as needed
plt.xlabel('Potential Energy')
plt.ylabel('Probability Density')
plt.title('Histogram - Probability Distribution of Potential Energy')
plt.grid(True)

# Save the figure as "histogram_potential_energy.png"
plt.savefig('histogram_potential_energy.png')

# Show the histogram plot
plt.show()

