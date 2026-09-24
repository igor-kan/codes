import numpy as np
from merton_jump_diffusion import merton_jump_diffusion_sample


def test_merton_diffusion():
    S = merton_jump_diffusion_sample(100.0, 0.05, 0.15, 0.5, -0.05, 0.1, 1.0, 50, 500)
    assert S.shape == (500, 51)
    assert np.all(S > 0.0)
