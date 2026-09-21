import numpy as np
from airy_stress_function import cantilever_end_load_stresses


def test_cantilever_boundary_conditions():
    P = 1000.0  # N
    L = 2.0     # m
    c = 0.1     # half-depth
    b = 0.05    # width

    # At top and bottom surfaces y = +-c, shear stress must be 0
    top = cantilever_end_load_stresses(P, L, c, b, 1.0, c)
    bot = cantilever_end_load_stresses(P, L, c, b, 1.0, -c)
    assert np.isclose(top["sigma_xy"], 0.0)
    assert np.isclose(bot["sigma_xy"], 0.0)

    # Maximum shear stress is at neutral axis y = 0
    mid = cantilever_end_load_stresses(P, L, c, b, 1.0, 0.0)
    assert mid["sigma_xy"] < 0
