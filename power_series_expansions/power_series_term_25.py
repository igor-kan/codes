def compute_power_series_term_25(x):
    """Computes the 25th term of a power series."""
    return (x ** 25) / 25

def test_compute_25():
    assert compute_power_series_term_25(1) == 1.0 / 25
