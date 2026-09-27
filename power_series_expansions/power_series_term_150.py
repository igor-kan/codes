def compute_power_series_term_150(x):
    """Computes the 150th term of a power series."""
    return (x ** 150) / 150

def test_compute_150():
    assert compute_power_series_term_150(1) == 1.0 / 150
