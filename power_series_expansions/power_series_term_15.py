def compute_power_series_term_15(x):
    """Computes the 15th term of a power series."""
    return (x ** 15) / 15

def test_compute_15():
    assert compute_power_series_term_15(1) == 1.0 / 15
