import numpy as np
from langevin_particle_dynamics import langevin_simulate


def test_langevin():
    x, v = langevin_simulate(0.0, 0.0, gamma=2.0, T=1.0, mass=1.0, dt=0.01, n_steps=1000)
    assert len(x) == 1001
    # Check thermal equipartition <v^2> approx k_B T / m = 1.0
    assert np.isclose(np.mean(v[200:]**2), 1.0, rtol=0.3)
