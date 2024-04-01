import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt("avgsd_ep_s10_p1000_g1001_r1o5.data")

# Extract the values for plotting
bandwidth = data[:, 0]
stddev = data[:, 2]

# List of legend labels
legend_labels = ["range:-1.5:1.5"]

# Plot the standard deviation with custom legend label
plt.plot(bandwidth, stddev, 'o-', label=legend_labels[0])

plt.xlabel('Bandwidth')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation vs Bandwidth - Entropic Double Well Potential')

# Add legend
plt.legend()

# Save the figure
plt.savefig('sd_bw_ep_s10_p1000_g1001_r1o5.png')

# Show the plot
plt.show()

