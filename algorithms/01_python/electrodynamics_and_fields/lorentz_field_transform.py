"""
Lorentz Transformation of Electric and Magnetic Fields.
References: Landau & Lifshitz - The Classical Theory of Fields (Vol. 2, Ch. 3).
"""
import numpy as np

def transform_fields_boost_x(E: np.ndarray, B: np.ndarray, beta: float, c: float = 1.0):
    """Transform E and B fields under a boost along the x-axis with velocity v = beta * c."""
    gamma = 1.0 / np.sqrt(1.0 - beta**2)
    Ex, Ey, Ez = E
    Bx, By, Bz = B

    Ex_prime = Ex
    Ey_prime = gamma * (Ey - beta * c * Bz)
    Ez_prime = gamma * (Ez + beta * c * By)

    Bx_prime = Bx
    By_prime = gamma * (By + (beta / c) * Ez)
    Bz_prime = gamma * (Bz - (beta / c) * Ey)

    return np.array([Ex_prime, Ey_prime, Ez_prime]), np.array([Bx_prime, By_prime, Bz_prime])
