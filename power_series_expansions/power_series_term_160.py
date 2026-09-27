def compute_power_series_term_160(x):
    """Computes the 160th term of a power series."""
    return (x ** 160) / 160

def test_compute_160():
    assert compute_power_series_term_160(1) == 1.0 / 160
