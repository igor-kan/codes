import numpy as np
from arnold_cat_map import arnold_cat_step, arnold_cat_lyapunov


def test_cat_map():
    lam = arnold_cat_lyapunov()
    assert np.isclose(lam, 0.96242365)

    x, y = arnold_cat_step(0.3, 0.4)
    assert 0.0 <= x < 1.0
    assert 0.0 <= y < 1.0
