"""Grad-Shafranov Equation for Axisymmetric Tokamak MHD Equilibria.

Models Delta* psi = R d/dR(1/R d psi/dR) + d^2 psi / dZ^2 = - mu_0 R^2 p'(psi) - F F'(psi).
"""

import numpy as np


class GradShafranovOperator:
    """Elliptic Grad-Shafranov differential operator."""

    @staticmethod
    def delta_star_point(psi_grid: np.ndarray, r_val: float, dr: float, dz: float, i: int, j: int) -> float:
        """Finite difference evaluation of Delta* psi at grid point (i, j)."""
        d2psi_dz2 = (psi_grid[i, j + 1] - 2.0 * psi_grid[i, j] + psi_grid[i, j - 1]) / (dz**2)
        dpsi_dr = (psi_grid[i + 1, j] - psi_grid[i - 1, j]) / (2.0 * dr)
        d2psi_dr2 = (psi_grid[i + 1, j] - 2.0 * psi_grid[i, j] + psi_grid[i - 1, j]) / (dr**2)
        # R d/dR(1/R dpsi/dr) = d^2psi/dr^2 - 1/R dpsi/dr
        term_r = d2psi_dr2 - (1.0 / r_val) * dpsi_dr
        return float(term_r + d2psi_dz2)
