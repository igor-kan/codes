def compute_power_series_term_225(x):
    """Computes the 225th term of a power series."""
    return (x ** 225) / 225

def test_compute_225():
    assert compute_power_series_term_225(1) == 1.0 / 225
