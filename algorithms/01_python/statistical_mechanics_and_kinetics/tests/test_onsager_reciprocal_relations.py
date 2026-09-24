import numpy as np
from onsager_reciprocal_relations import verify_onsager_symmetry, seebeck_coefficient


def test_onsager():
    L = np.array([[2.0, 0.5], [0.5, 3.0]])
    assert verify_onsager_symmetry(L)
    S = seebeck_coefficient(2.0, 0.5, T=300.0)
    assert S < 0.0
