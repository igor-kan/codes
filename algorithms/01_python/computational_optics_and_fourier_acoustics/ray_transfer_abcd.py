"""ABCD Ray Transfer Matrix Analysis and Gaussian Beam Propagation.

Complex beam parameter: 1/q(z) = 1/R(z) - i * lambda / (pi * w(z)^2).
ABCD transformation law: q_out = (A * q_in + B) / (C * q_in + D).
"""
import numpy as np
from typing import Tuple


def free_space_matrix(d: float) -> np.ndarray:
    """Free space drift matrix."""
    return np.array([[1.0, d], [0.0, 1.0]])


def thin_lens_matrix(f: float) -> np.ndarray:
    """Thin lens with focal length f."""
    return np.array([[1.0, 0.0], [-1.0 / f, 1.0]])


def gaussian_q_parameter(waist_w0: float, wavelength: float, z: float = 0.0) -> complex:
    """Compute q = z + i * z_R where z_R = pi * w0^2 / lambda."""
    z_R = np.pi * (waist_w0**2) / wavelength
    return complex(z, z_R)


def transform_gaussian_q(q_in: complex, M: np.ndarray) -> complex:
    """Transform q_in through ABCD optical system."""
    A, B = M[0, 0], M[0, 1]
    C, D = M[1, 0], M[1, 1]
    return (A * q_in + B) / (C * q_in + D)


def beam_radius_from_q(q: complex, wavelength: float) -> float:
    """Extract beam radius w from complex parameter q: w = sqrt(-lambda / (pi * Im(1/q)))."""
    inv_q_im = (1.0 / q).imag
    return float(np.sqrt(-wavelength / (np.pi * inv_q_im)))
