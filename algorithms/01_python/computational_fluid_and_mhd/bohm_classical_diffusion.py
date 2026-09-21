"""Plasma Cross-Field Transport: Classical vs. Bohm Diffusion.

Classical collisional diffusion: D_perp = k_B * T * nu_coll / (m * omega_c^2) ~ B^(-2).
Anomalous Bohm diffusion: D_Bohm = k_B * T / (16 * e * B) ~ B^(-1).
"""
import numpy as np

K_B = 1.380649e-23
E_CHARGE = 1.602176634e-19


def bohm_diffusion_coefficient(T_electron_ev: float, B: float) -> float:
    """Calculate Bohm diffusion coefficient D_Bohm = T_e(eV) / (16 * B) in m^2/s."""
    if B <= 0:
        raise ValueError("Magnetic field B must be positive")
    return float(T_electron_ev / (16.0 * B))


def classical_perpendicular_diffusion(T_electron_ev: float, B: float, collision_freq: float, m_e: float = 9.1093837e-31) -> float:
    """Calculate classical cross-field diffusion D_perp."""
    omega_c = E_CHARGE * B / m_e
    k_T = T_electron_ev * E_CHARGE
    return float(k_T * collision_freq / (m_e * omega_c**2))
