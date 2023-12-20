import numpy as np
import matplotlib.pyplot as plt

# Load the data from the files
data_seed1 = np.loadtxt("avgsd_scaling1_seed1.data")
data_seed2 = np.loadtxt("avgsd_scaling1_seed2.data")

# Extract the values for plotting - data from seed1
bandwidth_seed1 = data_seed1[:, 0]
stddev_seed1 = data_seed1[:, 2]

# Extract the values for plotting - data from seed2
bandwidth_seed2 = data_seed2[:, 0]
stddev_seed2 = data_seed2[:, 2]

# Plotting both sets of data on the same plot
plt.plot(bandwidth_seed1, stddev_seed1, 'o-', label='Seed 1')
plt.plot(bandwidth_seed2, stddev_seed2, 'o-', label='Seed 2')

# Set labels and title
plt.xlabel('Bandwidth')
plt.ylabel('Standard Deviation')
plt.title('SD vs Bandwidth for Scaling 1')
plt.legend()

# Save the figure
plt.savefig('stddev_bandwidth_scaling1_seeds.png')

# Show the plot
plt.show()

