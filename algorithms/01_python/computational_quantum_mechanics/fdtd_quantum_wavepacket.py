"""
FDTD Wavepacket Evolution for 1D Schrödinger Equation.
References: Izaac & Wang - Computational Quantum Mechanics.
"""
import numpy as np

class QuantumFDTD1D:
    def __init__(self, x_grid, v_grid, dt, hbar=1.0, m=1.0):
        self.x = x_grid
        self.dx = x_grid[1] - x_grid[0]
        self.V = v_grid
        self.dt = dt
        self.hbar = hbar
        self.m = m

    def step(self, psi_real, psi_imag):
        """Staggered leapfrog update for real and imaginary parts."""
        # Update real part: d(Re)/dt = (H/hbar) Im
        h_im = -0.5 * (self.hbar / self.m) * (np.roll(psi_imag, 1) - 2 * psi_imag + np.roll(psi_imag, -1)) / (self.dx**2) + (self.V / self.hbar) * psi_imag
        psi_real_new = psi_real + self.dt * h_im
        # Update imag part: d(Im)/dt = -(H/hbar) Re
        h_re = -0.5 * (self.hbar / self.m) * (np.roll(psi_real_new, 1) - 2 * psi_real_new + np.roll(psi_real_new, -1)) / (self.dx**2) + (self.V / self.hbar) * psi_real_new
        psi_imag_new = psi_imag - self.dt * h_re
        return psi_real_new, psi_imag_new
