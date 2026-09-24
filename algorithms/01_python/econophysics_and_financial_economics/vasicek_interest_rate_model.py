"""Vasicek Short-Rate Model and Zero-Coupon Bond Analytical Pricing.

dr_t = a * (b - r_t) * dt + sigma * dW_t.
Bond price: P(t, T) = A(t, T) * exp(-B(t, T) * r_t).
"""
import numpy as np


def vasicek_bond_price(r: float, tau: float, a: float, b: float, sigma: float) -> float:
    """Price zero-coupon bond with time to maturity tau = T - t."""
    B = (1.0 - np.exp(-a * tau)) / a
    A = np.exp((b - sigma**2 / (2.0 * a**2)) * (B - tau) - (sigma**2 * B**2) / (4.0 * a))
    return float(A * np.exp(-B * r))
