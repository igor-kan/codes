import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from henon_heiles_system import henon_heiles_hamiltonian, henon_heiles_derivs

def test_energy_conservation():
    s = np.array([0.1, 0.1, 0.1, 0.1])
    E0 = henon_heiles_hamiltonian(*s)
    # Single RK4 step
    dt = 0.01
    k1 = henon_heiles_derivs(s)
    k2 = henon_heiles_derivs(s + 0.5 * dt * k1)
    k3 = henon_heiles_derivs(s + 0.5 * dt * k2)
    k4 = henon_heiles_derivs(s + dt * k3)
    s_next = s + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    E1 = henon_heiles_hamiltonian(*s_next)
    assert np.isclose(E0, E1, atol=1e-5)
