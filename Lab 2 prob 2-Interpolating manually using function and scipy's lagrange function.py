# The code you provided has two approaches for calculating and plotting the Lagrange polynomial:
# Manual Calculation using Lagrange_Func: This approach manually calculates the Lagrange polynomial using nested loops and numpy.poly1d.
# Using scipy.interpolate.lagrange: This approach leverages the lagrange function from the scipy.interpolate library, which is more concise and easier to use.


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Data points
x = np.array([0, 20, 40, 60, 80, 100])
y = np.array([26.0, -48.6, 61.6, -71.2, 74.8, -75.2])

# User input for interpolation
point = float(input("Enter x-coordinate to interpolate: "))

# Manual Lagrange Polynomial Calculation
def lagrange_manual(x, y):
    n = len(x)
    p = np.poly1d(0.0)
    for i in range(n):
        L = np.poly1d(y[i])
        for j in range(n):
            if j != i:
                L *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])
        p += L
    return p

# Calculate using manual method
p_manual = lagrange_manual(x, y)
interpolated_value_manual = p_manual(point)

# Display manual results
print("\nManual Lagrange Polynomial")
print(p_manual)
print(f"Interpolated value at x = {point} using manual method is: {interpolated_value_manual}\n")

# Calculate using scipy's lagrange function
f_scipy = lagrange(x, y)
interpolated_value_scipy = f_scipy(point)

# Display scipy results
print("\nScipy Lagrange Polynomial")
print(f_scipy)
print(f"Interpolated value at x = {point} using scipy method is: {interpolated_value_scipy}\n")

# Plotting the results
x_new = np.linspace(0, 100, 100)
fig = plt.figure(figsize=(6, 5))

# Plot the polynomial curve
plt.plot(x_new, f_scipy(x_new), 'b', label='Lagrange Poly (scipy)')

# Plot the original data points
plt.plot(x, y, 'ro', label='Data Points')

# Plot the interpolated point
plt.plot(point, interpolated_value_scipy, 'go', markersize=10, label=f'Interpolated Point ({point})')

# Plot settings
plt.title('Lagrange Polynomial')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
