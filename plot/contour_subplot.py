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

# Define ranges
ranges = [(-6.0, 6.0), (-5.5, 5.5), (-5.0, 5.0), (-4.5, 4.5), (-4.0, 4.0), (-3.5, 3.5), (-3.0, 3.0), (-2.5, 2.5)]

# Create subplots for each range
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(12, 16))
axes = axes.flatten()

for i, (range_vals) in enumerate(ranges):
    start, end = range_vals
    x = np.linspace(start, end, 200)
    y = np.linspace(start, end, 200)
    X, Y = np.meshgrid(x, y)
    
    Z = potential_energy(X, Y, hx, hy, x0, delta)

    # Set values greater than 15 to a specific color
    Z[Z > 15] = 15  # You can set any value you like for U(x, y) > 15

    # Create a contour plot for each range
    contour = axes[i].contourf(X, Y, Z, levels=15, cmap='viridis')
    plt.colorbar(contour, ax=axes[i], label='U(X,Y)', ticks=[0, 5, 10, 15])  # Add a colorbar with ticks
    axes[i].set_xlabel('X')
    axes[i].set_ylabel('Y')
    axes[i].set_title(f'Contour Plot of Potential Energy: {start} to {end}')
    axes[i].grid(True)

# Adjust layout and display
plt.tight_layout()

# Save the figure as "subplots_contour_ranges_labels.png"
plt.savefig('subplots_contour_ranges_labels.png')

# Show the plot
plt.show()

