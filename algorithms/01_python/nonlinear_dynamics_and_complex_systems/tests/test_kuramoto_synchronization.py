import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kuramoto_synchronization import kuramoto_order_parameter

def test_kuramoto_order():
    # Identical phases -> r = 1
    phases = np.zeros(10)
    assert np.isclose(abs(kuramoto_order_parameter(phases)), 1.0)
    # Uniformly spaced phases -> r = 0
    phases_unif = np.linspace(0, 2*np.pi, 8, endpoint=False)
    assert np.isclose(abs(kuramoto_order_parameter(phases_unif)), 0.0)
