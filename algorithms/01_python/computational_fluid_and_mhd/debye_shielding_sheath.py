"""Plasma Debye Shielding and Bohm Sheath Velocity Criterion.

Debye length: lambda_D = sqrt(epsilon_0 * k_B * T_e / (n_e * e^2)).
Plasma frequency: omega_pe = sqrt(n_e * e^2 / (epsilon_0 * m_e)).
Bohm sheath criterion: ions enter the electrostatic sheath with velocity v_i >= c_s = sqrt(k_B * T_e / m_i).
"""
import numpy as np

EPSILON_0 = 8.8541878128e-12
K_B = 1.380649e-23
E_CHARGE = 1.602176634e-19
M_E = 9.1093837e-31


def debye_length(n_e: float, T_electron_ev: float) -> float:
    """Calculate Debye shielding length in meters."""
    if n_e <= 0 or T_electron_ev <= 0:
        raise ValueError("Density and temperature must be positive")
    T_kelvin = T_electron_ev * E_CHARGE / K_B
    return float(np.sqrt(EPSILON_0 * K_B * T_kelvin / (n_e * E_CHARGE**2)))


def electron_plasma_frequency(n_e: float) -> float:
    """omega_pe in rad/s."""
    return float(np.sqrt(n_e * E_CHARGE**2 / (EPSILON_0 * M_E)))


def bohm_sound_speed(T_electron_ev: float, m_ion: float) -> float:
    """Ion acoustic sound speed c_s = sqrt(k_B * T_e / m_i)."""
    return float(np.sqrt(T_electron_ev * E_CHARGE / m_ion))
