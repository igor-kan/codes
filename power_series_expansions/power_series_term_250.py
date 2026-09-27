def compute_power_series_term_250(x):
    """Computes the 250th term of a power series."""
    return (x ** 250) / 250

def test_compute_250():
    assert compute_power_series_term_250(1) == 1.0 / 250
