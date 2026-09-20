"""
1D Compressible Euler Equations: Sod Shock Tube Solver.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 9).
"""
import numpy as np

def euler_flux(rho, u, p, gamma=1.4):
    """Euler equations conserved flux vector F(U)."""
    E = p / (gamma - 1.0) + 0.5 * rho * u**2
    F1 = rho * u
    F2 = rho * u**2 + p
    F3 = u * (E + p)
    return np.array([F1, F2, F3])

def lax_friedrichs_step(U, dx, dt, gamma=1.4):
    """Lax-Friedrichs finite volume update for 1D Euler system."""
    # U has shape (3, N): [rho, rho*u, E]
    rho = U[0]
    u = U[1] / np.maximum(rho, 1e-8)
    E = U[2]
    p = (gamma - 1.0) * (E - 0.5 * rho * u**2)
    p = np.maximum(p, 1e-8)

    F = euler_flux(rho, u, p, gamma)
    
    U_new = U.copy()
    # Lax-Friedrichs: U_i^{n+1} = 0.5 (U_{i+1} + U_{i-1}) - 0.5 (dt/dx) (F_{i+1} - F_{i-1})
    U_new[:, 1:-1] = 0.5 * (U[:, 2:] + U[:, :-2]) - 0.5 * (dt / dx) * (F[:, 2:] - F[:, :-2])
    return U_new
