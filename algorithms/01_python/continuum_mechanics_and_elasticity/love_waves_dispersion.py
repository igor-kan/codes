"""Love Wave Dispersion in a Layered Elastic Medium.

Love waves are SH (shear horizontal) guided waves in an elastic layer of thickness d
overlying a half-space substrate:
tan(k * d * sqrt((c / c_T1)^2 - 1)) = (mu_2 / mu_1) * sqrt(1 - (c / c_T2)^2) / sqrt((c / c_T1)^2 - 1).
Propagation requires c_T1 < c < c_T2.
"""
import numpy as np
from scipy.optimize import brentq


def love_wave_dispersion_relation(c: float, omega: float, d: float,
                                  c_T1: float, mu_1: float,
                                  c_T2: float, mu_2: float) -> float:
    """Evaluate dispersion relation residual for phase velocity c."""
    if c <= c_T1 or c >= c_T2:
        return np.nan
    k = omega / c
    p = np.sqrt((c / c_T1)**2 - 1.0)
    q = np.sqrt(1.0 - (c / c_T2)**2)
    lhs = np.tan(k * d * p)
    rhs = (mu_2 / mu_1) * (q / p)
    return float(lhs - rhs)
