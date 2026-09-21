"""
Diffusion of Radioactive Particles with Constant Decay Rate.
Reference: Zeldovich, Higher Mathematics for Beginners.
"""
import numpy as np

def steady_state_decay_diffusion(x: np.ndarray, D: float, lambda_decay: float, C0: float) -> np.ndarray:
    """
    Solves D d^2 C / dx^2 - lambda C = 0 with C(0) = C0, C(x -> infty) = 0:
    C(x) = C0 exp(- x / L_diff), where L_diff = sqrt(D / lambda).
    """
    l_diff = np.sqrt(D / lambda_decay)
    return C0 * np.exp(-x / l_diff)
