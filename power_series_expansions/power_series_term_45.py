def compute_power_series_term_45(x):
    """Computes the 45th term of a power series."""
    return (x ** 45) / 45

def test_compute_45():
    assert compute_power_series_term_45(1) == 1.0 / 45
