def compute_power_series_term_95(x):
    """Computes the 95th term of a power series."""
    return (x ** 95) / 95

def test_compute_95():
    assert compute_power_series_term_95(1) == 1.0 / 95
