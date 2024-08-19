# Implement Lagrange polynomial interpolation using Python and numpy.

# It works by calculating the Lagrange basis polynomials for each data point and then adding them together to form the final polynomial.

import numpy as np

# Known data points
x = [0, 20, 40, 60, 80, 100]
y = [26.0, -48.6, 61.6, -71.2, 74.8, -75.2]

# Function to calculate the Lagrange polynomial
def lagrange_interpolation(x, y):
    n = len(x)  # Number of data points
    polynomial = np.poly1d(0.0)  # Initialize the final polynomial to 0
    
    # Outer loop to build each Lagrange basis polynomial
    for i in range(n):
        basis_polynomial = np.poly1d(y[i])  # Start with the y-value as the constant term
        for j in range(n):
            if j != i:
                # Construct the term (x - x[j]) / (x[i] - x[j])
                basis_polynomial *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])
        
        # Add the current basis polynomial to the final polynomial
        polynomial += basis_polynomial
    
    return polynomial

# Calculate the Lagrange polynomial
lagrange_poly = lagrange_interpolation(x, y)
print("Lagrange Polynomial:")
print(lagrange_poly)

# Get user input for interpolation
point = float(input("Enter x-coordinate to interpolate: "))
interpolated_value = lagrange_poly(point)

# Print the interpolated result
print("\nLagrange Polynomial Interpolation")
print(f"Interpolated value at x = {point} is: {interpolated_value:.4f}")










# Plot a Lagrange interpolation polynomial along with the original data points and the interpolated point.

import matplotlib.pyplot as plt
import numpy as np  # Ensure numpy is imported

# Data points
x = [0, 20, 40, 60, 80, 100]
y = [26.0, -48.6, 61.6, -71.2, 74.8, -75.2]

# Interpolated point (xi, yi)
xi = 45
yi = 31.29079589843832

# Compute Lagrange polynomial using all data points
p = lagrange_poly(x[0:6], y[0:6])  # Or simply use x and y without slicing, since the entire list is used
print(p)

# Generate x values for the plot
xp = np.linspace(0, x[5], 100)  # Create 100 evenly spaced x values from 0 to 100

# Evaluate the polynomial at each x value
yp = p(xp)

# Plotting the polynomial
plt.plot(xp, yp, label='Lagrange Poly')  # Plot the Lagrange polynomial curve

# Plot the interpolated point
plt.plot(xi, yi, 'bo', label='Interpolated Point')  # Plot the interpolated point in blue

# Plot the original data points
plt.plot(x[0:6], y[0:6], 'ro', label='Data Points')  # Plot the original data points in red

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Add a legend
plt.legend()

# Display the plot
plt.show()

