import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("particle_dist_b0.data")
ignore = int(data.shape[0] / 10)
subset_data = data[ignore:, 1]

#Determines the no of rows to ignore (10% of the total rows) using 'data.shape[0]'.Subset of data ignoring the initial rows is) is selected. 
average = np.average(subset_data)
stddev = np.std(subset_data, ddof=1)

#ddof-DeltaDegreesofFreedom,by default 'ddof=0' is population standard deviation
#ddof=1, sample standard deviation, used for a subset of data rather than the entire population


# Prompt the user to enter the bandwidth value
bandwidth = float(input("Enter the bandwidth value: "))

# Open the output file in write mode
with open("avg_sd_b0.data", "w") as output_file:
    # Write the bandwidth, average, and standard deviation in a row-wise format
    output_file.write("Bandwidth\tAverage\tStandardDeviation\n")
    output_file.write("{}\t{}\t{}\n".format(bandwidth, average, stddev))

# Plotting the averages with error bars
#x = [bandwidth]
#y = [average]
#error = [stddev]

#Will plot a single data point representing the average with an error bar indicating the standard deviation
#plt.errorbar(x, y, yerr=error, fmt='o')
#plt.xlabel('Bandwidth')
#plt.ylabel('Average')
#plt.title('Averages with Standard deviation as Error Bars')
#plt.show()

