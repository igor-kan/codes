import numpy as np
from mohr_circle_3d import mohr_circles_3d, octahedral_stresses


def test_mohr_circles():
    s1, s2, s3 = 100.0, 50.0, 10.0
    circles = mohr_circles_3d(s1, s2, s3)
    c13, r13 = circles["circle_13"]
    assert np.isclose(c13, 55.0)
    assert np.isclose(r13, 45.0)

    sig_oct, tau_oct = octahedral_stresses(s1, s2, s3)
    assert np.isclose(sig_oct, (100.0 + 50.0 + 10.0) / 3.0)
