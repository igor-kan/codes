def compute_power_series_term_60(x):
    """Computes the 60th term of a power series."""
    return (x ** 60) / 60

def test_compute_60():
    assert compute_power_series_term_60(1) == 1.0 / 60
