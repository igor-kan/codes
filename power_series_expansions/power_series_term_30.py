def compute_power_series_term_30(x):
    """Computes the 30th term of a power series."""
    return (x ** 30) / 30

def test_compute_30():
    assert compute_power_series_term_30(1) == 1.0 / 30
