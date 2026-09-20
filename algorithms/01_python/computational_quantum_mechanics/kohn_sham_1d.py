"""
1D Kohn-Sham Density Functional Theory with Local Density Approximation.
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 6).
"""
import numpy as np

def lda_exchange_potential_1d(density: np.ndarray) -> np.ndarray:
    """Slater-type LDA exchange potential in 1D proportional to -n(x)^(1/3)."""
    return -(3.0 / np.pi)**(1.0 / 3.0) * np.maximum(density, 1e-12)**(1.0 / 3.0)

def hartree_potential_1d(density: np.ndarray, x: np.ndarray) -> np.ndarray:
    """1D Hartree potential integral V_H(x) = int n(x') / sqrt((x - x')^2 + 1) dx'."""
    v_h = np.zeros_like(x)
    dx = x[1] - x[0]
    for i, xi in enumerate(x):
        soft_coulomb = 1.0 / np.sqrt((xi - x)**2 + 1.0)
        v_h[i] = np.trapezoid(density * soft_coulomb, x)
    return v_h
