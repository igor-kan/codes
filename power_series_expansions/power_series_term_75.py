def compute_power_series_term_75(x):
    """Computes the 75th term of a power series."""
    return (x ** 75) / 75

def test_compute_75():
    assert compute_power_series_term_75(1) == 1.0 / 75
