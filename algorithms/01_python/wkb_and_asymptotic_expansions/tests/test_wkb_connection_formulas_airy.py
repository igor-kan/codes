import numpy as np
from wkb_connection_formulas_airy import wkb_airy_turning_point_matching


def test_airy():
    x = np.array([0.0])
    ai, bi = wkb_airy_turning_point_matching(x)
    # Ai(0) = 1 / (3^(2/3) * Gamma(2/3)) approx 0.355028
    assert np.isclose(ai[0], 0.355028, atol=1e-4)
