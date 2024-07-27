#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def gaussian_kernel(size: int, sigma: float) -> np.ndarray:
    """Generate a Gaussian kernel."""
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return kernel / kernel.sum()

# Create a sample 2D array (image) to convolve with the Gaussian kernel
def create_sample_array(size: int) -> np.ndarray:
    """Create a sample 2D array with random values."""
    np.random.seed(0)  # For reproducibility
    return np.random.rand(size, size)

# Example usage in Jupyter Notebook
size = 11
sigma = 2.0

# Create a Gaussian kernel
kernel = gaussian_kernel(size, sigma)

# Create a sample array
sample_array = create_sample_array(50)

# Perform convolution
convoluted_array = convolve2d(sample_array, kernel, mode='same')

# Output the kernel values
print("Gaussian Kernel:\n", kernel)

# Plot the original array
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(sample_array, cmap='viridis')
plt.colorbar()
plt.title('Original Array')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(False)

# Plot the convoluted array
plt.subplot(1, 2, 2)
plt.imshow(convoluted_array, cmap='viridis')
plt.colorbar()
plt.title('Convoluted Array')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(False)

plt.tight_layout()
plt.show()


# In[3]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def gaussian_kernel_1d(size: int, sigma: float) -> np.ndarray:
    """Generate a 1D Gaussian kernel."""
    x = np.linspace(-size // 2, size // 2, size)
    kernel = np.exp(-x**2 / (2 * sigma**2))
    return kernel / kernel.sum()

def double_well_potential(x: np.ndarray) -> np.ndarray:
    """Compute the double-well potential function U(x) = x^4 - 4x^2 + 0.2x."""
    return x**4 - 4*x**2 + 0.2*x

# Example usage in Jupyter Notebook
size = 11
sigma = 2.0

# Generate a 1D Gaussian kernel
kernel_1d = gaussian_kernel_1d(size, sigma)

# Define the range and sample points
x = np.linspace(-5, 5, 500)

# Create the double-well potential array
potential_array = double_well_potential(x)

# Perform convolution
convoluted_array = convolve(potential_array, kernel_1d, mode='same')

# Plot the original potential and convoluted result
plt.figure(figsize=(12, 6))

# Plot the original potential
plt.subplot(1, 2, 1)
plt.plot(x, potential_array, label='Original Potential', color='blue')
plt.title('Original Double-Well Potential')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.grid(True)

# Plot the convoluted result
plt.subplot(1, 2, 2)
plt.plot(x, convoluted_array, label='Convoluted Potential', color='red')
plt.title('Convoluted Double-Well Potential')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.grid(True)

plt.tight_layout()
plt.show()


# In[5]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def gaussian_kernel_1d(size: int, sigma: float) -> np.ndarray:
    """Generate a 1D Gaussian kernel."""
    x = np.linspace(-size // 2, size // 2, size)
    kernel = np.exp(-x**2 / (2 * sigma**2))
    return kernel / kernel.sum()

def double_well_potential(x: np.ndarray) -> np.ndarray:
    """Compute the double-well potential function U(x) = x^4 - 4x^2 + 0.2x."""
    return x**4 - 4*x**2 + 0.2*x

# Example usage in Jupyter Notebook
size = 11
sigma = 2.0

# Generate a 1D Gaussian kernel
kernel_1d = gaussian_kernel_1d(size, sigma)

# Define the range and sample points in the new range
x = np.linspace(-2, 2, 500)

# Create the double-well potential array
potential_array = double_well_potential(x)

# Perform convolution
convoluted_array = convolve(potential_array, kernel_1d, mode='same')

# Plot the original potential and convoluted result
plt.figure(figsize=(12, 6))

# Plot the original potential
plt.subplot(1, 2, 1)
plt.plot(x, potential_array, label='Original Potential', color='blue')
plt.title('Original Double-Well Potential')
plt.xlabel('x')
plt.ylabel('Free Energy ($k_B T$)')
plt.grid(True)

# Plot the convoluted result
plt.subplot(1, 2, 2)
plt.plot(x, convoluted_array, label='Convoluted Potential', color='red')
plt.title('Convoluted Double-Well Potential')
plt.xlabel('x')
plt.ylabel('Free Energy ($k_B T$)')
plt.grid(True)

plt.tight_layout()
plt.show()


# In[ ]:




