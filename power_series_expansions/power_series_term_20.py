def compute_power_series_term_20(x):
    """Computes the 20th term of a power series."""
    return (x ** 20) / 20

def test_compute_20():
    assert compute_power_series_term_20(1) == 1.0 / 20
