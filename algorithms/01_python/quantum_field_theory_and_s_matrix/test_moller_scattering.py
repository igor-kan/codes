import numpy as np
from moller_scattering import moller_diff_cross_section_cm


def test_moller_symmetry():
    # Symmetric under theta <-> pi - theta for identical fermions
    s = 1.0  # 1 GeV^2
    th1 = np.pi / 4.0
    th2 = 3.0 * np.pi / 4.0
    ds1 = moller_diff_cross_section_cm(s, th1)
    ds2 = moller_diff_cross_section_cm(s, th2)
    assert np.isclose(ds1, ds2, rtol=1e-5)
