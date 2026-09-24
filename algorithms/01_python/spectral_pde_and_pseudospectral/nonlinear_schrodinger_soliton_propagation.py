"""Nonlinear Schrodinger (NLS) Equation i * psi_t + 0.5 * psi_xx + |psi|^2 * psi = 0."""
import numpy as np


def nls_bright_soliton(x: np.ndarray, t: float, eta: float = 1.0, v: float = 0.0) -> np.ndarray:
    """Exact fundamental bright soliton solution."""
    phase = 1j * (v * x - 0.5 * (v**2 - eta**2) * t)
    return eta * (1.0 / np.cosh(eta * (x - v * t))) * np.exp(phase)
