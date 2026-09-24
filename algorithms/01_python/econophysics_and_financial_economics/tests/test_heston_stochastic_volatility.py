import numpy as np
from heston_stochastic_volatility import simulate_heston_paths


def test_heston_positivity():
    S, V = simulate_heston_paths(100.0, 0.04, 0.05, 1.5, 0.04, 0.3, -0.7, 1.0, 100, 500)
    assert np.all(S > 0.0)
    assert np.all(V >= 0.0)
    assert np.isclose(np.mean(S[:, -1]), 100.0 * np.exp(0.05), rtol=0.08)
