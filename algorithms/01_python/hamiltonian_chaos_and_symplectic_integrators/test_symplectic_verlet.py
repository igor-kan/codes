import numpy as np
from symplectic_verlet import velocity_verlet_integrate


def test_harmonic_oscillator_energy_bounded():
    # Harmonic oscillator H = 0.5 * p^2 + 0.5 * q^2 -> F(q) = -q
    q0 = np.array([1.0])
    p0 = np.array([0.0])
    E0 = 0.5 * (q0[0]**2 + p0[0]**2)

    times, q_t, p_t = velocity_verlet_integrate(q0, p0, (0.0, 100.0), 2000, lambda q: -q)
    energies = 0.5 * (q_t[:, 0]**2 + p_t[:, 0]**2)

    # Symplectic integrator guarantees bounded energy oscillations without long-term drift
    max_energy_error = np.max(np.abs(energies - E0))
    assert max_energy_error < 5e-3
    assert np.abs(energies[-1] - E0) < 5e-3
