import numpy as np

def potential(x):
    """Potential function V(x)."""
    potential_value = x**2
    potential_value = 0.25 * potential_value**2 - 0.5 * potential_value
    return potential_value

def kernel(x, sigma):
    """Piecewise Parabolic Kernel function."""
    if x <= -sigma or x >= sigma:
        return 0.0
    elif x <= -0.5 * sigma:
        kernel_value = 1.0 + x / sigma
        kernel_value = kernel_value**2
        kernel_value = 2.0 * kernel_value / sigma
    elif x >= 0.5 * sigma:
        kernel_value = 1.0 - x / sigma
        kernel_value = kernel_value**2
        kernel_value = 2.0 * kernel_value / sigma
    else:
        kernel_value = x / sigma
        kernel_value = kernel_value**2
        kernel_value = 1.0 - 2.0 * kernel_value
        kernel_value = kernel_value / sigma
    return kernel_value

def main():
    dx = 0.01

    xlower_pot = -2.0
    xupper_pot = 2.0
    range_pot = xupper_pot - xlower_pot
    npoints_pot = int((range_pot - 0.1 * dx) / dx) + 2

    x = np.linspace(xlower_pot, xupper_pot, npoints_pot)

    potential_array = np.array([potential(xi) for xi in x])
    boltz_array = np.exp(-potential_array)
    boltz_array_conv = np.zeros_like(boltz_array)
    potential_array_conv = np.zeros_like(potential_array)

    sigma = 0.5
    npoints_kernel = int((sigma - 0.1 * dx) / dx) + 1
    npoints_kernel = 2 * npoints_kernel + 1  # odd number

    kernel_array = np.array([kernel(xi, sigma) for xi in np.linspace(-sigma, sigma, npoints_kernel)])

    # Convolution
    kernel_half = (npoints_kernel - 1) // 2
    for kount in range(npoints_pot):
        for kount_kernel in range(npoints_kernel):
            kount_kernel_shifted = kount - kernel_half + kount_kernel
            if 0 <= kount_kernel_shifted < npoints_pot:
                boltz_array_conv[kount_kernel_shifted] += boltz_array[kount] * kernel_array[kount_kernel] * dx

    # Calculate potential from convolved density
    with np.errstate(divide='ignore'):
        potential_array_conv = -np.log(boltz_array_conv)

    # Save to file
    with open('output_data.txt', 'w') as file:
        file.write("X\tPotential(X)\tExp(-Potential(X))\tConvolved Exp(-Potential(X))\tPotential from Convolved Density\n")
        for i in range(npoints_pot):
            file.write(f"{x[i]:.4f}\t{potential_array[i]:.4f}\t{boltz_array[i]:.4f}\t{boltz_array_conv[i]:.4f}\t{potential_array_conv[i]:.4f}\n")

if __name__ == "__main__":
    main()

