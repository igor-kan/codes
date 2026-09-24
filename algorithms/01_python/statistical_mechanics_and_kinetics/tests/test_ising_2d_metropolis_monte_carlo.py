import numpy as np
from ising_2d_metropolis_monte_carlo import ising_metropolis_step


def test_ising():
    np.random.seed(42)
    spins = np.ones((8, 8))
    # At very high beta (low T), ferromagnet remains aligned
    spins_next = ising_metropolis_step(spins, beta=10.0)
    assert np.sum(spins_next) >= 60
