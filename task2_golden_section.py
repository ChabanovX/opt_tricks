import math

def g(x):
    """Function for optimization: g(x) = (x-2)^2 + 3."""
    return (x - 2)**2 + 3

def golden_section(a, b, epsilon=1e-4):
    """
    Golden Section Method to find the minimum of g(x) in [a,b].
    Assumes g is unimodal.
    """
    phi = (1 + math.sqrt(5)) / 2.0
    while (b - a) > epsilon:
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi
        
        if g(x1) > g(x2):
            a = x1
        else:
            b = x2
    
    x_min = (a + b) / 2.0
    return x_min, g(x_min)

if __name__ == "__main__":
    # Test with [a,b] = [0,5] and epsilon = 1e-4
    x_min, f_min = golden_section(0, 5, 1e-4)
    print("Golden Section Method")
    print("====================")
    print(f"Approximate x_min: {x_min}")
    print(f"f(x_min): {f_min}")
    # Exact minimum is at x=2, f(2)=3, so we should get close to these values.