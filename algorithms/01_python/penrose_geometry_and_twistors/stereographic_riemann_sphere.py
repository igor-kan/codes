"""
Stereographic projection between the unit Riemann sphere S^2 and the extended complex plane C.
Reference: Penrose, The Road to Reality, Ch. 8 (The Riemann sphere and complex numbers).
"""
import numpy as np
from typing import Tuple, Union

def sphere_to_complex(x: float, y: float, z: float) -> complex:
    """
    Project point (x, y, z) on S^2 (x^2 + y^2 + z^2 = 1) from the North Pole (0, 0, 1)
    to the complex plane zeta = xi + i eta:
    zeta = (x + i y) / (1 - z)
    """
    if np.isclose(z, 1.0):
        return complex(np.inf, 0.0)
    return complex(x / (1.0 - z), y / (1.0 - z))

def complex_to_sphere(zeta: complex) -> Tuple[float, float, float]:
    """
    Inverse stereographic projection from complex plane to S^2.
    x = 2 Re(zeta) / (1 + |zeta|^2)
    y = 2 Im(zeta) / (1 + |zeta|^2)
    z = (|zeta|^2 - 1) / (1 + |zeta|^2)
    """
    if np.isinf(zeta.real) or np.isinf(zeta.imag):
        return (0.0, 0.0, 1.0)
    mod2 = (zeta.real**2 + zeta.imag**2)
    denom = 1.0 + mod2
    x = 2.0 * zeta.real / denom
    y = 2.0 * zeta.imag / denom
    z = (mod2 - 1.0) / denom
    return (float(x), float(y), float(z))
