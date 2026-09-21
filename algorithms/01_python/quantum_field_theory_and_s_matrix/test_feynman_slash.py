import numpy as np
from feynman_slash import feynman_slash, minkowski_dot, trace_two_slashes, trace_four_slashes


def test_trace_identities():
    a = np.array([5.0, 1.0, -2.0, 3.0])
    b = np.array([4.0, 0.0, 1.0, -1.0])
    c = np.array([3.0, 2.0, -1.0, 0.0])
    d = np.array([2.0, -1.0, 2.0, 1.0])

    # 2 slashes
    tr2 = trace_two_slashes(a, b)
    expected_tr2 = 4.0 * minkowski_dot(a, b)
    assert np.isclose(tr2, expected_tr2, atol=1e-10)

    # 4 slashes
    tr4 = trace_four_slashes(a, b, c, d)
    adotb = minkowski_dot(a, b)
    cdotd = minkowski_dot(c, d)
    adotc = minkowski_dot(a, c)
    bdotd = minkowski_dot(b, d)
    adotd = minkowski_dot(a, d)
    bdotc = minkowski_dot(b, c)
    expected_tr4 = 4.0 * (adotb * cdotd - adotc * bdotd + adotd * bdotc)
    assert np.isclose(tr4, expected_tr4, atol=1e-10)
