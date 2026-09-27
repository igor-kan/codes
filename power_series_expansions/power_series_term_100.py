def compute_power_series_term_100(x):
    """Computes the 100th term of a power series."""
    return (x ** 100) / 100

def test_compute_100():
    assert compute_power_series_term_100(1) == 1.0 / 100
