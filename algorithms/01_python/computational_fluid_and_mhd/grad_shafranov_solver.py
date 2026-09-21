"""Grad-Shafranov Equation and Solov'ev Analytical Tokamak Equilibrium.

Delta*(psi) = R * d/dR (1/R dpsi/dR) + d^2(psi)/dZ^2 = -mu_0 R^2 p'(psi) - F F'(psi).
Solov'ev exact analytical solution for poloidal magnetic flux psi(R, Z):
psi(R, Z) = psi_0 / (R_0^4 * kappa^2) * [ R^2 Z^2 + 0.25 * kappa^2 * (R^2 - R_0^2)^2 ].
"""
import numpy as np


def solovev_poloidal_flux(R: np.ndarray, Z: np.ndarray, R0: float, kappa: float, psi0: float = 1.0) -> np.ndarray:
    """Evaluate Solov'ev analytical flux surfaces psi(R, Z) for elongation kappa."""
    prefactor = psi0 / (R0**4 * kappa**2)
    term1 = (R**2) * (Z**2)
    term2 = 0.25 * (kappa**2) * ((R**2 - R0**2)**2)
    return prefactor * (term1 + term2)


def magnetic_field_components(R: float, Z: float, R0: float, kappa: float, B_tor0: float = 2.0) -> tuple:
    """Calculate poloidal fields B_R = -(1/R) dpsi/dZ, B_Z = (1/R) dpsi/dR, and toroidal field B_phi."""
    # dpsi/dZ = prefactor * 2 * R^2 * Z -> B_R = - prefactor * 2 * R * Z
    # dpsi/dR = prefactor * [ 2 * R * Z^2 + kappa^2 * (R^2 - R0^2) * R ] -> B_Z = (1/R) dpsi/dR
    prefactor = 1.0 / (R0**4 * kappa**2)
    dpsi_dZ = prefactor * 2.0 * (R**2) * Z
    dpsi_dR = prefactor * (2.0 * R * (Z**2) + (kappa**2) * (R**2 - R0**2) * R)

    B_R = - dpsi_dZ / R
    B_Z = dpsi_dR / R
    B_phi = B_tor0 * R0 / R
    return float(B_R), float(B_Z), float(B_phi)
