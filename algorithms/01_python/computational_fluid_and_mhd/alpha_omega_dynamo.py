"""Kinematic Mean-Field Alpha-Omega Solar Dynamo Model.

Toroidal field B_phi generated from poloidal field B_r by differential rotation shear Omega(r).
Poloidal field regenerated from toroidal field by helical cyclonic convection alpha.
Dynamo number: D = alpha_0 * dOmega/dr * R^3 / eta^2.
Dynamo wave frequency and butterfly diagram migration.
"""
import numpy as np


def dynamo_number(alpha_0: float, delta_omega: float, R: float, eta: float) -> float:
    """Compute dimensionless Dynamo number D = alpha_0 * delta_omega * R^3 / eta^2."""
    return float(alpha_0 * delta_omega * (R**3) / (eta**2))


def dynamo_wave_dispersion(k: float, alpha_0: float, d_omega: float, eta: float) -> tuple:
    """Calculate growth rate gamma and oscillation frequency omega of dynamo wave."""
    # Dispersion relation: (sigma + eta * k^2)^2 = i * k * alpha_0 * d_omega
    shear_coupling = k * alpha_0 * d_omega
    magnitude = np.sqrt(abs(shear_coupling))
    
    growth_rate = magnitude / np.sqrt(2.0) - eta * (k**2)
    osc_frequency = magnitude / np.sqrt(2.0)
    return float(growth_rate), float(osc_frequency)
