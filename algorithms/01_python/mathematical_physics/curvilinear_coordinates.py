"""
Curvilinear Coordinates: Scale Factors and Vector Differential Operators.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists (Ch. 3).
"""
import numpy as np

class CurvilinearSystem:
    def __init__(self, name="spherical"):
        self.name = name

    def scale_factors(self, u1, u2, u3):
        """Returns h1, h2, h3 scale factors."""
        if self.name == "spherical":
            # u1 = r, u2 = theta, u3 = phi
            r, theta = u1, u2
            return 1.0, r, r * np.sin(theta)
        elif self.name == "cylindrical":
            # u1 = rho, u2 = phi, u3 = z
            rho = u1
            return 1.0, rho, 1.0
        elif self.name == "cartesian":
            return 1.0, 1.0, 1.0
        else:
            raise NotImplementedError(f"Coordinate system {self.name} not implemented")

    def laplacian_scalar(self, f_func, u1, u2, u3, du=1e-4):
        """Compute Laplacian div(grad f) using numerical differentiation with scale factors."""
        h1, h2, h3 = self.scale_factors(u1, u2, u3)
        h_prod = h1 * h2 * h3

        # Midpoint evaluations for u1
        h1_half_p, h2_half_p, h3_half_p = self.scale_factors(u1 + 0.5 * du, u2, u3)
        h1_half_m, h2_half_m, h3_half_m = self.scale_factors(u1 - 0.5 * du, u2, u3)
        df_du1_p = (f_func(u1 + du, u2, u3) - f_func(u1, u2, u3)) / du
        df_du1_m = (f_func(u1, u2, u3) - f_func(u1 - du, u2, u3)) / du
        term1 = ((h2_half_p * h3_half_p / h1_half_p) * df_du1_p - (h2_half_m * h3_half_m / h1_half_m) * df_du1_m) / du

        # Midpoint evaluations for u2
        h1_half_p, h2_half_p, h3_half_p = self.scale_factors(u1, u2 + 0.5 * du, u3)
        h1_half_m, h2_half_m, h3_half_m = self.scale_factors(u1, u2 - 0.5 * du, u3)
        df_du2_p = (f_func(u1, u2 + du, u3) - f_func(u1, u2, u3)) / du
        df_du2_m = (f_func(u1, u2, u3) - f_func(u1, u2 - du, u3)) / du
        term2 = ((h1_half_p * h3_half_p / h2_half_p) * df_du2_p - (h1_half_m * h3_half_m / h2_half_m) * df_du2_m) / du

        # Midpoint evaluations for u3
        h1_half_p, h2_half_p, h3_half_p = self.scale_factors(u1, u2, u3 + 0.5 * du)
        h1_half_m, h2_half_m, h3_half_m = self.scale_factors(u1, u2, u3 - 0.5 * du)
        df_du3_p = (f_func(u1, u2, u3 + du) - f_func(u1, u2, u3)) / du
        df_du3_m = (f_func(u1, u2, u3) - f_func(u1, u2, u3 - du)) / du
        term3 = ((h1_half_p * h2_half_p / h3_half_p) * df_du3_p - (h1_half_m * h2_half_m / h3_half_m) * df_du3_m) / du

        return (term1 + term2 + term3) / h_prod
