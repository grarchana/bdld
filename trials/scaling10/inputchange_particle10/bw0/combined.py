import matplotlib.pyplot as plt

# Initialize empty lists to accumulate data for pos_x
time_data = []
pos_x_data = []

# Loop through the 10 files
for i in range(10):
    filename = f'traj_b0.data.{i}'
    
    # Read data from the current file for pos_x
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip().split()
            time = float(line[0])
            pos_x = float(line[1])
            data.append((time, pos_x))
    
    # Separate and accumulate the data for pos_x
    time, pos_x = zip(*data)
    time_data.extend(time)
    pos_x_data.extend(pos_x)

# Create the plot for pos_x from 10 files
plt.figure(figsize=(10, 6))
plt.plot(time_data, pos_x_data, label='pos_x.0', color='b')
plt.xlabel('Time')
plt.ylabel('Position (pos_x.0)')
plt.title('Time Series of pos_x.0 (bandwidth:1.00)')
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig('timeseries_pos_x_combined_b0.png')
plt.show()

