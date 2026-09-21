import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from spin_connection_cartan import cartan_torsion

def test_torsion_free():
    d_e = np.zeros((4, 4))
    omega = np.zeros((4, 4, 4))
    e = np.array([1.0, 0.0, 0.0, 0.0])
    T = cartan_torsion(d_e, omega, e)
    assert np.allclose(T, 0.0)
