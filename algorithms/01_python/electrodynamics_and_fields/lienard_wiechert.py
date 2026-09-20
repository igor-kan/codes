"""
Liénard-Wiechert Potentials for Relativistic Moving Charge.
References: Landau & Lifshitz - The Classical Theory of Fields (Vol. 2, Ch. 8).
"""
import numpy as np

def lienard_wiechert_potentials(q: float, r_obs: np.ndarray, r_source: np.ndarray, v_source: np.ndarray, c: float = 1.0):
    """
    Compute Liénard-Wiechert scalar potential Phi and vector potential A at observation point r_obs:
    R = r_obs - r_source
    Phi = q / (4 pi eps_0 * (R - R . v / c))
    A = (v / c^2) * Phi
    """
    R_vec = r_obs - r_source
    R = np.linalg.norm(R_vec)
    v = np.asarray(v_source, dtype=float)
    beta = v / c
    beta_dot_n = np.dot(R_vec / R, beta)

    kappa = 1.0 - beta_dot_n
    phi = q / (4.0 * np.pi * R * kappa)
    A = (v / (c**2)) * phi
    return phi, A
