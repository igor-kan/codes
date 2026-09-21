import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from wright_fisher_drift import simulate_wright_fisher

def test_wright_fisher_bounds():
    traj = simulate_wright_fisher(N_diploid=50, initial_p=0.5, generations=20)
    assert len(traj) == 20
    assert np.all((traj >= 0.0) & (traj <= 1.0))
