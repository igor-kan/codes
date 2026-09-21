"""
Second-Order Non-Degenerate Rayleigh-Schrödinger Perturbation Theory.
Reference: Chow, Mathematical Methods for Physicists, Ch. 11.
"""
import numpy as np

def second_order_energy_shift(unperturbed_energies: np.ndarray,
                              perturbation_matrix: np.ndarray,
                              state_idx: int) -> float:
    """
    E_n^(2) = sum_{k != n} |V_{nk}|^2 / (E_n^(0) - E_k^(0)).
    """
    e0 = unperturbed_energies[state_idx]
    shift = 0.0
    for k in range(len(unperturbed_energies)):
        if k != state_idx:
            v_nk = abs(perturbation_matrix[state_idx, k])**2
            denom = e0 - unperturbed_energies[k]
            shift += v_nk / denom
    return float(shift)
