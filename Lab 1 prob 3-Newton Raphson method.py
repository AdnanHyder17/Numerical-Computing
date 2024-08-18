# Find root of given problems by Newton Raphson method according to the instructions given in table.
# 1)  f1(x)=cos(x)−1.3x 
# 2)  f2(x)=2xcos(2x)−(x+1)^2

import numpy as np
from tabulate import tabulate

def newton_raphson(func, dfunc, initial_guess, tolerance=1e-4, max_iterations=1000):
  
    # Initialize variables
    current_guess = initial_guess
    iteration_data = []
    iteration_count = 0
    error = tolerance + 1  # Initialize error greater than tolerance

    # Perform iterations
    for _ in range(max_iterations):
        iteration_count += 1
        function_value = func(current_guess)
        derivative_value = dfunc(current_guess)

        # Check if derivative is near zero (which could lead to division by zero)
        if abs(derivative_value) < tolerance:
            raise Exception("Derivative is close to zero! Method may fail to converge.")

        # Update the guess using the Newton-Raphson formula
        previous_guess = current_guess
        current_guess = current_guess - function_value / derivative_value

        # Calculate the error (difference between current and previous guess)
        error = abs(current_guess - previous_guess)

        # Store iteration data for table display
        iteration_data.append([iteration_count, current_guess, func(current_guess), error])

        # Check if the error is within the specified tolerance
        if error < tolerance:
            # Display iteration results in a table
            print(tabulate(iteration_data, headers=['Iteration', 'Current Guess (xr)', 'f(xr)', 'Error'], tablefmt="github"))
            print(f"\nRoot of the function is approximately x = {current_guess:.9f}, found in {iteration_count} iterations with tolerance = {tolerance:.4f}.")
            return current_guess

    # Raise an exception if the method fails to converge within the maximum iterations
    raise Exception("Maximum iterations reached. Method did not converge.")

# Define the functions and their derivatives
def function1(x):
    return np.cos(x) - 1.3 * x

def function2(x):
    return 2 * x * np.cos(2 * x) - (x + 1) ** 2

def derivative_function1(x):
    return -np.sin(x) - 1.3

def derivative_function2(x):
    return -2 * (x + 1) + 2 * x * np.cos(2 * x) - 4 * np.sin(2 * x)

# Test cases with different functions and initial guesses
print("\nPart 1: ")
newton_raphson(function1, derivative_function1, -1, tolerance=0.001)

print("\nPart 2: ")
newton_raphson(function2, derivative_function2, -0.77, tolerance=0.00001)
