# 1)  f1(x)=cos(x)−1.3x 
# 2)  f2(x)=2xcos(2x)−(x+1)^2



import numpy as np
from tabulate import tabulate

def false_position(func, x_lower, x_upper, tolerance=1e-4, max_iterations=1000):

    iteration_data = []  # List to store iteration results for displaying in the table

    # Evaluate the function at the interval endpoints
    func_at_x_lower = func(x_lower)
    func_at_x_upper = func(x_upper)

    # Initialize the points for the algorithm
    previous_x = x_upper
    current_x = x_lower
    iteration_count = 0
    error = tolerance + 1  # Initialize error greater than tolerance

    # Start the iteration process
    for _ in range(max_iterations):
        iteration_count += 1

        # Calculate the new approximation using the False Position formula
        next_x = previous_x - func_at_x_upper * (previous_x - current_x) / (func_at_x_upper - func_at_x_lower)
        error = abs(next_x - previous_x)

        # Store the results of the current iteration for displaying later
        iteration_data.append([iteration_count, next_x, func(next_x), error])

        # Check if the error is within the specified tolerance
        if error < tolerance:
            # Display the results in a table format
            print(tabulate(iteration_data, headers=['Iteration', 'Root Approximation (xr)', 'f(xr)', "Error"], tablefmt="github"))
            print(f"\nRoot of the given function is x = {next_x:.5f} found in {iteration_count} iterations with a tolerance = {tolerance:.4f}.")
            return 

        # Update the interval points for the next iteration
        current_x = previous_x
        func_at_x_lower = func_at_x_upper
        previous_x = next_x
        func_at_x_upper = func(next_x)

    # If the loop completes without finding a root within the specified tolerance
    raise Exception("Maximum iterations reached. The method did not converge.")

# Define the functions for which we want to find roots
def func1(x):
    return np.cos(x) - 1.3 * x

def func2(x):
    return 2 * x * np.cos(2 * x) - (x + 1) ** 2

# Test the False Position method on the first function
print("\nPart 1: ")
false_position(func1, -1, 1, tolerance=0.001)

# Test the False Position method on the second function with two different intervals
print("\nPart 2: ")
false_position(func2, -1, -0.5)
