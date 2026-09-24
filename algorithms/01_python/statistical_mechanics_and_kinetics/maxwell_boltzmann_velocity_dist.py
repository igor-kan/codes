"""Maxwell-Boltzmann Molecular Speed Distribution and Characteristic Speeds."""
import numpy as np


def mb_speed_pdf(v: np.ndarray, m: float, T: float, k_B: float = 1.380649e-23) -> np.ndarray:
    """Evaluate f(v) = 4 * pi * (m / (2 * pi * k_B * T))^(3/2) * v^2 * exp(-m * v^2 / (2 * k_B * T))."""
    coeff = 4.0 * np.pi * (m / (2.0 * np.pi * k_B * T))**1.5
    return coeff * (v**2) * np.exp(-m * (v**2) / (2.0 * k_B * T))


def characteristic_speeds(m: float, T: float, k_B: float = 1.380649e-23) -> dict:
    """Most probable, mean, and root-mean-square speeds."""
    v_mp = np.sqrt(2.0 * k_B * T / m)
    v_mean = np.sqrt(8.0 * k_B * T / (np.pi * m))
    v_rms = np.sqrt(3.0 * k_B * T / m)
    return {"v_mp": v_mp, "v_mean": v_mean, "v_rms": v_rms}
