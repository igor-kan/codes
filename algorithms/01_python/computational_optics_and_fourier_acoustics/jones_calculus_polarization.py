"""Jones Calculus for Polarized Light and Optical Components.

Jones vectors: horizontal, vertical, right-circular, left-circular.
Jones matrices: linear polarizer at angle theta, quarter-wave plate, half-wave plate.
"""
import numpy as np


def linear_polarizer(theta_rad: float) -> np.ndarray:
    """Jones matrix for linear polarizer with transmission axis at theta."""
    c = np.cos(theta_rad)
    s = np.sin(theta_rad)
    return np.array([[c**2, c * s], [c * s, s**2]], dtype=complex)


def quarter_wave_plate(fast_axis_theta: float = 0.0) -> np.ndarray:
    """Jones matrix for quarter-wave plate with fast axis at fast_axis_theta."""
    # Base QWP with fast axis along x: diag(1, -i)
    qwp0 = np.array([[1.0, 0.0], [0.0, -1j]], dtype=complex)
    c, s = np.cos(fast_axis_theta), np.sin(fast_axis_theta)
    R = np.array([[c, s], [-s, c]], dtype=complex)
    return R.T @ qwp0 @ R


def half_wave_plate(fast_axis_theta: float = 0.0) -> np.ndarray:
    """Jones matrix for half-wave plate with fast axis at fast_axis_theta."""
    hwp0 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    c, s = np.cos(fast_axis_theta), np.sin(fast_axis_theta)
    R = np.array([[c, s], [-s, c]], dtype=complex)
    return R.T @ hwp0 @ R
