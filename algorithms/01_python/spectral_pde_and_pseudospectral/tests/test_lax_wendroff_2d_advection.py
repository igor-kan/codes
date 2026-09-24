import numpy as np
from lax_wendroff_2d_advection import lax_wendroff_step_2d


def test_lax_wendroff():
    u = np.ones((10, 10))
    u_next = lax_wendroff_step_2d(u, cx=0.1, cy=0.1)
    assert np.allclose(u_next, 1.0)
