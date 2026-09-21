"""Maxwell Viscoelastic Constitutive Model (Spring and Dashpot in Series).

deps/dt = (1/E) * dsigma/dt + sigma / eta.
Stress relaxation under step strain eps_0: sigma(t) = E * eps_0 * exp(-t / tau_M).
Relaxation time: tau_M = eta / E.
"""
import numpy as np


def maxwell_stress_relaxation(t: float, eps_0: float, E: float, eta: float) -> float:
    """Stress relaxation sigma(t) under sustained step strain eps_0."""
    tau_M = eta / E
    return float(E * eps_0 * np.exp(-t / tau_M))


def maxwell_deborah_number(relaxation_time: float, process_time: float) -> float:
    """Deborah number De = tau_M / t_obs. Large De -> elastic solid; small De -> viscous fluid."""
    return float(relaxation_time / process_time)
