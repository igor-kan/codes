import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from michaelis_menten_kinetics import reaction_velocity, lineweaver_burk_parameters

def test_enzyme_kinetics():
    V_true = 100.0
    K_true = 5.0
    S = np.array([1.0, 2.0, 5.0, 10.0, 20.0])
    v = reaction_velocity(S, V_true, K_true)
    V_est, K_est = lineweaver_burk_parameters(S, v)
    assert np.isclose(V_est, V_true)
    assert np.isclose(K_est, K_true)
