"""
Rankine-Hugoniot Jump Conditions for Normal Shock Waves.
Reference: Zeldovich & Raizer, Physics of Shock Waves.
"""
import numpy as np
from typing import Dict

def normal_shock_relations(mach1: float, gamma: float = 1.4) -> Dict[str, float]:
    """
    Computes downstream properties after a normal shock:
    - Downstream Mach number M2
    - Pressure ratio p2 / p1
    - Density ratio rho2 / rho1
    - Temperature ratio T2 / T1
    """
    if mach1 < 1.0:
        raise ValueError("Upstream Mach number must be >= 1.0 for a shock.")
        
    m1_sq = mach1**2
    p_ratio = 1.0 + (2.0 * gamma / (gamma + 1.0)) * (m1_sq - 1.0)
    rho_ratio = ((gamma + 1.0) * m1_sq) / (2.0 + (gamma - 1.0) * m1_sq)
    t_ratio = p_ratio / rho_ratio
    m2 = np.sqrt((2.0 + (gamma - 1.0) * m1_sq) / (2.0 * gamma * m1_sq - (gamma - 1.0)))
    
    return {
        "p2_over_p1": float(p_ratio),
        "rho2_over_rho1": float(rho_ratio),
        "T2_over_T1": float(t_ratio),
        "mach2": float(m2)
    }
