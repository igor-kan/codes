def compute_power_series_term_180(x):
    """Computes the 180th term of a power series."""
    return (x ** 180) / 180

def test_compute_180():
    assert compute_power_series_term_180(1) == 1.0 / 180
