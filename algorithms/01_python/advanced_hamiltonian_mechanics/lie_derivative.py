"""
Lie Bracket and Lie Derivative of Vector Fields.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics (Appendix 1).
"""
import numpy as np

def lie_bracket_vector_fields(X_func, Y_func, x: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """
    Compute Lie bracket [X, Y] = (X . grad) Y - (Y . grad) X at point x.
    """
    x = np.asarray(x, dtype=float)
    dim = len(x)
    X_val = X_func(x)
    Y_val = Y_func(x)

    # Directional derivative of Y along X: (X . grad) Y
    dY_X = (Y_func(x + h * X_val) - Y_func(x - h * X_val)) / (2.0 * h)
    # Directional derivative of X along Y: (Y . grad) X
    dX_Y = (X_func(x + h * Y_val) - X_func(x - h * Y_val)) / (2.0 * h)

    return dY_X - dX_Y
