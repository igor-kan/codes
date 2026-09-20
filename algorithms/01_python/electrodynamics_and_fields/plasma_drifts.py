"""
Single Particle Guiding-Center Drifts in Non-Uniform Electromagnetic Fields.
References: Arfken; Landau & Lifshitz.
"""
import numpy as np

def exb_drift_velocity(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Guiding center ExB drift velocity v_E = (E x B) / B^2."""
    B2 = np.dot(B, B)
    return np.cross(E, B) / B2

def grad_b_drift_velocity(v_perp: float, B: np.ndarray, grad_B: np.ndarray, q: float = 1.0, m: float = 1.0) -> np.ndarray:
    """Grad-B drift velocity v_grad = 0.5 (m v_perp^2 / (q B^3)) (B x grad B)."""
    B_mag = np.linalg.norm(B)
    prefactor = 0.5 * m * (v_perp**2) / (q * B_mag**3)
    return prefactor * np.cross(B, grad_B)
