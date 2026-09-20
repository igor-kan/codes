"""
Romberg Integration with Richardson Extrapolation.
References: Press et al. - Numerical Recipes (Ch. 4); Kincaid & Cheney.
"""
import numpy as np

def romberg(func, a: float, b: float, max_steps: int = 8, tol: float = 1e-10) -> float:
    """Compute definite integral using Romberg tableau."""
    R = np.zeros((max_steps, max_steps))
    h = b - a
    R[0, 0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, max_steps):
        h /= 2.0
        # Composite trapezoidal refinement with new midpoints
        n_midpoints = 2**(i - 1)
        k = np.arange(1, 2 * n_midpoints, 2)
        sum_f = np.sum(func(a + k * h))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_f

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4.0**j - 1.0)

        if i >= 3 and abs(R[i, i] - R[i - 1, i - 1]) < tol:
            return float(R[i, i])

    return float(R[max_steps - 1, max_steps - 1])
