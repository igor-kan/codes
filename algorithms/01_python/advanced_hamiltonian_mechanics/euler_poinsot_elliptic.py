"""
Euler-Poinsot Motion of Asymmetric Rigid Body.
References: Landau & Lifshitz - Mechanics (Vol. 1, Ch. 6); Arnold.
"""
import numpy as np

def euler_poinsot_derivatives(w: np.ndarray, I: np.ndarray) -> np.ndarray:
    """Euler's equations for torque-free rigid body: I1 w1_dot = (I2 - I3) w2 w3."""
    I1, I2, I3 = I
    w1, w2, w3 = w
    dw1 = (I2 - I3) * w2 * w3 / I1
    dw2 = (I3 - I1) * w3 * w1 / I2
    dw3 = (I1 - I2) * w1 * w2 / I3
    return np.array([dw1, dw2, dw3])

def euler_poinsot_step_rk4(w: np.ndarray, I: np.ndarray, dt: float) -> np.ndarray:
    """RK4 step for angular velocity."""
    k1 = euler_poinsot_derivatives(w, I)
    k2 = euler_poinsot_derivatives(w + 0.5 * dt * k1, I)
    k3 = euler_poinsot_derivatives(w + 0.5 * dt * k2, I)
    k4 = euler_poinsot_derivatives(w + dt * k3, I)
    return w + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
