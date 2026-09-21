import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature_importance_mda import permutation_mda

def test_mda():
    # Objective: predict column 0
    X = np.random.randn(50, 3)
    score_fn = lambda mat: np.corrcoef(mat[:, 0], X[:, 0])[0, 1]
    imp = permutation_mda(score_fn, X)
    # Shuffling column 0 should cause largest drop
    assert imp[0] > imp[1]
