import numpy as np
import matplotlib.pyplot as plt

# Load the data from the files
data1 = np.loadtxt("avgsd_scaling1_seed1.data")
data2 = np.loadtxt("avgsd_scaling1_seed2.data")

# Extract the values for plotting - data from file 1
bandwidth1 = data1[:, 0]
average1 = data1[:, 1]
stddev1 = data1[:, 2]

# Extract the values for plotting - data from file 2
bandwidth2 = data2[:, 0]
average2 = data2[:, 1]
stddev2 = data2[:, 2]

# Plotting both sets of data on the same plot
plt.errorbar(bandwidth1, average1, yerr=stddev1, fmt='o', label='Seed 1')
plt.errorbar(bandwidth2, average2, yerr=stddev2, fmt='o', label='Seed 2')

# Add a horizontal baseline at y = 500
plt.axhline(y=500, color='gray', linestyle='--', label='Baseline at 500')

# Set labels and title
plt.xlabel('Bandwidth')
plt.ylabel('Average')
plt.title('Scaling 1: Averages with Standard deviation as Error Bars')
plt.legend()

# Save the figure
plt.savefig('avgsd_scaling1_single.png')

# Show the plot
plt.show()

