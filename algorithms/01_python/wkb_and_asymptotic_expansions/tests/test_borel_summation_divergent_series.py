from borel_summation_divergent_series import borel_transform_coefficients


def test_borel():
    # a_n = n! (Euler divergent series)
    a = [1, 1, 2, 6, 24]
    b = borel_transform_coefficients(a)
    assert b == [1.0, 1.0, 1.0, 1.0, 1.0]
