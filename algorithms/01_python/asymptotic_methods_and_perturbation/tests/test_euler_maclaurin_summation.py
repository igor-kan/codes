import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from euler_maclaurin_summation import euler_maclaurin_first_order

def test_sum_integers():
    # sum_{k=1}^100 k = 5050
    f = lambda x: x
    df = lambda x: 1.0
    approx = euler_maclaurin_first_order(f, df, 1, 100)
    assert np.isclose(approx, 5050.0, rtol=1e-3)
