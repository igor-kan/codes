"""
Tight-Binding Dispersion and Hamiltonian for 1D/2D Crystals.
References: Izaac & Wang - Computational Quantum Mechanics.
"""
import numpy as np

def tight_binding_1d_dispersion(k: np.ndarray, t: float = 1.0, a: float = 1.0, epsilon0: float = 0.0) -> np.ndarray:
    """1D tight-binding band dispersion E(k) = epsilon0 - 2 t cos(k a)."""
    return epsilon0 - 2.0 * t * np.cos(k * a)

def tight_binding_1d_hamiltonian(n_sites: int, t: float = 1.0, periodic: bool = True) -> np.ndarray:
    """Construct tight-binding Hamiltonian matrix."""
    H = np.zeros((n_sites, n_sites))
    for i in range(n_sites - 1):
        H[i, i + 1] = -t
        H[i + 1, i] = -t
    if periodic and n_sites > 2:
        H[0, n_sites - 1] = -t
        H[n_sites - 1, 0] = -t
    return H
