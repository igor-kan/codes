import numpy as np
from dynamic_time_warping_distance import dtw_distance


def test_dtw():
    s1 = np.array([1.0, 2.0, 3.0, 4.0])
    s2 = np.array([1.0, 2.0, 3.0, 4.0])
    assert dtw_distance(s1, s2) == 0.0
    s3 = np.array([1.0, 1.0, 2.0, 3.0, 4.0])
    # Warped copy has zero or small distance
    assert dtw_distance(s1, s3) == 0.0
