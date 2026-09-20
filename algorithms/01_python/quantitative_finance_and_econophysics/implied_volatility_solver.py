"""
Implied Volatility Solver using Brent's Method.
References: Jovanovic - Econophysics.
"""
import numpy as np
from scipy.optimize import brentq
from black_scholes_greeks import black_scholes_call_price

def implied_volatility(market_price: float, S: float, K: float, T: float, r: float) -> float:
    """Invert Black-Scholes formula to find implied volatility sigma."""
    intrinsic = max(0.0, S - K * np.exp(-r * T))
    if market_price <= intrinsic:
        return 0.0
    
    def objective(sigma):
        return black_scholes_call_price(S, K, T, r, sigma) - market_price

    return float(brentq(objective, 1e-4, 5.0))
