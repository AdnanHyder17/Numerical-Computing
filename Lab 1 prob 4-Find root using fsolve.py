# Find root of given problems by using fsolve command of sympy.optimize
# 1)  f1(x)=cos(x)−1.3x 
# 2)  f2(x)=2xcos(2x)−(x+1)^2


import numpy as np
from scipy.optimize import fsolve

# Define the first function for which we want to find the root.
def func1(x):
    # The function is f(x) = cos(x) - 1.3 * x.
    # We are interested in finding the value of x where this function equals zero.
    return np.cos(x) - 1.3 * x

# Define the second function for which we want to find the root.
def func2(x):
    # The function is h(x) = 2 * x * cos(2 * x) - (x + 1)^2.
    # We are interested in finding the value(s) of x where this function equals zero.
    return 2 * x * np.cos(2 * x) - (x + 1) ** 2

print("\nPart 1: ")
# Use the fsolve function to find the root of the first function.
# fsolve takes the function and an initial guess as input.
# Here, we start with an initial guess of 0.8.
root = fsolve(func1, 0.8)

# fsolve returns a list of roots (even if there is only one root).
# We print the first root in the list.
print("Root is: ", root[0])

print("\nPart 2: ")
# Use the fsolve function to find the root(s) of the second function.
# In this case, we expect multiple roots, so we provide two initial guesses: -0.8 and -0.6.
# fsolve will try to find roots starting near these values.
root = fsolve(func2, [-0.8, -0.6])

# fsolve may return multiple roots if the function has more than one solution in the provided range.
# Here, we print the first root found by fsolve.
print("First Root is: ", root[0])
