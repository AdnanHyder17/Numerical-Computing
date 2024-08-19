x = [0, 20,40,60, 80, 100]
y = [26.0, -48.6, 61.6,-71.2, 74.8, -75.2]

# For calculating Lagrange polynomial
def Lagrange_Func(x, y):
    n = len(x)
    p = np.poly1d(0.0)
    for i in range(n):
        L = np.poly1d(y[i])
        for j in range(n):
            if j != i:
                L *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])
        p += L
    return p

# Calculating
p = Lagrange_Func(x, y)
print(p)

point = float(input("Enter x-coordinate to interpolate: "))
Value_of_interpolation = p(point)

# Printing
print("****LAGRANGE POLYNOMIAL****")
print(p)
print("Interpolated value at x =", point, "is:", Value_of_interpolation)
