import numpy as np
from metropolis_adjusted_langevin_mala import mala_proposal


def test_mala():
    grad = lambda x: -x
    x = np.array([1.0])
    xp = mala_proposal(x, grad, tau=0.1)
    assert len(xp) == 1
