"""Tree-Level QED Bhabha Scattering (e- + e+ -> e- + e+).

Differential cross section in center of mass frame (s-channel annihilation + t-channel scattering).
"""
import numpy as np

ALPHA_EM = 1.0 / 137.035999084


def bhabha_diff_cross_section_cm_ur(s: float, theta: float) -> float:
    """Calculate unpolarized Bhabha differential cross section in ultrarelativistic limit (E >> m).

    dsigma/dOmega = (alpha^2 / (4s)) * [ (1 + cos^4(theta/2)) / sin^4(theta/2)
                                       - 2 * cos^4(theta/2) / sin^2(theta/2)
                                       + (1 + cos^2(theta)) / 2 ]
    """
    if theta <= 0.0 or theta >= np.pi:
        raise ValueError("Theta must be in (0, pi)")
    
    sin_half = np.sin(theta / 2.0)
    cos_half = np.cos(theta / 2.0)
    cos_th = np.cos(theta)

    t1 = (1.0 + cos_half**4) / (sin_half**4)
    t2 = -2.0 * cos_half**4 / (sin_half**2)
    t3 = (1.0 + cos_th**2) / 2.0

    return float((ALPHA_EM**2 / (4.0 * s)) * (t1 + t2 + t3))
