import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from henon_attractor import simulate_henon_map

def test_henon_boundedness():
    traj = simulate_henon_map(500)
    assert np.all(np.abs(traj[:, 0]) < 2.0)
    assert np.all(np.abs(traj[:, 1]) < 1.0)
