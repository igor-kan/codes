"""1D Resistive Magnetic Induction Equation.

dB/dt = eta * d^2(B)/dx^2 + curl(v x B).
Calculates:
- Magnetic Reynolds number: R_m = v_0 * L / eta
- Magnetic diffusion time: tau_D = L^2 / eta.
"""
import numpy as np


def magnetic_reynolds_number(v0: float, L: float, eta: float) -> float:
    """Compute R_m = v0 * L / eta."""
    if eta <= 0:
        raise ValueError("Magnetic diffusivity eta must be positive")
    return float(v0 * L / eta)


def magnetic_diffusion_time(L: float, eta: float) -> float:
    """tau_D = L^2 / eta."""
    return float(L**2 / eta)


def simulate_magnetic_diffusion_1d(B_init: np.ndarray, dx: float, dt: float, eta: float, n_steps: int) -> np.ndarray:
    """Simulate pure 1D magnetic diffusion using explicit FTCS finite differences."""
    r = eta * dt / (dx**2)
    if r > 0.5:
        raise ValueError(f"CFL stability violated: eta * dt / dx^2 = {r} > 0.5")
    
    B = B_init.copy()
    for _ in range(n_steps):
        B[1:-1] = B[1:-1] + r * (B[2:] - 2.0 * B[1:-1] + B[:-2])
    return B
