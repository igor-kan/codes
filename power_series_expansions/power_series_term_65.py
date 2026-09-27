def compute_power_series_term_65(x):
    """Computes the 65th term of a power series."""
    return (x ** 65) / 65

def test_compute_65():
    assert compute_power_series_term_65(1) == 1.0 / 65
