import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stationary_phase_oscillatory import stationary_phase_eval

def test_stationary_phase():
    res = stationary_phase_eval(g_t0=1.0, f_t0=0.0, f_double_prime=2.0, k=100.0)
    assert abs(res) > 0.0
