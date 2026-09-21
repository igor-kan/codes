import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rayleigh_schrodinger_perturbation import second_order_energy_shift

def test_energy_shift():
    E0 = np.array([0.0, 10.0])
    V = np.array([[0.0, 1.0], [1.0, 0.0]])
    # E_0^(2) = 1^2 / (0 - 10) = -0.1
    shift = second_order_energy_shift(E0, V, state_idx=0)
    assert np.isclose(shift, -0.1)
