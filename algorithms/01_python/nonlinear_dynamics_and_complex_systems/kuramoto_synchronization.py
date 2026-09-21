"""
Kuramoto Model for Coupled Nonlinear Phase Oscillators Synchronization.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13; Kuramoto (1975).
"""
import numpy as np

def kuramoto_order_parameter(phases: np.ndarray) -> complex:
    """r e^{i psi} = (1 / N) sum_{j=1}^N e^{i theta_j}."""
    return complex(np.mean(np.exp(1j * phases)))
