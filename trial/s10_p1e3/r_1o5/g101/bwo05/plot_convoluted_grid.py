import matplotlib.pyplot as plt
import numpy as np

# Assuming the Grid class is defined as provided in the code

# Load data from file into a Grid object, skipping the first line
grid_data = np.loadtxt('convolution_output.txt', skiprows=1)

# Get the dimensions of the data grid
rows, columns = grid_data.shape

# Assuming the data is structured as a grid, reshape it accordingly
reshaped_data = grid_data.reshape(rows, columns)

# Create meshgrid for plotting
x = np.arange(0, columns)
y = np.arange(0, rows)
X, Y = np.meshgrid(x, y)

# Plot the data
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, reshaped_data, cmap='viridis')
plt.colorbar(label='Value')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Convolution Output,Entropic_DoubleWellPotential,Bandwidth:0.05,Range:-1.5:1.5')
plt.grid(True)

# Save the figure
plt.savefig('cg_plot_bo05.png')

# Show the plot
plt.show()

