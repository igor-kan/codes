"""Hertzian Elastic Contact Mechanics of Non-Conforming Solids.

Contact between two isotropic elastic spheres (R1, E1, nu1) and (R2, E2, nu2) under normal force F.
Equivalent radius: 1/R = 1/R1 + 1/R2.
Equivalent modulus: 1/E* = (1 - nu1^2)/E1 + (1 - nu2^2)/E2.
Contact radius: a = (3 * F * R / (4 * E*))^(1/3).
Maximum contact pressure: p_0 = 3 * F / (2 * pi * a^2).
Indentation depth: delta = a^2 / R.
"""
import numpy as np
from typing import Dict


def hertzian_sphere_contact(R1: float, E1: float, nu1: float,
                            R2: float, E2: float, nu2: float,
                            F: float) -> Dict[str, float]:
    """Calculate Hertz contact properties."""
    R_eff = 1.0 / (1.0 / R1 + 1.0 / R2)
    inv_E_star = (1.0 - nu1**2) / E1 + (1.0 - nu2**2) / E2
    E_star = 1.0 / inv_E_star

    a = (3.0 * F * R_eff / (4.0 * E_star))**(1.0 / 3.0)
    p0 = 3.0 * F / (2.0 * np.pi * a**2)
    delta = a**2 / R_eff

    return {"contact_radius": float(a), "max_pressure": float(p0), "indentation": float(delta), "E_star": float(E_star)}
