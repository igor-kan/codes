"""2D Complex Potential Flow W(z) and Kutta-Joukowski Lift Theorem.

Implements complex potential W(z) = phi + i psi for cylinder with circulation and lift L' = rho U Gamma.
"""

import numpy as np


class ComplexPotentialFlow:
    """Complex potential flow W(z)."""

    @staticmethod
    def cylinder_flow(z: complex, u_inf: float, cylinder_radius: float, circulation_gamma: float = 0.0) -> complex:
        """W(z) = U_inf (z + R^2 / z) - i Gamma / (2 pi) ln(z)."""
        r = cylinder_radius
        term1 = u_inf * (z + (r**2) / z)
        term2 = - 1.0j * (circulation_gamma / (2.0 * np.pi)) * np.log(z)
        return term1 + term2

    @staticmethod
    def kutta_joukowski_lift(density: float, u_inf: float, circulation_gamma: float) -> float:
        """Lift per unit span: L' = rho * U_inf * Gamma."""
        return density * u_inf * circulation_gamma
