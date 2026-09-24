"""Wigner Quasiprobability Phase Space Distribution."""
import numpy as np


def harmonic_ground_wigner(x: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Exact Wigner function for harmonic oscillator ground state W(x, p) = (1/pi) * exp(-x^2 - p^2)."""
    X, P = np.meshgrid(x, p)
    return (1.0 / np.pi) * np.exp(- (X**2 + P**2))
