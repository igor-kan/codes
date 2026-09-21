"""
Pair Production Kinematics and Nuclear Field Recoil.
References: Halliday, Resnick, Krane - Physics (Vol. 2).
"""
import numpy as np

def electron_positron_threshold_energy(m_nucleus: float = 0.0) -> float:
    """Minimum photon energy for e+ e- pair production: 2 m_e c^2 (1 + m_e / M)."""
    m_e = 0.51099895  # MeV
    if m_nucleus == 0:
        return 2.0 * m_e
    return float(2.0 * m_e * (1.0 + m_e / m_nucleus))
