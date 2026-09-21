"""
Relativistic Kinematics Threshold Production Energy.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 17).
"""
import numpy as np

def fixed_target_threshold_energy(m_projectile: float, m_target: float, final_masses: list) -> float:
    """
    Minimum kinetic energy of projectile hitting stationary target to produce final particles:
    s_th = (sum m_final)^2 = m_proj^2 + m_targ^2 + 2 m_targ E_proj.
    """
    m_tot = sum(final_masses)
    E_proj_th = (m_tot**2 - m_projectile**2 - m_target**2) / (2.0 * m_target)
    T_proj_th = E_proj_th - m_projectile
    return float(max(0.0, T_proj_th))
