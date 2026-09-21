import numpy as np
from dimensional_regularization import gamma_epsilon_pole, ms_bar_scale_factor


def test_gamma_pole():
    eps = 1e-4
    val = gamma_epsilon_pole(eps)
    assert np.isclose(val, 1e4 - 0.57721566, rtol=1e-4)

    mu_sq = 100.0
    scale = ms_bar_scale_factor(mu_sq, eps)
    assert np.isclose(scale, mu_sq, rtol=1e-3)
