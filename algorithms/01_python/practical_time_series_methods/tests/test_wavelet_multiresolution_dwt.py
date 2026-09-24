import numpy as np
from wavelet_multiresolution_dwt import haar_dwt


def test_haar():
    x = np.array([4.0, 6.0, 10.0, 12.0])
    a, d = haar_dwt(x)
    assert len(a) == 2
    assert len(d) == 2
    # Energy preservation
    assert np.isclose(np.sum(x**2), np.sum(a**2) + np.sum(d**2))
