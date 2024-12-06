def h(x):
    """Function for maximization: h(x) = -x^2 + 4x + 1."""
    return -x**2 + 4*x + 1

def h_prime(x):
    """Derivative of h: h'(x) = -2x + 4."""
    return -2*x + 4

def gradient_ascent(x0, alpha=0.1, N=100):
    """
    Gradient Ascent to find maximum of h(x).
    x0: initial guess
    alpha: learning rate
    N: number of iterations
    """
    x = x0
    for _ in range(N):
        x = x + alpha * h_prime(x)
    return x, h(x)

if __name__ == "__main__":
    # Test with x0=0, alpha=0.1, N=100
    x_max, f_max = gradient_ascent(0, 0.1, 100)
    print("Gradient Ascent Method")
    print("======================")
    print(f"Approximate x_max: {x_max}")
    print(f"f(x_max): {f_max}")
    # Expected: The maximum is at x=2 for this function, f(2)= -4 + 8 + 1=5.
    # We should get close to x=2 and f(x)=5.