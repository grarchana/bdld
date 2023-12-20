import numpy as np
import matplotlib.pyplot as plt

# List of filenames with corresponding scaling values
filenames = {
    "avgsd_scaling10.data": 10,
    "avgsd_scaling5.data": 5,
    "avgsd_scaling2.data": 2,
    "avgsd_scaling1.data": 1
}

# Create a figure with subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle('Averages with Standard deviation as Error Bars')

for i, (filename, scaling) in enumerate(filenames.items()):
    # Load data from each file
    data = np.loadtxt(filename)

    # Extract values for plotting
    bandwidth = data[:, 0]
    average = data[:, 1]
    stddev = data[:, 2]

    # Calculate subplot indices
    row = i // 2  # Row index
    col = i % 2   # Column index

    # Plotting in the respective subplot
    ax = axes[row, col]
    ax.errorbar(bandwidth, average, yerr=stddev, fmt='o')
    ax.set_xlabel('Bandwidth')
    ax.set_ylabel('Average')
    ax.set_title(f'Scaling: {scaling}')
    ax.axhline(y=500, color='gray', linestyle='--', label='Baseline at 500')
    ax.legend()
    ax.grid(True)

# Adjust layout and save the figure
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig('avgsd_scaling_subplots_labeled.png')

# Show the plot
plt.show()

