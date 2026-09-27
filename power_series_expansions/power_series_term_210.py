def compute_power_series_term_210(x):
    """Computes the 210th term of a power series."""
    return (x ** 210) / 210

def test_compute_210():
    assert compute_power_series_term_210(1) == 1.0 / 210
