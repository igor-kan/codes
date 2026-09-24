"""Allen-Cahn Phase-Field Equation u_t = eps^2 * u_xx - (u^3 - u) via ETD-RK."""
import numpy as np


def allen_cahn_free_energy(u: np.ndarray, dx: float, eps: float) -> float:
    """Ginzburg-Landau free energy F = int [0.5 eps^2 (u_x)^2 + 0.25 (u^2 - 1)^2] dx."""
    u_x = np.gradient(u, dx)
    energy = np.sum(0.5 * (eps**2) * (u_x**2) + 0.25 * ((u**2 - 1.0)**2)) * dx
    return float(energy)
