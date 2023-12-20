import matplotlib.pyplot as plt

# Read the data from the file
filename = 'traj_b0.data.0'
data = []

with open(filename, 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        line = line.strip().split()
        time = float(line[0])
        pos_x = float(line[1])
        data.append((time, pos_x))

# Separate time and pos_x values
time, pos_x = zip(*data)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, pos_x, label='pos_x.0', color='b')
plt.xlabel('Time')
plt.ylabel('pos_x.0')
plt.title('Time Series of pos_x.0_b0')
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig('time_series_b0.png')
plt.show()

