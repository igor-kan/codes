"""Saint-Venant Torsion of Prismatic Cylindrical Shafts.

Calculates torsional rigidity C = G * J and maximum shear stress for:
- Circular shafts: J = pi * R^4 / 2
- Elliptical shafts (semi-axes a, b): J = pi * a^3 * b^3 / (a^2 + b^2)
"""
import numpy as np


def circular_torsion(radius: float, shear_modulus: float, torque: float) -> tuple:
    """Torsional rigidity C, twist rate theta, and max shear stress tau_max."""
    J = 0.5 * np.pi * radius**4
    C = shear_modulus * J
    theta_prime = torque / C
    tau_max = torque * radius / J
    return C, theta_prime, tau_max


def elliptical_torsion(a: float, b: float, shear_modulus: float, torque: float) -> tuple:
    """Torsion of elliptical cross section with semi-axes a (major) and b (minor)."""
    J = np.pi * (a**3) * (b**3) / (a**2 + b**2)
    C = shear_modulus * J
    theta_prime = torque / C
    # Maximum stress occurs on boundary at minor axis endpoint (distance b from center along minor axis)
    tau_max = 2.0 * torque / (np.pi * a * b**2)
    return C, theta_prime, tau_max
