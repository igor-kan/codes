"""
Partial Wave Scattering and Cross Sections.
References: Landau & Lifshitz - Quantum Mechanics (Vol. 3, Ch. 17).
"""
import numpy as np

def hard_sphere_phase_shift(k: float, a: float, l: int = 0) -> float:
    """Phase shift delta_0 for hard sphere of radius a: delta_0 = -k a."""
    if l == 0:
        return -k * a
    else:
        # For small k a, delta_l approx -(k a)^(2l+1) / ((2l+1)!! (2l-1)!!)
        from math import prod
        denom = prod(range(1, 2 * l + 2, 2)) * prod(range(1, 2 * l, 2))
        return float(-(k * a)**(2 * l + 1) / denom)

def total_cross_section(k: float, phase_shifts: list) -> float:
    """Total scattering cross section sigma = (4 pi / k^2) sum (2l + 1) sin^2(delta_l)."""
    val = 0.0
    for l, delta in enumerate(phase_shifts):
        val += (2 * l + 1) * (np.sin(delta)**2)
    return float(4.0 * np.pi * val / (k**2))
