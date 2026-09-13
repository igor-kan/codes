"""
Variational Mechanics: Symbolic Euler-Lagrange Solver.

Derives equations of motion from Lagrangian L(q, dq/dt, t):
d/dt (dL/d(dq/dt)) - dL/dq = 0
"""

import sympy as sp

def solve_simple_pendulum():
    """Derive equation of motion for a simple pendulum of length l and mass m."""
    t = sp.Symbol("t", real=True)
    m, l, g = sp.symbols("m l g", positive=True)
    theta = sp.Function("theta")(t)
    theta_dot = theta.diff(t)
    
    # Kinetic and Potential Energy
    T = sp.Rational(1, 2) * m * (l * theta_dot)**2
    V = -m * g * l * sp.cos(theta)
    L = T - V
    
    # Euler-Lagrange: d/dt(dL/d(theta_dot)) - dL/d(theta) = 0
    p_theta = sp.diff(L, theta_dot)
    dp_dt = p_theta.diff(t)
    dL_dtheta = sp.diff(L, theta)
    
    eq_motion = sp.simplify(dp_dt - dL_dtheta)
    return eq_motion

if __name__ == "__main__":
    print("=== SYMBOLIC EULER-LAGRANGE SOLVER ===")
    eq = solve_simple_pendulum()
    print(f"Pendulum Euler-Lagrange Equation: {eq} = 0")
