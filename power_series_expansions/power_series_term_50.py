def compute_power_series_term_50(x):
    """Computes the 50th term of a power series."""
    return (x ** 50) / 50

def test_compute_50():
    assert compute_power_series_term_50(1) == 1.0 / 50
