"""Pauli Spin Observables and Larmor Spin Precession."""
import numpy as np

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def larmor_spin_precession(psi0: np.ndarray, B0: float, gyromagnetic_ratio: float, t: float) -> np.ndarray:
    """Precess spin-1/2 state under magnetic field along z-axis."""
    omega_L = gyromagnetic_ratio * B0
    U = np.diag([np.exp(0.5j * omega_L * t), np.exp(-0.5j * omega_L * t)])
    return U @ psi0
