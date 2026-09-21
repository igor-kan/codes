"""Birkhoff Normal Form for Nonlinear Hamiltonian Systems.

Nonlinear tune shift with action: omega(I) = omega_0 + alpha * I + O(I^2).
Computes nonlinear detuning and resonant island width.
"""
import numpy as np


def nonlinear_tune(action: float, omega0: float, alpha_anharmonic: float) -> float:
    """Birkhoff normal form frequency omega(I) = omega_0 + alpha * I."""
    return float(omega0 + alpha_anharmonic * action)


def resonance_island_width(epsilon_perturbation: float, alpha_anharmonic: float) -> float:
    """Calculate resonance island half-width in action Delta_I = 2 * sqrt(epsilon / |alpha|)."""
    if abs(alpha_anharmonic) < 1e-12:
        raise ValueError("Anharmonicity alpha must be non-zero")
    return float(2.0 * np.sqrt(abs(epsilon_perturbation / alpha_anharmonic)))
