def compute_power_series_term_125(x):
    """Computes the 125th term of a power series."""
    return (x ** 125) / 125

def test_compute_125():
    assert compute_power_series_term_125(1) == 1.0 / 125
