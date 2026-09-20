"""
Numerov Algorithm for 1D Time-Independent Schrödinger Equation.
Solves -hbar^2/(2m) psi''(x) + V(x) psi(x) = E psi(x).
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 3).
"""
import numpy as np

def numerov_step(psi_curr, psi_prev, k_sq_next, k_sq_curr, k_sq_prev, dx):
    """Single Numerov integration step to advance psi."""
    factor = dx**2 / 12.0
    term_curr = 2.0 * (1.0 - 5.0 * factor * k_sq_curr) * psi_curr
    term_prev = (1.0 + factor * k_sq_prev) * psi_prev
    psi_next = (term_curr - term_prev) / (1.0 + factor * k_sq_next)
    return psi_next

def numerov_solve_bound_state(v_func, e_guess, x_grid, hbar=1.0, m=1.0):
    """Integrate outwards from left boundary with energy E."""
    dx = x_grid[1] - x_grid[0]
    k_sq = 2.0 * m * (e_guess - v_func(x_grid)) / (hbar**2)
    
    psi = np.zeros_like(x_grid)
    psi[0] = 0.0
    psi[1] = 1e-5  # small perturbation
    for i in range(1, len(x_grid) - 1):
        psi[i + 1] = numerov_step(psi[i], psi[i - 1], k_sq[i + 1], k_sq[i], k_sq[i - 1], dx)
        
    # Normalize
    norm = np.sqrt(np.trapezoid(psi**2, x_grid))
    if norm > 1e-12:
        psi /= norm
    return psi
