from scipy.integrate import quad
from sympy import Symbol, integrate, sqrt

# definite integral
def integrand(x):
    return x**2

print(quad(integrand, 0, 1))

# indefinite integral
x = Symbol('x')
print(integrate(x**2, x))
