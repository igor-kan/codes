def compute_power_series_term_105(x):
    """Computes the 105th term of a power series."""
    return (x ** 105) / 105

def test_compute_105():
    assert compute_power_series_term_105(1) == 1.0 / 105
