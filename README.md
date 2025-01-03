# Numerical Methods: Root Finding, Optimization, and Gradient-Based Methods

This repository contains implementations of three numerical methods:

1. **Bisection Method** for Root-Finding
2. **Golden Section Method** for Unimodal Function Optimization
3. **Gradient Ascent Method** for Maximizing a Function

## Files

- `task1_bisection.py`: Implements the Bisection Method for `f(x) = x^3 - 6x^2 + 11x - 6`.
- `task2_golden_section.py`: Implements the Golden Section Method for finding the minimum of `g(x) = (x-2)^2 + 3`.
- `task3_gradient_ascent.py`: Implements the Gradient Ascent Method for maximizing `h(x) = -x^2 + 4x + 1`.
- `report.pdf`: A short report explaining the logic, observations, and challenges.

## Running the Code

To run each task:

```bash
python task1_bisection.py
python task2_golden_section.py
python task3_gradient_ascent.py
```

## Optimization Tricks and Considerations

### For the Bisection Method:
- **Initial Interval Selection**: Choose `[a,b]` such that `f(a)*f(b)<0`. A smaller interval closer to the root speeds up convergence.
- **Stopping Criterion**: Use a tolerance-based check, e.g. `|f(c)| < ε`. Fine-tune `ε` for faster convergence vs accuracy.

### For the Golden Section Method:
- **Unimodality**: Ensure the function is unimodal in the chosen interval. If not, the method may not yield the global minimum.
- **Interval Reduction**: The golden ratio ensures a constant reduction factor, making the method efficient.
- **Tolerance (`ε`)**: Balancing a smaller `ε` for accuracy vs computational cost is key.

### For Gradient Ascent:
- **Learning Rate (`α`)**: Start with a moderately small `α`. If the function oscillates, reduce `α`; if convergence is very slow, increase it slightly.
- **Number of Iterations**: Set a limit on iterations. If the method hasn't converged, reconsider parameters.
- **Convergence Check**: Instead of just relying on a fixed number of iterations, consider checking if changes in `x` or `f(x)` are below a threshold.

### General Tips:
- **Floating-Point Precision**: Be mindful of very small differences and use double precision if possible.
- **Function Properties**: Understanding the shape (e.g., unimodality, convexity) can guide method selection and parameter tuning.
- **Experimentation**: Adjust tolerances, intervals, and learning rates based on initial trials to find optimal parameters for convergence.

By implementing these methods and following these optimization strategies, you can efficiently find roots, minima, and maxima for a variety of mathematical functions.