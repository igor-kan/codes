"""
Kramers Escape Rate Over a Barrier.
References: Landau & Lifshitz - Statistical Physics (Vol. 5).
"""
import numpy as np

def kramers_escape_rate(delta_U: float, omega_a: float, omega_b: float, gamma: float, kBT: float) -> float:
    """Kramers escape rate in intermediate-to-high friction regime: r_K = (omega_a omega_b / (2 pi gamma)) exp(-delta_U / kBT)."""
    prefactor = (omega_a * omega_b) / (2.0 * np.pi * gamma)
    return float(prefactor * np.exp(-delta_U / kBT))
