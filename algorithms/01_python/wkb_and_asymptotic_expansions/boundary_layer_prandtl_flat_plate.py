"""Prandtl Laminar Boundary Layer Blasius Similarity Profile."""
import numpy as np


def blasius_boundary_thickness(x: float, Re_x: float) -> float:
    """delta(x) approx 5.0 * x / sqrt(Re_x)."""
    return float(5.0 * x / np.sqrt(Re_x))
