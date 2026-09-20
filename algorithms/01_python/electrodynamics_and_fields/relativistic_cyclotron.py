"""
Boris Algorithm for Relativistic Charged Particle Motion in EM Fields.
References: Landau & Lifshitz - The Classical Theory of Fields.
"""
import numpy as np

def boris_step(r, u, E, B, q, m, dt, c=1.0):
    """Boris pusher step for relativistic momentum u = gamma * v."""
    gamma = np.sqrt(1.0 + np.dot(u, u) / (c**2))
    # Half electric impulse
    u_minus = u + (q * E / m) * (0.5 * dt)
    gamma_minus = np.sqrt(1.0 + np.dot(u_minus, u_minus) / (c**2))

    # Magnetic rotation
    t_vec = (q * B / (m * gamma_minus)) * (0.5 * dt)
    s_vec = 2.0 * t_vec / (1.0 + np.dot(t_vec, t_vec))
    u_prime = u_minus + np.cross(u_minus, t_vec)
    u_plus = u_minus + np.cross(u_prime, s_vec)

    # Second half electric impulse
    u_new = u_plus + (q * E / m) * (0.5 * dt)
    gamma_new = np.sqrt(1.0 + np.dot(u_new, u_new) / (c**2))
    v_new = u_new / gamma_new
    r_new = r + v_new * dt

    return r_new, u_new
