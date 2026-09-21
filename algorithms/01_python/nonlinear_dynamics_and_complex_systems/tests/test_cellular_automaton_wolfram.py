import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cellular_automaton_wolfram import step_cellular_automaton_1d

def test_rule_30():
    # Rule 30 on single 1: 0, 0, 1, 0, 0 -> 0, 1, 1, 1, 0
    state = np.array([0, 0, 1, 0, 0], dtype=int)
    s1 = step_cellular_automaton_1d(state, 30)
    assert np.allclose(s1, [0, 1, 1, 1, 0])
