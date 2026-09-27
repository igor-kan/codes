def compute_power_series_term_110(x):
    """Computes the 110th term of a power series."""
    return (x ** 110) / 110

def test_compute_110():
    assert compute_power_series_term_110(1) == 1.0 / 110
