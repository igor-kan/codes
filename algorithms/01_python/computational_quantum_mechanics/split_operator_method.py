"""
Split-Operator Fourier Method for Time-Dependent Schrödinger Equation.
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 4).
"""
import numpy as np

class SplitOperator1D:
    def __init__(self, x_grid, v_grid, m=1.0, hbar=1.0):
        self.x = x_grid
        self.dx = x_grid[1] - x_grid[0]
        self.n = len(x_grid)
        self.V = v_grid
        self.m = m
        self.hbar = hbar

        # Momentum space grid
        self.k = 2.0 * np.pi * np.fft.fftfreq(self.n, self.dx)
        self.T = (self.hbar * self.k)**2 / (2.0 * self.m)

    def step(self, psi, dt):
        """Single symmetric Strang split-operator step: exp(-iV dt/2) exp(-iT dt) exp(-iV dt/2)."""
        # Half step potential
        psi = np.exp(-1j * self.V * (0.5 * dt / self.hbar)) * psi
        # Full step kinetic in Fourier space
        psi_k = np.fft.fft(psi)
        psi_k = np.exp(-1j * self.T * (dt / self.hbar)) * psi_k
        psi = np.fft.ifft(psi_k)
        # Half step potential
        psi = np.exp(-1j * self.V * (0.5 * dt / self.hbar)) * psi
        return psi
