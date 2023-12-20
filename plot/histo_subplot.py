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
range_names = ['-6.0:6.0', '-5.5:5.5', '-5.0:5.0', '-4.5:4.5', '-4.0:4.0', '-3.5:3.5', '-3.0:3.0', '-2.5:2.5']

# Create subplots for each range
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(12, 16))
axes = axes.flatten()

for i, (range_vals, name) in enumerate(zip(ranges, range_names)):
    start, end = range_vals
    x = np.linspace(start, end, 200)
    y = np.linspace(start, end, 200)
    X, Y = np.meshgrid(x, y)
    
    Z = potential_energy(X, Y, hx, hy, x0, delta)
    Z_flattened = Z.flatten()
    
    ax = axes[i]
    ax.hist(Z_flattened, bins=75, density=True, alpha=0.7, color='green', edgecolor='black')
    ax.set_title(name)
    ax.set_xlabel('Potential Energy')
    ax.set_ylabel('Probability Density')

# Adjust layout and display
plt.tight_layout()

# Save the figure as "subplots_histograms_ranges.png"
plt.savefig('subplots_histograms_ranges_ls200.png')

# Show the figure
plt.show()

