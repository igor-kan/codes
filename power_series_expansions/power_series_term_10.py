def compute_power_series_term_10(x):
    """Computes the 10th term of a power series."""
    return (x ** 10) / 10

def test_compute_10():
    assert compute_power_series_term_10(1) == 1.0 / 10
