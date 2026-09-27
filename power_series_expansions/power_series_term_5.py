def compute_power_series_term_5(x):
    """Computes the 5th term of a power series."""
    return (x ** 5) / 5

def test_compute_5():
    assert compute_power_series_term_5(1) == 1.0 / 5
