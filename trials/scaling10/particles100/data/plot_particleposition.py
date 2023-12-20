import numpy as np
import matplotlib.pyplot as plt

# List of data files
data_files = ["particle_dist_b0.data", "particle_dist_bo05.data", "particle_dist_b1.data"]

# List of bandwidth values
bandwidths = [0, 0.05, 1.0]

# Initialize an empty list to store the data
all_data = []

# Load and append data from each file
for file in data_files:
    data = np.loadtxt(file, skiprows=3)
    all_data.append(data)

# Plotting the number of particles for each bandwidth
for i, data in enumerate(all_data):
    time = data[:, 0] #Extract time values
    n_particles_0 = data[:, 1] #Extract n_particles_0_values
    bandwidth = bandwidths[i]
    label = f"Bandwidth {bandwidth}"

    plt.plot(time, n_particles_0, label=label)

# Set plot labels and title
plt.xlabel('Time')
plt.ylabel('Number of Particles (left)')
plt.title('Number of Particles vs Time')

# Add legend
plt.legend()

# Save the figure
plt.savefig('time_vs_numberofparticles_varybandwidth.png')

# Show the plot
plt.show()

