import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt("avgsd_scaling2.data")

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
plt.title('Averages with Standard deviation as Error Bars')

# Save the figure
plt.savefig('avgsd_scaling2.png')

# Show the plot
plt.show()

