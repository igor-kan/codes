"""
Lotka-Volterra Predator-Prey Dynamical System with Runge-Kutta 4 Integrator.
Reference: Campbell Biology (12th Ed.), Ch. 54 (Community Ecology).
"""
import numpy as np

def integrate_lotka_volterra(x0: float, y0: float, alpha: float, beta: float,
                              delta: float, gamma: float, t_max: float = 20.0, dt: float = 0.01) -> np.ndarray:
    """
    dx/dt = alpha x - beta x y
    dy/dt = delta x y - gamma y
    """
    n_steps = int(t_max / dt)
    traj = np.zeros((n_steps, 2))
    state = np.array([x0, y0], dtype=float)
    
    def deriv(s):
        x, y = s[0], s[1]
        dx = alpha * x - beta * x * y
        dy = delta * x * y - gamma * y
        return np.array([dx, dy])
        
    for i in range(n_steps):
        traj[i] = state
        k1 = deriv(state)
        k2 = deriv(state + 0.5 * dt * k1)
        k3 = deriv(state + 0.5 * dt * k2)
        k4 = deriv(state + dt * k3)
        state += (dt / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
        
    return traj
