"""
Hertzian Dipole Radiation and Larmor Formula.
References: Landau & Lifshitz - The Classical Theory of Fields.
"""
import numpy as np

def larmor_radiated_power(q: float, acceleration: float, c: float = 1.0, eps0: float = 1.0) -> float:
    """Larmor total radiated power P = q^2 a^2 / (6 pi eps0 c^3)."""
    return float((q**2 * acceleration**2) / (6.0 * np.pi * eps0 * c**3))

def dipole_far_field_power_pattern(theta: np.ndarray) -> np.ndarray:
    """Dipole angular radiation power pattern dP/dOmega ~ sin^2(theta)."""
    return np.sin(theta)**2
