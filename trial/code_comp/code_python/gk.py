import numpy as np
import matplotlib.pyplot as plt

# Potential function V(x) (updated)
def potential(x):
    return x**4 - 4*x**2 + 0.2*x

# Gaussian Kernel function
def gaussian_kernel(x, sigma):
    coeff = 1.0 / (np.sqrt(2.0 * np.pi) * sigma)
    exponent = -0.5 * (x**2) / (sigma**2)
    return coeff * np.exp(exponent)

# Parameters
dx = 0.01
xlower_pot = -2.0
xupper_pot = 2.0
sigma = 0.5

# Calculate grid sizes
range_pot = xupper_pot - xlower_pot
npoints_pot = int((range_pot - 0.1 * dx) / dx) + 2
npoints_kernel = int((sigma - 0.1 * dx) / dx) + 1
npoints_kernel = 2 * npoints_kernel + 1  # odd per construction

# Create arrays
x = np.linspace(xlower_pot, xupper_pot, npoints_pot)
potential_array = np.zeros(npoints_pot)
boltz_array = np.zeros(npoints_pot)
boltz_array_conv = np.zeros(npoints_pot)
potential_array_conv = np.zeros(npoints_pot)

# Calculate potential and boltzmann factors
for i in range(npoints_pot):
    xi = x[i]
    potential_array[i] = potential(xi)
    boltz_array[i] = np.exp(-potential_array[i])

# Kernel array
kernel_x = np.linspace(-sigma, sigma, npoints_kernel)
kernel_array = np.array([gaussian_kernel(kx, sigma) for kx in kernel_x])

# Convolution
for i in range(npoints_pot):
    for j in range(npoints_kernel):
        kount_target = i + (j - (npoints_kernel - 1) // 2)
        if 0 <= kount_target < npoints_pot:
            boltz_array_conv[kount_target] += boltz_array[i] * kernel_array[j] * dx

# Compute potential from convolved density
for i in range(npoints_pot):
    boltz_array_conv[i] = max(boltz_array_conv[i], 1e-10)  # Avoid log(0)
    potential_array_conv[i] = -np.log(boltz_array_conv[i])

# Save results to file
with open("output_data.txt", "w") as file:
    file.write("X\tPotential(X)\tExp(-Potential(X))\tConvolved Exp(-Potential(X))\tPotential from Convolved Density\n")
    for i in range(npoints_pot):
        file.write(f"{x[i]:.4f}\t{potential_array[i]:.4f}\t{boltz_array[i]:.4f}\t{boltz_array_conv[i]:.4f}\t{potential_array_conv[i]:.4f}\n")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, potential_array, label='Potential(x)')
plt.plot(x, boltz_array, label='Exp(-Potential(x))')
plt.plot(x, boltz_array_conv, label='Convolved Exp(-Potential(x))')
plt.plot(x, potential_array_conv, label='Potential from Convolved Density')
plt.xlabel('x')
plt.ylabel('Values')
plt.title('Potential and Density')
plt.legend()
plt.grid(True)
plt.savefig('density_plot_bwo5_gk.png', dpi=300)
plt.show()

