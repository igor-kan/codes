"""
Hohmann Orbital Transfer and Delta-V Budget.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics.
"""
import numpy as np

def hohmann_delta_v(r1: float, r2: float, GM: float = 1.0):
    """Compute Delta V_1 and Delta V_2 for circular coplanar transfer."""
    v1 = np.sqrt(GM / r1)
    v2 = np.sqrt(GM / r2)
    a_trans = 0.5 * (r1 + r2)
    v_trans1 = np.sqrt(GM * (2.0 / r1 - 1.0 / a_trans))
    v_trans2 = np.sqrt(GM * (2.0 / r2 - 1.0 / a_trans))

    dv1 = abs(v_trans1 - v1)
    dv2 = abs(v2 - v_trans2)
    return float(dv1), float(dv2), float(dv1 + dv2)
