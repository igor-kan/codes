"""
Lattice Boltzmann Method (LBM D2Q9) with BGK Collision Operator.
References: Landau & Lifshitz - Fluid Mechanics.
"""
import numpy as np

# D2Q9 discrete velocities: c_i = (cx, cy)
C_DIRS = np.array([
    [0, 0], [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])
WEIGHTS = np.array([4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36])

def equilibrium_distribution(rho: np.ndarray, u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Calculate Maxwell-Boltzmann equilibrium distribution f_eq_i."""
    ny, nx = rho.shape
    f_eq = np.zeros((9, ny, nx))
    u_sq = u**2 + v**2
    for i in range(9):
        cx, cy = C_DIRS[i]
        c_dot_u = cx * u + cy * v
        f_eq[i] = rho * WEIGHTS[i] * (1.0 + 3.0 * c_dot_u + 4.5 * (c_dot_u**2) - 1.5 * u_sq)
    return f_eq

def lbm_bgk_collision(f: np.ndarray, f_eq: np.ndarray, tau: float) -> np.ndarray:
    """BGK relaxation collision step: f_out = f - (f - f_eq) / tau."""
    return f - (f - f_eq) / tau
