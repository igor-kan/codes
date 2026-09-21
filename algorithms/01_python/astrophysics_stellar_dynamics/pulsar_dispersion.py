"""
Pulsar Dispersion Measure and Interstellar Electron Density.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 16).
"""
import numpy as np

def dispersion_delay(f1_MHz: float, f2_MHz: float, DM_pc_cm3: float) -> float:
    """Time delay Delta t = 4.1488e-3 * DM * (f1^-2 - f2^-2) in seconds."""
    k_DM = 4.148808e3  # MHz^2 pc^-1 cm^3 s
    return float(k_DM * DM_pc_cm3 * (f1_MHz**(-2.0) - f2_MHz**(-2.0)))
