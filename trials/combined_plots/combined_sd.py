import numpy as np
import matplotlib.pyplot as plt

# List of filenames and corresponding legend labels
file_legend_pairs = [
    ("avgsd_scaling10.data", "scaling10"),
    ("avgsd_scaling5.data", "scaling5"),
    ("avgsd_scaling2.data", "scaling2"),
    ("avgsd_scaling1.data", "scaling1")
]

# Create a figure with subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle('Standard Deviation vs Bandwidth')

for i, (filename, legend_label) in enumerate(file_legend_pairs):
    # Load the data from the file
    data = np.loadtxt(filename)

    # Extract the values for plotting
    bandwidth = data[:, 0]
    stddev = data[:, 2]

    # Calculate subplot indices
    row = i // 2  # Row index
    col = i % 2   # Column index

    # Plotting in the respective subplot
    ax = axes[row, col]
    ax.plot(bandwidth, stddev, 'o-', label=legend_label)
    ax.set_xlabel('Bandwidth')
    ax.set_ylabel('Standard Deviation')
    ax.set_title(f'{legend_label}')
    ax.legend()

# Adjust layout and save the figure
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig('stddev_bandwidth_subplots.png')

# Show the plot
plt.show()

