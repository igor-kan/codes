def compute_power_series_term_80(x):
    """Computes the 80th term of a power series."""
    return (x ** 80) / 80

def test_compute_80():
    assert compute_power_series_term_80(1) == 1.0 / 80
