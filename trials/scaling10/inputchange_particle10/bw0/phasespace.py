import matplotlib.pyplot as plt

# Read the data from the file for one walker (e.g., 'traj_b0.data.0')
filename = 'traj_b0.data.1'
data = []

with open(filename, 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        line = line.strip().split()
        pos_x = float(line[1])
        pos_y = float(line[2])
        data.append((pos_x, pos_y))

# Separate pos_x and pos_y values
pos_x, pos_y = zip(*data)

# Create a scatter plot
plt.figure(figsize=(8, 8))
plt.scatter(pos_x, pos_y, s=1, color='b')
plt.xlabel('X-Position')
plt.ylabel('Y-Position')
plt.title('phasespace_b0')
plt.grid(True)

# Save the figure
plt.savefig('phasespace_b0.png')
plt.show()

