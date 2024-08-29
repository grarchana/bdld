#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# 2D Entropic Double-Well Potential Function
def V(x, y, sigma_x=0.1, sigma_y=0.1, a=1.0):
    """
    Computes the 2D entropic double-well potential.

    Parameters:
    - x, y: Coordinates at which to evaluate the potential.
    - sigma_x: Width of the barrier in the x-direction.
    - sigma_y: Width of the opening of the barrier in the y-direction.
    - a: Scaling factor for the potential.

    Returns:
    - V(x, y): The potential value at coordinates (x, y).
    """
    return a * (x**6 + y**6 + np.exp(-(x/sigma_x)**2) * (1 - np.exp(-(y/sigma_y)**2)))

def gaussian_kernel_2d(x, y, sigma_kernel):
    """2D Gaussian Kernel function."""
    coeff = 1.0 / (2.0 * np.pi * sigma_kernel**2)
    exponent = -0.5 * (x**2 + y**2) / (sigma_kernel**2)
    return coeff * np.exp(exponent)

def convolve_density_2d(boltz_array, kernel_array, dx, dy):
    """Perform convolution on the 2D density array."""
    boltz_array_conv = np.zeros_like(boltz_array)
    kernel_half_x = (kernel_array.shape[0] - 1) // 2
    kernel_half_y = (kernel_array.shape[1] - 1) // 2
    
    for i in range(boltz_array.shape[0]):
        for j in range(boltz_array.shape[1]):
            for m in range(kernel_array.shape[0]):
                for n in range(kernel_array.shape[1]):
                    i_shift = i - kernel_half_x + m
                    j_shift = j - kernel_half_y + n
                    if 0 <= i_shift < boltz_array.shape[0] and 0 <= j_shift < boltz_array.shape[1]:
                        boltz_array_conv[i_shift, j_shift] += boltz_array[i, j] * kernel_array[m, n] * dx * dy
    
    return boltz_array_conv

def plot_results_2d(lattice_spacings, sigma_kernel, x_min, x_max, y_min, y_max):
    fig, axs = plt.subplots(3, len(lattice_spacings), figsize=(20, 15))
    
    # Set the figure background color to white
    fig.patch.set_facecolor('white')
    
    # Set the background color of all axes to white
    for ax in axs.flat:
        ax.set_facecolor('white')

    markers = ['o', 's', '^', 'D', '*']  # Different markers for different plots
    colors = ['orange', 'green', 'red', 'purple', 'blue']  # Different colors for different plots

    for i, dx in enumerate(lattice_spacings):
        dy = dx  # Assuming square grid
        x = np.arange(x_min, x_max + dx, dx)
        y = np.arange(y_min, y_max + dy, dy)
        X, Y = np.meshgrid(x, y)
        potential_array = V(X, Y)
        boltz_array = np.exp(-potential_array)
        
        # Normalize the Boltzmann density using the trapezium rule
        boltz_array /= np.trapz(np.trapz(boltz_array, y, axis=0), x, axis=0)
        
        # Kernel and its convolution
        kernel_size = int(5 * sigma_kernel)  # Extending kernel size
        kernel_x = np.arange(-kernel_size, kernel_size + dx, dx)
        kernel_y = np.arange(-kernel_size, kernel_size + dy, dy)
        Kernel_X, Kernel_Y = np.meshgrid(kernel_x, kernel_y)
        kernel_array = gaussian_kernel_2d(Kernel_X, Kernel_Y, sigma_kernel)
        
        # Normalize the kernel using the trapezium rule
        kernel_integral = np.trapz(np.trapz(kernel_array, kernel_y, axis=0), kernel_x, axis=0)
        kernel_array /= kernel_integral
        
        # Print the integral of the kernel to check if it is equal to one
        print(f'Integral of the Gaussian kernel for dx={dx}: {np.trapz(np.trapz(kernel_array, kernel_y, axis=0), kernel_x, axis=0)}')
        
        boltz_array_conv = convolve_density_2d(boltz_array, kernel_array, dx, dy)
        
        # Calculate potential from convolved density
        with np.errstate(divide='ignore'):
            potential_array_conv = -np.log(boltz_array_conv)
        
        # Plot Gaussian Kernel (2D plot using contour)
        axs[0, i].contourf(Kernel_X, Kernel_Y, kernel_array, levels=50, cmap='Blues')
        axs[0, i].set_xlabel('x')
        axs[0, i].set_ylabel('y')
        axs[0, i].set_title(f'Gaussian Kernel (dx={dx})')
        axs[0, i].grid(True)
        
        # Plot Equilibrium Density and Smoothed Density
        c1 = axs[1, i].contourf(X, Y, boltz_array, levels=50, cmap='Greens', alpha=0.7)
        c2 = axs[1, i].contour(X, Y, boltz_array_conv, levels=50, cmap='Reds', alpha=0.7)
        axs[1, i].set_xlabel('x')
        axs[1, i].set_ylabel('y')
        axs[1, i].set_title(f'Density (dx={dx})')
        axs[1, i].grid(True)
        
        # Compute and Plot Difference between Densities
        density_difference = boltz_array_conv - boltz_array
        axs[2, i].contourf(X, Y, density_difference, levels=50, cmap='Purples')
        axs[2, i].set_xlabel('x')
        axs[2, i].set_ylabel('y')
        axs[2, i].set_title(f'Difference (dx={dx})')
        axs[2, i].grid(True)
        
    # Add a main title to the figure
    fig.suptitle('Gaussian Kernel Convolution for Bandwidth 0.35, 2D Entropic Double-Well Potential, Range [-1.5:1.5]', fontsize=16, y=1.02)
    
    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig('GK_2d_double_well.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

if __name__ == "__main__":
    lattice_spacings = [0.025, 0.05, 0.075, 0.1, 0.15]  # Finer lattice spacings for 2D
    sigma_kernel = 0.35  # Fixed bandwidth for Gaussian kernel
    x_min, x_max = -1.5, 1.5  # Range in x direction
    y_min, y_max = -1.5, 1.5  # Range in y direction
    plot_results_2d(lattice_spacings, sigma_kernel, x_min, x_max, y_min, y_max)


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# 2D Entropic Double-Well Potential Function
def V(x, y, sigma_x=0.1, sigma_y=0.1, a=1.0):
    """
    Computes the 2D entropic double-well potential.

    Parameters:
    - x, y: Coordinates at which to evaluate the potential.
    - sigma_x: Width of the barrier in the x-direction.
    - sigma_y: Width of the opening of the barrier in the y-direction.
    - a: Scaling factor for the potential.

    Returns:
    - V(x, y): The potential value at coordinates (x, y).
    """
    return a * (x**6 + y**6 + np.exp(-(x/sigma_x)**2) * (1 - np.exp(-(y/sigma_y)**2)))

def gaussian_kernel_2d(x, y, sigma_kernel):
    """2D Gaussian Kernel function."""
    coeff = 1.0 / (2.0 * np.pi * sigma_kernel**2)
    exponent = -0.5 * (x**2 + y**2) / (sigma_kernel**2)
    return coeff * np.exp(exponent)

def convolve_density_2d(boltz_array, kernel_array, dx, dy):
    """Perform convolution on the 2D density array."""
    boltz_array_conv = np.zeros_like(boltz_array)
    kernel_half_x = (kernel_array.shape[0] - 1) // 2
    kernel_half_y = (kernel_array.shape[1] - 1) // 2
    
    for i in range(boltz_array.shape[0]):
        for j in range(boltz_array.shape[1]):
            for m in range(kernel_array.shape[0]):
                for n in range(kernel_array.shape[1]):
                    i_shift = i - kernel_half_x + m
                    j_shift = j - kernel_half_y + n
                    if 0 <= i_shift < boltz_array.shape[0] and 0 <= j_shift < boltz_array.shape[1]:
                        boltz_array_conv[i_shift, j_shift] += boltz_array[i, j] * kernel_array[m, n] * dx * dy
    
    return boltz_array_conv

def plot_results_2d(lattice_spacing, sigma_kernel, x_min, x_max, y_min, y_max):
    fig, axs = plt.subplots(3, 1, figsize=(8, 20))  # 3 rows, 1 column for the plots
    
    # Set the figure background color to white
    fig.patch.set_facecolor('white')
    
    # Set the background color of all axes to white
    for ax in axs.flat:
        ax.set_facecolor('white')

    dx = lattice_spacing
    dy = dx  # Assuming square grid
    x = np.arange(x_min, x_max + dx, dx)
    y = np.arange(y_min, y_max + dy, dy)
    X, Y = np.meshgrid(x, y)
    potential_array = V(X, Y)
    boltz_array = np.exp(-potential_array)
    
    # Normalize the Boltzmann density using the trapezium rule
    boltz_array /= np.trapz(np.trapz(boltz_array, y, axis=0), x, axis=0)
    
    # Kernel and its convolution
    kernel_size = int(5 * sigma_kernel)  # Extending kernel size
    kernel_x = np.arange(-kernel_size, kernel_size + dx, dx)
    kernel_y = np.arange(-kernel_size, kernel_size + dy, dy)
    Kernel_X, Kernel_Y = np.meshgrid(kernel_x, kernel_y)
    kernel_array = gaussian_kernel_2d(Kernel_X, Kernel_Y, sigma_kernel)
    
    # Normalize the kernel using the trapezium rule
    kernel_integral = np.trapz(np.trapz(kernel_array, kernel_y, axis=0), kernel_x, axis=0)
    kernel_array /= kernel_integral
    
    # Print the integral of the kernel to check if it is equal to one
    print(f'Integral of the Gaussian kernel: {np.trapz(np.trapz(kernel_array, kernel_y, axis=0), kernel_x, axis=0)}')
    
    boltz_array_conv = convolve_density_2d(boltz_array, kernel_array, dx, dy)
    
    # Calculate potential from convolved density
    with np.errstate(divide='ignore'):
        potential_array_conv = -np.log(boltz_array_conv)
    
    # Plot Gaussian Kernel (2D plot using contour)
    axs[0].contourf(Kernel_X, Kernel_Y, kernel_array, levels=50, cmap='Blues')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].set_title('Gaussian Kernel')
    axs[0].grid(True)
    
    # Plot Equilibrium Density and Smoothed Density
    axs[1].contourf(X, Y, boltz_array, levels=50, cmap='Greens', alpha=0.7)
    axs[1].contour(X, Y, boltz_array_conv, levels=50, cmap='Reds', alpha=0.7)
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('y')
    axs[1].set_title('Equilibrium Density (Green) and Smoothed Density (Red)')
    axs[1].grid(True)
    
    # Compute and Plot Difference between Densities
    density_difference = boltz_array_conv - boltz_array
    axs[2].contourf(X, Y, density_difference, levels=50, cmap='Purples')
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('y')
    axs[2].set_title('Density Difference')
    axs[2].grid(True)
    
    # Add a main title to the figure
    fig.suptitle('Gaussian Kernel Convolution for Bandwidth 0.35, 2D Entropic Double-Well Potential, Lattice Spacing 0.01', fontsize=16, y=1.02)
    
    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig('GK_2d_double_well_single_spacing.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()




# In[ ]:


if __name__ == "__main__":
    lattice_spacing = 0.01  # Only calculate for one lattice spacing
    sigma_kernel = 0.35  # Fixed bandwidth for Gaussian kernel
    x_min, x_max = -1.5, 1.5  # Range in x direction
    y_min, y_max = -1.5, 1.5  # Range in y direction
    plot_results_2d(lattice_spacing, sigma_kernel, x_min, x_max, y_min, y_max)


# In[ ]:




