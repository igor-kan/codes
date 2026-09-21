"""
Rössler 3D Continuous Chaotic System Numerical Integration.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np

def integrate_rossler(n_steps: int = 2000, dt: float = 0.02,
                      a: float = 0.2, b: float = 0.2, c: float = 5.7) -> np.ndarray:
    """
    dx/dt = -y - z
    dy/dt = x + a y
    dz/dt = b + z(x - c)
    """
    traj = np.zeros((n_steps, 3))
    state = np.array([0.1, 0.0, 0.0])
    
    def deriv(s):
        x, y, z = s
        return np.array([-y - z, x + a * y, b + z * (x - c)])
        
    for i in range(n_steps):
        traj[i] = state
        k1 = deriv(state)
        k2 = deriv(state + 0.5 * dt * k1)
        k3 = deriv(state + 0.5 * dt * k2)
        k4 = deriv(state + dt * k3)
        state += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        
    return traj
