"""Fermi-Dirac Distribution and Chemical Potential Sommerfeld Expansion."""
import numpy as np


def fermi_dirac_occupancy(E: np.ndarray, mu: float, T: float, k_B: float = 1.0) -> np.ndarray:
    """f(E) = [1 + exp((E - mu) / (k_B * T))]^(-1)."""
    arg = (E - mu) / (k_B * T)
    arg = np.clip(arg, -100.0, 100.0)
    return 1.0 / (1.0 + np.exp(arg))


def sommerfeld_chemical_potential(E_F: float, T: float, T_F: float) -> float:
    """mu(T) approx E_F * [1 - (pi^2 / 12) * (T / T_F)^2]."""
    return float(E_F * (1.0 - (np.pi**2 / 12.0) * (T / T_F)**2))
