"""
Rankine-Hugoniot Oblique Shock Jump Relations.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 9).
"""
import numpy as np

def normal_shock_mach_downstream(M1: float, gamma: float = 1.4) -> float:
    """Downstream Mach number M2 across a normal shock."""
    if M1 < 1.0:
        return M1
    num = (gamma - 1.0) * M1**2 + 2.0
    denom = 2.0 * gamma * M1**2 - (gamma - 1.0)
    return float(np.sqrt(num / denom))

def normal_shock_pressure_ratio(M1: float, gamma: float = 1.4) -> float:
    """Pressure ratio p2 / p1 across a normal shock."""
    return float(1.0 + (2.0 * gamma / (gamma + 1.0)) * (M1**2 - 1.0))
