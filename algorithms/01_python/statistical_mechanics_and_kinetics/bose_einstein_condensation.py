"""Bose-Einstein Condensation (BEC) Critical Temperature and Ground State Fraction."""
import numpy as np
from scipy.special import zeta


def bec_critical_temperature(n_density: float, m: float, hbar: float = 1.0545718e-34, k_B: float = 1.380649e-23) -> float:
    """T_c = (2 * pi * hbar^2 / (m * k_B)) * (n / zeta(3/2))^(2/3)."""
    zeta_3_2 = float(zeta(1.5))
    T_c = (2.0 * np.pi * (hbar**2) / (m * k_B)) * ((n_density / zeta_3_2)**(2.0 / 3.0))
    return float(T_c)


def condensate_fraction(T: float, T_c: float) -> float:
    """N_0 / N = 1 - (T / T_c)^(3/2) for T < T_c."""
    if T >= T_c:
        return 0.0
    return float(1.0 - (T / T_c)**1.5)
