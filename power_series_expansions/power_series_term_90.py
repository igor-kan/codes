def compute_power_series_term_90(x):
    """Computes the 90th term of a power series."""
    return (x ** 90) / 90

def test_compute_90():
    assert compute_power_series_term_90(1) == 1.0 / 90
