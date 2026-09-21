import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coupling_from_the_past import run_monotone_cftp

def test_cftp_sampler():
    # Simple birth-death chain on 3 states
    def update(s, u):
        if u < 0.3:
            return max(0, s - 1)
        elif u < 0.7:
            return min(2, s + 1)
        return s
    res = run_monotone_cftp(update, n_states=3, seed=123)
    assert res in [0, 1, 2]
