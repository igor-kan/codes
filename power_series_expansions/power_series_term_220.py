def compute_power_series_term_220(x):
    """Computes the 220th term of a power series."""
    return (x ** 220) / 220

def test_compute_220():
    assert compute_power_series_term_220(1) == 1.0 / 220
