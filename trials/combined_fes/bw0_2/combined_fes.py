import matplotlib.pyplot as plt

# List of filenames and corresponding scaling values
filenames = ["fes_b0_s10.png", "fes_b0_s5.png", "fes_b0_s2.png", "fes_b0_s1.png"]
scaling_values = [10, 5, 2, 1]

# Create a 2x2 subplot grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle('FES Plots with Different Scalings,bandwidth=0.0')

for i, (filename, scaling) in enumerate(zip(filenames, scaling_values)):
    # Calculate subplot indices
    row = i // 2  # Row index
    col = i % 2   # Column index
    
    # Load the image and display it in the corresponding subplot
    img = plt.imread(filename)
    axes[row, col].imshow(img)
    axes[row, col].axis('off')  # Turn off axis labels
    
    # Set title for each subplot indicating the scaling value
    axes[row, col].set_title(f'Scaling {scaling}')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Save the figure
plt.savefig('subplots_fes_scaling_b0_2.png')

# Show the plot
plt.show()

