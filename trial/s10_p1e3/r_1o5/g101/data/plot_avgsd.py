import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt("avgsd_ep_s10_p1000_g1001_r1o5.data")

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
plt.title('Averages with Standard deviation as Error Bars,EntropicDoubleWellPotential,grid1001')

# Add text to specify labeling
plt.text(0.95, 0.9, 'range:-1.5:1.5', horizontalalignment='right', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))


# Save the figure
plt.savefig('avg_bw_ep_s10_p1000_g501_r1o5.png')

# Show the plot
plt.show()

