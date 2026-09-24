import numpy as np
from hodrick_prescott_filter import hp_filter


def test_hp():
    t = np.linspace(0, 10, 100)
    y = 2.0 * t + np.sin(5.0 * t)
    trend, cycle = hp_filter(y, lamb=100.0)
    assert len(trend) == 100
    assert len(cycle) == 100
    assert np.allclose(trend + cycle, y)
