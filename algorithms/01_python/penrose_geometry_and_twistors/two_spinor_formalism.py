"""
Two-spinor algebra and conversion to null four-vectors.
Reference: Penrose & Rindler, Spinors and Space-Time; Penrose, The Road to Reality, Ch. 22.
"""
import numpy as np

# Levi-Civita symplectic metric epsilon_AB
EPSILON = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)

def spinor_inner_product(kappa: np.ndarray, eta: np.ndarray) -> complex:
    """
    Calculates the symplectic spinor scalar product:
    kappa_A eta^A = epsilon_{AB} kappa^A eta^B = kappa_0 eta_1 - kappa_1 eta_0.
    """
    return complex(kappa[0] * eta[1] - kappa[1] * eta[0])

def spinor_to_null_vector(kappa: np.ndarray) -> np.ndarray:
    """
    Constructs a future-directed null 4-vector v^mu from a 2-spinor kappa^A:
    v^mu = (1/sqrt(2)) * sigma^mu_{AB'} kappa^A bar{kappa}^{B'}
    using Pauli matrices sigma^0 = I, sigma^1 = sigma_x, sigma^2 = sigma_y, sigma^3 = sigma_z.
    """
    k0 = kappa[0]
    k1 = kappa[1]
    
    # Hermitean matrix X = kappa (kappa)^dagger
    v0 = 0.5 * (abs(k0)**2 + abs(k1)**2)
    v1 = 0.5 * (k0 * np.conj(k1) + k1 * np.conj(k0)).real
    v2 = 0.5 * (1j * (k0 * np.conj(k1) - k1 * np.conj(k0))).real
    v3 = 0.5 * (abs(k0)**2 - abs(k1)**2)
    
    return np.array([v0, v1, v2, v3], dtype=float)
