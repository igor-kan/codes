import numpy as np
from percus_yevick_hard_spheres import percus_yevick_compressibility_factor


def test_percus_yevick():
    Z0 = percus_yevick_compressibility_factor(0.0)
    assert Z0 == 1.0
    Z_dense = percus_yevick_compressibility_factor(0.2)
    assert Z_dense > 1.0
