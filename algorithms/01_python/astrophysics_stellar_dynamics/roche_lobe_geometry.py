"""
Roche Lobe Effective Radius (Eggleton Formula).
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 18).
"""
import numpy as np

def eggleton_roche_lobe_radius(q: float, a: float = 1.0) -> float:
    """
    Eggleton's analytical formula for effective Roche lobe radius r_L / a:
    r_L / a = 0.49 q^(2/3) / (0.6 q^(2/3) + ln(1 + q^(1/3)))
    where q = M1 / M2.
    """
    q_23 = q**(2.0 / 3.0)
    q_13 = q**(1.0 / 3.0)
    denom = 0.6 * q_23 + np.log(1.0 + q_13)
    return float(a * 0.49 * q_23 / denom)
