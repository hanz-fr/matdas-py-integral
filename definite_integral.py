from scipy.integrate import quad

# definite integral
def integrand(x):
    return x**2

print(quad(integrand, 0, 1))