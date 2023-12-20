import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt("avgsd_scaling1_seed2.data")

# Extract the values for plotting
bandwidth = data[:, 0]
average = data[:, 1]
stddev = data[:, 2]

# Add a horizontal baseline at y = 500
plt.axhline(y=500, color='gray', linestyle='--', label='Baseline at 500')

# Plotting the averages with error bars
plt.errorbar(bandwidth, average, yerr=stddev, fmt='o')
plt.xlabel('Bandwidth')
plt.ylabel('Average')

# Modify the title
plt.title('Averages with Standard deviation as Error Bars')

# Add text to specify scaling and seed information
plt.text(0.95, 0.9, 'Scaling 1 - Seed 2', horizontalalignment='right', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Save the figure
plt.savefig('avgsd_scaling1_seed2.png')

# Show the plot
plt.show()

