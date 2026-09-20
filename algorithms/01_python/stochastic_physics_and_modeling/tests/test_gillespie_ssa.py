import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gillespie_ssa import gillespie_step

def test_decay_process():
    # A -> 0 with rate k
    np.random.seed(42)
    k = 2.0
    stoich = np.array([[-1]])
    state = np.array([10])
    new_state, tau = gillespie_step(state, lambda s: np.array([k * s[0]]), stoich)
    assert new_state[0] == 9
    assert tau > 0.0
