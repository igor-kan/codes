import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lattice_boltzmann_d2q9 import equilibrium_distribution, lbm_bgk_collision

def test_lbm_density_conservation():
    rho = np.ones((10, 10))
    u = np.zeros((10, 10))
    v = np.zeros((10, 10))
    feq = equilibrium_distribution(rho, u, v)
    # sum_i f_eq_i = rho
    assert np.allclose(np.sum(feq, axis=0), rho)
