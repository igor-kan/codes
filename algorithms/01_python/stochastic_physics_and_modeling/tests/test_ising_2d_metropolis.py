import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ising_2d_metropolis import ising_metropolis_sweep, ising_magnetization

def test_ferromagnetic_alignment():
    np.random.seed(42)
    # At very low temperature (beta = 5.0 >> beta_c approx 0.44), spins align
    lattice = np.ones((10, 10))
    lattice = ising_metropolis_sweep(lattice, beta=5.0)
    mag = ising_magnetization(lattice)
    assert mag > 0.9
