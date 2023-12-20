import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt("avgsd_scaling5.data")

# Extract the values for plotting
bandwidth = data[:, 0]
stddev = data[:, 2]

# List of legend labels
legend_labels = ["scaling5"]

# Plot the standard deviation with custom legend label
plt.plot(bandwidth, stddev, 'o-', label=legend_labels[0])

# Set plot labels and title
plt.xlabel('Bandwidth')
plt.ylabel('Standard Deviation')
plt.title('SD vs Bandwidth scaling5')

# Add legend
plt.legend()

# Save the figure
plt.savefig('stddev_bandwidth_scaling5.png')

# Show the plot
plt.show()

