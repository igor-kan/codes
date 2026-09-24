"""Rayleigh-Ritz Variational Method for Quantum Ground State.

E_var = <psi|H|psi> / <psi|psi> >= E_exact.
"""
from scipy.optimize import minimize_scalar


def variational_harmonic_oscillator() -> float:
    """Find ground state of H = -0.5 d^2/dx^2 + 0.5 x^2 using Gaussian trial psi(x) = exp(-b x^2)."""
    def energy_fn(b):
        return 0.5 * b + 1.0 / (8.0 * b)
    res = minimize_scalar(energy_fn, bounds=(0.1, 2.0), method="bounded")
    return float(res.fun)
