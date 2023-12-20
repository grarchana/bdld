import numpy as np
import matplotlib.pyplot as plt

# Load the data from the files
data1 = np.loadtxt("avgsd_scaling1_seed1.data")
data2 = np.loadtxt("avgsd_scaling1_seed2.data")

# Create a figure with subplots (one row, two columns)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Extract the values for plotting - data from file 1
bandwidth1 = data1[:, 0]
average1 = data1[:, 1]
stddev1 = data1[:, 2]

# Plotting the averages with error bars for data from file 1
axes[0].errorbar(bandwidth1, average1, yerr=stddev1, fmt='o')
axes[0].set_xlabel('Bandwidth')
axes[0].set_ylabel('Average')
axes[0].set_title('Scaling 1 - Seed 1')
axes[0].axhline(y=500, color='gray', linestyle='--', label='Baseline at 500')
axes[0].legend()

# Extract the values for plotting - data from file 2
bandwidth2 = data2[:, 0]
average2 = data2[:, 1]
stddev2 = data2[:, 2]

# Plotting the averages with error bars for data from file 2
axes[1].errorbar(bandwidth2, average2, yerr=stddev2, fmt='o')
axes[1].set_xlabel('Bandwidth')
axes[1].set_ylabel('Average')
axes[1].set_title('Scaling 1 - Seed 2')
axes[1].axhline(y=500, color='gray', linestyle='--', label='Baseline at 500')
axes[1].legend()

# Adjust layout and save the figure
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig('avgsd_scaling1_subplots_baseline.png')

# Show the plot
plt.show()

