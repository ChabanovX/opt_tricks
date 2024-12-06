def f(x):
    """Function for root finding: f(x) = x^3 - 6x^2 + 11x - 6."""
    return x**3 - 6*x**2 + 11*x - 6

def bisection(a, b, epsilon=1e-6):
    """
    Bisection Method to find a root of f in [a,b].
    Assumes f(a)*f(b)<0.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a)*f(b)>0. No root guaranteed in [a,b].")

    while True:
        c = (a + b) / 2.0
        fc = f(c)
        
        if abs(fc) < epsilon:
            return c
        
        # Narrow down the interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

if __name__ == "__main__":
    # Test with [a,b] = [1,2] and epsilon = 1e-6
    root = bisection(1, 2, 1e-6)
    print("Bisection Method")
    print("================")
    print(f"Approximate root: {root}")
    print(f"f(root): {f(root)}")
    # Note: The exact root at x=1 should be found very quickly.