"""Action-Angle Variables and Diophantine Frequency Non-Resonance.

KAM non-resonance Diophantine condition:
|k1 * omega1 + k2 * omega2| >= gamma / (|k1| + |k2|)^tau
guaranteeing persistence of invariant KAM tori under small Hamiltonian perturbation.
"""
import numpy as np


def is_diophantine_non_resonant(omega1: float, omega2: float, gamma: float = 0.01,
                                tau: float = 2.0, max_k: int = 20) -> bool:
    """Test Diophantine condition up to harmonic order max_k."""
    for k1 in range(-max_k, max_k + 1):
        for k2 in range(-max_k, max_k + 1):
            if k1 == 0 and k2 == 0:
                continue
            k_norm = abs(k1) + abs(k2)
            denom = abs(k1 * omega1 + k2 * omega2)
            bound = gamma / (k_norm**tau)
            if denom < bound:
                return False
    return True


def golden_mean_frequency_ratio() -> float:
    """The most irrational frequency ratio (golden mean sigma = (sqrt(5) - 1) / 2)."""
    return float(0.5 * (np.sqrt(5.0) - 1.0))
