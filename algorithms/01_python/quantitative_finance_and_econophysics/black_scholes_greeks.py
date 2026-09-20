"""
Black-Scholes-Merton Analytical Option Pricing and Greeks.
References: Jovanovic - Econophysics and Financial Economics.
"""
import numpy as np
from scipy.stats import norm

def black_scholes_call_price(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Black-Scholes European call option price."""
    if T <= 0:
        return max(0.0, S - K)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return float(S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))

def black_scholes_greeks(S: float, K: float, T: float, r: float, sigma: float):
    """Compute Delta, Gamma, Vega, Theta, Rho for European call."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    theta = -(S * norm.pdf(d1) * sigma) / (2.0 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    return delta, gamma, vega, theta, rho
