def compute_power_series_term_240(x):
    """Computes the 240th term of a power series."""
    return (x ** 240) / 240

def test_compute_240():
    assert compute_power_series_term_240(1) == 1.0 / 240
