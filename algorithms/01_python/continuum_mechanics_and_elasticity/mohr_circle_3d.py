"""3D Mohr's Circle Representation of Stress State.

Given principal stresses sigma_1 >= sigma_2 >= sigma_3:
Draws the three principal circles in (sigma_n, tau) space.
Maximum shear stress: tau_max = (sigma_1 - sigma_3) / 2.
Octahedral normal and shear stresses.
"""
import numpy as np
from typing import Dict, Tuple


def mohr_circles_3d(s1: float, s2: float, s3: float) -> Dict[str, Tuple[float, float]]:
    """Return center and radius (C, R) for the three Mohr circles: (1-2), (2-3), (1-3)."""
    c12, r12 = 0.5 * (s1 + s2), 0.5 * (s1 - s2)
    c23, r23 = 0.5 * (s2 + s3), 0.5 * (s2 - s3)
    c13, r13 = 0.5 * (s1 + s3), 0.5 * (s1 - s3)
    return {"circle_12": (c12, r12), "circle_23": (c23, r23), "circle_13": (c13, r13)}


def octahedral_stresses(s1: float, s2: float, s3: float) -> Tuple[float, float]:
    """Octahedral normal stress sigma_oct and octahedral shear stress tau_oct."""
    sig_oct = (s1 + s2 + s3) / 3.0
    tau_oct = (1.0 / 3.0) * np.sqrt((s1 - s2)**2 + (s2 - s3)**2 + (s3 - s1)**2)
    return float(sig_oct), float(tau_oct)
