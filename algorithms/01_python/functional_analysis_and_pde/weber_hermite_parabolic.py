"""
Weber Differential Equation and Parabolic Cylinder Functions D_n(z).
Reference: Hassani, Mathematical Methods for Physics, Ch. 18.
"""
import numpy as np

def parabolic_cylinder_hermite(n: int, z: np.ndarray) -> np.ndarray:
    """
    D_n(z) = 2^(-n/2) exp(-z^2 / 4) H_n(z / sqrt(2)).
    """
    # Physicists Hermite polynomial H_n
    coeffs = [0] * n + [1]
    herm_vals = np.polynomial.hermite.hermval(z / np.sqrt(2.0), coeffs)
    return (2.0**(-0.5 * n)) * np.exp(-0.25 * z**2) * herm_vals
