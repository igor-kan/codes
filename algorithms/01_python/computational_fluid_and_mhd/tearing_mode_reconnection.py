"""Sweet-Parker and Resistive Tearing Mode Magnetic Reconnection Rates.

Lundquist number: S = mu_0 * L * v_A / eta.
Sweet-Parker steady reconnection rate: v_rec / v_A = S^(-1/2).
Linear FKR (Furth-Killeen-Rosenbluth) tearing mode maximum growth rate:
gamma * tau_A approx S^(-3/5).
"""
import numpy as np


def lundquist_number(L: float, v_A: float, eta_m: float) -> float:
    """Calculate Lundquist number S = L * v_A / eta_m."""
    if eta_m <= 0:
        raise ValueError("Magnetic diffusivity eta must be positive")
    return float(L * v_A / eta_m)


def sweet_parker_reconnection_rate(S: float) -> float:
    """Inflow Mach number M_in = v_rec / v_A = S^(-1/2)."""
    return float(1.0 / np.sqrt(S))


def fkr_tearing_growth_rate(S: float) -> float:
    """Normalized tearing mode growth rate gamma * tau_A ~ S^(-3/5)."""
    return float(S**(-0.6))
