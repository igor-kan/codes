import numpy as np
from hamiltonian_monte_carlo_nuts import hmc_sample_step


def test_hmc():
    U = lambda q: 0.5 * np.sum(q**2)
    grad_U = lambda q: q
    q = np.array([2.0])
    for _ in range(10):
        q = hmc_sample_step(q, U, grad_U)
    assert len(q) == 1
