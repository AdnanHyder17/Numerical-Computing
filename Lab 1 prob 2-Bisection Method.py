# find root of given problems by bisection method according to the instructions given in table.
# 1)  f1(x)=cos(x)−1.3x 
# 2)  f2(x)=2xcos(2x)−(x+1)^2


import numpy as np
from tabulate import tabulate

def bisection_method(func, lower_bound, upper_bound, tolerance=0.001, max_iterations=100):
    # Validate that the initial interval has function values with opposite signs
    if func(lower_bound) * func(upper_bound) >= 0:
        return "Error: The function should have opposite signs at the interval endpoints. Please choose a different interval."

    # Initialize variables for iteration
    results_table = []
    iteration = 0
    mid_point = upper_bound
    relative_error = tolerance + 1  # Initialize error larger than tolerance

    while iteration < max_iterations and relative_error > tolerance:
        previous_mid_point = mid_point
        mid_point = (lower_bound + upper_bound) / 2  # Calculate the midpoint
        iteration += 1
        relative_error = abs(mid_point - previous_mid_point)  # Calculate relative error

        # Determine which subinterval to keep based on the function sign
        if func(lower_bound) * func(mid_point) < 0:
            upper_bound = mid_point
        elif func(lower_bound) * func(mid_point) > 0:
            lower_bound = mid_point
        else:
            relative_error = 0  # Exact root found

        # Store the current iteration results
        results_table.append([
            iteration,
            lower_bound, func(lower_bound),
            upper_bound, func(upper_bound),
            mid_point, func(mid_point),
            relative_error
        ])

    # Print the results table
    print(tabulate(results_table, headers=[
        'Iteration', 'Lower Bound (x1)', 'f(x1)',
        'Upper Bound (x2)', 'f(x2)',
        'Midpoint (xr)', 'f(xr)', 'Error'
    ], tablefmt="github"))

    # Print the final root approximation
    print(f"\nRoot of the function is approximately x = {mid_point:.5f}, found in {iteration} iterations with tolerance = {tolerance:.4f}.")

    return mid_point

# Example usage for two functions
print('Part 1')
def function1(x):
    return np.cos(x) - 1.3 * x

bisection_method(function1, 0, 1)

print('\nPart 2')
def function2(x):
    return 2 * x * np.cos(2 * x) - (x + 1) ** 2

bisection_method(function2, -1, 1.5)
