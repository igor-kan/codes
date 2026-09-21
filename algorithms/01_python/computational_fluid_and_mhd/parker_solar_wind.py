"""Parker Isothermal Hydrodynamic Stellar Wind Model.

Calculates the transonic solar wind profile:
Critical sonic radius: r_c = G * M / (2 * a^2)
Transonic equation: (u / a)^2 - ln(u / a)^2 = 4 * ln(r / r_c) + 4 * (r_c / r) - 3.
Reference: Turner, Applied Scientific Computing in Python.
"""
import numpy as np
from scipy.optimize import brentq

G = 6.67430e-11
M_SUN = 1.98847e30


def parker_critical_radius(temperature: float, mean_molecular_weight: float = 0.5, mass: float = M_SUN) -> tuple:
    """Calculate isothermal sound speed a and critical radius r_c."""
    k_B = 1.380649e-23
    m_p = 1.6726219e-27
    a = np.sqrt(k_B * temperature / (mean_molecular_weight * m_p))
    r_c = G * mass / (2.0 * a**2)
    return float(a), float(r_c)


def parker_mach_number(r: float, r_c: float, branch: str = "accelerating") -> float:
    """Solve for Mach number M = u / a at radius r."""
    rhs = 4.0 * np.log(r / r_c) + 4.0 * (r_c / r) - 3.0

    def eqn(m):
        return m**2 - np.log(m**2) - rhs

    if branch == "accelerating":
        if r < r_c:
            return float(brentq(eqn, 1e-4, 1.0))
        elif np.isclose(r, r_c):
            return 1.0
        else:
            return float(brentq(eqn, 1.0, 50.0))
    else:
        raise NotImplementedError("Only accelerating transonic branch supported")
