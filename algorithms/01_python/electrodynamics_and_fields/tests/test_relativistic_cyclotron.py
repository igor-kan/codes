import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from relativistic_cyclotron import boris_step

def test_pure_magnetic_energy_conservation():
    # Pure magnetic field does zero work -> gamma must remain strictly invariant
    r = np.array([1.0, 0.0, 0.0])
    u = np.array([0.0, 0.5, 0.0])
    E = np.zeros(3)
    B = np.array([0.0, 0.0, 1.0])
    u_norm0 = np.linalg.norm(u)
    
    for _ in range(50):
        r, u = boris_step(r, u, E, B, q=1.0, m=1.0, dt=0.05)
        
    u_norm_f = np.linalg.norm(u)
    assert np.isclose(u_norm_f, u_norm0, atol=1e-10)
