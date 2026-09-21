import numpy as np
from photon_polarization_sum import photon_polarization_sum_feynman_gauge, check_ward_identity


def test_ward_identity():
    # Conserved electromagnetic current
    k = np.array([10.0, 0.0, 0.0, 10.0])  # light-like along z
    # Current perpendicular to k
    J = np.array([5.0, 2.0, -1.0, 5.0])
    assert check_ward_identity(J, k)
