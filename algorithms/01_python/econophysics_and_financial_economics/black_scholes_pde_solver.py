"""Black-Scholes-Merton PDE Finite Difference Implicit Solver.

dC/dt + 0.5 * sigma^2 * S^2 * d2C/dS2 + r * S * dC/dS - r * C = 0.
"""
import numpy as np
from scipy.stats import norm


def black_scholes_call_analytic(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """Analytical European call option price."""
    if T <= 0:
        return max(S - K, 0.0)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return float(S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))


def black_scholes_fdm_call(S0: float, K: float, T: float, r: float, sigma: float,
                           M: int = 100, N: int = 500, Smax: float = 300.0) -> float:
    """Solve Black-Scholes PDE via backward implicit Euler finite differences."""
    dS = Smax / M
    dt = T / N
    s_grid = np.linspace(0, Smax, M + 1)
    
    # Payoff at maturity
    V = np.maximum(s_grid - K, 0.0)
    
    # Tridiagonal matrix coefficients for interior nodes i=1..M-1
    i_idx = np.arange(1, M)
    alpha = 0.5 * dt * (r * i_idx - sigma**2 * i_idx**2)
    beta = 1.0 + dt * (sigma**2 * i_idx**2 + r)
    gamma = 0.5 * dt * (-r * i_idx - sigma**2 * i_idx**2)
    
    A = np.diag(beta) + np.diag(gamma[:-1], 1) + np.diag(alpha[1:], -1)
    
    for _ in range(N):
        rhs = V[1:M].copy()
        # Boundary conditions: V(0, t) = 0, V(Smax, t) = Smax - K * exp(-r * tau)
        rhs[0] -= alpha[0] * 0.0
        rhs[-1] -= gamma[-1] * (Smax - K * np.exp(-r * (T - _ * dt)))
        V[1:M] = np.linalg.solve(A, rhs)
        V[0] = 0.0
        V[M] = Smax - K * np.exp(-r * ((_ + 1) * dt))
        
    return float(np.interp(S0, s_grid, V))
