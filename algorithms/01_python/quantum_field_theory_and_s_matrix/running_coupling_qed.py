"""One-Loop QED Running Fine-Structure Constant and Landau Pole.

Renormalization group evolution of alpha(Q^2):
alpha(Q^2) = alpha(0) / [ 1 - (alpha(0) / (3*pi)) * ln(Q^2 / m_e^2) ].
"""
import numpy as np

ALPHA_0 = 1.0 / 137.035999084
M_E = 0.51099895e-3  # GeV


def qed_running_alpha(q_sq: float, alpha_init: float = ALPHA_0, m_fermion: float = M_E) -> float:
    """Calculate running alpha at momentum transfer squared Q^2 (GeV^2)."""
    if q_sq <= m_fermion**2:
        return alpha_init
    
    beta0 = 1.0 / (3.0 * np.pi)
    log_ratio = np.log(q_sq / m_fermion**2)
    denom = 1.0 - alpha_init * beta0 * log_ratio
    if denom <= 0.0:
        raise ValueError("Q^2 has exceeded the QED Landau pole")
    return float(alpha_init / denom)


def qed_landau_pole_energy(m_fermion: float = M_E, alpha_init: float = ALPHA_0) -> float:
    """Estimate QED Landau pole energy scale Lambda_QED (GeV)."""
    # 1 - (alpha / 3pi) ln(Lambda^2 / m^2) = 0 -> Lambda = m * exp(3pi / (2 * alpha))
    exponent = 3.0 * np.pi / (2.0 * alpha_init)
    # Exponent is huge (~645), so we return log10(Lambda)
    return float(np.log10(m_fermion) + exponent / np.log(10.0))
