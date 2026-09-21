import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from conditional_expectation_subsigma import conditional_expectation_partition

def test_conditional_expectation():
    X = np.array([2.0, 4.0, 10.0, 20.0])
    part = [[0, 1], [2, 3]]
    cond = conditional_expectation_partition(X, part)
    assert np.allclose(cond[:2], 3.0)
    assert np.allclose(cond[2:], 15.0)
