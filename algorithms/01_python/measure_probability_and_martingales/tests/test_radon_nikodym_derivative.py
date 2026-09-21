import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from radon_nikodym_derivative import discrete_radon_nikodym

def test_rn_density():
    Q = np.array([0.25, 0.25, 0.5])
    P = np.array([0.5, 0.1, 0.4])
    d = discrete_radon_nikodym(P, Q)
    # E_Q[dP/dQ] = sum Q[i] * (P[i]/Q[i]) = sum P[i] = 1.0
    assert np.isclose(np.sum(Q * d), 1.0)
