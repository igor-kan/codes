"""
WKB Semiclassical Phase and Amplitude Approximation for Wave Equations:
psi(x) approx (p(x))^{-1/2} exp( +- i/hbar int p(x') dx' ).
Reference: Mauch, Intro to Applied Mathematics, Ch. 29; Chow, Ch. 10.
"""
import numpy as np

def wkb_phase_integral(potential_func, energy: float, x_grid: np.ndarray, hbar: float = 1.0, m: float = 1.0) -> np.ndarray:
    """Computes semiclassical action S(x) = int_x0^x sqrt(2m(E - V(x'))) dx'."""
    V = potential_func(x_grid)
    classical_p = np.sqrt(np.maximum(0.0, 2.0 * m * (energy - V)))
    dx = x_grid[1] - x_grid[0]
    return np.cumsum(classical_p) * dx / hbar
