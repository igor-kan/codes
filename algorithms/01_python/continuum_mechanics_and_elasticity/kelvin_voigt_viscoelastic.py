"""Kelvin-Voigt Viscoelastic Constitutive Model (Spring and Dashpot in Parallel).

sigma(t) = E * eps(t) + eta * deps(t)/dt.
Creep compliance under constant stress sigma_0: eps(t) = (sigma_0 / E) * (1 - exp(-t / tau_R)).
Retardation time: tau_R = eta / E.
Dynamic storage and loss modulus: E'(omega) = E, E''(omega) = eta * omega.
"""
import numpy as np


def kelvin_voigt_creep(t: float, sigma_0: float, E: float, eta: float) -> float:
    """Creep strain eps(t) under sustained step stress sigma_0."""
    tau_R = eta / E
    return float((sigma_0 / E) * (1.0 - np.exp(-t / tau_R)))


def kelvin_voigt_dynamic_modulus(omega: float, E: float, eta: float) -> complex:
    """Complex dynamic modulus E*(omega) = E + i * eta * omega."""
    return complex(E, eta * omega)
