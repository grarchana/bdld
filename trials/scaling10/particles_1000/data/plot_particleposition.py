import numpy as np
import matplotlib.pyplot as plt

# List of data files
data_files = ["particle_dist_b0.data", "particle_dist_bo05.data", "particle_dist_bo1.data", "particle_dist_bo15.data", "particle_dist_bo2.data", "particle_dist_bo25.data", "particle_dist_bo3.data", "particle_dist_bo35.data", "particle_dist_bo4.data","particle_dist_bo45.data", "particle_dist_bo5.data", "particle_dist_bo55.data", "particle_dist_bo6.data", "particle_dist_bo65.data", "particle_dist_bo7.data", "particle_dist_bo75.data", "particle_dist_bo8.data", "particle_dist_bo85.data", "particle_dist_bo9.data","particle_dist_bo95.data", "particle_dist_b1.data"]

# List of bandwidth values
bandwidths = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]

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
plt.savefig('time_vs_np_scaling10.png')

# Show the plot
plt.show()

