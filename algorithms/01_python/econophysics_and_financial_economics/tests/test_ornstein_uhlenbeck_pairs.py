import numpy as np
from ornstein_uhlenbeck_pairs import fit_ornstein_uhlenbeck


def test_ou_fit():
    np.random.seed(42)
    dt = 0.01
    theta_true = 2.0
    mu_true = 5.0
    sigma_true = 0.5
    
    n_pts = 10000
    x = np.zeros(n_pts)
    x[0] = mu_true
    for i in range(1, n_pts):
        x[i] = x[i-1] + theta_true * (mu_true - x[i-1]) * dt + sigma_true * np.sqrt(dt) * np.random.randn()
        
    res = fit_ornstein_uhlenbeck(x, dt)
    assert np.isclose(res["mu"], mu_true, atol=0.2)
    assert np.isclose(res["theta"], theta_true, atol=0.4)
