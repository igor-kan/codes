"""
Langevin Dynamics Integrator with Fluctuation-Dissipation Theorem.
References: Landau & Lifshitz - Statistical Physics (Vol. 5, Ch. 12).
"""
import numpy as np

def langevin_overdamped_step(x, force_func, gamma, kBT, dt):
    """Overdamped Langevin step: dx = (F(x)/gamma) dt + sqrt(2 kBT dt / gamma) * N(0, 1)."""
    f = force_func(x)
    drift = (f / gamma) * dt
    diff_std = np.sqrt(2.0 * kBT * dt / gamma)
    noise = diff_std * np.random.normal(size=np.shape(x))
    return x + drift + noise

def langevin_underdamped_step(x, v, force_func, m, gamma, kBT, dt):
    """Underdamped Langevin step (velocity Verlet with friction and noise)."""
    f = force_func(x)
    sigma = np.sqrt(2.0 * gamma * kBT * dt) / m
    noise = sigma * np.random.normal(size=np.shape(x))
    # Half kick
    v_half = v + 0.5 * (f / m - (gamma / m) * v) * dt + 0.5 * noise
    x_new = x + v_half * dt
    f_new = force_func(x_new)
    v_new = v_half + 0.5 * (f_new / m - (gamma / m) * v_half) * dt + 0.5 * noise
    return x_new, v_new
