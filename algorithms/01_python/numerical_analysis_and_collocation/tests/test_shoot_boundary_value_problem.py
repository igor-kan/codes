from shoot_boundary_value_problem import shooting_linear_bvp


def test_shooting():
    s = shooting_linear_bvp(0.0, 1.0, 0.0, 1.0)
    # Solution is y(x) = sinh(x) / sinh(1), so y'(0) = 1 / sinh(1) approx 0.850918
    import numpy as np
    assert np.isclose(s, 1.0 / np.sinh(1.0), atol=1e-3)
