"""
Transfer Matrix Method for Quantum Barrier Tunneling.
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 2).
"""
import numpy as np

def barrier_transmission(E: float, V0: float, a: float, m: float = 1.0, hbar: float = 1.0) -> float:
    """Analytical & transfer matrix transmission coefficient through rectangular barrier of width a and height V0."""
    if E <= 0:
        return 0.0
    k1 = np.sqrt(2.0 * m * E) / hbar
    if E < V0:
        kappa = np.sqrt(2.0 * m * (V0 - E)) / hbar
        denom = 1.0 + (V0**2 / (4.0 * E * (V0 - E))) * (np.sinh(kappa * a)**2)
        return float(1.0 / denom)
    elif E > V0:
        k2 = np.sqrt(2.0 * m * (E - V0)) / hbar
        denom = 1.0 + (V0**2 / (4.0 * E * (E - V0))) * (np.sin(k2 * a)**2)
        return float(1.0 / denom)
    else:
        # E == V0
        denom = 1.0 + m * V0 * a**2 / (2.0 * hbar**2)
        return float(1.0 / denom)
