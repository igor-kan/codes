import numpy as np
from birkhoff_normal_form import nonlinear_tune, resonance_island_width


def test_birkhoff():
    w0 = 1.0
    alpha = 0.2
    assert nonlinear_tune(0.5, w0, alpha) == 1.1

    width = resonance_island_width(0.05, alpha)
    assert width > 0
