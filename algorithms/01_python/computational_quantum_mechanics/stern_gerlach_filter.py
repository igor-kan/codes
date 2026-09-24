"""Stern-Gerlach Sequential Filter and Quantum State Projection."""
import numpy as np


def spin_state_along_direction(theta: float, phi: float) -> np.ndarray:
    """Spin +1/2 state pointing along unit vector (sin theta cos phi, sin theta sin phi, cos theta)."""
    return np.array([np.cos(theta / 2.0), np.exp(1j * phi) * np.sin(theta / 2.0)])


def transition_probability(state_a: np.ndarray, state_b: np.ndarray) -> float:
    """Calculate Born rule projection probability P = |<a|b>|^2."""
    overlap = np.vdot(state_a, state_b)
    return float(np.abs(overlap)**2)
