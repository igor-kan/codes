import numpy as np
from hankel_bessel_transform_cylindrical import bessel_j0_roots


def test_bessel_roots():
    roots = bessel_j0_roots(3)
    assert len(roots) == 3
    assert np.isclose(roots[0], 2.4048, atol=1e-3)
