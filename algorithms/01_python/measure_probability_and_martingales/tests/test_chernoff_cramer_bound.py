import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chernoff_cramer_bound import bernoulli_chernoff_bound

def test_chernoff():
    # Fair coin: p=0.5. Probability of >= 80% heads in 100 tosses
    bound = bernoulli_chernoff_bound(0.5, 0.8, 100)
    assert bound < 1e-4
