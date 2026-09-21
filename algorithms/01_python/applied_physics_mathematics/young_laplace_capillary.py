"""
Young-Laplace Equation for Capillary Rise and Meniscus Pressure.
Reference: Zeldovich, Higher Mathematics for Beginners.
"""
import numpy as np

def jurin_capillary_height(gamma: float, theta_contact: float, r: float, rho: float, g: float = 9.80665) -> float:
    """
    Jurin's law: h = (2 gamma cos(theta)) / (rho g r).
    gamma: surface tension (N/m)
    theta_contact: contact angle (rad)
    r: tube radius (m)
    rho: fluid density (kg/m^3)
    """
    h = (2.0 * gamma * np.cos(theta_contact)) / (rho * g * r)
    return float(h)
