"""
Relativistic Bremsstrahlung Radiation Spectrum.
References: Landau & Lifshitz - The Classical Theory of Fields.
"""
import numpy as np

def bremsstrahlung_spectrum_kramer(omega: float, e_initial: float, Z: float = 1.0) -> float:
    """Kramer's classical approximation for thin target bremsstrahlung intensity dI/domega ~ Z (E_max - hbar omega)."""
    if omega >= e_initial:
        return 0.0
    return float(Z * (e_initial - omega))
