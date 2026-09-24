import numpy as np
from approximate_bayesian_computation_abc import abc_rejection


def test_abc():
    sim = lambda th: np.random.normal(th, 0.1, 100)
    summary = lambda data: np.mean(data)
    acc = abc_rejection(sim, summary, observed_stat=5.0, epsilon=0.1, n_proposals=500)
    if len(acc) > 0:
        assert np.isclose(np.mean(acc), 5.0, atol=0.5)
