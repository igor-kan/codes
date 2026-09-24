import numpy as np
from korteweg_de_vries_soliton_split_step import kdv_soliton_profile


def test_kdv_profile():
    x = np.linspace(-10, 10, 201)
    u = kdv_soliton_profile(x, c=4.0)
    assert np.isclose(np.max(u), 2.0, atol=1e-5)
