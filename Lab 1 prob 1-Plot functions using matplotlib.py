#  Plot all the given functions to observe the roots by visualization, fill the table by your visual guess of root. We have plotted one function for you.
# 1)  f(x)=cos(x)−1.3x 
# 2)  f(x)=2xcos(2x)−(x+1)^2


import numpy as np
from matplotlib import pyplot as plt

# Set the figure size for the plots
plt.rcParams["figure.figsize"] = [6.50, 6.50]

# Define the first function
def f(x):
    return np.cos(x) - 1.3 * x

# Generate a range of x values for plotting
x = np.linspace(-5, 5, 10000)  # 10,000 points between -5 and 5

# Plot the function f(x) with a red line
plt.plot(x, f(x), color='red', label='f(x) = cos(x) - 1.3x')

# Plot the x-axis (y = 0) for reference
plt.hlines(y=0, xmin=-5, xmax=5, color='blue', label='y = 0')

# Add gridlines for better visualization
plt.grid(True)

# Show the plot for the first function
plt.title('Plot of f(x) = cos(x) - 1.3x')
plt.legend()
plt.show()

# Define the second function
def h(x):
    return 2 * x * np.cos(2 * x) - (x + 1) ** 2

# Generate a range of x values for the second function plot
x = np.linspace(-3, 0, 10000)  # 10,000 points between -3 and 0

# Plot the function h(x) with a red line
plt.plot(x, h(x), color='red', label='h(x) = 2x*cos(2x) - (x+1)^2')

# Plot the x-axis (y = 0) for reference
plt.hlines(y=0, xmin=-3, xmax=0, color='blue', label='y = 0')

# Add gridlines for better visualization
plt.grid(True)

# Show the plot for the second function
plt.title('Plot of h(x) = 2x*cos(2x) - (x+1)^2')
plt.legend()
plt.show()
