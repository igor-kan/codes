import numpy as np
from kuramoto_sivashinsky_chaotic_flame import kuramoto_sivashinsky_linear_dispersion


def test_ks_instability():
    k = np.array([0.5, 1.0, 1.5])
    growth = kuramoto_sivashinsky_linear_dispersion(k)
    assert growth[0] > 0.0  # Unstable
    assert growth[1] == 0.0  # Marginal
    assert growth[2] < 0.0  # Stable damping
