import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transfinite_induction_simulator import simulate_transfinite_sequence

def test_transfinite_seq():
    s = lambda a, prev: prev + 1
    lim = lambda hist: max(hist) * 2
    res = simulate_transfinite_sequence(s, lim, 0.0, 10)
    assert len(res) == 10
