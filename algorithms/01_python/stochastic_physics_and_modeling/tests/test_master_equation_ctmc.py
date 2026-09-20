import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from master_equation_ctmc import solve_ctmc_master_equation, stationary_distribution_ctmc

def test_two_state_ctmc():
    # 0 <-> 1 with rates lambda=1, mu=2
    Q = np.array([[-1.0, 1.0], [2.0, -2.0]])
    pi = stationary_distribution_ctmc(Q)
    # pi_0 = 2/3, pi_1 = 1/3
    assert np.allclose(pi, [2/3, 1/3])
