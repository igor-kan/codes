import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mean_reversion_ornstein_uhlenbeck import fit_ou_process

def test_ou_fit():
    # Strongly mean-reverting series around 100
    x = 100.0 + np.sin(np.linspace(0, 10*np.pi, 200))
    theta, mu, hl = fit_ou_process(x)
    assert np.isclose(mu, 100.0, atol=1.0)
