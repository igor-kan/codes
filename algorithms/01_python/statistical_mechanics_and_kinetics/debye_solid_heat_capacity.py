"""Debye Model for Low-Temperature T^3 Phonon Heat Capacity."""
import numpy as np
from scipy.integrate import quad


def debye_heat_capacity(T: float, T_D: float, N_atoms: int = 1, k_B: float = 1.380649e-23) -> float:
    """C_V = 9 * N * k_B * (T / T_D)^3 * int_0^(T_D/T) x^4 exp(x) / (exp(x) - 1)^2 dx."""
    if T <= 0:
        return 0.0
    x_max = T_D / T
    def integrand(x):
        return (x**4 * np.exp(x)) / (np.expm1(x)**2)
    val, _ = quad(integrand, 0, x_max)
    return float(9.0 * N_atoms * k_B * (T / T_D)**3 * val)
