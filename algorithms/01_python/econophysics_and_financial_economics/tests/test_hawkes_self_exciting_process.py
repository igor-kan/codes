import numpy as np
from hawkes_self_exciting_process import simulate_univariate_hawkes


def test_hawkes():
    events = simulate_univariate_hawkes(mu=1.0, alpha=0.5, beta=1.0, T_max=10.0)
    assert len(events) > 0
    assert np.all(np.diff(events) > 0.0)
