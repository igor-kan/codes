def compute_power_series_term_120(x):
    """Computes the 120th term of a power series."""
    return (x ** 120) / 120

def test_compute_120():
    assert compute_power_series_term_120(1) == 1.0 / 120
