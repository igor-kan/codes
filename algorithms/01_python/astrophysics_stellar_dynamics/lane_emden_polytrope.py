"""
Lane-Emden Equation for Polytropic Stellar Interiors.
Solves 1/xi^2 d/dxi(xi^2 d theta/dxi) + theta^n = 0.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 10).
"""
import numpy as np
from scipy.integrate import solve_ivp

def lane_emden_solve(n: float, xi_max: float = 10.0, n_points: int = 500):
    """
    Solves Lane-Emden equation for polytropic index n.
    y = [theta, d_theta/d_xi]
    Initial conditions at xi=0: theta(0)=1, theta'(0)=0.
    """
    def odes(xi, y):
        theta, phi = y
        # Series expansion near xi=0 to avoid singularity: phi/xi = -theta^n / 3
        if xi < 1e-4:
            d_phi = -(xi / 3.0)
        else:
            theta_pos = max(0.0, theta)
            d_phi = -(theta_pos**n) - 2.0 * phi / xi
        return [phi, d_phi]

    sol = solve_ivp(odes, (1e-6, xi_max), [1.0, 0.0], t_eval=np.linspace(1e-6, xi_max, n_points))
    # Find first zero of theta (stellar surface xi_1)
    xi = sol.t
    theta = sol.y[0]
    sign_changes = np.where(theta <= 0)[0]
    xi_1 = xi[sign_changes[0]] if len(sign_changes) > 0 else xi[-1]
    return xi, theta, float(xi_1)
