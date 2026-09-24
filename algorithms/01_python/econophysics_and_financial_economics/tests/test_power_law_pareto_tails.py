import numpy as np
from power_law_pareto_tails import hill_estimator_tail_index


def test_hill_pareto():
    np.random.seed(42)
    # Generate true Pareto samples with shape a = 3.0
    u = np.random.uniform(0, 1, 10000)
    pareto_samples = (1.0 - u)**(-1.0 / 3.0)
    alpha_est = hill_estimator_tail_index(pareto_samples, k=500)
    assert np.isclose(alpha_est, 3.0, rtol=0.15)
