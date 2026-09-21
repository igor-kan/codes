import numpy as np
from canonical_perturbation_theory import secular_drift_averaged


def test_drift():
    # Periodic perturbation averaging to 0
    theta = np.linspace(0, 2 * np.pi, 100, endpoint=False)
    drift = secular_drift_averaged(theta, lambda th: np.array([np.sin(th), np.cos(2 * th)]))
    assert np.allclose(drift, np.zeros(2), atol=1e-12)
